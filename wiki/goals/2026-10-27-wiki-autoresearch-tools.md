# Goal — 2026-10-27 — wiki tool, autoresearch server, wiki search

**Status:** APPROVED (owner approved the plan, 2026-10-27).

**Decision owner:** Huy. **Audited by:** the coordinator at Close, against this file only. **Plan:** `~/.claude/plans/1-ok-2-ok-fluttering-raven.md`.

Shorthand: A = `~/Documents/Work/tools/agent-workflow`; S = `~/Documents/Work/tools/mcp/subagent-mcp`; R = `~/Documents/Work/tools/mcp/autoresearch-mcp`; K = `~/Documents/Work/tools/knowledge-base`.

| ID | Source | Success criterion | Artifact | UAT |
|---|---|---|---|---|
| G1 | owner: wiki tool | Wiki tool tests pass | `A/tools/wiki` | `uv run pytest -q` exits 0 |
| G2 | measured wiki sizes | `wiki lint` finds Linkcruiser's oversize index and log and changes nothing | Linkcruiser wiki | lint output names index-over-cap and log-over-cap, ≤3 missing link targets; `git status --porcelain` same before and after |
| G3 | owner: limits as proposed | Protocol states the six new rules and stays short | `A/skills/core/references/wiki-protocol.md` | grep each rule; `wc -l` < 80 |
| G4 | owner: CLI and MCP | wiki-mcp registered for Claude Code, Codex, pi | configs | `claude mcp list`, `codex mcp list`, pi `mcp.json` |
| G5 | owner: lanes plus sandbox | A child's script cannot read a `deny_read` path | `S` branch `autoresearch-aware` | `uv run pytest -q`; smoke shows "Operation not permitted" on a Claude-driver lane; codex result logged |
| G6 | spike report §8 | Autoresearch core rejects score spoofing, protected reads, zero-noise keeps, timeouts, out-of-scope edits | `R` | `uv run pytest -q` with the named tests |
| G7 | owner: MCP all agents use | Loop runs through MCP tools and CLI | `R` | fake-proposer fixture: ≥1 keep, ≥1 discard; live smoke 2 iterations, denials counted |
| G8 | owner: skill not ML-only | Skill installed; ML page points to it | `A/skills/autoresearch` | `grep -x autoresearch skills.txt`; link check empty; `train-loop.md` links it |
| G9 | owner: GPU approved | Real run on the Mac GPU; planted scorer reads fail | session store | 8 iteration rows; both planted reads failed; finalize report and held-out score; memory green |
| G10 | coordinator | Independent review of S and R changes resolved | `R/wiki/log.md` | every finding fixed or logged |
| G11 | owner: search on KB | Wiki search finds the right page and re-indexes incrementally | `K` branch `wiki-corpus` | `uv run pytest -q`; 3 queries top-3; second pass 0 re-embeds |
| G12 | coordinator | Independent review of K change resolved | `K/wiki/log.md` | every finding fixed or logged |

## Working pattern
Coordinator writes briefs and runs every UAT. Codex (subagent lane) builds multi-file code and reviews; Haiku subagents do mechanical text edits. Nothing pushed.

## Amendments
(none)
