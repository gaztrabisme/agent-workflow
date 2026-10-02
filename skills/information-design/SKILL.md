---
name: information-design
description: "Designs data graphics from question and dataset through chart choice, encoding, annotation, narrative and checked SVG or HTML. USE WHEN creating or reviewing charts, infographics, dashboards or data stories. visual-design owns broader composition and type; color-theory owns palette decisions; ux owns interactive product flows and UX writing. Keywords: information design, chart choice, data visualization, infographic, dashboard, data story, SVG chart, legend, annotation."
license: "Proprietary (private course-derived material, not for redistribution)"
---

# Information Design

This skill turns a reader's question and a trustworthy dataset into an explained, rendered data graphic. It supports charts, infographics, dashboards and data stories in SVG, composed into HTML where needed. The method is distilled from four courses; each course claim remains anchored in its lesson. Domain conventions govern the final chart and terminology.

> Inherits the `core` kernel. See [../core/SKILL.md](../core/SKILL.md); use its shared gates rather than copying their definitions.

## When it fires — and when a sibling owns it

- **This skill:** choosing and encoding charts; making infographics and data stories; explaining data through titles, labels, legends and annotations; reviewing rendered data graphics.
- **`visual-design` instead:** broad composition, typography, grids and visual systems. Keep chart semantics here and hand off broader form decisions.
- **`color-theory` instead:** palette, colour meaning, ramps, contrast and color-vision checks. This skill states what a colour encodes; color-theory decides and measures the palette.
- **`ux` instead:** product interaction flows and UX writing. This skill specifies what a chart must explain; ux owns the wider interactive experience and interface copy.

> **Disambiguation by artifact:** the chart, its data mappings and its explanatory key belong here; surrounding graphic composition, palette decisions and product interaction belong to the named siblings.

## Principles / anchoring rules

1. **Start with the reader's task and use context.** Data properties, reader needs, purpose, context and medium shape the visual form. (4217 · U2 · L04 · 00:00–01:08; 4217 · U2 · L04 · 02:25–03:22)
2. **Treat selection as a design decision.** Keep the rule, years, units, source and exceptions visible to readers. (2495 · U2 · L05 · 02:55–04:17; 2495 · U4 · L15 · 08:18–10:30; 4217 · U2 · L05 · 03:40–04:39)
3. **Test a visual idea against the data.** Sketching exposes structure; plotting determines whether it works. Revise the idea when it obscures the measure or story. (3601 · U3 · L09 · 17:37–18:45; 2495 · U4 · L10 · 05:08–06:30)
4. **Give every mark an explicit data role.** Distinguish the main measure from context, and state whether position shows value, rank or order. (2495 · U3 · L09 · 01:08–02:33; 2495 · U4 · L11 · 01:31–02:46; 2495 · U4 · L11 · 02:46–04:21)
5. **Write the key for the reader.** Explain marks, units, time span and selection in the order they are encountered; do not assume a chart explains itself. (2495 · U4 · L15 · 00:00–01:26; 4217 · U4 · L17 · 01:31–05:16; 4217 · U4 · L17 · 05:16–10:59)
6. **Render, measure, then ask a reader.** Check exact properties in code before using a fresh-context vision review for comprehension and visual judgments. (Owner decision 4; 3069 · U4 · L13 · 00:00–01:30; 3069 · U4 · L13 · 01:30–02:38)
7. **Domain conventions govern course taste.** Keep reusable chart logic general and put domain-specific components in the project. (Owner decision 6)

## The flow (at a glance)

| Stage | Decide | Check | Reference |
|---|---|---|---|
| 1. Brief | Reader, question, action, context and medium | Each is named before chart selection | [brief.md](references/method/brief.md) |
| 2. Source and data | Source reliability, fields, units, years, missingness and scope | Raw source is retained; selections and joins reconcile | [source-and-data.md](references/method/source-and-data.md) |
| 3. Story structure | Main finding, supporting layers, order and optional metaphor | One primary question remains answerable | [story-and-structure.md](references/method/story-and-structure.md) |
| 4. Chart and encoding | Chart form, variables, channels, scales and actual-value versus rank treatment | Encodings map to the intended fields and precision | [chart-and-encoding.md](references/method/chart-and-encoding.md) |
| 5. Annotation | Title, key, labels, units, dates, selection and source notes | A reader can decode every mark and caveat | [annotation-and-narrative.md](references/method/annotation-and-narrative.md) |
| 6. Render and delivery | SVG or HTML, target sizes and export format | Code checks pass before vision review; results are reported | [render-and-review.md](references/method/render-and-review.md) |

