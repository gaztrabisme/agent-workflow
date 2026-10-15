"""Source policies and structure only. Core owns all transfer and packaging."""
import copy
import mimetypes
import os
import re
import subprocess
from pathlib import Path

from .normalize import normalize_asset


def media_type(path):
    return {'.epub': 'application/epub+zip', '.vtt': 'text/vtt', '.md': 'text/markdown', '.py': 'text/plain'}.get(Path(path).suffix, mimetypes.guess_type(path)[0] or 'application/octet-stream')


def asset(path=None, *, url=None, content=None, role='original', language=None, mime=None, **extra):
    descriptor = {'role': role, 'language': language, 'media_type': mime or media_type(path or url or 'file.txt'), **extra}
    if path is not None:
        descriptor['local_path'] = str(path)
    if url:
        descriptor['url'] = url
    if content is not None:
        descriptor['inline'] = content
    return descriptor


def member(member_id, title, order, descriptors=(), parent=None, access='accessible', facts=None, gaps=()):
    return {'member_id': str(member_id), 'title': title, 'parent_id': parent, 'order': order,
            'access': access, 'descriptors': list(descriptors), 'facts': facts or {}, 'gaps': list(gaps)}


class Adapter:
    name = None
    kind = None

    def __init__(self, data, base):
        self.data = copy.deepcopy(data)
        self.base = Path(base).resolve()

    def capabilities(self):
        return {'adapter': self.name, 'transports': ['local', 'http'], 'normalization': ['text', 'pdf', 'epub', 'captions'], 'executes_source': False}

    def collect(self, discovery):
        return discovery['items']

    def probe(self, item):
        if item['facts'].get('protected'):
            return 'unsupported', ['Protected media: no transfer permitted.']
        return item['access'], item['gaps']

    def resolve_transport(self, descriptor):
        if 'inline' in descriptor:
            return {'kind': 'inline', 'content': descriptor['inline']}
        if descriptor.get('local_path'):
            path = (self.base / descriptor['local_path']).resolve()
            return {'kind': 'local', 'path': str(path)}
        if descriptor.get('url'):
            return {'kind': 'http', 'url': descriptor['url']}
        raise ValueError('Asset has no permitted transport.')

    def normalize(self, data, record, item, descriptor):
        blocks, figures, pixels, status, facts = normalize_asset(data, record, item, descriptor)
        if descriptor.get('reuse_input_chunks'):
            blocks = []
        return blocks, figures, pixels, status, facts

    def source_checks(self, discovery):
        ids = [item['member_id'] for item in discovery['items']]
        if len(ids) != len(set(ids)):
            raise ValueError('Discovery returned duplicate member identities.')
        expected = discovery.get('expected')
        if discovery['authoritative'] and expected is not None and set(expected) != set(ids):
            raise ValueError('Authoritative discovery membership mismatch.')
        if not discovery['source_id']:
            raise ValueError('Stable logical source ID is required.')

    def envelope(self, items, **extra):
        data = self.data
        return {'source_id': data['source_id'], 'title': data.get('title', data['source_id']),
                'kind': self.kind, 'scope': data.get('scope', 'complete selected source'),
                'canonical_url': data.get('canonical_url'), 'aliases': data.get('aliases', []),
                'creators': data.get('creators', []), 'publication_date': data.get('publication_date'),
                'revision_date': data.get('revision_date'), 'source_revision': data.get('source_revision'),
                'privacy': data.get('privacy_scope', 'owner-private'),
                'authoritative': data.get('inventory_complete', True),
                'discovery_ok': data.get('discovery_ok', True),
                'expected': data.get('expected_membership', [i['member_id'] for i in items]),
                'items': items, 'gaps': data.get('gaps', []), **extra}


