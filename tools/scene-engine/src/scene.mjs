import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import Ajv2020 from 'ajv/dist/2020.js';
import schema from './storyboard.schema.json' with { type: 'json' };

const ajv = new Ajv2020({ allErrors: true, strict: false, allowUnionTypes: true });
const validateSchema = ajv.compile(schema);
const assetFields = new Set(['src', 'poster', 'audio', 'wordTimings', 'source', 'bodyFile']);

export function diagnostic(code, message, fields = {}) {
  return {
    code, message,
    pointer: fields.pointer ?? null,
    sceneId: fields.sceneId ?? null,
    layerId: fields.layerId ?? null,
    frame: fields.frame ?? null,
    path: fields.path ?? null,
    hint: fields.hint ?? null,
    severity: fields.severity ?? 'error'
  };
}

function pointerEscape(value) {
  return String(value).replaceAll('~', '~0').replaceAll('/', '~1');
}

function walk(value, callback, pointer = '') {
  if (!value || typeof value !== 'object') return;
  if (Array.isArray(value)) {
    value.forEach((item, index) => walk(item, callback, `${pointer}/${index}`));
    return;
  }
  for (const [key, child] of Object.entries(value)) {
    const childPointer = `${pointer}/${pointerEscape(key)}`;
    callback(key, child, childPointer);
    walk(child, callback, childPointer);
  }
}

function readJson(filename) {
  try {
    return JSON.parse(fs.readFileSync(filename, 'utf8'));
  } catch (error) {
    if (error.code === 'ENOENT') throw Object.assign(new Error(`Storyboard not found: ${filename}`), { code: 'STORYBOARD_MISSING', path: filename, exitCode: 2 });
    throw Object.assign(new Error(`Invalid JSON: ${error.message}`), { code: 'JSON_INVALID', path: filename, exitCode: 2 });
  }
}

function resolveTimeline(story, errors) {
  const starts = new Map();
  const seen = new Set();
  let durationMs = 0;
  for (let index = 0; index < (story.scenes ?? []).length; index += 1) {
    const scene = story.scenes[index];
    const pointer = `/scenes/${index}`;
    if (seen.has(scene.id)) errors.push(diagnostic('SCHEMA_INVALID', `Duplicate scene id '${scene.id}'.`, { pointer: `${pointer}/id` }));
    seen.add(scene.id);
    let startMs = scene.startMs;
    if (scene.after !== undefined) {
      if (scene.startMs !== undefined) errors.push(diagnostic('TIME_REFERENCE_INVALID', 'A scene must use exactly one of startMs or after.', { pointer }));
      const predecessor = story.scenes.find((candidate) => candidate.id === scene.after);
      if (!predecessor || !starts.has(scene.after)) {
        errors.push(diagnostic('TIME_REFERENCE_INVALID', `after must name an earlier scene; '${scene.after}' is not earlier.`, { pointer: `${pointer}/after`, sceneId: scene.id }));
        startMs = 0;
      } else {
        startMs = starts.get(scene.after) + predecessor.durationMs + (scene.gapMs ?? 0);
      }
    } else if (startMs === undefined) {
      errors.push(diagnostic('TIME_REFERENCE_INVALID', 'A scene must declare startMs or after.', { pointer, sceneId: scene.id }));
      startMs = 0;
    } else if (scene.gapMs !== undefined) {
      errors.push(diagnostic('TIME_REFERENCE_INVALID', 'gapMs is only valid with after.', { pointer: `${pointer}/gapMs`, sceneId: scene.id }));
    }
    starts.set(scene.id, startMs);
    durationMs = Math.max(durationMs, startMs + (scene.durationMs ?? 0));
  }
  if (story.durationMs !== undefined && story.durationMs < durationMs) {
    errors.push(diagnostic('SCHEMA_INVALID', 'Root durationMs cannot end before a scene.', { pointer: '/durationMs' }));
  }
  if (story.durationMs !== undefined) durationMs = story.durationMs;
  return { scenes: (story.scenes ?? []).map((scene) => ({ ...scene, _startMs: starts.get(scene.id) ?? 0 })), durationMs };
}

