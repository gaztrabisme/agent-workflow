#!/usr/bin/env python3
"""Build an English, learning-only reading copy of an archived Domestika course."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path

import markdown
from PIL import Image, ImageDraw, ImageFont

from package_domestika import (CHROME, basename, caption_path, inspect_captions,
                               normalize_caption_language, tidy, validate_manifest)
from pdf_layout import duration, render_pdf, safe_fragment


HERE = Path(__file__).resolve().parent
RULES_PATH = HERE / 'marketing_rules.json'
LANGUAGE_NAMES = {
    'ca': 'Catalan', 'de': 'German', 'en': 'English', 'es': 'Spanish', 'fr': 'French',
    'it': 'Italian', 'ja': 'Japanese', 'ko': 'Korean', 'nl': 'Dutch', 'pl': 'Polish',
    'pt': 'Portuguese', 'ru': 'Russian', 'tr': 'Turkish', 'vi': 'Vietnamese', 'zh': 'Chinese',
}
TIME = r'(?:\d{1,2}:)?\d{1,2}:\d{2}(?:\.\d+)?'
SECTION = re.compile(rf'^## (.+?)\s*\[({TIME})\s*[–-]\s*({TIME})\]\s*$')
FIGURE = re.compile(rf'^::: figure ({TIME}) (F[\w.-]+\.jpg)\s*$')
KEY_POINTS = '### Key points (derived)'
MAX_GAP = 60
MIN_PROSE_RATIO = 0.35
THUMB = (480, 270)
LABEL = 30
STATES = ('excluded', 'prepared', 'drafted', 'checked')


# ---------------------------------------------------------------- times

def parse_time(value: str) -> float:
    parts = [float(part) for part in value.split(':')]
    seconds = 0.0
    for part in parts:
        seconds = seconds * 60 + part
    return seconds


def fmt_time(seconds: float) -> str:
    whole = int(seconds)
    hours, rest = divmod(whole, 3600)
    minutes, secs = divmod(rest, 60)
    return f'{hours}:{minutes:02d}:{secs:02d}' if hours else f'{minutes:02d}:{secs:02d}'


# ---------------------------------------------------------------- rules

def load_rules(course_id: int, path: Path = RULES_PATH) -> dict[str, list[re.Pattern]]:
    raw = json.loads(path.read_text(encoding='utf-8'))
    return {key: [re.compile(pattern.replace('{course_id}', str(course_id)), re.I)
                  for pattern in patterns]
            for key, patterns in raw.items() if not key.startswith('_')}


def first_match(patterns: list[re.Pattern], text: str) -> re.Pattern | None:
    return next((pattern for pattern in patterns if pattern.search(text)), None)


def is_intro_lesson(title: str, rules: dict) -> bool:
    return first_match(rules['intro_lessons'], title.strip()) is not None


class Removals:
    """Collects every removal so a person can audit what the rules took out."""

    def __init__(self):
        self.rows: list[tuple[str, str, str]] = []

    def add(self, rule: re.Pattern, where: str, text: str) -> None:
        self.rows.append((rule.pattern, where, re.sub(r'\s+', ' ', text).strip()[:400]))

    def count(self, where_prefix: str) -> int:
        return sum(1 for _, where, _ in self.rows if where.startswith(where_prefix))

    def write(self, path: Path) -> None:
        lines = [f'{where}\t{rule}\t{text}' for rule, where, text in self.rows]
        path.write_text('location\trule\tremoved text\n' + '\n'.join(lines) + '\n', encoding='utf-8')


# ---------------------------------------------------------------- HTML cleaning

class Node:
    def __init__(self, tag: str, attrs: dict[str, str] | None = None):
        self.tag, self.attrs, self.children = tag, attrs or {}, []

    def text(self) -> str:
        return ''.join(child if isinstance(child, str) else child.text() for child in self.children)


class TreeBuilder(HTMLParser):
    VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('root')
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, {key: value or '' for key, value in attrs})
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, {key: value or '' for key, value in attrs}))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


BLOCKS = {'p', 'div', 'li', 'blockquote', 'section', 'ul', 'ol'}
HEADINGS = {'h2', 'h3', 'h4'}


def serialize(node: Node) -> str:
    out = []
    for child in node.children:
        if isinstance(child, str):
            out.append(html.escape(child))
            continue
        attrs = ''.join(f' {key}="{html.escape(value, quote=True)}"' for key, value in child.attrs.items())
        if child.tag in TreeBuilder.VOID:
            out.append(f'<{child.tag}{attrs}>')
        else:
            out.append(f'<{child.tag}{attrs}>{serialize(child)}</{child.tag}>')
    return ''.join(out)


def own_heading(node: Node) -> str:
    for child in node.children:
        if isinstance(child, Node) and child.tag in HEADINGS:
            return re.sub(r'\s+', ' ', child.text()).strip()
    return ''


def _filter(node: Node, rules: dict, where: str, log: Removals) -> None:
    kept = []
    for child in node.children:
        if isinstance(child, str):
            kept.append(child)
            continue
        heading = own_heading(child) if child.tag in BLOCKS else ''
        rule = first_match(rules['item_headings'], heading) if heading else None
        if rule:
            log.add(rule, where, child.text())
            continue
        if child.tag == 'a':
            rule = first_match(rules['link_unwrap'], child.attrs.get('href', ''))
            if rule:
                _filter(child, rules, where, log)
                kept.extend(child.children)
                continue
        _filter(child, rules, where, log)
        if child.tag in BLOCKS:
            text = re.sub(r'\s+', ' ', child.text()).strip()
            rule = first_match(rules['cta_text'], text)
            if rule:
                log.add(rule, where, text)
                continue
            if not text and not _has_image(child):
                continue
        kept.append(child)
    node.children = kept


def _has_image(node: Node) -> bool:
    return any(isinstance(child, Node) and (child.tag == 'img' or _has_image(child))
               for child in node.children)


def clean_html(fragment: str, rules: dict, where: str, log: Removals) -> str:
    builder = TreeBuilder()
    builder.feed(fragment or '')
    _filter(builder.root, rules, where, log)
    return serialize(builder.root)


def clean_prose(text: str, rules: dict, where: str, log: Removals) -> str:
    if not first_match(rules['prose_cta'], text):
        return text
    lines = []
    for line in text.split('\n'):
        prefix = line[:len(line) - len(line.lstrip())]
        marker = re.match(r'(?:[-*+]|\d+[.)])\s+', line[len(prefix):])
        prefix += marker.group(0) if marker else ''
        kept = []
        for sentence in re.split(r'(?<=[.!?])\s+', line[len(prefix):]):
            sentence_rule = first_match(rules['prose_cta'], sentence)
            if sentence_rule is None:
                kept.append(sentence)
                continue
            # Drop only the matching clause, so teaching in the same sentence survives.
            clauses = re.split(r'(?<=;)\s+', sentence)
            survivors = []
            for clause in clauses:
                rule = first_match(rules['prose_cta'], clause)
                if rule:
                    log.add(rule, where, clause)
                else:
                    survivors.append(clause)
            if len(survivors) == len(clauses):
                log.add(sentence_rule, where, sentence)
            elif survivors:
                kept.append(re.sub(r';$', '.', ' '.join(survivors).rstrip()))
        if ' '.join(kept).strip():
            lines.append(prefix + ' '.join(kept))
        elif not line.strip():
            lines.append('')
    return '\n'.join(lines)


# ---------------------------------------------------------------- captions

def read_vtt(path: Path) -> list[tuple[float, float, str]]:
    text = path.read_text(encoding='utf-8-sig')
    cues: list[tuple[float, float, str]] = []
    for block in re.split(r'\n\s*\n', text.replace('\r\n', '\n')):
        lines = block.strip().split('\n')
        for index, line in enumerate(lines):
            found = re.match(rf'^({TIME})\s*-->\s*({TIME})', line.strip())
            if found:
                body = ' '.join(lines[index + 1:])
                body = re.sub(r'<[^>]+>', '', html.unescape(body))
                body = re.sub(r'\s+', ' ', body).strip()
                if body:
                    cues.append((parse_time(found.group(1)), parse_time(found.group(2)), body))
                break
    merged: list[tuple[float, float, str]] = []
    for start, end, body in cues:
        if merged:
            p_start, p_end, p_body = merged[-1]
            if body == p_body or p_body.endswith(body):
                merged[-1] = (p_start, max(p_end, end), p_body)
                continue
            if body.startswith(p_body):
                merged[-1] = (p_start, max(p_end, end), body)
                continue
        merged.append((start, end, body))
    return merged


def write_transcript(cues: list[tuple[float, float, str]], path: Path) -> int:
    path.write_text(''.join(f'[{fmt_time(start)}] {body}\n' for start, _, body in cues), encoding='utf-8')
    return sum(len(body.split()) for _, _, body in cues)


def native_language(folder: Path, name: str) -> str:
    settings_path = folder / f'{name}.download.json'
    try:
        settings = json.loads(settings_path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f'No download settings for {name}; re-run the packager for this unit.') from error
    if settings.get('default_language'):
        return normalize_caption_language(settings['default_language'])
    # Older work directories: the packager orders caption languages as (requested, default).
    languages = settings.get('caption_languages') or []
    if len(languages) in (1, 2):
        return normalize_caption_language(languages[-1])
    raise RuntimeError(f'Cannot tell the speaker\'s caption language for {name}.')


# ---------------------------------------------------------------- video

def ffmpeg_scan(mp4: Path) -> tuple[list[float], list[tuple[float, float | None]]]:
    chain = 'fps=5,scale=320:-2,freezedetect=n=0.003:d=1.5,select=gt(scene\\,0.3),showinfo'
    base = ['ffmpeg', '-hide_banner', '-nostats', '-i', str(mp4), '-an', '-vf', chain, '-f', 'null', '-']
    run = subprocess.run(base[:3] + ['-hwaccel', 'videotoolbox'] + base[3:], capture_output=True, text=True)
    if run.returncode:
        run = subprocess.run(base, capture_output=True, text=True)
    if run.returncode:
        raise RuntimeError(f'ffmpeg could not scan {mp4.name}: {run.stderr[-800:]}')
    cuts = [float(value) for value in re.findall(r'showinfo.*?pts_time:([\d.]+)', run.stderr)]
    starts = [float(v) for v in re.findall(r'freeze_start: ([\d.]+)', run.stderr)]
    ends = [float(v) for v in re.findall(r'freeze_end: ([\d.]+)', run.stderr)]
    freezes = [(start, ends[index] if index < len(ends) else None) for index, start in enumerate(starts)]
    return sorted(set(cuts)), freezes


def candidate_times(cuts: list[float], freezes: list[tuple[float, float | None]],
                    length: float) -> list[float]:
    times = []
    bounds = [0.0] + [cut for cut in cuts if 0 < cut < length] + [length]
    for start, end in zip(bounds, bounds[1:]):
        if end - start >= 1:
            times.append(end - 0.5)
        step = start + 30
        while step < end - 15:
            times.append(step)
            step += 30
    for start, end in freezes:
        end = length if end is None else end
        if end - start >= 3:
            times.append(end - 0.3)
    times = sorted(min(max(t, 0.5), length - 0.5) for t in times) or [length / 2]
    merged = [times[0]]
    for t in times[1:]:
        if t - merged[-1] < 2:
            merged[-1] = t
        else:
            merged.append(t)
    return [round(t, 1) for t in merged]


def grab_frame(mp4: Path, seconds: float, out: Path, width: int, quality: int) -> None:
    command = ['ffmpeg', '-v', 'error', '-y', '-ss', f'{seconds:.2f}', '-i', str(mp4),
               '-frames:v', '1', '-vf', f"scale='min({width},iw)':-2", '-q:v', str(quality), str(out)]
    run = subprocess.run(command, capture_output=True, text=True)
    if run.returncode or not out.exists():
        raise RuntimeError(f'Could not extract a frame at {fmt_time(seconds)} from {mp4.name}.')


def contact_sheets(thumbs: list[tuple[int, float, Path]], directory: Path) -> list[Path]:
    font = ImageFont.load_default(size=22)
    sheets = []
    for page, offset in enumerate(range(0, len(thumbs), 16), start=1):
        batch = thumbs[offset:offset + 16]
        rows = (len(batch) + 3) // 4
        sheet = Image.new('RGB', (4 * THUMB[0], rows * (THUMB[1] + LABEL)), 'white')
        draw = ImageDraw.Draw(sheet)
        for slot, (index, seconds, path) in enumerate(batch):
            x, y = (slot % 4) * THUMB[0], (slot // 4) * (THUMB[1] + LABEL)
            with Image.open(path) as image:
                image.thumbnail(THUMB)
                sheet.paste(image, (x, y + LABEL))
            draw.text((x + 8, y + 3), f'#{index:02d}  {fmt_time(seconds)}  ({seconds:.1f}s)', fill='black', font=font)
        target = directory / f'sheet-{page:02d}.png'
        sheet.save(target)
        sheets.append(target)
    return sheets


# ---------------------------------------------------------------- course layout

def unit_folder(workdir: Path, unit: dict) -> Path:
    return workdir / f'Unit {unit["number"]:02d} - {tidy(unit["title"])}'


def lesson_dir(workdir: Path, unit: dict, lesson: dict) -> Path:
    return workdir / 'reading' / f'U{unit["number"]:02d}' / f'L{lesson["number"]:02d}'


def load_course(manifest: Path, wanted: list[int] | None) -> tuple[dict, list[dict]]:
    course = json.loads(manifest.read_text(encoding='utf-8'))
    units = validate_manifest(course)
    if wanted:
        units = [unit for unit in units if unit['number'] in set(wanted)]
        if len(units) != len(set(wanted)):
            raise ValueError('At least one requested unit is not in this course.')
    return course, units


def progress_path(workdir: Path) -> Path:
    return workdir / 'reading' / 'progress.json'


def load_progress(workdir: Path) -> dict:
    try:
        return json.loads(progress_path(workdir).read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return {}


def save_progress(workdir: Path, progress: dict) -> None:
    progress_path(workdir).parent.mkdir(parents=True, exist_ok=True)
    progress_path(workdir).write_text(json.dumps(progress, indent=2) + '\n', encoding='utf-8')


def set_state(progress: dict, unit: dict, lesson: dict, state: str) -> None:
    progress[str(lesson['number'])] = {'unit': unit['number'], 'title': lesson['title'], 'state': state}


# ---------------------------------------------------------------- prepare

def prepare_lesson(course: dict, unit: dict, lesson: dict, workdir: Path) -> Path:
    folder, name = unit_folder(workdir, unit), basename(lesson)
    mp4 = folder / f'{name}.mp4'
    if not mp4.exists():
        raise RuntimeError(f'Missing video for lesson {lesson["number"]}: {mp4}')
    directory = lesson_dir(workdir, unit, lesson)
    (directory / 'thumbs').mkdir(parents=True, exist_ok=True)
    (directory / 'frames').mkdir(exist_ok=True)
    native = native_language(folder, name)
    transcripts, words = {}, 0
    for language in dict.fromkeys((native, 'en')):
        vtt = caption_path(folder, name, language)
        if not inspect_captions(vtt):
            if language == native:
                raise RuntimeError(f'Native ({native}) captions are missing or invalid: {vtt}')
            continue
        target = directory / f'transcript.{language}.txt'
        count = write_transcript(read_vtt(vtt), target)
        transcripts[language] = target.name
        if language == native:
            words = count
    meta = {
        'course_id': course['course_id'], 'unit': unit['number'], 'unit_title': unit['title'],
        'lesson': lesson['number'], 'lesson_id': lesson['id'], 'title': lesson['title'],
        'duration_seconds': lesson['duration_seconds'], 'url': lesson['url'],
        'mp4': str(mp4), 'file': mp4.name, 'native_language': native,
        'transcripts': transcripts, 'native_words': words,
    }
    (directory / 'lesson.json').write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    candidates_path = directory / 'candidates.json'
    signature = {'size': mp4.stat().st_size, 'mtime': int(mp4.stat().st_mtime)}
    try:
        previous = json.loads(candidates_path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        previous = {}
    sheets = sorted(directory.glob('sheet-*.png'))
    if previous.get('source') == signature and sheets:
        print(f'  L{lesson["number"]:02d}: reusing {len(previous["candidates"])} candidates', flush=True)
        return directory
    cuts, freezes = ffmpeg_scan(mp4)
    times = candidate_times(cuts, freezes, float(lesson['duration_seconds']))
    for old in list(directory.glob('thumbs/*.jpg')) + sheets:
        old.unlink()
    thumbs = []
    for index, seconds in enumerate(times, start=1):
        path = directory / 'thumbs' / f'{index:03d}.jpg'
        grab_frame(mp4, seconds, path, THUMB[0], 5)
        thumbs.append((index, seconds, path))
    sheets = contact_sheets(thumbs, directory)
    candidates_path.write_text(json.dumps({
        'source': signature, 'cuts': cuts,
        'freezes': [[start, end] for start, end in freezes],
        'candidates': [{'index': index, 'time': seconds} for index, seconds, _ in thumbs],
    }, indent=2) + '\n', encoding='utf-8')
    print(f'  L{lesson["number"]:02d}: {len(thumbs)} candidates on {len(sheets)} sheet(s), '
          f'native captions {native}', flush=True)
    return directory


def cmd_prepare(args) -> int:
    course, units = load_course(args.manifest, args.unit)
    rules = load_rules(course['course_id'])
    for unit in units:
        print(f'Unit {unit["number"]}: {unit["title"]}', flush=True)
        for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
            excluded = is_intro_lesson(lesson['title'], rules)
            if excluded:
                print(f'  L{lesson["number"]:02d}: excluded by intro rule ({lesson["title"]})', flush=True)
            else:
                prepare_lesson(course, unit, lesson, args.workdir)
            # Reload before each write: check runs from other agents update the same file.
            progress = load_progress(args.workdir)
            state = progress.get(str(lesson['number']), {}).get('state')
            if excluded:
                set_state(progress, unit, lesson, 'excluded')
            elif state not in ('drafted', 'checked'):
                set_state(progress, unit, lesson, 'prepared')
            save_progress(args.workdir, progress)
    return 0


# ---------------------------------------------------------------- frames

def cmd_frames(args) -> int:
    directory = args.lesson_dir.expanduser().resolve()
    meta = json.loads((directory / 'lesson.json').read_text(encoding='utf-8'))
    index_path = directory / 'frames.json'
    index = json.loads(index_path.read_text(encoding='utf-8')) if index_path.exists() else {}
    for value in args.at:
        seconds = parse_time(value)
        if not 0 <= seconds <= meta['duration_seconds']:
            raise ValueError(f'{value} is outside the video ({duration(meta["duration_seconds"])}).')
        stem = f'F{int(seconds // 60):02d}{int(seconds % 60):02d}'
        name = f'{stem}.jpg'
        suffix = ord('b')
        while name in index and abs(index[name] - seconds) > 0.05:
            name = f'{stem}{chr(suffix)}.jpg'
            suffix += 1
        grab_frame(Path(meta['mp4']), seconds, directory / 'frames' / name, 1600, 3)
        index[name] = round(seconds, 2)
        print(f'{name}\t{fmt_time(seconds)}', flush=True)
    index_path.write_text(json.dumps(dict(sorted(index.items())), indent=2) + '\n', encoding='utf-8')
    return 0


# ---------------------------------------------------------------- lesson.md

def parse_lesson(text: str) -> tuple[dict, list[dict], str, list[str]]:
    errors: list[str] = []
    front: dict[str, str] = {}
    lines = text.replace('\r\n', '\n').split('\n')
    if lines and lines[0].strip() == '---':
        try:
            end = lines.index('---', 1)
        except ValueError:
            return front, [], '', ['Front matter is not closed with ---.']
        for line in lines[1:end]:
            if ':' in line:
                key, value = line.split(':', 1)
                front[key.strip()] = value.strip()
        lines = lines[end + 1:]
    else:
        errors.append('Missing front matter.')
    sections: list[dict] = []
    key_points: list[str] = []
    mode = 'none'
    figure: dict | None = None
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if figure is not None:
            if stripped == ':::':
                sections[-1]['blocks'].append(('figure', figure))
                figure = None
            elif stripped.startswith('On screen:'):
                figure['on_screen'] = stripped[len('On screen:'):].strip()
            elif stripped.startswith('Shows:'):
                figure['shows'] = stripped[len('Shows:'):].strip()
            elif stripped:
                errors.append(f'Line {number}: unexpected text inside a figure block.')
            continue
        if line.startswith('## '):
            found = SECTION.match(line)
            if not found:
                errors.append(f'Line {number}: section heading lacks a [mm:ss–mm:ss] range: {line[:80]}')
                continue
            sections.append({'title': found.group(1).strip(), 'start': parse_time(found.group(2)),
                             'end': parse_time(found.group(3)), 'blocks': [], 'text': []})
            mode = 'section'
            continue
        if line.startswith('### '):
            if stripped == KEY_POINTS:
                mode = 'key_points'
                continue
            if 'key point' in stripped.lower():
                errors.append(f'Line {number}: key points must use the heading "{KEY_POINTS}".')
                continue
        if stripped.startswith('::: figure'):
            found = FIGURE.match(stripped)
            if not found or mode != 'section':
                errors.append(f'Line {number}: figure blocks look like "::: figure mm:ss Fmmss.jpg" and sit inside a section.')
                continue
            figure = {'time': parse_time(found.group(1)), 'label': found.group(1), 'file': found.group(2),
                      'on_screen': '', 'shows': ''}
            continue
        if mode == 'key_points':
            key_points.append(line)
        elif mode == 'section':
            sections[-1]['blocks'].append(('text', line))
            sections[-1]['text'].append(line)
        elif stripped:
            errors.append(f'Line {number}: text outside a section.')
    if figure is not None:
        errors.append('A figure block is not closed with :::.')
    return front, sections, '\n'.join(key_points).strip(), errors


def section_prose(section: dict) -> str:
    return '\n'.join(section['text']).strip()


def check_lesson(directory: Path, rules: dict, log: Removals | None = None) -> list[str]:
    meta = json.loads((directory / 'lesson.json').read_text(encoding='utf-8'))
    path = directory / 'lesson.md'
    if not path.exists():
        return ['lesson.md has not been written.']
    front, sections, key_points, errors = parse_lesson(path.read_text(encoding='utf-8'))
    length = float(meta['duration_seconds'])
    if str(front.get('lesson_id')) != str(meta['lesson_id']):
        errors.append(f'Front matter lesson_id must be {meta["lesson_id"]}.')
    if front.get('native_language') != meta['native_language']:
        errors.append(f'Front matter native_language must be {meta["native_language"]}.')
    if not sections:
        errors.append('No sections.')
    frames = directory / 'frames.json'
    frame_times = json.loads(frames.read_text(encoding='utf-8')) if frames.exists() else {}
    previous_end = None
    for section in sections:
        label = f'Section "{section["title"]}"'
        if section['start'] >= section['end']:
            errors.append(f'{label}: range starts after it ends.')
        if section['end'] > length + 1:
            errors.append(f'{label}: range ends after the video ({duration(length)}).')
        if previous_end is not None:
            if section['start'] < previous_end - 0.5:
                errors.append(f'{label}: range overlaps or is out of order.')
            elif section['start'] - previous_end > MAX_GAP:
                errors.append(f'{label}: {section["start"] - previous_end:.0f}s gap before it is not covered.')
        previous_end = section['end']
        if not section_prose(section):
            errors.append(f'{label}: has no prose.')
        for kind, block in section['blocks']:
            if kind != 'figure':
                continue
            where = f'{label}, figure {block["label"]}'
            if block['file'] not in frame_times or not (directory / 'frames' / block['file']).exists():
                errors.append(f'{where}: {block["file"]} was not extracted with the frames command.')
            elif abs(frame_times[block['file']] - block['time']) > 1.5:
                errors.append(f'{where}: timestamp does not match {block["file"]}.')
            if not section['start'] - 1 <= block['time'] <= section['end'] + 1:
                errors.append(f'{where}: timestamp is outside the section range.')
            if not block['on_screen']:
                errors.append(f'{where}: missing "On screen:" line.')
            if not block['shows']:
                errors.append(f'{where}: missing "Shows:" line.')
    if sections:
        if sections[0]['start'] > MAX_GAP:
            errors.append(f'First section starts at {fmt_time(sections[0]["start"])}; cover from the first minute.')
        if sections[-1]['end'] < length - MAX_GAP:
            errors.append(f'Last section ends at {fmt_time(sections[-1]["end"])}; the video runs to {duration(length)}.')
    body = path.read_text(encoding='utf-8')
    if '-->' in body or re.search(r'<c[.>]|</c>', body):
        errors.append('Caption markup (--> or <c>) left in the text.')
    prose_words = sum(len(section_prose(section).split()) for section in sections)
    needed = MIN_PROSE_RATIO * meta.get('native_words', 0)
    if prose_words < needed and not front.get('compression_note'):
        errors.append(f'Prose has {prose_words} words; the native transcript has {meta["native_words"]}. '
                      f'Write at least {needed:.0f} or explain in compression_note.')
    if log is not None:
        where = f'U{meta["unit"]:02d}/L{meta["lesson"]:02d}'
        for section in sections:
            clean_prose(section_prose(section), rules, where, log)
        if key_points:
            clean_prose(key_points, rules, where, log)
    return errors


def cmd_check(args) -> int:
    course, units = load_course(args.manifest, args.unit)
    rules = load_rules(course['course_id'])
    progress = load_progress(args.workdir)
    failed = 0
    for unit in units:
        for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
            if args.lesson and lesson['number'] not in args.lesson:
                continue
            if is_intro_lesson(lesson['title'], rules):
                set_state(progress, unit, lesson, 'excluded')
                continue
            directory = lesson_dir(args.workdir, unit, lesson)
            if not (directory / 'lesson.json').exists():
                print(f'U{unit["number"]:02d} L{lesson["number"]:02d}: not prepared')
                failed += 1
                continue
            log = Removals()
            errors = check_lesson(directory, rules, log)
            removed = len(log.rows)
            if errors:
                failed += 1
                if (directory / 'lesson.md').exists():
                    set_state(progress, unit, lesson, 'drafted')
                print(f'U{unit["number"]:02d} L{lesson["number"]:02d}: FAIL')
                for error in errors:
                    print(f'  - {error}')
            else:
                set_state(progress, unit, lesson, 'checked')
                print(f'U{unit["number"]:02d} L{lesson["number"]:02d}: ok ({removed} sentence(s) will be removed by rules)')
    save_progress(args.workdir, progress)
    return 1 if failed else 0


def cmd_status(args) -> int:
    course, units = load_course(args.manifest, args.unit)
    progress = load_progress(args.workdir)
    counts = dict.fromkeys(STATES + ('not started',), 0)
    for unit in units:
        for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
            state = progress.get(str(lesson['number']), {}).get('state', 'not started')
            counts[state] += 1
            print(f'U{unit["number"]:02d} L{lesson["number"]:02d}  {state:<11}  {lesson["title"]}')
    print('  '.join(f'{key}: {value}' for key, value in counts.items() if value))
    return 0


# ---------------------------------------------------------------- clean + build

def clean_course(course: dict, units: list[dict], workdir: Path, rules: dict) -> tuple[dict, Removals]:
    log = Removals()
    cleaned = {}
    for unit in units:
        where = f'U{unit["number"]:02d}'
        cleaned[unit['number']] = {
            'intro': clean_html(unit.get('intro_html') or '', rules, f'{where}/intro', log),
            'extras': [{'title': extra.get('title') or 'More',
                        'html': clean_html(extra.get('html') or '', rules,
                                           f'{where}/{extra.get("title") or "extra"}', log)}
                       for extra in unit.get('extras', [])],
        }
        for lesson in unit['lessons']:
            rule = first_match(rules['intro_lessons'], lesson['title'].strip())
            if rule:
                log.add(rule, f'{where}/L{lesson["number"]:02d}', f'Whole lesson: {lesson["title"]}')
    log.write(workdir / 'reading' / 'removed.log')
    return cleaned, log


def cmd_clean(args) -> int:
    course, units = load_course(args.manifest, args.unit)
    rules = load_rules(course['course_id'])
    (args.workdir / 'reading').mkdir(parents=True, exist_ok=True)
    _, log = clean_course(course, units, args.workdir, rules)
    for unit in units:
        for lesson in unit['lessons']:
            directory = lesson_dir(args.workdir, unit, lesson)
            if (directory / 'lesson.md').exists() and (directory / 'lesson.json').exists():
                check_lesson(directory, rules, log)
    log.write(args.workdir / 'reading' / 'removed.log')
    print(f'{len(log.rows)} removal(s); see {args.workdir / "reading" / "removed.log"}')
    return 0


STYLE = '''
@page { size: A4; margin: 16mm 17mm 18mm; }
body { font-family: Georgia, 'Times New Roman', serif; color: #1d1d1d; font-size: 10.5pt; line-height: 1.5; margin: 0; }
a { color: #1f4e8c; text-decoration: none; overflow-wrap: anywhere; }
h1 { font-size: 26pt; line-height: 1.15; margin: 0 0 10px; }
h2 { font-size: 18pt; margin: 0 0 6px; break-after: avoid; }
h3 { font-size: 13pt; margin: 18px 0 2px; break-after: avoid; }
h4 { font-size: 11pt; margin: 12px 0 4px; break-after: avoid; }
p { margin: 0 0 8px; }
img { max-width: 100%; }
.title-page { page-break-after: always; padding-top: 60mm; }
.title-page .meta { font-family: Arial, sans-serif; color: #555; font-size: 10pt; margin-top: 8px; }
.contents { page-break-after: always; font-family: Arial, sans-serif; font-size: 10pt; }
.contents ol { padding-left: 18px; }
.unit { page-break-before: always; }
.unit-label, .anchor { font-family: Menlo, Consolas, monospace; font-size: 8pt; color: #666; }
.lesson { border-top: 1px solid #ccc; margin-top: 22px; padding-top: 12px; }
.section { margin-top: 10px; }
figure { margin: 10px 0 14px; break-inside: avoid; }
figure img { display: block; max-height: 80mm; object-fit: contain; border: 1px solid #ddd; }
figcaption { font-family: Arial, sans-serif; font-size: 8.5pt; color: #333; margin-top: 4px; }
figcaption .label { font-weight: bold; }
.derived { background: #f4f4f1; border-left: 3px solid #999; padding: 6px 12px; margin: 12px 0; }
.extras { font-family: Arial, sans-serif; font-size: 9.5pt; border-top: 1px solid #ccc; margin-top: 22px; padding-top: 10px; }
.extras h2 { font-size: 12pt; }
.extras img { max-height: 70mm; }
.appendix { page-break-before: always; font-family: Arial, sans-serif; font-size: 8.5pt; }
table { border-collapse: collapse; width: 100%; }
td, th { border-bottom: 1px solid #ddd; padding: 3px 4px; text-align: left; vertical-align: top; }
'''
TEMPLATE_TEXT = ('Reading copy', 'Translated from', 'captions', 'Contents', 'Unit', 'Lesson',
                 'Figure', 'On screen', 'Shows', 'Key points (derived)', 'Appendix A: sources',
                 'Appendix B: figures', 'Teacher introduction, not included', 'Written from the')


def has_content(extra: dict) -> bool:
    """False when cleaning left only the section's own heading."""
    text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', extra['html']))).strip()
    return bool(text) and text.lower() != extra['title'].strip().lower()


