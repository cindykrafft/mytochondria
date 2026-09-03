#!/usr/bin/env python3
"""Held-up checks for bamCompare: --scaleFactorsMethod readCount (default),
--scaleFactors a:b, --scaleFactorsMethod None --normalizeUsing CPM, every
--operation, --pseudocount with one and two values, and the SES scale factors
on data with a known background ratio.

Reference: reads per bin from the fragment lists (numpy), readCount factors
min(n1, n2) / n as documented, getRatio's arithmetic written out by hand.
"""
import os
import re
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(31)
d = S.tmpdir()
L = 300000
BS = 50
# sample 2: uniform background; sample 1: the same background depth plus reads in 5 % of the genome
w1 = np.ones(L)
peaks = np.zeros(L, bool)
for p in rng.integers(0, L - 3000, 5):
    peaks[p:p + 3000] = True
r2, f2 = S.random_se_reads(rng, 0, L, 20000, 50, "b")
r1a, f1a = S.random_se_reads(rng, 0, L, 20000, 50, "a")
r1b, f1b = S.random_se_reads(rng, 0, L, 10000, 50, "c", weights=peaks.astype(float))
bam1 = S.write_bam(os.path.join(d, "b1.bam"), [("chr1", L)], r1a + r1b)
bam2 = S.write_bam(os.path.join(d, "b2.bam"), [("chr1", L)], r2)
f1 = f1a + f1b
c1 = S.bin_overlap_counts(f1, L, BS).astype(float)
c2 = S.bin_overlap_counts(f2, L, BS).astype(float)
n1, n2 = len(f1), len(f2)


def ref(op, sf, pc):
    v1, v2 = sf[0] * c1, sf[1] * c2
    if op in ("log2", "ratio", "reciprocal_ratio"):
        r = (v1 + pc[0]) / (v2 + pc[1])
        if op == "log2":
            return np.log2(r)
        if op == "reciprocal_ratio":
            return np.where(r >= 1, r, -1.0 / r)
        return r
    return {"subtract": v1 - v2, "add": v1 + v2, "mean": (v1 + v2) / 2, "first": v1, "second": v2}[op]


def run(extra):
    out = os.path.join(d, "o%d.bw" % (abs(hash(tuple(extra))) % 10**8))
    _, err = S.run(["bamCompare", "-b1", bam1, "-b2", bam2, "-o", out, "-bs", BS, "-p", 1] + extra)
    return S.read_bigwig_per_base(out, "chr1", L)[::BS], err


def report(name, got, expected):
    ok = np.allclose(np.nan_to_num(got), expected, rtol=1e-5, atol=1e-6)
    print("%-70s %s (max |diff| %.2e)" % (name, "OK" if ok else "MISMATCH", np.max(np.abs(np.nan_to_num(got) - expected))))


sf_rc = (min(n1, n2) / n1, min(n1, n2) / n2)
print("mapped reads %d / %d -> readCount factors %s" % (n1, n2, np.round(sf_rc, 6)))
for op in ["log2", "ratio", "subtract", "add", "mean", "reciprocal_ratio", "first", "second"]:
    got, _ = run(["--operation", op])
    report("readCount, --operation %s, pseudocount 1" % op, got, ref(op, sf_rc, (1, 1)))
got, _ = run(["--operation", "log2", "--pseudocount", "0.5", "2"])
report("readCount, log2, --pseudocount 0.5 2", got, ref("log2", sf_rc, (0.5, 2)))
got, _ = run(["--operation", "ratio", "--pseudocount", "0"])
report("readCount, ratio, --pseudocount 0 (0/0 -> nan, x/0 -> inf)", np.where(np.isfinite(got), got, 0),
       np.where(np.isfinite(ref("ratio", sf_rc, (0, 0))), np.nan_to_num(ref("ratio", sf_rc, (0, 0)), nan=0.0, posinf=0.0), 0))
got, _ = run(["--scaleFactors", "0.5:1.25", "--operation", "log2"])
report("--scaleFactors 0.5:1.25, log2", got, ref("log2", (0.5, 1.25), (1, 1)))
got, _ = run(["--scaleFactorsMethod", "None", "--normalizeUsing", "CPM", "--operation", "log2"])
report("--scaleFactorsMethod None --normalizeUsing CPM, log2", got, ref("log2", (1e6 / n1, 1e6 / n2), (1, 1)))
got, _ = run(["--scaleFactorsMethod", "None", "--normalizeUsing", "RPKM", "--operation", "subtract"])
report("--scaleFactorsMethod None --normalizeUsing RPKM, subtract", got,
       ref("subtract", (1e6 / n1 / (BS / 1e3), 1e6 / n2 / (BS / 1e3)), (1, 1)))
got, _ = run(["--scaleFactorsMethod", "None", "--normalizeUsing", "None", "--operation", "log2"])
report("--scaleFactorsMethod None --normalizeUsing None, log2 (factors 1,1)", got, ref("log2", (1, 1), (1, 1)))

# SES: the background depth of the two samples is identical (20,000 reads each),
# so the background-aligning factor is 1:1 while readCount gives 2:3.
_, err = run(["--scaleFactorsMethod", "SES", "--operation", "log2", "--verbose", "--numberOfSamples", "20000",
              "--sampleLength", "1000"])
_, out = S.run(["bamCompare", "-b1", bam1, "-b2", bam2, "-o", os.path.join(d, "ses.bw"), "-bs", BS, "-p", 1,
                "--scaleFactorsMethod", "SES", "--verbose", "--numberOfSamples", "20000", "--sampleLength", "1000"])
import subprocess, sys
r = subprocess.run([S.tool("bamCompare"), "-b1", bam1, "-b2", bam2, "-o", os.path.join(d, "ses.bw"), "-bs", str(BS), "-p", "1",
                    "--scaleFactorsMethod", "SES", "--verbose", "--numberOfSamples", "20000", "--sampleLength", "1000"],
                   capture_output=True, text=True)
m = re.search(r"Size factors using SES: \[([^\]]*)\]", r.stdout + r.stderr)
ses = [float(x) for x in m.group(1).split()]
print("SES factors %s; true background ratio 1.0 (so [1, 1] is ideal); readCount factors %s; the SES factor for sample 2 is within 10%% of 1: %s"
      % (np.round(ses, 4), np.round(sf_rc, 4), abs(ses[1] - 1.0) < 0.1 and abs(ses[0] - 1.0) < 0.1))
