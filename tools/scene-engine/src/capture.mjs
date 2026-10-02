import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';
import { frameCount, frameTimeMs } from './timeline.mjs';
import { canonicalHash, diagnostic } from './scene.mjs';

function sha256(data) { return crypto.createHash('sha256').update(data).digest('hex'); }
function fixtureBodyHashes(model, layer) {
  return (layer.fixtures ?? []).map((fixture) => ({
    urlPattern: fixture.urlPattern,
    method: (fixture.method ?? 'GET').toUpperCase(),
    sha256: sha256(fs.readFileSync(path.resolve(model.root, fixture.bodyFile)))
  }));
}
function globRegex(glob) {
  const toSource = (pattern) => {
    let source = '';
    for (let index = 0; index < pattern.length; index += 1) {
      const char = pattern[index];
      if (char === '\\' && index + 1 < pattern.length) {
        source += pattern[++index].replace(/[|\\{}()[\]^$+?.*]/g, '\\$&');
      } else if (char === '*' && pattern[index + 1] === '*') {
        if (pattern[index + 2] === '/') { source += '(?:.*/)?'; index += 2; }
        else { source += '.*'; index += 1; }
      } else if (char === '*') source += '[^/]*';
      else if (char === '?') source += '[^/]';
      else if (char === '{') {
        let depth = 1; let close = index + 1; const alternatives = []; let part = '';
        for (; close < pattern.length; close += 1) {
          const item = pattern[close];
          if (item === '\\' && close + 1 < pattern.length) { part += item + pattern[++close]; continue; }
          if (item === '{') depth += 1;
          else if (item === '}') {
            depth -= 1;
            if (depth === 0) { alternatives.push(part); break; }
          }
          if (item === ',' && depth === 1) { alternatives.push(part); part = ''; }
          else part += item;
        }
        if (depth === 0 && alternatives.length > 1) {
          source += `(?:${alternatives.map(toSource).join('|')})`;
          index = close;
        } else source += '\\{';
      } else source += char.replace(/[|\\()[\]^$+?.{}]/g, '\\$&');
    }
    return source;
  };
  return new RegExp(`^${toSource(String(glob))}$`);
}

function locatorFor(page, locator) {
  if (locator?.role) return page.getByRole(locator.role, { name: locator.name, exact: true });
  if (locator?.testId) return page.getByTestId(locator.testId);
  return page.locator(locator?.css ?? '');
}

async function locateUnique(page, selector, timeoutMs, stepIndex) {
  const locator = locatorFor(page, selector);
  try { await locator.first().waitFor({ state: 'visible', timeout: timeoutMs }); }
  catch { throw Object.assign(new Error(`Step ${stepIndex} locator was not found: ${JSON.stringify(selector)}`), { code: 'STEP_LOCATOR_NOT_FOUND', stepIndex, locator: selector, exitCode: 3 }); }
  const count = await locator.count();
  if (count !== 1) throw Object.assign(new Error(`Step ${stepIndex} locator matched ${count} elements: ${JSON.stringify(selector)}`), { code: 'STEP_LOCATOR_AMBIGUOUS', stepIndex, locator: selector, exitCode: 3 });
  return locator;
}

