#!/usr/bin/env python3
"""Build a WBS workbook from YAML data and a project settings file.

    python build.py --project project.yaml --data DATA_DIR [--out FILE.xlsx] [--plan-total N] [--recalc]

project.yaml holds everything specific to one project: sheet names and order, columns, roles, owners,
status labels, the effort rule, the plan total to reproduce, text caps and the marking colours.
The data folder holds the plan's tasks and the changes to them (see SCHEMA.md).

Exit 0 when the workbook is written. Exit 2, with a message on stderr, when project.yaml or a data file is
malformed or inconsistent (missing source on a removal, unknown IDs, unknown roles). Content problems such
as a missing criterion, a broken effort rule or a text over the cap are written as they are, and verify.py
reports them. Totals are live formulas; --recalc runs LibreOffice so the file carries cached values.
"""
import argparse
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wbs_common as wc  # noqa: E402
from wbs_common import BadInput, bad  # noqa: E402

WRAP = Alignment(wrap_text=True, vertical="top")
NUM_D = "0.00##"
NUM_TOT = "#,##0.0000"


def is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def as_list(v):
    if v is None:
        return []
    if isinstance(v, str):
        return [x.strip() for x in v.split(",") if x.strip()]
    return [str(x).strip() for x in v]


def fill(cfg, key):
    c = wc.rgb(cfg["marking"]["fills"][key])
    return PatternFill("solid", start_color=c, end_color=c)


