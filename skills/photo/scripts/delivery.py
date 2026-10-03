"""Create and verify reproducible sRGB delivery copies from a JSON spec."""

from __future__ import annotations

from io import BytesIO
import json
from pathlib import Path
import shutil
import tempfile

import numpy as np
from PIL import Image, ImageCms, ImageOps

from scripts.image_io import read_rgb, resize_rgb


_SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB"))
_SRGB_BYTES = _SRGB.tobytes()
_FORMATS = {"JPG": "JPEG", "JPEG": "JPEG", "PNG": "PNG", "WEBP": "WEBP",
            "TIF": "TIFF", "TIFF": "TIFF"}
_EXTENSIONS = {"JPEG": {".jpg", ".jpeg"}, "PNG": {".png"}, "WEBP": {".webp"},
               "TIFF": {".tif", ".tiff"}}


def _read_srgb(path: Path) -> np.ndarray:
    with Image.open(path) as image:
        profile_bytes = image.info.get("icc_profile")
        if not profile_bytes:
            # The photo grade pipeline emits untagged RGB values interpreted as sRGB.
            return read_rgb(path)
        oriented = ImageOps.exif_transpose(image).convert("RGB")
        try:
            source_profile = ImageCms.ImageCmsProfile(BytesIO(profile_bytes))
            converted = ImageCms.profileToProfile(oriented, source_profile, _SRGB,
                                                  outputMode="RGB")
        except Exception as exc:
            raise ValueError(f"could not convert embedded input profile to sRGB: {path}") from exc
        return np.asarray(converted, dtype=np.float64)/255


def _item_spec(item, spec_dir: Path, output_dir: Path):
    if not isinstance(item, dict) or "input" not in item or "file" not in item:
        raise ValueError("each delivery item needs input and file")
    filename = str(item["file"])
    if (not filename or Path(filename).name != filename or filename in {".", ".."}
            or filename.casefold() == "manifest.json"):
        raise ValueError("delivery file must be a plain filename inside --out")
    target = output_dir/filename
    fmt_value = str(item.get("format", Path(filename).suffix.lstrip("."))).upper()
    fmt = _FORMATS.get(fmt_value)
    if fmt is None:
        raise ValueError(f"unsupported delivery format: {fmt_value}")
    if Path(filename).suffix.lower() not in _EXTENSIONS[fmt]:
        raise ValueError(f"filename extension does not match {fmt}: {filename}")
    source = Path(item["input"])
    if not source.is_absolute():
        source = spec_dir/source
    source = source.resolve()
    if not source.is_file():
        raise FileNotFoundError(f"delivery input does not exist: {source}")
    crop = item.get("crop")
    if crop is not None:
        if not isinstance(crop, list) or len(crop) != 4:
            raise ValueError(f"{filename}: crop must be [x0,y0,x1,y1]")
        crop = list(map(int, crop))
    size = item.get("size")
    if size is not None:
        if not isinstance(size, list) or len(size) != 2:
            raise ValueError(f"{filename}: size must be [width,height]")
        size = list(map(int, size))
        if min(size) <= 0:
            raise ValueError(f"{filename}: output dimensions must be positive")
    quality = item.get("quality")
    if fmt in {"JPEG", "WEBP"}:
        quality = int(quality if quality is not None else (95 if fmt == "JPEG" else 90))
        if not 1 <= quality <= 100:
            raise ValueError(f"{filename}: lossy quality must be from 1 to 100")
    elif quality is not None:
        raise ValueError(f"{filename}: quality is only applicable to JPEG and WEBP")
    return {"source": source, "target": target, "filename": filename,
            "format": fmt, "quality": quality, "crop": crop, "size": size,
            "allow_upscale": bool(item.get("allow_upscale", False)),
            "note": str(item.get("note", ""))}


def _prepare(item):
    rgb = _read_srgb(item["source"])
    h, w = rgb.shape[:2]
    crop = item["crop"]
    if crop is None:
        crop = [0, 0, w, h]
    x0, y0, x1, y1 = crop
    if x0 < 0 or y0 < 0 or x1 > w or y1 > h or x1 <= x0 or y1 <= y0:
        raise ValueError(f"{item['filename']}: crop must be a non-empty in-bounds pixel rectangle")
    rgb = rgb[y0:y1, x0:x1]
    crop_h, crop_w = rgb.shape[:2]
    target_size = item["size"] or [crop_w, crop_h]
    target_w, target_h = target_size
    # Integer output sizes can differ slightly from the source ratio after the
    # final dimension is rounded; allow at most half an output pixel of error.
    rounding_error = min(abs(target_h-crop_h*target_w/crop_w),
                         abs(target_w-crop_w*target_h/crop_h))
    if rounding_error > .5+1e-9:
        raise ValueError(f"{item['filename']}: crop and output dimensions have different aspect ratios; choose an explicit crop")
    scale = max(target_w/crop_w, target_h/crop_h)
    upscaled = scale > 1+1e-9
    if upscaled and not item["allow_upscale"]:
        raise ValueError(f"{item['filename']}: upscaling {scale:.3f}x is disabled; reduce size or set allow_upscale true explicitly")
    if (target_w, target_h) != (crop_w, crop_h):
        rgb = resize_rgb(rgb, (target_w, target_h), Image.Resampling.LANCZOS)
    return rgb, list(target_size), crop, scale, upscaled


