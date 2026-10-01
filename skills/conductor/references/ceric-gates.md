# CERIC Gates

`ceric` (`../../ceric/SKILL.md`) is conductor's reading and auditing instrument, wired in as three gates of the flow. The method: pull a document's Claim, Evidence, Reasoning, Implications and Context out as quotes; mark what is missing; keep the hedges. The elements and their boundary rules: `../../ceric/references/elements.md`. The scoring instrument: `../../ceric/references/grading.md`.

## Gate 1 — Ground: read every input as a CERIC hunt

The hunt lands in **`grounded.md`** — beside the Plan Block, or at the wiki path the project uses. Minimal shape: one section per input document, each carrying Claim / Evidence / Reasoning / Context / Implications / MISSING, closing with the `Grounded:` line. The reasons explain why each claim matters to this decision. [book:learning-systems-thinking], Identify Your Reasons.

Every input document — the brief, the RFP, the prior wiki, a subagent's report — is read as a hunt, not skimmed:

- What it **claims**.
- On what **evidence**.
- By what **reasoning**.
- What came before it (**context**), and what it expects next (**implications**).
- What is **MISSING** — an element the document should supply and does not.

Each missing item becomes a Plan Block `DECIDE NOW` question and, while it remains open, an issue-log entry with a responsible owner and follow-up action. A gap noticed while grounding and not written down is a gap the run rediscovers later at full price. [book:pmbok-guide-7e], 4.6.2. Logs and Registers.

### Look beneath the event

For recurring problems, ask what patterns, system structures, and mental models may be sustaining the visible event. Treat proposed root causes as hypotheses to investigate, not established facts. [book:learning-systems-thinking], The Iceberg That Sinks Our Initiatives.

## Gate 2 — Converge: audit the synthesis before it lands

The object under audit is named by the run's shape: research → the synthesis; personas → the objection register; build → the run report and the ledger's claims, never the code. That is how this gate squares with `convergence.md`'s "each unit's own gates; conductor does not re-judge them": the unit's gates judge the work, Gate 2 audits what the run asserts about it.

Before the converged artifact lands, run the `ceric` audit on it. Check evidence with research or hands-on tests when that is what would settle the claim. [book:learning-systems-thinking], Reliable. Every claim gets a row:

| Claim | Evidence | Reasoning | Hedge | Verdict |
|---|---|---|---|---|

Verdicts: **supported** · **evidence only** (no reasoning) · **assertion** (no evidence) · **overstated** (hedge dropped).

The three convergence failure modes are the three bad verdicts:

- **Stapling** = claims without reasoning: each thread's findings survive side by side and nothing connects them.
- **Averaging** = claims without evidence: the merged number nobody sourced.
- **Overstated** = a hedge dropped: "consistent with" became "is".

A claim that fails is not merged. List it as open, name what would settle it, and assign a responsible owner for follow-up. [book:pmbok-guide-7e], 4.6.2. Logs and Registers.

## Gate 3 — Close: the UAT audit

Close audits the artifacts against the goal file's UAT column and nothing else (`goal-file.md`). A criterion that fails is reported as failed, never re-worded to conceal the result. Revise it only when its underlying assumption or tested functionality genuinely changed, and preserve the original row and verdict. [book:continuous-delivery], The Automated Acceptance Test Gate; [book:continuous-delivery], Essential Practices.

## Scale to stakes

Per the core kernel's cold-review rule: the audit is skippable for an internal, reversible synthesis, and never skippable for anything a client, investor or contract will test. When you skip it, say so out loud.
