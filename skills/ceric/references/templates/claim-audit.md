# Claim audit — <target artifact>

**Audit depth:** abstract | hunt | full · **Target:** `<alias=path>` · **Sources:** `<alias=path>, …` · **Reviewer:** <who> · **Review approach:** single | pair (<readers and resolution>) | DEFERRED (<reason>) (derived: dogfood 2026-10-01)

## 1. Six-field hunt of the target artifact

| Element | What the artifact says or omits | Source | Where | Why it matters |
|---|---|---|---|---|
| Claim | <main position> | target | § Executive summary | <scope> |
| Evidence | <evidence presented> | target | L12-L18 | <support stated> |
| Reasoning | <link from evidence to claim> | target | § Findings | <inference> |
| Context | <setting, population, conditions> | target | § Methods | <bounds> |
| Implications | <recommended action or consequence> | target | § Recommendation | <effect> |
| Missing | <important material absent> | target | <locator or not present> | <why it matters> |

## 2. Claim audit

Use one row per material claim within the declared depth. Copy one exact claim quote from
the target into each row, then link its support rows below by Claim ID. The checker
verifies these rows against the `target` source alias. (derived: dogfood 2026-10-01)

| Claim ID | Claim quote | Source | Where | Type | Reasoning stated in target | Hedge in target | Required validity checks | Verdict | Attribution | Hedge check | Defect or reason still open |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | “<claim text>” | target | § Summary | frequency | <evidence-to-claim step> | <may/likely/etc.> | construct; external; statistical | supported | correct | preserved | — |

## 3. Evidence checks

Put one exact source quote in each Quote cell. Each row names the source alias and its
page, line range, or section locator; add rows when a claim relies on several sources.

| Claim ID | Source | Quote | Where | How this bears on the claim | Evidence quality / limits |
|---|---|---|---|---|---|
| C01 | evidence-source | “<exact words>” | p4 | <what the passage supports> | <sample, version, uncertainty, etc.> |

## 4. Corpus and roll-up

| Source alias | File | Available? | Hunt result / missing material |
|---|---|---|---|
| target | <path> | yes | <sections checked> |
| evidence-source | <path or cited name> | no | <claims left open because source is absent> |

**Verdict counts:** supported <n> · evidence only <n> · assertion <n> · overstated <n> · open <n>.
**Attribution defects:** misattributed <n> · unavailable <n> · unclear <n>.
**Hedge changes:** weakened <n> · strengthened <n> · not assessable <n>.

The four adjudicated verdict labels remain `supported`, `evidence only`, `assertion`, and
`overstated`. `Open` means the evidence cannot yet be adjudicated because a material
source is missing or a check is incomplete; it is not a fifth verdict. Attribution and
hedge fields are independent defect counts and do not replace the verdict. (derived:
dogfood 2026-10-01)

For `Attribution`, use `correct`, `misattributed`, `unavailable`, or `unclear`. For
`Hedge check`, use `preserved`, `weakened`, `strengthened`, or `not assessable`. (derived:
dogfood 2026-10-01)
