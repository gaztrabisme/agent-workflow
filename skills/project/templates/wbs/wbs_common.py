"""Shared helpers for build.py and verify.py: project settings, YAML loading, LibreOffice recalculation.

Nothing here computes a figure. build.py and verify.py each derive figures on their own, so that the
verifier is an independent check of the builder. This module only reads settings and files.
"""
import fnmatch
import os
import shutil
import subprocess
import tempfile

import yaml

SOFFICE_TIMEOUT = 120

# Column keys each sheet must carry. Order and headers come from project.yaml.
TASK_DETAIL_KEYS = ["task_id", "row_type", "wbs_id", "section", "module", "task", "role", "dev", "qc", "ba",
                    "effort", "subtask_days", "over_threshold", "criteria", "status", "owner", "note"]
WBS_COMPUTED_KEYS = ["index", "id", "dev", "qc", "ba", "effort", "owner", "stories"]
STORY_KEYS = ["us_id", "story", "wbs_ids", "criteria", "origin", "note"]
ASSUMPTION_KEYS = ["index", "category", "text"]
DEPENDENCY_KEYS = ["id", "item", "from", "needed_by", "blocks", "status", "if_late"]
REFERENCE_KEYS = ["kind", "item", "reference"]
SHEET_KEYS = ["master", "summary", "wbs", "task_detail", "stories", "assumptions", "dependencies", "references"]
MASTER_NAMES = ["RATE", "MD_MONTH", "PM_PCT", "CONT_PCT"]

# Every setting project.yaml must give. A missing one is an input error (exit 2), never a silent default.
REQUIRED = [
    "pricing", "release.version", "release.date", "release.output_name", "release.stamp_first_sheet",
    "data.files.plan_tasks", "data.files.feature_map", "data.files.changes", "data.files.proposals",
    "data.files.assumptions", "data.files.dependencies", "data.files.glossary", "data.files.stories",
    "data.files.story_source", "data.files.task_criteria_pattern", "data.fields", "data.feature_key_parts",
    "plan.total", "plan.overhead_phase",
    "sheets", "internal_sheets", "columns.task_detail", "columns.wbs", "columns.stories", "columns.assumptions",
    "columns.dependencies", "columns.references", "wbs_required_fields",
    "master.rows", "master.forbidden_numbers", "master.forbidden_words",
    "roles.known", "owners.ours", "owners.all", "owners.excluded", "owners.excluded_option_roles",
    "owners.shared_row_label", "owners.other_owner_lines",
    "statuses.in_scope", "statuses.overhead", "statuses.option", "statuses.change", "statuses.add",
    "statuses.needs_source", "statuses.out_of_scope", "statuses.removal_source_marker",
    "dependencies.from", "dependencies.status",
    "ids.option_prefix", "ids.subtask_infix", "ids.change_add_prefix", "ids.proposal_add_prefix",
    "effort_rule.addons.qc", "effort_rule.addons.ba", "effort_rule.round_up_to", "effort_rule.tolerance",
    "effort_rule.no_dev_roles",
    "criteria.over_days", "criteria.min", "criteria.max", "criteria.subtask_max_days", "criteria.subtask_step",
    "criteria.clause", "criteria.clause_trigger",
    "text.cap", "text.subtask_name_cap", "text.forbid_diacritics", "text.person_names", "text.internal_source_patterns",
    "stories.origins", "stories.default_origin", "stories.verbatim_origin", "stories.fallback_source", "stories.required_row_prefixes",
    "marking.proposal_prefix", "marking.fills", "marking.highlight_fill", "marking.legend_sheet",
    "marking.legend_kind", "marking.legend",
    "texts", "documents", "summary",
]
TEXT_KEYS = ["section_added", "section_option", "note_added", "note_highlight", "note_option", "source_plan",
             "source_option", "ref_plan", "ref_overhead", "ref_added", "ref_orig", "row_type_task",
             "row_type_sub", "cap_list_tail", "cap_label_stories", "cap_label_blocks"]
