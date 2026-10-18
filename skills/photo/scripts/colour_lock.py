"""Put an AI-edited photo's colour balance back to the stage-1 colour, keeping the AI's brightness.

The edit may relight (change lightness) but must not re-tint. This shifts the edited image's mean a* and b*
(CIE Lab) to the stage-1 image's, for each of five lightness bands, so shadows and highlights are matched
separately. Lightness is untouched.

Usage: colour_lock.py STAGE1 EDITED OUT   -> prints JSON with the a*/b* shifts applied
"""
import json
import sys

import numpy as np
from PIL import Image

M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
WHITE = np.array([0.9505, 1.0, 1.089])


def to_lab(rgb):
    c = rgb / 255.0
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    xyz = lin @ M.T / WHITE
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def to_rgb(lab):
    fy = (lab[..., 0] + 16) / 116
    f = np.stack([fy + lab[..., 1] / 500, fy, fy - lab[..., 2] / 200], -1)
    xyz = np.where(f ** 3 > 0.008856, f ** 3, (f - 16 / 116) / 7.787) * WHITE
    lin = xyz @ np.linalg.inv(M).T
    lin = np.clip(lin, 0, 1)
    c = np.where(lin <= 0.0031308, lin * 12.92, 1.055 * lin ** (1 / 2.4) - 0.055)
    return np.clip(np.rint(c * 255), 0, 255).astype(np.uint8)


EDGES = [0, 20, 40, 60, 80, 101]


def band_means(lab):
    out = []
    for lo, hi in zip(EDGES[:-1], EDGES[1:]):
        m = (lab[..., 0] >= lo) & (lab[..., 0] < hi)
        out.append((lab[m][:, 1:].mean(0) if m.sum() > 500 else None, (lo + hi) / 2))
    return out


def lock(stage1, edited):
    ref = Image.open(stage1).convert("RGB")
    ed = Image.open(edited).convert("RGB")
    ref = ref.resize(ed.size, Image.LANCZOS)
    lr, le = to_lab(np.asarray(ref, float)), to_lab(np.asarray(ed, float))
    # match by band of the stage-1 lightness at the same place, so relighting does not move pixels between bands
    shifts = []
    for lo, hi in zip(EDGES[:-1], EDGES[1:]):
        m = (lr[..., 0] >= lo) & (lr[..., 0] < hi)
        if m.sum() > 500:
            shifts.append(((lo + hi) / 2, lr[m][:, 1:].mean(0) - le[m][:, 1:].mean(0)))
    xs = np.array([s[0] for s in shifts]); da = np.array([s[1][0] for s in shifts]); db = np.array([s[1][1] for s in shifts])
    L = lr[..., 0]
    out = le.copy()
    out[..., 1] += np.interp(L, xs, da)
    out[..., 2] += np.interp(L, xs, db)
    return Image.fromarray(to_rgb(out)), [dict(L=float(x), da=round(float(a), 2), db=round(float(b), 2)) for x, a, b in zip(xs, da, db)]


if __name__ == "__main__":
    img, shifts = lock(sys.argv[1], sys.argv[2])
    img.save(sys.argv[3], quality=95) if sys.argv[3].lower().endswith(".jpg") else img.save(sys.argv[3])
    print(json.dumps(shifts))
