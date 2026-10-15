#!/usr/bin/env node
/**
 * brandcheck.mjs — FPT brand conformance on a rendered page.
 *
 *   node scripts/brandcheck.mjs page.html --width 1754 --height 1240 [--json]
 *
 * WHY THIS EXISTS. Across eight versions of one sheet, the brand arrived only when
 * someone asked for it: the guidelines were in the project folder from the first hour
 * and version five still shipped in two off-brand typefaces on a design language's own
 * palette. A rule nobody can run is a rule that arrives late. Every check below is a
 * restatement of a numbered rule in references/fpt-brand.md, which cites the page in
 * FPT Software Brand Guidelines v4.0 (August 2026).
 *
 * What this cannot check, and must not pretend to: whether Orange is used "frequently
 * but not overwhelmingly" (p.57), whether the graphic element reinforces identity
 * "where it is lacking" (p.63), and whether the artefact counts as owned media under
 * the One FPT policy (p.33). Those are judgements; they are printed as prompts.
 */
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const ARGV = process.argv.slice(2);
const file = ARGV[0];
const argOf = (n, d) => { const i = ARGV.indexOf(n); return i < 0 ? d : ARGV[i + 1]; };
const W = Number(argOf('--width', 0));
const H = Number(argOf('--height', 0));
const ASJSON = ARGV.includes('--json');
// The two-layer rule (SKILL.md): brand owns palette/type/logo, the design language
// owns ground, geometry and devices. Declare the language's ground tokens so they are
// not reported as off-palette. Declaring them is the point - an undeclared colour is
// a colour nobody chose.
const GROUND = (argOf('--ground', '') || '').split(',')
  .map((h) => h.trim().toLowerCase()).filter(Boolean);

if (!file || !W || !H) {
  console.error('usage: brandcheck.mjs page.html --width N --height N [--ground "#hex,#hex"] [--json]');
  process.exit(2);
}

// references/fpt-brand.md §1 — the ARTWORK palette (guidelines p.56).
const ARTWORK = {
  '#f37021': 'Orange (primary, highlight)',
  '#034ea2': 'Blue (primary)',
  '#50b848': 'Green (primary)',
  '#19226d': 'Dark Violet Blue (secondary)',
  '#33b2c1': 'Emerald (secondary)',
};
// The LOGO palette (p.32). Deliberately different from the artwork palette; if these
// appear outside the logo image someone has sampled a colour off the mark.
const LOGO_ONLY = { '#0066b3': 'logo Blue', '#0db14b': 'logo Green' };
// Neutrals a sheet may use freely: white, black, and greys.
const isNeutral = (hx) => {
  const r = parseInt(hx.slice(1, 3), 16), g = parseInt(hx.slice(3, 5), 16), b = parseInt(hx.slice(5, 7), 16);
  return Math.max(r, g, b) - Math.min(r, g, b) <= 12;
};

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(file)).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

