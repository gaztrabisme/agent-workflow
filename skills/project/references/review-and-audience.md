# Review and audience

Who each artifact is for, how it is checked as the reader will see it, and who checks it. The checks a workbook or plan must pass before issue are in [the issue checklist](issue-checklist.md); how each of those checks is itself tested is in [the checklist test](checklist-uat.md).

## Reader declaration

Before writing an artifact, write down its reader. There are four:

| Reader | Who | What the copy carries |
|---|---|---|
| Internal | Our own notes and working files | Anything: tags, file names, decision IDs, man-days, rates, margin |
| Team | Colleagues who own other lanes | Short one-line points in the team's language; suggest and ask, do not defend earlier work |
| Client | The buyer and its reviewers | Scope, what it does, and the price on the cost page |
| Funder | Whoever pays or sponsors, if not the client | As for the client |

Client and funder copies carry no internal tags, no working-file names, no people's names used as labels, and no man-days, rates or margins unless the owner chose to show them. Cite a source by its own document title. [core artifact writing](../../core/references/artifact-writing.md#client-facing-pages) sets the rest for a client page:

- State an exclusion or caveat once, on the scope or out-of-scope page.
- Do not attribute a cut to the client.
- Do not state the client's or funder's budget limit.
- Do not headline a price outside the cost page.

The declared reader becomes a success criterion of the artifact, with its own reviewer (below). An artifact that serves two readers is written as two copies, each for its own reader.

## Rendered checks

Check every artifact as it will be seen. "Export succeeded" is not a check; a clean tool exit says the file was written, not that it reads correctly.

| Artifact | Check | Owning skill |
|---|---|---|
| Deck | Render every slide to an image and read each one | [presentation render and check](../../presentation/references/method/render-and-check.md) |
| Workbook | Recalculate, then read the values back and look at each sheet | [xlsx](../../xlsx/SKILL.md) (recalculate and verify steps) |
| Diagram | Run `check_diagram.py`, then export and read the PNG | [drawio checker](../../drawio/scripts/check_diagram.py), [drawio verification loop](../../drawio/references/quality-conventions.md) |
| Web page | Render it in a browser at its target sizes and read it | [frontend](../../frontend/SKILL.md) |

## Independent reviewer

The reviewer is an agent that did not produce the artifact. Brief it with the artifact, its declared reader and its quality criteria, not with the drafting conversation. Ask it to read the artifact as that reader. For a client or funder copy, ask: would the client read any sentence as blame, an upsell, an internal caveat, or a figure they did not ask to see? A reviewer with the drafter's context reads what the drafter meant, not what the page says. PRINCE2 requires the person who chairs a quality review to be independent of the product. [book:prince2-managing-successful-projects], 8.4. Technique: recommended quality review technique

## Deck speaker script

Before a deck is shown, walk it in order with an internal speaker script and have a second agent mark every repeat: [speaker-script pass](../../presentation/references/method/speaker-script-pass.md).