SUMMARY_KEYS = ["title", "headers", "base_title", "activities", "subtotal", "check", "dev_memo", "pm", "sub",
                "contingency", "total", "option_blocks", "option_lines", "other_title", "plan_check", "bridge",
                "notes_title", "notes"]
SUMMARY_SUB = {"option_lines": ["effort", "dev", "pm", "sub", "contingency", "total"],
               "plan_check": ["title", "effort", "dev", "pm", "sub", "contingency", "total", "reference",
                              "difference"],
               "bridge": ["title", "start", "end", "difference", "step_note", "labels"]}
BRIDGE_LABELS = ["excluded_owner", "other_owner", "proposal_change", "proposal_add", "highlight_add", "scope_add"]
FILL_KEYS = ["header", "title", "subheader", "block", "total", "input", "fill_in", "proposal"]


class BadInput(Exception):
    """Input rejected. The message names the file and the item."""


def bad(msg):
    raise BadInput(msg)


def get(cfg, dotted):
    cur = cfg
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(dotted)
        cur = cur[part]
    return cur


def load_project(path):
    """Read project.yaml, check every required setting is present, and add derived lookups."""
    if not os.path.exists(path):
        bad("project settings file not found: %s" % path)
    try:
        with open(path, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
    except yaml.YAMLError as e:
        bad("project.yaml is not valid YAML: %s" % e)
    if not isinstance(cfg, dict):
        bad("project.yaml is empty or not a mapping")
    if cfg.get("pricing") == "model":
        bad("pricing: model is not in the first cut")
    if cfg.get("pricing") != "team-sheet":
        bad("project.yaml: pricing must be team-sheet (got %r)" % cfg.get("pricing"))
    for key in REQUIRED:
        try:
            get(cfg, key)
        except KeyError:
            bad("project.yaml: missing setting %s" % key)
    for k in TEXT_KEYS:
        if k not in cfg["texts"]:
            bad("project.yaml: missing setting texts.%s" % k)
    for k in FILL_KEYS:
        if k not in cfg["marking"]["fills"]:
            bad("project.yaml: missing setting marking.fills.%s" % k)
    if cfg["marking"]["highlight_fill"] not in cfg["marking"]["fills"]:
        bad("project.yaml: marking.highlight_fill must name one of marking.fills")
    if cfg["marking"]["fills"]["proposal"] == cfg["marking"]["fills"]["fill_in"]:
        bad("project.yaml: the proposal fill must differ from the fill-in fill")

    # sheets: list of {key, name}; order is the workbook order
    names, seen = {}, []
    for s in cfg["sheets"]:
        if not isinstance(s, dict) or s.get("key") not in SHEET_KEYS or not s.get("name"):
            bad("project.yaml: each sheets item needs key (one of %s) and name" % ", ".join(SHEET_KEYS))
        names[s["key"]] = str(s["name"])
        seen.append(s["key"])
    if sorted(seen) != sorted(SHEET_KEYS):
        bad("project.yaml: sheets must list each of %s exactly once" % ", ".join(SHEET_KEYS))
    for k in cfg["internal_sheets"]:
        if k not in names:
            bad("project.yaml: internal_sheets names unknown sheet key %r" % k)
    if cfg["marking"]["legend_sheet"] not in names:
        bad("project.yaml: marking.legend_sheet names unknown sheet key %r" % cfg["marking"]["legend_sheet"])
    cfg["_sheet_name"] = names
    cfg["_sheet_order"] = [names[k] for k in seen]
    cfg["_shown"] = [names[k] for k in seen if k not in cfg["internal_sheets"]]

    # columns: per sheet, list of {key, header, width?, field?}; derive key -> letter
    need = {"task_detail": TASK_DETAIL_KEYS, "stories": STORY_KEYS, "assumptions": ASSUMPTION_KEYS,
            "dependencies": DEPENDENCY_KEYS, "references": REFERENCE_KEYS}
    cfg["_col"] = {}
    for sheet, cols in cfg["columns"].items():
        if not isinstance(cols, list) or not cols:
            bad("project.yaml: columns.%s must be a non-empty list" % sheet)
        keys = []
        for c in cols:
            if not isinstance(c, dict) or not c.get("key") or "header" not in c:
                bad("project.yaml: each columns.%s item needs key and header" % sheet)
            keys.append(c["key"])
        if len(set(keys)) != len(keys):
            bad("project.yaml: columns.%s lists a key twice" % sheet)
        if sheet in need and sorted(keys) != sorted(need[sheet]):
            bad("project.yaml: columns.%s must list each of %s exactly once" % (sheet, ", ".join(need[sheet])))
        if sheet == "wbs":
            for k in WBS_COMPUTED_KEYS:
                if k not in keys:
                    bad("project.yaml: columns.wbs must include key %s" % k)
        cfg["_col"][sheet] = {k: i + 1 for i, k in enumerate(keys)}

    master_names = [r.get("name") for r in cfg["master"]["rows"] if r.get("name")]
    for n in MASTER_NAMES:
        if n not in master_names:
            bad("project.yaml: master.rows must define the named input %s" % n)
    for o in cfg["owners"]["other_owner_lines"]:
        if o.get("owner") not in cfg["owners"]["all"]:
            bad("project.yaml: owners.other_owner_lines names unknown owner %r" % o.get("owner"))
    if cfg["owners"]["ours"] not in cfg["owners"]["all"]:
        bad("project.yaml: owners.ours must be one of owners.all")
    if cfg["owners"]["excluded"] is not None and cfg["owners"]["excluded"] not in cfg["owners"]["all"]:
        bad("project.yaml: owners.excluded must be null or one of owners.all")
    for k in cfg["statuses"]["needs_source"]:
        if k not in cfg["statuses"]["change"]:
            bad("project.yaml: statuses.needs_source names unknown status %r" % k)
    if cfg["stories"]["verbatim_origin"] is not None and \
            cfg["stories"]["verbatim_origin"] not in cfg["stories"]["origins"]:
        bad("project.yaml: stories.verbatim_origin must be null or one of stories.origins")
    for k in SUMMARY_KEYS:
        if k not in cfg["summary"]:
            bad("project.yaml: missing setting summary.%s" % k)
    for k, subs in SUMMARY_SUB.items():
        for sk in subs:
            if sk not in cfg["summary"][k]:
                bad("project.yaml: missing setting summary.%s.%s" % (k, sk))
    for k in BRIDGE_LABELS:
        if k not in cfg["summary"]["bridge"]["labels"]:
            bad("project.yaml: missing setting summary.bridge.labels.%s" % k)
    for k in cfg["statuses"]["out_of_scope"]:
        if k not in cfg["statuses"]["change"]:
            bad("project.yaml: statuses.out_of_scope names unknown status %r" % k)
    if cfg["stories"]["default_origin"] not in cfg["stories"]["origins"]:
        bad("project.yaml: stories.default_origin must be one of stories.origins")
    labels = list(cfg["statuses"]["change"].values()) + list(cfg["statuses"]["add"].values())
    for b in cfg["summary"]["option_blocks"]:
        if b.get("status") not in labels:
            bad("project.yaml: summary.option_blocks status %r is not a status label" % b.get("status"))
    acts = cfg["summary"].get("activities") or []
    for a in acts:
        if a.get("kind") not in ("role_plus_addon", "roles_net"):
            bad("project.yaml: summary activity %r has kind %r (role_plus_addon or roles_net)"
                % (a.get("label"), a.get("kind")))
        roles = [a["role"]] if a.get("kind") == "role_plus_addon" else (a.get("roles") or [])
        for r in roles:
            if r not in cfg["roles"]["known"]:
                bad("project.yaml: summary activity %r names unknown role %r" % (a.get("label"), r))
        if a.get("kind") == "role_plus_addon" and a.get("addon") not in ("qc", "ba"):
            bad("project.yaml: summary activity %r: addon must be qc or ba" % a.get("label"))
    return cfg


def letter(cfg, sheet, key):
    from openpyxl.utils import get_column_letter
    return get_column_letter(cfg["_col"][sheet][key])


def rename_keys(obj, aliases):
    """Rename this project's YAML field names to the template's names, at any depth."""
    if isinstance(obj, dict):
        return {aliases.get(k, k): rename_keys(v, aliases) for k, v in obj.items()}
    if isinstance(obj, list):
        return [rename_keys(x, aliases) for x in obj]
    return obj


def load_data(cfg, data_dir, file_key=None, name=None, required=True, default=None):
    """Load one data file named in project.yaml (data.files.<file_key>) or by name."""
    name = name or cfg["data"]["files"][file_key]
    path = os.path.join(data_dir, name)
    if not os.path.exists(path):
        if required:
            bad("missing input file %s" % path)
        return default
    try:
        with open(path, encoding="utf-8") as f:
            doc = yaml.safe_load(f)
    except yaml.YAMLError as e:
        bad("%s is not valid YAML: %s" % (name, e))
    if doc is None:
        return default
    aliases = {v: k for k, v in (cfg["data"]["fields"] or {}).items() if v != k}
    return rename_keys(doc, aliases)


def criteria_files(cfg, data_dir):
    pat = cfg["data"]["files"]["task_criteria_pattern"]
    return [n for n in sorted(os.listdir(data_dir)) if fnmatch.fnmatch(n, pat)]


def rgb(hex6):
    return ("FF" + str(hex6).upper().lstrip("#"))[-8:]


# ------------------------------------------------------------------ LibreOffice
def find_soffice():
    for c in (os.environ.get("SOFFICE"), shutil.which("soffice"),
              r"C:\Program Files\LibreOffice\program\soffice.exe",
              r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
              "/usr/bin/soffice", "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
        if c and os.path.exists(c):
            return c
    raise RuntimeError("LibreOffice soffice not found (set SOFFICE to its path)")


def recalc(path, outpath=None):
    """Recalculate `path` with LibreOffice headless so every formula has a cached value.
    Converts in a scratch folder and copies back: converting into the input's own folder fails."""
    path = os.path.abspath(path)
    outpath = os.path.abspath(outpath or path)
    soffice = find_soffice()
    src_dir = tempfile.mkdtemp(prefix="wbs_in_")
    out_dir = tempfile.mkdtemp(prefix="wbs_out_")
    try:
        src = os.path.join(src_dir, os.path.basename(path))
        shutil.copyfile(path, src)
        res = os.path.join(out_dir, os.path.basename(path))
        last = ""
        for attempt in (1, 2):
            prof = tempfile.mkdtemp(prefix="wbs_lo_profile_")
            uri = "file:///" + prof.replace("\\", "/").lstrip("/")
            proc = subprocess.Popen([soffice, "-env:UserInstallation=" + uri, "--headless",
                                     "--convert-to", "xlsx", "--outdir", out_dir, src],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                so, se = proc.communicate(timeout=SOFFICE_TIMEOUT)
                last = "exit %s: %s %s" % (proc.returncode, so, se)
                if proc.returncode == 0 and os.path.exists(res):
                    break
            except subprocess.TimeoutExpired:
                # LibreOffice sometimes hangs at start-up; kill the process tree and retry once.
                if os.name == "nt":
                    subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True)
                else:
                    proc.kill()
                proc.communicate()
                last = "timed out after %ss (attempt %d)" % (SOFFICE_TIMEOUT, attempt)
            finally:
                shutil.rmtree(prof, ignore_errors=True)
        if not os.path.exists(res):
            raise RuntimeError("LibreOffice recalculation failed: %s" % last)
        shutil.copyfile(res, outpath)
    finally:
        shutil.rmtree(src_dir, ignore_errors=True)
        shutil.rmtree(out_dir, ignore_errors=True)
    return outpath
