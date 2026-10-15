#!/usr/bin/env python3
"""Verify a WBS workbook against its YAML data and project settings.

    python verify.py FILE.xlsx --project project.yaml --data DATA_DIR [--plan-total N] [--max-lines 12]

This file does not import build.py. Every expected value is re-derived here from the YAML data, the
project settings and the rules in SCHEMA.md, then compared with the workbook. It imports wbs_common only
to read the settings and the data files.
Prints PASS or FAIL per check group, with the failing cells, and WARNING lines that do not fail the run.
Exit 0 only when every group passes; 1 when any fails; 2 when the settings or data cannot be read.
Figures are read from cached values, so recalculate the workbook first (build.py --recalc).
"""
import argparse
import math
import os
import re
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wbs_common as wc  # noqa: E402

TOL = 0.01
ERRORS = {"#VALUE!", "#REF!", "#DIV/0!", "#NAME?", "#N/A", "#NUM!", "#NULL!"}
VIET = re.compile("[ăâđêôơưĂÂĐÊÔƠƯẠ-ỿ]")
GROUPS = ["structure", "master inputs", "cached values", "task detail rows", "effort rule", "proposals",
          "sources", "removals", "live formulas", "effort summary", "base total", "reference check",
          "wbs sums", "criteria coverage", "stories", "dependencies", "references", "text length",
          "diacritics", "person names and sources", "acceptance clause", "proposal marking"]


def fnum(x):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) else None


def blank(x):
    return x is None or (isinstance(x, str) and x.strip() == "")


def close(a, b, tol=1e-6):
    if a is None or b is None:
        return a is None and b is None
    return abs(float(a) - float(b)) <= tol


def numbered(lines):
    return "\n".join("%d. %s" % (i, t) for i, t in enumerate(lines, 1)) if lines else None


def numbered_lines(cell):
    if blank(cell):
        return []
    return [re.sub(r"^\d+\.\s", "", ln) for ln in str(cell).split("\n")]


def sheet_rows(ws):
    return [list(r) for r in ws.iter_rows(values_only=True)]


def find_label(rows, label, start=0):
    for i in range(start, len(rows)):
        if rows[i] and rows[i][0] == label:
            return i
    return None


# ------------------------------------------------------------------ expected model (YAML and settings only)
def build_expected(cfg, d):
    S, T, O = cfg["statuses"], cfg["texts"], cfg["owners"]
    plan = wc.load_data(cfg, d, "plan_tasks")
    fm = wc.load_data(cfg, d, "feature_map")
    ch = wc.load_data(cfg, d, "changes", required=False, default={}) or {}
    pr = wc.load_data(cfg, d, "proposals", required=False, default={}) or {}
    rows = {str(r["id"]): r for r in fm["rows"]}
    tmap = {str(o["task_id"]): str(o["wbs_id"]) for o in (fm.get("task_map") or [])}
    fmap = {str(m["plan_feature"]): str(m["wbs_id"]) for m in fm["map"]}
    st_by = {str(s["task_id"]): s for s in (ch.get("status") or [])}
    n = int(cfg["data"]["feature_key_parts"])

    recs, by = [], {}
    for t in plan["tasks"]:
        pid = str(t["task_id"])
        over = t.get("phase") == cfg["plan"]["overhead_phase"]
        rec = {"id": pid, "kind": "overhead" if over else "plan",
               "wbs": tmap.get(pid) or fmap[".".join(pid.split(".")[:n])],
               "section": t.get("sheet") or "", "role": t.get("role"), "dev": t.get("dev"), "qc": t.get("qc"),
               "ba": t.get("ba"), "effort": t.get("effort"), "owner": O["ours"], "note": None,
               "status": S["overhead"] if over else S["in_scope"], "dod": t.get("dod"), "acs": [],
               "orig": None, "source": None, "proposal": False, "highlight": False}
        if not over and pid in st_by:
            s = st_by[pid]
            rec["status"] = S["change"][s["status"]]
            rec["owner"] = s["owner"]
            rec["note"] = str(s.get("reason") or "").strip() or None
            rec["source"] = s.get("source")
        recs.append(rec)
        by[pid] = rec

    def add(a, proposal):
        aid = str(a["id"])
        rec = {"id": aid, "kind": "add", "wbs": str(a["wbs_id"]), "section": T["section_added"],
               "role": a["role"], "dev": a.get("dev"), "qc": a.get("qc"), "ba": a.get("ba"),
               "effort": a["effort"], "owner": rows[str(a["wbs_id"])]["owner"], "status": S["add"][a["status"]],
               "dod": a.get("dod"), "acs": [], "orig": None, "source": a.get("source"), "proposal": proposal,
               "highlight": bool(a.get("highlight")) and not proposal}
        if proposal:
            rec["note"] = str(a.get("reason") or "").strip()
        else:
            rec["note"] = T["note_highlight"] if a.get("highlight") else T["note_added"]
        recs.append(rec)
        by[aid] = rec
    for a in ch.get("add") or []:
        add(a, False)
    for c in pr.get("change") or []:
        rec = by[str(c["task_id"])]
        rec["orig"] = {k: rec[k] for k in ("dev", "qc", "ba", "effort")}
        for k in ("dev", "qc", "ba", "effort"):
            rec[k] = c.get(k)
        rec["note"] = str(c.get("reason") or "").strip()
        rec["source"] = c.get("source")
        rec["proposal"] = True
    for a in pr.get("add") or []:
        add(a, True)
    for f in wc.criteria_files(cfg, d):
        doc = wc.load_data(cfg, d, name=f) or {}
        for t in doc.get("tasks") or []:
            rec = by.get(str(t["task_id"]))
            if rec is not None:
                rec["acs"] = [str(x).strip() for x in (t.get("acs") or [])]
    for rec in recs:
        rec["criteria"] = numbered(rec["acs"]) if rec["acs"] else rec["dod"]
    options = []
    for i, o in enumerate(plan.get("options") or [], 1):
        if o.get("role") in O["excluded_option_roles"]:
            continue
        options.append({"id": "%s%d" % (cfg["ids"]["option_prefix"], i), "kind": "option", "wbs": None,
                        "section": T["section_option"], "role": o.get("role"), "dev": o.get("dev"),
                        "qc": o.get("qc"), "ba": o.get("ba"), "effort": o.get("effort"), "owner": O["ours"],
                        "note": T["note_option"], "status": S["option"], "criteria": None, "acs": [],
                        "source": None, "proposal": False, "highlight": False})
    order = [str(r["id"]) for r in fm["rows"]]
    if O["excluded"] is not None:
        recs = [r for r in recs if r["owner"] != O["excluded"]]
        ours = {r["wbs"] for r in recs if r.get("wbs")}
        for rid in list(order):
            if rows[rid]["owner"] == O["excluded"]:
                if rid in ours:
                    rows[rid] = dict(rows[rid], owner=O["ours"])
                else:
                    order.remove(rid)
                    del rows[rid]
    sdoc = wc.load_data(cfg, d, "stories", required=False, default=None)
    srcdoc = wc.load_data(cfg, d, "story_source", required=False, default={}) or {}
    src_by = {str(s["us_id"]): s for s in (srcdoc.get("stories") or [])}
    stories = []
    items = (sdoc.get("stories") or []) if sdoc is not None else (srcdoc.get("stories") or [])
    for s in items:
        stories.append({"us_id": str(s["us_id"]), "title": str(s.get("title") or ""),
                        "story": s.get("story") if sdoc is not None else None,
                        "acs": [str(x) for x in (s.get("acs") or [])],
                        "wbs": [str(w) for w in (s.get("wbs_ids") or [])],
                        "origin": (s.get("origin") if sdoc is not None else None) or cfg["stories"]["default_origin"],
                        "source": s.get("source")})
    return {"recs": recs, "options": options, "by": {r["id"]: r for r in recs}, "changes": ch, "proposals": pr,
            "rows": rows, "rows_order": order, "plan_tasks": plan["tasks"], "stories": stories, "src_by": src_by,
            "deps": wc.load_data(cfg, d, "dependencies", required=False, default=[]) or [],
            "assumptions": wc.load_data(cfg, d, "assumptions", required=False, default=[]) or [],
            "glossary": wc.load_data(cfg, d, "glossary", required=False, default=[]) or []}


