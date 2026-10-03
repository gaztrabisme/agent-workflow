import json
import struct
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.measure_storyboard import (  # noqa: E402
    check_captions,
    check_cutoffs,
    check_holds,
    check_proportions,
    compare_video_frames,
    resolve_value,
)


def write_png(path: Path, width: int, height: int, color: tuple[int, int, int]) -> None:
    """Write a small RGB PNG using only the standard library."""
    def chunk(kind: bytes, data: bytes) -> bytes:
        return (struct.pack(">I", len(data)) + kind + data
                + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF))

    row = b"\x00" + bytes(color) * width
    pixels = row * height
    data = (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(pixels))
            + chunk(b"IEND", b""))
    path.write_bytes(data)


class MeasureStoryboardTests(unittest.TestCase):
    def setUp(self):
        self.storyboard = {
            "scenes": [{
                "id": "scene-a", "startMs": 0, "durationMs": 5000,
                "layers": [{
                    "id": "panel-a", "type": "group", "durationMs": 4000,
                    "children": [
                        {"id": "bar", "type": "shape", "width": 50,
                         "startMs": 0, "durationMs": 4000,
                         "tracks": [{"property": "scaleX", "keyframes": [
                             {"atMs": 0, "value": 0}, {"atMs": 2500, "value": 1}
                         ]}]},
                        {"id": "cap-a", "type": "text", "text": "Read this",
                         "durationMs": 1000, "tracks": [{"property": "opacity",
                             "keyframes": [{"atMs": 0, "value": 1},
                                           {"atMs": 1000, "value": 0}]}]},
                    ],
                }],
            }]
        }
        self.evidence = {
            "facts": {"hours": 5, "cost": 25, "budget": 100},
            "motionChecks": {"proportions": [
                {"name": "bar width", "layer": "bar", "property": "width",
                 "fact": "facts.hours", "scale": 10, "tolerance": 0},
                {"name": "budget share", "layer": "bar", "property": "width",
                 "ratio": {"numerator": "facts.cost", "denominator": "facts.budget"},
                 "scale": 2, "against": {"layer": "track", "property": "width"},
                 "tolerance": 0.25},
            ]},
        }
        self.storyboard["scenes"][0]["layers"][0]["children"].append(
            {"id": "track", "type": "shape", "width": 100, "durationMs": 4000})

    def test_resolve_fact_with_array_index(self):
        self.assertEqual(resolve_value({"facts": {"points": [4, 9]}}, "facts.points[1]"), 9)

    def test_proportions_use_evidence_facts_and_layer_dimensions(self):
        result = check_proportions(self.storyboard, self.evidence)
        self.assertEqual([check["pass"] for check in result["checks"]], [True, True])

    def test_unconfigured_proportions_are_not_a_measured_pass(self):
        result = check_proportions(self.storyboard, {"facts": {}})
        self.assertEqual(result["status"], "not_configured")
        not_applicable = check_proportions(self.storyboard, {
            "facts": {}, "motionChecks": {
                "proportionsNotApplicable": "No numeric encoding in this animation."
            }
        })
        self.assertEqual(not_applicable["status"], "not_applicable")

    def test_caption_rate_and_panel_hold(self):
        captions = check_captions(self.storyboard, self.evidence)
        holds = check_holds(self.storyboard, self.evidence)
        self.assertTrue(captions["checks"][0]["pass"])
        self.assertEqual(holds["checks"][0]["hold_ms"], 1500)
        self.assertTrue(holds["checks"][0]["pass"])

    def test_cutoff_reports_track_past_layer_end(self):
        layer = self.storyboard["scenes"][0]["layers"][0]["children"][0]
        layer["tracks"][0]["keyframes"].append({"atMs": 4100, "value": 1})
        result = check_cutoffs(self.storyboard)
        self.assertEqual(result["fail_count"], 1)
        self.assertEqual(result["checks"][0]["kind"], "track_outlives_layer")

    def test_frame_comparison_passes_identical_and_fails_visible_difference(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            mp4 = base / "clip.mp4"
            mp4.touch()
            check_dir = base / "checks" / "at-1000"
            check_dir.mkdir(parents=True)
            reference = check_dir / "render.png"
            write_png(reference, 64, 64, (128, 128, 128))

            def same_frame(_mp4, _at_ms, output):
                output.write_bytes(reference.read_bytes())

            passed = compare_video_frames(mp4, base / "checks", extractor=same_frame)
            self.assertTrue(passed["frames"][0]["pass"])

            def changed_frame(_mp4, _at_ms, output):
                write_png(output, 64, 64, (0, 0, 0))

            failed = compare_video_frames(mp4, base / "checks", extractor=changed_frame)
            self.assertFalse(failed["frames"][0]["pass"])


if __name__ == "__main__":
    unittest.main()
