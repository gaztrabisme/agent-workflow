"""Pure normalized blocks and figure occurrences; no translation or model calls."""
import io
import posixpath
import re
import zipfile
from html.parser import HTMLParser
from xml.etree import ElementTree as ET

from .storage import blob_record

PROFILE = 'archive-normalize/2'


class TextHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag in ('h1', 'h2', 'h3', 'h4', 'p', 'div', 'li', 'br', 'section') and not self.hidden:
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        if tag in ('h1', 'h2', 'h3', 'h4', 'p', 'div', 'li', 'section') and not self.hidden:
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def html_text(value):
    parser = TextHTML()
    parser.feed(value)
    return '\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip())


def epub_resources(data):
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        container = ET.fromstring(archive.read('META-INF/container.xml'))
        opf = next(e.attrib['full-path'] for e in container.iter() if e.tag.endswith('rootfile'))
        root = ET.fromstring(archive.read(opf))
        resources = {e.attrib['id']: posixpath.normpath(posixpath.join(posixpath.dirname(opf), e.attrib['href']))
                     for e in root.iter() if e.tag.endswith('}item')}
        result = []
        for e in root.iter():
            if e.tag.endswith('itemref'):
                resource = resources[e.attrib['idref']]
                if resource.startswith('/') or '..' in resource.split('/'):
                    raise ValueError('EPUB resource escapes the container.')
                result.append((resource, html_text(archive.read(resource).decode('utf-8'))))
        facts = {}
        for e in root.iter():
            key = e.tag.rsplit('}', 1)[-1]
            if key in ('title', 'creator', 'identifier', 'date', 'language', 'publisher') and e.text:
                facts.setdefault(key, []).append(e.text)
        return result, facts


def epub_images(data):
    resources, _ = epub_resources(data)
    images = []
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        for order, (parent, _) in enumerate(resources):
            root = ET.fromstring(archive.read(parent))
            for index, element in enumerate(e for e in root.iter() if e.tag.rsplit('}', 1)[-1] == 'img'):
                source = element.attrib.get('src', '')
                resource = posixpath.normpath(posixpath.join(posixpath.dirname(parent), source))
                if not source or '://' in source or resource.startswith('/') or '..' in resource.split('/'):
                    raise ValueError('EPUB image is not an internal permitted resource.')
                locator = {'kind': 'epub-image', 'resource': resource, 'parent_resource': parent, 'reading_order': order, 'occurrence': index}
                images.append((locator, archive.read(resource)))
    return images


def time_seconds(value):
    parts = value.replace(',', '.').split(':')
    return sum(float(v) * (60 ** i) for i, v in enumerate(reversed(parts)))


def cues(data):
    text = data.decode('utf-8-sig')
    result = []
    for part in re.split(r'\n\s*\n', text):
        lines = part.strip().splitlines()
        marker = next((i for i, line in enumerate(lines) if '-->' in line), None)
        if marker is None:
            continue
        left, right = lines[marker].split('-->', 1)
        start, end = time_seconds(left.strip()), time_seconds(right.strip().split()[0])
        if end < start:
            raise ValueError('Caption cue ends before it starts.')
        cue_id = lines[marker - 1] if marker else str(len(result) + 1)
        result.append((cue_id, start, end, html_text('\n'.join(lines[marker + 1:]))))
    if not result:
        raise ValueError('Caption file has no timed cues.')
    return result


def pdf_locator(page, index, rectangle=None):
    return {'kind': 'pdf-page', 'page': index + 1, 'page_label': page.get_label() or None,
            'width': page.rect.width, 'height': page.rect.height, 'rotation': page.rotation,
            'coordinate_system': 'top-left-points', 'rectangle': rectangle}


