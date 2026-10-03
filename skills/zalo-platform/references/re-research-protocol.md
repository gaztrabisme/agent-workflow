# Re-research protocol

How this skill stays true. Zalo's docs move — the messaging model changed on
01/01/2026, packages were discontinued on 01/06/2026, and the developer
documentation was **rehosted entirely** between 2026-07-21 and 2026-08-06. A
skill that reports 2026-07 facts as current in 2026-11 is worse than no skill,
because it is confidently wrong at exactly the moment a price goes into a
contract.

Two instruments, for two different kinds of fact:

| Instrument | Gets | Misses |
|---|---|---|
| **Crawl** (`crawl_zalo.py`) | Everything server-rendered — the bulk of it | Anything the browser computes |
| **Navigate** (`chrome-devtools` MCP) | Accordions, toggles, estimators, login-walled pages | Nothing, but it is slow and manual |

Crawl for coverage. Navigate for the handful of values crawling structurally
cannot see. Neither substitutes for the other.

---

## 1. When to re-research

| Trigger | Action |
|---|---|
| `kb_search.py --stale` says **>90 days** | Full re-crawl before answering anything commercial |
| **>30 days** and a price/policy answer is needed | Navigate the specific pricing page live; do not quote from the corpus alone |
| `kb_search.py` returns **no hits** on a topic that should exist | Coverage gap → targeted re-crawl. **Never fill the gap from memory** |
| A number is about to enter a **quote, contract or proposal** | Verify live regardless of corpus age. This one is not optional |
| An answer contradicts something the client's own vendor/BSP asserts | Re-read the primary page and cite it |
| Zalo announces a product change | Re-crawl the affected source |

---

## 2. The crawl loop

```bash
S=~/.claude/skills/zalo-platform

# 1. How old is the corpus, and what is in it?
python3 $S/scripts/kb_search.py --stale
python3 $S/scripts/kb_search.py --list-sources

# 2. Crawl fresh, somewhere else — never over the corpus you still need to diff
python3 $S/scripts/crawl_zalo.py --out /tmp/zalo-new
#    …or one surface:  -s platform-docs  -s solutions  -s bot  -s developers-legacy
#    check the frontier first with --dry-run

# 3. What moved, and which digests stand on it?
python3 $S/scripts/staleness_check.py --new /tmp/zalo-new

# 4. Read every hot change
python3 $S/scripts/staleness_check.py --new /tmp/zalo-new \
        --diff text/solutions/zalo.solutions__oa__pricing.txt

# 5. Update the digests the report named under "cited by" — THEN adopt
python3 $S/scripts/staleness_check.py --new /tmp/zalo-new --promote

# 6. Record the round in EVOLUTION.md
```

**Do not `--promote` before step 5.** Promotion overwrites the old text, and with
it the evidence for the edits you still owe. The report's "cited by" lines are
the work list; a promote with an empty work list is how a digest silently
diverges from its own citation.

### Sources, and why each is crawled the way it is

| Source | Frontier | Note |
|---|---|---|
| `platform-docs` | `docs.zaloplatforms.com/sitemap.xml` (~717) | **The unified hub, and the primary source** — MA 439, OA 179, ZBS 34, Social 33, BOT 19, TS 7 |
| `developers-legacy` | `stc-developers.zdn.vn/docs/sitemap.xml` (~317) | **Decommissioned in place 2026-08-06** — all 317 URLs return 200 with a ~450-char placeholder. Crawled only as a **tripwire**. URLs rewritten `developers.zalo.me/docs/X` → `stc-developers.zdn.vn/docs/v2/X` |
| `bot` | `bot.zapps.me/sitemap.xml` (~26) | Also mirrored at `platform-docs/docs/BOT` |
| `solutions` | link-following from seeds | `zalo.solutions` + `oa.zalo.me` — commercial and policy pages. No usable sitemap, but ordinary server-rendered pages, so link-following suffices |
| `archive-*` | — | Superseded snapshots, kept so older citations resolve. **Excluded from search by default**; opt in with `-s archive-<source>` |

