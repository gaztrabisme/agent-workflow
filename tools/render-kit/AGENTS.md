# render-kit

Reader: an agent that renders and checks visual work with this kit, or changes the kit. The full contract is `SPEC.md`; this file is what you need day to day.

`rk` turns an HTML or SVG file into the PNG or PDF a reader will see and checks it with code: resources, console errors, font fallback, overflow, text collisions, contrast, colour-vision deficiency, data fidelity, accessibility, value and chroma (through the `color-theory` skill), and PDF fonts. It then writes a brief for a reviewer who can see images and did not make the artifact. The kit never calls a model.

## Quick start

```bash
npm ci
npx playwright install chromium
bin/rk selftest
bin/rk check page.html --pdf --out-dir out/
bin/rk brief page.html --questions questions/slide.md --out-dir out/review --purpose "Daily drilling report, slide 3"
```

## The loop

1. Write the artifact as HTML or SVG, with the markup below.
2. `bin/rk check <file> [--pdf]`. Fix every `fail`, and re-run until none is left. Read every `skipped` and `incomplete` reason; they are not passes. `n/a` means the input had nothing for that check (no chart markup, no PDF).
3. `bin/rk brief <file> --questions <set> --out-dir <dir>`. Give `brief.md` and the PNGs to a reviewer that did not make the artifact and can see images. It fills `answers.json` from the template.
4. `bin/rk brief --verify <dir>/answers.json`. A `no` is a failure to fix. When no reviewer can see images, the answers are `not-judged` and the report says so; they never count as passes.

## Markup the checks read

| Attribute | Meaning |
|---|---|
| `data-rk-stage` | The artifact's area (capture and the offstage test) |
| `data-rk-focal` | The focal area (value and chroma checks) |
| `data-rk-series="<name>"` | A categorical series (colour-vision check) |
| `data-rk-chart` + `data-rk-{x,y}-{scale,domain,range}` | A chart root and its scales |
| `data-rk-mark` + `data-rk-x`, `data-rk-y`, `data-rk-x0`, `data-rk-y0`, `data-rk-points` | A data mark and its values |
| `data-rk-allow-overlap`, `data-rk-allow-truncate`, `data-rk-ignore` | Deliberate exceptions |

Details and exact rules: `SPEC.md` sections 6 and 8.

## Rules for changing the kit

- Every change keeps `npm test` and `bin/rk selftest` passing. A new check comes with a good sample that passes it and a bad sample that fails only it.
- Dependencies are pinned to exact versions; add one only with a row in `SPEC.md` section 10.
- One concern per file, at most 120 lines of logic.
- Full Chromium in new headless mode only; never the headless shell.
- No `file://` loading, no open network by default, no model calls.
- A threshold states where it came from (the table at the start of `SPEC.md` section 6).
