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
from urllib.request import Request, urlopen

from pdf_layout import render_pdf, unit_html


CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
LANGUAGE_TAGS = {
    'ar': 'ara', 'ca': 'cat', 'cs': 'ces', 'da': 'dan', 'de': 'deu',
    'el': 'ell', 'en': 'eng', 'es': 'spa', 'fi': 'fin', 'fr': 'fra',
    'he': 'heb', 'hi': 'hin', 'hr': 'hrv', 'hu': 'hun', 'id': 'ind',
    'it': 'ita', 'ja': 'jpn', 'ko': 'kor', 'ms': 'msa', 'nl': 'nld',
    'no': 'nor', 'pl': 'pol', 'pt': 'por', 'ro': 'ron', 'ru': 'rus',
    'sk': 'slk', 'sv': 'swe', 'th': 'tha', 'tr': 'tur', 'uk': 'ukr',
    'vi': 'vie', 'zh': 'zho',
}


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


def audio_language_tag(language: str) -> str:
    return LANGUAGE_TAGS[language.split('_', 1)[0]]


def normalize_caption_language(language: str) -> str:
    code = language.strip().lower().replace('-', '_')
    if not re.fullmatch(r'[a-z]{2,3}(?:_[a-z]{2,3}|_[0-9]{3})?', code):
        raise ValueError(f'Unsupported caption language tag: {language}')
    return code


def parse_hls_attributes(value: str) -> dict[str, str]:
    return {key: raw.strip().strip('"') for key, raw in
            re.findall(r'([A-Z0-9-]+)=((?:"[^"]*")|[^,]*)', value)}


def default_audio_language(media_url: str, fallback: str, lesson_number: int) -> str:
    try:
        request = Request(media_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request, timeout=30) as response:
            playlist = response.read(512 * 1024).decode('utf-8-sig', 'replace')
    except OSError as error:
        raise RuntimeError(f'Could not read the audio language tag for lesson {lesson_number}.') from error
    if not playlist.lstrip().startswith('#EXTM3U'):
        raise RuntimeError(f'Lesson {lesson_number} did not return an HLS playlist.')
    audio_tracks = []
    for line in playlist.splitlines():
        if line.startswith('#EXT-X-MEDIA:'):
            attributes = parse_hls_attributes(line.split(':', 1)[1])
            if attributes.get('TYPE') == 'AUDIO':
                audio_tracks.append(attributes)
    defaults = [track for track in audio_tracks if track.get('DEFAULT', '').upper() == 'YES']
    if not defaults:
        return fallback
    raw_languages = [track.get('LANGUAGE', '').strip() for track in defaults]
    if any(not language for language in raw_languages):
        raise RuntimeError(f'Lesson {lesson_number} has a default audio track without a language tag.')
    try:
        languages = {normalize_caption_language(language) for language in raw_languages}
    except ValueError as error:
        raise RuntimeError(f'Lesson {lesson_number} has an invalid default audio language tag.') from error
    if len(languages) != 1:
        raise RuntimeError(f'Lesson {lesson_number} has an ambiguous default audio language tag.')
    return languages.pop()


def find_caption_track(subtitles: dict, language: str) -> str | None:
    target = normalize_caption_language(language)
    for key in subtitles:
        if normalize_caption_language(key) == target:
            return key
    return None


def caption_path(directory: Path, name: str, language: str) -> Path:
    code = normalize_caption_language(language)
    return directory / f'{name}.{code}.vtt'


def inspect_video(path: Path, expected_seconds: int, max_height: int,
                  audio_language: str) -> bool:
    if not path.exists() or path.stat().st_size < 100_000:
        return False
    probe = subprocess.run(['ffprobe', '-v', 'error', '-show_format', '-show_streams',
                            '-of', 'json', str(path)], capture_output=True, text=True)
    if probe.returncode:
        return False
    info = json.loads(probe.stdout)
    streams = info.get('streams', [])
    video = [stream for stream in streams if stream['codec_type'] == 'video']
    duration = float(info.get('format', {}).get('duration') or 0)
    audio = [stream for stream in streams if stream['codec_type'] == 'audio']
    height = int(video[0].get('height') or 0) if len(video) == 1 else 0
    return (len(video) == 1 and 0 < height <= max_height
            and len(audio) == 1
            and audio[0].get('tags', {}).get('language') == audio_language_tag(audio_language)
            and abs(duration - expected_seconds) < max(8, expected_seconds * 0.03))


def tag_audio_language(path: Path, language: str) -> None:
    tag = audio_language_tag(language)
    temp = path.with_name(f'{path.stem}.tagged.mp4')
    temp.unlink(missing_ok=True)
    result = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(path), '-map', '0',
                             '-c', 'copy', '-metadata:s:a:0', f'language={tag}', str(temp)],
                            capture_output=True, text=True)
    if result.returncode or not temp.exists():
        temp.unlink(missing_ok=True)
        raise RuntimeError(f'Could not write the {language} audio tag to {path.name}.')
    temp.replace(path)


def format_selector(max_height: int, audio_language: str) -> str:
    return f'bestvideo[height<={max_height}]+bestaudio[language={audio_language}]'


