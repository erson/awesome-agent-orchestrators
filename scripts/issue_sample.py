"""Bounded GitHub issue sampling for Orchestration Atlas. Only aggregate measurements are published."""
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import median
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "data/issue-samples.json"
TEAM = {"OWNER", "MEMBER", "COLLABORATOR"}
OUTCOMES = {"COMPLETED", "NOT_PLANNED", "DUPLICATE"}
WEEK = timedelta(days=7)
BATCH = 16
DAILY_CAP = 320
REFRESH_DAYS = 2
FIELDS = """
    hasIssuesEnabled
    opened:issues(first:30,orderBy:{field:CREATED_AT,direction:DESC}) {
      totalCount nodes { id createdAt authorAssociation author {login __typename} }
    }
    closed:issues(first:30,states:CLOSED,orderBy:{field:UPDATED_AT,direction:DESC}) {
      totalCount nodes { createdAt closedAt stateReason }
    }
    backlog:issues(states:OPEN) {totalCount}
"""
COMMENTS = """
query($ids:[ID!]!) {rateLimit {cost remaining}
 nodes(ids:$ids) { ... on Issue {id comments(first:5) {pageInfo {hasNextPage}
 nodes {createdAt authorAssociation author {login __typename}}}}}
}
"""


def timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def spread(items, count):
    if len(items) <= count:
        return items
    return [items[round(i * (len(items) - 1) / (count - 1))] for i in range(count)]


def response(issue, connection):
    start = timestamp(issue["createdAt"])
    ambiguous = False
    for comment in connection["nodes"]:
        elapsed = timestamp(comment["createdAt"]) - start
        if elapsed > WEEK:
            break
        author = comment["author"]
        if comment["authorAssociation"] in TEAM:
            if author is None:
                ambiguous = True
            elif author["__typename"] == "User" and author["login"].lower() != issue["author"]["login"].lower():
                if ambiguous:
                    return {"result": "answered", "hours": None}
                return {"result": "answered", "hours": elapsed.total_seconds() / 3600}
    else:
        ambiguous |= connection["pageInfo"]["hasNextPage"]
    return {"result": "unknown" if ambiguous else "unanswered"}


def eligible(repository, now):
    recent = now - timedelta(days=90)
    return spread([i for i in repository["opened"]["nodes"]
                     if recent <= timestamp(i["createdAt"]) <= now - WEEK and i["author"]
                     and i["author"]["__typename"] == "User" and i["authorAssociation"] not in TEAM], 6)


def sample(repository, opened, previous, now, details):
    recent = now - timedelta(days=90)
    closed = spread([i for i in repository["closed"]["nodes"] if i["closedAt"]
                     and recent <= timestamp(i["closedAt"]) <= now], 6)
    cached = previous.get("cache", {})
    results = {i["id"]: cached[i["id"]] for i in opened if i["id"] in cached}
    for issue in opened:
        key = issue["id"]
        if key not in results and key in details:
            results[key] = response(issue, details[key])
    outcomes = dict.fromkeys(sorted(OUTCOMES | {"UNSPECIFIED"}), 0)
    durations = []
    for issue in closed:
        reason = issue["stateReason"]
        outcomes[reason if reason in OUTCOMES else "UNSPECIFIED"] += 1
        if reason == "COMPLETED":
            durations.append((timestamp(issue["closedAt"]) - timestamp(issue["createdAt"])).total_seconds()/86400)
    replies = [r for r in results.values() if r["result"] == "answered"]
    hours = [r["hours"] for r in replies if r.get("hours") is not None]
    unanswered = sum(r["result"] == "unanswered" for r in results.values())
    return {"date": now.date().isoformat(), "enabled": repository["hasIssuesEnabled"],
            "open": repository["backlog"]["totalCount"], "closed": repository["closed"]["totalCount"],
            "sampled": len(opened), "answered": len(replies), "unanswered": unanswered,
            "unknown": len(opened)-len(replies)-unanswered,
            "reply_hours": round(median(hours), 1) if len(hours) >= 3 else None,
            "outcomes": outcomes, "completion_days": round(median(durations), 1) if len(durations) >= 3 else None,
            "cache": {k:v for k,v in results.items() if v["result"] != "unknown"}}


