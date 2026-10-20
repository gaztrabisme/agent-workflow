# Hypothesis and change protocol

## From pattern to hypothesis

A pattern is evidence about a recurring gap. A hypothesis is one specific edit that could be shown wrong. Scientific claims are falsifiable, not provable; preserve that uncertainty in the wording. Do not propose a change without naming its target file, and do not bundle unrelated changes. [book:clean-architecture], Science to the Rescue

Use this reader-focused form:

```markdown
### H<n>: <short name>

**Pattern and trace:** <observation plus source and date>
**Source quality:** <directness, completeness, task identity and known capture limits>
**Root cause:** <mechanism, not symptom>
**Options considered:** <each briefly, with pros and cons>
**Proposed change:** <one edit>
**Target file(s):** <exact relative paths>
**Expected result:** <what should improve and what evidence could disprove it>
**Risk and rollback:** <failure mode; known-good revision and exact revert path>
**Validation:** <checkable later trace and predeclared evidence floor>
**Impact / Effort:** H | M | L / H | M | L
**Owner and revisit date:** <who will settle it, by when>
```

Write for the decision maker. Include the evidence behind a recommendation; a choice without its reasoning is not useful advice. Describe every considered option with concise pros and cons, including what was rejected. [book:facilitating-software-architecture], The Centrality of Advice; [book:facilitating-software-architecture], The Structure of an ADR

State what you expect to happen and what future evidence would prove that expectation wrong. A prediction is a testable expectation, not just a promise that a future trace will look different. [book:facilitating-software-architecture], Experiment with Your ADR Template

## The approval gate

Run the technical and managerial impact analysis before approval: identify affected files, consumers, risks and the extent of needed changes. The accountable authority then accepts, modifies, rejects or defers each request. [book:swebok], Requesting, Evaluating, and Approving Software Changes

Present one complete, self-contained block for the whole run. It must let the reader judge each hypothesis, its alternatives, evidence, target paths, blast radius, predicted result and rollback route without opening another file. Report approval gates and who owns each one; file lists and commit counts do not substitute for naming the decision that is needed. [book:continuous-delivery], Deploying and Promoting Your Application; [book:facilitating-software-architecture], Title

The decision taker receives advice and retains the choice; do not imply that a finding itself authorizes implementation. [book:facilitating-software-architecture], Direct Versus Representative Democracy

Use [`templates/approval-block.md`](templates/approval-block.md). Merge duplicates across skills into one hypothesis with several target paths. Preserve its essential fields, but revise the template in an approved later change if important sections are repeatedly left empty or half-filled. [book:facilitating-software-architecture], Experiment with Your ADR Template

Apply the Wu Wei filter: retain patterns tied to an observed failure, not theoretical purity; any new structure must earn its place through use. [book:site-reliability-engineering], The “Negative Lines of Code” Metric

Do not edit before approval by the gate owner: Huy, or the Improver session within the limits in its goal file (`wiki/goals/2026-10-20-improver.md` in the agent-workflow repo). The same stop applies to changes to workflow phases, trigger description, scripts or shared core. Never alter an integrity constraint or the Wu Wei filter through this loop.

After application, inspect the final change set to confirm that it contains only approved changes. [book:swebok], Implementing Software Changes

## Apply small, reversible changes

Make the smallest edit that closes the pattern and match the existing voice. Check in small changes frequently to the skill’s mainline; one hypothesis remains the traceability unit and may require several commits. Each check-in should preserve behavior or have a known-good revert path. [book:continuous-delivery], Essential Practices; [book:continuous-delivery], Prerequisites for Continuous Integration

Record every change for audit and rollback. State the expected result for each future check, so a later owner can compare it with evidence rather than a vague impression. [book:continuous-delivery], Managing Software Configuration; [book:swebok], Test Activities

## Recording and validation

Every applied change begins `PENDING`; include a named owner for each follow-up, a revisit date and a future checklist that another run can actually check. Never label a new change `KEEP` on application day. [book:software-engineering-at-google], Blameless Postmortem Culture

Before harvest, set the evidence floor for each verdict category and keep it fixed while examining the traces. The expected result must be testable.

Each gate owner records that gate’s decision (accept, modify, reject or defer) and rationale. A decision at one gate does not authorize changes assigned to another gate. No changes are applied until the responsible gate owner (Huy, or Improver after a blind judge on another provider accepts the change) approves.
