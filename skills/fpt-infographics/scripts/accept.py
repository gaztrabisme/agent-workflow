# -*- coding: utf-8 -*-
"""accept.py — run an artefact's acceptance criteria and report pass / superseded / FAIL.

    python scripts/accept.py criteria.toml [--json] [--only ID ...]

WHY THE STANDING/NEW SPLIT EXISTS
---------------------------------
Across eight versions of one sheet, each version's acceptance suite was written from
scratch. A requirement won in version 3 could therefore regress in version 4 with
nothing to notice it, and that is exactly what happened: a rule about confining each
duration to the block whose source gives it was won in v3 and broken again in v4 by a
chart that was restored without it. Nobody was careless. There was simply no artefact
that carried the earlier win forward.

So every criterion declares a class:

  standing  Won by an earlier version. Carries forward unchanged, for ever. A standing
            criterion that fails is reported as FAILED. It is never re-worded to match
            what was actually built, and never quietly dropped - that re-wording is the
            specific dishonesty this file exists to prevent.
  new       Introduced by the current goal.

and there is a third result beyond pass and fail:

  SUPERSEDED  A standing criterion that a later goal explicitly reversed. Recording it
              requires BOTH the id of the criterion that replaces it AND the goal's own
              words that reversed it, quoted. Without both it is an error, not a
              supersession. This is the hole: "superseded" with no quoted clause is
              indistinguishable from a failure someone relabelled.

A criterion whose check cannot run - missing file, crashed instrument, bad config - is
reported as FAIL with the reason. It is never skipped silently, because a skipped check
reads as a passing one in every summary anyone actually looks at.

THE CRITERIA FILE
-----------------
TOML, because the "statement" and "clause" fields carry sentences that need quoting and
the file needs comments explaining why a rule exists. `tomllib` is stdlib from 3.11.

    [meta]
    artefact = "one-pager/sheet.html"
    goal     = "goals/2026-09-18-thing.md"

    [[criterion]]
    id        = "S1"
    class     = "standing"            # or "new"
    statement = "The page fits its canvas with no scroll."
    [criterion.check]
    type = "shell"
    cmd  = ["node", "scripts/check.mjs", "{artefact}", "--preset", "a3-landscape"]
    expect_exit = 0

    [[criterion]]
    id        = "S7"
    class     = "standing"
    statement = "The delivery-model block carries its four labels."
    superseded_by = "N15"
    superseded_clause = "pay for the height by moving the delivery-model block off the sheet"

Check types:

  shell      cmd (list), expect_exit (int, default 0). {artefact} is substituted.
  grep       file, pattern (regex), expect = true|false, min_count (int, optional)
             Greps the file's BYTES. For a content rule about what the reader sees,
             use "text" instead - a self-contained sheet embeds base64 fonts, and any
             short pattern will eventually match inside them.
  text       cmd (list) printing text on stdout, pattern, expect / min_count
  json       cmd (list) producing JSON on stdout, path ("a.b.0.c"), op, value
             op is one of == != >= <= > < in contains
  python     module (path, relative to the criteria file), func - called with a dict of
             the meta table, returns (ok: bool, detail: str)

Exit code is 0 only when the FAIL count is zero. Superseded rows do not fail a run, but
they are counted and printed separately, and they never print as "pass".
"""
import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import tomllib

# Windows consoles default to cp1252 and this file prints em dashes and arrows.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PASS, SUPS, FAIL = "pass", "SUPS", "FAIL"


class Bad(Exception):
    """The criteria file is wrong, as opposed to the artefact being wrong."""


def _fmt(v, meta):
    return v.format(**meta) if isinstance(v, str) else v


# An interpreter that could not load its script also exits non-zero. If a criterion
# expects a non-zero exit, that is indistinguishable from the tool working - and a
# check that passes because the tool was broken is the exact failure this file exists
# to prevent. So look for the signatures of a tool that never ran.
DID_NOT_START = (
    "Cannot find module", "ModuleNotFoundError", "No such file or directory",
    "is not recognized as an internal or external command", "command not found",
)


def run_shell(chk, meta, cwd):
    cmd = [_fmt(c, meta) for c in chk["cmd"]]
    want = int(chk.get("expect_exit", 0))
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=600,
                           encoding="utf-8", errors="replace")
    except FileNotFoundError as e:
        return False, "cannot run %s: %s" % (cmd[0], e)
    except subprocess.TimeoutExpired:
        return False, "timed out after 600s: %s" % " ".join(cmd)
    err = p.stderr or ""
    for sig in DID_NOT_START:
        if sig in err:
            return False, ("the tool did not start (%r in stderr), so its exit code proves "
                           "nothing: %s" % (sig, " ".join(cmd)))
    ok = p.returncode == want
    tail = (p.stdout or p.stderr or "").strip().splitlines()
    detail = "exit %d (wanted %d)" % (p.returncode, want)
    if not ok and tail:
        detail += " :: " + tail[-1][:160]
    return ok, detail


