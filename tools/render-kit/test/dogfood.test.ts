import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile, writeFile } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { prepare } from '../src/render.ts';
import { report, rk, run, temp } from './helpers.ts';

test('AT31 reference palette passes the default CVD threshold',{timeout:60000},async()=>{
  const r=await report(['check','samples/good/cvd-12.svg','--out-dir',join(await temp(),'out')]);
  assert.equal(r.code,0,r.stderr);const cvd=r.data.checks.find((c:any)=>c.id==='cvd');
  assert.equal(cvd.status,'pass');assert.equal(cvd.thresholds.min_distance,.06);assert.equal(cvd.items.length,4);
});

test('AT32 horizontal stroked series are visible to CVD and fidelity',{timeout:60000},async()=>{
  const d=await temp(),r=await report(['check','samples/bad/horizontal-series.svg','--out-dir',join(d,'out')]);
  assert.equal(r.code,1,r.stderr);assert.deepEqual(r.data.checks.filter((c:any)=>c.status==='fail').map((c:any)=>c.id),['cvd']);
  const cvd=r.data.checks.find((c:any)=>c.id==='cvd');assert.equal(cvd.items.length,4);
  assert.ok(cvd.items.some((item:any)=>item.vision==='deuteranopia'&&Math.abs(item.distance-.039)<.002));
  assert.equal(r.data.checks.find((c:any)=>c.id==='fidelity').status,'pass');
  const session=await prepare({input:resolve('samples/bad/horizontal-series.svg'),scale:1,at:'end',settle:10000,boot:100,media:'screen',timeout:30000,allowNetwork:false,pdf:false,strict:false,thresholds:{},expectedRequests:[]});
  try{const boxes=await session.page.locator('[data-rk-series]').evaluateAll((els:any[])=>els.map(e=>e.getBoundingClientRect().height));assert.deepEqual(boxes,[0,0]);}finally{await session.stop();}
});

test('AT33 value thresholds, large focal vision question, and achromatic data graphic',{timeout:120000},async()=>{
  const d=await temp();
  const fixture={RK_COLOR_THEORY:resolve('test/fixtures/color-theory')};
  const threshold=await report(['check','samples/bad/value.html','--checks','value','--threshold','value.min_edge_share=0.1','--out-dir',join(d,'threshold')],fixture);
  assert.equal(threshold.code,0,threshold.stderr);assert.equal(threshold.data.checks[0].status,'pass');
  assert.equal(threshold.data.checks[0].thresholds.min_edge_share,.1);

  const graphic=await readFile('samples/good/data-graphic.svg','utf8'),plain=join(d,'large-focal.svg');
  await writeFile(plain,graphic.replace('data-rk-focal="data-graphic"','data-rk-focal'));
  const large=await report(['check',plain,'--checks','value','--out-dir',join(d,'large')],fixture);
  assert.equal(large.data.checks[0].status,'incomplete');
  assert.ok(large.data.checks[0].items.some((item:any)=>item.question?.includes('focal area')));

  const data=await report(['check','samples/good/data-graphic.svg','--checks','value','--threshold','value.min_edge_share=100','--threshold','value.data_graphic_min_edge_share=0.5','--out-dir',join(d,'graphic')],fixture);
  assert.equal(data.data.checks[0].status,'pass');assert.equal(data.data.checks[0].thresholds.data_graphic_min_edge_share,.5);
  const chroma=data.data.checks[0].items.find((item:any)=>item.check==='chroma'&&item.test==='T5');
  assert.ok(chroma);assert.equal(chroma.status,'n/a');assert.match(chroma.source_result,/T5 CHECK/);assert.match(chroma.result,/T5 N\/A/);
});

test('AT34 brief includes PDF and a PNG render for every PDF page',{timeout:120000},async()=>{
  const d=await temp(),r=await rk(['brief','samples/good/pdf-pages.html','--questions','questions/slide.md','--out-dir',d,'--pdf']);
  assert.equal(r.code,0,r.stderr);const md=await readFile(join(d,'brief.md'),'utf8');
  assert.match(md,/render\.pdf/);assert.match(md,/render-page-1\.png/);assert.match(md,/render-page-2\.png/);
  assert.match(md,/PDF and page images show the print output/);
  for(const name of ['render.pdf','render-page-1.png','render-page-2.png'])assert.ok(await readFile(join(d,name)),name);
  assert.match((await run('pdfinfo',[join(d,'render.pdf')])).stdout,/Pages:\s+2/);
});
