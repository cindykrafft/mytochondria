# Issue CA2 — `--max-expected-errors` and `--max-average-error-rate` ignore `--quality-base`

_Fields follow `.github/ISSUE_TEMPLATE/bug_report.md`._

**Title:** `--max-ee` / `--max-aer` always assume Phred+33; with `--quality-base 64` nothing is discarded

**Cutadapt and Python version:** 5.2 (PyPI wheel) and `main` @ 50e9fb8d, Python 3.12.3, Linux x86-64. Also reproduced on the 4.1, 4.2, 4.3, 4.4, 4.5, 4.9, 5.0 and 5.1 wheels.

**How installed:** `pip install cutadapt==5.2` / `pip install -e .` from a clone of `main`.

**Command-line parameters:** `cutadapt --max-ee 1 --quality-base 64 read.fastq`

**Example input read** (50 nt, every quality character `B` = Phred 2 in Phred+64
encoding, i.e. 50 × 10^−0.2 = 31.5 expected errors):

```
@r1
ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTAC
+
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
```

**Output Cutadapt produces:** the read is written; `Reads discarded as too many
expected errors` is not reported / 0.

**Expected output:** no read written (31.5 expected errors > 1).

**Minimal complete reproduction** (`mcve_ca2_max_ee_quality_base.py`; output from
`main` and 5.2 is identical):

```python
import subprocess, tempfile, os

read = "ACGT" * 12 + "AC"
qualities = chr(2 + 64) * 50  # Phred 2, Phred+64 encoding
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write(f"@r1\n{read}\n+\n{qualities}\n")
    out = subprocess.run(["cutadapt", "--max-ee", "1", "--quality-base", "64", path],
                         capture_output=True, text=True).stdout
    print(f"--max-ee 1 --quality-base 64: {out.count('@r1')} read(s) written")
    out = subprocess.run(["cutadapt", "-q", "20", "--quality-base", "64", path],
                         capture_output=True, text=True).stdout
    print(f"-q 20 --quality-base 64 (control): read trimmed to {len(out.splitlines()[-3])} nt")
```

```
--max-ee 1 --quality-base 64: 1 read(s) written (expected 0: 31.5 expected errors > 1)
-q 20 --quality-base 64 (control): read trimmed to 0 nt (expected 0: every base is below Q20)
```

**What shrinking the example showed.** Any Phred+64 file behaves the same: on
2,000 random reads (Phred 2–40, 50–150 nt) `--max-ee 0.5 / 1 / 2` and `--max-aer
0.01 / 0.02` keep all 2,000 with `--quality-base 64`, while the same reads encoded
as Phred+33 and filtered with the default base give exactly the Python reference
(0 / 0 / 2 kept). `-q` with `--quality-base 64` is correct, so the offset is only
lost for the two expected-error filters. The predicate computes 0.0058 expected
errors for a read whose true value is 7.26 (every quality read 31 too high).

**Cause.** `TooManyExpectedErrors.test` and `TooHighAverageErrorRate.test` call
`expected_errors(read.qualities)` with the default `base=33`
(`predicates.py:70-71`, `:91-95`), and `cli.py:762` / `:777` construct them without
`args.quality_base`, whereas `QualityTrimmer` and `NextseqQualityTrimmer` receive it
(`cli.py:941`, `:1058`).

**Proposed fix.** A `quality_base` parameter on both predicates, passed from the
CLI. Patch with two tests: `0002-Make-max-ee-and-max-aer-honour-quality-base.patch`
(tests fail on unmodified `main`, full suite passes with the patch).