### Scale the flow

- **Quick chart question:** stages 1 and 4; name the reader's comparison and the field mapped to each channel.
- **Critique of existing work:** start at stage 6, run T1–T10 in order, then return to the stage named by each failure.
- **Multi-chart dashboard or data story:** run all six stages, then apply the [dashboard method](references/method/dashboard.md); check shared scales, key numbers, alerts, missing-data states, ordering and labels together. (derived: dogfood 2026-10-02, F2)
- **After a fix:** rerun affected code checks, then the vision questions for the repaired stage and any stage whose reading order changed.
- **Domain-specific work:** apply the course-derived method to the brief, then follow the domain's required units, axis directions, terms and thresholds.

## Execution

### Output medium

- Use SVG for marks, diagrams and visualizations; compose multiple views and their explanatory text in HTML. (Owner decision 7)
- Use raster images only for photographs or textures. Follow the project delivery format when it overrides the working medium.
- Keep source data, units and field mappings with the editable artifact or its adjacent data record. Do not leave sample values looking like operational data.

### Chart templates

Templates use render-kit markup and are examples to adapt. The four drilling examples are marked **derived** because the courses do not teach drilling charts.

- [Template index](templates/README.md) — choose a starting form and see its source or derived status.
- [Line chart](templates/line-chart.svg) — sequential measures over time; use the derived drilling template for depth against report date. (derived: dogfood 2026-10-02, F6)
- [Bar chart](templates/bar-chart.svg) — category comparisons and lost-time split (**derived** drilling example).
- [Slope chart](templates/slope-chart.svg) — start-to-end change.
- [Small multiples](templates/small-multiples.svg) — repeated comparisons on a shared scale; adapted for mud properties (**derived** drilling example).
- [Scatterplot](templates/scatterplot.svg) — two quantitative fields; adapted for a trajectory view (**derived** drilling example).
- [Bubble chart](templates/bubble-chart.svg) — two positional fields plus size.
- [Radial series](templates/radial-series.svg) — a custom repeated time-series form; preserve the reference scale and key, then manually review its polar mapping where render-kit skips fidelity.
- [Drilling depth against time](templates/drilling-depth-time.svg), [lost-time split](templates/drilling-lost-time-split.svg), [mud properties](templates/drilling-mud-properties.svg) and [trajectory](templates/drilling-trajectory.svg) — derived domain views.
- [Dashboard](templates/dashboard.html) — composed status, metric, alert, missing-data and aligned-chart example (**derived** from dogfood findings F2 and F3). (derived: dogfood 2026-10-02, F2)

### Render-and-check loop

1. Mark the chart root with `data-rk-chart`, scale type, domain and range; give marks `data-rk-mark` and their source values. Use `data-rk-series` only for true color-coded categories, not one series name per bar or observation. Put `data-rk-stage` on the complete SVG root or rendered screen region. Use the render-kit markup contract. (derived: dogfood 2026-10-02, F1)
2. For charts and dashboards, interpret value and chroma results in the context of the data layer: value helps assess emphasis within the plotted marks, while chroma tests distinguishability only where colour carries category meaning. Declare the primary data view with `data-rk-focal="data-graphic"` when render-kit supports it; report tool thresholds and inconclusive results without calling them passes. (derived: dogfood 2026-10-02, F3)
3. Until render-kit treats stroked geometry as visible for colour-vision checks, include visible area swatches for declared categories so the check has a measurable region. (derived: dogfood 2026-10-02, F5)
4. Render the HTML or SVG through render-kit and run `bin/rk check`. Fix every applicable failure and render again. Read each `skipped` or `incomplete` result; it is not a pass. (Owner decision 4; render-kit agent instructions)
5. Run code checks first: resources, console errors, font fallback, overflow, text collisions, contrast, colour-vision deficiency, data fidelity, accessibility, value and chroma; PDF font checks apply when a PDF is produced.
6. Send the render and the specific vision questions in [review-checklist.md](references/method/review-checklist.md) to a fresh-context reviewer who did not make it and can see images. For print delivery, include the required PDF as a separate review input and verify its pages and embedded fonts; a PNG alone does not establish PDF delivery or legibility. (derived: dogfood 2026-10-02, F10)
7. Verify answers with render-kit. Without such a reviewer, mark vision checks **not judged**.
8. Report each test as measured, vision-judged, not judged or skipped, including the result, reason and return stage. Code checks cannot establish that the story is understood.