def _save(rgb: np.ndarray, path: Path, fmt: str, quality):
    image = Image.fromarray(np.rint(np.clip(rgb, 0, 1)*255).astype(np.uint8))
    options = {"format": fmt, "icc_profile": _SRGB_BYTES}
    if fmt == "JPEG":
        options.update(quality=quality, subsampling=0, optimize=True)
    elif fmt == "WEBP":
        options.update(quality=quality, method=6)
    else:
        options.update(optimize=True)
    image.save(path, **options)


def _check_files(paths, planned):
    actual_paths = ([path for path in paths[0].parent.iterdir() if path.is_file()]
                    if paths else [])
    results = []
    for path, item in zip(paths, planned):
        with Image.open(path) as image:
            profile_bytes = image.info.get("icc_profile", b"")
            profile_name = ""
            if profile_bytes:
                try:
                    profile_name = ImageCms.getProfileName(ImageCms.ImageCmsProfile(BytesIO(profile_bytes))).strip()
                except Exception:
                    profile_name = "<unreadable>"
            profile_ok = "srgb" in profile_name.casefold()
            dimensions_ok = list(image.size) == item["size"]
            format_ok = image.format == item["format"]
            results.append({"file": path.name, "dimensions": list(image.size),
                            "expected_dimensions": item["size"], "dimensions_ok": dimensions_ok,
                            "format": image.format, "expected_format": item["format"],
                            "format_ok": format_ok, "icc_profile": profile_name,
                            "icc_srgb_ok": profile_ok,
                            "passed": dimensions_ok and format_ok and profile_ok})
    count_ok = (len(actual_paths) == len(planned) and
                {p.name for p in actual_paths} == {item["filename"] for item in planned} and
                len(paths) == len(planned))
    return {"expected_file_count": len(planned), "actual_file_count": len(actual_paths),
            "file_count_ok": count_ok, "outputs": results,
            "passed": count_ok and all(result["passed"] for result in results)}


def deliver(spec_path, output_dir):
    spec_file = Path(spec_path).resolve()
    spec = json.loads(spec_file.read_text(encoding="utf-8"))
    items = spec.get("items") if isinstance(spec, dict) else None
    if not isinstance(items, list) or not items:
        raise ValueError("delivery spec must contain a non-empty items array")
    out = Path(output_dir).resolve()
    planned = [_item_spec(item, spec_file.parent, out) for item in items]
    names = [item["filename"] for item in planned]
    if len(set(names)) != len(names):
        raise ValueError("delivery spec has duplicate output filenames")
    manifest_target = out/"manifest.json"
    if manifest_target.exists() or any(item["target"].exists() for item in planned):
        raise FileExistsError("delivery output or manifest already exists; choose new filenames or an empty destination")
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="photo-delivery-", dir=out) as temp_name:
        staging = Path(temp_name)
        manifest_items = []
        stage_paths = []
        for item in planned:
            rgb, size, crop, scale, upscaled = _prepare(item)
            item["size"] = size
            staged = staging/item["filename"]
            _save(rgb, staged, item["format"], item["quality"])
            stage_paths.append(staged)
            manifest_items.append({"file": item["filename"], "input": str(item["source"]),
                                   "crop_xyxy": crop, "dimensions": size,
                                   "format": item["format"], "quality": item["quality"],
                                   "icc_profile": "sRGB IEC61966-2.1", "resampling": "Lanczos",
                                   "scale": scale, "upscaled": upscaled,
                                   "note": item["note"]})
        checks = _check_files(stage_paths, planned)
        if not checks["passed"]:
            raise ValueError("delivery code checks failed: " + json.dumps(checks, sort_keys=True))
        manifest = {"spec": str(spec_file), "output_directory": str(out),
                    "expected_file_count": len(planned), "actual_file_count": len(stage_paths),
                    "checks": checks, "outputs": manifest_items}
        staged_manifest = staging/"manifest.json"
        staged_manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True)+"\n", encoding="utf-8")
        moved = []
        try:
            for staged, item in zip(stage_paths, planned):
                final = item["target"]
                shutil.move(str(staged), str(final))
                moved.append(final)
            shutil.move(str(staged_manifest), str(manifest_target))
            moved.append(manifest_target)
        except Exception:
            for path in moved:
                path.unlink(missing_ok=True)
            raise
    return manifest
