import numpy as np

from scripts.color_math import linear_to_srgb, srgb_to_linear
from scripts.grade_color import color_adjust, hsl_bands, white_balance
from scripts.grade_tone import levels, tone_curve, vignette
from scripts.lut import apply_cube


def apply_recipe(rgb, recipe, recipe_dir="."):
    operations = recipe.get("operations") if isinstance(recipe, dict) else recipe
    if not isinstance(operations, list):
        raise ValueError("recipe must be an array or an object with an operations array")
    out = np.asarray(rgb, dtype=np.float64).copy()
    for op in operations:
        if not isinstance(op, dict) or "type" not in op:
            raise ValueError("each operation must be an object with a type")
        kind = op["type"]
        if kind == "exposure":
            out = linear_to_srgb(srgb_to_linear(out)*2**float(op.get("stops", 0)))
        elif kind == "white_balance":
            out = white_balance(out, op)
        elif kind == "levels":
            out = levels(out, float(op.get("black", 0)), float(op.get("white", 1)),
                         float(op.get("gamma", 1)))
        elif kind == "tone_curve":
            out = tone_curve(out, op.get("points", []))
        elif kind == "saturation":
            out = color_adjust(out, saturation=float(op.get("factor", 1)))
        elif kind == "vibrance":
            amount = float(op.get("amount", 0))
            if not -1 <= amount <= 1:
                raise ValueError("vibrance amount must be -1..1")
            out = color_adjust(out, vibrance=amount)
        elif kind == "hsl":
            out = hsl_bands(out, op.get("bands", []))
        elif kind == "lut":
            out = apply_cube(out, f"{recipe_dir}/{op['file']}")
        elif kind == "vignette":
            out = vignette(out, float(op.get("strength", .25)), float(op.get("radius", .72)),
                           tuple(op.get("center", [.5, .5])))
        else:
            raise ValueError(f"unknown grading operation: {kind}")
    if not np.isfinite(out).all():
        raise ValueError("recipe produced non-finite pixel values")
    return np.clip(out, 0, 1)
