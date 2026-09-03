#!/usr/bin/env python3
"""Notes verified by execution (design choices, latent paths, documentation):

N1  multiBamSummary bins: the multiprocessing chunk length is not rounded to
    the bin size (countReadsPerBin.get_chunk_length), so a chunk boundary
    inside a bin yields one short bin and restarts the grid (issue #1030);
    shown with --genomeChunkSize 62901 (the default chunk is only shorter than
    a chromosome for deep data).
N2  computeMatrix --skipZeros drops rows whose mean is exactly 0 (all-zero or
    cancelling values), not only all-zero rows (heatmapper._matrix.removeempty).
N3  bamCompare --scaleFactorsMethod SES computes its factors on unfiltered
    reads (SES_scaleFactor.estimateScaleFactor passes no filters): identical
    factors with and without --minMappingQuality even when the filter halves
    one sample.
N6  bigwigCompare drops the last run of a chunk when its value is exactly 0
    (writeBedGraph_bam_and_bw.py:135 `if previousValue and ...`).
N7  bamCoverage --ignoreForNormalization still writes the ignored chromosome,
    scaled with the factor computed from the other chromosomes (documented).
"""
import os
import re
import subprocess
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(91)
d = S.tmpdir()

# N1 -------------------------------------------------------------------------
L = 200000
reads, frags = S.random_se_reads(rng, 0, L, 20000, 50)
bam = S.write_bam(os.path.join(d, "a.bam"), [("chr1", L)], reads)
raw = os.path.join(d, "raw.tab")
S.run(["multiBamSummary", "bins", "-b", bam, "-o", os.path.join(d, "x.npz"), "-bs", 1000, "-p", 1, "--outRawCounts", raw,
       "--genomeChunkSize", 62901])
rows = sorted([(int(l.split()[1]), int(l.split()[2]), float(l.split()[3])) for l in open(raw) if not l.startswith("#")])
short = [(s, e) for s, e, v in rows if e - s != 1000]
print("N1 multiBamSummary bins -bs 1000 --genomeChunkSize 62901: %d bins, %d not 1000 bp: %s; grid restarts at %s"
      % (len(rows), len(short), short[:4], [s for s, e, v in rows if s % 1000 and (s, e) not in short][:3]))
print("   default chunk length for this file (countReadsPerBin.get_chunk_length): %d bp (genome %d, so a single chunk here)"
      % (int(1000 * 1e3 / (len(frags) / L * 1)), L))
S.run(["multiBamSummary", "bins", "-b", bam, "-o", os.path.join(d, "x.npz"), "-bs", 1000, "-p", 1, "--outRawCounts", raw])
rows = sorted([(int(l.split()[1]), int(l.split()[2]), float(l.split()[3])) for l in open(raw) if not l.startswith("#")])
print("   without --genomeChunkSize: %d bins, all 1000 bp: %s" % (len(rows), all(e - s == 1000 for s, e, v in rows)))

# N2 -------------------------------------------------------------------------
chroms = [("chr1", 5000)]
v = np.zeros(5000)
v[1000:1500] = 1.0
v[1500:2000] = -1.0          # region r_cancel: +1 / -1 -> mean 0
v[3000:4000] = 2.0
bw = S.write_bigwig(os.path.join(d, "s.bw"), chroms, {"chr1": v})
bed = os.path.join(d, "r.bed")
with open(bed, "w") as fh:
    fh.write("chr1\t1000\t2000\tr_cancel\t0\t+\nchr1\t2000\t2500\tr_zero\t0\t+\nchr1\t3000\t4000\tr_pos\t0\t+\n")
out = os.path.join(d, "m.gz")
S.run(["computeMatrix", "scale-regions", "-S", bw, "-R", bed, "-m", 100, "-bs", 10, "-o", out, "-p", 1, "--quiet", "--skipZeros"])
import gzip
kept = [l.split("\t")[3] for l in gzip.open(out, "rt") if not l.startswith("@")]
print("N2 computeMatrix --skipZeros keeps: %s (r_cancel has values +1 and -1, mean 0; r_zero is all zero)" % kept)

