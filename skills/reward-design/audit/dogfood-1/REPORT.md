# Unit T report — 2026-10-10-reward-skill

Run reviewed: 2026-10-11. **Task status: COMPLETE. Skill verdict: FAIL as a self-sufficient critique workflow.** The three requested files exist; all 27 checklist questions appear once per piece with observations, verdicts, exact source IDs/tiers and fixes. The critique contains all 27 slide rows and 58 second-by-second intervals, including the last half-second. This is a local inspection, not an audience-effect study or a production rebuild.

Outputs: [critique.md](critique.md), [skill-feedback.md](skill-feedback.md), and this report. The feedback contains 19 located findings with proposed edits. The main gaps are mixed verdict/evidence states, missing applicability and severity rules, missing existing-media measurement steps, and unscoped source/audience requirements. The critique required explicit local tailoring in these areas.

## Measured, judged, and not judged

Measured: PDF page count (27), page size (1440 × 810 pt), extracted slide text; MP4 duration (57.500 s), 1725 frames, H.264/yuv420p, 1920 × 1080 at 30 fps, stereo AAC/48 kHz; all-frame FFmpeg scene scores with and without the caption band; five main-content boundaries at 4.000, 12.500, 25.000, 38.000 and 44.000 s; 26 caption-band transitions confirmed by an independent pixel-presence measurement; chart callout/bar onsets measured in six regions; decoded audio, per-second RMS/peak, 26 silence intervals at −45 dBFS for at least 0.10 s (15.733 s in total), integrated loudness −16.0 LUFS, loudness range 3.8 LU, true peak −1.3 dBFS. The upper/late/recovery callouts lag the corresponding caption starts by about 2.633/2.679/2.837 s. Mono RMS and stereo whole-mix loudness are distinct measurements. Those thresholds are analysis choices, not audience limits. VTT windows and the piece’s drilling/training values are reported data, not independent transcription or source-truth verification. Visible arithmetic was checked separately.

Judged by eye: contact sheets of all 27 rendered slides, selected individual slides, 58 exact-second video frames and selected native-resolution key frames; visual relationships, promise/resolution pairs, visible qualifications, repetition and ending. The deck has no supplied playback timing. No slide duration is inferred. Expected benefits and top-three ranking are reviewer judgments, not measured audience effects.

Not judged: actual device listening, subjective synchrony, spoken intelligibility, music mood, reduced-motion playback, audience curiosity, comprehension, enjoyment, usefulness, delayed recall or retention. No participants or candidate edit were supplied. Original chart vectors, training logs and drilling ledgers are not in this packet; source truth is not certified. Inspection distinguishes absent substantiation from proven falsehood.

Evidence lives in [evidence/](evidence/), including repeatable scripts for [measurement/contact sheets](evidence/measure.py), [cue regions](evidence/measure_regions.py), [caption presence](evidence/measure_captions.py), and [critique assembly](evidence/write_critique.py); source text, images, probe, scene scores, loudness and silence logs, [per-second measurements](evidence/video/seconds.csv), and [measurement summary](evidence/video/measurements.json). [evidence/README.md](evidence/README.md) records extraction commands and limitations; [verification.json](evidence/verification.json) records the final coverage check.

Verified: both pieces have R01–R27 with exact source questions and trails; 27 slide rows and 58 contiguous video intervals; all required per-check fields; all 19 skill-feedback findings have locations/proposed edits; report samples match the critique. Deck verdicts: 0 meets / 13 partly / 4 misses / 10 not applicable. Video: 6 meets / 15 partly / 1 misses / 5 not applicable. These are mixed inspection/availability dispositions, not a psychological score. R25 misses denote an absent outcome-measurement record rather than an observed audience failure. R26 is inapplicable because no memory improvement is claimed. Every not-judged/skipped condition is explained in the critique.

## Output sample — deck top three

1. **Make the test a real payoff (slides 6–9).** Pair the same prompt with a baseline and the fine-tuned output, evaluate both against accuracy, audience fit and format, and show the result beside slide 9. If no comparison is available, label the examples unvalidated. Expected effect: lets the evaluator decide what the training achieved.
2. **Qualify the promised benefits where they appear (slides 9, 12–27).** Mark generated copy as draft material, annotate unsupported price/protection assurances, and put relevant uncertainties beside the safety and growth imagery. Expected effect: prevents the demonstration from presenting persuasive sample copy as established benefit.
3. **Make slide 27 close the demonstration.** Retain the last post and add a compact summary of the three delivered formats, what remains untested, and the next review step. Expected effect: gives the reader a usable conclusion instead of stopping on another example.

## Output sample — explainer top three

1. **Align the chart explanation with its reveal (16.088–22.419 s).** Retire the upper-section cue as the last-section sentence begins; show the relevant gap and its annotation before the recovery sentence. Expected effect: makes the central schedule story easier to follow.
2. **Distinguish cumulative lost time from finish variance (22.5–29.554 s).** Carry the 6 h endpoint into the 28.5 h lost-time scene and explicitly name the two measures; do not invent a recovery cause. Expected effect: resolves the most likely conceptual ambiguity between adjacent scenes.
3. **Keep the evidence visible during the cause explanation (25–38 s).** Introduce an integrated cause overview with the total, then highlight equipment, weather and hole condition as each is discussed; keep an inspectable final view. Expected effect: replaces the largely empty setup and brief completed chart with a comparison that supports the next action.

These rankings are reviewer predictions about task value, not measured effect sizes. No modified media was produced.

## Scope and records

The supplied reward-design SKILL.md and all ten references were read, with inherited core gates and selected V rows used for qualification. The piece briefs were treated as source context for this critique; their earlier renderer/rebuild instructions were not executed. The three requested Markdown files are the allowed project record and handoff; the reusable skill package and original media remain untouched. Independent audience and multi-model review are deferred to the coordinator; no subagents were used.
