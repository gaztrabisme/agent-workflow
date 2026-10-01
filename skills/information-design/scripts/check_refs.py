#!/usr/bin/env python3
"""Check skill-package paths, links, optional structure/format, and source anchors.

Derived package-audit checks from skill-builder dogfood 2026-10-01. The default
anchor pattern and source globs still suit a course-distilled skill; use
--no-anchor-check explicitly for an authored package with no citation corpus.

    check_refs.py <skill-root> [--sources 'references/course/*.md']
    check_refs.py <skill-root> --no-anchor-check --format --skeleton <path>

Exit 0 when checks pass, 1 when a defect is found. Missing sibling pointers are
reported as warnings because a skill can be reviewed outside its full constellation.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOMESTIKA_ANCHOR = r'\d+ · U\d+ · L\d{2,3} · \d{2}:\d{2}–\d{2}:\d{2}'
LINK = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')
CODE_SPAN = re.compile(r'`([^`]+)`')
LOCAL_DIRS = ('references/', 'scripts/', 'tests/', 'method/')
ROOT_FILES = {'SKILL.md', 'EVOLUTION.md', 'LICENSE', 'LICENSE.md', 'NOTICE.md', 'README.md'}
PATH_SUFFIXES = ('.md', '.py', '.sh', '.txt', '.json', '.yaml', '.yml', '.toml', '.csv', '.svg', '.png')
PACKAGE_DIRS = ('references', 'scripts', 'tests')


def glob_all(root: Path, patterns: list[str]) -> list[Path]:
    found: set[Path] = set()
    for pattern in patterns:
        found.update(path for path in root.glob(pattern) if path.is_file())
    return sorted(found)


def is_package_path(value: str) -> bool:
    value = value.strip().strip('<>')
    return (
        value.startswith(LOCAL_DIRS)
        or value.startswith('./')
        or value.startswith('../')
        or value in ROOT_FILES
        or value.endswith(PATH_SUFFIXES)
    )


def is_sibling(value: str) -> bool:
    return value.startswith('../')


def is_course_corpus(path: Path, root: Path) -> bool:
    """Course reading copies and frames are source evidence, not skill references."""
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        return False
    return len(parts) > 1 and parts[0] == 'references' and parts[1].startswith('course-')


def heading_key(heading: str) -> str:
    text = heading.lstrip('#').strip()
    text = re.sub(r'\s*\([^)]*\)\s*$', '', text)
    return re.sub(r'\s+', ' ', text).casefold()


def frontmatter_fields(text: str) -> dict[str, str]:
    match = re.match(r'\A---\s*\n(.*?)\n---(?:\s|\Z)', text, flags=re.S)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        found = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', line)
        if found:
            fields[found.group(1)] = found.group(2).strip().strip('"\'')
    return fields


def main() -> int:
    ap = argparse.ArgumentParser(description='Check a skill package and optional source anchors.')
    ap.add_argument('root', type=Path, help='skill directory')
    ap.add_argument('--anchor', default=DOMESTIKA_ANCHOR, help='regex for one source anchor')
    ap.add_argument('--sources', nargs='+', default=['references/course/*.md'],
                    help='globs of files that define the anchors')
    ap.add_argument('--files', nargs='+', default=['SKILL.md', 'references/**/*.md',
                                                   'tests/**/*.md'],
                    help='globs of Markdown files whose links and citations are checked')
    ap.add_argument('--no-anchor-check', action='store_true',
                    help='explicitly skip anchors for a package with no source corpus')
    ap.add_argument('--skeleton', type=Path,
                    help='skeleton file; every non-placeholder H2/H3 heading must be present')
    ap.add_argument('--format', action='store_true', dest='check_format',
                    help='check name, description, and SKILL.md line-count requirements offline')
    ap.add_argument('--public', action='store_true',
                    help='with --format, require a frontmatter license or a LICENSE file')
    args = ap.parse_args()

    root = args.root.resolve()
    skill_file = root / 'SKILL.md'
    if not skill_file.is_file():
        print(f'missing required file: {skill_file}')
        return 1

    skill_text = skill_file.read_text(encoding='utf-8')
    # The paid reading copies are an evidence corpus. Their lesson-to-frame and PDF
    # links are audited separately; enumerating every frame as a skill reference
    # would make the operating manual list hundreds of source assets.
    files = [path for path in glob_all(root, args.files)
             if not is_course_corpus(path, root)]
    if skill_file not in files:
        files.insert(0, skill_file)
    files = sorted(set(files))
    source_files = glob_all(root, args.sources) if not args.no_anchor_check else []
    anchor = re.compile(args.anchor)
    known: set[str] = set()
    for path in source_files:
        known.update(anchor.findall(path.read_text(encoding='utf-8')))

    problems = 0
    warnings = 0
    cited = 0
    print('Files scanned:')
    for path in files:
        print(f'  {path.relative_to(root)}')
    print('Anchor source files scanned:')
    if source_files:
        for path in source_files:
            print(f'  {path.relative_to(root)}')
    elif args.no_anchor_check:
        print('  skipped explicitly with --no-anchor-check')
    else:
        print('  none')

    for path in files:
        rel = path.relative_to(root)
        text = path.read_text(encoding='utf-8')
        for target in LINK.findall(text):
            if '://' in target or target.startswith('mailto:'):
                continue
            resolved = (path.parent / target).resolve()
            if resolved.exists():
                continue
            if is_sibling(target):
                warnings += 1
                print(f'WARNING {rel}: sibling pointer unavailable in this workspace: {target}')
            else:
                problems += 1
                print(f'{rel}: broken local link {target}')

        for found in anchor.findall(text):
            if args.no_anchor_check:
                continue
            cited += 1
            if found not in known:
                problems += 1
                print(f'{rel}: anchor not in sources: {found}')

    path_mentions = 0
    for value in CODE_SPAN.findall(skill_text):
        value = value.strip()
        if not is_package_path(value):
            continue
        path_mentions += 1
        resolved = (root / value).resolve()
        if resolved.exists():
            continue
        if is_sibling(value):
            warnings += 1
            print(f'WARNING SKILL.md: sibling path unavailable in this workspace: {value}')
        else:
            problems += 1
            print(f'SKILL.md: missing local path {value}')

    named_text = skill_text
    shipped: list[Path] = []
    for directory in PACKAGE_DIRS:
        folder = root / directory
        if folder.is_dir():
            shipped.extend(path for path in folder.rglob('*')
                           if path.is_file() and '__pycache__' not in path.parts
                           and path.suffix != '.pyc'
                           and not is_course_corpus(path, root))
    print('Reference/script/test files shipped:')
    for path in sorted(shipped):
        rel = path.relative_to(root).as_posix()
        print(f'  {rel}')
        if rel not in named_text and path.name not in named_text:
            problems += 1
            print(f'SKILL.md: shipped file is not named: {rel}')

    if args.skeleton:
        skeleton_path = args.skeleton if args.skeleton.is_absolute() else root / args.skeleton
        if not skeleton_path.is_file():
            problems += 1
            print(f'missing skeleton file: {skeleton_path}')
        else:
            target_headings = {heading_key(line) for line in skill_text.splitlines()
                               if re.match(r'^#{2,3}\s+', line)}
            expected = [line for line in skeleton_path.read_text(encoding='utf-8').splitlines()
                        if re.match(r'^#{2,3}\s+', line)]
            for heading in expected:
                if '<' in heading or '>' in heading:
                    continue
                key = heading_key(heading)
                if key not in target_headings:
                    problems += 1
                    print(f'SKILL.md: missing skeleton heading {heading}')

    if args.check_format:
        fields = frontmatter_fields(skill_text)
        name = fields.get('name', '')
        description = fields.get('description', '')
        if not name:
            problems += 1
            print('SKILL.md: frontmatter name is missing')
        elif name != root.name:
            problems += 1
            print(f'SKILL.md: name {name!r} does not match directory {root.name!r}')
        if not description:
            problems += 1
            print('SKILL.md: frontmatter description is missing')
        else:
            if len(description) > 1024:
                problems += 1
                print(f'SKILL.md: description is {len(description)} characters (maximum 1024)')
            if 'USE WHEN' not in description.upper():
                problems += 1
                print('SKILL.md: description is missing USE WHEN')
            if not re.search(r'\bKeywords\s*:', description, flags=re.I):
                problems += 1
                print('SKILL.md: description is missing Keywords:')
        line_count = len(skill_text.splitlines())
        if line_count > 500:
            problems += 1
            print(f'SKILL.md: {line_count} lines (maximum 500)')
        if args.public and not (fields.get('license') or (root / 'LICENSE').is_file()):
            problems += 1
            print('public package: declare a frontmatter license or include LICENSE')

    if args.no_anchor_check:
        print('WARNING: source-anchor check was explicitly skipped; no citation coverage is claimed.')
    elif not known:
        problems += 1
        print('ERROR: 0 known source anchors; the configured anchor corpus is empty. '
              'Add sources or pass --no-anchor-check for a non-distilled package.')
    elif cited == 0:
        warnings += 1
        print('WARNING: no source anchors were cited by the scanned files.')

    print(f'{len(files)} files scanned, {path_mentions} local paths checked, '
          f'{cited} anchors cited, {len(known)} known, {problems} problem(s), '
          f'{warnings} warning(s)')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
