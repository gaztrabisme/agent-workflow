# FPT brand — the rules, as checkable statements

Source: **FPT Software Brand Guidelines v4.0, August 2026**, 126 pages. Page numbers below
are that document's own. Every rule here is a restatement of a rule on that page, not an
inference from an example. Where the guideline hedges ("not recommended", "sparingly"),
this file keeps the hedge instead of hardening it into a ban — a rule stated stricter than
its source gets argued with and then ignored wholesale.

This file is law for **palette, typeface and logo**. A design language supplies ground,
geometry and devices; it does not supply colour or type. Where the two disagree, this file
wins and the design language's own palette is discarded. See `SKILL.md` §The two layers.

---

## 1. There are two palettes and they are not the same

This catches people every time. The guidelines say so themselves on both pages, and say the
difference is deliberate.

**Artwork palette (p.56) — use this for everything you build here.**

| Role | Name | HEX | Pantone |
|---|---|---|---|
| Primary | Orange | `#F37021` | 173 C |
| Primary | Blue | `#034EA2` | 293 C |
| Primary | Green | `#50B848` | 354 C |
| Secondary | Dark Violet Blue | `#19226D` | 2755 C |
| Secondary | Emerald | `#33B2C1` | 7466 C |

**Logo palette (p.32) — only inside the logo artwork itself, never in a chart or a panel.**
Orange `#F37021`, Blue `#0066B3`, Green `#0DB14B`.

> Checkable: no `#0066B3` and no `#0DB14B` anywhere in the page source. If either appears,
> someone has sampled a colour off the logo.

## 2. Colour usage

**Orange is the highlight, not the ground (p.57).** Used "frequently but not
overwhelmingly", and "mainly to highlight important details or grab attention". It combines
with black, white, Blue and Dark Violet Blue.

**Orange with Green or Emerald is not recommended (p.57)** — permitted only "very sparingly
or with other colors also included". Treat an Orange element sharing an edge with a Green or
Emerald element as a finding to justify, not an automatic failure.

**Blue and Green must not overshadow Orange (p.58).** Blue may be the dominant background
colour in most situations. **Green may be dominant only on a photographic image emphasising
sustainability** — so on a drawn sheet, Green is never the dominant colour.

**Neither Blue nor Dark Violet Blue may be combined with black elements (p.58).** This one
is absolute and easy to break by accident, because a default SVG `fill` computes to black.
Give every path an explicit fill; `fill="none"` counts.

**Gradients: minimum use (p.59).** For print, avoid entirely, the sole exception being
Dark Violet Blue → Blue.

## 3. Logo

**Full-colour logo only on a background that is at most 20% dark, or more than 85% dark
(p.33).** On a dark background the typography and the registered-trademark symbol change to
white. The 20–85% band is where the full-colour mark may not go at all.

> Checkable: sample the background behind the logo's bounding box and compute its darkness.
> Between 20% and 85%, fail.

**One FPT policy (p.33): the FPT Software logo must not be used for mass-media purposes.**
It is for owned media — internal communication channels, internal events — with exceptional
cases on mass media by arrangement. *A cold outbound sheet sent to prospects is not obviously
owned media.* This skill does not decide that question; it raises it once per artefact and
records the answer in the content brief.

**Partner logos** live in `assets/logo/partners/`, one file per variant, each with its source
and terms in that folder's `README.md`. Rule (Huy, 2026-09-25): choose by how the row reads.
Use official white logos when the ground has to be dark and every partner in the row has one;
otherwise use every partner's official full-colour logo on a light ground. One treatment per
row. Two white and one colour on a dark band was tried and rejected: the colour one read
weakly and the row looked inconsistent. Never recolour or redraw a partner's mark; all three
partners' terms forbid altering it. Each partner's permission terms are in the README; clearing them is the sender's
job, and the content brief records that it was raised.

## 4. Graphic element (the rounded-corner shape)

Optional. If used (p.63, p.66, p.67):

- Not more than **30%** of the design's space and visual attention. As a text frame, not
  more than **50%** (p.66).
- At least one rounded corner of the shape appears inside the design.
- Only to reinforce the identity **where it is lacking** — not as decoration on a page that
  already reads as FPT.
- Do not alter the shape ratio, alter the rounded corners, or crop them out. Do not combine
  two shapes into one with no visual distinction. No complicated effects. No colours outside
  the palette above (p.67).

## 5. Typography

**BR Omega is the primary typeface for all artworks (p.70, p.72)**, in print and digital.
Combine weights to build hierarchy — that is the guideline's own recommendation, not a
liberty. **BR Omega VN** carries the Vietnamese glyphs.

The substitutes are for other media and do not apply to a rendered sheet: Segoe UI for
shared Office files, FPT Daxline for FPT Corporation applications only and never as body
text (p.69), Inter for Google Docs.

**BR Omega ships as `.otf` — PostScript outlines — and must be converted before use.**
Chromium prints PDFs through Skia, which cannot embed a CFF web font and falls back to
Type3: unhinted, one content stream per glyph, which most viewers cache as a bitmap and
scale. That is what "pixelated when I zoom in" is. `scripts/fonts.py` does the conversion
and asserts the metrics do not move. Never point a build at raw `.otf`.

Measured metrics, 1000-unit em, after conversion:

| Weight | 400 | 500 | 600 | 700 | 900 | 400 italic |
|---|---|---|---|---|---|---|
| x-height | 470 | 473 | 479 | 484 | 492 | 470 |
| cap height | 700 | 700 | 700 | 700 | 700 | 700 |

An x-height of 0.470 em is small for a grotesque, and it is the reason the legibility floor
lands where it does: see `references/legibility.md`.

## 6. Design languages that can carry this palette

The inherited `references/design-languages/*.md` files each declare their own palette, and
this file overrides it. What survives the override is the language's **ground, geometry and
devices** — and that is only worth keeping where the ground does not fight the brand.

| Language | Verdict | Why |
|---|---|---|
| `cutaway` | **Yes** | Warm paper ground, ink linework, radii 0. Brand colour sits on it as accent. Shipped on the GEU sheet. |
| `blueprint` | **Yes** | Dark technical ground reads as Dark Violet Blue territory; white linework keeps Orange legible as the highlight. |
| `editorial` | **Yes** | Neutral paper and rules; the palette is free to do the work. |
| `naturalist-plate` | **Yes** | Plate ground and hairline detail; brand colour as the specimen accent. |
| `swiss` | Caution | Flat by construction and flagged high slop-risk upstream. Only on explicit request, and only with scene-craft imported. |
| `corporate-clean` | Caution | Same, and its default palette is the nearest to the brand, which makes the override invisible and the result generic. |
| `isometric-world` | Caution | Works, but needs a large colour count; keep to two colours per element (p.60 common mistakes). |
| `park-poster` | Caution | Its flat colour fields want to be dominant, and Green may not be dominant here. |
| `retro-print` | **No** | Built on off-palette inks and misregistration; overriding the colour removes the language. |
| `hand-drawn` | **No** | Informal register; wrong for a sheet carrying deal positioning. |
| `dark-glass` | **No** | Gradients and glows throughout, against p.59 and p.67. |
| `neo-brutalist` | **No** | Clashing colour is the point of it; flagged high slop-risk upstream. |
| `_template` | n/a | Scaffold for authoring a new language, not a language. |

Four yes, four caution, four no. Pick from the first column unless the brief says otherwise.