def main():
    now = datetime.now(timezone.utc)
    day = now.date().isoformat()
    data = json.loads(STORE.read_text()) if STORE.exists() else {}
    metrics = json.loads((ROOT/"data/metrics.json").read_text())["repos"]
    names = [p["repo"].lower() for p in json.loads((ROOT/"data/projects.json").read_text())["projects"]]
    cutoff = (now.date() - timedelta(days=REFRESH_DAYS)).isoformat()
    due = [name for name in names if not metrics.get(name, {}).get("error")
           and data.get(name, {}).get("date", "") <= cutoff]
    due.sort(key=lambda name: (data.get(name, {}).get("date", ""), name))
    sampled_today = sum(r.get("date") == day for r in data.values())
    targets = due[:max(0, DAILY_CAP - sampled_today)]
    started = time.monotonic()
    points = processed = 0
    remaining = None
    def query(document, variables):
        nonlocal remaining, points
        seconds = 120 - (time.monotonic()-started)
        if seconds <= 0 or points > 48 or (remaining is not None and remaining < 102):
            raise TimeoutError("time or point budget")
        result = subprocess.run(["gh","api","graphql","--input","-"], text=True, capture_output=True,
                                input=json.dumps({"query":document,"variables":variables}), timeout=seconds)
        payload = json.loads(result.stdout) if result.stdout.strip() else {}
        errors = payload.get("errors", [])
        if errors and any(e.get("type") != "NOT_FOUND" for e in errors):
            raise RuntimeError("GraphQL returned errors")
        if "data" not in payload or not payload["data"] or (result.returncode and not errors):
            raise RuntimeError("GitHub API request failed")
        result = payload["data"]
        points += result["rateLimit"]["cost"]
        remaining = result["rateLimit"]["remaining"]
        return result
    reason = "rotation complete"
    try:
        if targets:
            query("query {rateLimit {cost remaining}}", {})
        for offset in range(0, len(targets), BATCH):
            batch = targets[offset:offset+BATCH]
            fields = []
            for i, name in enumerate(batch):
                owner, repo = name.split("/")
                fields.append(f"r{i}:repository(owner:{json.dumps(owner)},name:{json.dumps(repo)}){{{FIELDS}}}")
            repos = query("{rateLimit{cost remaining} " + " ".join(fields) + "}", {})
            pending = []
            missing_ids = set()
            for i, name in enumerate(batch):
                repository = repos[f"r{i}"]
                if not repository:
                    continue
                opened = eligible(repository, now)
                previous = data.get(name, {})
                missing_ids.update(issue["id"] for issue in opened if issue["id"] not in previous.get("cache", {}))
                pending.append((name, repository, opened, previous))
            details = {}
            if missing_ids:
                nodes = query(COMMENTS, {"ids": sorted(missing_ids)})["nodes"]
                details = {n["id"]: n["comments"] for n in nodes if n and n.get("comments")}
            for name, repository, opened, previous in pending:
                data[name] = sample(repository, opened, previous, now, details)
            tmp = STORE.with_suffix(".tmp")
            tmp.write_text(json.dumps(data, indent=2, sort_keys=True)+"\n")
            tmp.replace(STORE)
            processed += len(pending)
            print(f"{processed} repositories, {points} points, {time.monotonic()-started:.1f}s", flush=True)
    except (TimeoutError, subprocess.TimeoutExpired, RuntimeError) as exc:
        reason = str(exc)
    msg = f"Issue sampling {day}: {processed}/{len(targets)} repositories, {points} reported GraphQL points, {time.monotonic()-started:.1f}s ({reason})."
    print(msg)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as file:
            print(msg, file=file)


if __name__ == "__main__":
    main()
