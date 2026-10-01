# RFI, RFP, and Proposal Response

Build the response around the evaluator’s decisions: answer the stated need, show the solution and trade-offs, trace coverage, state assumptions, and shape any later solicitation where the RFI explicitly feeds an RFP.

## Clarification questions and assumptions

- Make implicit requirements explicit. Use client questions and an assumptions register for unresolved matters that only the client can answer [book:software-architect-elevator], Architects Deal with Nonrequirements. (5907 · U3 · L20 · 02:47–03:41)
- Record assumptions and constraints; ask the client only for unresolved decisions that require its answer [book:fundamentals-enterprise-architecture], Sample Template. (5907 · U3 · L20 · 05:12–06:41)
- For an RFI, respond to inform and position, use assumptions, demonstrate domain knowledge, and avoid over-investing in precision pricing.
- Order business and domain questions first; put logistics questions last or omit them. The contracting sequence surfaces method, schedule, and cost constraints early because they matter to agreement [book:flawless-consulting], Navigating the Contracting Meeting.

## Response pack

- Lead the response with an executive summary, then add the solution narrative, traceability, and win themes needed by the evaluator [book:storytelling-with-data], Horizontal logic.
- For an RFP, compete against the published criteria and treat precision, traceability, and compliance as non-negotiable. Address every stated need and tailor the response to the client's industry, company size, and culture [book:hbr-guide-business-writing], **Understand your readers**.
- For a direct brief without a formal template, impose a response structure that leads with client outcome and value. The book anchors architecture in business needs translated into technical drivers [book:software-architect-elevator], Measuring an Architect's Value.
- Do not answer every clause only with feature matching; include a solution narrative and win theme. The book says to compare decision options and trade-offs beyond vendor names and feature lists [book:software-architect-elevator], Measuring an Architect's Value.
- Answer every stated RFP need and tailor the response to the client's industry, size, and culture [book:hbr-guide-business-writing], ***Tailor your message***.

## Requirements traceability

- Maintain lifecycle traceability; in the response, map each requirement to its solution element and phase [book:swebok], Requirements Tracing. (5907 · U3 · L23 · 08:42–10:47)

## Pre-submission quality review

- Before calling presale done, check the artifact set, decisions and rejected options, open assumptions, traceability gaps, every client export, and cross-artifact integrity.
- Run the complete Final QA pass on every client-bound deliverable, using a reviewer who did not author it.
- Inspect work as it is created and use peer reviews before accepting interim deliverables as done [book:head-first-pmp], Inspection, testing, and product evaluation.
- If the client's template is internally inconsistent, state your convention and proceed instead of asking permission for a decidable issue.
- Use a traceability matrix with requirement reference, client requirement, coverage status, approach/technology, and phase.
- Mark unmappable requirements Partial, Clarify, or Excluded with a reason instead of omitting them.
- In workbook mode, replace coverage status with scope treatment and open-item fields while keeping every requirement reference accounted for.
- Use one row per RFP requirement; RFI rows may group related requirements only if every reference still appears.
- Add an Origin column and put client items not yet addressed first in the matrix.
- The book traces requirements back to their stakeholders and forward to design and tests; preserve those links in both matrix directions [book:swebok], Chapter 1: Software Requirements.
- Explain each Ours row with a client anchor or explicit justification.
- The book uses why questions to surface decisions and assumptions; use clarification to expose the reasoning behind a claim [book:software-architect-elevator], Whys Reveal Decisions and Assumptions.
- The book says to research publicly available facts first and use client questions to uncover their situation, problems, and gaps [book:selling-to-big-companies], GUIDELINES FOR GOOD QUESTIONING.
- The book starts from business needs and derives technical drivers; ask about outcomes and baselines before requesting configuration detail [book:software-architect-elevator], Measuring an Architect’s Value.
- The book prunes goal-question-metric trees by signal and cost; apply that selection logic to clarification questions [book:software-architecture-metrics], Prioritize Metrics and Devise a Data Collection Strategy.
- On an RFI, pair each load-bearing question with an assumption that lets work proceed if unanswered.