Before adapting a shipped starter, run [scripts/check_templates.sh](scripts/check_templates.sh); it runs `rk check` on every SVG and HTML template. (derived: dogfood 2026-10-02, F1)

## Gates (declared, inherited from core)

- **Grounding gate.** Ground decisions in the brief, source data and lesson anchors. See [../core/references/grounding-gate.md](../core/references/grounding-gate.md).
- **Output Contract.** Deliver an editable SVG or HTML artifact, its source/field record, and a report of T1–T10. See [../core/references/output-contract.md](../core/references/output-contract.md) and [../core/references/wiki-protocol.md](../core/references/wiki-protocol.md).
- **Pushback and teach.** Explain when a requested chart or encoding conflicts with its data, reader task or domain convention, and offer a chart the reader can decode. See [../core/references/pushback-and-teach.md](../core/references/pushback-and-teach.md).

## Anti-patterns (hard no-list)

- Selecting a chart because it is attractive before naming the question, reader and context.
- Treating a cited channel ranking as a universal taxonomy or a chart form as proof of meaning.
- Encoding actual measures as ordinal positions without labelling both the rank and the actual value.
- Using area, angle or intensity for exact comparisons without acknowledging the lower precision described in the course's cited ranking.
- Adding visual layers or metaphor that compete with the central question or have no explicit key.
- Hiding source, units, time period, selection rules, missing values or data exceptions.
- Treating merged rows, copied values or placeholder examples as validated without comparing them with source data.
- Calling code checks a reader-comprehension pass, or calling unavailable vision review a pass.
- Letting course aesthetics override a domain's chart convention or required scale.

## Composition

- **Inherits:** `core`.
- **Works beside:** `visual-design` for composition and type; `color-theory` for palette and colour measurement; `ux` for interaction and UX writing.
- **Domain rule:** this skill owns chart semantics and its immediate key. The project owns specialist terms, domain encodings and operational thresholds.

## References

- [references/method/claim-audit.md](references/method/claim-audit.md) — the independent claim audit of every course citation (evidence per scope in `audit/`).
- [references/method/brief.md](references/method/brief.md) — define the reader, question and use context.
- [references/method/source-and-data.md](references/method/source-and-data.md) — check source, data, joins, selection and missingness.
- [references/method/story-and-structure.md](references/method/story-and-structure.md) — find the story and order its layers.
- [references/method/chart-and-encoding.md](references/method/chart-and-encoding.md) — choose chart forms, channels, scales and mapping rules.
- [references/method/annotation-and-narrative.md](references/method/annotation-and-narrative.md) — write and place explanatory text and keys.
- [references/method/render-and-review.md](references/method/render-and-review.md) — render, review and prepare delivery.
- [references/method/review-checklist.md](references/method/review-checklist.md) — T1–T10 pass conditions and return stages.
- [references/method/dashboard.md](references/method/dashboard.md) — dashboard composition, key-number and alert checks (**derived** from dogfood, not a course method).
- [references/method/measurement.md](references/method/measurement.md) — course procedures, independent checks and thresholds for T1–T10.
- [references/method/coverage.md](references/method/coverage.md) — lessons not cited by a method digest and why.
- [templates/README.md](templates/README.md) — chart-template index and source mapping.
- [questions/information-design-chart.md](questions/information-design-chart.md), [questions/information-design-dashboard.md](questions/information-design-dashboard.md) and [questions/information-design-print.md](questions/information-design-print.md) — ready-to-use, yes-means-pass vision questions (**derived** from dogfood finding F8).
- [scripts/check_templates.sh](scripts/check_templates.sh) — run render-kit checks on all shipped SVG and HTML templates.
- [references/course-2495/README.md](references/course-2495/README.md), [references/course-4217/README.md](references/course-4217/README.md), [references/course-3601/README.md](references/course-3601/README.md), [references/course-3069/README.md](references/course-3069/README.md) — checked source indexes and course-specific exclusions.
- [scripts/check_refs.py](scripts/check_refs.py) — verify package links and course anchors.
