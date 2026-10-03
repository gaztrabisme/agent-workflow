#!/usr/bin/env bash
set -u

skill_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tools_root="$(cd "$skill_root/../.." && pwd)"
rk_bin="${RK_BIN:-$tools_root/render-kit/bin/rk}"

if [[ ! -x "$rk_bin" ]]; then
  echo "render-kit executable not found: $rk_bin" >&2
  exit 2
fi

check_tmp="$(mktemp -d "${TMPDIR:-/tmp}/information-design-templates.XXXXXX")"
trap 'rm -rf "$check_tmp"' EXIT
failed=0
found=0

for template in "$skill_root"/templates/*.svg "$skill_root"/templates/*.html; do
  [[ -f "$template" ]] || continue
  found=1
  name="$(basename "$template")"
  stem="${name%.*}"
  out_dir="$check_tmp/$stem"
  log_file="$check_tmp/$stem.log"
  echo "Checking $name"
  if "$rk_bin" check "$template" --out-dir "$out_dir" >"$log_file" 2>&1; then
    echo "  PASS: rk check exited 0"
    if [[ -f "$out_dir/report.json" ]]; then
      python3 - "$out_dir/report.json" <<'PY'
import json
import sys

report = json.load(open(sys.argv[1], encoding="utf-8"))
for check in report.get("checks", []):
    if check.get("id") == "value" and check.get("status") in {"skipped", "incomplete"}:
        reason = check.get("reason") or "render-kit could not decide"
        print(f"  NOTE: value/chroma undecidable: {reason}")
PY
    fi
  else
    echo "  FAIL: rk check returned non-zero" >&2
    cat "$log_file" >&2
    failed=1
  fi
done

if [[ "$found" -eq 0 ]]; then
  echo "No SVG or HTML templates found under $skill_root/templates" >&2
  exit 2
fi
exit "$failed"
