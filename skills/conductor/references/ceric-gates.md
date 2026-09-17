# CERIC Gates

`ceric` (`../../ceric/SKILL.md`) is conductor's reading and auditing instrument, wired in as three gates of the flow. The method: pull a document's Claim, Evidence, Reasoning, Implications and Context out as quotes; mark what is missing; keep the hedges. The elements and their boundary rules: `../../ceric/references/elements.md`. The scoring instrument: `../../ceric/references/grading.md`.

## Gate 1 — Ground: read every input as a CERIC hunt

The hunt lands in **`grounded.md`** — beside the Plan Block, or at the wiki path the project uses. Minimal shape: one section per input document, each carrying Claim / Evidence / Reasoning / Context / Implications / MISSING, closing with the `Grounded:` line.

Every input document — the brief, the RFP, the prior wiki, a subagent's report — is read as a hunt, not skimmed:

- What it **claims**.
- On what **evidence**.
- By what **reasoning**.
- What came before it (**context**), and what it expects next (**implications**).
- What is **MISSING** — an element the document should supply and does not.

The missing register becomes the Plan Block's `DECIDE NOW` list and the questions handed to the lanes. A gap noticed while grounding and not written down is a gap the run rediscovers later at full price.

## Gate 2 — Converge: audit the synthesis before it lands

The object under audit is named by the run's shape: research → the synthesis; personas → the objection register; build → the run report and the ledger's claims, never the code. That is how this gate squares with `convergence.md`'s "each unit's own gates; conductor does not re-judge them": the unit's gates judge the work, Gate 2 audits what the run asserts about it.

Before the converged artifact lands, run the `ceric` audit on it. Every claim gets a row:

| Claim | Evidence | Reasoning | Hedge | Verdict |
|---|---|---|---|---|

Verdicts: **supported** · **evidence only** (no reasoning) · **assertion** (no evidence) · **overstated** (hedge dropped).

The three convergence failure modes are the three bad verdicts:

- **Stapling** = claims without reasoning: each thread's findings survive side by side and nothing connects them.
- **Averaging** = claims without evidence: the merged number nobody sourced.
- **Overstated** = a hedge dropped: "consistent with" became "is".

A claim that fails is not merged. It is listed as open, with what would settle it.

## Gate 3 — Close: the UAT audit

Close audits the artifacts against the goal file's UAT column and nothing else (`goal-file.md`). A criterion that fails is reported as failed, never re-worded.

## Scale to stakes

Per the core kernel's cold-review rule: the audit is skippable for an internal, reversible synthesis, and never skippable for anything a client, investor or contract will test. When you skip it, say so out loud.
