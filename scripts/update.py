#!/usr/bin/env python3
"""Fetch GitHub metrics for every project in data/projects.json, then render README.md and data/projects.csv.

Needs the GitHub CLI (gh), signed in with read access to public repositories. Repository data comes from the
GraphQL API in batches; contributors come from the REST API, because GraphQL does not expose them.

    python3 scripts/update.py                 fetch metrics older than 7 days, then render
    python3 scripts/update.py --refresh       fetch every project again, then render
    python3 scripts/update.py --render-only   render from data/metrics.json, no network calls
    python3 scripts/update.py --only a/b c/d  fetch only these projects (always fresh), then render
    python3 scripts/update.py --discover      search GitHub for new projects, write data/candidates.json
"""

import argparse
import concurrent.futures as cf
import csv
import html
import io
import json
import os
import re
import statistics
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_FILE = ROOT / "data" / "projects.json"
METRICS_FILE = ROOT / "data" / "metrics.json"
CSV_FILE = ROOT / "data" / "projects.csv"
FEATURES_FILE = ROOT / "data" / "features.json"
DISCOVERY_FILE = ROOT / "data" / "discovery.json"
CANDIDATES_FILE = ROOT / "data" / "candidates.json"
README_FILE = ROOT / "README.md"

NOW = datetime.now(timezone.utc)
TODAY = NOW.date()
MAX_AGE = timedelta(days=7)               # repository metrics
CONTRIBUTORS_MAX_AGE = timedelta(days=30)  # REST contributor lists change slowly and cost the most calls
BATCH = 20                                 # repositories per GraphQL query; halved when GitHub times out
README_BATCH = 10
README_CHARS = 60_000
README_PATHS = ["README.md", "readme.md", "Readme.md", "README.MD", "README.markdown", "README.rst",
                "README.txt", "README", "docs/README.md"]
RELEASE_PAGES = 20                         # at most 2,000 releases read per repository
REST_WORKERS = 2                           # GitHub asks clients to avoid concurrent requests; keep this small
RESERVE = 100                              # pause when fewer calls or points than this are left
TRANSIENT = {500, 502, 503, 504}           # retried; a failure keeps the previous snapshot
GONE = {404, 410, 451}                     # the repository no longer exists or is blocked
GAP_FIELDS = {
    "contributors": ["contributors", "bots", "top_author_share", "contributors_fetched_at"],
    "releases": ["latest_release_tag", "latest_release_at", "latest_release_prerelease", "releases_12m",
                 "releases_12m_capped"],
    "readme": ["features", "readme_found"],
}
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
    "license", "language", "languages", "features", "homepage", "archived", "topics", "url", "description",
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
    "languages, and how recently it was updated, plus the agents, isolation, and interfaces its README mentions. "
    "The [Single-maintainer risk](#single-maintainer-risk) table shows projects that depend on one person. "
    "The list starts from "
    "[andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) "
    "(CC0-1.0) and adds projects that list does not cover. Figures are a snapshot; see [Methodology](#methodology)."
)
METHOD = """## Methodology

**Source.** Projects start from [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) (CC0-1.0). Projects marked _(new)_ were found by GitHub search, the source's own references, and web search, and were not in that list. Each new project had to meet the same scope: it orchestrates, supervises, or coordinates several AI agents or agent sessions; it is open source or source-available; and it is active. Adjacent frameworks are general-purpose agent SDKs. They are listed separately because many teams use them for multi-agent orchestration. New candidates are found with saved GitHub searches (`data/discovery.json`) and reviewed by hand before they are added.

**Data.** GitHub GraphQL API for repository metadata, commits, releases, issues, pull requests, languages, and READMEs; GitHub REST API for contributors, which GraphQL does not expose. Both go through the GitHub CLI, collected on the date shown above (UTC). Repository figures refer to the default branch. Statuses and day counts are judged as of each project's collection date. Contributor lists are refreshed every 30 days, other figures every 7.

| Column | Definition |
|---|---|
| Stars, Forks | Repository metadata. |
| Language | Share of the repository's code by bytes, as GitHub's linguist detects it. Languages under 5% are left out of the tables. |
| Features | Agents, isolation, interfaces, protocols, and workflow features found by keyword in the README, the GitHub description, and topics (`data/features.json`). It is a heuristic: a passing mention also counts, and a feature the README does not name is missed. |
| License | The SPDX id GitHub detects. Check the license file before reuse; detection can be wrong. "None" means no license was detected, so default copyright applies. |
| Contributors | GitHub accounts (type `User`) with at least one commit on the default branch. Bots are excluded and counted separately in `data/metrics.json`. |
| Commits (90d) | Commits on the default branch in the 90 days before the snapshot. |
| Last commit | Committer date of the newest default-branch commit. `pushed_at` is not used, because it also changes when other branches are pushed. |
| Status | **Active**: last commit within 30 days. **Recent**: 31 to 90 days. **Slow**: 91 to 365 days. **Stale**: older than a year, or no commits. **Archived**: archived on GitHub. **Unavailable**: the repository no longer exists, or the API call failed and there is no earlier snapshot. Unavailable projects are not included in the count in the title. When a fetch fails temporarily, the previous snapshot is kept. |
| Latest release | Newest non-draft GitHub Release, pre-releases included. Projects that only push tags show "—". |
| Open issues / PRs | Open issues (excluding pull requests) and open pull requests. |

**Also in `data/projects.csv`.** Top-author share (the top human contributor's share of human contributions; values near 100% mean one person does almost all of the work), commits across all time on the default branch, releases in the last 12 months, stars per month since creation, age in months, every detected language with its share, and the detected features.

**Limitations.** Stars are a popularity signal, not a quality measure, and can be inflated. Contributor counts cover GitHub accounts only, so commits made under unlinked emails are not counted. Feature detection reads text, not code. Stale does not mean unusable; many small tools are finished. All figures are a point-in-time snapshot.
"""
MAINTAIN = """## Keeping it current

```sh
python3 scripts/update.py                # fetch metrics older than 7 days, then re-render
python3 scripts/update.py --refresh      # fetch everything again
python3 scripts/update.py --only a/b     # fetch these projects now, then re-render
python3 scripts/update.py --render-only  # rebuild this README from data/metrics.json
python3 scripts/update.py --discover     # search GitHub for new projects; results go to data/candidates.json
```

The script needs the GitHub CLI (`gh`) signed in. It runs GraphQL queries one at a time, and waits when GitHub's rate limits run low. To add a project, append an entry to `data/projects.json` with `repo`, `name`, `category`, `origin`, and `description`, then run the script. To stop a reviewed candidate from coming back, add it to `rejected` in `data/discovery.json`. Feature keywords live in `data/features.json`.

A GitHub Actions workflow (`.github/workflows/update.yml`) refreshes the metrics every day and commits the result. Every Monday it runs discovery and rewrites the open issue labelled `candidates` with the projects to review.
"""
CREDITS = """## Credits

The starting list, its categories, and its one-line descriptions come from [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators), released under CC0-1.0. The descriptions here are shortened rewrites; the originals are kept in `data/projects.json` as `list_description`.
"""

