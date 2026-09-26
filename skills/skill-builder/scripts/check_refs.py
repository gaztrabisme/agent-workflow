#!/usr/bin/env python3
"""Check a distilled skill's citations: every relative link resolves, every cited anchor exists.

An anchor is a citation string that locates a claim in the source material, such as the
Domestika reading-copy form "1140 · U3 · L09 · 05:00–06:14" (course · unit · lesson · time).
Anchors cited in the method files must appear somewhere in the source files.

    check_refs.py <skill-root>                       # defaults fit a course-distilled skill
    check_refs.py <skill-root> --sources 'references/book/*.md' --anchor 'p\\. \\d+'

Exit 0 when there are no problems, 1 otherwise.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOMESTIKA_ANCHOR = r'\d+ · U\d+ · L\d{2} · \d{2}:\d{2}–\d{2}:\d{2}'
LINK = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')
PATH_MENTION = re.compile(r'`((?:references|method)/[\w./ -]+\.md)`')


def glob_all(root: Path, patterns: list[str]) -> list[Path]:
    found: list[Path] = []
    for pattern in patterns:
        found.extend(sorted(root.glob(pattern)))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description="Check a distilled skill's links and cited anchors.")
    ap.add_argument('root', type=Path, help='skill directory')
    ap.add_argument('--anchor', default=DOMESTIKA_ANCHOR, help='regex for one anchor')
    ap.add_argument('--sources', nargs='+', default=['references/course/*.md'],
                    help='globs of the source files that define the anchors')
    ap.add_argument('--files', nargs='+', default=['SKILL.md', 'references/method/*.md'],
                    help='globs of the files whose links and citations are checked')
    args = ap.parse_args()

    root = args.root.resolve()
    anchor = re.compile(args.anchor)
    known: set[str] = set()
    for path in glob_all(root, args.sources):
        known.update(anchor.findall(path.read_text(encoding='utf-8')))
    files = glob_all(root, args.files)
    if not files:
        print(f'no files match {args.files} under {root}')
        return 1

    problems = cited = 0
    for path in files:
        rel = path.relative_to(root)
        text = path.read_text(encoding='utf-8')
        for target in LINK.findall(text):
            if '://' in target or target.startswith('mailto:'):
                continue
            if not (path.parent / target).exists():
                problems += 1
                print(f'{rel}: broken link {target}')
        for found in anchor.findall(text):
            cited += 1
            if found not in known:
                problems += 1
                print(f'{rel}: anchor not in sources: {found}')
        for name in PATH_MENTION.findall(text):
            target = root / name if name.startswith('references/') else root / 'references' / name
            if not target.exists():
                problems += 1
                print(f'{rel}: missing file {name}')

    print(f'{len(files)} files, {cited} anchors cited, {len(known)} known, {problems} problem(s)')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
