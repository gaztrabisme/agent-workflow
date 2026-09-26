import { spawn } from 'node:child_process';
import { AxeBuilder } from '@axe-core/playwright';
import type { CheckContext } from '../model.ts';
import { result, scanTextBoxes, stageRect } from './common.ts';
import { withAxePage } from './axe.ts';

function sample(png:string,rows:unknown[]){return new Promise<string>((resolve,reject)=>{const child=spawn('python3',['-c',sampler,png]);let out='',err='';child.stdout.on('data',(b:any)=>out+=b);child.stderr.on('data',(b:any)=>err+=b);child.stdin.on('error',()=>{});child.on('error',reject);child.on('close',(code:number|null)=>code===0?resolve(out):reject(new Error(err||`python exited ${code}`)));child.stdin.end(JSON.stringify(rows));});}
const sampler=`import sys,json,collections
import numpy as np
from PIL import Image
im=np.asarray(Image.open(sys.argv[1]).convert('RGB'),dtype=float)/255
rows=json.load(sys.stdin)
def lin(c): return np.where(c<=.04045,c/12.92,((c+.055)/1.055)**2.4)
def lab(c):
 r,g,b=lin(c).T
 l=np.cbrt(.4122214708*r+.5363325363*g+.0514459929*b);m=np.cbrt(.2119034982*r+.6806995451*g+.1073969566*b);s=np.cbrt(.0883024619*r+.2817188376*g+.6299787005*b)
 return np.stack([.2104542553*l+.793617785*m-.0040720468*s,1.9779984951*l-2.428592205*m+.4505937099*s,.0259040371*l+.7827717662*m-.808675766*s],axis=-1)
def lum(c): return lin(c)@np.array([.2126,.7152,.0722])
out=[]
for r in rows:
 x0,y0,x1,y1=[int(v) for v in r['box']]; crop=im[max(0,y0):min(im.shape[0],y1),max(0,x0):min(im.shape[1],x1)]
 if not crop.size: out.append({'selector':r['selector'],'incomplete':'text box outside capture'});continue
 fg=np.array(r['fg']); distance=np.linalg.norm(lab(crop.reshape(-1,3))-lab(fg.reshape(1,3))[0],axis=1);keep=distance>r['exclude']
 if not keep.any(): keep=distance>min(.01,r['exclude'])
 pixels=crop.reshape(-1,3)[keep]
 if not len(pixels): out.append({'selector':r['selector'],'incomplete':'no background pixels remain'});continue
 counts=collections.Counter(tuple((p*255).round().astype(int)) for p in pixels); bg=np.array(counts.most_common(1)[0][0])/255; share=counts.most_common(1)[0][1]/len(pixels)
 if share<r['min_share']: out.append({'selector':r['selector'],'incomplete':'background is not a dominant colour','share':share});continue
 a,b=sorted([float(lum(fg)),float(lum(bg))],reverse=True);out.append({'selector':r['selector'],'text':r['text'],'background':'#%02X%02X%02X'%tuple((bg*255).round().astype(int)),'ratio':(a+.05)/(b+.05),'required':r['required']})
print(json.dumps(out))`;

export async function run(ctx: CheckContext) {
  const boxes=await scanTextBoxes(ctx.session.page), stage=await stageRect(ctx.session.page,ctx.session.svgInput);
  const meta=await ctx.session.page.evaluate((rows:any[])=>rows.map(row=>{
    const e=document.querySelector(row.selector)!,s=getComputedStyle(e),svg=e.namespaceURI==='http://www.w3.org/2000/svg';
    const rgb=(s[svg?'fill':'color'].match(/[\d.]+/g)||[]).slice(0,3).map(Number);
    const size=parseFloat(s.fontSize),weight=parseInt(s.fontWeight)||400;
    return {selector:row.selector,box:[row.box.left,row.box.top,row.box.right,row.box.bottom],fg:rgb.map((x:number)=>x/255),text:s.color,required:size>=24||(size>=18.66&&weight>=700)?3:4.5};
  }),boxes);
  const rows=meta.map((r:any)=>({...r,exclude:ctx.options.thresholds['contrast.text_exclusion']??.1,min_share:ctx.options.thresholds['contrast.min_background_share']??.3,box:r.box.map((n:number,i:number)=>Math.round((n-(i%2?stage.top:stage.left))*ctx.options.scale))}));
  try {
    const measured=JSON.parse(await sample(ctx.png,rows)) as any[], failures=measured.filter(x=>x.ratio!==undefined&&x.ratio<x.required), incomplete=measured.filter(x=>x.incomplete);
    const axe=await withAxePage(ctx.session,page=>new AxeBuilder({page}).exclude('[data-rk-ignore]').withRules(['color-contrast']).analyze());
    const raw=axe.incomplete.flatMap(v=>v.nodes.map(n=>({rule:v.id,selectors:n.target,detail:'axe-core could not determine contrast'})));
    const axeIncomplete=await ctx.session.page.evaluate((rows:any[])=>rows.filter(row=>row.selectors.some((selector:string)=>{const e=document.querySelector(selector);if(!e)return true;const svg=e.namespaceURI==='http://www.w3.org/2000/svg';return !(svg&&(e.localName==='text'||e.localName==='tspan')||[...e.childNodes].some(n=>n.nodeType===Node.TEXT_NODE&&n.textContent?.trim()));})),raw);
    const rawFailures=axe.violations.flatMap(v=>v.nodes.map(n=>({rule:v.id,impact:v.impact,selectors:n.target,detail:n.failureSummary||v.help})));
    const axeFailures=await ctx.session.page.evaluate((rows:any[])=>rows.filter(row=>row.selectors.some((selector:string)=>{const e=document.querySelector(selector);return !!e&&e.namespaceURI!=='http://www.w3.org/2000/svg';})),rawFailures);
    const items=[...failures,...axeFailures,...incomplete,...axeIncomplete];
    return result(ctx,'contrast',failures.length||axeFailures.length?'fail':incomplete.length||axeIncomplete.length?'incomplete':'pass',items,incomplete.length||axeIncomplete.length?'some text backgrounds could not be measured':undefined);
  } catch(e) { return result(ctx,'contrast','incomplete',[],`pixel contrast measurement unavailable: ${String((e as Error).message).slice(-250)}`); }
}
