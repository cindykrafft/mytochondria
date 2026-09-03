#!/usr/bin/env python3
"""DT1: bamCompare --skipZeroOverZero writes shifted coordinates.

writeBedGraph.WriteBedGraph.writeBedGraph_worker run-length-encodes the bin
values and derives the coordinates of every interval from the *previous*
interval's end. A bin skipped by --skipZeroOverZero (`continue`, no reset)
therefore does not advance the running coordinate, and every interval after it
in the same chunk is shifted left by one bin. The sibling implementation for
bigWig input (writeBedGraph_bam_and_bw.writeBedGraph_worker, used by
bigwigCompare) resets `previousValue = None` on the skip and is correct.

Two BAMs on one 20-kb chromosome, reads confined to a few blocks so that many
50-bp bins have zero coverage in both files. Reference values are computed from
the fragment lists with numpy (readCount scale factors, log2 with the default
pseudocount 1). Prints, per option set, the number of bins whose value in the
output differs from the reference and the first intervals written.
"""
import os
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(7)
L = 20000
BS = 50
d = S.tmpdir()

# blocks of coverage: bins 10-19, 40-49, 100-109, 200-259, 300-399 (bin units)
blocks = [(10, 20), (40, 50), (100, 110), (200, 260), (300, 400)]
weights = np.zeros(L)
for b0, b1 in blocks:
    weights[b0 * BS:b1 * BS] = 1.0
r1, f1 = S.random_se_reads(rng, 0, L, 1500, 30, "a", weights=weights)
r2, f2 = S.random_se_reads(rng, 0, L, 900, 30, "b", weights=weights)
bam1 = S.write_bam(os.path.join(d, "b1.bam"), [("chr1", L)], r1)
bam2 = S.write_bam(os.path.join(d, "b2.bam"), [("chr1", L)], r2)

c1 = S.bin_overlap_counts(f1, L, BS).astype(float)
c2 = S.bin_overlap_counts(f2, L, BS).astype(float)
n1, n2 = len(f1), len(f2)
s1, s2 = min(n1, n2) / n1, min(n1, n2) / n2   # --scaleFactorsMethod readCount
both_zero = (c1 == 0) & (c2 == 0)
print("bins: %d, zero-over-zero bins: %d" % (len(c1), both_zero.sum()))


def reference(op):
    v1, v2 = s1 * c1, s2 * c2
    if op == "log2":
        return np.log2((v1 + 1) / (v2 + 1))
    if op == "subtract":
        return v1 - v2
    if op == "ratio":
        return (v1 + 1) / (v2 + 1)


def check(tag, extra, op, expect_skipped):
    out = os.path.join(d, tag + ".bg")
    S.run(["bamCompare", "-b1", bam1, "-b2", bam2, "-o", out, "-of", "bedgraph",
           "-bs", BS, "-p", 1, "--operation", op] + extra)
    bg = S.read_bedgraph(out)
    got = S.bedgraph_to_per_base(bg, "chr1", L)[::BS]     # value at each bin start
    ref = reference(op)
    if expect_skipped:
        ref = ref.copy()
        ref[both_zero] = np.nan
    ok = np.isclose(got, ref, atol=1e-4) | (np.isnan(got) & np.isnan(ref))
    print("\n%s (--operation %s %s): intervals written %d; bins with wrong value: %d of %d; "
          "bins with a value where the output should be empty: %d; bins empty that should have a value: %d"
          % (tag, op, " ".join(extra), len(bg), (~ok).sum(), len(ok),
             (~np.isnan(got) & np.isnan(ref)).sum(), (np.isnan(got) & ~np.isnan(ref)).sum()))
    print("  first 6 intervals:", [(s, e, round(v, 3)) for _, s, e, v in bg[:6]])
    print("  expected first 6 :", [(int(s), int(e), round(v, 3)) for s, e, v in first_intervals(ref)[:6]])
    return (~ok).sum()


def first_intervals(ref):
    """run-length encode the reference into (start, end, value), skipping NaN"""
    out = []
    i = 0
    while i < len(ref):
        if np.isnan(ref[i]):
            i += 1
            continue
        j = i + 1
        while j < len(ref) and ref[j] == ref[i]:
            j += 1
        out.append((i * BS, j * BS, ref[i]))
        i = j
    return out


bad_default = check("bamCompare_default", [], "log2", expect_skipped=False)
bad_skip = check("bamCompare_skip", ["--skipZeroOverZero"], "log2", expect_skipped=True)
bad_skip_sub = check("bamCompare_skip_subtract", ["--skipZeroOverZero"], "subtract", expect_skipped=True)

# The same option through bigwigCompare (sibling code path with the reset)
bw1 = os.path.join(d, "b1.bw")
bw2 = os.path.join(d, "b2.bw")
S.run(["bamCoverage", "-b", bam1, "-o", bw1, "-bs", BS, "-p", 1, "--scaleFactor", s1])
S.run(["bamCoverage", "-b", bam2, "-o", bw2, "-bs", BS, "-p", 1, "--scaleFactor", s2])
out = os.path.join(d, "bwc.bg")
S.run(["bigwigCompare", "-b1", bw1, "-b2", bw2, "-o", out, "-of", "bedgraph", "-bs", BS, "-p", 1,
       "--operation", "log2", "--skipZeroOverZero"])
got = S.bedgraph_to_per_base(S.read_bedgraph(out), "chr1", L)[::BS]
ref = reference("log2").copy()
ref[both_zero] = np.nan
ok = np.isclose(got, ref, atol=1e-4) | (np.isnan(got) & np.isnan(ref))
print("\nbigwigCompare --skipZeroOverZero on the scaled bamCoverage tracks: bins with wrong value: %d of %d"
      % ((~ok).sum(), len(ok)))
for b in np.flatnonzero(~ok):
    print("  bin %d (%d-%d): bigwigCompare %s, expected %.4f, c1=%d c2=%d; previous bin expected %.4f"
          % (b, b * BS, (b + 1) * BS, got[b], ref[b], c1[b], c2[b], ref[b - 1]))
print("  (the wrong bins are the trailing bins of a run whose value is exactly 0: "
      "writeBedGraph_bam_and_bw.py:135 tests `if previousValue and ...`, so a final run of 0.0 in a chunk is not written)")

print("\nSUMMARY: default %d wrong; --skipZeroOverZero log2 %d wrong, subtract %d wrong (of %d bins)"
      % (bad_default, bad_skip, bad_skip_sub, len(c1)))
