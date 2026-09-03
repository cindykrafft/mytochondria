# Issue CA1 — `-e 1` allows no errors at all for a 49 nt adapter (floating-point rounding of N/n)

_Fields follow `.github/ISSUE_TEMPLATE/bug_report.md` (Cutadapt and Python version;
how installed; command-line parameters; example read; output; expected output)._

**Title:** Absolute number of errors (`-e N`) is one too small for some adapter lengths (e.g. `-e 1` allows 0 errors for a 49 nt adapter)

**Cutadapt and Python version:** 5.2 (PyPI wheel) and `main` @ 50e9fb8d, Python 3.12.3, Linux x86-64. Also reproduced on the 4.1, 4.2, 4.3, 4.4, 4.5, 4.9, 5.0 and 5.1 wheels.

**How installed:** `pip install cutadapt==5.2` / `pip install -e .` from a clone of `main`.

**Command-line parameters:** `cutadapt -e 1 -a CAGATTTTCATATTATGCAGAAAATCTACTTCGCCTGATACGAGTCGGT read.fastq`

**Example input read** (the 49 nt adapter with one substitution at position 20, `A` → `T`, between four `G` on each side):

```
@r1
GGGGCAGATTTTCATATTATGCAGTAAATCTACTTCGCCTGATACGAGTCGGTGGGG
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
```

**Output Cutadapt produces:** the read is written unchanged (57 nt); the report says
`Reads with adapters: 0 (0.0%)`.

**Expected output:** `GGGG` (4 nt): the adapter occurs in full with one error, and
`-e 1` should allow one error ("using `-e 2` will set the maximum error rate to
0.2 for an adapter of length 10", user guide, "Error tolerance").

**Minimal complete reproduction** (`mcve_ca1_absolute_errors.py`, synthetic read
made in the script; output pasted from a run on `main` and on 5.2):

```python
import subprocess, tempfile, os

adapter = "CAGATTTTCATATTATGCAGAAAATCTACTTCGCCTGATACGAGTCGGT"  # 49 nt
occurrence = adapter[:20] + "T" + adapter[21:]  # one substitution
read = "GGGG" + occurrence + "GGGG"
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write(f"@r1\n{read}\n+\n{'I' * len(read)}\n")
    for e in ("1", "1.0000001"):
        out = subprocess.run(["cutadapt", "-e", e, "-a", adapter, path],
                             capture_output=True, text=True).stdout
        print(f"-e {e}: output read {out.splitlines()[-3]}")
```

```
-e 1: output read GGGGCAGATTTTCATATTATGCAGTAAATCTACTTCGCCTGATACGAGTCGGTGGGG (57 nt; expected 4 nt 'GGGG')
-e 1.0000001: output read GGGG (4 nt; expected 4 nt 'GGGG')
```

**What shrinking the example showed.** The read content does not matter, only the
adapter length and the value of `-e`: `-e 1` fails for lengths 49, 98, 103, 107,
161, 187, 196, 197, 206, 214, 237, 239, 249 and 253 (up to 300), `-e 2` for the same
lengths, `-e 3` for 47, 94, 147, 173, 188 and 294, `-e 5` for 77 and 154; `-e 1`
works for 48 and 50. Decimal rates typed by users (0.05 … 0.3) are not affected at
any length up to 300 (`-e 0.29` is, at 100 and 200). The same happens for 5'
adapters, anchored adapters with and without `--no-indels`, adapters with `N`
wildcards (the non-N length counts), and the demultiplexing index (`-e 1` on two
49 nt barcodes builds an index with `k = 0`).

**Cause.** `SingleAdapter.__init__` converts `-e N` to the rate `N / len`
(`adapters.py:580-582`). The aligner then floors `max_error_rate * m`
(`_align.pyx:343`) and accepts `cost <= length * max_error_rate` (`:513`, `:559`);
`PrefixComparer` floors it too (`:633`), as do `AdapterIndex` (`adapters.py:1378`,
`:1400`, `:1418`) and the k-mer heuristic (`kmer_heuristic.py:95`, `:142`). In
double precision `49 * (1 / 49) == 0.9999999999999999`, so the product floors to
0 and the comparison `1 <= 0.9999999999999999` fails.

**Proposed fix.** Add a small tolerance (1e-9, far below the resolution of any
meaningful rate) to every `length * rate` product, through one helper
(`max_errors_for_length()` in `align.py`) and a `DEF` constant in `_align.pyx`. Patch
with tests: `0001-Honour-an-absolute-number-of-errors-e-N-for-every-ad.patch`
(the new tests fail on unmodified `main`, the full suite passes with the patch). An
exact alternative would be to keep the integer N and the length and compare
`errors * len <= L * N` inside the aligner; happy to rework the patch that way if
preferred.