# ------------------------------------------------------------------ model
def read_model(cfg, data_dir):
    """Validate every input and return the rows to write. Raises BadInput on a structural problem."""
    files = cfg["data"]["files"]
    st_cfg = cfg["statuses"]
    IN_SCOPE = st_cfg["in_scope"]
    OWNERS = cfg["owners"]["all"]
    OURS = cfg["owners"]["ours"]
    ROLES = cfg["roles"]["known"]
    CHANGE = st_cfg["change"]
    ADD = st_cfg["add"]
    T = cfg["texts"]
    nparts = int(cfg["data"]["feature_key_parts"])

    plan = wc.load_data(cfg, data_dir, "plan_tasks")
    tasks = plan.get("tasks") if isinstance(plan, dict) else None
    if not tasks:
        bad("%s has no tasks list" % files["plan_tasks"])
    options = plan.get("options") or []

    fdoc = wc.load_data(cfg, data_dir, "feature_map")
    if not isinstance(fdoc, dict) or not fdoc.get("rows") or not fdoc.get("map"):
        bad("%s needs non-empty rows and map lists" % files["feature_map"])
    cdoc = wc.load_data(cfg, data_dir, "changes")
    if not isinstance(cdoc, dict):
        bad("%s is empty or not a mapping" % files["changes"])
    pdoc = wc.load_data(cfg, data_dir, "proposals", required=False, default={}) or {}
    if not isinstance(pdoc, dict):
        bad("%s must be a mapping with change and add lists" % files["proposals"])
    assumptions = wc.load_data(cfg, data_dir, "assumptions", required=False, default=[]) or []
    deps = wc.load_data(cfg, data_dir, "dependencies", required=False, default=[]) or []
    glossary = wc.load_data(cfg, data_dir, "glossary", required=False, default=[]) or []
    stories_doc = wc.load_data(cfg, data_dir, "stories", required=False, default=None)
    srcdoc = wc.load_data(cfg, data_dir, "story_source", required=False, default={}) or {}
    for key, lst in (("assumptions", assumptions), ("dependencies", deps), ("glossary", glossary)):
        if not isinstance(lst, list):
            bad("%s must be a list" % files[key])

    fm = files["feature_map"]
    rows = {}
    for r in fdoc["rows"]:
        rid = str(r.get("id") or "")
        if not rid:
            bad("%s: a row has no id" % fm)
        if rid in rows:
            bad("%s: WBS row %s is listed twice" % (fm, rid))
        for k in cfg["wbs_required_fields"]:
            if not r.get(k):
                bad("%s: WBS row %s has no %s" % (fm, rid, k))
        if r.get("owner") not in OWNERS:
            bad("%s: WBS row %s has owner %r (must be one of %s)" % (fm, rid, r.get("owner"), ", ".join(OWNERS)))
        rows[rid] = r

    fmap = {}
    for m in fdoc["map"]:
        pf = str(m.get("plan_feature") or "")
        if pf in fmap:
            bad("%s: feature %s is mapped twice" % (fm, pf))
        if str(m.get("wbs_id")) not in rows:
            bad("%s: feature %s maps to unknown WBS row %r" % (fm, pf, m.get("wbs_id")))
        fmap[pf] = m
    tmap = {}
    for o in fdoc.get("task_map") or []:
        tid = str(o.get("task_id") or "")
        if tid in tmap:
            bad("%s task_map: %s listed twice" % (fm, tid))
        if str(o.get("wbs_id")) not in rows:
            bad("%s task_map: %s maps to unknown WBS row %r" % (fm, tid, o.get("wbs_id")))
        tmap[tid] = str(o["wbs_id"])

    pt = files["plan_tasks"]
    task_ids, overhead_ids, recs = set(), set(), []
    for t in tasks:
        pid = str(t.get("task_id") or "")
        if not pid:
            bad("%s: a task has no id" % pt)
        if pid in task_ids:
            bad("%s: task id %s appears twice" % (pt, pid))
        task_ids.add(pid)
        if not is_number(t.get("effort")):
            bad("%s: task %s has no effort number" % (pt, pid))
        overhead = t.get("phase") == cfg["plan"]["overhead_phase"]
        if overhead:
            overhead_ids.add(pid)
        elif t.get("role") not in ROLES:
            bad("%s: task %s has unknown role %r" % (pt, pid, t.get("role")))
        parts = pid.split(".")
        if len(parts) <= nparts:
            bad("%s: task id %s has %d parts or fewer" % (pt, pid, nparts))
        feat = ".".join(parts[:nparts])
        if feat not in fmap:
            bad("plan feature %s (task %s) is not in %s" % (feat, pid, fm))
        recs.append({
            "kind": "overhead" if overhead else "plan", "id": pid,
            "wbs": tmap.get(pid, str(fmap[feat]["wbs_id"])), "overhead": overhead,
            "section": t.get("sheet") or "", "module": t.get("module") or "", "task": t.get("task") or "",
            "basis": t.get("basis") or "", "role": t.get("role") or None,
            "dev": t.get("dev"), "qc": t.get("qc"), "ba": t.get("ba"), "effort": t.get("effort"),
            "dod": t.get("dod") or None,
            "status": st_cfg["overhead"] if overhead else IN_SCOPE,
            "owner": OURS, "note": None, "proposal": False, "orig": None,
            "source": T["source_plan"].format(id=pid), "extra_source": None,
        })
    for tid in tmap:
        if tid not in task_ids:
            bad("%s task_map: unknown plan task %s" % (fm, tid))

    by_id = {r["id"]: r for r in recs}

    ch = files["changes"]
    status_by = {}
    for s in cdoc.get("status") or []:
        pid = str(s.get("task_id") or "")
        if pid not in task_ids:
            bad("%s status: unknown task id %r" % (ch, pid))
        if pid in status_by:
            bad("%s status: task %s is listed twice" % (ch, pid))
        if pid in overhead_ids:
            bad("%s status: %s is an overhead row; overhead is recomputed, not changed" % (ch, pid))
        st = s.get("status")
        if st not in CHANGE:
            bad("%s status for %s: bad status %r" % (ch, pid, st))
        if s.get("owner") not in OWNERS:
            bad("%s status for %s: bad owner %r" % (ch, pid, s.get("owner")))
        if st in st_cfg["needs_source"]:
            if not str(s.get("source") or "").strip():
                bad("%s status for %s: %s has no source" % (ch, pid, st))
            if not str(s.get("reason") or "").strip():
                bad("%s status for %s: %s has no reason" % (ch, pid, st))
        status_by[pid] = s
    for rec in recs:
        c = status_by.get(rec["id"])
        if c and rec["kind"] == "plan":
            rec["status"] = CHANGE[c["status"]]
            rec["owner"] = c["owner"]
            rec["note"] = str(c.get("reason") or "").strip() or None
            rec["extra_source"] = str(c.get("source") or "").strip() or None

    def make_add(a, fname, prefix):
        aid = str(a.get("id") or "")
        if not aid:
            bad("%s add: a row has no id" % fname)
        if aid in by_id:
            bad("%s add: id %s is already used" % (fname, aid))
        if prefix and not aid.startswith(prefix):
            bad("%s add: id %s does not start with %s" % (fname, aid, prefix))
        wbs = str(a.get("wbs_id") or "")
        if wbs not in rows:
            bad("%s add %s: unknown wbs_id %r" % (fname, aid, a.get("wbs_id")))
        if a.get("status") not in ADD:
            bad("%s add %s: bad status %r (must be one of %s)" % (fname, aid, a.get("status"), ", ".join(ADD)))
        if not is_number(a.get("effort")):
            bad("%s add %s has no effort number" % (fname, aid))
        for k in ("dev", "qc", "ba"):
            if a.get(k) is not None and not is_number(a.get(k)):
                bad("%s add %s: %s is not a number" % (fname, aid, k))
        if a.get("role") not in ROLES:
            bad("%s add %s: unknown role %r" % (fname, aid, a.get("role")))
        rec = {
            "kind": "add", "id": aid, "wbs": wbs, "overhead": False,
            "section": T["section_added"], "module": rows[wbs].get("module") or "", "task": a.get("task") or "",
            "basis": a.get("basis") or "", "role": a["role"],
            "dev": a.get("dev"), "qc": a.get("qc"), "ba": a.get("ba"), "effort": a["effort"],
            "dod": a.get("dod") or None, "highlight": bool(a.get("highlight")),
            "status": ADD[a["status"]], "owner": rows[wbs]["owner"],
            "note": None, "proposal": False, "orig": None,
            "source": str(a.get("source") or "").strip() or None, "extra_source": None,
        }
        by_id[aid] = rec
        recs.append(rec)
        return rec

    for a in cdoc.get("add") or []:
        rec = make_add(a, ch, cfg["ids"]["change_add_prefix"])
        if not rec["source"]:
            bad("%s add %s has no source" % (ch, rec["id"]))
        rec["note"] = T["note_highlight"] if rec.get("highlight") else T["note_added"]

    pf = files["proposals"]
    seen = set()
    for c in pdoc.get("change") or []:
        tid = str(c.get("task_id") or "")
        rec = by_id.get(tid)
        if rec is None:
            bad("%s change: unknown task %r" % (pf, tid))
        if rec["overhead"]:
            bad("%s change: %s is an overhead row" % (pf, tid))
        if tid in seen:
            bad("%s change: task %s is listed twice" % (pf, tid))
        if tid in status_by and status_by[tid]["status"] in st_cfg["out_of_scope"]:
            bad("%s change: %s is out of scope in %s; it cannot also be changed" % (pf, tid, ch))
        seen.add(tid)
        if not is_number(c.get("effort")):
            bad("%s change %s: effort is not a number" % (pf, tid))
        for k in ("dev", "qc", "ba"):
            if c.get(k) is not None and not is_number(c.get(k)):
                bad("%s change %s: %s is not a number" % (pf, tid, k))
        rec["orig"] = {"dev": rec["dev"], "qc": rec["qc"], "ba": rec["ba"], "effort": rec["effort"]}
        for k in ("dev", "qc", "ba", "effort"):
            rec[k] = c.get(k)
        if c.get("task"):
            rec["task"] = str(c["task"]).strip()
        rec["proposal"] = True
        rec["note"] = str(c.get("reason") or "").strip() or None
        rec["extra_source"] = str(c.get("source") or "").strip() or None

    for a in pdoc.get("add") or []:
        rec = make_add(a, pf, cfg["ids"]["proposal_add_prefix"])
        rec["proposal"] = True
        rec["note"] = str(a.get("reason") or "").strip() or None
        rec["extra_source"] = str(a.get("source") or "").strip() or None

    for i, o in enumerate(options, 1):
        if o.get("role") in cfg["owners"]["excluded_option_roles"]:
            continue
        recs.append({
            "kind": "option", "id": "%s%d" % (cfg["ids"]["option_prefix"], i), "wbs": "", "overhead": False,
            "section": T["section_option"], "module": o.get("option") or "", "task": o.get("task") or "",
            "basis": "", "role": o.get("role") or None,
            "dev": o.get("dev"), "qc": o.get("qc"), "ba": o.get("ba"), "effort": o.get("effort"),
            "dod": None, "status": st_cfg["option"], "owner": OURS,
            "note": T["note_option"], "proposal": False, "orig": None,
            "source": T["source_option"].format(section=o.get("section") or ""), "extra_source": None,
        })

    for rec in recs:
        if rec["kind"] in ("plan", "add") and not rec["overhead"]:
            if rec["status"] == IN_SCOPE and rec["owner"] == OURS and rec["role"] not in ROLES:
                bad("task %s has unknown role %r" % (rec["id"], rec["role"]))
        if rec["kind"] != "option" and rec["wbs"] not in rows:
            bad("task %s maps to unknown WBS row %r" % (rec["id"], rec["wbs"]))

    task_ac = {}
    for name in wc.criteria_files(cfg, data_dir):
        doc = wc.load_data(cfg, data_dir, name=name)
        items = (doc.get("tasks") if isinstance(doc, dict) else None) or []
        for t in items:
            tid = str(t.get("task_id") or "")
            if tid in task_ac:
                bad("%s: task %s is listed twice across the criteria files" % (name, tid))
            if tid not in by_id or by_id[tid]["kind"] == "option":
                bad("%s: unknown task %r" % (name, tid))
            subs = []
            for s in t.get("subtasks") or []:
                if not str(s.get("name") or "").strip() or not is_number(s.get("days")):
                    bad("%s: task %s has a sub-task without a name or days" % (name, tid))
                subs.append({"name": str(s["name"]).strip(), "days": s["days"]})
            task_ac[tid] = {"subtasks": subs, "acs": [str(x).strip() for x in (t.get("acs") or [])]}

    origins = cfg["stories"]["origins"]
    if stories_doc is not None:
        items = (stories_doc.get("stories") if isinstance(stories_doc, dict) else None) or []
        src_default = None
    else:
        items = srcdoc.get("stories") or []
        src_default = cfg["stories"]["fallback_source"]
    stories, seen_us = [], set()
    for s in items:
        us = str(s.get("us_id") or "")
        if not us or us in seen_us:
            bad("stories: story id %r missing or listed twice" % us)
        seen_us.add(us)
        origin = s.get("origin") or cfg["stories"]["default_origin"]
        if origin not in origins:
            bad("stories: %s has origin %r (must be one of %s)" % (us, origin, ", ".join(origins)))
        ids = as_list(s.get("wbs_ids"))
        if not ids:
            bad("stories: %s maps to no WBS row" % us)
        for w in ids:
            if w not in rows:
                bad("stories: %s maps to unknown WBS row %r" % (us, w))
        stories.append({
            "us_id": us, "title": str(s.get("title") or "").strip(),
            "story": str(s.get("story") or "").strip() or None,
            "acs": [str(x).strip() for x in (s.get("acs") or [])],
            "wbs_ids": ids, "origin": origin, "note": str(s.get("note") or "").strip() or None,
            "source": str(s.get("source") or src_default or "").strip() or None,
            "reason": str(s.get("reason") or "").strip() or None,
        })

    df = files["dependencies"]
    dep_ids, deps_out = set(), []
    for p in deps:
        did = str(p.get("id") or "")
        if not did or did in dep_ids:
            bad("%s: id %r missing or listed twice" % (df, did))
        dep_ids.add(did)
        if p.get("from") not in cfg["dependencies"]["from"]:
            bad("%s: %s from must be one of %s, not %r" % (df, did, ", ".join(cfg["dependencies"]["from"]),
                                                          p.get("from")))
        if p.get("status") not in cfg["dependencies"]["status"]:
            bad("%s: %s status must be one of %s" % (df, did, ", ".join(cfg["dependencies"]["status"])))
        blocks = as_list(p.get("blocks"))
        for w in blocks:
            if w not in rows:
                bad("%s: %s blocks unknown WBS row %r" % (df, did, w))
        deps_out.append({"id": did, "item": str(p.get("item") or "").strip(), "from": p["from"],
                         "needed_by": str(p.get("needed_by") or "").strip(), "blocks": blocks,
                         "status": p["status"], "if_late": str(p.get("if_late") or "").strip(),
                         "source": str(p.get("source") or "").strip()})

    asm_out = []
    for a in assumptions:
        if not isinstance(a, dict) or not str(a.get("text") or "").strip():
            bad("%s: an item has no text" % files["assumptions"])
        asm_out.append({"category": str(a.get("category") or "").strip(),
                        "text": str(a["text"]).strip(), "source": str(a.get("source") or "").strip()})
    gl_out = []
    for g in glossary:
        if not isinstance(g, dict) or not g.get("term") or not g.get("meaning"):
            bad("%s: an item has no term or meaning" % files["glossary"])
        gl_out.append({"term": str(g["term"]).strip(), "meaning": str(g["meaning"]).strip()})

    recs_all = recs
    recs, rows, order = drop_owner(recs, rows, [str(r["id"]) for r in fdoc["rows"]], cfg)
    return {"recs": recs, "recs_all": recs_all, "rows": rows, "rows_order": order, "plan_tasks": tasks,
            "task_ac": task_ac, "stories": stories, "deps": deps_out, "assumptions": asm_out,
            "glossary": gl_out}


