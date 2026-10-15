# Proposal: what the shared PM skills still add (2026-10-13)

Status: **decided 2026-10-13, all four as recommended** (owner). Applied: items 1 and 2 in `references/estimating.md` with two checklist lines (Evolution 5, PM28–PM30); item 3 in `delivery/references/delivery-lifecycle.md` (delivery Evolution 5); item 4's price-free copy planned in `templates/wbs/README.md`. The coverage script went to `solution-architect/scripts/` and the draw.io checker to `drawio/scripts/`, after the owner confirmed the authors' permission.

## Sources

| Source | What it is | Read before |
|---|---|---|
| Six skills shared by other PMs in the organisation, 13 Oct (`Documents/pwc/source/fpt-internal/pm-skills-2026-10-13/`): wbs-estimate, proposal-architect, technical-proposal, architecture-diagrams, fpt-deck-style, html-prototype | Skills with scripts | Evolution 3 took their PM rules; their scripts and the last three skills were not read |
| An SDLC accelerator kit (`Downloads/accelerator-kit.zip`, 9 Jul 2026, sender not recorded): five PM skills (pm-estimation, pm-reporting, resource-planning, risk-reserve-estimation, scope-sizing) with scripts and settings | A pipeline from client documents to requirements, code skeleton, PM estimate and dashboard | Not read |

Same tests as the WBS template proposal (`wbs-template-set-2026-10-13.md`): a method rule must work for a PM with Excel and no AI, name its standard, and rest on two projects' evidence; a script is optional and the method never depends on it.

## Proposed

### 1. Confidence stated with the estimate, and the risk budget built from named causes (method)

Proposed text, appended to "Where contingency lives" in `references/estimating.md`:

> State a confidence level with every estimate, from the evidence behind it: high when the scope is traced to the client's words and no input is missing; medium when it rests on assumptions, missing inputs or another party's work; low when the scope is not traced or a test of the approach has failed. A low-confidence estimate is a range to recover from, not a price: say what must be resolved, by whom, before it can be quoted.
>
> Build the risk budget from named causes. Each line names the cause, its evidence, its effect on effort, time or cost, its owner, and what would remove it; the provision for risks not yet identified is its own line. Do not cover a missing input with a larger general buffer.

Standard: PMBOK Guide 7th ed., 2.4 Planning Performance Domain ("For new and evolving technology components, the confidence in estimates is expected to be low"; point and range estimates) and 2.8.5.3 Management and Contingency Reserve ("Contingency reserve is set aside to address identified risks should they occur"); PRINCE2 2017, 10.3 (for simpler projects the risk budget is the sum of the planned risk responses) and 10.4 (a provision for risks yet to be identified).

Cases:
- PwC presale: one unverified input (about 200 fields to verify, never listed by the client) moved the plan by 46 days, 11%; the estimate was published as a range (345 / 407 / 495 days) with that input named.
- LSP presale: 167 of 169 tasks were three-point expert estimates with no past actuals behind them; nothing in the file said how sure any of them was.
- From the accelerator kit: green/amber/red bands defined by evidence; "Red reserve is not a quote; it is a recovery range"; "Do not hide missing data inside a larger buffer. Name it."

Not taken from the kit: its fixed reserve rates (15 / 25 / 40%) and its instruction to write "Unavailable" instead of estimating. The rates have no source; the second contradicts the owner's rule to estimate with a stated method rather than leave a gap.

### 2. A size limit on work packages (method)

Proposed text, appended to "Every row states its basis" in `references/estimating.md`:

> A row its lead cannot break into parts is not understood well enough to estimate. Decompose it, or plan a short investigation task first and estimate after it. Set the size above which a row must show its parts (the team's threshold, or 30 days if it has none) and list the rows above it.

Standard: Lewis, Project Planning, Scheduling, and Control, chapter 8 ("Break down a project only to a level that is sufficient to produce an estimate of the required accuracy"); Head First PMP, Define Activities (decompose work packages "into activities that can be estimated"). **The 30-day figure has no book source**: it is wbs-estimate's default ("A single >30 MD row means the requirement is not understood"), offered as a default the team overrides.

Cases:
- LSP presale: face enrolment estimated at 8 and 40 days by two people; the gap was an unstated scope assumption (photo collection), not speed.
- wbs-estimate warns on any row over 30 days; the WBS template's settings already carry a size threshold (`criteria.over_days`), used today only to require a definition of done.

Evidence is one of our projects plus a colleague's practice, short of the two-project test. Recommendation: adopt, because both books state the rule; the number stays a default.

### 3. The opening of every PM note (method, placement open)

Proposed text:

> Open every note a PM reads with four lines: status (on track, at risk, off track), the evidence it rests on, the main risk, and the next action with its owner.

Standard: PRINCE2 2017, A.11 Highlight report (date, period, status summary, work done and pending, issues and risks) and 12.2.3 Reporting progress.

Cases:
- Accelerator kit: every PM file opens with these four lines and a gate script refuses a file missing one.
- The owner's own instruction for reports (global instructions, "Global Context"): every end-of-run report must stand on its own for a reader who saw none of the work.

Placement: this skill covers planning before work starts; progress reporting belongs to `delivery` (its weekly cycle record, `references/delivery-lifecycle.md`) or, for any note, to core `artifact-writing.md`. Recommendation: put it in `delivery`, beside the weekly cycle record, and not in this skill.

## Accelerator candidates (optional scripts)

### 4. A copy of the workbook without prices (WBS template, second batch)

wbs-estimate builds an effort-only copy with no rate, cost or currency, and drops every assumption tagged as price-bearing. The rule already exists (checklist line 10: pricing assumptions on the internal sheet only); the WBS template's first cut has no pricing, so it has nothing to drop yet. Recommendation: build it into the template's pricing batch, with the price-bearing tag on assumptions as wbs-estimate does.

### 5. A requirement-coverage check (solution-architect)

technical-proposal's `audit_proposal.py` reads the client's requirement list and, for each requirement, lists the slides or sections most likely to answer it, without giving a verdict: a person reads each place and records whether it is met. solution-architect already requires a traceability matrix with no silent gaps (`SKILL.md`, "Shape the response"; [book:swebok], Requirements Tracing); what it lacks is a tool that points the reviewer to where each answer should be. Recommendation: adapt it as an optional script in solution-architect, credited to its author.

### 6. A draw.io checker (drawio)

architecture-diagrams' `check_diagram.py` flags shapes placed outside their container and shapes on top of each other, draws a preview image, and exits with an error when it finds either. Our drawio skill states the overlap rule in text (`references/quality-conventions.md`) with no check. Recommendation: adapt it as an optional script in drawio, credited to its author.

## Not proposed

- wbs-estimate's effort multipliers (first of a kind ×1.3, legacy interface ×1.4, regulated ×1.2, reused pattern ×0.7): no source, the same reason its ratio tables were left out in Evolution 3.
- The kit's story points scored from keywords in requirement text, its day rates and its role-mix percentages: no source.
- The kit's Claude and Copilot licence planning: outside project planning.
- fpt-deck-style (FPT's navy and orange colour codes, a three-card slide layout): no skill of ours has FPT colours, but the style comes from one deck and adopting it is a brand choice, not a gap.
- html-prototype: read for its outline only; not compared with the `ux` and `frontend` skills.

## Before adopting any script

The scripts belong to colleagues. Ask the author before copying code into a skill, and credit them in the script header either way.

## Decisions for the owner

1. **Confidence and risk budget** (item 1): adopt in `estimating.md`. Recommended.
2. **Size limit** (item 2): adopt with 30 days as a default the team overrides. Recommended.
3. **Note opening** (item 3): adopt in `delivery`, or in core `artifact-writing.md` for every note, or hold. Recommendation: `delivery`.
4. **Scripts** (items 4–6): price-free copy in the template's pricing batch; coverage check in solution-architect and diagram checker in drawio, each after asking its author. Recommended, in that order.

Each adopted item gets an `EVOLUTION.md` entry in its skill, with its cases and a validation test.