def master_value(cfg, name):
    for r in cfg["master"]["rows"]:
        if r.get("name") == name:
            return float(r["value"])
    raise KeyError(name)


def plan_check(ctx):
    cfg = ctx["cfg"]
    rows = [t for t in ctx["E"]["plan_tasks"] if t.get("phase") != cfg["plan"]["overhead_phase"]]
    eff = sum(float(t.get("effort") or 0) for t in rows)
    dev = sum(float(t.get("dev") or 0) for t in rows)
    return eff, dev, (eff + ctx["PM"] * dev) * (1 + ctx["CONT"])


# ------------------------------------------------------------------ workbook readers
def read_td(cfg, rows):
    col = cfg["_col"]["task_detail"]
    tasks, subs, order, dup = {}, [], [], []
    for i, r in enumerate(rows[1:], 2):
        r = r + [None] * max(0, len(col) - len(r))
        d = {k: r[c - 1] for k, c in col.items()}
        d["row"] = i
        if blank(d["task_id"]) and blank(d["row_type"]):
            continue
        if d["row_type"] == cfg["texts"]["row_type_sub"]:
            subs.append(d)
        else:
            if d["task_id"] in tasks:
                dup.append(d["task_id"])
            tasks[d["task_id"]] = d
            order.append(d["task_id"])
    return tasks, subs, dup, order


def load_refs(cfg, wb):
    col = cfg["_col"]["references"]
    out = {}
    for r in sheet_rows(wb[cfg["_sheet_name"]["references"]])[1:]:
        item, ref = r[col["item"] - 1], r[col["reference"] - 1]
        if item is not None:
            out[str(item)] = (out.get(str(item), "") + " " + str(ref or "")).strip()
    return out


def parent_of(cfg, sub_id):
    return str(sub_id).rsplit(cfg["ids"]["subtask_infix"], 1)[0]


# ------------------------------------------------------------------ groups
def g_structure(ctx):
    cfg, f = ctx["cfg"], []
    names = ctx["wbf"].sheetnames
    if names != cfg["_sheet_order"]:
        f.append("sheet order is %s, expected %s" % (names, cfg["_sheet_order"]))
    for ws in ctx["wbf"].worksheets:
        if ws.sheet_state != "visible":
            f.append("sheet %s is %s" % (ws.title, ws.sheet_state))
    for key, cols in cfg["columns"].items():
        name = cfg["_sheet_name"][key]
        if name not in names:
            continue
        got = [ctx["wbv"][name].cell(1, i).value for i in range(1, len(cols) + 1)]
        want = [c["header"] for c in cols]
        if got != want:
            f.append("%s header row is %s, expected %s" % (name, got, want))
    return f


def g_master(ctx):
    cfg, f = ctx["cfg"], []
    name = cfg["_sheet_name"]["master"]
    rows = sheet_rows(ctx["wbv"][name])
    found = {}
    for i, r in enumerate(rows, 1):
        if r and r[0] is not None:
            found.setdefault(r[0], (i, r[1] if len(r) > 1 else None))
    for spec in cfg["master"]["rows"]:
        label = spec["label"]
        if label not in found:
            f.append("%s: row '%s' is missing" % (name, label))
            continue
        i, v = found[label]
        if not close(fnum(v), spec["value"], 1e-9):
            f.append("%s B%d (%s) is %r, expected %r" % (name, i, label, v, spec["value"]))
        if spec.get("name"):
            dn = ctx["wbf"].defined_names.get(spec["name"])
            want = "%s!$B$%d" % (name if name.replace("_", "").isalnum() else "'%s'" % name, i)
            if dn is None:
                f.append("defined name %s is missing" % spec["name"])
            elif dn.attr_text != want:
                f.append("defined name %s points at %s, expected %s" % (spec["name"], dn.attr_text, want))
    nums = [float(x) for x in cfg["master"]["forbidden_numbers"]]
    words = [w.lower() for w in cfg["master"]["forbidden_words"]]
    for i, r in enumerate(rows, 1):
        for v in r:
            s = str(v).lower() if v is not None else ""
            if (fnum(v) is not None and any(close(v, x, 1e-12) for x in nums)) or any(w in s for w in words) \
                    or any(("%g" % x) in s for x in nums if x != int(x)):
                f.append("%s row %d holds a forbidden item: %r" % (name, i, v))
    pats = [re.compile(r"(?<![\d.])%s(?![\d])" % re.escape("%g" % x)) for x in nums]
    for wsf in ctx["wbf"].worksheets:
        for row in wsf.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("=") and any(p.search(c.value) for p in pats):
                    f.append("%s!%s formula uses a forbidden factor: %s" % (wsf.title, c.coordinate, c.value))
    return f


