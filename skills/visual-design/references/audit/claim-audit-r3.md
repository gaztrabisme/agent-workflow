# Claim audit
Writer: codex (dogfood fixes)
Auditor: glm
Round: 3

Scope: changed lines in `references/audit/dogfood-fix-r1.diff`. Anchored citations appear only on the rewritten T6 and T7 rows of `references/method/measurement.md`; every other changed line adds derived-labelled guidance or code with no anchor.

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | references/method/measurement.md | 5642 · U4 · L49 · 02:06–03:47 | Negative space is a dynamic component that separates elements and groups. | supported | |
| 2 | references/method/measurement.md | 5642 · U4 · L49 · 03:48–04:52 | Figure-ground principle: figures emerge via contour, value contrast or smaller area. | supported | |
| 3 | references/method/measurement.md | 5642 · U4 · L49 · 04:52–06:43 | Negative space organizes content, separates or relates elements, paces reading. | supported | Section states it "organizes content… pacing how it's read". |
| 4 | references/method/measurement.md | 5642 · U5 · L74 · 01:54–02:45 | Space distribution creates compositional unity; sparse design divides the frame. | supported | Labelled "derived from"; section names space use a resource for "compositional unity". |
| 5 | references/method/measurement.md | 5642 · U5 · L74 · 02:45–03:00 | A leg divides and orders the compositional space. | supported | |
| 6 | references/method/measurement.md | 5642 · U5 · L74 · 03:00–03:33 | A filled design leaves space reduced to a minimum. | supported | Supplies the "filled" half of the derived both-extremes claim. |
| 7 | references/method/measurement.md | 5642 · U5 · L74 · 08:00–08:35 | Chillida gives value to the void, the emptiness enclosed. | supported | Supplies the "mostly empty" half. |
| 8 | references/method/measurement.md | 5642 · U2 · L14 · 02:56–04:58 | Heading sizes set on an Instagram-proportioned artboard, judged at output size. | supported | |
| 9 | references/method/measurement.md | 5642 · U2 · L14 · 04:58–06:57 | Body set at 50 pt; canvas size misleads since output is smaller on a phone. | supported | |
| 10 | references/method/measurement.md | 5642 · U4 · L60 · 07:58–09:46 | Course builds a proportional scale from the golden ratio (9 × 1.618). | supported | |
| 11 | references/method/measurement.md | 5642 · U4 · L60 · 09:46–13:38 | Course extends the scale by Fibonacci addition (14.5 + 9 = 23.5…). | supported | |

## Added sentences

None.

All eight added guidance sentences carry an explicit "(derived: …)" label naming the run-2 dogfood finding, satisfying the labelling option: SKILL.md stage-1 check cell; brief-and-intent.md "Derived content verification" bullet; measurement.md T6 panel-background and set-target-first sentences, T7 deduplication sentence, and VD-T prefix paragraph; review-checklist.md VD-T prefix sentence and T11 n/a sentence. The remaining additions are code (measure_scale.py set deduplication, new regression test) and state no guidance.
