# The five elements — definitions, signals, where they hide, and where the lines fall

CERIC is Bjorn & Burgasser's method (cericmethod.com; *How to Critically Read the Scientific Research Literature*, Cambridge University Press, 2026). Definitions below are paraphrased from their workshop packet; the boundary rules are theirs where marked "key ruling" and this skill's where marked "observed".

## The elements

| Element | Tiếng Việt | What it is | Words that signal it |
|---|---|---|---|
| **Claim** | Luận điểm | The new knowledge the paper asserts: a direct answer to its research question. Often the title. | we find · we report · we show · we demonstrate · we have detected |
| **Evidence** | Bằng chứng | What the authors collected or built to support the claim: data, observations, instruments, samples, models, a simulation library. | we collected · we observed · we assembled · we surveyed · we simulated · using |
| **Reasoning** | Lập luận | The analysis and logic that connect the evidence to the claim: what was measured in the data, what it was compared with, what follows. | this shows · indicates · consistent with · we derive · we compare · we find that · rules out |
| **Implications** | Hệ quả | The future: why the result matters and what comes next. | this suggests · future work · a new tool for · will allow · remains to be |
| **Context** | Bối cảnh nghiên cứu | The past: what was known, and the gap that motivated the study. | prior work found · however · remains an open question · had not been · is expected to |

**The time rule.** For any phrase, ask: is this the *past* (Context), the *present argument* (Claim, Evidence, Reasoning), or the *future* (Implications)? Then, inside the present argument: was it *collected or built* (Evidence), *measured, derived or compared* (Reasoning), or *asserted as new* (Claim)?

A **subclaim** is a subordinate claim that must be true for the main claim to hold. A **hypothesis** is an untested claim. The **research gap** is the missing knowledge that motivates the study.

## Where each element hides (IMRaD map)

| Section | Elements you will find there |
|---|---|
| Title | Claim (a clear title states it) |
| Abstract | all five, compressed |
| Introduction | Context building to the Claim; look for the gap or rationale |
| Methods | Evidence, Reasoning |
| Results, figures, tables | Evidence, Reasoning, Claim (subclaims) |
| Discussion / Conclusion | Reasoning, Implications, Claim |

Read with a question, not from line one. Hunt the section the map names for the element you are missing.

## Boundary rules

These are where reads go wrong. Three strong models, reading the same paper unaided, broke rule 1 every time and rules 2 and 3 between them.

1. **Measured results are Reasoning, not Evidence** (key ruling). The instrument, the campaign, the sample, the simulation library are Evidence. The ring the authors resolved in the data, its diameter, the flux ratio, its stability across nights and pipelines, the model comparison and the mass that came out of it are Reasoning: analysis performed on the evidence. Test: *could this sentence exist before any analysis was run?* If yes, Evidence. If it reports what the analysis found, Reasoning.
2. **The authors' broad conclusion is a Claim, not an Implication** (key ruling). "Our observations provide powerful evidence for X in general" asserts new knowledge: a secondary Claim. "A new tool to explore X" is what comes next: an Implication. Test: *is the paper asserting this is now known, or saying what can now be done?*
3. **Analysis is not a Claim; a plan is not a Claim** (key ruling). "Consistent with a Kerr black hole" is Reasoning that supports the Claim "we have detected the shadow". "We will observe Sgr A*" is an Implication.
4. **A derived number is Reasoning even when it is a headline** (key ruling). The mass in the abstract is the output of the model comparison. It supports the claim; it is not the claim. If the paper's title is the mass, then it is the Claim.
5. **A hedge is part of the element it sits in.** "Consistent with", "candidate", "not inconsistent", "can be explained", "may", "cannot be excluded" set the strength of a Claim or a Reasoning step. Carry them into the paraphrase. Never replace them with prove, confirm, demonstrate, establish, definitive, unambiguous, or "is the X" where the paper says "consistent with the X". Where the paper's own strength changes between sections (abstract "consistent with", conclusion "we identify", title stated flat), record the ladder. That ladder is a finding about the paper.
6. **Context is stated past, not implied past** (observed). "First" and "newly" imply earlier work but name none. Tag them Evidence or Claim as their content dictates, and list the unstated prior work under *missing Context*.
7. **A method sentence is Evidence; the sentence that says why the method is trustworthy is Reasoning** (observed). "Four teams worked independently" is Evidence. "This avoids shared bias" is Reasoning. Do not tag both on the method sentence; the logic is where the logic is stated.
8. **A phrase can carry two elements; each tag needs its own reason** (observed). "We have resolved the source as a ring" is Reasoning (what the analysis found) and a subclaim (a ring must exist for the shadow claim). Write both reasons, or pick one.

### Worked example: the M87 abstract (Event Horizon Telescope Collaboration 2019, ApJL 875 L1), as the key marks it

| Phrase (abbreviated) | Element | Why |
|---|---|---|
| Title: "The Shadow of the Supermassive Black Hole" | Claim | The title asserts the detection. The key reads it as "[Detection of] the shadow…". |
| "black holes are expected to reveal a dark shadow…" | Context | The theoretical expectation; the past. |
| "we have assembled the Event Horizon Telescope… This allows us to reconstruct event-horizon-scale images…" | Evidence | The instrument and what it produced. |
| "We have resolved the central compact radio source as an asymmetric bright emission ring with a diameter of 42 ± 3 μas… recovered using different calibration and imaging schemes… stable over four different observations" | Reasoning | What the analysis of the data found and how it was checked. |
| "consistent with expectations for the shadow of a Kerr black hole… asymmetry… can be explained in terms of relativistic beaming… we compare our images to an extensive library of… simulations… and derive a central mass" | Reasoning | Comparison with theory and models; a derived number. |
| "provide powerful evidence for the presence of supermassive black holes in centers of galaxies and as the central engines of active galactic nuclei" | Claim (secondary) | The paper's broad assertion of new knowledge. |
| "a new tool to explore gravity in its most extreme limit and on a mass scale that was so far not accessible" | Implications | What can now be done. |

What the unaided reads did instead: filed the ring, the flux ratio, the four-day stability and the mass as Evidence (all three); filed the mass as a Claim (two); filed "powerful evidence for the presence of SMBHs" as an Implication (one); wrote "the image is the shadow of a Kerr black hole" where the paper says "consistent with" (one). Each is a half-mark off on the workshop's own scale.

## Hedge lexicon

Carry these verbatim from quote to paraphrase: *may · might · suggests · appears · consistent with · not inconsistent with · candidate · can be explained · cannot be excluded · disfavored · assumed · expected · likely · possible · tentative · preliminary · not yet · remains · limitation · caveat*.

Never introduce these unless the paper uses them for the same claim: *proves · confirms · demonstrates · establishes · definitive · unambiguous · certain · shows that · is the (X)* where the paper says *consistent with the (X)*.

## Missing is a finding

An element the paper does not supply is written down as absent, with why it matters and the research question it could inspire. It is never filled from another paper, from memory, or from what the paper "must have meant". Outside knowledge used to define a term is allowed and is marked †.
