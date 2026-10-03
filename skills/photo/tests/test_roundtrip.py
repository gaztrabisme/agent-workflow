import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

from scripts.roundtrip_core import merge, prepare
from scripts.grade_metrics import compare_metrics
from scripts.image_io import read_rgb, save_rgb


ROOT = Path(__file__).resolve().parents[1]


class RoundTripCliTests(unittest.TestCase):
    def test_local_edit_passes_and_protected_leak_fails(self):
        with tempfile.TemporaryDirectory() as td:
            work = Path(td)
            original = np.full((32, 32, 3), 0.45)
            mask = np.zeros((32, 32), dtype=np.uint8)
            mask[10:22, 10:22] = 255
            good = original.copy()
            good[10:22, 10:22, 0] = 0.8
            bad = good.copy()
            bad[:8, :8] = [0.9, 0.1, 0.1]
            needle = good.copy()
            needle[0, 0] = [1.0, 0.0, 1.0]
            resized = good[::2, ::2]
            save_rgb(original, work / "original.png")
            save_rgb(good, work / "good.png")
            save_rgb(bad, work / "bad.png")
            save_rgb(needle, work / "needle.png")
            save_rgb(resized, work / "resized.png")
            Image.fromarray(mask).save(work / "mask.png")
            for name, expected in (("good", 0), ("bad", 1), ("needle", 1), ("resized", 1)):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "scripts/roundtrip.py"), "verify",
                     str(work / "original.png"), str(work / f"{name}.png"),
                     "--mask", str(work / "mask.png"), "--out", str(work / name)],
                    capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                self.assertTrue((work / name / "compare.html").is_file())
                self.assertTrue((work / name / "close-up.png").is_file())
                page = (work / name / "compare.html").read_text(encoding="utf-8")
                self.assertIn(f"original.png", page)
                self.assertIn(f"{name}.png", page)
                self.assertIn("<details>", page)
                self.assertIn("#808080", page)
                if name == "resized":
                    report = json.loads(result.stdout)
                    self.assertTrue(report["alignment"]["edited_resized_to_original"])
                    self.assertTrue(report["roundtrip"]["manual_review_required"])
                elif name == "good":
                    report = json.loads(result.stdout)
                    self.assertIn("mask_core", report["delta_e_2000"])
                    self.assertIn("transition_band", report["delta_e_2000"])
                    self.assertNotIn("inside_mask", report["delta_e_2000"])
                    self.assertEqual(report["roundtrip"]["unchecked_outside_mask_width_px"], 0)
                    self.assertGreater(report["roundtrip"]["transition_band_pixels"], 0)

    def test_three_and_five_pixel_red_rings_fail_transition_band(self):
        with tempfile.TemporaryDirectory() as td:
            work = Path(td)
            original = np.full((80, 80, 3), .45)
            mask = np.zeros((80, 80), dtype=np.uint8)
            mask[25:55, 25:55] = 255
            save_rgb(original, work/"original.png")
            Image.fromarray(mask).save(work/"mask.png")
            for thickness in (3, 5):
                edited = original.copy()
                edited[25-thickness:55+thickness, 25-thickness:55+thickness] = [.95, .05, .05]
                edited[25:55, 25:55] = original[25:55, 25:55]
                save_rgb(edited, work/f"ring-{thickness}.png")
                result = subprocess.run(
                    [sys.executable, str(ROOT/"scripts/roundtrip.py"), "verify",
                     str(work/"original.png"), str(work/f"ring-{thickness}.png"),
                     "--mask", str(work/"mask.png"), "--out", str(work/f"review-{thickness}")],
                    capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, 1, result.stdout+result.stderr)
                report = json.loads(result.stdout)
                self.assertFalse(report["roundtrip"]["transition_band_passed"])
                self.assertGreater(report["roundtrip"]["transition_band_max_delta_e_2000"], 3)
                self.assertIsNotNone(report["roundtrip"]["transition_band_bbox_over_limit_xyxy"])

    def test_merge_composites_only_through_mask(self):
        with tempfile.TemporaryDirectory() as td:
            work = Path(td)
            original = np.full((32, 32, 3), .45)
            mask = np.zeros((32, 32), dtype=np.uint8); mask[10:22, 9:23] = 255
            save_rgb(original, work/"original.png")
            Image.fromarray(mask).save(work/"mask.png")
            prepare(work/"original.png", work/"mask.png", "edit the object", work/"prepared")
            crop_path = work/"prepared"/"region-crop.png"
            crop = read_rgb(crop_path)
            crop[:] = [.8, .2, .1]
            save_rgb(crop, work/"edited-crop.png")
            merge(work/"original.png", work/"edited-crop.png", work/"mask.png", work/"merged.png")
            merged = read_rgb(work/"merged.png")
            np.testing.assert_allclose(merged[mask == 0], original[mask == 0], atol=1/65535)
            self.assertGreater(float(merged[15, 15, 0]), float(original[15, 15, 0]))

    def test_compare_metrics_uses_mask_key_for_hard_mask(self):
        a = np.full((4, 4, 3), .5)
        b = a.copy(); b[1, 1] = .7
        mask = np.zeros((4, 4)); mask[1, 1] = 1
        metrics = compare_metrics(a, b, mask)["delta_e_2000"]
        self.assertEqual(metrics["mask"]["count"], 1)
        self.assertNotIn("inside_mask", metrics)


if __name__ == "__main__":
    unittest.main()
