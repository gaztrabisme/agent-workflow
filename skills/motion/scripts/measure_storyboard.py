#!/usr/bin/env python3
"""Measure a scene-engine storyboard against evidence and its rendered MP4.

Frame references are PNGs written by ``scene-engine check`` under
``checks/frames/at-<milliseconds>/render.png``. Optional proportion bindings live
in the evidence JSON; see references/method/measurement.md.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable, Iterator


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object in {path}")
    return value


def resolve_value(root: Any, reference: str) -> Any:
    """Resolve dotted paths such as facts.npt[0].hours in a JSON value."""
    tokens = re.findall(r"([^.\[\]]+)|\[(\d+)\]", reference)
    if not tokens:
        raise ValueError(f"invalid JSON value reference: {reference!r}")
    current = root
    for token in tokens:
        key = token[0] or token[1]
        if isinstance(current, list):
            current = current[int(key)]
        elif isinstance(current, dict):
            current = current[key]
        else:
            raise KeyError(reference)
    return current


def walk_layers(layers: list[dict[str, Any]], parent_start: int = 0
                ) -> Iterator[tuple[dict[str, Any], int]]:
    for layer in layers:
        absolute_start = parent_start + int(layer.get("startMs", 0))
        yield layer, absolute_start
        children = layer.get("children", [])
        if isinstance(children, list):
            yield from walk_layers(children, absolute_start)


def layer_index(storyboard: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], list[str]]:
    indexed: dict[str, dict[str, Any]] = {}
    duplicates: list[str] = []
    for scene in storyboard.get("scenes", []):
        for layer, _ in walk_layers(scene.get("layers", [])):
            layer_id = layer.get("id")
            if not layer_id:
                continue
            if layer_id in indexed:
                duplicates.append(str(layer_id))
            indexed[str(layer_id)] = layer
    return indexed, duplicates


def check_proportions(storyboard: dict[str, Any], evidence: dict[str, Any]
                     ) -> dict[str, Any]:
    config = evidence.get("motionChecks", evidence.get("motion_checks", {}))
    checks = config.get("proportions", []) if isinstance(config, dict) else []
    if not checks:
        reason = config.get("proportionsNotApplicable") if isinstance(config, dict) else None
        if reason:
            return {"status": "not_applicable", "reason": str(reason), "checks": []}
        return {"status": "not_configured", "checks": []}

    indexed, duplicates = layer_index(storyboard)
    results: list[dict[str, Any]] = []
    for spec in checks:
        name = spec.get("name", spec.get("layer", "proportion"))
        try:
            layer = indexed[spec["layer"]]
            actual = float(layer[spec["property"]])
            tolerance = float(spec.get("tolerance", 0.0))
            if "ratio" in spec:
                ratio = spec["ratio"]
                numerator = float(resolve_value(evidence, ratio["numerator"]))
                denominator = float(resolve_value(evidence, ratio["denominator"]))
                reference = spec["against"]
                denominator_layer = indexed[reference["layer"]]
                reference_size = float(denominator_layer[reference["property"]])
                if denominator == 0 or reference_size == 0:
                    raise ZeroDivisionError("proportion denominator is zero")
                expected = (numerator / denominator) * float(spec.get("scale", 1.0))
                actual = actual / reference_size
            else:
                fact = spec.get("fact", spec.get("expected_fact"))
                if not fact:
                    raise ValueError("proportion needs 'fact' or 'ratio'")
                expected = float(resolve_value(evidence, fact)) * float(spec.get("scale", 1.0))
                expected += float(spec.get("offset", 0.0))
            error = abs(actual - expected)
            results.append({"name": name, "expected": expected, "actual": actual,
                            "absolute_error": error, "tolerance": tolerance,
                            "pass": error <= tolerance})
        except (KeyError, TypeError, ValueError, ZeroDivisionError, IndexError) as exc:
            results.append({"name": name, "pass": False, "error": str(exc)})
    return {"status": "configured", "duplicate_layer_ids": sorted(set(duplicates)),
            "checks": results}


def _caption_window(layer: dict[str, Any], absolute_start: int) -> tuple[int, int]:
    opacity = next((track for track in layer.get("tracks", [])
                    if track.get("property") == "opacity"), None)
    duration = int(layer.get("durationMs", 0))
    if not opacity:
        return absolute_start, absolute_start + duration
    frames = opacity.get("keyframes", [])
    active = [i for i, frame in enumerate(frames) if float(frame.get("value", 0)) > 0]
    if not active:
        return absolute_start, absolute_start
    first = active[0]
    last = active[-1]
    start = int(frames[first]["atMs"])
    end = int(frames[last]["atMs"])
    for frame in frames[last + 1:]:
        if float(frame.get("value", 0)) <= 0:
            end = int(frame["atMs"])
            break
    if end <= start and duration > start:
        end = duration
    return absolute_start + start, absolute_start + end


def collect_captions(storyboard: dict[str, Any]) -> list[dict[str, Any]]:
    captions: list[dict[str, Any]] = []
    for scene in storyboard.get("scenes", []):
        scene_start = int(scene.get("startMs", 0))
        for cue in scene.get("captions", []):
            start = scene_start + int(cue["startMs"])
            end = scene_start + int(cue["endMs"])
            captions.append({"text": str(cue.get("text", "")), "startMs": start,
                             "endMs": end})
        for layer, absolute_start in walk_layers(scene.get("layers", []), scene_start):
            layer_id = str(layer.get("id", "")).casefold()
            is_caption = (layer.get("role") == "caption" or bool(layer.get("caption"))
                         or layer_id.startswith("cap-"))
            if is_caption and layer.get("text"):
                start, end = _caption_window(layer, absolute_start)
                captions.append({"text": str(layer["text"]), "startMs": start,
                                 "endMs": end})
    unique: dict[tuple[int, int, str], dict[str, Any]] = {}
    for cue in captions:
        unique[(cue["startMs"], cue["endMs"], cue["text"])] = cue
    return list(unique.values())


def check_captions(storyboard: dict[str, Any], evidence: dict[str, Any],
                   cps_limit: float | None = None) -> dict[str, Any]:
    config = evidence.get("motionChecks", evidence.get("motion_checks", {}))
    if cps_limit is None:
        cps_limit = float(config.get("captionCpsLimit", 20)) if isinstance(config, dict) else 20.0
    cues = collect_captions(storyboard)
    if not cues:
        return {"status": "not_configured", "limit_chars_per_second": cps_limit,
                "checks": []}
    results = []
    for cue in cues:
        duration = cue["endMs"] - cue["startMs"]
        char_count = len(cue["text"].replace("\n", " "))
        cps = char_count / (duration / 1000) if duration > 0 else math.inf
        results.append({"text": cue["text"].replace("\n", " "),
                        "startMs": cue["startMs"], "endMs": cue["endMs"],
                        "chars_per_second": cps, "pass": duration > 0 and cps <= cps_limit})
    return {"status": "measured", "limit_chars_per_second": cps_limit, "checks": results}


def check_holds(storyboard: dict[str, Any], evidence: dict[str, Any],
                minimum_hold_ms: int | None = None) -> dict[str, Any]:
    config = evidence.get("motionChecks", evidence.get("motion_checks", {}))
    if minimum_hold_ms is None:
        minimum_hold_ms = int(config.get("minimumHoldMs", 1500)) if isinstance(config, dict) else 1500
    results: list[dict[str, Any]] = []
    for scene in storyboard.get("scenes", []):
        for group in scene.get("layers", []):
            if group.get("type") != "group" or not group.get("children"):
                continue
            last_motion = 0
            for child in group.get("children", []):
                if str(child.get("id", "")).casefold().startswith("cap-"):
                    continue
                child_start = int(child.get("startMs", 0))
                for track in child.get("tracks", []):
                    times = [int(frame["atMs"]) for frame in track.get("keyframes", [])]
                    if times:
                        last_motion = max(last_motion, child_start + max(times))
            duration = int(group.get("durationMs", 0))
            hold = duration - last_motion
            results.append({"scene": scene.get("id"), "panel": group.get("id"),
                            "last_motion_end_ms": last_motion, "hold_ms": hold,
                            "minimum_hold_ms": minimum_hold_ms,
                            "pass": hold >= minimum_hold_ms})
    status = "measured" if results else "not_configured"
    return {"status": status, "checks": results}


def check_cutoffs(storyboard: dict[str, Any]) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for scene in storyboard.get("scenes", []):
        scene_duration = int(scene.get("durationMs", 0))
        for layer, absolute_start in walk_layers(scene.get("layers", [])):
            layer_id = layer.get("id", "(unnamed)")
            layer_duration = layer.get("durationMs")
            if layer_duration is not None and absolute_start + int(layer_duration) > scene_duration:
                results.append({"scene": scene.get("id"), "layer": layer_id,
                                "kind": "layer_outlives_scene",
                                "endMs": absolute_start + int(layer_duration),
                                "sceneDurationMs": scene_duration, "pass": False})
            if layer_duration is None:
                continue
            for track in layer.get("tracks", []):
                times = [int(frame["atMs"]) for frame in track.get("keyframes", [])]
                if times and max(times) > int(layer_duration):
                    results.append({"scene": scene.get("id"), "layer": layer_id,
                                    "track": track.get("property"), "kind": "track_outlives_layer",
                                    "endMs": max(times), "layerDurationMs": int(layer_duration),
                                    "pass": False})
    return {"status": "measured", "checks": results,
            "fail_count": sum(item["pass"] is False for item in results)}


def discover_check_frames(check_dir: Path) -> dict[int, Path]:
    frames: dict[int, Path] = {}
    for path in sorted(check_dir.rglob("*.png")):
        matches = re.findall(r"(?:at-|mp4-)(\d+)", path.as_posix())
        if matches:
            frames[int(matches[-1])] = path
    return frames


def extract_mp4_frame(mp4: Path, at_ms: int, output: Path) -> None:
    command = ["ffmpeg", "-v", "error", "-ss", f"{at_ms / 1000:.3f}",
               "-i", str(mp4), "-frames:v", "1", "-y", str(output)]
    subprocess.run(command, check=True, capture_output=True, text=True)


def media_dimensions(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height", "-of", "csv=s=x:p=0", str(path)],
        check=True, capture_output=True, text=True)
    width, height = result.stdout.strip().split("x", 1)
    return int(width), int(height)


def compare_images(actual_path: Path, reference_path: Path) -> dict[str, Any]:
    if media_dimensions(actual_path) != media_dimensions(reference_path):
        raise ValueError("MP4 frame and scene-engine check render have different dimensions")
    result = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", str(actual_path), "-i", str(reference_path),
         "-filter_complex", "[0:v]scale=480:270:flags=area[a];"
                           "[1:v]scale=480:270:flags=area[b];"
                           "[a][b]blend=all_mode=difference,signalstats,metadata=print",
         "-frames:v", "1", "-f", "null", "-"],
        check=True, capture_output=True, text=True)
    output = result.stdout + result.stderr
    metrics = {name: float(value) for name, value in re.findall(
        r"lavfi\.signalstats\.(YAVG|UAVG|VAVG|YMAX|UMAX|VMAX)=([0-9.]+)", output)}
    needed = {"YAVG", "UAVG", "VAVG", "YMAX", "UMAX", "VMAX"}
    if not needed.issubset(metrics):
        raise ValueError("FFmpeg did not return all signalstats difference values")
    mean = (metrics["YAVG"] + metrics["UAVG"] + metrics["VAVG"]) / 3
    maximum = max(metrics["YMAX"], metrics["UMAX"], metrics["VMAX"])
    return {"mean_abs_diff_yuv_480x270": mean,
            "max_component_abs_diff_yuv_480x270": maximum,
            "signalstats_480x270": metrics}


def compare_video_frames(mp4: Path, check_dir: Path, max_mean_diff: float = 3.0,
                         max_pixel_diff: float = 64.0,
                         extractor: Callable[[Path, int, Path], None] = extract_mp4_frame
                         ) -> dict[str, Any]:
    references = discover_check_frames(check_dir) if check_dir.is_dir() else {}
    results: list[dict[str, Any]] = []
    if references:
        with tempfile.TemporaryDirectory(prefix="motion-frames-") as temporary:
            temporary_path = Path(temporary)
            for at_ms, reference in sorted(references.items()):
                actual = temporary_path / f"frame-{at_ms}.png"
                try:
                    extractor(mp4, at_ms, actual)
                    metrics = compare_images(actual, reference)
                    passed = (metrics["mean_abs_diff_yuv_480x270"] <= max_mean_diff
                              and metrics["max_component_abs_diff_yuv_480x270"] <= max_pixel_diff)
                    results.append({"atMs": at_ms, **metrics, "pass": passed})
                except (OSError, subprocess.SubprocessError, ValueError) as exc:
                    results.append({"atMs": at_ms, "pass": False, "error": str(exc)})
    return {"status": "measured" if results else "missing_check_frames",
            "sample_size": "480x270", "max_mean_abs_diff_yuv": max_mean_diff,
            "max_component_abs_diff_yuv": max_pixel_diff,
            "frames": results}


def measure(storyboard: dict[str, Any], evidence: dict[str, Any], mp4: Path,
            check_dir: Path, max_mean_diff: float = 3.0,
            max_pixel_diff: float = 64.0, cps_limit: float | None = None,
            minimum_hold_ms: int | None = None,
            extractor: Callable[[Path, int, Path], None] = extract_mp4_frame) -> dict[str, Any]:
    result = {
        "proportions": check_proportions(storyboard, evidence),
        "captions": check_captions(storyboard, evidence, cps_limit),
        "holds": check_holds(storyboard, evidence, minimum_hold_ms),
        "cutoffs": check_cutoffs(storyboard),
        "frames": compare_video_frames(mp4, check_dir, max_mean_diff, max_pixel_diff, extractor),
    }
    failures: list[str] = []
    for name in ("proportions", "captions", "holds", "cutoffs"):
        section = result[name]
        if name == "proportions" and section.get("status") == "not_configured":
            failures.append("proportions.not_configured")
        for index, check in enumerate(section.get("checks", [])):
            if check.get("pass") is False:
                failures.append(f"{name}[{index}]")
        if name == "proportions" and section.get("duplicate_layer_ids"):
            failures.append("proportions.duplicate_layer_ids")
    if not result["frames"]["frames"]:
        failures.append("frames.missing_check_frames")
    else:
        for index, check in enumerate(result["frames"]["frames"]):
            if check.get("pass") is False:
                failures.append(f"frames[{index}]")
    result["pass"] = not failures
    result["failures"] = failures
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("storyboard", type=Path)
    parser.add_argument("evidence_json", type=Path)
    parser.add_argument("mp4", type=Path)
    parser.add_argument("--check-dir", type=Path,
                        help="scene-engine check PNGs (default: STORYBOARD/../checks/frames)")
    parser.add_argument("--max-frame-diff", type=float, default=3.0,
                        help="maximum mean YUV difference after 480x270 downsampling (default: 3)")
    parser.add_argument("--max-pixel-diff", type=float, default=64.0,
                        help="maximum YUV component difference in the 480x270 sample (default: 64)")
    parser.add_argument("--caption-cps-limit", type=float)
    parser.add_argument("--minimum-hold-ms", type=int)
    parser.add_argument("--output", type=Path, help="write full JSON report to this path")
    args = parser.parse_args(argv)
    check_dir = args.check_dir or args.storyboard.parent / "checks" / "frames"
    try:
        result = measure(read_json(args.storyboard), read_json(args.evidence_json), args.mp4,
                         check_dir, args.max_frame_diff, args.max_pixel_diff,
                         args.caption_cps_limit, args.minimum_hold_ms)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
