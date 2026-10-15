#!/usr/bin/env node
// Measure rendered geometry of [data-viz] elements. Used to audit "is it an infographic"
// as a proportion of page height rather than a matter of opinion.
//   node scripts/measure.mjs <file.html> <pageHeight> [out.json]
import { chromium } from 'playwright-core';
import { pathToFileURL } from 'node:url';
import { writeFileSync } from 'node:fs';

const [, , file, hArg = '1754', out] = process.argv;
const pageH = Number(hArg);
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1240, height: pageH } });
await p.goto(pathToFileURL(file).href, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(400);

const data = await p.evaluate(() => {
  const els = [...document.querySelectorAll('[data-viz]')];
  return els.map(e => {
    const r = e.getBoundingClientRect();
    const numeric = [...e.querySelectorAll('text, tspan')]
      .map(t => t.textContent.trim())
      .filter(t => /\d/.test(t));
    return {
      viz: e.getAttribute('data-viz'),
      tag: e.tagName.toLowerCase(),
      width: Math.round(r.width),
      height: Math.round(r.height),
      numericLabels: numeric.length,
      samples: numeric.slice(0, 6),
    };
  });
});
const drawn = data.reduce((s, d) => s + d.height, 0);
const result = { pageHeight: pageH, charts: data, drawnHeight: drawn,
                 drawnFraction: +(drawn / pageH).toFixed(4) };
console.log(JSON.stringify(result, null, 2));
if (out) writeFileSync(out, JSON.stringify(result, null, 2), 'utf8');
await b.close();
