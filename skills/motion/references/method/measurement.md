# Measurement: course checks and tool-independent evidence

The courses mostly preview work and judge whether it reads, moves or feels right. The qualitative defaults below are skill choices that operationalize those procedures; they are not numeric thresholds taught by the courses. Preserve any project-specific threshold from the brief or domain owner and report it separately.

| Test | Course's own way | Tool-independent check | Default threshold |
|---|---|---|---|
| T1 Purpose and evidence | Plan sender/receiver, message duration/available time and viewer/maker objectives; check data and links against their sources. (433 · U2 · L04 · 01:03–01:56; 433 · U2 · L04 · 01:56–02:46; 433 · U2 · L04 · 02:46–04:12; 3762 · U2 · L03 · 04:58–05:50) | Compare a source ledger against the storyboard's narration, captions, chart values and labels. Ask a reviewer to state the intended viewer response. | **Skill choice:** all factual claims have a cited source or are marked open; all six planning fields are stated. |
| T2 Premise and tone | Test whether the premise is clear about context but open about its visual realization; ask whether the intended tone is clear. (433 · U3 · L06 · 07:51–08:34; 433 · U3 · L07 · 02:55–03:42) | Fresh reviewer reads the brief and storyboard, then paraphrases subject, function and tone. | **Skill choice:** reviewer identifies all three without a conflicting interpretation; course gives no score or numeric threshold. |
| T3 Structure and message | Follow the event structure and check that the receiver can understand the message. (433 · U3 · L08 · 00:08–01:08; 433 · U3 · L08 · 05:43–06:50) | Reviewer summarizes the opening, key change and resolution from the panels or animatic. | **Skill choice:** the summary matches the intended message and omits no required beat; course provides no numeric threshold. |
| T4 Storyboard and continuity | Review the storyboard from a distance, question gaps or unnecessary material, and test with other people. Check shared forms/colors, speed and direction at transitions. (433 · U4 · L09 · 03:45–04:19; 433 · U4 · L11 · 02:21–02:42; 433 · U4 · L11 · 02:42–03:52) | Count narration/story beats mapped to panels; inspect adjacent scene endpoints; ask which element carries each transition and why it belongs. | **Skill choice:** every required beat has a panel and every transition has a stated reason. The 561 course suggests about 5–10 infographic panels for its own project, but gives no universal panel threshold. (561 · U2 · L04 · 02:33–03:28) |
| T5 Visual system and encoding | Check that source values keep their ordering/proportions while adapting data artwork; use a consistent plate system. (3762 · U4 · L13 · 01:12–02:49; 561 · U3 · L07 · 01:43–02:44; 561 · U3 · L07 · 02:45–06:02) | Compare structured source values with storyboard chart data and transformed dimensions; render plates and review repeated type/color/shape rules. | **Skill choice:** no unexplained value or proportional change; all declared constants appear in required scenes. |
| T6 Timing and reading | Imagine the storyboard in motion, assign scene time, replay and revise; play dense scenes and try to read their information. (433 · U5 · L14 · 00:30–01:32; 433 · U5 · L14 · 01:32–01:50; 561 · U4 · L11 · 00:02–01:56) | Read scene durations and reveal times from the storyboard JSON; review the render at normal speed with narration/captions. Ask the reviewer to repeat each required information group before it changes. | **Skill choice:** all required information can be read before removal and total runtime meets the brief. Course 561's 2–3 second title and roughly 10 second dense panel are example timings only. (561 · U4 · L11 · 00:02–01:56) |
| T7 Motion purpose and character | Define motion attributes, then preview and adjust until the movement expresses the chosen character and purpose. (503 · U3 · L10 · 01:21–02:42; 503 · U3 · L10 · 02:42–04:08; 503 · U3 · L11 · 02:53–04:31; 503 · U3 · L11 · 04:31–06:02) | Inspect storyboard movement notes and rendered frames; ask what each major movement communicates and what attracts attention first. | **Skill choice:** every major movement has a stated role and the reviewer recognizes the intended style; no numeric threshold in the course. |
| T8 Curves and choreography | Preview start, travel and arrival; adjust graph curves, keyframe timing, trigger/follower delays and shape effects. (503 · U4 · L13 · 03:18–04:20; 503 · U4 · L13 · 04:20–05:42; 503 · U5 · L20 · 04:33–06:31; 561 · U4 · L13 · 02:47–05:54) | Calculate property values at keyframes and sample rendered frames; compare trigger and response onset times; ask a reviewer whether cause/effect reads. | **Skill choice:** every element reaches its intended endpoint; no unplanned overshoot; triggers precede readable responses. Course provides no universal curve or delay threshold. |
| T9 Transition, loop and cutoff | Preview bounded ranges and compare intended loop/jump; place scene markers and inspect endpoints. (503 · U5 · L18 · 16:07–18:46; 503 · U5 · L20 · 10:46–12:26; 561 · U4 · L11 · 00:02–01:56) | Compare first/last pose values for a seamless loop; inspect key frames around scene boundaries and the final motion frame. Ask the reviewer whether any planned jump appears intentional. | **Skill choice:** every join matches its declared intent and every required move completes before its boundary. No universal tolerance supplied by the courses. |
| T10 Render and delivery | Review the rendered result, export settings and output size; render a preview when interactive playback is unreliable. (3762 · U5 · L20 · 00:24–01:26; 561 · U4 · L18 · 00:00–01:24; 561 · U4 · L18 · 01:24–03:15; 561 · U4 · L15 · 08:46–11:45) | Run `scene-engine validate`, render and check selected frames through render-kit; inspect the final file's dimensions, frame rate, duration and streams with a media probe. Run render-kit markup/checks on HTML/SVG visual assets. | **Skill choice:** validation has no errors and measured output matches the project contract; all applicable code failures are resolved. The courses do not set a general encoding or file-size threshold. |