def preflight_lesson(lesson: dict, max_height: int, audio_language: str,
                     caption_language: str, yt_dlp: str) -> tuple[str, list[str], str]:
    command = [yt_dlp, '--dump-single-json', '--skip-download', '--no-warnings',
               '--no-playlist', '--format', format_selector(max_height, audio_language),
               lesson['media_url']]
    result = subprocess.run(command, capture_output=True, text=True, timeout=90)
    if result.returncode:
        raise RuntimeError(f'Preflight could not read lesson {lesson["number"]}: access or stream selection failed.')
    try:
        info = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(f'Preflight metadata is invalid for lesson {lesson["number"]}.') from error
    selected = info.get('requested_formats') or []
    video = [item for item in selected if item.get('vcodec') not in (None, 'none')]
    audio = [item for item in selected if item.get('vcodec') in (None, 'none')
             and item.get('language') == audio_language]
    subtitles = info.get('subtitles') or {}
    default_language = default_audio_language(lesson['media_url'], audio_language,
                                              lesson['number'])
    requested_caption_codes = list(dict.fromkeys((caption_language, default_language)))
    caption_tracks = [find_caption_track(subtitles, language)
                      for language in requested_caption_codes]
    drm = (info.get('_has_drm') is True or bool(info.get('hls_aes'))
           or any(item.get('has_drm') is True for item in selected))
    if drm:
        raise RuntimeError(f'Lesson {lesson["number"]} is protected; this archiver does not handle DRM.')
    if len(video) != 1 or int(video[0].get('height') or 0) > max_height:
        raise RuntimeError(f'Lesson {lesson["number"]} has no selectable video at or below {max_height}p.')
    if len(audio) != 1:
        raise RuntimeError(f'Lesson {lesson["number"]} has no selectable {audio_language} audio track.')
    missing = [language for language, track in zip(requested_caption_codes, caption_tracks) if not track]
    if missing:
        missing_names = ', '.join(missing)
        raise RuntimeError(f'Lesson {lesson["number"]} has no requested/default-language caption track: {missing_names}.')
    selected_captions = list(dict.fromkeys(track for track in caption_tracks if track))
    selected_audio_caption = ', '.join(normalize_caption_language(track) for track in selected_captions)
    return (f'{int(video[0]["height"])}p video, {audio_language} audio, '
            f'default audio {default_language}, captions {selected_audio_caption}', selected_captions,
            default_language)


def preflight_units(units: list[dict], max_height: int, audio_language: str,
                    caption_language: str, yt_dlp: str) -> tuple[dict[int, list[str]], dict[int, str]]:
    caption_languages_by_lesson, default_languages_by_lesson = {}, {}
    for unit in units:
        for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
            selected, caption_languages, default_language = preflight_lesson(
                lesson, max_height, audio_language, caption_language, yt_dlp)
            print(f'Preflight U{unit["number"]} L{lesson["number"]}: {selected}', flush=True)
            caption_languages_by_lesson[lesson['id']] = caption_languages
            default_languages_by_lesson[lesson['id']] = default_language
    return caption_languages_by_lesson, default_languages_by_lesson