async function applyStep(page, step, index, layer) {
  const timeout = step.timeoutMs ?? 5000;
  if (step.action === 'goto') {
    if (!/^http:\/\/(127\.0\.0\.1|localhost)(:\d+)?\//.test(step.url ?? '')) throw Object.assign(new Error(`Step ${index} URL must be localhost.`), { code: 'SCHEMA_INVALID', stepIndex: index, exitCode: 2 });
    await page.goto(step.url, { waitUntil: 'domcontentloaded', timeout });
    return;
  }
  const locator = await locateUnique(page, step.locator, timeout, index);
  if (step.action === 'click') await locator.click({ timeout });
  else if (step.action === 'fill') await locator.fill(step.value, { timeout });
  else if (step.action === 'selectOption') await locator.selectOption(step.value, { timeout });
  else if (step.action === 'press') await locator.press(step.key, { timeout });
  else if (step.action === 'waitFor') await locator.waitFor({ state: 'visible', timeout });
  void layer;
}

function sampleCursor(points, time) {
  if (!points?.length) return null;
  if (time <= points[0].atMs) return points[0];
  for (let i = 1; i < points.length; i += 1) {
    const right = points[i]; const left = points[i - 1];
    if (time <= right.atMs) {
      const progress = (time - left.atMs) / (right.atMs - left.atMs);
      return { x: left.x + (right.x - left.x) * progress, y: left.y + (right.y - left.y) * progress, click: Boolean(right.click && time === right.atMs) };
    }
  }
  return points.at(-1);
}

async function updateOverlays(page, layer, time) {
  const cursor = sampleCursor(layer.cursor, time);
  const highlightRects = [];
  for (const highlight of layer.highlights ?? []) {
    if (time < highlight.startMs || time >= highlight.startMs + highlight.durationMs) continue;
    const locator = await locateUnique(page, highlight.locator, 50, 'highlight');
    const box = await locator.boundingBox();
    if (box) highlightRects.push({ ...box, color: highlight.color ?? '#FF3B30' });
  }
  await page.evaluate(({ cursorPose, rects }) => {
    document.querySelector('#scene-engine-capture-overlay')?.remove();
    const root = document.createElement('div'); root.id = 'scene-engine-capture-overlay';
    Object.assign(root.style, { position: 'fixed', inset: '0', zIndex: '2147483647', pointerEvents: 'none' });
    for (const rect of rects) {
      const box = document.createElement('div');
      const padding = 6;
      Object.assign(box.style, { position: 'absolute', left: `${rect.x - padding}px`, top: `${rect.y - padding}px`, width: `${rect.width + padding * 2}px`, height: `${rect.height + padding * 2}px`, boxSizing: 'border-box', border: `4px solid ${rect.color}`, borderRadius: '8px' });
      root.append(box);
    }
    if (cursorPose) {
      const pointer = document.createElement('div');
      Object.assign(pointer.style, { position: 'absolute', left: `${cursorPose.x}px`, top: `${cursorPose.y}px`, width: '22px', height: '22px', background: '#111827', border: '3px solid white', borderRadius: '50%', boxShadow: '0 1px 8px #0008', transform: 'translate(-50%,-50%)' });
      root.append(pointer);
      if (cursorPose.click) { const ring = document.createElement('div'); Object.assign(ring.style, { position: 'absolute', left: `${cursorPose.x}px`, top: `${cursorPose.y}px`, width: '44px', height: '44px', border: '3px solid #2563EB', borderRadius: '50%', transform: 'translate(-50%,-50%)' }); root.append(ring); }
    }
    document.documentElement.append(root);
  }, { cursorPose: cursor, rects: highlightRects });
}

export async function captureAppLayer(model, scene, layer, outDir, { timeoutMs = 30000, ffmpeg = 'ffmpeg' } = {}) {
  const errors = [];
  const destination = path.resolve(outDir);
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  const temp = `${destination}.tmp-${process.pid}-${Date.now()}`;
  fs.rmSync(temp, { recursive: true, force: true }); fs.mkdirSync(path.join(temp, 'frames'), { recursive: true });
  let context;
  try {
    context = await chromium.launchPersistentContext(path.join(temp, 'browser-profile'), {
      headless: true,
      viewport: { width: Math.max(1, Math.round(layer.width)), height: Math.max(1, Math.round(layer.height)) },
      deviceScaleFactor: 2, locale: layer.locale ?? 'en-US', timezoneId: layer.timeZoneId ?? 'UTC',
      colorScheme: 'light', reducedMotion: 'reduce'
    });
    const browserVersion = context.browser()?.version() ?? 'unknown';
    const page = await context.newPage();
    await page.addInitScript(() => {
      const probe = { contexts: [], rafScheduled: false };
      Object.defineProperty(window, '__sceneEngineCaptureProbe', { value: probe, configurable: false });
      const getContext = HTMLCanvasElement.prototype.getContext;
      HTMLCanvasElement.prototype.getContext = function (type, ...args) {
        const context = getContext.call(this, type, ...args);
        if (context) probe.contexts.push({ type: String(type).toLowerCase(), id: this.id || null });
        return context;
      };
      const requestAnimationFrame = window.requestAnimationFrame.bind(window);
      window.requestAnimationFrame = (callback) => {
        probe.rafScheduled = true;
        return requestAnimationFrame(callback);
      };
      window.__sceneEngineAdapters = window.__sceneEngineAdapters || [];
    });
    const origin = new URL(layer.url).origin;
    const fixtures = (layer.fixtures ?? []).map((fixture) => ({ ...fixture, regex: globRegex(fixture.urlPattern), method: (fixture.method ?? 'GET').toUpperCase() }));
    let fixtureCount = 0; let blockedUrl = null;
    await page.route('**/*', async (route) => {
      const request = route.request(); const url = request.url();
      if (url.startsWith('data:') || url.startsWith('file:')) return route.continue();
      const fixture = fixtures.find((item) => item.method === request.method().toUpperCase() && item.regex.test(url));
      if (fixture) {
        fixtureCount += 1;
        return route.fulfill({ status: fixture.status, contentType: fixture.contentType ?? 'application/octet-stream', body: fs.readFileSync(path.resolve(model.root, fixture.bodyFile)) });
      }
      let requestOrigin = '';
      try { requestOrigin = new URL(url).origin; } catch { }
      if (requestOrigin === origin) return route.continue();
      blockedUrl = url;
      return route.abort('blockedbyclient');
    });
    const appTimeout = timeoutMs || layer.readyTimeoutMs || 30000;
    try {
      await page.goto(layer.url, { waitUntil: 'domcontentloaded', timeout: appTimeout });
      await page.waitForSelector(layer.readySelector, { state: 'visible', timeout: appTimeout });
    } catch (error) {
      const code = blockedUrl ? 'FIXTURE_NOT_FOUND' : 'APP_LOAD_FAILED';
      throw Object.assign(new Error(blockedUrl ? `External request had no fixture: ${blockedUrl}` : `App did not reach ready selector '${layer.readySelector}' at ${layer.url}: ${error.message}`), { code, url: blockedUrl ?? layer.url, selector: layer.readySelector, exitCode: 3 });
    }
    const canvasState = await page.evaluate((lastFrame) => {
      const adapters = window.__sceneEngineAdapters ?? [];
      const adapterFailures = [];
      for (const adapter of adapters) {
        try {
          if (adapter.seekFrame(lastFrame, Math.floor(lastFrame * 1000 / 30)) === false || adapter.seekFrame(0, 0) === false || adapter.seekFrame(lastFrame, Math.floor(lastFrame * 1000 / 30)) === false) throw new Error('adapter rejected backward/forward seek');
        } catch (error) { adapterFailures.push({ id: adapter.id ?? null, layerId: adapter.layerId ?? null, message: error.message }); }
      }
      return {
        count: document.querySelectorAll('canvas').length,
        contexts: window.__sceneEngineCaptureProbe.contexts,
        rafScheduled: window.__sceneEngineCaptureProbe.rafScheduled,
        adapterCount: adapters.length,
        adapterFailures
      };
    }, Math.max(0, frameCount(layer.durationMs) - 1));
    const canvasContext = canvasState.contexts.find((item) => /webgl|experimental-webgl|webgpu/.test(item.type));
    const animatedCanvas = canvasState.count > 0 && canvasState.rafScheduled && canvasState.contexts.some((item) => /2d|webgl|experimental-webgl|webgpu/.test(item.type));
    if ((canvasContext || animatedCanvas) && !canvasState.adapterCount) {
      const id = canvasContext?.id ?? null;
      throw Object.assign(new Error(`Canvas${id ? ` '${id}'` : ''} uses ${canvasContext?.type ?? 'an animated 2D context'} without a deterministic seek adapter.`), { code: 'UNSEEKABLE', layerId: layer.id, frame: 0, exitCode: 1 });
    }
    if (canvasState.adapterFailures.length) {
      const adapter = canvasState.adapterFailures[0];
      throw Object.assign(new Error(`Adapter ${adapter.id ?? '(unnamed)'} on layer ${adapter.layerId ?? layer.id} cannot seek backwards: ${adapter.message}`), { code: 'UNSEEKABLE', layerId: adapter.layerId ?? layer.id, adapterId: adapter.id, frame: 0, exitCode: 1 });
    }
    const steps = layer.steps ?? []; let stepIndex = 0;
    const count = frameCount(layer.durationMs);
    const hashes = [];
    for (let frame = 0; frame < count; frame += 1) {
      const time = frameTimeMs(frame);
      while (stepIndex < steps.length && steps[stepIndex].atMs <= time) {
        try { await applyStep(page, steps[stepIndex], stepIndex, layer); }
        catch (error) {
          if (blockedUrl) throw Object.assign(error, { code: 'FIXTURE_NOT_FOUND', url: blockedUrl, exitCode: 3 });
          throw error;
        }
        stepIndex += 1;
      }
      await page.evaluate((ms) => {
        for (const animation of document.getAnimations({ subtree: true })) { animation.pause(); try { animation.currentTime = ms; } catch { } }
      }, time);
      const adapterFailure = await page.evaluate(({ frameIndex, timeMs }) => {
        for (const adapter of window.__sceneEngineAdapters) {
          try { if (adapter.seekFrame(frameIndex, timeMs) === false) throw new Error('adapter rejected frame'); }
          catch (error) { return { id: adapter.id ?? null, layerId: adapter.layerId ?? null, message: error.message }; }
        }
        return null;
      }, { frameIndex: frame, timeMs: time });
      if (adapterFailure) throw Object.assign(new Error(`Adapter ${adapterFailure.id ?? '(unnamed)'} on layer ${adapterFailure.layerId ?? layer.id} cannot seek frame ${frame}: ${adapterFailure.message}`), { code: 'UNSEEKABLE', layerId: adapterFailure.layerId ?? layer.id, adapterId: adapterFailure.id, frame, exitCode: 1 });
      await updateOverlays(page, layer, time);
      const bytes = await page.screenshot({ path: path.join(temp, 'frames', `frame-${String(frame).padStart(6, '0')}.png`), animations: 'allow', caret: 'hide' });
      hashes.push(sha256(bytes));
    }
    if (blockedUrl) throw Object.assign(new Error(`Unmatched external request: ${blockedUrl}`), { code: 'FIXTURE_NOT_FOUND', url: blockedUrl, exitCode: 3 });
    await context.close(); context = null;
    const rawVideo = path.join(temp, 'capture.mp4');
    await run(ffmpeg, ['-hide_banner', '-loglevel', 'error', '-y', '-framerate', '30', '-i', path.join(temp, 'frames', 'frame-%06d.png'), '-an', '-c:v', 'libx264', '-profile:v', 'high', '-level:v', '4.1', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'ultrafast', '-movflags', '+faststart', rawVideo], timeoutMs);
    fs.rmSync(path.join(temp, 'browser-profile'), { recursive: true, force: true });
    const storyboardHash = canonicalHash(model.story);
    const fixtureHashes = fixtureBodyHashes(model, layer);
    const layerHash = canonicalHash({ layer, fixtureHashes });
    const manifest = {
      format: 'scene-engine/capture@1', sceneId: scene.id, layerId: layer.id,
      appBuildId: layer.appBuildId ?? null,
      cssViewport: { width: layer.width, height: layer.height }, deviceScaleFactor: 2,
      frameCount: count, fixtureCount, hashes, storyboardHash, layerHash, fixtureHashes, browserVersion,
      videoPath: 'capture.mp4'
    };
    fs.writeFileSync(path.join(temp, 'manifest.json'), `${JSON.stringify(manifest, null, 2)}\n`);
    fs.rmSync(destination, { recursive: true, force: true }); fs.renameSync(temp, destination);
    return { ...manifest, manifestPath: path.join(destination, 'manifest.json'), videoPath: path.join(destination, 'capture.mp4') };
  } catch (error) {
    if (context) await context.close().catch(() => {});
    fs.rmSync(temp, { recursive: true, force: true });
    errors.push(diagnostic(error.code ?? 'APP_LOAD_FAILED', error.message, { sceneId: scene.id, layerId: error.layerId ?? layer.id, frame: error.frame ?? null, path: error.url ?? null, pointer: error.stepIndex == null ? null : `/steps/${error.stepIndex}`, hint: error.locator ? `Check locator ${JSON.stringify(error.locator)}.` : null }));
    throw Object.assign(error, { diagnostics: errors, exitCode: error.exitCode ?? 3 });
  }
}

export async function verifyReusableCapture(model, scene, layer, captureDir) {
  const directory = path.resolve(captureDir);
  const manifestPath = path.join(directory, 'manifest.json');
  const videoPath = path.join(directory, 'capture.mp4');
  if (!layer.appBuildId) throw Object.assign(new Error('appBuildId is required when reusing app-demo frames.'), { code: 'CAPTURE_MANIFEST_MISMATCH', exitCode: 2 });
  let manifest;
  try { manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8')); }
  catch { throw Object.assign(new Error('Capture manifest is missing or invalid.'), { code: 'CAPTURE_MANIFEST_MISMATCH', exitCode: 2 }); }
  const expectedStoryboardHash = canonicalHash(model.story);
  const fixtureHashes = fixtureBodyHashes(model, layer);
  const expectedLayerHash = canonicalHash({ layer, fixtureHashes });
  const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
  const profile = path.resolve(repoRoot, 'out', '.work', `browser-version-${process.pid}-${Date.now()}`);
  fs.mkdirSync(path.dirname(profile), { recursive: true });
  let context;
  let browserVersion = 'unknown';
  try {
    context = await chromium.launchPersistentContext(profile, { headless: true, viewport: { width: 1, height: 1 }, deviceScaleFactor: 1 });
    browserVersion = context.browser()?.version() ?? browserVersion;
  } finally {
    if (context) await context.close();
    fs.rmSync(profile, { recursive: true, force: true });
  }
  const matches = manifest.sceneId === scene.id && manifest.layerId === layer.id &&
    manifest.appBuildId === layer.appBuildId && manifest.storyboardHash === expectedStoryboardHash &&
    manifest.layerHash === expectedLayerHash && JSON.stringify(manifest.fixtureHashes ?? []) === JSON.stringify(fixtureHashes) &&
    manifest.browserVersion === browserVersion && manifest.deviceScaleFactor === 2 &&
    manifest.cssViewport?.width === layer.width && manifest.cssViewport?.height === layer.height &&
    fs.existsSync(videoPath);
  if (!matches || !Array.isArray(manifest.hashes) || manifest.hashes.length !== manifest.frameCount) throw Object.assign(new Error('Captured frames do not match storyboard, selected layer, app build, fixture bodies, viewport or browser.'), { code: 'CAPTURE_MANIFEST_MISMATCH', exitCode: 2, path: manifestPath, hint: 'Recapture the selected app-demo layer with this storyboard and browser build.' });
  for (let index = 0; index < manifest.frameCount; index += 1) {
    const frame = path.join(directory, 'frames', `frame-${String(index).padStart(6, '0')}.png`);
    if (!fs.existsSync(frame) || sha256(fs.readFileSync(frame)) !== manifest.hashes[index]) throw Object.assign(new Error(`Captured frame ${index} is missing or has changed.`), { code: 'CAPTURE_MANIFEST_MISMATCH', exitCode: 2, path: frame, hint: 'Recapture the selected app-demo layer with this storyboard and browser build.' });
  }
  return { manifest, videoPath };
}

async function run(command, args, timeoutMs) {
  const { spawn } = await import('node:child_process');
  await new Promise((resolve, reject) => {
    const child = spawn(command, args, { stdio: ['ignore', 'ignore', 'pipe'] });
    let stderr = ''; const timer = setTimeout(() => { child.kill('SIGKILL'); reject(Object.assign(new Error(`${command} exceeded ${timeoutMs} ms`), { code: 'RENDER_TIMEOUT', exitCode: 3 })); }, timeoutMs || 30000);
    child.stderr.on('data', (chunk) => { stderr += chunk.toString(); });
    child.once('error', (error) => { clearTimeout(timer); reject(Object.assign(error, { code: 'FFMPEG_FAILED', exitCode: 3 })); });
    child.once('close', (code) => { clearTimeout(timer); if (code === 0) resolve(); else reject(Object.assign(new Error(`${command} failed (${code}): ${stderr.trim()}`), { code: 'FFMPEG_FAILED', exitCode: 3 })); });
  });
}

export function appLayers(model, sceneId, layerId) {
  const scene = model.scenes.find((item) => item.id === sceneId);
  const matches = scene ? (scene.layers ?? []).filter((layer) => layer.type === 'appDemo' && (!layerId || layer.id === layerId)) : [];
  return { scene, matches };
}