def render_lesson(meta: dict, directory: Path, rules: dict, log: Removals,
                  figures: list[dict]) -> str:
    e = html.escape
    _, sections, key_points, _ = parse_lesson((directory / 'lesson.md').read_text(encoding='utf-8'))
    where = f'U{meta["unit"]:02d}/L{meta["lesson"]:02d}'
    lesson_anchor = f'{meta["course_id"]} · U{meta["unit"]} · L{meta["lesson"]:02d}'
    parts = [f'<section class="lesson" id="lesson-{meta["lesson"]}">',
             f'<div class="anchor">{e(lesson_anchor)} · {e(meta["file"])}</div>',
             f'<h2>Lesson {meta["lesson"]:02d} · {e(meta["title"])}</h2>']
    for section in sections:
        span = f'{fmt_time(section["start"])}–{fmt_time(section["end"])}'
        parts.append(f'<div class="section"><h3>{e(section["title"])}</h3>'
                     f'<div class="anchor">{e(lesson_anchor)} · {span}</div>')
        buffer: list[str] = []

        def flush():
            text = clean_prose('\n'.join(buffer).strip(), rules, where, log)
            if text:
                parts.append(safe_fragment(markdown.markdown(text)))
            buffer.clear()

        for kind, block in section['blocks']:
            if kind == 'text':
                buffer.append(block)
                continue
            flush()
            number = len(figures) + 1
            figures.append({'number': number, 'anchor': f'{lesson_anchor} · {block["label"]}',
                            'file': block['file'], 'on_screen': block['on_screen'], 'lesson': meta['lesson']})
            source = (directory / 'frames' / block['file']).as_uri()
            parts.append(f'<figure id="figure-{number}"><img src="{e(source, quote=True)}" alt="">'
                         f'<figcaption><span class="label">Figure {number}</span> · '
                         f'{e(lesson_anchor)} · {e(block["label"])}<br>'
                         f'<b>On screen:</b> {e(block["on_screen"])}<br>'
                         f'<b>Shows:</b> {e(block["shows"])}</figcaption></figure>')
        flush()
        parts.append('</div>')
    if key_points:
        text = clean_prose(key_points, rules, where, log)
        parts.append(f'<div class="derived"><h4>Key points (derived)</h4>'
                     f'{safe_fragment(markdown.markdown(text))}</div>')
    parts.append('</section>')
    return ''.join(parts)


