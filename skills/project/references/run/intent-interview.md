# Intent Interview

A short set of concrete "what should happen when…" questions put to the requester after Ground and before the Plan Block, so the plan is built on what they actually want rather than on the first reading of the prompt. Scenarios let the coordinator ask "what if" questions about the work in the requester's own terms. [book:swebok], 3. Requirements Elicitation. (derived: owner request 2026-10-03, adapted from the VibeWise plugin's build checkpoints)

## When it fires

Fire it when the request is substantive and at least one of these holds after Ground:

- **The outcome is open.** Two reasonable readings of the request would produce different artifacts, and building on the wrong one would mean redoing a stage. A difference the run can absorb cheaply is decided forward, not asked.
- **Behaviour at an edge is undecided.** A case the work must handle (a shared item deleted, a source that disagrees, a deadline missed, an input that is empty) has no answer in the prompt, the wiki or `decisions.md`.
- **A requirement conflicts with another** and the prompt does not say which wins.

Do not fire it when the request already answers these; when the requester says to skip, "just do it", or names the skill; for a follow-up inside an approved plan; or for a one-line fix or lookup. Ask nothing the project's wiki, `decisions.md` or the input documents already settle: Ground runs first so the questions are only the ones the record cannot answer.

## What to ask

- **What, not how.** Ask about the outcome and its behaviour: who uses it, what they see, what happens in a named case. Implementation choices (stack, lanes, engine, structure) stay as `Decisions for you` forks with recommendations. The form the requester or their audience receives (a live demo, a video, a deck, a shortlist they cut themselves) is an outcome, so it may be asked.
- **Concrete scenario.** Build each question from the requester's own material: named items, real files, a realistic case. Example: *"'Trip ideas' is in both Travel and Summer. When someone deletes Travel, what should happen to that note in Summer?"* — not *"Confirm the deletion requirements."*
- **Stand-alone.** Each question says in one line why it matters: what the answer changes in the work. No internal labels or fork IDs.
- **2 to 5 questions**, ordered by how much the answer would change the plan. If more than five seem needed, the request is not ready to plan; say so and ask the two that matter most.

## How to ask

- **One message, together with the plan.** Put the questions, numbered, at the top of the Plan Block message, and draft the plan below them on the stated defaults, marked `provisional on the answers`. A requester who steps away answers and gives go in one reply. Answers may be brief and in plain words.
- **Question first, default after.** Each question opens with the scenario and why it matters; the coordinator's default follows on its own line, labelled `Default if you skip:`. Keeping the scenario first makes the requester think about the case before reading the default; giving the default keeps every question answerable with "ok" or "skip", as core's pushback rule asks (`../../../core/references/pushback-and-teach.md`: recommend an option with its reason).
- **No default for facts only the requester holds.** When the answer is a fact the coordinator cannot reasonably assume (which client, which date, which files), write `No default: needed before go` instead of inventing one. The go does not stand until those are answered.
- **Answers and go.** If the answers match the defaults, or change nothing in the plan's stages, lanes, cost, goal criteria or (for client-facing work) its `Goal`, the go stands and the coordinator records the answers and dispatches. Otherwise the coordinator revises the plan and asks for go on the revised plan.
- **At most two more stops.** One follow-up round, only when an answer contradicts another answer or a recorded decision (name the contradiction), and one go on a revised plan. Where both are needed, send them together.

## Where the answers go

- **The run's ground record (`grounded.md`):** a dated `Intent` section appended for this run, listing each question, its default, and the requester's answer in their words (or "skipped").
- **Plan Block:** `Goal` is restated from the answers and lists them. `Decisions for you` keeps only choices still open; a skipped question is decided by its default and listed there as such. Where the coordinator sees a consequence of an answer the requester may not have weighed, it is stated beside that answer, and the answer stands unless the requester changes it.
- **Goal file:** a criterion that rests on an answer cites it, so Close checks the outcome the requester actually asked for.
