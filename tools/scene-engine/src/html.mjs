import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { allLayers } from './scene.mjs';
import { sampleTrack, sampleLayer } from './timeline.mjs';

const ENGINE_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PINNED_INTER_DATA = fs.readFileSync(path.join(ENGINE_ROOT, 'src/assets/fonts/InterVariable.woff2')).toString('base64');
const PINNED_FONT_FACES = `@font-face{font-family:'Arial';font-style:normal;font-weight:100 900;font-display:block;src:url(data:font/woff2;base64,${PINNED_INTER_DATA}) format('woff2');}@font-face{font-family:'Inter';font-style:normal;font-weight:100 900;font-display:block;src:url(data:font/woff2;base64,${PINNED_INTER_DATA}) format('woff2');}`;

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

function formatCounter(counter, progress) {
  const value = counter.from + (counter.to - counter.from) * Math.max(0, Math.min(1, progress));
  return `${counter.prefix ?? ''}${value.toFixed(counter.decimals ?? 0)}${counter.suffix ?? ''}`;
}

function shapeSvg(layer) {
  const width = Math.max(0, Number(layer.width) || 0); const height = Math.max(0, Number(layer.height) || 0);
  const id = `shape-${String(layer.id).replaceAll(/[^A-Za-z0-9_-]/g, '-')}`;
  let defs = '';
  let fill = typeof layer.fill === 'string' ? layer.fill : 'transparent';
  if (layer.fill && typeof layer.fill === 'object') {
    const angle = ((Number(layer.fill.angleDeg) || 0) - 90) * Math.PI / 180;
    const dx = Math.cos(angle) * 50; const dy = Math.sin(angle) * 50;
    defs += `<linearGradient id="${id}-gradient" x1="${50 - dx}%" y1="${50 - dy}%" x2="${50 + dx}%" y2="${50 + dy}%">${layer.fill.stops.map((stop) => `<stop offset="${stop.offset * 100}%" stop-color="${esc(stop.color)}" stop-opacity="${stop.opacity ?? 1}"/>`).join('')}</linearGradient>`;
    fill = `url(#${id}-gradient)`;
  }
  const stroke = layer.stroke ?? 'none';
  const dash = layer.strokeDash === 'dash' ? '12 8' : layer.strokeDash === 'dot' ? '2 7' : '';
  const dashAttrs = dash ? ` stroke-dasharray="${dash}" stroke-dashoffset="${Number(layer.strokeDashOffset) || 0}"` : '';
  const trimStart = Math.max(0, Math.min(1, Number(layer.trimStart ?? 0)));
  const trimEnd = Math.max(trimStart, Math.min(1, Number(layer.trimEnd ?? 1)));
  let graphic;
  if (layer.shape === 'ellipse') graphic = `<ellipse data-shape-graphic cx="${width / 2}" cy="${height / 2}" rx="${width / 2}" ry="${height / 2}" fill="${fill}" stroke="${stroke}" stroke-width="${layer.strokeWidth ?? 1}"${dashAttrs}/>`;
  else if (layer.shape === 'line' || layer.shape === 'path') {
    const d = layer.path || (layer.shape === 'line' ? `M 0 ${height / 2} L ${width} ${height / 2}` : '');
    const trimAttrs = trimStart !== 0 || trimEnd !== 1 ? ` pathLength="1" stroke-dasharray="${trimEnd - trimStart} ${1 - (trimEnd - trimStart)}" stroke-dashoffset="${-trimStart}"` : dashAttrs;
    graphic = `<path data-shape-graphic d="${esc(d)}" fill="${layer.shape === 'path' ? fill : 'none'}" stroke="${stroke}" stroke-width="${layer.strokeWidth ?? 1}" stroke-linecap="round" stroke-linejoin="round"${trimAttrs}/>`;
  } else {
    const radius = layer.shape === 'roundRect' ? Math.max(0, Number(layer.radiusPx ?? 18)) : 0;
    graphic = `<rect data-shape-graphic x="0" y="0" width="${width}" height="${height}" rx="${radius}" fill="${fill}" stroke="${stroke}" stroke-width="${layer.strokeWidth ?? 1}"${dashAttrs}/>`;
  }
  return `<svg class="shape-svg" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 ${width} ${height}" overflow="visible"><defs>${defs}</defs>${graphic}</svg>`;
}

