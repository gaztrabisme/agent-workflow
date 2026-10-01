#!/usr/bin/env python3
"""Summarize an explicitly supplied, harness-neutral evolution trace manifest.

Manifest JSONL records use: skill, task_id, date (YYYY-MM-DD), event
(invoke/read/friction/change), and optional detail. Invocation records use
parent_session_id when available; a prose or operations log may use a
documented task_id only with source="log". Rows marked reported=true are kept
separate from measured counts. The helper reports evidence; it does not select
skills or make verdicts.
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
            if "source" in row and not isinstance(row["source"], str):
                raise ValueError(f"{path}:{line_no}: source must be a string")
            if "reported" in row and not isinstance(row["reported"], bool):
                raise ValueError(f"{path}:{line_no}: reported must be true or false")
            if row["event"] == "invoke" and row.get("reported") is not True and not row.get("parent_session_id") and row.get("source") != "log":
                raise ValueError(f"{path}:{line_no}: invoke events require parent_session_id or source=log")
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
    data = defaultdict(lambda: {"invoke_sessions": set(), "log_invocations": set(), "read": set(), "friction": [], "change": [], "reported": []})
    for row in traces:
        state = data[row["skill"]]
        skill_dir = args.root / row["skill"]
        since, _, _ = ledger_state(skill_dir)
        if since and row["_date"] <= since:
            continue
        if row.get("reported") is True:
            state["reported"].append(row)
            continue
        event = row["event"]
        if event == "invoke":
            if row.get("parent_session_id"):
                state["invoke_sessions"].add(row["parent_session_id"])
            else:
                state["log_invocations"].add(row["task_id"])
        elif event == "read":
            state[event].add(row["task_id"])
        else:
            state[event].append((row["date"], row.get("detail", "")))

    print("# Evolution triage")
    print(f"\n- Skill root: `{args.root}`")
    print(f"- Trace manifest: `{args.traces}`")
    print("- Invocation evidence: distinct root session IDs and documented task labels from rows marked `source: log` are reported separately. Parent and child-agent sessions share the root ID. Read evidence remains separate.")
    print("- Rows marked `reported: true` are listed separately and excluded from measured counts.")
    print("- This table supports a decision; it does not choose or rank the skills.\n")
    print("| Skill | Last entry | Invoked parent sessions | Log task labels | Read tasks | Open items | PENDING | Friction | Changes | Trace gate |")
    print("|---|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for skill in skills:
        since, unchecked, pending = ledger_state(skill)
        row = data[skill.name]
        eligible = bool(row["invoke_sessions"] or row["log_invocations"] or row["read"])
        if not (skill / "EVOLUTION.md").is_file():
            open_items, pending_items, gate = "—", "—", "no ledger — counts vacuous"
        else:
            open_items, pending_items = str(unchecked), str(pending)
            gate = "evidence present" if eligible else "excluded: no post-entry task"
        print(f"| `{skill.name}` | {since or 'no entry'} | {len(row['invoke_sessions'])} | {len(row['log_invocations'])} | {len(row['read'])} | "
              f"{open_items} | {pending_items} | {len(row['friction'])} | {len(row['change'])} | {gate} |")
    known_skills = {skill.name for skill in skills}
    unmatched = sorted(set(data) - known_skills)
    if unmatched:
        print("\n## Unmatched manifest skills")
        for name in unmatched:
            print(f"- WARNING: manifest skill `{name}` has no matching skill directory with `SKILL.md` under `{args.root}`; its rows are not in the table.")
    print("\n## Trace details")
    for skill in skills:
        row = data[skill.name]
        details = row["friction"] + row["change"]
        if details:
            shown = min(5, len(details))
            print(f"\n### `{skill.name}` (showing {shown} of {len(details)} friction/change details)")
            for when, detail in details[:shown]:
                print(f"- {when}: {detail or '(no detail supplied)'}")
    reported = [(name, row) for name, state in sorted(data.items()) for row in state["reported"]]
    if reported:
        print("\n## Reported traces (not included in measured counts)")
        for name, row in reported:
            source = row.get("source", "unspecified")
            detail = row.get("detail", "")
            print(f"- `{name}` {row['date']} {row['event']} — task `{row['task_id']}` — source `{source}` — {detail or '(no detail supplied)'}")
    print("\nSelect by impact, effort, evidence quality and review capacity. State one trace for every pick and a reason for every skip.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
