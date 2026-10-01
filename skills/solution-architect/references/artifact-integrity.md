# Artifact Integrity

Check that the presale response, decision records, registers, estimate inputs, and client exports agree with one another. These are solution-architect-specific checks; shared completion and evidence gates stay in core.

## Language and governing text

- For Vietnamese engagements, keep language parity and the governing language explicit, and review the proposal for the intended register.

## Cross-artifact checks

- PMBOK requires a unique identifier for each requirement, but does not prescribe one engagement-wide ID spine or distinguish bid from delivery IDs [book:pmbok-guide-7e], 2.6.2. Deliverables.
- Head First traces each requirement across scope deliverables; this rule applies its ID spine to clarification, prerequisite, WBS, and cost views [book:head-first-pmp], Exam Answers.
- Record the current spine version in every artifact that keys to it.
- Reconcile counts for the same population across all artifacts so they agree.
- Recompute counts from the source artifact instead of incrementing remembered figures.
- Check that every referenced spine ID exists in the current spine version.
- Head First follows requirements from their source through implementation and verification, which is narrower than covering every claimed view or recording an explicit waiver [book:head-first-pmp], Now you’re ready to write a requirements document.
- Check that each client-facing claim's linked task content actually provides the promised capability.
- Compare what each linked task delivers with what the client-facing sentence promises, using task capability data or human review.
- Make the gate consume caveat and exception fields, or delete fields it does not read.
- When a gate never fails on a defect class, verify which property it actually checks before treating the class as absent.
- The book calls for one authoritative source for architecture information, while the rule adds filename, version, and content checks [book:fundamentals-enterprise-architecture], Distribute: Single Source of Truth.
- The book calls for a single authoritative source and avoiding duplicate locations; it does not prescribe an archive location for retired copies [book:fundamentals-enterprise-architecture], Distribute: Single Source of Truth.
- For bilingual work, declare the governing language and state the lag of every translation.
- Compare structure, function lists, IDs, and counts across languages, not prose alone.
- PMBOK requires related budget and planning changes when scope changes, but it does not prescribe a two-way reconciliation between cost and commitment artifacts [book:pmbok-guide-7e], 2.5.7. Monitoring New Work and Changes.
- Check both priced-but-uncommitted and committed-but-unpriced items.
- Head First supports a configuration management system as the controlled source of current project documents; the rule additionally requires exactly one live file and one named owner per artifact class [book:head-first-pmp], Chapter 16. Practice makes perfect: Practice PMP exam.
- The book warns against duplicate authoritative locations; it does not specify how to resolve divergent same-name files [book:fundamentals-enterprise-architecture], Distribute: Single Source of Truth.
- Check every register's prefix against all other registers before assigning a new ID namespace.
- Accommodate stakeholder vocabulary by changing labels, not by reusing a live prefix for a second concept.
- Preserve existing IDs when a register shrinks; leave gaps instead of renumbering referenced rows.
- Keep separate registers when their audiences and decisions differ, even if both registers share a name.
- Give deliberate multi-audience registers distinct prefixes and record in the index that they must not be reconciled.
- The book forbids adding words to quotations; checking a client-attributed quote against its source record applies that no-added-words rule to the exact wording [book:new-ethics-of-journalism], 2 Kicking the Stone: The Search for Reliable Evidence in Journalism.
- Keep each verified quotation byte-identical wherever it appears across artifacts.
- Script quotation checks by extracting sufficiently long quotes, filtering for named external speakers, and searching the source of record.
- If an attributed quotation cannot be located, remove quotation marks and paraphrase it instead.
- The book recommends automated fitness functions for architecture governance, rather than treating a manually typed mark as an executed check [book:software-architecture-hard-parts], Architecture Fitness Functions.
- The book explains that formula-linked summaries recalculate when source cells change; it does not explicitly prohibit typed totals [book:excel-for-accountants], Formulas Recalculate.
- The book favors automated fitness functions for architecture checks; it does not prescribe a script that reconciles engagement artifacts [book:software-architecture-metrics], Fitness Functions.
- Record how each check was run rather than claiming in prose that it passed.
- Verify the defect description itself against the artifacts before propagating it.
- The book relies on formulas to recalculate dependent values, but it does not describe refreshing cached values by opening and resaving a workbook [book:excel-for-accountants], Formulas Recalculate.
- Run integrity checks before any artifact goes to the client.
- Run integrity checks after every client-answer folding round.
- Run integrity checks when an enterprise bid converts to a delivery contract and the ID spine changes.
- Run integrity checks before signature.
- Extract spine ID sets and use set differences to find dangling references, uncovered IDs, and count mismatches.
- Raise integrity findings on shared artifacts as questions until the intended version is established, then log the reconciliation.

Reconcile the client’s requirements and your response, the price and the negotiated commitment, and every shared identifier. Check both directions: every client need has a response, and every priced or internally added item has a reason and an owner. Keep a separate register when two audiences need different fields.
