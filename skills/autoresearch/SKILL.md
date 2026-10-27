---
name: autoresearch
description: "Run an autonomous experiment loop through the autoresearch MCP server: a fresh agent proposes one change per iteration, the server trains and scores it in a sandbox the agent cannot read, and keeps only gains above the measured noise. USE WHEN a target has one number to improve and a command that measures it (model training loss, prompt eval score, benchmark time, test-suite runtime) and many small trials could find gains unattended. Not `applied-ml-problem-solver` (chooses the ML approach and metric), not `dev` (writes features), not `testing` (designs test strategy). Keywords: autoresearch, experiment loop, hill climb, overnight, keep or discard, noise floor, MAD, val_bpb, benchmark, prompt tuning, sandbox, held-out."
license: MIT
---

# Autoresearch

The loop produces three things: a session branch with one commit per kept change, `log.jsonl` with every trial, and `report.md` with the held-out score. Quote the held-out score, not the training or validation score, when you report a gain.

## Before starting

- Make the target a git repo. Each iteration runs in its own worktree.
- Write `train_cmd`. It runs in the iteration worktree under the sandbox. It reads `AUTORESEARCH_DATA`, `AUTORESEARCH_STEPS` and `AUTORESEARCH_SEED`. It may write only to `AUTORESEARCH_OUT` and its own `TMPDIR`; it cannot write the worktree.
- Write `eval_cmd`. The server runs it outside the sandbox. It reads `AUTORESEARCH_ARTIFACT` and prints one line per metric: `METRIC <name>=<value>`.
- If eval must run candidate code (for example to load a model the candidate defined), run that code in a child process sandboxed with deny on the session folder, send it inputs over a pipe, and compute the metric in the trusted parent. The server passes a private copy of the artifacts in `AUTORESEARCH_ARTIFACT` (under `~/.cache/autoresearch-snap/` by default); links and special files in the artifacts make the run crash.
- Put validation and held-out data and the eval script in `~/.autoresearch/<session>/`. The proposer cannot read that folder.
- Keep validation and held-out data only inside the session folder; a copy elsewhere is readable by the proposer.
- Put training data in `~/.cache/autoresearch-wt/<session>/data/`.
- Budget runs by steps (`AUTORESEARCH_STEPS`). Never budget by wall-clock time.
- Set `scope` to the files the proposer may edit. Every other file is off limits.
- Set `min_gain` to the smallest gain worth keeping.
- Pre-register the stop condition before the baseline: `max_iter` and a time cap. Write both into the session folder.

## Running

Call the MCP tools in this order:

1. `init`: creates the session branch and folders.
2. `baseline`: runs the unchanged target 5 times with different seeds.
3. `run` (background loop until the stop condition) or `iterate` (one step).
4. `status`: progress and current best.
5. `stop`: ends the loop. The session branch stays.
6. `finalize`: writes `report.md`.

For an overnight run, start the CLI under caffeinate so the Mac does not sleep: `caffeinate -i -s autoresearch run <session> --max-iter N`.

Before and during the run, follow the memory pressure rules in `~/.claude/machine.md`. Before the first iteration, check that the codex lane is open: `subagent doctor --prompt --json`.

## Keep rule

- The baseline is 5 runs. Record their median and MAD (median absolute deviation, the typical spread around the median).
- A change is kept only if its gain beats the larger of 2 x MAD and `min_gain`.
- A kept change must also pass confirmation: 3 more fresh-seed runs. The median of the confirmation runs alone (not the screening run) must beat the best by the threshold.
- Re-measure the noise after every keep.
- A run slower than 2 x the best's median time is a timeout. Count it as inconclusive, not as a loss.
- Reject any edit outside `scope`.
- Stop at a plateau: 10 consecutive non-keeps.

## Proposers

- Set `provider` to a subagent-mcp lane name (the example config uses `codex`) or to `claude-cli:<model>`, which runs the local `claude` CLI.
- Set `fallback_provider` (for example `claude-cli:haiku`) to retry the iteration once on that provider when the primary fails, is cancelled, times out, or raises during startup. A proposal that makes no change does not trigger the fallback.
- Set `proposer_timeout_s` (600 seconds by default). For the Claude CLI it bounds the whole proposal. For a subagent lane it bounds only the wait for the agent to become ready.
- A subagent lane gets a fresh child for each proposal. Every proposer is denied reads of the session folder and the snapshot root.
- It reads `state.md` and the list of tried ideas, makes one change, and ends its reply with `IDEA: <one line>`.
- It cannot call MCP servers.

## Limits

- The sandbox is macOS only (`sandbox-exec`).
- v1 runs one session at a time and one line of attack. Do not run parallel idea families.
- The PC (bppc) is not supported yet. Run on this Mac.
- The proposer can still read anything outside the session folder. Keep held-out answers and secrets inside the session folder.
- Training and evaluation together count as one run. If they take longer than `timeout_factor` (2.0 in the example config) times the current best's median wall time, the run is a timeout. A candidate that is legitimately slower per step (larger batch, deeper model) can be lost this way; raise `timeout_factor` when such changes are in scope.
- Cloud models' content filters may refuse prompts that read like data exfiltration; this does not affect normal proposals.

## After the run

- Read `report.md` and the held-out score before you claim a gain.
- Record the result in the project wiki's `decisions.md`.
- Add each rejected direction to the wiki's `Rejected Approaches`, with the reason it failed.
