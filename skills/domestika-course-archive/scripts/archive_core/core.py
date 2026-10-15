"""Durable reconciliation, shared packaging and atomic publication."""
import copy
import fcntl
import os
import shutil
import signal
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .adapters import ADAPTERS
from .contracts import file_record, validate_release
from .normalize import PROFILE
from .handoff import handoff_records
from .privacy import scan_text, scan_file
from .storage import atomic_bytes, blob_record, canonical, digest, fingerprint, load_json, save_json, safe_path
from .transports import transfer, transport_identity


def current_release(output):
    output = Path(output)
    pointer = output / 'CURRENT'
    if not pointer.exists():
        return None
    return safe_path(output, pointer.read_text().strip())


def checkpoint(stage, member_id):
    """Acceptance sends a real SIGKILL at explicit durable boundaries."""
    if os.environ.get('ARCHIVE_KILL_AT') == stage:
        target = os.environ.get('ARCHIVE_KILL_MEMBER')
        if target is None or target == member_id:
            os.kill(os.getpid(), signal.SIGKILL)


def document_bytes(manifest):
    """A portable faithful layout of original text. Translation remains explicit."""
    import fitz
    from html import escape
    parts = [manifest['source']['title'], 'Portable reading copy (derived layout; original text)', '']
    for item in manifest['items']:
        if item['state'] == 'tombstone':
            continue
        parts.extend([item['title'], 'Access: ' + item['access']])
        parts.extend(b['text'] for b in item['blocks'] if b['text'])
        parts.extend('Gap: ' + gap for gap in item['gaps'])
        parts.append('')
    text = '\n\n'.join(parts)
    scan_text(text)
    import io
    markup = '<html><body>' + ''.join('<p>' + escape(paragraph).replace('\n', '<br/>') + '</p>' for paragraph in text.split('\n\n')) + '</body></html>'
    story = fitz.Story(html=markup, user_css='body { font-family: serif; font-size: 11pt; line-height: 1.4; } p { margin-bottom: 10pt; }')
    buffer = io.BytesIO()
    writer = fitz.DocumentWriter(buffer)
    def rectangle(number, filled):
        return fitz.Rect(0, 0, 595, 842), fitz.Rect(42, 42, 553, 800), None
    story.write(writer, rectangle)
    writer.close()
    with fitz.open(stream=buffer.getvalue(), filetype='pdf') as document:
        document.set_metadata({'title': manifest['source']['title'], 'subject': 'Derived portable layout of original source text'})
        pdf = document.tobytes(deflate=True, no_new_id=True)

    return text.encode(), pdf



