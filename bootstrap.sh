#!/usr/bin/env bash
# Install or update agent-workflow with a fine-grained GitHub token. No GitHub login,
# no saved credential: the token is read from AW_GH_TOKEN (or asked for, hidden), passed
# to git only through the environment, and never written to disk.
#
#   ./bootstrap.sh                     install, or update if the folder exists
#   ./bootstrap.sh --dir <path>        install folder (default ~/Documents/Work/tools/agent-workflow)
#   ./bootstrap.sh --with-tools        also install render-kit and scene-engine dependencies
set -euo pipefail

REPO="gaztrabisme/agent-workflow"
DIR="$HOME/Documents/Work/tools/agent-workflow"
TOOLS=""
while [ $# -gt 0 ]; do
  case "$1" in
    --dir) DIR="$2"; shift 2 ;;
    --dir=*) DIR="${1#*=}"; shift ;;
    --with-tools) TOOLS="--with-tools"; shift ;;
    -h|--help) sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) printf 'Unknown option: %s (try --help)\n' "$1" >&2; exit 2 ;;
  esac
done

for c in git python3; do command -v "$c" >/dev/null || { echo "Error: $c is required." >&2; exit 1; }; done
git lfs version >/dev/null 2>&1 || { echo "Error: git-lfs is required (course images and PDFs)." >&2; exit 1; }

if [ -z "${AW_GH_TOKEN:-}" ]; then
  printf 'GitHub token (fine-grained, Contents: Read-only on %s): ' "$REPO" >&2
  read -r -s AW_GH_TOKEN; echo >&2
  [ -n "$AW_GH_TOKEN" ] || { echo "Error: the token cannot be empty." >&2; exit 1; }
fi

# git reads these variables as configuration for this process and its children
# (including git-lfs): send the token as a header, use no stored credentials, never prompt.
AUTH="$(printf 'x-access-token:%s' "$AW_GH_TOKEN" | base64 | tr -d '\n')"
export GIT_CONFIG_COUNT=2 \
  GIT_CONFIG_KEY_0="http.https://github.com/.extraheader" GIT_CONFIG_VALUE_0="AUTHORIZATION: basic $AUTH" \
  GIT_CONFIG_KEY_1="credential.helper" GIT_CONFIG_VALUE_1="" \
  GIT_TERMINAL_PROMPT=0
unset AUTH AW_GH_TOKEN

fail() { echo "Error: $1 Either the network is down, or GitHub refused the token (git then reports 'could not read Username', 401, 403 or 'not found'): check that it has not expired and has Contents: Read-only on $REPO." >&2; exit 1; }

if [ -d "$DIR/.git" ]; then
  git -C "$DIR" remote get-url origin | grep -q "$REPO" || { echo "Error: $DIR is a different repository." >&2; exit 1; }
  echo "Updating $DIR ..."
  git -C "$DIR" pull --ff-only || fail "git pull failed."
else
  [ -e "$DIR" ] && { echo "Error: $DIR exists and is not a git repository." >&2; exit 1; }
  echo "Cloning $REPO into $DIR (about 1.3 GB of course files follow) ..."
  mkdir -p "$(dirname "$DIR")"
  GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/$REPO.git "$DIR" || fail "git clone failed."
  git -C "$DIR" lfs install --local >/dev/null
fi
git -C "$DIR" lfs pull || fail "git lfs pull failed."

"$DIR/install.sh" $TOOLS
