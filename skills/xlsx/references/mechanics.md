# Mechanics — the file format, and where it lies to you

## 1. The two loads

```python
wf = openpyxl.load_workbook(p)                  # formula cells -> "=SUM(G6:R6)"
wv = openpyxl.load_workbook(p, data_only=True)  # formula cells -> cached value, or None
```

There is no load that gives you both. **Read the file twice.** `scripts/show.py` does exactly this and prints
`formulas: N   with a cached value: N   MISSING: N`.

| symptom | cause |
|---|---|
| a numeric filter sums a column to `0.0` | loaded without `data_only`; every cell was a formula *string* and got discarded as non-numeric |
| every figure reads `None` / blank | loaded with `data_only=True` on a file LibreOffice has not recalculated |
| a validator reports zeroes and passes | both of the above, combined with a filter that treats missing as 0 |

**Prefer to sum the literals the generator wrote** (e.g. a week grid) over a formula column that sums them.
Bound the range explicitly and assert the headers — a generator that appends three more numeric columns after
the grid inflates a `max_column` sum by hundreds and does it silently.

## 2. openpyxl discards cached values on load+save

openpyxl cannot evaluate a formula. On load+save it rewrites the formula string and **drops the cached value
LibreOffice put there**. The file still opens, non-formula sheets still look right, and no gate notices.

**Consequence for pipeline order — this is the rule the whole chain hangs on:**

```
generate → post-passes → RECALCULATE → read-back gates → (any further openpyxl write → RECALCULATE AGAIN)
```

Any script that opens the workbook must run *before* the recalculation, or the recalculation must run again
after it. A build that recalculates and then merges sheets ships blank figures.

## 3. Recalculating headlessly

```bash
SCRATCH=$(mktemp -d)
soffice --headless --convert-to xlsx --outdir "$SCRATCH" "$F"
cp "$SCRATCH/$(basename "$F")" "$F"
```

⛔ **`--outdir` at the input's own directory fails.** Measured:

```
Overwriting: C:\...\t.xlsx
Error: Please verify input parameters... (SfxBaseModel::impl_store <file:///...> failed:
       0x4c0c(Error Area:Sfx Class:Write Code:12))
exit 1     md5 of the input: UNCHANGED
```

The word *Overwriting* reads as success. The exit code is 1 — but `soffice … | tail -2` returns *tail's*
status, which is how this went unnoticed. Do not pipe the recalculation.

**Check for an open-file lock first.** Before rebuilding or recalculating, look for `.~lock.<name>#`
(LibreOffice) or `~$<name>` (Excel) beside the file. If one exists the user has it open: write to a new
name and say so. (derived: LSP 2026-10-08 — recalculation could not replace a workbook open in LibreOffice.)

On Windows LibreOffice is frequently **off `PATH`**: probe `"/c/Program Files/LibreOffice/program/soffice.exe"`
before concluding it is missing.

## 4. Two writers, two file shapes

Measured across nine workbooks from one engagement:

| | openpyxl 3.1.5 | LibreOffice (after recalc) |
|---|---|---|
| `xl/sharedStrings.xml` | **absent** | present |
| text storage | `t="inlineStr"` + `<is><t>` in the worksheet | shared-string index, `t="s"` |
| non-ASCII | **numeric character references**, `&#7842;` | literal UTF-8 |
| `docProps/app.xml` | `Microsoft Excel Compatible / Openpyxl 3.1.5` | `LibreOffice/…` |
| `xl/calcChain.xml` | absent | absent (in these files) |

Two things follow.

- **A regex over raw XML must `html.unescape` first**, or it is blind to every non-ASCII string in an
  openpyxl-written file. Use `html.unescape`, not a hand-rolled list of the five named entities.
- **Any tool that patches `sharedStrings.xml` only works on a recalculated workbook.** Check for the part
  before assuming the text is there.

`docProps/app.xml` tells you which writer produced the bytes in front of you. Read it first when a file
behaves unexpectedly.

## 5. Text lives in about twenty places

