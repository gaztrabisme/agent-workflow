import type { CheckContext } from '../model.ts';
import { cvdDistance, parseHex } from '../color.ts';
import { result } from './common.ts';

export async function run(ctx: CheckContext) {
  const groups = await ctx.session.page.evaluate(() => {
    const map = new Map<string, Map<string, number>>();
    for (const e of document.querySelectorAll('[data-rk-series]')) {
      const b=e.getBoundingClientRect(),style=getComputedStyle(e);let hidden=false;for(let n:Element|null=e;n;n=n.parentElement)if(Number(getComputedStyle(n).opacity)===0)hidden=true;
      if (e.closest('[data-rk-ignore]')||b.width===0||b.height===0||style.display==='none'||style.visibility==='hidden'||hidden) continue;
      const name = e.getAttribute('data-rk-series')!, s = style, color = s.fill !== 'none' ? s.fill : s.stroke;
      const counts = map.get(name) ?? new Map<string, number>(); counts.set(color, (counts.get(color) ?? 0) + 1); map.set(name, counts);
    }
    return [...map].map(([name, colors]) => [name, [...colors].sort((a,b)=>b[1]-a[1])[0][0]]);
  }) as [string, string][];
  if (groups.length < 2) return result(ctx, 'cvd', 'n/a', [], 'fewer than two declared series');
  const series = groups.map(([name, color]) => ({ name, color, rgb: color.match(/\d+(?:\.\d+)?/g)?.slice(0,3).map(Number).map(n=>n/255) ?? parseHex(color) }));
  const limit = ctx.options.thresholds['cvd.min_distance'] ?? 0.06, items: unknown[] = [], visions = ['normal','protanopia','deuteranopia','tritanopia'];
  for (const vision of visions) {
    let closest = { distance: Infinity, pair: [] as string[] };
    for (let i=0;i<series.length;i++) for (let j=i+1;j<series.length;j++) {
      const d = cvdDistance(series[i].rgb as [number,number,number], series[j].rgb as [number,number,number], vision);
      if (d < closest.distance) closest = { distance:d, pair:[series[i].name,series[j].name] };
    }
    items.push({ vision, pair:closest.pair, distance:Number(closest.distance.toFixed(4)), required:limit });
  }
  return result(ctx, 'cvd', items.some((i:any)=>i.distance<limit) ? 'fail' : 'pass', items);
}