function semanticChecks(story, scenes, errors, root) {
  const ids = new Map();
  const markerIds = new Set();
  const markers = story.markers ?? [];
  for (let i = 0; i < markers.length; i += 1) {
    const marker = markers[i];
    if (markerIds.has(marker.id)) errors.push(diagnostic('SCHEMA_INVALID', `Duplicate marker id '${marker.id}'.`, { pointer: `/markers/${i}/id` }));
    markerIds.add(marker.id);
    if (!scenes.some((scene) => scene.id === marker.sceneId) || marker.atMs > (scenes.find((scene) => scene.id === marker.sceneId)?.durationMs ?? -1)) {
      errors.push(diagnostic('TIME_REFERENCE_INVALID', 'Marker must lie within its declared scene.', { pointer: `/markers/${i}`, sceneId: marker.sceneId }));
    }
  }
  let layerCount = 0;
  for (let sceneIndex = 0; sceneIndex < scenes.length; sceneIndex += 1) {
    const scene = scenes[sceneIndex];
    const sceneLayers = new Map();
    const visit = (layers, prefix, parentDuration = scene.durationMs, parentStart = 0) => {
      for (let index = 0; index < (layers ?? []).length; index += 1) {
        const layer = layers[index];
        const pointer = `${prefix}/${index}`;
        const absoluteLayerStart = parentStart + (layer.startMs ?? 0);
        layerCount += 1;
        if (ids.has(layer.id)) errors.push(diagnostic('SCHEMA_INVALID', `Duplicate layer id '${layer.id}'.`, { pointer: `${pointer}/id`, sceneId: scene.id, layerId: layer.id }));
        ids.set(layer.id, { sceneId: scene.id, pointer, layer });
        sceneLayers.set(layer.id, layer);
        if (layer.startMs + layer.durationMs > parentDuration) errors.push(diagnostic('SCHEMA_INVALID', 'Layer interval extends past its containing scene or group.', { pointer, sceneId: scene.id, layerId: layer.id }));
        const tracks = layer.tracks ?? [];
        const trackProperties = new Set();
        for (let ti = 0; ti < tracks.length; ti += 1) {
          const track = tracks[ti];
          if (trackProperties.has(track.property)) errors.push(diagnostic('TRACK_VALUE_INVALID', 'A property can be targeted by only one track per layer.', { pointer: `${pointer}/tracks/${ti}/property`, sceneId: scene.id, layerId: layer.id }));
          trackProperties.add(track.property);
          let previous = -1;
          for (let ki = 0; ki < (track.keyframes ?? []).length; ki += 1) {
            const keyframe = track.keyframes[ki];
            let atMs = keyframe.atMs;
            if (typeof atMs === 'object') {
              if (atMs.marker) {
                const marker = markers.find((item) => item.id === atMs.marker);
                const ownerScene = marker && scenes.find((item) => item.id === marker.sceneId);
                atMs = marker && ownerScene ? marker.atMs + ownerScene._startMs - scene._startMs - absoluteLayerStart + (atMs.offsetMs ?? 0) : -1;
              } else if (atMs.wordIndex !== undefined) {
                try {
                  const timingFile = scene.narration?.wordTimings ? safeAssetPath(root, scene.narration.wordTimings) : null;
                  const timing = timingFile && JSON.parse(fs.readFileSync(timingFile, 'utf8'));
                  const word = timing?.words?.[atMs.wordIndex];
                  atMs = word ? word.startMs + (scene.narration?.audioOffsetMs ?? 0) - absoluteLayerStart + (atMs.offsetMs ?? 0) : -1;
                } catch { atMs = -1; }
              }
            }
            if (!Number.isInteger(atMs) || atMs <= previous || atMs < 0 || atMs > layer.durationMs) errors.push(diagnostic('TIME_REFERENCE_INVALID', 'Track times must resolve to strictly increasing positions within the layer.', { pointer: `${pointer}/tracks/${ti}/keyframes/${ki}/atMs`, sceneId: scene.id, layerId: layer.id }));
            previous = atMs;
            if (typeof keyframe.value === 'number' && !Number.isFinite(keyframe.value)) errors.push(diagnostic('TRACK_VALUE_INVALID', 'Track values must be finite.', { pointer: `${pointer}/tracks/${ti}/keyframes/${ki}/value`, sceneId: scene.id, layerId: layer.id }));
          }
        }
        if (layer.type === 'chart') {
          const isScatter = layer.kind === 'scatter';
          for (const [si, series] of (layer.series ?? []).entries()) {
            if (isScatter ? series.xValues?.length !== series.values?.length : series.values?.length !== layer.categories?.length) {
              errors.push(diagnostic('SCHEMA_INVALID', isScatter ? 'Scatter xValues and values must have equal lengths.' : 'Each chart series needs one value per category.', { pointer: `${pointer}/series/${si}`, sceneId: scene.id, layerId: layer.id }));
            }
          }
          if (layer.kind?.includes('Stacked') && (layer.series ?? []).some((series) => series.axis === 'secondary')) errors.push(diagnostic('SCHEMA_INVALID', 'Stacked charts cannot use a secondary axis.', { pointer: `${pointer}/series`, sceneId: scene.id, layerId: layer.id }));
          if (layer.kind === 'combo' && !(layer.series ?? []).some((series) => ['column', 'line'].includes(series.kind))) errors.push(diagnostic('SCHEMA_INVALID', 'Combo charts require at least one column or line series.', { pointer: `${pointer}/series`, sceneId: scene.id, layerId: layer.id }));
        }
        if (layer.type === 'appDemo') {
          let lastStep = -1;
          for (const [stepIndex, step] of (layer.steps ?? []).entries()) {
            const stepPointer = `${pointer}/steps/${stepIndex}`;
            if (step.atMs <= lastStep) errors.push(diagnostic('SCHEMA_INVALID', 'App steps must be strictly increasing.', { pointer: `${stepPointer}/atMs`, sceneId: scene.id, layerId: layer.id }));
            lastStep = step.atMs;
            if (step.atMs > layer.durationMs) errors.push(diagnostic('SCHEMA_INVALID', 'App step lies outside its layer interval.', { pointer: `${stepPointer}/atMs`, sceneId: scene.id, layerId: layer.id }));
            if (step.locator?.role && !('name' in step.locator)) errors.push(diagnostic('SCHEMA_INVALID', 'Role locators require name.', { pointer: `${stepPointer}/locator/name`, sceneId: scene.id, layerId: layer.id }));
          }
        }
        if (layer.effects?.mask) {
          const source = (layers ?? []).find((item) => item.id === layer.effects.mask.sourceLayerId);
          if (!source || source.type !== 'shape') errors.push(diagnostic('MASK_SOURCE_INVALID', 'Mask source must name a shape layer in the same scene.', { pointer: `${pointer}/effects/mask/sourceLayerId`, sceneId: scene.id, layerId: layer.id }));
        }
        if (layer.type === 'adapter' && layer.adapterId !== 'lottie' && !layer.adapterId.startsWith('builtin:')) errors.push(diagnostic('ADAPTER_NOT_REGISTERED', `Adapter '${layer.adapterId}' is not registered by this build.`, { pointer: `${pointer}/adapterId`, sceneId: scene.id, layerId: layer.id }));
        if (layer.type === 'group') visit(layer.children, `${pointer}/children`, layer.durationMs, absoluteLayerStart);
      }
    };
    visit(scene.layers, `/scenes/${sceneIndex}/layers`);
    for (const cue of Array.isArray(scene.captions) ? scene.captions : []) {
      if (cue.startMs >= cue.endMs || cue.endMs > scene.durationMs) errors.push(diagnostic('SCHEMA_INVALID', 'Caption cue must have startMs < endMs and fit inside its scene.', { pointer: `/scenes/${sceneIndex}/captions`, sceneId: scene.id }));
    }
  }
  return layerCount;
}

