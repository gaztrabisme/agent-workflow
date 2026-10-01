import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';

const root = fs.realpathSync(process.argv[2]);
const port = Number(process.argv[3] ?? 4178);
const mime = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json', '.png': 'image/png' };
const server = http.createServer((request, response) => {
  const urlPath = decodeURIComponent(new URL(request.url, `http://127.0.0.1:${port}`).pathname);
  const file = path.resolve(root, `.${urlPath}`);
  if (file !== root && !file.startsWith(root + path.sep)) { response.writeHead(403).end('forbidden'); return; }
  const target = fs.existsSync(file) && fs.statSync(file).isDirectory() ? path.join(file, 'index.html') : file;
  fs.readFile(target, (error, bytes) => {
    if (error) { response.writeHead(404).end('not found'); return; }
    response.writeHead(200, { 'content-type': mime[path.extname(target)] ?? 'application/octet-stream', 'cache-control': 'no-store' }).end(bytes);
  });
});
server.listen(port, '127.0.0.1');
process.on('SIGTERM', () => server.close(() => process.exit(0)));
process.on('SIGINT', () => server.close(() => process.exit(0)));
