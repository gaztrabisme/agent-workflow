#!/usr/bin/env node
// Scan every element for content taller/wider than its own box, and report the last child's
// clearance inside each fixed-height container. Catches text pushed through a border.
import { chromium } from 'playwright-core';
import { pathToFileURL } from 'node:url';

const [, , file] = process.argv;
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1240, height: 1754 } });
await p.goto(pathToFileURL(file).href, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(300);

const out = await p.evaluate(() => {
  const bad = [];
  for (const e of document.querySelectorAll('div, section, ul, li, p, h1, h3, h4')) {
    const oy = e.scrollHeight - e.clientHeight;
    const ox = e.scrollWidth - e.clientWidth;
    if (oy > 1 || ox > 1) {
      bad.push({ cls: e.className || e.tagName, overflowY: oy, overflowX: ox,
                 h: Math.round(e.getBoundingClientRect().height) });
    }
  }
  const clearance = [];
  for (const sel of ['.hero', '.offs', '.dm', '.fz', '.proof', '.mast']) {
    const c = document.querySelector(sel);
    if (!c) continue;
    const kids = [...c.children].filter(k => k.getBoundingClientRect().height > 0);
    if (!kids.length) continue;
    const last = kids[kids.length - 1].getBoundingClientRect();
    const box = c.getBoundingClientRect();
    clearance.push({ sel, below: +(box.bottom - last.bottom).toFixed(1),
                     padBottom: getComputedStyle(c).paddingBottom });
  }
  return { overflowing: bad, clearance };
});
console.log(JSON.stringify(out, null, 2));
await b.close();
