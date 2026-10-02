import type { CheckContext } from '../model.ts';
import { result, scanTextBoxes, stageRect, type TextBox } from './common.ts';

export async function run(ctx: CheckContext) {
  const tol = ctx.options.thresholds['overflow.tolerance_px'] ?? 1, boxes = await scanTextBoxes(ctx.session.page) as TextBox[], stage = await stageRect(ctx.session.page,ctx.session.svgInput,ctx.options.height===undefined&&!ctx.session.svgInput);
  const measured = await ctx.session.page.evaluate((selectors: string[]) => selectors.map(selector => {
    const e = document.querySelector(selector)!;
    const pad = (n: Element) => { const r = n.getBoundingClientRect(), s = getComputedStyle(n); return { left:r.left+parseFloat(s.borderLeftWidth), top:r.top+parseFloat(s.borderTopWidth), right:r.right-parseFloat(s.borderRightWidth), bottom:r.bottom-parseFloat(s.borderBottomWidth) }; };
    let clip: any = null, scroll: any = null, clipNode: Element|null=null, scrollNode: Element|null=null; for (let p = e.parentElement; p; p = p.parentElement) {
      const s=getComputedStyle(p);
      if(!scroll&&['auto','scroll'].includes(s.overflowX)&&p.scrollWidth>p.clientWidth+1){scroll=pad(p);scrollNode=p;}
      if(!clip&&s.overflow!=='visible'){clip=pad(p);clipNode=p;}
      if(clip&&scroll)break;
    }
    const s = getComputedStyle(e), truncated = s.textOverflow === 'ellipsis' && e.scrollWidth > e.clientWidth && !e.closest('[data-rk-allow-truncate]');
    const svg = e.closest('svg'), v = svg?.getBoundingClientRect();
    return { selector, element: pad(e), clip, scroll, clipIsScroll:!!clipNode&&clipNode===scrollNode, truncated, scrollWidth:e.scrollWidth, clientWidth:e.clientWidth, svg: v && { left:v.left,top:v.top,right:v.right,bottom:v.bottom } };
  }), boxes.map(b => b.selector));
  const items: unknown[] = [];
  const excess = (b: any, r: any) => ({ left:Math.max(0,b.left-r.left), top:Math.max(0,b.top-r.top), right:Math.max(0,r.right-b.right), bottom:Math.max(0,r.bottom-b.bottom) });
  const add = (kind: string, selector: string, amount: any) => { if (Object.values(amount).some(v => Number(v) > tol)) items.push({ kind, selector, overflow: amount }); };
  for (let i = 0; i < boxes.length; i++) {
    const b = boxes[i].box, m = measured[i];
    add('clipped-text', boxes[i].selector, excess(m.element, b));
    if (m.clip) {
      const clipped=excess(m.clip,b);
      if(m.clipIsScroll){clipped.left=0;clipped.right=0;}
      add('clipped-text', boxes[i].selector, clipped);
    }
    if (m.truncated) items.push({ kind: 'truncated-text', selector: boxes[i].selector, overflow: { right: m.scrollWidth-m.clientWidth } });
    if (m.svg) add('svg-text-viewport', boxes[i].selector, excess(m.svg, b));
  }
  const visible = await ctx.session.page.evaluate(() => [...document.querySelectorAll('*')].map(e => {
    const sel=(el:Element)=>{if(el.id&&document.querySelectorAll(`#${CSS.escape(el.id)}`).length===1)return `#${CSS.escape(el.id)}`;if(el===document.documentElement)return 'html';const parts:string[]=[];for(let n:Element|null=el;n&&n!==document.documentElement;n=n.parentElement){let i=1;for(let p=n.previousElementSibling;p;p=p.previousElementSibling)if(p.localName===n.localName)i++;parts.unshift(`${n.localName}:nth-of-type(${i})`);}return `html>${parts.join('>')}`;};
    const r=e.getBoundingClientRect(), s=getComputedStyle(e);let hidden=!!e.closest('[data-rk-ignore]');
    const details=e.closest('details:not([open])');if(details&&e.closest('summary')?.parentElement!==details)hidden=true;
    for(let n:Element|null=e;n;n=n.parentElement){const ns=getComputedStyle(n),nr=n.getBoundingClientRect();if(Number(ns.opacity)===0||/^inset\(\s*50%(?:\s+50%){0,3}(?:\s+round\b[^)]*)?\s*\)$/i.test(ns.clipPath)||(['absolute','fixed'].includes(ns.position)&&nr.width<=1.01&&nr.height<=1.01&&(ns.clip!=='auto'||ns.clipPath!=='none')))hidden=true;}
    const focusable=e.closest('a[href],area[href],button,input,select,textarea,[tabindex]:not([tabindex="-1"])');for(let n:Element|null=focusable;n;n=n.parentElement){const ns=getComputedStyle(n),nr=n.getBoundingClientRect();if(['absolute','fixed'].includes(ns.position)&&(nr.right<=0||nr.left>=innerWidth||nr.bottom<=0||nr.top>=innerHeight))hidden=true;}
    let scroll:any=null;for(let p=e.parentElement;p;p=p.parentElement){const ps=getComputedStyle(p);if(['auto','scroll'].includes(ps.overflowX)&&p.scrollWidth>p.clientWidth+1){const pr=p.getBoundingClientRect();scroll={left:pr.left+parseFloat(ps.borderLeftWidth),right:pr.right-parseFloat(ps.borderRightWidth)};break;}}
    const geometry=e.namespaceURI==='http://www.w3.org/2000/svg'&&['path','line','polyline','polygon','rect','circle','ellipse'].includes(e.localName),stroked=geometry&&(r.width===0||r.height===0)&&s.stroke!=='none'&&parseFloat(s.strokeWidth)>0;
    const clamp=(x:number)=>scroll?Math.max(scroll.left,Math.min(scroll.right,x)):x;
    return { selector:sel(e), left:clamp(r.left),top:r.top,right:clamp(r.right),bottom:r.bottom,visible:(r.width>0&&r.height>0||stroked)&&s.display!=='none'&&s.visibility!=='hidden'&&!hidden };
  }).filter(e => e.visible));
  for (const el of visible) add('offstage', el.selector, excess(stage, el));
  return result(ctx, 'overflow', items.length ? 'fail' : 'pass', items);
}
