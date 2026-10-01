# Dogfood run — 2026-09-27

Reader: whoever maintains `render-kit` next. This is one agent's real run through the
loop in `AGENTS.md` — no prior context with the kit, no help from `SPEC.md` beyond what
is logged below.

## What was made

Four artifacts in `design-programme/dogfood/run-1/`, built from the synthetic drilling
fixtures at `design-programme/fixtures/drilling/` (well "Larkspur-4"), by two small
stdlib-only Python generators kept in the same folder (`gen_charts.py`, `gen_slide.py`):

1. **`01-depth-time.svg`** — measured depth over 27 days (plus the spud point at day 0),
   as a line chart with a marker per day. Depth uses a reversed `data-rk-y-range`
   (`70,620` over domain `0,3900`) so depth increases downward on the page.
2. **`02-time-breakdown.svg`** — one stacked bar per day, 27 bars, segments = the 10
   operation codes in the data (`DRL, TRIP, CIRC, SURV, CSG, CMT, BOP, RIG, WOW,
   RIG-REPAIR`), each its own `data-rk-series`. The four real non-productive-time
   events (28.5 h total) are split out of their code's segment and drawn with a red
   outline and reduced opacity, same fill colour as the rest of that code.
3. **`03-trajectory.svg`** — true vertical depth against horizontal displacement
   (`sqrt(ns_m² + ew_m²)`) from all 128 stations in `survey.csv`, TVD reversed
   downward, a handful of station markers plus the connecting line.
4. **`04-slide-day10.html`** — 1920×1080 slide, "Daily drilling report, day 10", three
   KPI cards (depth 2800.5 m, progress 307.3 m, non-productive hours 0.0 — day 10
   genuinely had none), a resized/annotated variant of chart 1 with day 10 marked, and
   the depth KPI card marked `data-rk-focal`.

All values (depth, progress, NPT hours, survey geometry, operation-code hours) were
read out of the fixture JSON/CSV with a script, never hand-typed, so a `fidelity` fail
would have meant a real bug in the generator, not a typo.

## How the loop went

`rk selftest` passed cold on the unmodified kit. From there:

- **Chart 1** and **chart 3** passed all 11 checks on the first `rk check` — no
  iteration needed. Both are single-series line charts with generated, exact
  coordinates; nothing about them stressed the checks.
- **Chart 2** needed three rounds on `cvd` alone. Ten categorical series is a lot to
  spread across four colour-vision simulations at once; three different palette
  attempts each fixed the reported failing pair and immediately surfaced a new one
  elsewhere (see finding 3). `fidelity` passed on every attempt without changes —
  the stacked-segment geometry (cumulative `data-rk-y0` → `data-rk-y`) was right the
  first time once I'd read the exact rule in `SPEC.md` §6.8 (see finding 1).
