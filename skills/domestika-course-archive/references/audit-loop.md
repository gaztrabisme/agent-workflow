# Audit loop: reading copies without owner review

Reader: the coordinator producing reading copies when the owner will not review each lesson. The audit loop replaces that review: independent agents compare every lesson with its source and the writer fixes what they find, for at most three rounds.

Terms used below:
- **Lane**: one model family used for subagents (for example Claude agents, Codex, GLM). Two lanes see different things, so the auditor is never the writer's lane.
- **Finding**: one problem an auditor reports, with a kind, a severity and a verdict (`open`, `fixed` or `rejected`).
- **Blocked**: a lesson that still has an open High or Medium finding after round 3.

## Roles

| Step | Who | Writes |
|---|---|---|
| Write | writer lane, per `reading-copy.md` | `lesson.md`; `check` passes |
| Text audit | GLM, one run per unit | `text-audit.json`: prose against the native transcript, section by section |
| Vision audit | a lane other than the writer's | `audit.json`: keeps or rejects each text finding, opens every referenced frame once, looks for missing figures |
| Fix | the writer's lane | edits `lesson.md`, appends the round to `fix-notes.md` |
| Re-audit | the same auditor lane | a new `audit.json` for the next round |

## Finding kinds and severity

Kinds: `omission` (said, missing), `addition` (written, not said; Key points (derived) is exempt), `mistranslation`, `plug`, `figure-text` (an `On screen:` or `Shows:` line), `missing-figure`, `density` (near-duplicate figures), `promo` (a promotional screen kept as a figure).

- **High**: meaning is changed or lost (a reversed statement, a wrong number, a missing step of a procedure).
- **Medium**: a point or example is missing or wrong; on-screen text or a `Shows:` line is wrong; a figure is missing where a spoken cue points at the image, or the prose cannot be followed without it.
- **Low**: wording and caption polish; every other missing figure (interface dialogs, in-between states of a demo that differ only in progress); a close-up unless the prose refers to a detail unreadable in the full view.

Style, shortened filler and changed sentence order are not findings. Song lyrics shown on screen are never reproduced; a caption naming the song is correct.

## Rounds

- A lesson **passes** when no High or Medium finding is open and `check` exits 0.
- From round 2 the auditor carries every finding forward and re-audits only the sections the fixes touched. It may lower a severity, and raises one only to High when meaning is lost. A new finding is Medium or High only if it sits in text the fix changed; otherwise it is Low. It marks a finding `fixed` only after checking the text or frame itself; `fix-notes.md` is a claim.
- Low findings are optional for the writer.
- After round 3 an open High or Medium finding makes the lesson **blocked**, with `blocked_reason` naming the findings.

## What a blocked lesson may still be used for

When every open High or Medium finding is of kind `figure-text`, `missing-figure`, `density` or `promo`, the prose passed and the lesson stays a source for distillation: cite its prose, never its open captions, and list the open caption findings beside the lesson. When any open finding is about the prose (`omission`, `addition`, `mistranslation`, or a `plug` not tied to a figure), leave the lesson out of distillation. Report every blocked lesson at close either way.

## Running the loop

Drive it from disk, not from memory: for each lesson, the next action follows from which files exist and their timestamps.

- Re-audit when `lesson.md` is newer than `audit.json`. A fix that only disputes findings must still re-save `lesson.md`, or the lesson never returns to the auditor.
- Name each job by course, lesson, round and lane (`fx-<course>-L<nn>-r<round>-<lane>`). When a lesson changes writer lane, a name without the lane collides with the earlier writer's job and the new fix is never issued.
- Flag a lesson as stuck when its audit is over an hour old and `fix-notes.md` has nothing newer: the fixer was lost.
- Expect three rounds per lesson, not one. Budget about three audit jobs and two fix jobs per lesson, and put the bulk on the lanes with the most quota; a subscription lane with a short usage window will run out partway through a course.

Where the loop runs into cost, it is usually captions. Most findings are `figure-text`: a missing translation of a quoted phrase, a shortened label, changed capitalisation, a missing `[rest omitted]`. Writers who follow the `Frame captions` rules in `reading-copy.md` to the letter avoid most rounds.

A working set of briefs and loop scripts (state from disk, queue, blocked list) from a two-course run is kept in the design-programme lab, `briefs/run-2/`.
