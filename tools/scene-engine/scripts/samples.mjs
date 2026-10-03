import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { startStaticServer } from '../src/static-server.mjs';

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

const app = await startStaticServer(path.join(root, 'samples/fixture-app'));
try {
  const appDemo = JSON.parse(fs.readFileSync(path.join(root, 'samples/app-demo/storyboard.json'), 'utf8'));
  const appDemoLayer = appDemo.scenes.flatMap((scene) => scene.layers).find((layer) => layer.type === 'appDemo');
  if (!appDemoLayer) throw new Error('app-demo storyboard has no appDemo layer');
  appDemoLayer.url = `http://127.0.0.1:${app.address().port}/`;
  const appDemoStory = path.join(workDir, 'app-demo.storyboard.json');
  fs.writeFileSync(appDemoStory, `${JSON.stringify(appDemo, null, 2)}\n`);
  await command([path.join(root, 'src/cli.mjs'), 'render', appDemoStory, '--root', path.join(root, 'samples/app-demo'), '--out', path.join(outDir, 'app-demo.mp4'), '--renderer', 'auto', '--captions', 'both', '--timeout', '180000'], 'capture fixture app and render app-demo MP4');
} finally {
  await new Promise((resolve, reject) => app.close((error) => error ? reject(error) : resolve()));
}
process.stderr.write('\n[samples] all requested artifacts are in out/\n');
