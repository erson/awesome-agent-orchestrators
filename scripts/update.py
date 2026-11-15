#!/usr/bin/env python3
"""Fetch GitHub metrics for every project in data/projects.json, then render README.md and data/projects.csv.

Needs the GitHub CLI (gh), signed in with read access to public repositories.

    python3 scripts/update.py                 fetch metrics older than 7 days, then render
    python3 scripts/update.py --refresh       fetch every project again, then render
    python3 scripts/update.py --render-only   render from data/metrics.json, no network calls
"""

import argparse
import concurrent.futures as cf
import csv
import html
import json
import re
import statistics
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_FILE = ROOT / "data" / "projects.json"
METRICS_FILE = ROOT / "data" / "metrics.json"
CSV_FILE = ROOT / "data" / "projects.csv"
README_FILE = ROOT / "README.md"

NOW = datetime.now(timezone.utc)
TODAY = NOW.astimezone().date()
MAX_AGE = timedelta(days=7)
WORKERS = 4
STATUSES = ["Active", "Recent", "Slow", "Stale", "Archived", "Unavailable", "Not fetched"]
SHORT = {
    "terminal": "Terminal",
    "desktop": "Desktop & web",
    "swarms": "Swarms",
    "loops": "Loop runners",
    "tasks": "Task runners",
    "infra": "Infrastructure",
    "assistants": "Assistants",
    "resting": "Resting",
    "adjacent": "Adjacent frameworks",
}
CSV_FIELDS = [
    "repo", "name", "category", "origin", "status", "stars", "forks",
    "contributors", "bots", "top_author_share", "commits_90d", "commits_all_time",
    "last_commit_at", "days_since_commit", "created_at", "age_months", "stars_per_month",
    "latest_release_tag", "latest_release_at", "releases_12m", "open_issues", "open_prs",
    "license", "language", "archived", "topics", "url", "description",
]
TITLE = "Stop building new AI agent orchestrators"
INTRO = (
    "Before you write another orchestrator, check whether someone already has. This repo indexes "
    "{total} open-source and source-available tools that run, supervise, or coordinate AI agents: "
    "parallel coding agents, multi-agent swarms, loop and task runners, infrastructure, and personal assistants. "
    "{active} of them had a commit in the last 30 days.\n\n"
    "Most of these projects are doing the same few things: running several agent sessions side by side, "
    "isolating them in worktrees or containers, and routing tasks between them. The gap is rarely another "
    "orchestrator. It is maturity: more contributors, releases, docs, and tests. Pick one that is close to "
    "what you need and contribute to it, or fork it. If you still build your own, use this list to see what "
    "already exists and say what yours does differently.\n\n"
    "Every project has live GitHub metrics: stars, contributors, commit activity, releases, open work, license, "
    "and how recently it was updated. The [Single-maintainer risk](#single-maintainer-risk) table shows "
    "projects that depend on one person. The list starts from "
    "[andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) "
    "(CC0-1.0) and adds projects that list does not cover. Figures are a snapshot; see [Methodology](#methodology)."
)
METHOD = """## Methodology

**Source.** Projects start from [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) (CC0-1.0). Projects marked _(new)_ were found by GitHub search, the source's own references, and web search, and were not in that list. Each new project had to meet the same scope: it orchestrates, supervises, or coordinates several AI agents or agent sessions; it is open source or source-available; and it is active. Adjacent frameworks are general-purpose agent SDKs. They are listed separately because many teams use them for multi-agent orchestration.

**Data.** GitHub REST API through the GitHub CLI, collected on the date shown above (UTC). Repository figures refer to the default branch. Statuses and day counts are judged as of each project's collection date.

| Column | Definition |
|---|---|
| Stars, Forks, Language | Repository metadata. |
| License | The SPDX id GitHub detects. Check the license file before reuse; detection can be wrong. "None" means no license was detected, so default copyright applies. |
| Contributors | GitHub accounts (type `User`) with at least one commit on the default branch. Bots are excluded and counted separately in `data/metrics.json`. |
| Commits (90d) | Commits on the default branch in the 90 days before the snapshot. |
| Last commit | Committer date of the newest default-branch commit. `pushed_at` is not used, because it also changes when other branches are pushed. |
| Status | **Active**: last commit within 30 days. **Recent**: 31 to 90 days. **Slow**: 91 to 365 days. **Stale**: older than a year, or no commits. **Archived**: archived on GitHub. **Unavailable**: the API call failed. |
| Latest release | Newest non-draft GitHub Release, pre-releases included. Projects that only push tags show "—". |
| Open issues / PRs | Open issues (excluding pull requests) and open pull requests. |

**Also in `data/projects.csv`.** Top-author share (the top human contributor's share of human contributions; values near 100% mean one person does almost all of the work), commits across all time (approximate: the sum of contributor counts), releases in the last 12 months, stars per month since creation, and age in months.

**Limitations.** Stars are a popularity signal, not a quality measure, and can be inflated. Contributor counts cover GitHub accounts only, so commits made under unlinked emails are not counted. Stale does not mean unusable; many small tools are finished. All figures are a point-in-time snapshot.
"""
MAINTAIN = """## Keeping it current

```sh
python3 scripts/update.py                # fetch metrics older than 7 days, then re-render
python3 scripts/update.py --refresh      # fetch everything again
python3 scripts/update.py --render-only  # rebuild this README from data/metrics.json
```

The script needs the GitHub CLI (`gh`) signed in. To add a project, append an entry to `data/projects.json` with `repo`, `name`, `category`, `origin`, and `description`, then run the script.
"""
CREDITS = """## Credits

The starting list, its categories, and its one-line descriptions come from [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators), released under CC0-1.0. The descriptions here are shortened rewrites; the originals are kept in `data/projects.json` as `list_description`.
"""


