#!/usr/bin/env node
// Preflight layout checker — run BEFORE rendering the PNG.
//
//   node scripts/check.mjs input.html [--preset name] [--width N] [--height N|auto] [--json]
//
// Loads the page in headless Chromium and verifies the layout mechanically:
//
//   ERRORS (must fix before rendering):
//     text-collision   two text elements paint over each other
//     text-clipped     text cut off by an overflow-hidden ancestor
//     text-offcanvas   text extends past the canvas edge
//     text-too-small   computed font size below the readable floor
//     hero-multiple    more than one element marked data-hero
//     canvas-overflow  page content is larger than the canvas
//
//   WARNINGS (fix, or justify in one line at review):
//     hero-missing     no element marked data-hero (emphasis checks skipped)
//     hero-weak        the data-hero element occupies <10% of the canvas
//     text-small       font size readable but tight (below comfort floor)
//     text-near-miss   two text elements almost touching
//
// Deliberate layering (e.g. a giant translucent numeral behind a headline) is
// waived by putting data-overlap-ok on either element. Waivers are counted and
// reported — use them sparingly and only after visually confirming legibility.
//
// Exit code: 1 if any errors, 0 otherwise (warnings never fail the run).

import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const PRESETS = {
  square: { width: 1080, height: 1080 },
  story: { width: 1080, height: 1920 },
  wide: { width: 1920, height: 1080 },
  og: { width: 1200, height: 630 },
  a4: { width: 1240, height: 1754 },
  'a3-landscape': { width: 1754, height: 1240 },
  tall: { width: 1080, height: 'auto' },
};

// Font-size floors in CSS px. Errors below MIN, warnings below COMFORT.
const FONT_MIN = 9;
const FONT_COMFORT = 12;

function parseArgs(argv) {
  const args = {};
  const positional = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--preset') args.preset = argv[++i];
    else if (a === '--width') args.width = Number(argv[++i]);
    else if (a === '--height') { const v = argv[++i]; args.height = v === 'auto' ? 'auto' : Number(v); }
    else if (a === '--json') args.json = true;
    else if (a === '--pdf') args.pdf = argv[++i];
    else if (a === '--min-viz') args.minViz = Number(argv[++i]);
    else if (a === '--min-families') args.minFamilies = Number(argv[++i]);
    else if (a === '--min-drawn') args.minDrawn = Number(argv[++i]);
    else if (a === '--min-hero-ratio') args.minHero = Number(argv[++i]);
    else if (a.startsWith('--')) fail(`Unknown flag: ${a}`);
    else positional.push(a);
  }
  args.input = positional[0];
  return args;
}

function fail(msg) {
  console.error(`check.mjs: ${msg}`);
  console.error('Usage: node scripts/check.mjs input.html --preset NAME | --width N --height N|auto');
  console.error('       [--pdf out.pdf] [--min-viz N] [--min-families N] [--min-drawn F] [--min-hero-ratio F] [--json]');
  console.error('Presets: square story wide og a4 a3-landscape');
  process.exit(2);
}

const args = parseArgs(process.argv.slice(2));
if (!args.input) fail('need an input .html');

let { width, height } = args.preset
  ? PRESETS[args.preset] ?? fail(`unknown preset "${args.preset}" (have: ${Object.keys(PRESETS).join(', ')})`)
  : {};
if (args.width) width = args.width;
if (args.height !== undefined) height = args.height;
if (width === undefined || height === undefined) {
  fail('canvas size is required — pass --preset NAME, or --width N --height N. '
     + 'There is no default: checking a 1754x1240 sheet against an assumed 1080x1080 '
     + 'canvas reports dozens of errors that are artefacts of the assumption.');
}

const MIN_VIZ = args.minViz ?? 5;
const MIN_FAMILIES = args.minFamilies ?? 3;
const MIN_DRAWN = args.minDrawn ?? 0.30;
const MIN_HERO = args.minHero ?? 4;

// The six families are the six questions in references/data-vocabulary.md. A
// data-viz attribute is written "family:name"; the name is free text.
const FAMILIES = ['magnitude', 'category', 'part-to-whole', 'time', 'process', 'relation'];

