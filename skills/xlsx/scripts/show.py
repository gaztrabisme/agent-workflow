#!/usr/bin/env python
"""show.py — print what is actually inside a file, so you stop writing a throwaway
script to find out.

    python show.py FILE [SHEET_OR_SLIDE ...] [options]

Handles .xlsx/.xlsm, .pptx, .docx, .drawio(+.png/.svg with embedded XML), .csv,
.json, .yaml/.yml, .xml, .md/.txt, and the raw zip membership of any OOXML file.

Why it exists: an .xlsx cell can hold a formula, a cached value, both or neither, and
the three are three different loads. Printing a sheet without saying which one you
read is how a column of live formulas gets summed as zero. So the xlsx dump reads the
file TWICE — once for formulas, once for cached values — and prints both plus a
per-sheet reconciliation of how many cached values are missing.

Dependencies: stdlib always; openpyxl for .xlsx; python-pptx for .pptx (falls back to
a zip+regex reader when it is absent). Nothing project-specific. Copy it anywhere.

OPTIONS
  --values-only          xlsx: print cached values only (default prints both)
  --formulas-only        xlsx: print formula strings only
  --rows A:B             row range, 1-based inclusive (default 1:60)
  --cols N               stop after N columns (default 12)
  --width N              truncate each cell to N chars (default 60, 0 = no limit)
  --all                  no row/col/width limits
  --notes                pptx: include speaker notes
  --members              list the zip members with sizes; do not dump content
  --part MEMBER          print one raw zip member verbatim (an XML part, a rel file)
  --grep PATTERN         regex over the RAW XML of every part, entities unescaped.
                         Use this, not a cell walk, to answer "does this string
                         appear anywhere in the file" — text lives in ~20 places.
  --meta                 who wrote the file (docProps/app.xml) + part inventory summary
"""
import argparse
import csv
import html
import io
import json
import os
import re
import sys
import zipfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
else:                                                   # py<3.7 / odd wrappers
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")

OOXML = (".xlsx", ".xlsm", ".xltx", ".pptx", ".potx", ".docx", ".dotx")


# ── helpers ─────────────────────────────────────────────────────────────────────
def clip(v, width):
    if v is None:
        return ""
    s = str(v).replace("\n", "\\n").replace("\r", "")
    if width and len(s) > width:
        s = s[:width - 1] + "\u2026"
    return s


def parse_rows(spec):
    if not spec:
        return 1, 60
    a, _, b = spec.partition(":")
    return int(a or 1), int(b or 10 ** 9)


def head(title, ch="="):
    print("\n" + ch * 78)
    print(title)
    print(ch * 78)


# ── zip-level (works on every OOXML file, and on .zip) ──────────────────────────
def zip_members(path):
    with zipfile.ZipFile(path) as z:
        for i in z.infolist():
            print("%9d  %9d  %s" % (i.file_size, i.compress_size, i.filename))


def zip_part(path, member):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        hits = [n for n in names if n == member] or sorted(
            (n for n in names if member in n), key=len)
        if not hits:
            sys.exit("no member matching %r. Try --members." % member)
        for n in hits[:5]:
            head(n)
            raw = z.read(n)
            try:
                print(raw.decode("utf-8"))
            except UnicodeDecodeError:
                print("<%d binary bytes>" % len(raw))


TAG = re.compile(r"<[^>]+>")


def unescape2(s):
    """drawio stores an HTML label escaped inside an XML attribute, so entities
    arrive DOUBLE-escaped (`&amp;nbsp;`). One unescape leaves `&nbsp;` on screen."""
    out = html.unescape(s)
    return html.unescape(out) if re.search(r"&[a-zA-Z#][\w#]{1,8};", out) else out


def zip_grep(path, pattern):
    """Search the raw XML of every part. Entities are unescaped first.

    openpyxl writes non-ASCII as NUMERIC character references (`&#7842;`) while
    LibreOffice writes literal UTF-8 — so a regex for a non-ASCII string over raw
    bytes silently finds nothing in an openpyxl-written file. html.unescape closes
    that, and a hand-rolled list of the five named entities does not."""
    rx = re.compile(pattern, re.I)
    n = 0
    with zipfile.ZipFile(path) as z:
        for m in z.namelist():
            if not m.lower().endswith((".xml", ".rels")):
                continue
            text = html.unescape(TAG.sub(" ", z.read(m).decode("utf-8", "replace")))
            for chunk in re.split(r"\s{2,}|\n", text):
                chunk = chunk.strip()
                if chunk and rx.search(chunk):
                    n += 1
                    print("%-34s %s" % (m, clip(chunk, 200)))
    print("\n%d hit(s) for %r across the raw XML." % (n, pattern))


