#!/usr/bin/env python3
"""Summarize an explicitly supplied, harness-neutral evolution trace manifest.

Manifest JSONL records use: skill, task_id, date (YYYY-MM-DD), event
(invoke/read/friction/change), and optional detail. The helper reports evidence;
it does not select skills or make verdicts.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ENTRY = re.compile(r"^## (?:Evolution\s+\d+|Round\s+\d+|Birth)\b.*?(\d{4}-\d{2}-\d{2})", re.I)
PENDING = re.compile(r"\bPENDING\b", re.I)
UNCHECKED = re.compile(r"^\s*-\s+\[ \]", re.I)
EVENTS = {"invoke", "read", "friction", "change"}


def ledger_state(skill_dir: Path) -> tuple[date | None, int, int]:
    path = skill_dir / "EVOLUTION.md"
    if not path.is_file():
        return None, 0, 0
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    entries = [(i, ENTRY.match(line)) for i, line in enumerate(lines)]
    entries = [(i, m) for i, m in entries if m]
    if not entries:
        return None, 0, 0
    start, match = entries[-1]
    try:
        since = date.fromisoformat(match.group(1))
    except ValueError:
        since = None
    body = lines[start:]
    return since, sum(bool(UNCHECKED.match(line)) for line in body), sum(bool(PENDING.search(line)) for line in body)


def read_manifest(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8", errors="replace") as stream:
        for line_no, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
            required = ("skill", "task_id", "date", "event")
            if not all(row.get(key) for key in required):
                raise ValueError(f"{path}:{line_no}: require skill, task_id, date, and event")
            if row["event"] not in EVENTS:
                raise ValueError(f"{path}:{line_no}: event must be one of {', '.join(sorted(EVENTS))}")
            try:
                row["_date"] = date.fromisoformat(row["date"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{path}:{line_no}: date must be YYYY-MM-DD") from exc
            rows.append(row)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="directory containing skill directories")
    parser.add_argument("--traces", required=True, type=Path, help="explicit JSONL trace manifest")
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error(f"not a directory: {args.root}")
    if not args.traces.is_file():
        parser.error(f"not a file: {args.traces}")

    try:
        traces = read_manifest(args.traces)
    except (OSError, ValueError) as exc:
        print(f"triage: {exc}", file=sys.stderr)
        return 2

    skills = sorted(p for p in args.root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    data = defaultdict(lambda: {"invoke": set(), "read": set(), "friction": [], "change": []})
    for row in traces:
        state = data[row["skill"]]
        skill_dir = args.root / row["skill"]
        since, _, _ = ledger_state(skill_dir)
        if since and row["_date"] <= since:
            continue
        event = row["event"]
        if event in ("invoke", "read"):
            state[event].add(row["task_id"])
        else:
            state[event].append((row["date"], row.get("detail", "")))

    print("# Evolution triage")
    print(f"\n- Skill root: `{args.root}`")
    print(f"- Trace manifest: `{args.traces}`")
    print("- Independence unit: distinct `task_id`; invocation and read evidence remain separate.")
    print("- This table supports a decision; it does not choose or rank the skills.\n")
    print("| Skill | Last entry | Invoked tasks | Read tasks | Open items | PENDING | Friction | Changes | Trace gate |")
    print("|---|---|---:|---:|---:|---:|---:|---:|---|")
    for skill in skills:
        since, unchecked, pending = ledger_state(skill)
        row = data[skill.name]
        eligible = bool(row["invoke"] or row["read"])
        print(f"| `{skill.name}` | {since or 'no entry'} | {len(row['invoke'])} | {len(row['read'])} | "
              f"{unchecked} | {pending} | {len(row['friction'])} | {len(row['change'])} | "
              f"{'evidence present' if eligible else 'excluded: no post-entry task'} |")
    print("\n## Trace details")
    for skill in skills:
        row = data[skill.name]
        details = row["friction"] + row["change"]
        if details:
            print(f"\n### `{skill.name}`")
            for when, detail in details[:5]:
                print(f"- {when}: {detail or '(no detail supplied)'}")
    print("\nSelect by impact, effort, evidence quality and review capacity. State one trace for every pick and a reason for every skip.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
