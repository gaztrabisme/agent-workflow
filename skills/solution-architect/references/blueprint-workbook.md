# Blueprint Workbook

Use this workbook as the live carrier when an enterprise bid has multiple clarification and review rounds. Keep the evaluator’s decision artifacts together and propagate each answer to every affected sheet.

## Answer-folding loop

- For a live multi-round bid, converge the matrix, registers, questions, risks, WBS, and roadmap in a workbook with a cell-level change log.
- On a multi-week engagement, converge live artifacts into one workbook, use it as working memory, and generate the response from it.
- In workbook mode, use its column vocabulary as the authoritative equivalent of the markdown templates.

For each client answer, update every affected sheet, not only the question row. An answer about a channel can change traceability, use cases, scope treatment, work descriptions, roadmap, assumptions, and the open question. Log the previous and new cell values, reason, and source-answer reference; this is what lets a reviewer explain why a later workbook differs from the submitted one.

## Workbook purpose and audience

- Tailor the workbook and templates to this project’s context and organization before fixing its artifact set [book:pmbok-guide-7e], 3.3.5. Methods and Artifacts.
- Include the listed workbook sheets and required contents: executive summary, traceability, use cases, architecture, scope, WBS, roadmap, RACI, risks, assumptions, questions, commercial/AMS, team, source notes, and change log.
- In the executive summary sheet include problem, recommendation, phase focus, guardrails, KPIs, prepared-for/by, date, and status.
- In the traceability sheet record requirement ID, area, source text, response, mapped use cases, scope treatment, and open item.
- In the use-case sheet capture actor, channels, phase, KPIs, flow, integrations, data dependency, and complexity drivers.
- In the architecture sheet record each layer's components, description, indicative technology, and dependency or TBC.
- In the scope sheet state type, item, description, treatment, and key assumption.
- The book uses the WBS to schedule tasks with estimated durations, precedence, and assigned resources; it does not add an uncertainty-driver field [book:swebok], 7. Software Engineering Management Tools.
- In the roadmap sheet record stage, theme, gate, outcome, and dependencies.
- Include an activities-by-party RACI sheet [book:fundamentals-enterprise-architecture], What Is Stakeholder Engagement?.
- For failure risks, use FMEA to score probability and impact, derive criticality, and record mitigation [book:fundamentals-enterprise-architecture], Chapter 5. Enable and Enforce.
- The book places assumptions and constraints in each decision’s context; it does not specify a separate assumptions-and-dependencies register with action owners [book:fundamentals-enterprise-architecture], Sample Template.
- Record open-question priority, category, RFI reference, question, working assumption, and status.
- Include commercial options and AMS tiers in the commercial sheet.
- Record delivery roles, responsibilities, owner, and on-site or remote mode.

## Sheet inventory

- For each input document, record its source and how it was used.
- Record cell-level changes with old and new values, reason, source-answer reference, and change type.
- For each client answer, update every sheet it touches rather than partially propagating the answer.
- Move each open question through TBC/Open, Partially Resolved, and Resolved, and revise its working assumption to reflect known and deferred information.
- The book puts the recommendation’s context and alternative analysis in an architecture decision deliverable; it does not describe cell-level change logging [book:fundamentals-enterprise-architecture], Architecture Decision Deliverable.
- Add each client Q&A round and every dated input document to Source Notes with a note on how it was used.

## Scope treatment

- When waiting can improve a consequential choice, defer the decision while fixing its parameters instead of proceeding on an assumed position [book:software-architect-elevator], Deferring Decisions with Options.

## Name phases in client outcome language

- Mark committed and priced scope as Base.
- Mark scope committed to a later named phase and state its unlocking gate as Phased.
- Mark separately priced client-elected scope as Optional.
- State the analysis boundary and name the problem areas the engagement will leave untouched when defining exclusions [book:flawless-consulting], Elements of a Contract.
- For acknowledged requirements whose implementation is deferred, mark them in scope for design and frame the approach decision for the client.
- For significantly impactful choices, use a proof of concept or pilot in the organization’s environment to produce technical evidence [book:fundamentals-enterprise-architecture], The Importance of Experimentation.
- Record deferred scope and its tradeoff on the work-package row where the work is planned.
- The book puts outcomes and the user’s benefit ahead of feature descriptions; it does not prescribe outcome-based phase names or correction propagation [book:storytelling-in-design], Focus on Outcomes Instead of Features.
