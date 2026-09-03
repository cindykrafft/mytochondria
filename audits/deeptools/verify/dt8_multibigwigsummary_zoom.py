#!/usr/bin/env python3
"""DT8: multiBigwigSummary reports zoom-level approximations of the bin mean.

getScorePerBigWigBin.countFragmentsInRegions_worker calls
bwh.stats(chrom, start, end) with pyBigWig's default exact=False, which
answers from the bigWig's precomputed zoom level whose span fits the query,
so the reported "mean" is the average of every zoom-level record overlapping
the bin (records that straddle the bin edges count in full). Every other
deepTools consumer of bigWig values (computeMatrix, bigwigCompare,
bigwigAverage, plotFingerprint on bigWigs) reads the exact per-base values.

A bamCoverage track (50-bp bins) from synthetic reads with peaks is
summarised by multiBigwigSummary in bins mode at 10 kb, 2 kb and 1 kb and in
BED-file mode over peak-sized regions; the reference is numpy's nanmean of
bw.values() over the same intervals (also what pyBigWig's exact=True returns).
"""
import os
import numpy as np
import pyBigWig
import _synth as S

print(S.version(), "pyBigWig", pyBigWig.__version__)
rng = np.random.default_rng(71)
d = S.tmpdir()
L = 2000000
w = np.ones(L)
for p in rng.integers(0, L - 2000, 150):
    w[p:p + rng.integers(300, 2000)] += rng.integers(5, 40)
reads, frags = S.random_se_reads(rng, 0, L, 300000, 50, weights=w)
bam = S.write_bam(os.path.join(d, "s.bam"), [("chr1", L)], reads)
bw = os.path.join(d, "s.bw")
S.run(["bamCoverage", "-b", bam, "-o", bw, "-bs", 50, "-p", 1])
vals = S.read_bigwig_per_base(bw, "chr1", L)
handle = pyBigWig.open(bw)


def zoom_spans(path):
    """reduction levels from the bigWig header (64-byte main header, then one
    24-byte zoom header per level: uint32 reductionLevel, uint32 reserved,
    uint64 dataOffset, uint64 indexOffset)"""
    import struct
    with open(path, "rb") as fh:
        hdr = fh.read(64)
        magic, version, nlevels = struct.unpack("<IHH", hdr[:8])
        spans = []
        for i in range(nlevels):
            spans.append(struct.unpack("<IIQQ", fh.read(24))[0])
    return spans


print("zoom levels (reduction spans in bp) in the bamCoverage bigWig:", zoom_spans(bw))
# a second replicate track for the downstream correlation check
reads2, frags2 = S.random_se_reads(rng, 0, L, 300000, 50, weights=w)
bam2 = S.write_bam(os.path.join(d, "s2.bam"), [("chr1", L)], reads2)
bw2 = os.path.join(d, "s2.bw")
S.run(["bamCoverage", "-b", bam2, "-o", bw2, "-bs", 50, "-p", 1])
vals2 = S.read_bigwig_per_base(bw2, "chr1", L)


def summarise(mode, binsize=None, bed=None):
    raw = os.path.join(d, "raw.tab")
    cmd = ["multiBigwigSummary", mode, "-b", bw, bw2, "-o", os.path.join(d, "x.npz"), "-p", 1, "--outRawCounts", raw]
    cmd += ["-bs", binsize] if binsize else ["--BED", bed]
    S.run(cmd)
    rows = [l.rstrip("\n").split("\t") for l in open(raw) if not l.startswith("#")]
    return [(int(r[1]), int(r[2]), float(r[3]), float(r[4])) for r in rows]


for bs in [10000, 5000, 2000, 1000]:
    rows = summarise("bins", binsize=bs)
    rel, exact_ok = [], True
    for s, e, g, g2 in rows:
        ex = np.nanmean(vals[s:e])
        rel.append(abs(g - ex) / ex)
        exact_ok &= np.isclose(handle.stats("chr1", s, e, exact=True)[0], ex, rtol=1e-6)
    rel = np.array(rel)
    print("bins %5d bp: %d bins; |reported - exact| / exact: median %.2e, 95th pct %.2e, max %.2e; bins off by > 1%%: %d; stats(exact=True) equals numpy: %s"
          % (bs, len(rows), np.median(rel), np.percentile(rel, 95), rel.max(), (rel > 0.01).sum(), exact_ok))
    if bs in (10000, 2000):
        import scipy.stats
        rep = np.array([(g, g2) for s, e, g, g2 in rows])
        ex = np.array([(np.nanmean(vals[s:e]), np.nanmean(vals2[s:e])) for s, e, g, g2 in rows])
        print("      replicate correlation from the reported values: Pearson %.4f, Spearman %.4f; from exact means: Pearson %.4f, Spearman %.4f"
              % (np.corrcoef(rep.T)[0, 1], scipy.stats.spearmanr(rep)[0], np.corrcoef(ex.T)[0, 1], scipy.stats.spearmanr(ex)[0]))
        worst = np.argsort(rel)[-3:]
        for i in worst:
            s, e, g, g2 = rows[i]
            print("      bin %d-%d: reported %.3f, exact %.3f, exact mean of the 10 kb on either side %.3f / %.3f"
                  % (s, e, g, np.nanmean(vals[s:e]), np.nanmean(vals[max(0, s - 10000):s]) if s > 0 else float("nan"), np.nanmean(vals[e:e + 10000])))

bed = os.path.join(d, "peaks.bed")
with open(bed, "w") as fh:
    for p in sorted(rng.integers(0, L - 2000, 200)):
        fh.write("chr1\t%d\t%d\n" % (p, p + rng.integers(200, 1500)))
rows = summarise("BED-file", bed=bed)
rel = np.array([abs(g - np.nanmean(vals[s:e])) / np.nanmean(vals[s:e]) for s, e, g, g2 in rows])
print("BED-file (200 regions of 200-1500 bp): |reported - exact| / exact: median %.2e, 95th pct %.2e, max %.2e; regions off by > 1%%: %d"
      % (np.median(rel), np.percentile(rel, 95), rel.max(), (rel > 0.01).sum()))
