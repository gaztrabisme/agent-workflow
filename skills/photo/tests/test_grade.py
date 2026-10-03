import unittest
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image

from scripts.color_math import delta_e_2000, rgb_to_lab
from scripts.grade_ops import levels
from scripts.grade_color import white_balance
from scripts.grade_metrics import measure, recipe_output_range_warnings
from scripts.image_io import read_rgb, save_rgb
from scripts.lut import apply_cube

ROOT = Path(__file__).resolve().parents[1]


class ColourMathTests(unittest.TestCase):
    def test_srgb_white_maps_to_d65_lab_white(self):
        np.testing.assert_allclose(rgb_to_lab(np.ones((1, 3))), [[100, 0, 0]], atol=0.02)

    def test_delta_e_2000_matches_sharma_reference_pairs(self):
        a = np.array([[50, 2.6772, -79.7751], [50, 3.1571, -77.2803]])
        b = np.array([[50, 0, -82.7485], [50, 0, -82.7485]])
        np.testing.assert_allclose(delta_e_2000(a, b), [2.0425, 2.8615], atol=0.0001)

    def test_identity_cube_preserves_rgb(self):
        cube = """LUT_3D_SIZE 2
0 0 0
1 0 0
0 1 0
1 1 0
0 0 1
1 0 1
0 1 1
1 1 1
"""
        rgb = np.array([[[0.2, 0.4, 0.7], [1.0, 0.0, 0.5]]])
        np.testing.assert_allclose(apply_cube(rgb, cube), rgb, atol=1e-7)

    def test_levels_maps_black_white_and_gamma(self):
        src = np.array([[[0.0, 0.5, 1.0]]])
        np.testing.assert_allclose(levels(src, 0.2, 0.8, 1.0), [[[0, 0.5, 1]]])

    def test_gray_alpha_input_repeats_gray_and_ignores_alpha(self):
        from PIL import Image
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as td:
            path = Path(td)/"gray-alpha.png"
            Image.fromarray(np.array([[[128, 0], [64, 255]]], dtype=np.uint8), "LA").save(path)
            np.testing.assert_allclose(read_rgb(path), [[[128/255]*3, [64/255]*3]])

    def test_selected_neutral_region_includes_cast_pixels_and_reports_share(self):
        rgb = np.broadcast_to([0.55, 0.3, 0.1], (10, 10, 3)).copy()
        fallback = measure(rgb)["neutral_patch"]
        self.assertEqual(fallback["count"], 0)
        self.assertTrue(any("below 5%" in warning for warning in fallback["warnings"]))
        selected = measure(rgb, neutral_rect=(2, 3, 7, 8))["neutral_patch"]
        self.assertEqual(selected["count"], 25)
        self.assertEqual(selected["selection_share_of_image"], .25)
        self.assertIsNotNone(selected["b_mean"])

    def test_mask_reports_lightness_chroma_clipping_and_histogram(self):
        rgb = np.full((8, 8, 3), .5)
        rgb[2:4, 2:4] = [1, .2, .1]
        mask = np.zeros((8, 8)); mask[2:4, 2:4] = 1
        result = measure(rgb, mask)["masked_region"]
        self.assertEqual(result["count"], 4)
        self.assertEqual(result["share_of_image"], 4/64)
        self.assertGreater(result["l_star_mean"], 0)
        self.assertGreater(result["c_star_mean"], 0)
        self.assertEqual(result["clipped_highlights_pct"], 100)
        self.assertEqual(sum(result["histogram_l_star_0_100"]), 4)

    def test_white_balance_normalizes_gains_and_uses_linear_light(self):
        from scripts.color_math import srgb_to_linear
        neutral = np.full((3, 3, 3), .5)
        cool = white_balance(neutral, {"temperature": 4000})
        warm = white_balance(neutral, {"temperature": 8000})
        y_weights = np.array([.2126, .7152, .0722])
        self.assertAlmostEqual(float(np.dot(srgb_to_linear(cool)[0, 0], y_weights)),
                               float(np.dot(srgb_to_linear(neutral)[0, 0], y_weights)), places=7)
        self.assertGreater(cool[0, 0, 2], cool[0, 0, 0])
        self.assertGreater(warm[0, 0, 0], warm[0, 0, 2])
        tinted = np.broadcast_to([.6, .5, .4], (4, 4, 3)).copy()
        neutralized = white_balance(tinted, {"neutral_rect": [0, 0, 4, 4]})
        np.testing.assert_allclose(neutralized[0, 0], neutralized[0, 0, 0], atol=1e-6)

    def test_recipe_range_warning_identifies_lifted_black_and_lowered_white(self):
        warnings = recipe_output_range_warnings({"operations": [
            {"type": "tone_curve", "points": [[0, .015], [.5, .5], [1, .98]]}]})
        self.assertEqual(len(warnings), 2)
        self.assertIn("lifts encoded black", warnings[0])
        self.assertIn("lowers encoded white", warnings[1])

    def test_measure_cli_accepts_neutral_rectangle_and_mask(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rgb = np.full((10, 10, 3), .5); rgb[4:8, 4:8] = [1, .2, .1]
            mask = np.zeros((10, 10), dtype=np.uint8); mask[4:8, 4:8] = 255
            from scripts.image_io import save_rgb
            save_rgb(rgb, root/"photo.png"); Image.fromarray(mask).save(root/"mask.png")
            result = subprocess.run([sys.executable, str(ROOT/"scripts/grade.py"), "measure",
                                     str(root/"photo.png"), "--neutral-rect", "0", "0", "3", "3",
                                     "--mask", str(root/"mask.png")], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            metrics = json.loads(result.stdout)
            self.assertEqual(metrics["neutral_patch"]["selection_share_of_image"], .09)
            self.assertEqual(metrics["masked_region"]["count"], 16)
            self.assertEqual(metrics["masked_region"]["histogram_l_star_bins"], 16)

    def test_compare_cli_named_region_writes_100_percent_crop_and_file_labels(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            a = np.full((20, 24, 3), .4); b = a.copy(); b[4:10, 5:11] = .7
            save_rgb(a, root/"base.png"); save_rgb(b, root/"edit.png")
            Path(str(root/"edit.png")+".recipe.json").write_text(json.dumps({"operations": [
                {"type": "tone_curve", "points": [[0, .015], [1, .98]]}]}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT/"scripts/grade.py"), "compare",
                                     str(root/"base.png"), str(root/"edit.png"),
                                     "--region", "5", "4", "11", "10", "--region-name", "left eye",
                                     "--out", str(root/"review")], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
            metrics = json.loads(result.stdout)
            self.assertEqual(len(metrics["recipe_output_range_warnings"]), 2)
            with Image.open(root/"review"/"close-up.png") as crop:
                self.assertEqual(crop.size, (12, 6))
            page = (root/"review"/"compare.html").read_text(encoding="utf-8")
            self.assertIn("base.png ↔ edit.png", page)
            self.assertIn("left eye", page)
            self.assertIn("<details>", page)


if __name__ == "__main__":
    unittest.main()
