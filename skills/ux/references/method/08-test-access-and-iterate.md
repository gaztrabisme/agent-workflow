# Stage 8: Test, access, localize, and iterate

## Reader and scope

**Reader:** a team checking that the experience works for people and is ready for its next handoff. **Scope:** test the task and content with users, check access and localization needs, use evidence to decide what to change, and report what remains uncertain.

## Source lessons

- [798 · U2 · L05 — What the hell is UX Writing?](../course-798/U02-L05-what-the-hell-is-ux-writing.md)
- [798 · U4 · L13 — Accessibility, diversity and localization](../course-798/U04-L13-accessibility-diversity-and-localization.md)
- [1490 · U3 · L11 — Contextual research and testing](../course-1490/U03-L11-other-qualitative-techniques-contextual-research-and-testing.md)
- [1490 · U7 · L30 — Prototyping and testing 2](../course-1490/U07-L30-prototyping-and-testing-2.md)
- [1490 · U7 unit](../course-1490/U07-unit.md)

## First idea, stated as the rule

- Prepare a small set of realistic tasks, pilot the complete test, and explain that the interface is being evaluated rather than the participant. Invite people to think aloud and stay neutral. (1490 · U3 · L11 · 06:26–09:33; 1490 · U3 · L11 · 10:48–13:02; 1490 · U7 · L30 · 00:00–03:44)
- Observe task behavior, including where a participant gets stuck or cannot complete a task; the teacher treats Lola’s inability to find progress information as useful feedback. (1490 · U7 · L30 · 06:50–10:35)
- Give observed behavior more weight than participants' opinions of a prototype or app. (1490 · U7 · L30 · 00:00–03:44)
- Put screen-reader labels and help before the action that needs them. For a form, the course's example order is label, help text, then field. (798 · U4 · L13 · 04:28–08:09)
- Give meaningful images alternative text, make icons' destinations understandable, and use live text rather than baking words into images. (798 · U4 · L13 · 08:09–11:23)
- Localize for the language and culture, then give localization partners the flow, screen context, style notes, research, glossary, and alternatives they need. (798 · U4 · L13 · 11:23–13:18; 798 · U4 · L13 · 13:18–14:20; 798 · U4 · L13 · 14:20–16:09)
- Compare quantitative results with qualitative research when assessing content changes; clicks can show which version performed differently, while qualitative research can help explain why. (798 · U2 · L05 · 06:04–08:15; 798 · U2 · L06 · 01:30–03:08)

## Render, check, and review

**Editable medium:** use HTML for composed screens and interactive prototypes, SVG for maps and diagrams, and embed SVG in HTML as needed. Follow the project's delivery format and domain conventions when they require another format. (derived from owner decision 7) The course examples use wireframes (1490 · U7 · L25 · 00:00–01:00; 1490 · U7 · L25 · 01:00–02:58) and paper prototypes linked by hotspots in POP (1490 · U7 · L29 · 00:00–01:15).

1. Add `data-rk-stage` to identify each screen or flow stage in HTML/SVG. Use semantic live text, labels, and controls in interactive prototypes.
2. Run render-kit code checks first. Fix every `fail`; read each `skipped` or `incomplete` reason and record why it does not apply. Checks include overflow, text collisions, font fallback, contrast, resource loading, and accessibility when present.
3. Render the artifact and prepare a review brief from the specific questions in [review-checklist.md](review-checklist.md). Give the images and brief to a fresh-context reviewer who did not make the artifact.
4. Verify review answers; fix each `no` and render again. If no reviewer can see the images, report the vision checks as **not judged**, never as passed.
5. Report measured, vision-judged, not-judged, and skipped checks separately.

## Failures

**Problem: calling positive comments proof that a task works.**
- **The failure:** a participant says an app is easy and intuitive but gets lost repeatedly while using it. (1490 · U7 · L30 · 00:00–03:44)
- **The fix:** record task success, hesitation, wrong turns, and comments separately; use the evidence to make a change and test again. (1490 · U3 · L11 · 09:33–10:48; 1490 · U7 · L30 · 00:00–03:44)

**Problem: treating localization as a string-only handoff.**
- **The failure:** without screen and flow context, the partner cannot tell what a phrase means or how it needs to fit. (798 · U4 · L13 · 11:23–13:18; 798 · U4 · L13 · 14:20–16:09)
- **The fix:** share prior steps, the next action, and the experience flow so the partner can see the surrounding screen context. (798 · U4 · L13 · 11:23–13:18) Include contextual screenshots, style notes, research, shared terms, and earlier microcopy versions as appropriate. (798 · U4 · L13 · 13:18–14:20; 798 · U4 · L13 · 14:20–16:09)

## Check before moving on

**T9 — User test:** the pilot uses the real task and prototype; outcomes and observed behavior are recorded for each participant; the facilitator remains neutral.

**T10 — Accessibility and localization:** required labels and help are available in an understandable order; meaningful images and icons have useful names; text is live; localization receives flow, context, style, and terminology.

**T11 — Learning and iteration:** the team compares the result with a stated outcome, records what was measured and what needs judgment, and names the next change or test. If the target or evidence is missing, report the result as inconclusive.

**Practice the teacher sets:** prepare and pilot a usability test, test a prototype with users, record what happened, and iterate. See [1490 · U7 unit](../course-1490/U07-unit.md).

## Freshness and ownership

**Maintainer:** ux skill owner  
**Last reviewed:** 2026-10-02  
**Review due:** 2027-10-02 or when either source lesson changes