function layerHtml(model, scene, layer, captureMap, captionMode, localParentStart = 0) {
  const left = Number(layer.x) || 0; const top = Number(layer.y) || 0;
  const base = `left:${left}px;top:${top}px;width:${layer.width}px;height:${layer.height}px;z-index:${layer.z ?? 0};opacity:${layer.opacity ?? 1};transform-origin:${(layer.anchorX ?? .5) * 100}% ${(layer.anchorY ?? .5) * 100}%;rotate:${layer.rotation ?? 0}deg;scale:${layer.scaleX ?? 1} ${layer.scaleY ?? 1};`;
  const filter = layer.effects?.blurPx ? `filter:blur(${layer.effects.blurPx}px);` : '';
  const blend = layer.effects?.blendMode ? `mix-blend-mode:${layer.effects.blendMode};` : '';
  const backdrop = layer.effects?.backdropBlurPx ? `backdrop-filter:blur(${layer.effects.backdropBlurPx}px);` : '';
  const transform3d = Array.isArray(layer.effects?.transform3d) ? `transform:matrix3d(${layer.effects.transform3d.join(',')});` : '';
  let content = '';
  const type = layer.type;
  if (type === 'text') {
    const style = layer.style ?? {};
    const text = layer.counter ? (layer.__counterText ?? formatCounter(layer.counter, 0)) : (layer.text ?? (layer.runs ?? []).map((run) => run.text).join(''));
    const paragraphs = Array.isArray(layer.bullets) ? layer.bullets.map((item, index) => {
      const kind = item.kind ?? 'bullet'; const marker = kind === 'number' ? `${index + 1}.` : kind === 'bullet' ? '•' : '';
      return `<div class="bullet" data-level="${item.level ?? 0}" style="padding-left:${(item.level ?? 0) * 1.1}em"><span class="bullet-marker">${marker}</span><span>${esc(item.text)}</span></div>`;
    }).join('') : esc(text).replaceAll('\n', '<br>');
    content = `<div class="text" style="font-family:&quot;${cssString(style.fontFamily ?? 'Arial')}&quot;,Arial,sans-serif;font-size:${style.fontSize ?? 32}px;font-weight:${style.fontWeight ?? 400};color:${style.color ?? '#111111'};text-align:${style.align ?? 'left'};line-height:${style.lineHeight ?? 1.2};letter-spacing:${style.letterSpacing ?? 0}px;white-space:normal;overflow:hidden;">${paragraphs}</div>`;
  } else if (type === 'image') {
    content = `<img alt="${esc(layer.alt ?? '')}" src="${assetUrl(model, layer.src)}" style="width:100%;height:100%;object-fit:${layer.fit ?? 'contain'};display:block;"/>`;
  } else if (type === 'chart') {
    content = chartSvg(layer);
  } else if (type === 'shape') {
    content = shapeSvg(layer);
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
  const localStartMs = localParentStart + layer.startMs;
  const tracks = (layer.tracks ?? []).map((track) => ({ ...track, base: track.property.split('.').reduce((obj, key) => obj?.[key], layer) ?? (track.property.startsWith('style.') ? layer.style?.[track.property.split('.')[1]] : undefined) }));
  const trackData = tracks.length ? ` data-tracks="${esc(JSON.stringify(tracks))}"` : '';
  const counterData = layer.counter ? ` data-counter="${esc(JSON.stringify(layer.counter))}"` : '';
  const entrance = layer.__entranceProgress === undefined && layer.entrance && layer.entrance !== 'none' ? ` data-entrance="${esc(layer.entrance)}" data-entrance-duration="${layer.entranceDurationMs ?? 500}"` : '';
  const staticEntrance = layer.__entranceProgress === undefined ? '' : entranceCss(layer.entrance, layer.__entranceProgress, layer.width, layer.height);
  const element = `<div id="${esc(layer.id)}" class="layer layer-${type}" data-layer-id="${esc(layer.id)}" data-local-start="${localStartMs}" data-local-duration="${layer.durationMs}" data-base-scale-x="${layer.scaleX ?? 1}" data-base-scale-y="${layer.scaleY ?? 1}" data-width="${layer.width}" data-height="${layer.height}"${trackData}${counterData}${entrance} style="${base}${filter}${blend}${backdrop}${transform3d}${staticEntrance}">${content}</div>`;
  return element;
}

function cameraCss(scene) {
  const camera = scene.camera;
  if (!camera) return '';
  const properties = ['x', 'y', 'zoom', 'rotation'];
  const times = new Set([0, scene.durationMs - 1]);
  for (const track of camera.tracks ?? []) for (const frame of track.keyframes ?? []) if (Number.isInteger(frame.atMs)) times.add(frame.atMs);
  const frames = [...times].sort((a, b) => a - b).map((atMs) => {
    const value = { x: camera.x ?? 0, y: camera.y ?? 0, zoom: camera.zoom ?? 1, rotation: camera.rotation ?? 0 };
    for (const track of camera.tracks ?? []) value[track.property] = sampleTrack(value[track.property], track, atMs);
    const tx = -(value.x ?? 0); const ty = -(value.y ?? 0);
    return `${(atMs / scene.durationMs * 100).toFixed(5)}%{transform:translate(${tx}px,${ty}px) scale(${value.zoom ?? 1}) rotate(${value.rotation ?? 0}deg)}`;
  }).join('');
  const anchorX = (camera.anchorX ?? 0.5) * 100; const anchorY = (camera.anchorY ?? 0.5) * 100;
  return `<style>@keyframes camera-${scene.id}{${frames}}[data-scene-id="${esc(scene.id)}"]{transform-origin:${anchorX}% ${anchorY}%;animation:camera-${scene.id} ${scene.durationMs}ms linear 0ms both;}</style>`;
}

function mediaLayerHtml(model, scene, layer, captureMap, compositionDir, parent = { x: 0, y: 0, start: 0, z: 0 }) {
  if (layer.type === 'group') return (layer.children ?? []).map((child) => mediaLayerHtml(model, scene, child, captureMap, compositionDir, {
    x: parent.x + layer.x, y: parent.y + layer.y, start: parent.start + layer.startMs, z: parent.z + (layer.z ?? 0)
  })).join('');
  if (layer.type !== 'video' && layer.type !== 'appDemo') return '';
  if (layer.type === 'appDemo' && layer.__checkFrameDataUrl) {
    const startMs = scene._startMs + parent.start + layer.startMs;
    const left = parent.x + layer.x; const top = parent.y + layer.y;
    const z = parent.z + (layer.z ?? 0);
    const entrance = entranceCss(layer.entrance, Number(layer.__entranceProgress ?? 0), layer.width, layer.height);
    return `<div id="media-plane-${esc(scene.id)}-${esc(layer.id)}" class="scene-camera-plane" data-scene-id="${esc(scene.id)}"><img id="${esc(layer.id)}" class="stage-app-frame" data-layer-id="${esc(layer.id)}" data-scene-id="${esc(scene.id)}" data-scene-engine-start-ms="${startMs}" src="${esc(layer.__checkFrameDataUrl)}" alt="Captured app-demo frame" style="position:absolute;left:${left}px;top:${top}px;width:${layer.width}px;height:${layer.height}px;z-index:${z};object-fit:contain;pointer-events:none;${entrance}"/></div>`;
  }
  const source = captureMap.get(layer.id) ?? (layer.type === 'video' ? path.resolve(model.root, layer.src) : null);
  if (!source) return '';
  const startMs = scene._startMs + parent.start + layer.startMs;
  const left = parent.x + layer.x; const top = parent.y + layer.y;
  const z = parent.z + (layer.z ?? 0);
  const asset = compositionDir ? path.relative(compositionDir, source).split(path.sep).join('/') : pathToFileURL(source).href;
  const entrance = layer.__entranceProgress === undefined && layer.entrance && layer.entrance !== 'none' ? ` data-entrance="${esc(layer.entrance)}" data-entrance-duration="${layer.entranceDurationMs ?? 500}"` : '';
  const staticMediaTime = layer.__mediaTimeMs === undefined ? '' : ` data-static-media-time-ms="${layer.__mediaTimeMs}"`;
  const progress = Math.max(0, Math.min(1, Number(layer.__entranceProgress ?? 0)));
  const staticEntrance = entranceCss(layer.entrance, progress, layer.width, layer.height);
  return `<div id="media-plane-${esc(scene.id)}-${esc(layer.id)}" class="scene-camera-plane" data-scene-id="${esc(scene.id)}"><video id="${esc(layer.id)}" class="stage-media" data-layer-id="${esc(layer.id)}" data-scene-id="${esc(scene.id)}" data-local-start="${parent.start + layer.startMs}" data-local-duration="${layer.durationMs}" data-start="${startMs / 1000}" data-duration="${layer.durationMs / 1000}" data-scene-engine-start-ms="${startMs}" data-scene-engine-duration-ms="${layer.durationMs}"${staticMediaTime}${entrance} src="${asset}" autoplay muted playsinline preload="auto" style="position:absolute;left:${left}px;top:${top}px;width:${layer.width}px;height:${layer.height}px;z-index:${z};object-fit:contain;pointer-events:none;${staticEntrance}"></video></div>`;
}

function entranceCss(entrance, progress, width, height) {
  if (!entrance || entrance === 'none') return '';
  if (entrance === 'fade') return `opacity:${progress};`;
  if (entrance === 'flyInLeft') return `opacity:1;transform:translateX(${(progress - 1) * width}px);`;
  if (entrance === 'flyInRight') return `opacity:1;transform:translateX(${(1 - progress) * width}px);`;
  if (entrance === 'flyInUp') return `opacity:1;transform:translateY(${(progress - 1) * height}px);`;
  if (entrance === 'flyInDown') return `opacity:1;transform:translateY(${(1 - progress) * height}px);`;
  if (entrance === 'wipeLeft') return `opacity:1;clip-path:inset(0 ${(1 - progress) * 100}% 0 0);`;
  return '';
}

function captionCoveredByAuthorLayer(scene, cue, atMs = null) {
  const target = cue.text.trim().replaceAll(/\s+/g, ' ');
  let found = false;
  const visit = (layers, parent = { start: 0, y: 0 }) => {
    for (const layer of layers ?? []) {
      const start = parent.start + (layer.startMs ?? 0); const y = parent.y + (layer.y ?? 0);
      if (layer.type === 'text') {
        const text = (layer.text ?? (layer.runs ?? []).map((run) => run.text).join('') ?? '').trim().replaceAll(/\s+/g, ' ');
        const overlapsCue = start < cue.endMs && start + layer.durationMs > cue.startMs;
        const activeAtTime = atMs === null || (atMs >= start && atMs < start + layer.durationMs);
        if (text === target && y + layer.height >= 880 && overlapsCue && activeAtTime) found = true;
      }
      if (layer.type === 'group') visit(layer.children, { start, y });
    }
  };
  visit(scene.layers);
  return found;
}

function sceneCaptionsHtml(scene, captionMode) {
  if (!['burn-in', 'both'].includes(captionMode)) return '';
  return (scene.captions ?? []).filter((cue) => !captionCoveredByAuthorLayer(scene, cue)).map((cue) =>
    `<div class="caption" data-caption-start="${cue.startMs}" data-caption-end="${cue.endMs}" style="opacity:0">${esc(cue.text)}</div>`
  ).join('');
}

function seekRuntime(sceneModel, durationMs) {
  return `
const sceneModel=${sceneModel};
function seClamp(value,min=0,max=1){return Math.max(min,Math.min(max,value));}
function seEase(progress,easing){const p=seClamp(progress);const names={'ease-in':[.42,0,1,1],'ease-out':[0,0,.58,1],'ease-in-out':[.42,0,.58,1],linear:[0,0,1,1]};if(easing==='step-start')return 1;if(easing==='step-end')return p<1?0:1;const curve=Array.isArray(easing)?easing:(easing&&easing.cubicBezier)||names[easing||'linear'];if(!curve)return p;const cubic=(t,a,b)=>3*(1-t)*(1-t)*t*a+3*(1-t)*t*t*b+t*t*t;let lo=0,hi=1,t=p;for(let i=0;i<18;i++){const x=cubic(t,curve[0],curve[2]);if(Math.abs(x-p)<1e-7)break;if(x<p)lo=t;else hi=t;t=(lo+hi)/2;}return cubic(t,curve[1],curve[3]);}
function seValue(base,a,b,p){if(typeof a==='number'&&typeof b==='number')return a+(b-a)*p;if(typeof a==='string'&&typeof b==='string'&&/^#[0-9a-f]{6}$/i.test(a)&&/^#[0-9a-f]{6}$/i.test(b)){const aa=a.match(/[0-9a-f]{2}/gi).map(v=>parseInt(v,16));const bb=b.match(/[0-9a-f]{2}/gi).map(v=>parseInt(v,16));return '#'+aa.map((v,i)=>Math.round(v+(bb[i]-v)*p).toString(16).padStart(2,'0')).join('');}return p<1?a:b;}
function seTrack(track,time){const frames=track.keyframes||[];if(!frames.length||time<frames[0].atMs)return track.base; if(time>=frames[frames.length-1].atMs)return frames[frames.length-1].value;for(let i=1;i<frames.length;i++){const a=frames[i-1],b=frames[i];if(time<=b.atMs){const p=(time-a.atMs)/(b.atMs-a.atMs);return seValue(track.base,a.value,b.value,seEase(p,a.easing||'linear'));}}return track.base;}
function seEntrance(el,kind,p){const w=Number(el.dataset.width||el.videoWidth||el.clientWidth),h=Number(el.dataset.height||el.videoHeight||el.clientHeight),v=seClamp(p);el.style.transform='';el.style.clipPath='';if(kind==='fade'){el.style.opacity=String(v);return;}el.style.opacity='1';if(kind==='flyInLeft')el.style.transform='translateX('+((v-1)*w)+'px)';else if(kind==='flyInRight')el.style.transform='translateX('+((1-v)*w)+'px)';else if(kind==='flyInUp')el.style.transform='translateY('+((v-1)*h)+'px)';else if(kind==='flyInDown')el.style.transform='translateY('+((1-v)*h)+'px)';else if(kind==='wipeLeft')el.style.clipPath='inset(0 '+((1-v)*100)+'% 0 0)';}
function seFormatCounter(c,p){const value=c.from+(c.to-c.from)*seClamp(p);return (c.prefix||'')+value.toFixed(c.decimals||0)+(c.suffix||'');}
function seApplyTrack(el,track,value){const prop=track.property;const text=el.querySelector('.text');const graphic=el.querySelector('[data-shape-graphic]');if(prop==='x')el.style.left=value+'px';else if(prop==='y')el.style.top=value+'px';else if(prop==='width')el.style.width=value+'px';else if(prop==='height')el.style.height=value+'px';else if(prop==='opacity')el.style.opacity=String(value);else if(prop==='rotation')el.style.rotate=value+'deg';else if(prop==='style.fontSize'&&text)text.style.fontSize=value+'px';else if(prop==='style.color'&&text)text.style.color=value;else if(prop==='fill'&&graphic)graphic.setAttribute('fill',value);else if(prop==='stroke'&&graphic)graphic.setAttribute('stroke',value);else if(prop==='strokeWidth'&&graphic)graphic.setAttribute('stroke-width',String(value));}
window.__sceneEngineAdapters=window.__sceneEngineAdapters||[];
window.__sceneEngine={registerAdapter(id,layerId,seekFrame){if(!id||!layerId||typeof seekFrame!=='function')throw new TypeError('Adapter requires id, layerId and seekFrame(frameIndex, timeMs).');window.__sceneEngineAdapters.push({id,layerId,seekFrame});},seek(ms){const frameIndex=Math.floor(ms*30/1000);for(const adapter of window.__sceneEngineAdapters){try{const accepted=adapter.seekFrame(frameIndex,ms);if(accepted===false)throw new Error('adapter rejected frame');}catch(error){const failure=new Error('Adapter '+adapter.id+' on layer '+adapter.layerId+' cannot seek frame '+frameIndex+': '+error.message);failure.code='UNSEEKABLE';failure.adapterId=adapter.id;failure.layerId=adapter.layerId;failure.frame=frameIndex;throw failure;}}for(const scene of document.querySelectorAll('.scene')){const item=sceneModel.find(x=>x.id===scene.dataset.sceneId);if(!item)continue;const local=ms-item.startMs;const active=local>=0&&local<item.durationMs;scene.style.display=active?'block':'none';for(const a of scene.getAnimations({subtree:true})){a.pause();a.currentTime=Math.max(0,local);}for(const el of scene.querySelectorAll('.layer')){const start=Number(el.dataset.localStart),duration=Number(el.dataset.localDuration),t=local-start;const visible=active&&t>=0&&t<duration;el.style.display=visible?'':'none';const tracks=el.dataset.tracks?JSON.parse(el.dataset.tracks):[];let sx=Number(el.dataset.baseScaleX||1),sy=Number(el.dataset.baseScaleY||1);for(const track of tracks){const value=seTrack(track,t);if(track.property==='scaleX')sx=Number(value);else if(track.property==='scaleY')sy=Number(value);else seApplyTrack(el,track,value);}if(tracks.some(track=>track.property==='scaleX'||track.property==='scaleY'))el.style.scale=sx+' '+sy;const counter=el.dataset.counter?JSON.parse(el.dataset.counter):null;if(counter){const text=el.querySelector('.text');if(text)text.textContent=seFormatCounter(counter,t/duration);}const entrance=el.dataset.entrance;if(entrance)seEntrance(el,entrance,t/Number(el.dataset.entranceDuration||500));}for(const cue of scene.querySelectorAll('.caption')){const show=active&&local>=Number(cue.dataset.captionStart)&&local<Number(cue.dataset.captionEnd);cue.style.opacity=show?'1':'0';}}for(const video of document.querySelectorAll('.stage-media')){const scene=sceneModel.find(x=>x.id===video.dataset.sceneId);const sceneLocal=scene?ms-scene.startMs:ms;const local=sceneLocal-Number(video.dataset.localStart);const duration=Number(video.dataset.localDuration);const visible=sceneLocal>=0&&sceneLocal<scene.durationMs&&local>=0&&local<duration;video.parentElement.style.display=visible?'block':'none';video.pause();const mediaTime=video.dataset.staticMediaTimeMs===undefined?local:Number(video.dataset.staticMediaTimeMs);try{video.currentTime=Math.max(0,Math.min(video.duration||duration/1000,mediaTime/1000));}catch{}if(video.dataset.entrance)seEntrance(video,video.dataset.entrance,local/Number(video.dataset.entranceDuration||500));}return true;},verifyAdapters(){const adapters=window.__sceneEngineAdapters;if(!adapters.length)return {status:'pass',checked:0};const end=Math.max(1,${Math.max(1, durationMs - 1)});try{this.seek(end);this.seek(0);this.seek(end);this.seek(0);return {status:'pass',checked:adapters.length};}catch(error){return {status:'fail',code:error.code||'UNSEEKABLE',adapterId:error.adapterId||null,layerId:error.layerId||null,frame:error.frame??null,message:error.message};}},async ready(){await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));const videos=[...document.querySelectorAll('video')];await Promise.all(videos.map(v=>v.readyState>=2?Promise.resolve():new Promise(r=>{v.addEventListener('loadeddata',r,{once:true});setTimeout(r,3000);})));await Promise.all(videos.map(v=>v.seeking?new Promise(r=>{v.addEventListener('seeked',r,{once:true});setTimeout(r,3000);}):Promise.resolve()));return true;}};
window.__timelines=window.__timelines||{};if(window.gsap){const playhead={time:0};window.__timelines['scene-engine']=window.gsap.timeline({paused:true,onUpdate(){window.__sceneEngine.seek(playhead.time*1000);}}).to(playhead,{time:${durationMs/1000},duration:${durationMs/1000},ease:'none'});}window.__sceneEngine.seek(0);window.__sceneEngine.ready();`;
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
    return `${cameraCss(scene)}<div id="scene-${esc(scene.id)}" class="scene clip" data-scene-id="${esc(scene.id)}" data-start="${scene._startMs / 1000}" data-duration="${scene.durationMs / 1000}" data-track-index="${index}" style="background:${scene.background ?? model.story.background ?? '#FFFFFF'}">${layers}${sceneCaptionsHtml(scene, captionMode)}</div>`;
  }).join('\n');
  const media = model.scenes.map((scene) => (scene.layers ?? []).map((layer) => mediaLayerHtml(model, scene, layer, captureMap, compositionDir)).join('')).join('');
  const modelPayload = JSON.stringify(model.scenes.map((scene) => ({ id: scene.id, startMs: scene._startMs, durationMs: scene.durationMs, layers: allLayers(scene).map((layer) => ({ id: layer.id, startMs: layer.startMs, durationMs: layer.durationMs })) })));
  return `<!doctype html><html lang="${esc(model.story.language ?? 'en')}"><head><title>${esc(model.story.title)}</title><meta charset="utf-8"><meta name="viewport" content="width=1920,initial-scale=1"><style>
${PINNED_FONT_FACES}html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:${model.story.background ?? '#FFFFFF'};font-family:Arial,sans-serif}#stage{position:relative;width:1920px;height:1080px;overflow:hidden;background:${model.story.background ?? '#FFFFFF'}}.scene{position:absolute;inset:0;overflow:hidden}.scene-camera-plane{position:absolute;inset:0;pointer-events:none}.layer{position:absolute;box-sizing:border-box}.text{box-sizing:border-box;width:100%;height:100%;padding-top:3px;overflow:hidden}.bullet{display:flex;gap:.35em;padding-left:calc(1.1em * var(--level,1));position:relative}.bullet[data-level="1"]{padding-left:1.5em}.bullet[data-level="2"]{padding-left:2.5em}.bullet[data-level="3"]{padding-left:3.5em}.bullet-marker{min-width:1.1em}.shape-svg{display:block;overflow:visible;width:100%;height:100%}.caption{position:absolute;left:160px;right:160px;bottom:60px;min-height:64px;padding:18px 30px;background:rgba(12,18,29,.82);border-radius:12px;color:white;font:600 30px/1.2 Arial,sans-serif;text-align:center;z-index:99999;opacity:0;box-sizing:border-box}.unsupported{width:100%;height:100%;background:#f2f4f7;color:#667085;display:grid;place-items:center;font:18px Arial}
</style></head><body><div id="stage" data-rk-stage data-composition-id="scene-engine" data-start="0" data-width="1920" data-height="1080" data-duration="${model.durationMs / 1000}" data-fps="30">${scenes}${media}</div>
<script src="assets/gsap.min.js"></script><script>${seekRuntime(modelPayload, model.durationMs)}
</script></body></html>`;
}

