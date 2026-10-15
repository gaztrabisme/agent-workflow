# fpt-infographics — evolution ledger

How this file works: `../evolution/SKILL.md`. Each entry states what changed, why, and a
verdict. Verdicts start at `PENDING` and are settled by a later run against real traces:
`KEEP` needs **two independent real uses**, `REVISED` means the change was right but
scoped wrong, `REVERT` means it was wrong and the post-mortem is never compacted away.

Nothing here may be marked `KEEP` on the day it was applied.

---

## Evolution 1 — landing the plugin as a skill (2026-09-18)

**Grounded:** 41 typed prompts and the tool histogram from the CTBC session
(`ff9c61d4`, 23h35m, 8 versions, 334 Bash calls), `evolution/scripts/triage.py` over 13
skills and 296 transcripts, `review-note-v8.md`, the plugin's git state, the skills repo
git state. → Constrains this: **one engagement of evidence.** Mechanical rules are safe
to codify from it; taste rules are not, and are marked below where they appear.

**Harvest scope.** `epic-infographics` appears in exactly one engagement — 41 prompts on
one artefact, plus one passing mention elsewhere. That is deep but narrow. Everything
here is a hypothesis about a second engagement that has not happened.

### What was wrong

The skill being improved was a third-party plugin living in a version-stamped cache
directory. Eighteen scripts written during the engagement sat in that directory and
would have been erased by the next plugin update. The plugin has no ledger and is
invisible to the triage script, so six recurring failures were rediscovered rather than
prevented, and the brand arrived last on five of eight versions.

### Hypotheses applied

| # | Change | Target | Predicts | Verdict |
|---|---|---|---|---|
| 1 | The plugin's content lands as a skill in the constellation, inheriting `core` and carrying this ledger | whole tree, `SKILL.md`, `NOTICE.md` | The next engagement's instruments survive a plugin update, and triage can see this skill | **PENDING** |
| 2 | Brand owns palette/typeface/logo; a design language owns ground/geometry/devices, with a per-language verdict table | `references/fpt-brand.md` §6, `SKILL.md` §The two layers | No future sheet ships off-brand because a style file said its tokens were law | **PENDING** |
| 3 | The legibility gate refuses to run without a declared viewing condition | `scripts/legibility.mjs` | No future sheet is judged "big enough" without saying at what size and distance | **PENDING** |
| 4 | The preflight counts drawn representations and their families, the drawn share of height, the hero ratio and SVG scale integrity; the canvas is required | `scripts/check.mjs` | A page with nothing drawn on it cannot pass again | **PENDING** |
| 5 | The PDF's font dictionary is checked for Type3 | `scripts/check.mjs --pdf` | No PDF ships whose text pixelates on zoom | **PENDING** |
| 6 | Brand conformance becomes an instrument, not prose | `scripts/brandcheck.mjs` | The brand stops arriving only when someone asks for it | **PENDING** |
| 7 | The standing/new criteria split becomes permanent machinery, with SUPERSEDED requiring both a replacement id and a quoted goal clause | `scripts/accept.py` | A requirement won in one version cannot silently regress in the next | **PENDING** |
| 8 | Content rules are checked against rendered text, not file bytes | `scripts/pagetext.mjs`, `accept.py` `text` type | No more false positives from embedded base64 fonts, and no more false confidence | **PENDING** |
| 9 | A guard script fails the build on any path into the plugin cache | `scripts/nocache.py` | The fault that created this skill cannot be reintroduced | **PENDING** |
| 10 | The GEU sheet ships as a worked example whose acceptance suite is the skill's integration test | `examples/geu-ai-service-offering/` | A change that breaks the skill is caught by rebuilding one real sheet | **PENDING** |

### Taste rules, marked as such

Three rules in `SKILL.md` §Hard rules came from a single reviewer's reaction on a single
engagement and have **one** data point, not two: no label that narrates its own honesty;
a label is a noun phrase of four words or fewer; a line under a table that restates the
table gets deleted. They are written down because they are checkable and because the
same person will review the next sheet. If a second engagement disagrees with any of
them, the right verdict is `REVISED` — scope it to this reviewer — not `REVERT`.

### What was checked at Close

Run: `cd examples/geu-ai-service-offering && python ../../scripts/accept.py criteria.toml`
→ **13 pass, 1 superseded, 0 FAIL (of 14)**, exit 0.

