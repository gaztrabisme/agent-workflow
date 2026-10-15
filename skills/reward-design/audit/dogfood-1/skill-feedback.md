# Reward-design first-use feedback

Run: 2026-10-10-reward-skill. Reviewed 2026-10-11 against the supplied 27-slide PDF and 57.5-second explainer. **Verdict: FAIL as a self-sufficient critique workflow.** Completing the task required a locally invented verdict crosswalk, severity rubric, applicability rules, media measurements and comparison protocol. This verdict concerns usability of the skill, not whether its cited psychological mechanisms exist. The inspection deliverables are complete; no audience or neurological effect has been established.

Paths below are relative to `/Users/GaryT/Documents/Work/tools/agent-workflow/skills/reward-design/`, unless a `../core/` path is named. Line numbers refer to the read-only snapshot supplied for this run. Proposed edits were not applied to the skill package. High = prevents a faithful or reliable critique; medium = materially ambiguous/friction; low = synthesis/polish. These severity definitions are local because the skill supplies none.

## F01 — High — result and evidence status are conflated

**Locations:** `references/review-checklist.md:5`; `SKILL.md:61`.

The checklist permits PASS, FAIL, not judged or skipped, while many real findings are partial and contain both an inspectable feature and an untested response. This task also requests meets/partly/misses/not applicable. A caption can exist while comprehension remains unknown; a finite file can exist while host exit controls remain unknown. One result field cannot express these differences. I had to add both requested verdict and skill disposition to all 54 records. R25 is particularly prone to turning “no study supplied” into “bad media.”

**Proposed edit:** Replace checklist line 5 with: “Record two fields: inspection verdict (meets, partly, misses, not applicable) and evidence status (measured, reviewer-judged, not judged, skipped). State the unmet subcondition of a partial verdict. Unavailable audience evidence never becomes an observed audience failure. Use PASS/FAIL only for a declared, fully observed acceptance condition.” Update the critique schema at SKILL.md:61 to match.

**Later-use test:** Two reviewers given captions plus no audience data should independently mark caption presence as observed and comprehension as not judged, without awarding a composite pass.

## F02 — High — applicability is left to improvisation

**Locations:** `references/review-checklist.md:5`, `:20`, `:29–:36`; `SKILL.md:51`.

R10 assumes prediction participation; R19–R20 assume triggered feedback/celebration; R21–R22 require product routes; R26 presupposes a memory claim. The checklist addresses “nonapplicable channels” but not absent mechanisms, unsupported claims or the separation of file and host. Neither piece is a working UI. Crypto subject matter is not a loot box. “Training completed” is not automatically a user-success celebration. I had to decide these boundaries, and a different reviewer could legitimately score them differently.

**Proposed edit:** Add an Applicability column with explicit predicates: “R10: a prediction invitation exists”; “R19: a triggered state change exists”; “R20: celebration implies a net user outcome”; “R22: a payment/random-benefit route exists”; “R26: a memory benefit is claimed or the brief requires one.” For media files, scope host/player controls separately. Distinguish inapplicable from applicable-but-unavailable.

**Later-use test:** The same passive PDF should not acquire gambling/UI failures solely because it depicts coins or a completion message.

## F03 — High — mixed presence/response checks cannot be closed consistently

**Locations:** `references/review-checklist.md:13`, `:16–:18`, `:22–:28`, `:34–:35`; `SKILL.md:61`.

R03, R06–R08, R12 and R14–R18 combine design properties with actual viewer/listener responses. Line 5 warns that responses need audience evidence, but it gives no subcheck format. In this run the video’s readable axes were inspectable, the label lag was measurable, and the viewer’s explanation was unavailable. Those are three different kinds of evidence. A flat pass or failure conceals one of them.

**Proposed edit:** Give these rows two subchecks: “a. Artifact evidence present, truthful and located”; “b. Intended audience succeeds at the specified task.” Complete the first in an inspection and leave the second pending with a concrete test prompt. Neither screenshot legibility nor loudness should satisfy the audience subcheck.

**Later-use test:** An inspection-only run should produce useful findings without fabricating task search, listening or comprehension.

## F04 — High — timeline mapping lacks an extraction method

**Locations:** `SKILL.md:45`, `:59`; `references/timing-and-structure.md:3`, `:36–:40`.

The flow asks for locations and a cue sheet but provides no method for measuring an existing video. In this export, the largest full-frame scene scores were caption changes around 0.16; the real main-content boundaries were at 4.000, 12.500, 25.000, 38.000 and 44.000 s. A generic high-cut-threshold scan would miss two of them or count caption transitions as scenes. The useful critique depended on excluding the caption band, checking all frames and measuring individual chart regions—none of which the skill says to do.

