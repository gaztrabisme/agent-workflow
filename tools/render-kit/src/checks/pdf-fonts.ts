import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import type { CheckContext } from '../model.ts';
import { result } from './common.ts';

const exec = promisify(execFile);
export async function run(ctx: CheckContext) {
  if (!ctx.pdf) return result(ctx,'pdf-fonts','n/a',[],'no PDF produced');
  try {
    const {stdout}=await exec('pdffonts',[ctx.pdf],{timeout:10000});
    const items=String(stdout).split(/\r?\n/).slice(2).filter((x:string)=>x.trim()).map((line:string)=>{
      const m=line.match(/^(.*?)\s+(Type 3|CID Type 0C|CID Type 0|CID TrueType|TrueType|Type 1C|Type 1|Type 0)\s+/),tail=line.trim().split(/\s+/);
      return m?{font:m[1].trim(),type:m[2],embedded:tail[tail.length-5]}:null;
    }).filter((x:any):x is {font:string;type:string;embedded:string}=>!!x);
    const bad=items.filter(x=>x.type.includes('Type 3')||x.embedded==='no');
    return result(ctx,'pdf-fonts',bad.length?'fail':'pass',bad);
  } catch(e) { return result(ctx,'pdf-fonts','skipped',[],`pdffonts unavailable: ${String((e as Error).message).slice(-250)}`); }
}