def g_cached(ctx):
    f = []
    for wsf in ctx["wbf"].worksheets:
        wsv = ctx["wbv"][wsf.title]
        for row in wsf.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("="):
                    cv = wsv[c.coordinate].value
                    if cv is None:
                        f.append("%s!%s has no cached value (recalculate with LibreOffice)" % (wsf.title, c.coordinate))
                    elif isinstance(cv, str) and (cv in ERRORS or cv.startswith("Err:")):
                        f.append("%s!%s is an error value %s" % (wsf.title, c.coordinate, cv))
    return f


def g_task_rows(ctx):
    cfg, E, f = ctx["cfg"], ctx["E"], []
    tasks, subs, dup, order = ctx["td"]
    for d in dup:
        f.append("Task Detail: task %s appears more than once" % d)
    expected = E["recs"] + E["options"]
    exp_ids = {r["id"] for r in expected}
    for tid in order:
        if tid not in exp_ids:
            f.append("Task Detail: unexpected task row %s" % tid)
    over_days = cfg["criteria"]["over_days"]
    for rec in expected:
        d = tasks.get(rec["id"])
        if d is None:
            f.append("Task Detail: %s is missing" % rec["id"])
            continue
        where = "Task Detail row %d (%s)" % (d["row"], rec["id"])
        if (rec["section"] or "") != (d["section"] or ""):
            f.append("%s: section %r, expected %r" % (where, d["section"], rec["section"]))
        if rec["kind"] != "option" and d["wbs_id"] != rec["wbs"]:
            f.append("%s: WBS ID %r, expected %r" % (where, d["wbs_id"], rec["wbs"]))
        if (rec.get("role") or None) != (d["role"] or None):
            f.append("%s: role %r, expected %r" % (where, d["role"], rec.get("role")))
        for k in ("dev", "qc", "ba", "effort"):
            if not close(fnum(d[k]), fnum(rec.get(k))) and not (blank(d[k]) and rec.get(k) is None):
                f.append("%s: %s is %r, expected %r" % (where, k, d[k], rec.get(k)))
        if d["status"] != rec["status"]:
            f.append("%s: status %r, expected %r" % (where, d["status"], rec["status"]))
        if d["owner"] != rec["owner"]:
            f.append("%s: owner %r, expected %r" % (where, d["owner"], rec["owner"]))
        if str(d["note"] or "").strip() != str(rec["note"] or "").strip():
            f.append("%s: change note %r, expected %r" % (where, d["note"], rec["note"]))
        eff = fnum(rec.get("effort"))
        want_over = None if eff is None else ("Yes" if eff > over_days else "No")
        if (d["over_threshold"] or None) != want_over:
            f.append("%s: over-threshold flag %r, expected %r" % (where, d["over_threshold"], want_over))
        if rec.get("criteria") is not None and (d["criteria"] or "").strip() != rec["criteria"].strip():
            f.append("%s: acceptance criteria differ from the criteria file or the definition of done" % where)
    for s in subs:
        if parent_of(cfg, s["task_id"]) not in tasks:
            f.append("Task Detail row %d: sub-task %s has no task" % (s["row"], s["task_id"]))
    return f


def g_effort_rule(ctx):
    cfg, f = ctx["cfg"], []
    R = cfg["effort_rule"]
    rq, rb, step, tol = float(R["addons"]["qc"]), float(R["addons"]["ba"]), float(R["round_up_to"]), float(R["tolerance"])
    for tid, d in ctx["td"][0].items():
        if d["role"] in R["no_dev_roles"]:
            if any(fnum(d[k]) is not None for k in ("dev", "qc", "ba")):
                f.append("Task Detail %s: role %s carries no dev, but has dev or add-ons" % (tid, d["role"]))
            continue
        dev = fnum(d["dev"])
        if dev is None:
            continue
        qc, ba = fnum(d["qc"]), fnum(d["ba"])
        if (qc is None) != (ba is None):
            f.append("Task Detail %s: QC and BA add-ons must both be present or both blank" % tid)
            continue
        if qc is not None and (abs(qc - rq * dev) > tol or abs(ba - rb * dev) > tol):
            f.append("Task Detail %s: QC %s / BA %s are not %g / %g of Dev %s" % (tid, qc, ba, rq, rb, dev))
        want = math.ceil(round((dev + (qc or 0.0) + (ba or 0.0)) / step, 6)) * step
        if not close(fnum(d["effort"]), want):
            f.append("Task Detail %s: effort %s, rule gives %s" % (tid, d["effort"], want))
    return f


def proposal_items(E):
    return [(str(c.get("task_id")), c) for c in (E["proposals"].get("change") or [])] + \
           [(str(a.get("id")), a) for a in (E["proposals"].get("add") or [])]


def g_proposals(ctx):
    cfg, E, f = ctx["cfg"], ctx["E"], []
    tasks = ctx["td"][0]
    prefix = cfg["marking"]["proposal_prefix"]
    for tid, c in proposal_items(E):
        reason = str(c.get("reason") or "")
        if not reason.startswith(prefix):
            f.append("proposal %s: reason does not start with '%s'" % (tid, prefix))
        d = tasks.get(tid)
        if d is None:
            f.append("proposal %s: not in Task Detail" % tid)
        elif str(d["note"] or "").strip() != reason.strip():
            f.append("Task Detail %s: change note does not carry the proposal reason" % tid)
    return f


def g_sources(ctx):
    """Every changed or added figure, and every removal, names a source, and References carries it."""
    cfg, E, f = ctx["cfg"], ctx["E"], []
    refs = ctx["refs"]
    items = [("proposal", tid, c.get("source")) for tid, c in proposal_items(E)]
    items += [("added task", str(a.get("id")), a.get("source")) for a in (E["changes"].get("add") or [])]
    items += [("status change", str(s.get("task_id")), s.get("source")) for s in (E["changes"].get("status") or [])
              if s.get("status") in cfg["statuses"]["needs_source"]]
    excluded = {r["id"] for r in E["recs"]}
    for kind, tid, src in items:
        src = str(src or "").strip()
        if not src:
            f.append("%s %s: no source" % (kind, tid))
        elif tid in excluded and src not in refs.get(tid, ""):
            f.append("%s %s: References does not carry its source" % (kind, tid))
    for rid in E["rows_order"]:
        if blank(E["rows"][rid].get("source")):
            f.append("WBS row %s: no source" % rid)
    for i, a in enumerate(E["assumptions"], 1):
        if blank(a.get("source")):
            f.append("assumption #%d: no source" % i)
    return f


