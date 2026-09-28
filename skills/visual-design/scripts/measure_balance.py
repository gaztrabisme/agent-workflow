"""Luminance-contrast-weighted visual center."""

from __future__ import annotations

import math

import numpy as np

from pixels import luminance


def measure_balance(rgb: np.ndarray, intent: str | None = None) -> tuple[object, object, str]:
    lum = luminance(rgb)
    weights = np.abs(lum - np.median(lum))
    total = float(weights.sum())
    h, w = lum.shape
    yy, xx = np.indices(lum.shape, dtype=float)
    cx = float(((xx + 0.5) * weights).sum() / total) if total else w / 2
    cy = float(((yy + 0.5) * weights).sum() / total) if total else h / 2
    distance = math.hypot(cx - w / 2, cy - h / 2) / math.hypot(w, h)
    value = {"centroid_px": [round(cx, 3), round(cy, 3)], "distance_diagonals": distance}
    if intent == "asymmetric":
        return value, "vision review", "not_judged"
    if intent != "centered":
        return value, "declare centered/asymmetric; vision review", "not_judged"
    return value, 0.08, "pass" if distance <= 0.08 else "fail"