def zip_meta(path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        for p in ("docProps/app.xml", "docProps/core.xml", "docProps/custom.xml"):
            if p in names:
                x = z.read(p).decode("utf-8", "replace")
                head(p, "-")
                for m in re.finditer(r"<([\w:]+)>([^<]{1,200})</\1>", x):
                    print("  %-28s %s" % (m.group(1), m.group(2)))
        head("part inventory", "-")
        kinds = {}
        for n in names:
            kinds.setdefault(n.rsplit("/", 1)[0] if "/" in n else "(root)",
                             []).append(n)
        for k in sorted(kinds):
            print("  %-38s %d" % (k, len(kinds[k])))
        ss = "xl/sharedStrings.xml" in names
        print("\n  xl/calcChain.xml     %s" % ("present" if
              "xl/calcChain.xml" in names else "absent"))
        print("  xl/sharedStrings.xml %s" % ("present" if ss else "absent"))
        if any(n.startswith("xl/") for n in names) and not ss:
            print("    -> no shared strings: text is INLINE in the worksheet XML. "
                  "openpyxl writes it this way; LibreOffice rewrites to "
                  "sharedStrings on recalc. Any tool that patches "
                  "sharedStrings.xml will not find this file's text.")


# ── xlsx ────────────────────────────────────────────────────────────────────────
def show_xlsx(path, want, a):
    import openpyxl
    wf = openpyxl.load_workbook(path, data_only=False)   # formulas as strings
    wv = openpyxl.load_workbook(path, data_only=True)    # LibreOffice's cached values
    print("sheets: %s" % " | ".join(wf.sheetnames))
    r0, r1 = parse_rows(a.rows)
    for name in (want or wf.sheetnames):
        if name not in wf.sheetnames:
            print("\n!! no sheet %r" % name)
            continue
        sf, sv = wf[name], wv[name]
        head("%s   dims=%s  %d rows x %d cols"
             % (name, sf.dimensions, sf.max_row, sf.max_column))
        nf = ncached = 0
        for r in range(1, sf.max_row + 1):
            for c in range(1, sf.max_column + 1):
                f = sf.cell(r, c).value
                if isinstance(f, str) and f.startswith("="):
                    nf += 1
                    if sv.cell(r, c).value is not None:
                        ncached += 1
        if nf:
            print("formulas: %d   with a cached value: %d   MISSING: %d%s"
                  % (nf, ncached, nf - ncached,
                     "   <- recalculate before reading this sheet"
                     if nf - ncached else ""))
        for r in range(max(1, r0), min(sf.max_row, r1) + 1):
            cells = []
            for c in range(1, min(sf.max_column, a.cols) + 1):
                f, v = sf.cell(r, c).value, sv.cell(r, c).value
                if f is None and v is None:
                    cells.append("")
                    continue
                isform = isinstance(f, str) and f.startswith("=")
                if a.values_only:
                    cells.append(clip(v, a.width))
                elif a.formulas_only:
                    cells.append(clip(f, a.width))
                elif isform:
                    cells.append("%s -> %s" % (clip(f, a.width),
                                               "<NO CACHED VALUE>" if v is None
                                               else clip(v, a.width)))
                else:
                    cells.append(clip(f, a.width))
            if any(cells):
                print("%4d| %s" % (r, " | ".join(cells).rstrip(" |")))


# ── pptx ────────────────────────────────────────────────────────────────────────
def show_pptx(path, want, a):
    idx = {int(w) for w in want if str(w).isdigit()} or None
    try:
        from pptx import Presentation
    except ImportError:
        return _pptx_raw(path, idx, a)
    prs = Presentation(path)
    print("%d slides, %.2f x %.2f in"
          % (len(prs.slides._sldIdLst), prs.slide_width / 914400,
             prs.slide_height / 914400))
    for i, sl in enumerate(prs.slides, 1):
        if idx and i not in idx:
            continue
        head("slide %d   layout=%s" % (i, sl.slide_layout.name))
        for sh in sl.shapes:
            kind = str(sh.shape_type).split()[0] if sh.shape_type else "?"
            geo = "%.2f,%.2f %.2fx%.2f in" % (
                (sh.left or 0) / 914400, (sh.top or 0) / 914400,
                (sh.width or 0) / 914400, (sh.height or 0) / 914400)
            print("  [%s] %-22s %s" % (kind, clip(sh.name, 22), geo))
            if sh.has_text_frame:
                for p in sh.text_frame.paragraphs:
                    t = "".join(r.text for r in p.runs)
                    if t.strip():
                        sz = {r.font.size.pt for r in p.runs if r.font.size}
                        print("      %s%s" % (clip(t, a.width),
                                              "   [%spt]" % "/".join(
                                                  "%g" % s for s in sorted(sz))
                                              if sz else ""))
            if sh.has_table:
                for row in sh.table.rows:
                    print("      | " + " | ".join(
                        clip(c.text, 28) for c in row.cells))
        if a.notes and sl.has_notes_slide:
            nt = sl.notes_slide.notes_text_frame.text
            if nt.strip():
                print("  NOTES: %s" % clip(nt, a.width * 4 if a.width else 0))


def _pptx_raw(path, idx, a):
    """No python-pptx: a .pptx is a zip and a paragraph is <a:p>. Group runs by
    paragraph before joining or a heading fuses into its body."""
    print("(python-pptx absent — raw zip reader)")
    with zipfile.ZipFile(path) as z:
        slides = sorted((n for n in z.namelist()
                         if re.match(r"ppt/slides/slide\d+\.xml$", n)),
                        key=lambda n: int(re.search(r"(\d+)",
                                                    n.rsplit("/", 1)[1]).group(1)))
        for i, n in enumerate(slides, 1):
            if idx and i not in idx:
                continue
            head("slide %d   (%s)" % (i, n))
            xml = z.read(n).decode("utf-8", "ignore")
            for p in re.findall(r"<a:p\b.*?</a:p>", xml, re.S):
                line = "".join(html.unescape(t) for t in
                               re.findall(r"<a:t>(.*?)</a:t>", p, re.S))
                if line.strip():
                    print("   " + clip(line, a.width))


# ── drawio / xml / text ─────────────────────────────────────────────────────────
def show_drawio(path, a):
    raw = open(path, "rb").read()
    if raw[:4] == b"\x89PNG" or path.lower().endswith((".png", ".svg")):
        m = re.search(rb'content="([^"]*)"', raw) or re.search(rb'mxfile[^>]*>', raw)
        print("(embedded-XML export; %d bytes)" % len(raw))
        if m:
            print(html.unescape(m.group(0).decode("utf-8", "replace"))[:4000])
        return
    x = raw.decode("utf-8", "replace")
    if "<mxfile" in x and "&lt;mxGraphModel" in x:
        x = html.unescape(x)
    print(x if a.all else x[:20000])
    cells = re.findall(r'<mxCell[^>]*value="([^"]+)"', x)
    if cells:
        head("cell labels (%d)" % len(cells), "-")
        for c in cells:
            # unescape FIRST, then strip tags — a drawio label is HTML stored
            # escaped inside an XML attribute, so stripping before unescaping
            # strips nothing and you get `<b><font ...>` in the output.
            print("  " + re.sub(r"\s+", " ",
                                TAG.sub(" ", unescape2(c))).strip()[: a.width or None])


def show_text(path, a):
    if path.lower().endswith(".json"):
        print(json.dumps(json.load(open(path, encoding="utf-8")),
                         indent=2, ensure_ascii=False)[: None if a.all else 20000])
        return
    if path.lower().endswith(".csv"):
        r0, r1 = parse_rows(a.rows)
        with open(path, newline="", encoding="utf-8-sig", errors="replace") as fh:
            for i, row in enumerate(csv.reader(fh), 1):
                if i < r0:
                    continue
                if i > r1:
                    print("... (truncated at row %d)" % r1)
                    break
                print("%4d| %s" % (i, " | ".join(
                    clip(v, a.width) for v in row[:a.cols])))
        return
    with open(path, encoding="utf-8", errors="replace") as fh:
        s = fh.read()
    print(s if a.all else s[:20000])


# ── main ────────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("path")
    ap.add_argument("select", nargs="*", help="sheet names, or slide numbers")
    ap.add_argument("--rows", default=None, metavar="A:B")
    ap.add_argument("--cols", type=int, default=12)
    ap.add_argument("--width", type=int, default=60)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--values-only", action="store_true")
    ap.add_argument("--formulas-only", action="store_true")
    ap.add_argument("--notes", action="store_true")
    ap.add_argument("--members", action="store_true")
    ap.add_argument("--part", default=None, metavar="MEMBER")
    ap.add_argument("--grep", default=None, metavar="REGEX")
    ap.add_argument("--meta", action="store_true")
    a = ap.parse_args()

    p = os.path.expanduser(a.path)
    if not os.path.exists(p):
        sys.exit("no such file: %s" % p)
    if a.all:
        a.rows, a.cols, a.width = "1:1000000", 10 ** 6, 0

    ext = os.path.splitext(p)[1].lower()
    iszip = ext in OOXML or ext == ".zip" or zipfile.is_zipfile(p)

    if a.members:
        return zip_members(p)
    if a.part:
        return zip_part(p, a.part)
    if a.grep:
        if not iszip:
            rx = re.compile(a.grep, re.I)
            for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
                if rx.search(line):
                    print("%6d: %s" % (i, clip(line.rstrip(), 200)))
            return
        return zip_grep(p, a.grep)
    if a.meta:
        return zip_meta(p) if iszip else print(os.stat(p))

    if ext in (".xlsx", ".xlsm", ".xltx"):
        return show_xlsx(p, a.select, a)
    if ext in (".pptx", ".potx"):
        return show_pptx(p, a.select, a)
    if ext == ".drawio" or p.lower().endswith((".drawio.png", ".drawio.svg")):
        return show_drawio(p, a)
    if iszip:
        print("(zip-format file, no dedicated reader — members follow)")
        return zip_members(p)
    return show_text(p, a)


if __name__ == "__main__":
    main()
