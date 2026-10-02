---
name: ux
description: "An evidence-led method for scoping digital products, mapping user tasks, and writing interface content. USE WHEN researching needs, shaping a product flow, creating wireframes or prototypes, drafting onboarding, errors or microcopy, or reviewing accessibility and localization of words. Not `information-design` (charts and data), `visual-design` (composition), or `frontend` (building the UI), which own those artifacts. Keywords: UX, lean UX, UX writing, user research, product design, user flow, wireframe, prototype, microcopy, error message, onboarding, accessibility, localization."
license: "Proprietary (private course-derived material, not for redistribution)"
---

# UX

This skill produces a research-grounded product brief, user journey and flow, prioritized scope, wireframe or prototype with real interface copy, and a review with clear return stages. It helps product teams decide what to learn and build while writing the words people need at each step.

> Inherits the `core` kernel. See [../core/SKILL.md](../core/SKILL.md) and follow its canonical gates instead of copying their definitions.

## When it fires — and when a sibling owns it

- **This skill:** research and scope for a digital product; task journeys and flows; wireframes and prototypes; interface content, errors, onboarding, voice and tone; word accessibility and localization.
- **`information-design` instead:** chart and data presentation. UX can define a research question or success outcome; the data artifact and its encoding belong there.
- **`visual-design` instead:** composition and visual form. UX can define screen content and structure; composition decisions belong there.
- **`frontend` instead:** building the production UI. UX supplies the tested behavior, states, and content to implement.

> **Disambiguation by artifact:** route research, task behavior, content, and prototypes here; route a chart, composed visual artifact, or implemented interface to the skill that produces it.

## Principles / anchoring rules

1. **Balance user value, business value, and development effort.** (1490 · U2 · L04 · 02:24–03:22)
2. **Treat content as part of experience design from the beginning.** Real words affect screen space and layout. (798 · U2 · L05 · 00:07–01:55; 798 · U2 · L05 · 01:55–03:03)
3. **Keep findings, assumptions, and team interpretations distinct.** A proto-persona may help before research, but it remains provisional until evidence updates it. (798 · U2 · L06 · 05:52–08:19; 1490 · U4 · L14 · 00:00–01:04)
4. **Optimize for learning and user outcomes.** Prototype the smallest useful test, then use what the team learns to revise the work. (1490 · U2 · L04 · 04:41–05:12; 1490 · U2 · L04 · 06:48–08:20)
5. **Write for the whole task.** Help people understand what is happening, what action is available, and what comes next. (798 · U2 · L05 · 09:05–11:31; 798 · U3 · L09 · 02:40–06:25; 798 · U3 · L09 · 06:25–08:48)
6. **Make access and localization part of content design.** Provide clear order, labels, useful image descriptions, and context for localizing strings. (798 · U4 · L13 · 04:28–08:09; 798 · U4 · L13 · 08:09–11:23; 798 · U4 · L13 · 11:23–13:18; 798 · U4 · L13 · 13:18–14:20; 798 · U4 · L13 · 14:20–16:09)
7. **Let domain and project conventions govern.** If a convention from a course conflicts with the intended users, platform, or domain, follow the domain and record the reason. (owner decision 6)

## The flow (at a glance)

| Stage | Decide | Check | Reference |
|---|---|---|---|
| 1. Frame outcome and brief | User problem, outcome, business need, assumption, constraints | T1 names the user, task, outcome, and known limits | [01-frame-and-outcomes.md](references/method/01-frame-and-outcomes.md) |
| 2. Research and evidence | What is known, what needs research, and which method fits | T2 links claims to evidence or labels them as assumptions | [02-research-and-evidence.md](references/method/02-research-and-evidence.md) |
| 3. Synthesize user needs | Patterns, provisional user picture, important task | T3 retains evidence and distinguishes findings from hypotheses | [03-synthesize-user-needs.md](references/method/03-synthesize-user-needs.md) |
| 4. Prioritize scope | User need, business value, effort, and learning target | T4 ties the MVP to a user need and a testable assumption | [04-prioritize-scope.md](references/method/04-prioritize-scope.md) |
| 5. Map content and flows | Information labels, task routes, branches, outcomes | T5 covers entry, route, relevant branches, and completion | [05-map-content-and-flows.md](references/method/05-map-content-and-flows.md) |
| 6. Prototype with real content | Idea, fidelity, and interactions needed to learn | T6 uses realistic copy and has no unresolved applicable render failures | [06-prototype-with-real-content.md](references/method/06-prototype-with-real-content.md) |
| 7. Write interface content | Conversation, voice, tone, and message for each state | T7 checks function and recovery; T8 checks voice and tone | [07-write-interface-content.md](references/method/07-write-interface-content.md) |
| 8. Test, access, localize, iterate | Usability evidence, accessible words, context for localization, next learning | T9–T11 record behavior, access, and the next decision | [08-test-access-and-iterate.md](references/method/08-test-access-and-iterate.md) |

