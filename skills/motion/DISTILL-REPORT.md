# Motion skill distillation report

**Date:** 2026-10-02

## Written

- `SKILL.md`: six-stage operating method, scaling notes, scene-engine execution and render/check loop, core gates, anti-patterns and owner-controlled handoffs.
- `references/method/`: one digest for each stage, a ten-test review checklist, a measurement table for every test, and lesson coverage with reasons for unused lessons.
- `NOTICE.md`: private paid-course notice naming all four courses.
- `EVOLUTION.md`: Evolution 1 birth entry, classified as distilled and left PENDING.
- `scripts/check_refs.py`: decoded percent-encoded local links and excluded paid course corpora from the generic “named package files” check. Course anchors remain checked by the reference checker; unused lesson coverage is checked separately.

## Acceptance output

- `python3 scripts/check_refs.py . --sources 'references/course*/*.md'` — **exit 0**; 1145 anchors cited, 488 known, 0 problems, 0 warnings.
- `python3 /Users/GaryT/Documents/Work/lab/design-programme/checks/check_coverage.py .` — **exit 0**; 73 lessons, 73 covered (47 cited).
- `! grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' SKILL.md references/method` — **exit 0**; no matches.
- `npx -y skills-ref@latest validate .` — **blocked, exit 1**; npm could not resolve `registry.npmjs.org` (`ENOTFOUND`). The official validator has not passed.
- Offline fallback `python3 scripts/check_refs.py . --no-anchor-check --format` — **exit 0**. This confirms offline package format only; the separate acceptance command above passed the source-anchor check.
- Commit — **blocked by workspace permissions**. `git add` could not create `.git/index.lock` (`Operation not permitted`), so no files were staged or committed. No lock file remains. The requested commit message is `motion: method, review checklist, measurement, SKILL.md` with the specified co-author trailer.

## Open questions and follow-up

- No fresh-context real-use dogfood or independent claim audit was run during this package build. The course-derived method therefore remains **PENDING**; the validator and dogfood follow-up are recorded in `EVOLUTION.md`.
- Recheck the official `skills-ref` validator when npm registry access is available.
- Test the stage order on a non-narrative interface animation and on an animated infographic with more demanding data mappings before settling the evolution verdict.
