# Claim audit

Writer: codex
Auditor: glm
Round: 1

Scope: citations in `references/method/render-and-check.md`, `references/method/review-checklist.md`, `references/method/slide-design.md`, `references/method/story-and-structure.md`. One row per unique (file, anchor) pair. Anchors are quoted exactly as cited; where a pair is cited for more than one sentence, the verdict is the lowest of its uses and the Note separates them.

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | references/method/render-and-check.md | [book:playwright-docs], “Accessibility testing” | Read each skipped/incomplete item; a reviewer without the render leaves vision items not-judged. | supported | The section's disclaimer — automated tests detect only some common problems, "many accessibility problems can only be discovered through manual testing" — grounds the not-judged rule; the fail/skipped/incomplete vocabulary comes from the co-cited render-kit loop, not this book. |
| 2 | references/method/render-and-check.md | [src:output-pipelines/report.md], “F8. Editable PowerPoint from code” | Check rendered output and reopen PPTX structurally; a LibreOffice render is not proof of PowerPoint. | supported | F8: LibreOffice "is a usable automated check for overflow and layout, not proof of PowerPoint rendering"; generated PPTX objects (charts, workbook series) were read back structurally. |
| 3 | references/method/review-checklist.md | [book:storytelling-with-data], “Who, what, and how” | T1–T4 adapt the audience and outcome practices. | supported | Section: be clear on to whom you communicate and what you want the audience to know or do before visualizing. |
| 4 | references/method/review-checklist.md | [book:storytelling-with-data], “The 3‐minute story & Big Idea” | T1–T4 adapt the short-story practice. | supported | Section: the 3-minute story removes dependence on slides or visuals; the Big Idea is a single concise sentence. |
| 5 | references/method/review-checklist.md | [book:storytelling-with-data], “Storyboarding” | T1–T4 adapt the storyboard practice. | supported | Section: a low-tech visual outline of planned content, changeable before content is created. |
| 6 | references/method/review-checklist.md | [book:playwright-docs], “Accessibility testing” | Automated accessibility scans cannot find every issue. | supported | Disclaimer: automated tests detect some common problems; many problems are only discovered through manual testing. |
| 7 | references/method/review-checklist.md | [src:output-pipelines/report.md], “F5–F9” | T11–T18 reflect the research's medium-specific limits and owner checks. | overstated | The report has no "F5–F9" section; findings F5–F9 do record MP4/PDF/PPTX/app-capture limits (T11–T14, T16–T18), but the caption/narration checks in T15 come from F4 ("Audio: narration, timestamps, captions, music, loudness"), which the citation skips; owner checks sit in the co-cited scene-engine guide. |
| 8 | references/method/slide-design.md | [book:storytelling-with-data], “Chapter 5: think like a designer” | Audience and message drive design choices; decoration that does not help can be removed. | supported | Chapter: form follows function (what the audience must do determines the form); "if they don't support the message, they don't serve the purpose of communication". The prohibition on fixed font scales/recipes is the writer's own and is labelled derived. |
| 9 | references/method/slide-design.md | [book:whatwg-html], “Conformance requirements for authors” | Use meaningful headings and sequence in HTML instead of hiding content in a bitmap. | overstated | The section argues presentational markup leads to poorer accessibility and that semantic, media-independent markup works for more users; it never discusses headings, sequence, or bitmap-embedded communication. "Preserves content beyond the pixels" is labelled derived. |
| 10 | references/method/story-and-structure.md | [book:storytelling-with-data], “The 3‐minute story & Big Idea” | Write a spoken version and one-sentence point before slides; return to the brief if unstateable. | overstated | "Build the sequence" (supported): the 3-minute story removes dependence on slides and the Big Idea boils the so-what to one sentence, articulated before content creation. "Return when" (overstated): the section requires a stateable point and known outcome but says nothing about returning to a brief, slide jobs, or caveat placement. |
| 11 | references/method/story-and-structure.md | [book:storytelling-with-data], “Storyboarding” | Low-cost changeable outline; conclusion-first is a choice; return to the brief on defects. | overstated | Supported for the low-cost changeable outline ("rearrange (and add and remove) the pieces", attachment warning) and for presenting conclusion-at-end vs leading as a choice. Overstated for the per-slide job/claim/source/evidence/transition/caveat list and the return triggers: the section prescribes a low-tech outline plus early stakeholder acceptance "in line with the need", not per-slide field notes or repair routing. |
| 12 | references/method/story-and-structure.md | [book:storytelling-with-data], “Who, what, and how” | Put background, definitions, and appendix material where the audience can reach it. | overstated | The section sets who/what/how before visualizing and discusses how much detail belongs in the communication by mechanism (presenter present vs audience consuming alone); it gives no placement advice. The appendix advice appears in Chapter 5 ("push content to the appendix"); qualifier adjacency is labelled derived. |
| 13 | references/method/story-and-structure.md | [book:articulating-design-decisions], “Chapter 7. Choose a Message” | Note each planned slide's job, claim, source, evidence, transition, and caveat. | overstated | The chapter catalogues messages for justifying design decisions to stakeholders (business, design, research, limitations categories) and prescribes no per-slide story notes; "attach evidence and transition to each slide's job" is labelled derived, but source and caveat fields are not. |
| 14 | references/method/story-and-structure.md | [book:articulating-design-decisions], “Limitations” | Keep limitations and qualifiers near the statements they qualify. | unsupported | The section teaches three stakeholder justifications — "Not enough resources", "Limited by technology", "Complies with a standard" — and says nothing about where limitation material is placed in a document or deck. |

No citation in this scope uses a `[doc:https://…]` live-document source.

## Portability check

```
$ grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' .../SKILL.md .../references/method
(no matches; grep exited 1)
```

## Citation count

`check_claims.py … --sources` reports "64 citations" for the whole skill; the 40 unaudited rows it prints are capped before this scope's files. This table covers all 14 unique (file, anchor) pairs in the four in-scope method files (18 citation occurrences).