class GhError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message


def gh_api(endpoint, include=False, paginate=False, jq=None):
    """Run `gh api` and return stdout. Waits and retries when GitHub's rate limit is hit."""
    cmd = ["gh", "api"]
    if include:
        cmd.append("--include")
    if paginate:
        cmd.append("--paginate")
    if jq:
        cmd += ["--jq", jq]
    cmd.append(endpoint)
    for attempt in range(4):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0:
            return proc.stdout
        message = proc.stderr.strip()
        found = re.search(r"HTTP (\d{3})", message)
        code = int(found.group(1)) if found else None
        if code in (403, 429) and "rate limit" in message.lower():
            time.sleep(60 * (attempt + 1))
            continue
        raise GhError(code, message)
    raise GhError(None, f"rate limit persisted: {endpoint}")


def split_include(text):
    """Return lower-cased headers and the body of `gh api --include` output."""
    head, _, body = text.partition("\n\n")
    headers = {}
    for line in head.splitlines()[1:]:
        key, sep, value = line.partition(":")
        if sep:
            headers[key.strip().lower()] = value.strip()
    return headers, body


def list_total(headers, body):
    """Number of items behind a list endpoint that was requested with per_page=1."""
    found = re.search(r'[?&]page=(\d+)[^>]*>;\s*rel="last"', headers.get("link", ""))
    if found:
        return int(found.group(1))
    return len(json.loads(body or "[]"))


