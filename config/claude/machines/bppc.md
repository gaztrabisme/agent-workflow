## This machine: bppc (Windows)

The GPU workstation itself, booted into Windows 11 Pro: 32 cores, 128 GB RAM, NVIDIA RTX 5080 16 GB, user `bppc`. You are on it, so no SSH. The Linux setup the Mac's notes describe (containers, `start-llm`, `~/projects/`) has not been checked from Windows; do not assume it is reachable here.

| Item | Value |
|------|-------|
| agent-workflow | `~/Documents/Work/tools/agent-workflow` (also `~/.agent-workflow`) |
| knowledge-base | `~/knowledge-base`; Qdrant on `127.0.0.1:6333`. Update with `KB_QDRANT_VERSION=1.19.2`: Qdrant 1.18.x cannot restore the snapshots on Windows |
| subagent | `~/Documents/Work/tools/claude-subagent-delegation`, branch `windows-compat`; config `~/.config/subagent/config.toml` (Codex only) |
| Codex CLI | not on PATH; the Codex app's copy under `%LOCALAPPDATA%\OpenAI\Codex\bin\<hash>\codex.exe`, and the hash folder changes when the app updates |
| uv | `~/.local/bin` |

- **Git Bash cannot start subprocesses inside the Claude desktop app** (fork fails with `0xC0000142`), so the Bash tool and `.sh` scripts fail here. Use PowerShell. `install.sh` has no Windows port in the repo yet.
- **The subagent guard reads shell commands with bash rules,** so Windows paths with `\` in a worker's shell command are not checked reliably. Point delegations at a scratch folder or worktree.
- Files the desktop app writes under `%LOCALAPPDATA%\Temp\claude\...` may be invisible to PowerShell (packaged-app file redirection). Put scratch scripts in the session folder instead.
