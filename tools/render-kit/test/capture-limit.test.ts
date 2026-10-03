import { test } from 'node:test';
import assert from 'node:assert/strict';
import { writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { pngSize, report, temp } from './helpers.ts';

const stagePage = (height:number) => `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Capture limit stage</title><style>html,body{margin:0;width:1px;height:1px}[data-rk-stage]{width:1px;height:${height}px;background:white}</style></head><body><main data-rk-stage></main></body></html>`;
const page = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Capture limit page</title><style>html,body{margin:0;height:1px}</style></head><body></body></html>';
const inlineSvgPage = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Inline SVG page</title></head><body><svg width="1" height="1" xmlns="http://www.w3.org/2000/svg"></svg></body></html>';
const tallPage = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Tall document page</title><style>html,body{margin:0}body{height:16385px}</style></head><body></body></html>';

test('overflow reports the 16,384 px stage and page capture limit', { timeout: 90000 }, async () => {
  const d = await temp(), exact = join(d, 'exact.html'), tall = join(d, 'tall.html'), wide = join(d, 'wide.html'), documentTall = join(d, 'document-tall.html'), inlineSvg = join(d, 'inline-svg.html');
  await Promise.all([
    writeFile(exact, stagePage(16384)),
    writeFile(tall, stagePage(16385)),
    writeFile(wide, page),
    writeFile(documentTall, tallPage),
    writeFile(inlineSvg, inlineSvgPage),
  ]);

  const atLimit = await report(['check', exact, '--width', '1', '--checks', 'overflow', '--out-dir', join(d, 'exact')]);
  assert.equal(atLimit.code, 0, atLimit.stderr);
  assert.deepEqual(atLimit.data.checks[0].items, []);

  const overStage = await report(['check', tall, '--width', '1', '--checks', 'overflow', '--out-dir', join(d, 'tall')]);
  assert.equal(overStage.code, 1, overStage.stderr);
  const stageItem = overStage.data.checks[0].items.find((item:any) => item.kind === 'capture-limit');
  assert.equal(stageItem.target, 'first data-rk-stage');
  assert.match(stageItem.message, /height exceeds Chromium's 16,384 px/);
  assert.deepEqual(await pngSize(join(d, 'tall', 'render.png')), { width: 1, height: 16384 });

  const overPage = await report(['check', wide, '--width', '16385', '--height', '1', '--checks', 'overflow', '--out-dir', join(d, 'wide')]);
  assert.equal(overPage.code, 1, overPage.stderr);
  const pageItem = overPage.data.checks[0].items.find((item:any) => item.kind === 'capture-limit');
  assert.equal(pageItem.target, 'document page');
  assert.match(pageItem.message, /16,384 px/);
  assert.deepEqual(await pngSize(join(d, 'wide', 'render.png')), { width: 16384, height: 1 });

  const inlineSvgPageCheck = await report(['check', inlineSvg, '--width', '16385', '--height', '1', '--checks', 'overflow', '--out-dir', join(d, 'inline-svg')]);
  assert.equal(inlineSvgPageCheck.code, 1, inlineSvgPageCheck.stderr);
  const inlineSvgItem = inlineSvgPageCheck.data.checks[0].items.find((item:any) => item.kind === 'capture-limit');
  assert.equal(inlineSvgItem.target, 'document page');
  assert.match(inlineSvgItem.message, /16,384 px/);

  const overPageHeight = await report(['check', documentTall, '--width', '1', '--checks', 'overflow', '--out-dir', join(d, 'document-tall')]);
  assert.equal(overPageHeight.code, 1, overPageHeight.stderr);
  const tallPageItem = overPageHeight.data.checks[0].items.find((item:any) => item.kind === 'capture-limit');
  assert.equal(tallPageItem.target, 'document page');
  assert.match(tallPageItem.message, /16,384 px/);
  assert.deepEqual(await pngSize(join(d, 'document-tall', 'render.png')), { width: 1, height: 16384 });

  const fixedPage = await report(['check', documentTall, '--width', '1', '--height', '1', '--checks', 'overflow', '--out-dir', join(d, 'fixed-page')]);
  assert.equal(fixedPage.code, 1, fixedPage.stderr);
  assert.ok(fixedPage.data.checks[0].items.some((item:any) => item.kind === 'offstage'));
  assert.ok(fixedPage.data.checks[0].items.every((item:any) => item.kind !== 'capture-limit'));
});
