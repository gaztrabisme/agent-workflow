export type RGB = [number, number, number];
export type Lab = [number, number, number];
const clip = (x: number) => Math.max(0, Math.min(1, x));
export const linear = (x: number) => x <= 0.04045 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4;
export const srgb = (x: number) => x <= 0.0031308 ? 12.92 * x : 1.055 * x ** (1 / 2.4) - 0.055;
export function parseHex(value: string): RGB {
  const s = value.replace('#',''); if (!/^(?:[\da-f]{3}|[\da-f]{6})$/i.test(s)) throw new Error(`Invalid hex colour: ${value}`);
  const h = s.length === 3 ? [...s].map(c => c + c).join('') : s;
  return [0,2,4].map(i => parseInt(h.slice(i,i+2),16) / 255) as RGB;
}
export function oklab(rgb: RGB): Lab {
  const [r,g,b] = rgb.map(linear), l = Math.cbrt(.4122214708*r+.5363325363*g+.0514459929*b);
  const m = Math.cbrt(.2119034982*r+.6806995451*g+.1073969566*b), s = Math.cbrt(.0883024619*r+.2817188376*g+.6299787005*b);
  return [.2104542553*l+.793617785*m-.0040720468*s, 1.9779984951*l-2.428592205*m+.4505937099*s, .0259040371*l+.7827717662*m-.808675766*s];
}
export const distance = (a: Lab, b: Lab) => Math.hypot(a[0]-b[0],a[1]-b[1],a[2]-b[2]);
export function luminance(rgb: RGB) { return rgb.map(linear).reduce((s,c,i)=>s+c*[.2126,.7152,.0722][i],0); }
export function contrast(a: RGB, b: RGB) { const [hi,lo]=[luminance(a),luminance(b)].sort((x,y)=>y-x); return (hi+.05)/(lo+.05); }
const matrices: Record<string, number[][]> = {
  protanopia:[[.152286,1.052583,-.204868],[.114503,.786281,.099216],[-.003882,-.048116,1.051998]],
  deuteranopia:[[.367322,.860646,-.227968],[.280085,.672501,.047413],[-.011820,.042940,.968881]],
  tritanopia:[[1.255528,-.076749,-.178779],[-.078411,.930809,.147602],[.004733,.691367,.303900]],
};
export function simulate(rgb: RGB, vision: string): RGB {
  if (vision === 'normal') return rgb;
  const m = matrices[vision]; if (!m) throw new Error(`Unknown vision type: ${vision}`);
  const l = rgb.map(linear); return m.map(row => clip(srgb(row.reduce((s,x,i)=>s+x*l[i],0)))) as RGB;
}
export function cvdDistance(a: RGB, b: RGB, vision: string) { return distance(oklab(simulate(a,vision)),oklab(simulate(b,vision))); }
