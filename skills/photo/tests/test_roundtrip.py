import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

from scripts.image_io import save_rgb


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
                if name == "resized":
                    report = json.loads(result.stdout)
                    self.assertTrue(report["alignment"]["edited_resized_to_original"])
                    self.assertTrue(report["roundtrip"]["manual_review_required"])


if __name__ == "__main__":
    unittest.main()
