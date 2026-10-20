## This machine: mcbob (Mac)

knowledge-base repo: `~/Documents/Work/tools/knowledge-base`.

## GPU workstation (bppc)

A Linux PC on the home network: 32 cores, 128 GB RAM, NVIDIA RTX 5080 16 GB, user `bppc`, projects in `~/projects/`. It does training, container inference and the daily local LLM.

**Read `~/.claude/reference/bppc.md` before any SSH, Docker, training, file-transfer or remote-LLM work on it.** It holds the machine facts, the container launch patterns and the known failure patterns. Do not restate them here.

Rules that apply before that file is open:

- Connect LAN first, Tailscale second, and never gate the attempt on this Mac's subnet:
  ```bash
  for H in 192.168.1.17 100.106.185.34; do
    ssh -o ConnectTimeout=3 -o BatchMode=yes bppc@$H "echo ok" 2>/dev/null && { BPPC=$H; break; }
  done
  ```
- The LAN address is DHCP and has moved before. The Tailscale address `100.106.185.34` is the stable one. If the LAN address stops answering, `tailscale status` reports the current one.
- If both fail, Tailscale is probably down. It needs `sudo` and may need browser login, so Huy brings it up: ask him to run `! sudo tailscale up`, show him any login URL it prints, and do not open that URL yourself.
- bppc dual-boots Windows 11 from the same disk. When Windows is up, the Linux address answers with a different host key and the loop above fails; connect with `ssh bppc-win` (alias in `~/.ssh/config`: `bppc@192.168.1.17`, this Mac's `id_ed25519`, its own known_hosts entry). The shell is cmd. SSH there is LAN only (firewall: Private profile, no Tailscale on Windows). After a BIOS reset it boots Windows; Huy sets Boot Option #1 back to ubuntu.
- Daily local LLM on the PC: `start-llm` from this Mac (LAN first, Tailscale second, never runs sudo). Serves `http://<bppc>:8080/v1`; the API key is required and is in `~/.config/bppc-llm/api_key` (details in `~/.claude/reference/bppc.md`).

## Local LLM on this Mac (oMLX)

This Mac (mcbob, M3 Max, 96 GB) runs oMLX, an OpenAI-compatible MLX server. Use it for local LLM tasks (drafting, classification, extraction, summarisation, codegen, embeddings, batch jobs) with no dependency on the PC or the network.

The `omlx` skill (`~/.claude/skills/omlx/`) is the source of truth for how to use it. Do not re-document oMLX here. This file carries only the machine-specific values the skill leaves out:

| Item | Value |
|------|-------|
| Endpoint | `http://127.0.0.1:8000/v1` |
| API key | read it from `auth.api_key` in `~/.omlx/settings.json` and send it as `Authorization: Bearer <key>`; the skill's scripts read it there |
| Base path | `~/.omlx` (models, logs, cache, `settings.json`, `model_settings.json`) |
| LAN alias | `McBob.local:8000` |
| App / CLI | `oMLX.app` · `~/.omlx/bin/omlx` |

- **Probe before any substantial run:** `~/.claude/skills/omlx/scripts/omlx_probe.sh --model <id> --canary --deep`. If one line must stand in for it, call `/api/status` and read `models_loaded`. Never use `/v1/models`: it returns 200 with every model listed while none is loaded, so it passes a cold load of tens of GB as a warm call.
- **Keep memory pressure green (Huy, 2026-10-01).** Before and during any run on this Mac, read `memory_pressure` (system-wide free percentage) and `sysctl vm.swapusage`; evict idle oMLX models, keep one Metal job at a time and at or under 60 GB in-process, cap child processes, and report the pressure in every status line. When a run alone cannot stay green, say what else is using the memory rather than silently pushing on.
- **Check for another GPU tenant before loading a model on this Mac.** Any run that puts a model on the Mac's GPU (embedder, reranker, MLX, a test suite that loads one) first checks `ps` for training or MLX processes of other sessions and oMLX's `/api/status`. If another tenant holds the GPU, run on the CPU or ask that session first. Two MPS evals once killed another session's training run this way. A tenant is a process holding a model on the GPU, not a process whose name matches. An idle oMLX with 0 models loaded and Python MCP servers are not tenants; a guard script that flags them blocks every booked check (pi-mind lost its 2026-10-17 07:31 slot this way).
- **Never send generation parameters to oMLX.** No `temperature`, `top_p`, `top_k`, `min_p`, penalties, `seed`, `max_tokens`, `chat_template_kwargs.enable_thinking` or `thinking_budget` in any request, from any script, harness or SDK call (including `extra_body`). The server owns them: per model in `~/.omlx/model_settings.json`, globally in the `sampling` block of `~/.omlx/settings.json`. Read those files to know what a call runs with; if a run needs different values, change the server settings, not the request. Agentic models reason: do not turn thinking off to save tokens or time.
- **`response_format` without `type: "json_schema"` is silently unenforced.** No error, the model just talks. Send `type` and `name` whenever structured output is needed.

If oMLX cannot serve an architecture: `mlx_lm.server` / `mlx_lm.generate` (miniconda), or LM Studio with the `lms` CLI.

## Working on this Mac

- **No `timeout` command.** macOS has no `timeout(1)`; a command using it fails with `command not found: timeout`. Use the Bash tool's own timeout, or `perl -e 'alarm shift; exec @ARGV' <seconds> <command>`. `subagent doctor --prompt --json` takes over 3 minutes when cloud lanes are down and exits 1 if any lane is down, so read the JSON for the lane you need, not the exit code.
- **Scheduled jobs (launchd) cannot read `~/Documents`.** A launch agent that points at a script there fails with "Operation not permitted". Keep the source in the repo, install a copy outside Documents (for example `~/.bob-sentry/`), and point the plist at the copy. After loading a job, wait for its first run and read its error log before saying it works.
- **Closed-lid sleep kills overnight runs.** On 2026-10-15 the Mac slept at 05:11 during a gpt-oss judging run. When it woke, Metal reported a GPU timeout (`kIOGPUCommandBufferCallbackErrorTimeout`) and the runner stopped. Start any run longer than an hour as `caffeinate -i -s <script>` (or `caffeinate -i -s -w <pid>` for a run already going), and confirm with `pmset -g assertions | grep caffeinate`. To see whether the Mac slept, check `pmset -g log | grep -E " Sleep | Wake "`. Whether caffeinate holds with the lid closed and no external display was not verified.
- **Model downloads:** run `snapshot_download(repo, local_dir="/Volumes/Bobbie/omlx/models/<org>/<name>")` with `~/miniconda3/bin/python -I <script>`; the ieltsy `.venv` has no `huggingface_hub`. Run it with `run_in_background: true`; a 59 GB download took about 40 minutes. oMLX's model folder is on the external drive Bobbie: when `/Volumes/Bobbie` is not mounted, oMLX has no models and downloads have nowhere to go.
- **`~/.claude/CLAUDE.md`, `machine.md`, `standing-corrections.md`, `character-changelog.md` and `skills/*` are symlinks into `~/Documents/Work/tools/agent-workflow`** (`reference/` is not). Edit refuses to write through a link: run `readlink <file>` first and edit the target. Commit in agent-workflow, not in `~/.claude`.
- **The dcg command guard scans the whole Bash command text, heredoc bodies included.** Prose containing words such as "restore" or "delete" inside `cat > file <<EOF` gets the command blocked. Write documents with the Write tool; keep Bash for short commands.
- **Checking a local HTML page (a dashboard, a generated report) in the browser pane.** `browser_navigate` to a `file://` URL opens a static snapshot, and screenshot and JavaScript tools fail on it. Serve the folder instead: `python3 -m http.server <port> --bind 127.0.0.1` with `run_in_background: true`, then `mcp__Claude_Browser__preview_start` on `http://127.0.0.1:<port>/…`. Stop it with `pkill -f "http.server <port>"` when done. Huy opens the final page from disk with `open <path>`, so the file must not need the server.

## Starting another Claude session from a session

`mcp__ccd_session__start_session` returns "Starting sessions is not enabled here". Instead:

1. `cd <dir> && SID=$(uuidgen | tr A-Z a-z); nohup claude -p "<prompt>" --name <Name> --session-id $SID --permission-mode bypassPermissions --output-format stream-json --verbose > .run.jsonl &`. A `-p` run is one turn and does not receive messages from other sessions.
2. For a session that stays reachable: `tmux new-session -d -s <name> -c <dir> "claude --resume $SID --name <Name> --permission-mode bypassPermissions --remote-control <Name>"`, then `tmux send-keys -t <name> Down Enter` to accept the folder-trust prompt.
3. Use the same permission mode as the sessions it must talk to. When modes differ, the receiving session holds cross-session messages for approval, and a Desktop session cannot ask, so they expire undelivered.

It stops when the Mac sleeps or restarts. Check it with ListAgents. If the Desktop app reopens the same session, close the tmux copy so only one answers.

After a Mac restart the Desktop app reopens its own sessions within seconds. Run ListAgents before any `tmux new-session ... --resume`, and resume in tmux only the sessions that are missing. If two rows carry the same name, the one marked "Claude Desktop session" is the one Huy types into; message it by its ref (for example "IELTSy repo sync [b67925]") and `/exit` the tmux copy.

## Resume

Huy's current resume, its master fact file and the rules for editing them: `~/.claude/reference/resume.md`. Read it before writing any CV, LinkedIn or Upwork text.