REPO_FIELDS = """
  nameWithOwner url description homepageUrl stargazerCount forkCount isArchived isFork createdAt pushedAt
  licenseInfo { spdxId }
  primaryLanguage { name }
  languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { totalSize edges { size node { name } } }
  repositoryTopics(first: 20) { nodes { topic { name } } }
  issues(states: OPEN) { totalCount }
  pullRequests(states: OPEN) { totalCount }
  releases(first: 100, orderBy: {field: CREATED_AT, direction: DESC}) {
    pageInfo { hasNextPage endCursor }
    nodes { tagName publishedAt createdAt isDraft isPrerelease }
  }
  defaultBranchRef { target { ... on Commit {
    committedDate
    recent: history(since: $since) { totalCount }
    all: history { totalCount }
  } } }
"""
RELEASES_QUERY = """
query($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    releases(first: 100, after: $after, orderBy: {field: CREATED_AT, direction: DESC}) {
      pageInfo { hasNextPage endCursor }
      nodes { tagName publishedAt createdAt isDraft isPrerelease }
    }
  }
}
"""
SEARCH_QUERY = """
query($q: String!, $after: String) {
  search(query: $q, type: REPOSITORY, first: 50, after: $after) {
    pageInfo { hasNextPage endCursor }
    nodes { ... on Repository {
      nameWithOwner url description stargazerCount createdAt pushedAt isFork isArchived
      primaryLanguage { name }
      repositoryTopics(first: 20) { nodes { topic { name } } }
    } }
  }
}
"""


# --- GitHub access ---------------------------------------------------------------------------------------------

class GhError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message


class BudgetExceeded(Exception):
    """The run reached its time budget (--max-minutes). Work stops; what was fetched is kept."""


DEADLINE = None          # time.monotonic() value after which no new work starts; set by --max-minutes
MAX_REST_PAGES = 50      # contributor lists are capped by GitHub anyway; this guards against a pagination loop
MAX_FAILED_BATCHES = 3   # consecutive batches where every repository failed: stop instead of retrying forever


def check_budget(extra=0):
    if DEADLINE is not None and time.monotonic() + extra > DEADLINE:
        raise BudgetExceeded()


def gh_once(args, stdin=None):
    """Run `gh api --include` once and return (status, lower-cased headers, body). Status is None without a response."""
    proc = subprocess.run(["gh", "api", "--include", *args], input=stdin, capture_output=True, text=True)
    if not proc.stdout.startswith("HTTP/"):
        return None, {}, proc.stderr.strip()
    head, *rest = re.split(r"\r?\n\r?\n", proc.stdout, maxsplit=1)
    lines = head.splitlines()
    status = int(lines[0].split()[1])
    headers = {}
    for line in lines[1:]:
        key, sep, value = line.partition(":")
        if sep:
            headers[key.strip().lower()] = value.strip()
    return status, headers, rest[0] if rest else ""


