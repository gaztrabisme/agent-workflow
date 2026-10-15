#!/usr/bin/env node
// Crawl a JavaScript-rendered site with headless Chromium and dump rendered text per page.
//   node scripts/crawl.mjs <startUrl> <outDir> [maxPages]
import { chromium } from 'playwright-core';
import { writeFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const [, , start, outDir, maxArg = '20'] = process.argv;
const maxPages = Number(maxArg);
mkdirSync(outDir, { recursive: true });

const origin = new URL(start).origin;
const seen = new Set();
const queue = [start];
const pages = [];

const browser = await chromium.launch();
const ctx = await browser.newContext({
  viewport: { width: 1440, height: 2400 },
  userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36',
});
const page = await ctx.newPage();

while (queue.length && pages.length < maxPages) {
  const url = queue.shift();
  const key = url.split('#')[0].replace(/\/$/, '');
  if (seen.has(key)) continue;
  seen.add(key);
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 });
    await page.waitForTimeout(2500);                       // let client-side routing settle
    await page.evaluate(async () => {                       // trigger lazy sections
      for (let y = 0; y < document.body.scrollHeight; y += 450) {
        window.scrollTo(0, y); await new Promise(r => setTimeout(r, 420));
      }
      await new Promise(r => setTimeout(r, 2500));   // let count-up animations finish
    });
    await page.waitForTimeout(1500);

    const data = await page.evaluate(() => {
      const txt = document.body ? document.body.innerText : '';
      const links = [...document.querySelectorAll('a[href]')].map(a => a.href);
      const imgAlts = [...document.querySelectorAll('img[alt]')].map(i => i.alt).filter(Boolean);
      return { title: document.title, txt, links, imgAlts };
    });

    const clean = data.txt.replace(/\n{3,}/g, '\n\n').trim();
    pages.push({ url, title: data.title, chars: clean.length });
    const name = (new URL(url).pathname.replace(/[^a-z0-9]+/gi, '_') || 'index') + '.txt';
    writeFileSync(join(outDir, name),
      `URL: ${url}\nTITLE: ${data.title}\nIMG ALTS: ${data.imgAlts.join(' | ')}\n\n${clean}\n`, 'utf8');
    console.log(`  ${clean.length.toString().padStart(6)} chars  ${url}`);

    for (const l of data.links) {
      if (l.startsWith(origin) && !seen.has(l.split('#')[0].replace(/\/$/, ''))) queue.push(l);
    }
  } catch (e) {
    console.log(`  FAILED  ${url}  ${e.message.split('\n')[0]}`);
    pages.push({ url, error: e.message.split('\n')[0] });
  }
}

writeFileSync(join(outDir, '_index.json'), JSON.stringify(pages, null, 2), 'utf8');
await browser.close();
console.log(`\n${pages.filter(p => !p.error).length} pages captured -> ${outDir}`);
