#!/usr/bin/env python3
"""Check that every quotation in CERIC notes exists in the source, on the page the notes say it does.

Usage:
  check_quotes.py --paper <pdf|page-marked txt> --notes <md> [<md> ...]
                  [--freeform] [--extra <pdf|txt> ...] [--threshold 0.85] [--window 1]
                  [--min-words 6] [--json <path|->]

Template mode (default) reads markdown tables that have a `Quote` (or `Copied`) column and a `Page`
(or `Where`) column - the shape of this skill's ceric-notes.md template.
Freeform mode (--freeform) takes every quoted string of >= --min-words words in the files, "..." or
“...”, and looks for a page hint on the same line (p. 7 / pp. 7-8 / page 7 / printed page 7). A quote
with no hint is searched on every page and counted as "unpinned": it may be genuine, but nobody can
verify it without re-reading the whole document.

Scoring (the Opus run's checker, kept): text is NFKC-normalised, lower-cased and reduced to [a-z0-9];
the quote is cut into 10-character chunks; the score is the share of chunks found on the stated
page(s) +/- window. >= threshold passes. A failing quote that carries math symbols (± × ^ ≲ ≳ ∼ ☉,
superscripts) goes to an eye-check bucket rather than a flag: extraction scrambles those, so a rendered
page decides. A passing quote that carries a ratio (digits:digits), ±, ≳, ≲, <, > or ☉ is also listed,
as pass-eye: squash() strips exactly those symbols, so "≳10:1" and "10:1" verify identically and a
dropped symbol inverts the claim. pass-eye rows still exit 0; each one asks for a look at the rendered
page. --extra sources (the packet, say) rescue a quote that is not in the paper but is in them.

Exit 0 = nothing flagged; 1 = flagged quotes; 2 = usage or read error.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_pages import load_pages, squash  # noqa: E402

CHUNK = 10
MATH = re.compile(r'[±×^≲≳∼☉⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]|\^\{|_\{|\d\s?[-–+]\s?\d')
# symbols squash() deletes, so a quote carrying them can pass with the symbol gone
EYE = re.compile(r'[±≲≳<>☉]|\d\s?:\s?\d')
EYE_REASON = 'symbols may have been dropped by extraction; confirm on the rendered page'
PAGE_HINT = re.compile(
    r'(?:\bpp?\.?\s?|\bpages?\s|printed pages?\s|\bp(?=\d))(\d{1,2})(?:\s?[-–]\s?(\d{1,2}))?\b', re.I)
QUOTED = re.compile(r'“([^”]+?)”|"([^"\n]+?)"')


def score(quote: str, hay: str) -> float:
    q = squash(quote)
    if len(q) < CHUNK:
        return 1.0 if q and q in hay else 0.0
    chunks = [q[i:i + CHUNK] for i in range(0, len(q) - CHUNK + 1, CHUNK)]
    return sum(c in hay for c in chunks) / len(chunks)


def page_hints(text: str, max_page: int):
    pages = set()
    for a, b in PAGE_HINT.findall(text):
        lo, hi = int(a), int(b or a)
        if 1 <= lo <= max_page and lo <= hi <= max_page and hi - lo <= 3:
            pages.update(range(lo, hi + 1))
    return pages


def split_row(line: str):
    return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def template_items(path: str, max_page: int):
    """Rows of markdown tables with a quote column and a page/where column."""
    items, header = [], None
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.lstrip().startswith('|'):
            header = None
            continue
        cells = split_row(line)
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if all(set(c) <= set(':- ') for c in cells):
            continue
        qi = next((i for i, h in enumerate(header) if 'quote' in h or 'copied' in h), None)
        pi = next((i for i, h in enumerate(header) if 'page' in h or 'where' in h), None)
        if qi is None or qi >= len(cells):
            continue
        where = cells[pi] if pi is not None and pi < len(cells) else ''
        for piece in re.split(r'<br\s*/?>|\n', cells[qi]):
            piece = piece.strip().strip('“”"\'')
            if len(piece.split()) >= 1 and piece and not set(piece) <= set(':- '):
                items.append((path, n, piece, page_hints(where, max_page), where))
    return items


def freeform_items(path: str, max_page: int, min_words: int):
    items = []
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        hints = page_hints(line, max_page)
        for m in QUOTED.finditer(line):
            q = (m.group(1) or m.group(2)).strip()
            if len(q.split()) >= min_words:
                items.append((path, n, q, hints, line.strip()[:80]))
    return items


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--paper', required=True)
    ap.add_argument('--notes', nargs='+', required=True)
    ap.add_argument('--freeform', action='store_true')
    ap.add_argument('--extra', nargs='*', default=[])
    ap.add_argument('--threshold', type=float, default=0.85)
    ap.add_argument('--window', type=int, default=1)
    ap.add_argument('--min-words', type=int, default=6)
    ap.add_argument('--json')
    a = ap.parse_args()

    try:
        pages = {p: squash(t) for p, t in load_pages(a.paper).items()}
        extras = {os.path.basename(x): squash(''.join(load_pages(x).values())) for x in a.extra}
    except SystemExit as e:
        print(e, file=sys.stderr)
        return 2
    max_page = max(pages)
    whole = ''.join(pages[p] for p in sorted(pages))

    items = []
    for f in a.notes:
        items += freeform_items(f, max_page, a.min_words) if a.freeform else template_items(f, max_page)
    seen, uniq = set(), []
    for it in items:
        k = (it[0], squash(it[2]))
        if k not in seen:
            seen.add(k)
            uniq.append(it)

    rows, counts = [], {'pass': 0, 'pass-unpinned': 0, 'pass-extra': 0, 'pass-eye': 0, 'eye-check': 0, 'FLAG': 0}
    for f, n, q, hints, ctx in uniq:
        best_p, best_s = max(((p, score(q, h)) for p, h in pages.items()), key=lambda x: x[1])
        if hints:
            near = set()
            for p in hints:
                near.update(range(p - a.window, p + a.window + 1))
            s_stated = score(q, ''.join(pages.get(p, '') for p in sorted(near)))
        else:
            s_stated = None
        if hints and s_stated >= a.threshold:
            status = 'pass'
        elif not hints and best_s >= a.threshold:
            status = 'pass-unpinned'
        else:
            extra_hit = next((name for name, h in extras.items() if score(q, h) >= a.threshold), None)
            if extra_hit:
                status = 'pass-extra'
            elif MATH.search(q) and best_s >= 0.5:
                status = 'eye-check'
            else:
                status = 'FLAG'
        if status in ('pass', 'pass-unpinned', 'pass-extra') and EYE.search(q):
            status = 'pass-eye'
        counts[status] += 1
        rows.append({'file': os.path.basename(f), 'line': n, 'status': status, 'stated_pages': sorted(hints),
                     'score_stated': None if s_stated is None else round(s_stated, 2),
                     'best_page': best_p, 'best_score': round(best_s, 2), 'quote': q[:140], 'context': ctx})

    total = len(rows)
    pinned = sum(1 for r in rows if r['stated_pages'])
    print(f"quotes checked: {total}  pass: {counts['pass']}  pass-unpinned: {counts['pass-unpinned']}  "
          f"pass-extra: {counts['pass-extra']}  pass-eye: {counts['pass-eye']}  eye-check: {counts['eye-check']}  "
          f"FLAG: {counts['FLAG']}  | page hints on {pinned}/{total} quotes  | threshold {a.threshold}, window ±{a.window}")
    for r in rows:
        if r['status'] in ('FLAG', 'eye-check', 'pass-eye'):
            tail = f'  ({EYE_REASON})' if r['status'] == 'pass-eye' else ''
            print(f"  [{r['status']}] {r['file']}:{r['line']} stated={r['stated_pages'] or '-'} "
                  f"s={r['score_stated']} best=p{r['best_page']}@{r['best_score']} :: {r['quote'][:110]}{tail}")
    if a.json:
        out = json.dumps({'summary': counts, 'total': total, 'pinned': pinned, 'rows': rows}, indent=1,
                         ensure_ascii=False)
        if a.json == '-':
            print('---JSON---')
            print(out)
        else:
            open(a.json, 'w', encoding='utf-8').write(out)
    return 1 if counts['FLAG'] else 0


if __name__ == '__main__':
    sys.exit(main())
