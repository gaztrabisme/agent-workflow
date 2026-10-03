#!/usr/bin/env python3
"""Check that every relative link resolves and every cited course anchor exists.

Scans SKILL.md and references/method/*.md. An anchor is a citation such as
"1140 · U3 · L09 · 05:00–06:14"; it must match a section anchor in the source
files, by default references/course/*.md.

    check_refs.py --sources 'references/course*/*.md'    # every course folder
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANCHOR = re.compile(r'\d+ · U\d+ · L\d{2,3} · \d{2}:\d{2}–\d{2}:\d{2}')
LINK = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')


def glob_all(patterns: list[str]) -> list[Path]:
    found = []
    for pattern in patterns:
        found.extend(sorted(ROOT.glob(pattern)))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description='Check links and cited course anchors.')
    ap.add_argument('--sources', nargs='+', default=['references/course/*.md'],
                    help='globs of the source files that define the anchors, relative to the skill root')
    args = ap.parse_args()

    known = set()
    for path in glob_all(args.sources):
        known.update(ANCHOR.findall(path.read_text(encoding='utf-8')))
    files = [ROOT / 'SKILL.md', *sorted((ROOT / 'references' / 'method').glob('*.md'))]
    problems = cited = 0
    for path in files:
        text = path.read_text(encoding='utf-8')
        for target in LINK.findall(text):
            if '://' in target:
                continue
            if not (path.parent / target).exists():
                problems += 1
                print(f'{path.relative_to(ROOT)}: broken link {target}')
        for anchor in ANCHOR.findall(text):
            cited += 1
            if anchor not in known:
                problems += 1
                print(f'{path.relative_to(ROOT)}: anchor not in course: {anchor}')
        for name in re.findall(r'`((?:references|method)/[\w./-]+\.md)`', text):
            target = ROOT / name if name.startswith('references/') else ROOT / 'references' / name
            if not target.exists():
                problems += 1
                print(f'{path.relative_to(ROOT)}: missing file {name}')
    print(f'{len(files)} files, {cited} anchors cited, {len(known)} known, {problems} problem(s)')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
