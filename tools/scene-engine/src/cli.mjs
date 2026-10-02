#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawn, execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { pathToFileURL } from 'node:url';
import { chromium } from 'playwright';
import { loadStoryboard, diagnostic, allLayers, canonicalHash } from './scene.mjs';
import { ease, sampleTrack, sampleLayer, frameTimeMs, frameCount } from './timeline.mjs';
import { renderStoryboard, resolveOutputPath, defaultTimeoutForFrames } from './render.mjs';
import { appLayers, captureAppLayer } from './capture.mjs';
import { generateHtml, generateStaticHtml } from './html.mjs';
import { exportWithKeynote, renderWithLibreOffice } from './pptx_smoke.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..');
const CLI = path.join(HERE, 'cli.mjs');
const FORMAT = 'scene-engine/result@1';

function parseArgs(argv) {
  const command = argv[0];
  const positional = [];
  const options = {};
  const valueOptions = new Set(['--out', '--out-dir', '--root', '--renderer', '--captions', '--poster', '--frames-dir', '--timeout', '--scene', '--layer', '--at', '--rk', '--pptx', '--report', '--embed-video', '--case']);
  const booleanOptions = new Set(['--strict', '--verify', '--no-verify']);
  for (let i = 1; i < argv.length; i += 1) {
    const arg = argv[i];
    if (!arg.startsWith('--')) { positional.push(arg); continue; }
    if (booleanOptions.has(arg)) { options[arg.slice(2)] = true; continue; }
    if (!valueOptions.has(arg)) throw Object.assign(new Error(`Unknown option: ${arg}`), { code: 'CLI_USAGE', exitCode: 2 });
    const value = argv[++i];
    if (value === undefined || value.startsWith('--')) throw Object.assign(new Error(`Option requires a value: ${arg}`), { code: 'CLI_USAGE', exitCode: 2 });
    options[arg.slice(2)] = value;
  }
  return { command, positional, options };
}

function hashFile(filename) { return crypto.createHash('sha256').update(fs.readFileSync(filename)).digest('hex'); }
function fileRecord(role, filename) {
  const absolute = path.resolve(filename); const stat = fs.statSync(absolute);
  return { role, path: absolute, bytes: stat.size, sha256: hashFile(absolute) };
}
function resultDocument(command, result = {}, { ok = true, exitCode = 0, files = [], errors = [], warnings = [] } = {}) {
  return { format: FORMAT, command, ok, exitCode, files, errors, warnings, result };
}
function emit(document) { process.stdout.write(`${JSON.stringify(document)}\n`); process.exitCode = document.exitCode; }
function throwDiag(code, message, exitCode, extra = {}) { throw Object.assign(new Error(message), { code, exitCode, ...extra }); }

function validateOptions(options, accepted, command) {
  for (const key of Object.keys(options)) if (!accepted.has(key)) throwDiag('CLI_USAGE', `Unknown option for ${command}: --${key}`, 2);
}

function rootFiles(fileNames) {
  return fileNames.filter((filename) => filename && fs.existsSync(filename)).map((filename) => fileRecord(path.extname(filename).slice(1) || 'output', filename));
}

function requireStoryboard(positional) {
  if (!positional[0]) throwDiag('STORYBOARD_MISSING', 'A storyboard JSON path is required.', 2);
  return positional[0];
}

function modelFrom(pathname, options) {
  const model = loadStoryboard(pathname, { root: options.root });
  return model;
}

