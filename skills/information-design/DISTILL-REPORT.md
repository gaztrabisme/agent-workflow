# Information-design distillation report

**Status:** FAIL for complete validation and commit. The package and requested acceptance checks are complete; renderer checks, fresh-context vision review, the external skill validator and the requested commit could not finish in this environment.

## Written

- `SKILL.md`: six-stage workflow, scale notes, output and render loop, owner-approved gates, anti-patterns, artifact-based handoffs, and links to every method digest and chart template. It is 118 lines. The description is under the 1,024-character limit.
- `references/method/`: six anchored course digests (`brief`, `source-and-data`, `story-and-structure`, `chart-and-encoding`, `annotation-and-narrative`, `render-and-review`), ten-test `review-checklist.md`, per-test `measurement.md`, and lesson-by-lesson `coverage.md`.
- `templates/`: an index and 11 render-kit-marked SVG templates. Four drilling examples are labelled derived. The radial path declares a manual scale-review exception.
- `NOTICE.md` names the four private paid courses. `EVOLUTION.md` records Evolution 1 as distilled and PENDING. `scripts/check_refs.py` now treats course reading copies as anchor evidence, not as hundreds of operating-reference links.

## Acceptance and validation

- `python3 scripts/check_refs.py . --sources 'references/course*/*.md'` — **PASS**, exit 0; 10 operating files scanned, 262 anchors cited, 387 known, 0 problems and 0 warnings.
- `python3 /Users/GaryT/Documents/Work/lab/design-programme/checks/check_coverage.py .` — **PASS**, exit 0; 63 lessons, 63 covered (49 cited).
- Required forbidden-string `grep` negation — **PASS**, exit 0; no matches.
- Inline SVG/XML and data-to-mark review — **PASS**, exit 0; all 11 templates parsed and 83 mapped-mark or declared-exception checks passed. The radial mapping requires the manual review recorded in its markup and index.
- Render-kit `bin/rk check` — **BLOCKED**; each attempted template stopped with `listen EPERM: operation not permitted 127.0.0.1`. The renderer could not start its local listener, so no rendered output or render-kit code-check result is claimed.
- `npx -y skills-ref@latest validate .` — **BLOCKED**, exit 1; npm could not resolve `registry.npmjs.org` (`ENOTFOUND`). The coordinator's validator has therefore not supplied a result.
- Fresh-context vision review — **NOT JUDGED**. The session instruction forbids spawning subagents, and no independent image reviewer was available.
- Requested commit — **BLOCKED**. `git add` failed with `fatal: Unable to create '.git/index.lock': Operation not permitted`. The workspace exposes `.git` as read-only. No commit was created and nothing was pushed.

## Open work

1. Re-run render-kit rendering and checks when local listener access is available; resolve any reported failures and inspect the actual target-size output.
2. Re-run `npx -y skills-ref@latest validate .` when npm registry access is available.
3. Have a fresh-context reviewer judge T1–T10 on rendered charts, then complete two independent real-use dogfood runs. Keep `EVOLUTION.md` PENDING until that evidence exists.
4. Confirm the skill-chosen numeric defaults against each future project's domain requirements; the courses generally teach procedures and examples rather than universal thresholds.
5. Create the requested commit once a workspace with writable Git metadata is available.

**Requested commit message:** `information-design: method, review checklist, measurement, SKILL.md`

**Requested trailer:** `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