def _int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def pause(seconds, why):
    seconds = min(max(seconds, 1), 3700)
    check_budget(seconds)   # never start a wait that would run past the time budget
    if seconds >= 30:
        print(f"  {why}; waiting {seconds / 60:.1f} min", flush=True)
    time.sleep(seconds)


def call(args, stdin=None, retry_transient=True):
    """One API request with GitHub's rate-limit rules applied.

    Primary limit: when `x-ratelimit-remaining` is 0, wait until `x-ratelimit-reset`. Secondary limit: honour
    `retry-after`, otherwise wait at least a minute with exponential backoff. Before returning, pause if fewer
    than RESERVE calls or points are left, so the next request does not hit the limit."""
    for attempt in range(6):
        status, headers, body = gh_once(args, stdin)
        remaining = _int(headers.get("x-ratelimit-remaining"), None)
        reset = _int(headers.get("x-ratelimit-reset"), 0)
        if status is None:
            if attempt < 3:
                time.sleep(3 * 2 ** attempt)
                continue
            raise GhError(None, body)
        limited = (status in (403, 429) and ("rate limit" in body.lower() or "retry-after" in headers or remaining == 0)) \
            or (status == 200 and '"type":"RATE_LIMITED"' in body.replace(" ", ""))
        if limited:
            if "retry-after" in headers:
                pause(_int(headers["retry-after"], 60) + 1, "secondary rate limit")
            elif remaining == 0:
                pause(reset - time.time() + 5, f"{headers.get('x-ratelimit-resource', 'API')} rate limit reached")
            else:
                pause(60 * 2 ** min(attempt, 3), "secondary rate limit")
            continue
        if status in TRANSIENT and retry_transient and attempt < 3:
            time.sleep(3 * 2 ** attempt)
            continue
        if remaining is not None and remaining < RESERVE:
            pause(reset - time.time() + 5, f"only {remaining} {headers.get('x-ratelimit-resource', 'API')} calls left")
        return status, headers, body
    raise GhError(429, "rate limit persisted")


def graphql(query, variables, retry_transient=True):
    """Run a GraphQL query. Returns (data, errors); GitHub reports per-alias errors next to partial data."""
    status, _, body = call(["graphql", "--input", "-"], json.dumps({"query": query, "variables": variables}),
                           retry_transient)
    if status != 200:
        raise GhError(status, body[:300])
    try:
        doc = json.loads(body)
    except json.JSONDecodeError as err:
        raise GhError(None, f"bad GraphQL response: {err}") from err
    return doc.get("data") or {}, doc.get("errors") or []


def rest_pages(endpoint):
    """Yield the JSON items of a paginated REST endpoint, following the Link header."""
    url = endpoint
    for _ in range(MAX_REST_PAGES):
        if not url:
            return
        status, headers, body = call([url])
        if status == 204:
            return
        if status != 200:
            raise GhError(status, body[:300])
        yield from json.loads(body)
        found = re.search(r'<https://api\.github\.com/([^>]+)>;\s*rel="next"', headers.get("link", ""))
        url = found.group(1) if found else None


def rate_status():
    status, _, body = call(["rate_limit"])
    if status != 200:
        raise GhError(status, body[:300])
    res = json.loads(body)["resources"]
    return res["core"]["remaining"], res["graphql"]["remaining"]


def parse_ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def split_repo(repo):
    owner, _, name = repo.partition("/")
    return owner, name


# --- Features ----------------------------------------------------------------------------------------------------

def load_features():
    """Compile data/features.json into [(group, label, regex)], keeping the file's order."""
    groups = json.loads(FEATURES_FILE.read_text(encoding="utf-8"))["groups"]
    return [(group, label, re.compile("|".join(f"(?:{p})" for p in patterns), re.IGNORECASE))
            for group, labels in groups.items() for label, patterns in labels.items()]


def detect_features(compiled, *texts):
    """Labels whose keywords appear in any of the texts, in the order of data/features.json."""
    blob = "\n".join(t for t in texts if t)
    return [label for _, label, regex in compiled if regex.search(blob)]


# --- Fetching ----------------------------------------------------------------------------------------------------

def error_record(repo, code, message):
    return {"repo": repo, "fetched_at": NOW.isoformat(timespec="seconds"), "error": code,
            "error_message": (message or "")[:300]}


def published(nodes):
    return [r for r in nodes if r and not r.get("isDraft") and r.get("publishedAt")]


