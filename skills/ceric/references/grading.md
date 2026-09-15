# Grading a CERIC read

The instrument for scoring a CERIC read — your own before you hand it over, a subagent's before you trust it, or a participant's against a key. It is the workshop's own instrument (Bjorn & Burgasser grade a human expert 5/5 and an unaided DeepSeek run 3.5/5 with it), not one invented here.

## The score

Per element, against the source of record (the article itself; a key if one exists):

| Mark | Worth | Means |
|---|---|---|
| ✓ | 1 | The element's content matches the article and sits inside its boundary (see `elements.md`). |
| ○ | ½ | The core is right, but a load-bearing part is misfiled into another element or missing. Examples from the calibration run: measurements filed as Evidence; the paper's secondary claim filed as an Implication; the interpretive chain present but the validation chain, the rejected alternatives and the generalising step absent. |
| ✗ | 0 | Absent, wrong, or fabricated. |

Total out of 5. **Threshold to ship: ≥ 4.0.** Below that the read has at least two elements wrong in a way a reader will repeat.

## The five failure modes — PASS / FAIL rows

Each row needs its evidence line: the quote, the line, the check output.

| # | Failure mode | Detected by | FAIL when |
|---|---|---|---|
| a | A quote that is not in the article | `scripts/check_quotes.py` — every quote scored against its stated page ± 1; eye-check bucket for math-heavy quotes | any FLAG survives a human look at the rendered page |
| b | An element misidentified | `elements.md` boundary rules + `check_narrative.py` row lints (Evidence rows carrying result signals, Claim rows carrying future tense) + the grader | more than one misfiling in the notes |
| c | An absent element filled in | the missing register exists and names what the article does not give; the grader checks each "found" item against the article | any element content that the article does not contain |
| d | The authors' caution erased | `check_narrative.py` hedge and strengthener lints + the grader comparing each Claim/Reasoning sentence with its quote | a hedge in the quote is absent from the paraphrase, or a strengthener appears that the article never uses |
| e | Information added from outside | `check_narrative.py` numbers/terms-not-in-paper lints + the † convention | any untagged number, name or mechanism that is not in the article |

**Pass condition for a read:** score ≥ 4.0 · a, c, e = 0 · d = 0 on Claim and Reasoning · b ≤ 1 · mechanical rows green (eye-check rows resolved by a look at the page).

## Grading without a key

Grade against the article only: it is the source of record with or without a key. The boundary rules (`elements.md`) and the five failure modes still apply. Say in the scorecard that no key was used.

## Mechanical vs grader

| Check | Mechanical | Grader |
|---|---|---|
| Quote exists on the stated page | `check_quotes.py` | resolves eye-check rows |
| Every element row has a quote **or** is marked MISSING/THIN with a reason | `check_narrative.py` (shape) | whether the marking is right |
| Narrative: one paragraph, CCERI order, word band 150–450, no 8-word run copied from the article, each builder stem opens a sentence | `check_narrative.py` | whether the merged paragraph is truly in CCERI order after smoothing |
| Hedges survive; strengtheners absent | lint | judgement per sentence |
| Numbers and capitalised terms trace to the article or carry † | lint | judgement per item |
| Per-element ✓ ○ ✗ | — | grader, against the article (and the key) |
| Missing register is honest | — | grader |

Run the mechanical half with one command: `scripts/ceric_check.py <run_dir> --paper <pdf|txt>` (add `--freeform` for notes that do not use the templates).

## Grading procedure

1. Run `ceric_check.py`; keep its table. Resolve every eye-check row by reading the rendered page (the paper's tables and error bars do not survive text extraction).
2. Read the notes element by element against the article. Mark ✓ ○ ✗ with a one-line reason and the line that proves it. Apply the boundary rules literally: collected or built → Evidence; measured, derived, compared → Reasoning; what the paper asserts as new → Claim; what comes next → Implications; what came before and the gap → Context.
3. Fill the five failure-mode rows, each with its evidence line.
4. Check the missing register: is each listed absence really absent from the article? Is anything the article omits presented as found?
5. Write the scorecard: five element rows, five failure-mode rows, the mechanical rows, then ranked findings (most severe first, each with the fix).

A grader is a **cold reader**: it gets the run, the article and the instrument, never the reader's reasoning. Two graders on different models beat one grader twice — where they diverge, the judgement is soft, and that is where a human should look.

## Calibration

Three unaided reads of the same article (Claude Opus 5, Codex, Grok 4.6; 2026-09-15) and the workshop's DeepSeek run (3.5/5) are the baselines. A version of this skill that does not lift a fresh reader above the best of them added nothing. The calibration scorecards live with the fixtures (`$CERIC_FIXTURES`, default `~/Documents/Work/lab/ceric`, private; the article itself is CC BY 3.0 — DOI 10.3847/2041-8213/ab0ec7).
