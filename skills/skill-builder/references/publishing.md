# Publishing a skill publicly

A skill authored inside real work absorbs that work: client names, figures, personnel, market and regulatory
detail. Those specifics are *why* the skill is good — they're the evidence its rules were earned. They are
also the thing that must not ship.

This page is the gate between "the skill works" and "the skill is public." Run it in order; the last step is
the only one that actually proves anything.

## 1. Generalize — setting abstracted, mechanism sharp

Replace each identifier with **the shape that carried the lesson**, not a blank:

*(Examples below use invented names — see the warning at the end of this section.)*

| Instead of | Write |
|---|---|
| "Contoso's RFI" | "a regulated financial-services RFI" |
| "priced at ᶜ1.918M" | "a high-hundreds-of-man-days engagement" (or drop the figure) |
| "the managed LLM service isn't GA in Westland-North" | "a required managed service not available in the mandated region" |
| "the Fabrikam Messenger channel" | "a regional messaging channel" |
| "a 448-row change log across 52 slides" | "several hundred logged changes" |

The mechanism stays sharp — the reader still learns exactly what to do. What blurs is *whose deal it was*.
Watch four categories people forget: **currency codes**, **regional platform names**, **market-specific
regulatory terms**, and **fine-grained counts**. Counts feel anonymous and are not: a 448-row change log
identifies the artifact instantly to anyone who worked on it.

**Your threat model is insiders.** A stranger cannot re-identify a deal from "a regulated financial-services
RFI in an emerging market." The client and your employer can — and they are the two audiences with the power
to act on it. Generalize against *them*.

> **Write this page's own examples with invented names.** A guide about scrubbing is the last place a real
> client name should survive, and it is exactly where one hides — the examples feel like *documentation*
> rather than *content*, so they don't get scrubbed. Use obviously-fictional placeholders and let the
> denylist catch you if you slip.

## 2. Sever the linkage in both directions

If real traces are kept privately (they should be — the evolution loop needs them), then:

- **The public repo must never reveal that private traces exist.** Not the repo name, not a path, not
  "(trace held privately)", not "evidence held internally". Advertising a systematic client-harvest archive
  *is* the disclosure, and it compounds with whatever sector hints remain. Verdicts stand unattributed:
  "validated on a second independent engagement" is the strongest permitted form.
- **The private repo's own framing matters too.** Raw retrospectives read as ordinary professional practice.
  A README describing *a pipeline for distilling client work into a published personal asset* is more
  incriminating than the notes it introduces. A leaked archive of candid notes is survivable; a leaked
  document explaining the system is not.

## 3. Build the denylist, then run it

> **The denylist is itself sensitive — never commit it to the repo it protects.** It is, by construction, an
> enumerated list of every name you are hiding. Publishing it alongside the scrubbed content hands over the
> exact thing the scrub removed. Keep it in the **private** traces repo (or outside version control) and
> pass `--denylist <path>`; add `.scrub-denylist` to the public repo's `.gitignore` as a second line of
> defence. This is the easiest self-inflicted leak in the whole procedure.

`scripts/scrub_check.py` takes a `.scrub-denylist` (one regex per line, `~` prefix = soft/report-only).
Cover: client names **and abbreviations** · employer/partner names · every personal name (yours, teammates,
client executives) · countries, regions, cities, sites · currencies and money formats · platform and channel
names tied to a market · regulatory terms · org/repo handles · brand names.

**Word-bound short tokens** (`\bABC\b`). An unbounded short name matches inside ordinary words — a colleague
named "Ann" matches every "announcement" in the repo, and the false-positive flood will train you to ignore
the tool exactly when it matters.

```bash
python scripts/scrub_check.py <repo>              # working tree
python scripts/scrub_check.py <repo> --history    # + every blob in git history
```

## 4. History is not the working tree

Scrubbing files does nothing about the commits that contain the unscrubbed versions — **and commit messages
carry names too** ("Evolution 2: harvest completed <client> engagement"). Check before assuming:

```bash
python scripts/scrub_check.py <repo> --history
```

If history is dirty, the only safe route is a **fresh root commit**:

```bash
git checkout --orphan main          # keeps working tree, drops all ancestry
git add -A && git commit -m "..."   # a root commit: 0 parents
git branch -m master pre-public-history   # keep the old record LOCAL, out of muscle memory
git push -u origin main             # push this branch ONLY — never --all
```

Verify it is genuinely a root commit: `git rev-list --parents -n1 HEAD` should show no parent hash.

**The old branch is now a live hazard.** It still holds everything, `git push --all` publishes it, and it
keeps `--history` permanently red — which trains you to ignore the gate. Preserve it properly and remove it:

```bash
git bundle create ../private-repo/<skill>-pre-public-history.bundle pre-public-history
git bundle verify ../private-repo/<skill>-pre-public-history.bundle   # confirm before deleting
git branch -D pre-public-history
git reflog expire --expire=now --all && git gc --prune=now
```

### Fix leaks by rewriting, never by committing a fix

If a leak is already committed, **a follow-up commit that removes it preserves it in the diff.** Deleting a
line records the line. The scrub gate will keep failing and it will be right.

The only fix is to rewrite so the bad content never existed: make a fresh orphan commit from the corrected
working tree, then `git push --force-with-lease`. (Plain `--force` risks clobbering work you haven't seen;
`--force-with-lease` refuses if the remote moved.) Afterwards, expire the reflog and `gc` — and remember
`git log --all` includes the **remote-tracking ref**, so the old commit keeps showing up locally until the
force-push lands and you prune.

## 5. Verify from a clean clone — the only step that proves anything

Everything above verifies your *intent*. This verifies the *artifact*:

```bash
git clone https://github.com/<you>/<repo>.git /tmp/verify-live
python scripts/scrub_check.py /tmp/verify-live --history
```

Clone what the world can actually fetch and scan that. A local working tree can be clean while the push was
partial, a branch leaked, or a file was gitignored locally but committed earlier. Gate on the clone.

## 6. The public-facing files

- **`README.md`** — what it is, install, **dependencies on sibling skills** (a skill that references
  `../core/…` is broken for anyone who doesn't install `core`; say so and link it), composition, and how it
  evolves. Say honestly that verdicts may be `PENDING`; a log that shows its own failures is more credible
  than one that doesn't.
- **`LICENSE`** — pick one deliberately. Confirm the copyright name with the author rather than inferring a
  legal name from a git config.
- **`.gitignore`** — belt-and-braces patterns for engagement material (office documents, scratch dirs). Two
  traps: over-broad globs (`*trace*` swallows `traceability-matrix.md`, which a presale skill legitimately
  needs), and — less obvious — **the `.gitignore` is public too**. An entry named after your private-file
  convention (`EVOLUTION-traces.md`) discloses that the convention exists. Ignore *categories*
  (`*.xlsx`, `scratchpad/`), not the names of your secrets.

## Pre-push checklist

- [ ] Every identifier generalized to a shape; currencies, platforms, regulatory terms, and counts included
- [ ] No reference anywhere to the existence of private traces
- [ ] `.scrub-denylist` written, short tokens word-bounded, and **stored outside the public repo**
- [ ] `scrub_check.py` clean on the working tree
- [ ] `scrub_check.py --history` clean, **or** a fresh root commit created and the old branch renamed
- [ ] README names sibling-skill dependencies and where to get them
- [ ] LICENSE present, copyright holder confirmed with the author
- [ ] **Cloned the published repo and re-scanned it** — this is the gate
- [ ] Repo visibility confirmed via API, not assumed from the create command
