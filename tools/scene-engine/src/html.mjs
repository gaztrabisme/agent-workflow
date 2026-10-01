import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { allLayers } from './scene.mjs';
import { sampleTrack, sampleLayer } from './timeline.mjs';

const esc = (value = '') => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const cssString = (value = '') => String(value).replaceAll('\\', '\\\\').replaceAll('"', '\\"').replaceAll('\n', ' ');

function assetUrl(model, relative) {
  const absolute = path.resolve(model.root, relative);
  const extension = path.extname(absolute).toLowerCase();
  if (extension === '.svg' || extension === '.png' || extension === '.jpg' || extension === '.jpeg' || extension === '.webp' || extension === '.gif') {
    const mime = ({ '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.gif': 'image/gif' })[extension];
    return `data:${mime};base64,${fs.readFileSync(absolute).toString('base64')}`;
  }
  return pathToFileURL(absolute).href;
}

function chartSvg(layer) {
  const width = Math.max(120, Math.round(layer.width)); const height = Math.max(100, Math.round(layer.height));
  const colors = layer.style?.seriesColors ?? ['#2563EB', '#F97316', '#10B981', '#A855F7', '#EF4444'];
  const series = layer.series ?? [];
  const categories = layer.categories ?? [];
  const vals = series.flatMap((s) => s.values ?? []);
  const min = Math.min(0, ...vals); const max = Math.max(1, ...vals); const plot = { x: 48, y: 20, w: width - 64, h: height - 76 };
  const y = (v) => plot.y + plot.h - (v - min) / (max - min || 1) * plot.h;
  const step = plot.w / Math.max(1, categories.length); const groupedWidth = step * 0.72 / Math.max(1, series.length);
  let marks = '';
  for (let tick = 0; tick <= 4; tick += 1) {
    const yy = plot.y + plot.h * tick / 4;
    marks += `<line x1="${plot.x}" y1="${yy}" x2="${plot.x + plot.w}" y2="${yy}" stroke="${layer.style?.gridColor ?? '#D9DDE3'}"/>`;
    marks += `<text x="${plot.x - 8}" y="${yy + 5}" text-anchor="end" font-size="${layer.style?.fontSize ?? 14}" fill="#667085">${esc((max - (max - min) * tick / 4).toFixed(0))}</text>`;
  }
  const build = layer.build;
  const progress = build ? 1 : 1;
  if (['column', 'columnStacked', 'columnStacked100', 'bar', 'barStacked', 'barStacked100'].includes(layer.kind)) {
    series.forEach((s, si) => s.values.forEach((value, ci) => {
      const xx = plot.x + ci * step + step * 0.14 + si * groupedWidth;
      const yy = y(value); const hh = plot.y + plot.h - yy;
      marks += `<rect data-rk-mark="true" data-series-index="${si}" data-point-index="${ci}" data-value="${value}" x="${xx}" y="${yy + hh * (1 - progress)}" width="${groupedWidth * 0.88}" height="${hh * progress}" rx="3" fill="${colors[si % colors.length]}"/>`;
      if (layer.showValues) marks += `<text x="${xx + groupedWidth * 0.44}" y="${yy - 6}" text-anchor="middle" font-size="12" fill="#344054">${esc(value)}</text>`;
    }));
  } else {
    series.forEach((s, si) => {
      const points = s.values.map((value, ci) => `${plot.x + step * (ci + 0.5)},${y(value)}`).join(' ');
      marks += `<polyline points="${points}" fill="none" stroke="${colors[si % colors.length]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`;
      s.values.forEach((value, ci) => { const [cx, cy] = points.split(' ')[ci].split(','); marks += `<circle data-rk-mark="true" data-series-index="${si}" data-point-index="${ci}" data-value="${value}" cx="${cx}" cy="${cy}" r="5" fill="${colors[si % colors.length]}"/>`; });
    });
  }
  const labels = categories.map((name, i) => `<text x="${plot.x + step * (i + 0.5)}" y="${height - 28}" text-anchor="middle" font-family="Arial" font-size="${layer.style?.fontSize ?? 14}" fill="#475467">${esc(name)}</text>`).join('');
  const legend = layer.showLegend === false ? '' : series.map((s, i) => `<g transform="translate(${plot.x + i * 150},${height - 8})"><circle r="5" fill="${colors[i % colors.length]}"/><text x="10" y="4" font-family="Arial" font-size="12" fill="#475467">${esc(s.name)}</text></g>`).join('');
  return `<svg data-rk-chart="${esc(layer.kind)}" xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="${esc(layer.alt || 'Chart')}"><rect width="100%" height="100%" rx="16" fill="#FFFFFF"/>${marks}${labels}${legend}</svg>`;
}

