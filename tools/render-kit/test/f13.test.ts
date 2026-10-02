import { test } from 'node:test';
import assert from 'node:assert/strict';
import { chmod, readFile, writeFile } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { writeBrief } from '../src/brief.ts';
import { pngSize, report, temp } from './helpers.ts';

test('F13 brief keeps each group heading with its questions', async () => {
  const d = await temp(), questions = join(d, 'questions.md');
  await writeFile(questions, '# First group\n- First question?\n\n# Second group\n- Second question?\n');
  await writeBrief(join(d, 'brief'), questions, 'Grouped review', [{ label: 'Ready', input: 'ready.html', report: { checks: [], outputs: {} }, files: ['render.png'] }]);
  const brief = await readFile(join(d, 'brief', 'brief.md'), 'utf8');
  const firstHeading = brief.indexOf('# First group'), firstQuestion = brief.indexOf('Q1. First question?');
  const secondHeading = brief.indexOf('# Second group'), secondQuestion = brief.indexOf('Q2. Second question?');
  assert.ok(firstHeading < firstQuestion && firstQuestion < secondHeading && secondHeading < secondQuestion, brief);
});

test('F13 default capture includes full document height while --height stays fixed', { timeout: 90000 }, async () => {
  const d = await temp(), page = join(d, 'tall.html'), python = join(d, 'python3');
  await writeFile(page, '<!doctype html><html><body style="margin:0"><main style="height:1400px;position:relative"><p style="position:absolute;top:1320px;font:24px sans-serif">Bottom marker</p></main></body></html>');
  await writeFile(python, `#!/usr/bin/env node
const {readFileSync}=require('node:fs'); let input='';
process.stdin.on('data',chunk=>input+=chunk);
process.stdin.on('end',()=>{
  const rows=JSON.parse(input), png=readFileSync(process.argv[4]), width=png.readUInt32BE(16), height=png.readUInt32BE(20);
  console.log(JSON.stringify(rows.map(row => row.box[0]<0 || row.box[1]<0 || row.box[2]>width || row.box[3]>height
    ? {selector:row.selector,incomplete:'text box outside capture'}
    : {selector:row.selector,text:row.text,background:'#ffffff',ratio:21,required:row.required})));
});
`);
  await chmod(python, 0o755);

  const automatic = await report(['check', page, '--checks', 'overflow,contrast', '--out-dir', join(d, 'automatic')], { PATH: `${d}:${process.env.PATH ?? ''}` });
  assert.equal(automatic.code, 0, automatic.stderr);
  assert.ok(automatic.data.checks.every((check: any) => check.status === 'pass'));
  assert.ok(!JSON.stringify(automatic.data.checks).includes('text box outside capture'));
  assert.equal((await pngSize(automatic.data.outputs.png)).height, 1400);

  const fixed = await report(['check', page, '--height', '900', '--checks', 'overflow', '--out-dir', join(d, 'fixed')]);
  assert.equal(fixed.code, 1, fixed.stderr);
  assert.equal(fixed.data.checks[0].status, 'fail');
  assert.ok(fixed.data.checks[0].items.some((item: any) => item.kind === 'offstage'));
  assert.equal((await pngSize(fixed.data.outputs.png)).height, 900);
});

test('F13 whole-stage focal skips empty outside-region measurements with a clear reason', async () => {
  const d = await temp(), page = join(d, 'whole-stage.html'), python = join(d, 'python3'), called = join(d, 'python-called');
  await writeFile(page, '<!doctype html><html><body style="margin:0"><main data-rk-stage data-rk-focal style="width:1920px;height:1080px;background:#789"></main></body></html>');
  await writeFile(python, `#!/bin/sh\nprintf called > '${called}'\nprintf 'ValueError: zero-size array to reduction operation minimum which has no identity\\n' >&2\nexit 1\n`);
  await chmod(python, 0o755);

  const result = await report(['check', page, '--checks', 'value', '--out-dir', join(d, 'checked')], {
    RK_COLOR_THEORY: resolve('test/fixtures/color-theory'),
    PATH: `${d}:${process.env.PATH ?? ''}`
  });
  assert.equal(result.code, 0, result.stderr);
  assert.equal(result.data.checks[0].status, 'incomplete');
  assert.match(result.data.checks[0].reason, /entire captured stage|no outside pixels/i);
  await assert.rejects(readFile(called));
});