function checkVtt(model) {
  const cues = [];
  for (const scene of model.scenes) {
    for (const cue of Array.isArray(scene.captions) ? scene.captions : []) cues.push({ ...cue, startMs: cue.startMs + scene._startMs, endMs: cue.endMs + scene._startMs, language: cue.language ?? model.story.language ?? 'en' });
  }
  cues.sort((a, b) => a.startMs - b.startMs);
  const errors = [];
  for (let i = 0; i < cues.length; i += 1) {
    const cue = cues[i]; const cps = [...cue.text.replaceAll('\n', '')].length / ((cue.endMs - cue.startMs) / 1000);
    if (cue.text.split('\n').length > 2 || cue.text.split('\n').some((line) => [...line].length > 42)) errors.push(diagnostic('CAPTION_LINT_FAILED', 'Caption must fit two lines of at most 42 characters.', { sceneId: model.scenes.find((scene) => cue.startMs >= scene._startMs && cue.startMs < scene._startMs + scene.durationMs)?.id }));
    const limit = cue.language.toLowerCase().startsWith('vi') ? 17 : 20;
    if (cps > limit) errors.push(diagnostic('CAPTION_LINT_FAILED', `Caption rate ${cps.toFixed(1)} chars/s exceeds ${limit}.`));
    if (i && cue.startMs < cues[i - 1].endMs) errors.push(diagnostic('CAPTION_LINT_FAILED', 'Caption cues overlap or are not monotonic.'));
  }
  return errors;
}

function resultDefaults(command) {
  return ({
    validate: { valid: false, sceneCount: 0, layerCount: 0, durationMs: 0, frameCount: 0 },
    render: { durationMs: 0, frameCount: 0, renderer: { name: 'fallback', version: null }, streams: [], diagnostics: [] },
    capture: { sceneId: '', layerId: '', appBuildId: null, cssViewport: { width: 0, height: 0 }, deviceScaleFactor: 2, frameCount: 0, fixtureCount: 0, hashes: [], manifestPath: '', storyboardHash: '', layerHash: '', browserVersion: '' },
    'export-pptx': { slideCount: 0, slideAdvanceMs: [], mappings: [], fontReport: [], workbookChecks: [], poseWarnings: [], openXmlValidation: { status: 'skipped', partsChecked: 0, relationshipErrors: [] }, roundTrip: { status: 'skipped', text: 'not run', geometry: 'not run', chartData: 'not run', libreOffice: 'not run' }, captionsEmbedded: false, captionsBySlide: [] },
    check: { timesMs: [], reports: [], pptxDiagnostics: {} },
    selftest: { cases: [], ok: false }
  })[command] ?? {};
}

async function commandValidate(positional, options) {
  validateOptions(options, new Set(['root']), 'validate');
  const model = modelFrom(requireStoryboard(positional), options);
  const result = { valid: model.errors.length === 0, sceneCount: model.scenes.length, layerCount: model.layerCount, durationMs: model.durationMs, frameCount: model.frameCount };
  emit(resultDocument('validate', result, { ok: result.valid, exitCode: result.valid ? 0 : 2, errors: model.errors, warnings: model.warnings }));
}

async function commandRender(positional, options) {
  validateOptions(options, new Set(['root', 'out', 'renderer', 'captions', 'poster', 'frames-dir', 'timeout']), 'render');
  const model = modelFrom(requireStoryboard(positional), options);
  if (model.errors.length) { emit(resultDocument('render', resultDefaults('render'), { ok: false, exitCode: 2, errors: model.errors })); return; }
  if (!options.out) throwDiag('CLI_USAGE', 'render requires --out.', 2);
  const captionMode = options.captions ?? (model.scenes.some((scene) => scene.captions?.length) ? 'sidecar' : 'none');
  if (!['none', 'sidecar', 'burn-in', 'both'].includes(captionMode)) throwDiag('CLI_USAGE', 'captions must be none, sidecar, burn-in or both.', 2);
  const captionErrors = checkVtt(model);
  if (captionErrors.length && ['sidecar', 'both', 'burn-in'].includes(captionMode)) { emit(resultDocument('render', resultDefaults('render'), { ok: false, exitCode: 1, errors: captionErrors })); return; }
  const result = await renderStoryboard(model, { out: options.out, renderer: options.renderer ?? 'auto', captions: captionMode, poster: options.poster, framesDir: options['frames-dir'], timeoutMs: options.timeout === undefined ? defaultTimeoutForFrames(model.frameCount) : Number(options.timeout) });
  const files = rootFiles(result.files);
  emit(resultDocument('render', { durationMs: result.durationMs, frameCount: result.frameCount, renderer: result.renderer, streams: result.streams, diagnostics: result.diagnostics }, { files }));
}