def drop_owner(recs, rows, order, cfg):
    """Remove the excluded owner's work: its tasks, and WBS rows left with no task of ours.
    A row of that owner that still carries our tasks becomes our row."""
    owner = cfg["owners"]["excluded"]
    if owner is None:
        return recs, rows, order
    kept = [r for r in recs if r["owner"] != owner]
    ours = {r["wbs"] for r in kept if r.get("wbs")}
    rows = dict(rows)
    for rid in list(order):
        if rows[rid]["owner"] == owner:
            if rid in ours:
                rows[rid] = dict(rows[rid], owner=cfg["owners"]["ours"])
            else:
                order.remove(rid)
                del rows[rid]
    return kept, rows, order


# ------------------------------------------------------------------ writing helpers
def write_cell(ws, row, col, value, fmt=None, wrap=True, bold=False, fill_=None, text=True):
    """Write a value. text=True keeps strings as text, even one starting with '='.
    Pass text=False only for formulas this script builds."""
    cell = ws.cell(row=row, column=col)
    if value is not None:
        cell.value = value
        if text and isinstance(value, str):
            cell.data_type = "s"
    if fmt:
        cell.number_format = fmt
    if wrap:
        cell.alignment = WRAP
    if bold:
        cell.font = Font(bold=True)
    if fill_ is not None:
        cell.fill = fill_
    return cell