def record_from_graphql(repo, g):
    """Map one GraphQL repository object to the fields stored in data/metrics.json."""
    target = (g.get("defaultBranchRef") or {}).get("target") or {}
    langs = g.get("languages") or {}
    total = langs.get("totalSize") or 0
    record = {
        "repo": repo,
        "fetched_at": NOW.isoformat(timespec="seconds"),
        "full_name": g["nameWithOwner"],
        "url": g["url"],
        "github_description": g.get("description") or "",
        "homepage": g.get("homepageUrl") or "",
        "stars": g["stargazerCount"],
        "forks": g["forkCount"],
        "archived": g["isArchived"],
        "fork": g["isFork"],
        "created_at": g["createdAt"],
        "pushed_at": g["pushedAt"],
        "license": (g.get("licenseInfo") or {}).get("spdxId") or "",
        "language": (g.get("primaryLanguage") or {}).get("name") or "",
        "languages": [{"name": e["node"]["name"], "share": round(e["size"] / total, 3)}
                      for e in langs.get("edges") or []] if total else [],
        "topics": [n["topic"]["name"] for n in (g.get("repositoryTopics") or {}).get("nodes") or []],
        "open_issues": g["issues"]["totalCount"],
        "open_prs": g["pullRequests"]["totalCount"],
        "last_commit_at": target.get("committedDate"),
        "commits_90d": (target.get("recent") or {}).get("totalCount", 0),
        "commits_all_time": (target.get("all") or {}).get("totalCount", 0),
    }
    rel = g.get("releases") or {}
    record["_releases"] = published(rel.get("nodes") or [])
    record["_release_cursor"] = rel["pageInfo"]["endCursor"] if (rel.get("pageInfo") or {}).get("hasNextPage") else None
    record["_release_oldest"] = min((r["createdAt"] for r in rel.get("nodes") or [] if r and r.get("createdAt")),
                                    default=None)
    return record


def batch_query(repos):
    params = ["$since: GitTimestamp!"]
    parts = []
    variables = {"since": (NOW - timedelta(days=90)).strftime("%Y-%m-%dT%H:%M:%SZ")}
    for i, repo in enumerate(repos):
        owner, name = split_repo(repo)
        params += [f"$o{i}: String!", f"$n{i}: String!"]
        variables[f"o{i}"], variables[f"n{i}"] = owner, name
        parts.append(f"r{i}: repository(owner: $o{i}, name: $n{i}) {{ {REPO_FIELDS} }}")
    return f"query({', '.join(params)}) {{\n" + "\n".join(parts) + "\n}", variables


def fetch_batch(repos):
    """Fetch metadata for several repositories in one GraphQL query. When GitHub times out, split the batch."""
    query, variables = batch_query(repos)
    try:
        data, errors = graphql(query, variables, retry_transient=len(repos) == 1)
    except GhError as err:
        if len(repos) > 1 and (err.code in TRANSIENT or err.code is None):
            mid = len(repos) // 2
            return {**fetch_batch(repos[:mid]), **fetch_batch(repos[mid:])}
        return {repo: error_record(repo, err.code or "unknown", err.message) for repo in repos}
    by_alias = {}
    for e in errors:
        path = e.get("path") or []
        if path:
            by_alias.setdefault(path[0], e)
    out = {}
    for i, repo in enumerate(repos):
        g = data.get(f"r{i}")
        if g:
            out[repo] = record_from_graphql(repo, g)
            continue
        e = by_alias.get(f"r{i}") or (errors[0] if errors else {})
        code = 404 if e.get("type") == "NOT_FOUND" else "graphql"
        out[repo] = error_record(repo, code, e.get("message", "no data returned"))
    return out


def finish_releases(record):
    """Read further release pages while they still fall inside the last 12 months, then summarise releases."""
    cutoff = NOW - timedelta(days=365)
    releases = record.pop("_releases")
    cursor = record.pop("_release_cursor")
    oldest = record.pop("_release_oldest")
    pages, capped = 1, False
    owner, name = split_repo(record["full_name"])
    while cursor and oldest and parse_ts(oldest) >= cutoff:
        if pages >= RELEASE_PAGES:
            capped = True
            break
        data, errors = graphql(RELEASES_QUERY, {"owner": owner, "name": name, "after": cursor})
        rel = (data.get("repository") or {}).get("releases")
        if not rel:
            raise GhError("graphql", (errors[0] if errors else {}).get("message", "no releases returned"))
        nodes = rel.get("nodes") or []
        releases += published(nodes)
        oldest = min((r["createdAt"] for r in nodes if r and r.get("createdAt")), default=None)
        cursor = rel["pageInfo"]["endCursor"] if rel["pageInfo"]["hasNextPage"] else None
        pages += 1
    if releases:
        newest = max(releases, key=lambda r: r["publishedAt"])
        record.update(latest_release_tag=newest["tagName"], latest_release_at=newest["publishedAt"],
                      latest_release_prerelease=newest["isPrerelease"])
    record["releases_12m"] = sum(parse_ts(r["publishedAt"]) >= cutoff for r in releases)
    if capped:
        record["releases_12m_capped"] = True


