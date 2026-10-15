#!/usr/bin/env node
/**
 * legibility.mjs — measure whether the text on a rendered page can actually be read,
 * in visual angle, against published thresholds.
 *
 *   node scripts/legibility.mjs page.html --condition ID
 *   node scripts/legibility.mjs page.html --sheet-mm N --distance-mm N
 *                                         [--width N] [--height N]
 *                                         [--target ARCMIN] [--json]
 *
 * The viewing condition is required and has no default. The same type is comfortable
 * on an A3 poster and unreadable in a phone-sized social post, so the script refuses
 * to produce a verdict until it has been told which one is being made. Run it with no
 * condition to get the list of named ones; --sheet-mm with --distance-mm covers a size
 * that is not on the list.
 *
 * ---------------------------------------------------------------------------
 * THE MODEL
 *
 * Legibility is governed by the angle a glyph subtends at the eye, not by px or pt.
 * A glyph of height h at viewing distance D subtends
 *
 *     alpha = (h / D) radians = (h / D) * 3437.75 arcminutes        (small-angle)
 *
 * A design file has no physical size, so split it into a design term and a viewing term:
 *
 *     alpha = (h_px / W_px)  *  (W_mm / D_mm)  *  3437.75
 *             ^ relative glyph height  ^ viewing ratio k
 *
 * The first factor is a property of the layout. The second is a property of how the
 * artifact is looked at. Everything below reports both, so a size can be judged for a
 * named condition instead of by feel.
 *
 * ---------------------------------------------------------------------------
 * THE THRESHOLDS, AND WHERE THEY COME FROM
 *
 * Vision science uses lowercase x-height, because x-height predicts reading performance
 * far better than point size (point size is not even comparable across typefaces).
 *
 *   Legge, G. E. & Bigelow, C. A. (2011). "Does print size matter for reading?
 *   A review of findings from vision science and typography."
 *   Journal of Vision 11(5):8, 1-22.  doi:10.1167/11.5.8
 *
 *     - acuity limit for reading        x-height  0.08 deg  =  4.8 arcmin
 *     - Critical Print Size (CPS)       x-height  0.2  deg  = 12   arcmin
 *         the smallest print that still supports MAXIMUM reading speed,
 *         for young observers with normal vision under good conditions
 *     - the fluent range                x-height  0.2 - 2.0 deg
 *     - where real typography sits      x-height  0.3 - 0.4 deg = 18-24 arcmin
 *         books, newspapers and screens at habitual reading distance, i.e. roughly
 *         2x CPS - the margin that absorbs ageing, low contrast and poor light
 *
 * Display ergonomics uses uppercase (cap) height, and lands in the same place:
 *
 *   ISO 9241-303:2011, Ergonomics of human-system interaction, Part 303:
 *   Requirements for electronic visual displays
 *   ANSI/HFES 100-2007, Human Factors Engineering of Computer Workstations
 *
 *     - character height   16 arcmin minimum, 20-22 arcmin preferred
 *
 * The two agree: for a typeface with cap/x = 1.5, ISO's 16 arcmin cap height is
 * 10.7 arcmin of x-height, just under Legge's CPS. So this script judges
 * mixed-case text on x-height against Legge, and ALL-CAPS text on cap height
 * against ISO, and reports which rule each element was judged by.
 *
 * Contrast matters too: below roughly 10% Weber contrast, CPS rises steeply
 * (Legge et al. 1987, Vision Research 27:1165). WCAG 2.2 SC 1.4.3 asks for 4.5:1 for
 * text below 24px / 18.66px bold, 3:1 above. Both are reported.
 *
 * ---------------------------------------------------------------------------
 * HOW THE GLYPH HEIGHT IS MEASURED
 *
 * Not from a metrics table and not from font-size. For every distinct rendered font,
 * canvas TextMetrics.actualBoundingBoxAscent is measured on 'x' and on 'H' — the real
 * inked height of the font as the browser actually rasterises it, fallbacks included.
 *
 * SVG <text> is measured through its screen CTM, so a 12px label inside a viewBox that
 * is being shown at 0.59 scale is correctly reported as 7.1px. That scaling is invisible
 * to every CSS-based checker and is the most common way small type gets onto a page.
 */
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const ARGV = process.argv.slice(2);
const file = ARGV[0];
const argOf = (n, d) => { const i = ARGV.indexOf(n); return i < 0 ? d : ARGV[i + 1]; };
const W = Number(argOf('--width', 1754));
const H = Number(argOf('--height', 1240));
const ONLY = argOf('--condition', null);
const SHEET_MM = argOf('--sheet-mm', null);
const DIST_MM = argOf('--distance-mm', null);
const TARGET = Number(argOf('--target', 0));
const ASJSON = ARGV.includes('--json');