def run_grep(chk, meta, cwd):
    path = os.path.join(cwd, _fmt(chk["file"], meta))
    if not os.path.exists(path):
        return False, "no such file: %s" % path
    text = open(path, encoding="utf-8", errors="replace").read()
    hits = re.findall(_fmt(chk["pattern"], meta), text, re.M)
    n = len(hits)
    if "min_count" in chk:
        return n >= int(chk["min_count"]), "%d match(es), wanted >= %s" % (n, chk["min_count"])
    want = bool(chk.get("expect", True))
    return (n > 0) == want, "%d match(es), wanted %s" % (n, "some" if want else "none")


def _dig(obj, path):
    for part in path.split("."):
        if isinstance(obj, list):
            obj = obj[int(part)]
        else:
            if part not in obj:
                raise Bad("path %r: no key %r" % (path, part))
            obj = obj[part]
    return obj


OPS = {"==": lambda a, b: a == b, "!=": lambda a, b: a != b,
       ">=": lambda a, b: a >= b, "<=": lambda a, b: a <= b,
       ">": lambda a, b: a > b, "<": lambda a, b: a < b,
       "in": lambda a, b: a in b, "contains": lambda a, b: b in a}


def run_json(chk, meta, cwd):
    cmd = [_fmt(c, meta) for c in chk["cmd"]]
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=600,
                           encoding="utf-8", errors="replace")
    except FileNotFoundError as e:
        return False, "cannot run %s: %s" % (cmd[0], e)
    raw = p.stdout.strip()
    if not raw:
        return False, "no JSON on stdout (exit %d) :: %s" % (p.returncode, (p.stderr or "").strip()[:160])
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError as e:
        return False, "stdout is not JSON: %s" % e
    got = _dig(obj, chk["path"])
    op = chk.get("op", "==")
    if op not in OPS:
        raise Bad("unknown op %r" % op)
    return OPS[op](got, chk["value"]), "%s = %r, wanted %s %r" % (chk["path"], got, op, chk["value"])


def run_python(chk, meta, cwd):
    mod_path = os.path.join(cwd, chk["module"])
    if not os.path.exists(mod_path):
        return False, "no such module: %s" % mod_path
    spec = importlib.util.spec_from_file_location("_accept_ext", mod_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fn = getattr(mod, chk["func"], None)
    if fn is None:
        return False, "%s has no %s()" % (chk["module"], chk["func"])
    return fn(dict(meta))


def run_text(chk, meta, cwd):
    """Regex against a command's stdout - the rendered text, not the file's bytes.

    A content rule is about what the reader sees. Grepping the HTML source of a
    self-contained sheet searches its embedded base64 fonts too, where every short
    letter sequence eventually occurs: one sheet matched "TCV" three times and "PwC"
    once, all four inside the font data and none of them on the page.
    """
    cmd = [_fmt(c, meta) for c in chk["cmd"]]
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=600,
                           encoding="utf-8", errors="replace")
    except FileNotFoundError as e:
        return False, "cannot run %s: %s" % (cmd[0], e)
    if p.returncode != 0:
        return False, "%s exited %d, so there is no text to check :: %s" % (
            cmd[0], p.returncode, (p.stderr or "").strip()[:160])
    hits = re.findall(_fmt(chk["pattern"], meta), p.stdout, re.M)
    n = len(hits)
    if "min_count" in chk:
        return n >= int(chk["min_count"]), "%d match(es), wanted >= %s" % (n, chk["min_count"])
    want = bool(chk.get("expect", True))
    detail = "%d match(es), wanted %s" % (n, "some" if want else "none")
    if n and not want:
        detail += " :: " + ", ".join(sorted(set(str(h) for h in hits))[:6])
    return (n > 0) == want, detail


RUNNERS = {"shell": run_shell, "grep": run_grep, "json": run_json,
           "python": run_python, "text": run_text}


