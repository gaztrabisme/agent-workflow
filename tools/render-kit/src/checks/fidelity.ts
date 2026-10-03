import type { CheckContext, Scale } from '../model.ts';
import { parseMLPath, scaleMap } from '../geometry.ts';
import { result } from './common.ts';

type Raw = { selector:string; tag:string; attrs:Record<string,string|null>; points:number[][]; matrix:number[]; screen:number[]; path:string; scales:Record<string,{type:string|null;domain:string|null;range:string|null}> };
const nums=(s:string|null)=>s===null?[]:s.split(/[\s,]+/).map(Number);
const point=(p:number[],m:number[])=>[m[0]*p[0]+m[2]*p[1]+m[4],m[1]*p[0]+m[3]*p[1]+m[5]];
const screenPoint=(p:number[],m:number[])=>[m[0]*p[0]+m[2]*p[1]+m[4],m[1]*p[0]+m[3]*p[1]+m[5]];

export async function run(ctx:CheckContext){
 const raw=await ctx.session.page.evaluate(()=>[...document.querySelectorAll('[data-rk-chart] [data-rk-mark]')].filter(e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);let hidden=false;for(let n:Element|null=e;n;n=n.parentElement)if(Number(getComputedStyle(n).opacity)===0)hidden=true;const geometry=e.namespaceURI==='http://www.w3.org/2000/svg'&&['path','line','polyline','polygon','rect','circle','ellipse'].includes(e.localName),stroked=geometry&&(r.width===0||r.height===0)&&s.stroke!=='none'&&parseFloat(s.strokeWidth)>0;return !e.closest('[data-rk-ignore]')&&(r.width>0&&r.height>0||stroked)&&s.display!=='none'&&s.visibility!=='hidden'&&!hidden;}).map(e=>{
  const root=e.closest('[data-rk-chart]') as SVGGraphicsElement,mark=e as SVGGraphicsElement,rm=root.getCTM()!,em=mark.getCTM()!,m=rm.inverse().multiply(em),s=root.getScreenCTM()!,a:Record<string,string|null>={};
  for(const k of ['x','y','x0','y0','points'])a[`data-rk-${k}`]=e.getAttribute(`data-rk-${k}`);
  let p:number[][]=[];if(e.localName==='rect'){const x=Number(e.getAttribute('x')||0),y=Number(e.getAttribute('y')||0),w=Number(e.getAttribute('width')||0),h=Number(e.getAttribute('height')||0);p=a['data-rk-y']!==null?[[x+w/2,y],[x+w/2,y+h]]:[[x,y+h/2],[x+w,y+h/2]];}
  if(e.localName==='circle'||e.localName==='ellipse')p=[[Number(e.getAttribute('cx')||0),Number(e.getAttribute('cy')||0)]];
  if(e.localName==='polyline')p=[...(e as SVGPolylineElement).points].map(q=>[q.x,q.y]);
  const selector=e.id&&document.querySelectorAll(`#${CSS.escape(e.id)}`).length===1?`#${CSS.escape(e.id)}`:`html>${[...function*(n:Element){for(;n&&n!==document.documentElement;n=n.parentElement!){let i=1;for(let p=n.previousElementSibling;p;p=p.previousElementSibling)if(p.localName===n.localName)i++;yield `${n.localName}:nth-of-type(${i})`;}}(e)].reverse().join('>')}`;
  return {selector,tag:e.localName,attrs:a,points:p,matrix:[m.a,m.b,m.c,m.d,m.e,m.f],screen:[s.a,s.b,s.c,s.d,s.e,s.f],path:e.localName==='path'?e.getAttribute('d')||'':'',scales:{x:{type:root.getAttribute('data-rk-x-scale'),domain:root.getAttribute('data-rk-x-domain'),range:root.getAttribute('data-rk-x-range')},y:{type:root.getAttribute('data-rk-y-scale'),domain:root.getAttribute('data-rk-y-domain'),range:root.getAttribute('data-rk-y-range')}}};
 })) as Raw[];
 if(!raw.length)return result(ctx,'fidelity','n/a',[],'no chart marks');
 const tol=ctx.options.thresholds['fidelity.tolerance_px']??.5,items:any[]=[],incomplete:any[]=[];
 for(const mark of raw){
  let actual=mark.points.map(p=>point(p,mark.matrix)),data:number[][]=[],axes:string[]=[];
  if(mark.tag==='rect'){const axis=mark.attrs['data-rk-y']!==null?'y':mark.attrs['data-rk-x']!==null?'x':'';if(!axis)continue;axes=[axis];const value=Number(mark.attrs[`data-rk-${axis}`]),sc=mark.scales[axis],dom=nums(sc.domain);data=[[value],[Number(mark.attrs[`data-rk-${axis}0`]??(dom[0]<=0&&dom[1]>=0?0:Math.min(...dom)))]];}
  else if(mark.tag==='circle'||mark.tag==='ellipse'){axes=['x','y'].filter(a=>mark.attrs[`data-rk-${a}`]!==null);if(!axes.length)continue;data=[[]];}
  else {try{if(mark.tag==='path')actual=parseMLPath(mark.path).map(p=>point(p,mark.matrix));const values=nums(mark.attrs['data-rk-points']);data=values.reduce<number[][]>((a,n,i)=>{if(i%2===0)a.push([n]);else a[a.length-1].push(n);return a;},[]);}catch{incomplete.push({selector:mark.selector,detail:'curved path not checked'});continue;}axes=['x','y'];}
  let missing=false;const mapped:Record<string,(v:number)=>number|undefined>={};
  for(const axis of axes){const sc=mark.scales[axis],domain=nums(sc.domain),range=nums(sc.range),attr=mark.attrs[`data-rk-${axis}`];
   if(mark.tag==='rect'||mark.tag==='circle'||mark.tag==='ellipse'){if(attr===null)continue;}
   else if(mark.tag!=='rect'&&mark.tag!=='circle'&&mark.tag!=='ellipse'&&mark.attrs['data-rk-points']===null){items.push({selector:mark.selector,detail:'missing data-rk-points'});missing=true;break;}
   if(!sc.type||domain.length!==2||range.length!==2){items.push({selector:mark.selector,detail:'missing scale'});missing=true;break;}
   if(sc.type==='band'){mapped[axis]=()=>undefined;continue;}if(sc.type!=='linear'){incomplete.push({selector:mark.selector,detail:'scale type not supported'});missing=true;break;}
   const scale:Scale={type:sc.type,domain,range};mapped[axis]=(v:number)=>scaleMap(v,scale);
  }
  if(missing)continue;
  let expected:number[][]=[];
  if(mark.tag==='rect'){const axis=axes[0],val=data.map(x=>mapped[axis]!(x[0]));expected=actual.map((p,i)=>axis==='x'?[val[i]??p[0],p[1]]:[p[0],val[i]??p[1]]);}
  else if(mark.tag==='circle'||mark.tag==='ellipse'){expected=actual.map(p=>[mapped.x?.(Number(mark.attrs['data-rk-x']))??p[0],mapped.y?.(Number(mark.attrs['data-rk-y']))??p[1]]);}
  else expected=data.map((p,i)=>[mapped.x?.(p[0])??actual[i]?.[0],mapped.y?.(p[1])??actual[i]?.[1]]);
  const diffs=expected.map((p,i)=>{const a=screenPoint(p,mark.screen),b=screenPoint(actual[i]??[NaN,NaN],mark.screen);return Math.hypot(a[0]-b[0],a[1]-b[1]);});
  if(mark.tag==='rect'&&diffs.length===2){const dist=(a:number[],b:number[])=>Math.hypot(a[0]-b[0],a[1]-b[1]),e=expected.map(p=>screenPoint(p,mark.screen)),a=actual.map(p=>screenPoint(p,mark.screen));if(dist(e[0],a[1])+dist(e[1],a[0])<diffs[0]+diffs[1])diffs.splice(0,2,dist(e[0],a[1]),dist(e[1],a[0]));}
  if(actual.length!==expected.length||diffs.some(d=>d>tol))items.push({selector:mark.selector,expected,actual,difference_px:diffs});
 }
 return result(ctx,'fidelity',items.length?'fail':incomplete.length?'incomplete':'pass',[...items,...incomplete],incomplete.length?`${incomplete.length} mark(s) could not be checked`:undefined);
}