if (!file) {
  console.error('usage: legibility.mjs page.html --condition ID [--width N] [--height N]');
  console.error('       legibility.mjs page.html --sheet-mm N --distance-mm N');
  process.exit(1);
}

const RAD2ARCMIN = 3437.746770784939;

// Each condition is a physical width the sheet is shown at, and a distance it is read from.
// Ordered by viewing ratio k = sheetMm / distMm, worst first.
const CONDITIONS = [
  { id: 'phone-fit',   sheetMm: 71,   distMm: 350,  label: 'Phone, fit to width, 6.1" at 35 cm' },
  { id: 'laptop-fit',  sheetMm: 234,  distMm: 600,  label: 'PDF fit-to-window, 15.6" 1920x1080 laptop, at 60 cm' },
  { id: 'projected',   sheetMm: 2400, distMm: 4000, label: 'Projected, 2.4 m screen, viewer at 4 m' },
  { id: 'monitor-fit', sheetMm: 429,  distMm: 700,  label: 'PDF fit-to-window, 27" 2560x1440, at 70 cm' },
  { id: 'a4-print',    sheetMm: 297,  distMm: 400,  label: 'Printed A4 landscape, read at 40 cm' },
  { id: 'monitor-100', sheetMm: 485,  distMm: 600,  label: 'PDF at 100%, 24" 1920x1080, at 60 cm (scrolls)' },
  { id: 'a3-print',    sheetMm: 420,  distMm: 500,  label: 'Printed A3 landscape, read at 50 cm' },
];
for (const c of CONDITIONS) c.k = c.sheetMm / c.distMm;

// ---------------------------------------------------------------------------
// THE VIEWING CONDITION IS REQUIRED.
//
// A glyph height in pixels is not a legibility claim on its own. 16px clears the
// critical print size on a printed A3 read at 50 cm and falls under the acuity limit
// in a phone-sized social post. This skill makes posters, A4 handouts, projected
// slides and social graphics, so the script refuses to produce a verdict until it has
// been told which one is being made.
function resolveCondition() {
  const custom = SHEET_MM !== null || DIST_MM !== null;
  if (ONLY && custom) {
    console.error('\n  --condition and --sheet-mm/--distance-mm are alternatives; pass one.\n');
    process.exit(2);
  }
  if (custom) {
    const sheetMm = Number(SHEET_MM);
    const distMm = Number(DIST_MM);
    if (!(sheetMm > 0) || !(distMm > 0)) {
      console.error('\n  --sheet-mm and --distance-mm must both be given, in millimetres, > 0.\n');
      process.exit(2);
    }
    const c = { id: 'custom', sheetMm, distMm,
                label: `Custom, sheet ${sheetMm} mm wide, read at ${distMm} mm` };
    c.k = c.sheetMm / c.distMm;
    return c;
  }
  if (ONLY) {
    const c = CONDITIONS.find((x) => x.id === ONLY);
    if (c) return c;
    console.error(`\n  unknown condition '${ONLY}'.`);
    listConditions();
    process.exit(2);
  }
  console.error('\n  No viewing condition given, so there is no verdict to give.');
  console.error('  The same type is comfortable on a poster and unreadable on a phone.');
  listConditions();
  process.exit(1);
}

