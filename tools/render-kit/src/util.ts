import { access, mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname, extname, resolve } from 'node:path';

export const exists = async (path: string) => access(path).then(() => true, () => false);
export const jsonWrite = async (path: string, value: unknown) => { await mkdir(dirname(path), { recursive: true }); await writeFile(path, JSON.stringify(value, null, 2) + '\n'); };
export const jsonRead = async <T>(path: string): Promise<T> => JSON.parse(await readFile(path, 'utf8')) as T;
export const absoluteInput = (value: string) => /^https?:\/\//i.test(value) ? value : resolve(value);
export const isUrl = (value: string) => /^https?:\/\//i.test(value);
export const formatOf = (value: string) => extname(value).toLowerCase().slice(1);
export const clamp = (v: number, low: number, high: number) => Math.max(low, Math.min(high, v));
export const esc = (value: string) => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