def normalize_asset(data, asset, member, descriptor):
    """Return blocks, occurrences, additional pixel blobs, extraction status and facts."""
    blocks, figures, pixels, facts = [], [], {}, {}
    status = 'completed'
    media = asset['media_type']

    def block(text, locator, heading=None):
        blocks.append({'block_id': member['member_id'] + ':' + asset['sha256'][:12] + ':' + str(len(blocks)),
                       'asset_id': asset['asset_id'], 'text': text, 'locator': locator,
                       'heading': heading, 'derivation': descriptor.get('derivation', 'original'),
                       'language': asset['language']})

    def figure(data, locator):
        image = blob_record(data, 'image/png', 'figure')
        pixels[image['path']] = (image, data)
        figures.append({'figure_id': member['member_id'] + ':figure:' + asset['sha256'][:12] + ':' + str(len(figures)),
                        'member_id': member['member_id'], 'asset_id': asset['asset_id'],
                        'image_asset_id': image['asset_id'], 'locator': locator,
                        'caption': '', 'caption_status': 'not found',
                        'nearby_spans': [{'asset_id': asset['asset_id'], 'locator': b['locator']} for b in blocks[-1:]]})

    if media == 'application/pdf':
        import fitz
        with fitz.open(stream=data, filetype='pdf') as document:
            facts = {'pdf_metadata': document.metadata, 'physical_pages': len(document), 'headings': []}
            for index, page in enumerate(document):
                text = page.get_text(sort=True).rstrip('\n')
                heading = text.splitlines()[0] if text else None
                block(text, pdf_locator(page, index), heading)
                if heading:
                    facts['headings'].append(heading)
                if not text.strip():
                    status = 'ocr-required'
                elif text.count('\ufffd') > max(2, len(text) // 100):
                    status = 'extraction-failure'
                # Each display occurrence survives; identical pixels deduplicate later.
                for info in page.get_image_info(xrefs=True):
                    rect = list(info['bbox'])
                    if info['xref']:
                        pix = fitz.Pixmap(document, info['xref'])
                        if pix.colorspace and pix.colorspace.n > 3:
                            pix = fitz.Pixmap(fitz.csRGB, pix)
                        figure(pix.tobytes('png'), pdf_locator(page, index, rect))
                    else:
                        figure(page.get_pixmap(clip=fitz.Rect(rect), alpha=False).tobytes('png'), pdf_locator(page, index, rect))
                for drawing in page.get_drawings():
                    rect = drawing['rect'] & page.rect
                    if not rect.is_empty:
                        figure(page.get_pixmap(clip=rect, alpha=False).tobytes('png'), pdf_locator(page, index, list(rect)))
    elif media == 'application/epub+zip':
        resources, facts = epub_resources(data)
        for order, (resource, text) in enumerate(resources):
            block(text, {'kind': 'epub-resource', 'resource': resource, 'reading_order': order,
                         'start_offset': 0, 'end_offset': len(text)}, text.splitlines()[0] if text else None)
            if not text.strip():
                status = 'extraction-failure'
        from PIL import Image
        for locator, raw in epub_images(data):
            with Image.open(io.BytesIO(raw)) as image:
                output = io.BytesIO()
                image.save(output, format='PNG')
            figure(output.getvalue(), locator)
            figures[-1]['nearby_spans'] = [{'asset_id': asset['asset_id'], 'locator': b['locator']} for b in blocks if b['locator']['reading_order'] == locator['reading_order']]
    elif media == 'text/vtt':
        for cue_id, start, end, text in cues(data):
            block(text, {'kind': 'caption-cue', 'lesson_id': member['member_id'], 'cue_id': cue_id,
                         'start_seconds': start, 'end_seconds': end})
    elif media in ('text/html', 'application/xhtml+xml'):
        text = html_text(data.decode('utf-8'))
        block(text, {'kind': 'html-text', 'start_offset': 0, 'end_offset': len(text)}, text.splitlines()[0] if text else None)
    elif media.startswith('text/'):
        try:
            text = data.decode('utf-8')
            if '\0' in text:
                raise UnicodeError('Binary file')
            lines = max(1, len(text.splitlines()))
            if descriptor.get('commit'):
                locator = {'kind': 'code-lines', 'commit': descriptor['commit'], 'path': descriptor['repo_path'], 'start_line': 1, 'end_line': lines}
            else:
                locator = {'kind': 'markdown-lines', 'path': asset['path'], 'start_line': 1, 'end_line': lines}
            block(text.rstrip('\n'), locator, text.splitlines()[0] if text else None)
        except UnicodeError:
            status = 'extraction-failure'
    else:
        status = 'not-applicable'
    return blocks, figures, pixels, status, facts


def resolve(data, locator):
    """Open the exact normalized text or bytes named by a locator."""
    kind = locator['kind']
    if kind in ('markdown-lines', 'code-lines'):
        lines = data.decode('utf-8').splitlines()
        if not 1 <= locator['start_line'] <= locator['end_line'] <= max(1, len(lines)):
            raise ValueError('Line locator is outside the named file.')
    if kind == 'pdf-page':
        import fitz
        with fitz.open(stream=data, filetype='pdf') as document:
            page = document[locator['page'] - 1]
            if (page.rect.width, page.rect.height, page.rotation, page.get_label() or None) != (locator['width'], locator['height'], locator['rotation'], locator['page_label']):
                raise ValueError('PDF locator geometry mismatch.')
            if locator['rectangle'] is not None:
                return page.get_pixmap(clip=fitz.Rect(locator['rectangle']), alpha=False).tobytes('png')
            return page.get_text(sort=True).rstrip('\n')
    if kind == 'epub-resource':
        resources, _ = epub_resources(data)
        resource, text = resources[locator['reading_order']]
        if resource != locator['resource']:
            raise ValueError('EPUB reading order mismatch.')
        if not 0 <= locator['start_offset'] <= locator['end_offset'] <= len(text):
            raise ValueError('EPUB locator offset is outside the resource.')
        return text[locator['start_offset']:locator['end_offset']]
    if kind == 'epub-image':
        from PIL import Image
        for actual, raw in epub_images(data):
            if actual == locator:
                with Image.open(io.BytesIO(raw)) as image:
                    output = io.BytesIO(); image.save(output, format='PNG')
                    return output.getvalue()
        raise ValueError('EPUB image occurrence does not exist.')
    if kind == 'caption-cue':
        for cue_id, start, end, text in cues(data):
            if cue_id == locator['cue_id'] and start == locator['start_seconds'] and end == locator['end_seconds']:
                return text
        raise ValueError('Cue locator is not present in caption bytes.')
    if kind in ('markdown-lines', 'code-lines'):
        return '\n'.join(data.decode('utf-8').splitlines()[locator['start_line'] - 1:locator['end_line']])
    if kind == 'html-text':
        text = html_text(data.decode('utf-8'))
        if not 0 <= locator['start_offset'] <= locator['end_offset'] <= len(text):
            raise ValueError('HTML locator offset is outside the normalized text.')
        return text[locator['start_offset']:locator['end_offset']]
    if kind == 'asset-bytes':
        if not 0 <= locator['start_offset'] <= locator['end_offset'] <= len(data):
            raise ValueError('Byte locator offset is outside the asset.')
        return data[locator['start_offset']:locator['end_offset']]
    raise ValueError('Locator requires a frame timing observation.')
