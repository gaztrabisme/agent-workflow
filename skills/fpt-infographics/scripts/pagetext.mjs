#!/usr/bin/env node
/**
 * pagetext.mjs — print the text a reader can actually see on the rendered page.
 *
 *   node scripts/pagetext.mjs page.html [--width N] [--height N]
 *
 * WHY. Content rules ("no deal values on the client sheet", "no customer name outside
 * the cleared list") are about what the reader sees. Grepping the HTML source answers a
 * different question and answers it wrongly: a self-contained sheet embeds its fonts as
 * base64, and a long base64 blob contains every three-letter sequence you might search
 * for. Checking one such sheet for "TCV" found three matches and for "PwC" found one -
 * all four inside the font data, none on the page.
 *
 * So: render, then take the visible text. Includes SVG <text>, excludes anything
 * display:none, visibility:hidden or zero-sized, and excludes <title>/<style>/<script>.
 */
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const ARGV = process.argv.slice(2);
const file = ARGV[0];
const argOf = (n, d) => { const i = ARGV.indexOf(n); return i < 0 ? d : Number(ARGV[i + 1]); };
const W = argOf('--width', 1754);
const H = argOf('--height', 1240);

if (!file) { console.error('usage: pagetext.mjs page.html [--width N] [--height N]'); process.exit(2); }

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(file)).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

const text = await page.evaluate(() => {
  const NOPAINT = new Set(['TITLE', 'STYLE', 'SCRIPT', 'HEAD', 'META', 'LINK', 'NOSCRIPT', 'TEMPLATE']);
  const out = [];
  const walk = (node) => {
    for (const ch of node.childNodes) {
      if (ch.nodeType === 3) {
        const t = ch.textContent.replace(/\s+/g, ' ').trim();
        if (t) out.push(t);
        continue;
      }
      if (ch.nodeType !== 1) continue;
      if (NOPAINT.has(ch.tagName)) continue;
      const cs = getComputedStyle(ch);
      if (cs.display === 'none' || cs.visibility === 'hidden' || Number(cs.opacity) === 0) continue;
      walk(ch);
    }
  };
  walk(document.body);
  return out.join('\n');
});

await browser.close();
process.stdout.write(text + '\n');
