"""Pure shared block-to-chunk conversion. No consumer or model imports."""
from .storage import digest


def handoff_records(manifest):
    """One pure block-to-chunk pass. The consumer must not split these again."""
    source = {k: manifest['source'][k] for k in ['source_id', 'source_revision', 'privacy_scope']}
    chunks, images = [], []
    for item in manifest['items']:
        if item['state'] == 'tombstone':
            continue
        producing_revision = item['facts'].get('commit') or item['facts'].get('preserved_source_revision', source['source_revision'])
        for block in item['blocks']:
            if not block['text'].strip():
                continue
            span = {'source_revision': producing_revision, 'member_id': item['member_id'], 'asset_id': block['asset_id'], 'locator': block['locator']}
            embedding_input = (block['heading'] + '\n\n' if block['heading'] else '') + block['text']
            chunks.append({'schema_version': 'archive-text-chunk/v1', **source,
                           'producing_revision': producing_revision, 'chunk_id': block['block_id'], 'parent_id': item['member_id'], 'member_id': item['member_id'],
                           'text': block['text'], 'heading': block['heading'], 'derivation': block['derivation'],
                           'language': block['language'], 'figure_ids': [f['figure_id'] for f in item['figures']],
                           'embedding_input': embedding_input, 'embedding_input_sha256': digest(embedding_input.encode()),
                           'child_spans': [span], 'parent_spans': [span], 'context_spans': []})
        for figure in item['figures']:
            image = next(a for a in item['assets'] if a['asset_id'] == figure['image_asset_id'])
            images.append({'schema_version': 'archive-image-record/v1', **source, 'figure_id': figure['figure_id'],
                           'member_id': item['member_id'], 'producing_revision': producing_revision, 'blob_path': image['path'], 'blob_sha256': image['sha256'], 'occurrence': figure})
    return chunks, images

