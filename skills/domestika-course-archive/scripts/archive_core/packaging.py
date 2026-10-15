"""Shared ZIP verification and offline rendering preparation for compatibility tools."""
import base64
import html
import io
import re
import shutil
import zipfile
from pathlib import Path

from .privacy import scan_file, scan_text, scan_bytes
from .transports import transfer


def verified_zip(archive, files, *, preserve_existing=False):
    archive = Path(archive)
    temp = archive.with_name(archive.name + '.building')
    replacements = {member: Path(path) for member, path in files}
    if len(replacements) != len(files):
        raise ValueError('Duplicate ZIP members.')
    previous = []
    if preserve_existing:
        with zipfile.ZipFile(archive) as source:
            previous = [info for info in source.infolist() if info.filename not in replacements]
            if len({i.filename for i in previous}) != len(previous):
                raise ValueError('Duplicate existing ZIP members.')
    with zipfile.ZipFile(temp, 'w', allowZip64=True) as target:
        if preserve_existing:
            with zipfile.ZipFile(archive) as source:
                for info in previous:
                    with source.open(info) as reader, target.open(info, 'w', force_zip64=True) as writer:
                        shutil.copyfileobj(reader, writer, 1024 * 1024)
        for member, path in replacements.items():
            if not path.is_file():
                raise RuntimeError('Missing file before archiving.')
            scan_file(path)
            mode = zipfile.ZIP_STORED if path.suffix == '.mp4' else zipfile.ZIP_DEFLATED
            target.write(path, member, compress_type=mode)
    with zipfile.ZipFile(temp) as check:
        expected = {i.filename for i in previous} | set(replacements)
        if set(check.namelist()) != expected or len(check.namelist()) != len(expected) or check.testzip():
            raise RuntimeError('ZIP membership or CRC verification failed.')
    scan_file(temp)
    temp.replace(archive)


def localize_images(document):
    """Resolve ordinary images before rendering; signed links fail the common gate."""
    scan_text(document)
    pattern = re.compile(r'(<img\b[^>]*?\bsrc\s*=\s*)(["\'])(https?://[^"\']+)\2', re.I)
    def replace(match):
        url = html.unescape(match.group(3))
        data, _ = transfer({'kind': 'http', 'url': url})
        scan_bytes(data)
        from PIL import Image
        with Image.open(io.BytesIO(data)) as image:
            image.load()
            mime = Image.MIME.get(image.format)
            if not mime:
                raise ValueError('Remote image is not a supported raster format.')
        local = 'data:' + mime + ';base64,' + base64.b64encode(data).decode()
        return match.group(1) + match.group(2) + local + match.group(2)
    document = pattern.sub(replace, document)
    # Refuse any other remote-loading construct. Citation links remain usable.
    if re.search(r'(?:\b(?:src|srcset|poster)\s*=\s*["\']\s*https?://|url\(\s*["\']?https?://|<link\b[^>]*href\s*=\s*["\']https?://)', document, re.I):
        raise ValueError('Unlocalized remote rendering resource.')
    return document


def package_domestika_legacy(course, units, folders, caption_languages, archive):
    """Keep the existing file layout; packaging and privacy have one owner."""
    from package_domestika import basename, caption_path
    files = []
    for unit in units:
        folder = folders[unit['number']]
        paths = [folder / (folder.name + '.pdf')]
        for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
            stem = basename(lesson)
            paths.append(folder / (stem + '.mp4'))
            paths.extend(caption_path(folder, stem, language) for language in caption_languages[lesson['id']])
        files.extend((folder.name + '/' + path.name, path) for path in paths)
    verified_zip(archive, files)
