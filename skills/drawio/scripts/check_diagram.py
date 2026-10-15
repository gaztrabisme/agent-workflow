#!/usr/bin/env python3
"""
From the architecture-diagrams skill shared by its author, an FPT PM, on 13 Oct 2026; adapted with the
author's permission. Change: standard output is UTF-8, so a Windows console does not crash on
symbols in diagram labels.

check_diagram.py -- lint a draw.io / mxGraph XML diagram and render a wireframe
preview you can actually look at before shipping the diagram.

Why this exists: draw.io XML is written blind. The two failure modes that ruin a
diagram -- children placed with absolute canvas coordinates instead of
parent-relative ones, and shapes silently sitting on top of each other -- are
invisible in the source and obvious in the picture. This script surfaces both.

Usage:
    python3 check_diagram.py diagram.drawio                 # report + preview PNG
    python3 check_diagram.py diagram.drawio --png out.png   # choose preview path
    python3 check_diagram.py diagram.drawio --json          # machine-readable
    python3 check_diagram.py diagram.drawio --no-preview    # report only

Exit code is 1 if any ERROR-level finding is present, else 0.
"""

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

# --------------------------------------------------------------------------
# Model
# --------------------------------------------------------------------------


class Cell:
    __slots__ = ("id", "value", "style", "parent", "vertex", "edge", "source",
                 "target", "x", "y", "w", "h", "ax", "ay", "children", "sdict",
                 "lx", "ly")

    def __init__(self, el):
        self.id = el.get("id")
        self.value = (el.get("value") or "").strip()
        self.style = el.get("style") or ""
        self.parent = el.get("parent")
        self.vertex = el.get("vertex") == "1"
        self.edge = el.get("edge") == "1"
        self.source = el.get("source")
        self.target = el.get("target")
        geo = el.find("mxGeometry")
        self.x = _f(geo, "x")
        self.y = _f(geo, "y")
        self.w = _f(geo, "width")
        self.h = _f(geo, "height")
        self.ax = self.x          # absolute, resolved later
        self.ay = self.y
        self.children = []
        self.sdict = _parse_style(self.style)
        # an edge label can be pushed off the line with <mxPoint as="offset">
        self.lx = self.ly = 0.0
        if geo is not None:
            for pt in geo.findall("mxPoint"):
                if pt.get("as") == "offset":
                    self.lx = _numf(pt.get("x"), 0.0)
                    self.ly = _numf(pt.get("y"), 0.0)

    # convenience -------------------------------------------------------
    @property
    def is_container(self):
        return self.sdict.get("container") == "1" or "swimlane" in self.style or \
            "mxgraph.aws4.group" in self.style or self.sdict.get("childLayout") is not None

    @property
    def box(self):
        return (self.ax, self.ay, self.ax + self.w, self.ay + self.h)

    def label(self):
        t = re.sub(r"<br\s*/?>", " ", self.value, flags=re.I)
        t = re.sub(r"<[^>]+>", " ", t)
        t = _unescape(t)
        return re.sub(r"\s+", " ", t).strip()


def _unescape(t):
    import html
    return html.unescape(t)


def _f(geo, attr, default=0.0):
    if geo is None:
        return default
    try:
        return float(geo.get(attr) or default)
    except (TypeError, ValueError):
        return default


def _parse_style(style):
    out = {}
    for part in style.split(";"):
        if not part:
            continue
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
        else:
            out[part.strip()] = True
    return out


# An icon is a claim about technology. If the card's text names a different product,
# one of the two is wrong -- and the icon is the one readers trust. Keys are fragments
# of the stencil/URL; values are the words that legitimately go with that product.
PRODUCT_ALIASES = {
    "databricks": ["databricks", "lakeflow", "delta", "unity catalog", "auto loader",
                   "photon", "spark", "mlflow", "lakehouse", "medallion"],
    "data_factory": ["data factory", "adf", "integration runtime", "copy activity"],
    "event_hub": ["event hub", "eventhub", "kafka", "amqp", "iot hub"],
    "storage_account": ["storage", "adls", "blob", "volume", "data lake", "gen2", "object",
                        "file share", "landing"],
    "data_lake": ["data lake", "adls", "storage", "lakehouse", "gen2"],
    "powerbi": ["power bi", "powerbi", "pbi", "semantic model", "report", "dashboard"],
    "power_bi": ["power bi", "powerbi", "pbi", "semantic model", "report", "dashboard"],
    "machine_learning": ["machine learning", "mlflow", "model", "data science", "ml studio"],
    "active_directory": ["entra", "active directory", "aad", "identity", "sso", "oauth",
                         "grants", "access"],
    "sql_server": ["sql server", "mssql", "sql", "database", "oracle", "relational"],
    "api_management": ["api", "apim", "gateway", "rest"],
    "purview": ["purview", "catalog", "governance", "lineage", "glossary"],
    "synapse": ["synapse"],
    "cosmos": ["cosmos"],
    "log_analytics": ["log analytics", "kusto", "kql", "monitor", "logs"],
    "lambda": ["lambda", "function"],
    "kinesis": ["kinesis", "stream"],
    "snowflake": ["snowflake"],
    "bigquery": ["bigquery"],
}


