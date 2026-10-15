"""Durable file operations and jail checks shared by all adapters."""
import hashlib
import json
import os
import uuid
from pathlib import Path, PurePosixPath


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()


def fingerprint(value):
    return digest(canonical(value))


def safe_path(root, relative):
    part = PurePosixPath(relative)
    if not relative or part.is_absolute() or '..' in part.parts or '\\' in relative:
        raise ValueError('Unsafe relative archive path.')
    root = Path(root).resolve()
    result = root / relative
    if not result.resolve().is_relative_to(root):
        raise ValueError('Archive path escapes its root.')
    if any(p.is_symlink() for p in [result, *result.parents] if p != root.parent):
        raise ValueError('Archive path may not traverse symlinks.')
    return result


def atomic_bytes(path, data, mode=0o600):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, mode)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)
    fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def save_json(path, value):
    atomic_bytes(path, canonical(value) + b'\n')


def load_json(path, default=None):
    return json.loads(Path(path).read_text()) if Path(path).exists() else default


def blob_record(data, media_type, role, language=None):
    sha = digest(data)
    return {'asset_id': 'sha256:' + sha, 'path': 'blobs/' + sha, 'sha256': sha,
            'bytes': len(data), 'media_type': media_type, 'role': role, 'language': language}
