"""Offline, artifact-level acceptance for the five archive adapters."""
import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from archive_core.adapters import ADAPTERS
from archive_core.contracts import validate, validate_release
from archive_core.core import run_archive, current_release, install_release
from archive_core.normalize import resolve
from archive_core.privacy import PrivacyError, scan_text, scan_file, scan_release
from archive_core.storage import load_json, save_json, digest, safe_path

FIXTURES = ROOT / 'tests/fixtures/archive'
CLI = ROOT / 'scripts/archive.py'
EXPECTED = {
    'domestika': ['unit:1', 'lesson:11', 'unit:2', 'lesson:12'],
    'coursera-progressive': ['module:m1', 'activity:v1', 'activity:r1', 'activity:r2', 'activity:q1'],
    'coursera-locked': ['module:m1', 'activity:v1', 'activity:r1', 'activity:r2', 'activity:q1'],
    'book': ['pdf', 'epub'], 'paper': ['abstract', 'pdf'], 'paper-abstract': ['abstract'],
    'repository': ['file:README.md', 'file:danger.py', 'file:src/helper.txt'],
}


def create_repo(root):
    repo = root / 'repo'
    repo.mkdir()
    env = {**os.environ, 'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull,
           'GIT_AUTHOR_NAME': 'Archive Fixture', 'GIT_AUTHOR_EMAIL': 'archive@example.invalid',
           'GIT_COMMITTER_NAME': 'Archive Fixture', 'GIT_COMMITTER_EMAIL': 'archive@example.invalid',
           'GIT_AUTHOR_DATE': '2024-01-01T00:00:00+0000', 'GIT_COMMITTER_DATE': '2024-01-01T00:00:00+0000'}
    def git(*args):
        return subprocess.check_output(['git', '-c', 'core.hooksPath=/dev/null', '-c', 'commit.gpgsign=false', '-C', str(repo), *args], env=env, stderr=subprocess.DEVNULL).decode().strip()
    git('init', '-b', 'fixture', '--template=')
    (repo / 'README.md').write_text('# Fixture repository\nRead these exact committed lines.\n')
    (repo / 'danger.py').write_text('from pathlib import Path\nPath("EXECUTED").write_text("must never execute")\n')
    (repo / 'src').mkdir()
    (repo / 'src/helper.txt').write_text('Stable inert text.\nSecond line.\n')
    git('add', 'README.md', 'danger.py', 'src/helper.txt')
    git('commit', '-m', 'Deterministic archive fixture')
    commit = git('rev-parse', 'HEAD')
    if commit != 'e763a86a3686e6592e01eb46de349630270a00ec':
        raise AssertionError('Fixture commit differs from the fixed acceptance revision: ' + commit)
    save_json(root / 'repository.json', {'adapter': 'repository', 'source_id': 'repository:fixture', 'title': 'Inert repository fixture', 'repo': 'repo', 'commit': commit})
    return commit


