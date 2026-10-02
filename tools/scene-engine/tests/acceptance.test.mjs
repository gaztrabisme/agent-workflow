import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import net from 'node:net';
import { spawn, spawnSync, execFileSync } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright';
import { loadStoryboard, diagnostic } from '../src/scene.mjs';
import { ease, sampleTrack, sampleLayer, frameTimeMs, frameCount } from '../src/timeline.mjs';
import { generateHtml, generateStaticHtml, writeVtt } from '../src/html.mjs';
import { renderStoryboard, defaultTimeoutForFrames, selectRenderer } from '../src/render.mjs';
import { exportWithKeynote } from '../src/pptx_smoke.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUT = path.join(ROOT, 'out');
const WORK = path.join(OUT, '.work', 'acceptance');
const CLI = path.join(ROOT, 'src/cli.mjs');
fs.mkdirSync(WORK, { recursive: true });

function baseStory(layers = [], durationMs = 1000) {
  return { format: 'scene-engine/storyboard@1', title: 'Acceptance fixture', width: 1920, height: 1080, fps: 30, scenes: [{ id: 'scene', startMs: 0, durationMs, layers }] };
}
function layer(id, type = 'shape', extra = {}) {
  return { id, type, x: 0, y: 0, width: 300, height: 200, startMs: 0, durationMs: 1000, ...(type === 'shape' ? { shape: 'rect', fill: '#2563EB' } : {}), ...extra };
}
function storyFile(name, story, directory = WORK) {
  const filename = path.join(directory, name);
  fs.mkdirSync(path.dirname(filename), { recursive: true });
  fs.writeFileSync(filename, `${JSON.stringify(story, null, 2)}\n`);
  return filename;
}
function runCli(args) {
  const stdout = execFileSync(process.execPath, [CLI, ...args], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20 * 1024 * 1024 });
  return JSON.parse(stdout.trim());
}
function runCliAsync(args, env = process.env, cwd = ROOT) {
  return new Promise((resolve) => {
    const child = spawn(process.execPath, [CLI, ...args], { cwd, env, stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = ''; let stderr = '';
    child.stdout.on('data', (chunk) => stdout += chunk);
    child.stderr.on('data', (chunk) => stderr += chunk);
    child.once('close', (code) => resolve({ code, stdout, stderr }));
  });
}
function makeTone(filename, durationSeconds) {
  fs.mkdirSync(path.dirname(filename), { recursive: true });
  execFileSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i', `sine=frequency=660:duration=${durationSeconds}`, '-ac', '1', '-ar', '22050', '-c:a', 'pcm_s16le', filename]);
  return filename;
}
function segmentMeanVolume(filename, start, duration) {
  const result = spawnSync('ffmpeg', ['-hide_banner', '-i', filename, '-ss', String(start), '-t', String(duration), '-af', 'volumedetect', '-f', 'null', '-'], { encoding: 'utf8' });
  const match = `${result.stdout}\n${result.stderr}`.match(/mean_volume:\s*(-inf|[-\d.]+) dB/);
  return match ? (match[1] === '-inf' ? -120 : Number(match[1])) : NaN;
}
async function unusedPort() {
  const server = net.createServer();
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  const port = server.address().port;
  await new Promise((resolve) => server.close(resolve));
  return port;
}
async function startFixtureApp(port, root = path.join(ROOT, 'samples/fixture-app')) {
  const child = spawn(process.execPath, [path.join(ROOT, 'src/static-server.mjs'), root, String(port)], { cwd: ROOT, stdio: 'ignore' });
  const deadline = Date.now() + 10000;
  while (Date.now() < deadline) {
    if (child.exitCode !== null) throw new Error(`fixture app exited ${child.exitCode}`);
    try { if ((await fetch(`http://127.0.0.1:${port}/`)).ok) return child; } catch { }
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  child.kill('SIGTERM');
  throw new Error('fixture app did not start');
}
const MP4_RENDERERS = ['fallback', ...(fs.existsSync(path.join(ROOT, 'node_modules/.bin/hyperframes')) ? ['hyperframes'] : [])];
const RGB_FRAME_BYTES = 1920 * 1080 * 3;
function rawFrame(filename, timeMs = null) {
  const args = ['-hide_banner', '-loglevel', 'error', '-i', filename];
  if (timeMs !== null) args.push('-ss', (timeMs / 1000).toFixed(3));
  args.push('-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'rgb24', 'pipe:1');
  const result = spawnSync('ffmpeg', args, { maxBuffer: RGB_FRAME_BYTES + 1024 * 1024 });
  if (result.status !== 0) throw new Error(`ffmpeg frame extraction failed: ${result.stderr?.toString()}`);
  assert.equal(result.stdout.length, RGB_FRAME_BYTES, `expected one 1920x1080 RGB frame from ${filename}`);
  return result.stdout;
}
function rawPng(filename) {
  const result = spawnSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-i', filename, '-f', 'rawvideo', '-pix_fmt', 'rgb24', 'pipe:1'], { maxBuffer: 16 * 1024 * 1024 });
  if (result.status !== 0) throw new Error(`ffmpeg PNG decode failed: ${result.stderr?.toString()}`);
  return result.stdout;
}
function rgbPixel(frame, width, x, y) {
  const offset = (y * width + x) * 3;
  return [frame[offset], frame[offset + 1], frame[offset + 2]];
}
async function checkFrame(model, timeMs, filename) {
  fs.mkdirSync(path.dirname(filename), { recursive: true });
  fs.writeFileSync(filename.replace(/\.png$/, '.html'), generateStaticHtml(model, timeMs));
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
    await page.goto(pathToFileURL(filename.replace(/\.png$/, '.html')).href, { waitUntil: 'load' });
    await page.evaluate(() => window.__sceneEngine.ready());
    await page.evaluate(() => new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve))));
    await page.screenshot({ path: filename, animations: 'disabled' });
  } finally { await browser.close(); }
  return rawFrame(filename);
}
function assertMeanAbsoluteFrameDifference(expected, actual, renderer, timeMs, tolerance = 8) {
  let total = 0;
  for (let i = 0; i < expected.length; i += 1) total += Math.abs(expected[i] - actual[i]);
  const mean = total / expected.length;
  assert.ok(mean <= tolerance, `${renderer} MP4 differs from check model at ${timeMs} ms: mean absolute RGB difference ${mean.toFixed(2)} > ${tolerance}`);
}
function assertRegionMeanDifference(expected, actual, region, renderer, timeMs, tolerance = 8) {
  let total = 0;
  for (let y = region.y; y < region.y + region.height; y += 1) for (let x = region.x; x < region.x + region.width; x += 1) {
    const offset = (y * 1920 + x) * 3;
    total += Math.abs(expected[offset] - actual[offset]) + Math.abs(expected[offset + 1] - actual[offset + 1]) + Math.abs(expected[offset + 2] - actual[offset + 2]);
  }
  const mean = total / (region.width * region.height * 3);
  assert.ok(mean <= tolerance, `${renderer} MP4 content differs from check model at ${timeMs} ms in ${JSON.stringify(region)}: mean absolute RGB difference ${mean.toFixed(2)} > ${tolerance}`);
}
function assertRgbPixelNear(frame, x, y, expected, tolerance, label) {
  const offset = (y * 1920 + x) * 3;
  const actual = [frame[offset], frame[offset + 1], frame[offset + 2]];
  assert.ok(actual.every((channel, index) => Math.abs(channel - expected[index]) <= tolerance), `${label}: expected RGB ${expected.join(',')} ±${tolerance}, received ${actual.join(',')}`);
}
async function compareMp4WithCheck(model, testId, timesMs, { captions = 'none', regions = [] } = {}) {
  const failures = [];
  const references = new Map();
  for (const renderer of MP4_RENDERERS) {
    const output = path.join(OUT, 'tests', 'mp4-comparison', `${testId}-${renderer}.mp4`);
    const rendered = await renderStoryboard(model, { out: output, renderer, captions, timeoutMs: 120000 });
    assert.equal(rendered.durationMs, model.durationMs);
    for (const timeMs of timesMs) {
      const reference = await checkFrame(model, timeMs, path.join(WORK, 'mp4-comparison', `${testId}-${renderer}-${timeMs}.png`));
      references.set(`${renderer}:${timeMs}`, reference);
      const actual = rawFrame(output, timeMs);
      try {
        assertMeanAbsoluteFrameDifference(reference, actual, renderer, timeMs);
        for (const region of regions) assertRegionMeanDifference(reference, actual, region, renderer, timeMs);
      } catch (error) { failures.push(error.message); }
    }
  }
  assert.deepEqual(failures, [], failures.join('\n'));
  return references;
}
function zipText(filename, entry) { return execFileSync('unzip', ['-p', filename, entry], { encoding: 'utf8' }); }
function exportPptx(filename, output, extra = []) { return runCli(['export-pptx', filename, '--root', ROOT, '--out', output, ...extra]); }
function makeAt17Story(url) {
  return baseStory([layer('unseekable-dashboard', 'appDemo', {
    width: 640, height: 360, type: 'appDemo', url, readySelector: '[data-ready]', steps: [],
    appBuildId: 'at17-canvas-fixture', deviceScaleFactor: 2, viewport: 'layer-box-css-pixels'
  })], 1000);
}

