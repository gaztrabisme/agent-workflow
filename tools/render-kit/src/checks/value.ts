import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { mkdtemp, access } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import type { CheckContext, Status } from '../model.ts';
import { result } from './common.ts';

const exec = promisify(execFile);
const threshold = (ctx: CheckContext, name: string, fallback: number) => ctx.options.thresholds[`value.${name}`] ?? fallback;
const tLine = /^(T\d+) (PASS|FAIL|CHECK)\b/;

function achromatic(stdout: string, max: number) {
  const values = [...stdout.matchAll(/(?:mean OKLCH C|Focal box mean C|outermost ring)\s*((?:\d+(?:\.\d+)?|\.\d+))/gi)].map(m => Number(m[1]));
  return values.length > 0 && values.every(value => value <= max);
}

export async function run(ctx: CheckContext) {
  const focal = ctx.session.page.locator('[data-rk-focal]').first();
  if (!(await focal.count())) return result(ctx, 'value', 'n/a', [], 'no focal element');
  const box = await focal.boundingBox();
  if (!box) return result(ctx, 'value', 'n/a', [], 'no focal element');
  const marker = await focal.getAttribute('data-rk-focal');
  const hasChart = await focal.evaluate((el: Element) => el.matches('[data-rk-chart]') || !!el.querySelector('[data-rk-chart]') || !!el.closest('[data-rk-chart]'));
  const stage = await ctx.session.page.evaluate(({svgInput,fullDocument}:{svgInput:boolean;fullDocument:boolean}) => {
    const r = (document.querySelector('[data-rk-stage]') ?? (svgInput ? document.querySelector('body > svg') : null))?.getBoundingClientRect();
    const height = fullDocument ? Math.max(innerHeight, document.documentElement.scrollHeight, document.body?.scrollHeight ?? 0) : innerHeight;
    return { x:r?.x ?? 0, y:r?.y ?? 0, width:r?.width ?? innerWidth, height:r?.height ?? height };
  }, {svgInput:ctx.session.svgInput,fullDocument:ctx.options.height===undefined&&!ctx.session.svgInput});
  const scale = ctx.options.scale;
  const x0 = Math.round((box.x - stage.x) * scale), y0 = Math.round((box.y - stage.y) * scale);
  const x1 = Math.round((box.x + box.width - stage.x) * scale), y1 = Math.round((box.y + box.height - stage.y) * scale);
  const visibleWidth = Math.max(0, Math.min(box.x + box.width, stage.x + stage.width) - Math.max(box.x, stage.x));
  const visibleHeight = Math.max(0, Math.min(box.y + box.height, stage.y + stage.height) - Math.max(box.y, stage.y));
  const focalShare = visibleWidth * visibleHeight / Math.max(1, stage.width * stage.height);
  if (focalShare >= 1 - 1e-9) {
    const reason = 'focal element covers the entire captured stage; there are no outside pixels for value and chroma comparisons';
    return result(ctx, 'value', 'incomplete', [{ check:'value', status:'incomplete', reason }, { check:'chroma', status:'incomplete', reason }], reason);
  }
  const dataGraphic = marker === 'data-graphic';
  const edgeLimit = threshold(ctx, dataGraphic ? 'data_graphic_min_edge_share' : 'min_edge_share', dataGraphic ? 0.5 : 2);
  const maxAreaShare = threshold(ctx, 'max_focal_area_share', 0.5);
  const chromaMax = threshold(ctx, 'achromatic_chroma_max', 0.01);
  const root = process.env.RK_COLOR_THEORY ?? fileURLToPath(new URL('../../../skills/color-theory/', import.meta.url)), script = join(root, 'scripts', 'checks.py');
  const temp = await mkdtemp(join(tmpdir(), 'rk-value-'));
  try { await access(script); } catch { return result(ctx, 'value', 'skipped', [], `color-theory script not found: ${script}`); }

  const rows: any[] = [], errors: string[] = [];
  for (const mode of ['value', 'chroma'] as const) {
    try {
      const args = [script, mode, ctx.png, '--focal', `${x0},${y0},${x1},${y1}`];
      if (mode === 'value') args.push('--out', temp);
      const { stdout } = await exec('python3', args, { timeout: 30000 });
      const lines = String(stdout).split(/\r?\n/);
      const found = lines.map((line: string, index: number) => ({ line, index, match:line.match(tLine) })).filter((row: any) => row.match);
      if (!found.length) { errors.push(`${mode}: ${String(stdout).slice(-300) || 'no T-line returned'}`); continue; }
      for (let i = 0; i < found.length; i++) {
        const row = found[i], previous = i ? found[i - 1].index + 1 : 0;
        const match = row.match as RegExpMatchArray;
        const detail = lines.slice(previous, row.index).filter((line: string) => line.trim()).join(' ');
        const test = match[1], sourceStatus = match[2].toLowerCase();
        let itemStatus: Status = sourceStatus === 'check' ? 'incomplete' : sourceStatus as Status;
        let finalLine = row.line, question: string | undefined;

        if (mode === 'value' && test === 'T1') {
          const measured = detail.match(/\(([\d.]+)x its area share(?: of value edges)?\)/i);
          if (!dataGraphic && focalShare > maxAreaShare) {
            itemStatus = 'incomplete';
            question = 'Does the focal area remain an effective visual entry point at this scale?';
            finalLine = `T1 INCOMPLETE (focal area covers ${(focalShare * 100).toFixed(1)}% of the frame; confirm visually).`;
          } else if (measured) {
            itemStatus = Number(measured[1]) >= edgeLimit ? 'pass' : 'fail';
            finalLine = `T1 ${itemStatus.toUpperCase()} (render-kit threshold: focal box holds at least ${edgeLimit}x its area share of value edges).`;
          } else {
            itemStatus = 'incomplete';
            question = 'Does the focal area hold enough visual weight for the intended reading order?';
            finalLine = `T1 INCOMPLETE (could not read measured edge share; source: ${row.line}).`;
          }
        }
        if (mode === 'chroma' && test === 'T5' && sourceStatus === 'check') {
          if ((hasChart || dataGraphic) && achromatic(String(stdout), chromaMax)) {
            itemStatus = 'n/a';
            finalLine = `T5 N/A (data graphic is achromatic at or below ${chromaMax} OKLCH C).`;
          } else {
            itemStatus = 'incomplete';
            question = 'Does the focal area stand out through chroma in the intended reading order?';
          }
        }
        rows.push({ check:mode, test, status:itemStatus, detail, result:finalLine, source_result:row.line, ...(question ? { question } : {}) });
      }
    } catch (e) { errors.push(`${mode}: ${String((e as any).stderr ?? e).slice(-300)}`); }
  }
  if (rows.some(row => row.status === 'fail')) return result(ctx, 'value', 'fail', rows, errors.length ? errors.join(' | ') : undefined);
  if (rows.some(row => row.status === 'incomplete') || errors.length) {
    return result(ctx, 'value', rows.length ? 'incomplete' : 'skipped', rows, errors.length ? errors.join(' | ') : undefined);
  }
  return rows.length ? result(ctx, 'value', 'pass', rows) : result(ctx, 'value', 'skipped', [], 'no value or chroma T-lines returned');
}
