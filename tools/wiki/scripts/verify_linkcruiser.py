"""Run the supplied read-only corpus acceptance check and retain its evidence."""

import argparse
from collections import Counter
from contextlib import redirect_stdout
import hashlib
from io import StringIO
import json
from pathlib import Path
import subprocess
import sys


def snapshot(folder):
    return {str(path.relative_to(folder)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(folder.rglob("*")) if path.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wiki", type=Path)
    parser.add_argument("--no-sync", action="store_true", help="use the existing offline environment")
    parser.add_argument("--system-python", action="store_true", help="fallback: run the CLI function from src")
    args = parser.parse_args()
    folder = args.wiki.expanduser().resolve()
    workspace = Path(__file__).resolve().parents[1]
    command = ["uv", "run", *(["--no-sync"] if args.no_sync else []), "wiki", "lint", str(folder)]
    def run(extra):
        if not args.system_python:
            return subprocess.run([*command, *extra], cwd=workspace, capture_output=True, text=True)
        sys.path.insert(0, str(workspace / "src"))
        from wiki_tool.cli import main as cli_main

        stream = StringIO()
        with redirect_stdout(stream):
            code = cli_main(["lint", str(folder), *extra])
        return subprocess.CompletedProcess([sys.executable, "wiki_tool.cli.main"], code, stream.getvalue(), "")

    before = snapshot(folder)
    text_run = run([])
    json_run = run(["--json"])
    after = snapshot(folder)
    findings = json.loads(json_run.stdout)["findings"] if json_run.returncode == 0 else []
    counts = Counter(item["rule"] for item in findings)
    rules = ["index-over-cap", "log-over-cap", "unreachable", "index-dead-entry",
             "broken-link", "run-report-in-index", "undated-page"]
    passed = (bool(before) and before == after and text_run.returncode == json_run.returncode == 0
              and all(counts[rule] for rule in ["index-over-cap", "log-over-cap", "run-report-in-index"])
              and counts["broken-link"] <= 3)
    report = {"verdict": "PASS" if passed else "FAIL", "command": command,
              "execution": "system Python, CLI function from src" if args.system_python else "uv console script",
              "wiki": str(folder), "files_checked": len(before), "unchanged": before == after,
              "counts": {rule: counts[rule] for rule in rules}, "return_codes": [text_run.returncode, json_run.returncode],
              "stderr": text_run.stderr, "before": before, "after": after}
    destination = workspace / "wiki"
    (destination / "linkcruiser-acceptance.json").write_text(json.dumps(report, indent=2) + "\n")
    (destination / "linkcruiser-lint.txt").write_text(text_run.stdout)
    if json_run.returncode == 0:
        (destination / "linkcruiser-findings.json").write_text(json_run.stdout)
    print("\n".join(text_run.stdout.splitlines()[:20]))
    print(json.dumps({key: report[key] for key in ["verdict", "files_checked", "unchanged", "counts"]}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
