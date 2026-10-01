import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const outDir = path.join(root, 'out');
const workDir = path.join(outDir, '.work');
fs.mkdirSync(workDir, { recursive: true });
fs.mkdirSync(outDir, { recursive: true });

function parseCsv(filename) {
  const lines = fs.readFileSync(filename, 'utf8').trim().split(/\r?\n/);
  const [header, ...rows] = lines.map((line) => line.split(',').map((cell) => cell.trim()));
  return rows.map((row) => Object.fromEntries(header.map((name, index) => [name, row[index]])));
}

function command(args, name) {
  return new Promise((resolve, reject) => {
    process.stderr.write(`\n[samples] ${name}\n`);
    const child = spawn(process.execPath, args, { cwd: root, env: { ...process.env, HYPERFRAMES_NO_TELEMETRY: '1' }, stdio: 'inherit' });
    child.once('error', reject);
    child.once('close', (code) => code === 0 ? resolve() : reject(new Error(`${name} failed with exit ${code}`)));
  });
}

async function waitForApp(child) {
  const deadline = Date.now() + 12000;
  while (Date.now() < deadline) {
    if (child.exitCode !== null) throw new Error(`fixture app exited ${child.exitCode}`);
    try { const response = await fetch('http://127.0.0.1:4178/'); if (response.ok) return; } catch { }
    await new Promise((resolve) => setTimeout(resolve, 150));
  }
  throw new Error('fixture app did not start on port 4178');
}

const explainer = JSON.parse(fs.readFileSync(path.join(root, 'samples/explainer/storyboard.json'), 'utf8'));
const csv = parseCsv(path.join(root, 'samples/explainer/chart.csv'));
const chart = explainer.scenes.flatMap((scene) => scene.layers).find((layer) => layer.id === 'signal-chart');
chart.categories = csv.map((row) => row.month);
chart.series = [
  { name: 'Visits', values: csv.map((row) => Number(row.visits)) },
  { name: 'Qualified', values: csv.map((row) => Number(row.qualified)) }
];
const explainerStory = path.join(workDir, 'explainer.storyboard.json');
fs.writeFileSync(explainerStory, `${JSON.stringify(explainer, null, 2)}\n`);
await command([path.join(root, 'src/cli.mjs'), 'render', explainerStory, '--root', path.join(root, 'samples/explainer'), '--out', path.join(outDir, 'explainer.mp4'), '--renderer', 'auto', '--captions', 'both', '--timeout', '180000'], 'render explainer MP4 with CSV-backed chart');
await command([path.join(root, 'src/cli.mjs'), 'export-pptx', explainerStory, '--root', path.join(root, 'samples/explainer'), '--out', path.join(outDir, 'explainer.pptx'), '--verify'], 'export editable explainer PPTX');

const app = spawn(process.execPath, [path.join(root, 'src/static-server.mjs'), path.join(root, 'samples/fixture-app'), '4178'], { cwd: root, stdio: 'ignore' });
try {
  await waitForApp(app);
  await command([path.join(root, 'src/cli.mjs'), 'render', path.join(root, 'samples/app-demo/storyboard.json'), '--root', path.join(root, 'samples/app-demo'), '--out', path.join(outDir, 'app-demo.mp4'), '--renderer', 'auto', '--captions', 'both', '--timeout', '180000'], 'capture fixture app and render app-demo MP4');
} finally {
  app.kill('SIGTERM');
}
process.stderr.write('\n[samples] all requested artifacts are in out/\n');