- **Slide** needed one round: a 0.4–2 px text clip on the KPI numbers (`overflow`,
  caused by `line-height` too tight for the font's ascender) and a 4.27:1 contrast
  ratio against a 4.5:1 requirement on the focal card's label text (`contrast`). Both
  were genuine — fixed by loosening `line-height` and switching the label to white —
  and both checks passed cleanly after.
- `rk brief` produced a `brief.md` and `answers.template.json` for all four artifacts
  against the matching question set (`chart.md` ×3, `slide.md` ×1). I filled
  `answers.json` myself as `"dogfood agent (maker, not independent)"` and ran
  `rk brief --verify`:
  - Chart 1, chart 3, slide: no `no` answers; slide had one honest `unsure` (some
    empty space in the chart card). `verify` exited 0 for all three.
  - Chart 2: 5 of 8 `no` (first read, main takeaway, colour-only distinguishability,
    level of detail, tracing one code across bars) — real self-critique of a
    10-category stacked bar built to the letter of the brief's own requirement that
    every operation code get its own series. `rk brief --verify` correctly exited 1
    and listed exactly `["Q1","Q2","Q5","Q7","Q8"]`. I did not rebuild the chart to
    force these to `yes`: the brief's requirement (10 explicit series) and good
    colour-only legibility are in real tension, and that tension is itself worth
    recording rather than papering over.

I opened `SPEC.md` once, deliberately, because `AGENTS.md` left a real gap: see
finding 1 below.

## Final status

| Artifact | Last `rk check` | Report |
|---|---|---|
| `01-depth-time.svg` | **pass** (8 pass, 3 n/a, 0 fail) | `dogfood/run-1/check-01/report.json` |
| `02-time-breakdown.svg` | **pass** (9 pass, 2 n/a, 0 fail) | `dogfood/run-1/check-02/report.json` |
| `03-trajectory.svg` | **pass** (8 pass, 3 n/a, 0 fail) | `dogfood/run-1/check-03/report.json` |
| `04-slide-day10.html` (`--pdf`) | **pass** (11 pass, 0 n/a, 0 fail) | `dogfood/run-1/check-04/report.json` |

Brief reports: `dogfood/run-1/brief-0{1,2,3,4}/report.json`, `brief.md`, `answers.json`.

## Findings

| # | Severity | Finding | Evidence | Status |
|---|---|---|---|---|
| 1 | Medium | `AGENTS.md`'s markup table documents `data-rk-mark`'s attributes by name only ("`data-rk-x`, `data-rk-y`, `data-rk-x0`, `data-rk-y0` … as in 6.8") and never says which value is the bar's top and which is its base for a stacked segment, or that a reversed `data-rk-*-range` is a supported, intentional way to draw a downward-increasing axis. Both are stated precisely in `SPEC.md` §6.8 and §8 ("a reversed range … is allowed"), which `AGENTS.md` tells the reader to open only "when AGENTS.md leaves you unable to proceed" — this was that case. Without the SPEC read I would have had to guess whether `data-rk-y0` was the segment's own height or the cumulative base, and guessed wrong at least once given how the two are easy to conflate. | `AGENTS.md` markup table vs. `SPEC.md:171-179` ("its top and bottom edges must equal `scaleY(data-rk-y)` and `scaleY(base)` … where `base` is `data-rk-y0` if given"); confirmed by `check-02/report.json` `fidelity: pass` once built to that rule. | fixed: AGENTS.md updated (coordinator, run 1 close) |
| 2 | Medium | The CLI has no `--help` and no per-command flag help. `bin/rk --help` and bare `bin/rk` both just print a one-line usage string; flags like `check`'s `--pdf`/`--out-dir`/`--checks` and `brief`'s `--questions`/`--purpose`/`--verify` exist only in `AGENTS.md`'s two example command lines and had to be reverse-engineered by trial. | `bin/rk --help` → `{"error":"Unknown command: --help"}`; `bin/rk` (no args) → `Usage: rk <render\|check\|text\|brief\|selftest>`. | fixed: global and per-command usage now list command flags |
| 3 | Medium | Choosing a `cvd`-passing palette for a chart that legitimately needs many categorical series (10 operation codes here, driven by the brief's own "each operation code a `data-rk-series`" requirement) took three full `rk check` round trips: each palette fix resolved the reported failing pair and immediately exposed a new failing pair elsewhere in the 10×10×4-vision-type matrix. The check's math and threshold are well documented (`SPEC.md` §6.7) but there is no accompanying guidance or reference palette for the >8-category case, which is exactly where colour-only encoding is hardest to get right by hand. | `check-02` `cvd` failures across three attempts: `["CSG","RIG"]` 0.1178→ ok but `["CIRC","RIG"]` 0.0539 fail; then `["RIG","WOW"]` 0.037/0.0448 fail; fixed by moving `RIG` to `#0077BB`. Final `check-02/report.json`: `cvd: pass`. | fixed: `AGENTS.md` adds a 12-series palette, `cvd` guidance and alternatives beyond 12 |
| 4 | Low | `rk brief`'s `--out-dir` writes `answers.template.json`, not `answers.json`; the reviewer (or, here, the dogfood agent) has to know to copy the template before filling it in and calling `--verify`. `AGENTS.md` step 3 says the reviewer "fills `answers.json` from the template," which reads as if the tool produces `answers.json` directly. | `ls brief-01/` → `answers.template.json`, `brief.md`, `render.png`, `report.json` (no `answers.json` until copied). | fixed: AGENTS.md updated (coordinator, run 1 close) |
| 5 | Low | One `rk brief` invocation (the very first of the session, output piped through `tail`) reported an exit code of 1 with a fully normal, error-free JSON result (`brief.md`, images and `questions` count all present, nothing in stderr). Five subsequent identical invocations, run without piping through another command, all exited 0. Could not reproduce it in isolation, so this may be an artifact of my own shell pipeline rather than `rk` itself — logged for visibility, not confidence. | First call: `./bin/rk brief samples/good/chart.svg --questions questions/chart.md --out-dir <dir> --purpose "test purpose" 2>&1 \| tail -60` → tool-reported exit 1, JSON output otherwise identical to later exit-0 runs. | open |

No High-severity findings: every `fail` the kit produced across all four artifacts and the selftest suite was a genuine defect in my artifact (a real 0.4–2 px text clip, a real 4.27:1 contrast ratio, real too-close colour pairs), and every `pass`/`n/a` matched what SPEC.md says should happen. The mechanical checks did not give a wrong answer in this run.
