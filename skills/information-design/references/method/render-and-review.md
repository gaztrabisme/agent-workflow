# Render and review: check the artifact at its real size

## Reader and scope

**Reader:** a designer finishing an HTML/SVG data graphic. **Scope:** render the editable artifact, run exact code checks, get a fresh-context vision review, fix issues and export the needed formats. This stage operationalizes the owner's render-kit contract; it is not taught by the courses.

**Source lessons:** [course 2495 · U4 L16](../course-2495/U04-L16-always-keeping-in-mind-the-readers-legends-and-feedback-2.md) and [L17](../course-2495/U04-L17-finishing-the-job.md); [course 4217 · U4 L18](../course-4217/U04-L18-the-legend-and-the-text-2.md) and [L19](../course-4217/U04-L19-final-details-mobile-version-and-export.md); [course 3069 · U4 L13](../course-3069/U04-L13-feedback-and-final-edits.md) and [L14](../course-3069/U04-L14-sharing-your-work.md); [course 3601 · U4 L15](../course-3601/U04-L15-spelling-it-out-2.md).

## Render, run code checks, then review visually

1. Keep a reproducible source dataset and a clear mapping of fields to marks. Put axes, labels and SVG marks in editable HTML/SVG, not a flattened image. (derived execution from 3601 · U3 · L10 · 04:30–05:52; 3601 · U3 · L10 · 05:52–07:27; 3601 · U3 · L10 · 07:27–08:56; 3601 · U3 · L10 · 08:56–10:52; 3601 · U3 · L10 · 10:52–14:05; owner decision 7)
2. Add the render-kit markup: `data-rk-stage` and `data-rk-focal`; chart root `data-rk-chart` with scale type, domain and range; and marks with `data-rk-mark` plus data values. Declare intentional overlap or truncation. (render-kit `AGENTS.md`; owner decision 4)
3. Run `bin/rk check` before vision review. Address resource loading, console errors, font fallback, overflow, text collisions, contrast, colour-vision deficiency, data fidelity, accessibility, value and chroma checks, and PDF fonts when applicable. Render again after each fix. A skipped or incomplete check is not a pass. (render-kit `AGENTS.md`; owner decision 4)
4. Prepare a specific review brief from [review-checklist.md](review-checklist.md), with rendered images and questions. A reviewer who did not make the artifact and can see the images answers; verify those answers with the kit. If such a reviewer is unavailable, report vision checks as not judged. (owner decision 4; render-kit `AGENTS.md`)
5. Review at expected size and medium. Courses inspect close detail and overall composition, print at intended size, view mobile exports on a phone, and ask non-experts to interpret the work. (2495 · U4 · L16 · 10:00–11:15; 2495 · U4 · L17 · 00:00–01:15; 3601 · U4 · L15 · 05:34–06:58; 4217 · U4 · L18 · 08:45–10:39; 4217 · U4 · L19 · 08:45–10:45; 3069 · U4 · L13 · 01:30–02:38)
6. Revise at the stage that owns the failure, then rerun affected code checks and visual questions. Export the format and aspect ratio needed by the actual reader context. (2495 · U4 · L17 · 03:11–04:23; 2495 · U4 · L17 · 04:23–06:49; 2495 · U4 · L17 · 06:49–07:40; 2495 · U4 · L17 · 07:40–09:11; 4217 · U4 · L19 · 00:00–02:15; 4217 · U4 · L19 · 02:15–05:45; 3069 · U4 · L14 · 01:46–02:24; 3069 · U4 · L14 · 02:24–03:07; 3069 · U4 · L14 · 03:07–03:59; 3069 · U4 · L14 · 03:59–04:25)

## Report what was actually checked

For T1–T10 state **measured**, **vision-judged**, **not judged**, or **skipped**. Include measured values, failure and fix, reviewer response, or a reason a check did not apply. Code checks assess rendering and declared data; a reader's response is evidence about understanding, not a substitute for data validation. (owner decision 4)

**Rule synthesized (derived):** finish only after code results have no unresolved applicable failures and each required vision question is either passed by a fresh-context reviewer or reported as not judged. Derived from the owner's code-first/reviewer-second decision and course practices of proofreading, viewing at output size and collecting reader feedback. (derived from owner decision 4; 2495 · U4 · L16 · 10:00–11:15; 3069 · U4 · L13 · 00:00–01:30; 3069 · U4 · L13 · 01:30–02:38)

## Failures

**Problem 1: approving the source instead of the render.** At small sizes, labels and layout can fail even when the editable file contains them. Render at target size and inspect. (4217 · U4 · L19 · 08:45–10:45; 3069 · U4 · L13 · 01:30–02:38)

**Problem 2: treating unavailable review as success.** A check needing another person's eyes is not judged until a fresh reviewer can see the render. (owner decision 4)

## Check before moving on

Pass T8–T10 when all applicable render-kit code checks pass, the intended output sizes/formats are represented, and required vision checks are passed or honestly marked not judged. Return to the stage named by the failure before exporting again.

**Practice the teachers set:** revise after feedback, inspect the intended medium, then prepare the final export. See [course 2495, Unit 4](../course-2495/U04-unit.md), [course 4217, Unit 4](../course-4217/U04-unit.md) and [course 3069, Unit 4](../course-3069/U04-unit.md).

## Freshness and ownership

**Maintainer:** information-design skill owner. **Last reviewed:** 2026-10-02. **Review due:** when render-kit markup/checks or the owner's review decision changes.
