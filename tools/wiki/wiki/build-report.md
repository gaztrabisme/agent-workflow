# Build report

Owner: repository owner. Reviewed: 2026-10-27.

Verdict: **PASS against the owner-approved rule changes and corpus acceptance**.
Independent review remains deferred, as recorded below.

## Changes

Pages below any directory named `inputs/` or `raw/`, at any depth within the
wiki, are immutable source copies. They are exempt from broken-link,
undated-page and unreachable findings. Lint makes no changes to them.

`unreachable` replaces `not-in-index`. Starting at index.md, lint follows
Markdown links transitively with no depth limit, tracking visited files to
terminate cycles. At every step it selects the existing page-relative target
before the repo-root target. Linked external Markdown and exempt pages can be
intermediates. Index, log pages, runs/ and goals/ remain exempt from unreachable.
The CLI and MCP share this implementation. README and tests reflect both rules.

## Verification

| Gate | Observed result |
| --- | --- |
| `uv run pytest -q` | PASS: 65 cases in 1.95 seconds |
| `ruff check src tests scripts` | PASS |
| `git diff --check -- .` | PASS |
| Exact uv console lint, text and JSON | PASS: both exit 0, no stderr |
| Linkcruiser hash check | PASS: all 284 file paths and SHA-256 values match before/after |
| Corpus acceptance | PASS: required cap/run-report findings present; broken-link count 0 (limit 3) |
| Independent review | DEFERRED: automatic approval review rejected the reviewer-agent tool as unrecognized |

The new tests were run before implementation: 12 failed and 30 passed, exposing
the missing rule name and source-copy exemptions. The complete suite passed
after implementation. No real wiki edits, project commits or pushes were made.

## Linkcruiser per-rule counts

The verification script executed this command, then its `--json` variant:

```sh
uv run wiki lint ~/Documents/Work/projects/Linkcruiser/wiki
```

| Rule | Findings |
| --- | ---: |
| `index-over-cap` | 1 |
| `log-over-cap` | 1 |
| `unreachable` | 31 |
| `index-dead-entry` | 0 |
| `broken-link` | 0 |
| `run-report-in-index` | 1 |
| `undated-page` | 22 |

The previous 135 broken links were all in source copies, now excluded under the
owner's explicit decision. Reachability reports 31 pages needing a path from
index.md. The command is report-only and returns 0 with these findings.

## First 20 output lines

```text
Wiki: /Users/GaryT/Documents/Work/projects/Linkcruiser/wiki

index-over-cap (1):
  index.md: 237 lines exceeds cap 200

log-over-cap (1):
  log.md: 2531 lines exceeds cap 400

run-report-in-index (1):
  index.md: 19 run report links; at most one roll-up allowed

undated-page (22):
  accepted-2026-10-20/receipt.md: no date in filename or first 15 lines
  accepted-2026-10-23/receipt.md: no date in filename or first 15 lines
  accepted-context-2026-10-19/receipt.md: no date in filename or first 15 lines
  acquisition-2026-10-20/receipt.md: no date in filename or first 15 lines
  cell-2026-09-05-jobs/persona-recruiter.md: no date in filename or first 15 lines
  cell-2026-09-05-jobs/review-primitives-legacy.md: no date in filename or first 15 lines
  cv-cohort-2026-10-22/maturity.md: no date in filename or first 15 lines
  cv-cohort-2026-10-22/review.md: no date in filename or first 15 lines
```

## Evidence and rerun

- [Full lint output](linkcruiser-lint.txt).
- [Structured findings](linkcruiser-findings.json).
- [Before/after SHA-256 snapshots and command results](linkcruiser-acceptance.json).
- [Exact collected test list](test-list.txt): 65 cases.

```sh
uv run pytest -q
ruff check src tests scripts
python3 scripts/verify_linkcruiser.py ~/Documents/Work/projects/Linkcruiser/wiki
```

The verifier snapshots all files, runs the console commands, and compares file
paths and hashes. It writes evidence only to this tool's wiki/ folder. The corpus
is read without writes, including all source copies.

## Test coverage

- All seven lint rules: positive/negative cases, cap boundaries and overrides.
- Source-copy exclusions: inputs/, raw/, both at nested depths; similarly named
  myinputs/ and rawdata/ remain checked. Copy bytes remain unchanged.
- Reachability: direct links and missing paths, depth 1/3/40, reachable cycles,
  disconnected cycles, links through exempt pages, external intermediates,
  repo-root fallback, and precedence when both targets exist. The retired
  not-in-index finding is absent.
- Existing log tests: both chronological directions, title placement, worktree
  routing, date ranges, whole-entry rotation, pointers, idempotence, dry runs,
  merge ordering/deletion and data-preservation cases.
- Existing interface tests: JSON/strict exits, search stub, MCP import,
  four-tool discovery and an in-memory shared-lint call.

## LOAD use

| Requested source | Used? | Application |
| --- | --- | --- |
| skills/core/references/wiki-protocol.md | YES, loaded in the initial build | Index summaries, append-only session log, active-work, decisions and source boundaries |
| knowledge-base/knowledge_base/server.py lines 1–60 | YES, loaded in the initial build | Deferred imports, FastMCP instance, requested decorators and stdio mcp.run() style |
| Books | NO | None relevant to this mechanical build |

## Previous baseline and review

The first build reported FAIL because the original rule included source copies
and the environment could not complete the plain uv commands. The owner
confirmed the initial tests and hash check, then explicitly approved source-copy
exclusions and transitive reachability. Plain uv tests and corpus lint now run
successfully; the old scope and environment blockers no longer describe the
current result.

The requested functional gates above passed. Independent review remains deferred:
automatic approval review rejected the reviewer-agent launch because it did not
recognize the tool. Self-inspection and passing tests are not counted as an
independent review. Self-inspection checked traversal direction, cycles,
resolution precedence and source-copy exclusions against the regression cases.