const out = await page.evaluate(({ ARTWORK, LOGO_ONLY, W, H, GROUND }) => {
  const ground = new Set(GROUND);
  const errors = [], warnings = [], notes = [];
  const norm = (c) => {
    const m = c && c.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?/);
    if (!m) return null;
    if (m[4] !== undefined && Number(m[4]) === 0) return null;   // fully transparent
    return '#' + [1, 2, 3].map((i) => (+m[i]).toString(16).padStart(2, '0')).join('');
  };
  const grey = (hx) => {
    const r = parseInt(hx.slice(1, 3), 16), g = parseInt(hx.slice(3, 5), 16), b = parseInt(hx.slice(5, 7), 16);
    return Math.max(r, g, b) - Math.min(r, g, b) <= 12;
  };
  const lum = (hx) => {
    const v = [1, 3, 5].map((i) => parseInt(hx.slice(i, i + 2), 16) / 255)
      .map((c) => (c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4)));
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
  };
  const who = (el) => (el.getAttribute && el.getAttribute('data-viz'))
    || (typeof el.className === 'string' && el.className.trim().split(/\s+/)[0]) || el.tagName;

  const SKIP = new Set(['HTML', 'HEAD', 'META', 'TITLE', 'STYLE', 'SCRIPT', 'LINK', 'BR']);
  const off = new Map(), logoLeak = new Map();
  const oranges = [], greens = [], emeralds = [], blues = [], dvbs = [], blacks = [];

  for (const el of document.querySelectorAll('*')) {
    if (SKIP.has(el.tagName)) continue;
    // The root <svg> and anything inside <defs> paint nothing themselves; their
    // computed fill is the initial black and would read as an off-brand colour.
    if (el.tagName === 'svg' || el.closest('defs')) continue;
    const b = el.getBoundingClientRect();
    if (!b.width && !b.height) continue;
    const isSvg = el.namespaceURI === 'http://www.w3.org/2000/svg';
    const cs = getComputedStyle(el);
    // fill/stroke are only meaningful on SVG nodes; on HTML they report the initial
    // value black and say nothing about what is painted.
    const props = isSvg ? ['fill', 'stroke', 'color'] : ['color', 'backgroundColor', 'borderTopColor'];
    const here = new Set();
    for (const p of props) {
      const v = cs[p];
      if (!v || v === 'none' || v.includes('rgba(0, 0, 0, 0)')) continue;
      if (p === 'color' && !el.textContent.trim()) continue;  // inherited, paints nothing
      const hx = norm(v);
      if (!hx) continue;
      here.add(hx);
      if (hx === '#f37021') oranges.push({ b, who: who(el), p });
      if (hx === '#50b848') greens.push({ b, who: who(el), p });
      if (hx === '#33b2c1') emeralds.push({ b, who: who(el), p });
      if (hx === '#034ea2') blues.push({ b, who: who(el), p });
      if (hx === '#19226d') dvbs.push({ b, who: who(el), p });
      if (hx === '#000000') blacks.push({ b, who: who(el), p });
      if (LOGO_ONLY[hx]) logoLeak.set(hx, (logoLeak.get(hx) || '') + ' ' + who(el) + '/' + p);
      else if (!ARTWORK[hx] && !grey(hx) && !ground.has(hx)) off.set(hx, (off.get(hx) || 0) + 1);
    }
    // p.60 common mistakes: never more than two colours in one element.
    const brandHere = [...here].filter((h) => ARTWORK[h]);
    if (brandHere.length > 2) {
      warnings.push(`three-colours   ${who(el)} carries ${brandHere.length} brand colours (${brandHere.join(' ')}) — p.60 allows two`);
    }
  }

  // §1 — logo palette must not leak into artwork.
  for (const [hx, where] of logoLeak) {
    errors.push(`logo-palette    ${hx} (${LOGO_ONLY[hx]}) used in artwork:${where} — artwork uses the p.56 palette, not the logo's`);
  }
  // §1 — anything outside the palette and not a neutral.
  for (const [hx, n] of [...off].sort((a, b) => b[1] - a[1])) {
    warnings.push(`off-palette     ${hx} on ${n} element(s) — not in the p.56 artwork palette and not a neutral`);
  }

  // §2 — Blue and Dark Violet Blue must not be combined with black elements (p.58).
  // Absolute, and easy to hit by accident: an SVG path with no fill computes to black.
  const nearBlack = [];
  for (const k of [...blues, ...dvbs]) for (const bl of blacks) {
    const dx = Math.max(0, Math.max(k.b.left - bl.b.right, bl.b.left - k.b.right));
    const dy = Math.max(0, Math.max(k.b.top - bl.b.bottom, bl.b.top - k.b.bottom));
    if (Math.hypot(dx, dy) < 40) nearBlack.push(`${k.who}(${k.p}) with black ${bl.who}(${bl.p})`);
  }
  if (nearBlack.length) {
    errors.push(`blue-with-black ${nearBlack.length} Blue/Dark-Violet-Blue element(s) beside a black element — p.58 forbids it. `
      + `A common cause is an SVG path with no explicit fill, which computes to black: give it fill="none". `
      + `First: ${[...new Set(nearBlack)].slice(0, 3).join(' · ')}`);
  }

  // §2 — Orange with Green or Emerald is NOT RECOMMENDED, permitted very sparingly
  // (p.57). A warning to justify, not a failure: the guideline hedges and so do we.
  const clash = [];
  for (const o of oranges) for (const g of [...greens, ...emeralds]) {
    const dx = Math.max(0, Math.max(o.b.left - g.b.right, g.b.left - o.b.right));
    const dy = Math.max(0, Math.max(o.b.top - g.b.bottom, g.b.top - o.b.bottom));
    const d = Math.hypot(dx, dy);
    if (d < 120) clash.push(`${o.who}(${o.p}) <-> ${g.who}(${g.p}) ${Math.round(d)}px`);
  }
  const clashes = [...new Set(clash)];
  if (clashes.length) {
    warnings.push(`orange-green    ${clashes.length} Orange/Green-or-Emerald pair(s) within 120px — p.57 says not recommended `
      + `"unless very sparingly or with other colors also included". Justify or separate. First: ${clashes.slice(0, 3).join(' · ')}`);
  }

  // §2 — Green may be dominant only on a photographic image emphasising
  // sustainability (p.58), so never on a drawn sheet.
  let area = { '#50b848': 0, '#034ea2': 0, '#f37021': 0 };
  for (const [arr, hx] of [[greens, '#50b848'], [blues, '#034ea2'], [oranges, '#f37021']]) {
    for (const e of arr) if (e.p === 'backgroundColor' || e.p === 'fill') area[hx] += e.b.width * e.b.height;
  }
  const canvas = W * H;
  if (area['#50b848'] / canvas > 0.25 && area['#50b848'] >= Math.max(area['#034ea2'], area['#f37021'])) {
    errors.push(`green-dominant  Green covers ${Math.round(area['#50b848'] / canvas * 100)}% and is the largest brand area — `
      + `p.58 allows Green as dominant only on a photo emphasising sustainability`);
  }

  // §3 — the full-colour logo needs a background at most 20% dark or over 85% dark (p.33).
  const logo = document.querySelector('.logo, [data-logo], img[alt*="FPT" i]');
  let logoNote = null;
  if (logo) {
    const r = logo.getBoundingClientRect();
    // Walk up for the nearest ancestor that actually paints a background.
    let bg = null;
    for (let el = logo.parentElement; el; el = el.parentElement) {
      const c = norm(getComputedStyle(el).backgroundColor);
      if (c) { bg = c; break; }
    }
    if (bg) {
      const darkPct = Math.round((1 - lum(bg)) * 100);
      logoNote = { bg, darkPct, at: [Math.round(r.x), Math.round(r.y)] };
      if (darkPct > 20 && darkPct <= 85) {
        errors.push(`logo-background the logo sits on ${bg}, which is ${darkPct}% dark — p.33 permits the full-colour mark `
          + `only at 20% dark or less, or more than 85% dark`);
      } else if (darkPct > 85) {
        notes.push(`logo on a ${darkPct}% dark ground: p.33 requires the typography and the ® to be white. Confirm by eye.`);
      }
    }
  } else {
    warnings.push('logo-missing    no element matched .logo / [data-logo] / img[alt*=FPT] — the mark could not be checked');
  }

  // §5 — BR Omega must be the typeface actually in use.
  const fams = new Map();
  const NOPAINT = new Set(['TITLE', 'STYLE', 'SCRIPT', 'HEAD', 'META', 'LINK', 'NOSCRIPT', 'TEMPLATE']);
  for (const el of document.querySelectorAll('*')) {
    if (NOPAINT.has(el.tagName)) continue;
    const own = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
    if (!own) continue;
    const rr = el.getBoundingClientRect();
    if (!rr.width || !rr.height) continue;
    const f = getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim();
    fams.set(f, (fams.get(f) || 0) + 1);
  }
  const ranked = [...fams].sort((a, b) => b[1] - a[1]);
  const nonBrOmega = ranked.filter(([f]) => !/^BR Omega/i.test(f));
  if (!ranked.some(([f]) => /^BR Omega/i.test(f))) {
    errors.push(`typeface        no text is set in BR Omega — p.70 makes it the primary typeface for all artworks. `
      + `Found: ${ranked.slice(0, 3).map(([f, n]) => `${f} x${n}`).join(', ')}`);
  } else if (nonBrOmega.length) {
    warnings.push(`typeface-mixed  ${nonBrOmega.length} non-BR-Omega famil(y/ies): `
      + nonBrOmega.slice(0, 4).map(([f, n]) => `${f} x${n}`).join(', '));
  }

  return {
    errors, warnings, notes, logo: logoNote,
    fonts: ranked.slice(0, 6),
    counts: { orange: oranges.length, blue: blues.length, green: greens.length,
              emerald: emeralds.length, dvb: dvbs.length, black: blacks.length },
  };
}, { ARTWORK, LOGO_ONLY, W, H, GROUND });