def _icon_product(style):
    """The product an icon claims, as a lowercase slug, or None if it is not a product icon."""
    m = re.search(r"image=[^;]*?/([^/;]+)\.(?:svg|png)", style, re.I)
    if m:
        return m.group(1).lower()
    m = re.search(r"(?:resIcon=|shape=)mxgraph\.[a-z0-9_]+\.([a-z0-9_]+)", style, re.I)
    if m:
        return m.group(1).lower()
    return None


def _mentions(label, term):
    if len(term) <= 3:
        return re.search(r"\b%s\b" % re.escape(term), label) is not None
    return term in label


def load_cells(path):
    raw = open(path, "r", encoding="utf-8").read()
    # Tolerate a full <mxfile> wrapper, a bare <mxGraphModel>, or a naked <root>.
    try:
        root_el = ET.fromstring(raw)
    except ET.ParseError as e:
        print("ERROR: the file is not well-formed XML -- %s" % e, file=sys.stderr)
        sys.exit(2)

    models = root_el.iter("mxGraphModel")
    model = next(models, None)
    if model is None and root_el.tag == "mxGraphModel":
        model = root_el
    search_root = model if model is not None else root_el

    cells = []
    for el in search_root.iter("mxCell"):
        cells.append(Cell(el))
    # UserObject / object wrappers carry the label; the mxCell inside has the geometry.
    for el in search_root.iter():
        if el.tag in ("object", "UserObject"):
            inner = el.find("mxCell")
            if inner is not None:
                c = Cell(inner)
                c.id = el.get("id") or c.id
                c.value = (el.get("label") or c.value or "").strip()
                cells = [x for x in cells if x is not c]
                cells.append(c)
    return cells


def resolve(cells):
    by_id = {c.id: c for c in cells if c.id}
    for c in cells:
        p = by_id.get(c.parent)
        if p is not None:
            p.children.append(c)

    # Absolute coordinates: a child's geometry is relative to its parent's origin.
    def walk(cell, ox, oy, depth=0):
        if depth > 40:
            return
        cell.ax = cell.x + ox
        cell.ay = cell.y + oy
        for ch in cell.children:
            walk(ch, cell.ax, cell.ay, depth + 1)

    roots = [c for c in cells if c.parent not in by_id]
    for r in roots:
        walk(r, 0.0, 0.0)
    return by_id


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

ERROR, WARN, INFO = "ERROR", "WARN", "INFO"


def _inter_area(a, b):
    dx = min(a[2], b[2]) - max(a[0], b[0])
    dy = min(a[3], b[3]) - max(a[1], b[1])
    return dx * dy if dx > 0 and dy > 0 else 0.0


def _seg_hits_box(p, q, box, pad=2.0):
    """Crude but adequate: sample the segment and test containment."""
    x0, y0, x1, y1 = box
    x0, y0, x1, y1 = x0 + pad, y0 + pad, x1 - pad, y1 - pad
    for i in range(1, 24):
        t = i / 24.0
        x = p[0] + (q[0] - p[0]) * t
        y = p[1] + (q[1] - p[1]) * t
        if x0 < x < x1 and y0 < y < y1:
            return True
    return False