def build_html(course: dict, units: list[dict], workdir: Path, rules: dict,
               teacher: str | None) -> tuple[str, Removals, list[dict], set[str]]:
    e = html.escape
    cleaned, log = clean_course(course, units, workdir, rules)
    figures: list[dict] = []
    languages: set[str] = set()
    sources, body, contents = [], [], []
    for unit in units:
        contents.append(f'<li><a href="#unit-{unit["number"]}">Unit {unit["number"]} · {e(unit["title"])}</a><ol>')
        lessons_html = []
        for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
            name = basename(lesson)
            if is_intro_lesson(lesson['title'], rules):
                sources.append((unit, lesson, f'{name}.mp4', 'Teacher introduction, not included'))
                continue
            directory = lesson_dir(workdir, unit, lesson)
            if not (directory / 'lesson.json').exists():
                raise RuntimeError(f'Lesson {lesson["number"]} has not been prepared.')
            errors = check_lesson(directory, rules)
            if errors:
                raise RuntimeError(f'Lesson {lesson["number"]} fails check: {errors[0]}')
            meta = json.loads((directory / 'lesson.json').read_text(encoding='utf-8'))
            languages.add(meta['native_language'])
            lessons_html.append(render_lesson(meta, directory, rules, log, figures))
            contents.append(f'<li><a href="#lesson-{lesson["number"]}">Lesson {lesson["number"]:02d} · {e(lesson["title"])}</a></li>')
            sources.append((unit, lesson, f'{name}.mp4', f'{name}.{meta["native_language"]}.vtt'))
        contents.append('</ol></li>')
        extras = ''.join(f'<section class="extras">{safe_fragment(extra["html"])}</section>'
                         for extra in cleaned[unit['number']]['extras'] if has_content(extra))
        body.append(f'<section class="unit" id="unit-{unit["number"]}">'
                    f'<div class="unit-label">{course["course_id"]} · U{unit["number"]}</div>'
                    f'<h1>Unit {unit["number"]} · {e(unit["title"])}</h1>'
                    f'{safe_fragment(cleaned[unit["number"]]["intro"])}{"".join(lessons_html)}{extras}</section>')
    names = sorted(LANGUAGE_NAMES.get(code.split('_')[0], code) for code in languages)
    origin = ('Written from the English captions' if names == ['English']
              else f'Translated from {" and ".join(names)} captions')
    source_rows = ''.join(
        f'<tr><td>{unit["number"]}</td><td>{lesson["number"]:02d}</td><td>{lesson["id"]}</td>'
        f'<td><a href="{e(lesson["url"], quote=True)}">{e(lesson["title"])}</a></td>'
        f'<td>{duration(lesson["duration_seconds"])}</td><td>{e(file)}</td><td>{e(note)}</td></tr>'
        for unit, lesson, file, note in sources)
    figure_rows = ''.join(
        f'<tr><td><a href="#figure-{fig["number"]}">{fig["number"]}</a></td><td>{e(fig["anchor"])}</td>'
        f'<td>{e(fig["file"])}</td><td>{e(fig["on_screen"][:120])}</td></tr>' for fig in figures)
    teacher_line = f'<div class="meta">{e(teacher)}</div>' if teacher else ''
    document = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
      <title>{e(course["course_title"])} - Reading copy</title><style>{STYLE}</style></head><body>
      <section class="title-page"><div class="unit-label">Course {course["course_id"]}</div>
      <h1>{e(course["course_title"])}</h1>{teacher_line}
      <div class="meta">Reading copy · {e(origin)}</div></section>
      <nav class="contents"><h2>Contents</h2><ol>{"".join(contents)}
      <li><a href="#appendix-a">Appendix A: sources</a></li><li><a href="#appendix-b">Appendix B: figures</a></li></ol></nav>
      {"".join(body)}
      <section class="appendix" id="appendix-a"><h2>Appendix A: sources</h2>
      <table><tr><th>Unit</th><th>Lesson</th><th>ID</th><th>Title</th><th>Length</th><th>File</th><th>Captions used</th></tr>{source_rows}</table></section>
      <section class="appendix" id="appendix-b"><h2>Appendix B: figures</h2>
      <table><tr><th>Figure</th><th>Anchor</th><th>File</th><th>On screen</th></tr>{figure_rows}</table></section>
      </body></html>'''
    return document, log, figures, languages


def add_to_zip(archive: Path, pdf: Path, member: str) -> None:
    temp = archive.with_name(archive.name + '.building')
    temp.unlink(missing_ok=True)
    with zipfile.ZipFile(archive, 'r') as source:
        previous = [info for info in source.infolist() if info.filename != member]
        with zipfile.ZipFile(temp, 'w', allowZip64=True) as target:
            for info in previous:
                with source.open(info) as reader, target.open(info, 'w', force_zip64=True) as writer:
                    shutil.copyfileobj(reader, writer, 1024 * 1024)
            target.write(pdf, member, compress_type=zipfile.ZIP_DEFLATED)
    expected = {info.filename for info in previous} | {member}
    with zipfile.ZipFile(temp, 'r') as check:
        if set(check.namelist()) != expected:
            raise RuntimeError('The ZIP contents do not match after adding the reading copy.')
        corrupt = check.testzip()
        if corrupt:
            raise RuntimeError(f'ZIP integrity check failed at {corrupt}.')
    temp.replace(archive)


def cmd_build(args) -> int:
    course, units = load_course(args.manifest, args.unit)
    rules = load_rules(course['course_id'])
    if args.zip and args.unit:
        raise ValueError('--zip needs the whole course; drop --unit.')
    for text in TEMPLATE_TEXT:
        rule = first_match(rules['template_forbidden'], text)
        if rule:
            raise RuntimeError(f'Page template contains forbidden text: {text}')
    if not Path(CHROME).exists():
        raise RuntimeError('Google Chrome is required to render the reading copy.')
    document, log, figures, _ = build_html(course, units, args.workdir, rules, args.teacher)
    log.write(args.workdir / 'reading' / 'removed.log')
    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    html_path = args.workdir / 'reading' / 'reading-copy.html'
    html_path.write_text(document, encoding='utf-8')
    render_pdf(CHROME, html_path, output)
    print(f'Reading copy: {output} ({len(figures)} figures, {len(log.rows)} removal(s) logged)')
    if args.zip:
        member = f'{tidy(course["course_title"])} - reading copy.pdf'
        add_to_zip(args.zip.expanduser().resolve(), output, member)
        print(f'Added to ZIP as {member}; member set and CRC verified.')
    return 0


# ---------------------------------------------------------------- CLI

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)

    def course_command(name: str, help_text: str):
        command = sub.add_parser(name, help=help_text)
        command.add_argument('manifest', type=Path, help='JSON saved by collect_domestika.js')
        command.add_argument('--workdir', type=Path, required=True, help='The packager work directory')
        command.add_argument('--unit', type=int, action='append', help='Limit to this unit (repeatable)')
        return command

    course_command('prepare', 'Write transcripts, candidate frames and contact sheets')
    check = course_command('check', 'Validate lesson.md files')
    check.add_argument('--lesson', type=int, action='append', help='Limit to this lesson number (repeatable)')
    course_command('status', 'Show progress per lesson')
    course_command('clean', 'Apply marketing rules and write removed.log')
    build = course_command('build', 'Render the reading copy PDF')
    build.add_argument('--output', type=Path, required=True, help='Destination PDF')
    build.add_argument('--zip', type=Path, help='Course ZIP to add the PDF to (whole course only)')
    build.add_argument('--teacher', help='Teacher name for the title page')
    frames = sub.add_parser('frames', help='Extract kept frames at full resolution')
    frames.add_argument('lesson_dir', type=Path, help='reading/UNN/LNN directory')
    frames.add_argument('--at', action='append', required=True, help='Timestamp mm:ss[.f] (repeatable)')
    args = parser.parse_args()
    if hasattr(args, 'workdir'):
        args.workdir = args.workdir.expanduser().resolve()
    handlers = {'prepare': cmd_prepare, 'check': cmd_check, 'status': cmd_status,
                'clean': cmd_clean, 'build': cmd_build, 'frames': cmd_frames}
    return handlers[args.command](args)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, RuntimeError, OSError, subprocess.TimeoutExpired) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