test('AT01', () => {
  const story = baseStory([
    layer('text', 'text', { text: 'Editable title' }),
    layer('shape', 'shape'),
    layer('image', 'image', { src: 'samples/explainer/signal-map.png', alt: 'Signals' }),
    layer('chart', 'chart', { kind: 'column', categories: ['Jan'], series: [{ name: 'Visits', values: [12] }] })
  ]);
  const model = loadStoryboard(storyFile('at01.json', story), { root: ROOT });
  assert.deepEqual(model.errors, []);
  assert.equal(model.layerCount, 4);
  assert.equal(model.frameCount, 30);
});

test('AT02', () => {
  const fixtureDir = path.join(ROOT, 'tests/fixtures/at02');
  const link = path.join(fixtureDir, 'escape.md');
  if (!fs.existsSync(link)) fs.symlinkSync('../../../SPEC.md', link);
  const model = loadStoryboard(path.join(fixtureDir, 'storyboard.json'));
  assert.ok(model.errors.some((item) => item.code === 'PATH_OUTSIDE_ROOT' && item.pointer === '/scenes/0/layers/0/src'));
  assert.ok(model.errors.some((item) => item.pointer === '/scenes/0/layers/1/id' && item.message.includes('Duplicate layer id')));
});

test('AT03', () => {
  assert.ok(Math.abs(ease(0.25, 'linear') - 0.25) < 0.01);
  assert.ok(Math.abs(ease(0.5, 'ease-in-out') - 0.5) < 0.01);
  assert.equal(ease(0.25, 'step-start'), 1);
  assert.equal(ease(0.25, 'step-end'), 0);
  const bezier = ease(0.5, { cubicBezier: [0.42, 0, 0.58, 1] });
  assert.ok(Math.abs(bezier - 0.5) < 0.01);
});

test('AT04', () => {
  const story = { ...baseStory(), scenes: [
    { id: 'outgoing', startMs: 0, durationMs: 1100, layers: [layer('a', 'text', { durationMs: 1100, text: 'A', tracks: [{ property: 'opacity', keyframes: [{ atMs: 0, value: 1 }, { atMs: 1000, value: 0 }] }] })] },
    { id: 'incoming', startMs: 800, durationMs: 1000, layers: [layer('b', 'text', { durationMs: 1000, text: 'B', tracks: [{ property: 'opacity', keyframes: [{ atMs: 0, value: 0 }, { atMs: 300, value: 1 }] }] })] }
  ] };
  const model = loadStoryboard(storyFile('at04.json', story), { root: ROOT });
  assert.deepEqual(model.errors, []);
  assert.equal(model.scenes[0]._startMs + model.scenes[0].durationMs - model.scenes[1]._startMs, 300);
  const html = generateHtml(model);
  assert.match(html, /outgoing/);
  assert.match(html, /incoming/);
  assert.match(html, /opacity:0/);
});

test('AT05', async (t) => {
  const story = baseStory([layer('seek-box', 'shape', { tracks: [{ property: 'x', keyframes: [{ atMs: 0, value: 0 }, { atMs: 900, value: 400 }] }] })]);
  const model = loadStoryboard(storyFile('at05.json', story), { root: ROOT });
  const htmlFile = path.join(WORK, 'at05.html'); fs.writeFileSync(htmlFile, generateHtml(model));
  const context = await chromium.launchPersistentContext(path.join(WORK, 'at05-profile'), { headless: true, viewport: { width: 1920, height: 1080 } });
  t.after(() => context.close());
  const page = await context.newPage(); await page.goto(pathToFileURL(htmlFile).href); await page.evaluate(() => window.__sceneEngine.ready());
  await page.evaluate(() => window.__sceneEngine.seek(900)); const first = await page.screenshot();
  await page.evaluate(() => window.__sceneEngine.seek(200));
  await page.evaluate(() => window.__sceneEngine.seek(900)); const second = await page.screenshot();
  assert.deepEqual(first, second);
});

test('AT06', async (t) => {
  const story = baseStory([layer('adapter-stage')], 1000);
  const model = loadStoryboard(storyFile('at06.json', story), { root: ROOT });
  const htmlFile = path.join(WORK, 'at06.html'); fs.writeFileSync(htmlFile, generateHtml(model));
  const context = await chromium.launchPersistentContext(path.join(WORK, 'at06-profile'), { headless: true, viewport: { width: 1920, height: 1080 } });
  t.after(() => context.close());
  const page = await context.newPage();
  await page.addInitScript(() => {
    let lastFrame = -1;
    window.__sceneEngineAdapters = [{ id: 'history-adapter', layerId: 'adapter-stage', seekFrame(frame) { if (frame < lastFrame) return false; lastFrame = frame; return true; } }];
  });
  await page.goto(pathToFileURL(htmlFile).href); await page.evaluate(() => window.__sceneEngine.ready());
  const probe = await page.evaluate(() => window.__sceneEngine.verifyAdapters());
  assert.equal(probe.status, 'fail');
  assert.equal(probe.code, 'UNSEEKABLE');
  assert.equal(probe.adapterId, 'history-adapter');
  assert.equal(probe.layerId, 'adapter-stage');
  assert.equal(probe.frame, 0);
});

test('AT07', () => {
  const pkg = JSON.parse(fs.readFileSync(path.join(ROOT, 'package.json'), 'utf8'));
  assert.equal(pkg.dependencies.hyperframes, '0.8.78');
  const renderer = fs.readFileSync(path.join(ROOT, 'src/render.mjs'), 'utf8');
  assert.match(renderer, /HYPERFRAMES_NO_TELEMETRY: '1'/);
  assert.match(renderer, /\['lint', compositionDir\]/);
});

test('AT08', async () => {
  const filename = storyFile('at08.json', baseStory([layer('missing-hyperframes')], 1000));
  const output = path.join(OUT, 'tests', 'at08-missing.mp4'); fs.rmSync(output, { force: true });
  const env = { ...process.env, SCENE_ENGINE_HYPERFRAMES_BIN: path.join(WORK, 'missing', 'hyperframes') };
  const result = await runCliAsync(['render', filename, '--root', ROOT, '--renderer', 'hyperframes', '--captions', 'none', '--out', output], env);
  const document = JSON.parse(result.stdout.trim());
  assert.equal(result.code, 3);
  assert.equal(document.errors[0].code, 'HYPERFRAMES_MISSING');
  assert.match(document.errors[0].message, /unavailable/i);
  assert.equal(fs.existsSync(output), false);
});

test('AT09', async () => {
  const audio = makeTone(path.join(WORK, 'at09.wav'), 0.5);
  const story = baseStory([layer('voice-title', 'text', { text: 'Narration starts after a short offset.' })], 2000);
  story.scenes[0].narration = { text: 'Narration starts after a short offset.', audio: 'out/.work/acceptance/at09.wav', audioOffsetMs: 250, gainDb: 0 };
  const model = loadStoryboard(storyFile('at09.json', story), { root: ROOT });
  const output = path.join(OUT, 'tests', 'at09.mp4');
  const result = await renderStoryboard(model, { out: output, renderer: 'fallback', captions: 'none', timeoutMs: 60000 });
  assert.equal(result.streams.find((stream) => stream.type === 'audio').codec, 'aac');
  assert.equal(result.streams.find((stream) => stream.type === 'audio').sampleRate, 48000);
  assert.equal(result.diagnostics[0].mode, 'two-pass-loudnorm');
  const silence = segmentMeanVolume(output, 0.03, 0.16);
  const voice = segmentMeanVolume(output, 0.4, 0.16);
  assert.ok(Number.isFinite(silence) && Number.isFinite(voice) && voice > silence + 20, `expected offset silence then voice, got ${silence} dB then ${voice} dB`);
});

test('AT10', () => {
  const model = loadStoryboard(path.join(ROOT, 'samples/explainer/storyboard.json'));
  const vtt = path.join(OUT, 'tests', 'at10.vtt'); fs.mkdirSync(path.dirname(vtt), { recursive: true });
  writeVtt(model, vtt);
  const content = fs.readFileSync(vtt, 'utf8');
  assert.ok(content.startsWith('WEBVTT\n'));
  assert.match(content, /00:00:01\.200 --> 00:00:04\.700/);
  const starts = [...content.matchAll(/(\d\d:\d\d:\d\d\.\d{3}) -->/g)].map((match) => match[1]);
  assert.equal(starts.length, 4);
});

test('AT11', () => {
  const model = loadStoryboard(path.join(ROOT, 'samples/explainer/storyboard.json'));
  const html = generateHtml(model, { captionMode: 'burn-in' });
  assert.match(html, /class="caption"/);
  assert.match(html, /data-caption-start="1200" data-caption-end="4700"/);
  assert.match(html, /cue\.style\.opacity=show\?'1':'0'/);
  assert.match(html, /useful question/);
});

test('AT12', () => {
  const output = path.join(OUT, 'tests', 'at12.pptx'); fs.mkdirSync(path.dirname(output), { recursive: true });
  const result = runCli(['export-pptx', 'samples/explainer/storyboard.json', '--root', 'samples/explainer', '--out', output, '--verify']);
  assert.equal(result.ok, true);
  assert.equal(result.result.slideCount, 3);
  assert.ok(result.result.mappings.some((item) => item.representation === 'native-text'));
  assert.ok(result.result.mappings.some((item) => item.representation === 'native-chart'));
  const shapes = execFileSync(path.join(ROOT, '.venv/bin/python'), ['-c', "from pptx import Presentation; p=Presentation('" + output + "'); s=[sh for sl in p.slides for sh in sl.shapes]; assert any(sh.has_chart for sh in s); assert any(sh.has_text_frame and sh.text_frame.text.strip() for sh in s); print('ok')"], { encoding: 'utf8' });
  assert.match(shapes, /ok/);
});

