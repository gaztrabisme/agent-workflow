import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

from scripts.color_math import delta_e_2000, rgb_to_lab
from scripts.grade_metrics import _describe, compare_metrics
from scripts.image_io import read_mask, read_rgb, resize_rgb, save_rgb, write_compare_assets


def _crop_box(mask, width, height, padding=8):
    ys, xs = np.where(mask > .5)
    if not len(xs):
        raise ValueError("edit mask is empty")
    return (max(0, int(xs.min())-padding), max(0, int(ys.min())-padding),
            min(width, int(xs.max())+padding+1), min(height, int(ys.max())+padding+1))


def prepare(original, mask_path, brief, out_dir):
    src, mask_file, out = Path(original).resolve(), Path(mask_path).resolve(), Path(out_dir).resolve()
    rgb = read_rgb(src)
    mask = read_mask(mask_file, rgb.shape)
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
    box = _crop_box(mask, rgb.shape[1], rgb.shape[0])
    save_rgb(rgb[box[1]:box[3], box[0]:box[2]], out/"region-crop.png")
    text = ("# Edit brief\n\n## May change\n\n"+brief.strip()+
            "\n\n## Must not change\n\nPixels outside the supplied mask; subject identity, pose, expression, "
            "composition, text, and all unrequested details. Use the crop as context; the original is authoritative.\n")
    (out/"edit-brief.md").write_text(text, encoding="utf-8")
    return {"original_copy": str(copied), "mask": str(out/"mask.png"),
            "crop": str(out/"region-crop.png"), "brief": str(out/"edit-brief.md"),
            "size": [rgb.shape[1], rgb.shape[0]], "mask_bbox_xyxy": list(box)}


def merge(original, edited_crop, mask_path, output):
    source, crop_path = Path(original).resolve(), Path(edited_crop).resolve()
    mask_file, target = Path(mask_path).resolve(), Path(output).resolve()
    if target in {source, crop_path, mask_file}:
        raise ValueError("merge output must differ from the original, edited crop, and mask")
    if target.exists():
        raise FileExistsError("merge output already exists")
    base = read_rgb(source)
    mask = read_mask(mask_file, base.shape)
    box = _crop_box(mask, base.shape[1], base.shape[0])
    patch = read_rgb(crop_path)
    expected = (box[3]-box[1], box[2]-box[0])
    if patch.shape[:2] != expected:
        raise ValueError(f"edited crop is {patch.shape[1]}x{patch.shape[0]}, expected {expected[1]}x{expected[0]} from the mask and 8-pixel crop padding")
    merged = base.copy()
    alpha = mask[box[1]:box[3], box[0]:box[2], None]
    merged[box[1]:box[3], box[0]:box[2]] = (
        patch*alpha + base[box[1]:box[3], box[0]:box[2]]*(1-alpha))
    save_rgb(merged, target)
    return {"output": str(target), "original": str(source), "edited_crop": str(crop_path),
            "mask": str(mask_file), "mask_bbox_xyxy": list(box), "composite": "mask alpha"}


