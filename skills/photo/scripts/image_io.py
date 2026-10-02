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
        Image.fromarray(np.rint(rgb*255).astype(np.uint8)).save(path)


def resize_rgb(rgb, size, method=Image.Resampling.BICUBIC):
    w, h = size
    source = np.rint(np.clip(rgb, 0, 1)*65535).astype(np.uint16)
    channels = [np.asarray(Image.fromarray(source[..., i]).resize(
        (w, h), method), dtype=np.float64)/65535 for i in range(3)]
    return np.stack(channels, axis=-1)


def read_mask(path, shape):
    with Image.open(path) as im:
        mask = np.asarray(ImageOps.exif_transpose(im).convert("L"), dtype=np.float64)/255
    if mask.shape != tuple(shape[:2]):
        raise ValueError(f"mask size {mask.shape[::-1]} does not match image {shape[1]}x{shape[0]}")
    return mask


def compare_page(out, metrics, note="", a_name="Reference", b_name="Edited",
                 region_name="Centre crop", crop_box=None):
    out = Path(out)
    data = html.escape(json.dumps(metrics, indent=2, sort_keys=True))
    message = html.escape(note)
    left, right = html.escape(a_name), html.escape(b_name)
    roi = html.escape(region_name)
    title = html.escape(f"{a_name} ↔ {b_name} — Photo comparison")
    box = html.escape(str(crop_box))
    page = f'''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<style>html,body{{margin:0;min-height:100%;width:100%}}body{{background:#808080;color:#171717;font:16px/1.5 system-ui,sans-serif}}
main{{box-sizing:border-box;width:100%;min-height:100vh;margin:0;padding:24px}}.content{{width:100%;margin:0 auto}}h1{{font-size:1.4rem;overflow-wrap:anywhere}}.images{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
figure{{margin:0;min-width:0}}img{{display:block;width:100%;height:auto;background:#808080}}figcaption{{padding:8px 0;color:#171717;font-weight:600;overflow-wrap:anywhere}}
.crop-scroll{{max-width:100%;overflow-x:auto;overflow-y:hidden;background:#808080}}.crop-scroll img{{width:auto;max-width:none;height:auto}}details{{margin-top:20px;padding:12px 16px;background:#dedede}}summary{{cursor:pointer;font-weight:650}}pre{{white-space:pre-wrap;background:#f4f1e8;padding:16px;overflow:auto}}
@media(max-width:650px){{.images{{grid-template-columns:1fr}}}}</style>
<main data-rk-stage="comparison"><div class="content"><h1>{left} ↔ {right}</h1><p>{message}</p>
<div class="images"><figure><img src="side-by-side.png" alt="Full-frame side-by-side comparison of {left} and {right}"><figcaption>Reference file: {left} | Edited file: {right}</figcaption></figure>
<figure><img src="difference.png" alt="Amplified absolute RGB difference between {left} and {right}"><figcaption>Difference between {left} and {right}, amplified 4×</figcaption></figure></div>
<h2>100% close-up: {roi}</h2><p>Source-pixel crop, box x0,y0,x1,y1: {box}. Scroll horizontally to compare both crops at their original pixel size.</p>
<figure><div class="crop-scroll"><img src="close-up.png" alt="100 percent source-pixel crops: {left} on the left, {right} on the right"></div>
<figcaption>Reference crop: {left} | Edited crop: {right}</figcaption></figure>
<details><summary>Measurements (JSON)</summary><pre>{data}</pre></details></div></main></html>'''
    (out/"compare.html").write_text(page, encoding="utf-8")


def _comparison_crop(shape, mask=None, region=None, region_name=None):
    h, w = shape[:2]
    if region is not None:
        x0, y0, x1, y1 = map(int, region)
        if x0 < 0 or y0 < 0 or x1 > w or y1 > h or x1 <= x0 or y1 <= y0:
            raise ValueError("comparison region must be a non-empty in-bounds x0,y0,x1,y1 box")
        return (x0, y0, x1, y1), region_name or "named region"
    if mask is not None:
        ys, xs = np.where(mask >= .5)
        if len(xs):
            pad = 8
            box = (max(0, int(xs.min())-pad), max(0, int(ys.min())-pad),
                   min(w, int(xs.max())+pad+1), min(h, int(ys.max())+pad+1))
            return box, region_name or "edit-mask bounds"
    crop_w, crop_h = min(w, 512), min(h, 512)
    x0, y0 = max(0, (w-crop_w)//2), max(0, (h-crop_h)//2)
    return (x0, y0, x0+crop_w, y0+crop_h), region_name or "centre crop (512-pixel maximum)"


def write_compare_assets(a, b, out, metrics, note="", a_name="Reference", b_name="Edited",
                         mask=None, region=None, region_name=None):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    if a.shape != b.shape:
        raise ValueError("comparison images must be aligned before rendering")
    box, chosen_name = _comparison_crop(a.shape, mask, region, region_name)
    save_rgb(np.concatenate((a, b), axis=1), out/"side-by-side.png")
    save_rgb(np.abs(a-b)*4, out/"difference.png")
    x0, y0, x1, y1 = box
    save_rgb(np.concatenate((a[y0:y1, x0:x1], b[y0:y1, x0:x1]), axis=1), out/"close-up.png")
    compare_page(out, metrics, note, a_name, b_name, chosen_name, box)
