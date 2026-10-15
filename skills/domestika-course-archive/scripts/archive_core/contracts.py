"""Offline JSON Schema validation, then referential and locator validation."""
import json
from pathlib import Path

import jsonschema
from referencing import Registry, Resource

from .normalize import resolve, normalize_asset
from .handoff import handoff_records
from .privacy import scan_release
from .storage import safe_path, digest, load_json

SCHEMAS = Path(__file__).resolve().parents[2] / 'contracts' / 'v1'


def validate(name, value):
    schemas = [json.loads(p.read_text()) for p in SCHEMAS.glob('*.json')]
    registry = Registry().with_resources((s['$id'], Resource.from_contents(s)) for s in schemas)
    schema = next(s for s in schemas if s['title'] == name)
    jsonschema.Draft202012Validator(schema, registry=registry, format_checker=jsonschema.FormatChecker()).validate(value)


def file_record(root, relative):
    path = safe_path(root, relative)
    data = path.read_bytes()
    return {'path': relative, 'sha256': digest(data), 'bytes': len(data)}


def check_file(root, record):
    actual = file_record(root, record['path'])
    if actual != {k: record[k] for k in actual}:
        raise ValueError('Handoff file hash or length mismatch.')
    return safe_path(root, record['path']).read_bytes()


def validate_release(root, *, verify_locators=True, privacy_verified_hashes=frozenset()):
    root = Path(root)
    handoff = load_json(root / 'kb-handoff.json')
    manifest = load_json(root / 'manifest.json')
    validate('kb-handoff', handoff)
    validate('archive-manifest', manifest)
    roles = {'manifest': 'manifest.json', 'text_chunks': 'text-chunks.jsonl', 'image_records': 'image-records.jsonl'}
    if any(handoff[role]['path'] != path for role, path in roles.items()):
        raise ValueError('Handoff role path mismatch.')
    if handoff['source'] != manifest['source'] or handoff['ordered_membership'] != manifest['ordered_membership']:
        raise ValueError('Handoff source or membership mismatch.')
    if handoff['state'] == 'completed':
        receipt = handoff['consumer_receipt']
        source = handoff['source']
        if receipt is None or any(receipt[k] != source[k] for k in ['source_id', 'source_revision']):
            raise ValueError('Completed handoff requires a matching consumer receipt.')
        for medium in ['text_chunks', 'image_records']:
            if receipt['expected_' + medium] != handoff['expected_' + medium] or receipt['actual_' + medium] != handoff['expected_' + medium]:
                raise ValueError('Consumer receipt counts mismatch.')
    elif handoff['consumer_receipt'] is not None:
        raise ValueError('Pending handoff cannot claim a consumer receipt.')
    if manifest['handoff_state'] != handoff['state']:
        raise ValueError('Archive handoff state mismatch.')
    items = manifest['items']
    members = {i['member_id']: i for i in items}
    if len(members) != len(items):
        raise ValueError('Duplicate manifest member.')
    ordered = [i['member_id'] for i in items if i['state'] != 'tombstone']
    if ordered != manifest['ordered_membership']:
        raise ValueError('Manifest ordered membership mismatch.')
    if manifest['inventory_complete']:
        if manifest['expected_membership']['value'] != ordered or manifest['expected_count']['value'] != len(ordered):
            raise ValueError('Authoritative expected and actual membership differ.')
    assets = {}
    for item in items:
        for asset in item['assets']:
            check_file(root, asset)
            if asset['asset_id'] != 'sha256:' + asset['sha256']:
                raise ValueError('Asset identity/hash mismatch.')
            assets[asset['asset_id']] = asset
        item_assets = {a['asset_id']: a for a in item['assets']}
        for block in item['blocks']:
            if block['asset_id'] not in item_assets:
                raise ValueError('Block references an asset outside its member.')
            data = check_file(root, item_assets[block['asset_id']])
            locator = block['locator']
            if locator['kind'] == 'markdown-lines' and locator['path'] != item_assets[block['asset_id']]['path']:
                raise ValueError('Markdown locator path does not name its asset.')
            if locator['kind'] == 'code-lines' and (locator['commit'] != item['facts'].get('commit', manifest['source']['source_revision']) or 'file:' + locator['path'] != item['member_id']):
                raise ValueError('Code locator commit or file membership mismatch.')
            if locator['kind'] == 'caption-cue' and locator['lesson_id'] != item['member_id']:
                raise ValueError('Caption locator names another lesson.')
            if verify_locators and resolve(data, locator) != block['text']:
                raise ValueError('Locator does not open the named text.')
        # Regenerate occurrences to check both physical locations and pixel hashes.
        for original in [a for a in item['assets'] if a['media_type'] in ('application/pdf', 'application/epub+zip')] if verify_locators else []:
            data = check_file(root, original)
            _, generated, pixels, _, _ = normalize_asset(data, original, item, {})
            expected = [f for f in item['figures'] if f['asset_id'] == original['asset_id']]
            if generated != expected:
                raise ValueError('Figure occurrence location mismatch.')
            for path, (record, pixel_data) in pixels.items():
                if check_file(root, record) != pixel_data:
                    raise ValueError('Figure pixels do not match the named occurrence.')
    for derivation in manifest['derivations']:
        if derivation['asset_id'] not in assets or not set(derivation['input_asset_ids']).issubset(assets):
            raise ValueError('Document derivation references unknown assets.')
        if derivation['removal_log'] is not None and derivation['removal_log'] not in {a['path'] for a in assets.values()}:
            raise ValueError('Document derivation removal log is not a referenced blob.')
    declared = {f['path'] for f in handoff['blobs']}
    expected_blobs = {a['path'] for a in assets.values()}
    if declared != expected_blobs or len(declared) != len(handoff['blobs']):
        raise ValueError('Handoff blob membership mismatch.')
    for record in [handoff['manifest'], handoff['text_chunks'], handoff['image_records'], *handoff['blobs']]:
        check_file(root, record)
    chunks = [json.loads(line) for line in check_file(root, handoff['text_chunks']).splitlines()]
    images = [json.loads(line) for line in check_file(root, handoff['image_records']).splitlines()]
    if len(chunks) != handoff['expected_text_chunks'] or len(images) != handoff['expected_image_records']:
        raise ValueError('Handoff record counts mismatch.')
    expected_blocks = {b['block_id'] for i in items if i['state'] != 'tombstone' for b in i['blocks'] if b['text'].strip()}
    if {c['chunk_id'] for c in chunks} != expected_blocks or len({c['chunk_id'] for c in chunks}) != len(chunks):
        raise ValueError('Handoff chunk membership mismatch.')
    expected_figures = {f['figure_id'] for i in items if i['state'] != 'tombstone' for f in i['figures']}
    if {r['figure_id'] for r in images} != expected_figures or len(images) != len(expected_figures):
        raise ValueError('Handoff image membership mismatch.')
    for row, name in [*((c, 'text-chunk') for c in chunks), *((r, 'image-record') for r in images)]:
        validate(name, row)
        if any(row[k] != manifest['source'][k] for k in ['source_id', 'source_revision', 'privacy_scope']):
            raise ValueError('Record source mismatch.')
        if row['member_id'] not in members or members[row['member_id']]['state'] == 'tombstone':
            raise ValueError('Record names an inactive member.')
    for chunk in chunks:
        if digest(chunk['embedding_input'].encode()) != chunk['embedding_input_sha256']:
            raise ValueError('Embedding input hash mismatch.')
        for span in chunk['child_spans'] + chunk['parent_spans'] + chunk['context_spans']:
            if span['member_id'] != chunk['member_id'] or span['asset_id'] not in assets:
                raise ValueError('Chunk span membership mismatch.')
        child = chunk['child_spans']
        if len(child) != 1 or (verify_locators and resolve(check_file(root, assets[child[0]['asset_id']]), child[0]['locator']) != chunk['text']):
            raise ValueError('Chunk provenance does not open its text.')
    for row in images:
        if row['occurrence'] not in members[row['member_id']]['figures']:
            raise ValueError('Image occurrence is not in its member.')
        image = assets[row['occurrence']['image_asset_id']]
        if row['blob_path'] != image['path'] or row['blob_sha256'] != image['sha256']:
            raise ValueError('Image record pixel identity mismatch.')
    expected_chunks, expected_images = handoff_records(manifest)
    if chunks != expected_chunks or images != expected_images:
        raise ValueError('Handoff records differ from normalized manifest provenance.')
    allowed = {'kb-handoff.json', 'manifest.json', 'text-chunks.jsonl', 'image-records.jsonl', 'reading-copy.pdf', 'reading-copy.md', *declared}
    actual = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    if actual != allowed:
        raise ValueError('Unexpected or missing release files.')
    scan_release(root, verified_hashes=privacy_verified_hashes)
    return {'members': len(ordered), 'text_chunks': len(chunks), 'image_records': len(images), 'state': handoff['state']}