function layerHtml(model, scene, layer, captureMap, captionMode, localParentStart = 0) {
  const left = Number(layer.x) || 0; const top = Number(layer.y) || 0;
  const base = `left:${left}px;top:${top}px;width:${layer.width}px;height:${layer.height}px;z-index:${layer.z ?? 0};opacity:${layer.opacity ?? 1};transform-origin:${(layer.anchorX ?? .5) * 100}% ${(layer.anchorY ?? .5) * 100}%;rotate:${layer.rotation ?? 0}deg;scale:${layer.scaleX ?? 1} ${layer.scaleY ?? 1};`;
  const filter = layer.effects?.blurPx ? `filter:blur(${layer.effects.blurPx}px);` : '';
  const blend = layer.effects?.blendMode ? `mix-blend-mode:${layer.effects.blendMode};` : '';
  let content = '';
  const type = layer.type;
  if (type === 'text') {
    const style = layer.style ?? {};
    const text = layer.text ?? (layer.runs ?? []).map((run) => run.text).join('');
    const paragraphs = Array.isArray(layer.bullets) ? layer.bullets.map((item) => `<div class="bullet">${esc(item)}</div>`).join('') : esc(text).replaceAll('\n', '<br>');
    content = `<div class="text" style="font-family:&quot;${cssString(style.fontFamily ?? 'Arial')}&quot;,Arial,sans-serif;font-size:${style.fontSize ?? 32}px;font-weight:${style.fontWeight ?? 400};color:${style.color ?? '#111111'};text-align:${style.align ?? 'left'};line-height:${style.lineHeight ?? 1.2};letter-spacing:${style.letterSpacing ?? 0}px;white-space:normal;overflow:hidden;">${paragraphs}</div>`;
  } else if (type === 'image') {
    content = `<img alt="${esc(layer.alt ?? '')}" src="${assetUrl(model, layer.src)}" style="width:100%;height:100%;object-fit:${layer.fit ?? 'contain'};display:block;"/>`;
  } else if (type === 'chart') {
    content = chartSvg(layer);
  } else if (type === 'shape') {
    const shapeCss = layer.shape === 'ellipse' ? 'border-radius:50%;' : layer.shape === 'roundRect' ? `border-radius:${layer.radiusPx ?? 18}px;` : '';
    const fill = typeof layer.fill === 'string' ? layer.fill : 'transparent';
    content = `<div style="width:100%;height:100%;${shapeCss}background:${fill};${layer.stroke ? `border:${layer.strokeWidth ?? 1}px solid ${layer.stroke};` : ''}"></div>`;
  } else if (type === 'table') {
    const rows = [layer.columns ?? [], ...(layer.rows ?? [])];
    content = `<table style="width:100%;height:100%;border-collapse:collapse;font:18px Arial;background:white;">${rows.map((row, ri) => `<tr>${row.map((cell) => `<${ri === 0 ? 'th' : 'td'} style="border:1px solid #D0D5DD;padding:10px;text-align:left;">${esc(cell ?? '')}</${ri === 0 ? 'th' : 'td'}>`).join('')}</tr>`).join('')}</table>`;
  } else if (type === 'video' || type === 'appDemo') {
    return '';
  } else if (type === 'adapter') {
    content = `<div class="unsupported">${esc(layer.adapterId)}</div>`;
  } else if (type === 'group') {
    content = (layer.children ?? []).map((child) => layerHtml(model, scene, child, captureMap, captionMode, layer.startMs)).join('');
  }
  if (type === 'shape' && layer.effects?.mask) content = '';
  const element = `<div id="${esc(layer.id)}" class="layer layer-${type}" data-layer-id="${esc(layer.id)}" data-local-start="${(localParentStart + layer.startMs) / 1000}" data-local-duration="${layer.durationMs / 1000}" style="${base}${filter}${blend}">${content}</div>`;
  const animationRules = (layer.tracks ?? []).map((track, index) => {
    const id = `kf-${layer.id.replaceAll(/[^A-Za-z0-9_-]/g, '-')}-${index}`;
    const property = track.property;
    const cssProp = ({ x: 'left', y: 'top', width: 'width', height: 'height', opacity: 'opacity', rotation: 'rotate', scaleX: '--se-scale-x', scaleY: '--se-scale-y', 'style.fontSize': 'font-size', 'style.color': 'color', fill: 'background-color', stroke: 'border-color', strokeWidth: 'border-width' })[property];
    if (!cssProp) return '';
    const unit = ['x', 'y', 'width', 'height', 'style.fontSize', 'strokeWidth'].includes(property) ? 'px' : (property === 'rotation' ? 'deg' : '');
    const baseValue = property.split('.').reduce((obj, key) => obj?.[key], layer);
    const frames = [{ atMs: 0, value: baseValue ?? (property.startsWith('style.') ? layer.style?.[property.split('.')[1]] : undefined) }, ...track.keyframes].filter((item) => item.value !== undefined);
    const keyframes = frames.map((frame) => `${(frame.atMs / layer.durationMs * 100).toFixed(5)}%{${cssProp === '--se-scale-x' ? 'scale' : cssProp}:${cssProp === '--se-scale-x' ? `${frame.value} var(--se-scale-y,1)` : `${frame.value}${unit}`};}`).join('');
    return `@keyframes ${id}{${keyframes}}[data-layer-id="${esc(layer.id)}"]{animation:${id} ${layer.durationMs}ms linear ${scene._startMs + localParentStart + layer.startMs}ms both;}`;
  }).join('');
  const captions = captionMode === 'burn-in' || captionMode === 'both' ? (scene.captions ?? []).map((caption, index) => {
    const id = `cap-${scene.id}-${index}`;
    const start = caption.startMs; const end = caption.endMs;
    return `<div class="caption" style="animation:${id} ${scene.durationMs}ms linear ${scene._startMs}ms both;--cap-start:${start / scene.durationMs * 100}%;--cap-end:${end / scene.durationMs * 100}%">${esc(caption.text)}</div><style>@keyframes ${id}{0%,${(start / scene.durationMs * 100).toFixed(4)}%{opacity:0} ${(start / scene.durationMs * 100).toFixed(4)}%,${(end / scene.durationMs * 100).toFixed(4)}%{opacity:1} ${(end / scene.durationMs * 100).toFixed(4)}%,100%{opacity:0}}</style>`;
  }).join('') : '';
  return `<style>${animationRules}</style>${element}${captions}`;
}