def verify(original, edited, mask_path, out_dir, mean_limit=1.0, p99_limit=3.0,
           feather_radius=5, band_mean_limit=1.0, band_p99_limit=2.0,
           band_max_limit=3.0):
    source, edit, out = Path(original).resolve(), Path(edited).resolve(), Path(out_dir).resolve()
    a, b = read_rgb(source), read_rgb(edit)
    original_size, edited_size = [a.shape[1], a.shape[0]], [b.shape[1], b.shape[0]]
    resized = a.shape[:2] != b.shape[:2]
    preview = resize_rgb(b, (a.shape[1], a.shape[0])) if resized else b
    if resized:
        b = resize_rgb(b, (a.shape[1], a.shape[0]), Image.Resampling.NEAREST)
    mask = read_mask(mask_path, a.shape)
    if min(mean_limit, p99_limit, feather_radius, band_mean_limit,
           band_p99_limit, band_max_limit) < 0:
        raise ValueError("limits and feather radius must be non-negative")
    feather = np.asarray(Image.fromarray(np.rint(mask*255).astype(np.uint8), "L").filter(
        ImageFilter.GaussianBlur(feather_radius)), dtype=float)/255
    protected = feather <= .05
    if not protected.any():
        raise ValueError("feathered mask leaves no protected pixels to verify")
    hard_mask = mask >= .5
    transition = (~hard_mask) & (~protected)
    delta = delta_e_2000(rgb_to_lab(a), rgb_to_lab(b))
    stats = _describe(delta[protected])
    mask_core = _describe(delta[feather >= .95])
    band_stats = _describe(delta[transition])
    over = protected & (delta > 3)
    changed_y, changed_x = np.where(over)
    bbox = ([int(changed_x.min()), int(changed_y.min()), int(changed_x.max())+1, int(changed_y.max())+1]
            if len(changed_x) else None)
    band_over = transition & (delta > band_max_limit)
    band_y, band_x = np.where(band_over)
    band_bbox = ([int(band_x.min()), int(band_y.min()), int(band_x.max())+1, int(band_y.max())+1]
                 if len(band_x) else None)
    max_index = np.unravel_index(np.argmax(np.where(protected, delta, -np.inf)), delta.shape)
    band_max_index = (np.unravel_index(np.argmax(np.where(transition, delta, -np.inf)), delta.shape)
                      if transition.any() else None)
    max_xy = [int(max_index[1]), int(max_index[0])]
    band_max_xy = ([int(band_max_index[1]), int(band_max_index[0])]
                   if band_max_index is not None else None)
    protected_passed = stats["mean"] <= mean_limit and stats["p99"] <= p99_limit and stats["max"] <= 3.0
    band_passed = (band_stats["mean"] is None or
                   (band_stats["mean"] <= band_mean_limit and
                    band_stats["p99"] <= band_p99_limit and
                    band_stats["max"] <= band_max_limit))
    thresholds_passed = protected_passed and band_passed
    passed = thresholds_passed and not resized
    metrics = {"delta_e_2000": {"all": _describe(delta.ravel()), "mask_core": mask_core,
                                "transition_band": band_stats, "outside_mask": stats},
               "alignment": {"original_size": original_size, "edited_size": edited_size,
                             "edited_resized_to_original": resized,
                             "verification_method": "nearest-neighbour" if resized else None,
                             "preview_method": "bicubic" if resized else None},
               "roundtrip": {"passed": passed, "statistics_passed": thresholds_passed,
                             "manual_review_required": resized,
                             "failure_reason": "resized_edit_requires_manual_review" if resized else None,
                             "protected_definition": "feathered mask coverage <= 0.05",
                             "transition_band_definition": "outside hard mask (coverage < 0.5) and feathered coverage > 0.05",
                             "feather_radius_px": feather_radius,
                             "limits": {"protected": {"mean": mean_limit, "p99": p99_limit, "max": 3.0},
                                        "transition_band": {"mean": band_mean_limit,
                                                            "p99": band_p99_limit,
                                                            "max": band_max_limit}},
                             "protected_pixels": stats["count"], "mean_delta_e_2000": stats["mean"],
                             "p99_delta_e_2000": stats["p99"], "max_delta_e_2000": stats["max"],
                             "max_pixel_xy": max_xy, "max_limit": 3.0,
                             "bbox_delta_e_over_3_xyxy": bbox,
                             "transition_band_passed": band_passed,
                             "transition_band_pixels": band_stats["count"],
                             "transition_band_mean_delta_e_2000": band_stats["mean"],
                             "transition_band_p99_delta_e_2000": band_stats["p99"],
                             "transition_band_max_delta_e_2000": band_stats["max"],
                             "transition_band_max_pixel_xy": band_max_xy,
                             "transition_band_bbox_over_limit_xyxy": band_bbox,
                             "unchecked_outside_mask_width_px": 0}}
    out.mkdir(parents=True, exist_ok=True)
    outputs = [out/name for name in ("side-by-side.png", "difference.png", "close-up.png", "compare.html", "verify.json")]
    inputs = {source, edit, Path(mask_path).resolve()}
    if inputs & {p.resolve() for p in outputs} or any(p.exists() for p in outputs):
        raise FileExistsError("verification outputs must be new paths in an empty directory")
    note = f"Protected pixels: feathered mask coverage ≤ 0.05; Gaussian radius {feather_radius}px. "
    if resized:
        note += f"Edited image resized from {edited_size} to {original_size} with nearest-neighbour for verification and bicubic for display."
    else:
        note += "Image dimensions matched."
    write_compare_assets(a, preview, out, metrics, note, source.name, edit.name, mask=mask)
    (out/"verify.json").write_text(json.dumps(metrics, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    return {"out": str(out), **metrics}
