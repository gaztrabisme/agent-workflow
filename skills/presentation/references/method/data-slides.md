# Data slides

## Specify meaning before appearance

Give information-design the reader's question, trusted source, fields, selection rule, units, time span, missing values, and intended comparison before the chart is styled. The receiving skill makes chart form and data mapping decisions from the reader's task and source data. [information-design/SKILL.md](../../../information-design/SKILL.md#principles--anchoring-rules); [book:storytelling-with-data], “Who, what, and how”.

Keep every mark tied to a data role and preserve whether position shows value, rank, or order; show units, time span, selection, exceptions, and source with the graphic. [information-design/SKILL.md](../../../information-design/SKILL.md#principles--anchoring-rules); [book:storytelling-with-data], “Chapter 2: choosing an effective visual”.

Use a title or annotation that tells the reader what to notice, and remove decoration that competes with the data or the main point. [book:storytelling-with-data], “Chapter 3: clutter is your enemy!”; [book:storytelling-with-data], “Chapter 4: focus your audience’s attention”.

## Preserve data through export

Keep chart semantics and source values in structured form so an export can preserve a real chart object when editability is required. The tested native-PowerPoint subset uses native charts with an embedded workbook; the fallback is documented per slide when the design cannot map to a native object. [src:output-pipelines/report.md], “F8. Editable PowerPoint from code”; [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”.

Do not infer that a chart is editable from how it looks. Verify its data object and workbook structure after export, and disclose any chart rendered as an image. [src:output-pipelines/experiments/README.md], “04-pptx-native”; [information-design/SKILL.md](../../../information-design/SKILL.md#anti-patterns). (derived: visual similarity does not establish retained chart semantics.)

## Return when

Return a disputed chart form, field mapping, or data caveat to information-design; return placement, hierarchy, or surrounding style to visual-design; return palette meaning to color-theory. [information-design/SKILL.md](../../../information-design/SKILL.md#composition); [visual-design/SKILL.md](../../../visual-design/SKILL.md#composition); [color-theory/SKILL.md](../../../color-theory/SKILL.md#composition).
