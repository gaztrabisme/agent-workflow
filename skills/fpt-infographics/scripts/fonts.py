# -*- coding: utf-8 -*-
"""BR Omega for the web and for print, with TrueType-flavoured outlines.

WHY THIS EXISTS. BR Omega ships as .otf - PostScript (CFF) outlines. Chromium prints
PDFs through Skia, and Skia cannot serialise a CFF web font as a real embedded font, so
it falls back to Type3: one PDF content stream per glyph. The glyphs are still vector
paths, so the file is not rasterised - but Type3 fonts carry no hinting, and most PDF
viewers cache one rasterisation of a Type3 glyph and scale that bitmap instead of
re-rendering at each zoom level. That is what "pixelated when I zoom in" is, and it is
invisible to every check that only counts selectable characters.

Converting the cubic CFF outlines to quadratic glyf outlines makes the font TrueType-
flavoured, and Skia then embeds it as Type0 / CIDFontType2 with a real FontFile2.

Two modes:

    python scripts/fonts.py build  [--src DIR]   .otf -> assets/fonts/*.woff2
    python scripts/fonts.py css                  assets/fonts/*.woff2 -> @font-face on stdout

`build` is run once, when the licensed .otf files are available. The woff2 files it
writes are what the skill keeps: small, diffable, and already converted.

`css` inlines those woff2 files as base64 at build time, so a rendered sheet is a single
self-contained HTML file that still shows the right typeface after it is emailed. Keep
the files on disk; inline them into the output. Never the other way round.

Requires: fontTools, brotli.
"""
import argparse
import base64
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
FONTDIR = os.path.join(SKILL, "assets", "fonts")

MAX_ERR = 1.0  # font units on a 1000-unit em; far below a device pixel at any size here

# Weight coverage is deliberate, not exhaustive: the brand's text weights plus one
# italic. Sixteen faces in every output would be 500 KB of base64 for nothing.
WANT = [("BROmega-Regular.otf", "bromega-400.woff2", 400, "normal"),
        ("BROmega-Medium.otf", "bromega-500.woff2", 500, "normal"),
        ("BROmega-SemiBold.otf", "bromega-600.woff2", 600, "normal"),
        ("BROmega-Bold.otf", "bromega-700.woff2", 700, "normal"),
        ("BROmega-Black.otf", "bromega-900.woff2", 900, "normal"),
        ("BROmega-RegularItalic.otf", "bromega-400i.woff2", 400, "italic")]


def otf_to_ttf(font, max_err=MAX_ERR):
    """CFF cubics -> glyf quadratics. Follows fontTools' own otf2ttf recipe."""
    from fontTools.pens.cu2quPen import Cu2QuPen
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    from fontTools.ttLib import newTable

    assert font.sfntVersion == "OTTO" and "CFF " in font, "not a CFF-flavoured OpenType font"
    order = font.getGlyphOrder()
    glyphset = font.getGlyphSet()

    quad = {}
    for name in order:
        pen = TTGlyphPen(glyphset)
        glyphset[name].draw(Cu2QuPen(pen, max_err, reverse_direction=True))
        quad[name] = pen.glyph()

    font["loca"] = newTable("loca")
    glyf = font["glyf"] = newTable("glyf")
    glyf.glyphOrder = order
    glyf.glyphs = quad
    del font["CFF "]

    # maxp must be version 1.0 for TrueType; the TrueType-only fields are recalculated
    # from glyf at compile time.
    maxp = font["maxp"]
    maxp.tableVersion = 0x00010000
    for k, v in (("maxZones", 1), ("maxTwilightPoints", 0), ("maxStorage", 0),
                 ("maxFunctionDefs", 0), ("maxInstructionDefs", 0),
                 ("maxStackElements", 0), ("maxSizeOfInstructions", 0),
                 ("maxComponentElements", 0), ("maxComponentDepth", 0)):
        setattr(maxp, k, v)
    maxp.numGlyphs = len(quad)

    font["post"].formatType = 3.0      # TrueType does not need glyph names
    font["head"].indexToLocFormat = 0  # recomputed by loca.compile
    if "DSIG" in font:
        del font["DSIG"]               # the signature is void once the outlines change
    font.sfntVersion = "\000\001\000\000"
    return font


def cmd_build(src):
    from fontTools.ttLib import TTFont

    os.makedirs(FONTDIR, exist_ok=True)
    missing = [fn for fn, _, _, _ in WANT if not os.path.exists(os.path.join(src, fn))]
    if missing:
        sys.exit("missing .otf source(s) in %s:\n  %s" % (src, "\n  ".join(missing)))

    for fn, out, weight, style in WANT:
        f = TTFont(os.path.join(src, fn))
        before = (f["head"].unitsPerEm, f["OS/2"].sxHeight, f["OS/2"].sCapHeight,
                  f["hmtx"]["H"][0] if "H" in f.getGlyphOrder() else None)
        otf_to_ttf(f)
        f.flavor = "woff2"
        buf = io.BytesIO()
        f.save(buf)
        data = buf.getvalue()

        # The conversion must not move a single metric. The legibility gate measures
        # x-height and cap-height off the rendered font; if those shift, every
        # measurement taken against this font is wrong by the same amount silently.
        chk = TTFont(io.BytesIO(data))
        after = (chk["head"].unitsPerEm, chk["OS/2"].sxHeight, chk["OS/2"].sCapHeight,
                 chk["hmtx"]["H"][0] if "H" in chk.getGlyphOrder() else None)
        assert before == after, "%s: metrics moved %s -> %s" % (fn, before, after)
        assert "glyf" in chk and "CFF " not in chk, "%s: still CFF" % fn

        with open(os.path.join(FONTDIR, out), "wb") as fh:
            fh.write(data)
        print("  %-28s -> %-20s %4d KB   upem=%d x=%d cap=%d"
              % (fn, out, len(data) // 1024, after[0], after[1], after[2]))
    print("\nwrote %d faces to %s" % (len(WANT), FONTDIR))


def cmd_css():
    out = []
    for _, fn, weight, style in WANT:
        p = os.path.join(FONTDIR, fn)
        if not os.path.exists(p):
            sys.exit("missing %s - run: python scripts/fonts.py build --src <otf dir>" % p)
        b64 = base64.b64encode(open(p, "rb").read()).decode()
        out.append("@font-face{font-family:'BR Omega';font-style:%s;font-weight:%d;"
                   "font-display:block;src:url(data:font/woff2;base64,%s) format('woff2');}"
                   % (style, weight, b64))
    sys.stdout.write("\n".join(out))


def font_css():
    """Importable form of `css`, for a build script that assembles the HTML."""
    buf = io.StringIO()
    stdout, sys.stdout = sys.stdout, buf
    try:
        cmd_css()
    finally:
        sys.stdout = stdout
    return buf.getvalue()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("mode", choices=["build", "css"])
    ap.add_argument("--src", default=os.environ.get("BROMEGA_OTF", ""),
                    help="directory holding the licensed BR Omega .otf files")
    a = ap.parse_args()
    if a.mode == "build":
        if not a.src:
            sys.exit("build needs --src <dir of BR Omega .otf files> (or $BROMEGA_OTF)")
        cmd_build(a.src)
    else:
        cmd_css()
