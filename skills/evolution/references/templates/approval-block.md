# Approval Block — one decision record for the whole run

Write a concise title that tells the reader the gist of the proposed decision without opening this block. [book:facilitating-software-architecture], Title

## Run summary

<One sentence: what was reviewed, the decision needed, and its expected value.>

## Approval gates and owners

| Gate | What must be true | Accountable approver | Evidence needed |
|---|---|---|---|
| <gate> | <decision condition> | <named authority> | <trace or check> |

Each gate has a named authority before review begins. Put the complete decision record in one place so the approver needs no other file to understand the request. [book:continuous-delivery], Deploying and Promoting Your Application

## Settled verdicts

| Skill | Item | Verdict | Evidence and reason |
|---|---|---|---|
| | | | |

Settled verdicts lead the record. A run that settles prior items and proposes nothing new is complete.

## Hypotheses

Rank by impact and effort, without replacing judgment with a formula. Merge duplicate findings into one hypothesis with all affected files.

### H1: <short decision title>

**Pattern and trace:** <evidence and source quality>
**Root cause:** <mechanism>
**Options:** <all considered options, brief pros and cons>
**Proposed change:** <one reversible edit>
**Files and blast radius:** <exact paths and affected consumers>
**Expected result and falsifier:** <observable effect, plus what would disprove it>
**Risk and rollback:** <known-good state and revert path>
**Validation owner and date:** <who checks what, by when>
**Impact / Effort:** <H/M/L / H/M/L>
**Status:** PENDING after application

## Rejected patterns and options

| Candidate | Evidence considered | Why not selected |
|---|---|---|
| | | |

If there were no rejected candidates, state whether the harvest was thin or the Wu Wei filter was not applied.

## Decision

For each gate, the named authority records its decision and rationale. Confirm that every required gate has approved its changes before application; no changes have been applied yet.