const browser = await chromium.launch();
let report;
try {
  const page = await browser.newPage({
    viewport: { width, height: height === 'auto' ? 1080 : height },
  });
  await page.goto(pathToFileURL(resolve(args.input)).href, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150); // settle layout after font swap
  // Animated files are checked at their END state — mid-build opacity/offsets
  // would hide text from every geometry check below.
  await page.evaluate(() => {
    for (const a of document.getAnimations()) {
      a.pause();
      const t = a.effect?.getComputedTiming();
      if (t && Number.isFinite(t.endTime)) a.currentTime = t.endTime;
    }
  });

  report = await page.evaluate(({ width, height, FONT_MIN, FONT_COMFORT,
                                MIN_VIZ, MIN_FAMILIES, MIN_DRAWN, MIN_HERO, FAMILIES }) => {
    const boundsH = height === 'auto' ? document.documentElement.scrollHeight : height;
    const errors = [];
    const warnings = [];
    let waived = 0;

    const visible = (el) => {
      for (let n = el; n && n !== document.documentElement; n = n.parentElement) {
        const cs = getComputedStyle(n);
        if (cs.display === 'none' || cs.visibility === 'hidden') return false;
        if (parseFloat(cs.opacity) < 0.05) return false;
      }
      return true;
    };

    const describe = (el) => {
      let sel = el.tagName.toLowerCase();
      if (el.id) sel += `#${el.id}`;
      else if (el.classList.length) sel += '.' + [...el.classList].slice(0, 2).join('.');
      const text = (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 28);
      return text ? `<${sel}> “${text}${text.length === 28 ? '…' : ''}”` : `<${sel}>`;
    };
    const at = (r) => `at ${Math.round(r.left)},${Math.round(r.top)} ${Math.round(r.width)}×${Math.round(r.height)}`;

    // ---- collect text leaves with glyph-tight rects -------------------------
    // Range rects hug the actual glyphs, so a full-width <p> box next to a
    // floated figure doesn't false-positive the collision check.
    const byElement = new Map();
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.textContent.trim()) continue;
      const el = node.parentElement;
      if (!el || !visible(el)) continue;
      (byElement.get(el) ?? byElement.set(el, []).get(el)).push(node);
    }

    // Line boxes and char cells include ascent/descent air far beyond the
    // glyph ink, especially on display type. The canvas TextMetrics API
    // measures the actual ink bounds for a string in a given font, so the
    // rects below hug what is really painted.
    const mctx = document.createElement('canvas').getContext('2d');
    const metricsFor = (el, text) => {
      const cs = getComputedStyle(el);
      mctx.font = `${cs.fontStyle} ${cs.fontWeight} ${parseFloat(cs.fontSize)}px ${cs.fontFamily}`;
      const m = mctx.measureText(text);
      return {
        fontAsc: m.fontBoundingBoxAscent ?? 0,
        fontDesc: m.fontBoundingBoxDescent ?? 0,
        inkAsc: m.actualBoundingBoxAscent ?? 0,
        inkDesc: m.actualBoundingBoxDescent ?? 0,
        advance: m.width,
      };
    };
    const bboxOf = (pts) => {
      const xs = pts.map((p) => p.x);
      const ys = pts.map((p) => p.y);
      const left = Math.min(...xs), right = Math.max(...xs);
      const top = Math.min(...ys), bottom = Math.max(...ys);
      return { left, right, top, bottom, width: right - left, height: bottom - top };
    };

    const leaves = [];
    for (const [el, nodes] of byElement) {
      const fontSize = parseFloat(getComputedStyle(el).fontSize);
      let rects = [];

      if (el instanceof SVGElement) {
        // Per-character ink boxes, honoring each char's rotation, so labels
        // on a curved path don't inherit the whole arc's bounding box.
        try {
          const ctm = el.getScreenCTM();
          const n = el.getNumberOfChars();
          const chars = el.textContent;
          if (ctm && n) {
            for (let i = 0; i < n; i++) {
              const ch = chars[i];
              if (!ch || !ch.trim()) continue;
              const ext = el.getExtentOfChar(i);
              const m = metricsFor(el, ch);
              const rot = (el.getRotationOfChar(i) * Math.PI) / 180;
              // Rebuild the ink box in char-local coords (origin: cell
              // center), rotate it, then map through the screen CTM.
              const cx = ext.x + ext.width / 2;
              const cy = ext.y + ext.height / 2;
              const baseOff = (m.fontAsc - m.fontDesc) / 2; // baseline below cell center
              const w2 = m.advance / 2;
              const cos = Math.cos(rot), sin = Math.sin(rot);
              const pts = [
                [-w2, baseOff - m.inkAsc], [w2, baseOff - m.inkAsc],
                [-w2, baseOff + m.inkDesc], [w2, baseOff + m.inkDesc],
              ].map(([x, y]) => {
                const rx = cx + x * cos - y * sin;
                const ry = cy + x * sin + y * cos;
                return { x: ctm.a * rx + ctm.c * ry + ctm.e, y: ctm.b * rx + ctm.d * ry + ctm.f };
              });
              rects.push(bboxOf(pts));
            }
          }
        } catch { /* not an SVGTextContentElement */ }
        if (!rects.length) rects = [el.getBoundingClientRect()];
      } else {
        // Range rects hug the line boxes; shave each down to the measured
        // ink ascent/descent. Which sides carry the metric air depends on
        // the text's orientation (rotated headers, vertical writing modes).
        let angle = 0;
        for (let n = el; n && n !== document.documentElement; n = n.parentElement) {
          const t = getComputedStyle(n).transform;
          if (t && t !== 'none') {
            const m = new DOMMatrix(t);
            angle += Math.atan2(m.b, m.a) * 180 / Math.PI;
          }
        }
        if (getComputedStyle(el).writingMode.startsWith('vertical')) angle += 90;
        const norm = ((Math.round(angle) % 360) + 360) % 360;
        const upright = norm % 180 < 3 || norm % 180 > 177;
        const sideways = Math.abs((norm % 180) - 90) < 3;

        const text = nodes.map((n) => n.textContent).join(' ').trim();
        const m = metricsFor(el, text);
        const airTop = Math.max(0, m.fontAsc - m.inkAsc);
        const airBottom = Math.max(0, m.fontDesc - m.inkDesc);
        let iL = 0, iR = 0, iT = 0, iB = 0;
        if (upright) { iT = airTop; iB = airBottom; }
        else if (sideways) { iL = iR = (airTop + airBottom) / 2; }
        else { iL = iR = iT = iB = (airTop + airBottom) / 2; } // arbitrary rotation: AABB is loose anyway

        for (const node of nodes) {
          const range = document.createRange();
          range.selectNodeContents(node);
          for (const r of range.getClientRects()) {
            const left = r.left + Math.min(iL, r.width / 3);
            const right = r.right - Math.min(iR, r.width / 3);
            const top = r.top + Math.min(iT, r.height / 3);
            const bottom = r.bottom - Math.min(iB, r.height / 3);
            rects.push({ left, right, top, bottom, width: right - left, height: bottom - top });
          }
        }
      }

      rects = rects.filter((r) => r.width > 0.5 && r.height > 0.5);
      if (!rects.length) continue;
      const inkArea = rects.reduce((s, r) => s + r.width * r.height, 0);
      leaves.push({ el, rects, fontSize, inkArea });
    }

    // ---- font-size floors ---------------------------------------------------
    for (const { el, fontSize } of leaves) {
      if (fontSize < FONT_MIN) {
        errors.push(`text-too-small  ${describe(el)} is ${fontSize.toFixed(1)}px (floor ${FONT_MIN}px)`);
      } else if (fontSize < FONT_COMFORT) {
        warnings.push(`text-small      ${describe(el)} is ${fontSize.toFixed(1)}px (comfort floor ${FONT_COMFORT}px)`);
      }
    }

    // ---- text vs canvas edges ----------------------------------------------
    const EDGE = 2;
    for (const { el, rects } of leaves) {
      for (const r of rects) {
        if (r.left < -EDGE || r.top < -EDGE || r.right > width + EDGE || r.bottom > boundsH + EDGE) {
          errors.push(`text-offcanvas  ${describe(el)} ${at(r)} leaves the ${width}×${boundsH} canvas`);
          break;
        }
      }
    }

    // ---- text vs overflow-clipping ancestors --------------------------------
    for (const { el, rects } of leaves) {
      if (el instanceof SVGElement) continue; // svg clipping is usually intentional chart framing
      for (let anc = el; anc && anc !== document.body; anc = anc.parentElement) {
        const cs = getComputedStyle(anc);
        const clips = (v) => v === 'hidden' || v === 'clip' || v === 'scroll' || v === 'auto';
        if (!clips(cs.overflowX) && !clips(cs.overflowY)) continue;
        const box = anc.getBoundingClientRect();
        const cut = rects.some((r) =>
          (clips(cs.overflowX) && (r.left < box.left - EDGE || r.right > box.right + EDGE)) ||
          (clips(cs.overflowY) && (r.top < box.top - EDGE || r.bottom > box.bottom + EDGE)));
        if (cut) {
          errors.push(`text-clipped    ${describe(el)} is cut off by overflow-hidden ${describe(anc)}`);
          break;
        }
      }
    }

    // ---- text-on-text collisions -------------------------------------------
    // Sum the ink-rect intersections between the two elements and compare to
    // the smaller element's total ink area, so a one-char graze between long
    // labels reads as a near-miss while a label buried under another element
    // reads as a collision.
    const COLLIDE_RATIO = 0.12; // error: >12% of the smaller element's ink covered
    const NEAR_RATIO = 0.05;    // warning above this
    const seenPairs = new Set();
    for (let i = 0; i < leaves.length; i++) {
      for (let j = i + 1; j < leaves.length; j++) {
        const a = leaves[i];
        const b = leaves[j];
        if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
        let inter = 0;
        let worstArea = 0;
        let where = null;
        for (const ra of a.rects) {
          for (const rb of b.rects) {
            const w = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left);
            const h = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
            if (w < 4 || h < 4) continue;
            inter += w * h;
            if (w * h > worstArea) {
              worstArea = w * h;
              where = { left: Math.max(ra.left, rb.left), top: Math.max(ra.top, rb.top), width: w, height: h };
            }
          }
        }
        if (!inter) continue;
        const ratio = inter / Math.min(a.inkArea, b.inkArea);
        if (ratio < NEAR_RATIO) continue;
        const key = `${describe(a.el)}|${describe(b.el)}`;
        if (seenPairs.has(key)) continue;
        seenPairs.add(key);
        if (a.el.closest('[data-overlap-ok]') || b.el.closest('[data-overlap-ok]')) {
          waived++;
          continue;
        }
        const line = `${describe(a.el)} and ${describe(b.el)} ${at(where)} (${Math.round(ratio * 100)}% of the smaller one's ink covered)`;
        if (ratio >= COLLIDE_RATIO) errors.push(`text-collision  ${line}`);
        else warnings.push(`text-near-miss  ${line}`);
      }
    }

    // ---- page must fit the canvas ------------------------------------------
    if (height !== 'auto') {
      const sw = document.documentElement.scrollWidth;
      const sh = document.documentElement.scrollHeight;
      if (sw > width + EDGE || sh > boundsH + EDGE) {
        errors.push(`canvas-overflow page is ${sw}×${sh}, canvas is ${width}×${boundsH} — content escapes or scrolls`);
      }
    }

    // ---- hero emphasis ------------------------------------------------------
    const heroes = [...document.querySelectorAll('[data-hero]')];
    if (heroes.length === 0) {
      warnings.push('hero-missing    no element carries data-hero — mark the hero so emphasis can be checked');
    } else if (heroes.length > 1) {
      errors.push(`hero-multiple   ${heroes.length} elements carry data-hero — an infographic has exactly one hero`);
    } else {
      const r = heroes[0].getBoundingClientRect();
      const share = (r.width * r.height) / (width * boundsH);
      if (share < 0.1) {
        warnings.push(`hero-weak       ${describe(heroes[0])} covers ${Math.round(share * 100)}% of the canvas — the hero should dominate at a glance`);
      }
    }

    // ---- is anything actually drawn? ---------------------------------------
    //
    // The failure this catches: a page of pure text blocks that passed a 14-row
    // acceptance suite and was still not an infographic. Every mechanical check it
    // had measured overflow, contrast and collision - none asked whether the page
    // draws its data at all.
    const vizEls = [...document.querySelectorAll('[data-viz]')];
    const vizRaw = vizEls.map((e) => e.getAttribute('data-viz').trim()).filter(Boolean);
    const vizNames = [...new Set(vizRaw)];
    const fams = new Set();
    const badFam = [];
    for (const v of vizNames) {
      const [f, ...rest] = v.split(':');
      if (!rest.length) { badFam.push(`${v} (no family prefix)`); continue; }
      if (!FAMILIES.includes(f)) { badFam.push(`${v} (unknown family "${f}")`); continue; }
      fams.add(f);
    }
    if (vizNames.length < MIN_VIZ) {
      errors.push(`viz-too-few     ${vizNames.length} distinct data-viz representation(s), floor is ${MIN_VIZ} — `
        + `mark each drawn representation with data-viz="family:name", and if there are none, this is not an infographic`);
    }
    if (badFam.length) {
      errors.push(`viz-family      ${badFam.length} data-viz value(s) not in ${FAMILIES.join('|')}: ${badFam.join(', ')}`);
    }
    if (fams.size < MIN_FAMILIES) {
      errors.push(`viz-monotonous  ${fams.size} distinct family/families (${[...fams].join(', ') || 'none'}), floor is ${MIN_FAMILIES} — `
        + `five bar charts is one family, not five representations`);
    }

    // ---- how much of the page is drawn, rather than typeset? ----------------
    // Union of the vertical extents of the SVGs, so overlapping drawings are not
    // double-counted.
    const iv = [];
    for (const sv of document.querySelectorAll('svg')) {
      const r = sv.getBoundingClientRect();
      if (r.height > 0 && r.width > 0) iv.push([r.top, r.bottom]);
    }
    iv.sort((a, b) => a[0] - b[0]);
    let covered = 0, curS = null, curE = null;
    for (const [a, b] of iv) {
      if (curS === null) { curS = a; curE = b; continue; }
      if (a <= curE) { curE = Math.max(curE, b); } else { covered += curE - curS; curS = a; curE = b; }
    }
    if (curS !== null) covered += curE - curS;
    const drawnShare = boundsH ? +(covered / boundsH).toFixed(3) : 0;
    if (drawnShare < MIN_DRAWN) {
      errors.push(`drawn-thin      drawn elements span ${Math.round(drawnShare * 100)}% of page height, floor is ${Math.round(MIN_DRAWN * 100)}%`);
    }

    // ---- hero ratio ---------------------------------------------------------
    // The walk must test for a DIRECT non-empty text node. An earlier version
    // skipped any element with children, so a two-line <h1> containing a <br> was
    // invisible and it reported 30px as the largest type on a page with a 128px
    // headline.
    let maxFs = 0, maxWho = '';
    const fsTally = new Map();
    for (const el of document.querySelectorAll('*')) {
      const own = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
      if (!own) continue;
      const f = parseFloat(getComputedStyle(el).fontSize) || 0;
      if (!f) continue;
      fsTally.set(f, (fsTally.get(f) || 0) + 1);
      if (f > maxFs) { maxFs = f; maxWho = el.textContent.trim().replace(/\s+/g, ' ').slice(0, 30); }
    }
    // body size = the most common size on the page, which needs no selector and so
    // works on any layout.
    let bodyFs = 0, bodyN = -1;
    for (const [f, n] of fsTally) if (n > bodyN || (n === bodyN && f < bodyFs)) { bodyFs = f; bodyN = n; }
    const heroRatio = bodyFs ? +(maxFs / bodyFs).toFixed(2) : 0;
    if (heroRatio && heroRatio < MIN_HERO) {
      errors.push(`hero-flat       largest type ${maxFs}px is ${heroRatio}x the body ${bodyFs}px, floor is ${MIN_HERO}x — nothing anchors the page`);
    }

    // ---- SVG text must not be shrunk by its own viewBox ---------------------
    //
    // A chart drawn in a 322-unit viewBox and shown 216px wide paints every label at
    // 0.671 of its declared size. A CSS-based checker reads the declared 11px and is
    // satisfied; the reader gets 7.38px.
    let svgScaleMin = Infinity, svgScaleWorst = '';
    for (const t of document.querySelectorAll('svg text')) {
      const m = t.getScreenCTM && t.getScreenCTM();
      if (!m) continue;
      const sc = Math.sqrt(Math.abs(m.a * m.d - m.b * m.c)) || m.a || 1;
      if (sc < svgScaleMin) {
        svgScaleMin = sc;
        svgScaleWorst = (t.closest('[data-viz]')?.getAttribute('data-viz') || 'svg')
          + ' :: ' + t.textContent.trim().slice(0, 24);
      }
    }
    if (svgScaleMin !== Infinity && svgScaleMin < 0.999) {
      errors.push(`svg-shrunk      SVG text renders at ${svgScaleMin.toFixed(3)} of declared size (${svgScaleWorst}) — `
        + `set each chart's viewBox width equal to the pixel width it is shown at`);
    }

    return {
      errors, warnings, waived, textElements: leaves.length,
      viz: vizNames.length, families: [...fams], drawnShare, heroRatio,
      heroPx: maxFs, bodyPx: bodyFs, heroText: maxWho,
      svgScaleMin: svgScaleMin === Infinity ? null : +svgScaleMin.toFixed(4), svgScaleWorst,
    };
  }, { width, height, FONT_MIN, FONT_COMFORT, MIN_VIZ, MIN_FAMILIES, MIN_DRAWN, MIN_HERO, FAMILIES });
} finally {
  await browser.close();
}