def g_removals(ctx):
    cfg, E, f = ctx["cfg"], ctx["E"], []
    tasks, refs = ctx["td"][0], ctx["refs"]
    marker = cfg["statuses"]["removal_source_marker"]
    for s in E["changes"].get("status") or []:
        if s["status"] not in cfg["statuses"]["needs_source"]:
            continue
        pid = str(s["task_id"])
        src = str(s.get("source") or "")
        if marker and marker not in src:
            f.append("removal %s: source %r does not contain '%s'" % (pid, src, marker))
        label = cfg["statuses"]["change"][s["status"]]
        if s.get("owner") == cfg["owners"]["excluded"]:
            continue
        d = tasks.get(pid)
        if d is None or d["status"] != label:
            f.append("removal %s: Task Detail status is not %s" % (pid, label))
    return f


def summary_formula_labels(cfg):
    S = cfg["summary"]
    base = [a["label"] for a in S["activities"]] + [S[k]["label"] for k in
                                                     ("subtotal", "check", "dev_memo", "pm", "sub", "contingency", "total")]
    opt = [S["option_lines"][k]["label"] for k in ("effort", "dev", "pm", "sub", "contingency", "total")]
    other = [o["label"] for o in cfg["owners"]["other_owner_lines"]]
    plan = [S["plan_check"][k]["label"] for k in ("pm", "sub", "contingency", "total", "difference")]
    bridge = [S["bridge"][k]["label"] for k in ("start", "end", "difference")]
    return base, opt, other, plan, bridge


def g_formulas(ctx):
    """Summary cells are formulas over the detail: no typed totals on the WBS or the summary sheet."""
    cfg, f = ctx["cfg"], []
    ws = ctx["wbf"][cfg["_sheet_name"]["wbs"]]
    col = cfg["_col"]["wbs"]
    id_col = col["id"]
    for r in range(2, ws.max_row + 1):
        rid = ws.cell(r, id_col).value
        if rid is None:
            continue
        for k in ("dev", "qc", "ba", "effort"):
            v = ws.cell(r, col[k]).value
            if not (isinstance(v, str) and v.startswith("=")):
                f.append("%s!%s (%s, %s) is a typed value %r, not a formula" % (ws.title, ws.cell(r, col[k]).coordinate,
                                                                                rid, k, v))
    rows = list(ctx["wbf"][cfg["_sheet_name"]["summary"]].iter_rows())
    base, opt, other, plan, bridge = summary_formula_labels(cfg)
    S = cfg["summary"]
    blocks = [(S["base_title"], base)] + [(b["title"], opt) for b in S["option_blocks"]] + \
             [(S["other_title"], other), (S["plan_check"]["title"], plan), (S["bridge"]["title"], bridge)]
    labels = [r[0].value for r in rows]
    for title, want in blocks:
        if not want:
            continue
        if title not in labels:
            f.append("summary block %r is missing" % title)
            continue
        start = labels.index(title)
        for lab in want:
            j = next((i for i in range(start, len(rows)) if labels[i] == lab), None)
            if j is None:
                f.append("summary line %r is missing under %r" % (lab, title))
                continue
            v = rows[j][1].value
            if not (isinstance(v, str) and v.startswith("=")):
                f.append("summary %s (%s) is a typed value %r, not a formula" % (rows[j][1].coordinate, lab, v))
    return f


def expected_block(cfg, wr, PM, CONT):
    S = cfg["summary"]
    out = {}
    eff = 0.0
    for a in S["activities"]:
        if a["kind"] == "role_plus_addon":
            v = sum(r["effort"] for r in wr if r["role"] == a["role"]) + sum(r[a["addon"]] for r in wr)
        else:
            v = sum(r["effort"] - r["qc"] - r["ba"] for r in wr if r["role"] in a["roles"])
        out[a["label"]] = v
        eff += v
    devtot = sum(r["dev"] for r in wr)
    pm = PM * devtot
    sub = eff + pm
    cont = CONT * sub
    out.update({S["subtotal"]["label"]: eff, S["dev_memo"]["label"]: devtot, S["pm"]["label"]: pm,
                S["sub"]["label"]: sub, S["contingency"]["label"]: cont, S["total"]["label"]: sub + cont})
    return out


def td_rows(ctx, status=None, owner=None):
    cfg = ctx["cfg"]
    status = status or cfg["statuses"]["in_scope"]
    owner = owner or cfg["owners"]["ours"]
    return [{"role": t["role"], "effort": fnum(t["effort"]) or 0, "dev": fnum(t["dev"]) or 0,
             "qc": fnum(t["qc"]) or 0, "ba": fnum(t["ba"]) or 0}
            for t in ctx["td"][0].values() if t["status"] == status and t["owner"] == owner]


