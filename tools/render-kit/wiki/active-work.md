# Active work

Owner: render-kit maintainers  
Last reviewed: 2026-10-02

## Current state

Presentation dogfood finding F1 is complete: `overflow` reports when the first stage or an unstaged page exceeds Chromium's 16,384 px screenshot bound, and `rk check` keeps a bounded diagnostic PNG so it can write the failure report. `AGENTS.md` documents that only the first stage is used and gives a per-slide deck-check loop. F1's implementation and verification are recorded in `../FIX-REPORT-dogfood.md`.

Frontend dogfood findings F2, F4, and F11 remain complete. Expected HTTP failures can be declared by URL pattern and status; visual checks skip documented hidden patterns and accept wide content inside active horizontal scroll containers; and `rk brief` can include several labelled inputs in one review. The F13 motion fixes remain recorded in `../SPEC.md` and `../FIX-REPORT-dogfood.md`. Photo dogfood F12 is complete: multi-state briefs repeat each answer slot with its state label, and verification requires every state/question pair; single-state answer files retain their previous shape.

## Next steps

No follow-up is required for F1, F2, F4, F11, F12, or F13.
