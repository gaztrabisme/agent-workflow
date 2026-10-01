import unittest

import numpy as np

from scripts.color_math import delta_e_2000, rgb_to_lab
from scripts.grade_ops import levels
from scripts.image_io import read_rgb
from scripts.lut import apply_cube


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


if __name__ == "__main__":
    unittest.main()
