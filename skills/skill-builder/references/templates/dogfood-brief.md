# Dogfood Brief — template

Dogfood is a hard gate: the reviewer must use the skill on real work, not merely read it. A self-review misses blind spots; use a fresh-context reviewer and give it a specific task. [book:looks-good-to-me], Be your own first reviewer

## Brief shape (fill and hand to the reviewer)

> You are dogfooding a newly authored or structurally refined skill `<name>` at `<path>`. Actually **use** it on a real task and then report as a clear, professional critic. Be direct about defects, but critique the artifact rather than the person. Defer where approaches are equally valid; suggest alternatives when the chosen approach is deficient. [book:software-engineering-at-google], Code Review Best Practices
>
> **Read first:** `<path>/SKILL.md`, every file under `<path>/references/`, and the shared kernel at `../../../core/SKILL.md`.
>
> **Use it on real work:** <concrete task and inputs>. Produce the task artifacts under `<evidence path>` so the report shows the skill was used, not just read.
>
> **Do not modify skill files.** Scratch work belongs under `<evidence path>`.
>
> **Judge the skill:** would it trigger for this task and distinguish siblings? What step, template, or reference was missing? Where was there friction, contradiction, or overreach? Could each gate be carried out? Do links resolve? Does the skill claim more than its source supports?
>
> **Deliverable:** summarize the produced artifacts and compare with the past result after your own work is complete. Give 5–12 ranked findings, each with severity, cause, and a specific fix; name the single most important missing thing. Give 2–4 points that actually helped.

## Tasks for a skill distilled from a course

Use all three; each exercises a different part of `../distill-course.md`:

1. **Plan from a brief.** Pair two goals the source treats separately, run the method end to end, and cite anchors.
2. **Critique work.** Use a real or mocked artifact and run the whole review checklist without the source application. Say which checks were measured, judged visually, not judged, or skipped. At least one task must make an artifact through the complete render-and-check path.
3. **Fact question.** Route a question to the factual library and verify a computed number.

## Pass condition (state it before running)

The skill passes this dogfood when it fires on the right task without a sibling collision, each required gate is actionable, references resolve, and no high-severity defect remains after fixes. A `PENDING` entry still needs two independent real uses before `KEEP`. (field rule)

## After the run

- Save the evidence before opening the old output for comparison. State what the run produced, then compare it with the earlier artifact.
- Rank 5–12 findings from most severe to least. For each, include the cause and a concrete fix, and call out the most important missing thing. Score severity from **1 to 5** (5 is most severe); include a compatible bucket such as `[high]`, `[med]`, or `[low]` for the fix gate. Add 2–4 useful points only when they helped on this task. [book:building-reliable-ai-systems], Step 4: Report metrics
- For a high-impact or recurring finding, add a short postmortem: impact, contributing conditions, root cause if known, and follow-up action. Use a causal technique such as five whys when it helps. [book:site-reliability-engineering], Appendix D. Example Postmortem
- Have the writer fold findings back into the skill. Record one fix or evidence-based rejection per finding and list the coverage rows touched. Rerun dogfood when a high-severity finding forced a structural change; rerun mechanical checks after every edit. [book:continuous-delivery], Chapter 4: Implementing a Testing Strategy
- Record the result as an evolution entry with verdict `PENDING`; do not settle the entry on the same run that wrote it. (field rule)
