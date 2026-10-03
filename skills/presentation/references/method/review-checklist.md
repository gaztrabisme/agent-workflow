# Review checklist

Run only tests that apply to the requested output. Mark each result **pass**, **fail**, **not judged**, **skipped**, or **incomplete**; identify its repair stage and evidence in [measurement.md](measurement.md). A non-applicable output test is skipped with a reason.

| ID | Check and pass condition | Check type | Return stage |
|---|---|---|---|
| T1 | The audience, intended outcome, setting, evidence, limitations, and requested media are recorded. | Brief review | Brief and audience |
| T2 | The main point fits in one sentence, and the short spoken story supports it. | Vision: “Can I state the intended point and why it matters after reading the brief?” | Story and structure |
| T3 | Each factual claim can be traced to supplied evidence; assumptions and unsupported claims are identified. | Source audit | Brief, story, or data slides |
| T4 | Each slide has a clear job and the sequence builds or reveals the point in an intentional order. | Vision: “Does each slide move the explanation forward?” | Story and structure |
| T5 | The governing identity is named; the owner's profile is marked draft if used; visual and color decisions came from their owners. | Source/profile review | Slide design |
| T6 | The focal point and reading order support the slide's job without competing decoration. | Vision: “What do I notice first, and does it match the slide's point?” | Slide design |
| T7 | Text, charts, notes, or captions remain legible at the intended viewing or listening size. | Vision: “Can I read or follow the important content at its actual delivery size?” | Slide design or output by medium |
| T8 | Chart values, units, labels, selection, time span, and source match the source data. | Data reconciliation plus vision | Data slides |
| T9 | Meaning is not carried by color alone; structure and text have meaningful order; applicable contrast checks pass. | Render-kit and access review | Slide design or data slides |
| T10 | Applicable render-kit checks have no unresolved `fail`; every `skipped` or `incomplete` result is understood and recorded. | Code: `rk check` | Slide design or output by medium |
| T11 | PDF page count and dimensions match the slide set; fonts and tags are inspected; any PDF/UA claim has separate evidence. | Code plus visual review | Output by medium |
| T12 | Reopened PPTX contains the expected native text and shape objects; picture fallbacks are listed. | Code: python-pptx reopen | Output by medium |
| T13 | Charts expected to be editable reopen as native charts with their expected series and values. | Code: python-pptx reopen | Data slides or output by medium |
| T14 | MP4 matches the agreed codec, profile, pixel format, dimensions, frame rate, range, color tags, and audio stream. | Code: ffprobe | Output by medium |
| T15 | Required caption sidecar exists, cues are ordered, narration matches the approved script, and audio is intelligible. | Code plus listening review | Output by medium |
| T16 | A demo represents the stated app state, uses approved fixtures, and does not imply a mockup or synthetic data is live. | Vision and fact review | Brief or output by medium |
| T17 | Requested PowerPoint/Keynote owner checks are recorded by app and build; an `owner-check` result is not reported as pass. | Owner check | Delivery and editability |
| T18 | Every requested deliverable exists, its companion files are listed, and the final report separates pass, fail, not-judged, skipped, incomplete, and owner-check results. | File and report review | Delivery and editability |

T1–T4 adapt the audience, outcome, short story, and storyboard practices. [book:storytelling-with-data], “Who, what, and how”; [book:storytelling-with-data], “The 3‐minute story & Big Idea”; [book:storytelling-with-data], “Storyboarding”.

T5–T10 route visual-system and chart decisions to their owners and use render-kit for mechanical checks; automated accessibility scans cannot find every issue. [visual-design/SKILL.md](../../../visual-design/SKILL.md); [information-design/SKILL.md](../../../information-design/SKILL.md); [color-theory/SKILL.md](../../../color-theory/SKILL.md); [render-kit AGENTS.md](../../../../tools/render-kit/AGENTS.md); [book:playwright-docs], “Accessibility testing”.

T11–T18 adapt the output research's audio, MP4, PDF, PowerPoint, and app-capture findings, plus the scene-engine owner checks, into review prompts. [src:output-pipelines/report.md], “F4. Audio: narration, timestamps, captions, music, loudness”; [src:output-pipelines/report.md], “F5. MP4 for PowerPoint, embedding, native motion and fonts”; [src:output-pipelines/report.md], “F6. HTML to PDF with Chromium”; [src:output-pipelines/report.md], “F8. Editable PowerPoint from code”; [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”; [src:output-pipelines/report.md], “F9. Capturing demos of real apps with source access”; [scene-engine AGENTS.md](../../../../tools/scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”. (derived: the checklist translates these source limits into checks for the requested deliverables.)
