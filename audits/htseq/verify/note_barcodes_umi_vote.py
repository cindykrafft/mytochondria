#!/usr/bin/env python3
"""Note: `htseq-count-barcodes` collapses the reads of one (cell, UMI) to a
single count by majority vote over the per-read assignments, and the special
counters (`__no_feature`, `__alignment_not_unique`, `__too_low_aQual`,
`__ambiguous`) take part in that vote (count_with_barcodes.py, lines 389-406:
`top = udic.most_common(2)`; ties discard the UMI).

So a molecule with one read uniquely assigned to gene A and two reads that
fall outside any feature is counted as `__no_feature`, not as gene A; one read
in A and one multimapper (NH=2) is a tie and the molecule is discarded.

Synthetic 10x-style BAM (CB/UB tags), one cell, single-end, MAPQ 255:
  UMI  m1: 3 reads in A                       -> A         (baseline)
  UMI  m2: 1 read in A + 2 reads outside      -> ?
  UMI  m3: 1 read in A + 1 multimapper (NH=2) -> ?
  UMI  m4: 2 reads in A + 1 in B (A/B not overlapping: distinct alignments) -> A
  UMI  m5: 1 read in A + 1 read in B          -> tie -> discarded
  UMI  m6: 2 reads in A + 3 reads with MAPQ 0 -> ?
The reference column is "the molecule is counted for the gene its uniquely
assigned reads support" (cellranger's rule: unassigned reads are ignored).
"""
import os
import subprocess
import sys
import tempfile

import pysam
import HTSeq

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0])
tmp = tempfile.mkdtemp()
gtf = os.path.join(tmp, "g.gtf")
with open(gtf, "w") as f:
    f.write('chr1\tsrc\texon\t1001\t2000\t.\t+\t.\tgene_id "A";\n')
    f.write('chr1\tsrc\texon\t5001\t6000\t.\t+\t.\tgene_id "B";\n')
hdr = {"HD": {"VN": "1.6"}, "SQ": [{"SN": "chr1", "LN": 10000}]}
bam = os.path.join(tmp, "g.bam")
reads = [  # (umi, name, start, mapq, nh, secondary)
    ("m1", "a", 1100, 255, 1, False), ("m1", "b", 1200, 255, 1, False), ("m1", "c", 1300, 255, 1, False),
    ("m2", "a", 1100, 255, 1, False), ("m2", "b", 8000, 255, 1, False), ("m2", "c", 8100, 255, 1, False),
    ("m3", "a", 1100, 255, 1, False), ("m3", "b", 1200, 3, 2, False),
    ("m4", "a", 1100, 255, 1, False), ("m4", "b", 1200, 255, 1, False), ("m4", "c", 5100, 255, 1, False),
    ("m5", "a", 1100, 255, 1, False), ("m5", "b", 5100, 255, 1, False),
    ("m6", "a", 1100, 255, 1, False), ("m6", "b", 1200, 255, 1, False),
    ("m6", "c", 1300, 0, 1, False), ("m6", "d", 1400, 0, 1, False), ("m6", "e", 1500, 0, 1, False),
]
with pysam.AlignmentFile(bam, "wb", header=hdr) as f:
    for umi, n, start, mapq, nh, sec in reads:
        a = pysam.AlignedSegment()
        a.query_name = f"{umi}_{n}"
        a.query_sequence = "A" * 30
        a.query_qualities = pysam.qualitystring_to_array("I" * 30)
        a.flag = 0x100 if sec else 0
        a.reference_id, a.reference_start, a.mapping_quality = 0, start, mapq
        a.cigartuples = [(0, 30)]
        a.set_tags([("NH", nh), ("CB", "AAAACCCCGGGGTTTT-1"), ("UB", umi)])
        f.write(a)

out = os.path.join(tmp, "counts.tsv")
cmd = [sys.executable, "-W", "ignore", "-m", "HTSeq.scripts.count_with_barcodes", "-q", "-s", "yes",
       "-c", out, bam, gtf]
p = subprocess.run(cmd, capture_output=True, text=True)
print("exit", p.returncode, p.stderr.strip())
print("\nhtseq-count-barcodes output (rows: feature, column: the one cell):")
print(open(out).read())

print("Per-UMI expectation if unassigned reads were ignored (cellranger rule) vs what the vote gives:")
print("  m1 3xA            -> A     (both)")
print("  m2 1xA + 2 outside-> A     (reference)   vs __no_feature (vote: 2 > 1)")
print("  m3 1xA + 1 NH=2   -> A     (reference)   vs tie 1:1 -> UMI discarded")
print("  m4 2xA + 1xB      -> A     (both; the B read is a distinct molecule collision, A wins the vote)")
print("  m5 1xA + 1xB      -> tie   (both discard)")
print("  m6 2xA + 3 MAPQ 0 -> A     (reference)   vs __too_low_aQual (vote: 3 > 2)")
print("Reference total for A: 4 molecules (m1, m2, m3, m4) + m6 = 5; B: 0.")
