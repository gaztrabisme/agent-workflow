#!/usr/bin/env bash
# Code quality scanner — JSON summary to stdout, full output to log file.
# Requires applicable quality tools; records exactly which tools ran.
#
# Set DEV_SKILL_DIR to the installed dev skill directory once.
# Usage: bash "$DEV_SKILL_DIR/scripts/run-quality.sh" [options] [path]
#
# Options:
#   --log-dir DIR        Directory for log files (default: fresh directory under TMPDIR)
#   --strict             Accepted for compatibility; errors always fail
#   --security-only      Run only security checks (bandit)
#   --lint-only          Run only lint checks (ruff)
#   --types-only         Run only type checks (pyright or tsc)
#
# Output (stdout): JSON summary
#   {"status":"pass","lint":{"errors":0,"warnings":3},"security":{"issues":0},"types":{"errors":0},"log":"logs/quality.log"}
#   {"status":"fail","lint":{"errors":5,"warnings":3},"security":{"issues":2,"critical":["B105:hardcoded_password"]},"types":{"errors":1},"log":"logs/quality.log"}

set -euo pipefail

# ── Parse arguments ──────────────────────────────────────
log_dir=""
target_path="."
run_lint=true
run_security=true
run_types=true

while [[ $# -gt 0 ]]; do
    case "$1" in
        --log-dir)
            log_dir="$2"
            shift 2
            ;;
        --strict)
            shift
            ;;
        --security-only)
            run_lint=false
            run_types=false
            shift
            ;;
        --lint-only)
            run_security=false
            run_types=false
            shift
            ;;
        --types-only)
            run_lint=false
            run_security=false
            shift
            ;;
        --)
            shift
            target_path="${1:-.}"
            break
            ;;
        *)
            target_path="$1"
            shift
            ;;
    esac
done

if [[ -z "$log_dir" ]]; then
    tmp_root="${TMPDIR:-/tmp}"
    log_dir=$(mktemp -d "${tmp_root%/}/dev-quality.XXXXXX")
else
    mkdir -p "$log_dir"
fi
log_file="${log_dir}/quality.log"
> "$log_file"

# ── Helpers ──────────────────────────────────────────────
json_escape() {
    local s="$1" code hex control
    s="${s//\\/\\\\}"
    s="${s//\"/\\\"}"
    for ((code = 1; code < 32; code++)); do
        printf -v hex '%02x' "$code"
        printf -v control '%b' "\\x$hex"
        s="${s//"$control"/\\u00$hex}"
    done
    printf '%s' "$s"
}

has_python_files() {
    find "$target_path" -name '*.py' -not -path '*/node_modules/*' -not -path '*/.venv/*' -not -path '*/__pycache__/*' -not -path '*/.git/*' -print -quit 2>/dev/null | grep -q .
}

has_js_files() {
    find "$target_path" \( -name '*.js' -o -name '*.mjs' -o -name '*.cjs' -o -name '*.ts' -o -name '*.jsx' -o -name '*.tsx' -o -name '*.mts' -o -name '*.cts' \) -not -path '*/node_modules/*' -not -path '*/.venv/*' -not -path '*/__pycache__/*' -not -path '*/.git/*' -print -quit 2>/dev/null | grep -q .
}

has_typescript_files() {
    find "$target_path" \( -name '*.ts' -o -name '*.tsx' -o -name '*.mts' -o -name '*.cts' \) -not -path '*/node_modules/*' -not -path '*/.venv/*' -not -path '*/__pycache__/*' -not -path '*/.git/*' -print -quit 2>/dev/null | grep -q .
}