def parse_ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def fetch_repo(repo):
    """Collect metrics for one repo. Each endpoint is independent, so one failure leaves the rest intact."""
    record = {"repo": repo, "fetched_at": NOW.isoformat(timespec="seconds")}
    try:
        meta = json.loads(gh_api(f"repos/{repo}"))
    except GhError as err:
        record.update(error=err.code or "unknown", error_message=err.message[:300])
        return record
    record.update(
        full_name=meta["full_name"],
        url=meta["html_url"],
        github_description=meta.get("description") or "",
        stars=meta["stargazers_count"],
        forks=meta["forks_count"],
        open_issues_and_prs=meta["open_issues_count"],
        language=meta.get("language") or "",
        license=(meta.get("license") or {}).get("spdx_id") or "",
        archived=meta["archived"],
        fork=meta["fork"],
        created_at=meta["created_at"],
        pushed_at=meta["pushed_at"],
        topics=meta.get("topics", []),
    )
    gaps = []
    try:
        head = json.loads(gh_api(f"repos/{repo}/commits?per_page=1"))
        record["last_commit_at"] = head[0]["commit"]["committer"]["date"] if head else None
    except GhError as err:
        gaps.append(f"last_commit:{err.code}")
    since = (NOW - timedelta(days=90)).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        headers, body = split_include(gh_api(f"repos/{repo}/commits?per_page=1&since={since}", include=True))
        record["commits_90d"] = list_total(headers, body)
    except GhError as err:
        gaps.append(f"commits_90d:{err.code}")
    try:
        rows = gh_api(f"repos/{repo}/contributors?per_page=100", paginate=True, jq=".[] | [.type, .contributions] | @tsv")
        pairs = [line.split("\t") for line in rows.splitlines() if line.strip()]
        humans = [int(n) for kind, n in pairs if kind == "User"]
        record.update(
            contributors=len(humans),
            bots=sum(kind == "Bot" for kind, _ in pairs),
            top_author_share=round(max(humans) / sum(humans), 3) if humans and sum(humans) else None,
            commits_all_time=sum(int(n) for _, n in pairs),
        )
    except GhError as err:
        gaps.append(f"contributors:{err.code}")
    try:
        releases = [r for r in json.loads(gh_api(f"repos/{repo}/releases?per_page=100"))
                    if not r.get("draft") and r.get("published_at")]
        if releases:
            newest = max(releases, key=lambda r: r["published_at"])
            record.update(
                latest_release_tag=newest["tag_name"],
                latest_release_at=newest["published_at"],
                latest_release_prerelease=newest["prerelease"],
            )
        cutoff = NOW - timedelta(days=365)
        record["releases_12m"] = sum(parse_ts(r["published_at"]) >= cutoff for r in releases)
    except GhError as err:
        gaps.append(f"releases:{err.code}")
    try:
        headers, body = split_include(gh_api(f"repos/{repo}/pulls?state=open&per_page=1", include=True))
        open_prs = list_total(headers, body)
        record.update(open_prs=open_prs, open_issues=max(meta["open_issues_count"] - open_prs, 0))
    except GhError as err:
        gaps.append(f"pulls:{err.code}")
    if gaps:
        record["gaps"] = gaps
    return record


def needs_fetch(cached, refresh):
    if refresh or cached is None or cached.get("error"):
        return True
    return parse_ts(cached["fetched_at"]) < NOW - MAX_AGE


def save_metrics(cache):
    payload = {"generated_at": NOW.isoformat(timespec="seconds"), "repos": cache}
    METRICS_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def collect(projects, cache, refresh):
    todo = [p["repo"] for p in projects if needs_fetch(cache.get(p["repo"].lower()), refresh)]
    print(f"fetching {len(todo)} of {len(projects)} projects", flush=True)
    if not todo:
        return
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        jobs = {pool.submit(fetch_repo, repo): repo for repo in todo}
        for done, job in enumerate(cf.as_completed(jobs), start=1):
            repo = jobs[job]
            try:
                record = job.result()
            except Exception as exc:  # keep going, and record the failure for this repo
                record = {"repo": repo, "fetched_at": NOW.isoformat(timespec="seconds"),
                          "error": "exception", "error_message": str(exc)[:300]}
            cache[repo.lower()] = record
            if done % 20 == 0 or done == len(todo):
                save_metrics(cache)
                print(f"  {done}/{len(todo)}", flush=True)


def as_of(m):
    """UTC date the record was collected. Statuses and day counts are judged as of that date."""
    return parse_ts(m["fetched_at"]).date() if m.get("fetched_at") else TODAY


def status_of(m):
    if not m:
        return "Not fetched"
    if m.get("error"):
        return "Unavailable"
    if m.get("archived"):
        return "Archived"
    if not m.get("last_commit_at"):
        return "Stale"
    days = (as_of(m) - parse_ts(m["last_commit_at"]).date()).days
    if days <= 30:
        return "Active"
    if days <= 90:
        return "Recent"
    if days <= 365:
        return "Slow"
    return "Stale"


def build_rows(projects, cache):
    rows = []
    for p in projects:
        m = cache.get(p["repo"].lower(), {})
        row = {**p, **m, "status": status_of(m)}
        last = m.get("last_commit_at")
        row["days_since_commit"] = (as_of(m) - parse_ts(last).date()).days if last else None
        created = m.get("created_at")
        months = max((as_of(m) - parse_ts(created).date()).days / 30.44, 1.0) if created else None
        row["age_months"] = round(months, 1) if months else None
        row["stars_per_month"] = round(m.get("stars", 0) / months, 1) if months else None
        rows.append(row)
    return rows


