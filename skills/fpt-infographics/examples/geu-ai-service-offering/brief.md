# Worked example — GEU AI Service Offering

The sheet this skill was built from. Eight versions, twenty-three hours, four rejections.
It is here to show the method end to end, not to be reused as content.

    cd examples/geu-ai-service-offering
    python build.py
    node ../../scripts/render.mjs sheet.html sheet.png --preset a3-landscape --scale 1
    node ../../scripts/topdf.mjs  sheet.html sheet.pdf --preset a3-landscape
    python ../../scripts/accept.py criteria.toml

Nothing here reads from the project it came from. `criteria.toml` proves it (N5), and
that suite is also the skill's integration test: if it passes, the skill works.

## The decisions, and what forced each one

| Decision | What it is | Why |
|---|---|---|
| Viewing condition | `a3-print` — 420 mm wide, read at 50 cm, k = 0.840 | Declared first, before any layout. Also within 4% of a PDF at 100% on a 24″ monitor, so one build serves both. |
| Canvas | 1754 × 1240, landscape | The reviewer chose landscape over portrait after seeing both. |
| Design language | `cutaway`, ground and geometry only | Warm paper and ink linework carry an estate drawing; its palette is discarded for the brand's. |
| Type floor | 16 px mixed case, 14.5 px all caps | Computed from the condition and BR Omega's own x-height of 0.470 em. Not chosen. |
| Audience | Client only | The internal variant carries every account name and deal value. It stays in the project. |

## Content, and where each part comes from

| On the sheet | Source |
|---|---|
| Five offerings, three pillars, the entry questions | `GEU - AI Service Offerings.pdf`, the internal template |
| Client-safe wording, TRUSTED BY, partners, accelerators | Slide 44 of the Fast-Track deck — the cleared, client-facing version |
| Data Hub phase names and durations | Enterprise AI Data Hub deck, slides 7 and 18 |
| Solution counts and reduction figures | FleziNergy site crawl, September 2026 |
| Win counts | The internal template, counts only |

**Withheld from the client sheet, deliberately:** every deal value, every pipeline
figure, every internal owner and sponsor, the pricing model, and ten customer names not
on slide 44's cleared list. Criteria S5 and S6 enforce both, against the *rendered text*
rather than the file — an embedded base64 font contains every short letter sequence you
could search for, and grepping the source found four matches that were not on the page.

## The eleven representations

Marked `data-viz="family:name"` so the preflight can count them. All six families of
`references/data-vocabulary.md` appear, which is what stops a sheet being five bar
charts in a row.

`magnitude` win pictograms ×4, accounts count · `process` Data Hub phases ·
`relation` AIX funding, pod nesting · `time` Fast Track gate ·
`part-to-whole` solutions bar · `category` reduction bars

## Measured

| | |
|---|---|
| Text at or above the 12′ floor at `a3-print` | **100%**, smallest 12.3′ |
| Smallest SVG viewBox scale | 1.000 |
| Drawn share of page height | 71% |
| Hero ÷ body | 128 px ÷ 16 px = 8.00× |
| PDF fonts | Type0 × 4 — no Type3 |
| Brand | 0 errors, 0 warnings |
| Acceptance | 13 pass, 1 superseded, 0 FAIL |

## Known and accepted

- **It cannot be read fit-to-window on a laptop.** 1% of the text clears the floor
  there against 100% at A3, and 23% falls below the acuity limit entirely. Send it
  saying "print A3 or view at 100%", or split it by pillar. `references/legibility.md`.
- **The delivery-model block is gone and nothing replaced its claim.** The sheet says
  nothing about how delivery is run. That was a deliberate trade for type size, recorded
  as criterion S8 SUPERSEDED with the goal clause that reversed it.
- **The logo slots carry wordmarks, not logos.** No logo file existed for any of the
  thirteen named organisations. Drop files into `assets/logos/<slug>.svg|png|jpg` and
  they are picked up with no layout change.
- **"Growth Engine for 2027+" is FPT's growth, not the customer's.** Worth a sentence
  from whoever presents it.
- **The One FPT question is open.** Guideline p.33 restricts the FPT Software mark to
  owned media. A cold outbound sheet is not obviously owned media, and `brandcheck.mjs`
  raises this on every run precisely because no script can settle it.
