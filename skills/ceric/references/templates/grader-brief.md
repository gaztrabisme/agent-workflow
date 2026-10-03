# Grader brief — template

Hand this to a fresh-context agent. It gets the run, the source and the instrument; it does not get the reader's reasoning or any other grader's output.

> You are grading a CERIC read of `<source>` written by someone else. You have not seen it before and you do not know who wrote it. Grade it cold against the source, using the instrument in `<skill>/references/grading.md` and the element boundaries in `<skill>/references/elements.md`.
>
> **Inputs.** The run: `<run_dir>` (read every file). The source: `<alias=path>`; use page-marked text and rendered pages when it has pages, or the authoritative source text when it does not. The mechanical check output: `<ceric_check output>`. `<If a key exists: the gold digest at <gold.md>, sections <n>; use it for content coverage and boundary rulings, not as a script.>`
>
> **Scope.** Grade `<which activity / which element group>`. Do not grade anything else.
>
> **Method.** (1) For each element, decide ✓ ○ ✗ against the source; write the one-line reason and cite the run's line and the source's page, line range, or section that proves it. Apply the boundary rules literally — collected or built is Evidence, measured or derived is Reasoning, the source's own assertion is a Claim, future work is an Implication, the gap is Context. (2) Fill the five failure-mode rows; each PASS or FAIL carries its evidence line (a quote, a line number, a check output). (3) Check the missing register against the source both ways: listed absences that are actually present, and absent content presented as found. (4) Note every quotation in the run that the mechanical check flagged, and say whether the rendered page or authoritative text settles it.
>
> **Do not** reward volume, style or effort. Do not penalise a reader for keeping a hedge the key dropped. Do not resolve a doubt in the reader's favour; write the doubt down as a finding with the line.
>
> **Deliverable** (structured): `scores` — one row per element `{element, mark, reason, run_line, source_locator}`; `failure_modes` — five rows `{mode, verdict, evidence}`; `coverage` — for a main-text hunt, which of the key's items are present, absent, or contradicted; `findings` — ranked most-severe-first, each `{severity, claim, quote_from_run, location, fix}`; `what_worked` — 2–4 things the read did that a reader should copy.