export function writeComposition(model, directory, options) {
  fs.mkdirSync(directory, { recursive: true });
  const assetDirectory = path.join(directory, 'assets');
  fs.mkdirSync(assetDirectory, { recursive: true });
  fs.copyFileSync(path.join(ENGINE_ROOT, 'node_modules/gsap/dist/gsap.min.js'), path.join(assetDirectory, 'gsap.min.js'));
  const html = generateHtml(model, { ...options, compositionDir: directory });
  fs.writeFileSync(path.join(directory, 'index.html'), html);
  return path.join(directory, 'index.html');
}

function sampleLayerTree(layer, parentTime, appCaptures = new Map()) {
  const state = sampleLayer(layer, parentTime);
  const localTime = parentTime - layer.startMs;
  if (state.entrance && state.entrance !== 'none') state.__entranceProgress = Math.max(0, Math.min(1, localTime / (state.entranceDurationMs ?? 500)));
  if (state.type === 'video' || state.type === 'appDemo') state.__mediaTimeMs = Math.max(0, localTime);
  if (layer.type === 'appDemo' && appCaptures.has(layer.id)) {
    const capture = appCaptures.get(layer.id);
    const index = Math.min(capture.frameCount - 1, Math.max(0, Math.floor(localTime * 30 / 1000)));
    const filename = path.join(capture.directory, 'frames', `frame-${String(index).padStart(6, '0')}.png`);
    state.__checkFrameDataUrl = `data:image/png;base64,${fs.readFileSync(filename).toString('base64')}`;
  }
  if (layer.type === 'group') state.children = (layer.children ?? []).filter((child) => localTime >= child.startMs && localTime < child.startMs + child.durationMs).map((child) => sampleLayerTree(child, localTime, appCaptures));
  delete state.tracks;
  delete state.build;
  delete state.rangeTracks;
  delete state.reveal;
  return state;
}

