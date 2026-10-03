import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { readdir } from 'node:fs/promises';
import { join } from 'node:path';

const exec = promisify(execFile);

export async function renderPdfPages(pdf: string, outDir: string) {
  const prefix = join(outDir, 'render-page');
  try {
    await exec('pdftoppm', ['-png', '-cropbox', '-r', '96', pdf, prefix], { timeout: 60000 });
  } catch (e) {
    throw new Error(`could not render PDF pages with pdftoppm: ${String((e as any).stderr ?? e).slice(-300)}`);
  }
  const entries = await readdir(outDir) as string[];
  const names = entries.map((name: string) => {
    const match = name.match(/^render-page-(\d+)\.png$/);
    return match ? { name, page: Number(match[1]) } : null;
  }).filter((item): item is { name:string; page:number } => item !== null).sort((a,b) => a.page - b.page).map(item => item.name);
  if (!names.length) throw new Error('pdftoppm produced no PDF page images');
  return names;
}