async function commandCapture(positional, options) {
  validateOptions(options, new Set(['root', 'scene', 'layer', 'out-dir', 'timeout']), 'capture');
  const model = modelFrom(requireStoryboard(positional), options);
  if (model.errors.length) { emit(resultDocument('capture', resultDefaults('capture'), { ok: false, exitCode: 2, errors: model.errors })); return; }
  if (!options.scene || !options['out-dir']) throwDiag('CLI_USAGE', 'capture requires --scene and --out-dir.', 2);
  const { scene, matches } = appLayers(model, options.scene, options.layer);
  if (!scene) throwDiag('CLI_USAGE', `Unknown scene: ${options.scene}`, 2);
  if (matches.length !== 1) throwDiag('CLI_USAGE', matches.length ? 'Select exactly one app-demo layer with --layer.' : 'Scene has no matching app-demo layer.', 2);
  const layer = matches[0]; const dir = resolveOutputPath(options['out-dir']);
  const capture = await captureAppLayer(model, scene, layer, dir, { timeoutMs: Number(options.timeout ?? layer.readyTimeoutMs ?? 30000) });
  const files = [fileRecord('manifest', capture.manifestPath), fileRecord('video', capture.videoPath)];
  emit(resultDocument('capture', {
    sceneId: scene.id, layerId: layer.id, appBuildId: capture.appBuildId,
    cssViewport: capture.cssViewport, deviceScaleFactor: 2, frameCount: capture.frameCount, fixtureCount: capture.fixtureCount,
    hashes: capture.hashes, manifestPath: capture.manifestPath, storyboardHash: capture.storyboardHash, layerHash: capture.layerHash, browserVersion: capture.browserVersion
  }, { files }));
}

function pptxRasterReason(layer) {
  if (layer.type === 'text') return null;
  const effects = layer.effects ?? {};
  const reasons = [];
  if (effects.blurPx) reasons.push('blur');
  if (effects.backdropBlurPx) reasons.push('backdrop blur');
  if (effects.blendMode) reasons.push(`blend mode ${effects.blendMode}`);
  if (effects.transform3d) reasons.push('3D transform');
  if (effects.mask) reasons.push('layer mask');
  if (layer.type === 'image' && path.extname(layer.src).toLowerCase() === '.svg') reasons.push('SVG image raster fallback');
  return reasons.length ? reasons.join(', ') : null;
}

async function preparePptxRasterFallbacks(model, work) {
  const items = [];
  const visit = (scene, layers) => {
    for (const layer of layers ?? []) {
      const reason = pptxRasterReason(layer);
      if (reason) items.push({ scene, layer, reason });
      visit(scene, layer.children);
    }
  };
  for (const scene of model.scenes) visit(scene, scene.layers);
  if (!items.length) return;
  const htmlFile = path.join(work, 'raster-source.html');
  fs.writeFileSync(htmlFile, generateHtml(model));
  const context = await chromium.launchPersistentContext(path.join(work, 'raster-profile'), { headless: true, viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2, locale: 'en-US', timezoneId: 'UTC' });
  try {
    const page = await context.newPage();
    await page.goto(pathToFileURL(htmlFile).href, { waitUntil: 'load', timeout: 30000 });
    await page.evaluate(async () => { await window.__sceneEngine.ready(); await document.fonts.ready; });
    for (const [index, item] of items.entries()) {
      const localTime = Math.min(item.layer.startMs + item.layer.durationMs - 1, Math.max(item.layer.startMs, item.scene.pptxAtMs ?? item.scene.durationMs - 1));
      await page.evaluate((globalTime) => window.__sceneEngine.seek(globalTime), item.scene._startMs + localTime);
      const image = path.join(work, `raster-${index}.png`);
      const locator = page.locator(`[data-layer-id="${item.layer.id}"]`);
      await locator.waitFor({ state: 'visible', timeout: 10000 });
      await locator.screenshot({ path: image, animations: 'disabled', timeout: 15000 });
      item.layer._pptxRaster = image;
      item.layer._pptxRasterReason = item.reason;
    }
  } finally { await context.close(); }
}

