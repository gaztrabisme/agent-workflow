# Work log

## 2026-10-02 — F13 closed

- Grounded: F13 in the motion dogfood report and the existing render-kit contract in `../SPEC.md` → fixed the three observed defects without adding dependencies.
- Added acceptance coverage for heading/question order, tall HTML capture with fixed-height override, and whole-stage value guarding.
- Verified with `npm test` (44 passed) and `./bin/rk selftest` (19 sample expectations passed), using a temporary venv with the optional NumPy and Pillow dependencies. `git diff --check` passed.

## 2026-10-02 — Frontend F2, F4, and F11 closed

- Grounded: frontend findings F2, F4, and F11 in `/Users/GaryT/Documents/Work/lab/design-programme/dogfood/runs-3-5/frontend/report.md` and the linked check evidence → added expected-request matching, visual-check exclusions and horizontal-scroll handling, and labelled multi-input briefs.
- Added regression coverage for exact request URL/status matching, the documented hidden and scrolling patterns, and two labelled states with no PDF.
- Updated the CLI help, `../SPEC.md`, `../AGENTS.md`, and `../FIX-REPORT-dogfood.md`.
- Verified with `npm test` (47 passed) and `./bin/rk selftest` (19 sample expectations passed), using `/tmp/rk-f13-venv/bin` first on `PATH` because the default Python lacks NumPy and Pillow. `git diff --check` passed.
