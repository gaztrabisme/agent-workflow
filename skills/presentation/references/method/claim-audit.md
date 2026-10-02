# Claim audit

This audit keeps the source-backed method claims, owner-profile observations, field rules carried forward, and tool contracts distinct. The evidence index is in [audit/evidence.md](../../audit/evidence.md); package scope and exclusions are in [audit/README.md](../../audit/README.md).

## Source decisions

| Claim used | Source and support | Limit carried into the skill |
|---|---|---|
| Audience/outcome precede visualization; concise point and outline guide the story | [book:storytelling-with-data], “Who, what, and how”; “The 3‐minute story & Big Idea”; “Storyboarding” | Story order is a choice for the audience, not a universal formula. |
| Explain design choices in relation to goals, use, and constraints | [book:articulating-design-decisions], “Chapter 7. Choose a Message”; “Limitations” | A reasoned design case does not prove the audience will agree or that an outcome will occur. |
| Keep composition, color, chart semantics, product copy, and motion with their specialist owners | [visual-design/SKILL.md](../../../visual-design/SKILL.md); [color-theory/SKILL.md](../../../color-theory/SKILL.md); [information-design/SKILL.md](../../../information-design/SKILL.md); [ux/SKILL.md](../../../ux/SKILL.md); [motion/SKILL.md](../../../motion/SKILL.md); [frontend/SKILL.md](../../../frontend/SKILL.md) | These links define skill boundaries, not empirical claims about quality. |
| The owner's visual profile is provisional | [brand-profile README](../../../../brand-profile/README.md); [brand-profile PROFILE](../../../../brand-profile/PROFILE.md), “Evidence and confidence” | Evidence is one poster and one deck; 10–20 additional references and owner review are still pending. |
| Fixed-size HTML scenes can feed separate PDF and native PPTX paths | [src:output-pipelines/report.md], “Use case 1”; “F6”; “F8”; “F8b”; [src:output-pipelines/experiments/README.md], “04-pptx-native” and “05-html-pdf” | PPTX files were structurally read and rendered through LibreOffice, not PowerPoint. |
| A single universal HTML presenter shell is not established by the research | [src:synthesis.md], “Contradictions”; [src:output-pipelines/report.md], “F7” | Select a static or presenter shell based on required presentation features; retain the disagreement as open. |
| App capture should use the app itself where practical | [src:output-pipelines/report.md], “F9” | The measured path used a stand-in app, not real Angular/React/Vue applications. |
| Rendered output needs code checks and visual judgment | [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop”; [book:playwright-docs], “Accessibility testing” | Render-kit does not make model or human vision judgments; manual review is required for questions code cannot answer. |
| HTML should retain meaningful document structure; media may require captions | [book:whatwg-html], “Conformance requirements for authors”; [book:wcag-22], “Success Criterion 1.2.2 Captions (Prerecorded)”; [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface” | Agent-interface benchmark results are not treated as evidence of human comprehension or slide quality. |
| MP4 stream settings are verifiable through metadata | [src:output-pipelines/report.md], “F5”; [src:output-pipelines/experiments/README.md], “01-mp4-for-powerpoint” | The settings were measured; playback inside PowerPoint was not verified by the study. |
| PowerPoint and Keynote compatibility needs named owner checks | [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks” | `owner-check` is a pending manual status, not a pass. |

## Carried field rules

- Keep the first render in bug-hunt mode; inspect for overlap, overflow, wrapping, contrast, and leftover placeholders, then fix and recheck affected slides. (field rule (pptx))
- Inspect decoded video frames, distinguish mockups from live applications, and ensure captions/narration do not imply unmeasured speed or latency. (field rule (screencast))
- Apply these as QA and representation controls, not as a fixed aesthetic recipe or an automatic signoff. (derived: the new skill routes aesthetics to the owner's design skills and requires artifact evidence.)

## Open claims

- A successful PPTX reopen or LibreOffice render does not establish how current PowerPoint or Keynote will render, repair, animate, edit, or play the file. [src:output-pipelines/report.md], “Risks and unknowns”; [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”.
- A successful app-capture run against the stand-in does not establish coverage for every production app, WebGL/canvas surface, backend, or locale. [src:output-pipelines/report.md], “F9”; “Risks and unknowns”.
- Vision items remain open until a reviewer with access to the rendered artifact answers the specific question; a tool report cannot settle them. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop”.