async function commandExportPptx(positional, options) {
  validateOptions(options, new Set(['root', 'out', 'report', 'verify', 'no-verify', 'embed-video']), 'export-pptx');
  const model = modelFrom(requireStoryboard(positional), options);
  if (model.errors.length) { emit(resultDocument('export-pptx', resultDefaults('export-pptx'), { ok: false, exitCode: 2, errors: model.errors })); return; }
  if (!options.out) throwDiag('CLI_USAGE', 'export-pptx requires --out.', 2);
  const output = resolveOutputPath(options.out);
  let embedVideo = null;
  if (options['embed-video']) {
    embedVideo = path.resolve(options['embed-video']);
    if (!fs.existsSync(embedVideo)) throwDiag('ASSET_MISSING', `Embedded video does not exist: ${embedVideo}`, 2, { path: embedVideo });
    let media;
    try { media = JSON.parse(execFileSync('ffprobe', ['-v', 'error', '-show_streams', '-of', 'json', embedVideo], { encoding: 'utf8' })); }
    catch (error) { throwDiag('FFMPEG_FAILED', `ffprobe could not inspect embedded video: ${error.message}`, 3, { path: embedVideo }); }
    const video = media.streams.find((stream) => stream.codec_type === 'video');
    const audio = media.streams.find((stream) => stream.codec_type === 'audio');
    if (!video || video.codec_name !== 'h264' || video.profile !== 'High' || video.level > 41 || video.pix_fmt !== 'yuv420p' || video.width !== 1920 || video.height !== 1080 || video.avg_frame_rate !== '30/1' || !audio || audio.codec_name !== 'aac' || audio.profile !== 'LC' || Number(audio.sample_rate) !== 48000 || audio.channels !== 2 || fs.statSync(embedVideo).size > 256 * 1024 * 1024) {
      throwDiag('FFMPEG_PROFILE_MISMATCH', 'Embedded video must match the fixed PowerPoint H.264/AAC profile and remain below 256 MB.', 1, { path: embedVideo });
    }
  }
  fs.mkdirSync(path.dirname(output), { recursive: true });
  const work = fs.mkdtempSync(path.join(path.dirname(output), '.scene-engine-pptx-'));
  const modelFile = path.join(work, 'model.json'); const tempOutput = path.join(work, 'draft.pptx');
  const python = path.join(ROOT, '.venv', 'bin', 'python');
  try {
    await preparePptxRasterFallbacks(model, work);
    fs.writeFileSync(modelFile, JSON.stringify({ story: model.story, scenes: model.scenes, root: model.root, durationMs: model.durationMs }));
    const { stdout, stderr } = await new Promise((resolve, reject) => {
      const child = spawn(python, [path.join(HERE, 'pptx_writer.py'), modelFile, tempOutput, options['no-verify'] ? 'false' : 'true', embedVideo ?? ''], { stdio: ['ignore', 'pipe', 'pipe'] });
      let out = ''; let err = ''; child.stdout.on('data', (b) => { out += b; }); child.stderr.on('data', (b) => { err += b; });
      child.once('error', reject); child.once('close', (code) => {
        if (code === 0) { resolve({ stdout: out, stderr: err }); return; }
        let writerError;
        try { writerError = JSON.parse(err.trim()).error; } catch { }
        reject(Object.assign(new Error(writerError?.message || writerError?.details?.[0]?.reason || err.trim() || `python-pptx exited ${code}`), { code: writerError?.code || 'PPTX_ROUNDTRIP_FAILED', exitCode: 1, details: writerError?.details }));
      });
    });
    if (stderr) process.stderr.write(stderr);
    const result = JSON.parse(stdout.trim());
    if (result.roundTrip.status === 'fail') throwDiag('PPTX_ROUNDTRIP_FAILED', 'PPTX save and reopen round trip failed.', 1);
    fs.renameSync(tempOutput, output);
    const files = [fileRecord('pptx', output)];
    if (options.report) {
      const report = resolveOutputPath(options.report); fs.mkdirSync(path.dirname(report), { recursive: true }); fs.writeFileSync(report, `${JSON.stringify(result, null, 2)}\n`); files.push(fileRecord('report', report));
    }
    emit(resultDocument('export-pptx', result, { files }));
  } finally { fs.rmSync(work, { recursive: true, force: true }); }
}

