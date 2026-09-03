# Issue CA4 — anchored / non-internal adapters with one inserted base are not found (k-mer heuristic window too short)

_Fields follow `.github/ISSUE_TEMPLATE/bug_report.md`._

**Title:** `^ADAPTER` (and `ADAPTER$`, `XADAPTER`, `ADAPTERX`) not trimmed when the read carries the adapter with an inserted base and exactly one error is allowed

**Cutadapt and Python version:** 5.2 (PyPI wheel) and `main` @ 50e9fb8d, Python 3.12.3, Linux x86-64. Reproduced on 4.3, 4.4, 4.5, 4.9, 5.0 and 5.1; not on 4.1 or 4.2 (before the k-mer heuristic of 4.3).

**How installed:** `pip install cutadapt==5.2` / `pip install -e .` from a clone of `main`.

**Command-line parameters:** `cutadapt -g ^CTGTCTCTTATACACATCT read.fastq` (default `-e 0.1`, which allows one error on this 19 nt Nextera adapter).

**Example input read** (the adapter with a `G` inserted after its third base,
followed by eight `A`):

```
@r1
CTGGTCTCTTATACACATCTAAAAAAAA
+
IIIIIIIIIIIIIIIIIIIIIIIIIIII
```

**Output Cutadapt produces:** the read is written unchanged
(`CTGGTCTCTTATACACATCTAAAAAAAA`).

**Expected output:** `AAAAAAAA`. The alignment has one error (an insertion) on 19
adapter bases, error rate 0.053 < 0.1. The same read with the non-anchored form
`-g CTGTCTCTTATACACATCT` is trimmed to `AAAAAAAA`, and with `--debug` the aligner
reports the match; only the k-mer prefilter rejects it.

**Minimal complete reproduction** (`mcve_ca4_prefilter_insertion.py`; output from
`main` and 5.2):

```python
import subprocess, tempfile, os

adapter = "CTGTCTCTTATACACATCT"
read = adapter[:3] + "G" + adapter[3:] + "AAAAAAAA"
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write(f"@r1\n{read}\n+\n{'I' * len(read)}\n")
    for spec in ("^" + adapter, adapter):
        out = subprocess.run(["cutadapt", "-g", spec, path], capture_output=True, text=True).stdout
        print(f"-g {spec:21s}: output read {out.splitlines()[-3]}")
```

```
-g ^CTGTCTCTTATACACATCT : output read CTGGTCTCTTATACACATCTAAAAAAAA (expected AAAAAAAA)
-g CTGTCTCTTATACACATCT  : output read AAAAAAAA (expected AAAAAAAA)
```

**What shrinking the example showed.** It needs (a) an anchored or non-internal
adapter (regular `-g`/`-a` are fine), (b) indels enabled (the default; with
`--no-indels` an insertion cannot match anyway), (c) an inserted base in the read,
and (d) exactly one allowed error, so that the prefilter searches two k-mer chunks:
adapters of 10–19 nt at `-e 0.1`, or any length with `-e 1`. Which insertion
positions are lost depends on the chunk: for `^ADAPTER` positions 1–8 of the 19-mer
(the first chunk), for `ADAPTER$` positions 11–18. Over all insertion positions and
random flanks, `^ADAPTER` loses 37 % (19 nt, `-e 0.1`) and 44 % (34 nt Illumina
adapter, `-e 1`) of the reads the aligner accepts; `ADAPTER$`, `XADAPTER`, `ADAPTERX`
lose 17–44 %. With three or more allowed errors (34 nt at `-e 0.1`) nothing is
lost. `-e 1` on the 34 nt adapter through the CLI: `-g ^AD` 392/700 reads trimmed,
`-g AD` 700/700.

**Cause.** `kmer_heuristic.create_back_overlap_searchsets` searches the chunks of
each error class in a window exactly as long as the class's longest adapter prefix
(`kmer_heuristic.py:114-115`, `(-length, None)`; mirrored to `(0, length)` for 5'
adapters at `:157-159`). An occurrence with an inserted base spans `length + 1`
read positions: the chunk beyond the insertion is shifted out of the window and the
chunk containing it is broken. Regular adapters are rescued by the internal search
set `(0, None)` (`:161-163`); anchored and non-internal adapters are built with
`internal=False` and have none, so `kmers_present()` returns False and `match_to`
returns `None` without aligning (`adapters.py:964-965`, `:1001-1002`).

A second, smaller blind spot of the same prefilter: for `-b` (anywhere) adapters,
reads that lie entirely inside the adapter (which the aligner matches) are rejected
— 114 of the 234 internal substrings of the Illumina adapter at `-O 3`. Not
addressed by the patch below.

**Proposed fix.** Widen each class's window by its number of allowed errors,
`(-(length + max_errors), None)` — one line; the four expected windows in
`tests/test_kmer_heuristic.py` change accordingly. Patch with tests:
`0004-Fix-k-mer-heuristic-missing-anchored-adapters-with-a.patch` (three new
`test_adapters.py` tests fail on unmodified `main`; with the patch the heuristic no
longer loses any of 2,000 / 3,500 / 2,200 accepted reads in the harness and the full
suite passes).