function checkAssets(story, root, errors) {
  const realRoot = fs.realpathSync(root);
  walk(story, (key, value, pointer) => {
    if (!assetFields.has(key) || typeof value !== 'string' || !value) return;
    if (path.isAbsolute(value) || /^[a-z]+:\/\//i.test(value)) {
      errors.push(diagnostic('PATH_OUTSIDE_ROOT', 'Asset paths must be relative to the project root.', { pointer, path: value, hint: 'Use a project-relative file path.' }));
      return;
    }
    const candidate = path.resolve(realRoot, value);
    let realAsset;
    try { realAsset = fs.realpathSync(candidate); }
    catch { errors.push(diagnostic('ASSET_MISSING', `Asset does not exist: ${value}`, { pointer, path: candidate, hint: 'Add the asset or correct the storyboard path.' })); return; }
    const relative = path.relative(realRoot, realAsset);
    if (relative === '..' || relative.startsWith(`..${path.sep}`) || path.isAbsolute(relative)) errors.push(diagnostic('PATH_OUTSIDE_ROOT', `Asset resolves outside the project root: ${value}`, { pointer, path: realAsset, hint: 'Move the asset into the project root or change --root.' }));
  });
}

function safeAssetPath(root, value) {
  if (typeof value !== 'string' || path.isAbsolute(value)) return null;
  try {
    const absolute = fs.realpathSync(path.resolve(root, value));
    const relative = path.relative(root, absolute);
    return relative === '..' || relative.startsWith(`..${path.sep}`) || path.isAbsolute(relative) ? null : absolute;
  } catch { return null; }
}