function cameraCss(scene) {
  const camera = scene.camera;
  if (!camera?.tracks?.length) return '';
  const properties = ['x', 'y', 'zoom', 'rotation'];
  const times = new Set([0, scene.durationMs - 1]);
  for (const track of camera.tracks) for (const frame of track.keyframes ?? []) if (Number.isInteger(frame.atMs)) times.add(frame.atMs);
  const frames = [...times].sort((a, b) => a - b).map((atMs) => {
    const value = { x: camera.x ?? 0, y: camera.y ?? 0, zoom: camera.zoom ?? 1, rotation: camera.rotation ?? 0 };
    for (const track of camera.tracks) value[track.property] = sampleTrack(value[track.property], track, atMs);
    const tx = -(value.x ?? 0); const ty = -(value.y ?? 0);
    return `${(atMs / scene.durationMs * 100).toFixed(5)}%{transform:translate(${tx}px,${ty}px) scale(${value.zoom ?? 1}) rotate(${value.rotation ?? 0}deg)}`;
  }).join('');
  const anchorX = (camera.anchorX ?? 0.5) * 100; const anchorY = (camera.anchorY ?? 0.5) * 100;
  return `<style>@keyframes camera-${scene.id}{${frames}}[data-scene-id="${esc(scene.id)}"]{transform-origin:${anchorX}% ${anchorY}%;animation:camera-${scene.id} ${scene.durationMs}ms linear ${scene._startMs}ms both;}</style>`;
}

