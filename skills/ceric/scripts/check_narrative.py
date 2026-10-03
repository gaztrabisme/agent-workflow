#!/usr/bin/env python3
"""Mechanical checks on a CERIC narrative summary and sentence builders.

Usage:
  check_narrative.py --narrative <md> --paper <pdf|txt> [--builders <md>] [--extra <pdf|txt> ...]
                     [--notes <md>] [--min-words 150] [--max-words 450] [--run 8] [--json <path|->]

Hard checks (exit 1 on failure):
  words        the merged paragraph is inside the word band (the key's own narrative is ~440 words)
  copied       no run of >= --run consecutive words is copied from the paper (or an --extra source)
  builders     each of the five packet stems opens a sentence in --builders, if given: the stem stands at
               the start of a line or right after '. ', not merely somewhere in the file
  paragraph    in template mode (a heading matching /merge|narrative/ exists) that section holds exactly one paragraph

Lints (reported, never fail - a grader reads them):
  cceri        each sentence of the paragraph is labelled by its dominant element signal; the collapsed label
               sequence should run Context -> Claim -> Evidence -> Reasoning -> Implications. This lint is
               advisory (keyword-based): sentences about the wording itself (ladder, hedge, strength, wording)
               are labelled neutral and skipped when the order is judged
  hedges       hedge words present in the paragraph and builders; strengtheners present, and whether the paper uses them
  numbers      numbers in the paragraph/builders that do not occur in the paper text and are not † - tagged
  terms        capitalised terms (not sentence-initial) absent from the paper text - candidates for outside information
  rows         with --notes in template shape: Evidence rows carrying result/derivation signals; Claim rows carrying future tense

The paragraph is the longest block of consecutive non-heading, non-table, non-list lines in --narrative,
or, in template mode, the single block under the narrative heading.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_pages import load_pages  # noqa: E402

STEMS = {
    'claim': "this paper's central claim is",
    'evidence': 'the evidence that supports it is',
    'reasoning': 'the reasoning that justifies it is',
    'implications': 'these findings motivate future work',
    'context': 'the motivation for this study was',
}
HEDGES = [r'consistent with', r'not inconsistent', r'candidates?', r'can be explained', r'may', r'might',
          r'suggests?', r'cannot be excluded', r'disfavou?r(?:ed|s)?', r'assum(?:e|ed|es|ption|ptions)',
          r'expected', r'appears?', r'likely', r'possibl[ey]', r'not yet', r'remains?', r'cannot', r'unclear',
          r'caution', r'limitations?', r'tentative', r'preliminary', r'if\b', r'would']
STRENGTHENERS = [r'proves?', r'proven', r'proof', r'confirm(?:s|ed|ing)?', r'demonstrat(?:es?|ed|ing)',
                 r'establish(?:es|ed)?', r'definitiv(?:e|ely)', r'unambiguous(?:ly)?', r'certain(?:ly)?',
                 r'undeniabl[ey]', r'shows? that', r'is the shadow', r'conclusively', r'directly (?:proves?|confirms?)']
# element signals, weighted; explicit sentence-builder phrases outweigh keywords
SIGNALS = {
    'Co': [(3, r"\b(?:the motivation for this study|before this study|prior to this|earlier (?:work|observations|studies))"),
           (2, r"\b(?:prior|earlier|previous(?:ly)?|before|had (?:already|been|not)|was known|could not|had left|"
               r"unimaged|too little|not been imaged)\b"),
           (1, r"\b(?:predict(?:s|ed|ion)?|expected to|theory|motivat(?:ed|ion)|gap)\b")],
    'C': [(3, r"\b(?:central claim|this paper(?:'s| claims| reports)|the authors (?:claim|report|identify|conclude|find)|"
              r"reports? that|we (?:find|report|show))"),
          (1, r"\b(?:claim|reported|identif(?:y|ies|ied)|conclude[sd]?|finding)\b")],
    'E': [(3, r"\b(?:the evidence (?:that supports|is|comes)|evidence (?:comes|is))"),
          (1, r"\b(?:evidence|observ(?:ed|ations?|ing)|telescope|data|array|nights?|campaign|measure(?:d|ments?)?|"
              r"collected|simulat(?:ions?|ed)|stations?|baselines?|library|images?)\b")],
    'R': [(3, r"\b(?:the reasoning (?:that justifies|is)|the authors reason)"),
          (1, r"\b(?:reason(?:s|ing)?|because|explain(?:s|ed|ing)?|consistent with|interpret|infer(?:red)?|"
              r"deriv(?:e|ed)|compar(?:e|ed|ison)|indicat(?:e|es|ing)|therefore|thus|rule[sd]? out|favou?rs?|"
              r"convert|yields?|so the|matches?)\b")],
    'I': [(3, r"\b(?:these findings motivate|motivate future work|future work|implications?)\b"),
          (2, r"\b(?:motivates?|motivated|new tool|complement(?:ary|s)?|follow-up|further (?:work|tests?|observations?)|"
              r"next (?:steps?|tests?|campaign)|later campaign|now possible|can now|turn(?:s)? the)\b"),
          (1, r"\b(?:future|next|will (?:test|need|require)|planned|opens?|enable)\b")],
}
RESULT_SIGNALS = re.compile(r"\b(we find|consistent with|derive|indicat|implies|therefore|thus|shows that|"
                            r"is explained|can be explained|yields?|infer)|±", re.I)
FUTURE = re.compile(r"\b(will|future|next step|should be|remains to|plan(?:ned)? to)\b", re.I)
# sentences about the wording itself (the hedge ladder, a strength note) are not element sentences
META = re.compile(r'\b(ladder\w*|hedge\w*|strength\w*|wording)\b', re.I)
STOP_TERMS = {'ceric', 'cceri', 'claim', 'evidence', 'reasoning', 'implications', 'context', 'activity', 'packet',
              'step', 'builders', 'sentence', 'rewrite', 'paper', 'participant', 'reader', 'sources', 'self'}


def toks(s):
    s = re.sub(r'-\s*\n\s*', '', s)
    s = re.sub(r"[’']", '', s)
    return re.findall(r'[a-z]+\d*|\d+(?:\.\d+)?', s.lower())


def blocks(lines):
    """Paragraph blocks: runs of lines that are not headings, tables, lists, rules or blank."""
    out, cur = [], []
    for ln in lines:
        s = ln.strip()
        if (not s or s.startswith(('#', '|', '- ', '* ', '> ', '---', '†')) or re.match(r'^\d+[.)]\s', s)
                or (s.startswith('**') and s.endswith('**')) or re.match(r'^\*\*[^*]{1,40}:\*\*', s)):
            if cur:
                out.append(' '.join(cur))
                cur = []
            continue
        cur.append(s)
    if cur:
        out.append(' '.join(cur))
    return out


def narrative_paragraph(text):
    lines = text.splitlines()
    heads = [(i, ln) for i, ln in enumerate(lines) if re.match(r'^#{1,6}\s', ln)]
    for i, (idx, h) in enumerate(heads):
        if re.search(r'merge|narrative paragraph|^#+\s*narrative\s*$', h, re.I) and not re.search(r'summary\s*$', h, re.I):
            end = heads[i + 1][0] if i + 1 < len(heads) else len(lines)
            section = [ln for ln in lines[idx + 1:end] if not ln.strip().startswith('---')]
            bl = [b for b in blocks(section) if len(b.split()) >= 50]
            if bl:
                return max(bl, key=lambda b: len(b.split())), len(bl), 'template'
    bl = blocks(lines)
    if not bl:
        return '', 0, 'none'
    return max(bl, key=lambda b: len(b.split())), sum(1 for b in bl if len(b.split()) >= 100), 'longest-block'


def copied_runs(text, grams, n, allow=''):
    t = toks(text)
    runs, i = [], 0
    while i <= len(t) - n:
        if tuple(t[i:i + n]) in grams:
            j = i + n
            while j < len(t) and tuple(t[j - n + 1:j + 1]) in grams:
                j += 1
            run = ' '.join(t[i:j])
            if run not in allow:
                runs.append(run)
            i = j
        else:
            i += 1
    return runs


def label_sentence(sent):
    low = sent.lower()
    scores = {}
    for el, pats in SIGNALS.items():
        scores[el] = sum(w * len(re.findall(p, low)) for w, p in pats)
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None


def cceri_order(par):
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z“"(])', par)
    labels = [None if META.search(s) else label_sentence(s) for s in sents if s.strip()]
    seq = []
    for l in labels:
        if l and (not seq or seq[-1] != l):
            seq.append(l)
    order = ['Co', 'C', 'E', 'R', 'I']
    idx = [order.index(l) for l in seq]
    monotonic = all(b >= a for a, b in zip(idx, idx[1:]))
    return labels, seq, monotonic


def opens_sentence(low: str, stem: str) -> bool:
    """True when stem opens a sentence: at the start of a line, or right after '. '."""
    for m in re.finditer(re.escape(stem), low):
        s = m.start()
        if s == 0 or low[s - 1] == '\n' or (s >= 2 and low[s - 2:s] == '. '):
            return True
    return False


def numbers_not_in(text, paper_flat):
    out = []
    for m in re.finditer(r'(?<![\w.])(\d[\d,]*\.?\d*)(?![\w])', text):
        num = m.group(1).replace(',', '')
        if len(num) <= 1:
            continue
        window = text[max(0, m.start() - 60):m.end() + 60]
        if '†' in window:
            continue
        if num not in paper_flat:
            out.append(m.group(1))
    return sorted(set(out))


def terms_not_in(text, paper_low):
    out = set()
    for sent in re.split(r'(?<=[.!?])\s+', text):
        words = re.findall(r"[A-Za-z][A-Za-z’'\-–]+", sent)
        for w in words[1:]:
            if w[0].isupper() and len(w) > 2:
                core = re.sub(r"[’'\-–].*$", '', w).lower()
                if core in STOP_TERMS or w.lower() in STOP_TERMS:
                    continue
                if core and core not in paper_low and w.lower() not in paper_low:
                    out.add(w)
    return sorted(out)


def row_lints(path):
    lints, header = [], None
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.lstrip().startswith('|'):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if all(set(c) <= set(':- ') for c in cells):
            continue
        ei = next((i for i, h in enumerate(header) if 'element' in h), None)
        qi = next((i for i, h in enumerate(header) if 'quote' in h or 'copied' in h or 'own' in h), None)
        if ei is None or qi is None or max(ei, qi) >= len(cells):
            continue
        el, txt = cells[ei].lower(), cells[qi]
        if el.startswith('evidence') and RESULT_SIGNALS.search(txt):
            lints.append(f'line {n}: Evidence row carries a result/derivation signal -> is it Reasoning? :: {txt[:90]}')
        if el.startswith('claim') and FUTURE.search(txt):
            lints.append(f'line {n}: Claim row carries future tense -> is it an Implication? :: {txt[:90]}')
    return lints


def count_lexicon(lex, text):
    out = {}
    for pat in lex:
        n = len(re.findall(r'\b' + pat + r'\b', text))
        if n:
            out[pat.replace('\\b', '')] = n
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--narrative', required=True)
    ap.add_argument('--paper', required=True)
    ap.add_argument('--builders')
    ap.add_argument('--extra', nargs='*', default=[])
    ap.add_argument('--notes')
    ap.add_argument('--min-words', type=int, default=150)
    ap.add_argument('--max-words', type=int, default=450)
    ap.add_argument('--run', type=int, default=8)
    ap.add_argument('--json')
    a = ap.parse_args()

    paper = ' '.join(load_pages(a.paper).values())
    # copied-run check is against the PAPER only: --extra sources (a packet, a key) are legitimately quoted by design
    st = toks(paper)
    grams = {tuple(st[i:i + a.run]) for i in range(len(st) - a.run + 1)}
    title_block = ' '.join(st[:60])  # naming the paper's title is not copying
    paper_low = set(toks(paper))
    paper_flat = re.sub(r',', '', paper)
    paper_l = paper.lower()

    text = open(a.narrative, encoding='utf-8').read()
    par, n_long, mode = narrative_paragraph(text)
    words = len(par.split())
    res = {'mode': mode, 'words': words, 'band': [a.min_words, a.max_words], 'long_paragraphs': n_long,
           'paragraph_head': par[:160]}
    hard = {'words': a.min_words <= words <= a.max_words}
    runs = copied_runs(par, grams, a.run, title_block)
    res['copied_runs'] = runs
    hard['copied'] = not runs
    if mode == 'template':
        hard['paragraph'] = n_long == 1
    labels, seq, ok = cceri_order(par)
    res['sentence_labels'] = labels
    res['cceri_order'] = seq
    res['cceri_ok'] = ok

    btext = ''
    if a.builders:
        braw = open(a.builders, encoding='utf-8').read()
        btext = ' '.join(blocks(braw.splitlines()))
        low = re.sub(r"[’']", "'", braw.lower())
        present = {k: opens_sentence(low, v) for k, v in STEMS.items()}
        res['builder_stems'] = present
        hard['builders'] = all(present.values())
        res['builder_copied_runs'] = copied_runs(btext, grams, a.run, title_block)
        hard['copied'] = hard['copied'] and not res['builder_copied_runs']

    scan = (par + ' ' + btext).lower()
    res['hedges'] = count_lexicon(HEDGES, scan)
    st = count_lexicon(STRENGTHENERS, scan)
    res['strengtheners'] = {k: {'count': v, 'in_paper': bool(re.search(r'\b' + k + r'\b', paper_l))} for k, v in st.items()}
    res['numbers_not_in_paper'] = numbers_not_in(par + ' ' + btext, paper_flat)
    res['terms_not_in_paper'] = terms_not_in(par + ' ' + btext, paper_low)
    if a.notes:
        res['row_lints'] = row_lints(a.notes)
    res['hard'] = hard
    res['ok'] = all(hard.values())

    print(f"narrative ({mode}): {words} words [band {a.min_words}-{a.max_words}] -> {'ok' if hard['words'] else 'FAIL'}; "
          f"long paragraphs in file: {n_long}" + (f" -> {'ok' if hard.get('paragraph') else 'FAIL'}" if 'paragraph' in hard else ''))
    print(f"copied runs >= {a.run}: {len(runs)}" + (f" -> FAIL: {runs}" if runs else ' -> ok'))
    if a.builders:
        print(f"builder stems: {sum(res['builder_stems'].values())}/5 -> {'ok' if hard['builders'] else 'FAIL'} "
              f"{[k for k, v in res['builder_stems'].items() if not v]}; builder copied runs: {res['builder_copied_runs']}")
    print(f"CCERI order (advisory, keyword-based): {' '.join(seq)} -> "
          f"{'monotonic' if ok else 'not monotonic'}   [{' '.join(l or '-' for l in labels)}]")
    print(f"hedges: {res['hedges'] or 'none'}")
    print(f"strengtheners: {res['strengtheners'] or 'none'}")
    print(f"numbers not in paper (untagged): {res['numbers_not_in_paper'] or 'none'}")
    print(f"terms not in paper: {res['terms_not_in_paper'] or 'none'}")
    for l in res.get('row_lints', []):
        print('  row lint:', l)
    if a.json:
        out = json.dumps(res, indent=1, ensure_ascii=False)
        if a.json == '-':
            print('---JSON---')
            print(out)
        else:
            open(a.json, 'w', encoding='utf-8').write(out)
    return 0 if res['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