**Proposed edit:** Add a “Review existing playback” procedure: probe duration/fps/timebase; render exact-time frames; log all-frame change scores; classify content changes, captions and builds separately; visually confirm candidates; record audio signal events separately from supplied transcript times. State thresholds/crop regions and frame precision as analyst choices. Warn that fades and small builds can evade a scene detector. Link a minimal local measurement recipe, not a universal threshold.

**Later-use test:** Reviewers should recover five main scenes changes and 26 caption transitions separately, rather than report a single undifferentiated cut count.

## F05 — High — prototype times and observed times share one field

**Locations:** `SKILL.md:59`; `references/timing-and-structure.md:36`, `:40`.

“Use exact planned times only when the project needs them” is planning advice, but a critique needs exact *observed* times. The video’s 18.767 s late-section callout is a measurement; changing it to 16.088 s would be a proposed edit. A sampled-frame description has yet another precision. Mixing these encourages reviewers to turn approximate eyeballing into precise-looking evidence or to avoid measurements the task actually needs.

**Proposed edit:** Split the field into `observed_time`, `measurement_method/precision`, `reported_transcript_time`, and `proposed_time`. Label a proposed timing as a prototype choice; do not label observed export timing that way. For fades, distinguish first detectable pixels, readable state and audience-perceived onset.

## F06 — High — the critique path is not an executable order

**Locations:** `SKILL.md:41–:53`, `:63`; `references/review-checklist.md:45`.

The main table starts with mapping and ends with the checklist; line 53 says a critique starts with the checklist; checklist line 45 says production siblings review rendered mechanics first. There is no explicit inspection-only path for an already rendered, immutable artifact. Both supplied pieces lack editable source in this packet. Following all three readings literally would require either re-production or a return to the checklist before the needed measurements exist.

**Proposed edit:** Add a critique-mode sequence: “Read brief and checklist → declare scope/applicability/evidence access → probe/render/map the supplied artifact → inspect promise/cues/payoff/agency → return defects to their owning stage → propose tests and handoff.” Require candidate re-render and affected-check rerun only after a candidate exists. Keep the seven stages as diagnostic destinations, not competing orders.

## F07 — High — severity has no decision rule

**Locations:** `SKILL.md:61`; `references/review-checklist.md:5`.

Both demand severity but define no labels, anchors or relation to an unjudged item. An absent source ledger, a lagging annotation, a decorative detail and absent enjoyment research are different problems. I had to invent a rubric and mark evaluation gaps separately. Without that, the reader cannot tell what must be corrected before publication versus what requires a future test.

**Proposed edit:** Define severity for *observed* defects: high = wrong/deceptive critical inference, missing essential decision information or unfulfilled core promise; medium = materially obscured relationship or completion; low = optional refinement. For unavailable evidence, record priority-to-test and release implication separately, not defect severity. Add one media example per label.

## F08 — High — unavailable source truth has no practical disposition

**Locations:** `SKILL.md:67`; `references/timing-and-structure.md:48`; `references/review-checklist.md:18–:19`.

The skill requires source facts and source-checked comprehension. Here slide 6 explicitly reconstructs a historical chart, and the video cites an external fictional ledger/well plan, but neither source is supplied. The video’s arithmetic can be checked from visible numbers; the ledger, liner placement and causal story cannot. A visual comparison cannot turn the artifact into its own independent truth source. The gate says to ground claims but does not tell an inspection reviewer how to proceed with this common source deficit.

**Proposed edit:** Require separate provenance states: “reported by artifact,” “internally checked,” “verified against supplied source,” and “source unavailable.” Scope truth claims accordingly. Continue with located inspection findings while requesting the exact missing source in the handoff; withhold fidelity/comprehension certification that depends on it. Never invent a cause or source reconstruction from an animated trace.

## F09 — Medium — reader, subject and sample audience can be confused

**Locations:** `SKILL.md:45`, `:88`; `references/timing-and-structure.md:7`; `references/review-checklist.md:11`.

The deck brief does not name its evaluator, while slide 8 names novices as the audience for generated marketing copy. These are different audiences. Using the latter for R01 would change the entire critique from evaluating a prompt-engineering demonstration to writing crypto education. The briefs also contain commands from earlier dogfoods; “consume the brief” has no rule for separating artifact context from the current reviewer’s mandate.

**Proposed edit:** At stage 1 record `artifact_reader`, `subject/sample_audience`, `reader_decision`, `delivery_context`, and `assumption/source`. Treat supplied prior production briefs as context unless the current task asks to execute them. When audience is missing, state a provisional audience and condition the recommendations on it; do not promote an embedded prompt’s audience automatically.