def g_effort_summary(ctx):
    cfg, f = ctx["cfg"], []
    S = cfg["summary"]
    rows = sheet_rows(ctx["wbv"][cfg["_sheet_name"]["summary"]])
    PM, CONT, MD, RATE = ctx["PM"], ctx["CONT"], ctx["MD"], ctx["RATE"]
    exp = expected_block(cfg, td_rows(ctx), PM, CONT)
    i = find_label(rows, S["base_title"])
    if i is None:
        return ["summary block %r is missing" % S["base_title"]]
    for label, want in exp.items():
        j = find_label(rows, label, i)
        if j is None:
            f.append("summary line '%s' is missing" % label)
            continue
        got = fnum(rows[j][1])
        if got is None or abs(got - want) > TOL:
            f.append("summary '%s' B%d is %r, recomputed %.4f" % (label, j + 1, rows[j][1], want))
            continue
        if label != S["dev_memo"]["label"]:
            if fnum(rows[j][2]) is None or abs(rows[j][2] - got / MD) > 0.005:
                f.append("summary '%s' C%d (man-months) is not days / days per month" % (label, j + 1))
            if fnum(rows[j][4]) is None or abs(rows[j][4] - got / MD * RATE) > 1:
                f.append("summary '%s' E%d (cost) is not man-months x rate" % (label, j + 1))
    j = find_label(rows, S["check"]["label"], i)
    if j is None or abs(fnum(rows[j][1]) or 0) > TOL:
        f.append("summary check line is %r, must be 0" % (rows[j][1] if j is not None else None))
    OL = S["option_lines"]
    for blk in S["option_blocks"]:
        rs = td_rows(ctx, status=blk["status"])
        eff = sum(r["effort"] for r in rs)
        tot = (eff + PM * sum(r["dev"] for r in rs)) * (1 + CONT)
        h = find_label(rows, blk["title"])
        if h is None:
            f.append("summary block %r is missing" % blk["title"])
            continue
        for lab, want in ((OL["effort"]["label"], eff), (OL["total"]["label"], tot)):
            j = find_label(rows, lab, h)
            if j is None or abs((fnum(rows[j][1]) or 0) - want) > TOL:
                f.append("summary %r line %r is not %.4f" % (blk["title"], lab, want))
    for o in cfg["owners"]["other_owner_lines"]:
        want = sum(r["effort"] for r in td_rows(ctx, owner=o["owner"]))
        j = find_label(rows, o["label"], i)
        if j is None or abs((fnum(rows[j][1]) or 0) - want) > TOL:
            f.append("summary '%s' is not %.4f" % (o["label"], want))
    P = S["plan_check"]
    h = find_label(rows, P["title"], i)
    if h is None:
        f.append("summary plan check block is missing")
    else:
        eff, dev, tot = plan_check(ctx)
        for lab, want in ((P["effort"]["label"], eff), (P["dev"]["label"], dev), (P["total"]["label"], tot)):
            j = find_label(rows, lab, h)
            if j is None or abs((fnum(rows[j][1]) or 0) - want) > TOL:
                f.append("summary '%s' is not %.4f (recomputed from the plan tasks)" % (lab, want))
    BR = S["bridge"]
    hb = find_label(rows, BR["title"], i)
    if hb is None:
        f.append("summary bridge block is missing")
    else:
        base_eff = sum(r["effort"] for r in td_rows(ctx))
        for lab, want in ((BR["start"]["label"], plan_check(ctx)[0]), (BR["end"]["label"], base_eff),
                          (BR["difference"]["label"], 0.0)):
            j = find_label(rows, lab, hb)
            if j is None or abs((fnum(rows[j][1]) or 0) - want) > TOL:
                f.append("summary bridge '%s' is not %.4f" % (lab, want))
    return f


def g_base(ctx):
    """The base total recomputed from the YAML alone (not from the workbook's own rows)."""
    cfg, E, f = ctx["cfg"], ctx["E"], []
    base = [r for r in E["recs"] if r["status"] == cfg["statuses"]["in_scope"] and r["owner"] == cfg["owners"]["ours"]]
    eff = sum(float(r["effort"] or 0) for r in base)
    dev = sum(float(r["dev"] or 0) for r in base)
    tot = (eff + ctx["PM"] * dev) * (1 + ctx["CONT"])
    ctx["yaml_total"] = (tot, eff, dev)
    rows = sheet_rows(ctx["wbv"][cfg["_sheet_name"]["summary"]])
    i = find_label(rows, cfg["summary"]["total"]["label"])
    got = fnum(rows[i][1]) if i is not None else None
    if got is None or abs(got - tot) > TOL:
        f.append("summary total is %r; recomputed from the in-scope rows of the YAML: %.4f" % (got, tot))
    return f


def g_reference(ctx):
    cfg, f = ctx["cfg"], []
    P = cfg["summary"]["plan_check"]
    eff, dev, tot = plan_check(ctx)
    if abs(tot - ctx["plan_total"]) > TOL:
        f.append("plan total recomputed from the plan tasks is %.4f; the owner's figure is %.4f" % (tot, ctx["plan_total"]))
    rows = sheet_rows(ctx["wbv"][cfg["_sheet_name"]["summary"]])
    h = find_label(rows, P["title"])
    if h is None:
        return f + ["summary plan check block is missing"]
    j, k, m = (find_label(rows, P[x]["label"], h) for x in ("total", "reference", "difference"))
    if j is None or k is None or m is None:
        return f + ["summary plan check lines are missing"]
    if abs((fnum(rows[j][1]) or 0) - tot) > TOL:
        f.append("cached plan total %r differs from the recomputed %.4f" % (rows[j][1], tot))
    if abs((fnum(rows[k][1]) or 0) - ctx["plan_total"]) > 1e-6:
        f.append("reference figure %r is not %.4f" % (rows[k][1], ctx["plan_total"]))
    if abs(fnum(rows[m][1]) or 0) > TOL:
        f.append("reference difference is %r, must be 0" % rows[m][1])
    return f


def g_wbs(ctx):
    cfg, E, f = ctx["cfg"], ctx["E"], []
    col = cfg["_col"]["wbs"]
    rows = sheet_rows(ctx["wbv"][cfg["_sheet_name"]["wbs"]])
    OURS, IN = cfg["owners"]["ours"], cfg["statuses"]["in_scope"]
    by_row = {}
    for t in ctx["td"][0].values():
        if t["status"] == IN and t["owner"] == OURS and t["wbs_id"]:
            by_row.setdefault(t["wbs_id"], []).append(t)
    got = {r[col["id"] - 1]: r for r in rows[1:] if r and r[col["id"] - 1] in E["rows"]}
    for rid in E["rows_order"]:
        r = got.get(rid)
        if r is None:
            f.append("WBS: row %s is missing" % rid)
            continue
        ts = by_row.get(rid, [])
        for k in ("dev", "qc", "ba", "effort"):
            w = sum(fnum(t[k]) or 0 for t in ts)
            v = fnum(r[col[k] - 1])
            if v is None or abs(v - w) > TOL:
                f.append("WBS %s %s is %r, expected %.4f" % (rid, k, r[col[k] - 1], w))
        own = E["rows"][rid]["owner"]
        want = own if own == OURS or not ts else cfg["owners"]["shared_row_label"].format(owner=own)
        if r[col["owner"] - 1] != want:
            f.append("WBS %s owner is %r, expected %r" % (rid, r[col["owner"] - 1], want))
    tot = [r for r in rows if r and r[col["id"] - 1] == "TOTAL"]
    if not tot:
        return f + ["WBS: TOTAL row is missing"]
    for k in ("dev", "qc", "ba", "effort"):
        s = sum(fnum(r[col[k] - 1]) or 0 for r in rows[1:] if r and r[col["id"] - 1] in E["rows"])
        if abs((fnum(tot[0][col[k] - 1]) or 0) - s) > TOL:
            f.append("WBS TOTAL %s is %r, expected %.4f" % (k, tot[0][col[k] - 1], s))
    return f