The superseded row is S8, the delivery-model block, quoting the goal clause that removed
it. It is not counted as a pass.

### Settled from the record, not carried forward

- The **v3 no-charts page does not exist** — v4 overwrote the filename. The check for it
  is proven against `tests/fixtures/no-drawn-data.html` instead.
- **No Type3 PDF survived** the engagement either; v7's was re-rendered after the fix.
  Proven against `tests/fixtures/cff-type3.html`, which uses raw CFF outlines on purpose.
- `review-note-v8.md`'s **34% at laptop-fit is wrong**. Measured on the rebuilt sheet:
  1% clears the 12′ floor, 77% slowed, 23% below the acuity limit.

### Open, for the next run to settle

1. **Do the four "caution" design languages actually work on brand?** The table in
   `references/fpt-brand.md` §6 is reasoned from each language's palette and ground, not
   from a built sheet. Only `cutaway` and `blueprint` have ever been built.
2. **Are the composition floors right?** 5 representations, 3 families, 30% drawn, hero
   4× are defaults chosen from one sheet's numbers (which were 11, 6, 71%, 8×). A second
   artefact of a different shape will say whether they are floors or accidents.
3. **Does the `family:name` convention survive contact?** It is new; the GEU sheet had to
   be retrofitted with it.
4. **The One FPT question is unresolved.** Guideline p.33 limits the FPT Software mark to
   owned media, and the founding artefact is a cold outbound sheet. `brandcheck.mjs`
   raises it every run; nobody has answered it.
