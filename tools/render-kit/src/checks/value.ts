import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { mkdtemp, access } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import type { CheckContext } from '../model.ts';
import { result } from './common.ts';

const exec = promisify(execFile);
export async function run(ctx: CheckContext) {
  const focal=ctx.session.page.locator('[data-rk-focal]').first();
  if(!(await focal.count())) return result(ctx,'value','n/a',[],'no focal element');
  const box = await focal.boundingBox();
  if (!box) return result(ctx,'value','n/a',[],'no focal element');
  const stage = await ctx.session.page.evaluate((svgInput:boolean) => { const r=(document.querySelector('[data-rk-stage]')??(svgInput?document.querySelector('body > svg'):null))?.getBoundingClientRect();return {x:r?.x??0,y:r?.y??0}; },ctx.session.svgInput);
  const x0=Math.round((box.x-stage.x)*ctx.options.scale), y0=Math.round((box.y-stage.y)*ctx.options.scale), x1=Math.round((box.x+box.width-stage.x)*ctx.options.scale), y1=Math.round((box.y+box.height-stage.y)*ctx.options.scale);
  const root=process.env.RK_COLOR_THEORY??resolve('../skills/color-theory'), script=join(root,'scripts','checks.py');
  const temp=await mkdtemp(join(tmpdir(),'rk-value-'));
  try { await access(script); } catch { return result(ctx,'value','skipped',[],`color-theory script not found: ${script}`); }
  const all:unknown[]=[], errors:string[]=[];
  for(const mode of ['value','chroma']) try {
    const args=[script,mode,ctx.png,'--focal',`${x0},${y0},${x1},${y1}`];if(mode==='value')args.push('--out',temp);
    const {stdout}=await exec('python3',args,{timeout:30000});
    const lines=String(stdout).split(/\r?\n/), items=lines.filter((line:string)=>/^T\d+ (?:PASS|FAIL)\b/.test(line));
    if(!items.length)errors.push(`${mode}: ${stdout.slice(-300)}`);
    for(const line of items){const idx=lines.indexOf(line);all.push({test:line.split(' ')[0],detail:lines.slice(Math.max(0,idx-2),idx).join(' '),result:line});}
  } catch(e) { errors.push(`${mode}: ${String((e as any).stderr??e).slice(-300)}`); }
  if(all.some((x:any)=>x.result.includes('FAIL')))return result(ctx,'value','fail',all);
  return errors.length?result(ctx,'value','skipped',all,errors.join(' | ').slice(-300)):result(ctx,'value','pass',all);
}