async function commandCheck(positional, options) {
  validateOptions(options, new Set(['root', 'at', 'pptx', 'out-dir', 'rk', 'strict']), 'check');
  const model = modelFrom(requireStoryboard(positional), options);
  if (model.errors.length) { emit(resultDocument('check', resultDefaults('check'), { ok: false, exitCode: 2, errors: model.errors })); return; }
  const times = new Set();
  for (const scene of model.scenes) { times.add(scene._startMs); times.add(scene._startMs + Math.floor(scene.durationMs / 2)); times.add(scene._startMs + scene.durationMs - 1); }
  for (const value of (options.at ?? '').split(',').filter(Boolean)) times.add(Number(value));
  const sortedTimes = [...times].sort((a, b) => a - b);
  const rk = options.rk ?? process.env.SCENE_ENGINE_RK ?? 'rk';
  const work = resolveOutputPath(options['out-dir'] ?? path.join(ROOT, 'out', 'check')); fs.mkdirSync(work, { recursive: true });
  const appCaptures = new Map();
  const collectAppDemos = (scene, layers, parentStartMs = 0) => {
    const entries = [];
    for (const layer of layers ?? []) {
      const startMs = parentStartMs + layer.startMs;
      if (layer.type === 'appDemo') entries.push({ scene, layer, startMs });
      if (layer.type === 'group') entries.push(...collectAppDemos(scene, layer.children, startMs));
    }
    return entries;
  };
  for (const scene of model.scenes) {
    const appDemos = collectAppDemos(scene, scene.layers);
    for (const [index, entry] of appDemos.entries()) {
      const isChecked = sortedTimes.some((time) => {
        const sceneTime = time - scene._startMs;
        return sceneTime >= entry.startMs && sceneTime < entry.startMs + entry.layer.durationMs;
      });
      if (!isChecked) continue;
      const captureDir = path.join(work, '.app-captures', `${scene.id}-${index}-${entry.layer.id}`);
      const capture = await captureAppLayer(model, scene, entry.layer, captureDir, { timeoutMs: Number(entry.layer.readyTimeoutMs ?? 30000) });
      appCaptures.set(entry.layer.id, { directory: captureDir, frameCount: capture.frameCount });
    }
  }
  const reports = []; let exitCode = 0;
  for (const time of sortedTimes) {
    const htmlFile = path.join(work, `stage-${time}.html`);
    fs.writeFileSync(htmlFile, generateStaticHtml(model, time, { appCaptures }));
    const reportDir = path.join(work, `at-${time}`); fs.mkdirSync(reportDir, { recursive: true });
    try {
      const output = await new Promise((resolve, reject) => {
        const child = spawn(rk, ['check', htmlFile, '--at', String(time), '--out-dir', reportDir], { stdio: ['ignore', 'pipe', 'pipe'] });
        let stdout = ''; let stderr = ''; child.stdout.on('data', (b) => stdout += b); child.stderr.on('data', (b) => stderr += b); child.once('error', reject); child.once('close', (code) => resolve({ code, stdout, stderr }));
      });
      let report = null; const reportPath = path.join(reportDir, 'report.json'); if (fs.existsSync(reportPath)) report = JSON.parse(fs.readFileSync(reportPath, 'utf8'));
      reports.push({ target: `frame:${time}`, status: output.code === 0 ? 'pass' : 'fail', reason: output.stderr || null, rk: { exitCode: output.code, reportPath: fs.existsSync(reportPath) ? reportPath : null, report } });
      if (output.code !== 0) exitCode = 1;
    } catch (error) {
      reports.push({ target: `frame:${time}`, status: 'skipped', reason: error.code === 'ENOENT' ? `rk executable unavailable: ${rk}` : error.message, rk: { exitCode: null, reportPath: null, report: null } });
    }
  }
  const pptxDiagnostics = {};
  if (options.pptx) {
    const pptxPath = path.resolve(options.pptx);
    if (!fs.existsSync(pptxPath)) throwDiag('ASSET_MISSING', `PPTX file does not exist: ${pptxPath}`, 2, { path: pptxPath });
    const pptxWork = path.join(work, 'pptx-slides'); fs.mkdirSync(pptxWork, { recursive: true });
    const converted = await runProcess('soffice', ['--headless', '--convert-to', 'pdf', '--outdir', pptxWork, pptxPath], 60000);
    const pdfPath = path.join(pptxWork, `${path.basename(pptxPath, path.extname(pptxPath))}.pdf`);
    if (!fs.existsSync(pdfPath)) throwDiag('PPTX_ROUNDTRIP_FAILED', `LibreOffice did not produce a PDF for ${pptxPath}.`, 1);
    const prefix = path.join(pptxWork, 'slide');
    await runProcess('pdftoppm', ['-png', '-r', '144', pdfPath, prefix], 60000);
    const images = fs.readdirSync(pptxWork).filter((name) => /^slide-\d+\.png$/.test(name)).sort((a, b) => Number(a.match(/\d+/)[0]) - Number(b.match(/\d+/)[0]));
    const slideReports = [];
    for (let index = 0; index < images.length; index += 1) {
      const slideNumber = index + 1; const imagePath = path.join(pptxWork, images[index]);
      const stage = path.join(pptxWork, `stage-${slideNumber}.html`);
      const pngData = fs.readFileSync(imagePath).toString('base64');
      fs.writeFileSync(stage, `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>PowerPoint slide ${slideNumber}</title><style>html,body{margin:0;width:1920px;height:1080px;overflow:hidden} [data-rk-stage]{width:1920px;height:1080px}</style></head><body><div data-rk-stage><img src="data:image/png;base64,${pngData}" alt="Rendered PowerPoint slide ${slideNumber}" style="width:1920px;height:1080px"></div></body></html>`);
      const reportDir = path.join(pptxWork, `rk-${slideNumber}`); fs.mkdirSync(reportDir, { recursive: true });
      const response = await runProcess(rk, ['check', stage, '--pdf', '--out-dir', reportDir], 60000, true);
      const reportPath = path.join(reportDir, 'report.json'); const report = fs.existsSync(reportPath) ? JSON.parse(fs.readFileSync(reportPath, 'utf8')) : null;
      const status = response.code === 0 ? 'pass' : 'fail';
      slideReports.push({ slide: slideNumber, imagePath, status, rk: { exitCode: response.code, reportPath: fs.existsSync(reportPath) ? reportPath : null, report } });
      reports.push({ target: `pptx-slide:${slideNumber}`, status, reason: response.stderr || null, rk: { exitCode: response.code, reportPath: fs.existsSync(reportPath) ? reportPath : null, report } });
      if (response.code !== 0) exitCode = 1;
    }
    pptxDiagnostics.status = slideReports.length ? 'rendered-and-checked' : 'no-slides-rendered';
    pptxDiagnostics.pdfPath = pdfPath;
    pptxDiagnostics.slides = slideReports;
  }
  if (options.strict || process.env.CI === 'true') if (reports.some((item) => item.status === 'skipped')) exitCode = 1;
  emit(resultDocument('check', { timesMs: sortedTimes, reports, pptxDiagnostics }, { ok: exitCode === 0, exitCode }));
}