5. **`animate.mjs` and `references/motion.md` are inherited and untested here.** No trace
   of motion in the record. If still unused at the next run, consider removing them
   (Wu Wei — `core` spine #9).

### Checklist for the next Phase 2

- [x] Were the instruments still in place, or did something point back into the cache?
- [x] Did a second artefact get built with this skill? Which design language?
- [x] Did the legibility gate's required-condition rule cause friction, or catch something?
- [x] Did `accept.py` record a SUPERSEDED row, and did it carry its quoted clause?
- [ ] Did any of the three taste rules get contradicted by a different reviewer?
- [x] Are the composition floors still the defaults, or did someone override them, and why?

Answered below. **No verdict above has moved.** One independent use is not the two that `KEEP`
requires, and nothing here was written on the day it was applied.

---

## Checklist answers — first independent use (2026-09-18)

**The artefact.** A client-facing profile of FPT Software's Global Energy & Utilities unit, at
`C:\Users\HuyTL10\Documents\CTBC\business\geu-profile\`. Built the same day the skill landed, on
purpose changing three things so that it tested the skill rather than repeating it: **A4 portrait**
(1240×1754) rather than A3 landscape, an **ad-hoc viewing condition** of a 210 mm sheet at 400 mm
(`k = 0.525`) rather than a named preset, and the **`editorial`** design language, which the brand
table marks "Yes" and which nobody had built. Four research streams and two verifiers fed it.

**Were the instruments still in place?** Yes. `nocache.py` clean, `fpt-infographics/` unmodified
since `76bbeff` — the build was run entirely from the skill as committed, and the run's goal
forbade editing it so that a misfiring gate would be recorded rather than papered over.

**Did the required-condition rule cause friction, or catch something?** It caught something before
any layout existed. At `k = 0.525` the floor is 17.54 px against the founding sheet's 15.51 px, so
the page carries type 13% larger on a canvas 29% narrower and holds roughly 40% less per unit of
area. The first build ran 200 px past the canvas and every recovery was paid in leading and chrome.
No friction: the `--sheet-mm / --distance-mm` path worked first time.

**Did `accept.py` record a SUPERSEDED row?** No. Nothing on this artefact reversed a standing
criterion, so the machinery was not exercised. Still unproven in the field.

**Are the composition floors right?** They held without being argued with: 5 representations across
5 families (the floor is 5 and 3), 52% drawn against a 40% floor, hero exactly 8.00× — and that
last one is the interesting number. The hero ratio *set* the type size rather than describing it:
body 18 px forced a 144 px hero, and 144 px is where the title landed. On a portrait canvas the
floor is a binding constraint, not a check.

**The taste rules** were not tested. The same reviewer has not seen this sheet.

### Findings against the skill, from using it

Recorded, not fixed — the run's goal forbade editing the skill, on the reasoning that a first
independent use which quietly works around its own instruments measures nothing.

| # | Finding | File |
|---|---|---|
| 1 | **`legibility.mjs` decides "is this all caps?" from `node.textContent`**, which CSS `text-transform: uppercase` does not change. A label written mixed-case and uppercased in CSS is judged against the 12′ x-height threshold instead of the 16′ cap-height one — an x-height none of its rendered glyphs has. Measured on a fixture: identical pixels, **11.3′ and "slow"** from mixed-case source, **16.4′ and "ok"** from literal capitals. Errs safe (demands a larger size) but makes the ISO cap rule unreachable for any CSS-uppercased label, and the requirement to write capitals literally is nowhere in the skill. | `scripts/legibility.mjs:278` |
| 2 | **`accept.py` runs `.format()` over a `text` criterion's regex.** `_fmt(chk["pattern"], meta)` at line 217 substitutes `{artefact}` — so `[^.]{0,40}` or `\d{1,3}` raises `KeyError: '0,40'`. Bounded quantifiers are among the most ordinary things in a regex. Reports as FAIL, so nothing passes silently. | `scripts/accept.py:217` |
| 3 | **`accept.py`'s `text` check hard-codes `re.M` with no way to request case insensitivity.** An inline `(?i)` is the only route and Python rejects it unless it is at position 0, so it cannot be joined to other alternatives. A `flags` key would remove the class. | `scripts/accept.py` `run_text` |
| 4 | **`check.mjs --json` carries no contrast, no width and no height.** Contrast appears only as an error line and the canvas dimensions appear nowhere, so "lowest contrast is at or above 4.5:1" and "the canvas is A4 portrait" cannot be written as `json` criteria against the preflight at all. Both had to move to a project-side `python` check reading `legibility.mjs --json`, which does carry `W`, `H` and a per-row `contrast`. The SVG key is `svgScaleMin`, not the `minSvgScale` its error name suggests. | `scripts/check.mjs`, `scripts/accept.py` |
| 5 | **`editorial` loses its identity carrier to the brand rule.** The language file names Fraunces 900 as "typography at extreme scale" and names Fraunces or Libre Franklin in all five of its signature devices. BR Omega is law, so the serif goes and what survives is warm paper, radii 0, rules instead of boxes, a column grid, and the devices' geometry without their typeface. | `references/design-languages/editorial.md` vs `references/fpt-brand.md` §5 |
| 6 | **Every gate passed on a page that was flat, typeset and bland, and the reviewer said so.** The first sheet cleared the preflight, the brand check and the legibility gate with 5 representations in 5 families, and had **no drawn subject at all**. `composition.md` names this exactly — "flat graphic minimalism is a slop signal in itself", and "if the answer is 'looking at a well-designed page', start over" — but **nothing in the toolchain measures it**. `check.mjs` counts representations and drawn share; a page of bar strips and hairlines satisfies both. This is the largest gap in the instrument set: the skill can prove a sheet is correct and cannot tell you it is dead. | `scripts/check.mjs`, `references/composition.md` |
| 7 | **No gate catches text sitting on top of a drawing.** `check.mjs` tests text against other text and against overflow-hidden containers. A title placed over an illustration collides with nothing it measures. Found only by opening the PNG. | `scripts/check.mjs` |
| 8 | **The preflight cannot see text that overflows its own SVG.** An SVG does not clip by default, so a label longer than the space its chart left it paints outside the viewBox, stays inside the canvas, and passes. It happened twice here. | `scripts/check.mjs` |
| 10 | **`legibility.mjs` cannot measure contrast for SVG text on a dark sheet.** It resolves an SVG text element's background by looking for an enclosing `<rect>` with a fill, and falls back to a hard-coded paper constant when it finds none — so on a Dark Violet Blue ground every chart's text reported **1.05:1** for type that actually measures 6.6:1 or better. Two conditions make it fail: a chart with no background rect at all, and a glyph box that crosses its enclosing rect's edge by a pixel, which drops the lookup back to paper. Both are fixable in the *sheet* — declare a ground rect in every chart, fill boxes with the ground instead of `fill="none"`, and keep baselines clear of box edges — and all three are things a dark sheet has to know. None of them is written down anywhere. **The gate failed safe and was right to fail**, but a first-time author on a dark ground would read 1.05:1 and have no idea why. | `scripts/legibility.mjs` `svgBgOf` |
| 9 | **`brandcheck.mjs` earned its place.** Moving a content block onto a Dark Violet Blue field surfaced a real guideline violation in the same minute: an SVG group with no explicit fill computed to `#000000`, and p.58 forbids black beside Blue or Dark Violet Blue. Its error text named the cause before I had looked. **This is the one gate in the set that found a fault looking would not have found.** | `scripts/brandcheck.mjs` |

| 11 | **The brand reference stops one page short of the rule that governs a branded dark ground.** `references/fpt-brand.md` §3 records p.33 — full-colour mark only under 20% dark or over 85% dark, typography and ® white on dark — and stops there. **p.34 is the next page and it is the one that applies to any sheet drawn on an FPT colour:** *"On other background colors, the white or black version of the FPT Software logo should be used instead. The white version must be used for backgrounds using brand colors."* On the Dark Violet Blue ground of this build the all-white mark is **required** and the full-colour mark is wrong. Three parts of the skill are affected: the reference does not carry the rule, `assets/logo/` ships only a full-colour PNG so an author has nothing else to reach for, and `brandcheck.mjs` §3 has no p.34 test — it passed the full-colour mark at 98% dark under p.33 and printed a note asking a human to confirm the typography by eye. **The note fired for the wrong reason and a human who confirmed it by eye would have confirmed the wrong thing.** | `references/fpt-brand.md` §3 · `scripts/brandcheck.mjs` §3 · `assets/logo/` |
| 12 | **The skill frames the One FPT question so it cannot be answered, and the guideline answers it.** §3 of the brand reference says *"A cold outbound sheet sent to prospects is not obviously owned media. This skill does not decide that question; it raises it once per artefact."* That makes the test owned-media-versus-not, which has no answer for a client document — which is why two artefacts across two engagements both recorded it unresolved. The guideline's own sentence, printed verbatim on pp. 32, 33 **and** 34, makes the test **mass-media-versus-not**: *"FPT Software logo must not be used for mass media purposes, to comply with the One FPT policy. The FPT Software logo can be used on owned media (internal communication channels, internal events, or any exceptional cases on mass media)."* A sheet sent to a named client is not mass media and the prohibition does not reach it. The guideline also names the authority for an exceptional case — FPT Software MCP.GBC.Communications, **MCP.PR@fpt.com** — on all three pages, and the skill's reference omits it, so a reader who wants the answer in writing is not told where to get it. | `references/fpt-brand.md` §3 |
| 13 | **No gate measures whether a page argues anything, and this run proved the cost twice.** Build 1 and build 2 both cleared every instrument — preflight 0/0, brand 0/0, 100% above the legibility floor, 5 representations in 5 families, Type0 fonts — and the reviewer called the first *"not wow enough, no graphics, kinda bland"* and the second *"like 7/10, this is sth HR gonna nod at and say cool then file it to somewhere forgotten"*. The second verdict was not about polish: the sheet listed facts and argued nothing. The argument it needed was in the sources from the first hour, in a cleared slide's own speaker notes, and two builds walked past it because nothing in the skill asks *what does this page claim*. Finding 6 named the visual half of this gap. This is the other half, and it is the more expensive one — a page can be drawn, textured and beautiful and still be a catalogue. **A "what is the one sentence this page argues, and where in the sources is it" step belongs in the compose stage, before layout.** | `references/composition.md`, `SKILL.md` |

### Open questions, revisited

1. **The four "caution" languages** are still unbuilt. This run used a "Yes" — `editorial` — so the table's four rows at Caution and four at No are still reasoned rather than built. Two of thirteen were built before; three now.
2. **The composition floors** now have a second data point. See above.
3. **The `family:name` convention survived contact.** It was used from the first line of a new file rather than retrofitted, and the preflight counted 5 families without argument.
4. **The One FPT question is closed, against the guideline itself.** It was recorded unanswered on two artefacts because the skill framed it as owned-media-versus-not. The guideline bars **mass media**; a sheet sent to a named client is not mass media. Finding 12. `brandcheck.mjs` will keep raising it until §3 of the reference is reworded, and a fix for that is not applied here because this run may not edit the skill's references.
5. **`animate.mjs` and `references/motion.md` are still unused.** No trace of motion in this run either. Second consecutive engagement with no use.