function listConditions() {
  console.error('\n  Named conditions (--condition ID):\n');
  console.error('    ' + 'id'.padEnd(14) + 'sheet'.padStart(8) + 'distance'.padStart(10)
    + 'k'.padStart(7) + '   what it is');
  for (const c of [...CONDITIONS].sort((a, b) => a.k - b.k)) {
    console.error('    ' + c.id.padEnd(14) + `${c.sheetMm} mm`.padStart(8)
      + `${c.distMm} mm`.padStart(10) + c.k.toFixed(3).padStart(7) + '   ' + c.label);
  }
  console.error('\n  Or give a size that is not listed:  --sheet-mm N --distance-mm N');
  console.error('  Larger k is easier to read. Ranked worst first.\n');
}

const COND = resolveCondition();

// x-height thresholds, arcmin (Legge & Bigelow 2011)
const X = { acuity: 4.8, cps: 12, comfort: 18 };
// cap-height thresholds, arcmin (ISO 9241-303 / ANSI-HFES 100)
const C = { min: 16, preferred: 20 };

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(file)).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

const data = await page.evaluate(() => {
  const cv = document.createElement('canvas');
  const ctx = cv.getContext('2d');
  const inkCache = new Map();

  /** True inked height of 'x' and 'H' for a given font, in px.
   *
   * actualBoundingBoxAscent is reported to integer device pixels, so measuring a 12px
   * font directly gives 6 where the truth is 5.64 - an 8% error on the one quantity the
   * whole instrument is judging against a 12 arcmin bar. So the ratio is measured once
   * at 1000px, where integer rounding is 0.1%, and applied to the real size. This is
   * still a measurement of the font as the browser rasterises it, fallbacks included. */
  const RATIO_AT = 1000;
  function ratios(style, weight, family) {
    const key = `${style}|${weight}|${family}`;
    if (inkCache.has(key)) return inkCache.get(key);
    ctx.font = `${style} ${weight} ${RATIO_AT}px ${family}`;
    const v = {
      x: ctx.measureText('x').actualBoundingBoxAscent / RATIO_AT,
      cap: ctx.measureText('H').actualBoundingBoxAscent / RATIO_AT,
    };
    inkCache.set(key, v);
    return v;
  }

  const srgb = (c) => {
    const m = c && c.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?/);
    if (!m) return null;
    return { r: +m[1], g: +m[2], b: +m[3], a: m[4] === undefined ? 1 : +m[4] };
  };
  const lum = (c) => {
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
  };
  const ratio = (fg, bg) => {
    const a = lum(fg), b = lum(bg);
    return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
  };

  const PAPER = { r: 250, g: 246, b: 236, a: 1 };   // the plate, when nothing else is behind

  /** Resolved background behind an element: nearest opaque ancestor fill, else the paper. */
  function bgOf(el) {
    let n = el;
    while (n && n !== document.documentElement) {
      if (n.namespaceURI === 'http://www.w3.org/2000/svg') break;
      const c = srgb(getComputedStyle(n).backgroundColor);
      if (c && c.a > 0.5) return { c, from: n.className || n.tagName };
      n = n.parentElement;
    }
    return { c: PAPER, from: 'paper' };
  }

  /** For SVG text: a filled rect in the same <svg> whose box encloses the text. */
  function svgBgOf(el) {
    const owner = el.ownerSVGElement;
    if (!owner) return { c: PAPER, from: 'paper' };
    const tb = el.getBoundingClientRect();
    let best = null;
    for (const r of owner.querySelectorAll('rect, circle')) {
      const f = getComputedStyle(r).fill;
      if (!f || f === 'none' || f.startsWith('url(')) continue;
      const c = srgb(f);
      if (!c || c.a < 0.5) continue;
      const rb = r.getBoundingClientRect();
      if (rb.left <= tb.left + 1 && rb.right >= tb.right - 1
          && rb.top <= tb.top + 1 && rb.bottom >= tb.bottom - 1) {
        if (!best || (rb.width * rb.height) < best.area) best = { c, area: rb.width * rb.height, from: r.tagName };
      }
    }
    return best ? { c: best.c, from: best.from } : { c: PAPER, from: 'paper' };
  }

  const out = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  let node;
  while ((node = walker.nextNode())) {
    const s = node.textContent.replace(/\s+/g, ' ').trim();
    if (!s) continue;
    const el = node.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const box = el.getBoundingClientRect ? el.getBoundingClientRect() : null;

    const isSvg = el.namespaceURI === 'http://www.w3.org/2000/svg';
    // scale from user units to device px, so an SVG scaled by its viewBox is measured as shown
    let scale = 1;
    if (isSvg && el.getScreenCTM) {
      const m = el.getScreenCTM();
      if (m) scale = Math.sqrt(Math.abs(m.a * m.d - m.b * m.c)) || m.a || 1;
    }
    const fsDeclared = parseFloat(cs.fontSize) || 0;
    const rt = ratios(cs.fontStyle, cs.fontWeight, cs.fontFamily);
    const m = { x: rt.x * fsDeclared, cap: rt.cap * fsDeclared };

    const upper = /^[^a-z]*$/.test(s) && /[A-Z]/.test(s);
    const fg = srgb(cs.color) || { r: 0, g: 0, b: 0, a: 1 };
    const bg = isSvg ? svgBgOf(el) : bgOf(el);

    out.push({
      text: s.slice(0, 44),
      role: isSvg
        ? (el.closest('[data-viz]')?.getAttribute('data-viz') || 'svg')
        : (typeof el.className === 'string' && el.className ? el.className : el.tagName.toLowerCase()),
      svg: isSvg,
      fsDeclared: +fsDeclared.toFixed(2),
      scale: +scale.toFixed(4),
      fsShown: +(fsDeclared * scale).toFixed(2),
      xPx: +(m.x * scale).toFixed(3),
      capPx: +(m.cap * scale).toFixed(3),
      xRatio: +rt.x.toFixed(4),
      capRatio: +rt.cap.toFixed(4),
      upper,
      contrast: +ratio(fg, bg.c).toFixed(2),
      bgFrom: String(bg.from).slice(0, 18),
      y: box ? Math.round(box.top) : 0,
    });
  }
  return out;
});

