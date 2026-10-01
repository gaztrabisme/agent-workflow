import html
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

from scripts.png16 import read_rgb16, write_rgb16


def read_rgb(path):
    with Image.open(path) as source:
        orientation = source.getexif().get(274, 1)
        high = read_rgb16(path)
        if high is not None:
            return _orient(high, orientation).astype(np.float64)/65535
        image = ImageOps.exif_transpose(source)
        if image.mode not in ("RGB", "RGBA", "L", "LA", "I;16", "I;16B", "I;16L", "I", "F"):
            image = image.convert("RGB")
        arr = np.asarray(image)
        if arr.ndim == 2:
            arr = np.repeat(arr[..., None], 3, axis=-1)
        elif arr.shape[-1] == 2:
            arr = np.repeat(arr[..., :1], 3, axis=-1)
        elif arr.shape[-1] >= 3:
            arr = arr[..., :3]
        if arr.dtype == np.uint16 or (arr.dtype.kind in "iu" and arr.max(initial=0) > 255):
            return arr.astype(np.float64)/65535
        if arr.dtype.kind == "f":
            return np.clip(arr.astype(np.float64), 0, 1)
        return arr.astype(np.float64)/255


def _orient(arr, orientation):
    if orientation == 2: return arr[:, ::-1]
    if orientation == 3: return arr[::-1, ::-1]
    if orientation == 4: return arr[::-1]
    if orientation == 5: return arr.transpose(1, 0, 2)
    if orientation == 6: return np.rot90(arr, 3)
    if orientation == 7: return arr.transpose(1, 0, 2)[::-1, ::-1]
    if orientation == 8: return np.rot90(arr, 1)
    return arr


def save_rgb(rgb, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rgb = np.clip(np.asarray(rgb, float), 0, 1)
    if path.suffix.lower() == ".png":
        write_rgb16(path, rgb)
    else:
        Image.fromarray(np.rint(rgb*255).astype(np.uint8), "RGB").save(path)


def resize_rgb(rgb, size, method=Image.Resampling.BICUBIC):
    w, h = size
    source = np.rint(np.clip(rgb, 0, 1)*65535).astype(np.uint16)
    channels = [np.asarray(Image.fromarray(source[..., i], "I;16").resize(
        (w, h), method), dtype=np.float64)/65535 for i in range(3)]
    return np.stack(channels, axis=-1)


def read_mask(path, shape):
    with Image.open(path) as im:
        mask = np.asarray(ImageOps.exif_transpose(im).convert("L"), dtype=np.float64)/255
    if mask.shape != tuple(shape[:2]):
        raise ValueError(f"mask size {mask.shape[::-1]} does not match image {shape[1]}x{shape[0]}")
    return mask


def compare_page(out, metrics, note=""):
    out = Path(out)
    data = html.escape(json.dumps(metrics, indent=2, sort_keys=True))
    message = html.escape(note)
    page = f'''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Photo comparison</title>
<style>html,body{{margin:0;min-height:100%}}body{{background:#171817;color:#f4f1e8;font:16px/1.5 system-ui,sans-serif}}
main{{box-sizing:border-box;width:100%;min-height:100vh;margin:0;padding:24px}}.content{{max-width:1100px;margin:0 auto}}h1{{font-size:1.4rem}}.images{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
figure{{margin:0}}img{{display:block;width:100%;height:auto;background:#292b29}}figcaption{{padding:8px 0;color:#c8c7bf}}
pre{{white-space:pre-wrap;background:#242624;padding:16px;border-radius:8px;overflow:auto}}
@media(max-width:650px){{.images{{grid-template-columns:1fr}}}}</style>
<main data-rk-stage="comparison"><div class="content"><h1>Photo edit comparison</h1><p>{message}</p>
<div class="images"><figure><img src="side-by-side.png" alt="Original and edited image side by side"><figcaption>Original | Edited</figcaption></figure>
<figure><img src="difference.png" alt="Amplified absolute RGB difference"><figcaption>Difference amplified 4×</figcaption></figure></div>
<h2>Measurements</h2><pre>{data}</pre></div></main></html>'''
    (out/"compare.html").write_text(page, encoding="utf-8")


def write_compare_assets(a, b, out, metrics, note=""):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    if a.shape != b.shape:
        raise ValueError("comparison images must be aligned before rendering")
    save_rgb(np.concatenate((a, b), axis=1), out/"side-by-side.png")
    save_rgb(np.abs(a-b)*4, out/"difference.png")
    compare_page(out, metrics, note)
