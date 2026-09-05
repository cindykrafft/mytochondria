Title: bamCompare (4.0.0 Rust backend): --operation first/second/add/mean write the log2 ratio, and reciprocal_ratio is inverted

<!-- deeptools/deepTools .github/ISSUE_TEMPLATE.md checklist -->

- [x] Search whether this issue (or a similar issue) has been solved before: no prior report found (searched the open issues for bamCompare operation first/second/add/mean/log2 on the Rust backend; nothing related — the tracker has no 4.0.0 report on bamCompare's operations yet).
- [x] deepTools version: 4.0.0, `master` @ `4db9d816` ("4.0.0 cleanup (#1450)"), built with `maturin develop --release` (cargo 1.94.1) into Python 3.12.3; not present in 3.5.6 (`bamCompare_old` on the same tree is correct)
- [x] Full command producing the issue: `bamCompare -b1 A.bam -b2 B.bam -o out.bg -of bedgraph --scaleFactors 1:1 --pseudocount 0 --binSize 50 --no_collapse --operation first` (and `second`, `add`, `mean`, `reciprocal_ratio`); script below builds the BAMs
- [x] Output printed: see below

**What happens.** `calc_ratio` in `src/calc.rs` (lines 111–169) has match arms for `log2`, `ratio`, `reciprocal_ratio` and `subtract` and a catch-all `_` arm that computes the log2 ratio ("No operation is never allowed (on the py arg level, so just default to log2)"). `bamCompare2.py` still offers all eight operations (`choices=['log2', 'ratio', 'subtract', 'add', 'mean', 'reciprocal_ratio', 'first', 'second']`, line 118), so `--operation first`, `second`, `add` and `mean` silently write the same track as `--operation log2` — with the pseudocount added, so the "scaled signal of the first file" the help promises is not obtainable from the new backend at all. In the same function the `reciprocal_ratio` arm returns `den / num` when `num / den >= 1` and `-num / den` otherwise (lines 137–148), the inverse of the documented rule ("the negative of the inverse of the ratio if the ratio is less than 0", i.e. a/b if a/b ≥ 1 else −b/a, which `getRatio.py` implements and doctests in 3.5.x): 3/2 comes out as 0.67 instead of 1.5 and 2/3 as −0.33 instead of −3.

**Minimal script** (two single-end BAMs on a 300-bp chromosome; A has 3, 1, 2 reads and B 2, 3, 2 reads in the bins at 0, 100 and 200 bp; every operation compared with its definition):

```python
import os, subprocess, sys, tempfile
import numpy as np, pysam

BIN = os.path.dirname(sys.executable)
d = tempfile.mkdtemp()
A_counts = np.array([3, 0, 1, 0, 2, 0], dtype=float)   # reads per 50-bp bin
B_counts = np.array([2, 0, 3, 0, 2, 0], dtype=float)

def write_bam(path, counts):
    with pysam.AlignmentFile(path, "wb", reference_names=["chr1"], reference_lengths=[300]) as fh:
        n = 0
        for b, c in enumerate(counts):
            for _ in range(int(c)):
                a = pysam.AlignedSegment()
                a.query_name = "r%d" % n; n += 1
                a.query_sequence = "A" * 50
                a.flag = 0; a.reference_id = 0; a.reference_start = 50 * b
                a.mapping_quality = 30; a.cigar = ((0, 50),)
                a.query_qualities = pysam.qualitystring_to_array("I" * 50)
                fh.write(a)
    pysam.index(path)

write_bam(os.path.join(d, "A.bam"), A_counts)
write_bam(os.path.join(d, "B.bam"), B_counts)
with np.errstate(divide="ignore", invalid="ignore"):
    ratio = A_counts / B_counts
    expected = {"log2": np.log2(ratio), "ratio": ratio,
                "reciprocal_ratio": np.where(ratio >= 1, ratio, -1.0 / ratio),   # a/b if a/b >= 1 else -b/a
                "subtract": A_counts - B_counts, "first": A_counts, "second": B_counts,
                "add": A_counts + B_counts, "mean": (A_counts + B_counts) / 2.0}
wrong = []
for op in ["log2", "ratio", "subtract", "reciprocal_ratio", "first", "second", "add", "mean"]:
    out = os.path.join(d, op + ".bg")
    subprocess.run([os.path.join(BIN, "bamCompare"), "-b1", os.path.join(d, "A.bam"), "-b2", os.path.join(d, "B.bam"),
                    "-o", out, "-of", "bedgraph", "--scaleFactors", "1:1", "--pseudocount", "0", "--binSize", "50",
                    "--no_collapse", "--operation", op, "-p", "1"], check=True, capture_output=True)
    got = np.array([float(l.split()[3]) for l in open(out)])
    exp = expected[op]
    ok = np.allclose(np.nan_to_num(got, nan=0, posinf=1e9, neginf=-1e9), np.nan_to_num(exp, nan=0, posinf=1e9, neginf=-1e9), atol=0.011)
    print("--operation %-16s got %-40s expected %s%s" % (op, np.round(got, 2), np.round(exp, 2), "" if ok else "   <- WRONG"))
    if not ok:
        wrong.append(op)
print("operations with wrong output:", wrong)
assert not wrong
```

**Output** (4.0.0 @ `4db9d816`):

```
bamCompare 4.0.0
--operation log2             got [ 0.58   nan -1.58   nan  0.     nan]    expected [ 0.58   nan -1.58   nan  0.     nan]
--operation ratio            got [1.5   nan 0.33  nan 1.    nan]          expected [1.5   nan 0.33  nan 1.    nan]
--operation subtract         got [ 1.  0. -2.  0.  0.  0.]                expected [ 1.  0. -2.  0.  0.  0.]
--operation reciprocal_ratio got [ 0.67   nan -0.33   nan  1.     nan]    expected [ 1.5  nan -3.   nan  1.   nan]   <- WRONG
--operation first            got [ 0.58   nan -1.58   nan  0.     nan]    expected [3. 0. 1. 0. 2. 0.]   <- WRONG
--operation second           got [ 0.58   nan -1.58   nan  0.     nan]    expected [2. 0. 3. 0. 2. 0.]   <- WRONG
--operation add              got [ 0.58   nan -1.58   nan  0.     nan]    expected [5. 0. 4. 0. 4. 0.]   <- WRONG
--operation mean             got [ 0.58   nan -1.58   nan  0.     nan]    expected [2.5 0.  2.  0.  2.  0. ]   <- WRONG
operations with wrong output: ['reciprocal_ratio', 'first', 'second', 'add', 'mean']
AssertionError
```

The same happens on the shipped `testA.bam`/`testB.bam` with the default pseudocount: `first`, `second`, `add` and `mean` are byte-identical to the `log2` output (`3R 0 50 0 | 3R 50 100 -1 | 3R 100 150 0 | 3R 150 200 -0.58`), and `reciprocal_ratio` gives `1, -0.5, 1, -0.67` where 3.5.6 gives `1, -2, 1, -1.5`. `bamCompare_old` is right in every case.

**Fix.** Four explicit arms for `first`, `second`, `add` and `mean` returning the scaled signal(s) without a pseudocount (as 3.5.x did, and as the `--pseudocount` help says: "Only useful together with --operation log2 or --operation ratio"), the `reciprocal_ratio` branches swapped, and the catch-all made a panic so an unknown operation can no longer produce a plausible-looking track. The existing `test_calc_ratio` pins the inverted value (`-0.27` for 6/22; the documented rule gives −22/6 = −3.67), so that expectation changes with the fix. A PR with the fix, two cargo tests and a pytest over all five operations on `testA`/`testB` follows.

One thing I left alone but want to flag: the `subtract` arm also adds the pseudocounts before subtracting (`num - den` with both pseudocounts), which is invisible at the default `--pseudocount 1` but shifts every value by `p1 − p2` with two different pseudocounts; 3.5.x subtracted the scaled signals only.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/deeptools)

---
_Generated by [Claude Code](https://claude.ai/code)_