// ---- the PDF must not carry Type3 fonts ------------------------------------
//
// BR Omega ships as CFF (PostScript) outlines. Skia cannot embed a CFF web font and
// falls back to Type3: unhinted, one content stream per glyph. The glyphs stay vector,
// so a check that counts selectable characters passes - and most viewers still cache
// one rasterisation per glyph and scale that bitmap, which is what "pixelated when I
// zoom in" is. Convert to TrueType outlines first: scripts/fonts.py.
if (args.pdf) {
  const { execFileSync } = await import('node:child_process');
  const py = `
import sys, json
try:
    import pymupdf
except ImportError:
    print(json.dumps({"err": "pymupdf not installed"})); sys.exit(0)
d = pymupdf.open(sys.argv[1])
seen = {}
for p in range(d.page_count):
    for f in d.get_page_fonts(p):
        seen[f[3]] = f[2]
print(json.dumps({"fonts": seen}))
`;
  let out;
  try {
    out = JSON.parse(execFileSync('python', ['-c', py, args.pdf], { encoding: 'utf8' }));
  } catch (e) {
    out = { err: String(e.message || e).split('\n')[0] };
  }
  if (out.err) {
    report.warnings.push(`pdf-unchecked   could not read ${args.pdf}: ${out.err}`);
  } else {
    const t3 = Object.entries(out.fonts).filter(([, ty]) => /type3/i.test(ty));
    report.pdfFonts = out.fonts;
    if (t3.length) {
      report.errors.push(`pdf-type3       ${t3.length} Type3 font(s) in ${args.pdf} `
        + `(${t3.map(([n]) => n || '<unnamed>').join(', ')}) — convert the .otf to TrueType outlines with scripts/fonts.py`);
    }
  }
}

