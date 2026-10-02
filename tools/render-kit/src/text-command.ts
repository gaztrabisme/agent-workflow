import { readFile, mkdtemp, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import type { RunOptions, Session } from './model.ts';
import { prepare } from './render.ts';
import { wrapText, svgWrappedText } from './text.ts';

const familyOf=(font:string)=>font.match(/\d+(?:\.\d+)?px\s+(.+)$/)?.[1].split(',')[0].trim().replace(/^['"]|['"]$/g,'')??'';
async function sessionFor(font:string,text:string,fontFile?:string){
 const dir=await mkdtemp(join(tmpdir(),'rk-text-')),html=join(dir,'page.html');await writeFile(html,'<!doctype html><html lang="en"><title>Text measure</title><body></body></html>');
 const options:RunOptions={input:html,scale:1,at:0,settle:0,boot:0,media:'screen',timeout:30000,allowNetwork:false,pdf:false,strict:false,thresholds:{},expectedRequests:[]};
 const session=await prepare(options);
 try{
  const data=fontFile?(await readFile(fontFile)).toString('base64'):'';
  await session.page.evaluate(async ({font,text,data,ext})=>{
   const el=document.createElement('span');el.id='measure';el.textContent=text;el.style.cssText=`position:fixed;left:-10000px;top:0;white-space:pre;font:${font}`;document.body.append(el);
   if(data){const mime=ext==='woff2'?'font/woff2':ext==='woff'?'font/woff':ext==='otf'?'font/otf':'font/ttf';const face=new FontFace(font.match(/\d+(?:\.\d+)?px\s+(.+)$/)![1].split(',')[0].trim().replace(/^['"]|['"]$/g,''),`url(data:${mime};base64,${data})`);await face.load();document.fonts.add(face);}
   await document.fonts.load(font,text);
  },{font,text,data,ext:fontFile?.split('.').pop()?.toLowerCase()??''});
  const row=await session.page.evaluate(()=>{const e=document.querySelector('#measure')!,f=getComputedStyle(e).fontFamily.split(',')[0].trim().replace(/^['"]|['"]$/g,'');const c=document.createElement('canvas').getContext('2d')!;c.font=getComputedStyle(e).font;const m=c.measureText(e.textContent||'');return {family:f,font:c.font,width:m.width,ascent:m.actualBoundingBoxAscent,descent:m.actualBoundingBoxDescent,custom:[...document.fonts].some(x=>x.family.toLowerCase()===f.toLowerCase()&&x.status==='loaded'),generic:['serif','sans-serif','monospace','cursive','fantasy','system-ui','ui-serif','ui-sans-serif','ui-monospace','ui-rounded','math','emoji','fangsong'].includes(f.toLowerCase())};});
  const root=(await session.cdp.send('DOM.getDocument')).root.nodeId,node=await session.cdp.send('DOM.querySelector',{nodeId:root,selector:'#measure'}),fonts=(await session.cdp.send('CSS.getPlatformFontsForNode',{nodeId:node.nodeId})).fonts as {familyName:string;isCustomFont:boolean}[];
  const ok=row.generic||(row.custom?fonts.length>0&&fonts.every(f=>f.isCustomFont):fonts.length>0&&fonts.every(f=>f.familyName.toLowerCase()===row.family.toLowerCase()));
  if(!ok)throw new Error(`Font fallback: requested "${row.family}", actual ${fonts.map(f=>f.familyName).join(', ')||'unknown'}`);
  return {session,row};
 }catch(e){await session.stop();throw e;}
}

export async function textCommand(kind:'measure'|'wrap',font:string,text:string,width:number|undefined,opts:{lineHeight:number;maxLines?:number;format:'json'|'svg';x:number;y:number;fontFile?:string}){
 const {session,row}=await sessionFor(font,text,opts.fontFile);
 try{if(kind==='measure')return {value:{width:row.width,ascent:row.ascent,descent:row.descent,font:row.font},code:0};
  const size=Number(font.match(/(\d+(?:\.\d+)?)px/)?.[1]??16),wrapped=await session.page.evaluate(({fn,font,text,width,size,ratio,maxLines})=>{const wrap=new Function(`return (${fn})`)();const c=document.createElement('canvas').getContext('2d')!;c.font=font;return wrap(text,width,(s:string)=>c.measureText(s).width,size,ratio,maxLines);},{fn:wrapText.toString(),font,text,width,size,ratio:opts.lineHeight,maxLines:opts.maxLines});
  return {value:opts.format==='svg'?svgWrappedText(wrapped,font,opts.x,opts.y):wrapped,code:wrapped.overflow?1:0,raw:wrapped};
 }finally{await session.stop();}
}