def write_csv(rows):
    with CSV_FILE.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            flat = {}
            for key in CSV_FIELDS:
                value = row.get(key)
                if isinstance(value, list):
                    value = ";".join(value)
                flat[key] = "" if value is None else value
            writer.writerow(flat)


def cell(text):
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def fmt_int(value):
    return "—" if value is None else f"{value:,}"


def day(ts):
    return ts[:10] if ts else "—"


def name_link(row):
    url = row.get("url") or f"https://github.com/{row['repo']}"
    tag = " _(new)_" if row["origin"] == "discovered" else ""
    return f"[{cell(row['name'])}]({url}){tag}"


def license_label(row):
    if row.get("error") or row.get("license") is None:
        return "—"
    if row["license"] == "":
        return "None"
    return "Other" if row["license"] == "NOASSERTION" else row["license"]


def anchor(title):
    """GitHub's heading anchor: lower-case, drop punctuation, spaces to hyphens."""
    return re.sub(r"[^\w\- ]", "", title.strip().lower()).replace(" ", "-")


def project_description(row):
    desc = cell(row.get("description") or row.get("list_description") or row.get("github_description"))
    if row.get("notes"):
        desc = f"{desc} ({cell(row['notes'])})".strip()
    if len(desc) <= 120:
        return desc or "—"
    escaped = html.escape(desc).replace(r"\|", "&#124;")
    return f"<details><summary>Description</summary>{escaped}</details>"


def project_table(rows):
    lines = [
        "| Project | Popularity | Activity | Other details |",
        "|---|---|---|---|",
    ]
    for r in sorted(rows, key=lambda r: (-(r.get("stars") or 0), r["name"].lower())):
        tag = r.get("latest_release_tag")
        if tag:
            tag = re.sub(r"([._/@-])", r"\1<wbr>", cell(tag))
        release = f"{tag} ({day(r.get('latest_release_at'))})" if tag else "—"
        open_work = "—" if r.get("open_prs") is None else f"{fmt_int(r.get('open_issues'))} / {fmt_int(r['open_prs'])}"
        lines.append("| " + " | ".join([
            f"{name_link(r)}<br>{project_description(r)}",
            f"**{fmt_int(r.get('stars'))} stars**<br>{fmt_int(r.get('contributors'))} contributors<br>{fmt_int(r.get('forks'))} forks",
            f"**{r['status']}**<br>{fmt_int(r.get('commits_90d'))} commits (90d)<br>Last commit: {day(r.get('last_commit_at'))}",
            f"Release: {release}<br>Issues / PRs: {open_work}<br>License: {license_label(r)}",
        ]) + " |")
    return "\n".join(lines)


def glance_table(rows):
    contributors = [r["contributors"] for r in rows if r.get("contributors") is not None]
    days = [r["days_since_commit"] for r in rows if r.get("days_since_commit") is not None]
    lines = [
        "| Metric | Value |",
        "|---|--:|",
        f"| Projects tracked | {len(rows):,} |",
        f"| Total stars | {sum(r.get('stars') or 0 for r in rows):,} |",
    ]
    if contributors:
        lines.append(f"| Median contributors per project | {statistics.median(contributors):g} |")
    if days:
        lines.append(f"| Median days since last commit | {statistics.median(days):g} |")
    for s in STATUSES:
        lines.append(f"| Status: {s} | {sum(r['status'] == s for r in rows):,} |")
    return "\n".join(lines)


def category_overview(categories, rows):
    lines = [
        "| Category | Projects | Total stars | Active or recent | Stale or archived |",
        "|---|--:|--:|--:|--:|",
    ]
    for cat in categories:
        members = [r for r in rows if r["category"] == cat["id"]]
        if not members:
            continue
        active = sum(r["status"] in ("Active", "Recent") for r in members)
        stale = sum(r["status"] in ("Stale", "Archived") for r in members)
        stars = sum(r.get("stars") or 0 for r in members)
        lines.append(f"| [{SHORT.get(cat['id'], cat['id'])}](#{anchor(cat['title'])}) | {len(members)} | {stars:,} | {active} | {stale} |")
    return "\n".join(lines)


