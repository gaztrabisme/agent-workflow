# Artifact Writing

Write for the result the reader needs and keep the permanent rationale in a durable decision record.

## Purpose, audience, and scope

- Fix the outcome you want the reader to produce before drafting; keep every sentence advancing that outcome. Do not produce an unrequested document that no decision depends on. [book:hbr-guide-business-writing], Know why you’re writing.

## Staged drafting and editing

- Separate gathering ideas and evidence, organizing them, drafting, and quality-control editing. Use distinct editing sweeps, each checking one property; reserve at least as much time for editing as for writing. [book:hbr-guide-business-writing], Divide the writing process into four separate tasks; [book:hbr-guide-business-writing], Call in the Judge.

## Decision rationale and deliverable prose

- For a non-trivial implementation report, include a concise decisions-and-why section. Keep it to three to five key decisions, one line for each choice and its reason, and call out choices where a naive alternative would work but has a subtle failure mode. [book:facilitating-software-architecture], Consequences; [book:software-engineering-at-google], Write Good Change Descriptions.
- Put teaching and forks in the conversation, permanent decisions and rationale in decisions.md, and only the conclusion plus a reference token in a handoff or client-facing artifact.
- In non-exempt tabular deliverables, keep prose cells of twelve or more words to at most one per 100 non-empty cells. Move a multi-clause cell's rationale to decisions.md and put a reference in the cell. (derived: dogfood 2026-10-01)
- Exempt an internal design spec or architecture document only when it is for internal use, its purpose is to specify or evaluate a system/design structure for implementation, and its primary readers are the people who build or review that structure. Client-facing proposals, decision briefs, and capability summaries remain under the prose budget even when they contain technical material. If one artifact serves both audiences, split the design rationale into decisions.md and apply the budget to the reader-facing table. (derived: dogfood 2026-10-01)
- Do not defend a choice inside a deliverable; put that rationale in decisions.md.
## Recipient and polarity checks

- Use section headings as labels. Do not phrase H1–H4 headings as questions, argumentative claims, or defensive justifications; put the claim or explanation in the body or decisions.md. (derived: dogfood 2026-10-01)
- For each row or section, name its recipient and the decision they must make; test whether the content helps that recipient make that decision.
- Run both the prose budget and the lane test because they catch different defects.
- Before restating a negative rule, read the restatement back and check what action it authorizes.

## Client-facing pages

- Say what is in scope and what it does. State an exclusion or caveat once, on the scope or out-of-scope page; do not repeat it on other pages, where it reads as an upsell or as bad news told twice. Do not attribute a cut to the client, do not state the client's or funder's budget limit, and do not headline a price outside the cost page. Leave the nuance to the presenter. (derived: PwC PoC deck 2026-10-13 — the presenting team removed exactly these four kinds of sentence before the meeting)
- Before a client deck is shown, run a "read it as the client in the room" pass by a reviewer who did not write it: would the client read any sentence as blame, an upsell, an internal caveat, or a figure they did not ask to see?