# N3 -------------------------------------------------------------------------
L = 300000
r1, f1 = [], []
starts = rng.integers(0, L - 50, 20000)
for i in range(20000):
    r1.append(S.se_read(0, int(starts[i]), 50, bool(i % 2), "a%d" % i, mapq=5 if i % 2 else 30))   # half the reads MAPQ 5
r2, f2 = S.random_se_reads(rng, 0, L, 20000, 50, "b")
b1 = S.write_bam(os.path.join(d, "b1.bam"), [("chr1", L)], r1)
b2 = S.write_bam(os.path.join(d, "b2.bam"), [("chr1", L)], r2)
for extra in [[], ["--minMappingQuality", "10"]]:
    r = subprocess.run([S.tool("bamCompare"), "-b1", b1, "-b2", b2, "-o", os.path.join(d, "s.bw"), "-bs", "50", "-p", "1",
                        "--scaleFactorsMethod", "SES", "--verbose", "-n", "20000"] + extra, capture_output=True, text=True)
    m = re.search(r"Size factors using SES: \[([^\]]*)\]", r.stdout + r.stderr)
    print("N3 bamCompare SES factors %-28s: %s" % (" ".join(extra) or "(no filter)", m.group(1).split()))
print("   (sample 1 has 20,000 reads, 10,000 of them MAPQ 5; sample 2 has 20,000 reads; the readCount method gives factors [1, 0.5] with the filter)")

# N6 -------------------------------------------------------------------------
L = 4000
v1 = np.zeros(L)
v1[:1000] = 2.0
v1[1000:2000] = 1.0            # bins 1000-2000 have value 1 in both -> log2 ratio 0 at the end of the chunk
v2 = v1.copy()
v2[:1000] = 1.0
bw1 = S.write_bigwig(os.path.join(d, "c1.bw"), [("chr1", L)], {"chr1": v1})
bw2 = S.write_bigwig(os.path.join(d, "c2.bw"), [("chr1", L)], {"chr1": v2})
out = os.path.join(d, "c.bg")
S.run(["bigwigCompare", "-b1", bw1, "-b2", bw2, "-o", out, "-of", "bedgraph", "-bs", 100, "-p", 1, "--operation", "log2",
       "--pseudocount", 0, "--skipZeroOverZero"])
print("N6 bigwigCompare --skipZeroOverZero, log2, pseudocount 0: intervals %s (expected [(0,1000,1.0), (1000,2000,0.0)]; the trailing 0-valued run is missing)"
      % [(s, e, v) for c, s, e, v in S.read_bedgraph(out)])

# N7 -------------------------------------------------------------------------
chroms = [("chr1", 100000), ("chr2", 100000)]
ra, fa = S.random_se_reads(rng, 0, 100000, 4000, 50, "a")
rb, fb = S.random_se_reads(rng, 1, 100000, 4000, 50, "b")
bam = S.write_bam(os.path.join(d, "two.bam"), chroms, ra + rb)
out = os.path.join(d, "n.bw")
S.run(["bamCoverage", "-b", bam, "-o", out, "-bs", 50, "-p", 1, "--normalizeUsing", "CPM", "--ignoreForNormalization", "chr2"])
c1 = S.read_bigwig_per_base(out, "chr1", 100000)[::50]
c2 = S.read_bigwig_per_base(out, "chr2", 100000)[::50]
print("N7 CPM --ignoreForNormalization chr2: chr1 = counts*1e6/%d: %s; chr2 written: %s, with the same factor: %s"
      % (len(fa), np.allclose(c1, S.bin_overlap_counts(fa, 100000, 50) * 1e6 / len(fa), rtol=1e-5), np.nansum(c2) > 0,
         np.allclose(np.nan_to_num(c2), S.bin_overlap_counts(fb, 100000, 50) * 1e6 / len(fa), rtol=1e-5)))