def header(cfg, ws, names, row=1):
    for i, name in enumerate(names, 1):
        c = ws.cell(row=row, column=i, value=name)
        c.fill = fill(cfg, "header")
        c.font = Font(bold=True, color="FFFFFF")
        c.alignment = Alignment(wrap_text=True, vertical="center")


def sheet_setup(cfg, wb, key):
    """Header row and widths from columns.<key>; returns the worksheet."""
    ws = wb[cfg["_sheet_name"][key]]
    cols = cfg["columns"][key]
    header(cfg, ws, [c["header"] for c in cols])
    for i, c in enumerate(cols, 1):
        if c.get("width"):
            ws.column_dimensions[get_column_letter(i)].width = c["width"]
    ws.freeze_panes = (cfg.get("freeze") or {}).get(key, "A2")
    return ws


def numbered(lines):
    return "\n".join("%d. %s" % (i, t) for i, t in enumerate(lines, 1)) if lines else None


def cap_list(cfg, ids, label):
    """Comma list of IDs. If it would pass the text cap, cut it and say how many are left."""
    cap = cfg["text"]["cap"]
    tail_fmt = cfg["texts"]["cap_list_tail"]
    text = ", ".join(ids)
    if len(text) <= cap:
        return text or None
    kept = []
    for i in ids:
        tail = tail_fmt.format(n=len(ids) - len(kept) - 1, label=label)
        if len(", ".join(kept + [i])) + len(tail) > cap:
            break
        kept.append(i)
    return ", ".join(kept) + tail_fmt.format(n=len(ids) - len(kept), label=label)


def fmt_num(x):
    return "%g" % x if is_number(x) else "not given"


