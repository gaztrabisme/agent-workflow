import type { Scale } from './model.ts';

export function scaleMap(value: number, scale: Scale) {
  if (scale.type !== 'linear' || scale.domain.length !== 2 || scale.range.length !== 2) throw new Error(`unsupported scale: ${scale.type}`);
  return scale.range[0] + (value-scale.domain[0])/(scale.domain[1]-scale.domain[0])*(scale.range[1]-scale.range[0]);
}

export function parseMLPath(d: string): number[][] {
  const tokens = d.match(/[ML]|[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?/g) ?? [];
  if (tokens.join('').replaceAll('+','') !== d.replace(/[\s,]+/g,'').replaceAll('+','')) throw new Error('path has unsupported commands or syntax');
  const points: number[][] = []; let command = '';
  for (let i=0;i<tokens.length;) {
    if (tokens[i] === 'M' || tokens[i] === 'L') command = tokens[i++];
    if (!command || i+1>=tokens.length || /[ML]/.test(tokens[i+1])) throw new Error('path has incomplete coordinates');
    points.push([Number(tokens[i++]),Number(tokens[i++])]);
    if (command === 'M') command = 'L';
  }
  if (!points.length) throw new Error('path has no vertices');
  return points;
}