function mediaLayerHtml(model, scene, layer, captureMap, compositionDir, parent = { x: 0, y: 0, start: 0, z: 0 }) {
  if (layer.type === 'group') return (layer.children ?? []).map((child) => mediaLayerHtml(model, scene, child, captureMap, compositionDir, {
    x: parent.x + layer.x, y: parent.y + layer.y, start: parent.start + layer.startMs, z: parent.z + (layer.z ?? 0)
  })).join('');
  if (layer.type !== 'video' && layer.type !== 'appDemo') return '';
  const source = captureMap.get(layer.id) ?? (layer.type === 'video' ? path.resolve(model.root, layer.src) : null);
  if (!source) return '';
  const startMs = scene._startMs + parent.start + layer.startMs;
  const left = parent.x + layer.x; const top = parent.y + layer.y;
  const z = parent.z + (layer.z ?? 0);
  const asset = compositionDir ? path.relative(compositionDir, source).split(path.sep).join('/') : pathToFileURL(source).href;
  return `<div id="media-plane-${esc(scene.id)}-${esc(layer.id)}" class="scene-camera-plane" data-scene-id="${esc(scene.id)}"><video id="${esc(layer.id)}" class="stage-media" data-layer-id="${esc(layer.id)}" data-start="${startMs / 1000}" data-duration="${layer.durationMs / 1000}" data-scene-engine-start-ms="${startMs}" data-scene-engine-duration-ms="${layer.durationMs}" src="${asset}" autoplay muted playsinline preload="auto" style="position:absolute;left:${left}px;top:${top}px;width:${layer.width}px;height:${layer.height}px;z-index:${z};object-fit:contain;pointer-events:none;"></video></div>`;
}

function toGlobalCaptions(model) {
  const cues = [];
  for (const scene of model.scenes ?? []) {
    if (Array.isArray(scene.captions)) for (const cue of scene.captions) cues.push({ ...cue, startMs: cue.startMs + (scene._startMs ?? scene.startMs ?? 0), endMs: cue.endMs + (scene._startMs ?? scene.startMs ?? 0) });
  }
  return cues.sort((a, b) => a.startMs - b.startMs);
}