Run this review on each client-bound file and export. Have a reviewer who did not author the deliverable perform the complete Final QA pass. These checks came from defects that reached real deliverables:

1. Read every label with its value; editing can shift a row under the wrong label.
2. Remove internal review notes and comments from every circulated copy.
3. Recompute totals and currency conversions from the raw inputs.
4. Check numeric columns for ranges that were converted into dates.
5. Walk agenda and section numbering together.
6. Match version and date across cover, footer, filename, and status line.
7. Open every artifact with an embedded diagram and compare figures on the image with the current source.
8. Find earlier exports that may still circulate before correcting a published figure.
9. Search important quantities in digit and word form; after correcting one, recheck every quantity in the sentence.
10. Re-sweep every occurrence of a correction instead of trusting its tracker status.
11. After splitting a slide or section, check continuation titles, counters, and density.
12. Check the working file and each circulated export; a clean source does not prove its PDF or image export is sound.

## Choose the response posture

- Use the response template as the starting document, consult this guidance for rationale, and use the blueprint workbook as the live carrier on multi-week engagements.
- Maintain client and internal question buckets and copy each client-question fallback into the assumptions register.

## Win themes and evidence

- Treat the assumptions register as a primary artifact, keep it current with every open item, and surface high-impact low-confidence items in the response.
- Write three to five win themes, each mapped to a published or inferred evaluation criterion and backed by proof. MEDDICC aligns value proposition with pain, Metrics, and customer Decision Criteria; the count and proof requirement are additions [book:meddicc], COMPETITION.

## Response writing and presentation

- Check that every label matches its adjacent content.
- Remove internal reviewer comments and team-language notes from client exports.
- Recompute totals and currency conversions from raw cells.
- Scan numeric columns for date-coerced ranges.
- Walk all agenda and section numbers to verify that their order and values agree.
- Reconcile the version and date across cover, footer, filename, and status line.
- Open every artifact containing an embedded diagram and check the exported image and all figures against the current source.
- Review response decks with vertical logic so every item supports its title and unrelated content is cut or moved to an appendix [book:storytelling-with-data], Vertical logic.
- Prepare a concise three minute story and a single sentence Big Idea before building a long presentation [book:storytelling-with-data], The 3‐minute story & Big Idea.
- Write response summaries for the executive, scrutinizing evaluator, and future reference reader [book:hbr-guide-business-writing], **Memos and Reports**.
- Separate drafting, organizing, editing, and proofreading into distinct passes [book:hbr-guide-business-writing], **Divide the writing process into four separate tasks**.
- Structure a client win narrative as a six-step commercial teaching pitch: start with client challenges and insight, quantify consequences, make relevance personal, present a new way, then position the solution [book:challenger-sale], A PURPOSEFUL CHOREOGRAPHY.
- Tailor each RFP response to every stated need and the client’s industry, company size, and culture [book:hbr-guide-business-writing], ***Tailor your message***.

## Shape a later RFP from an RFI

- Before correcting figures that appeared on a canvas, find where prior exports were sent and identify stale downstream copies.
- Search every important quantity both as digits and words, and verify the other quantities in the same sentence.
- On re-review, re-sweep the full deliverable for each supposedly fixed string instead of trusting a status tracker.
- After splitting a dense slide, check the section counter, title, and continuation-slide density.
- Treat the working file and any circulating export as separate deliverables; name and check both.
- Do not submit a matrix with silent coverage gaps.
- Do not over-ask the client or ask permission for conventions that can be decided internally.
- Match pricing precision to the solicitation: avoid precision pricing for unscored RFIs and do not give vague pricing for scored RFPs.

When the RFI explicitly feeds a future RFP, use the response to shape its criteria toward your differentiators by teaching which requirements matter and why; bid when those criteria reflect your differentiated offer. Make missing decision criteria visible, and state inferred future scoring criteria as inference because an RFI has not published a scorecard [book:challenger-sale], Teaching for Differentiation.
