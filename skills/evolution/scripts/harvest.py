#!/usr/bin/env python3
"""Stream session transcripts into compact, agent-readable evidence files.

Never loads a transcript into memory. Emits per-session:
  <sid>.turns.md   -- every user prompt verbatim + what the turn cost
  <sid>.tools.md   -- tool histogram, latency split, error/retry signatures
and a global summary.md. Stdlib only.
"""
import json, os, re, sys, collections, datetime as dt
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)

NOISE = re.compile(r"<(local-command-caveat|command-name|command-message|command-args|local-command-stdout|system-reminder)")

def ts(s):
    try: return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception: return None

def textof(content):
    if isinstance(content, str): return content
    out = []
    if isinstance(content, list):
        for b in content:
            if isinstance(b, dict) and b.get("type") == "text": out.append(b.get("text", ""))
    return "\n".join(out)

def human(sec):
    if sec is None: return "?"
    m, s = divmod(int(sec), 60); h, m = divmod(m, 60)
    return ("%dh%02dm" % (h, m)) if h else ("%dm%02ds" % (m, s))

summary = []
for f in sorted(ROOT.glob("*.jsonl"), key=lambda p: -p.stat().st_size):
    sid = f.stem
    turns = []          # (ts, text, promptSource)
    tools = collections.Counter()
    tool_err = collections.Counter()
    tool_ms = collections.Counter()   # summed latency per tool
    tool_n = collections.Counter()
    pending = {}        # tool_use_id -> (ts, name)
    bash_cmds = collections.Counter()
    asst_text_chars = 0; asst_text_blocks = 0
    thinking_chars = 0
    sidechain_msgs = 0
    first = last = None
    lines = 0
    big_results = []    # (chars, tool, snippet)
    file_writes = collections.Counter()
    with f.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            lines += 1
            try: d = json.loads(line)
            except Exception: continue
            t = ts(d.get("timestamp", "") or "")
            if t:
                first = first or t; last = t
            if d.get("isSidechain"): sidechain_msgs += 1
            typ = d.get("type")
            msg = d.get("message") or {}
            if typ == "user" and not d.get("isMeta"):
                c = msg.get("content")
                txt = textof(c) if not isinstance(c, str) else c
                # tool results
                if isinstance(c, list):
                    for b in c:
                        if isinstance(b, dict) and b.get("type") == "tool_result":
                            tid = b.get("tool_use_id")
                            st, nm = pending.pop(tid, (None, "?"))
                            if st and t:
                                tool_ms[nm] += (t - st).total_seconds(); tool_n[nm] += 1
                            if b.get("is_error"): tool_err[nm] += 1
                            body = b.get("content")
                            bs = textof(body) if not isinstance(body, str) else body
                            if bs and len(bs) > 20000:
                                big_results.append((len(bs), nm, bs[:120].replace("\n", " ")))
                if txt and not NOISE.match(txt.strip()) and not d.get("isSidechain"):
                    if txt.strip(): turns.append((t, txt.strip()))
            elif typ == "assistant":
                for b in (msg.get("content") or []):
                    if not isinstance(b, dict): continue
                    if b.get("type") == "text":
                        asst_text_chars += len(b.get("text", "")); asst_text_blocks += 1
                    elif b.get("type") == "thinking":
                        thinking_chars += len(b.get("thinking", ""))
                    elif b.get("type") == "tool_use":
                        nm = b.get("name", "?")
                        tools[nm] += 1
                        if t: pending[b.get("id")] = (t, nm)
                        inp = b.get("input") or {}
                        if nm in ("Bash", "PowerShell"):
                            cmd = (inp.get("command") or "")[:160].replace("\n", " ")
                            bash_cmds[cmd] += 1
                        if nm in ("Write", "Edit", "NotebookEdit"):
                            file_writes[str(inp.get("file_path", "?"))] += 1

    dur = (last - first).total_seconds() if first and last else None
    # per-turn cost
    tl = []
    for i, (t, txt) in enumerate(turns):
        nxt = turns[i + 1][0] if i + 1 < len(turns) else last
        gap = (nxt - t).total_seconds() if (t and nxt) else None
        tl.append((t, gap, txt))

    with (OUT / ("%s.turns.md" % sid)).open("w", encoding="utf-8") as o:
        o.write("# %s\n\n%s -> %s  (%s wall)  %d prompts  %d lines\n\n" %
                (sid, first, last, human(dur), len(turns), lines))
        for t, gap, txt in tl:
            o.write("\n## [%s] +%s\n\n```\n%s\n```\n" %
                    (t.strftime("%Y-%m-%d %H:%M") if t else "?", human(gap), txt[:4000]))

    with (OUT / ("%s.tools.md" % sid)).open("w", encoding="utf-8") as o:
        o.write("# %s tools\n\n" % sid)
        o.write("wall=%s  assistant_text=%d chars in %d blocks  thinking=%d chars  sidechain_msgs=%d\n\n"
                % (human(dur), asst_text_chars, asst_text_blocks, thinking_chars, sidechain_msgs))
        o.write("| tool | calls | errors | total wait | mean |\n|---|---|---|---|---|\n")
        for nm, n in tools.most_common():
            o.write("| %s | %d | %d | %s | %.1fs |\n" %
                    (nm, n, tool_err[nm], human(tool_ms[nm]), tool_ms[nm] / max(tool_n[nm], 1)))
        o.write("\n## repeated shell commands (>=3x)\n\n")
        for c, n in bash_cmds.most_common(40):
            if n >= 3: o.write("- %dx `%s`\n" % (n, c))
        o.write("\n## most-written files\n\n")
        for p, n in file_writes.most_common(25): o.write("- %dx %s\n" % (n, p))
        o.write("\n## oversized tool results (>20k chars)\n\n")
        for c, nm, s in sorted(big_results, reverse=True)[:25]:
            o.write("- %d chars %s :: %s\n" % (c, nm, s))

    summary.append(dict(sid=sid, mb=round(f.stat().st_size / 1048576, 1), first=str(first), last=str(last),
                        wall=human(dur), prompts=len(turns), tool_calls=sum(tools.values()),
                        tool_wait=human(sum(tool_ms.values())), asst_chars=asst_text_chars,
                        think_chars=thinking_chars, sidechain=sidechain_msgs,
                        top=", ".join("%s:%d" % (k, v) for k, v in tools.most_common(6))))

with (OUT / "summary.md").open("w", encoding="utf-8") as o:
    o.write("# session summary (%s)\n\n" % ROOT.name)
    o.write("| session | MB | start | wall | prompts | tool calls | tool wait | asst chars | think chars | sidechain | top tools |\n")
    o.write("|---|---|---|---|---|---|---|---|---|---|---|\n")
    for s in summary:
        o.write("| %s | %s | %s | %s | %d | %d | %s | %d | %d | %d | %s |\n" %
                (s["sid"][:8], s["mb"], s["first"][:16], s["wall"], s["prompts"], s["tool_calls"],
                 s["tool_wait"], s["asst_chars"], s["think_chars"], s["sidechain"], s["top"]))
print("wrote", len(summary), "sessions to", OUT)