### Scale the flow

- **Quick copy question:** inspect the task route and state, draft the message, and run T5, T7, and relevant T10 checks.
- **Critique of an existing product:** start with T1–T11; for each failure, return to the stage in the checklist, make one concrete change, and rerun affected tests.
- **Early product idea:** run stages 1–4 and prototype the riskiest assumption. Mark any persona or journey details that have not been researched as provisional.
- **Single feature or short flow:** combine related stages when useful, but keep evidence, decision, and checks visible.
- **Several audiences or connected flows:** run the full sequence and check shared navigation, voice, terminology, and error recovery across the experience.
- **After a fix:** rerun the changed stage's checks and every downstream check the change could affect. A changed flow can affect copy, accessibility order, and localization context.

## Course crosswalk decisions

- **Writing early; styling after structure checks.** The UX writing course puts content into design from the beginning and shows real copy changing layout. The product-design course validates wireframe structure before final UI styling. This skill drafts real content early and delays final styling until the structure has been tested. (derived from 798 · U2 · L05 · 00:07–01:55; 798 · U2 · L05 · 01:55–03:03; 1490 · U7 · L25 · 01:00–02:58; 1490 · U7 · L26 · 03:13–04:26)
- **Provisional personas are not evidence.** One course demonstrates a proto-persona before research; the other defines personas from researched patterns. This skill allows a provisional starting profile but requires it to be labeled and updated from evidence. (derived from 798 · U2 · L06 · 05:52–08:19; 1490 · U4 · L14 · 00:00–01:04)
- **Metrics describe outcomes; interviews and observation explore reasons.** The courses use counts, click tests, interviews, and observed behavior for different questions. Do not infer why people acted from counts alone. (derived from 798 · U2 · L05 · 06:04–08:15; 1490 · U3 · L09 · 01:25–02:20; 1490 · U3 · L10 · 01:15–02:11; 1490 · U3 · L10 · 02:11–03:11; 1490 · U3 · L10 · 03:11–03:32; 1490 · U7 · L30 · 00:00–03:44)

## Execution

### Output medium

- Use HTML for composed screens and interactive prototypes; use SVG for sitemaps, flows, and diagrams; embed SVG in HTML when useful. (derived from owner decision 7)
- Use the project's required delivery format when it differs. Keep project-specific components in project code and follow domain conventions over course style.
- A plan names stage decisions. A prototype includes realistic words and states. A critique reports each failed test, evidence, return stage, and one change. Cite course anchors in delivered method explanations, such as `798 · U4 · L12 · 05:50–10:41`.

### Render-and-check loop

1. Mark each HTML/SVG screen or flow area with `data-rk-stage`. Use semantic live text, labels, and controls in interactive prototypes.
2. Run render-kit code checks first. Fix each failure and render again. Read all skipped or incomplete results and explain why the check does not apply. Applicable checks include resource loading, console errors, font fallback, overflow, text collisions, contrast, and accessibility.
3. Prepare a render-kit brief using the specific questions in [review-checklist.md](references/method/review-checklist.md). Give the rendered images and questions to a fresh-context reviewer who did not make the artifact.
4. Verify the review answers, fix every `no`, and rerender. If a visual check cannot be judged, report it as not judged. Never treat a skip or missing reviewer as a pass.
5. Report measured, vision-judged, not-judged, and skipped checks separately.

**Code checks:** render-kit checks mechanical rendering, text fit, and applicable accessibility properties; measurement.md also names countable fields and task outcomes.

