"""Pure measures and render-kit sample integration checks."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from measure_balance import measure_balance
from measure_focal import measure_focal
from measure_grid import measure_grid
from measure_scale import measure_scale
from measure_space import measure_space, union_area

PYTHON = sys.executable
AGENT_WORKFLOW = Path(os.environ.get("AGENT_WORKFLOW", Path.home() / ".agent-workflow"))
RENDER_KIT = AGENT_WORKFLOW / "tools" / "render-kit"
RK = RENDER_KIT / "bin/rk"
HELPER = ROOT / "scripts/measure_boxes.mjs"
CHECKS = ROOT / "scripts/checks.py"


class PureMeasures(unittest.TestCase):
    def test_balance_centred_and_off_centre(self):
        pixels = np.ones((40, 40, 3))
        pixels[15:25, 5:15] = 0
        pixels[15:25, 25:35] = 0
        self.assertEqual(measure_balance(pixels, "centered")[2], "pass")
        pixels[:, 30:] = 0
        self.assertEqual(measure_balance(pixels, "centered")[2], "fail")

    def test_grid_guides_and_tolerance(self):
        boxes = {"grid": [[16, 0, 66, 10], [238, 0, 66, 10]], "css_frame": [320, 200],
                 "scale": 1, "columns": 4, "gutter": 8, "margin": 16}
        self.assertEqual(measure_grid(boxes)[2], "pass")
        boxes["grid"][1][0] = 248
        self.assertEqual(measure_grid(boxes)[2], "fail")

    def test_space_union_does_not_double_count_overlap(self):
        self.assertEqual(union_area([[0, 0, 2, 2], [1, 0, 2, 2]], 4, 4), 6)
        boxes = {"frame": [10, 10], "occupies": [[0, 0, 5, 5]], "space_target": 0.75}
        self.assertEqual(measure_space(boxes)[2], "pass")

    def test_type_scale_ratios(self):
        self.assertEqual(measure_scale({"font_sizes": [32, 24, 18]})[2], "pass")
        self.assertEqual(measure_scale({"font_sizes": [32, 30, 20]})[2], "fail")

    def test_type_scale_deduplicates_repeated_same_level_text(self):
        result, _, status = measure_scale({"font_sizes": [32, 24, 24, 18, 18]})
        self.assertEqual(status, "pass")
        self.assertEqual(result["font_sizes_px"], [32, 24, 18])

    def test_focal_edge_energy_density(self):
        pixels = np.ones((30, 30, 3))
        pixels[9:21, 9:21] = 0
        self.assertEqual(measure_focal(pixels, [8, 8, 14, 14])[2], "pass")
        self.assertEqual(measure_focal(pixels, [0, 0, 4, 4])[2], "fail")


def sample_test(sample: Path, should_fail: str | None):
    def run(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            out = Path(temp)
            env = {**os.environ, "RK_COLOR_THEORY": str(AGENT_WORKFLOW / "skills" / "color-theory")}
            rendered = subprocess.run([str(RK), "check", str(sample), "--out-dir", str(out)],
                                      capture_output=True, text=True, env=env)
            self.assertTrue((out / "render.png").is_file(), rendered.stdout + rendered.stderr)
            json.loads(rendered.stdout)
            boxes_path = out / "boxes.json"
            helper = subprocess.run(["node", str(HELPER), str(sample), "--render-kit", str(RENDER_KIT), "--out", str(boxes_path)],
                                    capture_output=True, text=True)
            self.assertEqual(helper.returncode, 0, helper.stderr)
            boxes = json.loads(boxes_path.read_text())
            statuses = {}
            for name in ("grid", "balance", "space", "scale", "focal"):
                checked = subprocess.run([PYTHON, str(CHECKS), name, str(out / "render.png"), "--boxes", str(boxes_path)],
                                         capture_output=True, text=True)
                result = json.loads(checked.stdout)
                statuses[name] = result["status"]
                self.assertEqual(checked.returncode, 1 if result["status"] == "fail" else 0, checked.stderr)
                expected_source = {"space": "data-vd-space-target + skill default tolerance",
                                   "scale": "data-vd-type-scale"}.get(name, "skill default")
                self.assertEqual(result["source"], expected_source)
            expected = {name: ("fail" if name == should_fail else "pass") for name in statuses}
            self.assertEqual(statuses, expected, f"{sample.name}: {boxes}")
    return run


for category, failure in (("good", None), ("bad", "grid"), ("bad", "balance"),
                          ("bad", "space"), ("bad", "scale"), ("bad", "focal")):
    for name in ("grid", "balance", "space", "scale", "focal") if category == "good" else (failure,):
        sample = ROOT / "samples" / category / f"{name}.svg"
        setattr(PureMeasures, f"test_sample_{category}_{name}", sample_test(sample, failure))


if __name__ == "__main__":
    unittest.main()
