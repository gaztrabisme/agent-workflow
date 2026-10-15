#!/bin/bash
# Structural check for skills/reward-design, run from the repository root.
python3 -I - <<'PY'
import re,sys,pathlib
S=pathlib.Path("skills/reward-design"); errs=[]
t=(S/"SKILL.md").read_text() if (S/"SKILL.md").exists() else ""
if not re.search(r"(?m)^name:\s*reward-design\s*$",t): errs.append("frontmatter name")
if "dopamine" not in (t.split("---")[1].lower() if t.count("---")>=2 else ""): errs.append("dopamine keyword")
if "reward-design" not in pathlib.Path("skills.txt").read_text().split(): errs.append("skills.txt")
for ref in re.findall(r"`(references/[^`]+\.md)`",t):
    if not (S/ref).exists(): errs.append(f"SKILL.md points to missing {ref}")
for p in (S/"references").glob("*.md"):
    if f"references/{p.name}" not in t: errs.append(f"orphan reference {p.name}")
em=(S/"references/evidence-map.md")
ids=set()
for u in "ABCDE":
    f=S/f"audit/research/{u}/findings.md"
    ids|=set(re.findall(rf"(?m)^### ({u}\d+)\b",f.read_text()))
if em.exists():
    e=em.read_text()
    miss=[i for i in sorted(ids) if not re.search(rf"\|\s*{i}\s*\|",e)]
    if miss: errs.append(f"evidence-map missing {miss}")
else: errs.append("evidence-map.md missing")
for f in ["reading-list.md","dark-patterns.md","review-checklist.md","myths.md"]:
    if not (S/"references"/f).exists(): errs.append(f"missing references/{f}")
if not ((S/"EVOLUTION.md").exists() and "PENDING" in (S/"EVOLUTION.md").read_text()): errs.append("EVOLUTION PENDING")
for sib in ["presentation","motion","visual-design","information-design","ux"]:
    if "reward-design" not in pathlib.Path(f"skills/{sib}/SKILL.md").read_text(): errs.append(f"no pointer in {sib}")
if len(t.splitlines())>230: errs.append(f"SKILL.md {len(t.splitlines())} lines")
if errs: print("FAIL"); [print(" ",x) for x in errs]; sys.exit(1)
print(f"PASS: {len(ids)} finding IDs mapped, SKILL.md {len(t.splitlines())} lines")
PY
