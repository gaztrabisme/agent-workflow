import { readFile } from 'node:fs/promises';
import { mkdtemp } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import type { RunOptions } from './model.ts';
import { checkInput } from './runner.ts';

type Expectation={input:string;fail:string[]};
export async function selftest(strict=false){
 const expected=JSON.parse(await readFile('samples/expectations.json','utf8')) as Expectation[],rows:any[]=[];
 for(const sample of expected){
  const dir=await mkdtemp(join(tmpdir(),'rk-selftest-'));
  const options:RunOptions={input:resolve('samples',sample.input),scale:1,at:'end',settle:10000,boot:100,media:'screen',timeout:30000,allowNetwork:false,pdf:true,strict:false,outDir:dir,thresholds:{},expectedRequests:[]};
  const {report}=await checkInput(options),actual=report.checks.filter((c:any)=>c.status==='fail').map((c:any)=>c.id),skipped=report.checks.filter((c:any)=>c.status==='skipped').map((c:any)=>c.id);
  const unmet=sample.fail.filter(id=>skipped.includes(id)),expectedFailures=sample.fail.filter(id=>!unmet.includes(id)),unexpected=actual.filter((id:string)=>!expectedFailures.includes(id)),missing=expectedFailures.filter(id=>!actual.includes(id));
  rows.push({input:sample.input,expected:sample.fail,actual,skipped,unmet,unexpected,missing,ok:!unexpected.length&&!missing.length&&(!strict||!skipped.length&&!unmet.length)});
 }
 const ok=rows.every(r=>!r.unexpected.length&&!r.missing.length&&(!strict||!r.skipped.length&&!r.unmet.length));
 return {samples:rows,ok,code:ok?0:1};
}