# ------------------------------------------------------------------ sheets
def build_master(cfg, wb):
    ws = wb[cfg["_sheet_name"]["master"]]
    header(cfg, ws, cfg["master"].get("headers") or ["Item", "Value", "Note"])
    for i, r in enumerate(cfg["master"]["rows"], 2):
        write_cell(ws, i, 1, r["label"])
        write_cell(ws, i, 2, r["value"], fmt=r.get("format"), fill_=fill(cfg, "input"))
        write_cell(ws, i, 3, r.get("note"))
        if r.get("name"):
            wb.defined_names[r["name"]] = DefinedName(r["name"], attr_text="%s!$B$%d"
                                                      % (quote_sheet(ws.title), i))
    for letter_, w in {"A": 34, "B": 14, "C": 70}.items():
        ws.column_dimensions[letter_].width = w
    ws.freeze_panes = "A2"


def quote_sheet(name):
    return name if name.replace("_", "").isalnum() else "'%s'" % name.replace("'", "''")


def criteria_for(rec, model):
    ac = model["task_ac"].get(rec["id"], {})
    if ac.get("acs"):
        return numbered(ac["acs"])
    return rec.get("dod")


def build_task_detail(cfg, wb, model):
    ws = sheet_setup(cfg, wb, "task_detail")
    col = cfg["_col"]["task_detail"]
    T = cfg["texts"]
    over_days = cfg["criteria"]["over_days"]
    hl_fill, pr_fill = fill(cfg, cfg["marking"]["highlight_fill"]), fill(cfg, "proposal")
    ncols = len(col)
    r = 2
    for rec in model["recs"]:
        effort = rec["effort"]
        vals = {"task_id": rec["id"], "row_type": T["row_type_task"], "wbs_id": rec["wbs"] or None,
                "section": rec["section"], "module": rec["module"], "task": rec["task"], "role": rec["role"],
                "dev": rec["dev"], "qc": rec["qc"], "ba": rec["ba"], "effort": effort, "subtask_days": None,
                "over_threshold": None if effort is None else ("Yes" if effort > over_days else "No"),
                "criteria": criteria_for(rec, model), "status": rec["status"], "owner": rec["owner"],
                "note": rec["note"]}
        write_row(ws, r, col, vals)
        row_fill = pr_fill if rec.get("proposal") else hl_fill if rec.get("highlight") else None
        if row_fill is not None:
            for c in range(1, ncols + 1):
                ws.cell(row=r, column=c).fill = row_fill
        r += 1
        for i, s in enumerate(model["task_ac"].get(rec["id"], {}).get("subtasks", []), 1):
            write_row(ws, r, col, {"task_id": "%s%s%d" % (rec["id"], cfg["ids"]["subtask_infix"], i),
                                   "row_type": T["row_type_sub"], "wbs_id": rec["wbs"] or None,
                                   "task": s["name"], "subtask_days": s["days"]})
            r += 1
    last = r - 1
    ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(ncols), last)
    return last


def write_row(ws, r, col, vals):
    for key, c in col.items():
        v = vals.get(key)
        fmt = NUM_D if key in ("dev", "qc", "ba", "effort", "subtask_days") else None
        write_cell(ws, r, c, v if v != "" else None, fmt=fmt)


def td_range(cfg, key, last):
    L = wc.letter(cfg, "task_detail", key)
    return "%s!$%s$2:$%s$%d" % (quote_sheet(cfg["_sheet_name"]["task_detail"]), L, L, last)


def base_pairs(cfg, status=None, owner=None):
    return [("row_type", '"%s"' % cfg["texts"]["row_type_task"]),
            ("status", '"%s"' % (status or cfg["statuses"]["in_scope"])),
            ("owner", '"%s"' % (owner or cfg["owners"]["ours"]))]


def sumifs(cfg, last, sum_key, pairs):
    return "SUMIFS(%s,%s)" % (td_range(cfg, sum_key, last),
                              ",".join("%s,%s" % (td_range(cfg, k, last), v) for k, v in pairs))


def build_wbs(cfg, wb, model, last):
    ws = sheet_setup(cfg, wb, "wbs")
    col = cfg["_col"]["wbs"]
    fields = {c["key"]: c.get("field", c["key"]) for c in cfg["columns"]["wbs"]}
    OURS, IN_SCOPE = cfg["owners"]["ours"], cfg["statuses"]["in_scope"]
    hl_fill = fill(cfg, cfg["marking"]["highlight_fill"])
    tot_fill = fill(cfg, "total")
    stories_by_wbs = {}
    for st in model["stories"]:
        for w in st["wbs_ids"]:
            stories_by_wbs.setdefault(w, []).append(st["us_id"])
    sums = ("dev", "qc", "ba", "effort")
    row_no = 2
    for rid in model["rows_order"]:
        r = model["rows"][rid]
        for key, c in col.items():
            if key == "index":
                write_cell(ws, row_no, c, "=ROW()-1", text=False)
            elif key == "id":
                write_cell(ws, row_no, c, rid)
            elif key in sums:
                pairs = [("wbs_id", "$%s%d" % (wc.letter(cfg, "wbs", "id"), row_no))] + base_pairs(cfg)
                write_cell(ws, row_no, c, "=" + sumifs(cfg, last, key, pairs), fmt=NUM_D, text=False)
            elif key == "owner":
                ours_here = any(t["wbs"] == rid and t["status"] == IN_SCOPE and t["owner"] == OURS
                                for t in model["recs"])
                own = r["owner"]
                write_cell(ws, row_no, c, own if own == OURS or not ours_here
                           else cfg["owners"]["shared_row_label"].format(owner=own))
            elif key == "stories":
                write_cell(ws, row_no, c, cap_list(cfg, stories_by_wbs.get(rid, []), cfg["texts"]["cap_label_stories"]))
            else:
                v = r.get(fields[key])
                write_cell(ws, row_no, c, v if v is None or isinstance(v, str) else str(v))
        if any(t["wbs"] == rid and t.get("highlight") for t in model["recs"]):
            for key in sums:
                ws.cell(row=row_no, column=col[key]).fill = hl_fill
        row_no += 1
    total = row_no
    write_cell(ws, total, col["id"], "TOTAL", bold=True, fill_=tot_fill)
    for key in sums:
        L = wc.letter(cfg, "wbs", key)
        write_cell(ws, total, col[key], "=SUM(%s2:%s%d)" % (L, L, total - 1), fmt=NUM_D, bold=True,
                   fill_=tot_fill, text=False)
    ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(len(col)), total - 1)