**Vision checks:** a fresh reviewer answers the specific questions about task comprehension, content hierarchy, message usefulness, flow continuity, and fit. A static render cannot prove screen-reader order; test keyboard and spoken navigation for T10.

## Gates (declared, inherited from core)

- **Grounding gate.** Use the brief, user evidence, product constraints, existing flows and content, and the relevant anchored course lessons as the substrate. See [../core/references/grounding-gate.md](../core/references/grounding-gate.md).
- **Output Contract.** Name the primary artifact and show evidence for each success criterion. Keep measured, judged, not-judged, and skipped results distinct. See [../core/references/output-contract.md](../core/references/output-contract.md) and [../core/references/wiki-protocol.md](../core/references/wiki-protocol.md).
- **Pushback and teach.** If the requested copy or flow blocks user understanding, access, or recovery, explain the consequence and recommend a concrete improvement. See [../core/references/pushback-and-teach.md](../core/references/pushback-and-teach.md).

## Anti-patterns (hard no-list)

- Treating the requested feature as the validated problem.
- Presenting team assumptions or an unresearched proto-persona as user evidence.
- Using survey counts to claim why users behaved as they did.
- Delaying real content until the wireframe is fixed, or polishing a prototype before testing its risky assumption.
- Writing a screen without its entry point, context, and next step.
- Using an error as a dead end or a button label that misstates its action.
- Treating an empathy map as research or a prioritization score as an objective decision.
- Omitting screen-reader order, help text, live text, useful names, or localization context.
- Treating code checks as evidence that people understand the experience.
- Calling a skipped check or unavailable vision review a pass.
- Presenting a course preference as a universal domain rule.
- Copying paid course material outside this private skill; see [NOTICE.md](NOTICE.md).

## Composition

- **Inherits:** [core](../core/SKILL.md) for shared gates.
- **Hands off to:** [information-design](../information-design/SKILL.md) for chart and data artifacts; [visual-design](../visual-design/SKILL.md) for composition; [frontend](../frontend/SKILL.md) for production UI implementation.
- **Domain rule:** product, platform, audience, accessibility, and legal conventions govern when they conflict with a course example.

## References

- [references/method/01-frame-and-outcomes.md](references/method/01-frame-and-outcomes.md) — align the problem, outcome, and constraints.
- [references/method/02-research-and-evidence.md](references/method/02-research-and-evidence.md) — choose research methods and preserve evidence.
- [references/method/03-synthesize-user-needs.md](references/method/03-synthesize-user-needs.md) — synthesize findings and keep assumptions provisional.
- [references/method/04-prioritize-scope.md](references/method/04-prioritize-scope.md) — choose a testable, valuable scope.
- [references/method/05-map-content-and-flows.md](references/method/05-map-content-and-flows.md) — organize content and map task routes.
- [references/method/06-prototype-with-real-content.md](references/method/06-prototype-with-real-content.md) — choose fidelity and test realistic content.
- [references/method/07-write-interface-content.md](references/method/07-write-interface-content.md) — write voice, tone, and interaction copy.
- [references/method/08-test-access-and-iterate.md](references/method/08-test-access-and-iterate.md) — test behavior, access, localization, and learning.
- [references/method/review-checklist.md](references/method/review-checklist.md) — numbered tests and return stages.
- [references/method/measurement.md](references/method/measurement.md) — source procedures, independent checks, and thresholds for T1–T11.
- [references/method/coverage.md](references/method/coverage.md) — lessons not cited by a method digest and reasons.
- [references/course-798/README.md](references/course-798/README.md) — source index for *Introduction to UX Writing*.
- [references/course-1490/README.md](references/course-1490/README.md) — source index for *Digital Product Design with Lean and UX*.
- [references/course-798/BLOCKED.md](references/course-798/BLOCKED.md) and [references/course-1490/BLOCKED.md](references/course-1490/BLOCKED.md) — excluded and caption-only lesson status.
- [scripts/check_refs.py](scripts/check_refs.py) — verify local links and course anchors.
- [NOTICE.md](NOTICE.md) — private course-material notice.
- [EVOLUTION.md](EVOLUTION.md) — design-run history and validation state.
