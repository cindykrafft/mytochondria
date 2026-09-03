#!/usr/bin/env python3
"""DT7: --ignoreDuplicates alone does not enter the normalisation denominator.

getScaleFactor.fraction_kept returns 1.0 early when --minMappingQuality,
--samFlagInclude, --samFlagExclude, --minFragmentLength and --maxFragmentLength
are all unset; it does not test --ignoreDuplicates (and --exactScaling cannot
override the early return). The per-bin counts are deduplicated, but the
"number of mapped reads" used by CPM, RPKM, RPGC and BPM, and by bamCompare's
--scaleFactorsMethod readCount, is the count before duplicate removal. Adding
any other filter (e.g. --minMappingQuality 1 on reads that all pass) makes the
sampler run and the denominator deduplicated.

Two single-end BAMs, every read MAPQ 30: sample A with 40 % exact duplicates
(same start and strand), sample B with none. Compares bamCoverage CPM tracks
and bamCompare readCount factors with the closed form.
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
            reads.append(S.se_read(0, starts[i], RL, bool(rev[i]), "%sd%d" % (prefix, i)))
            frags.append((int(starts[i]), int(starts[i]) + RL, bool(rev[i])))
    return reads, frags


def dedup(frags):
    seen, out = set(), []
    for f in frags:
        if (f[0], f[2]) in seen:
            continue
        seen.add((f[0], f[2]))
        out.append(f)
    return out


ra, fa = make(6000, 0.67, "a")
rb, fb = make(6000, 0.0, "b")
bamA = S.write_bam(os.path.join(d, "A.bam"), [("chr1", L)], ra)
bamB = S.write_bam(os.path.join(d, "B.bam"), [("chr1", L)], rb)
nA, nB = len(fa), len(fb)
dA, dB = dedup(fa), dedup(fb)
print("sample A: %d reads, %d after duplicate removal (%.1f%% duplicates); sample B: %d reads, %d after"
      % (nA, len(dA), 100.0 * (nA - len(dA)) / nA, nB, len(dB)))
countsA = S.bin_overlap_counts(dA, L, BS)


def cpm(extra):
    out = os.path.join(d, "c%d.bw" % (abs(hash(tuple(extra))) % 10**8))
    r = subprocess.run([S.tool("bamCoverage"), "-b", bamA, "-o", out, "-bs", str(BS), "-p", "1", "--normalizeUsing", "CPM",
                        "--verbose"] + extra, capture_output=True, text=True)
    fac = float(re.search(r"Final scaling factor: ([0-9.e+-]+)", r.stdout + r.stderr).group(1))
    return S.read_bigwig_per_base(out, "chr1", L)[::BS], fac


print("\n%-58s %-14s %-16s %s" % ("bamCoverage on A", "scale factor", "1e6/mapped used", "track = dedup counts * 1e6 / dedup mapped?"))
for extra in [["--ignoreDuplicates"], ["--ignoreDuplicates", "--exactScaling"], ["--ignoreDuplicates", "--minMappingQuality", "1"],
              ["--ignoreDuplicates", "--minMappingQuality", "1", "--exactScaling"]]:
    t, fac = cpm(extra)
    ref = countsA * 1e6 / len(dA)
    print("%-58s %-14.4f %-16.0f %s (max rel diff %.1e; 1e6/%d = %.4f, 1e6/%d = %.4f)"
          % (" ".join(extra), fac, 1e6 / fac, np.allclose(t, ref, rtol=1e-3), np.max(np.abs(t - ref) / np.maximum(ref, 1e-9)),
             len(dA), 1e6 / len(dA), nA, 1e6 / nA))

print("\nbamCompare --scaleFactorsMethod readCount (A vs B):")
for extra in [["--ignoreDuplicates"], ["--ignoreDuplicates", "--minMappingQuality", "1"]]:
    r = subprocess.run([S.tool("bamCompare"), "-b1", bamA, "-b2", bamB, "-o", os.path.join(d, "x.bw"), "-bs", str(BS), "-p", "1",
                        "--verbose"] + extra, capture_output=True, text=True)
    m = re.search(r"Size factors using total number of mapped reads: \[([^\]]*)\]", r.stdout + r.stderr)
    got = [float(x) for x in m.group(1).split()]
    exp_dd = [min(len(dA), len(dB)) / len(dA), min(len(dA), len(dB)) / len(dB)]
    exp_raw = [min(nA, nB) / nA, min(nA, nB) / nB]
    print("  %-48s factors %s; from deduplicated counts %s; from raw counts %s"
          % (" ".join(extra), np.round(got, 4), np.round(exp_dd, 4), np.round(exp_raw, 4)))