def bridge_lines(cfg, recs):
    """Steps from the plan's original effort to the base effort: label, days, note."""
    B = cfg["summary"]["bridge"]["labels"]
    IN_SCOPE, OURS, EXCL = cfg["statuses"]["in_scope"], cfg["owners"]["ours"], cfg["owners"]["excluded"]
    out = {}

    def add(key, v):
        out[key] = out.get(key, 0.0) + v
    for r in recs:
        if r["kind"] == "plan":
            orig = r["orig"].get("effort", r["effort"]) if r["orig"] else r["effort"]
            if r["status"] != IN_SCOPE:
                add(r["status"], -float(orig or 0))
            elif r["owner"] != OURS:
                add(B["excluded_owner"] if r["owner"] == EXCL else B["other_owner"].format(owner=r["owner"]),
                    -float(orig or 0))
            elif r["orig"]:
                add(B["proposal_change"], float(r["effort"] or 0) - float(orig or 0))
        elif r["kind"] == "add" and r["status"] == IN_SCOPE and r["owner"] == OURS:
            add(B["proposal_add"] if r["proposal"] else B["highlight_add"] if r.get("highlight")
                else B["scope_add"], float(r["effort"] or 0))
    note = cfg["summary"]["bridge"]["step_note"]
    return [(k, v, note) for k, v in out.items() if abs(v) > 1e-9]


