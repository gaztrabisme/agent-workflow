# Distillation report: courses 1560 and 5642 U3

## Files changed

- `SKILL.md` — added the 1560 and 5642 course provenance, updated the light and graphic-color flow, added the semantic-differential review path and T10–T12, and clarified the two wheel models while preserving the existing license line.
- `NOTICE.md` — named both new course exports and retained the private-use and redistribution notice.
- `EVOLUTION.md` — recorded Evolution 3 with verdict PENDING, anchored course claims, the crosswalk findings and validation results.
- `references/method/light.md` — added the 1560 exposure, source-quality, ambient-light, bounce and material workflow, with a derived order and scene examples.
- `references/method/functional-color.md` — added the 5642 three-function classification, nine variables, color-family associations and semantic-differential use, with cultural-context limits.
- `references/method/value-plan.md` — added the exposure-range decision and its relation to the value hierarchy.
- `references/method/temperature-saturation.md` — added the 1560 cool-ambient and warm-lamp night-scene example.
- `references/method/photoshop-techniques.md` — added a tool-neutral digital-painting light-pass equivalent.
- `references/method/mistakes-checklist.md` — added T10 semantic target fit, T11 audience agreement and T12 variant distinction with pass conditions.
- `references/method/measurement.md` — added the seven-point profile measures and brief-defined thresholds for T10–T12.
- `references/method/science-crosswalk.md` — documented the RYB versus RGB/CMY wheel distinction, temperature and saturation context, historical numeric models, and contextual limits on color-family meanings.
- `references/method/coverage.md` — listed all eight lesson files not cited by a method digest, with reasons.

No exported course file or file under `references/color-science/` was changed. The removed 1560 U3 L08 lesson remains excluded as blocked.

## Acceptance output

- `python3 scripts/check_refs.py --sources 'references/course*/*.md'` — exit 0; `17 files, 414 anchors cited, 616 known, 0 problem(s)`.
- `python3 /Users/GaryT/Documents/Work/lab/design-programme/checks/check_coverage.py .` — exit 0; `52 lessons, 52 covered (44 cited)`.
- `! grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|frontend-design|Read tool|Bash tool|subagent_type' SKILL.md references/method` — exit 0; no matches.
- Skill size — `SKILL.md` is 139 lines; its description is 701 characters.
- `npx -y skills-ref@latest validate .` — not run here; the coordinator has network access and runs it separately.
- Requested commit — not created: the workspace permission profile allows reading `.git` but denies writing `.git/index.lock`; the changes remain in the working tree.

## Open questions

- The coordinator's `skills-ref` validation is still pending.
- Creating the requested local commit requires write access to this repository's `.git` directory.
- Evolution 3 remains PENDING until the merged method is used on real design work.
