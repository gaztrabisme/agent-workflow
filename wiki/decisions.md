# Decisions

| Date | Decision | Rejected |
|---|---|---|
| 2026-10-03 | One private repo for the 28 skills and three tools, each skill keeping its history | Staying as 28 separate repos; a fresh start without history |
| 2026-10-03 | Course images and PDFs in Git LFS across all history | Plain git (slow to clone, near GitHub's size advice); release downloads (separate fetch step, no history) |
| 2026-10-03 | Knowledge base stays its own repo and server; data ships as release `data-v10` | Packaging it with the skills; putting data in git |
| 2026-10-03 | Anthropic's skills (`docx`, `xlsx`), all MCP servers and API keys stay out | Packaging them |
| 2026-10-03 | Dropped the read-once and post-compaction-reminder hooks (rarely triggered; Claude Code reloads CLAUDE.md itself); kept dcg and the code-quality hook | Keeping all four |
| 2026-10-03 | `bppc.md`, Codex and Gemini instruction files not packaged | Packaging them |
| 2026-10-03 | plan-goal plugin stays its own repo, cloned by the installer | Moving it into this repo |
| 2026-10-03 | Old per-skill repos archived (reversible); deletion left to the owner | Deleting them |
| 2026-10-03 | Skills reach tools through `~/.agent-workflow`, a link the installer makes | Hard-coded Mac paths |
| 2026-10-11 | New skill `reward-design`: plans and critiques anticipation, surprise and payoff; "dopamine" is a trigger keyword only, every technique carries an evidence tier, dark patterns are taught for recognition and never recommended; rendering stays with presentation, motion, visual-design, color-theory, information-design, ux, frontend | A literal "release dopamine" skill (overclaims); folding the material into the existing design skills (no single owner for sound and reward timing) |
