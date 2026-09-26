#!/usr/bin/env python3
"""Measure an image for the review tests in references/method/mistakes-checklist.md.

Runs without Photoshop. Value is OKLab L, saturation is OKLCH chroma (see
references/method/measurement.md for why). Thresholds printed as PASS/FAIL are this
skill's working defaults, not the teacher's numbers; the checklist says when to override.

  checks.py value  IMG --focal x0,y0,x1,y1 [--levels 4] [--out DIR]   T1, T2 (+ grayscale PNGs)
  checks.py chroma IMG --focal x0,y0,x1,y1 [--rings 5]                T5
  checks.py spread IMG                                                  T6
  checks.py sample IMG x,y [x,y ...]                                    T7 (OKLCH and warm/cool band)
  checks.py contrast HEX HEX                                            WCAG 2 contrast ratio

Coordinates are pixels, or fractions of width/height when every value is <= 1.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image

# Björn Ottosson's OKLab matrices (bottosson.github.io/posts/oklab).
M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929],
               [0.2119034982, 0.6806995451, 0.1073969566],
               [0.0883024619, 0.2817188376, 0.6299787005]])
M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468],
               [1.9779984951, -2.4285922050, 0.4505937099],
               [0.0259040371, 0.7827717662, -0.8086757660]])
# Photoshop Hue/Saturation ranges: 30° core, 30° falloff each side (frames at 1140 · U4 · L18 · 05:09–07:27).
RANGES = {'Reds': 0, 'Yellows': 60, 'Greens': 120, 'Cyans': 180, 'Blues': 240, 'Magentas': 300}


def to_linear(c: np.ndarray) -> np.ndarray:
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def oklab(rgb: np.ndarray) -> np.ndarray:
    return np.cbrt(to_linear(rgb) @ M1.T) @ M2.T


def oklch(rgb: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    lab = oklab(rgb)
    return lab[..., 0], np.hypot(lab[..., 1], lab[..., 2]), np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) % 360


def wcag_luminance(rgb: np.ndarray) -> float:
    return float(to_linear(rgb) @ np.array([0.2126, 0.7152, 0.0722]))


def load(path: Path) -> np.ndarray:
    return np.asarray(Image.open(path).convert('RGB'), dtype=float) / 255


def box(spec: str, shape: tuple[int, ...]) -> tuple[int, int, int, int]:
    values = [float(v) for v in spec.split(',')]
    if all(v <= 1 for v in values):
        values = [values[0] * shape[1], values[1] * shape[0], values[2] * shape[1], values[3] * shape[0]]
    x0, y0, x1, y1 = (int(round(v)) for v in values)
    return x0, y0, x1, y1


def band(hue: float, chroma: float) -> str:
    if chroma < 0.02:
        return 'neutral'
    if 20 <= hue <= 100:
        return 'warm'
    if 200 <= hue <= 320:
        return 'cool'
    return 'boundary (green or purple side: judge in context)'


def cmd_value(args) -> int:
    rgb = load(args.image)
    L = oklab(rgb)[..., 0]
    x0, y0, x1, y1 = box(args.focal, rgb.shape)
    gy, gx = np.gradient(L)
    edge = np.hypot(gx, gy)
    inside = np.zeros_like(L, dtype=bool)
    inside[y0:y1, x0:x1] = True
    area = inside.mean()
    share = edge[inside].sum() / max(edge.sum(), 1e-9)
    ratio = share / max(area, 1e-9)
    levels = np.clip(np.floor(L * args.levels), 0, args.levels - 1) / max(args.levels - 1, 1)
    out = Path(args.out or args.image.parent)
    stem = args.image.stem
    Image.fromarray((np.clip(L, 0, 1) * 255).astype(np.uint8)).save(out / f'{stem}-value.png')
    Image.fromarray((levels * 255).astype(np.uint8)).save(out / f'{stem}-levels{args.levels}.png')
    print(f'Focal box covers {area:.1%} of the image and holds {share:.1%} of the value-edge energy '
          f'({ratio:.2f}x its area share).')
    print(f'Focal mean L {L[inside].mean():.3f}, rest {L[~inside].mean():.3f}; '
          f'focal L range {np.ptp(L[inside]):.3f}, rest {np.ptp(L[~inside]):.3f}.')
    print(f'T1 {"PASS" if ratio >= 2 else "FAIL"} (default: focal box holds at least 2x its area share of value edges).')
    print(f'Wrote {stem}-value.png and {stem}-levels{args.levels}.png to {out}; T2 is judged on the levels image.')
    return 0


def cmd_chroma(args) -> int:
    rgb = load(args.image)
    _, C, _ = oklch(rgb)
    x0, y0, x1, y1 = box(args.focal, rgb.shape)
    cy, cx = (y0 + y1) / 2, (x0 + x1) / 2
    yy, xx = np.indices(C.shape)
    dist = np.hypot(yy - cy, xx - cx)
    edges = np.linspace(0, dist.max() + 1, args.rings + 1)
    means = []
    for i in range(args.rings):
        ring = (dist >= edges[i]) & (dist < edges[i + 1])
        means.append(float(C[ring].mean()) if ring.any() else 0.0)
        print(f'ring {i + 1} (distance {edges[i]:.0f}-{edges[i + 1]:.0f}px): mean OKLCH C {means[-1]:.3f}')
    inner = float(C[y0:y1, x0:x1].mean())
    print(f'Focal box mean C {inner:.3f}; outermost ring {means[-1]:.3f}.')
    print(f'T5 {"PASS" if inner >= max(means[1:]) else "CHECK"} (default: the focal box is at least as chromatic as '
          f'every ring outside it; an inverted layout, such as the terrifying recipe, is a deliberate exception).')
    return 0


def cmd_spread(args) -> int:
    hsv = np.asarray(Image.open(args.image).convert('RGB').convert('HSV'), dtype=float)
    hue, sat = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255
    colored = sat > 0.1
    shares = {}
    for name, center in RANGES.items():
        distance = np.abs((hue - center + 180) % 360 - 180)
        weight = np.clip((45 - distance) / 30, 0, 1)
        shares[name] = float((weight * colored).sum() / colored.size)
    for name, share in sorted(shares.items(), key=lambda item: -item[1]):
        print(f'{name:<9} moves {share:.1%} of the image')
    ordered = sorted(shares.values(), reverse=True)
    fail = ordered[0] > 0.8 and ordered[1] < 0.05
    print(f'T6 {"FAIL" if fail else "PASS"} (default: fails if one range moves more than 80% and no other range moves 5%; '
          f'a deliberately restrained or pastel palette may fail on purpose, 1140 · U4 · L18 · 05:09–07:27).')
    return 0


def cmd_sample(args) -> int:
    rgb = load(args.image)
    for point in args.points:
        x, y = (float(v) for v in point.split(','))
        if x <= 1 and y <= 1:
            x, y = x * (rgb.shape[1] - 1), y * (rgb.shape[0] - 1)
        pixel = rgb[int(round(y)), int(round(x))]
        L, C, H = (float(v) for v in oklch(pixel))
        hexcode = '#%02X%02X%02X' % tuple(int(round(v * 255)) for v in pixel)
        print(f'({x:.0f},{y:.0f}) {hexcode}  OKLCH L {L:.3f} C {C:.3f} h {H:.0f}  {band(H, C)}')
    return 0


def cmd_contrast(args) -> int:
    colors = [np.array([int(h.lstrip('#')[i:i + 2], 16) / 255 for i in (0, 2, 4)]) for h in (args.a, args.b)]
    high, low = sorted((wcag_luminance(c) for c in colors), reverse=True)
    ratio = (high + 0.05) / (low + 0.05)
    print(f'{args.a} on {args.b}: {ratio:.2f}:1  AA text {"pass" if ratio >= 4.5 else "fail"}, '
          f'AA large text {"pass" if ratio >= 3 else "fail"}, AAA {"pass" if ratio >= 7 else "fail"}')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    value = sub.add_parser('value')
    value.add_argument('image', type=Path)
    value.add_argument('--focal', required=True)
    value.add_argument('--levels', type=int, default=4)
    value.add_argument('--out')
    chroma = sub.add_parser('chroma')
    chroma.add_argument('image', type=Path)
    chroma.add_argument('--focal', required=True)
    chroma.add_argument('--rings', type=int, default=5)
    spread = sub.add_parser('spread')
    spread.add_argument('image', type=Path)
    sample = sub.add_parser('sample')
    sample.add_argument('image', type=Path)
    sample.add_argument('points', nargs='+')
    contrast = sub.add_parser('contrast')
    contrast.add_argument('a')
    contrast.add_argument('b')
    args = parser.parse_args()
    handlers = {'value': cmd_value, 'chroma': cmd_chroma, 'spread': cmd_spread, 'sample': cmd_sample,
                'contrast': cmd_contrast}
    return handlers[args.command](args)


if __name__ == '__main__':
    sys.exit(main())
