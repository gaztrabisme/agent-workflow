#!/usr/bin/env node
// Print an HTML infographic to a single-page PDF at its own pixel size.
// Vector text, selectable, no margins.
//
//   node scripts/topdf.mjs input.html output.pdf --preset a3-landscape
//   node scripts/topdf.mjs input.html output.pdf --width 1754 --height 1240
//   node scripts/topdf.mjs input.html output.pdf 1754 1240        (legacy positional)
//
// The flags match render.mjs and check.mjs on purpose. This script used to take only
// positional sizes while its two siblings took flags, and passing --width to it
// produced "viewport.width: expected integer, got float NaN" - a confusing error for
// a calling convention, which cost real time on the engagement this skill came from.
//
// The canvas is required. There is no default: printing a 1754x1240 sheet at an
// assumed 1920x1080 silently crops it, and the PDF still looks plausible.
//
// If the text in the output looks pixelated when zoomed, the fonts are Type3 - see
// scripts/fonts.py, and check it with: check.mjs page.html --preset X --pdf out.pdf
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
};

const argv = process.argv.slice(2);
const positional = [];
let preset, width, height;
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--preset') preset = argv[++i];
  else if (a === '--width') width = Number(argv[++i]);
  else if (a === '--height') height = Number(argv[++i]);
  else if (a.startsWith('--')) { usage(`unknown flag: ${a}`); }
  else positional.push(a);
}
const [src, out, pw, ph] = positional;

function usage(msg) {
  console.error(`topdf.mjs: ${msg}`);
  console.error('Usage: node scripts/topdf.mjs input.html output.pdf --preset NAME');
  console.error('       node scripts/topdf.mjs input.html output.pdf --width N --height N');
  console.error(`Presets: ${Object.keys(PRESETS).join(' ')}`);
  process.exit(2);
}

if (!src || !out) usage('need input.html and output.pdf');
if (preset) {
  if (!PRESETS[preset]) usage(`unknown preset "${preset}"`);
  ({ width, height } = PRESETS[preset]);
}
if (width === undefined && pw !== undefined) width = Number(pw);
if (height === undefined && ph !== undefined) height = Number(ph);
if (!Number.isFinite(width) || !Number.isFinite(height) || width <= 0 || height <= 0) {
  usage('canvas size is required and must be two positive numbers');
}

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width, height } });
await page.goto(pathToFileURL(resolve(src)).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.pdf({
  path: out,
  width: `${width}px`,
  height: `${height}px`,
  printBackground: true,
  pageRanges: '1',
  margin: { top: '0', bottom: '0', left: '0', right: '0' },
});
await browser.close();
console.log(`pdf written ${out} (${width}x${height}, 1 page)`);
