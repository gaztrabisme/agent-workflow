#!/usr/bin/env python3
"""Extract a PDF to page-marked text: a `===== PAGE N =====` line, then that page's text.

Usage:  extract_pages.py <file.pdf> [-o out.txt]

Backends tried in order: PyMuPDF (fitz), pypdf, pdftotext. The one that ran is printed on stderr.
Every checker in this skill reads this format, and so should the agent doing the reading: a quote
without a page is a quote nobody can verify.

Extraction silently drops or mangles math glyphs, and this script's own normalisation deletes them
from both sides of every comparison, so a misquote that lost a ≳ verifies exactly like the true
sentence. The CLI therefore prints a glyph report on stderr after extraction: per-page counts of
≳ ≲ ± × ☉, plus a warning that ≳/≲ can extract as > < or vanish, so ratios and limits must be
confirmed on the rendered page.

Also importable: load_pages(path) accepts a .pdf or an already-marked .txt and returns {page: text};
squash(s) is the normalisation every checker compares with.
"""
import argparse
import re
import shutil
import subprocess
import sys
import unicodedata

MARK = re.compile(r'^===== PAGE (\d+) =====$', re.M)
GLYPHS = '≳≲±×☉'


def glyph_report(pages):
    """Per-page counts of the glyphs extraction is known to drop or mangle, on stderr."""
    lines = []
    for i, t in enumerate(pages, 1):
        counts = ' '.join(f'{g}×{t.count(g)}' for g in GLYPHS if t.count(g))
        if counts:
            lines.append(f'  p{i}: {counts}')
    print('glyph report (≳ ≲ ± × ☉): ' + ('found on some pages:' if lines else 'none found'), file=sys.stderr)
    for ln in lines:
        print(ln, file=sys.stderr)
    print('note: ≳/≲ can extract as > < or vanish; ratios and limits must be confirmed on the rendered page',
          file=sys.stderr)


def squash(s: str) -> str:
    """NFKD, combining marks stripped, lower-case, letters and digits only.
    Drops ligatures, diacritics, line-break hyphens and math symbols, so both sides compare on the same footing."""
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn')
    return re.sub(r'[^a-z0-9]', '', s.lower())


def via_fitz(path):
    import fitz  # PyMuPDF
    return [p.get_text() for p in fitz.open(path)]


def via_pypdf(path):
    from pypdf import PdfReader
    return [p.extract_text() or '' for p in PdfReader(path).pages]


def via_pdftotext(path):
    if not shutil.which('pdftotext'):
        raise RuntimeError('pdftotext not on PATH')
    out = subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True, check=True).stdout
    pages = out.split('\f')
    return pages[:-1] if pages and not pages[-1].strip() else pages


def extract(path):
    errors = []
    for name, fn in (('fitz', via_fitz), ('pypdf', via_pypdf), ('pdftotext', via_pdftotext)):
        try:
            pages = fn(path)
            if pages and any(p.strip() for p in pages):
                return name, pages
        except Exception as e:  # noqa: BLE001 - try the next backend
            errors.append(f'{name}: {e}')
    raise SystemExit(f'no backend could read {path}\n' + '\n'.join(errors))


def render(pages):
    return ''.join(f'\n===== PAGE {i} =====\n{t}\n' for i, t in enumerate(pages, 1))


def load_pages(path):
    """{page_number: text} from a .pdf (extracted now) or a page-marked .txt."""
    if path.lower().endswith('.pdf'):
        _, pages = extract(path)
        return {i: t for i, t in enumerate(pages, 1)}
    raw = open(path, encoding='utf-8').read()
    parts = MARK.split(raw)
    if len(parts) < 3:
        return {1: raw}  # unmarked text: treat as one page
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('pdf')
    ap.add_argument('-o', '--out')
    a = ap.parse_args()
    backend, pages = extract(a.pdf)
    glyph_report(pages)
    text = render(pages)
    if a.out:
        open(a.out, 'w', encoding='utf-8').write(text)
        print(f'{a.pdf}: {len(pages)} pages via {backend} -> {a.out}', file=sys.stderr)
    else:
        sys.stdout.write(text)
        print(f'{a.pdf}: {len(pages)} pages via {backend}', file=sys.stderr)


if __name__ == '__main__':
    main()