class ArchiveAcceptance(unittest.TestCase):
    def setUp(self):
        artifacts = os.environ.get('ARCHIVE_ACCEPT_DIR')
        if artifacts:
            self.work = Path(tempfile.mkdtemp(prefix=self._testMethodName + '-', dir=artifacts))
        else:
            directory = tempfile.TemporaryDirectory()
            self.addCleanup(directory.cleanup)
            self.work = Path(directory.name)
        self.inputs = self.work / 'inputs'
        shutil.copytree(FIXTURES, self.inputs)
        self.commit = create_repo(self.inputs)

    def run_source(self, name, output=None):
        output = output or self.work / name
        result = run_archive(self.inputs / (name + '.json'), output)
        release = Path(result['release'])
        return result, load_json(release / 'manifest.json'), release

    def test_every_adapter_membership_locators_reuse_and_sanitized_handoff(self):
        for name, expected in EXPECTED.items():
            with self.subTest(adapter=name):
                result, manifest, release = self.run_source(name)
                self.assertEqual(manifest['ordered_membership'], expected)
                self.assertEqual(result['metrics']['added'], len(expected))
                self.assertEqual(result['metrics']['changed'], 0)
                checked = validate_release(release)
                self.assertEqual(checked['members'], len(expected))
                self.assertEqual(checked['state'], 'pending')
                for item in manifest['items']:
                    assets = {a['asset_id']: a for a in item['assets']}
                    for a in assets.values():
                        self.assertEqual(digest((release / a['path']).read_bytes()), a['sha256'])
                    for b in item['blocks']:
                        data = (release / assets[b['asset_id']]['path']).read_bytes()
                        self.assertEqual(resolve(data, b['locator']), b['text'])
                # Instrument the actual expensive normalization and transfer seams.
                with patch('archive_core.contracts.normalize_asset', side_effect=AssertionError('Rerun verification reparsed bytes')), patch('fitz.open', side_effect=AssertionError('Rerun reparsed a verified PDF')), patch('archive_core.core.transfer', side_effect=AssertionError('Rerun transferred unchanged bytes')), patch.object(ADAPTERS[manifest['adapter']], 'normalize', side_effect=AssertionError('Rerun parsed unchanged bytes')):
                    rerun, again, _ = self.run_source(name)
                self.assertEqual(rerun['metrics'], {'added': 0, 'changed': 0, 'reused': len(expected), 'quarantined': 0, 'removed': 0, 'new_transfers': 0, 'new_parses': 0})
                self.assertEqual(again['source'], manifest['source'])
                if name == 'domestika':
                    self.assertEqual(manifest['items'][-1]['access'], 'locked')
                    languages = {a['language'] for i in manifest['items'] for a in i['assets'] if a['role'] == 'captions'}
                    self.assertEqual(languages, {'es', 'en'})
                elif name == 'coursera-progressive':
                    self.assertEqual([i['access'] for i in manifest['items'][-2:]], ['unresolved', 'locked'])
                    self.assertEqual(manifest['expected_count'], {'value': None, 'reason': 'not found'})
                elif name == 'coursera-locked':
                    self.assertTrue(all(i['access'] == 'locked' for i in manifest['items'][1:]))
                elif name == 'book':
                    self.assertEqual(manifest['items'][0]['extraction_status'], 'ocr-required')
                    self.assertEqual([b['locator']['page'] for b in manifest['items'][0]['blocks']], [1, 2])
                    self.assertEqual([b['locator']['reading_order'] for b in manifest['items'][1]['blocks']], [0, 1])
                    self.assertEqual(len(manifest['items'][0]['figures']), 4)
                    self.assertLess(len({f['image_asset_id'] for f in manifest['items'][0]['figures']}), 4)
                    self.assertEqual(len(manifest['items'][1]['figures']), 2)
                    for figure in manifest['items'][1]['figures']:
                        source = next(a for a in manifest['items'][1]['assets'] if a['asset_id'] == figure['asset_id'])
                        image = next(a for a in manifest['items'][1]['assets'] if a['asset_id'] == figure['image_asset_id'])
                        self.assertEqual(resolve((release / source['path']).read_bytes(),figure['locator']),(release / image['path']).read_bytes())
                elif name == 'paper-abstract':
                    self.assertEqual(manifest['archive_state'], 'partial')
                elif name == 'repository':
                    self.assertEqual(manifest['source']['source_revision'], self.commit)
                    self.assertFalse((self.inputs / 'repo/EXECUTED').exists())
                print('PROVED', name, 'expected=', expected, 'actual=', manifest['ordered_membership'], 'rerun=', rerun['metrics'], 'release=', release)

    def test_interruption_recovery_every_adapter_repeated_kills(self):
        for name in ['domestika', 'coursera-progressive', 'book', 'paper', 'repository']:
            for boundary in ['after-transfer', 'after-parse', 'before-publish']:
                with self.subTest(adapter=name, kill=boundary):
                    output = self.work / (name + '-' + boundary)
                    env = {**os.environ, 'ARCHIVE_KILL_AT': boundary}
                    run = subprocess.run([sys.executable, str(CLI), 'run', str(self.inputs / (name + '.json')), '--output', str(output)], env=env, capture_output=True)
                    self.assertEqual(run.returncode, -9, run.stderr)
                    self.assertFalse((output / 'CURRENT').exists())
                    self.assertFalse((output / 'releases').exists())
                    before = {str(p.relative_to(output)): digest(p.read_bytes()) for p in (output / '.state/transfers').glob('*.json')}
                    result, manifest, release = self.run_source(name, output)
                    after = {str(p.relative_to(output)): digest(p.read_bytes()) for p in (output / '.state/transfers').glob('*.json')}
                    self.assertTrue(before.items() <= after.items())
                    self.assertEqual(manifest['ordered_membership'], EXPECTED[name])
                    validate_release(release)
                    if boundary == 'before-publish':
                        self.assertEqual(result['metrics']['new_transfers'], 0)
                        self.assertEqual(result['metrics']['new_parses'], 0)
                    elif boundary == 'after-parse':
                        self.assertGreaterEqual(len(list((output / '.state/parses').glob('*.json'))), 1)
                    # Repeating the same run proves recovered records become reusable.
                    again, _, _ = self.run_source(name, output)
                    self.assertEqual((again['metrics']['new_transfers'], again['metrics']['new_parses']), (0, 0))
                    print('PROVED interruption_recovery', name, boundary, result['metrics'])

    def test_failed_discovery_never_deletes_and_narrower_selection_preserves(self):
        _, original, release = self.run_source('book')
        output = self.work / 'book'
        pointer = (output / 'CURRENT').read_bytes()
        path = self.inputs / 'book.json'
        data = load_json(path)
        bad = copy.deepcopy(data)
        bad['expected_membership'] = ['pdf', 'epub', 'missing']
        save_json(path, bad)
        with self.assertRaises(ValueError):
            run_archive(path, output)
        self.assertEqual((output / 'CURRENT').read_bytes(), pointer)
        validate_release(release)
        bad = copy.deepcopy(data); bad['discovery_ok'] = False
        save_json(path, bad)
        failed = run_archive(path, output)
        preserved = load_json(Path(failed['release']) / 'manifest.json')
        self.assertEqual(preserved['ordered_membership'], original['ordered_membership'])
        self.assertEqual(failed['metrics']['removed'], 0)
        self.assertEqual(failed['metrics']['quarantined'], 2)
        narrow = copy.deepcopy(data); narrow['files'] = data['files'][:1]; narrow['scope'] = 'PDF only'
        save_json(path, narrow)
        narrowed = run_archive(path, output)
        narrow_manifest = load_json(Path(narrowed['release']) / 'manifest.json')
        self.assertEqual(narrow_manifest['ordered_membership'], ['pdf', 'epub'])
        self.assertEqual(narrowed['metrics']['removed'], 0)
        self.assertTrue(release.exists())
        second = run_archive(path, output)
        self.assertEqual(second['metrics']['removed'], 0)
        self.assertEqual(load_json(Path(second['release']) / 'manifest.json')['ordered_membership'], ['pdf', 'epub'])

    def test_authoritative_same_scope_removal_tombstones_retains_bytes(self):
        _, old, previous = self.run_source('book')
        path = self.inputs / 'book.json'
        data = load_json(path); data['files'] = data['files'][:1]
        save_json(path, data)
        result, manifest, release = self.run_source('book')
        self.assertEqual(result['metrics']['removed'], 1)
        self.assertEqual(manifest['ordered_membership'], ['pdf'])
        removed = next(i for i in manifest['items'] if i['member_id'] == 'epub')
        self.assertEqual(removed['state'], 'tombstone')
        self.assertTrue(all((release / a['path']).exists() for a in removed['assets']))
        self.assertTrue(previous.exists())

    def test_lost_access_keeps_prior_evidence(self):
        _, old, _ = self.run_source('coursera-progressive')
        path = self.inputs / 'coursera-progressive.json'
        data = load_json(path); data['modules'][0]['items'][0]['isLocked'] = True
        save_json(path, data)
        result, manifest, release = self.run_source('coursera-progressive')
        item = manifest['items'][1]
        self.assertEqual(item['access'], 'locked')
        self.assertEqual(item['state'], 'quarantined')
        self.assertEqual(item['blocks'], old['items'][1]['blocks'])
        self.assertEqual(result['metrics']['quarantined'], 1)
        validate_release(release)

    def test_changed_asset_only_reparses_changed_member(self):
        self.run_source('repository')
        # A source version change with unchanged selected blobs reuses the unchanged members.
        path = self.inputs / 'book.json'
        self.run_source('book')
        import fitz
        pdf = self.inputs / 'book.pdf'
        with fitz.open(pdf) as document:
            document[0].insert_text((50,350), 'New source content.')
            document.save(self.inputs / 'changed.pdf')
        (self.inputs / 'changed.pdf').replace(pdf)
        result, manifest, _ = self.run_source('book')
        self.assertEqual({k: result['metrics'][k] for k in ['added','changed','reused','quarantined','removed','new_transfers','new_parses']},
                         {'added':0,'changed':1,'reused':1,'quarantined':0,'removed':0,'new_transfers':1,'new_parses':1})

    def test_repository_readme_only_stays_selected_commit_and_scope(self):
        path = self.inputs / 'repository.json'
        data = load_json(path); data['files'] = ['README.md']
        save_json(path, data)
        # Dirty working files are irrelevant: locators refer to the commit blob.
        (self.inputs / 'repo/README.md').write_text('Changed working tree\n')
        _, manifest, _ = self.run_source('repository')
        self.assertEqual(manifest['ordered_membership'], ['file:README.md'])
        self.assertIn('exact committed lines', manifest['items'][0]['blocks'][0]['text'])
        self.assertEqual(manifest['source']['selected_scope'], 'repository files: README.md')
        self.assertFalse((self.inputs / 'repo/EXECUTED').exists())

    def test_sanitized_manifest_scan_rejects_nested_and_rendered_secrets(self):
        for url in ['https://example.invalid/file?Signature=SYNTHETIC', 'https://example.invalid/file?X-Amz-Signature=SYNTHETIC',
                    'https://example.invalid/file?access_token=SYNTHETIC', 'https://example.invalid/file?a=1&amp;token=SYNTHETIC',
                    'https://example.invalid/#access_token=SYNTHETIC', 'https://example.invalid/file?\ntoken=SYNTHETIC',
                    'https%3A%2F%2Fexample.invalid%2Ffile%3Ftoken%3DSYNTHETIC']:
            with self.subTest(url_kind=url.split('?')[0]):
                with self.assertRaises(PrivacyError): scan_text({'nested': [url]})
        import fitz
        pdf = self.work / 'secret.pdf'
        doc = fitz.open(); page = doc.new_page(); page.insert_text((50,50),'https://example.invalid/file?token=SYNTHETIC'); doc.save(pdf,deflate=True); doc.close()
        with self.assertRaises(PrivacyError): scan_file(pdf)
        doc = fitz.open(); page = doc.new_page(); page.insert_text((50,50),'Safe visible label'); page.insert_link({'kind':fitz.LINK_URI,'from':fitz.Rect(50,40,160,60),'uri':'https://example.invalid/file?signature=SYNTHETIC'}); doc.save(self.work/'linked.pdf',deflate=True); doc.close()
        with self.assertRaises(PrivacyError): scan_file(self.work/'linked.pdf')
        _, _, release = self.run_source('paper')
        (release / 'report.txt').write_text('https://example.invalid/file?token=SYNTHETIC')
        with self.assertRaises(PrivacyError): scan_release(release)

    def test_transport_projection_restricted_never_released(self):
        path = self.inputs / 'coursera-progressive.json'
        data = load_json(path)
        data['modules'][0]['items'][0]['files'][0]['downloadUrl'] += '?token=SYNTHETIC'
        save_json(path, data)
        _, manifest, release = self.run_source('coursera-progressive')
        self.assertNotIn('SYNTHETIC', json.dumps(manifest))
        state = self.work / 'coursera-progressive/.state'
        self.assertIn('SYNTHETIC', (state/'transport.json').read_text())
        self.assertEqual(state.stat().st_mode & 0o777, 0o700)
        self.assertEqual((state/'transport.json').stat().st_mode & 0o777, 0o600)
        self.assertFalse(any('transport' in p.name for p in release.rglob('*')))
        scan_release(release)

    def test_release_install_preserves_outbox_and_archive_staging(self):
        _, _, release = self.run_source('paper')
        target = self.work / 'installed'
        (target/'outbox').mkdir(parents=True)
        (target/'outbox/draft.json').write_text('{"draft":"unsent"}')
        (target/'.state/staging').mkdir(parents=True)
        (target/'.state/staging/completed-transfer').write_bytes(b'resumable')
        before = [(target/'outbox/draft.json').read_bytes(), (target/'.state/staging/completed-transfer').read_bytes()]
        installed = install_release(release, target)
        self.assertEqual(before, [(target/'outbox/draft.json').read_bytes(), (target/'.state/staging/completed-transfer').read_bytes()])
        validate_release(installed)
        self.assertEqual(current_release(target), Path(installed))
        (Path(installed)/'manifest.json').write_text('{}')
        with self.assertRaises(Exception): install_release(release,target)

    def test_handoff_rejects_hash_membership_paths_and_fake_receipt(self):
        _, _, release = self.run_source('paper')
        handoff_path = release/'kb-handoff.json'
        handoff = load_json(handoff_path)
        for mutation in ['hash','membership','path','receipt','role']:
            bad = copy.deepcopy(handoff)
            if mutation == 'hash': bad['blobs'][0]['sha256'] = '0'*64
            elif mutation == 'membership': bad['ordered_membership'] = ['invented']
            elif mutation == 'path': bad['blobs'][0]['path'] = '../outside'
            elif mutation == 'receipt': bad['state'] = 'completed'
            elif mutation == 'role':
                from archive_core.contracts import file_record
                bad['manifest'] = file_record(release, 'reading-copy.md')
            save_json(handoff_path,bad)
            with self.assertRaises((ValueError, FileNotFoundError, __import__('jsonschema').ValidationError)): validate_release(release)
            save_json(handoff_path,handoff)
        with self.assertRaises(ValueError): safe_path(release, '../outside')
        outside = self.work/'outside'; outside.write_text('x')
        (release/'symlink').symlink_to(outside)
        with self.assertRaises(PrivacyError): scan_release(release)

    def test_adapter_operation_interface_and_offline_recordings(self):
        required = ['capabilities','discover','collect','probe','resolve_transport','normalize','source_checks']
        for adapter in ADAPTERS.values():
            self.assertTrue(all(callable(getattr(adapter,name,None)) for name in required))
        page = (FIXTURES/'domestika-unit.html').read_text()
        self.assertIn('window.__INITIAL_PROPS__ = JSON.parse(',page)
        self.assertIn('course_lesson_11',page)
        playlist = (FIXTURES/'master.m3u8').read_text()
        self.assertIn('DEFAULT=YES',playlist)
        self.assertIn('TYPE=SUBTITLES',playlist)
        self.assertIn('ungradedWidget',(FIXTURES/'coursera-page.html').read_text())
        self.assertLess(sum(p.stat().st_size for p in (ROOT/'tests/fixtures').rglob('*') if p.is_file()), 5*1024*1024)

    def test_playlist_fixture_rejects_wrong_audio_duration_and_protection(self):
        from archive_core.transports import transfer
        base = {'kind':'playlist','fixture_media':str(FIXTURES/'lesson.mp4'),'fixture_playlist':str(FIXTURES/'master.m3u8'),'audio':'en','captions':'en','max_height':1080,'duration_seconds':1}
        transfer(base)
        for field,value in [('audio','es'),('duration_seconds',3600),('max_height',100)]:
            with self.subTest(field=field), self.assertRaises(ValueError): transfer({**base,field:value})
        playlist=self.work/'protected.m3u8';playlist.write_text((FIXTURES/'master.m3u8').read_text()+'\n#EXT-X-KEY:METHOD=AES-128,URI="synthetic-key"\n')
        with self.assertRaises(ValueError):transfer({**base,'fixture_playlist':str(playlist)})

    def test_http_direct_download_recording_and_query_content_identity(self):
        import io
        from archive_core.transports import transport_identity
        self.assertNotEqual(transport_identity({'kind':'http','url':'https://example.invalid/article?id=A'}),transport_identity({'kind':'http','url':'https://example.invalid/article?id=B'}))
        self.assertEqual(transport_identity({'kind':'http','url':'https://example.invalid/article?id=A&token=SYNTHETIC-A'}),transport_identity({'kind':'http','url':'https://example.invalid/article?id=A&token=SYNTHETIC-B'}))
        path=self.inputs/'coursera-progressive.json';data=load_json(path)
        expected={}
        for f in data['modules'][0]['items'][0]['files']:
            payload=(self.inputs/f.pop('path')).read_bytes();f['sha256']=digest(payload);expected[f['downloadUrl']]=payload
        save_json(path,data)
        calls=[]
        def recorded_response(request,timeout):
            calls.append(request.full_url);return io.BytesIO(expected[request.full_url])
        with patch('archive_core.transports.urlopen',side_effect=recorded_response):
            result,_,_=self.run_source('coursera-progressive')
        self.assertEqual(set(calls),set(expected));self.assertEqual(result['metrics']['new_transfers'],2)
        with patch('archive_core.transports.urlopen',side_effect=AssertionError('HTTP rerun accessed network')):
            result,_,_=self.run_source('coursera-progressive')
        self.assertEqual((result['metrics']['new_transfers'],result['metrics']['new_parses']),(0,0))

    def test_portable_reading_pdf_preserves_nonlatin_original_text(self):
        import fitz
        original='中文与来源。 Ελληνικά στοιχεία.'
        text=self.inputs/'multilingual.txt';text.write_text(original+'\n')
        data=load_json(self.inputs/'book.json');data['files']=[{'id':'text','path':'multilingual.txt'}]
        save_json(self.inputs/'book.json',data)
        _,manifest,release=self.run_source('book')
        with fitz.open(release/'reading-copy.pdf') as doc:
            extracted=''.join(p.get_text() for p in doc)
        self.assertIn('中文与来源',extracted);self.assertIn('Ελληνικά',extracted)
        self.assertEqual(manifest['items'][0]['blocks'][0]['text'],original)

    def test_selected_git_repo_never_executes_promisor_helper(self):
        repo=self.inputs/'repo'
        def git(*args):return subprocess.check_output(['git','-C',str(repo),*args]).decode().strip()
        blob=git('rev-parse',self.commit+':README.md')
        (repo/'.git/objects'/blob[:2]/blob[2:]).unlink()
        marker=self.work/'HELPER_EXECUTED'
        git('config','core.repositoryformatversion','1')
        git('config','extensions.partialClone','origin')
        git('config','remote.origin.promisor','true')
        git('config','remote.origin.url','ext::sh -c touch% '+str(marker))
        git('config','protocol.ext.allow','always')
        with self.assertRaises(subprocess.CalledProcessError):self.run_source('repository')
        self.assertFalse(marker.exists())
        self.assertFalse((self.work/'repository/CURRENT').exists())

    def test_pointer_write_failure_does_not_advance_scope_history(self):
        from archive_core import core
        self.run_source('book')
        output=self.work/'book';pointer=(output/'CURRENT').read_bytes()
        path=self.inputs/'book.json';data=load_json(path);data['files']=data['files'][:1];save_json(path,data)
        original=core.atomic_bytes
        def fail_pointer(path,data,*args,**kwargs):
            if Path(path).name=='CURRENT':raise OSError('Synthetic pointer failure')
            return original(path,data,*args,**kwargs)
        with patch('archive_core.core.atomic_bytes',side_effect=fail_pointer),self.assertRaises(OSError):run_archive(path,output)
        self.assertEqual((output/'CURRENT').read_bytes(),pointer)
        result,manifest,_=self.run_source('book')
        self.assertEqual(result['metrics']['removed'],1)
        self.assertEqual(manifest['ordered_membership'],['pdf'])

    def test_large_stored_video_zip_compatibility_and_nested_pdf_scan(self):
        import zipfile
        from archive_core.packaging import verified_zip
        video=self.work/'large.mp4'
        with video.open('wb') as stream:stream.truncate(64*1024*1024+1)
        archive=self.work/'large.zip';verified_zip(archive,[('Unit 1/large.mp4',video)])
        self.assertTrue(archive.exists())
        import fitz
        pdf=self.work/'secret-nested.pdf';doc=fitz.open();page=doc.new_page();page.insert_text((50,50),'https://example.invalid/file?token=SYNTHETIC');doc.save(pdf,deflate=True);doc.close()
        with zipfile.ZipFile(self.work/'nested.zip','w',compression=zipfile.ZIP_DEFLATED) as z:z.write(pdf,'nested.pdf')
        with self.assertRaises(PrivacyError):scan_file(self.work/'nested.zip')

    def test_release_install_rejects_other_source_and_privacy_identity(self):
        _,_,paper=self.run_source('paper');_,_,book=self.run_source('book')
        target=self.work/'book';before=(target/'CURRENT').read_bytes()
        with self.assertRaises(ValueError):install_release(paper,target)
        self.assertEqual((target/'CURRENT').read_bytes(),before)
        # Independently enforce CURRENT identity, even if a pointer is altered outside the installer.
        copied=target/'releases/foreign';shutil.copytree(paper,copied)
        (target/'CURRENT').write_text('releases/foreign\n')
        with self.assertRaises(ValueError):self.run_source('book')

    def test_zip_metadata_comments_are_privacy_scanned(self):
        import zipfile
        for location in ['archive','member','extra']:
            path=self.work/(location+'.zip')
            with zipfile.ZipFile(path,'w') as archive:
                info=zipfile.ZipInfo('ordinary.txt')
                secret=b'https://example.invalid/file?token=SYNTHETIC'
                if location=='archive':archive.comment=secret
                elif location=='member':info.comment=secret
                else:
                    import struct
                    info.extra=struct.pack('<HH',1234,len(secret))+secret
                archive.writestr(info,b'Ordinary text')
            with self.assertRaises(PrivacyError):scan_file(path)

    def test_garbled_text_is_retained_with_extraction_failure(self):
        path=self.inputs/'garbled.txt';path.write_bytes(b'\xff\x00garbled')
        data=load_json(self.inputs/'book.json');data['files']=[{'id':'garbled','path':'garbled.txt'}];save_json(self.inputs/'book.json',data)
        _,manifest,release=self.run_source('book')
        self.assertEqual(manifest['ordered_membership'],['garbled'])
        self.assertEqual(manifest['items'][0]['extraction_status'],'extraction-failure')
        asset=next(a for a in manifest['items'][0]['assets'] if a['role']=='book')
        self.assertEqual((release/asset['path']).read_bytes(),b'\xff\x00garbled')

    def test_stream_scan_rejects_signature_at_long_url_chunk_boundary(self):
        data=b'A'*(1024*1024-20000)+b' '+b'https://example.invalid/'+b'x'*20000+b'?token=SYNTHETIC'
        path=self.work/'boundary.txt';path.write_bytes(data)
        with self.assertRaises(PrivacyError):scan_file(path)
        from urllib.parse import quote
        url='https://example.invalid/'+'x'*20000+'?token=SYNTHETIC'
        for depth in range(1,5):
            url=quote(url,safe='');path.write_bytes(b'A'*(1024*1024-20000)+b' '+url.encode())
            with self.subTest(encoding_depth=depth),self.assertRaises(PrivacyError):scan_file(path)

    def test_processing_revision_reparses_without_retransferring_assets(self):
        _,before,_=self.run_source('book')
        with patch('archive_core.core.PROFILE','archive-normalize/next-fixture'):
            result,after,_=self.run_source('book')
        self.assertEqual(before['source'],after['source'])
        self.assertEqual(result['metrics']['new_transfers'],0)
        self.assertEqual(result['metrics']['new_parses'],2)
        self.assertEqual(result['metrics']['changed'],2)

    def test_legacy_domestika_artifacts_enter_pending_handoff_without_duplicate_prose(self):
        from archive_core.compatibility import emit_domestika_handoff
        from package_domestika import basename
        course=load_json(self.inputs/'domestika.json');unit=course['units'][0]
        folder=self.work/'Unit 01 - Preservation';folder.mkdir()
        shutil.copy2(FIXTURES/'book.pdf',folder/(folder.name+'.pdf'))
        stem=basename(unit['lessons'][0])
        shutil.copy2(FIXTURES/'lesson.mp4',folder/(stem+'.mp4'))
        shutil.copy2(FIXTURES/'requested.en.vtt',folder/(stem+'.en.vtt'))
        shutil.copy2(FIXTURES/'native.es.vtt',folder/(stem+'.es.vtt'))
        output=self.work/'legacy.handoff';folders={1:folder};languages={11:['en','es']}
        result=emit_domestika_handoff(course,[unit],folders,languages,output)
        release=Path(result['release']);manifest=load_json(release/'manifest.json');validate_release(release)
        self.assertEqual(manifest['ordered_membership'],['unit:1','lesson:11'])
        pdf=next(a for a in manifest['items'][0]['assets'] if a['role']=='unit-document')
        self.assertIn(pdf['asset_id'],[d['asset_id'] for d in manifest['derivations']])
        derivation=next(d for d in manifest['derivations'] if d['asset_id']==pdf['asset_id'])
        own_pixels={f['image_asset_id'] for f in manifest['items'][0]['figures'] if f['asset_id']==pdf['asset_id']}
        self.assertFalse(own_pixels.intersection(derivation['input_asset_ids']))
        self.assertFalse(any(b['asset_id']==pdf['asset_id'] for i in manifest['items'] for b in i['blocks']))
        # A checked English reading PDF is explicitly labeled and references its original inputs/log.
        reading=self.work/'reading.pdf';shutil.copy2(FIXTURES/'paper.pdf',reading)
        with self.assertRaises(ValueError):emit_domestika_handoff(course,[unit],folders,languages,output,reading_pdf=reading)
        log=self.work/'removed.log';log.write_text('location\trule\tremoved text\n')
        result=emit_domestika_handoff(course,[unit],folders,languages,output,reading_pdf=reading,removal_log=log)
        release=Path(result['release']);manifest=load_json(release/'manifest.json');validate_release(release)
        translation=next(d for d in manifest['derivations'] if d['derivation']=='translation')
        self.assertTrue(translation['input_asset_ids']);self.assertIsNotNone(translation['removal_log'])
        chunks=[json.loads(line) for line in (release/'text-chunks.jsonl').read_text().splitlines()]
        self.assertTrue(any(c['derivation']=='translation' for c in chunks))
        with patch('archive_core.compatibility.probe_local_video',side_effect=AssertionError('Unchanged preserved media was reprobed')):
            again=emit_domestika_handoff(course,[unit],folders,languages,output,reading_pdf=reading,removal_log=log)
        self.assertEqual((again['metrics']['new_transfers'],again['metrics']['new_parses']),(0,0))
        self.assertEqual(again['handoff_state'],'pending')
        for field,value in [('duration_seconds',3600),('requested_audio','es')]:
            bad=copy.deepcopy(unit);bad['lessons'][0][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):emit_domestika_handoff(course,[bad],folders,languages,output)

    def test_concurrent_legacy_handoffs_preserve_each_callers_snapshot(self):
        import threading
        from concurrent.futures import ThreadPoolExecutor
        from archive_core import compatibility
        from package_domestika import basename
        course=load_json(self.inputs/'domestika.json');unit=course['units'][0]
        folder=self.work/'Unit 01 - Preservation';folder.mkdir();stem=basename(unit['lessons'][0])
        shutil.copy2(FIXTURES/'paper.pdf',folder/(folder.name+'.pdf'))
        shutil.copy2(FIXTURES/'lesson.mp4',folder/(stem+'.mp4'))
        for lang,name in [('en','requested.en.vtt'),('es','native.es.vtt')]:shutil.copy2(FIXTURES/name,folder/(stem+'.'+lang+'.vtt'))
        output=self.work/'concurrent.handoff';ready=threading.Event();release=threading.Event();actual=compatibility.run_archive
        def delayed(path,output):
            if load_json(path)['course_title']=='First':
                ready.set();self.assertTrue(release.wait(20))
            return actual(path,output)
        first=copy.deepcopy(course);first['course_title']='First';second=copy.deepcopy(course);second['course_title']='Second'
        with patch('archive_core.compatibility.run_archive',side_effect=delayed),ThreadPoolExecutor(max_workers=2) as pool:
            job=pool.submit(compatibility.emit_domestika_handoff,first,[unit],{1:folder},{11:['en','es']},output)
            self.assertTrue(ready.wait(20))
            try:
                result2=compatibility.emit_domestika_handoff(second,[unit],{1:folder},{11:['en','es']},output)
            finally:release.set()
            result1=job.result(timeout=20)
        self.assertEqual(load_json(Path(result1['release'])/'manifest.json')['source']['title'],'First')
        self.assertEqual(load_json(Path(result2['release'])/'manifest.json')['source']['title'],'Second')
        self.assertFalse(list((output/'.state').glob('compatibility-*.json')))

    def test_contract_positive_negative_fixtures(self):
        directory = ROOT/'tests/fixtures/contracts'
        cases = list(directory.glob('*.json'))
        self.assertGreaterEqual(len(cases), 2)
        import jsonschema
        for path in cases:
            case = load_json(path)
            if case['valid']:
                validate(case['schema'],case['value'])
            else:
                with self.assertRaises(jsonschema.ValidationError): validate(case['schema'],case['value'])


if __name__ == '__main__': unittest.main()
