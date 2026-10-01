#!/usr/bin/env python3
"""Check quoted text at an explicit page, line, or section in its named source.

Usage:
  check_quotes.py (--paper <pdf|txt> | --source <alias=path> ...)
                  --notes <md> [<md> ...] [--freeform] [--extra <path> ...]
                  [--min-words 6] [--json <path|->]

Template mode reads markdown tables with a Quote (or Copied) column, a Page (or Where)
column, and optionally a Source column. With one configured source, Source may be omitted.
With multiple sources, every row must name its source alias. Freeform rows may include
`Source: alias` plus a page, line, or section locator on the quoted line.

Page sources are PDFs or page-marked text files. Plain text and markdown sources use
`L12` / `L12-L15` or `§ Heading` locators. A locator is required: an unmarked text file is
not treated as an informative `p1`. Text is NFKC-normalised, lower-cased, and reduced to
letters and digits for matching. Symbol-sensitive matches remain pass-eye and need a
human check against the original rendered page, or a character-by-character check against
the authoritative text when the source has no rendered form.

Exit 0 = no flagged or unresolved eye-check rows; 1 = one or more flagged/eye-check rows;
2 = usage or read error. pass-eye rows require human review before delivery.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_pages import MARK, load_pages, squash  # noqa: E402

MATH = re.compile(r'[±×^≲≳≤≥∼≈≠÷∑∏√∞∝∈∉∧∨→←↔☉⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]|\^\{|_\{|\d\s?[-–+*/=<>≤≥:]\s?\d|[α-ωΑ-Ω]')
EYE = re.compile(r'[±≲≳≤≥<>!=≈≠÷∑∏√∞∝∈∉→←↔☉]|\d\s?:\s?\d')
EYE_REASON = 'symbol-sensitive text needs human review against the original source'
PAGE_HINT = re.compile(
    r'(?:\bpp?\.?\s?|\bpages?\s|printed pages?\s|\bp(?=\d))(\d{1,2})(?:\s?[-–]\s?(\d{1,2}))?\b', re.I)
LINE_HINT = re.compile(r'^\s*(?:l(?:ines?)?\s*)?(\d+)(?:\s*[-–]\s*(?:l(?:ines?)?\s*)?(\d+))?\s*$', re.I)
LINE_PREFIX = re.compile(r'^\s*(?:l(?:ines?)?\s*)?(\d+)(?:\s*[-–]\s*(?:l(?:ines?)?\s*)?(\d+))?\b', re.I)
SECTION_HINT = re.compile(r'^\s*(?:§|section\s+)(.+?)\s*$', re.I)
QUOTED = re.compile(r'“([^”]+?)”|"([^"\n]+?)"')
HEADING = re.compile(r'^(#{1,6})\s+(.+?)\s*#*\s*$', re.M)


def page_hints(text: str, max_page: int):
    pages = set()
    for a, b in PAGE_HINT.findall(text):
        lo, hi = int(a), int(b or a)
        if 1 <= lo <= max_page and lo <= hi <= max_page and hi - lo <= 3:
            pages.update(range(lo, hi + 1))
    return pages


def split_row(line: str):
    return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def template_items(path: str):
    """Read quote, source, and locator cells from markdown tables."""
    items, header = [], None
    with open(path, encoding='utf-8') as handle:
        for n, line in enumerate(handle, 1):
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
            si = next((i for i, h in enumerate(header) if h == 'source' or h.startswith('source ')), None)
            if qi is None or qi >= len(cells):
                continue
            where = cells[pi] if pi is not None and pi < len(cells) else ''
            source = cells[si] if si is not None and si < len(cells) else ''
            for piece in re.split(r'<br\s*/?>|\n', cells[qi]):
                piece = piece.strip().strip('“”"\'')
                if piece and not set(piece) <= set(':- '):
                    items.append((path, n, piece, source, where, where))
    return items


def freeform_items(path: str, min_words: int):
    items = []
    with open(path, encoding='utf-8') as handle:
        for n, line in enumerate(handle, 1):
            source_match = re.search(r'\bSource\s*:\s*([^;|]+)', line, re.I)
            source = source_match.group(1).strip() if source_match else ''
            where_match = re.search(r'\bWhere\s*:\s*([^;|]+)', line, re.I)
            if where_match:
                where = where_match.group(1).strip()
            else:
                locator_match = LINE_PREFIX.search(line) or SECTION_HINT.search(line) or PAGE_HINT.search(line)
                where = locator_match.group(0).strip() if locator_match else ''
            for m in QUOTED.finditer(line):
                q = (m.group(1) or m.group(2)).strip()
                if len(q.split()) >= min_words:
                    items.append((path, n, q, source, where, line.strip()[:100]))
    return items


def load_source(alias: str, path: str):
    if not os.path.isfile(path):
        raise OSError(f'{alias}: source file not found: {path}')
    if path.lower().endswith('.pdf'):
        return {'alias': alias, 'path': path, 'kind': 'page', 'pages': load_pages(path)}
    with open(path, encoding='utf-8') as handle:
        raw = handle.read()
    if MARK.search(raw):
        return {'alias': alias, 'path': path, 'kind': 'page', 'pages': load_pages(path)}
    return {'alias': alias, 'path': path, 'kind': 'text', 'raw': raw}


def source_aliases(sources):
    aliases = {}
    ambiguous = set()
    for key, source in sources.items():
        candidates = {key.casefold(), os.path.basename(source['path']).casefold(),
                      os.path.splitext(os.path.basename(source['path']))[0].casefold()}
        for candidate in candidates:
            if candidate in aliases and aliases[candidate] != key:
                ambiguous.add(candidate)
            else:
                aliases[candidate] = key
    for candidate in ambiguous:
        aliases[candidate] = None
    return aliases


def text_scope(source, where):
    raw = source['raw']
    lines = raw.splitlines()
    line_match = LINE_HINT.fullmatch(where.strip())
    if line_match:
        start, end = int(line_match.group(1)), int(line_match.group(2) or line_match.group(1))
        if start < 1 or end < start or end > len(lines):
            return None, 'line locator is outside the source'
        return '\n'.join(lines[start - 1:end]), f'L{start}-L{end}' if end != start else f'L{start}'

    section_match = SECTION_HINT.fullmatch(where.strip())
    if section_match:
        wanted = squash(section_match.group(1))
        headings = list(HEADING.finditer(raw))
        for index, heading in enumerate(headings):
            title = re.sub(r'\s*#+\s*$', '', heading.group(2)).strip()
            if squash(title) != wanted:
                continue
            level = len(heading.group(1))
            end = len(raw)
            for next_heading in headings[index + 1:]:
                if len(next_heading.group(1)) <= level:
                    end = next_heading.start()
                    break
            return raw[heading.end():end], f'§ {title}'
        return None, 'section heading not found'
    return None, 'text source needs an L12/L12-L15 or § Heading locator'


def source_scope(source, where):
    if source['kind'] == 'page':
        max_page = max(source['pages']) if source['pages'] else 0
        pages = page_hints(where, max_page)
        if not pages:
            return None, [], 'page source needs a valid pN or ppN-N locator'
        return '\n'.join(source['pages'][p] for p in sorted(pages)), sorted(pages), ''
    scope, display = text_scope(source, where)
    return scope, display, '' if scope is not None else display


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--paper', help='single primary PDF or page-marked text source (alias: paper)')
    ap.add_argument('--source', action='append', default=[], metavar='ALIAS=PATH',
                    help='repeat to configure a named source for per-row Source cells')
    ap.add_argument('--notes', nargs='+', required=True)
    ap.add_argument('--freeform', action='store_true')
    ap.add_argument('--extra', nargs='*', default=[], help='additional sources; aliases are file name and stem')
    ap.add_argument('--min-words', type=int, default=6)
    ap.add_argument('--json')
    a = ap.parse_args()

    configs = {}
    extra_aliases = set()
    if a.paper:
        configs['paper'] = a.paper
    try:
        for spec in a.source:
            if '=' not in spec:
                raise ValueError(f'--source must be ALIAS=PATH: {spec}')
            alias, path = spec.split('=', 1)
            if not alias.strip() or not path.strip():
                raise ValueError(f'--source must be ALIAS=PATH: {spec}')
            configs[alias.strip()] = path.strip()
        for path in a.extra:
            base = os.path.basename(path)
            alias = os.path.splitext(base)[0]
            if alias in configs:
                alias = base
            configs[alias] = path
            extra_aliases.add(alias)
        if not configs:
            raise ValueError('provide --paper or at least one --source ALIAS=PATH')
        sources = {alias: load_source(alias, path) for alias, path in configs.items()}
    except (OSError, ValueError, SystemExit) as e:
        print(e, file=sys.stderr)
        return 2
    aliases = source_aliases(sources)

    items = []
    try:
        for f in a.notes:
            items += freeform_items(f, a.min_words) if a.freeform else template_items(f)
    except OSError as e:
        print(e, file=sys.stderr)
        return 2

    rows = []
    counts = {'pass': 0, 'pass-unpinned': 0, 'pass-extra': 0, 'pass-eye': 0, 'eye-check': 0, 'FLAG': 0}
    for f, n, q, source_hint, where, ctx in items:
        source_key = aliases.get(source_hint.casefold()) if source_hint else None
        if not source_hint and len(sources) == 1:
            source_key = next(iter(sources))
        source = sources.get(source_key) if source_key else None
        scope, locator, locator_error = source_scope(source, where) if source else (None, [], 'source alias missing or ambiguous')
        qnorm = squash(q)
        exact = bool(scope is not None and qnorm and qnorm in squash(scope))
        if not source or locator_error:
            status = 'FLAG'
            reason = locator_error or 'source alias not found'
        elif exact:
            status = 'pass-eye' if MATH.search(q) or EYE.search(q) else ('pass-extra' if source_key in extra_aliases else 'pass')
            reason = ''
        elif MATH.search(q) or EYE.search(q):
            status = 'eye-check'
            reason = EYE_REASON
        else:
            status = 'FLAG'
            reason = 'quote is not an exact normalized match at the stated locator'
        counts[status] += 1
        page_match = source['kind'] == 'page' if source else False
        best_page = None
        best_exact = False
        if page_match and qnorm:
            best_page = max(source['pages'], key=lambda p: int(qnorm in squash(source['pages'][p])))
            best_exact = qnorm in squash(source['pages'][best_page])
        rows.append({'file': os.path.basename(f), 'line': n, 'status': status,
                     'source': source_key, 'locator': locator if source and not locator_error else where,
                     'locator_error': reason, 'stated_pages': locator if page_match and not locator_error else [],
                     'exact_stated_page_match': exact if page_match else None,
                     'exact_locator_match': exact, 'best_page': best_page,
                     'best_page_match': best_exact, 'quote': q[:140], 'context': ctx})

    total = len(rows)
    pinned = sum(1 for r in rows if r['source'] and r['locator'] and not r['locator_error'])
    exact_pass = counts['pass'] + counts['pass-extra']
    print(f"quotes checked: {total}  exact-locator pass: {exact_pass}  pass-eye: {counts['pass-eye']}  "
          f"eye-check: {counts['eye-check']}  FLAG: {counts['FLAG']}  | source+locator on {pinned}/{total} quotes")
    for r in rows:
        if r['status'] in ('FLAG', 'eye-check', 'pass-eye'):
            tail = f"  ({r['locator_error']})" if r['locator_error'] else ''
            print(f"  [{r['status']}] {r['file']}:{r['line']} source={r['source'] or r['context']} "
                  f"where={r['locator'] or '-'} exact={r['exact_locator_match']} :: {r['quote'][:110]}{tail}")
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
