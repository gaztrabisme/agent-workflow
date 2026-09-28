# Review checklist: twelve tests for visual design

Reader: an agent reviewing a finished artifact or an existing design. Run code checks first, then send the rendered artifact and the specific vision questions to a fresh-context reviewer.

When reported beside color-theory checks, prefix this checklist's test IDs as VD-T1 through VD-T12; these local checklist IDs remain T1–T12. (derived: run-2 dogfood, finding row 4's collision between visual-design and color-theory test IDs)

## Tests

| # | Test | Pass condition | Return to |
|---|---|---|---|
| T1 | Message and audience | A fresh viewer can state the intended message and likely audience from the artifact, consistent with the brief. For a deliberately abstract artifact, the viewer identifies the intended category or reading rather than guessing an unrelated one. | Stage 1: brief and intent |
| T2 | Concept and abstraction | The artifact uses the brief's stated literal/subjective and figurative/abstract positions; required content remains recognizable at the chosen level. | Stage 2: research and concept |
| T3 | Form and figure-ground | The intended grouping is readable at thumbnail size. Any figure/ground ambiguity is deliberate and described in the brief. | Stage 3: form and unity |
| T4 | Grid alignment | Every element declared as grid-bound aligns with its declared grid anchor within the default tolerance. Non-grid elements are either exempted or intentionally placed. | Stage 4: composition and movement |
| T5 | Visual balance | The measured weight centre is reported relative to the frame centre. It passes the default when a centred/calm composition is intended; otherwise the independent reviewer confirms that the off-centre arrangement reads as balanced for the stated purpose. | Stage 4: composition and movement |
| T6 | Negative space | The measured negative-space ratio is within the declared target interval, and a fresh viewer confirms that the spaces group, separate or pace content rather than look accidental. | Stage 4: composition and movement |
| T7 | Type scale | The declared adjacent hierarchy levels meet the default type-scale ratio, and the reviewer can distinguish each level at intended output size. | Stage 5: type and system |
| T8 | Focal-area dominance | The measured focal-area contrast-energy share meets the default; a fresh viewer reports the intended focal element first or describes a deliberately different entry point from the brief. | Stage 4: composition and movement |
| T9 | Movement and reading path | The reviewer traces the intended entry point and endpoint without being diverted by an unrelated element. If a complex or crossing path is intended, its purpose is stated. | Stage 4: composition and movement |
| T10 | Typography and rendering | Render-kit reports no unresolved applicable failure for overflow, font fallback or text collision; text is correct and readable at its actual size. Any skipped/incomplete relevant check is reported, not passed. | Stage 5: type and system |
| T11 | System consistency | Every declared constant appears in all required variants; each variable changes only within its stated range; a reviewer can recognize the pieces as one system. Report n/a when no variants are required. (derived: run-2 dogfood, finding row 5's one-off artifact applicability gap) | Stage 5: type and system |
| T12 | Hardest application | Required elements are legible in the most constrained application at its actual minimum size, and every required format/support is represented. | Stage 6: medium and variants |

## Course checks behind these tests

- The course reviews clarity, balance, contrast, unity and salience, with examples for identity, posters, magazine covers, book covers, editorial interiors and web composition. (5642 · U4 · L47 · 00:09–01:37; 5642 · U4 · L47 · 01:37–02:44; 5642 · U4 · L47 · 02:45–03:35; 5642 · U4 · L47 · 03:35–04:53; 5642 · U4 · L47 · 04:53–05:55; 5642 · U4 · L47 · 05:56–06:29; 5642 · U4 · L47 · 06:29–07:15; 5642 · U4 · L47 · 07:15–08:42)
- Balance checks ask whether the composition pulls to one side; ambiguity checks ask whether an element is nearly but not exactly centred. (5642 · U2 · L19 · 00:00–02:16; 5642 · U2 · L19 · 02:16–04:28)
- The eye's path, weight and unity can be read and tested through reorientation, counterweights and single-versus-combined paths. (5642 · U5 · L75 · 00:06–00:58; 5642 · U5 · L75 · 00:58–02:04; 5642 · U5 · L75 · 02:14–03:15; 5642 · U5 · L75 · 03:15–03:27; 5642 · U5 · L75 · 03:27–04:14; 5642 · U5 · L75 · 04:14–04:40; 5642 · U5 · L75 · 04:40–05:23; 5642 · U5 · L75 · 05:23–06:23; 5642 · U5 · L75 · 06:23–06:39; 5642 · U5 · L75 · 06:39–07:37; 5642 · U5 · L75 · 07:37–08:27; 5642 · U5 · L75 · 08:27–09:22; 5642 · U5 · L75 · 09:22–10:34; 5642 · U5 · L75 · 10:34–11:56; 5642 · U5 · L77 · 09:00–09:22; 5642 · U5 · L77 · 09:22–09:53; 5642 · U5 · L77 · 09:53–11:04; 5642 · U5 · L77 · 11:04–11:25; 5642 · U5 · L77 · 11:25–11:49; 5642 · U5 · L77 · 11:49–12:03; 5642 · U5 · L77 · 12:03–12:34; 5642 · U5 · L77 · 12:34–13:19; 5642 · U5 · L77 · 13:19–13:34; 5642 · U5 · L77 · 13:36–14:24; 5642 · U5 · L77 · 14:24–15:03)
- The course shows a mark on a constrained spine, an avatar and responsive formats; it also recommends an identity that is easy to apply and templates/examples for colleagues. (5642 · U7 · L96 · 01:48–02:32; 5642 · U7 · L103 · 02:24–03:14; 5642 · U7 · L103 · 03:14–04:24; 5642 · U7 · L103 · 04:24–05:43; 5642 · U7 · L104 · 01:01–01:17; 5642 · U7 · L104 · 01:17–01:30)

The course does not give universal numeric thresholds for T4–T12. Numeric defaults in [measurement.md](measurement.md) are choices made by this skill; a threshold is a screen for review, not a substitute for judgment.

After any layout, shape or hierarchy change, rerun T3–T9 as applicable. After a type or system change, rerun T7 and T10–T12 as applicable. Recheck all render-kit code failures after every fix.
