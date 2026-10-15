# Attribution

This skill is derived from **Epic Infographics** by OrRon, MIT licensed.

- Upstream: https://github.com/OrRon/EpicInfographics
- Landed from plugin version `0.2.0` on 2026-09-18.
- Upstream `LICENSE` is kept verbatim beside this file and covers all inherited material.

**Inherited unchanged:** `references/charts.md`, `references/composition.md`,
`references/data-vocabulary.md`, `references/illustration-and-texture.md`,
`references/motion.md`, all thirteen files under `references/design-languages/`,
`templates/skeleton.html`, and `scripts/render.mjs`, `scripts/animate.mjs`.

**Inherited and modified:**
- `scripts/check.mjs` — canvas size made required (it silently defaulted to 1080x1080);
  added the `a3-landscape` preset, the drawn-representation and family count, the drawn
  share of page height, the hero ratio, SVG viewBox scale integrity, and a Type3 check
  on a printed PDF.
- `scripts/render.mjs` — canvas size made required, same defect; `a3-landscape` added.
- `scripts/topdf.mjs` — rewritten to take the same flags as its two siblings, which it
  did not; canvas size made required.

**Written for this skill:** `SKILL.md`, `references/fpt-brand.md`,
`references/legibility.md`, `references/acceptance.md`, `assets/**`, and
`scripts/legibility.mjs`, `scripts/probe.mjs`, `scripts/topdf.mjs`,
`scripts/measure.mjs`, `scripts/crawl.mjs`, `scripts/slack.mjs`,
`scripts/overflow-scan.mjs`, `scripts/accept.py`, `scripts/brandcheck.mjs`,
`scripts/pagetext.mjs`, `scripts/nocache.py`, `scripts/fonts.py`, `tests/**`,
`examples/**`, `EVOLUTION.md`.

**Not carried over from the plugin cache:** eleven superseded one-off probes
(`probe.mjs`, `probe-box.mjs`, `probe_v5`–`probe_v7`, `tw.mjs`, `tw2.mjs`,
`whitespace.mjs`, `ws2.mjs`, `cols.mjs`, `gaps.mjs`). `probe_v8.mjs` was folded into
`check.mjs` and deleted.

There is no upstream remote configured and no tracking branch. This is a copy, not a
fork: upstream fixes do not arrive automatically and must be pulled in by hand.
