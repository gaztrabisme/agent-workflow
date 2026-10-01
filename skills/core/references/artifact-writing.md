# Artifact Writing

Write for the result the reader needs and keep the permanent rationale in a durable decision record.

## Purpose, audience, and scope

- Fix the outcome you want the reader to produce before drafting; keep every sentence advancing that outcome. Do not produce an unrequested document that no decision depends on. [book:hbr-guide-business-writing], Know why you’re writing.

## Staged drafting and editing

- Separate gathering ideas and evidence, organizing them, drafting, and quality-control editing. Use distinct editing sweeps, each checking one property; reserve at least as much time for editing as for writing. [book:hbr-guide-business-writing], Divide the writing process into four separate tasks; [book:hbr-guide-business-writing], Call in the Judge.

## Decision rationale and deliverable prose

- For a non-trivial implementation report, include a concise decisions-and-why section. Keep it to three to five key decisions, one line for each choice and its reason, and call out choices where a naive alternative would work but has a subtle failure mode. [book:facilitating-software-architecture], Consequences; [book:software-engineering-at-google], Write Good Change Descriptions.
- Put teaching and forks in the conversation, permanent decisions and rationale in decisions.md, and only the conclusion plus a reference token in a handoff or client-facing artifact.
- In a table, keep prose cells of twelve or more words to at most one per 100 non-empty cells. Move a multi-clause cell's rationale to decisions.md and put a reference in the cell. Do not apply this prose restriction to internal design specs or architecture documents.
- Do not defend a choice inside a deliverable; put that rationale in decisions.md.
- Use section headings as labels. If a reader could disagree with a heading, move its explanation to decisions.md.

## Recipient and polarity checks

- For each row or section, name its recipient and the decision they must make; test whether the content helps that recipient make that decision.
- Run both the prose budget and the lane test because they catch different defects.
- Before restating a negative rule, read the restatement back and check what action it authorizes.
