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

### Every remote branch, not just the one you're on

**A scan of your current branch can report clean while a full copy of the leak sits one branch over.**
Stale feature branches, abandoned agent branches, and anything pushed and forgotten are complete copies of
the history you are trying to clean — and `filter-repo` will not touch a branch that exists only on the
remote, because it rewrites *local* refs.

Enumerate the remote before you believe any result:

```bash
git ls-remote --heads origin              # what the world can actually fetch
git fetch origin                          # pull them into local refs so --history sees them
for b in $(git branch -r | grep -v HEAD | sed 's|origin/||'); do
  git branch --track "$b" "origin/$b" 2>/dev/null
done
```

Then re-run the scan. Do not delete a stale branch to make the scan pass without reading it first — an
abandoned branch is exactly where unmerged work hides, and deleting it destroys content that exists nowhere
else.

### Preserve history when it's worth keeping — redact, don't orphan

The orphan procedure above is the blunt instrument: guaranteed clean, but it discards every commit. When the
repo has real history worth keeping (an evolution ledger, a decision trail), **`git-filter-repo` redacts the
identifiers across every blob and commit message while preserving the commit graph**:

```bash
cat > redactions.txt <<'EOF'
Documents/Work/Contoso==>an internal work path    # longest/most specific FIRST
Contoso Accelerator==>an internal accelerator
Contoso==>the employer
EOF
git filter-repo --replace-text redactions.txt --force
```

Order matters — entries apply in sequence, so a bare `Contoso==>` listed first will mangle the longer
strings before they match. Two gotchas: `filter-repo` **removes the `origin` remote** as a safety measure
(re-add it), and removing the remote also destroys the remote-tracking refs that `--force-with-lease` needs
for its baseline, so the push fails with `stale info`. Fix that by pinning the lease explicitly rather than
falling back to a bare `--force`:

```bash
git remote add origin <url>
git push --force-with-lease=main:<known-remote-sha> origin main
```

Cleanest when several branches are involved: run it in a **fresh clone** (which has every branch in its
original form), then push each branch from there. Filtering an already-filtered repo produces a duplicated
parallel lineage.

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
cd /tmp/verify-live
for b in $(git branch -r | grep -v HEAD | sed 's|origin/||'); do
  git branch --track "$b" "origin/$b" 2>/dev/null      # every branch, or you scan one of them
done
python scripts/scrub_check.py /tmp/verify-live --history
```

Clone what the world can actually fetch and scan that. A local working tree can be clean while the push was
partial, a branch leaked, or a file was gitignored locally but committed earlier. Gate on the clone.

**Check what is actually tracked, too.** A leak you find in your working tree may never have been published
(untracked file), and a file you assume is local may be committed. `git ls-files` is the authority — not
`ls`. Report the difference honestly rather than overstating or understating the exposure.

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

## 7. The gate is not one-time, and it is not per-repo

The failure this page was written for is a *publish-time* leak. The failure that actually happens is
**drift**: a skill published clean months ago, then evolved, harvested, and re-pushed a dozen times — each
edit written inside real work, each one a chance to reintroduce an identifier. Meanwhile a sibling skill was
made public without ever running the gate at all, because the gate lived in the head of whoever published
the *first* repo.

Two rules follow:

- **Scan the constellation, not the repo you happen to be publishing.** Identifiers are shared — the same
  employer, manager, and client accounts appear across every skill authored in that job. So the denylist
  should be shared too: keep one `all-skills.scrub-denylist` in the private store covering what is common,
  with per-engagement lists supplementing it. A per-skill denylist silently misses a sibling's client.
- **Re-run the sweep on a schedule, not on a trigger.** Before any push is the floor; a periodic sweep across
  every public skill is what actually catches drift. Confirm visibility from the API each time
  (`gh repo view --json isPrivate`) — a repo you believe is private is a belief, not a fact.

```bash
for s in <skill> <skill> …; do
  python scripts/scrub_check.py "$s" --denylist ~/…/all-skills.scrub-denylist --history
done
```

When the sweep finds a new identifier (a client you hadn't listed, a codename), add it to the shared
denylist immediately — the value of the list is that it accumulates, and the one you skip adding is the one
that ships.

## Pre-push checklist

- [ ] Every identifier generalized to a shape; currencies, platforms, regulatory terms, and counts included
- [ ] No reference anywhere to the existence of private traces
- [ ] `.scrub-denylist` written, short tokens word-bounded, and **stored outside the public repo**
- [ ] `scrub_check.py` clean on the working tree
- [ ] `scrub_check.py --history` clean, **or** history redacted (`filter-repo`) / a fresh root commit created
- [ ] **`git ls-remote --heads origin` enumerated** and every branch scanned — not just the current one
- [ ] Unmerged work on stale branches read before any branch is deleted
- [ ] README names sibling-skill dependencies and where to get them
- [ ] LICENSE present, copyright holder confirmed with the author
- [ ] **Cloned the published repo, tracked every branch, and re-scanned it** — this is the gate
- [ ] Repo visibility confirmed via API, not assumed from the create command
- [ ] Sibling skills swept with the shared denylist — the leak is rarely only in the repo you're publishing
