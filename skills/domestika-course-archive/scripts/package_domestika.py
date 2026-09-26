#!/usr/bin/env python3
"""Make an annotated ZIP from a signed-in Domestika course manifest."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.parse import urlparse

from pdf_layout import render_pdf, unit_html


CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def tidy(name: str) -> str:
    name = re.sub(r'[^\w\s.-]', '', name, flags=re.UNICODE)
    name = re.sub(r'\s+', ' ', name).strip(' .')
    return name[:80] or 'Untitled'


def basename(lesson: dict) -> str:
    slug = re.sub(r'[^a-z0-9]+', '-', lesson['title'].lower()).strip('-') or 'lesson'
    return f'{lesson["number"]:02d}-{slug[:65].rstrip("-")}'


def validate_manifest(data: dict) -> list[dict]:
    if data.get('version') != 1 or not data.get('course_id') or not data.get('course_title'):
        raise ValueError('This is not a supported course manifest.')
    units = data.get('units')
    if not isinstance(units, list) or not units:
        raise ValueError('The manifest contains no units.')
    if len(units) != data.get('expected_units'):
        raise ValueError('The manifest is missing one or more units.')
    lessons = sum(len(u.get('lessons', [])) for u in units)
    if lessons != data.get('expected_lessons'):
        raise ValueError('The manifest is missing one or more lessons.')
    unit_numbers, lesson_numbers, lesson_ids = set(), set(), set()
    for unit in units:
        if unit['number'] in unit_numbers or not unit.get('lessons'):
            raise ValueError('Duplicate unit or empty unit in manifest.')
        unit_numbers.add(unit['number'])
        if urlparse(unit['url']).netloc != 'www.domestika.org':
            raise ValueError('Unexpected unit page URL.')
        for lesson in unit['lessons']:
            source = urlparse(lesson['media_url'])
            if source.scheme != 'https' or source.netloc != 'cdn-videos.domestika.org' or not source.path.endswith('.m3u8'):
                raise ValueError(f'Unexpected stream URL for lesson {lesson["number"]}.')
            if lesson['number'] in lesson_numbers or lesson['id'] in lesson_ids:
                raise ValueError('Duplicate lesson in manifest.')
            lesson_numbers.add(lesson['number'])
            lesson_ids.add(lesson['id'])
    return sorted(units, key=lambda u: u['number'])


def inspect_video(path: Path, expected_seconds: int) -> bool:
    if not path.exists() or path.stat().st_size < 100_000:
        return False
    probe = subprocess.run(['ffprobe', '-v', 'error', '-show_format', '-show_streams',
                            '-of', 'json', str(path)], capture_output=True, text=True)
    if probe.returncode:
        return False
    info = json.loads(probe.stdout)
    streams = info.get('streams', [])
    duration = float(info.get('format', {}).get('duration') or 0)
    return (any(s['codec_type'] == 'video' for s in streams)
            and any(s['codec_type'] == 'audio' for s in streams)
            and abs(duration - expected_seconds) < max(8, expected_seconds * 0.03))


def inspect_captions(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 30:
        return False
    text = path.read_text(encoding='utf-8-sig')
    return text.lstrip().startswith('WEBVTT') and bool(re.search(r'(?:\d\d:)?\d\d:\d\d\.\d{3}\s*-->', text))


def download_lesson(lesson: dict, directory: Path, name: str, max_height: int, yt_dlp: str) -> None:
    mp4 = directory / f'{name}.mp4'
    vtt = directory / f'{name}.vtt'
    if inspect_video(mp4, lesson['duration_seconds']) and inspect_captions(vtt):
        print(f'  Reusing {mp4.name}', flush=True)
        return
    template = directory / f'{name}.%(ext)s'
    command = [yt_dlp, '--no-playlist', '--no-warnings', '--newline',
               '--concurrent-fragments', '8', '--retries', '5', '--fragment-retries', '5',
               '--format', f'bestvideo[height<={max_height}]+bestaudio[language=en]',
               '--merge-output-format', 'mp4', '--write-subs', '--sub-langs', 'en',
               '--sub-format', 'vtt', '--output', str(template), lesson['media_url']]
    print(f'  Downloading {name} ({max_height}p maximum)…', flush=True)
    log_path = directory / f'{name}.download.log'
    with log_path.open('w', encoding='utf-8') as log:
        run = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
    if run.returncode:
        raise RuntimeError(f'Download failed for {name}. See {log_path}')
    english = directory / f'{name}.en.vtt'
    if english.exists():
        english.replace(vtt)
    if not inspect_video(mp4, lesson['duration_seconds']):
        raise RuntimeError(f'The video is missing or invalid: {mp4}')
    if not inspect_captions(vtt):
        raise RuntimeError(f'English timed captions are missing or invalid: {vtt}')
    log_path.unlink(missing_ok=True)


def make_archive(course: dict, units: list[dict], folders: dict[int, Path], archive: Path) -> None:
    temp = archive.with_name(archive.name + '.building')
    temp.unlink(missing_ok=True)
    with zipfile.ZipFile(temp, 'w', allowZip64=True) as target:
        for unit in units:
            folder = folders[unit['number']]
            pdf = folder / f'{folder.name}.pdf'
            files = [pdf]
            for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
                base = basename(lesson)
                files += [folder / f'{base}.mp4', folder / f'{base}.vtt']
            for path in files:
                if not path.exists():
                    raise RuntimeError(f'Missing file before archiving: {path}')
                mode = zipfile.ZIP_STORED if path.suffix == '.mp4' else zipfile.ZIP_DEFLATED
                target.write(path, f'{folder.name}/{path.name}', compress_type=mode)
    temp.replace(archive)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path, help='JSON saved by collect_domestika.js')
    parser.add_argument('--output', type=Path, help='Destination ZIP path')
    parser.add_argument('--workdir', type=Path, help='Folder for resumable intermediate files')
    parser.add_argument('--max-height', type=int, default=1080, help='Maximum video height (default: 1080)')
    parser.add_argument('--unit', type=int, action='append', help='Package only this unit (repeatable)')
    args = parser.parse_args()
    if args.max_height < 240 or args.max_height > 2160:
        parser.error('--max-height must be between 240 and 2160')
    yt_dlp = shutil.which('yt-dlp')
    for executable in ('ffmpeg', 'ffprobe'):
        if not shutil.which(executable):
            parser.error(f'{executable} is required. Install it before packaging.')
    if not yt_dlp or not Path(CHROME).exists():
        parser.error('yt-dlp and Google Chrome are required. See README.md.')
    course = json.loads(args.manifest.read_text(encoding='utf-8'))
    units = validate_manifest(course)
    if args.unit:
        wanted = set(args.unit)
        units = [unit for unit in units if unit['number'] in wanted]
        if len(units) != len(wanted):
            parser.error('At least one requested unit is not in this course.')
    output = (args.output or Path.cwd() / f'domestika-course-{course["course_id"]}.zip').expanduser().resolve()
    workdir = (args.workdir or output.with_suffix('.work')).expanduser().resolve()
    if output == args.manifest.resolve() or output.is_dir():
        parser.error('Choose a ZIP file path for --output.')
    workdir.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    folders = {}
    for unit in units:
        folder = workdir / f'Unit {unit["number"]:02d} - {tidy(unit["title"])}'
        folder.mkdir(exist_ok=True)
        folders[unit['number']] = folder
        names = {lesson['id']: basename(lesson) for lesson in unit['lessons']}
        html_path = folder / f'{folder.name}.html'
        pdf_path = folder / f'{folder.name}.pdf'
        html_path.write_text(unit_html(course, unit, names), encoding='utf-8')
        print(f'Unit {unit["number"]}: {unit["title"]}', flush=True)
        render_pdf(CHROME, html_path, pdf_path)
        for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
            download_lesson(lesson, folder, names[lesson['id']], args.max_height, yt_dlp)
    print('Creating ZIP…', flush=True)
    make_archive(course, units, folders, output)
    print(f'Complete: {output}', flush=True)
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, RuntimeError, OSError, subprocess.TimeoutExpired) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