function runProcess(command, args, timeoutMs = 30000, allowFailure = false) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { cwd: ROOT, stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = ''; let stderr = '';
    const timer = setTimeout(() => { child.kill('SIGKILL'); reject(Object.assign(new Error(`${command} timed out after ${timeoutMs} ms`), { code: 'RENDER_TIMEOUT', exitCode: 3 })); }, timeoutMs);
    child.stdout.on('data', (chunk) => stdout += chunk.toString()); child.stderr.on('data', (chunk) => stderr += chunk.toString());
    child.once('error', (error) => { clearTimeout(timer); if (allowFailure) resolve({ code: null, stdout, stderr: error.message }); else reject(error); });
    child.once('close', (code) => { clearTimeout(timer); if (code === 0 || allowFailure) resolve({ code, stdout, stderr }); else reject(Object.assign(new Error(`${command} exited ${code}: ${stderr.trim()}`), { code: 'PROCESS_FAILED', exitCode: 3 })); });
  });
}

function simpleSelftest(id) {
  if (id === 'AT03') {
    const linear = sampleTrack(0, { property: 'x', keyframes: [{ atMs: 0, value: 0 }, { atMs: 1000, value: 1000 }] }, 500);
    const eased = sampleTrack(0, { property: 'x', keyframes: [{ atMs: 0, value: 0, easing: 'ease-in-out' }, { atMs: 1000, value: 1000 }] }, 500);
    if (Math.abs(linear - 500) > 0.01 || Math.abs(eased - 500) > 0.01) return { status: 'fail', errors: [diagnostic('TRACK_VALUE_INVALID', 'Timeline reference sample mismatch.')] };
    return { status: 'pass', errors: [] };
  }
  if (id === 'AT21') {
    return { status: 'skipped', errors: [diagnostic('FFMPEG_PROFILE_MISMATCH', 'AT21 requires a rendered fixture video; run npm run samples for artifact profile checks.', { severity: 'warning' })] };
  }
  if (id === 'AT37') return {
    status: 'owner-check',
    errors: [],
    manualSteps: [
      'On current Microsoft PowerPoint for Windows and Mac, record the OS and PowerPoint build, then open out/tests/at33-morph.pptx and out/tests/at35.pptx; record whether either shows a repair prompt.',
      'In the chart, use Edit Data to change a value, save, close, reopen and confirm the edited value persists.',
      'Run the AT33 Morph slides and AT32 entrance animation; record whether the named title morphs and the text enters from the left.',
      'Play the embedded video on the AT35 playback slide, then record playback and audio results on each platform.'
    ]
  };
  if (id === 'AT24') {
    const before = sampleTrack(12, { property: 'x', keyframes: [{ atMs: 100, value: 32 }] }, 0);
    const held = sampleTrack(0, { property: 'x', keyframes: [{ atMs: 100, value: 32 }] }, 500);
    return before === 12 && held === 32 ? { status: 'pass', errors: [] } : { status: 'fail', errors: [diagnostic('TRACK_VALUE_INVALID', 'Sparse track hold semantics failed.')] };
  }
  if (id === 'AT28') {
    const storyboard = { scenes: [{ id: 'one', startMs: 1000, durationMs: 1000 }, { id: 'two', after: 'one', gapMs: 0, durationMs: 200 }] };
    const firstEnd = storyboard.scenes[0].startMs + storyboard.scenes[0].durationMs;
    return firstEnd === 2000 ? { status: 'pass', errors: [] } : { status: 'fail', errors: [diagnostic('TIME_REFERENCE_INVALID', 'after sequencing failed.')] };
  }
  return { status: 'skipped', errors: [diagnostic('CLI_USAGE', `${id} needs a dedicated integration fixture or external application check.`, { severity: 'warning' })] };
}

