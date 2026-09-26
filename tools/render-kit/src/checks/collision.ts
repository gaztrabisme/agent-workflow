import type { CheckContext } from '../model.ts';
import { result, scanTextBoxes, type TextBox } from './common.ts';

export async function run(ctx: CheckContext) {
  const min = ctx.options.thresholds['collision.min_overlap_px'] ?? 1;
  const boxes = (await scanTextBoxes(ctx.session.page) as TextBox[]).sort((a:TextBox, b:TextBox) => a.box.left - b.box.left), items: unknown[] = [];
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length && boxes[j].box.left < boxes[i].box.right - min; j++) {
    const a = boxes[i], b = boxes[j], wa = Math.min(a.box.right,b.box.right)-Math.max(a.box.left,b.box.left), ha = Math.min(a.box.bottom,b.box.bottom)-Math.max(a.box.top,b.box.top);
    if (a.owner === b.owner || a.ancestors.some(x => x.selector === b.owner) || b.ancestors.some(x => x.selector === a.owner)) continue;
    if (a.ancestors.some(x => x.allow) || b.ancestors.some(x => x.allow) || wa <= min || ha <= min) continue;
    items.push({ selectors:[a.selector,b.selector], overlap:{ left:Math.max(a.box.left,b.box.left), top:Math.max(a.box.top,b.box.top), width:wa, height:ha } });
  }
  return result(ctx, 'collision', items.length ? 'fail' : 'pass', items);
}