def build_effort_summary(cfg, wb, model, last, plan_total):
    S_ = cfg["summary"]
    ws = wb[cfg["_sheet_name"]["summary"]]
    title_fill, sub_fill, block_fill = fill(cfg, "title"), fill(cfg, "subheader"), fill(cfg, "block")
    tot_fill, in_fill = fill(cfg, "total"), fill(cfg, "input")

    def S(sum_key, pairs):
        return sumifs(cfg, last, sum_key, pairs)

    def q(s):
        return '"%s"' % s

    BASE = base_pairs(cfg)

    def role_net(role):
        p = BASE + [("role", q(role))]
        return "(%s-%s-%s)" % (S("effort", p), S("qc", p), S("ba", p))

    ws.cell(row=1, column=1, value=S_["title"])
    for c in range(1, 7):
        ws.cell(row=1, column=c).fill = title_fill
    ws.cell(row=1, column=1).font = Font(bold=True, color="FFFFFF", size=16)
    for c, name in enumerate(S_["headers"], 1):
        cell = ws.cell(row=2, column=c, value=name)
        cell.fill = sub_fill
        cell.font = Font(bold=True, color="FFFFFF")
    state = {"r": 3}

    def title(text):
        r = state["r"]
        for c in range(1, 7):
            ws.cell(row=r, column=c).fill = block_fill
        write_cell(ws, r, 1, text, bold=True, fill_=block_fill)
        state["r"] += 1

    def line(spec, days, money=True, bold=False, fill_=None, italic=False, fmt=NUM_D):
        """spec: {label, note}. days: formula text (no '=') or a number. money: add MM, rate and cost."""
        r = state["r"]
        write_cell(ws, r, 1, spec["label"], bold=bold, fill_=fill_)
        d = write_cell(ws, r, 2, ("=" + days) if isinstance(days, str) else days, fmt=fmt, bold=bold,
                       fill_=fill_, text=False)
        if money:
            write_cell(ws, r, 3, "=B%d/MD_MONTH" % r, fmt="0.00", bold=bold, fill_=fill_, text=False)
            write_cell(ws, r, 4, "=RATE", fmt="#,##0", fill_=fill_, text=False)
            write_cell(ws, r, 5, "=C%d*D%d" % (r, r), fmt="#,##0", bold=bold, fill_=fill_, text=False)
        if italic:
            ws.cell(row=r, column=1).font = Font(italic=True)
            d.font = Font(italic=True)
        write_cell(ws, r, 6, spec.get("note") or "")
        state["r"] += 1
        return r

    def gap():
        state["r"] += 1

    # a. Base
    title(S_["base_title"])
    first = state["r"]
    for a in S_["activities"]:
        if a["kind"] == "role_plus_addon":
            f = S("effort", BASE + [("role", q(a["role"]))]) + "+" + S(a["addon"], BASE)
        else:
            f = "+".join(role_net(r) for r in a["roles"])
        line(a, f)
    last_act = state["r"] - 1
    eff = line(S_["subtotal"], "SUM(B%d:B%d)" % (first, last_act), bold=True)
    line(S_["check"], "B%d-%s" % (eff, S("effort", BASE)), money=False, italic=True, fmt=NUM_TOT)
    dev = line(S_["dev_memo"], S("dev", BASE), money=False, italic=True)
    pm = line(S_["pm"], "PM_PCT*B%d" % dev)
    sub = line(S_["sub"], "B%d+B%d" % (eff, pm), bold=True)
    cont = line(S_["contingency"], "CONT_PCT*B%d" % sub)
    line(S_["total"], "B%d+B%d" % (sub, cont), bold=True, fill_=tot_fill)
    gap()

    # b. Option statuses (outside the base total)
    OL = S_["option_lines"]
    for blk in S_["option_blocks"]:
        title(blk["title"])
        p = base_pairs(cfg, status=blk["status"])
        e = line(OL["effort"], S("effort", p), bold=True)
        d = line(OL["dev"], S("dev", p), money=False, italic=True)
        pmr = line(OL["pm"], "PM_PCT*B%d" % d)
        s2 = line(OL["sub"], "B%d+B%d" % (e, pmr))
        c2 = line(OL["contingency"], "CONT_PCT*B%d" % s2)
        line(OL["total"], "B%d+B%d" % (s2, c2), bold=True)
        gap()

    # c. Other owners (outside our total)
    if cfg["owners"]["other_owner_lines"]:
        title(S_["other_title"])
        for o in cfg["owners"]["other_owner_lines"]:
            line(o, S("effort", base_pairs(cfg, owner=o["owner"])), money=False)
        gap()

    # d. Check against the plan's original figures (all plan rows except overhead)
    P = S_["plan_check"]
    orig_eff = orig_dev = 0.0
    for t in model["plan_tasks"]:
        if t.get("phase") == cfg["plan"]["overhead_phase"]:
            continue
        orig_eff += float(t.get("effort") or 0)
        orig_dev += float(t.get("dev") or 0)
    title(P["title"])
    pe = line(P["effort"], round(orig_eff, 6), money=False)
    pdv = line(P["dev"], round(orig_dev, 6), money=False)
    ppm = line(P["pm"], "PM_PCT*B%d" % pdv, money=False)
    psub = line(P["sub"], "B%d+B%d" % (pe, ppm), money=False)
    pcont = line(P["contingency"], "CONT_PCT*B%d" % psub, money=False)
    ptot = line(P["total"], "B%d+B%d" % (psub, pcont), money=False, bold=True)
    pfig = line(P["reference"], plan_total, money=False, fill_=in_fill, fmt=NUM_TOT)
    line(P["difference"], "B%d-B%d" % (ptot, pfig), money=False, fmt=NUM_TOT)
    gap()

    # e. Bridge: the plan's effort to this estimate's base effort
    BR = S_["bridge"]
    title(BR["title"])
    first_b = state["r"]
    line(BR["start"], "B%d" % pe, money=False)
    for label, val, note in bridge_lines(cfg, model["recs_all"]):
        line({"label": label, "note": note}, round(val, 6), money=False)
    end_b = line(BR["end"], "SUM(B%d:B%d)" % (first_b, state["r"] - 1), money=False, bold=True)
    line(BR["difference"], "B%d-B%d" % (end_b, eff), money=False, fmt=NUM_TOT)
    gap()

    title(S_["notes_title"])
    for n in S_["notes"]:
        write_cell(ws, state["r"], 1, n)
        state["r"] += 1
    for letter_, w in {"A": 60, "B": 14, "C": 13, "D": 18, "E": 14, "F": 56}.items():
        ws.column_dimensions[letter_].width = w
    ws.freeze_panes = "A3"


def build_user_stories(cfg, wb, model):
    ws = sheet_setup(cfg, wb, "stories")
    col = cfg["_col"]["stories"]
    for i, st in enumerate(model["stories"], 2):
        vals = {"us_id": st["us_id"], "story": st["title"] + ("\n" + st["story"] if st["story"] else ""),
                "wbs_ids": ", ".join(st["wbs_ids"]), "criteria": numbered(st["acs"]),
                "origin": cfg["stories"]["origins"][st["origin"]], "note": st["note"]}
        for k, c in col.items():
            write_cell(ws, i, c, vals[k])
    if model["stories"]:
        ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(len(col)), len(model["stories"]) + 1)


def build_assumption(cfg, wb, items):
    ws = sheet_setup(cfg, wb, "assumptions")
    col = cfg["_col"]["assumptions"]
    for i, a in enumerate(items, 1):
        vals = {"index": i, "category": a["category"], "text": a["text"]}
        for k, c in col.items():
            write_cell(ws, i + 1, c, vals[k])


def build_dependency(cfg, wb, items):
    ws = sheet_setup(cfg, wb, "dependencies")
    col = cfg["_col"]["dependencies"]
    for i, d in enumerate(items, 2):
        vals = dict(d, blocks=cap_list(cfg, d["blocks"], cfg["texts"]["cap_label_blocks"]))
        for k, c in col.items():
            write_cell(ws, i, c, vals[k])