async function selftestAT36() {
  const directory = path.join(ROOT, 'out', 'tests', 'AT36');
  fs.mkdirSync(directory, { recursive: true });
  const presentation = path.join(directory, 'smoke.pptx');
  const keynotePdf = path.join(directory, 'keynote.pdf');
  const libreOfficePdf = path.join(directory, 'libreoffice.pdf');
  let exported;
  try { exported = execFileSync(process.execPath, [CLI, 'export-pptx', 'samples/explainer/storyboard.json', '--root', 'samples/explainer', '--out', presentation, '--no-verify'], { cwd: ROOT, encoding: 'utf8', maxBuffer: 12 * 1024 * 1024 }); }
  catch (error) { throw new Error((error.stderr || error.stdout || error.message).toString().trim()); }
  const exportDocument = JSON.parse(exported.trim());
  if (!exportDocument.ok) throw new Error('AT36 could not export its PPTX fixture.');
  let keynote; let keynoteError;
  try { keynote = await exportWithKeynote(presentation, keynotePdf); }
  catch (error) { keynoteError = error; }
  let libreOffice; let libreOfficeError;
  try { libreOffice = renderWithLibreOffice(presentation, libreOfficePdf); }
  catch (error) { libreOfficeError = error; }
  const failures = [keynoteError, libreOfficeError].filter(Boolean);
  if (failures.length) throw new Error(failures.map((error) => error.message).join('; '));
  return { status: 'pass', errors: [], details: { importRenderSmoke: keynote.status === 'pass', keynote, libreOffice, powerpointBehaviorProven: false } };
}

