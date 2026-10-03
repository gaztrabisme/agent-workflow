# Review and handoff: render, inspect and report

## Reader and scope

**Reader:** an agent completing or critiquing a motion piece. **Scope:** make the rendered evidence usable and route each failure to the stage that owns it.

**Source lessons:**
- [3762 · U5 · L20](../course-3762/U05-L20-export-and-output.md)
- [561 · U4 · L15](../course-561/U04-L15-adding-fine-details-of-animation-and-textures-2.md)
- [561 · U4 · L18](../course-561/U04-L18-renders.md)
- [433 · U5 · L16](../course-433/U05-L16-let-s-give-life-to-our-history.md)

## First idea, stated as the rule

- Replay a bounded sequence and refine its timing or transitions; if live playback is too heavy to judge, render a preview and review that output. (561 · U4 · L15 · 08:46–11:45; 561 · U4 · L17 · 09:01–10:18)
- Before rendering, review the export settings for format, duration, encoding details and estimated file size; then choose the filename and destination and render. (3762 · U5 · L20 · 00:24–01:26)
- Course 561 shows a high-quality master followed by a compressed sharing version; output choice depends on the delivery context. (561 · U4 · L18 · 00:00–01:24; 561 · U4 · L18 · 01:24–03:15)
- The storyboard and animatic remain useful handoff artifacts because they carry scene order, durations, camera or transition notes and sound ideas into animation. (433 · U5 · L16 · 03:32–04:40; 433 · U5 · L16 · 04:40–05:29; 433 · U5 · L16 · 05:29–07:06)

## Idea that is best shown as a table

| Check class | Example | Evidence |
|---|---|---|
| Code | Schema, IDs, time bounds, asset paths, render metadata | `scene-engine validate`, `scene-engine check`, media probe |
| Vision | Message, tone, reading, continuity, curve feel and visual coherence | Fresh-context reviewer answers checklist questions against rendered frames/clip |
| Deferred | A judgment with no reviewer, unavailable source or inapplicable test | State **not judged** or **skipped** and give the reason |

## Compare the MP4 with storyboard check frames

`scene-engine check` renders from the storyboard model, so it cannot establish that the MP4 contains the same motion or captions. List the authored keyframe times, scene start/middle/end and any risky transition or caption moments in the explicit `--at` list; cut the MP4 at each of those times; then compare each cut with the matching check render using `scripts/measure_storyboard.py`. The MP4 comparison is required evidence for T10. Treat a difference outside the known-good renderer/codec floor as a failure, return to the owning storyboard or render decision, and render again. (derived: dogfood 2026-10-02, F1)

```bash
scene-engine check storyboard.json --at <milliseconds,...> --rk ../tools/render-kit/bin/rk
python3 scripts/measure_storyboard.py storyboard.json evidence.json render.mp4 \
  --check-dir checks/frames --output checks/measure.json
```

## Brief a motion reviewer

Prepare a contact sheet HTML containing four to six labeled frames from the MP4, chosen across the piece and around any uncertain transitions, then pass that one sheet to `rk brief`. Put the clip path in `--purpose` and give the reviewer access to the clip; the brief tool's single PNG cannot carry the playback file. Put `[PLAYBACK]` in questions that require normal-speed reading, movement character or trigger/follower judgment, whether the ending feels intentional, or voice intelligibility and pronunciation. Ask only for frame inspection on questions about composition, hierarchy, data encoding or isolated poses. Send the generated `brief.md`, its listed PNG, and the clip path together. (derived: dogfood 2026-10-02, F11)

```bash
bin/rk brief motion-contact-sheet.html --questions motion-questions.md \
  --out-dir review/brief --purpose "Clip path: render.mp4; play for [PLAYBACK] questions"
```

## Render-kit limitations seen in dogfood

- `rk brief` may print group headings separately from their questions; repeat the group or test label inside each question so its context survives. (derived: dogfood 2026-10-02, F13)
- If a whole-stage focal element makes the `value` check incomplete or hit a zero-size error, set `data-rk-focal` on the actual focal content area. If the automated result remains incomplete, record it as incomplete and route the value judgment to a vision reviewer. (derived: dogfood 2026-10-02, F13)
- For HTML pages taller than 1080 px, pass their full pixel height explicitly, for example `bin/rk check board.html --height 1600 --out-dir checks/board`. (derived: dogfood 2026-10-02, F13)

## A rule you derived (derived)

Keep code checks and vision judgments in separate report columns. The course examples mix direct timeline inspection with judgments such as smoothness or readability; separating them makes each conclusion auditable. (derived from 561 · U4 · L15 · 08:46–11:45; 561 · U4 · L16 · 05:53–09:08; 433 · U5 · L16 · 05:29–07:06; 433 · U5 · L16 · 07:06–08:12)

## Failures

**Problem 1 (derived from the course's pre-render settings check): a preview is mistaken for final delivery.**
- **The failure (derived):** the motion has been reviewed, but the requested rendered output has not been checked against its format or runtime. (3762 · U5 · L20 · 00:24–01:26)
- **The fix:** render with scene-engine, inspect the actual output and measure delivery properties against the brief.

**Problem 2: a check is reported as a pass without its evidence.**
- **The failure:** a technical pass is used to imply visual or narrative success. (derived from 433 · U5 · L14 · 02:57–03:26; 561 · U4 · L15 · 08:46–11:45)
- **The fix:** report code and vision results separately; label unavailable vision as not judged.

## Check before moving on

1. **T10 — Render and delivery:** pass when scene-engine validation succeeds, the video is rendered, selected frames and the output contract are checked, and each applicable visual test has a reviewer result or an explicit not-judged/skipped status.

**Practice the teacher sets:** render a reviewed version, inspect its output, and make a delivery copy when needed. See [Unit 4](../course-561/U04-unit.md), [renders](../course-561/U04-L18-renders.md), and [export/output](../course-3762/U05-L20-export-and-output.md).

## Freshness and ownership

**Maintainer:** skill owner  
**Last reviewed:** 2026-10-02  
**Review due:** 2027-10-02 or when the scene-engine or render-kit contract changes
