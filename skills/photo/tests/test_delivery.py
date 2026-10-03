import json
import subprocess
import sys
import tempfile
import unittest
from io import BytesIO
from pathlib import Path

import numpy as np
from PIL import Image, ImageCms

from scripts.delivery import deliver
from scripts.image_io import read_rgb, save_rgb

ROOT = Path(__file__).resolve().parents[1]


class DeliveryTests(unittest.TestCase):
    def test_deliver_crops_resizes_embeds_srgb_and_checks_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = np.zeros((12, 20, 3), dtype=float)
            source[..., 0] = np.linspace(0, 1, 20)[None, :]
            save_rgb(source, root/"source.png")
            spec = {"items": [{"input": "source.png", "file": "approval.jpg",
                               "crop": [2, 2, 18, 10], "size": [8, 4],
                               "format": "JPEG", "quality": 91}]}
            (root/"delivery.json").write_text(json.dumps(spec), encoding="utf-8")
            result = deliver(root/"delivery.json", root/"out")
            output = root/"out"/"approval.jpg"
            with Image.open(output) as image:
                self.assertEqual(image.size, (8, 4))
                self.assertEqual(image.format, "JPEG")
                profile = ImageCms.ImageCmsProfile(BytesIO(image.info["icc_profile"]))
                self.assertIn("srgb", ImageCms.getProfileName(profile).casefold())
            self.assertTrue(result["checks"]["passed"])
            self.assertEqual(result["checks"]["expected_file_count"], 1)
            self.assertEqual(result["checks"]["actual_file_count"], 1)
            manifest = json.loads((root/"out"/"manifest.json").read_text(encoding="utf-8"))
            self.assertTrue(manifest["checks"]["outputs"][0]["icc_srgb_ok"])
            self.assertEqual(read_rgb(output).shape, (4, 8, 3))

    def test_delivery_rejects_upscale_unless_spec_explicitly_allows_it(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            save_rgb(np.full((4, 4, 3), .5), root/"source.png")
            spec_file = root/"delivery.json"
            spec_file.write_text(json.dumps({"items": [{"input": "source.png", "file": "story.jpg",
                                                          "size": [8, 8]}]}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "upscaling"):
                deliver(spec_file, root/"out")
            spec_file.write_text(json.dumps({"items": [{"input": "source.png", "file": "story.jpg",
                                                          "size": [8, 8], "allow_upscale": True}]}), encoding="utf-8")
            result = deliver(spec_file, root/"out")
            self.assertTrue(result["outputs"][0]["upscaled"])
            self.assertEqual(result["outputs"][0]["scale"], 2)

    def test_grade_cli_deliver_subcommand(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            save_rgb(np.full((6, 8, 3), .4), root/"source.png")
            (root/"delivery.json").write_text(json.dumps({"items": [
                {"input": "source.png", "file": "web.jpg", "size": [4, 3],
                 "format": "JPEG", "quality": 88}]}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT/"scripts/grade.py"), "deliver",
                                     str(root/"delivery.json"), "--out", str(root/"out")],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
            self.assertTrue(json.loads(result.stdout)["checks"]["passed"])

    def test_deliver_supports_lossless_tiff_with_srgb_profile(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            save_rgb(np.full((6, 8, 3), .4), root/"source.png")
            (root/"delivery.json").write_text(json.dumps({"items": [
                {"input": "source.png", "file": "archive.tif", "format": "TIFF"}]}),
                encoding="utf-8")
            result = deliver(root/"delivery.json", root/"out")
            with Image.open(root/"out"/"archive.tif") as image:
                self.assertEqual(image.format, "TIFF")
                profile = ImageCms.ImageCmsProfile(BytesIO(image.info["icc_profile"]))
                self.assertIn("srgb", ImageCms.getProfileName(profile).casefold())
            self.assertTrue(result["checks"]["passed"])

    def test_delivery_accepts_dimension_rounding_but_rejects_different_crop_ratio(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            save_rgb(np.full((163, 300, 3), .4), root/"source.png")
            spec_file = root/"delivery.json"
            spec_file.write_text(json.dumps({"items": [{"input": "source.png", "file": "web.jpg",
                                                          "size": [120, 65]}]}), encoding="utf-8")
            result = deliver(spec_file, root/"out")
            self.assertTrue(result["checks"]["passed"])
            spec_file.write_text(json.dumps({"items": [{"input": "source.png", "file": "wrong.jpg",
                                                          "size": [120, 50]}]}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "different aspect ratios"):
                deliver(spec_file, root/"other-out")


if __name__ == "__main__":
    unittest.main()
