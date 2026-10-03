import { mkdir } from 'node:fs/promises';
import { dirname } from 'node:path';
import type { RunOptions, Session } from './model.ts';
import { CHROMIUM_CAPTURE_LIMIT_PX } from './capture-limit.ts';
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

export async function capture(session: Session, options: RunOptions, out: string, format: 'png' | 'pdf', boundOversizedPng = false) {
  await mkdir(dirname(out), { recursive: true });
  const page = session.page;
  const fullDocument = options.height === undefined && !session.svgInput;
  const stage = await page.evaluate(({svgInput,fullDocument}:{svgInput:boolean;fullDocument:boolean}) => {
    const element = document.querySelector('[data-rk-stage]') ?? (svgInput?document.querySelector('body > svg'):null);
    const pageHeight = fullDocument ? Math.max(innerHeight, document.documentElement.scrollHeight, document.body?.scrollHeight ?? 0) : innerHeight;
    if (!element) return { x: 0, y: 0, width: innerWidth, height: pageHeight };
    const b = element.getBoundingClientRect(), bottom = Math.min(pageHeight, b.bottom);
    return { x: Math.max(0, b.x), y: Math.max(0, b.y), width: Math.max(0, Math.min(innerWidth, b.right) - Math.max(0, b.x)), height: Math.max(0, bottom - Math.max(0, b.y)) };
  },{svgInput:session.svgInput,fullDocument});
  const clip = { ...stage }, exceedsCaptureLimit = format === 'png' && boundOversizedPng &&
    (Math.ceil(stage.width * session.scale) > CHROMIUM_CAPTURE_LIMIT_PX || Math.ceil(stage.height * session.scale) > CHROMIUM_CAPTURE_LIMIT_PX);
  if (exceedsCaptureLimit) {
    clip.width = Math.min(clip.width, CHROMIUM_CAPTURE_LIMIT_PX / session.scale);
    clip.height = Math.min(clip.height, CHROMIUM_CAPTURE_LIMIT_PX / session.scale);
  }
  if (options.simulate) await session.cdp.send('Emulation.setEmulatedVisionDeficiency', { type: options.simulate as 'protanopia'|'deuteranopia'|'tritanopia'|'achromatopsia' });
  if (format === 'png') await page.screenshot({ path: out, clip, fullPage: fullDocument, animations: 'allow' });
  else {
    await page.emulateMedia({ media: options.media });
    const hasPageRule = await page.evaluate(() => [...document.styleSheets].some(sheet => { try { return [...sheet.cssRules].some(rule => rule.cssText.startsWith('@page')); } catch { return false; } }));
    if (!hasPageRule) await page.addStyleTag({ content: `@page{size:${stage.width}px ${stage.height}px;margin:0}html,body{margin:0}` });
    await page.pdf({ path: out, width:`${stage.width}px`, height:`${stage.height}px`, margin:{top:'0px',right:'0px',bottom:'0px',left:'0px'}, preferCSSPageSize: true, printBackground: true, tagged: true, outline: true });
    if(session.url.toLowerCase().endsWith('.svg'))await normalizePdfBox(out,stage.width,stage.height);
  }
  return format === 'png' ? { width: Math.round(clip.width * session.scale), height: Math.round(clip.height * session.scale) }
    : { width: stage.width * 0.75, height: stage.height * 0.75 };
}
