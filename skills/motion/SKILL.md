---
name: motion
description: "A course-distilled method for planning stories, storyboards, animatics and choreography for motion design and animated infographics. USE WHEN shaping a motion piece, planning beats or transitions, setting animation curves, or reviewing animated information. Static chart selection belongs to information-design; page composition belongs to visual-design; deck and demo sequencing belongs to presentation. Keywords: motion design, animation, storyboard, animatic, animation curves, easing, choreography, animated infographic, timing, loop."
license: "Proprietary (private course-derived material, not for redistribution)"
---

# Motion

Motion turns a brief, script or information set into a story plan, storyboard, timed animatic and motion choreography, then checks the rendered sequence. It plans motion and writes the storyboard in the owner's `scene-engine` format; it does not own the underlying static chart method or page composition.

> Inherits `core`; see [../core/SKILL.md](../core/SKILL.md). Keep shared gates in their canonical references.

## When it fires — and when a sibling owns it

- **This skill:** plan or critique an animated story, storyboard, animatic, timing, movement system, animation curves, transitions, loop or animated infographic.
- **`information-design` instead:** choose and validate a static chart form or data encoding. Motion carries an established encoding through time.
- **`visual-design` instead:** solve static composition, hierarchy, typography or visual identity. Motion can consult it for the frame's visual system.
- **`presentation` instead:** design a deck or demo as a presentation artifact. Motion owns the moving sequence itself.

> **Disambiguation by artifact:** choose the owner from the output being decided: motion sequence, static chart, composed graphic, or deck/demo.

## Principles / anchoring rules

1. **Make movement serve the message.** Motion should inform, focus attention and express. (503 · U3 · L10 · 01:21–02:42)
2. **Keep the receiver's understanding in view.** Structure can be playful, but the recipient still needs to understand the message. (433 · U3 · L08 · 05:43–06:50)
3. **Verify information before animating it.** Check data and links against their sources, and preserve the data proportions when adapting the artwork. (3762 · U2 · L03 · 04:58–05:50; 3762 · U4 · L13 · 01:12–02:49)
4. **Keep a coherent movement language.** Define motion attributes and use a clear order when several elements move; the teacher's series uses a character to guide movement style. (503 · U3 · L10 · 02:42–04:08; 503 · U3 · L11 · 04:31–06:02)
5. **Use transitions to carry continuity.** Shared form, color, speed or direction can connect scenes; omit a transition that has no narrative reason. (433 · U4 · L11 · 02:21–02:42; 433 · U4 · L11 · 02:42–03:52)
6. **Let reading time set the choreography.** Dense infographic content should appear in sequence and remain visible long enough to read; the course's title and dense-panel timings are examples, not universal defaults. (561 · U2 · L06 · 10:45–12:04; 561 · U4 · L11 · 00:02–01:56)
7. **Treat course preferences as examples.** Project, audience and domain conventions govern over a course's aesthetic choices. (derived from 433 · U3 · L06 · 00:49–01:37; 3762 · U4 · L14 · 00:00–02:56; 561 · U4 · L13 · 02:47–05:54)

## The flow (at a glance)

| Stage | Decide | Check before moving on | Reference |
|---|---|---|---|
| 1. Intent and evidence | Sender, receiver, purpose, runtime, production time and source facts | Message, audience and verified information are named | [purpose-and-evidence.md](references/method/purpose-and-evidence.md) |
| 2. Story and tone | Premise, narrative personality, event order and ending | A viewer can follow the message through the chosen structure | [story-and-tone.md](references/method/story-and-tone.md) |
| 3. Visual direction | Reference attributes, information encoding and repeatable visual rules | The visual system carries the information without changing it | [visual-direction.md](references/method/visual-direction.md) |
| 4. Storyboard and animatic | Panels, framing, transitions, scene time and sound cues | The timed rough version reads and resolves as intended | [storyboard-and-animatic.md](references/method/storyboard-and-animatic.md) |
| 5. Choreography | Movement purpose, curve, trigger, follower and loop behavior | Timing and relationships read in the rendered motion | [choreography.md](references/method/choreography.md) |
| 6. Review and handoff | Fixes, render settings and delivery evidence | Code checks pass; visual questions pass or are marked not judged | [review-and-handoff.md](references/method/review-and-handoff.md) |

### Scale the flow

- **Quick motion question:** use stages 1, 2 and 5; include stage 6 for a concrete edit or critique.
- **New storyboard or animatic:** run stages 1–4, then use stage 5 for the motion that the storyboard calls for.
- **Full motion piece:** run all six stages in order.
- **Critique:** start at stage 6, report each failed test and return to its named stage.
- **After a fix:** rerun the failed test and any later test whose evidence depends on the changed timing, pose, scene or content.

## Execution

### Output medium

