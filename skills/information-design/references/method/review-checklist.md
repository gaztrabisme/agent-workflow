# Review checklist: ten tests for a data graphic

Run code checks first, then give the render and specific questions to a fresh-context reviewer who did not make the artifact and can see images. When vision review is unavailable, report those tests as **not judged**.

| # | Test | Pass condition | Return to |
|---|---|---|---|
| T1 | Reader and question | Audience, reader question, use context and medium are explicit; a reviewer can tell what the view is for. | Stage 1: brief |
| T2 | Source and provenance | Every displayed field traces to a named source and definition; no unresolved value or join mismatch remains. | Stage 2: source and data |
| T3 | Selection and missingness | Period, included population, filter, exclusions, substitute years and missing values are documented where relevant. | Stage 2: source and data |
| T4 | Story structure | One primary question and answer lead; each supporting layer has a stated role and does not replace the main answer. | Stage 3: story structure |
| T5 | Chart and channel fit | Chart type and visual channels match the reader task, field types and required precision; deliberate ordinal positions are labelled as order/rank. | Stage 4: chart and encoding |
| T6 | Data-to-mark fidelity | Rendered marks, labels, scales and units agree with the source values and documented transformations. | Stage 4: chart and encoding |
| T7 | Key and context | Reader can find the title, period, units, source, selection rule and an explanation for every visible encoding. | Stage 5: annotation |
| T8 | Panel comparison and reading order | Comparable panels use consistent domains; a reviewer can follow the intended order without confusing supporting views for the main finding. | Stage 3 or 4: structure or chart choice |
| T9 | Render integrity | All applicable render-kit code checks pass with no unresolved errors, collisions, overflow or data-fidelity failure. | Stage 6: render and review |
| T10 | Reader understanding and delivery | At target size, an unbriefed reader can explain what the artifact shows and its main point; every required output format is present and legible. | Stage 5 or 6: annotation or delivery |

## Reporting a critique

For each failed test report: the test ID, what was measured or seen, its result, the stage to return to and one concrete correction. Separate machine checks from vision judgments. A code pass cannot prove understanding; a vision answer cannot prove source-data accuracy.

After a fix, rerun every affected code check and the vision question for any stage whose data, encoding, annotation or reading order changed.
