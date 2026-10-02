import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { spawn, execFileSync } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright';
import { writeComposition, writeVtt } from './html.mjs';
import { captureAppLayer, verifyReusableCapture } from './capture.mjs';
import { allLayers } from './scene.mjs';
import { frameCount, frameTimeMs } from './timeline.mjs';

const ENGINE_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

export function resolveOutputPath(filePath) { return path.resolve(filePath); }

async function spawnLogged(command, args, { cwd, env = process.env, timeoutMs = 30000, label = command, streamOutput = false } = {}) {
  return await new Promise((resolve, reject) => {
    const child = spawn(command, args, { cwd, env, stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = ''; let stderr = '';
    const timer = setTimeout(() => { child.kill('SIGKILL'); reject(Object.assign(new Error(`${label} timed out after ${timeoutMs} ms`), { code: 'RENDER_TIMEOUT', exitCode: 3, stdout, stderr })); }, timeoutMs);
    child.stdout.on('data', (chunk) => { const text = chunk.toString(); stdout += text; if (streamOutput) process.stderr.write(text); });
    child.stderr.on('data', (chunk) => { const text = chunk.toString(); stderr += text; if (streamOutput) process.stderr.write(text); });
    child.once('error', (error) => { clearTimeout(timer); reject(Object.assign(error, { code: 'PROCESS_FAILED', exitCode: 3 })); });
    child.once('close', (code, signal) => {
      clearTimeout(timer);
      if (code === 0) resolve({ stdout, stderr });
      else reject(Object.assign(new Error(`${label} exited ${code ?? signal}: ${(stderr.trim() || stdout.trim())}`), { code: 'RENDER_FAILED', exitCode: 3, stdout, stderr, processCode: code }));
    });
  });
}

function playwrightShell() {
  const cache = path.join(os.homedir(), 'Library', 'Caches', 'ms-playwright');
  const candidates = [
    path.join(cache, 'chromium_headless_shell-1243', 'chrome-headless-shell-mac-arm64', 'chrome-headless-shell'),
    path.join(cache, 'chromium_headless_shell-1243', 'chrome-headless-shell-mac-x64', 'chrome-headless-shell')
  ];
  return candidates.find((item) => fs.existsSync(item)) ?? null;
}

function hyperframesBinary() {
  const configured = process.env.SCENE_ENGINE_HYPERFRAMES_BIN;
  return configured ? path.resolve(configured) : path.join(ENGINE_ROOT, 'node_modules/.bin/hyperframes');
}

export function defaultTimeoutForFrames(frames) {
  return Math.min(900000, Math.max(30000, 30000 + Math.max(0, Number(frames) || 0) * 125));
}

export function selectRenderer(model, requested = 'auto') {
  if (requested !== 'auto') return { name: requested, warning: null };
  if (!fs.existsSync(hyperframesBinary())) return { name: 'fallback', warning: null };
  if (model.scenes.length === 1 && model.frameCount >= 1200) {
    return { name: 'fallback', warning: {
      code: 'HYPERFRAMES_LONG_SINGLE_SCENE',
      message: `The ${model.frameCount}-frame single-scene composition exceeds the tested HyperFrames range; using the frame-by-frame fallback renderer. The 57.5-second, 95-layer dogfood case stalled in HyperFrames.`
    } };
  }
  return { name: 'hyperframes', warning: null };
}

function assertFontsPinned(model) {
  for (const layer of model.scenes.flatMap(allLayers)) {
    const family = layer.style?.fontFamily;
    if (!family || ['Arial', 'Inter'].includes(String(family).trim())) continue;
    throw Object.assign(new Error(`Font '${family}' is not bundled with scene-engine; HyperFrames renders fail closed before attempting a font download.`), { code: 'FONT_UNPINNED', exitCode: 3, layerId: layer.id, fontFamily: String(family) });
  }
}

function probe(ffprobe, file) {
  const output = execFileSync(ffprobe, ['-v', 'error', '-show_streams', '-show_format', '-of', 'json', file], { encoding: 'utf8' });
  return JSON.parse(output);
}

function streamSummary(result) {
  return result.streams.map((stream) => ({
    type: stream.codec_type, codec: stream.codec_name,
    profile: stream.profile ?? null, level: stream.level ?? null,
    pix_fmt: stream.pix_fmt ?? null, width: stream.width ?? null, height: stream.height ?? null,
    frameRate: stream.avg_frame_rate ?? null, sampleRate: stream.sample_rate ? Number(stream.sample_rate) : null,
    channels: stream.channels ?? null, colorRange: stream.color_range ?? null,
    colorPrimaries: stream.color_primaries ?? null, colorTransfer: stream.color_transfer ?? null,
    colorSpace: stream.color_space ?? null
  }));
}

function assertProfile(probeResult, fileSize) {
  const video = probeResult.streams.find((stream) => stream.codec_type === 'video');
  const audio = probeResult.streams.find((stream) => stream.codec_type === 'audio');
  const failures = [];
  if (!String(probeResult.format?.format_name ?? '').split(',').includes('mp4')) failures.push('container is not MP4');
  if (!video || video.codec_name !== 'h264' || video.profile !== 'High' || video.level > 41 || video.pix_fmt !== 'yuv420p' || video.width !== 1920 || video.height !== 1080 || video.avg_frame_rate !== '30/1') failures.push('video must be H.264 High@4.1 or lower, yuv420p, 1920x1080 at 30/1');
  if (video && (video.color_primaries !== 'bt709' || video.color_transfer !== 'bt709' || video.color_space !== 'bt709' || video.color_range !== 'tv')) failures.push('video must carry limited-range BT.709 color tags');
  if (!audio || audio.codec_name !== 'aac' || audio.profile !== 'LC' || Number(audio.sample_rate) !== 48000 || audio.channels !== 2) failures.push('audio must be AAC-LC 48 kHz stereo');
  if (fileSize > 256 * 1024 * 1024) failures.push('video exceeds 256 MB');
  return failures;
}

function narrationInputs(model) {
  const inputs = [];
  for (const scene of model.scenes) {
    const narration = scene.narration;
    if (!narration?.audio) continue;
    const audioPath = path.resolve(model.root, narration.audio);
    const probeResult = probe('ffprobe', audioPath);
    const audio = probeResult.streams.find((stream) => stream.codec_type === 'audio');
    const audioDurationMs = Math.round(Number(probeResult.format?.duration ?? audio?.duration ?? 0) * 1000);
    const audioOffsetMs = narration.audioOffsetMs ?? 0;
    if (!audio || !audioDurationMs || audioOffsetMs + audioDurationMs > scene.durationMs) {
      throw Object.assign(new Error(`Narration audio exceeds scene '${scene.id}' (${audioOffsetMs + audioDurationMs} ms > ${scene.durationMs} ms).`), { code: 'NARRATION_OVERFLOW', exitCode: 1, sceneId: scene.id, path: audioPath, hint: 'Increase the authored scene duration or shorten the narration input.' });
    }
    if (narration.wordTimings) {
      const timingPath = path.resolve(model.root, narration.wordTimings);
      const timing = JSON.parse(fs.readFileSync(timingPath, 'utf8'));
      for (const [index, word] of (timing.words ?? []).entries()) if (word.endMs > audioDurationMs) throw Object.assign(new Error(`Word timing ${index} exceeds narration audio in scene '${scene.id}'.`), { code: 'NARRATION_OVERFLOW', exitCode: 1, sceneId: scene.id, path: timingPath, hint: 'Keep every word end within the probed audio duration.' });
    }
    inputs.push({ path: audioPath, offsetMs: scene._startMs + audioOffsetMs, gainDb: narration.gainDb ?? 0, sceneId: scene.id });
  }
  return inputs;
}

async function captureLayerMap(model, workDir, timeoutMs, framesDir) {
  const map = new Map();
  const appLayers = model.scenes.flatMap((scene) => (scene.layers ?? []).filter((layer) => layer.type === 'appDemo').map((layer) => ({ scene, layer })));
  if (framesDir) {
    let manifest;
    try { manifest = JSON.parse(fs.readFileSync(path.join(path.resolve(framesDir), 'manifest.json'), 'utf8')); }
    catch { throw Object.assign(new Error('Capture manifest is missing or invalid.'), { code: 'CAPTURE_MANIFEST_MISMATCH', exitCode: 2 }); }
    const selected = appLayers.filter(({ scene, layer }) => scene.id === manifest.sceneId && layer.id === manifest.layerId);
    if (selected.length !== 1) throw Object.assign(new Error('Capture manifest does not identify exactly one app-demo layer in this storyboard.'), { code: 'CAPTURE_MANIFEST_MISMATCH', exitCode: 2 });
    const [{ scene, layer }] = selected;
    const reused = await verifyReusableCapture(model, scene, layer, framesDir);
    map.set(layer.id, reused.videoPath);
    for (const entry of appLayers) {
      if (entry.layer.id === layer.id && entry.scene.id === scene.id) continue;
      const captureDir = path.join(workDir, `capture-${entry.layer.id}`);
      const result = await captureAppLayer(model, entry.scene, entry.layer, captureDir, { timeoutMs });
      map.set(entry.layer.id, result.videoPath);
    }
    return map;
  }
  for (const scene of model.scenes) {
    for (const layer of scene.layers ?? []) {
      if (layer.type !== 'appDemo') continue;
      const captureDir = path.join(workDir, `capture-${layer.id}`);
      const result = await captureAppLayer(model, scene, layer, captureDir, { timeoutMs });
      map.set(layer.id, result.videoPath);
    }
  }
  return map;
}

async function fallbackRender(htmlFile, workDir, durationMs, timeoutMs) {
  const framesDir = path.join(workDir, 'frames'); fs.mkdirSync(framesDir, { recursive: true });
  const context = await chromium.launchPersistentContext(path.join(workDir, 'browser-profile'), { headless: true, viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1, locale: 'en-US', timezoneId: 'UTC' });
  try {
    const page = await context.newPage();
    await page.goto(pathToFileURL(htmlFile).href, { waitUntil: 'load', timeout: timeoutMs });
    await page.evaluate(() => window.__sceneEngine.ready());
    const seekability = await page.evaluate(() => window.__sceneEngine.verifyAdapters());
    if (seekability.status === 'fail') throw Object.assign(new Error(seekability.message), { code: 'UNSEEKABLE', exitCode: 1, adapterId: seekability.adapterId, layerId: seekability.layerId, frame: seekability.frame });
    const total = frameCount(durationMs); const progressStep = Math.max(1, Math.ceil(total / 20));
    for (let i = 0; i < total; i += 1) {
      const time = frameTimeMs(i);
      await page.evaluate((t) => window.__sceneEngine.seek(t), time);
      await page.screenshot({ path: path.join(framesDir, `frame-${String(i).padStart(6, '0')}.png`), animations: 'allow', caret: 'hide' });
      if ((i + 1) % progressStep === 0 || i + 1 === total) process.stderr.write(`[scene-engine] fallback render ${Math.round((i + 1) / total * 100)}% (${i + 1}/${total} frames)\n`);
    }
  } finally { await context.close(); }
  const raw = path.join(workDir, 'fallback.mp4');
  await spawnLogged('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-framerate', '30', '-i', path.join(framesDir, 'frame-%06d.png'), '-an', '-c:v', 'libx264', '-crf', '22', '-preset', 'ultrafast', raw], { timeoutMs, label: 'fallback FFmpeg encode' });
  return raw;
}

async function verifySeekAdapters(htmlFile, timeoutMs) {
  const context = await chromium.launchPersistentContext(path.join(path.dirname(htmlFile), 'seek-probe-profile'), { headless: true, viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  try {
    const page = await context.newPage();
    await page.goto(pathToFileURL(htmlFile).href, { waitUntil: 'load', timeout: timeoutMs });
    await page.evaluate(() => window.__sceneEngine.ready());
    const result = await page.evaluate(() => window.__sceneEngine.verifyAdapters());
    if (result.status === 'fail') throw Object.assign(new Error(result.message), { code: 'UNSEEKABLE', exitCode: 1, adapterId: result.adapterId, layerId: result.layerId, frame: result.frame });
  } finally { await context.close(); }
}

async function hyperframesRender(htmlFile, raw, timeoutMs) {
  const binary = hyperframesBinary();
  const shell = playwrightShell();
  if (!fs.existsSync(binary)) throw Object.assign(new Error('Pinned HyperFrames CLI is not installed.'), { code: 'HYPERFRAMES_MISSING', exitCode: 3 });
  if (!shell) throw Object.assign(new Error('Playwright Chromium 1243 headless shell was not found in the user browser cache.'), { code: 'HYPERFRAMES_MISSING', exitCode: 3 });
  const env = { ...process.env, HYPERFRAMES_NO_TELEMETRY: '1', PRODUCER_HEADLESS_SHELL_PATH: shell };
  const compositionDir = path.dirname(htmlFile);
  try {
    const lint = await spawnLogged(binary, ['lint', compositionDir], { env, timeoutMs, label: 'HyperFrames lint', streamOutput: true });
  } catch (error) { throw Object.assign(error, { code: 'HYPERFRAMES_LINT_FAILED', exitCode: 1, message: `HyperFrames lint failed: ${error.message}` }); }
  try {
    const render = await spawnLogged(binary, ['render', compositionDir, '-o', raw, '--quality', 'delivery'], { env, timeoutMs, label: 'HyperFrames render', streamOutput: true });
  } catch (error) { throw Object.assign(error, { code: 'HYPERFRAMES_RENDER_FAILED', exitCode: 3, message: `HyperFrames render failed: ${error.message}` }); }
  return '0.8.78';
}

function audioGraph(audioInputs, durationMs, firstAudioInputIndex = 0, silenceIndex = audioInputs.length) {
  const durationSec = (durationMs / 1000).toFixed(3);
  const lines = [];
  const labels = [];
  for (let i = 0; i < audioInputs.length; i += 1) {
    const item = audioInputs[i]; const index = i + firstAudioInputIndex; const label = `voice${i}`;
    const gain = Number(item.gainDb).toFixed(2);
    lines.push(`[${index}:a]volume=${gain}dB,adelay=${Math.round(item.offsetMs)}:all=1,apad=whole_dur=${durationSec},atrim=duration=${durationSec},asetpts=PTS-STARTPTS[${label}]`);
    labels.push(`[${label}]`);
  }
  lines.push(`[${silenceIndex}:a]atrim=duration=${durationSec},asetpts=PTS-STARTPTS[silence]`);
  labels.push('[silence]');
  lines.push(`${labels.join('')}amix=inputs=${labels.length}:duration=longest:normalize=0,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[mix]`);
  return lines.join(';');
}

function loudnormStats(stderr) {
  const matches = [...stderr.matchAll(/\{\s*"input_i"[\s\S]*?\}/g)];
  if (!matches.length) throw new Error('FFmpeg loudnorm measurement JSON was missing.');
  return JSON.parse(matches.at(-1)[0]);
}

async function transcode(raw, target, durationMs, timeoutMs, narration = []) {
  const durationSec = (durationMs / 1000).toFixed(3);
  const base = ['-hide_banner', '-loglevel', 'error', '-y'];
  if (!narration.length) {
    const args = [...base, '-i', raw, '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=48000', '-t', durationSec, '-vf', 'scale=1920:1080:flags=lanczos,fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'fast', '-crf', '19', '-profile:v', 'high', '-level:v', '4.1', '-x264-params', 'colorprim=bt709:transfer=bt709:colormatrix=bt709:range=limited', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:a', 'aac', '-profile:a', 'aac_low', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-shortest', '-movflags', '+faststart', target];
    await spawnLogged('ffmpeg', args, { timeoutMs, label: 'FFmpeg delivery transcode' });
    return { mode: 'silent-aac', integratedTargetLufs: null, truePeakTargetDbtp: null };
  }
  const measurementInputs = [];
  for (const item of narration) measurementInputs.push('-i', item.path);
  const measurementSilence = narration.length;
  const measurementGraph = `${audioGraph(narration, durationMs, 0, measurementSilence)};[mix]loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json[normalized]`;
  const measured = await spawnLogged('ffmpeg', ['-hide_banner', '-loglevel', 'info', '-y', ...measurementInputs, '-f', 'lavfi', '-t', durationSec, '-i', 'anullsrc=channel_layout=stereo:sample_rate=48000', '-filter_complex', measurementGraph, '-map', '[normalized]', '-f', 'null', '-'], { timeoutMs, label: 'FFmpeg loudnorm measurement' });
  const stats = loudnormStats(measured.stderr);
  const renderInputs = [...base, '-i', raw];
  for (const item of narration) renderInputs.push('-i', item.path);
  const silenceIndex = narration.length + 1;
  const renderGraph = `${audioGraph(narration, durationMs, 1, silenceIndex)};[mix]loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=${stats.input_i}:measured_TP=${stats.input_tp}:measured_LRA=${stats.input_lra}:measured_thresh=${stats.input_thresh}:offset=${stats.target_offset}:linear=true:print_format=summary[normalized]`;
  const args = [...renderInputs, '-f', 'lavfi', '-t', durationSec, '-i', 'anullsrc=channel_layout=stereo:sample_rate=48000', '-filter_complex', renderGraph, '-map', '0:v:0', '-map', '[normalized]', '-t', durationSec, '-vf', 'scale=1920:1080:flags=lanczos,fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'fast', '-crf', '19', '-profile:v', 'high', '-level:v', '4.1', '-x264-params', 'colorprim=bt709:transfer=bt709:colormatrix=bt709:range=limited', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:a', 'aac', '-profile:a', 'aac_low', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-shortest', '-movflags', '+faststart', target];
  await spawnLogged('ffmpeg', args, { timeoutMs, label: 'FFmpeg delivery transcode' });
  return { mode: 'two-pass-loudnorm', integratedTargetLufs: -16, truePeakTargetDbtp: -1.5, inputIntegratedLufs: Number(stats.input_i), inputTruePeakDbtp: Number(stats.input_tp), inputLra: Number(stats.input_lra) };
}

export async function renderStoryboard(model, { out, renderer = 'auto', captions = 'sidecar', poster, framesDir, timeoutMs } = {}) {
  const finalPath = path.resolve(out);
  timeoutMs ??= defaultTimeoutForFrames(model.frameCount ?? frameCount(model.durationMs));
  fs.mkdirSync(path.dirname(finalPath), { recursive: true });
  const workParent = path.join(path.dirname(finalPath), '.work'); fs.mkdirSync(workParent, { recursive: true });
  const workDir = fs.mkdtempSync(path.join(workParent, 'render-'));
  const temporaryMp4 = path.join(workDir, 'delivery.mp4');
  const diagnostics = [];
  const selection = selectRenderer(model, renderer);
  const engine = selection.name;
  if (selection.warning) {
    diagnostics.push({ type: 'renderer-selection', ...selection.warning });
    process.stderr.write(`[scene-engine] Warning ${selection.warning.code}: ${selection.warning.message}\n`);
  }
  if (engine === 'hyperframes' && !fs.existsSync(hyperframesBinary())) throw Object.assign(new Error(`HyperFrames executable is unavailable: ${hyperframesBinary()}`), { code: 'HYPERFRAMES_MISSING', exitCode: 3, path: hyperframesBinary() });
  try {
    if (engine === 'hyperframes') assertFontsPinned(model);
    const narration = narrationInputs(model);
    const captureMap = await captureLayerMap(model, workDir, timeoutMs, framesDir);
    const compositionDir = path.join(workDir, 'composition');
    const assetDir = path.join(compositionDir, 'assets'); fs.mkdirSync(assetDir, { recursive: true });
    for (const layer of model.scenes.flatMap(allLayers)) {
      if (layer.type !== 'video' && layer.type !== 'appDemo') continue;
      const source = layer.type === 'video' ? path.resolve(model.root, layer.src) : captureMap.get(layer.id);
      if (!source) continue;
      const safeId = layer.id.replaceAll(/[^A-Za-z0-9_.-]/g, '_');
      const destination = path.join(assetDir, `${safeId}.mp4`);
      if (path.resolve(source) !== path.resolve(destination)) fs.copyFileSync(source, destination);
      captureMap.set(layer.id, destination);
    }
    const htmlFile = writeComposition(model, compositionDir, { captionMode: captions, captureMap });
    const raw = path.join(workDir, 'raw.mp4');
    let rendererVersion = null;
    await verifySeekAdapters(htmlFile, timeoutMs);
    if (engine === 'hyperframes') rendererVersion = await hyperframesRender(htmlFile, raw, timeoutMs);
    else { await fallbackRender(htmlFile, workDir, model.durationMs, timeoutMs); fs.renameSync(path.join(workDir, 'fallback.mp4'), raw); rendererVersion = process.version; }
    const audioNormalization = await transcode(raw, temporaryMp4, model.durationMs, timeoutMs, narration);
    diagnostics.push({ type: 'audio-normalization', ...audioNormalization });
    const probeResult = probe('ffprobe', temporaryMp4);
    const stat = fs.statSync(temporaryMp4);
    const profileErrors = assertProfile(probeResult, stat.size);
    if (profileErrors.length) throw Object.assign(new Error(profileErrors.join('; ')), { code: 'FFMPEG_PROFILE_MISMATCH', exitCode: 1, profileErrors });
    const posterPath = poster ? path.resolve(poster) : finalPath.replace(/\.mp4$/i, '.png');
    await spawnLogged('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-i', temporaryMp4, '-frames:v', '1', '-update', '1', posterPath], { timeoutMs, label: 'Poster extraction' });
    if (captions === 'sidecar' || captions === 'both') writeVtt(model, finalPath.replace(/\.mp4$/i, '.vtt'));
    fs.renameSync(temporaryMp4, finalPath);
    const files = [finalPath, posterPath];
    if (captions === 'sidecar' || captions === 'both') files.push(finalPath.replace(/\.mp4$/i, '.vtt'));
    const probeFinal = probe('ffprobe', finalPath);
    return {
      renderer: { name: engine, version: rendererVersion },
      durationMs: model.durationMs, frameCount: model.frameCount,
      streams: streamSummary(probeFinal), diagnostics, files
    };
  } catch (error) {
    fs.rmSync(finalPath, { force: true });
    fs.rmSync(temporaryMp4, { force: true });
    throw Object.assign(error, { diagnostics: error.diagnostics ?? diagnostics });
  } finally {
    fs.rmSync(workDir, { recursive: true, force: true });
  }
}