def analyse(cells, by_id):
    findings = []

    def add(sev, code, msg, cid=None):
        findings.append({"severity": sev, "code": code, "message": msg, "cell": cid})

    verts = [c for c in cells if c.vertex and c.w > 0 and c.h > 0]
    edges = [c for c in cells if c.edge]

    # A small unlabelled icon parented to a labelled card is decoration, not a shape the
    # reader counts. Treating it as one produces a flood of false "unlabelled shape"
    # findings, and a linter that cries wolf gets ignored -- which costs more than the
    # checks are worth.
    def _decorative(c):
        if c.label() or c.w * c.h > 3600:
            return False
        p = by_id.get(c.parent)
        return bool(p is not None and p.vertex and p.label())

    decor = {c.id for c in verts if _decorative(c)}
    real = [c for c in verts if c.id not in decor]

    # A composite service card (icon + title + a few capability rows) is ONE thing to the
    # reader even though it is several cells. Counting each row against the shape budget
    # would push every solution-architecture diagram over the limit for being detailed,
    # which is the whole point of the style.
    def _composite_child(c):
        p = by_id.get(c.parent)
        return bool(p is not None and p.vertex and p.label() and not p.is_container
                    and p.w * p.h > 6000)

    def _has_icon(c):
        if "shape=mxgraph." in c.style or "image=" in c.style:
            return True
        return any(k.id in decor and ("shape=mxgraph." in k.style or "image=" in k.style)
                   for k in c.children)

    # -- structural ----------------------------------------------------
    seen = {}
    for c in cells:
        if c.id in seen:
            add(ERROR, "duplicate_id", "Two cells share id '%s'; draw.io keeps only one." % c.id, c.id)
        seen[c.id] = c

    for e in edges:
        for end in ("source", "target"):
            ref = getattr(e, end)
            if ref is None:
                add(WARN, "loose_edge_end",
                    "Edge '%s' has no %s -- it will dangle in space instead of attaching to a shape."
                    % (e.label() or e.id, end), e.id)
            elif ref not in by_id:
                add(ERROR, "dangling_edge",
                    "Edge '%s' points at %s id '%s', which does not exist. The edge will not render."
                    % (e.label() or e.id, end, ref), e.id)

    # -- containment ---------------------------------------------------
    for c in verts:
        p = by_id.get(c.parent)
        if p is None or not (p.vertex and p.w > 0):
            continue
        cb, pb = c.box, p.box
        if _inter_area(cb, pb) <= 0:
            add(ERROR, "child_outside_parent",
                "'%s' sits entirely outside its parent '%s'. This is nearly always because its "
                "geometry was written in absolute canvas coordinates -- inside a container, x/y are "
                "measured from the container's top-left corner."
                % (c.label() or c.id, p.label() or p.id), c.id)
        elif cb[0] < pb[0] - 1 or cb[1] < pb[1] - 1 or cb[2] > pb[2] + 1 or cb[3] > pb[3] + 1:
            add(WARN, "child_overflows_parent",
                "'%s' spills past the edge of its parent '%s'; either shrink it or grow the container."
                % (c.label() or c.id, p.label() or p.id), c.id)

    # -- visual nesting that isn't real parenting ----------------------
    # A shape drawn inside a boundary box but parented to the layer looks right and
    # behaves wrong: drag the boundary in draw.io and its "contents" stay behind. For a
    # file the user will edit, that is a defect even though it renders correctly.
    def _is_ancestor(anc, node):
        cur, hop = by_id.get(node.parent), 0
        while cur is not None and hop < 25:
            if cur is anc:
                return True
            cur, hop = by_id.get(cur.parent), hop + 1
        return False

    boxes = [c for c in verts if c.w >= 150 and c.h >= 100]
    orphans = 0
    for c in verts:
        if c.w * c.h > 60000:
            continue
        holders = [b for b in boxes if b is not c
                   and _inter_area(c.box, b.box) / max(c.w * c.h, 1) > 0.9]
        if not holders:
            continue
        inner = min(holders, key=lambda b: b.w * b.h)
        if _is_ancestor(inner, c):
            continue
        orphans += 1
        if orphans <= 3:
            add(WARN, "nested_but_not_parented",
                "'%s' is drawn inside '%s' but is not parented to it. Set parent=\"%s\" and make "
                "its x/y relative to that box, so the group moves as one when the user edits the "
                "file." % (c.label() or c.id, inner.label() or inner.id, inner.id), c.id)
    if orphans > 3:
        add(WARN, "nested_but_not_parented",
            "%d shapes in total are drawn inside a boundary box without being parented to it. The "
            "picture is right but the file is fragile to edit." % orphans)

    # -- containers with a lot of dead space ---------------------------
    # Measured on the children's bounding extent, not their area: icons are small by
    # nature, so summed area says nothing, but a container that stretches 400px past its
    # last child is genuinely half-empty.
    for p in verts:
        kids = [k for k in p.children if k.vertex and k.w > 0]
        if len(kids) < 1 or p.w * p.h < 30000 or "swimlane" in p.style \
                or not p.is_container:
            continue
        # An icon's label is not part of its geometry but does occupy space, so give every
        # labelled child a realistic footprint before judging how much room is wasted.
        def _eff(k):
            lw = 170 if (k.label() and "verticalLabelPosition=bottom" in k.style) else k.w
            lh = k.h + (34 if (k.label() and "verticalLabelPosition=bottom" in k.style) else 0)
            cx, cy = k.ax + k.w / 2, k.ay + k.h / 2
            return (cx - max(k.w, lw) / 2, cy - k.h / 2, cx + max(k.w, lw) / 2, cy - k.h / 2 + lh)

        effs = [_eff(k) for k in kids]
        kx0 = min(e[0] for e in effs); kx1 = max(e[2] for e in effs)
        ky0 = min(e[1] for e in effs); ky1 = max(e[3] for e in effs)
        slack_w = 1 - ((kx1 - kx0) + 48) / p.w
        slack_h = 1 - ((ky1 - ky0) + 88) / p.h   # 88 = label bar + padding
        if max(slack_w, slack_h) > 0.35:
            add(WARN, "container_has_dead_space",
                "'%s' is %dx%d but its contents only span %dx%d. Shrink it to hug its contents -- "
                "a boundary with a large empty region reads as 'something is missing here'."
                % (p.label() or p.id, p.w, p.h, kx1 - kx0, ky1 - ky0), p.id)

    # -- overlap among siblings ---------------------------------------
    by_parent = {}
    for c in verts:
        by_parent.setdefault(c.parent, []).append(c)
    for pid, group in by_parent.items():
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                if a.is_container or b.is_container:
                    continue
                area = _inter_area(a.box, b.box)
                if area <= 0:
                    continue
                smallest = min(a.w * a.h, b.w * b.h) or 1
                largest = max(a.w * a.h, b.w * b.h) or 1
                # A big background band with shapes sitting on top of it is a legitimate
                # draw.io idiom, not a collision: the small shape is fully enclosed and the
                # two differ a lot in area. Only partial overlaps are real problems.
                if area / smallest > 0.95 and largest / smallest > 2.5:
                    continue
                if area / smallest > 0.03:
                    add(ERROR if area / smallest > 0.4 else WARN, "shapes_overlap",
                        "'%s' and '%s' overlap by %d%% -- move one of them."
                        % (a.label() or a.id, b.label() or b.id, round(100 * area / smallest)), a.id)

    # -- edges cutting through unrelated shapes ------------------------
    centres = {c.id: ((c.ax + c.w / 2), (c.ay + c.h / 2)) for c in verts}
    leaf = [c for c in real if not c.is_container]
    # Background bands and zone rectangles are meant to be crossed by edges; only edges
    # that disappear behind a *node-sized* shape are ambiguous about where they end.
    canvas_area = 1.0
    if verts:
        canvas_area = max(1.0, (max(c.ax + c.w for c in verts) - min(c.ax for c in verts)) *
                          (max(c.ay + c.h for c in verts) - min(c.ay for c in verts)))
    node_like = [c for c in leaf if (c.w * c.h) / canvas_area < 0.06
                 and not _composite_child(c)]
    for e in edges:
        if e.source not in centres or e.target not in centres:
            continue
        p, q = centres[e.source], centres[e.target]
        for v in node_like:
            if v.id in (e.source, e.target) or v.id in decor:
                continue
            # skip shapes related to either endpoint: a child of one, or the card the
            # endpoint lives inside. An edge between two boxes in the same card is not
            # "hidden" by the card that contains them both.
            if any(_anc_of(by_id, v, end) for end in (e.source, e.target)):
                continue
            if any(by_id.get(end) is not None and _anc_of(by_id, by_id[end], v.id)
                   for end in (e.source, e.target)):
                continue
            if _seg_hits_box(p, q, v.box, pad=4):
                add(WARN, "edge_crosses_shape",
                    "The edge %s -> %s runs straight through '%s'. Re-order the nodes or route the "
                    "edge around it; a line that vanishes under a shape hides where it ends."
                    % (_name(by_id, e.source), _name(by_id, e.target), v.label() or v.id), e.id)
                break

    # -- straightness of pinned edges ----------------------------------
    # When an edge pins both ends with exitX/exitY and entryX/entryY, the author intended a
    # specific run. If neither axis lines up, draw.io inserts a dog-leg -- which reads as an
    # accident rather than a decision.
    for e in edges:
        s_, t_ = by_id.get(e.source), by_id.get(e.target)
        sd = e.sdict
        if not (s_ and t_) or "exitX" not in sd or "entryX" not in sd:
            continue
        try:
            px = s_.ax + float(sd["exitX"]) * s_.w
            py = s_.ay + float(sd["exitY"]) * s_.h
            qx = t_.ax + float(sd["entryX"]) * t_.w
            qy = t_.ay + float(sd["entryY"]) * t_.h
        except (ValueError, KeyError):
            continue
        dx, dy = abs(px - qx), abs(py - qy)
        if dx > 3 and dy > 3:
            add(WARN, "edge_not_straight",
                "Edge '%s' pins both ends but they do not line up: %dpx across and %dpx down, "
                "so draw.io will bend it. Move a shape or change the exit/entry fraction until "
                "one axis is zero." % (e.label() or e.id, round(dx), round(dy)), e.id)

    # -- edge crossings (quality metric) -------------------------------
    # Use the author's pinned exit/entry points where they exist. Centre-to-centre is a
    # fiction once anchors are set, and it invents crossings that are not in the drawing.
    def _seg(e):
        s_, t_ = by_id.get(e.source), by_id.get(e.target)
        sd = e.sdict
        if s_ and t_ and "exitX" in sd and "entryX" in sd:
            try:
                return ((s_.ax + float(sd["exitX"]) * s_.w, s_.ay + float(sd["exitY"]) * s_.h),
                        (t_.ax + float(sd["entryX"]) * t_.w, t_.ay + float(sd["entryY"]) * t_.h))
            except (TypeError, ValueError):
                pass
        if e.source in centres and e.target in centres:
            return (centres[e.source], centres[e.target])
        return None

    segs = [g for g in (_seg(e) for e in edges) if g]
    crossings = 0
    for i in range(len(segs)):
        for j in range(i + 1, len(segs)):
            if _segments_cross(segs[i], segs[j]):
                crossings += 1
    if crossings:
        add(INFO if crossings <= 2 else WARN, "edge_crossings",
            "%d edge crossing(s). Crossings are the layout flaw that most reliably slows a reader "
            "down; try reordering nodes before accepting them." % crossings)

    # -- labelling -----------------------------------------------------
    for c in real:
        if not c.label():
            add(WARN, "unlabeled_shape",
                "A shape (%s) carries no label. Every icon needs its service name and its role here; "
                "icon sets are not universally memorised." % (c.id,), c.id)
    unlabeled_edges = [e for e in edges if not e.label()]
    if edges and len(unlabeled_edges) == len(edges):
        add(WARN, "no_edge_labels",
            "None of the %d connections is labelled. At minimum label the protocol or the payload on "
            "the flows that carry the story." % len(edges))

    # -- is there room for the arrow to be seen? -----------------------
    for e in edges:
        s_, t_ = by_id.get(e.source), by_id.get(e.target)
        if not (s_ and t_) or not (s_.vertex and t_.vertex):
            continue
        gx = max(0.0, s_.ax - (t_.ax + t_.w), t_.ax - (s_.ax + s_.w))
        gy = max(0.0, s_.ay - (t_.ay + t_.h), t_.ay - (s_.ay + s_.h))
        gap = (gx * gx + gy * gy) ** 0.5
        if 0 < gap < 20:
            add(WARN, "edge_has_no_room",
                "Only %dpx between '%s' and '%s' for the connector between them. An arrowhead is "
                "about 10px on its own, so the line reads as a join rather than a direction -- "
                "open the gap to 25px or more, or drop the arrow and let adjacency say it."
                % (round(gap), _name(by_id, e.source), _name(by_id, e.target)), e.id)

    # -- does the icon agree with the text? ----------------------------
    for c in real:
        lab = c.label().lower()
        if not lab:
            continue
        # A "[Container: X]" line names the technology outright, so that is what the icon
        # has to agree with. "[Software System]" and "[Person]" name none, so fall back to
        # the whole card.
        m = re.search(r"\[([^\]]*:[^\]]*)\]", lab)
        scope = m.group(1) if m else lab
        for kid in c.children:
            if not kid.vertex or kid.label():
                continue
            prod = _icon_product(kid.style)
            if not prod:
                continue
            for key, terms in PRODUCT_ALIASES.items():
                if key not in prod:
                    continue
                if not any(_mentions(scope, t) for t in terms):
                    add(WARN, "icon_contradicts_label",
                        "'%s' wears a %s icon, but its type line names none of: %s. An icon is a claim "
                        "about which technology does the work -- make the card's [type] line and "
                        "the icon agree, or the reader believes the icon."
                        % (c.label(), prod.replace("_", " "), ", ".join(terms[:4])), c.id)
                break

    # -- arrow direction ----------------------------------------------
    for e in edges:
        s = e.sdict
        arrowheads = {"classic", "classicThin", "block", "blockThin", "open", "openThin",
                      "openAsync", "async", "halfCircle", "ERone", "baseDash"}
        # BPMN message flows legitimately carry a hollow circle at the source end
        # (startArrow=oval), which is a marker, not a second arrowhead.
        if s.get("startArrow") in arrowheads and s.get("endArrow") not in (None, "none"):
            add(WARN, "bidirectional_arrow",
                "Edge '%s' has arrowheads at both ends. Draw the two flows separately or label "
                "request/response -- a double-headed arrow hides which side initiates."
                % (e.label() or e.id), e.id)

    # -- typography and canvas ----------------------------------------
    for c in cells:
        fs = c.sdict.get("fontSize")
        if fs:
            try:
                if float(fs) < 10:
                    add(WARN, "tiny_text",
                        "fontSize=%s on '%s' is unreadable once the diagram is scaled into a slide; "
                        "11-12pt is the practical floor." % (fs, c.label() or c.id), c.id)
            except ValueError:
                pass

    if verts:
        minx = min(c.ax for c in verts)
        miny = min(c.ay for c in verts)
        maxx = max(c.ax + c.w for c in verts)
        maxy = max(c.ay + c.h for c in verts)
        w, h = maxx - minx, maxy - miny
        ratio = (w / h) if h else 0
        add(INFO, "canvas",
            "Bounding box %dx%d (aspect %.2f). A 16:9 slide is 1.78; 4:3 is 1.33." % (w, h, ratio))
        if ratio > 3.2:
            add(WARN, "too_wide",
                "Aspect %.2f is far wider than any slide. Wrap the flow onto a second row or split "
                "the diagram; shrinking it to fit will make the labels unreadable." % ratio)
        elif 0 < ratio < 0.45:
            add(WARN, "too_tall",
                "Aspect %.2f is much taller than a slide. Consider a left-to-right layout." % ratio)

    # -- icon coverage -------------------------------------------------
    top_ic = [c for c in leaf if not _composite_child(c)]
    iconish = [c for c in top_ic if _has_icon(c)]
    if top_ic:
        pct = 100 * len(iconish) / len(top_ic)
        add(INFO if pct >= 60 else WARN, "icon_coverage",
            "%d of %d top-level shapes (%d%%) use a real stencil or icon. Plain rectangles where a "
            "vendor or capability icon exists make the diagram look generic."
            % (len(iconish), len(top_ic), round(pct)))

    top = [c for c in leaf if not _composite_child(c)]
    counts = {"shapes": len(verts), "leaf_shapes": len(top), "edges": len(edges),
              "containers": len([c for c in verts if c.is_container]), "crossings": crossings}
    wide = bool(verts) and (max(c.ax + c.w for c in verts) - min(c.ax for c in verts)) > 1750
    budget = 30 if wide else 22
    if len(top) > budget:
        add(WARN, "too_many_shapes",
            "%d top-level shapes. A slide caps out around 20 and a design-document diagram around "
            "30; past that the reader stops seeing a structure and starts reading a list. Split "
            "into a context view plus a detail view." % len(top))
    return findings, counts


