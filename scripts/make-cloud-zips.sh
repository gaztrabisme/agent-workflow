#!/usr/bin/env bash
# Build one upload zip per skill for claude.ai (Settings > Customize > Skills).
#
#   ./scripts/make-cloud-zips.sh [output-folder]      default: ~/agent-workflow-cloud
#
# Each zip holds one folder, <skill>/, with SKILL.md at its top. Images, PDFs, audio,
# video and zip files are left out: they make six design skills 82-325 MB each, and the
# lesson text and method files keep working without them.
set -euo pipefail

AW="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-$HOME/agent-workflow-cloud}"
mkdir -p "$OUT"
command -v zip >/dev/null || { echo "zip is required" >&2; exit 1; }

cd "$AW/skills"
while read -r name; do
  [ -n "$name" ] || continue
  rm -f "$OUT/$name.zip"
  zip -q -r "$OUT/$name.zip" "$name" \
    -x '*.git*' '*.DS_Store' '*/__pycache__/*' '*/.ruff_cache/*' '*/local/*' \
       '*.jpg' '*.jpeg' '*.png' '*.pdf' '*.webp' '*.gif' '*.mp4' '*.wav' '*.mov' '*.zip'
  size=$(wc -c < "$OUT/$name.zip" | tr -d ' ')
  printf '%-28s %9s bytes  %s files\n' "$name" "$size" "$(unzip -Z1 "$OUT/$name.zip" | wc -l | tr -d ' ')"
done < "$AW/skills.txt"
