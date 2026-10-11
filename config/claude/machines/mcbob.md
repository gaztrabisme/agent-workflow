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
- **Check for another GPU tenant before loading a model on this Mac.** Any run that puts a model on the Mac's GPU (embedder, reranker, MLX, a test suite that loads one) first checks `ps` for training or MLX processes of other sessions and oMLX's `/api/status`. If another tenant holds the GPU, run on the CPU or ask that session first. Two MPS evals once killed another session's training run this way.
- **Never send generation parameters to oMLX.** No `temperature`, `top_p`, `top_k`, `min_p`, penalties, `seed`, `max_tokens`, `chat_template_kwargs.enable_thinking` or `thinking_budget` in any request, from any script, harness or SDK call (including `extra_body`). The server owns them: per model in `~/.omlx/model_settings.json`, globally in the `sampling` block of `~/.omlx/settings.json`. Read those files to know what a call runs with; if a run needs different values, change the server settings, not the request. Agentic models reason: do not turn thinking off to save tokens or time.
- **`response_format` without `type: "json_schema"` is silently unenforced.** No error, the model just talks. Send `type` and `name` whenever structured output is needed.

If oMLX cannot serve an architecture: `mlx_lm.server` / `mlx_lm.generate` (miniconda), or LM Studio with the `lms` CLI.
