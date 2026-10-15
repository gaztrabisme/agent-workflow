# Goal — land epic-infographics as the FPT skill

Fired 2026-09-18. Requested by Huy Tran Le. The goal paragraph as dispatched is at the
bottom, verbatim; **this file is not edited after dispatch** and a criterion that fails
is reported as failed rather than re-worded.

## Why

`epic-infographics` is a third-party plugin (MIT, `github.com/OrRon/EpicInfographics`).
The copy that runs lives in a version-stamped cache directory the plugin system owns:

    ~/.claude/plugins/cache/epic-infographics/epic-infographics/0.2.0/skills/epic-infographics/

Eighteen scripts written during the CTBC engagement were sitting in that directory —
sixteen under `scripts/` and two at the skill root — and the next `/plugin update` would
have erased all of them, including the 331-line legibility instrument. The plugin is also
invisible to `evolution/scripts/triage.py`, which reads the thirteen skills in
`~/.claude/skills/` and cannot see a plugin, so nothing tracked what it learned.

Evidence: 41 typed prompts over 23h35m in one session, 8 versions, 4 rejections,
9 review notes, 4 adversarial audits.

## Success criteria

Audited by `examples/geu-ai-service-offering/criteria.toml`, run with `scripts/accept.py`.

| # | Criterion | UAT | Result |
|---|---|---|---|
| 1 | The skill exists in the constellation, inherits `core`, declares gates, carries a ledger | `ls ~/.claude/skills/fpt-infographics/{SKILL.md,EVOLUTION.md}` | pass |
| 2 | Upstream LICENSE and attribution kept | `LICENSE` + `NOTICE.md` present, provenance stated | pass |
| 3 | Nothing points into the plugin cache | `python scripts/nocache.py` | pass |
| 4 | Brand assets carried, not referenced out | `assets/fonts/*.woff2` ×6, `assets/logo/`, `references/fpt-brand.md` | pass |
| 5 | Fonts are TrueType-flavoured; PDFs carry no Type3 | `check.mjs --pdf` reports `Type0` only | pass |
| 6 | The seven durable instruments survive; the superseded probes do not | `ls scripts/` | pass |
| 7 | Legibility takes a declared viewing condition and refuses without one | `legibility.mjs page.html` exits 1 and lists the conditions | pass |
| 8 | A sheet with nothing drawn on it fails the preflight | `check.mjs tests/fixtures/no-drawn-data.html --preset a3-landscape` | pass |
| 9 | A Type3 PDF fails the preflight | `check.mjs tests/fixtures/cff-type3.html --pdf tests/fixtures/cff-type3.pdf` | pass |
| 10 | The standing/new split is permanent, with a guarded SUPERSEDED state | `accept.py` on the example; guard demo | pass |
| 11 | The worked example rebuilds from the skill alone | `cd examples/... && python build.py` | pass |
| 12 | The rebuild reproduces the shipped numbers | `accept.py criteria.toml` → 13 pass, 1 superseded, 0 FAIL | pass |
| 13 | The ledger's first entry is written, verdicts PENDING | `EVOLUTION.md` | pass |

## Decided forward during the run

Recorded because these were decided without going back to the requester.

| # | Fork | Decision | Why |
|---|---|---|---|
| 1 | Does the worked example ship the internal sheet? | No — client render, source and brief only; `WINS_INTERNAL` deleted on the way in | A skill directory is read and copied far more casually than a project folder |
| 2 | Vendor `node_modules`? | No — gitignored, one `npm install` | 19 MB of binaries in git rots; the Chromium binaries are already shared |
| 3 | Fonts as base64 blob or files? | Files on disk, inlined at build time | The repo stays diffable and the emailed sheet stays self-contained |
| 4 | Keep the installed plugin? | Yes, untouched, for non-FPT work | Nothing is deleted |
| 5 | Gate the inherited animation code? | No | No trace of it in the record; never used |
| 6 | Where do the brand rules get enforced? | A new `brandcheck.mjs`, not inside `check.mjs` | Keeps the inherited file's diff small and the attribution honest |
| 7 | Content rules grep the source or the rendered text? | Rendered text, via a new `pagetext.mjs` | Grepping the source matched "TCV" ×3 and "PwC" ×1 inside embedded base64 fonts |

