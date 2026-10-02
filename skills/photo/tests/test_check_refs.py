import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReferenceCheckerTests(unittest.TestCase):
    def test_checker_counts_relative_links_and_parses_inline_commands(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root/"references/course-test").mkdir(parents=True)
            (root/"references").mkdir(exist_ok=True)
            (root/"scripts").mkdir()
            (root/"SKILL.md").write_text(
                "See [guide](references/guide.md). Run `scripts/tool.py --version`. "
                "Anchor: 1 · U1 · L01 · 00:00–00:01.\n", encoding="utf-8")
            (root/"references/guide.md").write_text("Guide.\n", encoding="utf-8")
            (root/"references/course-test/anchors.md").write_text(
                "1 · U1 · L01 · 00:00–00:01\n", encoding="utf-8")
            (root/"scripts/tool.py").write_text("pass\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT/"scripts/check_refs.py"), str(root)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
            self.assertIn("1 Markdown links checked", result.stdout)
            self.assertIn("0 problem(s)", result.stdout)


if __name__ == "__main__":
    unittest.main()
