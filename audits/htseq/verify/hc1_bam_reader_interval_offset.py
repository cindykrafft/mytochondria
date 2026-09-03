#!/usr/bin/env python3
"""HC1: `BAM_Reader.__getitem__(iv)` (HTSeq/__init__.py) calls
`pysam.AlignmentFile.fetch(iv.chrom, iv.start + 1, iv.end)`. pysam's fetch
takes 0-based half-open coordinates, and HTSeq's GenomicInterval is 0-based
half-open too, so the `+ 1` shifts the query window right by one base: an
alignment whose last aligned base is `iv.start` overlaps `iv` (its
`GenomicInterval.overlaps` says so) but is not returned.

Part A: minimal case -- five 10-nt reads around a [100, 200) window.
Part B: random windows and reads; the set returned by `reader[iv]` compared
with the brute-force set of records whose reference span overlaps `iv`
(computed from pysam, independent of HTSeq), and with pysam's own
`fetch(iv.start, iv.end)`.
Part C: the tutorial's use (doc/tutorials/tss.rst: `sortedbamfile[window]`):
the coverage profile around a TSS built with `reader[window]` vs the same
profile from `fetch(window.start, window.end)`.
"""
import os
import random
import sys
import tempfile

import numpy as np
import pysam
import HTSeq

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0], "pysam", pysam.__version__)
tmp = tempfile.mkdtemp()
hdr = {"HD": {"VN": "1.6", "SO": "coordinate"}, "SQ": [{"SN": "chr1", "LN": 100000}]}


def write_bam(path, reads):
    """reads: list of (name, start0, length, strand)."""
    with pysam.AlignmentFile(path, "wb", header=hdr) as f:
        for name, start, L, strand in sorted(reads, key=lambda x: x[1]):
            a = pysam.AlignedSegment()
            a.query_name, a.query_sequence, a.flag = name, "A" * L, (16 if strand == "-" else 0)
            a.reference_id, a.reference_start, a.mapping_quality = 0, start, 60
            a.cigartuples = [(0, L)]
            a.query_qualities = pysam.qualitystring_to_array("I" * L)
            f.write(a)
    pysam.index(path)


# ------------------------------------------------------------- Part A
print("\n== A. minimal: window chr1:[100,200), 10-nt reads")
bam = os.path.join(tmp, "a.bam")
reads = [("ends_at_99_[90,100)", 90, 10, "+"), ("covers_base_100_[91,101)", 91, 10, "+"),
         ("[95,105)", 95, 10, "+"), ("[199,209)", 199, 10, "+"), ("[200,210)", 200, 10, "+")]
write_bam(bam, reads)
iv = HTSeq.GenomicInterval("chr1", 100, 200, ".")
got = [a.read.name for a in HTSeq.BAM_Reader(bam)[iv]]
expected = [a.read.name for a in HTSeq.BAM_Reader(bam) if a.iv.overlaps(iv)]
print("  reader[iv]                          ->", got)
print("  records with a.iv.overlaps(iv)      ->", expected)
print("  pysam fetch(chr1, 100, 200)         ->",
      [r.query_name for r in pysam.AlignmentFile(bam).fetch("chr1", 100, 200)])
print("  MISSED by reader[iv]:", sorted(set(expected) - set(got)))

# ------------------------------------------------------------- Part B
print("\n== B. random windows and reads (2,000 reads of 20-150 nt on chr1, 300 windows)")
rng = random.Random(7)
reads = [(f"r{i}", rng.randint(0, 90000), rng.randint(20, 150), rng.choice("+-")) for i in range(2000)]
bam = os.path.join(tmp, "b.bam")
write_bam(bam, reads)
span = {n: (s, s + L) for n, s, L, _ in reads}
n_windows = 300
n_missed_windows = 0
n_missed_reads = 0
n_extra = 0
examples = []
for w in range(n_windows):
    s = rng.randint(0, 95000)
    e = s + rng.randint(1, 3000)
    iv = HTSeq.GenomicInterval("chr1", s, e, ".")
    got = {a.read.name for a in HTSeq.BAM_Reader(bam)[iv]}
    truth = {n for n, (a, b) in span.items() if a < e and b > s}
    fetch = {r.query_name for r in pysam.AlignmentFile(bam).fetch("chr1", s, e)}
    assert fetch == truth, "pysam fetch is not the brute-force truth?!"
    missed = truth - got
    extra = got - truth
    n_missed_reads += len(missed)
    n_extra += len(extra)
    if missed:
        n_missed_windows += 1
        if len(examples) < 3:
            examples.append((s, e, sorted((n, span[n]) for n in missed)))
print(f"  windows with at least one overlapping record missing from reader[iv]: {n_missed_windows}/{n_windows}")
print(f"  overlapping records missed in total: {n_missed_reads}; non-overlapping records returned: {n_extra}")
for s, e, m in examples:
    print(f"    window [{s},{e}): missed {m}")
print("  every missed record ends exactly at iv.start+1 (i.e. covers only base iv.start):",
      all(span[n][1] == s + 1 for s, e, m in examples for n, _ in m))

# ------------------------------------------------------------- Part C
print("\n== C. TSS-profile style use (doc/tutorials/tss.rst): coverage in a +-100 window around position 50000")
tss = 50000
halfwin = 100
window = HTSeq.GenomicInterval("chr1", tss - halfwin, tss + halfwin, ".")
prof_htseq = np.zeros(2 * halfwin, dtype=int)
for almnt in HTSeq.BAM_Reader(bam)[window]:
    a, b = max(almnt.iv.start, window.start), min(almnt.iv.end, window.end)
    prof_htseq[a - window.start:b - window.start] += 1
prof_ref = np.zeros(2 * halfwin, dtype=int)
for r in pysam.AlignmentFile(bam).fetch("chr1", window.start, window.end):
    a, b = max(r.reference_start, window.start), min(r.reference_end, window.end)
    prof_ref[a - window.start:b - window.start] += 1
print("  coverage at the window's first base: reader[window] =", prof_htseq[0], " fetch(start,end) =", prof_ref[0])
print("  positions where the two profiles differ:", np.nonzero(prof_htseq != prof_ref)[0].tolist())
print("\nRESULT: BAM_Reader[iv] misses records covering only base iv.start:", n_missed_reads > 0)