export function generateStaticHtml(model, atMs, { appCaptures = new Map() } = {}) {
  const activeScenes = model.scenes.filter((scene) => atMs >= scene._startMs && atMs < scene._startMs + scene.durationMs);
  const scenes = activeScenes.map((scene) => {
    const localTime = atMs - scene._startMs;
    const camera = scene.camera ? { ...scene.camera, tracks: [] } : undefined;
    if (camera) for (const track of scene.camera.tracks ?? []) {
      const defaults = { x: 0, y: 0, zoom: 1, rotation: 0 };
      camera[track.property] = sampleTrack(camera[track.property] ?? defaults[track.property], track, localTime);
    }
    const activeLayers = (scene.layers ?? []).filter((layer) => localTime >= layer.startMs && localTime < layer.startMs + layer.durationMs).map((layer) => sampleLayerTree(layer, localTime, appCaptures)).map((layer) => ({ ...layer, startMs: 0, durationMs: 1000 }));
    const captions = (scene.captions ?? []).filter((cue) => localTime >= cue.startMs && localTime < cue.endMs && !captionCoveredByAuthorLayer(scene, cue, localTime)).map((cue) => ({ ...cue, startMs: 0, endMs: 1000 }));
    return { ...scene, _startMs: 0, startMs: 0, durationMs: 1000, layers: activeLayers, captions, camera };
  });
  const staticModel = { ...model, durationMs: 1000, frameCount: 30, scenes, story: { ...model.story, durationMs: 1000 } };
  let html = generateHtml(staticModel, { captionMode: 'burn-in' });
  html = html.replace('<script src="assets/gsap.min.js"></script>', '');
  html = html.replace('window.__sceneEngine.seek(0);window.__sceneEngine.ready();', 'window.__sceneEngine.seek(0);window.__sceneEngine.ready();');
  return html;
}
