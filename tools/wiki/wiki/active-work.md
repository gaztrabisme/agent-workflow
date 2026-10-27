# Active work

Owner: repository owner. Reviewed: 2026-10-27.

Implemented the owner-approved source-copy exclusions and transitive
`unreachable` rule. `uv run pytest -q` passes all 65 cases; Ruff passes.

Linkcruiser acceptance: PASS against the revised rules. The exact uv lint command
reports zero broken links and 31 unreachable pages. All 284 file paths and
SHA-256 values match before/after the command. The report includes all seven
rule counts and the first 20 output lines.

Next: use the findings to maintain the wiki; no real wiki edits were made.
Independent review remains deferred because automatic approval review rejected
the reviewer-agent tool. See [build report](build-report.md).