class Domestika(Adapter):
    name, kind = 'domestika', 'course'

    @staticmethod
    def package_legacy(course, units, folders, caption_languages, archive):
        from .packaging import package_domestika_legacy
        package_domestika_legacy(course, units, folders, caption_languages, archive)

    def capabilities(self):
        return {**super().capabilities(), 'transports': ['local', 'http', 'playlist'], 'legacy_cli': 'package_domestika.py'}

    def discover(self):
        data = self.data
        data.setdefault('source_id', 'domestika:' + str(data['course_id']))
        data.setdefault('title', data['course_title'])
        items = []
        for unit in sorted(data['units'], key=lambda u: u['number']):
            parent = 'unit:' + str(unit['number'])
            content = unit.get('intro_html', '') + ''.join(e['html'] for e in unit.get('extras', []))
            notes = [asset(content=content, mime='text/html', role='unit-notes')]
            if unit.get('preserved_pdf'):
                notes.append(asset(unit['preserved_pdf'], mime='application/pdf', role='unit-document', derivation='derived',
                                   transform_version='domestika-unit-layout/1', reuse_input_chunks=True,
                                   input_members=[parent, *['lesson:' + str(l['id']) for l in unit['lessons']]]))
            items.append(member(parent, unit['title'], len(items), notes))
            for lesson in sorted(unit['lessons'], key=lambda l: l['number']):
                descriptors = []
                if lesson.get('transcript_html'):
                    descriptors.append(asset(content=lesson['transcript_html'], mime='text/html', role='transcript'))
                if lesson.get('preserved_media'):
                    descriptors.append(asset(lesson['preserved_media'], mime='video/mp4', role='video'))
                elif lesson.get('media_url'):
                    descriptors.append(asset(lesson.get('media_fixture'), url=lesson['media_url'], mime='video/mp4', role='video',
                                             playlist=True, requested_audio=lesson.get('requested_audio', 'en'),
                                             requested_captions=lesson.get('requested_captions', 'en'),
                                             max_height=lesson.get('max_height', 1080), duration_seconds=lesson.get('duration_seconds'),
                                             playlist_fixture=lesson.get('playlist_fixture')))
                for caption in lesson.get('captions', []):
                    descriptors.append(asset(caption.get('path'), url=caption.get('url'), mime='text/vtt', role='captions', language=caption['language']))
                items.append(member('lesson:' + str(lesson['id']), lesson['title'], len(items), descriptors, parent,
                                    lesson.get('access', 'accessible'), {'duration_seconds': lesson.get('duration_seconds'), 'protected': lesson.get('protected', False), 'verified_media': lesson.get('verified_media')}))
        if data.get('reading_copy_pdf') and items:
            items[0]['descriptors'].append(asset(data['reading_copy_pdf'], mime='application/pdf', role='reading-copy', language='en', derivation='translation',
                                                 transform_version='domestika-native-reading-copy/1', input_members=[i['member_id'] for i in items]))
            if data.get('reading_copy_removal_log'):
                items[0]['descriptors'].append(asset(data['reading_copy_removal_log'], mime='text/plain', role='removal-log', reuse_input_chunks=True))
        if data.get('expected_units') is not None and len(data['units']) != data['expected_units']:
            raise ValueError('Domestika unit discovery is incomplete.')
        lessons = sum(len(u['lessons']) for u in data['units'])
        if data.get('expected_lessons') is not None and lessons != data['expected_lessons']:
            raise ValueError('Domestika lesson discovery is incomplete.')
        return self.envelope(items)

    def resolve_transport(self, descriptor):
        if descriptor.get('playlist'):
            transport = {'kind': 'playlist', 'url': descriptor['url'], 'audio': descriptor['requested_audio'],
                         'captions': descriptor['requested_captions'], 'max_height': descriptor['max_height'],
                         'duration_seconds': descriptor['duration_seconds']}
            if descriptor.get('local_path'):
                transport['fixture_media'] = str((self.base / descriptor['local_path']).resolve())
            if descriptor.get('playlist_fixture'):
                transport['fixture_playlist'] = str((self.base / descriptor['playlist_fixture']).resolve())
            return transport
        return super().resolve_transport(descriptor)


class Coursera(Adapter):
    name, kind = 'coursera', 'course'

    def discover(self):
        items = []
        for module in self.data['modules']:
            parent = 'module:' + module['id']
            items.append(member(parent, module['name'], len(items), facts={'type': 'module'}))
            for activity in module['items']:
                access = 'locked' if activity.get('isLocked') else 'accessible'
                descriptors, gaps = [], []
                kind = activity['typeName']
                if kind == 'reading':
                    body = activity.get('content', {})
                    if 'ungradedWidget' in str(body):
                        access, gaps = ('locked' if access == 'locked' else 'unresolved'), ['Embedded ungradedWidget reading remains unresolved.']
                    else:
                        descriptors.append(asset(content=body.get('html', ''), mime='text/html', role='reading'))
                elif kind == 'lecture':
                    for file in activity.get('files', []):
                        descriptors.append(asset(file.get('path'), url=file.get('downloadUrl'), mime=file.get('mediaType'),
                                                 role=file['role'], language=file.get('language'), sha256=file.get('sha256')))
                else:
                    access = 'locked' if access == 'locked' else 'unsupported'
                    gaps.append('Unsupported activity type: ' + kind)
                items.append(member('activity:' + activity['id'], activity['name'], len(items), descriptors, parent,
                                    access, {'type': kind}, gaps))
        return self.envelope(items)


class Book(Adapter):
    name, kind = 'book', 'book'

    def discover(self):
        items = [member(f['id'], f.get('title', Path(f['path']).name), i,
                        [asset(f['path'], role='book', mime=media_type(f['path']), language=f.get('language'), derivation=f.get('derivation', 'original'), transform_version=f.get('transform_version', 'supplied-source/1'), input_members=f.get('input_members', []))],
                        facts={'edition': f.get('edition'), 'edition_reason': None if f.get('edition') else 'not found'})
                 for i, f in enumerate(self.data['files'])]
        return self.envelope(items)


