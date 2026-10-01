# Grounding Gate

Ground covered decisions in a substrate before deciding. Leave a short record of what you consulted and what it changed.

## Ground covered decisions

- Before designing, implementing, or making a covered-domain claim, consult the relevant substrate for prior art, exact terms, or theory. Record: Grounded: <source or query> → applied <finding>, or → nothing relevant. [book:critical-thinking-about-research], 10 Research Syntheses and Meta-Analysis.
- If the domain is not covered and grounding is skipped, say so explicitly. [book:building-applications-ai-agents], Trust in Interaction Design.
- Do not make a claim you cannot ground; mark it explicitly as an assumption or unknown instead. [book:learning-systems-thinking], Be Honest About Potential Pitfalls.
- When a literature synthesis is warranted, use a staged process: formulate the question, search, gather sources, appraise methods, integrate findings, interpret them, and present the result. [book:critical-thinking-about-research], 10 Research Syntheses and Meta-Analysis.
- For empirical claims, note the evidence design behind a source as well as its source reliability. Evidence hierarchies are domain-specific guides, not mechanical verdicts. [book:how-to-read-a-paper], The traditional hierarchy of evidence.

## Evidence fields and attribution

- In a table, store a reported value in a separate field ending in _reported; reserve the unsuffixed field for a value measured or verified directly.
- Never put a reported value in a measured field, even temporarily.
- Put grades for external sources in a table column, not in a footnote.
- For a constraint attributed to another party, verify whose words state it; a citation to a source alone is not attribution.
- Ask whose sentence it is. Do not present your own statement as another party's constraint.
- Check the primary source rather than relying on a summary, and record the speaker beside the constraint.
- For a tabular attributed constraint, record the speaker in a stated_by column.
- When asked to refresh a number or date from memory, reread the primary source instead of recalling a summary.

## Verify claims and quoted strings

- When verifying one quantity in a clause, verify every quantity in that clause. After correcting one, re-sweep the whole artifact. Search for numeric values in both digit and word forms.
- Use quotation marks only when the exact enclosed characters, in that order, can be produced from a source of record; otherwise remove the marks and keep an honest paraphrase. [book:research-methods-psychology], Chapter 4: Ethical Guidelines for Psychology Research.
- Verify guards, sentinels, acceptance strings, and defect descriptions against their source when recording them. Run the source-string search at the moment you write the string down.

## Checks as executable contracts

- Express important invariants as checkable preconditions, postconditions, or assertions so an invalid state fails visibly. [book:swebok], Assertions, Design by Contract, and Defensive Programming; [book:swebok], Preconditions, Postconditions, and Invariants.
- Do not ship a check whose output is mostly noise; scope it until findings are useful signal. [book:site-reliability-engineering], Bigtable SRE: A Tale of Over-Alerting.
- Write the check's scoping predicate beside it. Identify engagement-specific configuration separately from portable check logic.
- Label a tuned check that is not run as a tool, not as an active gate.
- A narrow predicate needs a non-empty-corpus assertion; otherwise a stale predicate can pass without checking anything. [book:swebok], Assertions, Design by Contract, and Defensive Programming.

## Probe limitations before declaring them

- Probe a claimed limitation through a time-boxed investigation of one question; gather concrete information without drawing conclusions from the probe alone. Record the falsifiable check beside the limitation you declare. [book:facilitating-software-architecture], Introducing Spikes.
- Do not treat which alone as a capability probe. Check default installation locations and equivalent libraries before concluding.
- Re-probe a limitation when the environment may have changed, and verify it again before allowing it to shape scope or a plan.
- Point a tool's defaults at the current artifact and update them when the artifact moves. If a frequently changing target cannot be kept current, require the argument instead.
- Echo resolved inputs in tool output before the verdict. Every check that resolves its own inputs must state what it resolved.

## Confidential material and external claims

- Keep local partner-track material on this machine.
- Do not quote internal funding amounts to clients in early conversations.
- Do not promise vendor funding until the vendor partner account team confirms it. [book:flawless-consulting], Ground Rules for Contracting.
- Read the source deck, cite its method, and do not redistribute the third-party deck.
- Determine the funding track from deal size before promising a pathway; confirm current tiers with the vendor partner team.
- Get current funding tiers from vendor partner materials, not from a skill or an old summary.
- Do not present vendor funding as a price list; confirm it with the vendor partner account team before client discussion.
