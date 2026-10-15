"""Permitted shared transports. Transport capabilities never enter releases."""
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlsplit, parse_qsl, urlencode

from .adapters import git
from .storage import digest
from .privacy import SENSITIVE


def transport_identity(transport):
    """Content fingerprints exclude expiring access URLs and absolute machine paths."""
    kind = transport['kind']
    if kind == 'inline':
        return digest(transport['content'].encode())
    if kind == 'local':
        return digest(Path(transport['path']).read_bytes())
    if kind == 'git-blob':
        return transport['blob']
    if kind == 'playlist' and transport.get('fixture_media'):
        return digest(Path(transport['fixture_media']).read_bytes() + Path(transport['fixture_playlist']).read_bytes())
    url = urlsplit(transport['url'])
    ordinary_query = urlencode([(k, v) for k, v in parse_qsl(url.query, keep_blank_values=True) if not SENSITIVE.search(k)])
    return digest((url.scheme + '://' + url.netloc + url.path + '?' + ordinary_query).encode())


def playlist_probe(text, transport):
    if not text.lstrip().startswith('#EXTM3U'):
        raise ValueError('Invalid streaming playlist.')
    if re.search(r'#EXT-X-(?:KEY|SESSION-KEY):.*METHOD=(?!NONE)', text):
        raise ValueError('Protected playlist: transfer refused.')
    from package_domestika import parse_hls_attributes
    tracks = [parse_hls_attributes(line.split(':', 1)[1]) for line in text.splitlines() if line.startswith('#EXT-X-MEDIA:')]
    audio = [t for t in tracks if t.get('TYPE') == 'AUDIO']
    if not any(t.get('LANGUAGE') == transport['audio'] for t in audio):
        raise ValueError('Requested audio language is unavailable.')
    defaults = [t.get('LANGUAGE') for t in audio if t.get('DEFAULT') == 'YES']
    if len(set(defaults)) > 1 or any(not v for v in defaults):
        raise ValueError('Default audio language is ambiguous or unavailable.')
    required = {transport['captions'], *(defaults or [transport['audio']])}
    subtitles = {t.get('LANGUAGE') for t in tracks if t.get('TYPE') == 'SUBTITLES'}
    if not required.issubset(subtitles):
        raise ValueError('Requested/native caption tracks are unavailable.')
    return required


def probe_local_video(path, max_height, audio_language, expected_seconds):
    from package_domestika import audio_language_tag
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)], capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
    streams = info['streams']
    video = [s for s in streams if s['codec_type'] == 'video']
    audio = [s for s in streams if s['codec_type'] == 'audio']
    duration = float(info['format']['duration'])
    if len(video) != 1 or not 0 < video[0]['height'] <= max_height or len(audio) != 1 or audio[0].get('tags', {}).get('language') != audio_language_tag(audio_language) or (expected_seconds is not None and abs(duration - expected_seconds) > max(8, expected_seconds * .03)):
        raise ValueError('Preserved media does not meet selected audio/height/duration.')
    return {'duration_seconds': duration, 'height': video[0]['height'], 'audio_language': audio_language}


def transfer(transport):
    kind = transport['kind']
    if kind == 'inline':
        return transport['content'].encode(), []
    if kind == 'local':
        return Path(transport['path']).read_bytes(), []
    if kind == 'git-blob':
        return git(transport['repo'], 'cat-file', 'blob', transport['blob']), []
    if kind == 'http':
        if urlsplit(transport['url']).scheme not in ('https', 'http'):
            raise ValueError('Only ordinary HTTP file URLs are permitted.')
        try:
            with urlopen(Request(transport['url'], headers={'User-Agent': 'archive-core/1'}), timeout=30) as response:
                return response.read(), []
        except OSError:
            raise ValueError('HTTP transfer failed (transport details suppressed).') from None
    if kind == 'playlist':
        if transport.get('fixture_media'):
            text = Path(transport['fixture_playlist']).read_text()
            required = playlist_probe(text, transport)
            media = Path(transport['fixture_media'])
            probe_local_video(media, transport['max_height'], transport['audio'], transport.get('duration_seconds'))
            return media.read_bytes(), []
        # The mature Domestika selector keeps language, duration and DRM policy.
        from package_domestika import preflight_lesson, download_lesson
        yt_dlp = shutil.which('yt-dlp')
        if not yt_dlp:
            raise ValueError('yt-dlp is required for streaming transport.')
        lesson = {'number': 1, 'media_url': transport['url'], 'duration_seconds': transport['duration_seconds']}
        _, captions, native = preflight_lesson(lesson, transport['max_height'], transport['audio'], transport['captions'], yt_dlp)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            download_lesson(lesson, path, 'media', transport['max_height'], transport['audio'], captions, native, yt_dlp)
            extra = [(p.read_bytes(), 'text/vtt', 'captions', p.stem.split('.')[-1]) for p in path.glob('*.vtt')]
            return (path / 'media.mp4').read_bytes(), extra
    raise ValueError('Unsupported transport.')