def g_criteria(ctx):
    cfg, f = ctx["cfg"], []
    C = cfg["criteria"]
    tasks, subs, _, _ = ctx["td"]
    subs_by = {}
    for s in subs:
        subs_by.setdefault(parent_of(cfg, s["task_id"]), []).append(s)
    for tid, d in tasks.items():
        if d["status"] != cfg["statuses"]["in_scope"]:
            continue
        eff = fnum(d["effort"])
        if eff is None:
            continue
        lines = numbered_lines(d["criteria"])
        if eff <= C["over_days"]:
            if not lines:
                f.append("%s: in scope, effort %.2f, has no acceptance criteria" % (tid, eff))
            continue
        if not (C["min"] <= len(lines) <= C["max"]):
            f.append("%s: effort %.2f needs %d to %d criteria, has %d" % (tid, eff, C["min"], C["max"], len(lines)))
        ss = subs_by.get(tid, [])
        if not ss:
            f.append("%s: effort %.2f has no sub-tasks" % (tid, eff))
            continue
        tot = sum(fnum(s["subtask_days"]) or 0 for s in ss)
        if abs(tot - eff) > 0.001:
            f.append("%s: sub-task days sum to %.3f, effort is %.2f" % (tid, tot, eff))
    step = float(C["subtask_step"])
    for s in subs:
        days = fnum(s["subtask_days"])
        if days is None:
            f.append("%s: sub-task has no days" % s["task_id"])
            continue
        if days > C["subtask_max_days"]:
            f.append("%s: sub-task %.2f days is over %s" % (s["task_id"], days, C["subtask_max_days"]))
        if abs(days / step - round(days / step)) > 1e-9:
            f.append("%s: sub-task days %s are not a multiple of %s" % (s["task_id"], days, step))
    return f


def g_stories(ctx):
    cfg, E, f = ctx["cfg"], ctx["E"], []
    col = cfg["_col"]["stories"]
    rows = sheet_rows(ctx["wbv"][cfg["_sheet_name"]["stories"]])
    got = {str(r[col["us_id"] - 1]): r for r in rows[1:] if r and r[col["us_id"] - 1]}
    verbatim = cfg["stories"]["verbatim_origin"]
    for st in E["stories"]:
        r = got.get(st["us_id"])
        if r is None:
            f.append("User Stories: %s is missing" % st["us_id"])
            continue
        want_text = st["title"] + ("\n" + st["story"] if st["story"] else "")
        if str(r[col["story"] - 1] or "").strip() != want_text.strip():
            f.append("%s: story text differs from the input" % st["us_id"])
        if str(r[col["wbs_ids"] - 1] or "") != ", ".join(st["wbs"]):
            f.append("%s: WBS IDs %r, expected %r" % (st["us_id"], r[col["wbs_ids"] - 1], ", ".join(st["wbs"])))
        exp_acs = st["acs"]
        if verbatim and st["origin"] == verbatim and st["us_id"] in E["src_by"]:
            exp_acs = [str(x) for x in E["src_by"][st["us_id"]]["acs"]]
            if st["acs"] and st["acs"] != exp_acs:
                f.append("%s: input criteria differ from the story source file (these are verbatim)" % st["us_id"])
        if (r[col["criteria"] - 1] or "").strip() != (numbered(exp_acs) or "").strip():
            f.append("%s: acceptance criteria differ from the input" % st["us_id"])
        for w in st["wbs"]:
            if w not in E["rows"]:
                f.append("%s: WBS ID %s does not exist" % (st["us_id"], w))
    covered = {w for st in E["stories"] for w in st["wbs"]}
    eff_by = {}
    for t in ctx["td"][0].values():
        if t["status"] == cfg["statuses"]["in_scope"] and t["owner"] == cfg["owners"]["ours"] and t["wbs_id"]:
            eff_by[t["wbs_id"]] = eff_by.get(t["wbs_id"], 0) + (fnum(t["effort"]) or 0)
    prefixes = tuple(cfg["stories"]["required_row_prefixes"] or [])
    for rid in E["rows_order"]:
        if prefixes and rid.startswith(prefixes) and eff_by.get(rid, 0) > 0 and rid not in covered:
            f.append("WBS %s has effort of ours but no user story" % rid)
    return f


def g_deps(ctx):
    cfg, E, f = ctx["cfg"], ctx["E"], []
    col = cfg["_col"]["dependencies"]
    rows = sheet_rows(ctx["wbv"][cfg["_sheet_name"]["dependencies"]])
    got = {str(r[col["id"] - 1]): r for r in rows[1:] if r and r[col["id"] - 1]}
    for d in E["deps"]:
        did = str(d["id"])
        r = got.get(did)
        if r is None:
            f.append("Dependency: %s is missing" % did)
            continue
        if d.get("from") not in cfg["dependencies"]["from"]:
            f.append("%s: from %r is not one of %s" % (did, d.get("from"), cfg["dependencies"]["from"]))
        if d.get("status") not in cfg["dependencies"]["status"]:
            f.append("%s: status %r is not one of %s" % (did, d.get("status"), cfg["dependencies"]["status"]))
        blocks = d.get("blocks") or []
        if isinstance(blocks, str):
            blocks = [x.strip() for x in blocks.split(",")]
        for w in blocks:
            if str(w) not in E["rows"]:
                f.append("%s: blocks unknown WBS row %s" % (did, w))
        cell = str(r[col["blocks"] - 1] or "")
        if cell != ", ".join(str(w) for w in blocks) and "more:" not in cell:
            f.append("%s: Blocks cell %r does not match the input" % (did, cell))
        if blank(r[col["if_late"] - 1]):
            f.append("%s: If late is empty" % did)
        if not str(d.get("source") or "").strip():
            f.append("%s: no source" % did)
    return f