export function writeVtt(model, destination) {
  const timestamp = (ms) => {
    const total = Math.max(0, Math.round(ms)); const h = Math.floor(total / 3600000); const m = Math.floor(total / 60000) % 60; const s = Math.floor(total / 1000) % 60; const milli = total % 1000;
    return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}.${String(milli).padStart(3, '0')}`;
  };
  const body = toGlobalCaptions(model).map((cue, i) => `${i + 1}\n${timestamp(cue.startMs)} --> ${timestamp(cue.endMs)}\n${cue.text}\n`).join('\n');
  fs.writeFileSync(destination, `WEBVTT\n\n${body}`);
}

export function generateHtml(model, { captionMode = 'none', captureMap = new Map(), compositionDir = null } = {}) {
  const scenes = model.scenes.map((scene, index) => {
    const layers = [...(scene.layers ?? [])].sort((a, b) => (a.z ?? 0) - (b.z ?? 0)).map((layer) => layerHtml(model, scene, layer, captureMap, captionMode)).join('\n');
    return `${cameraCss(scene)}<div id="scene-${esc(scene.id)}" class="scene clip" data-scene-id="${esc(scene.id)}" data-start="${scene._startMs / 1000}" data-duration="${scene.durationMs / 1000}" data-track-index="${index}" style="background:${scene.background ?? model.story.background ?? '#FFFFFF'}">${layers}</div>`;
  }).join('\n');
  const media = model.scenes.map((scene) => (scene.layers ?? []).map((layer) => mediaLayerHtml(model, scene, layer, captureMap, compositionDir)).join('')).join('');
  const modelPayload = JSON.stringify(model.scenes.map((scene) => ({ id: scene.id, startMs: scene._startMs, durationMs: scene.durationMs, layers: allLayers(scene).map((layer) => ({ id: layer.id, startMs: layer.startMs, durationMs: layer.durationMs })) })));
  return `<!doctype html><html lang="${esc(model.story.language ?? 'en')}"><head><title>${esc(model.story.title)}</title><meta charset="utf-8"><meta name="viewport" content="width=1920,initial-scale=1"><style>
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:${model.story.background ?? '#FFFFFF'};font-family:Arial,sans-serif}#stage{position:relative;width:1920px;height:1080px;overflow:hidden;background:${model.story.background ?? '#FFFFFF'}}.scene{position:absolute;inset:0;overflow:hidden}.scene-camera-plane{position:absolute;inset:0;pointer-events:none}.layer{position:absolute;box-sizing:border-box}.text{box-sizing:border-box;width:100%;height:100%;padding-top:3px;overflow:hidden}.bullet{padding-left:1.1em;position:relative}.bullet:before{content:'•';position:absolute;left:0}.caption{position:absolute;left:160px;right:160px;bottom:60px;min-height:64px;padding:18px 30px;background:rgba(12,18,29,.82);border-radius:12px;color:white;font:600 30px/1.2 Arial,sans-serif;text-align:center;z-index:99999;opacity:0;box-sizing:border-box}.unsupported{width:100%;height:100%;background:#f2f4f7;color:#667085;display:grid;place-items:center;font:18px Arial}
</style></head><body><div id="stage" data-rk-stage data-composition-id="scene-engine" data-start="0" data-width="1920" data-height="1080" data-duration="${model.durationMs / 1000}" data-fps="30">${scenes}${media}</div>
<script src="assets/gsap.min.js"></script><script>
const sceneModel=${modelPayload};
window.__sceneEngine={seek(ms){for(const scene of document.querySelectorAll('.scene')){const item=sceneModel.find(x=>x.id===scene.dataset.sceneId);const local=ms-item.startMs;scene.style.display=local>=0&&local<item.durationMs?'block':'none';for(const a of scene.getAnimations({subtree:true})){a.pause();a.currentTime=Math.max(0,local);}}for(const video of document.querySelectorAll('.stage-media')){const local=ms-Number(video.dataset.sceneEngineStartMs);const duration=Number(video.dataset.sceneEngineDurationMs);video.parentElement.style.display=local>=0&&local<duration?'block':'none';video.pause();try{video.currentTime=Math.max(0,Math.min(video.duration||duration/1000,local/1000));}catch{}}return true},async ready(){await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));await Promise.all([...document.querySelectorAll('video')].map(v=>v.readyState>=2?Promise.resolve():new Promise(r=>{v.addEventListener('loadeddata',r,{once:true});setTimeout(r,3000)})));return true}};
window.__timelines=window.__timelines||{};if(window.gsap){const playhead={time:0};window.__timelines["scene-engine"]=window.gsap.timeline({paused:true,onUpdate(){window.__sceneEngine.seek(playhead.time*1000);}}).to(playhead,{time:${model.durationMs/1000},duration:${model.durationMs/1000},ease:"none"});}window.__sceneEngine.seek(0);window.__sceneEngine.ready();
</script></body></html>`;
}

export function writeComposition(model, directory, options) {
  fs.mkdirSync(directory, { recursive: true });
  const assetDirectory = path.join(directory, 'assets');
  fs.mkdirSync(assetDirectory, { recursive: true });
  fs.copyFileSync(path.resolve('node_modules/gsap/dist/gsap.min.js'), path.join(assetDirectory, 'gsap.min.js'));
  const html = generateHtml(model, { ...options, compositionDir: directory });
  fs.writeFileSync(path.join(directory, 'index.html'), html);
  return path.join(directory, 'index.html');
}

function sampleLayerTree(layer, parentTime) {
  const state = sampleLayer(layer, parentTime);
  const localTime = parentTime - layer.startMs;
  if (layer.type === 'group') state.children = (layer.children ?? []).filter((child) => localTime >= child.startMs && localTime < child.startMs + child.durationMs).map((child) => sampleLayerTree(child, localTime));
  delete state.tracks;
  delete state.build;
  delete state.rangeTracks;
  delete state.reveal;
  return state;
}

export function generateStaticHtml(model, atMs) {
  const activeScenes = model.scenes.filter((scene) => atMs >= scene._startMs && atMs < scene._startMs + scene.durationMs);
  const scenes = activeScenes.map((scene) => {
    const localTime = atMs - scene._startMs;
    const activeLayers = (scene.layers ?? []).filter((layer) => localTime >= layer.startMs && localTime < layer.startMs + layer.durationMs).map((layer) => sampleLayerTree(layer, localTime)).map((layer) => ({ ...layer, startMs: 0, durationMs: 1000, entrance: 'none' }));
    const captions = (scene.captions ?? []).filter((cue) => localTime >= cue.startMs && localTime < cue.endMs).map((cue) => ({ ...cue, startMs: 0, endMs: 1000 }));
    return { ...scene, _startMs: 0, startMs: 0, durationMs: 1000, layers: activeLayers, captions, camera: undefined };
  });
  const staticModel = { ...model, durationMs: 1000, frameCount: 30, scenes, story: { ...model.story, durationMs: 1000 } };
  let html = generateHtml(staticModel, { captionMode: 'none' });
  html = html.replace('<script src="assets/gsap.min.js"></script>', '');
  const captions = scenes.flatMap((scene) => scene.captions).map((cue) => `<div class="caption" style="opacity:1">${esc(cue.text)}</div>`).join('');
  if (captions) html = html.replace('</div>\n<script>', `${captions}</div>\n<script>`);
  html = html.replace('window.__sceneEngine.seek(0);window.__sceneEngine.ready();', 'window.__sceneEngine.seek(0);window.__sceneEngine.ready();');
  return html;
}
