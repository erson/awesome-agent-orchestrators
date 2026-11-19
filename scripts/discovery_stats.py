"""Local discovery measurements. Raw counts start when instrumentation is enabled."""

import json
import re


def load(path):
    if not path.exists():
        return {"queries": {}, "candidates": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("queries"), dict) or not isinstance(data.get("candidates"), dict):
        raise ValueError("expected queries and candidates objects")
    for query, counts in data["queries"].items():
        if not query.strip() or not isinstance(counts, dict) or not all(
            type(counts.get(k)) is int and counts[k] >= 0 for k in ("pages", "raw")
        ):
            raise ValueError(f"invalid query counters for {query}")
    for repo, entry in data["candidates"].items():
        if not re.fullmatch(r"[a-z0-9-]+/[a-z0-9._-]+", repo) or not isinstance(entry, dict):
            raise ValueError(f"invalid candidate {repo}")
        sources = entry.get("queries")
        if not isinstance(sources, list) or not sources or not all(isinstance(q, str) and q.strip() for q in sources):
            raise ValueError(f"invalid query attribution for {repo}")
        if len(set(sources)) != len(sources) or entry.get("decision") not in ("open", "accepted", "rejected"):
            raise ValueError(f"invalid candidate record for {repo}")
    return data


def record_page(data, query, raw):
    counts = data["queries"].setdefault(query, {"pages": 0, "raw": 0})
    counts["pages"] += 1
    counts["raw"] += raw


def attribute(data, candidates):
    for candidate in candidates:
        queries = candidate["queries"]
        if queries:
            key = candidate["repo"].lower()
            entry = data["candidates"].setdefault(key, {"queries": [], "decision": "open"})
            entry["queries"] = sorted(set(entry["queries"]).union(queries))


def reconcile(data, indexed, rejected):
    for repo, entry in data["candidates"].items():
        if repo in indexed:
            entry["decision"] = "accepted"
        elif repo in rejected:
            entry["decision"] = "rejected"


def totals(data):
    template = {"raw": 0, "pages": 0, "unique": 0, "exclusive": 0, "accepted": 0, "rejected": 0}
    result = {q: {**template, **counts} for q, counts in data["queries"].items()}
    for candidate in data["candidates"].values():
        queries = candidate["queries"]
        for query in queries:
            counts = result.setdefault(query, template.copy())
            counts["unique"] += 1
            counts["exclusive"] += len(queries) == 1
            if candidate["decision"] != "open":
                counts[candidate["decision"]] += 1
    return result


def markdown(data):
    lines = [
        "### Discovery query performance", "",
        "Raw counts include repeated results across measured pages. Distinct candidates include attributable "
        "records from the initial queue. Exclusive candidates matched just one recorded query. "
        "Acceptance is accepted / reviewed. Earlier unrecorded decisions are unknown.", "",
        "| Query | Pages | Raw results | Distinct candidates | Exclusive | Accepted | Rejected | Acceptance |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for query, counts in sorted(totals(data).items()):
        reviewed = counts["accepted"] + counts["rejected"]
        rate = f"{counts['accepted'] / reviewed:.0%}" if reviewed else "—"
        name = query.replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {name} | {counts['pages']} | {counts['raw']} | {counts['unique']} | "
                     f"{counts['exclusive']} | {counts['accepted']} | {counts['rejected']} | {rate} |")
    return "\n".join(lines)