await browser.close();

// ---------------------------------------------------------------- group and score
const groups = new Map();
for (const e of data) {
  const key = `${e.role}|${e.fsShown}|${e.upper}`;
  if (!groups.has(key)) groups.set(key, { ...e, n: 0, samples: [] });
  const g = groups.get(key);
  g.n++;
  if (g.samples.length < 2) g.samples.push(e.text);
  g.contrast = Math.min(g.contrast, e.contrast);
}
const rows = [...groups.values()].sort((a, b) => a.xPx - b.xPx);

const angle = (px, k) => (px / W) * k * RAD2ARCMIN;

function verdict(g, k) {
  const a = angle(g.upper ? g.capPx : g.xPx, k);
  const t = g.upper ? C : X;
  let v;
  if (g.upper) v = a >= C.preferred ? 'good' : a >= C.min ? 'ok' : a >= C.min * 0.67 ? 'slow' : 'fail';
  else v = a >= X.comfort ? 'good' : a >= X.cps ? 'ok' : a >= X.acuity ? 'slow' : 'fail';
  return { a, v };
}

if (ASJSON) {
  console.log(JSON.stringify({ file, W, H, condition: COND, conditions: CONDITIONS,
                               thresholds: { x: X, cap: C }, rows }, null, 1));
  process.exit(0);
}

const conds = [COND];

