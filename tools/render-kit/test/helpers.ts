import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { mkdtemp, readFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const exec=promisify(execFile);
export async function run(command:string,args:string[],env?:Record<string,string|undefined>){
 try{const r=await exec(command,args,{encoding:'utf8',timeout:240000,maxBuffer:32*1024*1024,env:{...process.env,...env}});return {code:0,stdout:String(r.stdout),stderr:String(r.stderr)};}
 catch(e:any){return {code:typeof e.code==='number'?e.code:2,stdout:String(e.stdout??''),stderr:String(e.stderr??e.message??e)};}
}
export const rk=(args:string[],env?:Record<string,string|undefined>)=>run('./bin/rk',args,env);
export const temp=()=>mkdtemp(join(tmpdir(),'rk-test-'));
export async function pngSize(path:string){const b=await readFile(path);return {width:b.readUInt32BE(16),height:b.readUInt32BE(20)};}
export async function report(args:string[],env?:Record<string,string|undefined>){const r=await rk(args,env);return { ...r, data:r.stdout.trim().startsWith('{')?JSON.parse(r.stdout):null };}
