#!/usr/bin/env python3
"""DT7 on 4.0.0: --ignoreDuplicates no longer exists in bamCoverage/bamCompare
(CHANGES.txt 4.0.0: "Duplicate reads can be removed via the --samFlagExclude
option"). This checks that the documented replacement, --samFlagExclude 1024 on
a BAM with marked duplicates, enters the normalisation denominator: the Rust
pileup (src/covcalc.rs, bam_pileup) counts `mapped` after filter_record, so the
CPM factor and the readCount factors should use the deduplicated count.

Sample A: 6000 unique reads plus ~40 % exact duplicates carrying flag 0x400;
sample B: 6000 reads, no duplicates.
"""
import os
import re
import subprocess
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(61)
d = S.tmpdir()
L = 200000
BS, RL = 50, 50


def make(n_unique, dup_frac, prefix):
    starts = rng.integers(0, L - RL, n_unique)
    rev = rng.random(n_unique) < 0.5
    reads, frags = [], []
    for i in range(n_unique):
        reads.append(S.se_read(0, starts[i], RL, bool(rev[i]), "%s%d" % (prefix, i)))
        frags.append((int(starts[i]), int(starts[i]) + RL, bool(rev[i])))
        if rng.random() < dup_frac:
            r = S.se_read(0, starts[i], RL, bool(rev[i]), "%sd%d" % (prefix, i))
            r.flag |= 0x400          # marked duplicate
            reads.append(r)
            frags.append((int(starts[i]), int(starts[i]) + RL, bool(rev[i])))
    return reads, frags


ra, fa = make(6000, 0.67, "a")
rb, fb = make(6000, 0.0, "b")
bamA = S.write_bam(os.path.join(d, "A.bam"), [("chr1", L)], ra)
bamB = S.write_bam(os.path.join(d, "B.bam"), [("chr1", L)], rb)
nA, nB = len(fa), len(fb)
dA = [f for f, r in zip(fa, ra) if not (r.flag & 0x400)]
print("sample A: %d reads, %d unmarked (%.1f%% marked duplicates); sample B: %d reads" % (nA, len(dA), 100.0 * (nA - len(dA)) / nA, nB))
countsA = S.bin_overlap_counts(dA, L, BS)

print("\n%-40s %-14s %-16s %s" % ("bamCoverage on A, CPM", "scale factor", "1e6/factor", "track = dedup counts * 1e6 / dedup mapped (to the 2-decimal output rounding)?"))
for extra in [[], ["--samFlagExclude", "1024"]]:
    out = os.path.join(d, "c%d.bw" % len(extra))
    r = subprocess.run([S.tool("bamCoverage"), "-b", bamA, "-o", out, "-bs", str(BS), "-p", "1", "--normalizeUsing", "CPM",
                        "--verbose"] + extra, capture_output=True, text=True)
    fac = float(re.search(r"Scale factor: ([0-9.e+-]+)", r.stdout + r.stderr).group(1))
    t = S.read_bigwig_per_base(out, "chr1", L)[::BS]
    ref = countsA * 1e6 / len(dA)
    print("%-40s %-14.4f %-16.0f %s (max |diff| %.3g; 1e6/%d = %.4f, 1e6/%d = %.4f)"
          % (" ".join(extra) or "(no filter)", fac, 1e6 / fac, np.allclose(t, ref, atol=0.0051), np.max(np.abs(t - ref)),
             len(dA), 1e6 / len(dA), nA, 1e6 / nA))

print("\nbamCompare --scaleFactorsMethod readCount (A vs B):")
for extra in [[], ["--samFlagExclude", "1024"]]:
    r = subprocess.run([S.tool("bamCompare"), "-b1", bamA, "-b2", bamB, "-o", os.path.join(d, "x.bw"), "-bs", str(BS), "-p", "1",
                        "--verbose"] + extra, capture_output=True, text=True)
    m = re.search(r"scale factor1 = ([0-9.e+-]+), scale factor2 = ([0-9.e+-]+)", r.stdout + r.stderr)
    got = [float(m.group(1)), float(m.group(2))]
    exp_dd = [min(len(dA), nB) / len(dA), min(len(dA), nB) / nB]
    exp_raw = [min(nA, nB) / nA, min(nA, nB) / nB]
    print("  %-28s factors %s; from deduplicated counts %s; from raw counts %s"
          % (" ".join(extra) or "(no filter)", np.round(got, 4), np.round(exp_dd, 4), np.round(exp_raw, 4)))
