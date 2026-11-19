"""Summarize locally rendered index files against a PR base revision."""

import csv
import html
import io
from pathlib import Path
import subprocess
import sys


def git(*args):
    return subprocess.check_output(["git", *args], encoding="utf-8")


def projects(contents):
    return {row["repo"].lower(): row for row in csv.DictReader(io.StringIO(contents, newline=""))}


def preview(base):
    csv_path = Path("data/projects.csv")
    before = projects(git("show", f"{base}:{csv_path}"))
    with csv_path.open(encoding="utf-8", newline="") as current:
        after = projects(current.read())
    added = len(after.keys() - before.keys())
    removed = len(before.keys() - after.keys())
    updated = sum(after[key] != before[key] for key in before.keys() & after.keys())
    print("## Generated index preview\n")
    print(f"Projects added: {added} · updated: {updated} · removed: {removed}")
    for path in ("README.md", str(csv_path)):
        diff = git("diff", "--no-ext-diff", "--no-color", "--unified=0", base, "--", path)
        print(f"\n### {path}\n")
        if not diff:
            print("No changes.")
            continue
        # Only display content from diff hunks. Show bounded, escaped snippets of untrusted project text.
        lines = []
        in_hunk = False
        for line in diff.splitlines():
            if line.startswith("@@"):
                in_hunk = True
            elif in_hunk and line.startswith(("+", "-")):
                lines.append(line)
        additions = sum(line.startswith("+") for line in lines)
        print(f"{additions} lines added · {len(lines) - additions} removed\n")
        print("<pre>")
        for line in lines[:12]:
            print(html.escape(line[:240]) + ("…" if len(line) > 240 else ""))
        print("</pre>")
        if len(lines) > 12:
            print(f"\nShowing 12 of {len(lines)} changed lines.")


if __name__ == "__main__":
    preview(sys.argv[1])