## F10 — Medium — static deck timing is acknowledged but not operationalized

**Locations:** `SKILL.md:23`; `references/timing-and-structure.md:3`; `references/review-checklist.md:22`.

The skill correctly says not to infer static playback duration, yet R12 requires processing before the “next change” and playback observation. The PDF has no advance schedule or live recording. A dense page may be poor for projection and acceptable as a reading document. I could flag density but could not assign a reading-time failure without inventing delivery conditions.

**Proposed edit:** Add modes before applying R12: reader-paced document, live slides, narrated deck/video, interactive states. In reader-paced mode inspect navigation/legibility and record task reading time; in live mode require an actual advance sequence/rehearsal. If live delivery is unknown, mark timing not judged and retain the observable layout finding.

## F11 — High — semantic alignment and perceptual synchrony need separate checks

**Locations:** `references/review-checklist.md:17`, `:25`; `references/sound.md:17–:18`, `:40`.

The captions and waveform roughly align, but the explanatory labels lag their sentences by about 2.6–2.8 s. Caption onset precision does not make the explanation synchronous. Conversely, these label lags do not establish a lip-sync defect or a listener’s perceived delay. R07 and R15 partly overlap without distinguishing the event types, making a technically aligned export easy to mis-score.

**Proposed edit:** Add an event-pair field: impact/contact, visible speech, narrated reference-to-mark, musical transition-to-reveal. Assess narrated reference-to-mark under semantic cue alignment; assess perceived audiovisual synchrony by normal-speed device listening. Record physical timing as supporting evidence, never as a universal perceptual pass threshold.

**Later-use test:** This video should receive a measured chart-cue finding even if its audio/caption clocks match, with perceived synchrony still pending.

## F12 — Medium — the sound-review prerequisites are unstated

**Locations:** `references/review-checklist.md:24–:28`; `references/sound.md:29`, `:35–:40`; `SKILL.md:68`.

The skill says unavailable sound is not judged, but does not distinguish audio-file presence, decoded signal, supplied captions, audition and listener evidence. I measured −16.0 LUFS and zero-sample gaps, but could not certify voice comprehension, musical meaning or mood. VTT-derived rates also undercount expanded numbers and are not actual spoken rates. R17 needs a bed/silence comparison yet gives no applicability procedure when stems or an audible bed are unknown.

**Proposed edit:** Add a prerequisite record: “audio stream present; signal decoded; mix auditioned; stems known; listener task tested.” State explicitly that LUFS, waveform alignment and captions do not establish speech content, intelligibility or mood. Confirm a bed before requesting its A/B test. Mark caption-derived rates as text-window proxies; establish spoken pace through actual listening/transcription when it matters.

## F13 — Medium — audience acceptance cannot always be read from the brief

**Locations:** `SKILL.md:63`; `references/review-checklist.md:41–:43`; `references/timing-and-structure.md:49`.

“Choose acceptance criteria from the brief” is insufficient when a brief supplies format/codec/duration but no comprehension rubric, participants, observation period or recall delay. That is the case here. The seven-stage flow still asks for clarity, enjoyment and memory. I had to derive factual task prompts and leave thresholds/delay unassigned. An arbitrary delay would not become defensible merely by appearing in a test record.

**Proposed edit:** “Derive provisional task questions from the brief’s stated audience decision; mark them as proposed. If the brief lacks thresholds, participant plan or a relevant recall delay, leave effect acceptance pending until those are defined. Memory tests are conditional on a memory objective. Do not delay an inspection-only critique while awaiting a study.”

## F14 — Medium — exceeding expectation is presented as a required payoff test

**Locations:** `SKILL.md:33`, `:48`; `references/timing-and-structure.md:12`; `references/mechanisms.md:31`.

Stage 4 asks to test whether the payoff exceeds “the actual expectation,” but gives no baseline expectation method and no disposition for a dependable factual answer that simply meets its promise. For this operations summary, clear delivery can be the valued outcome. Asking viewers about desired surprise could prime a response or pressure an unnecessary flourish. Line 33 acknowledges that expected outcomes can be enjoyable; the stage table does not reflect that exception.

**Proposed edit:** “First test whether the answer fulfills the promise and supports the audience’s decision. Exceeding expectation is optional; if it is a project objective, record a pre-answer expectation measure and its limits. Do not require surprise or claim subjective excess from an inspection.”

## F15 — Medium — source tiers do not indicate relevance to the check

**Locations:** `references/review-checklist.md:11`, `:14`, `:18`; `references/evidence-map.md:10–:18`; `SKILL.md:27–:29`.