test('AT13', () => {
  const chart = layer('combo-chart', 'chart', { kind: 'combo', categories: ['Q1', 'Q2', 'Q3'], series: [
    { name: 'Units', kind: 'column', axis: 'primary', values: [12, 18, 16] },
    { name: 'Margin', kind: 'line', axis: 'secondary', values: [0.12, 0.14, 0.18] }
  ] });
  const filename = storyFile('at13.json', baseStory([
    layer('combo-title', 'text', { text: 'Units and margin', width: 700, height: 80 }),
    layer('combo-marker', 'shape', { x: 750, y: 20, width: 80, height: 80, decorative: true }),
    chart
  ])); const output = path.join(OUT, 'tests', 'at13-combo.pptx');
  const document = exportPptx(filename, output);
  assert.equal(document.ok, true);
  const xml = zipText(output, 'ppt/charts/chart1.xml');
  assert.match(xml, /<c:lineChart>/);
  assert.equal((xml.match(/<c:valAx>/g) ?? []).length, 2);
  assert.match(xml, /<c:axPos val="r"/);
  assert.equal(document.result.workbookChecks[0].series, 2);
  assert.ok(document.result.workbookChecks[0].workbookPart);
  assert.ok(execFileSync('unzip', ['-Z1', output], { encoding: 'utf8' }).split('\n').includes(document.result.workbookChecks[0].workbookPart));
});
test('AT14', () => {
  const title = layer('editable-title', 'text', { text: 'Effects keep title editable.', style: { fontFamily: 'Arial', fontSize: 40 } });
  const effect = layer('effect-panel', 'shape', { alt: 'Blurred evidence panel', effects: { blurPx: 3, blendMode: 'multiply', transform3d: [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1] } });
  const filename = storyFile('at14.json', baseStory([title, effect])); const output = path.join(OUT, 'tests', 'at14-fallback.pptx');
  const document = exportPptx(filename, output);
  assert.equal(document.ok, true);
  assert.equal(document.result.mappings.find((item) => item.layerId === 'effect-panel').representation, 'rasterized-layer');
  assert.match(document.result.mappings.find((item) => item.layerId === 'effect-panel').reason, /blur.*blend.*3D/);
  const inspect = execFileSync(path.join(ROOT, '.venv/bin/python'), ['-c', "from pptx import Presentation; import sys; p=Presentation(sys.argv[1]); shapes=[s for slide in p.slides for s in slide.shapes]; assert any(s.has_text_frame and 'Effects keep title editable.' in s.text_frame.text for s in shapes); pic=next(s for s in shapes if s.name == 'effect-panel' and s.shape_type == 13); assert pic.image.size[0] >= 600 and pic.image.size[1] >= 400, pic.image.size; assert pic._element.nvPicPr.cNvPr.get('descr') == 'Blurred evidence panel'; print('editable text + 2x picture + alt text')", output], { encoding: 'utf8' });
  assert.match(inspect, /editable text \+ 2x picture/);
});

test('AT15', async (t) => {
  const port = await unusedPort(); const server = await startFixtureApp(port);
  t.after(() => server.kill('SIGTERM'));
  const story = JSON.parse(fs.readFileSync(path.join(ROOT, 'samples/app-demo/storyboard.json'), 'utf8'));
  story.scenes[0].layers.find((item) => item.id === 'dashboard-demo').url = `http://127.0.0.1:${port}/`;
  const filename = storyFile('at15.json', story);
  const result = runCli(['capture', filename, '--root', path.join(ROOT, 'samples/app-demo'), '--scene', 'dashboard', '--layer', 'dashboard-demo', '--out-dir', path.join(OUT, 'tests/at15'), '--timeout', '30000']);
  assert.equal(result.ok, true);
  assert.equal(result.result.deviceScaleFactor, 2);
  assert.equal(result.result.frameCount, 72);
  assert.equal(result.result.hashes.length, 72);
});

test('AT16', async (t) => {
  const port = await unusedPort(); const server = await startFixtureApp(port);
  t.after(() => server.kill('SIGTERM'));
  const story = JSON.parse(fs.readFileSync(path.join(ROOT, 'samples/app-demo/storyboard.json'), 'utf8'));
  const appLayer = story.scenes[0].layers.find((item) => item.id === 'dashboard-demo');
  appLayer.url = `http://127.0.0.1:${port}/`; appLayer.readySelector = '[data-testid=never]'; appLayer.readyTimeoutMs = 1000;
  const result = await runCliAsync(['capture', storyFile('at16.json', story), '--root', path.join(ROOT, 'samples/app-demo'), '--scene', 'dashboard', '--layer', 'dashboard-demo', '--out-dir', path.join(OUT, 'tests/at16'), '--timeout', '1000']);
  const document = JSON.parse(result.stdout.trim());
  assert.equal(result.code, 3);
  assert.equal(document.errors[0].code, 'APP_LOAD_FAILED');
  assert.match(document.errors[0].message, /ready selector/);
});

test('AT17', async (t) => {
  const appRoot = path.join(WORK, 'at17-app'); fs.mkdirSync(appRoot, { recursive: true });
  fs.writeFileSync(path.join(appRoot, 'index.html'), '<!doctype html><div data-ready>ready</div><canvas id="draw" width="40" height="40"></canvas><script>const c=document.querySelector("canvas").getContext("2d");function tick(){c.fillStyle="#2563EB";c.fillRect(Math.random()*20,0,20,20);requestAnimationFrame(tick)}tick();</script>');
  const port = await unusedPort(); const server = await startFixtureApp(port, appRoot); t.after(() => server.kill('SIGTERM'));
  const filename = storyFile('at17.json', makeAt17Story(`http://127.0.0.1:${port}/`));
  const outDir = path.join(OUT, 'tests', 'at17'); fs.rmSync(outDir, { recursive: true, force: true });
  const result = await runCliAsync(['capture', filename, '--root', appRoot, '--scene', 'scene', '--layer', 'unseekable-dashboard', '--out-dir', outDir, '--timeout', '3000']);
  const document = JSON.parse(result.stdout.trim());
  assert.equal(result.code, 1);
  assert.equal(document.errors[0].code, 'UNSEEKABLE');
  assert.equal(document.errors[0].layerId, 'unseekable-dashboard');
  assert.equal(document.errors[0].frame, 0);
  assert.match(document.errors[0].message, /canvas.*deterministic seek adapter/i);
  assert.equal(fs.existsSync(outDir), false);
});

test('AT18', async () => {
  const story = baseStory([layer('fallback-box')], 1000);
  const filename = storyFile('at18.json', story);
  const model = loadStoryboard(filename, { root: ROOT });
  const output = path.join(OUT, 'tests', 'at18.mp4');
  const result = await renderStoryboard(model, { out: output, renderer: 'fallback', captions: 'none', timeoutMs: 60000 });
  assert.equal(result.renderer.name, 'fallback');
  assert.equal(result.frameCount, 30);
  assert.ok(result.streams.some((stream) => stream.type === 'audio' && stream.codec === 'aac'));
  assert.ok(result.streams.some((stream) => stream.type === 'video' && stream.width === 1920 && stream.height === 1080));
});

test('AT19', () => {
  const filename = storyFile('at19.json', baseStory([], 1000));
  const result = runCli(['check', filename, '--root', ROOT, '--at', '800', '--rk', '../render-kit/bin/rk', '--out-dir', path.join(OUT, 'tests/at19')]);
  const model = loadStoryboard(filename, { root: ROOT });
  const expected = new Set([800]);
  for (const scene of model.scenes) for (const time of [scene._startMs, scene._startMs + Math.floor(scene.durationMs / 2), scene._startMs + scene.durationMs - 1]) expected.add(time);
  const expectedTimes = [...expected].sort((a, b) => a - b);
  assert.deepEqual(result.result.timesMs, expectedTimes);
  assert.equal(result.result.reports.length, expectedTimes.length);
  assert.deepEqual(result.result.reports.map((item) => item.rk.report.at_ms), expectedTimes);
  assert.ok(result.result.reports.every((item) => item.status === 'pass'));
});

test('AT20', () => {
  const filename = storyFile('at20.json', baseStory([], 1000));
  const outDir = path.join(OUT, 'tests/at20'); fs.rmSync(outDir, { recursive: true, force: true });
  const result = runCli(['check', filename, '--root', ROOT, '--pptx', path.join(OUT, 'tests/at12.pptx'), '--at', '500', '--rk', '../render-kit/bin/rk', '--out-dir', outDir]);
  assert.equal(result.result.pptxDiagnostics.status, 'rendered-and-checked');
  assert.equal(result.result.pptxDiagnostics.slides.length, 3);
  assert.ok(result.result.pptxDiagnostics.slides.every((slide) => slide.rk.report));
});