def fetch_readmes(full_names):
    """Return {full_name: README text or None}, trying the usual README file names. Splits on timeouts."""
    if not full_names:
        return {}
    params, parts, variables = [], [], {}
    lookups = " ".join(f'p{j}: object(expression: "HEAD:{path}") {{ ... on Blob {{ text }} }}'
                       for j, path in enumerate(README_PATHS))
    for i, full in enumerate(full_names):
        owner, name = split_repo(full)
        params += [f"$o{i}: String!", f"$n{i}: String!"]
        variables[f"o{i}"], variables[f"n{i}"] = owner, name
        parts.append(f"r{i}: repository(owner: $o{i}, name: $n{i}) {{ {lookups} }}")
    query = f"query({', '.join(params)}) {{\n" + "\n".join(parts) + "\n}"
    try:
        data, _ = graphql(query, variables, retry_transient=len(full_names) == 1)
    except GhError as err:
        if len(full_names) > 1 and (err.code in TRANSIENT or err.code is None):
            mid = len(full_names) // 2
            return {**fetch_readmes(full_names[:mid]), **fetch_readmes(full_names[mid:])}
        raise
    out = {}
    for i, full in enumerate(full_names):
        repo = data.get(f"r{i}") or {}
        text = next((repo[f"p{j}"]["text"] for j in range(len(README_PATHS))
                     if (repo.get(f"p{j}") or {}).get("text")), None)
        out[full] = text[:README_CHARS] if text else None
    return out


def fetch_contributors(full_name):
    pairs = [(c.get("type"), c.get("contributions", 0)) for c in rest_pages(f"repos/{full_name}/contributors?per_page=100")]
    humans = [n for kind, n in pairs if kind == "User"]
    return {
        "contributors": len(humans),
        "bots": sum(kind == "Bot" for kind, _ in pairs),
        "top_author_share": round(max(humans) / sum(humans), 3) if humans and sum(humans) else None,
        "contributors_fetched_at": NOW.isoformat(timespec="seconds"),
    }


def contributors_due(old, refresh):
    if refresh or not old or old.get("error") or old.get("contributors") is None:
        return True
    stamp = old.get("contributors_fetched_at") or old.get("fetched_at")
    return parse_ts(stamp) < NOW - CONTRIBUTORS_MAX_AGE


def needs_fetch(cached, refresh):
    if refresh or cached is None or cached.get("error") or cached.get("last_error"):
        return True
    if "languages" not in cached:   # written before languages and features were collected
        return True
    return parse_ts(cached["fetched_at"]) < NOW - MAX_AGE


def merge_record(old, new):
    """Combine a fresh fetch with the cached record.

    A repository that is gone replaces the cache. A temporary failure keeps the previous snapshot and notes the
    error, so a 502 or a rate limit does not wipe a project's metrics. Fields a step failed to return are
    carried over from the previous snapshot."""
    usable = old if old and not old.get("error") else None
    if new.get("error"):
        if new["error"] in GONE or usable is None:
            return new
        kept = {k: v for k, v in usable.items() if not k.startswith("last_error")}
        return {**kept, "last_error": new["error"], "last_error_message": new.get("error_message", ""),
                "last_error_at": new["fetched_at"]}
    if usable:
        for gap in new.get("gaps", []):
            for key in GAP_FIELDS.get(gap.split(":")[0], []):
                if key not in new and key in usable:
                    new[key] = usable[key]
    return new


def write_atomic(path, text):
    """Write to a temporary file, then rename it, so an interrupted run never leaves a truncated file."""
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    os.replace(tmp, path)


