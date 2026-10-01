const easeCurves = {
  linear: [0, 0, 1, 1],
  'ease-in': [0.42, 0, 1, 1],
  'ease-out': [0, 0, 0.58, 1],
  'ease-in-out': [0.42, 0, 0.58, 1]
};

function cubic(t, a, b) { return 3 * (1 - t) ** 2 * t * a + 3 * (1 - t) * t ** 2 * b + t ** 3; }

export function ease(progress, easing = 'linear') {
  const p = Math.max(0, Math.min(1, progress));
  if (easing === 'step-start') return 1;
  if (easing === 'step-end') return p < 1 ? 0 : 1;
  const bezier = Array.isArray(easing) ? easing : (typeof easing === 'object' ? easing.cubicBezier : easeCurves[easing]);
  if (!bezier) return p;
  const [x1, y1, x2, y2] = bezier;
  let low = 0; let high = 1; let t = p;
  for (let i = 0; i < 18; i += 1) {
    const x = cubic(t, x1, x2);
    if (Math.abs(x - p) < 1e-7) break;
    if (x < p) low = t; else high = t;
    t = (low + high) / 2;
  }
  return cubic(t, y1, y2);
}

function srgbToLinear(channel) { return channel <= 0.04045 ? channel / 12.92 : ((channel + 0.055) / 1.055) ** 2.4; }
function linearToSrgb(channel) { return channel <= 0.0031308 ? 12.92 * channel : 1.055 * channel ** (1 / 2.4) - 0.055; }
function colorToOklab(color) {
  const rgb = color.match(/[0-9a-f]{2}/gi)?.map((c) => srgbToLinear(parseInt(c, 16) / 255)) ?? [0, 0, 0];
  const [r, g, b] = rgb;
  const l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3);
  const m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3);
  const s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3);
  return [0.2104542553 * l + 0.793617785 * m - 0.0040720468 * s, 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s, 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s];
}
function oklabToColor([L, a, b]) {
  const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3;
  const m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3;
  const s = (L - 0.0894841775 * a - 1.291485548 * b) ** 3;
  const channels = [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s];
  return `#${channels.map((c) => Math.round(Math.max(0, Math.min(1, linearToSrgb(c))) * 255).toString(16).padStart(2, '0')).join('')}`;
}

export function interpolate(a, b, progress, path = '') {
  if (typeof a === 'number' && typeof b === 'number') return a + (b - a) * progress;
  if (typeof a === 'string' && typeof b === 'string' && /^#[0-9a-f]{6}$/i.test(a) && /^#[0-9a-f]{6}$/i.test(b)) {
    return oklabToColor(colorToOklab(a).map((component, index) => component + (colorToOklab(b)[index] - component) * progress));
  }
  return progress < 1 ? a : b;
}

function setPath(target, path, value) {
  const keys = path.split('.');
  let current = target;
  for (const key of keys.slice(0, -1)) current = current[key] ??= {};
  current[keys.at(-1)] = value;
}

export function sampleTrack(base, track, localMs) {
  const frames = track.keyframes ?? [];
  if (!frames.length || localMs < frames[0].atMs) return base;
  if (localMs >= frames.at(-1).atMs) return frames.at(-1).value;
  for (let i = 1; i < frames.length; i += 1) {
    const next = frames[i]; const previous = frames[i - 1];
    if (localMs <= next.atMs) {
      const progress = (localMs - previous.atMs) / (next.atMs - previous.atMs);
      return interpolate(previous.value, next.value, ease(progress, previous.easing ?? 'linear'), track.property);
    }
  }
  return base;
}

export function sampleLayer(layer, localMs) {
  const state = structuredClone(layer);
  const tracks = state.tracks ?? [];
  delete state.tracks;
  for (const track of tracks) setPath(state, track.property, sampleTrack(track.property.split('.').reduce((v, k) => v?.[k], state), track, localMs - layer.startMs));
  return state;
}

export function frameTimeMs(frameIndex) { return Math.floor(frameIndex * 1000 / 30); }
export function frameCount(durationMs) { return Math.ceil(durationMs * 30 / 1000); }
