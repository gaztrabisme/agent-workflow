"""Bridge verified legacy Domestika artifacts into the same core handoff."""
import copy
import os
import uuid
from pathlib import Path

from .core import run_archive
from .storage import save_json, load_json, digest, fingerprint
from .transports import probe_local_video


def emit_domestika_handoff(course, units, folders, caption_languages, output, *, reading_pdf=None, removal_log=None):
    from package_domestika import basename, caption_path, inspect_captions
    output = Path(output)
    if reading_pdf and (not removal_log or not Path(removal_log).is_file()):
        raise ValueError('English reading-copy handoff requires its removal log.')
    state = output / '.state'
    state.mkdir(parents=True, mode=0o700, exist_ok=True)
    os.chmod(state, 0o700)
    snapshot = copy.deepcopy(course)
    snapshot['adapter'] = 'domestika'
    snapshot['units'] = copy.deepcopy(units)
    snapshot['expected_units'] = len(units)
    snapshot['expected_lessons'] = sum(len(u['lessons']) for u in units)
    snapshot['scope'] = 'Domestika units: ' + ','.join(str(u['number']) for u in units)
    for unit in snapshot['units']:
        folder = Path(folders[unit['number']])
        pdf = folder / (folder.name + '.pdf')
        if pdf.is_file():
            unit['preserved_pdf'] = str(pdf.resolve())
        for lesson in unit['lessons']:
            stem = basename(lesson)
            media = folder / (stem + '.mp4')
            settings = load_json(folder / (stem + '.download.json'), {})
            policy = {'sha256': digest(media.read_bytes()), 'max_height': settings.get('max_height', lesson.get('max_height', 1080)),
                      'audio_language': settings.get('audio_language', lesson.get('requested_audio', 'en')), 'expected_seconds': lesson.get('duration_seconds'), 'profile': 'preserved-video/1'}
            marker = state / 'media-probes' / (fingerprint(policy) + '.json')
            measured = load_json(marker)
            if measured is None:
                measured = probe_local_video(media, policy['max_height'], policy['audio_language'], policy['expected_seconds'])
                save_json(marker, measured)
            lesson['verified_media'] = measured
            lesson['preserved_media'] = str(media.resolve())
            native = settings.get('default_language', caption_languages[lesson['id']][-1] if caption_languages[lesson['id']] else policy['audio_language'])
            if native not in caption_languages[lesson['id']] or not caption_languages[lesson['id']]:
                raise ValueError('Preserved requested/native captions are missing.')
            if not all(inspect_captions(caption_path(folder, stem, lang)) for lang in caption_languages[lesson['id']]):
                raise ValueError('Preserved caption files are missing or invalid.')
            lesson['captions'] = [{'path': str(caption_path(folder, stem, lang).resolve()), 'language': lang}
                                  for lang in caption_languages[lesson['id']]]
    if reading_pdf:
        snapshot['reading_copy_pdf'] = str(Path(reading_pdf).resolve())
        if removal_log and Path(removal_log).is_file():
            snapshot['reading_copy_removal_log'] = str(Path(removal_log).resolve())
    path = state / ('compatibility-' + uuid.uuid4().hex + '.json')
    save_json(path, snapshot)
    try:
        return run_archive(path, output)
    finally:
        path.unlink(missing_ok=True)
