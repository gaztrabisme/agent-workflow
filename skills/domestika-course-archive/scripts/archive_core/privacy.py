"""One release privacy gate, including compressed and rendered content."""
import html
import io
import re
import zipfile
import tempfile
import shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit, parse_qsl


class PrivacyError(ValueError):
    pass


SENSITIVE = re.compile(r'(?:signature|(?:^|[-_])sig$|token|credential|authorization|cookie|api[-_]?key|policy|key[-_]?pair[-_]?id|^expires$|^jwt$|^auth$|^hdnea$|^hdnts$)', re.I)
URL = re.compile(r'https?://[^\s<>"\'`\\]+', re.I)


def decode_for_scan(value):
    # Decode HTML entities and nested percent encodings before inspecting URLs.
    text = str(value)
    for _ in range(4):
        decoded = html.unescape(unquote(text)).replace('\\u0026', '&').replace('\\/', '/')
        if decoded == text:
            break
        text = decoded
    text = text.replace('\\n', '').replace('\\r', '')
    return text


def scan_text(value):
    text = decode_for_scan(value)
    text = text + '\n' + re.sub(r'\s*\n\s*', '', text)
    for match in URL.finditer(text):
        url = urlsplit(match.group().rstrip(').,;]}'))
        if url.username or url.password:
            raise PrivacyError('Release contains a URL credential (value suppressed).')
        parameters = parse_qsl(url.query, keep_blank_values=True) + parse_qsl(url.fragment.split('?', 1)[-1], keep_blank_values=True)
        if any(SENSITIVE.search(k) for k, _ in parameters):
            raise PrivacyError('Release contains a signed or token URL (value suppressed).')
    # Never serialize credential fields even when they are not embedded in URLs.
    if re.search(r'"(?:cookies?|access_token|refresh_token|authorization|api_key)"\s*:', text, re.I):
        raise PrivacyError('Release contains a credential field (value suppressed).')


def scan_bytes(data, depth=0):
    if depth > 8:
        raise PrivacyError('Release compression nesting exceeds scan limit.')
    scan_text(data.decode('utf-8', 'replace'))
    if zipfile.is_zipfile(io.BytesIO(data)):
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            scan_zip(archive, depth)
    if data.startswith(b'%PDF'):
        import fitz
        with fitz.open(stream=data, filetype='pdf') as document:
            scan_text(document.metadata)
            for page in document:
                scan_text(page.get_text())
                scan_text(page.get_links())
                for annotation in page.annots() or []:
                    scan_text(annotation.info)
            for xref in range(1, document.xref_length()):
                scan_text(document.xref_object(xref))
                if document.xref_is_stream(xref):
                    scan_text(document.xref_stream(xref).decode('utf-8', 'replace'))
            for name in document.embfile_names():
                scan_bytes(document.embfile_get(name), depth + 1)


def scan_zip(archive, depth=0):
    if depth > 8:
        raise PrivacyError('Release compression nesting exceeds scan limit.')
    scan_text(archive.comment.decode('utf-8', 'replace'))
    for info in archive.infolist():
        scan_text(info.filename)
        scan_text(info.comment.decode('utf-8', 'replace'))
        scan_text(info.extra.decode('utf-8', 'replace'))
        if info.file_size > 64 * 1024 * 1024 and info.file_size > max(1, info.compress_size) * 1000:
            raise PrivacyError('Release contains an excessive decompression ratio.')
        with archive.open(info) as stream:
            if info.file_size <= 64 * 1024 * 1024:
                scan_bytes(stream.read(), depth + 1)
            else:
                prefix = stream.read(8)
                if prefix.startswith((b'%PDF', b'PK')):
                    with tempfile.TemporaryDirectory(prefix='archive-scan-') as directory:
                        path = Path(directory) / 'member'
                        with path.open('wb') as target:
                            target.write(prefix)
                            shutil.copyfileobj(stream, target, 1024 * 1024)
                        scan_file(path, depth=depth + 1)
                else:
                    scan_stream(stream, prefix)


def scan_stream(stream, carry=b''):
    while True:
        block = stream.read(1024 * 1024)
        if not block:
            scan_text(carry.decode('utf-8', 'replace'))
            break
        combined = carry + block
        scan_text(combined.decode('utf-8', 'replace'))
        decoded = decode_for_scan(combined.decode('utf-8', 'replace'))
        matches = list(URL.finditer(decoded))
        unfinished = matches[-1].group() if matches and matches[-1].end() == len(decoded) else ''
        if len(unfinished) > 65536:
            raise PrivacyError('Unterminated release URL exceeds scan limit.')
        starts = list(re.finditer(rb'https?(?::|%3a|%253a|%25253a|%2525253a)', combined, re.I))
        carry = combined[starts[-1].start():] if unfinished and starts else combined[-16384:]
        if len(carry) > 8 * 1024 * 1024:
            raise PrivacyError('Encoded unfinished release URL exceeds scan limit.')


def scan_file(path, *, depth=0):
    path = Path(path)
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as archive:
            scan_zip(archive, depth)
        return
    with path.open('rb') as stream:
        prefix = stream.read(8)
        if prefix.startswith(b'%PDF'):
            scan_bytes(prefix + stream.read(), depth)
        else:
            scan_stream(stream, prefix)


def scan_release(root, *, verified_hashes=frozenset()):
    for path in Path(root).rglob('*'):
        if path.is_symlink():
            raise PrivacyError('Release may not contain symlinks.')
        if path.is_file():
            from .storage import digest
            if digest(path.read_bytes()) not in verified_hashes:
                scan_file(path)
