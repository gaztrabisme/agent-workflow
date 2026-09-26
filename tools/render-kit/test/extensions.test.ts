import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { createServer, type AddressInfo } from 'node:net';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { prepare } from '../src/render.ts';
import { rk, run, temp, report } from './helpers.ts';

const base={scale:1,settle:10000,boot:100,media:'screen' as const,timeout:30000,allowNetwork:false,pdf:false,strict:false,thresholds:{}};
test('AT23 boot and runFor advance every requestAnimationFrame',{timeout:30000},async()=>{for(const [at,want] of [[1000,110],[0,10]] as const){const session=await prepare({...base,input:'samples/good/raf.html',at});try{const x=await session.page.locator('#square').evaluate((e:any)=>parseFloat(getComputedStyle(e).left));assert.ok(Math.abs(x-want)<=1);assert.equal(await session.page.locator('#placeholder').count(),0);}finally{await session.stop();}}});
test('AT24 PDF follows screen or print media',{timeout:60000},async()=>{const d=await temp();for(const [media,has] of [['screen',true],['print',false]] as const){const p=join(d,`${media}.pdf`),r=await rk(['render','samples/good/print-media.html','--out',p,'--media',media]);assert.equal(r.code,0,r.stderr);const text=await run('pdftotext',[p,'-']);assert.equal(text.stdout.includes('screen-only'),has);}});
test('AT25 CVD threshold override is reported',async()=>{const r=await report(['check','samples/bad/cvd.svg','--checks','cvd','--threshold','cvd.min_distance=0.03','--out-dir',join(await temp(),'out')]);assert.equal(r.code,0,r.stderr);assert.equal(r.data.checks[0].status,'pass');assert.equal(r.data.checks[0].thresholds.min_distance,.03);});
test('AT26 dense grid checks in under 60 seconds',{timeout:65000},async()=>{const start=Date.now(),r=await rk(['check','samples/good/dense.svg','--out-dir',join(await temp(),'out')]);assert.equal(r.code,0,r.stderr);assert.ok(Date.now()-start<60000);});
test('AT27 local URL works and URL root is refused',{timeout:60000},async()=>{const probe=createServer();await new Promise<void>(ok=>probe.listen(0,'127.0.0.1',ok));const port=(probe.address() as AddressInfo).port;await new Promise<void>(ok=>probe.close(()=>ok()));const child=spawn('python3',['-m','http.server',String(port),'--bind','127.0.0.1','--directory','samples/good'],{stdio:'ignore'});const url=`http://127.0.0.1:${port}/slide.html`;
 try{let ready=false;for(let i=0;i<50&&!ready;i++){try{ready=(await fetch(url)).ok;}catch{}if(!ready)await new Promise(r=>setTimeout(r,100));}assert.ok(ready,'python server did not start');const local=await report(['check','samples/good/slide.html','--out-dir',join(await temp(),'file')]),served=await report(['check',url,'--out-dir',join(await temp(),'url')]);assert.equal(local.code,0,local.stderr);assert.equal(served.code,0,served.stderr);assert.deepEqual(served.data.checks.map((c:any)=>c.status),local.data.checks.map((c:any)=>c.status));const refused=await rk(['check',url,'--root','samples/good']);assert.equal(refused.code,2);assert.match(refused.stdout,/root/i);}finally{child.kill();await new Promise<void>(ok=>child.once('exit',()=>ok()));}});
