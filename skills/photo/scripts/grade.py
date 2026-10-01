#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.grade_metrics import compare_metrics, measure
from scripts.grade_ops import apply_recipe
from scripts.image_io import read_mask, read_rgb, resize_rgb, write_compare_assets


def _json(value):
    print(json.dumps(value, sort_keys=True, separators=(",", ":")))


def _apply(args):
    source, recipe_path, target = map(lambda x: Path(x).resolve(), (args.input, args.recipe, args.output))
    recipe_side = Path(str(target)+".recipe.json")
    hash_side = Path(str(target)+".input.sha256")
    targets = (target, recipe_side, hash_side)
    if source in targets:
        raise ValueError("output and provenance paths must differ from the input")
    if any(p.exists() for p in targets):
        raise FileExistsError("refusing to overwrite an existing output or provenance file")
    recipe = json.loads(recipe_path.read_text(encoding="utf-8"))
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    result = apply_recipe(read_rgb(source), recipe, recipe_path.parent)
    target.parent.mkdir(parents=True, exist_ok=True)
    from scripts.image_io import save_rgb
    save_rgb(result, target)
    recipe_side.write_text(json.dumps(recipe, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    hash_side.write_text(digest+"  "+source.name+"\n", encoding="utf-8")
    _json({"output": str(target), "recipe": str(recipe_side), "input_sha256": digest,
           "size": [int(result.shape[1]), int(result.shape[0])]})


def _measure(args):
    rgb = read_rgb(args.image)
    mask = read_mask(args.mask, rgb.shape) if args.mask else None
    _json({"image": str(Path(args.image).resolve()), "size": [rgb.shape[1], rgb.shape[0]],
           **measure(rgb, mask)})


def _compare(args):
    a, b = read_rgb(args.a), read_rgb(args.b)
    before, after = [a.shape[1], a.shape[0]], [b.shape[1], b.shape[0]]
    resized = a.shape[:2] != b.shape[:2]
    if resized:
        b = resize_rgb(b, (a.shape[1], a.shape[0]))
    mask = read_mask(args.mask, a.shape) if args.mask else None
    metrics = compare_metrics(a, b, mask)
    metrics["alignment"] = {"reference_size": before, "edited_size": after,
                            "edited_resized_to_reference": resized}
    out = Path(args.out).resolve()
    sources = {Path(args.a).resolve(), Path(args.b).resolve()}
    if args.mask: sources.add(Path(args.mask).resolve())
    generated = {out/name for name in ("side-by-side.png", "difference.png", "compare.html")}
    if sources & {p.resolve() for p in generated}:
        raise ValueError("comparison outputs must not overwrite an input or mask")
    if any(p.exists() for p in generated):
        raise FileExistsError("comparison output already exists; choose an empty directory")
    note = "Edited image resized to reference dimensions with bicubic interpolation." if resized else "Images already share dimensions."
    write_compare_assets(a, b, out, metrics, note)
    _json({"out": str(out), **metrics})


def main():
    parser = argparse.ArgumentParser(description="Deterministic photo grading and comparison")
    sub = parser.add_subparsers(dest="command", required=True)
    apply = sub.add_parser("apply"); apply.add_argument("input"); apply.add_argument("recipe"); apply.add_argument("output"); apply.set_defaults(run=_apply)
    meas = sub.add_parser("measure"); meas.add_argument("image"); meas.add_argument("--mask"); meas.set_defaults(run=_measure)
    comp = sub.add_parser("compare"); comp.add_argument("a"); comp.add_argument("b"); comp.add_argument("--mask"); comp.add_argument("--out", required=True); comp.set_defaults(run=_compare)
    args = parser.parse_args()
    try:
        args.run(args)
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
