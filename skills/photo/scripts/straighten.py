"""Estimate and correct camera roll (sideways tilt) from upright edges: walls, doors, windows, screens.

Method: OpenCV's line-segment detector finds straight segments. Segments within 12 degrees of vertical
are kept. Their lean is modelled as   lean = roll + k * (x_offset_from_centre)   because pointing the
camera up or down makes uprights fan out from the centre (keystone) while roll tilts them all equally.
A weighted (by length) least-squares fit with outlier rejection gives roll at the image centre.
A photo is only rotated when the fit is confident: enough upright length, small residual, |roll| >= 0.3
and <= 5 degrees.

Rotation is done on the full-size image with bicubic resampling, then cropped to the largest centred
rectangle of the original aspect ratio that contains no empty corners.

Usage:
  straighten.py estimate IMG [IMG ...]           -> JSON lines
  straighten.py apply IN OUT --angle DEG          (positive = rotate counter-clockwise)
  straighten.py selftest IMG [IMG ...]            rotate by known angles and check the estimate follows
"""
import argparse
import json
import math
import sys

import cv2
import numpy as np
from PIL import Image

ANALYSIS = 1600
MAX_FROM_VERTICAL = 12.0
MIN_ROLL, MAX_ROLL = 0.5, 5.0  # 0.5: above the self-test error (max 0.46 deg)


def _gray(img):
    im = img.convert("L")
    im.thumbnail((ANALYSIS, ANALYSIS))
    return np.asarray(im)


def segments(gray):
    lsd = cv2.createLineSegmentDetector(cv2.LSD_REFINE_STD)
    lines = lsd.detect(gray)[0]
    if lines is None:
        return np.zeros((0, 4))
    return lines.reshape(-1, 4)


def estimate_gray(gray):
    h, w = gray.shape
    segs = segments(gray)
    x0, y0, x1, y1 = segs.T
    dx, dy = x1 - x0, y1 - y0
    length = np.hypot(dx, dy)
    # orient every segment top-to-bottom; lean = angle from vertical, positive when the top leans right
    flip = dy < 0
    dx = np.where(flip, -dx, dx)
    dy = np.abs(dy)
    lean = np.degrees(np.arctan2(-dx, dy))  # image y grows downward: top-right lean gives negative dx
    keep = (length >= 0.04 * math.hypot(w, h)) & (np.abs(lean) <= MAX_FROM_VERTICAL)
    if keep.sum() < 4:
        return dict(roll=None, reason="fewer than 4 long upright edges", n=int(keep.sum()))
    xs = ((x0 + x1) / 2 - w / 2)[keep] / w
    a, L = lean[keep], length[keep]
    m = np.ones(len(a), bool)
    for _ in range(5):
        A = np.stack([np.ones(m.sum()), xs[m]], 1)
        W = np.sqrt(L[m])
        coef, *_ = np.linalg.lstsq(A * W[:, None], a[m] * W, rcond=None)
        res = a - (coef[0] + coef[1] * xs)
        new = np.abs(res) <= max(1.0, 2.5 * np.sqrt(np.average(res[m] ** 2, weights=L[m])))
        if (new == m).all():
            break
        m = new
    roll, slope = float(coef[0]), float(coef[1])
    rms = float(np.sqrt(np.average(res[m] ** 2, weights=L[m])))
    total = float(L[m].sum() / h)  # upright length in picture heights
    spread = float(xs[m].max() - xs[m].min()) if m.sum() > 1 else 0.0
    confident = m.sum() >= 4 and total >= 0.8 and rms <= 1.2
    return dict(roll=round(roll, 2), keystone=round(slope, 2), rms=round(rms, 2), n=int(m.sum()),
                upright_length=round(total, 2), x_spread=round(spread, 2), confident=bool(confident))


def decide(est):
    if est.get("roll") is None or not est.get("confident"):
        return 0.0
    r = est["roll"]
    if abs(r) < MIN_ROLL or abs(r) > MAX_ROLL:
        return 0.0
    if abs(r) > 3.0 and est["upright_length"] < 2.0:  # IMG_6787: -4.35 from short edges, visibly wrong
        return 0.0
    # rotating the image counter-clockwise by a makes uprights lean left by a, so rotating by +r removes lean r
    return r


def crop_box(w, h, deg):
    """Largest centred rectangle with the original aspect that fits inside the rotated frame."""
    t = math.radians(abs(deg))
    c, s = math.cos(t), math.sin(t)
    # scale factor so a w*h box rotated by t fits inside the original w*h canvas
    k = min(w / (w * c + h * s), h / (w * s + h * c))
    cw, ch = w * k, h * k
    return (int(round((w - cw) / 2)), int(round((h - ch) / 2)), int(round((w + cw) / 2)), int(round((h + ch) / 2)))


def rotate(img, deg, crop=True):
    out = img.rotate(deg, resample=Image.BICUBIC, expand=False)
    if crop and deg:
        out = out.crop(crop_box(img.width, img.height, deg))
    return out


def estimate(path):
    return dict(file=path, **estimate_gray(_gray(Image.open(path))))


def selftest(paths, angles=(-2.0, -1.0, 1.0, 2.0)):
    rows = []
    for p in paths:
        img = Image.open(p)
        base = estimate_gray(_gray(img))
        if not base.get("confident"):
            rows.append(dict(file=p, skipped="base estimate not confident"))
            continue
        for a in angles:
            # rotating the image counter-clockwise by a makes uprights lean left by a: expected roll = base - a
            e = estimate_gray(_gray(rotate(img, a, crop=True)))
            err = None if e.get("roll") is None else round(e["roll"] - (base["roll"] - a), 2)
            rows.append(dict(file=p, applied=a, base=base["roll"], got=e.get("roll"), error=err, confident=e.get("confident")))
    return rows


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("estimate"); s.add_argument("images", nargs="+")
    s = sub.add_parser("apply"); s.add_argument("inp"); s.add_argument("out"); s.add_argument("--angle", type=float, required=True)
    s = sub.add_parser("selftest"); s.add_argument("images", nargs="+")
    a = ap.parse_args()
    if a.cmd == "estimate":
        for p in a.images:
            e = estimate(p)
            e["rotate_by"] = decide(e)
            print(json.dumps(e))
    elif a.cmd == "apply":
        img = Image.open(a.inp)
        icc = img.info.get("icc_profile")
        rotate(img.convert("RGB"), a.angle).save(a.out, quality=95, **({"icc_profile": icc} if icc else {}))
    else:
        rows = selftest(a.images)
        for r in rows:
            print(json.dumps(r))
        errs = [abs(r["error"]) for r in rows if r.get("error") is not None]
        if errs:
            print(json.dumps(dict(n=len(errs), mean_abs_error=round(float(np.mean(errs)), 3), max_abs_error=round(float(np.max(errs)), 3))))
        sys.exit(0 if errs and max(errs) <= 0.3 else 1)


if __name__ == "__main__":
    main()
