import { AxeBuilder } from '@axe-core/playwright';
import type { CheckContext } from '../model.ts';
import { result } from './common.ts';
import { withAxePage } from './axe.ts';

export async function run(ctx: CheckContext) {
  const report=await withAxePage(ctx.session,async page=>new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).exclude('[data-rk-ignore]').disableRules(['color-contrast']).analyze());
  const violations = report.violations.flatMap(v => v.nodes.map(n => ({ rule: v.id, impact: v.impact, selectors: n.target })));
  const incomplete = report.incomplete.map(v => ({ rule: v.id, impact: v.impact, selectors: v.nodes.flatMap(n => n.target) }));
  const items = [...violations, ...incomplete];
  const check = result(ctx, 'a11y', violations.length ? 'fail' : incomplete.length ? 'incomplete' : 'pass', items, incomplete.length ? `${incomplete.length} axe-core incomplete rule(s)` : undefined);
  check.items.unshift({ engine: 'axe-core', version: report.testEngine.version });
  return check;
}
