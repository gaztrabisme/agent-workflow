import type { CheckContext } from '../model.ts';
import { result, scanTextBoxes, stageRect, type TextBox } from './common.ts';

export async function run(ctx: CheckContext) {
  const tol = ctx.options.thresholds['overflow.tolerance_px'] ?? 1, boxes = await scanTextBoxes(ctx.session.page) as TextBox[], stage = await stageRect(ctx.session.page,ctx.session.svgInput);
  const measured = await ctx.session.page.evaluate((selectors: string[]) => selectors.map(selector => {
    const e = document.querySelector(selector)!;
    const pad = (n: Element) => { const r = n.getBoundingClientRect(), s = getComputedStyle(n); return { left:r.left+parseFloat(s.borderLeftWidth), top:r.top+parseFloat(s.borderTopWidth), right:r.right-parseFloat(s.borderRightWidth), bottom:r.bottom-parseFloat(s.borderBottomWidth) }; };
    let clip: any = null; for (let p = e.parentElement; p; p = p.parentElement) if (getComputedStyle(p).overflow !== 'visible') { clip = pad(p); break; }
    const s = getComputedStyle(e), truncated = s.textOverflow === 'ellipsis' && e.scrollWidth > e.clientWidth && !e.closest('[data-rk-allow-truncate]');
    const svg = e.closest('svg'), v = svg?.getBoundingClientRect();
    return { selector, element: pad(e), clip, truncated, scrollWidth:e.scrollWidth, clientWidth:e.clientWidth, svg: v && { left:v.left,top:v.top,right:v.right,bottom:v.bottom } };
  }), boxes.map(b => b.selector));
  const items: unknown[] = [];
  const excess = (b: any, r: any) => ({ left:Math.max(0,b.left-r.left), top:Math.max(0,b.top-r.top), right:Math.max(0,r.right-b.right), bottom:Math.max(0,r.bottom-b.bottom) });
  const add = (kind: string, selector: string, amount: any) => { if (Object.values(amount).some(v => Number(v) > tol)) items.push({ kind, selector, overflow: amount }); };
  for (let i = 0; i < boxes.length; i++) {
    const b = boxes[i].box, m = measured[i];
    add('clipped-text', boxes[i].selector, excess(m.element, b));
    if (m.clip) add('clipped-text', boxes[i].selector, excess(m.clip, b));
    if (m.truncated) items.push({ kind: 'truncated-text', selector: boxes[i].selector, overflow: { right: m.scrollWidth-m.clientWidth } });
    if (m.svg) add('svg-text-viewport', boxes[i].selector, excess(m.svg, b));
  }
  const visible = await ctx.session.page.evaluate(() => [...document.querySelectorAll('*')].filter(e => !e.closest('[data-rk-ignore]')).map(e => {
    const sel=(el:Element)=>{if(el.id&&document.querySelectorAll(`#${CSS.escape(el.id)}`).length===1)return `#${CSS.escape(el.id)}`;if(el===document.documentElement)return 'html';const parts:string[]=[];for(let n:Element|null=el;n&&n!==document.documentElement;n=n.parentElement){let i=1;for(let p=n.previousElementSibling;p;p=p.previousElementSibling)if(p.localName===n.localName)i++;parts.unshift(`${n.localName}:nth-of-type(${i})`);}return `html>${parts.join('>')}`;};
    const r=e.getBoundingClientRect(), s=getComputedStyle(e);let hidden=false;for(let n:Element|null=e;n;n=n.parentElement)if(Number(getComputedStyle(n).opacity)===0)hidden=true;return { selector:sel(e), left:r.left,top:r.top,right:r.right,bottom:r.bottom,visible:r.width>0&&r.height>0&&s.display!=='none'&&s.visibility!=='hidden'&&!hidden };
  }));
  for (const el of visible) if (el.visible) add('offstage', el.selector, excess(stage, el));
  return result(ctx, 'overflow', items.length ? 'fail' : 'pass', items);
}
