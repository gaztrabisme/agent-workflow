#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
if [[ -z "${ARCHIVE_ACCEPT_DIR:-}" ]]; then
  ARCHIVE_ACCEPT_DIR="$(mktemp -d "${TMPDIR:-/tmp}/archive-P3-accept.XXXXXX")"
  export ARCHIVE_ACCEPT_DIR
fi
mkdir -p "$ARCHIVE_ACCEPT_DIR"
python3 -m unittest discover -s tests -v
printf 'Archive acceptance artifacts: %s\n' "$ARCHIVE_ACCEPT_DIR"
