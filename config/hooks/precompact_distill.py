"""PreCompact hook: before a session is compacted, queue the lessons it teaches.

Hook mode (default): reads the hook's JSON from stdin, starts a detached copy of this
script with --run, and exits 0 at once, so compaction never waits and is never blocked.

Notify mode (--notify, a Stop hook): when a review for this session has finished, shows
its one-line result in the session's own window once.

Run mode (--run): condenses the transcript since the last compaction into a short text
file, asks a separate `claude -p` (read-only tools, no MCP servers) for lessons, and
appends any to ~/.claude/lessons-queue.md for Huy to approve. A routine session yields
"NOTHING TO LEARN" and queues nothing. Every run leaves one line in
~/.claude/distill/runs.log. Nothing is applied: the queue is a proposal list.
"""

import json
import os
import re
import subprocess
import sys
import time

HOME = os.path.expanduser("~")
WORK = os.path.join(HOME, ".claude", "distill")
QUEUE = os.path.join(HOME, ".claude", "lessons-queue.md")
PROMPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "distill_prompt.md")
CLAUDE = os.environ.get("DISTILL_CLAUDE") or os.path.join(HOME, ".local", "bin", "claude")
MODEL = os.environ.get("DISTILL_MODEL", "sonnet")
MAX_CHARS = 400_000          # condensed transcript cap; the newest part is kept
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
TROUBLE = re.compile(r"error|blocked|denied|failed|traceback|timed out|exit code [1-9]", re.I)


def mark_done(session, text):
    """Leave a note for the session's Stop hook to show once in its window."""
    d = os.path.join(WORK, "done")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, session), "w").write(text)


def log(line):
    os.makedirs(WORK, exist_ok=True)
    with open(os.path.join(WORK, "runs.log"), "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {line}\n")


def text_of(content):
    if isinstance(content, str):
        return content
    out = []
    for c in content or []:
        if isinstance(c, dict):
            if c.get("type") == "text":
                out.append(c.get("text", ""))
            elif isinstance(c.get("content"), (str, list)):
                out.append(text_of(c["content"]))
    return "\n".join(out)


def condense(transcript):
    """Turn the JSONL transcript since the last compaction into readable lines."""
    rows = []
    for line in open(transcript, errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if d.get("type") == "system" and d.get("subtype") == "compact_boundary":
            rows = ["(earlier part of the session was compacted before this point)"]
            continue
        msg = d.get("message") or {}
        content = msg.get("content")
        if d.get("type") == "user" and not d.get("isCompactSummary"):
            if isinstance(content, str):
                t = REMINDER.sub("", content).strip()
                if t:
                    rows.append(f"USER: {t[:4000]}")
                continue
            for c in content or []:
                if c.get("type") == "tool_result":
                    t = REMINDER.sub("", text_of(c.get("content"))).strip()
                    bad = c.get("is_error") or TROUBLE.search(t[:2000] or "")
                    rows.append(f"RESULT{' (ERROR)' if c.get('is_error') else ''}: {t[:1500 if bad else 200]}")
                elif c.get("type") == "text":
                    t = REMINDER.sub("", c.get("text", "")).strip()
                    if t:
                        rows.append(f"USER: {t[:4000]}")
        elif d.get("type") == "assistant":
            for c in content or []:
                if c.get("type") == "text" and c.get("text", "").strip():
                    rows.append(f"CLAUDE: {c['text'].strip()[:3000]}")
                elif c.get("type") == "tool_use":
                    rows.append(f"TOOL {c.get('name')}: {json.dumps(c.get('input'), ensure_ascii=False)[:400]}")
    body = "\n".join(rows)
    if len(body) > MAX_CHARS:
        body = "(start cut to fit)\n" + body[-MAX_CHARS:]
    return body


def run(transcript, session, cwd, trigger):
    os.makedirs(WORK, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    cond = os.path.join(WORK, f"{stamp}-{session[:8]}.txt")
    open(cond, "w").write(condense(transcript))
    prompt = open(PROMPT).read().replace("{TRANSCRIPT}", cond).replace("{CWD}", cwd)
    env = dict(os.environ, DISTILL_CHILD="1")
    try:
        out = subprocess.run(
            [CLAUDE, "-p", "--model", MODEL, "--no-session-persistence", "--strict-mcp-config",
             "--allowedTools", "Read", "Grep", "Glob",
             "--disallowedTools", "Bash", "Edit", "Write", "NotebookEdit", "Agent", "WebFetch", "WebSearch"],
            input=prompt, capture_output=True, text=True, timeout=1800, cwd=cwd or HOME, env=env)
        answer = out.stdout.strip()
    except Exception as e:  # never let a failure surface in the session
        log(f"FAILED session={session[:8]} trigger={trigger} {e!r}")
        return
    if out.returncode != 0 or not answer:
        log(f"FAILED session={session[:8]} trigger={trigger} rc={out.returncode} {out.stderr.strip()[:300]!r}")
        return
    if answer.startswith("NOTHING TO LEARN"):
        log(f"nothing session={session[:8]} trigger={trigger} cwd={cwd}")
        mark_done(session, "Lesson review of the last compaction: nothing to learn.")
        return
    n = answer.count("\n### ") + answer.startswith("### ")
    new = not os.path.exists(QUEUE)
    with open(QUEUE, "a") as f:
        if new:
            f.write("# Lessons queue\n\nProposed by the pre-compaction review. Nothing here is applied until "
                    "Huy approves it. Delete an entry once it is applied or rejected.\n")
        f.write(f"\n## {time.strftime('%Y-%m-%d %H:%M')} · {os.path.basename(cwd) or cwd} · "
                f"session {session[:8]} · {trigger}\n\n{answer}\n")
    log(f"queued {n} session={session[:8]} trigger={trigger} cwd={cwd}")
    mark_done(session, f"Lesson review of the last compaction: {n} lesson(s) queued in "
                       f"~/.claude/lessons-queue.md for Huy's approval.")


def notify():
    """Stop hook: show a finished review's result once, in that session's window."""
    try:
        p = json.load(sys.stdin)
    except ValueError:
        return
    f = os.path.join(WORK, "done", p.get("session_id", ""))
    if p.get("session_id") and os.path.isfile(f):
        msg = open(f).read().strip()
        os.remove(f)
        print(json.dumps({"systemMessage": msg}))


def main():
    if "--notify" in sys.argv:
        notify()
        return
    if "--run" in sys.argv:
        _, _, transcript, session, cwd, trigger = sys.argv
        run(transcript, session, cwd, trigger)
        return
    if os.environ.get("DISTILL_CHILD"):
        return
    try:
        p = json.load(sys.stdin)
    except ValueError:
        return
    t = p.get("transcript_path")
    if not t or not os.path.exists(t):
        return
    os.makedirs(WORK, exist_ok=True)
    errlog = open(os.path.join(WORK, "child-stderr.log"), "a")
    subprocess.Popen(
        [sys.executable, os.path.abspath(__file__), "--run", t, p.get("session_id", "unknown"),
         p.get("cwd", ""), p.get("trigger", "")],
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=errlog, start_new_session=True)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
