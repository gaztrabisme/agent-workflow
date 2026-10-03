# Computer-Vision Inspection Heuristics

These are practical probes for visual-inspection decisions. They are derived from dogfood (2026-10-01), not a general guarantee that one approach fits every factory.

## Separate measurement from defect detection

- If the decision is a dimensional or color tolerance, first test a calibrated measurement path. Check scale, illumination, optics, field of view, and measurement repeatability before treating it as a learned-classification problem.
- For known defect families, compare a detector or classifier against the current inspection process and a simple baseline.
- For rare or not-yet-enumerated defects, anomaly detection can surface unusual examples; it does not establish that an anomaly is a defect or guarantee recall. Confirm alerts and evaluate recall by defect family at the operating flag rate.

## Check the instrument and reference truth

- Verify pixel resolution across the field of view against the smallest tolerance or feature that drives the decision.
- Check lighting and optics across expected shifts and operating conditions. Dust, lamp ageing, focus, and color drift can change the input without a model change.
- Use a stable reference target or golden sample on a defined cadence; record its measurements and the response to drift.
- If inspectors are both the comparator and the only label source, use the independent-reference protocol in `templates/eval-harness.md`. Inspector agreement alone is not evidence of correctness.

## Worked example

An inspection line has one decision about a measured dimension and another about a surface defect. Validate the dimension with a calibrated gauge and repeatability check; evaluate defect detection separately on confirmed examples, including rare defect families. Check the reference target over operating conditions, then set separate gates for measurement error and defect recall at the chosen flag rate. Do not claim performance on a defect that has no independently confirmed examples.