class Paper(Adapter):
    name, kind = 'paper', 'paper'

    def discover(self):
        data = self.data
        if data.get('arxiv'):
            if not re.fullmatch(r'(?:\d{4}\.\d{4,5}|[a-z-]+/\d{7})v\d+', data['arxiv']):
                raise ValueError('Paper requires an exact arXiv version.')
            logical = data['arxiv'].rsplit('v', 1)[0]
            data.setdefault('source_id', 'arxiv:' + logical)
            data.setdefault('source_revision', 'arxiv:' + data['arxiv'])
            data.setdefault('canonical_url', 'https://arxiv.org/abs/' + data['arxiv'])
            data.setdefault('aliases', [{'namespace': 'arxiv', 'value': logical}, {'namespace': 'arxiv-version', 'value': data['arxiv']}])
        elif data.get('doi'):
            data.setdefault('source_id', 'doi:' + data['doi'])
            data.setdefault('source_revision', 'doi:' + data['doi'])
            data.setdefault('canonical_url', 'https://doi.org/' + data['doi'])
            data.setdefault('aliases', [{'namespace': 'doi', 'value': data['doi']}])
        else:
            raise ValueError('Paper requires arXiv version or DOI.')
        items = [member('abstract', 'Abstract', 0, [asset(content=data.get('abstract', ''), mime='text/plain', role='abstract')])]
        for file in data.get('files', []):
            items.append(member(file['id'], file.get('title', 'Paper full text'), len(items),
                                [asset(file.get('path'), url=file.get('url'), mime=file.get('media_type') or media_type(file.get('path') or file['url']), role='paper')]))
        gaps = list(data.get('gaps', []))
        if len(items) == 1:
            gaps.append('Abstract-only paper; full text not found.')
        return self.envelope(items, gaps=gaps)


def git(repo, *args):
    # These read-only Git plumbing commands never check out or execute source code.
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    env.update({'GIT_NO_LAZY_FETCH': '1', 'GIT_NO_REPLACE_OBJECTS': '1',
                'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull,
                'GIT_TERMINAL_PROMPT': '0'})
    return subprocess.check_output(['git', '--no-optional-locks', '-c', 'core.hooksPath=/dev/null',
                                    '-c', 'core.fsmonitor=false', '-c', 'protocol.allow=never',
                                    '-c', 'protocol.ext.allow=never', '-c', 'credential.helper=',
                                    '-C', str(repo), *args], env=env, stderr=subprocess.DEVNULL)


class Repository(Adapter):
    name, kind = 'repository', 'repository'

    def capabilities(self):
        return {**super().capabilities(), 'transports': ['git-blob'], 'executes_source': False}

    def discover(self):
        repo = (self.base / self.data['repo']).resolve()
        revision = self.data['commit']
        if not re.fullmatch(r'[a-f0-9]{40}|[a-f0-9]{64}', revision):
            raise ValueError('Repository requires an exact commit hash.')
        actual = git(repo, 'rev-parse', revision + '^{commit}').decode().strip()
        if actual != revision:
            raise ValueError('Repository commit does not resolve exactly.')
        inventory = []
        for entry in git(repo, 'ls-tree', '-rz', revision).split(b'\0'):
            if entry:
                metadata, name = entry.split(b'\t', 1)
                mode, kind, blob = metadata.decode().split()
                inventory.append((name.decode(), mode, kind, blob))
        selected = self.data.get('files')
        if selected is None:
            selected = [name for name, *_ in inventory]
        if not set(selected).issubset({name for name, *_ in inventory}):
            raise ValueError('Selected repository files are not in the exact commit.')
        items = []
        for name, mode, kind, blob in inventory:
            if name not in selected:
                continue
            descriptor = {'repo': str(repo), 'commit': revision, 'repo_path': name, 'blob': blob, 'role': 'source-file',
                          'media_type': 'text/plain', 'language': None}
            supported = kind == 'blob' and mode in ('100644', '100755')
            items.append(member('file:' + name, name, len(items), [descriptor] if supported else [],
                                access='accessible' if supported else 'unsupported', facts={'mode': mode, 'git_blob': blob, 'commit': revision},
                                gaps=[] if supported else ['Symlink or submodule retained without dereferencing.']))
        self.data['source_revision'] = revision
        self.data.setdefault('scope', 'repository files: ' + ','.join(sorted(selected)))
        return self.envelope(items)

    def resolve_transport(self, descriptor):
        return {'kind': 'git-blob', 'repo': descriptor['repo'], 'commit': descriptor['commit'],
                'path': descriptor['repo_path'], 'blob': descriptor['blob']}


ADAPTERS = {a.name: a for a in [Domestika, Coursera, Book, Paper, Repository]}