## Corrections to the record made during the run

- The goal paragraph says **sixteen** scripts in the plugin cache. The true count is
  **eighteen**: sixteen under `scripts/` and `cols.mjs` and `gaps.mjs` at the skill root.
  Seven were durable and moved; eleven were superseded one-offs and were left to die.
- The plan block said `geu-ai-offerings.html` was the v3 build with no charts. It is not
  — v4 overwrote that filename at 17:58 on 17 Sep and the file has four charts. **The
  no-charts page no longer exists on disk.** That check is proven against a fixture
  instead, `tests/fixtures/no-drawn-data.html`.
- No Type3 PDF survived either; v7's was re-rendered after the font fix. Proven against
  `tests/fixtures/cff-type3.html`, which sets type in the raw CFF `.otf` on purpose.
- `review-note-v8.md` records 34% of text clearing the bar at `laptop-fit`. Measured now
  on the rebuilt sheet: **1%** clears the 12′ floor, 77% is slowed, 23% is below the
  acuity limit. `references/legibility.md` carries the measured table.

## The goal, as dispatched

> Land the MIT-licensed epic-infographics plugin as a skill at
> `~/.claude/skills/fpt-infographics/` - a skill, not a plugin, so no plugin update can
> overwrite it as the next one would have erased the sixteen scripts now in the plugin's
> cache - keeping its LICENSE and attribution, inheriting core, declaring its gates, and
> carrying an EVOLUTION.md ledger so evolution/scripts/triage.py can see it, which it
> cannot today. Scope is FPT-wide: any brand-compliant sheet for any business unit, with
> the GEU AI Service Offering sheet as the single worked example carried as brief, client
> render and source, never the internal sheet, so the five GEU offerings, the cleared
> customer-name list, the drawn energy estate and every proportion tuned to that page stay
> in the CTBC project. Separate the two layers the plugin conflates: the FPT palette,
> typeface and logo are law for every output, while a design language still supplies
> ground, geometry and devices, and the skill names which of the thirteen inherited
> languages can carry the brand without a colour fight. Carry the brand assets - BR Omega
> converted from PostScript to TrueType outlines so Chromium stops emitting unhinted Type3
> glyphs that viewers scale as bitmaps, the FPT logo, and the guideline rules as checkable
> text (Orange never beside Green, at most two colours per element, full-colour logo only
> on bright grounds, graphic element under thirty percent) - because the guidelines PDF
> lives in this project and the next will not have it, recording that BR Omega is
> commercially licensed and this embedding is safe only while the skills repository has no
> remote. Rescue the seven durable instruments out of the plugin cache before it is
> refreshed and let the nine superseded one-off probes die rather than moving dead code.
> Generalise the legibility gate from v8's fixed bar of a printed A3 at fifty centimetres
> into a viewing condition the skill demands before it will build and then measures
> against. Close the six failure classes the feedback record contains, each of which the
> plugin's own preflight passed: a sheet with no drawn data on it at all, labels that
> narrate their own honesty, brand arriving only when asked, type below the threshold for
> fluent reading with charts silently shrunk by their own viewBox, claims with no source
> behind them including FPT citing its own marketing site as if it were outside
> corroboration, and internal deal data reaching a customer sheet. Make the
> standing-versus-new criteria split permanent, so a criterion won in an earlier version
> carries forward and a failure on it is reported as a failure rather than re-worded. Keep
> the two-audience mechanism as machinery while the cleared-names list stays project-side.
> Require one adversarial read against sources before delivery, as the plugin already
> requires looking at your own render. It is done when a fresh build of the worked example,
> run from the skill alone with nothing imported from business/work/, reproduces the
> shipped numbers - every text element at or above the declared bar, smallest SVG viewBox
> scale 1.000, lowest contrast at or above 4.5:1, zero Type3 font objects in the PDF, zero
> preflight errors from the repaired check - when the skill's acceptance script passes
> every row with any failure reported as a failure, when `grep -r "plugins/cache"` returns
> nothing anywhere in the skill, and when the ledger's first entry is written with its
> verdicts left at PENDING.
