# The delivery lifecycle

Use the phases to organize the signed-client records. A short engagement can use lighter review and reporting, while still keeping its contract, baseline and acceptance evidence clear.

## Phase −1 — Pre-signature effort inputs

This is a bounded delivery contribution to the estimate, not contract delivery. Do not baseline, track or accept work before a contract exists. [book:swebok], 3.2. Software Acquisition and Supplier Contract Management

For the operational signature gate, treat a contract as in force when the client has accepted a specific proposal version and fee in writing, whether in an executed contract, email or chat. Record the date, channel, exact version and fee, and a reference to the acceptance record in the baseline control fields. A conditional or ambiguous message is not enough; route contract status to solution-architect. (derived: dogfood 2026-10-01)

When solution-architect sends a work breakdown for pricing, delivery owns the effort input, release split and cut order because the delivery lead will be accountable for the signed commitment. Supply the estimate, schedule and cost inputs (5907 · U3 · L22 · 03:57–06:18), the release split in the buyer's recorded language, and the cut order with what the client loses at each cut. [book:swebok], 7. Software Engineering Management Tools

Start an effort sheet with the effort column empty so the discipline leads who will do the work can estimate their own rows. Never accept a prefilled effort form; build estimates from individual estimates by the people who will do the work. [book:user-story-mapping], The Secret to Good Estimation; [book:head-first-pmp], Estimation tools and techniques (5907 · U3 · L22 · 03:57–06:18)

Estimate the total effort and compare it with each contributor's actual availability over the delivery window. Record planned hours per week, allocation, and external or other-employer constraints, then convert the available time to person-days if useful. Return a capacity verdict and the size of any gap for a rescope, staffing or duration decision. (derived: dogfood 2026-10-01)

Observed: a delivery PM rejected a prefilled presale WBS and rebuilt 234 task rows with the effort cells empty for discipline leads. Preserve this distinction in future estimates: the delivery lead controls the estimate method and ownership; the leads supply credible row estimates.

## Phase 0 — Mobilise the signed baseline

Convert the signed proposal and its supporting artifacts into a delivery baseline (5907 · U3 · L22 · 01:11–02:54). At kickoff, freeze scope, schedule and cost as the plan of record and record the source for each. The scope baseline is the approved scope statement, work breakdown structure and associated dictionary under change control; keep linked schedule and cost baselines as separate records. [book:pmbok-guide-7e], 4.6.5. Baselines

Inherit the signed acceptance-criteria IDs verbatim. Use that single spine for the scope list, acceptance tracker, test references and invoice trigger; do not renumber it or make a parallel delivery list.

Reconcile the signed acceptance annex against the priced cost model before freezing the baseline. Compare both directions: every annex criterion or function appears in the cost model, and every priced function appears in the annex. Compare counts across the annex, cost model and workplan. Keep the signed proposal, cost model, annex, roadmap, client-obligation register, risk register and ID spine as the handoff inputs; report mismatches instead of silently repairing them.

Record the exact compared values beside each check. For every discrepancy, record its financial exposure, who was informed, the date and its resolution. A checkbox alone is not evidence that two versions agree. One past engagement priced a deleted function and counted the same population four different ways across its documents; the comparison table is meant to expose that kind of mismatch while there is still a decision to make.

If the signed cost model or effort input is missing, mark reconciliation as failed and do not freeze the baseline. Run the Phase −1 estimate loop now to supply the delivery-owned effort, schedule and cost inputs; send any missing negotiated scope or contract terms back to solution-architect. Reconcile the returned records before freezing. (derived: dogfood 2026-10-01)

Use the delivery-baseline template for the baseline version, freeze date, T0 event and date, exact source versions, governing language and ID spine. Carry forward the presale risk register, and also review historical project data for recurring risk patterns so the inherited list is not the only risk input. [book:project-management-with-ai], Employing data-driven decision-making

## Phase 1 — Open the signed-client trackers

Before the first deliverable is due, create the acceptance tracker with one Not started row for every signed criterion. Start the client-obligation tracker from the signed handoff and convert each relative deadline to a calendar date when the baseline's T0 date is known. Open the change-request log at kickoff with no entries, tell the client it exists, and use the change-request rate stated in the contract.

An absent tracker cannot show that work is unstarted or blocked. Keep the records aligned to the signed criterion spine, and link each blocked criterion to the client obligation that supplies its missing precondition.

## Phase 2 — Run the record cycle

Update effort spent, deliverables submitted and criteria signed from current records. Reassess risk and capacity; record new requests through change control; publish the cycle record from the trackers. The weekly reporting cadence is the default. [book:project-management-with-ai], Understanding automation in project management (5907 · U3 · L18 · 06:13–07:32)

Open every cycle record and every other note a PM reads with four lines: status (on track, at risk, off track), the evidence it rests on, the main risk, and the next action with its owner. [book:prince2-managing-successful-projects], A.11. Highlight report; [book:prince2-managing-successful-projects], 12.2. PRINCE2's requirements for managing progress

Delivery remains active while the software is being built. Keep its baseline, obligation and acceptance records current alongside engineering cycles; the delivery lead is not a substitute for the people doing the build. [book:head-first-pmp], Sometimes you need to change your plans

## Phase 3 — Accept in batches

Move each criterion through preparation, demonstration, client review and a written acceptance or deficiency record. Record criteria as they complete rather than holding all acceptance until close. [book:user-story-mapping], Evaluate Each Piece (5907 · U3 · L26 · 00:00–01:29)

Use the acceptance-execution reference for test preparation, rejection evidence and how a newly requested behavior enters change control.

## After final acceptance — Warranty

Track defects reported during the contractual warranty period in the warranty defect log. Reuse the signed criterion IDs and the acceptance test: a failure against a signed criterion is a defect; behavior the signed set does not require is a change request. Use severity and response windows from the contract, and record each fix and retest. Link the log from the close record and enter its end date and final disposition when the warranty expires. (derived: dogfood 2026-10-01)

## Phase 4 — Close and hand over

At close, record final acceptance, warranty start, final invoice release and the retrospective. Send the final invoice against the acceptance record, not simply because the team considers the work finished.

Hand over documentation, credentials, runbooks and an honest list of open defects. Close the client-obligation tracker with which dependencies slipped and by how much. Return estimate-versus-actual results by phase to solution-architect so future estimates can use delivery evidence. [book:swebok], 5.2. Closure Activities; [book:learning-agile], Story Points and Velocity

The close record is the durable summary of what was accepted, what was handed over, which client dependencies affected the work and what the estimate should learn from actuals. Use the close-record template.

## Records in more than one language

For Vietnamese-speaking engagements, review translated status, acceptance and change records for register and parity with the signed scope. Have a person review translated client-facing text for tone and accuracy, and have a person check any translation of legal or contract language before relying on it. Declare which language version governs if the versions disagree. [book:project-management-with-ai], Translating documents and correspondence into different languages
