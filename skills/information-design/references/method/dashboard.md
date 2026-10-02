# Dashboard composition (derived: dogfood 2026-10-02, F2)

Use this method when one composed screen combines status, key numbers, alerts and multiple data views. It extends the six-stage chart method; it does not replace the reader brief, source ledger, chart decisions or render review.

## Compose for a short operational read

1. Put the subject, reporting period and current state in a status line.
2. Give every key-number tile a named measure, value, unit, period and comparison baseline. If a target or comparison is unavailable, say **Not set** or **No baseline set**. Do not let an omitted target look like zero or a normal state.
3. Order alert items by operational severity and action priority. Each alert includes a severity word, what happened, why it matters or its cause, and the next action. Make severity legible through words and shape as well as colour; follow color-theory's functional-color signal policy for palette and signal semantics.
4. Give missing data its own state: name the missing field, explain what cannot be compared or shown, and say what source or action would restore the view. Never draw an absent plan or limit as if it were zero.
5. Align panels that share a physical scale. For depth tracks, use the same depth domain, axis direction and pixel range so a depth appears at the same vertical position in every view. If units or domains differ, show separate axes and do not imply direct alignment.
6. Keep one primary answer visually first. Supporting panels should answer a named follow-up question without competing with the status or main view.

## Dashboard checks

- **Key-number completeness (T2):** every displayed number has a unit, period and baseline, or explicitly says the baseline is not set; its source and definition are traceable.
- **Alert actionability (T7):** every alert has a severity word, cause or reason, and next action; colour is not the only severity cue.
- **Missing-data honesty (T3):** unavailable plan, target, limit or source data is explicit and includes a useful recovery step.
- **Cross-view alignment (T8):** any panels intended for direct comparison share domain, direction and pixel range; the primary answer reads before secondary detail.

These checks apply alongside T1–T10 in [review-checklist.md](review-checklist.md). For value and chroma review on charts or dashboards, assess the plotted data layer and data categories separately from text, borders and panel decoration. Mark the primary plotted layer with `data-rk-focal="data-graphic"` and use render-kit's data-graphic thresholds when available; report any undecidable result as inconclusive rather than as a pass. (derived: dogfood 2026-10-02, F3)