def save_metrics(cache):
    payload = {"generated_at": NOW.isoformat(timespec="seconds"), "repos": cache}
    write_atomic(METRICS_FILE, json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def preflight():
    try:
        core, points = rate_status()
    except GhError as err:
        sys.exit(f"cannot reach the GitHub API through gh; run `gh auth status`.\n{err.message}")
    print(f"  GraphQL points left this hour: {points:,} · REST calls left: {core:,}", flush=True)


def enrich(records, cache, refresh, features):
    """Add releases, README features, and contributors to freshly fetched records, in place."""
    ok = [r for r in records if not r.get("error")]
    for record in ok:
        try:
            finish_releases(record)
        except GhError as err:
            for key in ("_releases", "_release_cursor", "_release_oldest"):
                record.pop(key, None)
            record.setdefault("gaps", []).append(f"releases:{err.code}")
    for start in range(0, len(ok), README_BATCH):
        chunk = ok[start:start + README_BATCH]
        try:
            texts = fetch_readmes([r["full_name"] for r in chunk])
        except GhError as err:
            for record in chunk:
                record.setdefault("gaps", []).append(f"readme:{err.code}")
            continue
        for record in chunk:
            text = texts.get(record["full_name"])
            record["readme_found"] = text is not None
            record["features"] = detect_features(features, text, record["github_description"], " ".join(record["topics"]))

    def contributors(record):
        old = cache.get(record["repo"].lower())
        if not contributors_due(old, refresh):
            for key in GAP_FIELDS["contributors"]:
                if key in old:
                    record[key] = old[key]
            return
        try:
            record.update(fetch_contributors(record["full_name"]))
        except GhError as err:   # e.g. 403 when the contributor list is too large for the API
            record.setdefault("gaps", []).append(f"contributors:{err.code}")

    with cf.ThreadPoolExecutor(max_workers=REST_WORKERS) as pool:
        list(pool.map(contributors, ok))


def collect(projects, cache, refresh, features):
    todo = [p["repo"] for p in projects if needs_fetch(cache.get(p["repo"].lower()), refresh)]
    print(f"fetching {len(todo)} of {len(projects)} projects", flush=True)
    if not todo:
        return
    preflight()
    done, failed_batches = 0, 0
    for start in range(0, len(todo), BATCH):
        try:
            check_budget()
        except BudgetExceeded:
            print(f"  time budget reached; {len(todo) - done} projects left for the next run", flush=True)
            return
        chunk = todo[start:start + BATCH]
        try:
            fetched = fetch_batch(chunk)
            enrich(list(fetched.values()), cache, refresh, features)
        except BudgetExceeded:
            print(f"  time budget reached; {len(todo) - done} projects left for the next run", flush=True)
            return
        except Exception as exc:  # keep going; the previous snapshot of these repos is kept
            fetched = {repo: error_record(repo, "exception", str(exc)) for repo in chunk}
        for repo, record in fetched.items():
            cache[repo.lower()] = merge_record(cache.get(repo.lower()), record)
        done += len(chunk)
        save_metrics(cache)
        print(f"  {done}/{len(todo)}", flush=True)
        # Circuit breaker: if whole batches keep failing (bad token, GitHub outage), stop rather than burn the run.
        if all(r.get("error") and r["error"] not in GONE for r in fetched.values()):
            failed_batches += 1
            if failed_batches >= MAX_FAILED_BATCHES:
                sys.exit(f"stopping: {failed_batches} batches in a row failed completely "
                         f"(last error: {next(iter(fetched.values())).get('error_message', '')[:200]})")
        else:
            failed_batches = 0


def report(projects, cache):
    """Print projects that need attention in data/projects.json."""
    gone, failing, renamed, capped = [], [], [], []
    for p in projects:
        m = cache.get(p["repo"].lower()) or {}
        if m.get("error"):
            gone.append(f"{p['repo']} ({m['error']})")
        if m.get("last_error"):
            failing.append(f"{p['repo']} ({m['last_error']}, kept snapshot from {day(m.get('fetched_at'))})")
        if m.get("full_name") and m["full_name"].lower() != p["repo"].lower():
            renamed.append(f"{p['repo']} -> {m['full_name']}")
        if m.get("releases_12m_capped"):
            capped.append(p["repo"])
    for label, items in [("unavailable", gone), ("fetch failed, previous snapshot kept", failing),
                         ("renamed or moved; update data/projects.json", renamed),
                         (f"more than {RELEASE_PAGES * 100} releases, count is a lower bound", capped)]:
        if items:
            print(f"{label} ({len(items)}):")
            for item in items:
                print(f"  {item}")


# --- Discovery ---------------------------------------------------------------------------------------------------

def discover(doc, cache, features, days, report=None):
    """Search GitHub for recently created projects that match data/discovery.json and are not indexed yet."""
    cfg = json.loads(DISCOVERY_FILE.read_text(encoding="utf-8"))
    days = days or cfg.get("window_days", 30)
    start = (NOW - timedelta(days=days)).date().isoformat()
    known = {p["repo"].lower() for p in doc["projects"]}
    known |= {m["full_name"].lower() for m in cache.values() if m.get("full_name")}
    rejected = {r.lower() for r in cfg.get("rejected", [])}
    previous = {}
    if CANDIDATES_FILE.exists():
        previous = {c["repo"].lower(): c for c in json.loads(CANDIDATES_FILE.read_text(encoding="utf-8"))["candidates"]}
    preflight()
    found = {}
    try:
        for query in cfg["queries"]:
            check_budget()
            full = f"{query} created:>={start} stars:>={cfg.get('min_stars', 10)} fork:false archived:false"
            after, hits = None, 0
            for _ in range(20):   # GitHub returns at most 1,000 results per search
                data, errors = graphql(SEARCH_QUERY, {"q": full, "after": after})
                result = data.get("search")
                if not result:
                    print(f"  search failed: {query}: {(errors[0] if errors else {}).get('message', 'no data')}")
                    break
                for node in result["nodes"]:
                    if not node or not node.get("nameWithOwner"):
                        continue
                    key = node["nameWithOwner"].lower()
                    if key in known or key in rejected or node["isFork"] or node["isArchived"]:
                        continue
                    hits += 1
                    topics = [n["topic"]["name"] for n in (node.get("repositoryTopics") or {}).get("nodes") or []]
                    entry = found.setdefault(key, {
                        "repo": node["nameWithOwner"],
                        "url": node["url"],
                        "description": node.get("description") or "",
                        "stars": node["stargazerCount"],
                        "language": (node.get("primaryLanguage") or {}).get("name") or "",
                        "topics": topics,
                        "created_at": node["createdAt"],
                        "pushed_at": node["pushedAt"],
                        "features": detect_features(features, node.get("description"), " ".join(topics)),
                        "first_seen": previous.get(key, {}).get("first_seen", TODAY.isoformat()),
                        "queries": [],
                    })
                    if query not in entry["queries"]:
                        entry["queries"].append(query)
                if not result["pageInfo"]["hasNextPage"]:
                    break
                after = result["pageInfo"]["endCursor"]
            print(f"  {hits:>4}  {query}", flush=True)
    except BudgetExceeded:
        print("  time budget reached; keeping the candidates found so far", flush=True)
    # Keep earlier candidates that were neither added nor rejected, even if they fell out of the window.
    for key, entry in previous.items():
        if key not in found and key not in known and key not in rejected:
            found[key] = entry
    candidates = sorted(found.values(), key=lambda c: (-c["stars"], c["repo"].lower()))
    payload = {"generated_at": NOW.isoformat(timespec="seconds"), "window_start": start, "candidates": candidates}
    write_atomic(CANDIDATES_FILE, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    fresh = [c for c in candidates if c["first_seen"] == TODAY.isoformat()]
    print(f"{len(candidates)} candidates in {CANDIDATES_FILE.relative_to(ROOT)} ({len(fresh)} first seen today)")
    for c in candidates[:20]:
        print(f"  {c['stars']:>6}  {c['repo']}  {c['description'][:80]}")
    if report:
        write_atomic(Path(report), candidates_markdown(candidates, start))


def candidates_markdown(candidates, start, limit=150):
    """Review list for a GitHub issue. Issue bodies are capped at 65,536 characters, so long lists are cut."""
    today = TODAY.isoformat()
    lines = [
        f"Repositories created since {start} that match the searches in `data/discovery.json` and are not in the index. "
        f"{len(candidates)} open candidates, {sum(c['first_seen'] == today for c in candidates)} new this run.",
        "",
        "To add one, append it to `data/projects.json` with `origin: \"discovered\"`. To dismiss one, add it to "
        "`rejected` in `data/discovery.json`. This issue is rewritten on every discovery run.",
        "",
        "| | Repository | Stars | Language | Created | Description | Features |",
        "|---|---|--:|---|---|---|---|",
    ]
    for c in candidates[:limit]:
        new = "🆕" if c["first_seen"] == today else ""
        desc = cell(c["description"])[:140]
        feats = ", ".join(c["features"]) if isinstance(c.get("features"), list) else ""
        lines.append(f"| {new} | [{cell(c['repo'])}]({c['url']}) | {c['stars']:,} | {cell(c['language']) or '—'} | "
                     f"{day(c['created_at'])} | {desc or '—'} | {feats or '—'} |")
    if len(candidates) > limit:
        lines += ["", f"{len(candidates) - limit} more in `data/candidates.json`."]
    return "\n".join(lines)[:65000] + "\n"


# --- Rendering ---------------------------------------------------------------------------------------------------

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
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=CSV_FIELDS, extrasaction="ignore")
    writer.writeheader()
    for row in rows:
        flat = {}
        for key in CSV_FIELDS:
            value = row.get(key)
            if key == "languages":
                value = ";".join(f"{l['name']} {l['share']:.1%}" for l in value or [])
            elif isinstance(value, list):
                value = ";".join(value)
            flat[key] = "" if value is None else value
        writer.writerow(flat)
    write_atomic(CSV_FILE, buf.getvalue())


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


def language_label(row):
    shown = [f"{l['name']} {l['share']:.0%}" for l in row.get("languages") or [] if l["share"] >= 0.05][:3]
    return ", ".join(shown) or cell(row.get("language")) or "—"


def features_label(row):
    if not isinstance(row.get("features"), list):
        return "—"
    return ", ".join(row["features"]) or "none detected"


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
            f"{name_link(r)}<br>{project_description(r)}<br>_Features:_ {features_label(r)}",
            f"**{fmt_int(r.get('stars'))} stars**<br>{fmt_int(r.get('contributors'))} contributors<br>{fmt_int(r.get('forks'))} forks",
            f"**{r['status']}**<br>{fmt_int(r.get('commits_90d'))} commits (90d)<br>Last commit: {day(r.get('last_commit_at'))}",
            f"Language: {language_label(r)}<br>Release: {release}<br>Issues / PRs: {open_work}<br>License: {license_label(r)}",
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


def language_overview(rows):
    live = [r for r in rows if r["status"] != "Unavailable" and r.get("language")]
    counts = {}
    for r in live:
        counts[r["language"]] = counts.get(r["language"], 0) + 1
    lines = ["| Main language | Projects | Share |", "|---|--:|--:|"]
    for lang, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:12]:
        lines.append(f"| {cell(lang)} | {n} | {n / len(live):.0%} |")
    return "\n".join(lines)


