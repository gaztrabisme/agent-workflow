import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, resolve, sep } from 'node:path';
import type { AddressInfo } from 'node:net';

const types: Record<string, string> = { '.html': 'text/html', '.svg': 'image/svg+xml', '.css': 'text/css', '.js': 'text/javascript', '.mjs': 'text/javascript', '.png': 'image/png', '.jpg': 'image/jpeg', '.woff2': 'font/woff2', '.woff': 'font/woff', '.json': 'application/json' };
const dim = (s: string | null) => s ? parseFloat(s) * (s.endsWith('pt') ? 96 / 72 : s.endsWith('in') ? 96 : s.endsWith('cm') ? 96 / 2.54 : 1) : NaN;

export function svgSize(svg: string) {
  const tag = svg.match(/<svg\b[^>]*>/i)?.[0] ?? '';
  const attr = (name: string) => tag.match(new RegExp(`\\b${name}=["']([^"']+)`, 'i'))?.[1] ?? null;
  const vb = (attr('viewBox') ?? '').trim().split(/[\s,]+/).map(Number);
  const width = dim(attr('width')) || vb[2] || 800, height = dim(attr('height')) || vb[3] || 600;
  return { width, height };
}

export async function startServer(rootPath: string, entryPath: string) {
  const root = resolve(rootPath), entry = resolve(entryPath), wrapSvg = entry.toLowerCase().endsWith('.svg');
  const server = createServer(async (req:{url?:string}, res:{writeHead:(status:number,headers?:Record<string,string>)=>any;end:(body?:any)=>any}) => {
    try {
      const pathname = decodeURIComponent(new URL(req.url ?? '/', 'http://localhost').pathname);
      const file = resolve(root, `.${pathname}`);
      if (file !== root && !file.startsWith(root + sep)) { res.writeHead(404).end('Not found'); return; }
      let body = await readFile(file);
      if (wrapSvg && file === entry) body = Buffer.from(svgWrapper(body.toString('utf8')));
      res.writeHead(200, { 'content-type': `${wrapSvg && file === entry ? 'text/html' : types[extname(file)] ?? 'application/octet-stream'}; charset=utf-8` });
      res.end(body);
    } catch { res.writeHead(404).end('Not found'); }
  });
  await new Promise<void>((ok, bad) => { server.once('error', bad); server.listen(0, '127.0.0.1', ok); });
  const port = (server.address() as AddressInfo).port;
  return { server, url: `http://127.0.0.1:${port}/${encodeURI(entry.slice(root.length + 1))}`, root };
}

export function svgWrapper(svg: string) {
  const { width, height } = svgSize(svg);
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>SVG</title><style>html,body{margin:0;width:${width}px;height:${height}px;background:transparent}@page{size:${width}px ${height}px;margin:0}body{overflow:hidden}body>svg{display:block}</style></head><body>${svg}</body></html>`;
}