### Three crawl traps, all of which have already cost a research round

1. **Docusaurus renders its sidebar client-side.** A doc page's server HTML
   contains ~12 nav links, not the tree. A link-following crawler reaches a
   dozen pages *and reports success*. Always drive from `sitemap.xml`.
   (Measured 2026-08-06: link-following 12 pages, sitemap 318.)
2. **`developers.zalo.me` serves its docs in an iframe from a CDN.** Fetching the
   pretty URL returns a contentless shell. This is what made an earlier round
   conclude the docs were un-crawlable and hand-drive a browser for hours. Rewrite
   to the CDN host and it is ordinary HTML.
3. **A 200 is not content.** When Zalo retired the legacy CDN it did not 404 or
   redirect — it kept answering 200 and served a placeholder. A crawler that
   checks status codes reports a perfect run while archiving 317 empty pages.
   This is why `staleness_check.py` compares **text**, never status, and why the
   dead host is still crawled: the diff is the only thing that can see it.

---

## 3. When to navigate instead — and what to navigate

Use the `chrome-devtools` MCP when the value is produced by the browser. Known
targets, each already identified as a gap:

| Target | Why crawling cannot see it |
|---|---|
| `zalo.solutions/oa/pricing` — **6-month price column** | Behind a 6 tháng / 1 năm toggle; the crawl captures whichever state is default |
| `zalo.solutions/oa/pricing` — package comparison rows | Table cells extract positionally; per-package allowances need visual confirmation |
| `zalo.solutions/business-message/pricing` — estimator | Computes a combined price from template + buttons + components on selection |
| `bot.zapps.me` FAQ accordions | Bodies load on click. ✅ Read 2026-08-06 — closed the proactive-send question |
| `oa.zalo.me/home/...` policy pages | Several returned 0 characters to the crawler — client-rendered |

**Navigation procedure:**
1. `new_page` → `navigate_page` to the URL.
2. `take_snapshot` to get the accessibility tree with element uids.
3. `click` the accordion / toggle / option that reveals the value.
4. `take_snapshot` again (or `take_screenshot` when layout carries meaning).
5. Record the value **with the date you read it** and the exact interaction —
   "clicked *6 tháng*, read column 2" — so the next person can reproduce it.

**Navigation findings are cited differently.** They have no corpus file, so cite
them as `[NAV: <url> · read YYYY-MM-DD · <interaction>]`. Never dress a
navigation finding as a crawl citation; the next re-crawl will not reproduce it
and the mismatch will read as corruption.

---

## 4. Citation discipline (the rule the whole skill rests on)

- Every factual claim in a reference carries a `[S#]` / `[T#]` / `[NAV]` key
  resolving to a **Sources** table with **file path · URL · fetch date**.
- The corpus file path must appear **literally** in the digest — that string is
  what `staleness_check.py` greps to tell you which digests a changed page
  invalidates. Prose-only citations silently break the tooling.
- **A claim you cannot ground, you do not make.** Say "not in the corpus" and
  offer to re-crawl. This is the honesty corollary of the grounding gate
  (`../../core/references/grounding-gate.md`).
- Mark evidence class honestly: documentation `[S#]` ≠ live test `[T#]` ≠ browser
  reading `[NAV]` ≠ third-party blog. A BSP's blog post is **not** a primary
  source, however confident it sounds.
- When two primary pages disagree, **say so and pick with a reason** — do not
  silently choose. (Live example: the interaction list in
  `messaging-and-cost.md` §2.)

---

## 5. After a round, record it

Append to `EVOLUTION.md`: date, what was crawled, what moved, which digests
changed, and — most valuable — **which previously-held belief turned out wrong**.
The corrections are the highest-value output of a re-research round; they are
what stops the same wrong number going into a second proposal.
