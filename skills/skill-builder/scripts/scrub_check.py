#!/usr/bin/env python3
"""Pre-publication denylist gate for a skill repo going public.

Zero hits required before any push. Checks the working tree and, with --history,
every blob in git history — because a scrubbed working tree above a dirty history
publishes the dirty history.

Usage:
    scrub_check.py <repo_path> [--denylist FILE] [--history]

Denylist file format (default: <repo>/.scrub-denylist):
    # comment lines and blanks ignored
    <regex> | <label>
    \bACME\b            | client abbrev
    Contoso             | client name
    ~ \bChris\b         | teammate   <- leading "~" makes it SOFT (reported, not fatal)

Word-bound short tokens (\b...\b) or they will match inside innocent words —
e.g. a name like "Ann" matches inside every "announcement". Unbounded short
tokens produce a false-positive flood that trains you to ignore the tool.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

# Always fatal, regardless of the per-skill denylist. If a public repo carries
# private engagement traces, the fact that they EXIST is itself the disclosure —
# it tells readers a systematic client-harvest archive is out there.
ALWAYS = [
    (r"held privately", "trace linkage"),
    (r"private trace", "trace linkage"),
    (r"trace repo", "trace linkage"),
    (r"-traces\b", "trace repo name"),
]

TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".sh", ".toml"}


def load_denylist(path: Path):
    hard, soft = list(ALWAYS), []
    if not path.exists():
        return hard, soft
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        is_soft = line.startswith("~")
        if is_soft:
            line = line[1:].strip()
        pat, _, label = (p.strip() for p in line.partition("|"))
        entry = (pat, label or "denylisted")
        (soft if is_soft else hard).append(entry)
    return hard, soft


def scan(text, source, patterns):
    hits = []
    lines = text.splitlines()
    for pat, label in patterns:
        try:
            rx = re.compile(pat, re.IGNORECASE)
        except re.error as e:
            print(f"!! bad regex {pat!r}: {e}", file=sys.stderr)
            continue
        for m in rx.finditer(text):
            n = text[: m.start()].count("\n") + 1
            ctx = lines[n - 1].strip()[:110] if n <= len(lines) else ""
            hits.append((source, n, label, m.group(0), ctx))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", type=Path)
    ap.add_argument("--denylist", type=Path, default=None)
    ap.add_argument("--history", action="store_true",
                    help="also scan every blob in git history (required before first push)")
    args = ap.parse_args()

    repo = args.repo.resolve()
    deny_path = args.denylist or (repo / ".scrub-denylist")
    hard_pats, soft_pats = load_denylist(deny_path)
    if not deny_path.exists():
        print(f"~~ no denylist at {deny_path} — running with built-in linkage rules only")

    hard, soft, scanned = [], [], 0
    for f in sorted(repo.rglob("*")):
        if not f.is_file() or ".git/" in str(f) or f.suffix not in TEXT_SUFFIXES:
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        rel = str(f.relative_to(repo))
        hard += scan(text, rel, hard_pats)
        soft += scan(text, rel, soft_pats)
        scanned += 1

    if args.history:
        try:
            log = subprocess.run(["git", "-C", str(repo), "log", "--all", "-p"],
                                 capture_output=True, text=True, timeout=300).stdout
            hard += scan(log, "GIT-HISTORY", hard_pats)
        except Exception as e:
            print(f"XX history scan failed: {e}")
            sys.exit(2)

    if soft:
        print(f"~~ {len(soft)} SOFT hits (review; may be legitimate):")
        for s, n, lab, tok, ctx in soft:
            print(f"   {s}:{n}  [{lab}]  {tok!r}  | {ctx}")
        print()

    if hard:
        print(f"XX FAIL — {len(hard)} denylist hits:")
        for s, n, lab, tok, ctx in hard:
            print(f"   {s}:{n}  [{lab}]  {tok!r}  | {ctx}")
        print("\nDo not push. Scrub, then re-run.")
        sys.exit(1)

    scope = f"{scanned} files" + (" + full git history" if args.history else "")
    print(f"OK — 0 denylist hits across {scope}")
    if not args.history:
        print("   NOTE: history not scanned. Re-run with --history before the first push.")


if __name__ == "__main__":
    main()
