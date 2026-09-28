"""Adjacent ratios between rendered type levels."""

from __future__ import annotations


def measure_scale(boxes: dict) -> tuple[object, object, str]:
    sizes = sorted({float(v) for v in boxes.get("font_sizes", []) if float(v) > 0}, reverse=True)
    if len(sizes) < 2:
        return {"font_sizes_px": sizes, "reason": "need at least two data-vd-type levels"}, "declared scale", "skipped"
    ratios = [sizes[i] / sizes[i + 1] for i in range(len(sizes) - 1)]
    threshold = float(boxes.get("type_scale") or 1.25)
    return {"font_sizes_px": sizes, "adjacent_ratios": ratios}, threshold, "pass" if min(ratios) >= threshold else "fail"
