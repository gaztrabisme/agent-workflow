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
from urllib.parse import unquote, urlsplit

DOMESTIKA_ANCHOR = r'\d+ · U\d+ · L\d{2,3} · \d{2}:\d{2}–\d{2}:\d{2}'
LINK = re.compile(r'!?\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)')
FENCED_CODE = re.compile(r'(?ms)^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[ \t]*$')
CITATION_ID = re.compile(r'\[(book|src):([A-Za-z0-9_./-]+)')
SOURCE_ROW = re.compile(r'^\|\s*`(book|src):([^`]+)`\s*\|')
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
    ap.add_argument('--files', nargs='+', default=['**/*.md'],
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
    files = glob_all(root, args.files)
    if skill_file not in files:
        files.insert(0, skill_file)
    files = sorted(set(files))
    source_files = glob_all(root, args.sources) if not args.no_anchor_check else []
    source_index = root / 'references' / 'sources.md'
    mapped_ids: set[str] = set()
    if source_index.is_file():
        for line in source_index.read_text(encoding='utf-8').splitlines():
            match = SOURCE_ROW.match(line)
            if match:
                mapped_ids.add(f'{match.group(1)}:{match.group(2)}')
    anchor = re.compile(args.anchor)
    known: set[str] = set()
    for path in source_files:
        known.update(anchor.findall(path.read_text(encoding='utf-8')))

    problems = 0
    warnings = 0
    cited = 0
    links_checked = 0
    citation_locations: dict[str, list[Path]] = {}
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
        markdown = FENCED_CODE.sub('', text)
        markdown = CODE_SPAN.sub('', markdown)
        for match in LINK.finditer(markdown):
            target = match.group(1).strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith('mailto:'):
                continue
            links_checked += 1
            local_target = unquote(parsed.path)
            resolved = ((root / local_target) if local_target.startswith('/')
                        else (path.parent / local_target)).resolve() if local_target else path.resolve()
            if resolved.exists():
                continue
            if is_sibling(local_target):
                warnings += 1
                print(f'WARNING {rel}: sibling pointer unavailable in this workspace: {target}')
            else:
                problems += 1
                print(f'{rel}: broken local link {target}')

        for kind, identifier in CITATION_ID.findall(markdown):
            citation = f'{kind}:{identifier}'
            citation_locations.setdefault(citation, []).append(rel)
        for found in anchor.findall(text):
            if args.no_anchor_check:
                continue
            cited += 1
            if found not in known:
                problems += 1
                print(f'{rel}: anchor not in sources: {found}')

    # (derived: dogfood 2026-10-02, F11) Do not report a clean run that checked no Markdown links.
    if links_checked == 0:
        problems += 1
        print('ERROR: 0 Markdown links checked; verify the Markdown file glob and link syntax.')

    if source_index.is_file():
        for citation, locations in sorted(citation_locations.items()):
            if citation not in mapped_ids:
                problems += 1
                print(f'{locations[0]}: citation missing from references/sources.md: {citation}')
    elif citation_locations:
        warnings += 1
        print('WARNING citation-ID mapping skipped: references/sources.md is not present.')

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
                           and path.suffix != '.pyc')
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
        print('WARNING: source-anchor verification was explicitly skipped; citation-ID mapping runs only when references/sources.md exists.')
    elif not known:
        problems += 1
        print('ERROR: 0 known source anchors; the configured anchor corpus is empty. '
              'Add sources or pass --no-anchor-check for a non-distilled package.')
    elif cited == 0:
        warnings += 1
        print('WARNING: no source anchors were cited by the scanned files.')

    print(f'{len(files)} files scanned, {links_checked} Markdown links checked, '
          f'{path_mentions} inline paths checked, '
          f'{cited} anchors cited, {len(known)} known, {problems} problem(s), '
          f'{warnings} warning(s)')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
