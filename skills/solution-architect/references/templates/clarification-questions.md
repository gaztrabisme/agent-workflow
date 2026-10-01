# Clarification Questions — template

*Separate client-only questions from matters the solution architect can decide or research internally. Pair each client question with a working assumption and its impact if wrong.*

## Questions for the client

| Priority | Requirement or criterion served | Question | Working assumption | Impact if wrong | Client answer |
|---|---|---|---|---|---|
| | | | | | |

## Resolve internally

| Open point | Why it does not need a client answer | Action / owner |
|---|---|---|
| | | |

## Question discipline

- Maintain one client-question bucket and one internal-resolution bucket, ordering business/domain matters before logistics.
- Give every client question a fallback assumption and copy that assumption to the assumptions register.
- The book asks for a response when an assumption proves false; stating the impact of selected assumptions is the rule’s explicit extension [book:semantic-software-design], RAID.
- Link each question to its delivery acceptance criterion or enterprise requirement reference.
- For each client question, record priority, served criterion/reference, category, question, assumption, impact, answer, and respondent.
- Mark a question P1 only when it blocks a criterion, price, or design decision; mark an improvable but nonblocking question P2.
- Group client questions by function or requirement area rather than by internal numbering.
- For internal questions, record the original ask, why not to ask the client, and the action or owner; route conventions and research internally.
- The book supports pruning a GQM tree toward strong signals; reframing configuration questions as outcome/baseline questions is the rule’s added practice [book:software-architecture-metrics], Prioritize Metrics and Devise a Data Collection Strategy.
