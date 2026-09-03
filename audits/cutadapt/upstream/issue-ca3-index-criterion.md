# Issue CA3 — demultiplexing index picks the best adapter by number of matches, `--no-index` by alignment score

_Fields follow `.github/ISSUE_TEMPLATE/bug_report.md`._

**Title:** Adapter index chooses the adapter with the most matching bases, not the best alignment score; same read is assigned differently with `--no-index`

**Cutadapt and Python version:** 5.2 (PyPI wheel) and `main` @ 50e9fb8d, Python 3.12.3, Linux x86-64. Also reproduced on 5.0 and 5.1; not on 4.1, 4.2, 4.3, 4.4, 4.5 or 4.9, which assign the read as `--no-index` does — it came in with the 5.0 index changes (#827).

**How installed:** `pip install cutadapt==5.2` / `pip install -e .` from a clone of `main`.

**Command-line parameters:**
`cutadapt -e 0.1 -g A=^ACGTACGTACGT -g B=^ACGTACGTACA -o {name}.fastq read.fastq`
and the same with `--no-index`.

**Example input read** (starts with `ACGTACGTACAGT`: that is barcode B
(`ACGTACGTACA`, 11 nt) exactly — 11 matches, 0 errors, score 11 — and barcode A
(`ACGTACGTACGT`, 12 nt) with one inserted base — 12 matches, 1 indel, score
12 − 2 = 10):

```
@r1
ACGTACGTACAGTTTTTTTTTTTTTTTTTTTTT
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
```

**Output Cutadapt produces:** default (index): the read is written to `A.fastq`
with the info `score=12 errors=1`. With `--no-index`: written to `B.fastq`,
`score=11 errors=0`.

**Expected output:** the same assignment in both modes. The documented criterion
("Alignment algorithm changes in Cutadapt 4": the score with match +1, mismatch −1,
indel −2 "is used to decide which of the overlaps … is the best one") gives B; the
index applies the pre-4.0 "maximal number of matches" rule that the same page
describes as replaced.

**Minimal complete reproduction** (`mcve_ca3_index_criterion.py`; output from
`main` and 5.2):

```python
import subprocess, tempfile, os

read = "ACGTACGTACAGT" + "T" * 20
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write(f"@r1\n{read}\n+\n{'I' * len(read)}\n")
    for extra in ([], ["--no-index"]):
        d = os.path.join(tmp, "noindex" if extra else "index")
        os.mkdir(d)
        subprocess.run(["cutadapt", "--quiet", "-e", "0.1", "-g", "A=^ACGTACGTACGT",
                        "-g", "B=^ACGTACGTACA", *extra, "-o", os.path.join(d, "{name}.fastq"), path], check=True)
        assigned = [n for n in ("A", "B", "unknown")
                    if os.path.exists(os.path.join(d, n + ".fastq")) and os.path.getsize(os.path.join(d, n + ".fastq"))]
        print(f"{'--no-index' if extra else 'default   '}: read written to {assigned}.fastq")
```

```
default   : read written to ['A'].fastq
--no-index: read written to ['B'].fastq
```

**What shrinking the example showed.** Two barcodes of different length where one
is the other's prefix plus a substitution (`B = A[:10] + X`) reproduce it
deterministically in both list orders. On random barcode sets (6 barcodes of 10–12
nt, 10,000 reads with one random edit, `-e 1`) the index and the score rule agree
on every read; with six 10-nt barcodes they disagree on 2 of 10,000 (score ties,
broken by errors-then-length in the index and by list order in `MultipleAdapters`).
Independently of the assignment, the `score` recorded for every indexed match is the
number of matches (10 for a barcode matched with one insertion, where the aligner
gives 8), so a list that mixes indexed barcodes with a regular adapter compares
different quantities: `-g ^bc1 -g ^bc2 -a ADAPTER` on a read carrying bc1 with an
insertion plus 9 nt of the 3' adapter trims the barcode by default (score field 10)
and the 3' adapter with `--no-index` (score 9).

**Cause.** `AdapterIndex._make_index` stores `(adapter, errors, matches)`
(`adapters.py:1421-1442`), `_match_to_multiple_lengths` ranks by `matches`
(`:1522`) and both pass `matches` into the `score` slot of the `Match`
(`:1490`, `:1533`); `_lookup_with_n` (`:1535-1551`) returns `match.score` into the
same slot, so the index is inconsistent with itself as well.
`MultipleAdapters.match_to` (`:1278-1284`) ranks by score.

**Proposed fix.** Store the alignment score in the index (it follows from errors,
matches and the two lengths), rank and detect ambiguity by score, keep the 5.0
behaviour of not assigning ambiguous reads. Patch with tests:
`0003-Choose-the-best-adapter-by-alignment-score-also-when.patch`. Because this
changes which reads count as ambiguous, I am raising it as an issue before opening
the PR.
