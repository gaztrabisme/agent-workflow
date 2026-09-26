import type { Page } from 'playwright';

export async function waitAndBoot(page: Page, options: { boot: number; waitFor?: string; timeout: number }) {
  await page.clock.runFor(options.boot);
  await page.evaluate(() => document.fonts.ready);
  const start = Date.now(); let elapsed = 0;
  while (options.waitFor && !(await page.locator(options.waitFor).count())) {
    if (elapsed >= options.timeout || Date.now() - start >= options.timeout) throw new Error(`Timed out waiting for ${options.waitFor}`);
    await page.clock.runFor(16); elapsed += 16;
  }
  await page.waitForLoadState('networkidle', { timeout: options.timeout });
  await page.evaluate(() => { (window as any).__rkAnimations = document.getAnimations(); });
}

export async function seek(page: Page, at: number | 'end', settle: number, boot: number) {
  const duration = at === 'end' ? settle : at;
  await page.clock.runFor(duration);
  if(at!=='end'&&await page.evaluate(()=>typeof (window as any).__rkRafPending==='function'&&(window as any).__rkRafPending()>0)){
    const target=new Date(Date.parse('2026-01-01T00:00:00.000Z')+boot+duration);
    await page.clock.setFixedTime(target);await page.clock.runFor(16);await page.clock.pauseAt(target);
  }
  await page.evaluate(({ duration, end, boot }) => {
    const animations = (window as any).__rkAnimations as Animation[];
    for (const animation of animations) {
      try { if (end && animation.effect?.getComputedTiming().endTime !== Infinity) animation.finish();
        else { animation.pause(); animation.currentTime = boot + duration; } } catch { /* detached or cancelled animation */ }
    }
    for (const svg of document.querySelectorAll('svg')) {
      const root = svg as SVGSVGElement; root.pauseAnimations?.(); root.setCurrentTime?.((boot + duration) / 1000);
    }
  }, { duration, end: at === 'end', boot });
}
