import { chromium } from 'playwright';
import { resolve, dirname } from 'node:path';
import { stat, readFile } from 'node:fs/promises';
import type { RunOptions, Session } from './model.ts';
import { isUrl } from './util.ts';
import { startServer, svgSize } from './server.ts';

export async function openSession(options: RunOptions): Promise<Session> {
  const input = isUrl(options.input) ? options.input : resolve(options.input);
  let local: Awaited<ReturnType<typeof startServer>> | undefined;
  let svgInput=false;
  let width=options.width??1920,height=options.height??1080;
  if (!isUrl(input)) {
    if (!(await stat(input).catch(() => null))?.isFile()) throw new Error(`Input file does not exist: ${input}`);
    svgInput=input.toLowerCase().endsWith('.svg');
    if(svgInput&&(!options.width||!options.height)){const size=svgSize(await readFile(input,'utf8'));width=options.width??size.width;height=options.height??size.height;}
    local = await startServer(options.root ?? dirname(input), input);
  }
  const url = local?.url ?? input;
  const browser = await chromium.launch({ channel: 'chromium', headless: true });
  const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: options.scale, locale: 'en-US', timezoneId: 'UTC' });
  const page = await context.newPage(), cdp = await context.newCDPSession(page);
  const blocked: Session['blocked'] = [], errors: string[] = [];
  const origin = new URL(url).origin;
  await page.route('**/*', async route => {
    const requested = route.request().url();
    if (!options.allowNetwork && new URL(requested).origin !== origin) {
      blocked.push({ url: requested, reason: 'blocked by network policy' }); await route.abort('blockedbyclient'); return;
    }
    await route.continue();
  });
  page.on('response', response => { if (response.status() >= 400) blocked.push({ url: response.url(), reason: `HTTP ${response.status()}` }); });
  page.on('requestfailed', request => { if (!blocked.some(x => x.url === request.url())) blocked.push({ url: request.url(), reason: request.failure()?.errorText ?? 'request failed' }); });
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', msg => { if (msg.type() === 'error') {
    const location=msg.location().url,text=msg.text();
    const requestFailure=blocked.some(row=>row.url===location||text.includes(row.url))||/Failed to load resource: net::ERR_(?:ABORTED|BLOCKED_BY_CLIENT)/.test(text);
    if(!requestFailure)errors.push(text);
  } });
  await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
  await page.clock.install({ time: new Date('2026-01-01T00:00:00.000Z') });
  await page.clock.pauseAt(new Date('2026-01-01T00:00:00.000Z'));
  await page.addInitScript(() => {
    const w=window as any,native=w.requestAnimationFrame.bind(window);let pending=0;
    w.requestAnimationFrame=(callback:FrameRequestCallback)=>native((time:number)=>{pending--;callback(time);});
    const schedule=w.requestAnimationFrame;w.requestAnimationFrame=(callback:FrameRequestCallback)=>{pending++;return schedule(callback);};
    w.__rkRafPending=()=>pending;
  });
  return { browser, context, page, cdp, url, blocked, errors, width, height, scale: options.scale, svgInput, allowNetwork:options.allowNetwork,
    stop: async () => { await browser.close(); await new Promise<void>(ok => local ? local.server.close(() => ok()) : ok()); } };
}