test('AT21', () => {
  const profile = fs.readFileSync(path.join(ROOT, 'src/render.mjs'), 'utf8');
  assert.match(profile, /-profile:v', 'high'/);
  assert.match(profile, /-level:v', '4\.1'/);
  assert.match(profile, /AAC-LC/);
  assert.equal(frameCount(1001), 31);
});

test('AT22', () => {
  const unknown = spawnSync(process.execPath, [CLI, 'not-a-command'], { cwd: ROOT, encoding: 'utf8' });
  const output = JSON.parse(unknown.stdout.trim());
  assert.equal(unknown.status, 2);
  assert.equal(output.exitCode, 2);
  assert.equal(output.errors[0].code, 'CLI_USAGE');
  const bad = path.join(ROOT, 'tests/fixtures/at22-bad.json');
  fs.writeFileSync(bad, '{ definitely not json');
  try {
    const result = spawnSync(process.execPath, [CLI, 'validate', bad], { cwd: ROOT, encoding: 'utf8' });
    assert.equal(JSON.parse(result.stdout.trim()).errors[0].code, 'JSON_INVALID');
  } finally { fs.rmSync(bad, { force: true }); }
});

test('AT23', () => {
  const story = baseStory([layer('custom', 'adapter', { adapterId: 'unknown-adapter', source: 'unused.json', config: {} })]);
  const model = loadStoryboard(storyFile('at23.json', story), { root: ROOT });
  assert.ok(model.errors.some((item) => item.code === 'ADAPTER_NOT_REGISTERED'));
});

test('AT24', () => {
  const layerValue = layer('sparse', 'text', { text: 'x', x: 10, opacity: 1, tracks: [
    { property: 'x', keyframes: [{ atMs: 500, value: 110 }] },
    { property: 'opacity', keyframes: [{ atMs: 0, value: 1 }, { atMs: 500, value: 0.5 }] },
    { property: 'style.color', keyframes: [{ atMs: 0, value: '#000000' }, { atMs: 1000, value: '#FFFFFF' }] }
  ] });
  layerValue.style = { color: '#000000' };
  const before = sampleLayer(layerValue, 100);
  const middle = sampleLayer(layerValue, 750);
  assert.equal(before.x, 10);
  assert.ok(Math.abs(before.opacity - 0.9) < 0.01);
  assert.equal(middle.x, 110);
  assert.equal(middle.opacity, 0.5);
  assert.notEqual(middle.style.color, '#000000');
});

test('AT25', () => {
  const story = baseStory([layer('masked', 'shape', { effects: { mask: { sourceLayerId: 'missing' } } })]);
  story.scenes[0].camera = { tracks: [{ property: 'zoom', keyframes: [{ atMs: 0, value: 1 }, { atMs: 999, value: 1.1 }] }] };
  const model = loadStoryboard(storyFile('at25.json', story), { root: ROOT });
  assert.ok(model.errors.some((item) => item.code === 'MASK_SOURCE_INVALID'));
  const cameraStory = baseStory([layer('move')]); cameraStory.scenes[0].camera = story.scenes[0].camera;
  const html = generateHtml(loadStoryboard(storyFile('at25-camera.json', cameraStory), { root: ROOT }));
  assert.match(html, /@keyframes camera-scene/);
});

test('AT26', () => {
  const story = baseStory([layer('bullets', 'text', { text: 'One\nTwo', bullets: [{ text: 'One' }, { text: 'Two' }], split: 'word' })]);
  const html = generateHtml(loadStoryboard(storyFile('at26.json', story), { root: ROOT }));
  assert.match(html, /class="bullet"/);
});

test('AT27', () => {
  const story = baseStory([layer('scatter', 'chart', { kind: 'scatter', categories: ['a', 'b'], series: [{ name: 's', xValues: [1], values: [2, 3] }] })]);
  const model = loadStoryboard(storyFile('at27.json', story), { root: ROOT });
  assert.ok(model.errors.some((item) => item.message.includes('equal lengths')));
  const good = loadStoryboard(path.join(ROOT, 'samples/explainer/storyboard.json'));
  assert.match(generateHtml(good), /<svg/);
});

test('AT28', () => {
  const story = { ...baseStory(), scenes: [
    { id: 'first', startMs: 1000, durationMs: 760, layers: [layer('one', 'text', { durationMs: 760, text: 'A' })] },
    { id: 'second', after: 'first', durationMs: 500, layers: [layer('two', 'text', { durationMs: 500, text: 'B' })] }
  ] };
  const model = loadStoryboard(storyFile('at28.json', story), { root: ROOT });
  assert.deepEqual(model.errors, []);
  assert.equal(model.scenes[1]._startMs, 1760);
  assert.equal(frameTimeMs(53), 1766);
});

test('AT29', async () => {
  makeTone(path.join(WORK, 'at29.wav'), 6);
  const wordFile = path.join(WORK, 'at29-words.json');
  const words = [
    ['We', 0, 500], ['can', 600, 1000], ['read.', 1100, 1500],
    ['Caption', 2200, 2800], ['boundary', 2850, 3500], ['has', 3550, 3850], ['exactly', 3900, 4350], ['forty', 4400, 4750], ['two', 4800, 5000], ['characters', 5050, 5550], ['in', 5600, 5750], ['two', 5800, 6000]
  ].map(([text, startMs, endMs]) => ({ text, startMs, endMs }));
  fs.writeFileSync(wordFile, JSON.stringify({ format: 'scene-engine/word-timings@1', language: 'en', words }));
  const story = baseStory([layer('words-title')], 7000);
  story.scenes[0].narration = { text: 'Read the words.', audio: 'out/.work/acceptance/at29.wav', audioOffsetMs: 200, wordTimings: 'out/.work/acceptance/at29-words.json' };
  story.scenes[0].captions = 'fromWordTimings';
  const model = loadStoryboard(storyFile('at29.json', story), { root: ROOT });
  assert.deepEqual(model.errors, []);
  assert.equal(model.scenes[0].captions.length, 2);
  assert.equal(model.scenes[0].captions[0].startMs, 200);
  assert.equal(model.scenes[0].captions[0].endMs, 1700);
  assert.ok(model.scenes[0].captions[1].text.includes('\n'));
  const output = path.join(OUT, 'tests', 'at29.vtt'); writeVtt(model, output);
  const vtt = fs.readFileSync(output, 'utf8'); assert.ok(vtt.startsWith('WEBVTT\n'));
  const overflow = structuredClone(story); overflow.scenes[0].durationMs = 5000;
  const overflowModel = loadStoryboard(storyFile('at29-overflow.json', overflow), { root: ROOT });
  await assert.rejects(renderStoryboard(overflowModel, { out: path.join(OUT, 'tests', 'at29-overflow.mp4'), renderer: 'fallback', captions: 'none' }), (error) => error.code === 'NARRATION_OVERFLOW' && error.exitCode === 1);
  assert.equal(fs.existsSync(path.join(OUT, 'tests', 'at29-overflow.mp4')), false);
});

test('AT30', () => {
  const story = { ...baseStory([layer('bg')]), durationMs: undefined, background: undefined };
  delete story.durationMs; delete story.background;
  const model = loadStoryboard(storyFile('at30.json', story), { root: ROOT });
  assert.equal(model.durationMs, 1000);
  assert.equal(model.story.background, undefined);
  assert.deepEqual(model.errors, []);
});

test('AT31', () => {
  const model = loadStoryboard(path.join(ROOT, 'samples/app-demo/storyboard.json'));
  assert.deepEqual(model.errors, []);
  const app = model.scenes[0].layers.find((item) => item.type === 'appDemo');
  assert.equal(app.viewport, 'layer-box-css-pixels');
  assert.ok(app.steps.some((step) => step.locator.role === 'button' && step.locator.name === 'Compare periods'));
});

test('AT32', () => {
  const title = layer('pose-title', 'text', {
    x: 1750, y: 80, width: 400, height: 220, scaleX: 1.5, scaleY: 1,
    bullets: [{ text: 'First point', kind: 'bullet', level: 0 }, { text: 'Second point', kind: 'number', level: 1 }],
    style: { fontFamily: 'SceneEngineMissingFont', fontSize: 36 },
    entrance: 'flyInLeft', entranceDurationMs: 500,
    tracks: [{ property: 'opacity', keyframes: [{ atMs: 0, value: 0 }, { atMs: 999, value: 0 }] }]
  });
  const story = baseStory([title]); story.scenes[0].pptxAtMs = 0;
  const filename = storyFile('at32.json', story); const output = path.join(OUT, 'tests', 'at32-timing.pptx');
  const document = exportPptx(filename, output);
  assert.equal(document.ok, true);
  const slide = zipText(output, 'ppt/slides/slide1.xml');
  assert.match(slide, /<p:animEffect[^>]*filter="fly\(left\)"/);
  assert.match(slide, /dur="500"/);
  assert.match(slide, /<a:buChar[^>]*char="•"/);
  assert.match(slide, /<a:buAutoNum[^>]*type="arabicPeriod"/);
  assert.doesNotMatch(slide, /• First point|1\. Second point/);
  assert.equal(document.result.roundTrip.status, 'pass');
  assert.equal(document.result.mappings.find((item) => item.layerId === 'pose-title').representation, 'native-text');
  assert.deepEqual(document.result.fontReport.find((item) => item.layerId === 'pose-title'), {
    sceneId: 'scene', layerId: 'pose-title', requested: 'SceneEngineMissingFont', emitted: 'Arial', status: 'substituted'
  });
  assert.deepEqual(new Set(document.result.poseWarnings.map((item) => item.code)), new Set(['PPTX_POSE_INVISIBLE', 'PPTX_POSE_CLIPPED', 'PPTX_TEXT_REFLOW']));
});

test('AT33', async (t) => {
  const svg = path.join(WORK, 'at33.svg');
  fs.writeFileSync(svg, '<svg xmlns="http://www.w3.org/2000/svg" width="120" height="80"><rect width="120" height="80" fill="#2563eb"/><circle cx="60" cy="40" r="20" fill="#ffffff"/></svg>');
  const first = { id: 'morph-start', startMs: 0, durationMs: 1000, layers: [
    layer('morph-title-one', 'text', { name: '!!shared-title', text: 'Schema-checked Morph title', width: 900, height: 100 }),
    layer('svg-mark', 'image', { src: 'out/.work/acceptance/at33.svg', width: 120, height: 80, alt: 'Blue mark' }),
    layer('schema-chart', 'chart', { kind: 'column', categories: ['A', 'B'], series: [{ name: 'Count', values: [3, 7] }] })
  ] };
  const second = { id: 'morph-end', after: 'morph-start', durationMs: 1000, layers: [
    layer('morph-title-two', 'text', { name: '!!shared-title', text: 'Schema-checked Morph title, continued', width: 1100, height: 100 })
  ] };
  const filename = storyFile('at33.json', { ...baseStory(), scenes: [first, second] });
  const output = path.join(OUT, 'tests', 'at33-morph.pptx');
  const document = exportPptx(filename, output);
  assert.equal(document.ok, true);
  assert.equal(document.result.openXmlValidation.status, 'pass');
  assert.ok(document.result.openXmlValidation.partsChecked >= 10);
  assert.equal(document.result.roundTrip.status, 'pass');
  assert.equal(document.result.roundTrip.libreOffice, 'pass');
  assert.match(zipText(output, 'ppt/slides/slide2.xml'), /p159:morph[^>]*option="byObject"/);
  assert.match(zipText(output, 'ppt/slides/slide1.xml'), /asvg:svgBlip r:embed="rId\d+"/);
  assert.match(zipText(output, 'ppt/slides/slide1.xml'), /name="svg-mark" descr="Blue mark"/);
  assert.ok(execFileSync('unzip', ['-Z1', output], { encoding: 'utf8' }).split('\n').some((name) => /^ppt\/media\/imageSvg\d+\.svg$/.test(name)));
  const keynotePdf = path.join(OUT, 'tests', 'at33-keynote.pdf');
  const keynote = await exportWithKeynote(output, keynotePdf);
  if (keynote.status === 'owner-check') {
    assert.equal(keynote.manualSteps[0], 'owner-check: grant Automation permission (Terminal/Codex → Keynote) and rerun npm run selftest -- --case AT36');
    t.diagnostic(keynote.manualSteps[0]);
  } else {
    assert.equal(keynote.status, 'pass');
    assert.ok(fs.statSync(keynotePdf).size > 0);
  }
});

test('AT34', () => {
  const categories = ['Jan', 'Feb', 'Mar']; const seriesData = [{ name: 'Visits', values: [10, 20, 30] }];
  const filename = storyFile('at34.json', baseStory([layer('formula-chart', 'chart', { kind: 'column', categories, series: seriesData })]));
  const output = path.join(OUT, 'tests', 'at34-valid.pptx'); const corrupt = path.join(OUT, 'tests', 'at34-corrupt.pptx');
  const document = exportPptx(filename, output, ['--no-verify']); assert.equal(document.ok, true);
  const expected = [{ layerId: 'formula-chart', chartPart: 'ppt/charts/chart1.xml', categories, seriesData }];
  const script = `import json,runpy,sys,zipfile\nsrc,dst,target,checks,writer=sys.argv[1:]\nchanged=False\nwith zipfile.ZipFile(src) as a, zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED) as b:\n  for item in a.infolist():\n    data=a.read(item.filename)\n    if item.filename=='ppt/charts/chart1.xml':\n      text=data.decode(); old='!$B$2:$B$4'; changed=old in text; data=text.replace(old,'!$B$2:$B$2',1).encode()\n    b.writestr(item,data)\nif not changed: raise SystemExit('formula fixture was not found')\nmodule=runpy.run_path(writer)\ntry: module['verify_and_publish'](dst,target,json.loads(checks))\nexcept module['PackageValidationError'] as error: print(json.dumps({'code':error.code,'details':error.details})); raise SystemExit(0)\nraise SystemExit('mismatched workbook passed validation')`;
  const target = path.join(OUT, 'tests', 'at34-should-not-publish.pptx'); fs.rmSync(target, { force: true });
  const result = spawnSync(path.join(ROOT, '.venv/bin/python'), ['-c', script, output, corrupt, target, JSON.stringify(expected), path.join(ROOT, 'src/pptx_writer.py')], { cwd: ROOT, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr || result.stdout);
  const validation = JSON.parse(result.stdout.trim());
  assert.equal(validation.code, 'PPTX_WORKBOOK_MISMATCH');
  assert.equal(validation.details[0].code, 'PPTX_WORKBOOK_MISMATCH');
  assert.equal(fs.existsSync(target), false);
});
test('AT35', () => {
  const story = baseStory([
    layer('playback-title', 'text', { text: 'Full storyboard playback', width: 700, height: 100, alt: 'Embedded video acceptance title' }),
    layer('playback-marker', 'shape', { x: 800, y: 120, width: 120, height: 120, decorative: true }),
    layer('app-footage', 'video', { src: 'out/tests/at15/capture.mp4', poster: 'out/tests/at18.png', muted: true })
  ], 1000);
  const filename = storyFile('at35.json', story);
  const output = path.join(OUT, 'tests', 'at35.pptx');
  const result = runCli(['export-pptx', filename, '--root', ROOT, '--out', output, '--embed-video', path.join(OUT, 'tests/at18.mp4'), '--verify']);
  assert.equal(result.ok, true);
  assert.equal(result.result.slideCount, 2);
  assert.ok(result.result.mappings.some((item) => item.representation === 'native-movie'));
  assert.equal(result.result.captionsEmbedded, false);
  const count = execFileSync(path.join(ROOT, '.venv/bin/python'), ['-c', "from pptx import Presentation; p=Presentation('" + output + "'); print(len(p.slides))"], { encoding: 'utf8' });
  assert.equal(Number(count.trim()), 2);
});
test('AT36', (t) => {
  const document = runCli(['selftest', '--case', 'AT36']);
  const smoke = document.result.cases.find((item) => item.id === 'AT36');
  assert.equal(document.ok, true);
  assert.equal(smoke.status, 'pass');
  assert.ok(['pass', 'owner-check'].includes(smoke.details.keynote.status));
  assert.equal(smoke.details.importRenderSmoke, smoke.details.keynote.status === 'pass');
  assert.equal(smoke.details.libreOffice.status, 'pass');
  assert.equal(smoke.details.powerpointBehaviorProven, false);
  if (smoke.details.keynote.status === 'owner-check') {
    assert.equal(smoke.details.keynote.manualSteps[0], 'owner-check: grant Automation permission (Terminal/Codex → Keynote) and rerun npm run selftest -- --case AT36');
    t.diagnostic(smoke.details.keynote.manualSteps[0]);
  } else assert.ok(fs.statSync(smoke.details.keynote.pdf).size > 0);
  assert.ok(fs.statSync(smoke.details.libreOffice.pdf).size > 0);
});
test('AT37 owner-check: current PowerPoint on Windows and Mac', (t) => {
  const document = runCli(['selftest', '--case', 'AT37']);
  const ownerCheck = document.result.cases.find((item) => item.id === 'AT37');
  assert.equal(document.ok, true);
  assert.equal(ownerCheck.status, 'owner-check');
  assert.ok(ownerCheck.manualSteps.length >= 3);
  t.skip('owner-check: release owner must record OS and PowerPoint builds, confirm AT33/AT35 open without repair, edit and retain chart data after save/reopen, verify Morph and entrance timing, and play embedded video.');
});

test('AT38', () => {
  const document = runCli(['validate', 'samples/explainer/storyboard.json', '--root', 'samples/explainer']);
  assert.deepEqual(Object.keys(document).sort(), ['command', 'errors', 'exitCode', 'files', 'format', 'ok', 'result', 'warnings']);
  for (const item of document.errors) for (const key of ['code', 'message', 'pointer', 'sceneId', 'layerId', 'frame', 'path', 'hint', 'severity']) assert.ok(key in item);
});

test('AT39', async (t) => {
  const port = await unusedPort(); const server = await startFixtureApp(port);
  t.after(() => server.kill('SIGTERM'));
  const appRoot = path.join(ROOT, 'samples/app-demo');
  const source = JSON.parse(fs.readFileSync(path.join(appRoot, 'storyboard.json'), 'utf8'));
  const scene = structuredClone(source.scenes[0]);
  scene.id = 'demo'; scene.durationMs = 1000; delete scene.captions; delete scene.narration;
  const selected = scene.layers.find((item) => item.type === 'appDemo');
  Object.assign(selected, { url: `http://127.0.0.1:${port}/`, durationMs: 1000, steps: [], cursor: [], highlights: [], appBuildId: 'fixture-v1' });
  const second = { ...structuredClone(selected), id: 'dashboard-demo-spare', appBuildId: 'fixture-v1-spare' };
  scene.layers = [selected, second];
  const story = { ...source, durationMs: 1000, scenes: [scene] };
  const filename = storyFile('at39.json', story);
  const captureDir = path.join(OUT, 'tests/at39/capture');
  const captureResult = await runCliAsync(['capture', filename, '--root', appRoot, '--scene', 'demo', '--layer', selected.id, '--out-dir', captureDir, '--timeout', '30000']);
  assert.equal(captureResult.code, 0, captureResult.stderr);
  const captureDocument = JSON.parse(captureResult.stdout.trim());
  assert.equal(captureDocument.result.layerId, selected.id);
  assert.equal(captureDocument.result.frameCount, 30);
  assert.equal(fs.readdirSync(path.join(captureDir, 'frames')).filter((name) => name.endsWith('.png')).length, 30);

  const reused = await runCliAsync(['render', filename, '--root', appRoot, '--frames-dir', captureDir, '--renderer', 'fallback', '--captions', 'none', '--out', path.join(OUT, 'tests/at39/reused.mp4'), '--timeout', '60000']);
  assert.equal(reused.code, 0, reused.stderr);
  assert.equal(JSON.parse(reused.stdout.trim()).result.frameCount, 30);

  selected.appBuildId = 'fixture-v2';
  const mismatchFile = storyFile('at39-build-mismatch.json', story);
  const mismatch = await runCliAsync(['render', mismatchFile, '--root', appRoot, '--frames-dir', captureDir, '--renderer', 'fallback', '--captions', 'none', '--out', path.join(OUT, 'tests/at39/rejected.mp4'), '--timeout', '60000']);
  assert.equal(mismatch.code, 2);
  assert.equal(JSON.parse(mismatch.stdout.trim()).errors[0].code, 'CAPTURE_MANIFEST_MISMATCH');
  assert.equal(fs.existsSync(path.join(OUT, 'tests/at39/rejected.mp4')), false);
});

test('MP4 comparison: second-scene tracks and captions use scene-local time (F2)', async () => {
  const story = { ...baseStory(), scenes: [
    { id: 'first', startMs: 0, durationMs: 1000, background: '#172033', layers: [layer('first-layer', 'text', { durationMs: 1000, text: 'First scene' })] },
    { id: 'second', startMs: 1000, durationMs: 1000, background: '#FFFFFF', captions: [{ startMs: 200, endMs: 800, text: 'Second scene caption' }], layers: [
      layer('second-moving', 'shape', { x: 100, y: 100, width: 180, height: 120, durationMs: 1000, fill: '#2563EB', tracks: [{ property: 'x', keyframes: [{ atMs: 0, value: 100 }, { atMs: 800, value: 600 }] }] })
    ] }
  ] };
  const model = loadStoryboard(storyFile('mp4-f2.json', story), { root: ROOT });
  assert.deepEqual(model.errors, []);
  await compareMp4WithCheck(model, 'f2-scene-local', [1500], { captions: 'burn-in' });
});

test('MP4 comparison: distinct tracks, easing, and end-value hold are rendered (F3)', async () => {
  const story = baseStory([layer('tracked-shape', 'shape', {
    x: 100, y: 120, width: 200, height: 140, fill: '#E4572E', durationMs: 1800,
    tracks: [
      { property: 'x', keyframes: [{ atMs: 0, value: 100, easing: 'ease-out' }, { atMs: 900, value: 600 }] },
      { property: 'opacity', keyframes: [{ atMs: 0, value: 0 }, { atMs: 300, value: 1 }] }
    ]
  })], 1800);
  const model = loadStoryboard(storyFile('mp4-f3.json', story), { root: ROOT });
  assert.deepEqual(model.errors, []);
  await compareMp4WithCheck(model, 'f3-tracks-easing-hold', [450, 1350], { regions: [{ x: 70, y: 80, width: 720, height: 260 }] });
});

test('MP4 comparison: supported schema motion features preserve visible content (F4)', async () => {
  const videoPath = path.join(WORK, 'mp4-comparison', 'f4-color.mp4');
  fs.mkdirSync(path.dirname(videoPath), { recursive: true });
  execFileSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i', 'color=c=red:s=320x180:r=30:d=0.5', '-f', 'lavfi', '-i', 'color=c=blue:s=320x180:r=30:d=1.5', '-filter_complex', '[0:v][1:v]concat=n=2:v=1:a=0[v]', '-map', '[v]', '-an', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', videoPath]);
  const story = baseStory([
    layer('counter', 'text', { x: 40, y: 30, width: 300, height: 80, durationMs: 1800, text: 'Revenue', counter: { from: 0, to: 18, decimals: 0, prefix: '$', suffix: 'M' } }),
    layer('bullets', 'text', { x: 40, y: 130, width: 400, height: 150, durationMs: 1800, text: 'Benefits', bullets: [{ text: 'First point', kind: 'bullet', level: 0 }, { text: 'Second point', kind: 'number', level: 1 }] }),
    layer('path', 'shape', { x: 520, y: 60, width: 400, height: 220, durationMs: 1800, shape: 'path', path: 'M 10 190 C 100 20 280 20 390 190', fill: '#FFFFFF', stroke: '#2563EB', strokeWidth: 12, trimStart: 0.12, trimEnd: 0.82 }),
    layer('line', 'shape', { x: 1000, y: 80, width: 260, height: 100, durationMs: 1800, shape: 'line', stroke: '#E4572E', strokeWidth: 10, strokeDash: 'dot', strokeDashOffset: 4 }),
    layer('video-entrance', 'video', { src: 'out/.work/acceptance/mp4-comparison/f4-color.mp4', x: 1300, y: 320, width: 320, height: 180, durationMs: 1800, entrance: 'fade', entranceDurationMs: 500 })
  ], 1800);
  const model = loadStoryboard(storyFile('mp4-f4.json', story), { root: ROOT });
  assert.deepEqual(model.errors, []);
  const staticAt = generateStaticHtml(model, 900);
  const references = await compareMp4WithCheck(model, 'f4-counter-bullets-shapes-video', [300, 900], { regions: [
    { x: 20, y: 20, width: 430, height: 280 },
    { x: 500, y: 40, width: 450, height: 260 },
    { x: 980, y: 60, width: 300, height: 150 },
    { x: 1280, y: 300, width: 380, height: 220 }
  ] });
  for (const renderer of MP4_RENDERERS) assertRgbPixelNear(references.get(`${renderer}:300`), 1470, 410, [255, 102, 102], 8, `${renderer} check frame must show the video at its authored 60% fade opacity`);
  for (const renderer of MP4_RENDERERS) assertRgbPixelNear(references.get(`${renderer}:900`), 1470, 410, [0, 0, 255], 8, `${renderer} check frame must seek to the video source time sampled at 900 ms`);
  assert.match(staticAt, /\$9M/);
  assert.match(staticAt, /First point/);
  assert.match(staticAt, /Second point/);
  assert.match(staticAt, /<path/);

  for (const unsupported of [
    layer('chart-build', 'chart', { kind: 'column', categories: ['A'], series: [{ name: 'S', values: [4] }], build: { mode: 'grow' } }),
    layer('chart-state', 'chart', { kind: 'column', categories: ['A'], series: [{ name: 'S', values: [4] }], dataStates: [{ atMs: 500, series: [{ name: 'S', values: [8] }] }] }),
    layer('masked', 'shape', { effects: { mask: { sourceLayerId: 'mask-source' } } })
  ]) {
    const rejected = loadStoryboard(storyFile(`mp4-f4-rejected-${unsupported.id}.json`, baseStory([unsupported])), { root: ROOT });
    assert.ok(rejected.errors.some((item) => item.code === 'FEATURE_UNSUPPORTED'), `${unsupported.id} must fail validation with FEATURE_UNSUPPORTED`);
  }
});

test('MP4 comparison: one-scene burn-in captions follow each cue interval (F7)', async () => {
  const authored = [layer('caption-test', 'text', { x: 100, y: 100, width: 500, height: 120, durationMs: 2000, text: 'Author layer' })];
  for (let index = 0; index < 5; index += 1) authored.push(layer(`caption-neighbor-${index}`, 'shape', { x: 40 + index * 180, y: 300, width: 80, height: 70, durationMs: 2000, fill: '#2563EB' }));
  const story = baseStory(authored, 2000);
  story.scenes[0].captions = [
    { startMs: 200, endMs: 600, text: 'First cue' },
    { startMs: 800, endMs: 1200, text: 'Second cue' },
    { startMs: 1400, endMs: 1700, text: 'Final cue' }
  ];
  const model = loadStoryboard(storyFile('mp4-f7.json', story), { root: ROOT });
  assert.deepEqual(model.errors, []);
  await compareMp4WithCheck(model, 'f7-burn-in-cues', [300, 900, 1350, 1800], { captions: 'burn-in', regions: [{ x: 120, y: 880, width: 1680, height: 180 }] });
});

test('check does not add a scene caption over an active author text layer (F7)', () => {
  const story = baseStory([layer('author-caption', 'text', { x: 100, y: 920, width: 500, height: 100, durationMs: 1000, text: 'Same words' })], 1000);
  story.scenes[0].captions = [{ startMs: 100, endMs: 900, text: 'Same words' }];
  const model = loadStoryboard(storyFile('mp4-f7-no-duplicate.json', story), { root: ROOT });
  const html = generateStaticHtml(model, 500);
  assert.equal([...html.matchAll(/Same words/g)].length, 1);
});

test('validate rejects captions that violate the explicit two-line 42-character lint (F7)', () => {
  const story = baseStory([], 1000);
  story.scenes[0].captions = [{ startMs: 100, endMs: 900, text: 'This cue is far too long to fit on one line and has no authored line break.' }];
  const model = loadStoryboard(storyFile('mp4-f7-lint.json', story), { root: ROOT });
  assert.ok(model.errors.some((item) => item.code === 'CAPTION_LINT'));
});

test('F6 scales the default render timeout and chooses fallback for the 57.5-second single scene', () => {
  assert.equal(defaultTimeoutForFrames(30), 33750);
  assert.equal(defaultTimeoutForFrames(1725), 245625);
  const fixture = loadStoryboard(path.join(ROOT, 'tests/fixtures/motion/storyboard.json'), { root: path.join(ROOT, 'tests/fixtures/motion') });
  assert.deepEqual(fixture.errors, []);
  assert.equal(fixture.frameCount, 1725);
  const selection = selectRenderer(fixture, 'auto');
  assert.equal(selection.name, 'fallback');
  assert.equal(selection.warning?.code, 'HYPERFRAMES_LONG_SINGLE_SCENE');
});

test('F6 pins renderer fonts locally and fails closed on an unbundled HyperFrames font', async (t) => {
  const story = baseStory([layer('font-check', 'text', { text: 'Pinned font', style: { fontFamily: 'Arial', fontSize: 36 } })]);
  const model = loadStoryboard(storyFile('f6-fonts.json', story), { root: ROOT });
  const html = generateHtml(model);
  assert.match(html, /data:font\/woff2;base64,/);
  assert.doesNotMatch(html, /fonts\.googleapis\.com|fonts\.gstatic\.com/);
  if (!fs.existsSync(path.join(ROOT, 'node_modules/.bin/hyperframes'))) return t.skip('HyperFrames is not installed');
  const unpinned = loadStoryboard(storyFile('f6-unpinned-font.json', baseStory([layer('font-check', 'text', { text: 'Unpinned', style: { fontFamily: 'Avenir Next' } })])), { root: ROOT });
  await assert.rejects(() => renderStoryboard(unpinned, { out: path.join(OUT, 'tests/f6-unpinned.mp4'), renderer: 'hyperframes' }), { code: 'FONT_UNPINNED' });
});

test('F8 resolves renderer assets from the install and writes --out outside the repository', async (t) => {
  const storyPath = storyFile('f8-outside-cwd.json', baseStory([layer('outside-path', 'shape')], 1000));
  const outDir = fs.mkdtempSync(path.join(os.tmpdir(), 'scene-engine-output-'));
  const output = path.join(outDir, 'outside.mp4');
  t.after(() => fs.rmSync(outDir, { recursive: true, force: true }));
  const result = await new Promise((resolve) => {
    const child = spawn(process.execPath, [CLI, 'render', storyPath, '--root', ROOT, '--renderer', 'fallback', '--captions', 'none', '--out', output], { cwd: os.tmpdir(), env: process.env, stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = ''; let stderr = '';
    child.stdout.on('data', (chunk) => stdout += chunk);
    child.stderr.on('data', (chunk) => stderr += chunk);
    child.once('close', (code) => resolve({ code, stdout, stderr }));
  });
  assert.equal(result.code, 0, result.stderr);
  assert.equal(JSON.parse(result.stdout.trim()).ok, true);
  assert.ok(fs.statSync(output).size > 0);
});

test('F2 check composites the captured app-demo frame used by its MP4', async (t) => {
  const appRoot = fs.mkdtempSync(path.join(WORK, 'f2-app-'));
  fs.writeFileSync(path.join(appRoot, 'index.html'), '<!doctype html><html><head><style>html,body{margin:0;width:640px;height:360px;background:#244E72;color:white;font:700 32px Arial;display:grid;place-items:center}</style></head><body><main data-ready>App report 27</main></body></html>');
  const port = await unusedPort(); const server = await startFixtureApp(port, appRoot);
  t.after(() => { server.kill('SIGTERM'); fs.rmSync(appRoot, { recursive: true, force: true }); });
  const app = layer('checked-dashboard', 'appDemo', { x: 500, y: 300, width: 640, height: 360, url: `http://127.0.0.1:${port}/`, readySelector: '[data-ready]', appBuildId: 'f2-fixture-v1', steps: [] });
  const filename = storyFile('f2-app-demo.json', baseStory([app], 1000));
  const model = loadStoryboard(filename, { root: appRoot });
  assert.deepEqual(model.errors, []);
  const movie = path.join(OUT, 'tests', 'f2-app-demo.mp4');
  const rendered = await renderStoryboard(model, { out: movie, renderer: 'fallback', captions: 'none', timeoutMs: 60000 });
  assert.equal(rendered.durationMs, 1000);
  const checkDir = path.join(OUT, 'tests', 'f2-app-demo-check'); fs.rmSync(checkDir, { recursive: true, force: true });
  const checked = await runCliAsync(['check', filename, '--root', appRoot, '--at', '500', '--rk', path.resolve(ROOT, '../render-kit/bin/rk'), '--out-dir', checkDir]);
  assert.equal(checked.code, 0, checked.stderr);
  const document = JSON.parse(checked.stdout.trim());
  const report = document.result.reports.find((entry) => entry.target === 'frame:500');
  assert.equal(report.status, 'pass');
  const checkImage = report.rk.report.outputs.png;
  assert.ok(fs.existsSync(checkImage));
  assertMeanAbsoluteFrameDifference(rawFrame(checkImage), rawFrame(movie, 500), 'fallback app-demo', 500);
});

test('F2 static app-demo check samples the scene camera at its requested time', () => {
  const story = baseStory([layer('camera-app', 'appDemo', { width: 320, height: 180, url: 'http://127.0.0.1:3000/', readySelector: '[data-ready]', appBuildId: 'f2-camera-v1' })]);
  story.scenes[0].camera = { tracks: [{ property: 'x', keyframes: [{ atMs: 0, value: 0 }, { atMs: 999, value: 140 }] }] };
  const model = loadStoryboard(storyFile('f2-camera-sample.json', story), { root: ROOT });
  const captureDir = path.join(WORK, 'f2-camera-capture'); const frameDir = path.join(captureDir, 'frames');
  fs.mkdirSync(frameDir, { recursive: true });
  fs.writeFileSync(path.join(frameDir, 'frame-000015.png'), Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jf9sAAAAASUVORK5CYII=', 'base64'));
  const html = generateStaticHtml(model, 500, { appCaptures: new Map([['camera-app', { directory: captureDir, frameCount: 30 }]]) });
  assert.match(html, /class="stage-app-frame"/);
  assert.match(html, /translate\(-70\.\d+px,-?0px\) scale\(1\) rotate\(0deg\)/);
});

test('F3 writes chartStyle and roundRect radius into the reopened PPTX XML', () => {
  const filename = storyFile('f3-chart-style.json', baseStory([
    layer('style-panel', 'shape', { shape: 'roundRect', x: 40, y: 40, width: 300, height: 140, radiusPx: 24, fill: '#F2F4F7' }),
    layer('styled-chart', 'chart', {
      x: 400, y: 40, width: 1200, height: 900, kind: 'line', categories: ['Step 1', 'Step 2', 'Step 3'],
      series: [{ name: 'Training', values: [0.8, 0.5, 0.2] }, { name: 'Validation', values: [0.9, 0.6, 0.3] }],
      style: { fontSize: 22, seriesColors: ['#0B6E4F', '#C44536'], axisTitleX: 'Step', axisTitleY: 'Loss', numberFormat: '0.00', gridColor: '#D9A441' }
    }),
    layer('combo-chart', 'chart', {
      x: 400, y: 500, width: 1200, height: 500, kind: 'combo', categories: ['A', 'B'],
      series: [
        { name: 'First line', kind: 'line', values: [1, 2] },
        { name: 'Middle bars', kind: 'column', values: [3, 4] },
        { name: 'Last line', kind: 'line', values: [5, 6] }
      ],
      style: { seriesColors: ['#112233', '#445566', '#778899'] }
    })
  ]));
  const output = path.join(OUT, 'tests', 'f3-chart-style.pptx');
  const document = exportPptx(filename, output, ['--no-verify']);
  assert.equal(document.ok, true);
  assert.equal(document.result.openXmlValidation.status, 'pass');
  let script = `import sys, zipfile, xml.etree.ElementTree as ET\nfrom pptx import Presentation\nfrom pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE\npath=sys.argv[1]\np=Presentation(path)\nshapes=[s for slide in p.slides for s in slide.shapes]\nchart_shape=next(s for s in shapes if s.has_chart)\nassert len(chart_shape.chart.series)==2\nassert any(s.name=='style-panel' and s.auto_shape_type==MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE for s in shapes)\nwith zipfile.ZipFile(path) as z:\n chart=ET.fromstring(z.read('ppt/charts/chart1.xml'))\n slide=ET.fromstring(z.read('ppt/slides/slide1.xml'))\nns={'c':'http://schemas.openxmlformats.org/drawingml/2006/chart','a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}\ncolors=[x.get('val') for x in chart.findall('.//c:ser/c:spPr/a:solidFill/a:srgbClr',ns)] + [x.get('val') for x in chart.findall('.//c:ser/c:spPr/a:ln/a:solidFill/a:srgbClr',ns)]\nassert '0B6E4F' in colors and 'C44536' in colors, colors\ntitles=[''.join(t.text or '' for t in x.findall('.//a:t',ns)) for x in chart.findall('.//c:catAx/c:title',ns)+chart.findall('.//c:valAx/c:title',ns)]\nassert any(t=='Step' for t in titles) and any(t=='Loss' for t in titles), titles\nassert any(x.get('formatCode')=='0.00' for x in chart.findall('.//c:valAx/c:numFmt',ns))\nassert any(x.get('val')=='D9A441' for x in chart.findall('.//c:valAx/c:majorGridlines/c:spPr/a:ln/a:solidFill/a:srgbClr',ns))\nassert any(x.get('sz')=='1100' for x in chart.findall('.//a:defRPr',ns)), 'chartStyle fontSize was not converted from px into PPTX points'\nshape=next(x for x in slide.findall('.//p:sp',ns) if any(n.get('name')=='style-panel' for n in x.findall('./p:nvSpPr/p:cNvPr',ns)))\nadj=shape.find('./p:spPr/a:prstGeom/a:avLst/a:gd',ns)\nassert adj is not None and adj.get('name')=='adj' and adj.get('fmla')=='val 17143', ET.tostring(shape,encoding='unicode')\nprint('python-pptx reopen + chartStyle XML + roundRect radius passed')`;
  script=script.replace('assert len(chart_shape.chart.series)==2', 'assert len(chart_shape.chart.series)==2\nassert sum(1 for s in shapes if s.has_chart)==2');
  script=script.replace(" slide=ET.fromstring(z.read('ppt/slides/slide1.xml'))", " slide=ET.fromstring(z.read('ppt/slides/slide1.xml'))\n combo=ET.fromstring(z.read('ppt/charts/chart2.xml'))");
  script=script.replace("shape=next(x for x in slide.findall", "combo_colors={ser.find('c:idx',ns).get('val'): next((x.get('val') for x in ser.findall('./c:spPr/a:solidFill/a:srgbClr',ns)+ser.findall('./c:spPr/a:ln/a:solidFill/a:srgbClr',ns)),None) for ser in combo.findall('.//c:ser',ns)}\nassert combo_colors=={'0':'112233','1':'445566','2':'778899'}, combo_colors\nshape=next(x for x in slide.findall");
  const inspect = execFileSync(path.join(ROOT, '.venv/bin/python'), ['-c', script, output], { encoding: 'utf8' });
  assert.match(inspect, /python-pptx reopen \+ chartStyle XML/);
});

test('F4 export, capture and check outputs resolve outside both repository and caller cwd', async (t) => {
  const callerCwd = fs.mkdtempSync(path.join(os.tmpdir(), 'scene-engine-foreign-cwd-'));
  const outputRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'scene-engine-foreign-output-'));
  const appRoot = path.join(callerCwd, 'app'); fs.mkdirSync(appRoot);
  fs.writeFileSync(path.join(appRoot, 'index.html'), '<!doctype html><html><body><main data-ready>Foreign cwd app</main></body></html>');
  t.after(() => { fs.rmSync(callerCwd, { recursive: true, force: true }); fs.rmSync(outputRoot, { recursive: true, force: true }); });
  const exportStory = storyFile('f4-export.json', baseStory([layer('title', 'text', { text: 'External output' })]), callerCwd);
  const deckPath = path.join(outputRoot, 'deck', 'external.pptx'); const reportPath = path.join(outputRoot, 'reports', 'export.json');
  const exported = await runCliAsync(['export-pptx', exportStory, '--root', ROOT, '--out', path.relative(callerCwd, deckPath), '--report', path.relative(callerCwd, reportPath), '--no-verify'], process.env, callerCwd);
  assert.equal(exported.code, 0, exported.stderr);
  assert.ok(fs.statSync(deckPath).size > 0); assert.ok(JSON.parse(fs.readFileSync(reportPath, 'utf8')).slideCount > 0);

  const port = await unusedPort(); const server = await startFixtureApp(port, appRoot); t.after(() => server.kill('SIGTERM'));
  const appStory = baseStory([layer('foreign-app', 'appDemo', { width: 320, height: 180, url: `http://127.0.0.1:${port}/`, readySelector: '[data-ready]', appBuildId: 'f4-foreign-v1', steps: [] })]);
  const appFilename = storyFile('f4-capture.json', appStory, callerCwd); const captureDir = path.join(outputRoot, 'capture');
  const captured = await runCliAsync(['capture', appFilename, '--root', appRoot, '--scene', 'scene', '--layer', 'foreign-app', '--out-dir', path.relative(callerCwd, captureDir)], process.env, callerCwd);
  assert.equal(captured.code, 0, captured.stderr); assert.ok(fs.existsSync(path.join(captureDir, 'manifest.json')));

  const checkStory = storyFile('f4-check.json', baseStory([layer('checked', 'shape')]), callerCwd); const checkDir = path.join(outputRoot, 'check');
  const checked = await runCliAsync(['check', checkStory, '--root', ROOT, '--rk', path.resolve(ROOT, '../render-kit/bin/rk'), '--out-dir', path.relative(callerCwd, checkDir)], process.env, callerCwd);
  assert.equal(checked.code, 0, checked.stderr); assert.ok(fs.existsSync(path.join(checkDir, 'stage-500.html')));
});

test('F5 same-origin fixtures and selectOption drive a staged error state; F12 highlights stay outline-only', async (t) => {
  const appRoot = fs.mkdtempSync(path.join(WORK, 'f5-app-'));
  fs.mkdirSync(path.join(appRoot, 'fixtures'), { recursive: true });
  fs.writeFileSync(path.join(appRoot, 'fixtures', 'error.json'), '{"message":"Staged error"}');
  fs.writeFileSync(path.join(appRoot, 'index.html'), `<!doctype html><html><head><style>html,body{margin:0;width:640px;height:360px;background:#fff;font:20px Arial}#mode{position:absolute;left:80px;top:40px;width:220px;height:42px}#result{position:absolute;left:80px;top:120px;width:400px;height:100px;background:#888;color:#fff;padding:16px;box-sizing:border-box}</style></head><body><select id="mode" data-ready><option value="normal">Normal</option><option value="error">Error</option></select><div id="result">Waiting</div><script>const mode=document.querySelector('#mode'),result=document.querySelector('#result');async function load(){try{const response=await fetch('/api?mode='+mode.value);const value=await response.json();result.textContent=value.message;result.style.background=response.ok?'#287A4B':'#FF0000'}catch{result.textContent='No fixture';result.style.background='#888'}}mode.addEventListener('change',load);load()</script></body></html>`);
  const port = await unusedPort(); const server = await startFixtureApp(port, appRoot);
  t.after(() => { server.kill('SIGTERM'); fs.rmSync(appRoot, { recursive: true, force: true }); });
  const app = layer('fixture-select', 'appDemo', {
    width: 640, height: 360, url: `http://127.0.0.1:${port}/`, readySelector: '#mode', appBuildId: 'f5-fixture-v1',
    fixtures: [{ urlPattern: `**/api\\?mode={error,success}`, status: 503, contentType: 'application/json', bodyFile: 'fixtures/error.json' }],
    steps: [{ atMs: 200, action: 'selectOption', locator: { css: '#mode' }, value: 'error' }],
    highlights: [{ locator: { css: '#mode' }, startMs: 300, durationMs: 500, color: '#FF3B30' }]
  });
  const filename = storyFile('f5-select-highlight.json', baseStory([app]));
  const result = await runCliAsync(['capture', filename, '--root', appRoot, '--scene', 'scene', '--layer', 'fixture-select', '--out-dir', path.join(OUT, 'tests/f5-select-highlight')]);
  assert.equal(result.code, 0, result.stderr);
  const capture = JSON.parse(result.stdout.trim());
  assert.equal(capture.result.fixtureCount, 1, 'the same-origin error request must be fulfilled by its fixture');
  const frame = rawPng(path.join(OUT, 'tests/f5-select-highlight', 'frames', 'frame-000020.png'));
  assert.deepEqual(rgbPixel(frame, 1280, 400, 320), [255, 0, 0], 'selectOption should reach the fixture-backed error state');
  assert.deepEqual(rgbPixel(frame, 1280, 8, 8), [255, 255, 255], 'highlight overlay must not tint the rest of the app frame');
  let orangeOutlinePixels = 0;
  for (let offset = 0; offset < frame.length; offset += 3) if (frame[offset] > 240 && frame[offset + 1] > 30 && frame[offset + 1] < 100 && frame[offset + 2] > 20 && frame[offset + 2] < 90) orangeOutlinePixels += 1;
  assert.ok(orangeOutlinePixels > 20, `expected a padded orange outline, found ${orangeOutlinePixels} pixels`);
});