def evaluate(crit, meta, cwd):
    """-> (state, detail). Every path returns one of PASS / SUPS / FAIL."""
    cid = crit.get("id", "<no id>")
    klass = crit.get("class")
    if klass not in ("standing", "new"):
        return FAIL, 'class must be "standing" or "new", got %r' % klass

    by = crit.get("superseded_by")
    clause = crit.get("superseded_clause")
    if by or clause:
        # The guard. A supersession is only a supersession if it names its replacement
        # AND quotes the goal that reversed it. Otherwise it is a failure wearing a
        # different word, which is the one thing this whole file exists to stop.
        if klass != "standing":
            return FAIL, "only a standing criterion can be superseded (%s is %s)" % (cid, klass)
        if not by:
            return FAIL, "superseded_clause given without superseded_by — name the criterion that replaces it"
        if not clause or not clause.strip():
            return FAIL, ("superseded_by given without superseded_clause — quote the goal's own "
                          "words that reversed this criterion, verbatim")
        return SUPS, 'superseded by %s — goal clause: "%s"' % (by, clause.strip())

    chk = crit.get("check")
    if not isinstance(chk, dict):
        return FAIL, "no [criterion.check] table"
    t = chk.get("type")
    if t not in RUNNERS:
        return FAIL, "unknown check type %r (have: %s)" % (t, ", ".join(sorted(RUNNERS)))
    try:
        ok, detail = RUNNERS[t](chk, meta, cwd)
    except Bad as e:
        return FAIL, "criteria file: %s" % e
    except Exception as e:                      # a crashed check is a FAIL, never a skip
        return FAIL, "check raised %s: %s" % (type(e).__name__, e)
    return (PASS if ok else FAIL), detail


def main():
    ap = argparse.ArgumentParser(description="Run acceptance criteria for one artefact.")
    ap.add_argument("criteria", help="path to a .toml criteria file")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--only", nargs="*", default=None, metavar="ID")
    a = ap.parse_args()

    path = os.path.abspath(a.criteria)
    if not os.path.exists(path):
        sys.exit("no such criteria file: %s" % path)
    try:
        with open(path, "rb") as fh:
            doc = tomllib.load(fh)
    except tomllib.TOMLDecodeError as e:
        sys.exit("%s is not valid TOML: %s\n"
                 "  A regex belongs in a single-quoted TOML literal string, which does no\n"
                 "  escape processing. Use  pattern = '\\$[0-9]+'  and not the double-quoted\n"
                 "  form, where a backslash starts an escape sequence." % (path, e))

    meta = doc.get("meta", {})
    # Every relative path in the file - artefact, grep targets, script paths, the cwd
    # commands run in - resolves against meta.root, itself relative to the criteria
    # file. Default "." means "beside the criteria file".
    cwd = os.path.normpath(os.path.join(os.path.dirname(path), meta.get("root", ".")))
    if not os.path.isdir(cwd):
        sys.exit("meta.root does not exist: %s" % cwd)
    crits = doc.get("criterion", [])
    if not crits:
        sys.exit("criteria file has no [[criterion]] entries: %s" % path)

    seen, rows = set(), []
    for c in crits:
        cid = c.get("id", "<no id>")
        if a.only and cid not in a.only:
            continue
        if cid in seen:
            rows.append((cid, c.get("class", "?"), c.get("statement", ""), FAIL,
                         "duplicate id — an id must identify one criterion"))
            continue
        seen.add(cid)
        state, detail = evaluate(c, meta, cwd)
        rows.append((cid, c.get("class", "?"), c.get("statement", ""), state, detail))

    npass = sum(1 for r in rows if r[3] == PASS)
    nsups = sum(1 for r in rows if r[3] == SUPS)
    nfail = sum(1 for r in rows if r[3] == FAIL)

    if a.json:
        print(json.dumps({"criteria": path, "meta": meta,
                          "rows": [dict(zip(("id", "class", "statement", "state", "detail"), r)) for r in rows],
                          "pass": npass, "superseded": nsups, "fail": nfail}, indent=1))
    else:
        print("\n  ACCEPTANCE — %s" % meta.get("artefact", path))
        if meta.get("goal"):
            print("  goal: %s" % meta["goal"])
        print()
        for cid, kl, stmt, state, detail in rows:
            mark = {PASS: "  ", SUPS: "~ ", FAIL: "x "}[state]
            print("  %s%-5s %-8s %-4s  %s" % (mark, cid, kl, state, stmt))
            if state != PASS or not stmt:
                print("            %s" % detail)
        print("\n  %d pass, %d superseded, %d FAIL (of %d)\n" % (npass, nsups, nfail, len(rows)))
        if nsups:
            print("  A superseded row is not a pass. It is a standing criterion a later goal")
            print("  reversed, and the clause that reversed it is quoted above.\n")

    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
