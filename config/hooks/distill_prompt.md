You are reviewing one Claude Code session, just before its context was compacted. The condensed transcript is at {TRANSCRIPT}. It covers the part of the session since the previous compaction. The session ran in {CWD}. Read it in full with the Read tool (use offset and limit; it may be long).

Your job: find lessons this session teaches that would make future sessions better, and say exactly where each one should be written down. You only propose. You change no file.

## What counts as a lesson

Look for these, in this order:

1. **Corrections by Huy.** He said something was wrong, unclear, or not what he asked for. Quote him.
2. **Tool failures.** A tool call failed, was blocked, timed out, or returned something wrong: an MCP tool, a hook, a script, a CLI, a permission rule. Note whether the session found a workaround.
3. **Workarounds the session invented.** Something it had to figure out that the next session will have to figure out again (a path, a flag, a gotcha on a machine).
4. **Wrong assumptions.** The session stated something as fact and later found it false.
5. **Approaches that worked** and are not yet written anywhere, only if they will clearly recur.

Not lessons: one-off facts about a task, things already written in the target file (check with Read or Grep before proposing), routine work that went fine, and anything only one session will ever need.

## Where lessons go

Name one exact target file for each lesson, and check it exists (Glob or Read). Candidates:

- a skill: `~/.claude/skills/<skill>/SKILL.md` or a file in its `references/`;
- global rules: `~/.claude/CLAUDE.md` (only for rules that hold in every project);
- Huy's corrections log: `~/.claude/standing-corrections.md` (before-and-after pairs, its own line format: `DATE · SURFACE · BEFORE -> AFTER · RULE`);
- a machine note: `~/.claude/machine.md`, `~/.claude/reference/*.md`;
- a hook or its config: `~/Documents/Work/tools/agent-workflow/config/hooks/*`, or a tool's own config (for example the dcg command guard);
- an MCP server's code or config, a script, or a project's `CLAUDE.md` or wiki;
- the project the session ran in ({CWD}): its `CLAUDE.md`, `AGENTS.md` or notes.

The Character section of `~/.claude/CLAUDE.md` changes only through Huy with a changelog entry; if a lesson belongs there, say so and propose nothing more specific.

## Output

If there is nothing worth keeping, output exactly one line and nothing else:

NOTHING TO LEARN

Otherwise output one block per lesson, at most 7, most useful first, in this form and plain words (the reader is Huy, who did not see the session):

### <one-line lesson, a full sentence>
- **Kind:** correction | tool failure | workaround | wrong assumption | worked well
- **Evidence:** a short quote from the transcript, with its rough position (for example "near line 4200")
- **Target:** <exact file path>
- **Change:** the exact text to add or replace, ready to paste; for code or config, the diff
- **Why there:** one sentence

Output nothing before the first block and nothing after the last.
