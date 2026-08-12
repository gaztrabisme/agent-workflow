#!/usr/bin/env python3
"""Search the archived Zalo documentation corpus and return matches WITH citations.

This is the grounding instrument for the `zalo-platform` skill. Every claim the
skill makes about the Zalo platform must trace to a hit from this script — the
output format is designed so the citation is impossible to lose: each hit
carries its source URL and the date that page was fetched.

Usage:
    kb_search.py "48 giờ"                       # search everything
    kb_search.py "getPhoneNumber" -s miniapp    # restrict to one source
    kb_search.py "hạn mức" -C 3 -n 40           # more context, more hits
    kb_search.py -e "\\d+ ?đ/tin"                # regex mode
    kb_search.py --cite text/solutions/foo.txt  # print the citation for a file
    kb_search.py --list-sources
    kb_search.py --stale                        # age of the corpus

Sources: developers (stc-developers.zdn.vn CDN) · solutions (zalo.solutions +
oa.zalo.me) · miniapp (miniapp.zaloplatforms.com) · bot (bot.zapps.me).

Exit codes: 0 hits found · 1 no hits (so callers can branch on "not in corpus",
which is a meaningful answer — see the skill's honesty rule).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import unicodedata
from pathlib import Path

KB = Path(__file__).resolve().parent.parent / "references" / "knowledge-base"
MANIFEST = KB / "manifest.json"


def _load_manifest() -> dict[str, dict]:
    """Map relative text path -> manifest record."""
    if not MANIFEST.exists():
        sys.exit(f"manifest not found: {MANIFEST}")
    return {r["text"]: r for r in json.load(MANIFEST.open(encoding="utf-8"))}


def _fold(s: str) -> str:
    """Casefold + strip Vietnamese diacritics, so 'han muc' finds 'hạn mức'.

    Zalo's docs are Vietnamese; queries get typed both ways. Folding both sides
    means a diacritic-less query still hits. Offsets are preserved because NFD
    combining marks are dropped without touching base characters.
    """
    s = unicodedata.normalize("NFD", s.casefold())
    return "".join(c for c in s if not unicodedata.combining(c))


def citation(rec: dict) -> str:
    return f"[{rec['text']} · {rec['url']} · fetched {rec['fetched']}]"


def _iter_files(sources: list[str] | None, manifest: dict[str, dict]):
    for rel, rec in sorted(manifest.items()):
        if sources:
            if rec["source"] not in sources:
                continue
        # Superseded snapshots are kept so older citations still resolve, but a
        # search must not surface a stale page as if it were current. Opt in
        # explicitly with -s archive-<source>.
        elif rec["source"].startswith("archive-"):
            continue
        path = KB / rel
        if path.exists():
            yield rec, path


def search(
    pattern: str,
    *,
    regex: bool,
    sources: list[str] | None,
    context: int,
    max_hits: int,
    files_only: bool,
) -> int:
    manifest = _load_manifest()
    flags = re.IGNORECASE

    # Plain queries AND their terms rather than matching the phrase literally.
    # The old behaviour was `re.escape(_fold(pattern))` -- one literal substring,
    # on one line -- so any query whose word order or spacing differed from the
    # page missed silently. In the only real consultation this skill has had,
    # 4 of 5 content queries came back empty that way, and one of the misses
    # ("phí duyệt") was written up as a fact not existing. Vietnamese docs
    # interleave these words constantly: the page says "phí" in the price
    # sentence and "duyệt template" in the workflow sentence.
    if regex:
        _rx = re.compile(pattern, flags)
        def matches(ln: str) -> bool:
            return _rx.search(ln) is not None
    else:
        terms = [re.compile(re.escape(_fold(t)), flags) for t in pattern.split()]
        if not terms:                       # whitespace-only query
            terms = [re.compile(re.escape(_fold(pattern)), flags)]
        def matches(ln: str) -> bool:
            folded = _fold(ln)
            return all(t.search(folded) for t in terms)

    hits = 0
    for rec, path in _iter_files(sources, manifest):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        # Lines 1-3 of every text file are the SOURCE/FETCHED/TITLE header the
        # crawler writes. Skip them so a search for a URL fragment doesn't match
        # every file's own header and drown the real hits.
        matched = [i for i, ln in list(enumerate(lines))[3:] if matches(ln)]
        if not matched:
            continue
        if files_only:
            print(f"{len(matched):4d}  {citation(rec)}")
            hits += 1
            if hits >= max_hits:
                break
            continue

        print(f"\n=== {rec['title']}\n    {citation(rec)}")
        for i in matched:
            lo, hi = max(3, i - context), min(len(lines), i + context + 1)
            for j in range(lo, hi):
                mark = ">" if j == i else " "
                print(f"  {mark} {j + 1:5d} | {lines[j]}")
            if context:
                print("    " + "-" * 40)
            hits += 1
            if hits >= max_hits:
                print(f"\n[truncated at {max_hits} hits — raise with -n]")
                return 0
    if not hits:
        print(
            f"NO HITS for {pattern!r}"
            + (f" in source(s) {sources}" if sources else "")
            + "\n\nThis is a retrieval result, not an answer. Before you report the "
            "fact absent, run a second query form:\n"
            "  1. fewer terms, or the one most distinctive term\n"
            "  2. regex, to span wording you did not guess:  -e \"duyệt.{0,40}template\"\n"
            "  3. page level rather than line level:  -l \"<term>\"\n"
            "\nOnly after a second form also comes back empty may you write \"not in "
            "the corpus\" — and then say which queries you ran, so the next reader can "
            "tell a coverage gap from a phrasing miss.\n"
            "\nThis matters because it has already gone wrong: on 2026-08-06 a literal "
            "miss on \"phí duyệt\" was written up as \"Template approval fees — None "
            "found\" and carried into a client cost model. The page was in the corpus; "
            "the query was not the way to reach it.\n"
            "\nCoverage gaps: references/re-research-protocol.md. Never fill the gap "
            "from memory."
        )
        return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pattern", nargs="?", help="text (diacritic-insensitive) or regex with -e")
    ap.add_argument("-e", "--regex", action="store_true", help="treat pattern as a regex")
    ap.add_argument("-s", "--source", action="append", help="developers|solutions|miniapp|bot (repeatable)")
    ap.add_argument("-C", "--context", type=int, default=1, help="context lines (default 1)")
    ap.add_argument("-n", "--max-hits", type=int, default=25, help="max hits (default 25)")
    ap.add_argument("-l", "--files-only", action="store_true", help="list matching pages, not lines")
    ap.add_argument("--cite", metavar="RELPATH", help="print the citation for one corpus file")
    ap.add_argument("--list-sources", action="store_true")
    ap.add_argument("--stale", action="store_true", help="report corpus age")
    args = ap.parse_args()

    manifest = _load_manifest()

    if args.list_sources:
        counts: dict[str, int] = {}
        for r in manifest.values():
            counts[r["source"]] = counts.get(r["source"], 0) + 1
        for s, n in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"{s:12s} {n:4d} pages")
        return 0

    if args.stale:
        dates = sorted({r["fetched"] for r in manifest.values()})
        newest = _dt.date.fromisoformat(dates[-1])
        age = (_dt.date.today() - newest).days
        # Report what a search actually reaches. The old line printed the whole
        # manifest, archives included, which is neither the searchable set nor
        # the number SKILL.md quotes -- three different figures for one corpus.
        live = sum(1 for r in manifest.values() if not r["source"].startswith("archive-"))
        print(f"corpus: {live} searchable pages ({len(manifest)} incl. archived "
              f"snapshots) · fetched {dates[0]}..{dates[-1]} · {age} days old")
        if age > 90:
            print("STALE (>90d) — re-crawl before quoting anything commercial. "
                  "See references/re-research-protocol.md")
        elif age > 30:
            print("AGING (>30d) — verify pricing/policy claims live before quoting.")
        return 0

    if args.cite:
        rec = manifest.get(args.cite) or manifest.get(args.cite.lstrip("./"))
        if not rec:
            print(f"not in manifest: {args.cite}", file=sys.stderr)
            return 1
        print(citation(rec))
        return 0

    if not args.pattern:
        ap.error("pattern required (or use --list-sources / --stale / --cite)")

    return search(
        args.pattern,
        regex=args.regex,
        sources=args.source,
        context=args.context,
        max_hits=args.max_hits,
        files_only=args.files_only,
    )


if __name__ == "__main__":
    sys.exit(main())
