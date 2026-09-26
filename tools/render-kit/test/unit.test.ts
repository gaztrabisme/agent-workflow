import { test } from 'node:test';
import assert from 'node:assert/strict';
import { contrast, cvdDistance, oklab, parseHex } from '../src/color.ts';
import { scaleMap, parseMLPath } from '../src/geometry.ts';
import { wrapText } from '../src/text.ts';
import { checkExit } from '../src/report.ts';

test('OKLab white and WCAG black on white',()=>{assert.ok(Math.abs(oklab(parseHex('#ffffff'))[0]-1)<1e-4);assert.ok(Math.abs(oklab(parseHex('#ffffff'))[1])<1e-4);assert.ok(Math.abs(oklab(parseHex('#ffffff'))[2])<1e-4);assert.equal(contrast(parseHex('#000000'),parseHex('#ffffff')),21);});
test('deuteranopia red-green distance is calibrated',()=>{assert.ok(Math.abs(cvdDistance(parseHex('#d62728'),parseHex('#2ca02c'),'deuteranopia')-.039)<.002);});
test('linear scale supports a reversed range',()=>{assert.equal(scaleMap(5,{type:'linear',domain:[0,10],range:[100,0]}),50);});
test('absolute M/L parser preserves vertex order',()=>{assert.deepEqual(parseMLPath('M 1,2 L3,4 5 6'),[[1,2],[3,4],[5,6]]);assert.throws(()=>parseMLPath('M1 2 C3 4'));});
test('greedy wrapping uses the supplied measuring function',()=>{const out=wrapText('one two three',70,s=>s.length*10,20);assert.deepEqual(out.lines.map(x=>x.text),['one two','three']);assert.ok(out.lines.every(x=>x.width<=70));assert.equal(wrapText('oversize',20,s=>s.length*10,20).overflow,true);});
test('check exit codes cover fail, strict, skipped, incomplete, and n/a',()=>{
 assert.equal(checkExit([{id:'x',status:'pass',items:[],thresholds:{}}],false),0);assert.equal(checkExit([{id:'x',status:'fail',items:[],thresholds:{}}],false),1);
 for(const status of ['skipped','incomplete'] as const){assert.equal(checkExit([{id:'x',status,items:[],thresholds:{}}],false),0);assert.equal(checkExit([{id:'x',status,items:[],thresholds:{}}],true),1);}
 assert.equal(checkExit([{id:'x',status:'n/a',items:[],thresholds:{}}],true),0);
});
