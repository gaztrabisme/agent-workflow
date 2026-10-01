#!/usr/bin/env python3
"""Require each quotation to match its explicitly cited page after text normalisation.

Usage:
  check_quotes.py --paper <pdf|page-marked txt> --notes <md> [<md> ...]
                  [--freeform] [--min-words 6] [--json <path|->]

Template mode reads markdown tables with a Quote (or Copied) column and a Page (or Where)
column. Freeform mode reads quoted strings of at least --min-words words and looks for a
page hint on that line. An exact match on a cited page passes. A quote with no page hint,
a near-match, or a match on another page is flagged. Math and symbol-sensitive matches
are marked pass-eye and must be checked on the rendered page before handoff; a math quote
that extraction cannot match is marked eye-check for manual review.

Text is NFKC-normalised, lower-cased, and reduced to letters and digits. This makes
spacing and punctuation differences harmless; symbols that can change a mathematical
claim trigger visual review because this normalisation removes them.

Exit 0 = no flagged or unresolved eye-check rows; 1 = one or more flagged/eye-check rows;
2 = usage or read error. pass-eye rows require human page review before delivery.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_pages import load_pages, squash  # noqa: E402

MATH = re.compile(r'[±×^≲≳≤≥∼≈≠÷∑∏√∞∝∈∉∧∨→←↔☉⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]|\^\{|_\{|\d\s?[-–+*/=<>≤≥:]\s?\d|[α-ωΑ-Ω]')
EYE = re.compile(r'[±≲≳≤≥<>!=≈≠÷∑∏√∞∝∈∉→←↔☉]|\d\s?:\s?\d')
EYE_REASON = 'symbols may be lost during text extraction; confirm on the rendered page'
PAGE_HINT = re.compile(
    r'(?:\bpp?\.?\s?|\bpages?\s|printed pages?\s|\bp(?=\d))(\d{1,2})(?:\s?[-–]\s?(\d{1,2}))?\b', re.I)
QUOTED = re.compile(r'“([^”]+?)”|"([^"\n]+?)"')


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
    """Rows from markdown tables that have a quote and page/where column."""
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
            if piece and not set(piece) <= set(':- '):
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
    ap.add_argument('--extra', nargs='*', default=[],
                    help='accepted for ceric_check compatibility; extra sources cannot verify a paper quote')
    ap.add_argument('--min-words', type=int, default=6)
    ap.add_argument('--json')
    a = ap.parse_args()

    try:
        pages = {p: squash(t) for p, t in load_pages(a.paper).items()}
    except SystemExit as e:
        print(e, file=sys.stderr)
        return 2
    if not pages:
        print('no pages found in source', file=sys.stderr)
        return 2
    max_page = max(pages)
    items = []
    for f in a.notes:
        items += freeform_items(f, max_page, a.min_words) if a.freeform else template_items(f, max_page)
    # Check every occurrence: identical wording with a different page citation still
    # needs its own page check, and symbol variants may normalise to the same letters.
    uniq = items

    rows = []
    counts = {'pass': 0, 'pass-unpinned': 0, 'pass-extra': 0, 'pass-eye': 0, 'eye-check': 0, 'FLAG': 0}
    for f, n, q, hints, ctx in uniq:
        qnorm = squash(q)
        exact = bool(hints and qnorm and qnorm in ''.join(pages.get(p, '') for p in sorted(hints)))
        best_p = max(pages, key=lambda p: int(qnorm in pages[p])) if qnorm else min(pages)
        best_exact = bool(qnorm and qnorm in pages.get(best_p, ''))
        if exact:
            status = 'pass-eye' if MATH.search(q) or EYE.search(q) else 'pass'
        elif MATH.search(q) or EYE.search(q):
            status = 'eye-check'
        else:
            status = 'FLAG'
        counts[status] += 1
        rows.append({'file': os.path.basename(f), 'line': n, 'status': status,
                     'stated_pages': sorted(hints), 'exact_stated_page_match': exact,
                     'best_page': best_p, 'best_page_match': best_exact,
                     'quote': q[:140], 'context': ctx})

    total = len(rows)
    pinned = sum(1 for r in rows if r['stated_pages'])
    print(f"quotes checked: {total}  exact-page pass: {counts['pass']}  pass-eye: {counts['pass-eye']}  "
          f"eye-check: {counts['eye-check']}  FLAG: {counts['FLAG']}  | page hints on {pinned}/{total} quotes")
    for r in rows:
        if r['status'] in ('FLAG', 'eye-check', 'pass-eye'):
            tail = f'  ({EYE_REASON})' if r['status'] in ('eye-check', 'pass-eye') else ''
            print(f"  [{r['status']}] {r['file']}:{r['line']} stated={r['stated_pages'] or '-'} "
                  f"exact-on-stated={r['exact_stated_page_match']} best=p{r['best_page']} "
                  f"exact-on-best={r['best_page_match']} :: {r['quote'][:110]}{tail}")
    if a.json:
        out = json.dumps({'summary': counts, 'total': total, 'pinned': pinned, 'rows': rows}, indent=1,
                         ensure_ascii=False)
        if a.json == '-':
            print('---JSON---')
            print(out)
        else:
            with open(a.json, 'w', encoding='utf-8') as handle:
                handle.write(out)
    return 1 if counts['FLAG'] or counts['eye-check'] else 0


if __name__ == '__main__':
    sys.exit(main())
