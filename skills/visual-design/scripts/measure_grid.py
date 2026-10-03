"""Alignment of declared element edges to equal column grids."""

from __future__ import annotations


def measure_grid(boxes: dict) -> tuple[object, object, str]:
    grid = boxes.get("grid", [])
    if not grid or not boxes.get("columns"):
        return {"reason": "missing grid boxes or column declaration"}, "declared grid", "skipped"
    scale = float(boxes["scale"])
    width, height = boxes["css_frame"]
    cols, gutter, margin = int(boxes["columns"]), float(boxes["gutter"]), float(boxes["margin"])
    col_width = (width - 2 * margin - (cols - 1) * gutter) / cols
    starts = [margin + i * (col_width + gutter) for i in range(cols)]
    guides = starts + [x + col_width for x in starts]
    errors = []
    for box in grid:
        x, _, bw, _ = box
        errors.extend(min(abs(edge / scale - line) for line in guides) for edge in (x, x + bw))
    value = max(errors, default=0.0)
    threshold = max(1.0, 0.001 * min(width, height))
    return {"max_edge_deviation_css_px": value}, threshold, "pass" if value <= threshold else "fail"
