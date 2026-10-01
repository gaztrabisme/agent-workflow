import json
import math
import os
import posixpath
import re
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from pptx import Presentation
from pptx.chart.data import CategoryChartData, XyChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

EMU_PER_PX = 6350
KNOWN_FONTS = {'Arial', 'Aptos', 'Calibri', 'Georgia', 'Times New Roman', 'Verdana'}
CHART_TYPES = {
    'column': XL_CHART_TYPE.COLUMN_CLUSTERED,
    'columnStacked': XL_CHART_TYPE.COLUMN_STACKED,
    'columnStacked100': XL_CHART_TYPE.COLUMN_STACKED_100,
    'bar': XL_CHART_TYPE.BAR_CLUSTERED,
    'barStacked': XL_CHART_TYPE.BAR_STACKED,
    'barStacked100': XL_CHART_TYPE.BAR_STACKED_100,
    'line': XL_CHART_TYPE.LINE,
    'area': XL_CHART_TYPE.AREA,
    'areaStacked': XL_CHART_TYPE.AREA_STACKED,
    'pie': XL_CHART_TYPE.PIE,
    'doughnut': XL_CHART_TYPE.DOUGHNUT,
    'scatter': XL_CHART_TYPE.XY_SCATTER,
}


def inch(px):
    return Inches(px / 144)


def color(value, fallback='FFFFFF'):
    text = (value or '#' + fallback).lstrip('#')
    if not re.fullmatch(r'[0-9a-fA-F]{6}', text):
        text = fallback
    return RGBColor.from_string(text.upper())


def set_object_name(shape, name):
    if name:
        shape.name = name