def _anc_of(by_id, node, ancestor_id):
    cur, hop = by_id.get(node.parent), 0
    while cur is not None and hop < 25:
        if cur.id == ancestor_id:
            return True
        cur, hop = by_id.get(cur.parent), hop + 1
    return False


def _name(by_id, cid):
    c = by_id.get(cid)
    return (c.label() or cid) if c else str(cid)


def _segments_cross(s1, s2):
    (p1, p2), (p3, p4) = s1, s2
    if len({p1, p2, p3, p4}) < 4:
        return False

    def orient(a, b, c):
        v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return (v > 1e-9) - (v < -1e-9)

    return (orient(p1, p2, p3) != orient(p1, p2, p4) and
            orient(p3, p4, p1) != orient(p3, p4, p2))


# --------------------------------------------------------------------------
# Wireframe preview
# --------------------------------------------------------------------------

def render(cells, findings, out_png, max_w=1700):
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return None

    verts = [c for c in cells if c.vertex and c.w > 0 and c.h > 0]
    edges = [c for c in cells if c.edge]
    if not verts:
        return None

    bad = {f["cell"] for f in findings if f["severity"] == ERROR and f["cell"]}
    warn = {f["cell"] for f in findings if f["severity"] == WARN and f["cell"]}

    minx = min(c.ax for c in verts) - 40
    miny = min(c.ay for c in verts) - 40
    maxx = max(c.ax + c.w for c in verts) + 40
    maxy = max(c.ay + c.h for c in verts) + 40
    scale = min(max_w / max(maxx - minx, 1), 2.0)
    W = int((maxx - minx) * scale)
    H = int((maxy - miny) * scale)
    W, H = max(W, 200), max(H, 150)

    img = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(img)

    def font(size):
        for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                  "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"):
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size)
                except OSError:
                    pass
        return ImageFont.load_default()

    def T(x, y):
        return ((x - minx) * scale, (y - miny) * scale)

    def fill_of(c):
        f = c.sdict.get("fillColor")
        if f and re.fullmatch(r"#[0-9A-Fa-f]{6}", f):
            return f
        if "resIcon=" in c.style or "image=" in c.style:
            return "#dbe7f5"
        return "#f2f2f2"

    # containers first so leaves paint on top
    for c in sorted(verts, key=lambda v: (not v.is_container, -(v.w * v.h))):
        x0, y0 = T(c.ax, c.ay)
        x1, y1 = T(c.ax + c.w, c.ay + c.h)
        outline = "#cc0000" if c.id in bad else ("#e08900" if c.id in warn else "#5a5a5a")
        width = 3 if c.id in bad else (2 if c.id in warn else 1)
        if c.is_container:
            # paint a container's own tint when it has one -- a layer palette is invisible
            # in the preview otherwise, and you cannot review a colour you cannot see
            f = c.sdict.get("fillColor")
            band = f if (f and re.fullmatch(r"#[0-9A-Fa-f]{6}", f)) else None
            d.rectangle([x0, y0, x1, y1], fill=band, outline=outline, width=width)
        else:
            d.rectangle([x0, y0, x1, y1], fill=fill_of(c), outline=outline, width=width)
        lab = c.label()
        if lab:
            st = c.sdict
            # honour the cell's own fontSize -- assuming 11pt everywhere made the preview
            # wrap 10pt text a line early and mis-size boxes that were actually fine
            fs = _numf(st.get("fontSize"), 11) or 11
            fnt = font(max(7, int(fs * min(scale, 1.4))))
            cw = max(3.0, fnt.size * 0.55)
            pad = _numf(st.get("spacingLeft"), 0) * scale
            below = st.get("verticalLabelPosition") == "bottom"
            box_w = (x1 - x0) - pad
            lines = _wrap(lab, max(6, int(box_w // cw)))[:3]
            th = len(lines) * (fnt.size + 2)
            if below:
                tx, ty = x0, y1 + 2
                box_w = x1 - x0
                lines = _wrap(lab, max(6, int(box_w // cw)))[:2]
            elif c.is_container or st.get("verticalAlign") == "top":
                # spacingTop is how a composite card drops its title below the icon;
                # ignoring it makes the wireframe show a collision that isn't there.
                tx = x0 + 4 + pad
                ty = y0 + 3 + _numf(st.get("spacingTop"), 0) * scale
            elif st.get("verticalAlign") == "bottom":
                # a card whose icon sits on top pushes its text to the floor; drawing it
                # centred makes the preview show a collision with the icon that isn't there
                tx = x0 + 4 + pad
                ty = y1 - th - 3 - _numf(st.get("spacingBottom"), 0) * scale
            elif st.get("verticalAlign") == "middle" or st.get("verticalAlign") is None:
                tx, ty = x0 + 4 + pad, (y0 + y1) / 2 - th / 2
            else:
                tx, ty = x0 + 4 + pad, y0 + 3
            for i, line in enumerate(lines):
                w = d.textlength(line, font=fnt) if hasattr(d, "textlength") else len(line) * 6
                px = tx + (box_w - w) / 2 if st.get("align") == "center" and not below else tx
                if below:
                    px = x0 + (box_w - w) / 2
                d.text((px, ty + i * (fnt.size + 2)), line, fill="#111111", font=fnt)

    by_id = {c.id: c for c in cells if c.id}
    for e in edges:
        s, t = by_id.get(e.source), by_id.get(e.target)
        if not s or not t or not s.vertex or not t.vertex:
            continue
        # draw from the pinned exit/entry points when the author set them, so the preview
        # shows the run that draw.io will actually route rather than a centre-to-centre line
        sd = e.sdict
        if "exitX" in sd and "entryX" in sd:
            try:
                p = T(s.ax + float(sd["exitX"]) * s.w, s.ay + float(sd["exitY"]) * s.h)
                q = T(t.ax + float(sd["entryX"]) * t.w, t.ay + float(sd["entryY"]) * t.h)
            except (ValueError, KeyError):
                p = T(s.ax + s.w / 2, s.ay + s.h / 2)
                q = T(t.ax + t.w / 2, t.ay + t.h / 2)
        else:
            p = T(s.ax + s.w / 2, s.ay + s.h / 2)
            q = T(t.ax + t.w / 2, t.ay + t.h / 2)
        col = "#cc0000" if e.id in bad else ("#e08900" if e.id in warn else "#2b6cb0")
        d.line([p, q], fill=col, width=2)
        _arrow(d, p, q, col)
        lab = e.label()
        if lab:
            # honour the label offset, otherwise the preview shows labels sitting on the
            # lines when the real render has them beside -- and vice versa
            lxm, lym = (p[0] + q[0]) / 2 + e.lx * scale, (p[1] + q[1]) / 2 + e.ly * scale
            d.text((lxm - 40, lym - 6), lab[:44], fill="#2b6cb0", font=font(10))

    img.save(out_png)
    return out_png


def _arrow(d, p, q, col, size=10):
    import math
    ang = math.atan2(q[1] - p[1], q[0] - p[0])
    spread = math.radians(24)
    a = (q[0] - size * math.cos(ang - spread), q[1] - size * math.sin(ang - spread))
    b = (q[0] - size * math.cos(ang + spread), q[1] - size * math.sin(ang + spread))
    d.polygon([q, a, b], fill=col)


def _numf(v, default=0.0):
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def _wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= width:
            cur = (cur + " " + w).strip()
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [text[:width]]


# --------------------------------------------------------------------------

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--png", default=None, help="where to write the wireframe preview")
    ap.add_argument("--no-preview", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    cells = load_cells(args.file)
    by_id = resolve(cells)
    findings, counts = analyse(cells, by_id)

    png = None
    if not args.no_preview:
        png = args.png or os.path.splitext(args.file)[0] + ".preview.png"
        png = render(cells, findings, png)

    if args.json:
        print(json.dumps({"counts": counts, "preview": png, "findings": findings}, indent=2))
    else:
        order = {ERROR: 0, WARN: 1, INFO: 2}
        print("%s: %d shapes (%d containers), %d edges"
              % (os.path.basename(args.file), counts["shapes"], counts["containers"], counts["edges"]))
        print("-" * 72)
        for f in sorted(findings, key=lambda x: order[x["severity"]]):
            print("[%-5s] %-22s %s" % (f["severity"], f["code"], f["message"]))
        n_err = sum(1 for f in findings if f["severity"] == ERROR)
        n_warn = sum(1 for f in findings if f["severity"] == WARN)
        print("-" * 72)
        print("%d error(s), %d warning(s)" % (n_err, n_warn))
        if png:
            print("Wireframe preview written to %s -- open it and look at it before you ship." % png)

    return 1 if any(f["severity"] == ERROR for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
