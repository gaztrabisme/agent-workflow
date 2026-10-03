#!/usr/bin/env node
// Read layout boxes from the same prepared Chromium page used by render-kit.
import { parseArgs } from 'node:util';
import { resolve, join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { writeFile } from 'node:fs/promises';

const { values, positionals } = parseArgs({ args: process.argv.slice(2), allowPositionals: true,
  options: { 'render-kit': { type: 'string' }, out: { type: 'string' }, width: { type: 'string' },
    height: { type: 'string' }, scale: { type: 'string' }, at: { type: 'string' }, settle: { type: 'string' },
    boot: { type: 'string' }, root: { type: 'string' }, 'wait-for': { type: 'string' },
    timeout: { type: 'string' }, 'allow-network': { type: 'boolean' } } });
if (positionals.length !== 1 || !values['render-kit']) throw new Error('Usage: measure_boxes.mjs input.html|svg --render-kit DIR [--out boxes.json] [render options]');
const root = resolve(values['render-kit']);
const { runOptions } = await import(pathToFileURL(join(root, 'src/args.ts')));
const { prepare } = await import(pathToFileURL(join(root, 'src/render.ts')));
const options = await runOptions(positionals[0], { width: values.width, height: values.height,
  scale: values.scale, at: values.at, settle: values.settle, boot: values.boot, root: values.root,
  'wait-for': values['wait-for'], timeout: values.timeout, 'allow-network': values['allow-network'] });
const session = await prepare(options);
try {
  const data = await session.page.evaluate((svgInput) => {
    const stage = document.querySelector('[data-rk-stage]') ?? (svgInput ? document.querySelector('body > svg') : null);
    const r = stage?.getBoundingClientRect() ?? { x: 0, y: 0, right: innerWidth, bottom: innerHeight, width: innerWidth, height: innerHeight };
    const left = Math.max(0, r.x), top = Math.max(0, r.y);
    const width = Math.min(innerWidth, r.right) - left, height = Math.min(innerHeight, r.bottom) - top;
    const scale = devicePixelRatio;
    const box = (el) => { const b = el.getBoundingClientRect(); return [(b.x - left) * scale, (b.y - top) * scale, b.width * scale, b.height * scale]; };
    const visible = (el) => { const s = getComputedStyle(el), b = el.getBoundingClientRect();
      return !el.closest('[data-rk-ignore]') && s.display !== 'none' && s.visibility !== 'hidden' && s.opacity !== '0' && b.width > 0 && b.height > 0; };
    const list = (selector) => [...document.querySelectorAll(selector)].filter(visible).map(box);
    const fonts = [...document.querySelectorAll('[data-vd-type]')].filter(visible).map(el => parseFloat(getComputedStyle(el).fontSize));
    return { frame: [Math.round(width * scale), Math.round(height * scale)], css_frame: [width, height], scale,
      columns: Number(stage?.dataset.vdColumns) || null, gutter: Number(stage?.dataset.vdGutter) || 0,
      margin: Number(stage?.dataset.vdMargin) || 0, space_target: stage?.dataset.vdSpaceTarget ? Number(stage.dataset.vdSpaceTarget) : null,
      type_scale: stage?.dataset.vdTypeScale ? Number(stage.dataset.vdTypeScale) : 1.25,
      type_scale_source: stage?.dataset.vdTypeScale ? 'data-vd-type-scale' : 'skill default',
      balance_intent: stage?.dataset.vdBalance || null, grid: list('[data-vd-grid]'),
      occupies: list('[data-vd-occupies]'), font_sizes: fonts,
      focal: document.querySelector('[data-rk-focal]') && visible(document.querySelector('[data-rk-focal]'))
        ? box(document.querySelector('[data-rk-focal]')) : null };
  }, session.svgInput);
  const output = JSON.stringify(data, null, 2);
  if (values.out) await writeFile(resolve(values.out), output + '\n');
  else process.stdout.write(output + '\n');
} finally { await session.stop(); }