- Write the editable motion plan as a `scene-engine/storyboard@1` JSON storyboard. The scene-engine stage is 1920×1080 CSS pixels at 30 fps; scene starts and layer tracks use the time origins in [SPEC §4](../../scene-engine/SPEC.md#4-scene-model). Course project sizes and frame rates are examples only.
- Use editable HTML/SVG for visual boards and artwork where useful. Add render-kit markup to those files and render/check them with the owner's `render-kit`; the final motion is rendered by `scene-engine`.
- Keep project-specific artwork and assets in the project. Use stable scene and layer IDs, descriptive notes, and source references for factual content.

### Render-and-check loop

1. Draft the storyboard and any HTML/SVG visual boards. Keep each fact tied to its source and each planned movement tied to a story or reading purpose.
2. Run `scene-engine validate` before rendering. Fix schema, bounds, timing, track and asset-path errors.
3. Render with `scene-engine`; check key frames through its `check` command and render-kit. Probe the finished video's dimensions, frame rate, duration and streams against the requested delivery contract.
4. Run exact code checks first. Then give rendered frames or the clip plus the specific questions in [review-checklist.md](references/method/review-checklist.md) to a fresh-context reviewer who did not make the work and can see it. A vision check without that reviewer is **not judged**.
5. Fix failures at their return stage, render again, and repeat dependent code and vision checks. Report each check as measured, vision-judged, not judged or skipped, with a reason for the last two.

**Code checks:** storyboard schema and cross-field validation; resolved scene/layer/track timing; asset containment; data/value correspondence when data is exposed in structured source and output; render-kit checks for applicable HTML/SVG; output metadata and key-frame comparison.

**Vision checks:** message comprehension, tone, readable dwell time, transition continuity, movement character, useful cause/effect, and whether motion distracts from information. Use a concrete question for each; code results cannot establish these judgments.

### Scene-engine timing notes

- Put each scene's `durationMs` in the storyboard. Use `startMs` for a fixed start or `after` plus optional `gapMs` to place a scene after an earlier one.
- Scene starts are storyboard-relative; layer start/duration are scene-local; track keyframe times are layer-local. State the intended event at the scene/layer level so the timing origin is clear.
- A track targets one property and carries absolute values. Use only easing and property paths supported by [scene-engine SPEC §4](../../scene-engine/SPEC.md#4-scene-model); validation rejects unsupported fields and paths.
- Run commands as shown in [scene-engine/AGENTS.md](../../scene-engine/AGENTS.md). For selected frames, use its `check` command with the render-kit path. Static visual checks and markup are described in [render-kit/AGENTS.md](../../render-kit/AGENTS.md).

## Gates (declared, inherited from core)

- **Grounding gate:** substrate is the brief or script, source records for facts, the cited course lessons, the storyboard and rendered output. Mark inference as derived. See [grounding-gate.md](../core/references/grounding-gate.md).
- **Output Contract:** a plan names each stage decision; a critique lists test, evidence, return stage and one concrete change. Report measured, judged, not judged and skipped checks. See [output-contract.md](../core/references/output-contract.md) and [wiki-protocol.md](../core/references/wiki-protocol.md).
- **Pushback and teach:** when a requested movement would obscure reading or break a domain convention, explain the consequence and cite the relevant method anchor. See [pushback-and-teach.md](../core/references/pushback-and-teach.md).

## Anti-patterns (hard no-list)

- Animating before deciding what the viewer should understand or feel.
- Treating an evocative premise as permission to change sourced facts or data proportions.
- Adding movement to every element at once, or choosing curves without considering their role.
- Forcing transitions or loops that undermine the narrative.
- Using a course's example timings, character, chart mapping or aesthetic as a universal rule.
- Hiding information behind simultaneous reveals or dwell times that do not allow reading.
- Treating a valid storyboard or smooth render as proof that the message is understood.
- Calling an unavailable vision review a pass.
- Stating a course method without its anchor or presenting a derived rule as the teacher's words.

## Composition

- **Inherits:** `core`.
- **Hands off:** `information-design` for static chart choice and data encoding; `visual-design` for static composition and visual systems; `presentation` for a deck or demo whose main artifact is a presentation.
- **Execution owner:** `scene-engine` produces motion from its storyboard format; `render-kit` renders and checks HTML/SVG visual assets and selected frames.
- **Grounded:** read `core` and its grounding, output and pushback references; `visual-design` for its staged method/checklist and `color-theory` for its method/measurement split; course notes and cited lessons for the motion workflow. Reused conventions: anchored method claims, stage-return tests, code before vision, tool-independent measures, and domain conventions over course taste.

## References

- [references/method/claim-audit.md](references/method/claim-audit.md) — the independent claim audit of every course citation (evidence per scope in `audit/`).
- [references/method/purpose-and-evidence.md](references/method/purpose-and-evidence.md) — set objectives and verify information before visualizing it.
- [references/method/story-and-tone.md](references/method/story-and-tone.md) — turn input into premise, tone, structure and a message-led story.
- [references/method/visual-direction.md](references/method/visual-direction.md) — research visual direction and preserve the meaning of information.
- [references/method/storyboard-and-animatic.md](references/method/storyboard-and-animatic.md) — prototype the sequence, transitions, timing and sound.
- [references/method/choreography.md](references/method/choreography.md) — set movement language, curves and relationships between elements.
- [references/method/review-checklist.md](references/method/review-checklist.md) — numbered review tests, pass conditions and return stages.
- [references/method/measurement.md](references/method/measurement.md) — course procedure, tool-independent check and default threshold for every test.
- [references/method/review-and-handoff.md](references/method/review-and-handoff.md) — run the code-first/render/vision loop and report evidence.
- [references/method/coverage.md](references/method/coverage.md) — lesson inventory for lessons not cited in a method digest.
- [scripts/check_refs.py](scripts/check_refs.py) — verify source anchors, links and package paths.
- [references/course-3762/README.md](references/course-3762/README.md), [references/course-503/README.md](references/course-503/README.md), [references/course-433/README.md](references/course-433/README.md), [references/course-561/README.md](references/course-561/README.md) — reading-copy inventories.
- Course status notes: [3762](references/course-3762/BLOCKED.md), [503](references/course-503/BLOCKED.md), [433](references/course-433/BLOCKED.md), and [561](references/course-561/BLOCKED.md); respect excluded lessons and caption-only limits.
- Scene-engine contract: [scene-engine/AGENTS.md](../../scene-engine/AGENTS.md) and [scene-engine/SPEC.md §4](../../scene-engine/SPEC.md#4-scene-model).
- Render-kit contract: [render-kit/AGENTS.md](../../render-kit/AGENTS.md).
- [NOTICE.md](NOTICE.md) — private paid-course source notice.