def run_archive(input_path, output):
    input_path, output = Path(input_path).resolve(), Path(output).resolve()
    data = load_json(input_path)
    adapter = ADAPTERS[data.get('adapter', 'domestika')](data, input_path.parent)
    output.mkdir(parents=True, exist_ok=True)
    state = output / '.state'
    state.mkdir(mode=0o700, exist_ok=True)
    os.chmod(state, 0o700)
    (output / 'outbox').mkdir(exist_ok=True)
    with (state / 'lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return _run(adapter, state, output)


def _run(adapter, state, output):
    discovery = adapter.discover()
    adapter.source_checks(discovery)
    previous_path = current_release(output)
    previous = load_json(previous_path / 'manifest.json') if previous_path else None
    identity = {'source_id': discovery['source_id'], 'privacy': discovery['privacy']}
    if previous and (previous['source']['source_id'] != identity['source_id'] or previous['privacy'] != identity['privacy'] or previous['adapter'] != adapter.name):
        raise ValueError('Current release belongs to another source, adapter or privacy scope.')
    binding = load_json(state / 'binding.json')
    if binding is not None and identity != binding:
        raise ValueError('Output belongs to another source or privacy scope.')
    save_json(state / 'binding.json', identity)
    old = {i['member_id']: i for i in previous['items']} if previous else {}
    metrics = {k: 0 for k in ['added', 'changed', 'reused', 'quarantined', 'removed', 'new_transfers', 'new_parses']}
    items, public_discovery, projection = [], [], {}
    def verified_scan(record):
        marker = state / 'verified' / (record['sha256'] + '.json')
        if load_json(marker) != {'privacy_profile': 'privacy/2', 'sha256': record['sha256']}:
            scan_file(state / record['path'])
            save_json(marker, {'privacy_profile': 'privacy/2', 'sha256': record['sha256']})
    if not discovery['discovery_ok']:
        if previous is None:
            raise ValueError('Discovery failed; there is no verified release to preserve.')
        discovery['items'] = []
        discovery['authoritative'] = False
    for incoming in adapter.collect(discovery):
        item = {k: copy.deepcopy(v) for k, v in incoming.items() if k != 'descriptors'}
        item['access'], item['gaps'] = adapter.probe(incoming)
        descriptors = incoming['descriptors'] if item['access'] == 'accessible' else []
        sanitized, transports = [], []
        for descriptor in descriptors:
            transport = adapter.resolve_transport(descriptor)
            transport_key = fingerprint({'member': item['member_id'], 'descriptor': len(transports)})
            projection[transport_key] = {'transport': transport, 'supplied_url': descriptor.get('url')}
            # Restricted projection is the ONLY persistent storage for capabilities.
            public = {k: v for k, v in descriptor.items() if k not in ['url', 'local_path', 'repo', 'playlist_fixture']}
            public['content_identity'] = descriptor.get('sha256') or transport_identity(transport)
            sanitized.append(public)
            transports.append(transport)
        scan_text(canonical(item).decode())
        scan_text(canonical(sanitized).decode())
        source_fingerprint = fingerprint({'item': item, 'assets': sanitized})
        item['fingerprint'] = fingerprint({'source_fingerprint': source_fingerprint, 'profile': PROFILE})
        public_discovery.append({'member_id': item['member_id'], 'fingerprint': source_fingerprint})
        item_key = fingerprint({'source': discovery['source_id'], 'privacy': discovery['privacy'], 'member': item['member_id'], 'fingerprint': item['fingerprint']})
        cache_path = state / 'members' / (item_key + '.json')
        cached = load_json(cache_path)
        if cached is not None and all((state / a['path']).exists() and digest((state / a['path']).read_bytes()) == a['sha256'] for a in cached['assets']):
            item = cached
            metrics['reused'] += 1
        elif item['access'] != 'accessible':
            item.update({'assets': [], 'blocks': [], 'figures': [], 'state': 'active', 'extraction_status': 'not-applicable'})
            if item['member_id'] in old:
                kept = old[item['member_id']]
                item.update({k: copy.deepcopy(kept[k]) for k in ['assets', 'blocks', 'figures', 'extraction_status']})
                item['facts']['preserved_source_revision'] = kept['facts'].get('preserved_source_revision', previous['source']['source_revision'])
                item['state'] = 'quarantined'
                item['gaps'].append('Earlier verified evidence preserved after loss of access.')
                metrics['quarantined'] += 1
            else:
                metrics['added'] += 1
            save_json(cache_path, item)
        else:
            item.update({'assets': [], 'blocks': [], 'figures': [], 'state': 'active', 'extraction_status': 'not-applicable'})
            statuses = []
            for index, (descriptor, transport) in enumerate(zip(descriptors, transports)):
                asset_identity = {k: v for k, v in sanitized[index].items() if k != 'commit'}
                key = fingerprint({'source': discovery['source_id'], 'privacy': discovery['privacy'], 'member': item['member_id'], 'index': index, 'identity': asset_identity})
                transferred_path = state / 'transfers' / (key + '.json')
                transfer_records = load_json(transferred_path)
                if transfer_records is None or any(not (state / a['path']).exists() or digest((state / a['path']).read_bytes()) != a['sha256'] for a in transfer_records):
                    save_json(state / 'transport.json', projection)
                    raw, extra = transfer(transport)
                    if descriptor.get('sha256') and digest(raw) != descriptor['sha256']:
                        raise ValueError('Transferred asset does not match expected content hash.')
                    record = blob_record(raw, descriptor['media_type'], descriptor['role'], descriptor.get('language'))
                    transfer_records = [record] + [blob_record(b, mime, role, lang) for b, mime, role, lang in extra]
                    for record, raw in [(record, raw), *((r, e[0]) for r, e in zip(transfer_records[1:], extra))]:
                        atomic_bytes(state / record['path'], raw)
                        verified_scan(record)
                    save_json(transferred_path, transfer_records)
                    metrics['new_transfers'] += int(transport['kind'] != 'inline')
                    checkpoint('after-transfer', item['member_id'])
                for record in transfer_records:
                    normalized_key = fingerprint({'asset_key': key, 'content_hash': record['sha256'], 'profile': PROFILE})
                    normalized_path = state / 'parses' / (normalized_key + '.json')
                    normalized = load_json(normalized_path)
                    if normalized is None:
                        raw = (state / record['path']).read_bytes()
                        blocks, figures, pixels, status, facts = adapter.normalize(raw, record, item, descriptor)
                        for path, (pixel_record, pixel_data) in pixels.items():
                            atomic_bytes(state / path, pixel_data)
                            verified_scan(pixel_record)
                        normalized = {'blocks': blocks, 'figures': figures, 'pixels': [r for r, _ in pixels.values()], 'status': status, 'facts': facts}
                        save_json(normalized_path, normalized)
                        metrics['new_parses'] += 1
                        checkpoint('after-parse', item['member_id'])
                    normalized = copy.deepcopy(normalized)
                    for block in normalized['blocks']:
                        if block['locator']['kind'] == 'code-lines':
                            block['locator']['commit'] = descriptor['commit']
                    if descriptor.get('derivation', 'original') != 'original':
                        item['facts'].setdefault('asset_derivations', []).append({'asset_id': record['asset_id'], 'derivation': descriptor['derivation'],
                                        'transform_version': descriptor.get('transform_version', PROFILE), 'input_members': descriptor.get('input_members', []), 'removal_log': None})
                    item['assets'].extend([record, *normalized['pixels']])
                    item['blocks'].extend(normalized['blocks'])
                    item['figures'].extend(normalized['figures'])
                    item['facts'].update(normalized['facts'])
                    statuses.append(normalized['status'])
            item['assets'] = list({a['asset_id']: a for a in item['assets']}.values())
            item['extraction_status'] = next((s for s in ['extraction-failure', 'ocr-required', 'partial', 'completed'] if s in statuses), 'not-applicable')
            if item['extraction_status'] in ('extraction-failure', 'ocr-required'):
                item['gaps'].append(item['extraction_status'] + ': source bytes retained.')
            save_json(cache_path, item)
            metrics['changed' if item['member_id'] in old else 'added'] += 1
        items.append(item)
        checkpoint('after-member', item['member_id'])
    save_json(state / 'transport.json', projection)
    seen = {i['member_id'] for i in items}
    same_scope = previous and previous['scope'] == discovery['scope']
    scope_path = state / 'scopes' / (fingerprint(discovery['scope']) + '.json')
    scope_history = load_json(scope_path, previous['expected_membership']['value'] if same_scope else None)
    removable = set(scope_history or []) if discovery['authoritative'] and discovery['discovery_ok'] else set()
    for member_id, former in old.items():
        if member_id in seen:
            continue
        retained = copy.deepcopy(former)
        retained['facts'].setdefault('preserved_source_revision', previous['source']['source_revision'])
        if retained['state'] == 'tombstone':
            items.append(retained)
            continue
        if member_id in removable:
            retained['state'] = 'tombstone'
            metrics['removed'] += 1
        else:
            retained['state'] = 'quarantined'
            retained['gaps'] = list(set(retained['gaps'] + ['No authoritative same-scope removal evidence.']))
            metrics['quarantined'] += 1
        items.append(retained)
    source_hash = fingerprint(public_discovery)
    source = {'schema_version': 'mind/source@1', 'source_id': discovery['source_id'],
              'source_revision': discovery['source_revision'] or 'sha256:' + source_hash, 'source_hash': source_hash,
              'privacy_scope': discovery['privacy'], 'kind': discovery['kind'], 'title': discovery['title'],
              'aliases': discovery['aliases'], 'canonical_url': discovery['canonical_url'], 'creators': discovery['creators'],
              'publication_date': {'value': discovery['publication_date'], 'reason': None if discovery['publication_date'] else 'not found'},
              'revision_date': {'value': discovery['revision_date'], 'reason': None if discovery['revision_date'] else 'not found'},
              'acquired_at': previous['source']['acquired_at'] if previous else datetime.now(timezone.utc).isoformat(),
              'selected_scope': discovery['scope'], 'derivation': 'original'}
    if not discovery['discovery_ok']:
        source = copy.deepcopy(previous['source'])
    ordered = [i['member_id'] for i in items if i['state'] != 'tombstone']
    complete = bool(discovery['authoritative'] and discovery['discovery_ok'] and set(ordered) == set(discovery['expected'] or []))
    manifest = {'schema_version': 'archive-manifest/v1', 'adapter': adapter.name, 'source': source,
                'scope': discovery['scope'], 'expected_membership': {'value': discovery['expected'] if complete else None, 'reason': None if complete else 'not found'},
                'expected_count': {'value': len(discovery['expected']) if complete else None, 'reason': None if complete else 'not found'},
                'inventory_complete': complete, 'ordered_membership': ordered, 'items': items,
                'rights': adapter.data.get('rights', 'Owner-authorized private preservation; no public redistribution grant.'),
                'privacy': discovery['privacy'], 'verification': 'passed',
                'archive_state': 'partial' if discovery['gaps'] or not complete or any(i['access'] != 'accessible' or i['gaps'] for i in items if i['state'] != 'tombstone') else 'completed',
                'handoff_state': 'pending', 'gaps': discovery['gaps'], 'metrics': metrics, 'derivations': []}
    # Source content and metadata determine portable output reuse, independently of counters.
    for item in items:
        item['assets'] = [a for a in item['assets'] if a['role'] != 'portable-reading']
    document_key = fingerprint({'source': source, 'items': items})
    docs = load_json(state / 'documents' / (document_key + '.json'))
    if docs is None:
        markdown, pdf = document_bytes(manifest)
        docs = [blob_record(markdown, 'text/markdown', 'portable-reading'), blob_record(pdf, 'application/pdf', 'portable-reading')]
        for record, raw in zip(docs, [markdown, pdf]):
            atomic_bytes(state / record['path'], raw)
            verified_scan(record)
        save_json(state / 'documents' / (document_key + '.json'), docs)
    for member in items:
        for derivation in member['facts'].get('asset_derivations', []):
            input_assets = list(dict.fromkeys(a['asset_id'] for i in items if i['member_id'] in derivation['input_members'] for a in i['assets'] if a['role'] not in ('unit-document', 'reading-copy', 'removal-log', 'portable-reading', 'figure')))
            removal = next((a['path'] for a in member['assets'] if a['role'] == 'removal-log'), None) if derivation['derivation'] == 'translation' else None
            manifest['derivations'].append({k: derivation[k] for k in ['asset_id', 'derivation', 'transform_version']} | {'input_asset_ids': input_assets, 'removal_log': removal})
    if items:
        # Reading PDF reuses the original normalized blocks; it is not ingested twice.
        item = items[0]
        input_ids = list(dict.fromkeys(b['asset_id'] for i in items for b in i['blocks']))
        item['assets'] = list({a['asset_id']: a for a in item['assets'] + docs}.values())
        manifest['derivations'] += [{'asset_id': d['asset_id'], 'derivation': 'derived', 'transform_version': 'portable-layout/1',
                                    'input_asset_ids': input_ids, 'removal_log': None} for d in docs]
    stage = state / 'staging' / uuid.uuid4().hex
    stage.mkdir(parents=True)
    for item in items:
        for record in item['assets']:
            source_path = state / record['path']
            if not source_path.exists() and previous_path:
                atomic_bytes(source_path, safe_path(previous_path, record['path']).read_bytes())
            atomic_bytes(stage / record['path'], source_path.read_bytes())
    for record, name in zip(docs, ['reading-copy.md', 'reading-copy.pdf']):
        atomic_bytes(stage / name, (state / record['path']).read_bytes())
    save_json(stage / 'manifest.json', manifest)
    chunks, images = handoff_records(manifest)
    for name, rows in [('text-chunks.jsonl', chunks), ('image-records.jsonl', images)]:
        atomic_bytes(stage / name, b''.join(canonical(row) + b'\n' for row in rows))
    blobs = {a['path'] for i in items for a in i['assets']}
    handoff = {'schema_version': 'kb-handoff/v1', 'source': source, 'manifest': file_record(stage, 'manifest.json'),
               'text_chunks': file_record(stage, 'text-chunks.jsonl'), 'image_records': file_record(stage, 'image-records.jsonl'),
               'blobs': [file_record(stage, p) for p in sorted(blobs)], 'ordered_membership': ordered,
               'expected_text_chunks': len(chunks), 'expected_image_records': len(images), 'state': 'pending', 'consumer_receipt': None}
    save_json(stage / 'kb-handoff.json', handoff)
    trusted_hashes = set()
    for record in [a for i in items for a in i['assets']] + docs:
        verified_scan(record)
        trusted_hashes.add(record['sha256'])
    validate_release(stage, verify_locators=False, privacy_verified_hashes=trusted_hashes)
    checkpoint('before-publish', '')
    release_id = fingerprint({'manifest': manifest, 'handoff': handoff})
    relative = 'releases/' + release_id
    destination = output / relative
    destination.parent.mkdir(exist_ok=True)
    if destination.exists():
        validate_release(destination, verify_locators=False, privacy_verified_hashes=trusted_hashes)
        shutil.rmtree(stage)
    else:
        os.replace(stage, destination)
    checkpoint('before-pointer', '')
    atomic_bytes(output / 'CURRENT', (relative + '\n').encode())
    if discovery['authoritative'] and discovery['discovery_ok']:
        save_json(scope_path, discovery['expected'])
    return {'release': str(destination), 'metrics': metrics, 'archive_state': manifest['archive_state'], 'handoff_state': 'pending'}


def install_release(release, output):
    """Install immutable data only; local checkpoints and outbox are independent."""
    release, output = Path(release).resolve(), Path(output).resolve()
    validate_release(release)
    incoming = load_json(release / 'manifest.json')
    identity = {'source_id': incoming['source']['source_id'], 'privacy': incoming['privacy']}
    binding = load_json(output / '.state' / 'binding.json')
    previous_path = current_release(output)
    previous = load_json(previous_path / 'manifest.json') if previous_path else None
    if (binding is not None and binding != identity) or (previous is not None and (previous['source']['source_id'] != identity['source_id'] or previous['privacy'] != identity['privacy'] or previous['adapter'] != incoming['adapter'])):
        raise ValueError('Cannot install a release over another source or privacy scope.')
    output.mkdir(parents=True, exist_ok=True)
    (output / 'outbox').mkdir(exist_ok=True)
    releases = output / 'releases'
    releases.mkdir(exist_ok=True)
    name = fingerprint(load_json(release / 'kb-handoff.json'))
    destination = releases / name
    if destination.exists():
        validate_release(destination)
    else:
        stage = output / ('.install-' + uuid.uuid4().hex)
        shutil.copytree(release, stage)
        validate_release(stage)
        os.replace(stage, destination)
    atomic_bytes(output / 'CURRENT', ('releases/' + name + '\n').encode())
    return str(destination)
