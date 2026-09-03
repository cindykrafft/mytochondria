#!/usr/bin/env python3
"""Note: what `--nonunique fraction` divides by, and the documentation's claim
that with `fraction` (or `random`) "the sum of all counts will be equal to the
number of reads (or read pairs)" (doc/htseqcount.rst).

The code divides 1 by the number of overlapping *features* of one alignment
record (count_features_per_file.py, `val = 1.0 / len(fs)`); it never divides
by NH, the number of alignments of the read. So a multimapper whose secondary
alignments are scored (`--secondary-alignments score`) contributes 1 per
alignment record, NH in total. Also, every ambiguous unit is counted once in
`__ambiguous` *and* fractionally in the features.

Synthetic data: 100 unique reads in gene A; 50 reads overlapping A and B
(ambiguous); 40 multimappers with NH=3 whose three alignments (primary +
two secondary) each fall in one gene (A, B, C). All MAPQ 60.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import HTSeq  # noqa: E402
from htseq_port import Rec, SPECIAL, run_htseq_count, write_bams, write_gtf  # noqa: E402

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0])
tmp = tempfile.mkdtemp()
gtf = os.path.join(tmp, "f.gtf")
features = [("chr1", 1000, 2000, "+", "exon", {"gene_id": "A"}),
            ("chr1", 1800, 3000, "+", "exon", {"gene_id": "B"}),
            ("chr1", 5000, 6000, "+", "exon", {"gene_id": "C"})]
write_gtf(gtf, features)
recs = []
for i in range(100):
    recs.append(Rec(f"u{i}", "chr1", 1100 + i, [("M", 50)], "+", mapq=60, nh=1))
for i in range(50):
    recs.append(Rec(f"amb{i}", "chr1", 1850 + i, [("M", 50)], "+", mapq=60, nh=1))
for i in range(40):
    recs.append(Rec(f"mm{i}", "chr1", 1200 + i, [("M", 50)], "+", mapq=60, nh=3))
    recs.append(Rec(f"mm{i}", "chr1", 2500 + i, [("M", 50)], "+", mapq=60, nh=3, secondary=True))
    recs.append(Rec(f"mm{i}", "chr1", 5500 + i, [("M", 50)], "+", mapq=60, nh=3, secondary=True))
name_bam, _ = write_bams(os.path.join(tmp, "f"), recs, {"chr1": 10000})
n_reads = 100 + 50 + 40
print(f"reads: {n_reads} (100 unique in A, 50 ambiguous A/B, 40 multimappers NH=3 with 3 records each); "
      f"records: {len(recs)}")

for sec in ("ignore", "score"):
    for nonunique in ("none", "all", "fraction", "random"):
        cli, _ = run_htseq_count(name_bam, gtf, ["-m", "union", "-s", "yes", "--nonunique", nonunique,
                                                  "--secondary-alignments", sec, "-a", "0"])
        feat = {k: v for k, v in cli.items() if not k.startswith("__")}
        s = sum(feat.values())
        print(f"--secondary-alignments {sec:6s} --nonunique {nonunique:8s}: A={feat['A']:g} B={feat['B']:g} C={feat['C']:g}"
              f"  sum(features)={s:g}  {' '.join(f'{k[2:]}={cli[k]:g}' for k in SPECIAL if cli[k])}"
              f"  sum(features)+no_feature == reads? {abs(s + cli['__no_feature'] - n_reads) < 1e-9}")
print("\nWith --secondary-alignments score and --nonunique fraction each of the 40 multimappers adds 3 counts")
print("(one per alignment record, 1/len(features) each), so the feature sum exceeds the number of reads by 80;")
print("with the default (ignore) the primary record alone is counted, sum(features) + no_feature == reads.")