function captionLineBreak(text) {
  if ([...text].length <= 42) return text;
  const words = text.split(/\s+/);
  for (let cut = 1; cut < words.length; cut += 1) {
    const left = words.slice(0, cut).join(' '); const right = words.slice(cut).join(' ');
    if ([...left].length <= 42 && [...right].length <= 42) return `${left}\n${right}`;
  }
  return null;
}

function generatedCaptions(scene, root, errors, index) {
  if (scene.captions !== 'fromWordTimings') return Array.isArray(scene.captions) ? scene.captions : [];
  const timingPath = safeAssetPath(root, scene.narration?.wordTimings);
  if (!timingPath) {
    errors.push(diagnostic('SCHEMA_INVALID', 'fromWordTimings requires an in-root narration.wordTimings file.', { pointer: `/scenes/${index}/narration/wordTimings`, sceneId: scene.id }));
    return [];
  }
  let timing;
  try { timing = JSON.parse(fs.readFileSync(timingPath, 'utf8')); }
  catch (error) { errors.push(diagnostic('SCHEMA_INVALID', `Cannot read word timings: ${error.message}`, { pointer: `/scenes/${index}/narration/wordTimings`, sceneId: scene.id })); return []; }
  const words = timing.words ?? [];
  const offset = scene.narration?.audioOffsetMs ?? 0;
  const language = timing.language ?? scene.narration?.language ?? 'en';
  const cues = [];
  let group = [];
  const commit = () => {
    if (!group.length) return;
    const text = captionLineBreak(group.map((word) => word.text).join(' '));
    const rawStart = group[0].startMs; const rawEnd = group.at(-1).endMs;
    cues.push({ startMs: rawStart, endMs: Math.min(rawEnd, scene.durationMs), text: text ?? group.map((word) => word.text).join(' '), language });
    group = [];
  };
  let previousEnd = -1;
  for (const [wordIndex, word] of words.entries()) {
    if (!word || typeof word.text !== 'string' || !Number.isInteger(word.startMs) || !Number.isInteger(word.endMs) || word.startMs >= word.endMs || word.startMs < previousEnd) {
      errors.push(diagnostic('SCHEMA_INVALID', 'Word timings must be ordered and each end must follow its start.', { pointer: `/scenes/${index}/narration/wordTimings/words/${wordIndex}`, sceneId: scene.id }));
      continue;
    }
    previousEnd = word.endMs;
    const normalized = { ...word, startMs: word.startMs + offset, endMs: word.endMs + offset };
    const candidate = [...group, normalized];
    const candidateText = captionLineBreak(candidate.map((item) => item.text).join(' '));
    const span = normalized.endMs - (group[0]?.startMs ?? normalized.startMs);
    const silence = group.length ? normalized.startMs - group.at(-1).endMs : 0;
    const punctuation = /[.!?]["')\]]?$/.test(group.at(-1)?.text ?? '');
    if (group.length && (punctuation || silence > 500 || span > 7000 || !candidateText)) commit();
    group.push(normalized);
  }
  commit();
  for (const [cueIndex, cue] of cues.entries()) {
    if (!cue.text || cue.startMs >= scene.durationMs || cue.startMs >= cue.endMs) errors.push(diagnostic('NARRATION_OVERFLOW', 'Generated caption falls outside its scene.', { pointer: `/scenes/${index}/captions/${cueIndex}`, sceneId: scene.id }));
  }
  return cues;
}

export function loadStoryboard(storyboardPath, { root } = {}) {
  const absolutePath = path.resolve(storyboardPath);
  const story = readJson(absolutePath);
  const errors = [];
  const valid = validateSchema(story);
  if (!valid) {
    for (const item of validateSchema.errors ?? []) errors.push(diagnostic(item.keyword === 'required' ? 'SCHEMA_INVALID' : 'SCHEMA_INVALID', item.message ?? 'Schema validation failed.', { pointer: item.instancePath || '/', path: item.params?.missingProperty ?? null, hint: item.schemaPath ?? null }));
  }
  const rootPath = path.resolve(root ?? path.dirname(absolutePath));
  if (!fs.existsSync(rootPath)) errors.push(diagnostic('ASSET_MISSING', `Project root does not exist: ${rootPath}`, { path: rootPath }));
  let realRoot = rootPath;
  try { realRoot = fs.realpathSync(rootPath); } catch { /* diagnosed above */ }
  const timeline = resolveTimeline(story, errors);
  if (fs.existsSync(realRoot)) checkAssets(story, realRoot, errors);
  const layerCount = semanticChecks(story, timeline.scenes, errors, realRoot);
  const scenes = timeline.scenes.map((scene, index) => ({ ...scene, captions: generatedCaptions(scene, realRoot, errors, index) }));
  if (story.scenes) {
    for (const scene of timeline.scenes) {
      if (scene.pptxAtMs !== undefined && (scene.pptxAtMs < 0 || scene.pptxAtMs >= scene.durationMs)) errors.push(diagnostic('SCHEMA_INVALID', 'pptxAtMs must be within the scene interval.', { pointer: `/scenes/${story.scenes.indexOf(scene)}/pptxAtMs`, sceneId: scene.id }));
    }
  }
  const durationMs = timeline.durationMs || 0;
  return {
    story, storyboardPath: absolutePath, root: realRoot, scenes, durationMs,
    frameCount: Math.ceil(durationMs * 30 / 1000), layerCount, errors, warnings: []
  };
}

export function canonicalHash(value) {
  return crypto.createHash('sha256').update(JSON.stringify(value)).digest('hex');
}

export function allLayers(scene) {
  const result = [];
  const visit = (layers) => { for (const layer of layers ?? []) { result.push(layer); if (layer.type === 'group') visit(layer.children); } };
  visit(scene.layers);
  return result;
}

export function cleanModel(model) {
  return { ...model.story, scenes: model.story.scenes };
}
