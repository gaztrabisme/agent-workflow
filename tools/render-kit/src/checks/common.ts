import type { CheckContext, CheckResult, Status } from '../model.ts';
import { thresholdFor } from '../thresholds.ts';

export type TextBox={selector:string;owner:string;box:{left:number;top:number;right:number;bottom:number};ancestors:{selector:string;allow:boolean}[]};

export function result(ctx: CheckContext, id: string, status: Status, items: unknown[] = [], reason?: string): CheckResult {
  return { id, status, thresholds: thresholdFor(id, ctx.options.thresholds), items, ...(reason ? { reason } : {}) };
}

export async function scanTextBoxes(page: CheckContext['session']['page']) {
  return page.evaluate(() => {
    const svgNS = 'http://www.w3.org/2000/svg';
    const selector = (e: Element): string => {
      if (e.id && document.querySelectorAll(`#${CSS.escape(e.id)}`).length === 1) return `#${CSS.escape(e.id)}`;
      if(e===document.documentElement)return 'html';
      const parts: string[] = [];
      for (let n: Element | null = e; n && n !== document.documentElement; n = n.parentElement) {
        let i = 1; for (let p = n.previousElementSibling; p; p = p.previousElementSibling) if (p.localName === n.localName) i++;
        parts.unshift(`${n.localName}:nth-of-type(${i})`);
      }
      return `html>${parts.join('>')}`;
    };
    const visible = (e: Element) => {
      if (e.closest('[data-rk-ignore]')) return false;
      const r = e.getBoundingClientRect(), s = getComputedStyle(e);
      for(let n:Element|null=e;n;n=n.parentElement)if(Number(getComputedStyle(n).opacity)===0)return false;
      const geometry=e.namespaceURI==='http://www.w3.org/2000/svg'&&['path','line','polyline','polygon','rect','circle','ellipse'].includes(e.localName);
      const stroked=geometry&&(r.width===0||r.height===0)&&s.stroke!=='none'&&parseFloat(s.strokeWidth)>0;
      return (r.width > 0 && r.height > 0 || stroked) && s.display !== 'none' && s.visibility !== 'hidden';
    };
    const rects = (nodes: Node[]) => {
      const out = nodes.flatMap(node => { const r = document.createRange(); r.selectNodeContents(node); return [...r.getClientRects()]; });
      if (!out.length) return null;
      return { left: Math.min(...out.map(r => r.left)), top: Math.min(...out.map(r => r.top)), right: Math.max(...out.map(r => r.right)), bottom: Math.max(...out.map(r => r.bottom)) };
    };
    const boxes: any[] = [];
    for (const e of document.querySelectorAll('*')) {
      if (!visible(e)) continue;
      const svgText = e.namespaceURI === svgNS && e.localName === 'text';
      if (svgText) {
        const spans = [...e.querySelectorAll('tspan')];
        const units = spans.length ? spans : [e];
        for (const unit of units) {
          const box = unit === e ? rects([...e.childNodes].filter(n => n.nodeType === Node.TEXT_NODE && n.textContent?.trim())) : (() => { const r = unit.getBoundingClientRect(); return { left: r.left, top: r.top, right: r.right, bottom: r.bottom }; })();
          if (box) boxes.push({ selector: selector(unit), owner: selector(e), box, ancestors: ancestorData(unit) });
        }
      } else {
        const nodes = [...e.childNodes].filter(n => n.nodeType === Node.TEXT_NODE && n.textContent?.trim());
        const box = nodes.length ? rects(nodes) : null;
        if (box) boxes.push({ selector: selector(e), owner: selector(e), box, ancestors: ancestorData(e) });
      }
    }
    function ancestorData(e: Element) {
      const rows = []; for (let n: Element | null = e; n; n = n.parentElement) rows.push({ selector: selector(n), allow: n.hasAttribute('data-rk-allow-overlap') }); return rows;
    }
    return boxes;
  });
}

export async function stageRect(page: CheckContext['session']['page'],svgInput=false,fullDocument=false) {
  return page.evaluate(({useSvg,fullDocument}:{useSvg:boolean;fullDocument:boolean}) => {
    const el = document.querySelector('[data-rk-stage]') ?? (useSvg?document.querySelector('body > svg'):null);
    const r = el?.getBoundingClientRect();
    const bottom = fullDocument ? Math.max(innerHeight, document.documentElement.scrollHeight, document.body?.scrollHeight ?? 0) : innerHeight;
    return r ? { left: r.left, top: r.top, right: r.right, bottom: r.bottom } : { left: 0, top: 0, right: innerWidth, bottom };
  },{useSvg:svgInput,fullDocument});
}
