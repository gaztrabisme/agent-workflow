#!/usr/bin/env python3
"""Rebuild the ID map from immutable A–E/V and current skill references.

Run from the repository root: python3 skills/reward-design/audit/build_evidence_map.py
Requires all 129 original and V IDs to match; rejects unsupported IDs used in methods.
Writes only skills/reward-design/references/evidence-map.md.
"""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "audit/research"
EXPECTED = {f"{unit}{number}" for unit in "ABCDE"
            for number in range(1, 30 if unit == "E" else 26)}


def main():
    originals = {}
    for unit in "ABCDE":
        content = (RESEARCH / unit / "findings.md").read_text()
        for match in re.finditer(r"(?m)^### ([A-E]\d+) (.+)$", content):
            ident, title = match.groups()
            if ident in originals:
                raise ValueError(f"Duplicate original ID: {ident}")
            originals[ident] = (unit, title)

    verified = {}
    for line in (RESEARCH / "V/claims-verified.md").read_text().splitlines():
        if not re.match(r"^\| [A-E]\d+ \|", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 6:
            raise ValueError(f"Malformed V row: {line}")
        ident, name, verdict, tier, correction, citation = cells
        if ident in verified:
            raise ValueError(f"Duplicate V ID: {ident}")
        if verdict not in {"supported", "weakened", "unsupported"}:
            raise ValueError(f"Invalid verdict: {ident}")
        if tier not in {"T1", "T2", "T3", "T4"}:
            raise ValueError(f"Invalid tier: {ident}")
        verified[ident] = (name, verdict, tier)

    if set(originals) != EXPECTED or set(verified) != EXPECTED:
        raise ValueError("Original/V IDs differ from the nonempty 129-ID contract")

    documents = [ROOT / "SKILL.md"] + sorted(
        path for path in (ROOT / "references").glob("*.md")
        if path.name != "evidence-map.md"
    )
    uses = {ident: [] for ident in EXPECTED}
    for path in documents:
        content = path.read_text()
        referenced = set(re.findall(r"\b[A-E]\d+\b", content))
        if referenced - EXPECTED:
            raise ValueError(f"Unknown IDs in {path}: {referenced - EXPECTED}")
        for ident in referenced:
            if path == ROOT / "SKILL.md":
                uses[ident].append("[SKILL.md](../SKILL.md)")
            else:
                uses[ident].append(f"[{path.name}]({path.name})")

    text = [
        "# Evidence map",
        "",
        "Reader: a designer checking an ID's final evidence method, verdict and use.",
        "Every finding appears once: A1–A25, B1–B25, C1–C25, D1–D25 and E1–E29.",
        "[V](../audit/research/V/claims-verified.md) overrides the original findings;",
        "a supported verdict preserves caveats and does not validate every proposed recipe.",
        "",
        "## Tier and source rules",
        "",
        "T1 means brain measurement or formal meta-analysis, not strong, replicated or proven design efficacy;",
        "T2 means replicated controlled behavior; T3 means single-study, observational or scholarly theory/synthesis;",
        "T4 means practitioner craft/practice. Recipes are design inferences unless tested as described.",
        "E rows carry V's corrected source classification, not blanket empirical book grades;",
        "[reading-list.md](reading-list.md) spells out book kinds and individually graded claims remain separate.",
        "",
        "The technique link opens the exact original finding, including its full citation and caveats.",
        "Use the same-ID V row for final wording, correction sources and access limitations.",
        "Myth rows support the debunking, and dark-pattern rows support recognition rather than recommendation.",
        "Use locations below are generated from actual ID mentions in SKILL.md and the nine other references.",
        "",
        "## Findings",
        "",
        "| ID | technique | final tier | V verdict | where used in the skill |",
        "|---|---|---|---|---|",
    ]
    for ident in sorted(EXPECTED, key=lambda item: (item[0], int(item[1:]))):
        unit, title = originals[ident]
        name, verdict, tier = verified[ident]
        slug = re.sub(r"[^\w\- ]", "", f"{ident} {title}".lower()).replace(" ", "-")
        source = f"../audit/research/{unit}/findings.md#{slug}"
        used = ", ".join(uses[ident]) or "not used"
        if verdict == "unsupported" and uses[ident] and not all(
            "myths.md" in location for location in uses[ident]
        ):
            raise ValueError(f"Unsupported ID used as method: {ident}")
        text.append(f"| {ident} | [{name}]({source}) | {tier} | {verdict} | {used} |")

    text.extend([
        "",
        "## Applied corrections and access limits",
        "",
        "- A10 → T3: drug manipulation measured behavior/skin conductance, not the brain; 29 completed, 27 analysed.",
        "- A18 → T1: EEG is brain measurement; single-study uncertainty and indirect localization remain.",
        "- B12 → T3: prediction before reveal is task-dependent; the follow-up found no clear true-distribution recall advantage.",
        "- C1 → T3: ITPRA is scholarly expectation theory; the cue-sheet recipe is a design inference.",
        "- C4 → T1: DTI measures brain structure; small correlational groups do not establish causation or training effects.",
        "- C20 → T3: four related studies are proof of concept, with selection, training, small-sample and forced-choice limits.",
        "- D12 → T4: Pixar's lesson exists, but its specific Adams credit was not retrieved; origin uses [Adams's own 2013 account](https://www.aerogrammestudio.com/2013/06/05/back-to-the-story-spine/) of his 1991 invention.",
        "- Supported-row refinements are carried into the digests: A3 competing uncertainty accounts; A6 unrelated-fact interference; A7 mixed novelty-memory outcomes; A8/A25 coding dispute and mean-quality comparison; A12 16 recruited/15 in relevant contrasts; A15 corrected localization; A16 predetermined feedback; A20 visual/auditory boundary and uncertain fluency explanation.",
        "- A23's corrected article record is [JSTOR 44430317](https://www.jstor.org/stable/44430317), replacing the original issue-level pointer. A24 additionally distinguishes BOLD hemodynamics from neurochemistry; V supplies the measurement-method source.",
        "- C10/C11 do not establish earcons/icons as the best default; later comparisons often favor speech-based alerts. C12 follows the erratum and analysed sample. C25's pleasure interaction was outside the measured striatal regions.",
        "- D6 carries the later controlled counterexample to indiscriminate amplification. D14's comment analysis remains observational, distinct from craft. D15's campaign aggregation remains observational. D21's two video baselines stay distinct. D24 supplies no unavailable prototype-paper results or legal opinion. D25 remains a harm association, not causal proof or proof that free surprise is harmless.",
        "- E's supported verdicts concern bibliography only. Corrected whole-book kinds, edition/release/copyright distinctions and contributor credits are in the reading list; frameworks stay T4. E4's 2021 successor is an E discovery lead, not the book checked in V's row.",
        "",
        "V supplied 122 supported, 7 weakened and 0 unsupported verdicts. No ID was left out.",
        "Original research remains unchanged, including superseded tiers; always apply this map and V.",
        "Full-text access was uneven and replication searches were targeted, not systematic.",
        "[V's report](../audit/research/V/REPORT.md) records abstracts, indexed text, mirrors and inaccessible sources.",
        "Some support rests on primary abstracts or records; no unavailable methods or full books are claimed read here.",
        "The supplied V report mentions supplementary notes and checked-source copies that are absent from this input packet;",
        "use the shipped table and reports, and treat those missing supplements as unavailable.",
        "",
        "Maintainer: reward-design skill owner. Reviewed: 2026-10-10. Regenerate with `python3 skills/reward-design/audit/build_evidence_map.py` from the repository root after method edits; recheck when V changes.",
    ])
    destination = ROOT / "references/evidence-map.md"
    destination.write_text("\n".join(text) + "\n")
    print(f"Wrote {destination.relative_to(ROOT)}: {len(EXPECTED)} IDs, "
          f"{sum(not value for value in uses.values())} unused")


if __name__ == "__main__":
    main()
