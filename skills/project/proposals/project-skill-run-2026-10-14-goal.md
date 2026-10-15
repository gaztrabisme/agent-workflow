# Goal: build the `project` skill and its first three specialist skills (2026-10-14)

Status: approved by the owner 14 Oct 2026 ("Final confirmation" on `project-skill-2026-10-14.md`, decisions 1 to 5; conductor dropped entirely; `SKILL.md` an introduction and index, all instructions in smaller modules; gap skills built from this engagement's material and the knowledge base).

| ID | Criterion | Evidence | Check |
|---|---|---|---|
| G1 | `project/SKILL.md` is an introduction and index only; every instruction lives in a module under `references/` | `project/SKILL.md` | Read it: no rule text beyond one-line pointers; under 120 lines |
| G2 | No rule from the old project-management or conductor `SKILL.md` is lost | mapping table from the refactor agent | Spot-check 10 rows against the old text in git (`5c8e304`) |
| G3 | No skill named `conductor` remains; live links in other skills resolve | `grep`, `check_refs.py` | `check_refs.py project --no-anchor-check` reports no problem except the known `grounded.md` output-name false alarm; grep finds no `../conductor/` or `../project-management/` outside dated records |
| G4 | Roles module: who holds each role set per project; the two rules (outside acceptance; producer never approves) | `references/roles.md` | Read |
| G5 | Running agents written in PRINCE2 terms, with the approach declaration | `references/run/flow.md` | Read |
| G6 | Review and audience module; checklist stress-test module with a how-to-check, failure and broken example for all 17 lines | `references/review-and-audience.md`, `references/checklist-uat.md` | Count 17 rows; read 3 |
| G7 | Checklist stress test run blind: one agent seeds defects, a fresh agent who has not seen the answer key finds them | run note | Detection per line recorded; lines that failed are rewritten or marked |
| G8 | Speaker-script pass in `presentation`; run on the PoC deck as an internal script, with a repetition list | `presentation` method file; `Documents/pwc/docs/` script note | Read the repetition list; the deck file unchanged (hash) |
| G9 | Three specialist skills (`infrastructure`, `data-engineering`, `testing`), each cited to knowledge-base books, tested on this engagement's material, with project names only in their `EVOLUTION.md` | three skill folders | `check_refs.py` per skill; grep rule text for client names; read each test record |
| G10 | Nothing in the presale workspace edited except the new script note; nothing pushed | mtime check, `git status` | Run |