def inspect_captions(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 30:
        return False
    text = path.read_text(encoding='utf-8-sig')
    return text.lstrip().startswith('WEBVTT') and bool(re.search(r'(?:\d\d:)?\d\d:\d\d\.\d{3}\s*-->', text))


def download_lesson(lesson: dict, directory: Path, name: str, max_height: int,
                    audio_language: str, caption_languages: list[str], default_language: str,
                    yt_dlp: str) -> None:
    mp4 = directory / f'{name}.mp4'
    caption_files = {language: caption_path(directory, name, language)
                     for language in caption_languages}
    settings_path = directory / f'{name}.download.json'
    expected_settings = {'max_height': max_height, 'audio_language': audio_language,
                         'caption_languages': [normalize_caption_language(language)
                                               for language in caption_languages],
                         'default_language': normalize_caption_language(default_language)}
    try:
        saved_settings = json.loads(settings_path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        saved_settings = None
    media_valid = inspect_video(mp4, lesson['duration_seconds'], max_height, audio_language)
    captions_valid = all(inspect_captions(path) for path in caption_files.values())
    if media_valid and captions_valid:
        if saved_settings != expected_settings:
            settings_path.write_text(json.dumps(expected_settings, indent=2) + '\n', encoding='utf-8')
        print(f'  Reusing {mp4.name}', flush=True)
        return
    template = directory / f'{name}.%(ext)s'
    command = [yt_dlp, '--no-playlist', '--no-warnings', '--newline',
               '--concurrent-fragments', '8', '--retries', '5', '--fragment-retries', '5',
               '--format', format_selector(max_height, audio_language),
               '--merge-output-format', 'mp4', '--write-subs', '--sub-langs',
               ','.join(caption_languages),
               '--sub-format', 'vtt', '--output', str(template), lesson['media_url']]
    if media_valid:
        command.insert(1, '--skip-download')
    if mp4.exists() or any(path.exists() for path in caption_files.values()):
        command.insert(1, '--force-overwrites')
    if media_valid:
        print(f'  Downloading captions for {name}…', flush=True)
    else:
        print(f'  Downloading {name} ({max_height}p maximum)…', flush=True)
    log_path = directory / f'{name}.download.log'
    with log_path.open('w', encoding='utf-8') as log:
        run = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
    if run.returncode:
        raise RuntimeError(f'Download failed for {name}. See {log_path}')
    for language, expected_path in caption_files.items():
        code = normalize_caption_language(language)
        candidates = (directory / f'{name}.{language}.vtt',
                     directory / f'{name}.{code}.vtt',
                     directory / f'{name}.{code.replace("_", "-")}.vtt')
        source = next((candidate for candidate in candidates if candidate.exists()), None)
        if source and source != expected_path:
            source.replace(expected_path)
    if not media_valid:
        if not mp4.exists():
            raise RuntimeError(f'The video is missing: {mp4}')
        tag_audio_language(mp4, audio_language)
    if not inspect_video(mp4, lesson['duration_seconds'], max_height, audio_language):
        raise RuntimeError(f'The video is missing or invalid: {mp4}')
    for language, path in caption_files.items():
        if not inspect_captions(path):
            raise RuntimeError(f'{language} timed captions are missing or invalid: {path}')
    log_path.unlink(missing_ok=True)
    settings_path.write_text(json.dumps(expected_settings, indent=2) + '\n', encoding='utf-8')


def make_archive(course: dict, units: list[dict], folders: dict[int, Path],
                 caption_languages_by_lesson: dict[int, list[str]], archive: Path) -> None:
    from archive_core.adapters import Domestika
    Domestika.package_legacy(course, units, folders, caption_languages_by_lesson, archive)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path, help='JSON saved by collect_domestika.js')
    parser.add_argument('--output', type=Path, help='Destination ZIP path')
    parser.add_argument('--workdir', type=Path, help='Folder for resumable intermediate files')
    parser.add_argument('--max-height', type=int, default=1080, help='Maximum video height (default: 1080)')
    parser.add_argument('--audio-language', default='en', help='Audio language code (default: en)')
    parser.add_argument('--caption-language', default='en', help='Timed caption language code (default: en)')
    parser.add_argument('--unit', type=int, action='append', help='Package only this unit (repeatable)')
    parser.add_argument('--probe-only', action='store_true', help='Check selected lesson tracks and DRM without downloading')
    args = parser.parse_args()
    if args.max_height < 240 or args.max_height > 2160:
        parser.error('--max-height must be between 240 and 2160')
    if not re.fullmatch(r'[a-z]{2}(?:_[a-z]{2})?', args.audio_language):
        parser.error('--audio-language must be a language code such as en or es_la')
    if not re.fullmatch(r'[a-z]{2,3}(?:[-_](?:[a-z]{2,3}|[0-9]{3}))?', args.caption_language):
        parser.error('--caption-language must be a language code such as en or es_la')
    if args.audio_language.split('_', 1)[0] not in LANGUAGE_TAGS:
        parser.error('--audio-language must use a supported MP4 language code; see LANGUAGE_TAGS in the script')
    yt_dlp = shutil.which('yt-dlp')
    if not yt_dlp:
        parser.error('yt-dlp is required. Install it before using this archiver.')
    if not args.probe_only:
        for executable in ('ffmpeg', 'ffprobe'):
            if not shutil.which(executable):
                parser.error(f'{executable} is required. Install it before packaging.')
        if not Path(CHROME).exists():
            parser.error('Google Chrome is required to render the unit PDFs.')
    course = json.loads(args.manifest.read_text(encoding='utf-8'))
    units = validate_manifest(course)
    if args.unit:
        wanted = set(args.unit)
        units = [unit for unit in units if unit['number'] in wanted]
        if len(units) != len(wanted):
            parser.error('At least one requested unit is not in this course.')
    caption_languages_by_lesson, default_languages_by_lesson = preflight_units(units, args.max_height, args.audio_language,
                                                  args.caption_language, yt_dlp)
    if args.probe_only:
        preflight_count = len(caption_languages_by_lesson)
        print(f'Preflight complete: {preflight_count} lesson playlists checked; no files downloaded.', flush=True)
        return 0
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
        html_path.write_text(unit_html(course, unit, names, caption_languages_by_lesson), encoding='utf-8')
        print(f'Unit {unit["number"]}: {unit["title"]}', flush=True)
        render_pdf(CHROME, html_path, pdf_path)
        for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
            download_lesson(lesson, folder, names[lesson['id']], args.max_height,
                            args.audio_language, caption_languages_by_lesson[lesson['id']],
                            default_languages_by_lesson[lesson['id']], yt_dlp)
    print('Creating ZIP…', flush=True)
    make_archive(course, units, folders, caption_languages_by_lesson, output)
    from archive_core.compatibility import emit_domestika_handoff
    handoff = emit_domestika_handoff(course, units, folders, caption_languages_by_lesson, output.with_suffix('.handoff'))
    print(f'Knowledge-base handoff: {handoff["release"]} (pending)', flush=True)
    print(f'Complete: {output}', flush=True)
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, RuntimeError, OSError, subprocess.TimeoutExpired) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
