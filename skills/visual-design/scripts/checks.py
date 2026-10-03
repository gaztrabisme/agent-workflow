#!/usr/bin/env python3
"""Measure composition from a render-kit PNG and optional boxes JSON.

Usage: checks.py {grid,balance,space,scale,focal} render.png [--boxes boxes.json]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

from measure_balance import measure_balance
from measure_focal import measure_focal
from measure_grid import measure_grid
from measure_scale import measure_scale
from measure_space import measure_space


def read_pixels(path: Path) -> np.ndarray:
    image = Image.open(path).convert("RGBA")
    background = Image.new("RGBA", image.size, "white")
    return np.asarray(Image.alpha_composite(background, image).convert("RGB"), dtype=float) / 255


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("test", choices=("grid", "balance", "space", "scale", "focal"))
    parser.add_argument("image", type=Path)
    parser.add_argument("--boxes", type=Path, help="JSON written by scripts/measure_boxes.mjs")
    args = parser.parse_args()
    boxes = json.loads(args.boxes.read_text()) if args.boxes else {}
    pixels = read_pixels(args.image)
    if boxes.get("frame") and tuple(boxes["frame"]) != (pixels.shape[1], pixels.shape[0]):
        parser.error("boxes PNG dimensions do not match the input image; rerun measure_boxes.mjs with matching render options")
    handlers = {"grid": lambda: measure_grid(boxes), "balance": lambda: measure_balance(pixels, boxes.get("balance_intent")),
                "space": lambda: measure_space(boxes), "scale": lambda: measure_scale(boxes),
                "focal": lambda: measure_focal(pixels, boxes.get("focal"))}
    if args.test != "balance" and not args.boxes:
        parser.error(f"{args.test} requires --boxes from measure_boxes.mjs")
    value, threshold, status = handlers[args.test]()
    source = "skill default"
    if args.test == "space" and boxes.get("space_target") is not None:
        source = "data-vd-space-target + skill default tolerance"
    if args.test == "scale":
        source = boxes.get("type_scale_source", "skill default")
    print(json.dumps({"test": args.test, "value": value, "threshold": threshold,
                      "status": status, "source": source}, allow_nan=False))
    return 1 if status == "fail" else 0


if __name__ == "__main__":
    sys.exit(main())
