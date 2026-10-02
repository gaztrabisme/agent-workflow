import json
import math
import os
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from copy import deepcopy
from io import BytesIO
from pathlib import Path
from lxml import etree

from pptx import Presentation
from pptx.chart.data import CategoryChartData, XyChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt
from pptx.oxml.xmlchemy import OxmlElement
from pptx.oxml.ns import qn

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
SCHEMA_ROOT = Path(__file__).resolve().parent.parent / 'schemas' / 'ecma-376'
PML_NS = 'http://schemas.openxmlformats.org/presentationml/2006/main'
DML_NS = 'http://schemas.openxmlformats.org/drawingml/2006/main'
CHART_NS = 'http://schemas.openxmlformats.org/drawingml/2006/chart'
PKG_REL_NS = 'http://schemas.openxmlformats.org/package/2006/relationships'
CONTENT_NS = 'http://schemas.openxmlformats.org/package/2006/content-types'
REL_ID_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
SCHEMA_BY_NAMESPACE = {
    PML_NS: SCHEMA_ROOT / 'transitional' / 'pml.xsd',
    DML_NS: SCHEMA_ROOT / 'transitional' / 'dml-main.xsd',
    CHART_NS: SCHEMA_ROOT / 'transitional' / 'dml-chart.xsd',
    'http://schemas.openxmlformats.org/spreadsheetml/2006/main': SCHEMA_ROOT / 'transitional' / 'sml.xsd',
    PKG_REL_NS: SCHEMA_ROOT / 'opc' / 'opc-relationships.xsd',
    CONTENT_NS: SCHEMA_ROOT / 'opc' / 'opc-contentTypes.xsd',
    'http://schemas.openxmlformats.org/package/2006/metadata/core-properties': SCHEMA_ROOT / 'opc' / 'opc-coreProperties.xsd',
    'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties': SCHEMA_ROOT / 'transitional' / 'shared-documentPropertiesExtended.xsd',
    'http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes': SCHEMA_ROOT / 'transitional' / 'shared-documentPropertiesVariantTypes.xsd',
    'http://schemas.openxmlformats.org/officeDocument/2006/custom-properties': SCHEMA_ROOT / 'transitional' / 'shared-documentPropertiesCustom.xsd',
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


def set_alt_text(shape, alt):
    c_nv_pr = shape._element.find(f'.//{{{PML_NS}}}cNvPr')
    if c_nv_pr is not None:
        c_nv_pr.set('descr', alt or '')


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
    paragraphs = layer.get('bullets') or [{'text': text, 'kind': 'none'} for text in layer.get('text', '').split('\n')]
    for index, item in enumerate(paragraphs):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        bullet = item if isinstance(item, dict) else {'text': item, 'kind': 'bullet', 'level': 0}
        paragraph.text = str(bullet.get('text', ''))
        paragraph.level = int(bullet.get('level', 0))
        paragraph.font.name = emitted
        paragraph.font.size = Pt(float(style.get('fontSize', 32)) * 0.5)
        paragraph.font.bold = int(style.get('fontWeight', 400)) >= 600
        paragraph.font.color.rgb = color(style.get('color', '#111111'))
        paragraph.alignment = {'left': PP_ALIGN.LEFT, 'center': PP_ALIGN.CENTER, 'right': PP_ALIGN.RIGHT}.get(style.get('align', 'left'), PP_ALIGN.LEFT)
        paragraph_properties = paragraph._p.get_or_add_pPr()
        for existing in list(paragraph_properties):
            if existing.tag in {qn('a:buChar'), qn('a:buAutoNum'), qn('a:buNone')}:
                paragraph_properties.remove(existing)
        bullet_kind = bullet.get('kind', 'bullet') if layer.get('bullets') else 'none'
        if bullet_kind == 'number':
            auto_num = OxmlElement('a:buAutoNum'); auto_num.set('type', 'arabicPeriod'); bullet_element = auto_num
        elif bullet_kind == 'bullet':
            char = OxmlElement('a:buChar'); char.set('char', '•'); bullet_element = char
        else:
            bullet_element = OxmlElement('a:buNone')
        insertion = next((position for position, child in enumerate(paragraph_properties) if child.tag in {qn('a:tabLst'), qn('a:defRPr'), qn('a:extLst')}), len(paragraph_properties))
        paragraph_properties.insert(insertion, bullet_element)
    reason = None if emitted == requested else 'font substituted to Arial'
    unsupported_text_effects = effect_reasons(layer)
    if unsupported_text_effects:
        reason = '; '.join(filter(None, [reason, f"unsupported text effects dropped: {', '.join(unsupported_text_effects)}"]))
    mapping.append({'layerId': layer['id'], 'representation': 'native-text', 'reason': reason, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
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
    if layer.get('shape') == 'roundRect' and 'radiusPx' in layer:
        short_side = min(float(layer['width']), float(layer['height']))
        adjustment = round(min(0.5, float(layer['radiusPx']) / short_side) * 100000) if short_side else 0
        geometry = shape._element.spPr.prstGeom
        av_list = geometry.find(qn('a:avLst'))
        if av_list is None:
            av_list = OxmlElement('a:avLst')
            geometry.append(av_list)
        guide = av_list.find(qn('a:gd'))
        if guide is None:
            guide = OxmlElement('a:gd')
            av_list.append(guide)
        guide.set('name', 'adj')
        guide.set('fmla', f'val {adjustment}')
    mapping.append({'layerId': layer['id'], 'representation': 'native-shape', 'reason': None, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
    return shape


def effect_reasons(layer):
    effects = layer.get('effects') or {}
    result = []
    if effects.get('blurPx'): result.append('blur')
    if effects.get('backdropBlurPx'): result.append('backdrop blur')
    if effects.get('blendMode'): result.append(f"blend mode {effects['blendMode']}")
    if effects.get('transform3d'): result.append('3D transform')
    if effects.get('mask'): result.append('layer mask')
    return result


def add_secondary_axis(chart):
    plot_area = chart._chartSpace.chart.plotArea
    value_axes = plot_area.findall(qn('c:valAx'))
    category_axes = plot_area.findall(qn('c:catAx'))
    if not value_axes or not category_axes:
        raise ValueError('Combo chart requires a category axis and primary value axis.')
    category_id = category_axes[0].find(qn('c:axId')).get('val')
    secondary = deepcopy(value_axes[0])
    secondary.find(qn('c:axId')).set('val', '100001')
    secondary.find(qn('c:crossAx')).set('val', category_id)
    position = secondary.find(qn('c:axPos'))
    if position is not None: position.set('val', 'r')
    crosses = secondary.find(qn('c:crosses'))
    if crosses is None:
        crosses = OxmlElement('c:crosses'); secondary.append(crosses)
    crosses.set('val', 'max')
    plot_area.append(secondary)
    return '100001'


def normalize_chart_axis_ids(chart):
    plot_area = chart._chartSpace.chart.plotArea
    axis_tags = {qn('c:catAx'), qn('c:valAx'), qn('c:dateAx'), qn('c:serAx')}
    axes = [child for child in plot_area if child.tag in axis_tags]
    identifiers = {}
    for index, axis in enumerate(axes, start=1):
        old = axis.find(qn('c:axId')).get('val')
        new = str(110000 + index)
        identifiers[old] = new
        axis.find(qn('c:axId')).set('val', new)
    for axis in axes:
        cross = axis.find(qn('c:crossAx'))
        if cross is not None and cross.get('val') in identifiers:
            cross.set('val', identifiers[cross.get('val')])
    chart_tags = {qn('c:barChart'), qn('c:lineChart'), qn('c:areaChart'), qn('c:pieChart'), qn('c:doughnutChart'), qn('c:scatterChart'), qn('c:radarChart'), qn('c:surfaceChart'), qn('c:stockChart')}
    for plot in plot_area:
        if plot.tag in chart_tags:
            for axis_id in plot.findall(qn('c:axId')):
                if axis_id.get('val') in identifiers:
                    axis_id.set('val', identifiers[axis_id.get('val')])
            grouping = plot.find(qn('c:grouping'))
            if grouping is not None and grouping.get('val') == 'clustered':
                grouping.set('val', 'standard')


def configure_combo_chart(chart, layer):
    plot_area = chart._chartSpace.chart.plotArea
    base = plot_area.find(qn('c:barChart'))
    if base is None:
        raise ValueError('Combo chart base plot was not created.')
    original_series = base.findall(qn('c:ser'))
    if len(original_series) != len(layer['series']):
        raise ValueError('Combo chart series did not map to the generated workbook.')
    category_id = plot_area.find(qn('c:catAx')).find(qn('c:axId')).get('val')
    primary_value_id = plot_area.find(qn('c:valAx')).find(qn('c:axId')).get('val')
    secondary_value_id = add_secondary_axis(chart) if any(item.get('axis') == 'secondary' for item in layer['series']) else primary_value_id
    grouped = {}
    for source, series in zip(original_series, layer['series']):
        chart_kind = series.get('kind') or 'column'
        grouped.setdefault((chart_kind, series.get('axis', 'primary')), []).append(source)
    plot_area.remove(base)
    chart_elements = []
    for (chart_kind, axis), source_series in grouped.items():
        tag = {'column': 'barChart', 'line': 'lineChart', 'area': 'areaChart'}[chart_kind]
        plot = deepcopy(base)
        plot.tag = qn(f'c:{tag}')
        for current in plot.findall(qn('c:ser')): plot.remove(current)
        if tag != 'barChart':
            for name in ('barDir', 'gapWidth', 'overlap', 'serLines'):
                current = plot.find(qn(f'c:{name}'))
                if current is not None: plot.remove(current)
        else:
            bar_direction = plot.find(qn('c:barDir'))
            if bar_direction is not None: bar_direction.set('val', 'col')
        for source in source_series:
            cloned = deepcopy(source)
            pivot = next((i for i, child in enumerate(plot) if child.tag not in {qn('c:barDir'), qn('c:grouping'), qn('c:varyColors')}), len(plot))
            plot.insert(pivot, cloned)
        axis_ids = plot.findall(qn('c:axId'))
        if len(axis_ids) < 2: raise ValueError('Combo plot is missing category/value axis references.')
        axis_ids[0].set('val', category_id)
        axis_ids[1].set('val', secondary_value_id if axis == 'secondary' else primary_value_id)
        chart_elements.append(plot)
    insert_at = 1 if len(plot_area) and plot_area[0].tag == qn('c:layout') else 0
    for offset, element in enumerate(chart_elements): plot_area.insert(insert_at + offset, element)


def apply_chart_style(chart, layer):
    style = layer.get('style') or {}
    font_size = style.get('fontSize')
    font_family = style.get('fontFamily')
    font_points = Pt(float(font_size) * 0.5) if font_size is not None else None
    if font_size is not None:
        chart.font.size = font_points
    if font_family:
        chart.font.name = str(font_family)
    if chart.has_legend:
        if font_size is not None: chart.legend.font.size = font_points
        if font_family: chart.legend.font.name = str(font_family)

    plot_area = chart._chartSpace.chart.plotArea
    has_category_axis = plot_area.find(qn('c:catAx')) is not None
    has_value_axis = plot_area.find(qn('c:valAx')) is not None
    category_axis = chart.category_axis if has_category_axis or layer.get('kind') == 'scatter' else None
    value_axis = chart.value_axis if has_value_axis else None
    horizontal_bar = str(layer.get('kind', '')).startswith('bar')
    x_axis, y_axis = (value_axis, category_axis) if horizontal_bar else (category_axis, value_axis)
    if style.get('axisTitleX') and x_axis is not None:
        x_axis.has_title = True
        x_axis.axis_title.text_frame.text = str(style['axisTitleX'])
    if style.get('axisTitleY') and y_axis is not None:
        y_axis.has_title = True
        y_axis.axis_title.text_frame.text = str(style['axisTitleY'])
    if style.get('numberFormat') and value_axis is not None:
        value_axis.tick_labels.number_format = str(style['numberFormat'])
    if style.get('gridColor') and value_axis is not None:
        value_axis.has_major_gridlines = True
        value_axis.major_gridlines.format.line.color.rgb = color(style['gridColor'])

    colors = style.get('seriesColors') or []
    if colors:
        series_nodes = plot_area.findall('.//c:ser', {'c': CHART_NS})
        for traversal_index, series in enumerate(series_nodes):
            index_node = series.find(qn('c:idx'))
            try:
                index = int(index_node.get('val')) if index_node is not None else traversal_index
            except (TypeError, ValueError):
                index = traversal_index
            if index >= len(colors): continue
            plot = series.getparent()
            is_line = plot.tag in {qn('c:lineChart'), qn('c:scatterChart')}
            properties = series.find(qn('c:spPr'))
            if properties is None:
                properties = OxmlElement('c:spPr')
                series.insert(3, properties)
            for fill in list(properties):
                if fill.tag in {qn('a:noFill'), qn('a:solidFill'), qn('a:gradFill'), qn('a:blipFill'), qn('a:pattFill'), qn('a:grpFill')}:
                    properties.remove(fill)
            solid = OxmlElement('a:solidFill')
            srgb = OxmlElement('a:srgbClr')
            srgb.set('val', str(colors[index]).lstrip('#').upper())
            solid.append(srgb)
            if is_line:
                line = properties.find(qn('a:ln'))
                if line is None:
                    line = OxmlElement('a:ln')
                    properties.append(line)
                for fill in list(line):
                    if fill.tag in {qn('a:noFill'), qn('a:solidFill'), qn('a:gradFill'), qn('a:blipFill'), qn('a:pattFill'), qn('a:grpFill')}:
                        line.remove(fill)
                line.insert(0, solid)
            else:
                properties.insert(0, solid)


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
    if layer.get('kind') == 'combo': configure_combo_chart(chart, layer)
    normalize_chart_axis_ids(chart)
    chart.has_legend = bool(layer.get('showLegend', True))
    if chart.has_legend:
        chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.has_title = False
    apply_chart_style(chart, layer)
    if layer.get('showValues'):
        for series in chart.series:
            series.has_data_labels = True
    mapping.append({'layerId': layer['id'], 'representation': 'native-chart', 'reason': None, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
    workbook_checks.append({'layerId': layer['id'], 'chartPart': str(chart.part.partname).lstrip('/'), 'status': 'pending', 'categories': layer.get('categories', []), 'seriesData': layer['series'], 'workbookGeneratedBy': 'python-pptx'})
    return chart


def add_layer(slide, layer, root, scene_id, mapping, font_report, workbook_checks, slide_number=1, svg_records=None):
    kind = layer['type']
    if kind == 'text':
        return add_text(slide, layer, mapping, font_report, scene_id)
    if layer.get('_pptxRaster'):
        picture = slide.shapes.add_picture(layer['_pptxRaster'], inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']))
        set_object_name(picture, layer.get('name') or layer['id'])
        set_alt_text(picture, layer.get('alt', ''))
        is_svg = kind == 'image' and Path(layer.get('src', '')).suffix.lower() == '.svg'
        if is_svg and svg_records is not None:
            svg_records.append({'slide': slide_number, 'shapeId': picture.shape_id, 'source': str((root / layer['src']).resolve())})
        mapping.append({'layerId': layer['id'], 'representation': 'native-svg-with-png-fallback' if is_svg else 'rasterized-layer', 'reason': layer.get('_pptxRasterReason') or ', '.join(effect_reasons(layer)), 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False), 'scale': '2x'})
        return picture
    if kind == 'shape':
        return add_shape(slide, layer, mapping)
    if kind == 'image':
        image_path = (root / layer['src']).resolve()
        picture = slide.shapes.add_picture(str(image_path), inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']))
        set_object_name(picture, layer.get('name') or layer['id'])
        set_alt_text(picture, layer.get('alt', ''))
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
        for child in layer.get('children', []): add_layer(slide, child, root, scene_id, mapping, font_report, workbook_checks, slide_number, svg_records)
        return None
    if kind == 'video':
        source = (root / layer['src']).resolve()
        poster = (root / layer['poster']).resolve() if layer.get('poster') else None
        try:
            movie = slide.shapes.add_movie(str(source), inch(layer['x']), inch(layer['y']), inch(layer['width']), inch(layer['height']), poster_frame_image=str(poster) if poster else None, mime_type='video/mp4')
            set_alt_text(movie, layer.get('alt', ''))
            mapping.append({'layerId': layer['id'], 'representation': 'native-movie', 'reason': None, 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
            return movie
        except Exception as error:
            mapping.append({'layerId': layer['id'], 'representation': 'unsupported', 'reason': str(error), 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
            return None
    mapping.append({'layerId': layer['id'], 'representation': 'unsupported', 'reason': f'{kind} export is not implemented; video capture remains in MP4 output', 'alt': layer.get('alt', ''), 'decorative': layer.get('decorative', False)})
    return None


class SchemaResolver(etree.Resolver):
    def resolve(self, url, public_id, context):
        external = {
            'http://dublincore.org/schemas/xmls/qdc/2003/04/02/dc.xsd': SCHEMA_ROOT / 'dublin-core' / 'dc.xsd',
            'http://dublincore.org/schemas/xmls/qdc/2003/04/02/dcterms.xsd': SCHEMA_ROOT / 'dublin-core' / 'dcterms.xsd',
            'http://www.dublincore.org/schemas/xmls/qdc/2003/04/02/dcmitype.xsd': SCHEMA_ROOT / 'dublin-core' / 'dcmitype.xsd',
            'http://www.w3.org/2001/03/xml.xsd': SCHEMA_ROOT / 'dublin-core' / 'xml.xsd',
        }
        if url in external:
            return self.resolve_filename(str(external[url]), context)
        return None


SCHEMA_CACHE = {}


def xml_schema(path):
    key = str(path)
    if key not in SCHEMA_CACHE:
        parser = etree.XMLParser(resolve_entities=False, no_network=True)
        parser.resolvers.add(SchemaResolver())
        SCHEMA_CACHE[key] = etree.XMLSchema(etree.parse(key, parser))
    return SCHEMA_CACHE[key]


def check_xml_parts(parts, errors):
    checked = 0
    for name, payload in parts:
        if not (name.endswith('.xml') or name.endswith('.rels') or name == '[Content_Types].xml'):
            continue
        try:
            document = etree.fromstring(payload)
        except etree.XMLSyntaxError as error:
            errors.append({'part': name, 'reason': str(error), 'code': 'PPTX_SCHEMA_INVALID'}); continue
        namespace = etree.QName(document).namespace
        schema_path = SCHEMA_BY_NAMESPACE.get(namespace)
        if schema_path is None or not schema_path.exists():
            errors.append({'part': name, 'namespace': namespace, 'reason': 'No vendored ECMA-376 schema is registered for this part.', 'code': 'PPTX_SCHEMA_INVALID'}); continue
        try:
            schema = xml_schema(schema_path)
            if namespace == PML_NS and document.tag == f'{{{PML_NS}}}sld':
                alternates = document.findall('{http://schemas.openxmlformats.org/markup-compatibility/2006}AlternateContent')
                for alternate in alternates:
                    choices = alternate.findall('{http://schemas.openxmlformats.org/markup-compatibility/2006}Choice')
                    fallbacks = alternate.findall('{http://schemas.openxmlformats.org/markup-compatibility/2006}Fallback')
                    if len(choices) != 1 or len(fallbacks) != 1:
                        raise ValueError('Markup compatibility transition must contain one Choice and one Fallback.')
                    choice = choices[0]; fallback = fallbacks[0]
                    transition = choice.find(f'{{{PML_NS}}}transition')
                    morph = transition.find('{http://schemas.microsoft.com/office/powerpoint/2015/09/main}morph') if transition is not None else None
                    if transition is None or morph is None or choice.attrib.get('Requires') != 'p159' or morph.attrib.get('option') not in {'byObject', 'byWord', 'byChar'}:
                        raise ValueError('Morph Choice is missing its required p159 transition markup.')
                    fallback_transition = fallback.find(f'{{{PML_NS}}}transition')
                    if fallback_transition is None:
                        raise ValueError('Morph transition requires a valid fallback transition.')
                    for branch, is_morph in ((transition, True), (fallback_transition, False)):
                        clone = deepcopy(document)
                        clone_alt = clone.find('{http://schemas.openxmlformats.org/markup-compatibility/2006}AlternateContent')
                        candidate = deepcopy(branch)
                        if is_morph:
                            candidate_morph = candidate.find('{http://schemas.microsoft.com/office/powerpoint/2015/09/main}morph')
                            if candidate_morph is None: raise ValueError('Morph transition extension is malformed.')
                            candidate.remove(candidate_morph); candidate.append(OxmlElement('p:fade'))
                        clone.replace(clone_alt, candidate)
                        if not schema.validate(clone): raise ValueError(f'Morph transition base markup does not satisfy ECMA-376: {schema.error_log.last_error}')
                    document_for_schema = deepcopy(document)
                    document_alt = document_for_schema.find('{http://schemas.openxmlformats.org/markup-compatibility/2006}AlternateContent')
                    document_for_schema.remove(document_alt)
                if not schema.validate(document_for_schema if alternates else document):
                    raise ValueError(str(schema.error_log.last_error))
            elif not schema.validate(document):
                raise ValueError(str(schema.error_log.last_error))
            checked += 1
        except (ValueError, etree.XMLSchemaError) as error:
            errors.append({'part': name, 'reason': str(error), 'code': 'PPTX_SCHEMA_INVALID'})
        except (etree.XMLSchemaParseError, etree.XMLSyntaxError, OSError) as error:
            errors.append({'part': name, 'reason': f'Schema could not be loaded: {error}', 'code': 'PPTX_SCHEMA_INVALID'})
    return checked


def relationship_errors(names, parts):
    errors = []
    for name, payload in parts:
        if not name.endswith('.rels'): continue
        try: root = ET.fromstring(payload)
        except ET.ParseError as error:
            errors.append({'part': name, 'reason': str(error), 'code': 'PPTX_SCHEMA_INVALID'}); continue
        parent = Path(name).parent.parent
        for rel in root:
            target = rel.attrib.get('Target', '')
            if not target or rel.attrib.get('TargetMode') == 'External': continue
            normalized = posixpath.normpath((parent / target).as_posix())
            if normalized.startswith('../') or normalized not in names:
                errors.append({'part': name, 'target': target, 'reason': 'relationship target missing', 'code': 'PPTX_SCHEMA_INVALID'})
    return errors


def validate_package(filename):
    errors = []
    checked = 0
    with zipfile.ZipFile(filename) as archive:
        crc_error = archive.testzip()
        if crc_error: errors.append({'part': crc_error, 'reason': 'zip CRC failure', 'code': 'PPTX_SCHEMA_INVALID'})
        names = set(archive.namelist())
        parts = [(name, archive.read(name)) for name in names if name.endswith(('.xml', '.rels')) or name == '[Content_Types].xml']
        checked += check_xml_parts(parts, errors)
        errors.extend(relationship_errors(names, parts))
        content_types = next((payload for name, payload in parts if name == '[Content_Types].xml'), None)
        if content_types:
            root = ET.fromstring(content_types)
            defaults = {item.attrib.get('Extension', '').lower() for item in root if item.tag == f'{{{CONTENT_NS}}}Default'}
            overrides = {item.attrib.get('PartName', '').lstrip('/') for item in root if item.tag == f'{{{CONTENT_NS}}}Override'}
            for name in names:
                if name.endswith('/') or name in ('[Content_Types].xml',): continue
                extension = name.rsplit('.', 1)[-1].lower() if '.' in name else ''
                if extension not in defaults and name not in overrides:
                    errors.append({'part': name, 'reason': 'part has no content type declaration', 'code': 'PPTX_SCHEMA_INVALID'})
        for name in names:
            if not name.lower().endswith('.xlsx'): continue
            try:
                with zipfile.ZipFile(BytesIO(archive.read(name))) as workbook:
                    workbook_names = set(workbook.namelist())
                    workbook_parts = [(f'{name}!{item}', workbook.read(item)) for item in workbook_names if item.endswith(('.xml', '.rels')) or item == '[Content_Types].xml']
                    checked += check_xml_parts(workbook_parts, errors)
                    errors.extend(relationship_errors(workbook_names, [(item.split('!', 1)[-1], payload) for item, payload in workbook_parts]))
            except (zipfile.BadZipFile, OSError) as error:
                errors.append({'part': name, 'reason': f'embedded workbook is invalid: {error}', 'code': 'PPTX_SCHEMA_INVALID'})
    return errors, checked


def chart_formula_values(formula, workbook):
    match = re.fullmatch(r"(?:'((?:[^']|'')+)'|([^!]+))!\$?([A-Z]+)\$?(\d+)(?::\$?([A-Z]+)\$?(\d+))?", formula or '')
    if not match: raise ValueError(f'Unsupported chart formula: {formula!r}')
    sheet = (match.group(1) or match.group(2)).replace("''", "'")
    start_col, start_row, end_col, end_row = match.group(3), int(match.group(4)), match.group(5) or match.group(3), int(match.group(6) or match.group(4))
    def col_number(column):
        result = 0
        for char in column: result = result * 26 + ord(char) - 64
        return result
    def col_label(number):
        result = ''
        while number:
            number, remainder = divmod(number - 1, 26)
            result = chr(65 + remainder) + result
        return result
    if sheet not in workbook['sheets']: raise ValueError(f'Formula refers to missing sheet {sheet!r}.')
    values = []
    for row in range(start_row, end_row + 1):
        for column in range(col_number(start_col), col_number(end_col) + 1):
            address = f'{col_label(column)}{row}'
            if address not in workbook['cells'][sheet]: raise ValueError(f'Formula refers to empty cell {sheet}!{address}.')
            values.append(workbook['cells'][sheet][address])
    return values


def read_embedded_workbook(payload):
    with zipfile.ZipFile(BytesIO(payload)) as workbook:
        ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main', 'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships', 'rel': PKG_REL_NS}
        root = ET.fromstring(workbook.read('xl/workbook.xml'))
        rels = ET.fromstring(workbook.read('xl/_rels/workbook.xml.rels'))
        targets = {item.attrib['Id']: item.attrib['Target'] for item in rels}
        sheets = {}
        cells = {}
        shared = []
        if 'xl/sharedStrings.xml' in workbook.namelist():
            strings = ET.fromstring(workbook.read('xl/sharedStrings.xml'))
            shared = [''.join(node.itertext()) for node in strings.findall('s:si', ns)]
        for sheet in root.findall('s:sheets/s:sheet', ns):
            name = sheet.attrib['name']; target = targets[sheet.attrib[f"{{{ns['r']}}}id"]]
            sheet_path = posixpath.normpath(target.lstrip('/') if target.startswith('/') else posixpath.join('xl', target))
            sheets[name] = sheet_path
            sheet_root = ET.fromstring(workbook.read(sheet_path))
            sheet_cells = {}
            for cell in sheet_root.findall('.//s:sheetData/s:row/s:c', ns):
                value = cell.find('s:v', ns)
                if cell.attrib.get('t') == 'inlineStr':
                    item = cell.find('s:is', ns); parsed = ''.join(item.itertext()) if item is not None else ''
                elif value is None:
                    continue
                elif cell.attrib.get('t') == 's':
                    parsed = shared[int(value.text)]
                else:
                    try: parsed = float(value.text)
                    except (TypeError, ValueError): parsed = value.text
                sheet_cells[cell.attrib['r']] = parsed
            cells[name] = sheet_cells
        return {'sheets': sheets, 'cells': cells}


def cache_values(reference):
    if reference is None: return []
    for tag in ('strCache', 'numCache'):
        cache = reference.find(f'{{{CHART_NS}}}{tag}')
        if cache is not None:
            points = cache.findall(f'{{{CHART_NS}}}pt')
            return [next(iter(point)).text for point in sorted(points, key=lambda item: int(item.attrib.get('idx', 0)))]
    return []


def same_values(actual, expected):
    if len(actual) != len(expected): return False
    for left, right in zip(actual, expected):
        if (isinstance(left, (int, float)) and not isinstance(left, bool)) or (isinstance(right, (int, float)) and not isinstance(right, bool)):
            try:
                if not math.isclose(float(left), float(right), rel_tol=1e-8, abs_tol=1e-8): return False
            except (TypeError, ValueError): return False
        elif str(left) != str(right): return False
    return True


def validate_chart_workbooks(filename, workbook_checks):
    errors = []
    checks = []
    expected_by_part = {entry['chartPart']: entry for entry in workbook_checks}
    with zipfile.ZipFile(filename) as archive:
        for chart_part, expected in expected_by_part.items():
            rels_part = posixpath.join(posixpath.dirname(chart_part), '_rels', posixpath.basename(chart_part) + '.rels')
            try:
                rels = ET.fromstring(archive.read(rels_part))
                workbook_rel = next(item for item in rels if item.attrib.get('Type', '').endswith('/package'))
                workbook_part = posixpath.normpath(posixpath.join(posixpath.dirname(chart_part), workbook_rel.attrib['Target']))
                embedded = read_embedded_workbook(archive.read(workbook_part))
                chart = ET.fromstring(archive.read(chart_part))
            except (KeyError, StopIteration, ET.ParseError, zipfile.BadZipFile, ValueError) as error:
                errors.append({'code': 'PPTX_WORKBOOK_MISMATCH', 'part': chart_part, 'reason': str(error)})
                continue
            series_expected = {item['name']: item for item in expected['seriesData']}
            series_count = 0
            try:
                for series in chart.findall('.//c:ser', {'c': CHART_NS}):
                    name_ref = series.find('c:tx/c:strRef/c:f', {'c': CHART_NS})
                    name_value = next(iter(series.findall('c:tx//c:v', {'c': CHART_NS})), None)
                    name = name_value.text if name_value is not None else ''
                    formulas = []
                    for ref in series.findall('.//c:strRef', {'c': CHART_NS}) + series.findall('.//c:numRef', {'c': CHART_NS}):
                        formula_element = ref.find('c:f', {'c': CHART_NS})
                        if formula_element is None: continue
                        formula = formula_element.text
                        actual_cells = chart_formula_values(formula, embedded)
                        cached = cache_values(ref)
                        if cached and not same_values(actual_cells, cached): raise ValueError(f'{formula} does not match chart cache values.')
                        formulas.append((formula, actual_cells))
                    expected_series = series_expected.get(name)
                    if expected_series:
                        actual_value = next((values for formula, values in reversed(formulas) if '!' in formula), [])
                        if not same_values(actual_value, expected_series['values']): raise ValueError(f'Series {name!r} formula cells do not match authored values.')
                        series_count += 1
                for category_ref in chart.findall('.//c:cat/c:strRef', {'c': CHART_NS}):
                    formula_element = category_ref.find('c:f', {'c': CHART_NS})
                    if formula_element is None: continue
                    actual = chart_formula_values(formula_element.text, embedded)
                    cached = cache_values(category_ref)
                    if cached and not same_values(actual, cached): raise ValueError(f"{formula_element.text} does not match cached category labels.")
                    if not same_values(actual, expected['categories']): raise ValueError(f"{formula_element.text} cells do not match authored categories.")
                if series_count != len(series_expected): raise ValueError('Chart formulas do not cover every authored series.')
            except ValueError as error:
                errors.append({'code': 'PPTX_WORKBOOK_MISMATCH', 'part': chart_part, 'reason': str(error)})
                continue
            checks.append({'layerId': expected['layerId'], 'chartPart': chart_part, 'status': 'pass', 'categories': len(expected['categories']), 'series': len(expected['seriesData']), 'workbookPart': workbook_part})
    return errors, checks


class PackageValidationError(RuntimeError):
    def __init__(self, code, details):
        super().__init__(details[0].get('reason', code) if details else code)
        self.code = code
        self.details = details


def validate_for_publish(staging, workbook_checks):
    schema_errors, parts_checked = validate_package(staging)
    if schema_errors: raise PackageValidationError('PPTX_SCHEMA_INVALID', schema_errors)
    workbook_errors, checked_workbooks = validate_chart_workbooks(staging, workbook_checks)
    if workbook_errors: raise PackageValidationError('PPTX_WORKBOOK_MISMATCH', workbook_errors)
    return parts_checked, checked_workbooks


def verify_and_publish(staging, output_path, workbook_checks):
    parts_checked, checked_workbooks = validate_for_publish(staging, workbook_checks)
    os.replace(staging, output_path)
    return parts_checked, checked_workbooks


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
            f'{{{r_uri}}}id': notes_rel.attrib['Id']
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


def add_timing_xml(filename, slide_animations):
    if not any(slide_animations.values()): return
    ET.register_namespace('a', DML_NS)
    ET.register_namespace('r', REL_ID_NS)
    ET.register_namespace('p', PML_NS)
    p = lambda name: f'{{{PML_NS}}}{name}'
    with zipfile.ZipFile(filename, 'r') as source:
        updates = {}
        for slide_number, animations in slide_animations.items():
            if not animations: continue
            part = f'ppt/slides/slide{slide_number}.xml'
            root = ET.fromstring(source.read(part))
            timing = ET.Element(p('timing'))
            tn_list = ET.SubElement(timing, p('tnLst'))
            root_par = ET.SubElement(tn_list, p('par'))
            root_ctn = ET.SubElement(root_par, p('cTn'), {'id': '1', 'dur': 'indefinite', 'restart': 'never', 'nodeType': 'tmRoot'})
            root_children = ET.SubElement(root_ctn, p('childTnLst'))
            sequence = ET.SubElement(root_children, p('seq'), {'concurrent': '1', 'nextAc': 'seek'})
            sequence_ctn = ET.SubElement(sequence, p('cTn'), {'id': '2', 'dur': 'indefinite', 'nodeType': 'mainSeq'})
            sequence_children = ET.SubElement(sequence_ctn, p('childTnLst'))
            for index, item in enumerate(animations):
                par = ET.SubElement(sequence_children, p('par'))
                ctn = ET.SubElement(par, p('cTn'), {'id': str(3 + index * 2), 'fill': 'hold'})
                conditions = ET.SubElement(ctn, p('stCondLst'))
                ET.SubElement(conditions, p('cond'), {'delay': str(item['delayMs'])})
                children = ET.SubElement(ctn, p('childTnLst'))
                effect = ET.SubElement(children, p('animEffect'), {'transition': 'in', 'filter': item['filter']})
                behavior = ET.SubElement(effect, p('cBhvr'))
                ET.SubElement(behavior, p('cTn'), {'id': str(4 + index * 2), 'dur': str(item['durationMs']), 'fill': 'hold'})
                target = ET.SubElement(behavior, p('tgtEl'))
                ET.SubElement(target, p('spTgt'), {'spid': str(item['shapeId'])})
            children = list(root)
            insertion = next((index for index, node in enumerate(children) if node.tag == p('extLst')), len(children))
            root.insert(insertion, timing)
            updates[part] = ET.tostring(root, encoding='UTF-8', xml_declaration=True)
        fd, temporary = tempfile.mkstemp(prefix='.scene-engine-timing-', suffix='.pptx', dir=Path(filename).parent)
        os.close(fd)
        try:
            with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as target:
                for item in source.infolist(): target.writestr(item, updates.get(item.filename, source.read(item.filename)))
            os.replace(temporary, filename)
        except Exception:
            try: os.unlink(temporary)
            except FileNotFoundError: pass
            raise


def add_morph_transitions(filename, slide_numbers):
    if not slide_numbers: return
    morph_xml = ('<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">'
                 '<mc:Choice xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main" Requires="p159">'
                 '<p:transition spd="med">'
                 '<p159:morph option="byObject"/></p:transition></mc:Choice>'
                 '<mc:Fallback><p:transition spd="med"><p:fade/></p:transition></mc:Fallback>'
                 '</mc:AlternateContent>')
    with zipfile.ZipFile(filename, 'r') as source:
        updates = {}
        for slide_number in slide_numbers:
            part = f'ppt/slides/slide{slide_number}.xml'
            content = source.read(part).decode('utf-8')
            marker = '</p:clrMapOvr>'
            if marker not in content: raise ValueError(f'Cannot insert Morph transition into {part}: p:clrMapOvr is missing.')
            updates[part] = content.replace(marker, marker + morph_xml, 1).encode('utf-8')
        fd, temporary = tempfile.mkstemp(prefix='.scene-engine-morph-', suffix='.pptx', dir=Path(filename).parent)
        os.close(fd)
        try:
            with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as target:
                for item in source.infolist(): target.writestr(item, updates.get(item.filename, source.read(item.filename)))
            os.replace(temporary, filename)
        except Exception:
            try: os.unlink(temporary)
            except FileNotFoundError: pass
            raise


def morph_slide_numbers(scenes):
    def names(layers):
        found = set()
        for layer in layers or []:
            name = layer.get('name') or ''
            if name.startswith('!!'): found.add(name)
            found.update(names(layer.get('children')))
        return found
    result = []
    for index in range(len(scenes) - 1):
        if names(scenes[index].get('layers')) & names(scenes[index + 1].get('layers')):
            result.append(index + 2)
    return result


def add_svg_fallbacks(filename, records):
    if not records: return
    a_ns = DML_NS
    p_ns = PML_NS
    r_ns = REL_ID_NS
    asvg_ns = 'http://schemas.microsoft.com/office/drawing/2016/SVG/main'
    ext_uri = '{96DAC541-7B7A-43D3-8B79-37D633B846F1}'
    ET.register_namespace('a', a_ns); ET.register_namespace('p', p_ns); ET.register_namespace('r', r_ns)
    ET.register_namespace('asvg', asvg_ns)
    with zipfile.ZipFile(filename, 'r') as source:
        updates = {}
        additions = {}
        content_types = ET.fromstring(source.read('[Content_Types].xml'))
        if not any(item.tag == f'{{{CONTENT_NS}}}Default' and item.attrib.get('Extension', '').lower() == 'svg' for item in content_types):
            ET.SubElement(content_types, f'{{{CONTENT_NS}}}Default', {'Extension': 'svg', 'ContentType': 'image/svg+xml'})
        ET.register_namespace('', CONTENT_NS)
        updates['[Content_Types].xml'] = ET.tostring(content_types, encoding='UTF-8', xml_declaration=True)
        rel_tag = f'{{{PKG_REL_NS}}}Relationship'
        for index, item in enumerate(records, start=1):
            slide_part = f"ppt/slides/slide{item['slide']}.xml"
            rels_part = f"ppt/slides/_rels/slide{item['slide']}.xml.rels"
            slide = ET.fromstring(updates.get(slide_part, source.read(slide_part)))
            rels_bytes = updates.get(rels_part, source.read(rels_part) if rels_part in source.namelist() else None)
            rels = ET.fromstring(rels_bytes) if rels_bytes else ET.Element(f'{{{PKG_REL_NS}}}Relationships')
            used = [int(match.group(1)) for relation in rels for match in [re.fullmatch(r'rId(\d+)', relation.attrib.get('Id', ''))] if match]
            rel_id = f'rId{max(used, default=0) + 1}'
            media_name = f'imageSvg{index}.svg'
            media_part = f'ppt/media/{media_name}'
            rel_target = f'../media/{media_name}'
            ET.SubElement(rels, rel_tag, {'Id': rel_id, 'Type': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image', 'Target': rel_target})
            picture = next((node for node in slide.findall('.//p:pic', {'p': p_ns}) if node.find('.//p:cNvPr', {'p': p_ns}) is not None and node.find('.//p:cNvPr', {'p': p_ns}).attrib.get('id') == str(item['shapeId'])), None)
            blip = picture.find('.//a:blip', {'a': a_ns}) if picture is not None else None
            if blip is None: raise ValueError(f"SVG fallback picture shape {item['shapeId']} was not found on slide {item['slide']}.")
            ext_list = blip.find(f'{{{a_ns}}}extLst')
            if ext_list is None: ext_list = ET.SubElement(blip, f'{{{a_ns}}}extLst')
            extension = ET.SubElement(ext_list, f'{{{a_ns}}}ext', {'uri': ext_uri})
            ET.SubElement(extension, f'{{{asvg_ns}}}svgBlip', {f'{{{r_ns}}}embed': rel_id})
            updates[slide_part] = ET.tostring(slide, encoding='UTF-8', xml_declaration=True)
            ET.register_namespace('', PKG_REL_NS)
            updates[rels_part] = ET.tostring(rels, encoding='UTF-8', xml_declaration=True)
            additions[media_part] = Path(item['source']).read_bytes()
        fd, temporary = tempfile.mkstemp(prefix='.scene-engine-svg-', suffix='.pptx', dir=Path(filename).parent)
        os.close(fd)
        try:
            with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as target:
                for part in source.infolist(): target.writestr(part, updates.get(part.filename, source.read(part.filename)))
                for name, payload in additions.items(): target.writestr(name, payload)
            os.replace(temporary, filename)
        except Exception:
            try: os.unlink(temporary)
            except FileNotFoundError: pass
            raise


def python_edit_roundtrip(filename, output_directory):
    # python-pptx 1.0.2's plot inspector does not accept ECMA's `standard`
    # grouping on a bar chart. Normalize only the private edit-test copy; the
    # published package retains the schema-valid authored value.
    python_input = Path(output_directory) / 'python-pptx-input.pptx'
    with zipfile.ZipFile(filename, 'r') as source:
        with zipfile.ZipFile(python_input, 'w', zipfile.ZIP_DEFLATED) as target:
            for item in source.infolist():
                payload = source.read(item.filename)
                if re.fullmatch(r'ppt/charts/chart\d+\.xml', item.filename):
                    root = ET.fromstring(payload)
                    for bar_chart in root.findall('.//c:barChart', {'c': CHART_NS}):
                        grouping = bar_chart.find('c:grouping', {'c': CHART_NS})
                        if grouping is not None and grouping.get('val') == 'standard': grouping.set('val', 'clustered')
                    payload = ET.tostring(root, encoding='UTF-8', xml_declaration=True)
                target.writestr(item, payload)
    reopened = Presentation(python_input)
    if not reopened.slides: raise ValueError('python-pptx could not reopen a deck with no slides.')
    text_shape = next((shape for slide in reopened.slides for shape in slide.shapes if shape.has_text_frame and shape.text_frame.text.strip()), None)
    geometry_shape = next((shape for slide in reopened.slides for shape in slide.shapes if hasattr(shape, 'left') and hasattr(shape, 'width')), None)
    if text_shape is None or geometry_shape is None: raise ValueError('Round trip fixture needs editable text and positioned shapes.')
    text_shape.text_frame.text += ' [roundtrip]'
    original_left = geometry_shape.left
    geometry_shape.left = original_left + 12700
    chart = next((shape.chart for slide in reopened.slides for shape in slide.shapes if shape.has_chart), None)
    expected_chart_values = None
    if chart is not None and chart.chart_type != XL_CHART_TYPE.XY_SCATTER:
        categories = [str(category.label) for category in chart.plots[0].categories]
        chart_data = CategoryChartData(); chart_data.categories = categories
        updated = {}
        for series in chart.series:
            values = [float(value) + 0.25 for value in series.values]
            chart_data.add_series(series.name, values); updated[series.name] = values
        chart.replace_data(chart_data)
        expected_chart_values = updated
    roundtrip_file = Path(output_directory) / 'python-pptx-roundtrip.pptx'
    reopened.save(roundtrip_file)
    restored = Presentation(roundtrip_file)
    restored_text = next((shape.text_frame.text for slide in restored.slides for shape in slide.shapes if shape.has_text_frame and shape.text_frame.text.strip()), '')
    if '[roundtrip]' not in restored_text: raise ValueError('python-pptx text edit did not persist after reopen.')
    restored_geometry = next((shape for slide in restored.slides for shape in slide.shapes if shape.name == geometry_shape.name), None)
    if restored_geometry is None or restored_geometry.left != original_left + 12700: raise ValueError('python-pptx geometry edit did not persist after reopen.')
    restored_chart = next((shape.chart for slide in restored.slides for shape in slide.shapes if shape.has_chart), None)
    if expected_chart_values is not None:
        if restored_chart is None: raise ValueError('python-pptx chart disappeared after reopen.')
        actual = {series.name: list(series.values) for series in restored_chart.series}
        for name, values in expected_chart_values.items():
            if name not in actual or not same_values(actual[name], values): raise ValueError(f'python-pptx chart data edit did not persist for series {name!r}.')
    return {'status': 'pass', 'text': 'edited and reopened', 'geometry': 'edited position and reopened', 'chartData': 'edited values and reopened' if expected_chart_values is not None else 'no native chart', 'libreOffice': 'not run'}


def libreoffice_roundtrip(filename, output_directory):
    executable = os.environ.get('SCENE_ENGINE_SOFFICE') or shutil.which('soffice')
    if not executable:
        return {'status': 'skipped', 'text': 'not run', 'geometry': 'not run', 'chartData': 'not run', 'libreOffice': 'soffice unavailable'}
    base = Path(output_directory)
    pptx_dir = base / 'libreoffice-pptx'; pdf_dir = base / 'libreoffice-pdf'; profile = base / 'libreoffice-profile'
    pptx_dir.mkdir(parents=True, exist_ok=True); pdf_dir.mkdir(parents=True, exist_ok=True)
    command_base = [executable, f'-env:UserInstallation={profile.as_uri()}', '--headless']
    conversion = subprocess.run([*command_base, '--convert-to', 'pptx:Impress MS PowerPoint 2007 XML', '--outdir', str(pptx_dir), filename], capture_output=True, text=True, timeout=120)
    converted = pptx_dir / Path(filename).name
    if conversion.returncode != 0 or not converted.exists():
        raise RuntimeError(f'LibreOffice PPTX round trip failed: {(conversion.stderr or conversion.stdout).strip()}')
    # Reopen the saved PPTX in a second LibreOffice process and render both sides of the round trip.
    pdf_a = pdf_dir / f'{Path(filename).stem}-original.pdf'
    pdf_b = pdf_dir / f'{Path(filename).stem}-roundtrip.pdf'
    original_pdf = subprocess.run([*command_base, '--convert-to', 'pdf:impress_pdf_Export', '--outdir', str(pdf_dir), filename], capture_output=True, text=True, timeout=120)
    generated_a = pdf_dir / f'{Path(filename).stem}.pdf'
    if original_pdf.returncode != 0 or not generated_a.exists(): raise RuntimeError(f'LibreOffice original PDF render failed: {(original_pdf.stderr or original_pdf.stdout).strip()}')
    generated_a.replace(pdf_a)
    roundtrip_pdf = subprocess.run([*command_base, '--convert-to', 'pdf:impress_pdf_Export', '--outdir', str(pdf_dir), str(converted)], capture_output=True, text=True, timeout=120)
    generated_b = pdf_dir / f'{Path(filename).stem}.pdf'
    if roundtrip_pdf.returncode != 0 or not generated_b.exists(): raise RuntimeError(f'LibreOffice round-trip PDF render failed: {(roundtrip_pdf.stderr or roundtrip_pdf.stdout).strip()}')
    generated_b.replace(pdf_b)
    return {'status': 'pass', 'text': 'opened, saved as PPTX and reopened', 'geometry': 'original and round-trip PDFs rendered', 'chartData': 'chart parts retained in round-trip PPTX', 'libreOffice': 'pass'}


def main():
    model_path, output_path, verify = sys.argv[1], sys.argv[2], sys.argv[3] == 'true'
    embed_video = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
    with open(model_path, encoding='utf-8') as stream: model = json.load(stream)
    root = Path(model['root']).resolve()
    story = model['story']
    output_file = Path(output_path).resolve()
    output_file.parent.mkdir(parents=True, exist_ok=True)
    prs = Presentation()
    prs.slide_width = Inches(40 / 3); prs.slide_height = Inches(7.5)
    # python-pptx keeps the template's ``screen4x3`` preset after the custom
    # 16:9 extents are assigned. Keynote rejects that contradictory package
    # metadata, so label the dimensions with their matching standard preset.
    prs.part._element.sldSz.set('type', 'screen16x9')
    blank = prs.slide_layouts[6]
    mappings = []; font_report = []; workbook_checks = []; advances = []; pose_warnings = []; animations = {}; svg_records = []
    for scene in model['scenes']:
        slide = prs.slides.add_slide(blank)
        slide_number = len(prs.slides)
        animations[slide_number] = []
        bg = (scene.get('background') or story.get('background') or '#FFFFFF').lstrip('#')
        slide.background.fill.solid(); slide.background.fill.fore_color.rgb = color(bg)
        scene_mapping = []
        layers = list(enumerate(scene.get('layers', [])))
        layers.sort(key=lambda pair: (pair[1].get('z', 0), pair[0]))
        for _, layer in layers:
            if layer.get('type') == 'group':
                add_layer(slide, layer, root, scene['id'], scene_mapping, font_report, workbook_checks, slide_number, svg_records)
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
                    pose_warnings.append({'sceneId': scene['id'], 'layerId': sampled['id'], 'code': 'PPTX_POSE_INVISIBLE', 'message': 'Sampled pose is nearly invisible; emitted at full opacity.'})
                    sampled['opacity'] = 1
                if sampled.get('x', 0) < 0 or sampled.get('y', 0) < 0 or sampled.get('x', 0) + sampled.get('width', 0) > story['width'] or sampled.get('y', 0) + sampled.get('height', 0) > story['height']:
                    pose_warnings.append({'sceneId': scene['id'], 'layerId': sampled['id'], 'code': 'PPTX_POSE_CLIPPED', 'message': 'Sampled pose extends outside the slide bounds.'})
                if sampled.get('type') == 'text' and not math.isclose(float(sampled.get('scaleX', 1)), float(sampled.get('scaleY', 1)), abs_tol=1e-8):
                    pose_warnings.append({'sceneId': scene['id'], 'layerId': sampled['id'], 'code': 'PPTX_TEXT_REFLOW', 'message': 'Non-uniform text scaling can change line wrapping in PowerPoint.'})
                shape = add_layer(slide, sampled, root, scene['id'], scene_mapping, font_report, workbook_checks, slide_number, svg_records)
                entrance = sampled.get('entrance', 'none')
                entrance_filters = {'fade': 'fade', 'flyInLeft': 'fly(left)', 'flyInRight': 'fly(right)', 'flyInUp': 'fly(up)', 'flyInDown': 'fly(down)', 'wipeLeft': 'wipe(left)'}
                if entrance in entrance_filters and shape is not None:
                    animations[slide_number].append({'shapeId': shape.shape_id, 'filter': entrance_filters[entrance], 'durationMs': int(sampled.get('entranceDurationMs', 500)), 'delayMs': int(sampled.get('startMs', 0))})
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
    staging_handle, staging_name = tempfile.mkstemp(prefix='.scene-engine-export-', suffix='.pptx', dir=output_file.parent)
    os.close(staging_handle)
    staging = Path(staging_name)
    try:
        prs.save(staging)
        add_notes_master_reference(staging)
        add_timing_xml(staging, animations)
        add_morph_transitions(staging, morph_slide_numbers(model['scenes']))
        add_svg_fallbacks(staging, svg_records)
        try:
            parts_checked, checked_workbooks = validate_for_publish(staging, workbook_checks)
        except PackageValidationError as error:
            print(json.dumps({'error': {'code': error.code, 'details': error.details}}), file=sys.stderr)
            return 1
        workbook_checks = checked_workbooks
        round_trip = {'status': 'skipped', 'text': 'not run', 'geometry': 'not run', 'chartData': 'not run', 'libreOffice': 'not run'}
        if verify:
            with tempfile.TemporaryDirectory(prefix='scene-engine-pptx-verify-', dir=output_file.parent) as verify_directory:
                try:
                    round_trip = python_edit_roundtrip(staging, verify_directory)
                    lo_result = libreoffice_roundtrip(str(staging), verify_directory)
                    if lo_result['status'] == 'skipped': round_trip['libreOffice'] = lo_result['libreOffice']
                    else: round_trip.update(lo_result)
                except Exception as error:
                    print(json.dumps({'error': {'code': 'PPTX_ROUNDTRIP_FAILED', 'message': str(error)}}), file=sys.stderr)
                    return 1
        os.replace(staging, output_file)
        print(json.dumps({
            'slideCount': len(prs.slides), 'slideAdvanceMs': advances, 'mappings': mappings,
            'fontReport': font_report, 'workbookChecks': workbook_checks, 'poseWarnings': pose_warnings,
            'openXmlValidation': {'status': 'pass', 'partsChecked': parts_checked, 'relationshipErrors': []},
            'roundTrip': round_trip, 'captionsEmbedded': False,
            'captionsBySlide': [{'slide': i + 1, 'embedded': False, 'sidecarPath': None} for i in range(len(prs.slides))]
        }))
        return 0
    finally:
        try: staging.unlink()
        except FileNotFoundError: pass


if __name__ == '__main__':
    try:
        sys.exit(main())
    except PackageValidationError as error:
        print(json.dumps({'error': {'code': error.code, 'details': error.details}}), file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(json.dumps({'error': {'code': 'PPTX_SCHEMA_INVALID', 'message': str(error)}}), file=sys.stderr)
        sys.exit(1)