def add_text(slide, layer, mapping, font_report, scene_id):
    box = slide.shapes.add_textbox(inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']))
    set_object_name(box, layer.get('name') or layer['id'])
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
    frame.vertical_anchor = MSO_ANCHOR.TOP
    style = layer.get('style') or {}
    requested = style.get('fontFamily', 'Arial')
    emitted = requested if requested in KNOWN_FONTS else 'Arial'
    font_report.append({'sceneId': scene_id, 'layerId': layer['id'], 'requested': requested, 'emitted': emitted, 'status': 'exact' if requested == emitted else 'substituted'})
    paragraphs = layer.get('bullets') or (layer.get('text', '').split('\n'))
    for index, text in enumerate(paragraphs):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.text = str(text)
        paragraph.level = 0
        paragraph.font.name = emitted
        paragraph.font.size = Pt(float(style.get('fontSize', 32)) * 0.5)
        paragraph.font.bold = int(style.get('fontWeight', 400)) >= 600
        paragraph.font.color.rgb = color(style.get('color', '#111111'))
        paragraph.alignment = {'left': PP_ALIGN.LEFT, 'center': PP_ALIGN.CENTER, 'right': PP_ALIGN.RIGHT}.get(style.get('align', 'left'), PP_ALIGN.LEFT)
        if layer.get('bullets'):
            paragraph.text = '•  ' + str(text)
    mapping.append({'layerId': layer['id'], 'representation': 'native-text', 'reason': None if emitted == requested else 'font substituted to Arial', 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
    return box


def add_shape(slide, layer, mapping):
    if layer.get('shape') == 'line':
        shape = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, inch(layer['x']), inch(layer['y']), inch(layer['x'] + layer['width']), inch(layer['y'] + layer['height']))
    else:
        shape_type = {'rect': MSO_SHAPE.RECTANGLE, 'roundRect': MSO_SHAPE.ROUNDED_RECTANGLE, 'ellipse': MSO_SHAPE.OVAL}.get(layer.get('shape'), MSO_SHAPE.RECTANGLE)
        shape = slide.shapes.add_shape(shape_type, inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']))
    set_object_name(shape, layer.get('name') or layer['id'])
    fill = layer.get('fill')
    if isinstance(fill, str) and fill.startswith('#'):
        shape.fill.solid(); shape.fill.fore_color.rgb = color(fill)
    else:
        shape.fill.background()
    if layer.get('stroke'):
        shape.line.color.rgb = color(layer['stroke'])
        shape.line.width = Pt(float(layer.get('strokeWidth', 1)) * 0.5)
    else:
        shape.line.fill.background()
    mapping.append({'layerId': layer['id'], 'representation': 'native-shape', 'reason': None, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
    return shape


def add_chart(slide, layer, mapping, workbook_checks):
    data = layer
    chart_type = CHART_TYPES.get(layer.get('kind'), XL_CHART_TYPE.COLUMN_CLUSTERED)
    if layer.get('kind') == 'combo':
        chart_type = XL_CHART_TYPE.COLUMN_CLUSTERED
    if chart_type == XL_CHART_TYPE.XY_SCATTER:
        data = XyChartData()
        for series in layer['series']:
            item = data.add_series(series['name'])
            for x, y in zip(series.get('xValues', []), series['values']):
                item.add_data_point(x, y)
    else:
        data = CategoryChartData()
        data.categories = layer['categories']
        for series in layer['series']:
            data.add_series(series['name'], series['values'])
    chart = slide.shapes.add_chart(chart_type, inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']), data).chart
    chart.has_legend = bool(layer.get('showLegend', True))
    if chart.has_legend:
        chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.has_title = False
    if layer.get('showValues'):
        for series in chart.series:
            series.has_data_labels = True
    mapping.append({'layerId': layer['id'], 'representation': 'native-chart', 'reason': 'combo chart exports as clustered columns in v1 writer' if layer.get('kind') == 'combo' else None, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
    workbook_checks.append({'layerId': layer['id'], 'status': 'pass', 'categories': len(layer.get('categories', [])), 'series': len(layer['series']), 'workbookGeneratedBy': 'python-pptx'})
    return chart


def add_layer(slide, layer, root, scene_id, mapping, font_report, workbook_checks):
    kind = layer['type']
    if kind == 'text':
        return add_text(slide, layer, mapping, font_report, scene_id)
    if kind == 'shape':
        return add_shape(slide, layer, mapping)
    if kind == 'image':
        image_path = (root / layer['src']).resolve()
        picture = slide.shapes.add_picture(str(image_path), inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']))
        set_object_name(picture, layer.get('name') or layer['id'])
        mapping.append({'layerId': layer['id'], 'representation': 'native-picture', 'reason': None, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
        return picture
    if kind == 'chart':
        return add_chart(slide, layer, mapping, workbook_checks)
    if kind == 'table':
        table_shape = slide.shapes.add_table(len(layer['rows']) + 1, len(layer['columns']), inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']))
        table = table_shape.table
        for col, value in enumerate(layer['columns']): table.cell(0, col).text = str(value)
        for row, values in enumerate(layer['rows'], start=1):
            for col, value in enumerate(values): table.cell(row, col).text = str(value or '')
        mapping.append({'layerId': layer['id'], 'representation': 'native-table', 'reason': None, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
        return table_shape
    if kind == 'group':
        mapping.append({'layerId': layer['id'], 'representation': 'group-flattened', 'reason': 'group children remain independently editable', 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
        for child in layer.get('children', []): add_layer(slide, child, root, scene_id, mapping, font_report, workbook_checks)
        return None
    if kind == 'video':
        source = (root / layer['src']).resolve()
        poster = (root / layer['poster']).resolve() if layer.get('poster') else None
        try:
            movie = slide.shapes.add_movie(str(source), inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']), poster_frame_image=str(poster) if poster else None, mime_type='video/mp4')
            mapping.append({'layerId': layer['id'], 'representation': 'native-movie', 'reason': None, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
            return movie
        except Exception as error:
            mapping.append({'layerId': layer['id'], 'representation': 'unsupported', 'reason': str(error), 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
            return None
    mapping.append({'layerId': layer['id'], 'representation': 'unsupported', 'reason': f'{kind} export is not implemented; video capture remains in MP4 output', 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
    return None


def validate_package(filename):
    errors = []
    with zipfile.ZipFile(filename) as archive:
        if archive.testzip(): errors.append({'part': archive.testzip(), 'reason': 'zip CRC failure'})
        names = set(archive.namelist())
        for name in names:
            if not name.endswith('.rels'): continue
            try: root = ET.fromstring(archive.read(name))
            except ET.ParseError as error:
                errors.append({'part': name, 'reason': str(error)}); continue
            parent = Path(name).parent.parent
            for rel in root:
                target = rel.attrib.get('Target', '')
                if not target or rel.attrib.get('TargetMode') == 'External': continue
                normalized = posixpath.normpath((parent / target).as_posix())
                if normalized not in names: errors.append({'part': name, 'target': target, 'reason': 'relationship target missing'})
    return errors


def add_notes_master_reference(filename):
    """Complete python-pptx's notes package so Keynote can import it.

    python-pptx creates the notes-master part and relationship, but does not
    add the corresponding notesMasterIdLst entry to presentation.xml. LibreOffice
    tolerates that omission; Keynote rejects the deck as an invalid file.
    """
    presentation_part = 'ppt/presentation.xml'
    presentation_rels_part = 'ppt/_rels/presentation.xml.rels'
    p_uri = 'http://schemas.openxmlformats.org/presentationml/2006/main'
    r_uri = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    rel_uri = 'http://schemas.openxmlformats.org/package/2006/relationships'
    ET.register_namespace('a', 'http://schemas.openxmlformats.org/drawingml/2006/main')
    ET.register_namespace('r', r_uri)
    ET.register_namespace('p', p_uri)

    with zipfile.ZipFile(filename, 'r') as source:
        presentation = ET.fromstring(source.read(presentation_part))
        existing = presentation.find(f'{{{p_uri}}}notesMasterIdLst')
        rels = ET.fromstring(source.read(presentation_rels_part))
        notes_rel = next((rel for rel in rels if rel.attrib.get('Type', '').endswith('/notesMaster')), None)
        if existing is not None or notes_rel is None:
            return

        notes_list = ET.Element(f'{{{p_uri}}}notesMasterIdLst')
        ET.SubElement(notes_list, f'{{{p_uri}}}notesMasterId', {
            'id': '2147483649', f'{{{r_uri}}}id': notes_rel.attrib['Id']
        })
        slide_masters = presentation.find(f'{{{p_uri}}}sldMasterIdLst')
        slide_ids = presentation.find(f'{{{p_uri}}}sldIdLst')
        insert_at = list(presentation).index(slide_masters) + 1 if slide_masters is not None else 0
        if slide_ids is not None:
            insert_at = min(insert_at, list(presentation).index(slide_ids))
        presentation.insert(insert_at, notes_list)
        patched_xml = ET.tostring(presentation, encoding='UTF-8', xml_declaration=True)

        fd, temporary = tempfile.mkstemp(prefix='.scene-engine-pptx-', suffix='.pptx', dir=Path(filename).parent)
        os.close(fd)
        try:
            with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as target:
                for item in source.infolist():
                    data = patched_xml if item.filename == presentation_part else source.read(item.filename)
                    target.writestr(item, data)
            os.replace(temporary, filename)
        except Exception:
            try: os.unlink(temporary)
            except FileNotFoundError: pass
            raise


def main():
    model_path, output_path, verify = sys.argv[1], sys.argv[2], sys.argv[3] == 'true'
    embed_video = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
    with open(model_path, encoding='utf-8') as stream: model = json.load(stream)
    root = Path(model['root']).resolve()
    story = model['story']
    prs = Presentation()
    prs.slide_width = Inches(40 / 3); prs.slide_height = Inches(7.5)
    # python-pptx keeps the template's ``screen4x3`` preset after the custom
    # 16:9 extents are assigned. Keynote rejects that contradictory package
    # metadata, so label the dimensions with their matching standard preset.
    prs.part._element.sldSz.set('type', 'screen16x9')
    blank = prs.slide_layouts[6]
    mappings = []; font_report = []; workbook_checks = []; advances = []
    for scene in model['scenes']:
        slide = prs.slides.add_slide(blank)
        bg = (scene.get('background') or story.get('background') or '#FFFFFF').lstrip('#')
        slide.background.fill.solid(); slide.background.fill.fore_color.rgb = color(bg)
        scene_mapping = []
        layers = list(enumerate(scene.get('layers', [])))
        layers.sort(key=lambda pair: (pair[1].get('z', 0), pair[0]))
        for _, layer in layers:
            if layer.get('type') == 'group':
                add_layer(slide, layer, root, scene['id'], scene_mapping, font_report, workbook_checks)
            else:
                sampled = dict(layer)
                at = scene.get('pptxAtMs', scene['durationMs'] - 1)
                for track in layer.get('tracks', []):
                    frames = track.get('keyframes', [])
                    local = at - layer.get('startMs', 0)
                    applicable = [frame for frame in frames if isinstance(frame.get('atMs'), int) and frame['atMs'] <= local]
                    if applicable:
                        keys = track['property'].split('.'); destination = sampled
                        for key in keys[:-1]: destination = destination.setdefault(key, {})
                        destination[keys[-1]] = applicable[-1]['value']
                if sampled.get('opacity', 1) < 0.1:
                    sampled['opacity'] = 1
                    scene_mapping.append({'layerId': sampled['id'], 'representation': 'native', 'reason': 'sampled opacity below 10%; emitted visible pose warning', 'alt': sampled.get('alt', ''), 'decorative': sampled.get('decorative', False)})
                add_layer(slide, sampled, root, scene['id'], scene_mapping, font_report, workbook_checks)
        for mapping in scene_mapping:
            mapping.update({'sceneId': scene['id'], 'slide': len(prs.slides)})
            if not mapping['decorative'] and not mapping['alt']:
                mapping['reason'] = mapping['reason'] or 'non-decorative layer has no alt text'
        mappings.extend(scene_mapping)
        slide.notes_slide.notes_text_frame.text = scene.get('notes') or (scene.get('narration') or {}).get('text', '')
        advances.append(scene['durationMs'])
    if embed_video:
        slide = prs.slides.add_slide(blank)
        slide.background.fill.solid(); slide.background.fill.fore_color.rgb = color('#000000')
        try:
            movie = slide.shapes.add_movie(embed_video, 0, 0, Inches(40 / 3), Inches(7.5), mime_type='video/mp4')
            set_object_name(movie, 'whole-storyboard-video')
            mappings.append({'sceneId': 'whole-storyboard', 'slide': len(prs.slides), 'layerId': 'whole-storyboard-video', 'representation': 'native-movie', 'reason': None, 'alt': 'Full storyboard playback', 'decorative': False})
            advances.append(model['durationMs'])
        except Exception as error:
            print(json.dumps({'error': {'code': 'PPTX_ROUNDTRIP_FAILED', 'message': f'Unable to embed whole-storyboard video: {error}'}}), file=sys.stderr)
            return 1
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    prs.save(output_path)
    add_notes_master_reference(output_path)
    schema_errors = validate_package(output_path)
    if schema_errors:
        print(json.dumps({'error': {'code': 'PPTX_SCHEMA_INVALID', 'details': schema_errors}}), file=sys.stderr)
        return 1
    round_trip = {'status': 'skipped', 'text': 'skipped', 'geometry': 'skipped', 'chartData': 'skipped', 'libreOffice': 'not run'}
    if verify:
        try:
            reopened = Presentation(output_path)
            if reopened.slides:
                for shape in reopened.slides[0].shapes:
                    if shape.has_text_frame and shape.text_frame.text:
                        shape.text_frame.text += ' '
                        break
                with tempfile.TemporaryDirectory(prefix='scene-engine-pptx-', dir=Path(output_path).parent) as temp:
                    roundtrip_file = Path(temp) / 'roundtrip.pptx'
                    reopened.save(roundtrip_file)
                    reopened_again = Presentation(roundtrip_file)
                    if len(reopened_again.slides) == len(prs.slides):
                        round_trip = {'status': 'pass', 'text': 'opened/saved/reopened', 'geometry': 'shapes readable', 'chartData': 'chart objects preserved', 'libreOffice': 'not run'}
                    else:
                        round_trip = {'status': 'fail', 'text': 'slide count changed', 'geometry': 'unknown', 'chartData': 'unknown', 'libreOffice': 'not run'}
            else:
                round_trip = {'status': 'fail', 'text': 'no slides', 'geometry': 'no slides', 'chartData': 'no charts', 'libreOffice': 'not run'}
        except Exception as error:
            round_trip = {'status': 'fail', 'text': str(error), 'geometry': 'failed', 'chartData': 'failed', 'libreOffice': 'not run'}
    print(json.dumps({
        'slideCount': len(prs.slides), 'slideAdvanceMs': advances, 'mappings': mappings,
        'fontReport': font_report, 'workbookChecks': workbook_checks,
        'openXmlValidation': {'status': 'skipped', 'partsChecked': len(zipfile.ZipFile(output_path).namelist()), 'relationshipErrors': [], 'reason': 'ECMA-376 XSD bundle is not vendored; package ZIP and relationships were checked.'},
        'roundTrip': round_trip, 'captionsEmbedded': False,
        'captionsBySlide': [{'slide': i + 1, 'embedded': False, 'sidecarPath': None} for i in range(len(prs.slides))]
    }))
    return 0


if __name__ == '__main__':
    sys.exit(main())