A cell walk sees one. To answer *"does this string appear anywhere in this file"*, iterate the zip:

```python
with zipfile.ZipFile(path) as z:
    for m in z.namelist():
        if m.lower().endswith((".xml", ".rels")):
            text = html.unescape(re.sub(r"<[^>]+>", " ",
                                        z.read(m).decode("utf-8", "replace")))
```

Keep element boundaries as spaces or adjacent runs fuse into one word. The parts that carry reader-visible
text: `sharedStrings`, worksheet inline strings, **cached formula results** (an `iter_rows` reports the
formula, never the value the reader sees), sheet names in `workbook.xml`, `docProps/core|app|custom`,
headers/footers, defined names, comments, data-validation prompts, conditional formats, hyperlinks and their
tooltips, drawings, charts, tables, and number formats carrying quoted literals.

`scripts/show.py --grep PATTERN` is this loop.

## 6. Patching prose in a finished workbook

When the only change is wording, a full rebuild + double recalculation is ~90 s and risks the cached values.
Editing **one zip entry** is under a second. The safe shape:

- Rewrite the zip copying **every** other entry through unchanged, preserving name order and compression type.
- **Never touch a worksheet XML** — that is what keeps the cached values alive.
- **REFUSE to add or remove an `<si>`.** Indices shift; every later worksheet reference breaks. This is the
  boundary that makes the tool prose-only: it can change the text of a cell that already has text, and
  nothing else. No new rows, no captions in empty cells, no layout.
- **REFUSE a rich-text `<si>`** (more than one `<t>` run) — replacing the text silently drops the runs.
- **REFUSE an ambiguous `--find`** unless `--all` is passed, and report the refcount and owning sheets.
- Escape `&`, `<`, `>` on write; preserve `xml:space="preserve"`.
- Verify after writing: reopen, confirm the new text, and confirm a formula sheet **still has cached values**.

**Prerequisites to check, not assume:** no `xl/calcChain.xml`; no caption text inside any `<f>` element; no
formula containing a quoted string literal; `sharedStrings.xml` present at all (see §4).

⚠ **Row heights are explicit** (`<row ht="…">`) and live in worksheet XML, which this route will not touch, so
a materially longer replacement clips. Warn above ~80 characters of growth; substantial rewrites go through
the generator.

⛔ **The real hazard is divergence, not corruption.** A patched workbook whose generator still holds the old
sentence reverts silently on the next rebuild and **no ordinary gate notices**. Record every patch — file,
timestamp, old text, new text, and the generator file+line the operator must also edit — and wire a `--check`
that re-reads each record against both the workbook and the generator source into the gate suite.

## 7. Money that adds up

Round a column with **largest remainder**, never cell-by-cell:

```python
def apportion(exact, target):
    floors = [int(v) for v in exact]
    short  = int(round(target)) - sum(floors)
    order  = sorted(range(len(exact)), key=lambda i: exact[i] - floors[i], reverse=True)
    for i in order[:max(0, short)]:
        floors[i] += 1
    assert sum(floors) == int(round(target))
    return floors
```

A one-dollar gap between a printed column and its printed total is not trivial to the person checking it: they
cannot tell a rounding artifact from an error, so they distrust the whole sheet. Printing cents closes the
arithmetic and destroys readability, which is the opposite trade.

**And the addition chain must be visible.** If 19 rows sum to 36,599 and the total says 72,766, the 36,166
that bridges them needs its own labelled subtotal row — not an unlabelled one above the total.

## 8. Encoding on stdout

Every saved script starts:

```python
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
```

Windows consoles default to cp1252 and raise `UnicodeEncodeError` on `⚠`, `⛔`, `→`, Vietnamese diacritics —
10% of all tool errors in one measured corpus, applied inconsistently because it was re-typed per call.

⚠ **A backslash literal never goes through a shell heredoc.** The Bash tool collapses `\\` → `\` inside a
quoted heredoc, so `s.replace("\\", "/")` arrives as a SyntaxError. Write the script to a file, or use
`chr(92)`.
