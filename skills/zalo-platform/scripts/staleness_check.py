#!/usr/bin/env python3
"""Diff a fresh crawl against the shipped corpus and say which CITATIONS to re-read.

The point is not "what changed on the internet" — it is "which claims in this
skill's references are now standing on moved ground". So the report is organised
around the corpus files that digests cite, and it flags the pricing/policy pages
loudest because those are the ones that reach a client quote.

Usage:
    crawl_zalo.py --out /tmp/zalo-new           # 1. fresh crawl elsewhere
    staleness_check.py --new /tmp/zalo-new      # 2. what moved
    staleness_check.py --new /tmp/zalo-new --diff text/solutions/...txt   # 3. read it
    staleness_check.py --new /tmp/zalo-new --promote                      # 4. adopt

`--promote` overwrites the shipped corpus with the fresh crawl. Do it only after
the changed pages have been read and the affected digests updated — otherwise the
evidence for the edits you still owe is gone.
"""
from __future__ import annotations

import argparse
import difflib
import json
import shutil
import sys
from pathlib import Path

KB = Path(__file__).resolve().parent.parent / "references" / "knowledge-base"
REFS = Path(__file__).resolve().parent.parent / "references"

# Pages whose content is money or policy. A change here is never cosmetic.
HOT = (
    "pricing", "bang-gia", "chinh-sach", "policy", "dieu-khoan", "terms",
    "han-muc", "quota", "tin-nhan/tong-quan", "tuong-tac",
)


def load(root: Path) -> dict[str, dict]:
    m = root / "manifest.json"
    if not m.exists():
        sys.exit(f"no manifest at {m}")
    out = {}
    for r in json.load(m.open(encoding="utf-8")):
        if r.get("text"):
            out[r["text"]] = r
    return out


def body(root: Path, rel: str) -> list[str]:
    """Content lines, normalised so extractor quirks don't read as content change.

    Two crawls of an unchanged page differ in blank-line placement and in whether
    inline elements got joined ("Bắt đầuTài liệuFAQ" vs three lines) — artefacts
    of HTML-to-text, not of Zalo changing anything. Left raw, every page looks
    changed and the report is noise. So: strip, collapse whitespace, drop blanks.
    """
    p = root / rel
    if not p.exists():
        return []
    out = []
    for ln in p.read_text(encoding="utf-8").splitlines()[3:]:
        ln = " ".join(ln.split())
        if ln:
            out.append(ln)
    return out


def words(lines: list[str]) -> list[str]:
    """Word stream — immune to how the extractor happened to break lines."""
    return " ".join(lines).split()


def drift(old: list[str], new: list[str]) -> tuple[int, float]:
    """(words changed, similarity 0..1) between two normalised bodies."""
    a, b = words(old), words(new)
    if not a and not b:
        return 0, 1.0
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    same = sum(bl.size for bl in sm.get_matching_blocks())
    return (len(a) - same) + (len(b) - same), sm.ratio()


def is_hot(rel: str, url: str) -> bool:
    hay = (rel + " " + url).lower()
    return any(h in hay for h in HOT)


def cited_by(rel: str) -> list[str]:
    """Which reference digests cite this corpus file."""
    hits = []
    for md in sorted(REFS.glob("*.md")):
        try:
            if rel in md.read_text(encoding="utf-8"):
                hits.append(md.name)
        except OSError:
            continue
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--new", type=Path, required=True, help="root of the fresh crawl")
    ap.add_argument("--old", type=Path, default=KB, help=f"shipped corpus (default {KB})")
    ap.add_argument("--diff", metavar="RELPATH", help="print the unified diff for one file")
    ap.add_argument("--threshold", type=int, default=4, help="ignore drift under N words (default 4)")
    ap.add_argument("--promote", action="store_true", help="replace the shipped corpus with --new")
    args = ap.parse_args()

    old, new = load(args.old), load(args.new)

    if args.diff:
        d = difflib.unified_diff(
            body(args.old, args.diff), body(args.new, args.diff),
            fromfile=f"OLD {args.diff}", tofile=f"NEW {args.diff}", lineterm="",
        )
        print("\n".join(d) or "(no textual difference)")
        return 0

    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed: list[tuple[str, int, bool]] = []
    for rel in sorted(set(old) & set(new)):
        o, n = body(args.old, rel), body(args.new, rel)
        if o == n:
            continue
        delta, _ratio = drift(o, n)
        if delta >= args.threshold:
            changed.append((rel, delta, is_hot(rel, new[rel]["url"])))

    hot = [c for c in changed if c[2]]
    cold = [c for c in changed if not c[2]]

    print(f"corpus: {len(old)} old · {len(new)} new")
    print(f"changed {len(changed)} · new {len(added)} · gone {len(removed)}\n")

    if hot:
        print("!! PRICING / POLICY CHANGED — re-read before any quote or commitment")
        for rel, delta, _ in sorted(hot, key=lambda c: -c[1]):
            cites = cited_by(rel)
            print(f"  ~{delta:5d} words  {rel}")
            print(f"              {new[rel]['url']}")
            if cites:
                print(f"              cited by: {', '.join(cites)}  <-- UPDATE THESE")
        print()

    if cold:
        print(f"Other changed pages ({len(cold)}):")
        for rel, delta, _ in sorted(cold, key=lambda c: -c[1])[:30]:
            cites = cited_by(rel)
            tag = f"  [cited by {', '.join(cites)}]" if cites else ""
            print(f"  ~{delta:5d} words  {rel}{tag}")
        if len(cold) > 30:
            print(f"  … and {len(cold) - 30} more")
        print()

    if added:
        print(f"NEW pages ({len(added)}) — new docs often mean a new product or policy:")
        for rel in added[:30]:
            print(f"  + {new[rel]['url']}")
        if len(added) > 30:
            print(f"  … and {len(added) - 30} more")
        print()

    if removed:
        print(f"GONE ({len(removed)}) — a retired page can mean a discontinued product:")
        for rel in removed[:30]:
            cites = cited_by(rel)
            tag = f"  [cited by {', '.join(cites)}]  <-- DEAD CITATION" if cites else ""
            print(f"  - {old[rel]['url']}{tag}")
        if len(removed) > 30:
            print(f"  … and {len(removed) - 30} more")
        print()

    if args.promote:
        if args.new.resolve() == args.old.resolve():
            sys.exit("--promote needs --new to differ from --old")
        shutil.rmtree(args.old / "text", ignore_errors=True)
        shutil.copytree(args.new / "text", args.old / "text")
        shutil.copy2(args.new / "manifest.json", args.old / "manifest.json")
        print(f"PROMOTED {args.new} -> {args.old}")
        print("Now update every digest listed under 'cited by' above, and record "
              "the re-research round in EVOLUTION.md.")
    elif changed or added or removed:
        print("Nothing promoted. Read the changed pages (--diff), fix the digests, "
              "then re-run with --promote.")
    else:
        print("No material change. Corpus still current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