def reference_rows(cfg, model):
    """(kind, item, reference) rows: documents, tasks, WBS rows, assumptions, dependencies, stories, glossary."""
    T = cfg["texts"]
    out_labels = {cfg["statuses"]["change"][k] for k in cfg["statuses"]["out_of_scope"]}
    out = []
    for d in cfg["documents"]:
        out.append(("Document", d["name"], d["text"]))
    for rec in model["recs"]:
        if rec["kind"] == "option":
            out.append(("Option", rec["id"], rec["source"]))
            continue
        parts = []
        if rec["kind"] == "overhead":
            parts.append(T["ref_overhead"].format(id=rec["id"]))
        elif rec["kind"] == "plan":
            parts.append(T["ref_plan"].format(id=rec["id"]))
            parts.append("estimation basis: %s" % (rec["basis"] or "not given"))
        else:
            parts.append(T["ref_added"].format(id=rec["id"]))
            parts.append("estimation basis: %s" % (rec["basis"] or "not given"))
            parts.append("source: %s" % (rec["source"] or "not given"))
        if rec["orig"]:
            o = rec["orig"]
            parts.append(T["ref_orig"].format(dev=fmt_num(o["dev"]), effort=fmt_num(o["effort"])))
        if rec["extra_source"]:
            parts.append("source: %s" % rec["extra_source"])
        if rec["kind"] == "plan" and rec["extra_source"] is None and rec["status"] in out_labels:
            parts.append("status: %s" % rec["status"])
        if rec["note"]:
            parts.append("change: %s" % rec["note"])
        kind = "Task" if rec["kind"] in ("plan", "overhead") else "Added task"
        out.append((kind, rec["id"], "; ".join(parts)))
    for rid in model["rows_order"]:
        r = model["rows"][rid]
        out.append(("WBS row", rid, "Source: %s" % (r.get("source") or "not given")))
    for i, a in enumerate(model["assumptions"], 1):
        out.append(("Assumption", "#%d %s" % (i, a["category"]), "Source: %s" % (a["source"] or "not given")))
    for d in model["deps"]:
        out.append(("Dependency", d["id"], "Source: %s" % (d["source"] or "not given")))
    for st in model["stories"]:
        parts = ["Source: %s" % (st["source"] or "not given")]
        if st["reason"]:
            parts.append("mapping: %s" % st["reason"])
        out.append(("Story", st["us_id"], "; ".join(parts)))
    out.append(("Glossary", "Term", "Meaning"))
    for g in model["glossary"]:
        out.append(("Glossary", g["term"], g["meaning"]))
    return out


def build_references(cfg, wb, model):
    ws = sheet_setup(cfg, wb, "references")
    col = cfg["_col"]["references"]
    for i, (kind, item, ref) in enumerate(reference_rows(cfg, model), 2):
        for k, v in (("kind", kind), ("item", item), ("reference", ref)):
            write_cell(ws, i, col[k], v)


def write_legend(cfg, wb):
    """One colour legend: what each fill in the workbook means. Placed after the last row of the
    sheet named in marking.legend_sheet, in that sheet's first three columns."""
    M = cfg["marking"]
    ws = wb[cfg["_sheet_name"][M["legend_sheet"]]]
    r = ws.max_row + 2
    for item in M["legend"]:
        if item["fill"] not in M["fills"]:
            bad("project.yaml: marking.legend names unknown fill %r" % item["fill"])
        write_cell(ws, r, 1, M["legend_kind"])
        write_cell(ws, r, 2, item["name"], fill_=fill(cfg, item["fill"]))
        write_cell(ws, r, 3, item["meaning"])
        r += 1


def stamp(cfg, wb):
    R = cfg["release"]
    if not R["stamp_first_sheet"]:
        return
    ws = wb[cfg["_sheet_order"][0]]
    write_cell(ws, ws.max_row + 2, 1, "Version %s, %s" % (R["version"], R["date"] or "date not set"))


def build(cfg, data_dir, out_path, plan_total):
    model = read_model(cfg, data_dir)
    wb = Workbook()
    wb.remove(wb.active)
    for name in cfg["_sheet_order"]:
        wb.create_sheet(name)
    build_master(cfg, wb)
    last = build_task_detail(cfg, wb, model)
    build_wbs(cfg, wb, model, last)
    build_effort_summary(cfg, wb, model, last, plan_total)
    build_user_stories(cfg, wb, model)
    build_assumption(cfg, wb, model["assumptions"])
    build_dependency(cfg, wb, model["deps"])
    build_references(cfg, wb, model)
    write_legend(cfg, wb)
    stamp(cfg, wb)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    wb.save(out_path)
    return model


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", required=True, help="project settings file (project.yaml)")
    ap.add_argument("--data", required=True, help="folder holding the YAML data files")
    ap.add_argument("--out", help="output .xlsx (default: release.output_name in the current folder)")
    ap.add_argument("--plan-total", type=float, help="override plan.total from project.yaml")
    ap.add_argument("--recalc", action="store_true", help="recalculate with LibreOffice after writing")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    try:
        cfg = wc.load_project(args.project)
        out = args.out or cfg["release"]["output_name"]
        total = args.plan_total if args.plan_total is not None else float(cfg["plan"]["total"])
        model = build(cfg, args.data, out, total)
    except BadInput as e:
        print("ERROR: %s" % e, file=sys.stderr)
        return 2
    print("Wrote %s: %d task rows, %d WBS rows" % (out, len(model["recs"]), len(model["rows"])))
    if args.recalc:
        try:
            wc.recalc(out)
        except Exception as e:  # a LibreOffice failure is not a data error
            print("ERROR: recalculation failed: %s" % e, file=sys.stderr)
            return 1
        print("Recalculated %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