await browser.close();

// Judgements the guidelines make but no script can settle. Printed every run, so they
// are answered in the content brief rather than forgotten.
const PROMPTS = [
  'p.57 — is Orange used frequently but not overwhelmingly, and mainly to highlight?',
  'p.63 — if the graphic element is used, is it under 30% and does a rounded corner fall inside?',
  'p.33 — One FPT policy: is this artefact owned media? A cold outbound sheet is not obviously so.',
];

if (ASJSON) {
  console.log(JSON.stringify({ file, W, H, ...out, prompts: PROMPTS }, null, 1));
} else {
  console.log(`\n  BRAND — ${file}`);
  console.log(`  against FPT Software Brand Guidelines v4.0 (Aug 2026), via references/fpt-brand.md\n`);
  for (const e of out.errors) console.log(`  ✗ ERROR ${e}`);
  for (const w of out.warnings) console.log(`  ! warn  ${w}`);
  console.log(`\n  typeface     ${out.fonts.map(([f, n]) => `${f} x${n}`).join(' · ')}`);
  if (out.logo) console.log(`  logo ground  ${out.logo.bg}, ${out.logo.darkPct}% dark`);
  console.log(`  brand marks  ${Object.entries(out.counts).map(([k, v]) => `${k} ${v}`).join(' · ')}`);
  for (const n of out.notes) console.log(`  note         ${n}`);
  console.log(`\n  Answer in the content brief — no script can settle these:`);
  for (const p of PROMPTS) console.log(`    · ${p}`);
  console.log(`\nbrand: ${out.errors.length} error(s), ${out.warnings.length} warning(s)`);
}
process.exit(out.errors.length ? 1 : 0);
