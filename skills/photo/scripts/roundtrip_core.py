import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

from scripts.color_math import delta_e_2000, rgb_to_lab
from scripts.grade_metrics import _describe, compare_metrics
from scripts.image_io import read_mask, read_rgb, resize_rgb, save_rgb, write_compare_assets


def prepare(original, mask_path, brief, out_dir):
    src, mask_file, out = Path(original).resolve(), Path(mask_path).resolve(), Path(out_dir).resolve()
    rgb = read_rgb(src)
    mask = read_mask(mask_file, rgb.shape)
    ys, xs = np.where(mask > .5)
    if not len(xs):
        raise ValueError("edit mask is empty")
    out.mkdir(parents=True, exist_ok=True)
    copied = out/src.name
    targets = [copied, out/"mask.png", out/"region-crop.png", out/"edit-brief.md"]
    inputs = {src, mask_file}
    if len({t.resolve() for t in targets}) != len(targets):
        raise ValueError("original filename conflicts with a reserved preparation filename")
    if any(t.resolve() in inputs for t in targets):
        raise ValueError("prepared output paths must differ from the original and mask")
    if any(t.exists() for t in targets):
        raise FileExistsError("prepared output files already exist")
    shutil.copy2(src, copied)
    shutil.copy2(mask_file, out/"mask.png")
    box = (max(0, int(xs.min())-8), max(0, int(ys.min())-8),
           min(rgb.shape[1], int(xs.max())+9), min(rgb.shape[0], int(ys.max())+9))
    save_rgb(rgb[box[1]:box[3], box[0]:box[2]], out/"region-crop.png")
    text = ("# Edit brief\n\n## May change\n\n"+brief.strip()+
            "\n\n## Must not change\n\nPixels outside the supplied mask; subject identity, pose, expression, "
            "composition, text, and all unrequested details. Use the crop as context; the original is authoritative.\n")
    (out/"edit-brief.md").write_text(text, encoding="utf-8")
    return {"original_copy": str(copied), "mask": str(out/"mask.png"),
            "crop": str(out/"region-crop.png"), "brief": str(out/"edit-brief.md"),
            "size": [rgb.shape[1], rgb.shape[0]], "mask_bbox_xyxy": list(box)}


def verify(original, edited, mask_path, out_dir, mean_limit=1.0, p99_limit=3.0, feather_radius=5):
    source, edit, out = Path(original).resolve(), Path(edited).resolve(), Path(out_dir).resolve()
    a, b = read_rgb(source), read_rgb(edit)
    original_size, edited_size = [a.shape[1], a.shape[0]], [b.shape[1], b.shape[0]]
    resized = a.shape[:2] != b.shape[:2]
    preview = resize_rgb(b, (a.shape[1], a.shape[0])) if resized else b
    if resized:
        b = resize_rgb(b, (a.shape[1], a.shape[0]), Image.Resampling.NEAREST)
    mask = read_mask(mask_path, a.shape)
    if mean_limit < 0 or p99_limit < 0 or feather_radius < 0:
        raise ValueError("limits and feather radius must be non-negative")
    feather = np.asarray(Image.fromarray(np.rint(mask*255).astype(np.uint8), "L").filter(
        ImageFilter.GaussianBlur(feather_radius)), dtype=float)/255
    protected = feather <= .05
    if not protected.any():
        raise ValueError("feathered mask leaves no protected pixels to verify")
    delta = delta_e_2000(rgb_to_lab(a), rgb_to_lab(b))
    stats = _describe(delta[protected])
    inside = _describe(delta[feather >= .95])
    over = protected & (delta > 3)
    changed_y, changed_x = np.where(over)
    bbox = ([int(changed_x.min()), int(changed_y.min()), int(changed_x.max())+1, int(changed_y.max())+1]
            if len(changed_x) else None)
    max_index = np.unravel_index(np.argmax(np.where(protected, delta, -np.inf)), delta.shape)
    max_xy = [int(max_index[1]), int(max_index[0])]
    thresholds_passed = stats["mean"] <= mean_limit and stats["p99"] <= p99_limit and stats["max"] <= 3.0
    passed = thresholds_passed and not resized
    metrics = {"delta_e_2000": {"all": _describe(delta.ravel()), "inside_mask": inside,
                                "outside_mask": stats},
               "alignment": {"original_size": original_size, "edited_size": edited_size,
                             "edited_resized_to_original": resized,
                             "verification_method": "nearest-neighbour" if resized else None,
                             "preview_method": "bicubic" if resized else None},
               "roundtrip": {"passed": passed, "statistics_passed": thresholds_passed,
                             "manual_review_required": resized,
                             "failure_reason": "resized_edit_requires_manual_review" if resized else None,
                             "protected_definition": "feathered mask coverage <= 0.05",
                             "feather_radius_px": feather_radius,
                             "limits": {"mean": mean_limit, "p99": p99_limit, "max": 3.0},
                             "protected_pixels": stats["count"], "mean_delta_e_2000": stats["mean"],
                             "p99_delta_e_2000": stats["p99"], "max_delta_e_2000": stats["max"],
                             "max_pixel_xy": max_xy, "max_limit": 3.0,
                             "bbox_delta_e_over_3_xyxy": bbox}}
    out.mkdir(parents=True, exist_ok=True)
    outputs = [out/name for name in ("side-by-side.png", "difference.png", "compare.html", "verify.json")]
    inputs = {source, edit, Path(mask_path).resolve()}
    if inputs & {p.resolve() for p in outputs} or any(p.exists() for p in outputs):
        raise FileExistsError("verification outputs must be new paths in an empty directory")
    note = f"Protected pixels: feathered mask coverage ≤ 0.05; Gaussian radius {feather_radius}px. "
    if resized:
        note += f"Edited image resized from {edited_size} to {original_size} with nearest-neighbour for verification and bicubic for display."
    else:
        note += "Image dimensions matched."
    write_compare_assets(a, preview, out, metrics, note)
    (out/"verify.json").write_text(json.dumps(metrics, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    return {"out": str(out), **metrics}