## Reporting

For each test report **measured**, **vision-judged**, **not judged** or **skipped**. Include the reading for a measured property. If the reviewer is unavailable, record **not judged**. If a test does not apply, name why it is skipped. A rendered file can prove timing or metadata; it cannot prove that viewers understood the message.

## Scene-engine measurement notes

- `scene-engine` uses 1920×1080 CSS pixels at 30 fps, integer milliseconds, storyboard-relative scene starts, scene-local layer timing and layer-local track keyframes. (Owner contract: `scene-engine/SPEC.md` §4.)
- Run `scene-engine validate` before rendering; it checks schema, IDs, scene/layer/track bounds, resolved keyframe order, chart compatibility, caption bounds, mask sources and asset containment.
- Use `scene-engine check --at ... --rk ...` for selected key frames. Use HTML/SVG `data-rk-stage` and `data-rk-focal` where relevant to render-kit checks. Review exact failures before vision review.
- Do not infer comfortable reading speed from a character-per-second number alone; ask a reviewer to read the actual rendered information at normal playback speed. (derived from 561 · U4 · L11 · 00:02–01:56; 433 · U5 · L16 · 03:32–04:40; 433 · U5 · L16 · 04:40–05:29)

## Automated storyboard measurements

Run the shipped helper after `scene-engine check` has written reference PNGs. It measures caption characters per second, panel holds after the final child track, tracks or layers extending past their boundaries, configured storyboard proportions, and MP4 frames against check renders. The frame check cuts the MP4 at each `at-<milliseconds>` directory time and uses FFmpeg/ffprobe to compare downsampled image differences; the default mean and pixel thresholds are starting tolerances and must be checked against a known-good render from the same renderer/codec. A missing check frame fails the measurement. (derived: dogfood 2026-10-02, F10)

```bash
python3 scripts/measure_storyboard.py storyboard.json evidence.json render.mp4 \
  --check-dir checks/frames --output checks/measure.json
```

The evidence JSON may declare proportional bindings when facts and storyboard geometry are not connected by a shared schema. A direct binding compares one layer property to a fact times a scale; a ratio binding compares a layer property to a reference layer property and a fact ratio. Facts use dotted JSON paths, with `[index]` for arrays. (derived: dogfood 2026-10-02, F10)

```json
{
  "facts": {"hours": 9.5, "cost": 25, "budget": 100},
  "motionChecks": {
    "captionCpsLimit": 20,
    "minimumHoldMs": 1500,
    "proportions": [
      {"name": "lost-time bar", "layer": "lost-bar", "property": "width",
       "fact": "facts.hours", "scale": 60, "tolerance": 0.01},
      {"name": "budget share", "layer": "budget-fill", "property": "width",
       "ratio": {"numerator": "facts.cost", "denominator": "facts.budget"},
       "against": {"layer": "budget-track", "property": "width"}, "tolerance": 0.001}
    ]
  }
}
```

If no proportion bindings are present, the tool reports `not_configured` and leaves the measurement incomplete; that is not a measured T5 pass. For work with no numeric encoding, put a short `proportionsNotApplicable` reason in `motionChecks`. The helper's unit tests are in `tests/test_measure_storyboard.py`. (derived: dogfood 2026-10-02, F10)
