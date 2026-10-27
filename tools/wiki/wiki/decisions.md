# Decisions

Owner: repository owner. Reviewed: 2026-10-27.

## 2026-10-27 — shared core

Context: CLI and MCP must agree on findings and mutations.
Decision: use standard-library functions in one core module, thin argparse and
FastMCP wrappers, and structured dictionary results. Preserve whole dated entries.
Resolve links against the source page first and the wiki's parent second.

Grounded: supplied wiki protocol → index summaries, append-only events and living state.
Grounded: knowledge-base server.py lines 1–60 → lazy function imports and FastMCP instance.
Books: none relevant to this mechanical build; no book research performed.
Official FastMCP web lookup was blocked by the command review hook; verify the installed API directly.

## Rejected approaches

- Separate CLI/MCP implementations: would duplicate rules and risk different behavior.
- Root-only or page-only link checks: both reject valid links in the supplied corpus.
- Line-based rotation: can split entries and detach subheadings.

## Assumptions and constraints

- Date order is inferred from first and last dated entries; ties default newest-first.
- Dates in ranges use the first ISO date. Non-dated headings stay in their containing entry.
- Lint is read-only. Mutating acceptance runs use only synthetic wikis.
- Expected review weaknesses: ambiguous Markdown syntax, archive ordering, branch-file data preservation.

## 2026-10-27 — acceptance mismatch

Context: the supplied corpus has 238 Markdown pages, including archived source
copies in `recruitment-strategy-2026-10-11/inputs/`. All 135 broken links found
are in those copies; zero occur in other pages. The originals' relative link
bases were not preserved when copying.
Decision: retain the specified recursive “any page” rule and its two resolution
bases. Do not silently exclude copied inputs or add an unrequested resolution
base to force the ≤3 acceptance gate green. The first build reported FAIL
against that original criterion. This scope decision is superseded by the
owner-approved rule changes below.

Grounding and review limits: official web lookup, reviewer-agent launch, direct
uv corpus lint, and some environment install commands were rejected by automatic
approval review. The installed FastMCP 2.13.1 API was exercised in-memory.
Self-inspection and executable tests do not constitute independent review.

## 2026-10-27 — source copies and transitive reachability

Context: the owner confirmed the previous hash check/tests and decided two
changes from the Linkcruiser results.
Decision: pages below `inputs/` or `raw/` at any depth within the wiki are
immutable copies, exempt from broken-link, undated-page and unreachable.
Replace not-in-index with unreachable: follow Markdown links transitively from
index.md, using the existing page-relative-first and repo-root fallback.
Track visited files to terminate cycles. Links through exempt pages and linked
external Markdown may still reach maintained wiki pages.

Evidence: 65 passing uv pytest cases, Ruff PASS, exact uv corpus lint exit 0,
zero broken links, 31 unreachable pages, and unchanged hashes for all 284 files.
Rejected: retaining direct-index membership (would flag reachable topic pages)
or skipping source copies as graph nodes (would break otherwise valid paths).
