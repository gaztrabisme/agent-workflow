# Claim audit

Writer: codex
Auditor: glm
Round: 3

Scope: citations in `references/method/brief-and-audience.md` (the file changed after the round-2 audit). One row per unique (file, anchor) pair; where a pair is cited more than once, the verdict is the lowest of its uses and the Note separates them. Earlier round-2 rows for this file are kept, including the two historical rows for citations removed in round 1; rows for the other five method files remain in `audit/claim-audit-r2-1.md`. Every row was re-checked against the current text and its source; the re-checks that changed or confirmed a round-2 verdict are rows 1, 2, 3 and 8.

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | references/method/brief-and-audience.md | [book:storytelling-with-data], “Who, what, and how” | Record audience, what they should know or do, relationship, and data supporting the point. | supported | Four uses. Section defines who (audience, how they perceive you, the relationship you have with them), what (know or do), how (“What data is available that will help make my point? Data becomes supporting evidence”). Also grounds the acceptance sentence, the derived check-criteria sentence, and the pearls co-citation. |
| 2 | references/method/brief-and-audience.md | [book:storytelling-with-data], “Consulting for context: questions to ask” | Requester questions cover background, audience/decision maker, biases, data, risks, outcome, one-sentence message. | supported | Two uses. The section's bullet list asks exactly this: relevant or essential background, audience or decision maker, biases for or against the message, available data, risks, successful outcome, and the single-sentence version. Also co-cited in the derived check-criteria sentence. |
| 3 | references/method/brief-and-audience.md | [src:output-pipelines/report.md], “Use case 1” | Switch rules: fill a supplied template; never-edited decks ship PDF. | supported | Three uses. “Switch when”: a supplied PowerPoint template is filled via its layouts and placeholders; a never-edited deck skips the native writer and ships PDF. Also grounds the distinct-use-case sentence (use case 1 bundles live presentation, PDF export and editable PowerPoint as one use case with its own defaults and confidence) and the derived file-format and revisit-brief rules. |
| 4 | references/method/brief-and-audience.md | [src:output-pipelines/report.md], “Use case 2” | MP4 app demo is its own use case with different constraints. | supported | Use case 2 (MP4 demo of software, embeddable in PowerPoint) carries its own defaults, switch-when rules and confidence limits. |
| 5 | references/method/brief-and-audience.md | [src:output-pipelines/report.md], “Use case 3” | Narrated explainer is its own use case with different constraints. | supported | Use case 3 (explainer video with narration, captions, music) carries its own renderer, switch-when rules and confidence limits. |
| 6 | references/method/brief-and-audience.md | [src:output-pipelines/report.md], “Risks and unknowns” | Review records confidence limits where checks were structural or stand-ins. | supported | “Not verified here”: playback inside PowerPoint (LibreOffice stood in), real Angular/React/Vue apps (a stand-in app was used), Vietnamese alignment accuracy, Linux GPU effects; the per-use-case Confidence entries repeat the limits (use cases 1–2 not played in PowerPoint, use case 3 voices not listening-tested). |
| 7 | references/method/brief-and-audience.md | [book:storytelling-with-data], “The 3‐minute story & Big Idea” | Write a one-sentence Big Idea. | supported | “The Big Idea boils the so‐what down even further: to a single sentence.” |
| 8 | references/method/brief-and-audience.md | [book:storytelling-with-data], “Exploratory vs. explanatory analysis” | A data exploration is not an audience explanation; present what the audience needs. | supported | Round-3 re-check of the round-2 `overstated`: the section contrasts exploratory analysis (100 oysters, two pearls) with explanatory (a specific thing you want to explain), warns against showing all 100 oysters, and says “Concentrate on the pearls, the information your audience needs to know” — which is all the current anchor now claims. The previously unlabelled “Choose checks…” sentence moved under a (derived: …) label with its own citations (rows 1–2), so the round-2 finding no longer applies. |
| 9 | references/method/brief-and-audience.md | [book:articulating-design-decisions], “Chapter 7. Choose a Message” | Record audience, know/do, relationship, setting, time, evidence, risks, success | unsupported | Removed: this citation no longer appears in the text (unchanged since round 2). Round-1 finding kept for history: the chapter catalogues ready-made stakeholder messages and gives no brief-recording guidance. |
| 10 | references/method/brief-and-audience.md | [book:articulating-design-decisions], “Limitations” | Keep facts, opinions, estimates, assumptions, open questions distinguishable | unsupported | Removed: this citation no longer appears in the text (unchanged since round 2). Round-1 finding kept for history: the section gives three limitation messages for stakeholders, not fact/opinion separation. |

No citation in this scope uses a `[doc:https://…]` live-document source.

## Citation count

`check_claims.py … --sources` reported “66 citations, 66 audited, 1 not supported, 0 unaudited” before this audit, with `FAIL audit is older than: brief-and-audience.md` and `FAIL overstated: references/method/brief-and-audience.md [book:storytelling-with-data], “Exploratory vs`. This table covers all 8 unique (file, anchor) pairs in the in-scope file (16 citation occurrences) plus the 2 historical pairs whose citations were removed in round 1 (rows 9–10). The one non-supported live row (round-2 row 8) was re-checked against the current text and flips to `supported`: the unlabelled conclusion now carries a derived label and its own citations. After this table every live pair in the scope carries `supported`; the only non-`supported` rows are the historical ones (9–10).

## Portability check

```
$ grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' .../SKILL.md .../references/method
(no matches; grep exited 1)
```
