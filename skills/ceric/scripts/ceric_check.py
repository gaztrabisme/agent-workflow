#!/usr/bin/env python3
"""One command over a CERIC run directory: the mechanical half of the scorecard.

Usage:
  ceric_check.py <run_dir> --paper <pdf|txt> [--extra <pdf|txt> ...] [--freeform] [--json <path>]

Template mode expects `ceric-notes.md` and `narrative.md` in <run_dir> (this skill's templates).
Freeform mode (--freeform) takes every *.md in <run_dir> except README.md and files ending in
-report.md: the rest go to the quote check; the narrative is the file whose name contains
"narrative" (else the file with the longest paragraph); the builders file is the one whose name
contains "builder" (else the narrative file). The files picked for quotes, narrative and builders
are printed before the scorecard.

Prints a scorecard table. Exit 0 when both checkers pass; 1 otherwise.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, args):
    p = subprocess.run([sys.executable, os.path.join(HERE, script)] + args + ['--json', '-'],
                       capture_output=True, text=True)
    text = p.stdout
    head, _, js = text.partition('---JSON---')
    try:
        data = json.loads(js) if js.strip() else {}
    except json.JSONDecodeError:
        data = {}
    return p.returncode, head, data, p.stderr


def notes_size(path):
    """(table rows, words) in a notes file; separator rows of dashes do not count."""
    lines = open(path, encoding='utf-8').read().splitlines()
    rows = sum(1 for ln in lines if ln.lstrip().startswith('|') and not re.fullmatch(r'[\s:\-|]+', ln))
    words = sum(len(ln.split()) for ln in lines)
    return rows, words


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('run_dir')
    ap.add_argument('--paper', required=True)
    ap.add_argument('--extra', nargs='*', default=[])
    ap.add_argument('--freeform', action='store_true')
    ap.add_argument('--json')
    a = ap.parse_args()

    if a.freeform:
        files = sorted(glob.glob(os.path.join(a.run_dir, '*.md')))
        files = [f for f in files if os.path.basename(f).lower() != 'readme.md'
                 and not os.path.basename(f).lower().endswith('-report.md')]
        narrative = next((f for f in files if 'narrative' in os.path.basename(f).lower()), None)
        builders = next((f for f in files if 'builder' in os.path.basename(f).lower()), narrative)
        notes = None
    else:
        files = [os.path.join(a.run_dir, 'ceric-notes.md'), os.path.join(a.run_dir, 'narrative.md')]
        narrative = files[1]
        builders = files[1]
        notes = files[0]
    files = [f for f in files if os.path.exists(f)]
    if not files or not narrative or not os.path.exists(narrative):
        print(f'nothing to check in {a.run_dir} (need {"*.md" if a.freeform else "ceric-notes.md + narrative.md"})')
        return 1
    if a.freeform:
        print('picked for quotes: ' + (', '.join(os.path.basename(f) for f in files) or '-'))
        print(f"picked as narrative: {os.path.basename(narrative) if narrative else '-'} · "
              f"picked as builders: {os.path.basename(builders) if builders else '-'}")

    qargs = ['--paper', a.paper, '--notes'] + files + (['--freeform'] if a.freeform else [])
    if a.extra:
        qargs += ['--extra'] + a.extra
    q_rc, q_txt, q, q_err = run('check_quotes.py', qargs)
    nargs = ['--narrative', narrative, '--paper', a.paper, '--builders', builders]
    if a.extra:
        nargs += ['--extra'] + a.extra
    if notes and os.path.exists(notes):
        nargs += ['--notes', notes]
    n_rc, n_txt, n, n_err = run('check_narrative.py', nargs)

    s = q.get('summary', {})
    rows = [
        ('quotes', f"{q.get('total', 0)} checked · pass {s.get('pass', 0)} · unpinned {s.get('pass-unpinned', 0)} · "
                   f"via extra {s.get('pass-extra', 0)} · pass-eye {s.get('pass-eye', 0)} · "
                   f"eye-check {s.get('eye-check', 0)} · FLAG {s.get('FLAG', 0)}",
         'ok' if q_rc == 0 else 'FAIL'),
        ('page hints', f"{q.get('pinned', 0)}/{q.get('total', 0)} quotes carry a page", 'info'),
        ('narrative words', f"{n.get('words')} (band {n.get('band')}) · mode {n.get('mode')}",
         'ok' if n.get('hard', {}).get('words') else 'FAIL'),
        ('one paragraph', f"{n.get('long_paragraphs')} long paragraph(s)",
         ('ok' if n['hard']['paragraph'] else 'FAIL') if 'paragraph' in n.get('hard', {}) else 'info'),
        ('copied runs', f"{len(n.get('copied_runs', []))} in narrative · {len(n.get('builder_copied_runs', []))} in builders",
         'ok' if n.get('hard', {}).get('copied') else 'FAIL'),
        ('builder stems', f"{sum(n.get('builder_stems', {}).values())}/5",
         'ok' if n.get('hard', {}).get('builders', True) else 'FAIL'),
        ('CCERI order (advisory, keyword-based)', ' '.join(n.get('cceri_order', [])), 'advisory'),
        ('hedges', ', '.join(f'{k}×{v}' for k, v in n.get('hedges', {}).items()) or 'none', 'info'),
        ('strengtheners', ', '.join(f"{k}×{v['count']}{'' if v['in_paper'] else ' (not in paper)'}"
                                    for k, v in n.get('strengtheners', {}).items()) or 'none', 'info'),
        ('numbers not in paper', ', '.join(n.get('numbers_not_in_paper', [])) or 'none', 'lint'),
        ('terms not in paper', ', '.join(n.get('terms_not_in_paper', [])) or 'none', 'lint'),
        ('row lints', str(len(n.get('row_lints', []))), 'lint'),
    ]
    if notes and os.path.exists(notes):
        nrows, nwords = notes_size(notes)
        rows.append(('notes size', f"{nrows} table rows · {nwords} words in {os.path.basename(notes)}", 'info'))
    print(f'run: {a.run_dir}  paper: {a.paper}')
    print('| Check | Result | Verdict |\n|---|---|---|')
    for k, v, verdict in rows:
        print(f'| {k} | {v} | {verdict} |')
    for line in q_txt.splitlines():
        if line.strip().startswith('['):
            print('  ' + line.strip())
    for r in n.get('copied_runs', []) + n.get('builder_copied_runs', []):
        print('  copied run:', r)
    print('  sentence labels:', ' '.join(l or '-' for l in n.get('sentence_labels', [])))
    for l in n.get('row_lints', []):
        print('  row lint:', l)
    if q_err.strip() or n_err.strip():
        print('stderr:', (q_err + n_err).strip()[-1500:])
    if a.json:
        json.dump({'quotes': q, 'narrative': n}, open(a.json, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    return 0 if q_rc == 0 and n_rc == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