R01 cites wanting/liking A2 for audience relevance; R04 cites an operation-specific, attribution-unverified memo D3 for loop closure; R08 cites insight/brain association A17 beside segmentation B17 for evidence-based comprehension. These may motivate a heuristic, but do not directly validate the review question or a fix in this medium. The supplied V rows confirm these limits. A long T1/T4 trail can look more precise than the inspection instrument actually is. The existing “derived/not validated” warning does not distinguish the role of each citation.

**Proposed edit:** Rename “Findings” to “Rationale IDs” and add an evidence-role legend: direct task evidence, mechanistic analogy, craft precedent, ethical constraint. Retain corrected tiers, but state the exact task/medium tested and which part of the checklist is reviewer synthesis. Lead the finding with artifact evidence; do not rank fixes by tier count.

## F16 — Medium — “every striking detail” conflicts with expressive use

**Locations:** `SKILL.md:8`; `references/review-checklist.md:21`; `references/visual.md:28`.

The skill includes expressive experience as a valued outcome, while R11 requires every striking detail to support the core explanation. The deck’s generated illustrations legitimately demonstrate a requested output; treating them as merely decorative would miss that role. Some of their growth/safety implications are misleading, but relevance and truthfulness are different findings. A blanket educational rule could also erase expressive reward in a non-instructional piece.

**Proposed edit:** “For instructional media, each striking detail should support the explanation or a demonstrated output requirement. For expressive media, identify its brief-defined experiential role. In either case, check implied claims and distraction separately. Do not remove a relevant example merely because it is visually rich.”

## F17 — Low — no convergence step turns 27 checks into a usable change order

**Locations:** `SKILL.md:61`, `:89–:90`; `references/review-checklist.md:5`.

The output contract asks for one change per row but not consolidation, dependencies or a ranked handoff. The same measured chart lag appears in R07/R12/R15; the deck’s missing test result appears in R03/R04/R08/R23. Sending every row to several owners without synthesis produces duplicate or conflicting edits. This task’s useful top-three lists had to be added from outside the skill.

**Proposed edit:** End a critique with three consolidated changes ranked by expected task benefit/risk, with linked check IDs, one accountable production owner, dependencies and a test. State that ranking is reviewer inference, not measured uplift; explain when audience/context could reorder it.

## F18 — High — the absolute dopamine-measurement statement overclaims

**Locations:** `SKILL.md:10`; compare `references/mechanisms.md:15`, `references/sound.md:8`, and supplied V A9/A24 rows.

“No designer can measure it in an audience” is an absolute claim about who can conduct a measurement, not the supported warning that this workflow cannot infer dopamine from behavior or ordinary BOLD. The skill itself cites dopamine-sensitive PET under controlled listening. A designer collaborating in a suitable research study is not ruled out by those sources. The useful boundary is method and scope, not occupational identity.

**Proposed edit:** “This media-planning workflow does not measure audience dopamine. Gaze, clicks, retention, chills and ordinary BOLD cannot establish its release. Specialized dopamine-sensitive research methods do not provide a ready estimate for a new design. Evaluate anticipation, understanding, delivered value and reported experience here.”

## F19 — Medium — inherited review requirements are not scoped to this mode

**Locations:** `SKILL.md:12`, `:65–:68`; `../core/references/output-contract.md:40–:49`; `../core/references/wiki-protocol.md:21–:25`.

Core allows tailoring and reversible internal review, but also mandates independent multi-model sessions for a judgment likely to be tested, with completion/ship claims held when unavailable. This task explicitly reserves acceptance for the coordinator and supplies one critique lane; the prior piece briefs prohibit subagents. The skill never states whether the reviewer is producing an inspection record for that gate or shipping a validated judgment. Wiki initialization can similarly expand a small fixed-output task when the three requested files already form its allowed record.

**Proposed edit:** Add a critique-mode tailoring note: “The requested critique/report may serve as the project record. An inspection record is complete when evidence, limitations and handoff exist; independent audience/cold review is a separate pending gate when required. Identify the coordinator/owner, and do not claim production or audience validation before that gate.” Keep core’s release restrictions; distinguish them from completion of the internal inspection deliverable.

## Priority edit set and unresolved tests

Apply F01–F08 and F11 before the next dogfood: they determine whether the review can be followed and whether a result is honestly scored. F18 is a small but necessary correction. Then add the source/evidence-role and convergence changes, rather than more mechanism examples or books.

This run tests a PDF and a mostly narrated factual explainer only. It does not test a game, paid reward, live talk, emotional music, product flow or repeat-use behavior. No psychological recipe is validated by completing the critique. A second cold reviewer should use the revised instrument on the same packet without this report’s conclusions, then compare applicability, measured event classification, evidence status and priority order. Agreement should be assessed at those practical decisions, not by forcing every reviewer to choose identical aesthetic judgments.