# Resolve target-local tools before ancestor installations or PATH tools.
find_js_tool() {
    local dir="$target_dir" bin
    while [[ -n "$dir" ]]; do
        if [[ -x "$dir/node_modules/.bin/$1" ]]; then
            printf '%s' "$dir/node_modules/.bin/$1"
            return
        fi
        [[ "$dir" != / ]] || break
        dir=$(dirname "$dir")
    done
    bin=$(command -v "$1") || return 1
    [[ "$bin" == /* ]] || bin="$PWD/$bin"
    printf '%s' "$bin"
}

# Keep log paths relative to the caller while tools run from the target.
if [[ -d "$target_path" ]]; then
    target_dir=$(cd "$target_path" && pwd -P)
    target_path="$target_dir"
else
    target_dir=$(cd "$(dirname "$target_path")" && pwd -P)
    target_path="$target_dir/$(basename "$target_path")"
fi

# ── Detect project type ──────────────────────────────────
is_python=false
is_js=false
is_typescript=false

if has_python_files; then
    is_python=true
fi
if has_js_files; then
    is_js=true
fi
if has_typescript_files; then
    is_typescript=true
fi

if ! $is_python && ! $is_js; then
    echo '{"status":"error","checks_run":[],"message":"No supported scanner; configure a native gate."}'
    exit 2
fi

# ── Initialize counters ─────────────────────────────────
lint_errors=0
lint_warnings=0
lint_fixable=0
security_issues=0
security_critical=()
type_errors=0
overall_status="pass"
checks_run=()
checks_run_count=0

record_check() {
    checks_run+=("$1")
    checks_run_count=$((checks_run_count + 1))
}

# ── Ruff (lint + format check) ──────────────────────────
if $run_lint && $is_python && command -v ruff &>/dev/null; then
    record_check "ruff check"
    record_check "ruff format --check"
    echo "=== RUFF LINT ===" >> "$log_file"

    # Lint check
    ruff_output=$(ruff check "$target_path" --output-format=json 2>>"$log_file") || overall_status="fail"
    echo "$ruff_output" >> "$log_file"

    lint_errors=$(echo "$ruff_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if not isinstance(data, list) or any(not isinstance(d, dict) for d in data):
    raise ValueError('Expected Ruff finding list')
errors = [d for d in data if d.get('fix') is None]
print(len(errors))
" 2>>"$log_file") || { lint_errors=1; overall_status="fail"; }
    lint_fixable=$(echo "$ruff_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
fixable = [d for d in data if d.get('fix') is not None]
print(len(fixable))
" 2>>"$log_file") || { lint_fixable=0; overall_status="fail"; }
    lint_warnings=$lint_fixable

    # Format check
    echo "" >> "$log_file"
    echo "=== RUFF FORMAT CHECK ===" >> "$log_file"
    format_output=$(ruff format --check "$target_path" 2>&1) || overall_status="fail"
    echo "$format_output" >> "$log_file"
    format_issues=$(echo "$format_output" | grep -c "Would reformat" 2>/dev/null) || format_issues=0
    lint_warnings=$((lint_warnings + format_issues))
    if [[ ! "$format_output" =~ ^[0-9]+\ files?\ already\ formatted$ ]]; then
        lint_errors=$((lint_errors + 1))
        overall_status="fail"
    fi

    if [[ "$lint_errors" -gt 0 || "$lint_fixable" -gt 0 ]]; then
        overall_status="fail"
    fi

elif $run_lint && $is_python; then
    echo "Ruff is required for Python lint and format checks." >> "$log_file"
    lint_errors=$((lint_errors + 1))
    overall_status="fail"
fi

if $run_lint && $is_js; then
    # Let the installed ESLint version discover and validate its own config.
    eslint_bin=$(find_js_tool eslint) || eslint_bin=""
    if [[ -n "$eslint_bin" ]]; then
        record_check "eslint"
        echo "=== ESLINT ===" >> "$log_file"
        eslint_output=$(cd "$target_dir" && "$eslint_bin" "$target_path" --format json) 2>>"$log_file" || overall_status="fail"
        echo "$eslint_output" >> "$log_file"
        eslint_errors=$(echo "$eslint_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if not isinstance(data, list):
    raise ValueError('Expected ESLint result list')
counts = [d['errorCount'] for d in data]
if any(type(n) is not int or n < 0 for n in counts):
    raise ValueError('Invalid ESLint error count')
print(sum(counts))
" 2>>"$log_file") || { eslint_errors=1; overall_status="fail"; }
        eslint_warnings=$(echo "$eslint_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
counts = [d['warningCount'] for d in data]
if any(type(n) is not int or n < 0 for n in counts):
    raise ValueError('Invalid ESLint warning count')
print(sum(counts))
" 2>>"$log_file") || { eslint_warnings=0; overall_status="fail"; }
        lint_errors=$((lint_errors + eslint_errors))
        lint_warnings=$((lint_warnings + eslint_warnings))
        if [[ "$lint_errors" -gt 0 ]]; then
            overall_status="fail"
        fi
    else
        echo "ESLint and a project config are required for JS/TS lint checks." >> "$log_file"
        lint_errors=$((lint_errors + 1))
        overall_status="fail"
    fi
fi

# ── Bandit (security) ───────────────────────────────────
if $run_security && $is_python && command -v bandit &>/dev/null; then
    record_check "bandit"
    echo "" >> "$log_file"
    echo "=== BANDIT SECURITY SCAN ===" >> "$log_file"

    bandit_output=$(bandit -r "$target_path" -f json --exclude '*/.venv/*,*/node_modules/*,*/__pycache__/*' 2>>"$log_file") || overall_status="fail"
    echo "$bandit_output" >> "$log_file"

    security_issues=$(echo "$bandit_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if data.get('errors'):
    raise ValueError('Bandit left files unscanned')
results = data['results']
if not isinstance(results, list) or any(not isinstance(r, dict) for r in results):
    raise ValueError('Expected Bandit finding list')
print(len(results))
" 2>>"$log_file") || { security_issues=1; overall_status="fail"; }

    # Extract high/critical severity issues
    critical_list=$(echo "$bandit_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
results = data['results']
critical = [f\"{r['test_id']}:{r['test_name']}\" for r in results if r.get('issue_severity') in ('HIGH', 'MEDIUM')]
for c in critical[:5]:
    print(c)
" 2>>"$log_file") || { critical_list=""; overall_status="fail"; }

    if [[ -n "$critical_list" ]]; then
        while IFS= read -r line; do
            security_critical+=("$line")
        done <<< "$critical_list"
    fi

    if [[ "$security_issues" -gt 0 ]]; then
        overall_status="fail"
    fi
elif $run_security && $is_python; then
    echo "Bandit is required for Python security checks." >> "$log_file"
    security_issues=$((security_issues + 1))
    overall_status="fail"
fi

# ── Pyright (type checking) ─────────────────────────────
if $run_types && $is_python && command -v pyright &>/dev/null; then
    record_check "pyright"
    echo "" >> "$log_file"
    echo "=== PYRIGHT TYPE CHECK ===" >> "$log_file"

    pyright_output=$(pyright "$target_path" --outputjson 2>>"$log_file") || overall_status="fail"
    echo "$pyright_output" >> "$log_file"

    type_errors=$(echo "$pyright_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
count = data['summary']['errorCount']
if type(count) is not int or count < 0:
    raise ValueError('Invalid Pyright error count')
print(count)
" 2>>"$log_file") || { type_errors=1; overall_status="fail"; }

    if [[ "$type_errors" -gt 0 ]]; then
        overall_status="fail"
    fi
elif $run_types && $is_python; then
    echo "Pyright is required for Python type checks." >> "$log_file"
    type_errors=$((type_errors + 1))
    overall_status="fail"
fi

# ── TypeScript type checking ────────────────────────────
if $run_types && $is_typescript; then
    tsconfig_path=""
    tsconfig_dir="$target_dir"
    while [[ -n "$tsconfig_dir" ]]; do
        if [[ -f "$tsconfig_dir/tsconfig.json" ]]; then
            tsconfig_path="$tsconfig_dir/tsconfig.json"
            break
        fi
        [[ "$tsconfig_dir" != / ]] || break
        tsconfig_dir=$(dirname "$tsconfig_dir")
    done
    tsc_bin=$(find_js_tool tsc) || tsc_bin=""
    if [[ -n "$tsconfig_path" && -n "$tsc_bin" ]]; then
        record_check "tsc --noEmit"
        echo "" >> "$log_file"
        echo "=== TSC TYPE CHECK ===" >> "$log_file"
        # Resolve JSONC/extends through tsc, then check every referenced config.
        # Even --noEmit can write incremental metadata; keep that in a temp dir.
        if tsc_output=$(cd "$target_dir" && python3 - "$tsc_bin" "$tsconfig_path" 2>&1 <<'PY'
import json
from pathlib import Path
import subprocess
import sys
import tempfile

tsc, root_config = sys.argv[1:]
checked = set()
active = set()

def invoke(*args):
    result = subprocess.run([tsc, *args], capture_output=True, text=True)
    if result.returncode or result.stderr:
        raise ValueError(result.stdout + result.stderr or 'TypeScript failed without diagnostics')
    return result.stdout

def check(config, scratch):
    config = config.resolve()
    if config in active:
        raise ValueError(f'Cyclic TypeScript project reference: {config}')
    if config in checked:
        return
    active.add(config)
    data = json.loads(invoke('--showConfig', '--pretty', 'false', '-p', str(config)))
    references = data.get('references', [])
    if not isinstance(references, list):
        raise ValueError('Expected TypeScript project reference list')
    for reference in references:
        path = reference['path']
        if not isinstance(path, str) or not path:
            raise ValueError('Invalid TypeScript project reference path')
        child = config.parent / path
        if not path.endswith('.json'):
            child /= 'tsconfig.json'
        check(child, scratch)
    output = invoke('--noEmit', '--pretty', 'false', '--incremental',
                    '--tsBuildInfoFile', str(scratch / f'{len(checked)}.tsbuildinfo'),
                    '-p', str(config))
    if output:
        raise ValueError(output)
    active.remove(config)
    checked.add(config)

with tempfile.TemporaryDirectory(prefix='dev-quality-tsc-') as scratch:
    check(Path(root_config), Path(scratch))
PY
        ); then
            tsc_exit=0
        else
            tsc_exit=$?
        fi
        echo "$tsc_output" >> "$log_file"
        tsc_errors=$(echo "$tsc_output" | grep -cE 'error TS[0-9]+' 2>/dev/null) || tsc_errors=0
        if [[ "$tsc_exit" -ne 0 || -n "$tsc_output" ]]; then
            overall_status="fail"
            if [[ "$tsc_errors" -eq 0 ]]; then
                tsc_errors=1
            fi
        fi
        type_errors=$((type_errors + tsc_errors))
        if [[ "$type_errors" -gt 0 ]]; then
            overall_status="fail"
        fi
    else
        echo "TypeScript and tsconfig.json are required for TS type checks." >> "$log_file"
        type_errors=$((type_errors + 1))
        overall_status="fail"
    fi
fi

# ── Build JSON summary ──────────────────────────────────
critical_json="[]"
if [[ ${#security_critical[@]} -gt 0 ]]; then
    critical_json="["
    first=true
    for item in "${security_critical[@]}"; do
        escaped=$(json_escape "$item")
        if $first; then
            critical_json+="\"${escaped}\""
            first=false
        else
            critical_json+=",\"${escaped}\""
        fi
    done
    critical_json+="]"
fi

checks_run_json="["
first=true
if [[ "$checks_run_count" -gt 0 ]]; then
    for check in "${checks_run[@]}"; do
        escaped=$(json_escape "$check")
        if $first; then
            checks_run_json+="\"${escaped}\""
            first=false
        else
            checks_run_json+=",\"${escaped}\""
        fi
    done
fi
checks_run_json+="]"
if [[ "$checks_run_count" -eq 0 ]]; then
    overall_status="fail"
fi

escaped_log_file=$(json_escape "$log_file")
cat <<EOJSON
{"status":"${overall_status}","checks_run":${checks_run_json},"lint":{"errors":${lint_errors},"warnings":${lint_warnings},"fixable":${lint_fixable}},"security":{"issues":${security_issues},"critical":${critical_json}},"types":{"errors":${type_errors}},"log":"${escaped_log_file}"}
EOJSON

if [[ "$overall_status" == "fail" ]]; then
    exit 1
fi
exit 0
