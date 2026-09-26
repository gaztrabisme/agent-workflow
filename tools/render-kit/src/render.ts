import { mkdir } from 'node:fs/promises';
import { dirname } from 'node:path';
import type { RunOptions, Session } from './model.ts';
import { normalizePdfBox } from './pdf-size.ts';
import { openSession } from './browser.ts';
import { seek, waitAndBoot } from './seek.ts';

export async function prepare(options: RunOptions) {
  const session = await openSession(options);
  try {
    await session.page.goto(session.url, { waitUntil: 'load', timeout: options.timeout });
    await waitAndBoot(session.page, options);
    await seek(session.page, options.at, options.settle, options.boot);
    return session;
  } catch (error) { await session.stop(); throw error; }
}

export async function capture(session: Session, options: RunOptions, out: string, format: 'png' | 'pdf') {
  await mkdir(dirname(out), { recursive: true });
  const page = session.page;
  const stage = await page.evaluate((svgInput:boolean) => {
    const element = document.querySelector('[data-rk-stage]') ?? (svgInput?document.querySelector('body > svg'):null);
    if (!element) return { x: 0, y: 0, width: innerWidth, height: innerHeight };
    const b = element.getBoundingClientRect(); return { x: Math.max(0, b.x), y: Math.max(0, b.y), width: Math.min(innerWidth, b.right) - Math.max(0, b.x), height: Math.min(innerHeight, b.bottom) - Math.max(0, b.y) };
  },session.svgInput);
  if (options.simulate) await session.cdp.send('Emulation.setEmulatedVisionDeficiency', { type: options.simulate as 'protanopia'|'deuteranopia'|'tritanopia'|'achromatopsia' });
  if (format === 'png') await page.screenshot({ path: out, clip: stage, animations: 'allow' });
  else {
    await page.emulateMedia({ media: options.media });
    const hasPageRule = await page.evaluate(() => [...document.styleSheets].some(sheet => { try { return [...sheet.cssRules].some(rule => rule.cssText.startsWith('@page')); } catch { return false; } }));
    if (!hasPageRule) await page.addStyleTag({ content: `@page{size:${stage.width}px ${stage.height}px;margin:0}html,body{margin:0}` });
    await page.pdf({ path: out, width:`${stage.width}px`, height:`${stage.height}px`, margin:{top:'0px',right:'0px',bottom:'0px',left:'0px'}, preferCSSPageSize: true, printBackground: true, tagged: true, outline: true });
    if(session.url.toLowerCase().endsWith('.svg'))await normalizePdfBox(out,stage.width,stage.height);
  }
  return format === 'png' ? { width: Math.round(stage.width * session.scale), height: Math.round(stage.height * session.scale) }
    : { width: stage.width * 0.75, height: stage.height * 0.75 };
}