def top_by_stars(rows):
    top = sorted(rows, key=lambda r: -(r.get("stars") or 0))[:15]
    lines = ["| # | Project | Category | Stars | Contributors | Status |", "|--:|---|---|--:|--:|---|"]
    for i, r in enumerate(top, 1):
        lines.append(f"| {i} | {name_link(r)} | {SHORT.get(r['category'], r['category'])} | {fmt_int(r.get('stars'))} | {fmt_int(r.get('contributors'))} | {r['status']} |")
    return "\n".join(lines)


def recent_commits(rows):
    dated = sorted((r for r in rows if r.get("last_commit_at")), key=lambda r: r["last_commit_at"], reverse=True)[:15]
    lines = ["| # | Project | Category | Last commit | Commits (90d) | Status |", "|--:|---|---|---|--:|---|"]
    for i, r in enumerate(dated, 1):
        lines.append(f"| {i} | {name_link(r)} | {SHORT.get(r['category'], r['category'])} | {day(r['last_commit_at'])} | {fmt_int(r.get('commits_90d'))} | {r['status']} |")
    return "\n".join(lines)


def risk_table(rows):
    pool = [r for r in rows if r.get("top_author_share") is not None
            and (r.get("commits_all_time") or 0) >= 100 and not r.get("archived")]
    top = sorted(pool, key=lambda r: -r["top_author_share"])[:10]
    lines = ["| Project | Top author share | Contributors | Commits (all time, approx.) | Status |", "|---|--:|--:|--:|---|"]
    for r in top:
        lines.append(f"| {name_link(r)} | {r['top_author_share']:.0%} | {fmt_int(r.get('contributors'))} | {fmt_int(r.get('commits_all_time'))} | {r['status']} |")
    return "\n".join(lines)


def render_readme(doc, rows):
    cats = doc["categories"]
    origins = {o: sum(r["origin"] == o for r in rows) for o in ("awesome-list", "discovered", "adjacent")}
    dates = sorted({as_of(r).isoformat() for r in rows if r.get("fetched_at")})
    snapshot = dates[0] if len(dates) == 1 else f"{dates[0]} to {dates[-1]}" if dates else TODAY.isoformat()
    parts = [
        f"# {TITLE} — there are {len(rows)}", "",
        INTRO.format(total=len(rows), active=sum(r["status"] == "Active" for r in rows)), "",
        f"**Metrics collected {snapshot} (UTC)** · {origins['awesome-list']} from the source list · "
        f"{origins['discovered']} new · {origins['adjacent']} adjacent frameworks · refresh with `python3 scripts/update.py`",
        "",
        "## At a glance", "", glance_table(rows), "",
        "### Categories", "", category_overview(cats, rows), "",
        "### Top 15 by stars", "", top_by_stars(rows), "",
        "### Most recent commits", "", recent_commits(rows), "",
        "### Single-maintainer risk", "",
        "Projects where one person wrote nearly all human commits. Ten highest top-author shares among projects with at least 100 commits that are not archived.", "",
        risk_table(rows), "",
    ]
    for cat in cats:
        members = [r for r in rows if r["category"] == cat["id"]]
        if not members:
            continue
        parts += [f"## {cat['title']}", "", cat.get("description", ""), "", project_table(members), ""]
    parts += [METHOD, MAINTAIN, CREDITS]
    return "\n".join(parts).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--refresh", action="store_true", help="fetch every project, not only stale ones")
    parser.add_argument("--render-only", action="store_true", help="skip GitHub calls and render from the cache")
    parser.add_argument("--only", nargs="+", metavar="OWNER/REPO", help="fetch only these repos")
    args = parser.parse_args()

    doc = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))
    cache = {}
    if METRICS_FILE.exists():
        cache = json.loads(METRICS_FILE.read_text(encoding="utf-8")).get("repos", {})

    if not args.render_only:
        targets = doc["projects"]
        if args.only:
            wanted = {r.lower() for r in args.only}
            targets = [p for p in targets if p["repo"].lower() in wanted]
        collect(targets, cache, refresh=args.refresh)
        save_metrics(cache)

    rows = build_rows(doc["projects"], cache)
    write_csv(rows)
    README_FILE.write_text(render_readme(doc, rows), encoding="utf-8")
    print(f"rendered {README_FILE.name} and {CSV_FILE.name} for {len(rows)} projects")


if __name__ == "__main__":
    main()
