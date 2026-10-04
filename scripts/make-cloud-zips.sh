#!/usr/bin/env bash
# Build one upload zip per skill for claude.ai (Settings > Customize > Skills).
#
#   ./scripts/make-cloud-zips.sh [output-folder]      default: ~/agent-workflow-cloud
#
# Each zip holds one folder, <skill>/, with SKILL.md at its top. Images, PDFs, audio,
# video and zip files are left out: they make six design skills 82-325 MB each, and the
# lesson text and method files keep working without them. Skills over claude.ai's 200-file
# limit (color-theory, photo, zalo-platform) go through scripts/cloud_merge.py first.
set -euo pipefail

AW="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-$HOME/agent-workflow-cloud}"
mkdir -p "$OUT"
command -v zip >/dev/null || { echo "zip is required" >&2; exit 1; }

cd "$AW/skills"
while read -r name; do
  [ -n "$name" ] || continue
  rm -f "$OUT/$name.zip"
  case "$name" in
    color-theory|photo|zalo-platform)
      # more than 200 files: merge the reference libraries into fewer files first
      stage="$(mktemp -d)"
      python3 "$AW/scripts/cloud_merge.py" "$name" "$stage/$name" >&2
      (cd "$stage" && zip -q -r "$OUT/$name.zip" "$name" -x '*.DS_Store')
      printf '%-28s %9s bytes  %s files (merged)\n' "$name" "$(wc -c < "$OUT/$name.zip" | tr -d ' ')" "$(unzip -Z1 "$OUT/$name.zip" | grep -vc '/$')"
      continue ;;
  esac
  zip -q -r "$OUT/$name.zip" "$name" \
    -x '*.git*' '*.DS_Store' '*/__pycache__/*' '*/.ruff_cache/*' '*/local/*' '*/.claude/*' '*/.inventory/*' \
       '*.jpg' '*.jpeg' '*.png' '*.pdf' '*.webp' '*.gif' '*.mp4' '*.wav' '*.mov' '*.zip'
  size=$(wc -c < "$OUT/$name.zip" | tr -d ' ')
  printf '%-28s %9s bytes  %s files\n' "$name" "$size" "$(unzip -Z1 "$OUT/$name.zip" | wc -l | tr -d ' ')"
done < "$AW/skills.txt"