console.log(`\n  LEGIBILITY — ${file}`);
console.log(`  canvas ${W}x${H}px · ${data.length} text elements · ${rows.length} distinct sizes`);
console.log(`\n  Thresholds. Mixed case is judged on x-height (Legge & Bigelow 2011,`);
console.log(`  J Vision 11(5):8): ${X.acuity}' acuity limit · ${X.cps}' critical print size · ${X.comfort}' comfortable.`);
console.log(`  ALL CAPS is judged on cap height (ISO 9241-303 / ANSI-HFES 100): ${C.min}' minimum · ${C.preferred}' preferred.`);

// ---- per condition summary
console.log(`\n  SUMMARY — share of the page's text that clears each bar\n`);
console.log('  ' + 'condition'.padEnd(52) + 'k'.padStart(6) + 'good'.padStart(7) + 'ok'.padStart(6)
  + 'slow'.padStart(6) + 'fail'.padStart(6) + '   smallest');
for (const c of conds) {
  const tally = { good: 0, ok: 0, slow: 0, fail: 0 };
  let min = Infinity;
  for (const g of rows) {
    const { a, v } = verdict(g, c.k);
    tally[v] += g.n;
    min = Math.min(min, a);
  }
  const tot = Object.values(tally).reduce((x, y) => x + y, 0);
  const pc = (n) => (tot ? `${Math.round((100 * n) / tot)}%` : '-');
  console.log('  ' + c.label.padEnd(52) + c.k.toFixed(2).padStart(6)
    + pc(tally.good).padStart(7) + pc(tally.ok).padStart(6)
    + pc(tally.slow).padStart(6) + pc(tally.fail).padStart(6)
    + `   ${min.toFixed(1)}'`);
}

// ---- per size class, for the named condition (or the emailed default)
const focus = conds.find((c) => c.id === (ONLY || 'laptop-fit')) || conds[0];
console.log(`\n  BY SIZE CLASS — ${focus.label}  (k = ${focus.k.toFixed(3)})\n`);
console.log('  ' + 'role'.padEnd(22) + 'shown'.padStart(7) + 'x-ht'.padStart(7) + 'cap'.padStart(7)
  + 'angle'.padStart(8) + '  judged      verdict  contr   n  sample');
for (const g of rows) {
  const { a, v } = verdict(g, focus.k);
  console.log('  ' + String(g.role).slice(0, 21).padEnd(22)
    + `${g.fsShown}px`.padStart(7)
    + g.xPx.toFixed(1).padStart(7)
    + g.capPx.toFixed(1).padStart(7)
    + `${a.toFixed(1)}'`.padStart(8)
    + '  ' + (g.upper ? 'cap/ISO  ' : 'x-ht/L&B ')
    + v.padEnd(8) + String(g.contrast).padStart(6)
    + String(g.n).padStart(4) + '  ' + g.samples[0]);
}

// ---- prescription
if (TARGET) {
  console.log(`\n  PRESCRIPTION — every class raised to ${TARGET}' under "${focus.label}"\n`);
  console.log('  ' + 'role'.padEnd(22) + 'now'.padStart(8) + 'needs'.padStart(8) + 'factor'.padStart(8) + '  sample');
  let worst = 0;
  for (const g of rows) {
    const h = g.upper ? g.capPx : g.xPx;
    const need = (TARGET / RAD2ARCMIN) * (W / focus.k);      // required glyph height px
    const factor = need / h;
    worst = Math.max(worst, factor);
    console.log('  ' + String(g.role).slice(0, 21).padEnd(22)
      + `${g.fsShown}px`.padStart(8)
      + `${(g.fsShown * factor).toFixed(1)}px`.padStart(8)
      + `${factor.toFixed(2)}x`.padStart(8) + '  ' + g.samples[0]);
  }
  console.log(`\n  Largest factor required: ${worst.toFixed(2)}x.`);
  console.log(`  Area is the square of that: the same content would need ${(worst * worst).toFixed(1)}x the sheet,`);
  console.log(`  or the content has to come down to ${(100 / (worst * worst)).toFixed(0)}% of what is on it now.`);
}
console.log();
