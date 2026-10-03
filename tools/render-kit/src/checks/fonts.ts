import type { CheckContext } from '../model.ts';
import { scanTextBoxes, result } from './common.ts';

const generic = new Set(['serif', 'sans-serif', 'monospace', 'cursive', 'fantasy', 'system-ui', 'ui-serif', 'ui-sans-serif', 'ui-monospace', 'ui-rounded', 'math', 'emoji', 'fangsong']);

export async function run(ctx: CheckContext) {
  const boxes = await scanTextBoxes(ctx.session.page);
  const rows = await ctx.session.page.evaluate((selectors: string[]) => selectors.map(selector => {
    const e = document.querySelector(selector)!; const first = getComputedStyle(e).fontFamily.split(',')[0].trim().replace(/^['"]|['"]$/g, '');
    const custom = [...document.fonts].some(f => f.family.replace(/^['"]|['"]$/g, '').toLowerCase() === first.toLowerCase() && f.status === 'loaded');
    return { selector, family: first, generic: ['serif','sans-serif','monospace','cursive','fantasy','system-ui','ui-serif','ui-sans-serif','ui-monospace','ui-rounded','math','emoji','fangsong'].includes(first.toLowerCase()), custom };
  }), boxes.map(b => b.owner));
  const root = (await ctx.session.cdp.send('DOM.getDocument')).root.nodeId;
  const failures: unknown[] = [], incomplete: unknown[] = [];
  for (const row of rows) {
    if (row.generic) continue;
    const node = await ctx.session.cdp.send('DOM.querySelector', { nodeId: root, selector: row.selector });
    if (!node.nodeId) { incomplete.push({ selector: row.selector, detail: 'font node could not be queried' }); continue; }
    const used = (await ctx.session.cdp.send('CSS.getPlatformFontsForNode', { nodeId: node.nodeId })).fonts as { familyName: string; isCustomFont: boolean; glyphCount: number }[];
    const ok = row.custom ? used.length > 0 && used.every(f => f.isCustomFont) : used.length > 0 && used.every(f => f.familyName.toLowerCase() === row.family.toLowerCase());
    if (!ok) failures.push({ selector: row.selector, requested: row.family, actual: used });
  }
  return result(ctx, 'fonts', failures.length ? 'fail' : incomplete.length ? 'incomplete' : 'pass', [...failures, ...incomplete], incomplete.length ? `${incomplete.length} text font(s) could not be measured` : undefined);
}
