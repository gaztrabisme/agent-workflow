"""Focal-area luminance-gradient energy per unit area."""

from __future__ import annotations

import math

import numpy as np

from pixels import luminance


def measure_focal(rgb: np.ndarray, box: list[float] | None) -> tuple[object, object, str]:
    if not box:
        return {"reason": "missing data-rk-focal box"}, 1.25, "skipped"
    lum = luminance(rgb)
    gy, gx = np.gradient(lum)
    energy = np.hypot(gx, gy)
    h, w = lum.shape
    x, y, bw, bh = box
    x0, y0 = max(0, int(math.floor(x))), max(0, int(math.floor(y)))
    x1, y1 = min(w, int(math.ceil(x + bw))), min(h, int(math.ceil(y + bh)))
    if x1 <= x0 or y1 <= y0:
        return {"reason": "focal box is outside the PNG"}, 1.25, "skipped"
    area_share = (x1 - x0) * (y1 - y0) / (w * h)
    share = float(energy[y0:y1, x0:x1].sum() / max(float(energy.sum()), 1e-12))
    ratio = share / max(area_share, 1e-12)
    value = {"edge_energy_share": share, "area_share": area_share, "energy_per_area": ratio}
    return value, 1.25, "pass" if ratio >= 1.25 else "fail"