def g_references(ctx):
    cfg, E, f = ctx["cfg"], ctx["E"], []
    refs = ctx["refs"]
    for rec in E["recs"] + E["options"]:
        if rec["id"] not in refs:
            f.append("References: no entry for %s" % rec["id"])
        elif rec["kind"] == "plan" and cfg["texts"]["ref_plan"].format(id=rec["id"]) not in refs[rec["id"]]:
            f.append("References: %s does not cite its plan row" % rec["id"])
    for rid in E["rows_order"]:
        if rid not in refs:
            f.append("References: no entry for WBS row %s" % rid)
    for i, a in enumerate(E["assumptions"], 1):
        if not any(k.startswith("#%d " % i) or k == "#%d" % i for k in refs):
            f.append("References: no entry for assumption #%d" % i)
    for d in E["deps"]:
        if str(d["id"]) not in refs:
            f.append("References: no entry for %s" % d["id"])
    for st in E["stories"]:
        if st["us_id"] not in refs:
            f.append("References: no entry for story %s" % st["us_id"])
    col = cfg["_col"]["references"]
    terms = {str(r[col["item"] - 1]) for r in sheet_rows(ctx["wbv"][cfg["_sheet_name"]["references"]])[1:]
             if r and r[col["kind"] - 1] == "Glossary"}
    for g in E["glossary"]:
        if g["term"] not in terms:
            f.append("References: glossary term %s is missing" % g["term"])
    return f


def shown_cells(ctx):
    for name in ctx["cfg"]["_shown"]:
        for row in ctx["wbv"][name].iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value:
                    yield name, c, c.value


def g_length(ctx):
    cfg, f = ctx["cfg"], []
    cap, sub_cap = cfg["text"]["cap"], cfg["text"]["subtask_name_cap"]
    N = cfg["_sheet_name"]
    wcol, tcol, scol = cfg["_col"]["wbs"], cfg["_col"]["task_detail"], cfg["_col"]["stories"]
    verbatim = {st["us_id"] for st in ctx["E"]["stories"]
                if cfg["stories"]["verbatim_origin"] and st["origin"] == cfg["stories"]["verbatim_origin"]}
    for name, c, v in shown_cells(ctx):
        ws = ctx["wbv"][name]
        if name == N["wbs"] and c.column == wcol.get("acceptance"):
            lines = v.split("\n")
        elif name == N["task_detail"] and c.column == tcol["criteria"]:
            lines = numbered_lines(v)
        elif name == N["stories"] and c.column == scol["story"]:
            lines = v.split("\n")
        elif name == N["stories"] and c.column == scol["criteria"]:
            if str(ws.cell(c.row, scol["us_id"]).value or "") in verbatim:
                continue  # verbatim criteria from the story source are not capped
            lines = numbered_lines(v)
        elif name == N["task_detail"] and c.column == tcol["task"] and \
                ws.cell(c.row, tcol["row_type"]).value == cfg["texts"]["row_type_sub"]:
            if len(v) > sub_cap:
                f.append("%s!%s: sub-task name is %d characters; limit %d" % (name, c.coordinate, len(v), sub_cap))
            continue
        else:
            lines = [v]
        for ln in lines:
            if len(ln) > cap:
                f.append("%s!%s: %d characters; limit %d" % (name, c.coordinate, len(ln), cap))
                break
    return f


def g_diacritics(ctx):
    if not ctx["cfg"]["text"]["forbid_diacritics"]:
        return []
    return ["%s!%s has accented Vietnamese letters: %s" % (n, c.coordinate, v[:60])
            for n, c, v in shown_cells(ctx) if VIET.search(v)]


def g_names(ctx):
    """No person's name, no mention of the excluded owner, and no source citation on a shown sheet."""
    cfg, E, f = ctx["cfg"], ctx["E"], []
    names = cfg["text"]["person_names"] or []
    pat = re.compile(r"(?<![\w])(%s)(?![\w])" % "|".join(re.escape(x) for x in names)) if names else None
    excl = cfg["owners"]["excluded"]
    internal = [re.compile(p) for p in (cfg["text"]["internal_source_patterns"] or [])]
    for name, c, v in shown_cells(ctx):
        m = pat.search(v) if pat else None
        if m:
            f.append("%s!%s shows the name '%s': %s" % (name, c.coordinate, m.group(0), v[:60]))
        if excl and re.search(r"(?<![\w])%s(?![\w])" % re.escape(excl), v):
            f.append("%s!%s mentions %s, whose work is not shown: %s" % (name, c.coordinate, excl, v[:60]))
        for p in internal:
            m = p.search(v)
            if m:
                f.append("%s!%s cites an internal source ('%s'), which belongs on the internal sheet: %s"
                         % (name, c.coordinate, m.group(0), v[:60]))
                break
    return f


def g_acceptance(ctx):
    cfg, f = ctx["cfg"], []
    clause, trig = cfg["criteria"]["clause"], cfg["criteria"]["clause_trigger"]
    if not clause or not trig:
        return []
    trig = re.compile(trig)
    N = cfg["_sheet_name"]
    for name, c, v in shown_cells(ctx):
        if name == N["wbs"] and c.column == cfg["_col"]["wbs"].get("acceptance"):
            lines = v.split("\n")
        elif name == N["task_detail"] and c.column == cfg["_col"]["task_detail"]["criteria"]:
            lines = numbered_lines(v)
        else:
            continue
        for ln in lines:
            if trig.search(ln) and not ln.rstrip(". ").endswith(clause.rstrip(".")):
                f.append("%s!%s has a %% or time target without the test-method clause: %s"
                         % (name, c.coordinate, ln[:70]))
    return f


def cell_rgb(c):
    if c.fill is None or c.fill.fill_type != "solid":
        return None
    return str(c.fill.start_color.rgb)[-6:].upper()


