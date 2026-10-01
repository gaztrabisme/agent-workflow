# Progress, cost and status measures

Keep four views distinct in the cycle record: working increments, signed acceptance, effort spent and forecast against the baseline.

## Working progress and signed acceptance

Demonstrate working software to stakeholders each iteration. It shows what has landed and exposes promised work that did not. Do not use a status report or a signed-criteria count as the only evidence of delivered progress. [book:learning-agile], Principle #7: Working Software Is the Primary Measure of Progress.; [book:user-story-mapping], Use Your Story Map During Delivery

On an acceptance-gated engagement, calculate the commercial acceptance measure from the acceptance tracker: client-signed criteria divided by criteria in the signed spine. Keep it as the acceptance and payment view, not as a complete measure of working progress; the number of criteria alone may not reflect their relative value. [book:scrum-masters-path], Definition of Done vs. Acceptance

Show submitted-but-unsigned criteria separately from the signed ratio. A working-software demonstration helps explain current delivery progress; the signed ratio remains computed from the tracker, not read off a visual map. A story map can sit beside it as a done-versus-left view, using the existing criterion IDs rather than a second measurement system. [book:user-story-mapping], Use a Map to Visualize Progress

For fixed-price work, count each small deliverable 0 until it is complete, then 100. Keep criteria small enough for acceptance to land regularly; split an item that routinely takes several weeks into smaller signed criteria where the contract permits. [book:scrum-masters-path], Definition of Done; [book:user-story-mapping], Breaking Down a Big Cake

Do not report a subjective percent-complete figure as measured progress. A chart of remaining work can show its trend across a cycle; it does not replace the acceptance tracker or make a signed criterion count into delivery progress. [book:learning-agile], Burndown Charts; [book:scrum-masters-path], Burndown Chart

Effort burn is a cost-control measure, not progress. Update actual effort, submitted deliverables and signed criteria from records, and report estimates from people doing the work as estimates rather than completed value. [book:user-story-mapping], Manage Your Budget; [book:user-story-mapping], The Other Secret to Good Estimation

## Capacity and sustainable pace

Compare available capacity with required effort and record both the gap and contingency. If there is a positive gap, do not freeze it without a recorded rescope, staffing or duration decision. Make a zero-day gap explicit as a plan with no capacity buffer. [book:project-management-with-ai], Balancing workloads across teams; [book:project-management-with-ai], Optimizing resource allocation with AI

Base availability on each person's planned hours per week and allocation for the period, including known external or other-employer constraints. Recheck actual availability during delivery and rebalance the work when it changes (5907 · U2 · L08 · 01:38–03:00). (derived: dogfood 2026-10-01)

Size contingency from analyzed project-specific risks and spending evidence rather than an arbitrary reserve. Keep its owner and distribution visible in the baseline. [book:project-management-with-ai], Automating financial contingency planning

During delivery, monitor capacity and rebalance work as people approach their limits. Compare effort with the available working time and favor a pace that can be maintained by sponsors, developers and users. [book:project-management-with-ai], Balancing workloads across teams; [book:learning-agile], Principle #8: Agile Processes Promote Sustainable Development. The Sponsors, Developers, and Users Should Be Able to Maintain a Constant Pace Indefinitely.

### Small-engagement cycle view

For a small team or short engagement, put these four lines at the top of the weekly cycle record: Awaiting Client, signed acceptance ratio, change-request count, and available-capacity line. Keep the same baseline, acceptance, obligation, change, risk and cycle records underneath or linked; this is a compact view, not a waiver of required evidence. Use agreed RAG thresholds and a recorded exception action when a threshold is crossed or forecast. Leave automated alerts or risk forecasts out when no suitable data or capability exists. (derived: dogfood 2026-10-01)

## Cycle facts and variance

Update actual effort, deliverables submitted and criteria signed using facts only. For external suppliers, request progress evidence such as earned value or exit criteria; an assurance that work is on schedule is not enough to support a progress claim. [book:user-story-mapping], The Other Secret to Good Estimation; [book:project-planning-scheduling-control], CHAPTER 9 Project Scheduling

Use a weekly cycle to report from task-completion data. Refresh actuals, client obligations, changes and risks in the same record cycle. Keep the report on disk, not verbal-only, and derive each number from the current tracker rows; automated data collection can reduce manual reporting errors. Reassess whether risks have moved, materialized or newly appeared. [book:project-management-with-ai], Understanding automation in project management; [book:holacracy], Chapter 5: Operations; [book:project-management-with-ai], Automating data collection for reports

Compare accepted criteria, effort spent and the next milestone with the baseline. Record schedule variance, cost variance against accepted work and a one-line cause. Attribute the cause honestly, including when the client-side dependency caused it. Use progress-data analysis to locate bottlenecks and inform the cause line. [book:project-management-with-ai], Providing alerts when KPIs deviate from targets; [book:swebok], 3.4. Monitor Process; [book:pmbok-guide-7e], 2.2.2. Project Team Culture; [book:project-management-with-ai], Analyzing progress data to identify bottlenecks

## RAG and exception response

Derive RAG from the current variance and risk records, then sanity-check the result rather than choosing a color by feel. Do not report an engagement as green when the underlying performance result is red. [book:pmbok-guide-7e], 2.7.4. Measurement Pitfalls; [book:software-architect-elevator], Problems on the Way Up

Use agreed performance measures and thresholds for the status bands. Keep risk and overdue-obligation evidence visible in their own fields; do not make an unmitigated risk or a late critical-path obligation an automatic color override when the agreed metric thresholds do not say so. [book:pmbok-guide-7e], 2.4.8. Metrics

Where task-level schedule and cost indices are used, compare them with the defined control limits before applying the stoplight. Do not summarize away opposing task variances or let an unexplained favorable total hide an individual slip. [book:project-planning-scheduling-control], CHAPTER 13 Conducting Project Reviews; [book:project-planning-scheduling-control], Project Control

Agree an exception plan for a threshold that is crossed or forecast to be crossed. It can be a simple named action, such as a stakeholder meeting, but record what will happen and who will carry it out. [book:pmbok-guide-7e], 2.7.5. Troubleshooting Performance

Escalate any decision outside the delivery team's authority to the person with that authority, regardless of the RAG color. When reporting red, state the specific decision needed and the escalation channel. [book:pmbok-guide-7e], 2.2.4. Leadership Skills; [book:fundamentals-enterprise-architecture], Defining the Architecture Decision Workflow

Use alerts between weekly cycles when tracked measures trend away from their targets. Reassess risks each cycle; where useful data and a suitable forecasting capability exist, use forecasting to estimate risk likelihood and impact, then keep mitigation, owner and trend current in the risk record. [book:project-management-with-ai], Providing alerts when KPIs deviate from targets; [book:project-management-with-ai], Monitoring Risks in Real Time with AI Alerts; [book:project-management-with-ai], Selecting AI tools for risk management and forecasting

Amber or red status is useful only when its variance, cause and required action are visible. Report submitted criteria awaiting a client response separately from progress so delivery activity is not mistaken for acceptance. [book:learning-agile], Principle #7: Working Software Is the Primary Measure of Progress.
