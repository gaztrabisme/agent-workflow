# Photo skill distillation report

Date: 2026-10-02

## Written

- Seven anchored stage digests in references/method/: brief/session, capture/composition, keeper selection, RAW/base correction, retouch/compositing, grading/batching, and delivery/review.
- A twelve-test review checklist and one measurement row per test, with the course's procedure, a tool-independent check, and the origin of each threshold.
- A coverage table for all 97 exported lessons; 32 lesson prefixes are not cited by a method digest and have a four-or-more-word reason.
- SKILL.md, the proprietary private-course NOTICE.md, Evolution 1 with verdict PENDING, a field-rules reference carrying the former batch workflow, and a reusable session ledger.
- scripts/check_refs.py now scopes link/source checks to authored skill material and public CLI entry points, decodes percent-encoded local links, and treats course exports and imported helper modules as indexed source or implementation dependencies. Course reading copies and notes were not edited.

## Acceptance results

Ran from this repository:

| Command | Result |
|---|---|
| python3 scripts/check_refs.py . --sources 'references/course*/*.md' | Exit 0 — 13 authored files scanned, 386 anchors cited, 610 known anchors, 0 problems, 0 warnings. |
| python3 /Users/GaryT/Documents/Work/lab/design-programme/checks/check_coverage.py . | Exit 0 — 97 lessons, 97 covered (68 cited). |
| ! grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' SKILL.md references/method | Exit 0 — no matches. |
| python3 scripts/check_refs.py . --no-anchor-check --format | Exit 0 — offline format fallback passed; source anchors were explicitly skipped in this fallback. |
| SKILL.md size inspection | 113 lines; description 563 characters. |

The coordinator validator command npx -y skills-ref@latest validate . exited 1 because npm could not resolve registry.npmjs.org (ENOTFOUND). The official format validator did not pass; the offline fallback passed.

The requested commit was not created: the workspace permits reading `.git` but not writing to it, so `git add` was refused while creating `.git/index.lock`. The authored files remain in the working tree and were not committed.

## Review and open items

- The course notes and lesson indexes grounded the synthesis; exact anchor availability was checked against the reading copies. This run did not re-read every lesson from beginning to end or obtain an independent source-claim audit.
- A fresh-context reviewer and a real photo artifact were not available under the instruction not to spawn subagents. No vision result or dogfood pass is claimed. EVOLUTION.md remains PENDING.
- Before treating the skill as settled, obtain an independent claim/audience review, run it on at least two independent real photo tasks, and rerun skills-ref validation when npm access is available.
- Check the destination's current crop/profile/dimension requirements for each real delivery; course 227's two Story-crop labels conflict, so this skill sends crop decisions to the requested destination specification.
