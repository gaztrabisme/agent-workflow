import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1754, height: 1240 } });
await p.goto(pathToFileURL(resolve(process.argv[2])).href, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
const r = await p.evaluate(() => {
  const out = [];
  const deepest = (el) => {
    let m = 0;
    for (const n of el.querySelectorAll('*')) {
      const b = n.getBoundingClientRect();
      if (b.width && b.height) m = Math.max(m, b.bottom);
    }
    return Math.round(m);
  };
  for (const sel of ['.top', '.zA', '.zB', '.zC', '.zC .cl', '.zC .cr', '.zC .cs',
    '.spacer', '.foot', '.fcol.left', '.fcol.right']) {
    const e = document.querySelector(sel);
    if (!e) continue;
    const bb = e.getBoundingClientRect();
    out.push([sel, Math.round(bb.top), Math.round(bb.bottom), deepest(e),
      Math.round(bb.bottom - deepest(e))]);
  }
  return out;
});
console.log('  sel            top   box-bottom  content-bottom  slack');
for (const [s, t, bo, d, sl] of r) console.log('  ' + s.padEnd(14) + String(t).padStart(5) + String(bo).padStart(11) + String(d).padStart(14) + String(sl).padStart(8));
await b.close();