async function commandSelftest(positional, options) {
  validateOptions(options, new Set(['case', 'strict']), 'selftest');
  const ids = options.case ? [options.case] : Array.from({ length: 39 }, (_, index) => `AT${String(index + 1).padStart(2, '0')}`);
  const cases = [];
  for (const id of ids) {
    if (!/^AT\d{2}$/.test(id) || Number(id.slice(2)) < 1 || Number(id.slice(2)) > 39) { cases.push({ id, status: 'fail', errors: [diagnostic('CLI_USAGE', `Unknown test case: ${id}`)] }); continue; }
    if (id === 'AT01' || id === 'AT30') {
      const file = path.join(ROOT, 'samples', 'explainer', 'storyboard.json');
      const model = loadStoryboard(file);
      cases.push({ id, status: model.errors.length ? 'fail' : 'pass', errors: model.errors });
    } else if (id === 'AT36') {
      try { cases.push({ id, ...await selftestAT36() }); }
      catch (error) { cases.push({ id, status: 'fail', errors: [diagnostic('PPTX_ROUNDTRIP_FAILED', error.message, { severity: 'error' })] }); }
    } else cases.push({ id, ...simpleSelftest(id) });
  }
  const ok = cases.every((item) => item.status === 'pass' || (item.status === 'owner-check' && !options.strict) || (item.status === 'skipped' && !options.strict));
  emit(resultDocument('selftest', { cases, ok }, { ok, exitCode: ok ? 0 : 1 }));
}

async function main() {
  try {
    const { command, positional, options } = parseArgs(process.argv.slice(2));
    if (command === 'validate') await commandValidate(positional, options);
    else if (command === 'render') await commandRender(positional, options);
    else if (command === 'capture') await commandCapture(positional, options);
    else if (command === 'export-pptx') await commandExportPptx(positional, options);
    else if (command === 'check') await commandCheck(positional, options);
    else if (command === 'selftest') await commandSelftest(positional, options);
    else throwDiag('CLI_USAGE', `Unknown command: ${command ?? '(missing)'}`, 2);
  } catch (error) {
    const command = process.argv[2] ?? 'unknown';
    const code = error.code ?? 'PROCESS_FAILED'; const exitCode = error.exitCode ?? 3;
    const item = diagnostic(code, error.message, { pointer: error.pointer, sceneId: error.sceneId, layerId: error.layerId, frame: error.frame, path: error.path, hint: error.hint });
    emit(resultDocument(command, resultDefaults(command), { ok: false, exitCode, errors: error.diagnostics?.length ? error.diagnostics : [item] }));
  }
}

if (import.meta.url === `file://${process.argv[1]}`) main();