def feature_overview(rows, features):
    checked = [r for r in rows if r["status"] != "Unavailable" and isinstance(r.get("features"), list)]
    if not checked:
        return "_Not collected yet._"
    lines = [
        f"Share of the {len(checked)} projects whose README, description, or topics mention each feature. "
        "Keyword matching, so treat it as a rough guide; see [Methodology](#methodology).", "",
        "| Group | Feature | Projects | Share |", "|---|---|--:|--:|",
    ]
    for group, label, _ in features:
        n = sum(label in r["features"] for r in checked)
        lines.append(f"| {group} | {label} | {n} | {n / len(checked):.0%} |")
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
    lines = ["| Project | Top author share | Contributors | Commits (all time) | Status |", "|---|--:|--:|--:|---|"]
    for r in top:
        lines.append(f"| {name_link(r)} | {r['top_author_share']:.0%} | {fmt_int(r.get('contributors'))} | {fmt_int(r.get('commits_all_time'))} | {r['status']} |")
    return "\n".join(lines)


def render_readme(doc, rows, features):
    cats = doc["categories"]
    origins = {o: sum(r["origin"] == o for r in rows) for o in ("awesome-list", "discovered", "adjacent")}
    dates = sorted({as_of(r).isoformat() for r in rows if r.get("fetched_at")})
    snapshot = dates[0] if len(dates) == 1 else f"{dates[0]} to {dates[-1]}" if dates else TODAY.isoformat()
    live = [r for r in rows if r["status"] != "Unavailable"]
    parts = [
        f"# {TITLE} — there are {len(live)}", "",
        INTRO.format(total=len(live), active=sum(r["status"] == "Active" for r in live)), "",
        f"**Metrics collected {snapshot} (UTC)** · {origins['awesome-list']} from the source list · "
        f"{origins['discovered']} new · {origins['adjacent']} adjacent frameworks · refresh with `python3 scripts/update.py`",
        "",
        "## At a glance", "", glance_table(rows), "",
        "### Categories", "", category_overview(cats, rows), "",
        "### Features", "", feature_overview(rows, features), "",
        "### Languages", "", language_overview(rows), "",
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
    return re.sub(r"\n{3,}", "\n\n", "\n".join(parts)).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--refresh", action="store_true", help="fetch every project, not only stale ones")
    parser.add_argument("--render-only", action="store_true", help="skip GitHub calls and render from the cache")
    parser.add_argument("--only", nargs="+", metavar="OWNER/REPO", help="fetch only these repos, even if fresh")
    parser.add_argument("--discover", action="store_true", help="search GitHub for new projects and write data/candidates.json")
    parser.add_argument("--days", type=int, metavar="N", help="with --discover: projects created in the last N days")
    parser.add_argument("--report", metavar="FILE", help="with --discover: also write a Markdown review list")
    parser.add_argument("--max-minutes", type=float, metavar="N",
                        help="time budget: start no new work (and no rate-limit wait) after N minutes; "
                             "projects not reached are fetched on the next run")
    args = parser.parse_args()
    global DEADLINE
    if args.max_minutes is not None:
        if args.max_minutes <= 0:
            parser.error("--max-minutes must be positive")
        DEADLINE = time.monotonic() + args.max_minutes * 60
    if args.render_only and (args.refresh or args.only or args.discover):
        parser.error("--render-only makes no network calls, so it cannot be combined with other options")
    if (args.days or args.report) and not args.discover:
        parser.error("--days and --report only apply to --discover")

    doc = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))
    features = load_features()
    cache = {}
    if METRICS_FILE.exists():
        cache = json.loads(METRICS_FILE.read_text(encoding="utf-8")).get("repos", {})

    if args.discover:
        discover(doc, cache, features, args.days, args.report)
        return

    if not args.render_only:
        targets = doc["projects"]
        if args.only:
            wanted = {r.lower() for r in args.only}
            targets = [p for p in targets if p["repo"].lower() in wanted]
            unknown = wanted - {p["repo"].lower() for p in targets}
            if unknown:
                parser.error(f"not in data/projects.json: {', '.join(sorted(unknown))}")
        collect(targets, cache, args.refresh or bool(args.only), features)
        save_metrics(cache)

    report(doc["projects"], cache)
    rows = build_rows(doc["projects"], cache)
    write_csv(rows)
    write_atomic(README_FILE, render_readme(doc, rows, features))
    print(f"rendered {README_FILE.name} and {CSV_FILE.name} for {len(rows)} projects")


if __name__ == "__main__":
    main()
