# Goal — 2026-10-10 — reward-design skill

**Status:** APPROVED (owner "go", 2026-10-10)

**Decision owner / author:** Huy, 2026-10-10. **Audited by:** coordinator (Claude) at Close. **Contact:** Huy.

Run ID: `2026-10-10-reward-skill`. Run folder: `~/Documents/Work/lab/reward-skill-run/`.

## Deliverable — skills/reward-design/

| ID | Source | Success criterion | Artifact | UAT |
|---|---|---|---|---|
| G1 | owner request | Five research units each produce a findings file in the shared schema with a source link on every entry | `run/{A..E}/findings.md` | `bash check-all-findings.sh` exits 0 |
| G2 | Plan Block CHECK | An independent Codex session checked every claim the skill relies on; each has a verdict (supported / weakened / unsupported) | `run/V/claims-verified.md` | `bash check-verified.sh` exits 0 |
| G3 | AGENTS.md add-a-skill | Skill folder, frontmatter `name: reward-design`, line in `skills.txt`, linked by install | `skills/reward-design/SKILL.md`, `skills.txt` | `bash ~/Documents/Work/lab/reward-skill-run/check-skill.sh` exits 0 |
| G4 | Intent Q1 | Every technique in the skill carries an evidence tier; no claim marked unsupported in V appears without its caveat | `skills/reward-design/references/*` | `check-skill.sh` tier + unsupported-claim scan |
| G5 | Intent Q2 | A dark-patterns section exists and none is recommended | `skills/reward-design/` | `check-skill.sh` greps the section |
| G6 | Intent Q4 | Ranked reading list with rigour label and buy-first/later per book | `skills/reward-design/references/reading-list.md` | `check-skill.sh` column check |
| G7 | skill-builder | `EVOLUTION.md` with a PENDING entry; one trial critique on a real piece recorded | `skills/reward-design/EVOLUTION.md`, `run/T/critique.md` | `check-skill.sh` + file exists |
| G8 | Intent Q3 | Sibling skills presentation, motion, visual-design, information-design, ux each carry a one-line pointer | those SKILL.md files | `grep -l reward-design skills/{presentation,motion,visual-design,information-design,ux}/SKILL.md` lists 5 files |

## Working pattern (binds this run)
Owner: "You orchestrate Codex only." Every unit runs on Codex (`gpt-6.1-sol`, xhigh) via direct `codex exec` with live web search. Fallback: Codex resume; if Codex refuses, unit is blocked and reported. glm, deepseek, omlx closed today.

## Close audit (2026-10-11)
G1 PASS · G2 PASS · G3 PASS · G4 PASS · G5 PASS · G6 PASS · G7 PASS (trial critique recorded; its verdict on the skill was FAIL, fixed in Unit F) · G8 PASS.

## Amendments
2026-10-10 owner, at go: "You orchestrate Codex only." (Plan had Claude research agents; replaced by Codex.)

## Branch resolutions (before dispatch)
- F1 trial piece: owner named none → coordinator picks an existing deck/video artifact inside the repo.
- F2 reading list page: default yes.

## Goal block
Execute plan "reward-design skill" (wiki/goals/2026-10-10-reward-design-skill.md). Goal rows:
1 G1: `bash /Users/GaryT/Documents/Work/lab/reward-skill-run/check-all-findings.sh`
2 G2: `bash /Users/GaryT/Documents/Work/lab/reward-skill-run/check-verified.sh`
3 G3-G7: `bash /Users/GaryT/Documents/Work/lab/reward-skill-run/check-skill.sh`
4 G8: `bash /Users/GaryT/Documents/Work/lab/reward-skill-run/check-pointers.sh`
