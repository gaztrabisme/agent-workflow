"""Negative-space ratio from the union of declared occupied boxes."""

from __future__ import annotations


def union_area(boxes: list[list[float]], width: float, height: float) -> float:
    clipped = [[max(0, x), max(0, y), min(width, x + w), min(height, y + h)]
               for x, y, w, h in boxes]
    clipped = [b for b in clipped if b[2] > b[0] and b[3] > b[1]]
    xs = sorted({v for b in clipped for v in (b[0], b[2])})
    area = 0.0
    for left, right in zip(xs, xs[1:]):
        spans = sorted((b[1], b[3]) for b in clipped if b[0] < right and b[2] > left)
        covered, start, end = 0.0, None, None
        for top, bottom in spans:
            if start is None:
                start, end = top, bottom
            elif top <= end:
                end = max(end, bottom)
            else:
                covered += end - start
                start, end = top, bottom
        if start is not None:
            covered += end - start
        area += (right - left) * covered
    return area


def measure_space(boxes: dict) -> tuple[object, object, str]:
    occupied = boxes.get("occupies", [])
    if not occupied:
        return {"reason": "no data-vd-occupies boxes"}, "declared target", "skipped"
    width, height = map(float, boxes["frame"])
    ratio = 1 - union_area(occupied, width, height) / (width * height)
    target = boxes.get("space_target")
    if target is None:
        return {"negative_space_ratio": ratio}, "vision review", "not_judged"
    threshold = {"target": float(target), "tolerance": 0.05}
    status = "pass" if abs(ratio - float(target)) <= 0.05 else "fail"
    return {"negative_space_ratio": ratio}, threshold, status