def g_marking(ctx):
    """Proposals carry the prefix and the proposal fill; nothing else carries that fill; one legend."""
    cfg, E, f = ctx["cfg"], ctx["E"], []
    M = cfg["marking"]
    prop = wc.rgb(M["fills"]["proposal"])[-6:]
    ws = ctx["wbf"][cfg["_sheet_name"]["task_detail"]]
    col = cfg["_col"]["task_detail"]
    want = {tid for tid, _ in proposal_items(E)} & {r["id"] for r in E["recs"]}
    seen = set()
    for r in range(2, ws.max_row + 1):
        tid = ws.cell(r, col["task_id"]).value
        if tid is None:
            continue
        note = str(ws.cell(r, col["note"]).value or "")
        filled = cell_rgb(ws.cell(r, col["effort"])) == prop
        has_prefix = note.startswith(M["proposal_prefix"])
        if tid in want:
            seen.add(tid)
            if not filled:
                f.append("Task Detail %s is a proposed change but its effort cell lacks the proposal fill" % tid)
            if not has_prefix:
                f.append("Task Detail %s is a proposed change but its note lacks '%s'" % (tid, M["proposal_prefix"]))
        else:
            if filled:
                f.append("Task Detail %s carries the proposal fill but is not a proposed change" % tid)
            if has_prefix:
                f.append("Task Detail %s note starts with '%s' but is not in the proposals file"
                         % (tid, M["proposal_prefix"]))
    for tid in sorted(want - seen):
        f.append("proposed change %s is not in Task Detail" % tid)
    for wsf in ctx["wbf"].worksheets:
        if wsf.title in (ws.title, cfg["_sheet_name"][M["legend_sheet"]]):
            continue
        for row in wsf.iter_rows():
            for c in row:
                if cell_rgb(c) == prop:
                    f.append("%s!%s carries the proposal fill outside Task Detail" % (wsf.title, c.coordinate))
    lg = ctx["wbf"][cfg["_sheet_name"][M["legend_sheet"]]]
    legend = {}
    for row in lg.iter_rows():
        if row and row[0].value == M["legend_kind"] and len(row) > 2:
            legend[cell_rgb(row[1])] = row[2].value
    for item in M["legend"]:
        rgb = wc.rgb(M["fills"][item["fill"]])[-6:]
        if blank(legend.get(rgb)):
            f.append("colour legend on %s has no entry for the %s fill (%s)" % (lg.title, item["fill"], rgb))
    for key in ("fill_in", "proposal"):
        rgb = wc.rgb(M["fills"][key])[-6:]
        if rgb not in legend:
            f.append("colour legend does not explain the %s fill" % key)
    return f


GROUP_FN = {"structure": g_structure, "master inputs": g_master, "cached values": g_cached,
            "task detail rows": g_task_rows, "effort rule": g_effort_rule, "proposals": g_proposals,
            "sources": g_sources, "removals": g_removals, "live formulas": g_formulas,
            "effort summary": g_effort_summary, "base total": g_base, "reference check": g_reference,
            "wbs sums": g_wbs, "criteria coverage": g_criteria, "stories": g_stories, "dependencies": g_deps,
            "references": g_references, "text length": g_length, "diacritics": g_diacritics,
            "person names and sources": g_names, "acceptance clause": g_acceptance,
            "proposal marking": g_marking}


def warn_version(path, wb):
    """WARNING only: the file name and the first sheet should carry a version number and a date."""
    out = []
    ver, date = re.compile(r"v\d+(\.\d+)*", re.I), re.compile(r"\d{4}-\d{2}-\d{2}")
    base = os.path.basename(path)
    if not ver.search(base):
        out.append("file name %r carries no version number" % base)
    if not date.search(base):
        out.append("file name %r carries no date (YYYY-MM-DD)" % base)
    first = wb.worksheets[0]
    text = " ".join(str(c.value) for row in first.iter_rows() for c in row if isinstance(c.value, str))
    if not re.search(r"\bversion\b\s*\S+|\bv\d", text, re.I):
        out.append("first sheet %r carries no version number" % first.title)
    if not date.search(text):
        out.append("first sheet %r carries no date (YYYY-MM-DD)" % first.title)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx")
    ap.add_argument("--project", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--plan-total", type=float, help="override plan.total from project.yaml")
    ap.add_argument("--max-lines", type=int, default=12)
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        cfg = wc.load_project(args.project)
        E = build_expected(cfg, args.data)
    except wc.BadInput as e:
        print("ERROR: %s" % e, file=sys.stderr)
        return 2
    except (KeyError, TypeError, AttributeError) as e:
        print("ERROR: the data cannot be read against the settings: %s: %s" % (type(e).__name__, e),
              file=sys.stderr)
        return 2
    wbf = openpyxl.load_workbook(args.xlsx)
    wbv = openpyxl.load_workbook(args.xlsx, data_only=True)
    ctx = {"cfg": cfg, "E": E, "wbf": wbf, "wbv": wbv,
           "plan_total": args.plan_total if args.plan_total is not None else float(cfg["plan"]["total"]),
           "PM": master_value(cfg, "PM_PCT"), "CONT": master_value(cfg, "CONT_PCT"),
           "MD": master_value(cfg, "MD_MONTH"), "RATE": master_value(cfg, "RATE")}
    missing = [n for n in cfg["_sheet_order"] if n not in wbv.sheetnames]
    if missing:
        print("FAIL structure: sheets missing: %s" % ", ".join(missing))
        print("RESULT: FAIL")
        return 1
    ctx["td"] = read_td(cfg, sheet_rows(wbv[cfg["_sheet_name"]["task_detail"]]))
    ctx["refs"] = load_refs(cfg, wbv)
    failed = []
    for g in GROUPS:
        try:
            fails = GROUP_FN[g](ctx)
        except Exception as e:  # a crash is a failure of that group, reported with its cause
            fails = ["group crashed: %s: %s" % (type(e).__name__, e)]
        if fails:
            failed.append(g)
            print("FAIL %s (%d)" % (g, len(fails)))
            for x in fails[:args.max_lines]:
                print("   - %s" % x)
            if len(fails) > args.max_lines:
                print("   ... %d more" % (len(fails) - args.max_lines))
        else:
            print("PASS %s" % g)
    for w in warn_version(args.xlsx, wbf):
        print("WARNING version stamp: %s" % w)
    if "yaml_total" in ctx:
        tot, eff, dev = ctx["yaml_total"]
        print("Base total recomputed from the YAML: %.4f  (effort %.4f, dev %.4f)" % (tot, eff, dev))
    if failed:
        print("RESULT: FAIL (%d of %d groups): %s" % (len(failed), len(GROUPS), ", ".join(failed)))
        return 1
    print("RESULT: PASS (%d groups)" % len(GROUPS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
