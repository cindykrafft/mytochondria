#!/usr/bin/env python3
"""DT6: bamCoverage/bamCompare --smoothLength windows are truncated at the
edges of every multiprocessing chunk, not only at chromosome ends.

writeBedGraph.WriteBedGraph.writeBedGraph_worker smooths within the coverage
vector of its chunk (getSmoothRange(..., maxPosition=coverage.shape[0])), so
the bins within (smoothLength / binSize) / 2 of a chunk boundary average over
a one-sided window. Chunk boundaries fall every genomeChunkLength bases
(min(5e6, 2e6 / (mapped reads per bp * files)) rounded down to the bin size;
with --region, at most 1e6). The result therefore depends on the chunking and
differs from a sliding mean over the chromosome at those bins.

Single-end reads on a 3-Mb chromosome, --region chr1:0:3000000 (so the chunk
length is 1e6 and the boundaries are known), --binSize 50 --smoothLength 250
(a 5-bin window: 2 bins left, the bin, 2 bins right). Reference: the same
window over the whole chromosome's bin counts, truncated only at the
chromosome ends. Reports the bins that differ and their positions.
"""
import os
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(13)
d = S.tmpdir()
L = 3000000
BS, SMOOTH = 50, 250
weights = 1.0 + 4.0 * (np.sin(np.arange(L) / 700.0) > 0.7)     # non-uniform coverage
reads, frags = S.random_se_reads(rng, 0, L, 60000, 50, weights=weights)
bam = S.write_bam(os.path.join(d, "s.bam"), [("chr1", L)], reads)
counts = S.bin_overlap_counts(frags, L, BS).astype(float)


def sliding(x, left, right):
    out = np.empty_like(x)
    for i in range(len(x)):
        out[i] = x[max(0, i - left):min(len(x), i + right)].mean()
    return out


ref = sliding(counts, 2, 3)          # getSmoothRange: smoothTiles=5 -> 2 left, 3 (incl. self) right
for tag, extra in [("region", ["--region", "chr1:0:3000000"]), ("no_region", [])]:
    out = os.path.join(d, "sm_%s.bg" % tag)
    S.run(["bamCoverage", "-b", bam, "-o", out, "-of", "bedgraph", "-bs", BS, "-p", 1,
           "--smoothLength", SMOOTH] + extra)
    got = S.bedgraph_to_per_base(S.read_bedgraph(out), "chr1", L, fill=0.0)[::BS]
    bad = np.flatnonzero(~np.isclose(got, ref, atol=1e-6))
    print("\n%s: bins differing from the chromosome-wide sliding mean: %d of %d" % (" ".join(extra) or "(genome-wide)", len(bad), len(ref)))
    if len(bad):
        print("  positions (bp) of differing bins:", [int(b * BS) for b in bad][:20])
        for b in bad[:6]:
            print("  bin %d at %d bp: bamCoverage %.4f, chromosome-wide window mean %.4f" % (b, b * BS, got[b], ref[b]))
    print("  bins away from chunk edges equal the reference: %s"
          % np.allclose(np.delete(got, bad), np.delete(ref, bad), atol=1e-6))
# unsmoothed sanity check of the same data
unsm = os.path.join(d, "raw.bg")
S.run(["bamCoverage", "-b", bam, "-o", unsm, "-of", "bedgraph", "-bs", BS, "-p", 1])
got = S.bedgraph_to_per_base(S.read_bedgraph(unsm), "chr1", L, fill=0.0)[::BS]
print("\nunsmoothed track equals bin counts: %s" % np.array_equal(got, counts))