if (args.json) {
  console.log(JSON.stringify(report, null, 2));
} else {
  for (const e of report.errors) console.log(`  ✗ ERROR ${e}`);
  for (const w of report.warnings) console.log(`  ! warn  ${w}`);
  console.log(`  composition  ${report.viz} representation(s) in ${report.families.length} famil(y/ies) [${report.families.join(' ')}]`
    + ` · drawn ${Math.round(report.drawnShare * 100)}% of height · hero ${report.heroPx}px / body ${report.bodyPx}px = ${report.heroRatio}x`
    + (report.svgScaleMin === null ? '' : ` · min SVG scale ${report.svgScaleMin.toFixed(3)}`));
  if (report.pdfFonts) {
    const kinds = {};
    for (const ty of Object.values(report.pdfFonts)) kinds[ty] = (kinds[ty] || 0) + 1;
    console.log(`  pdf fonts    ${JSON.stringify(kinds)}`);
  }
  const waivedNote = report.waived ? `, ${report.waived} overlap(s) waived via data-overlap-ok` : '';
  console.log(`check: ${report.errors.length} error(s), ${report.warnings.length} warning(s) — ${report.textElements} text elements checked${waivedNote}`);
  if (report.errors.length === 0 && report.warnings.length === 0) {
    console.log('check: clean — go render');
  }
}
process.exit(report.errors.length ? 1 : 0);
