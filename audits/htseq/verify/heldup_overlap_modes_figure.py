#!/usr/bin/env python3
"""Held-up check: the eight rows of the documentation's overlap-mode figure
(doc/images/count_modes.png, described in doc/htseqcount.rst) run through the
shipped `htseq-count` for every mode and every --nonunique setting, and
compared with (a) the figure's stated outcome and (b) the independent
per-base port in htseq_port.py.

Each row is one single-end read on its own chromosome so the rows cannot
interact; gene_A is a two-exon gene, gene_B a one-exon gene. Coordinates are
0-based half-open in the generator (converted to GTF 1-based closed by
write_gtf).
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import HTSeq  # noqa: E402
from htseq_port import (Rec, SPECIAL, compare, per_base_sets, port_count,  # noqa: E402
                        run_htseq_count, write_bams, write_gtf)

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0])

# ---- the figure's rows: (row, description, features on that chromosome,
#      read (start, cigar), expected {mode: outcome})
A = lambda c, s, e: (c, s, e, "+", "exon", {"gene_id": "gene_A"})  # noqa: E731
B = lambda c, s, e: (c, s, e, "+", "exon", {"gene_id": "gene_B"})  # noqa: E731
ROWS = [
    (1, "read inside gene_A", [A("r1", 100, 400)], (150, [("M", 50)]),
     {"union": "gene_A", "intersection-strict": "gene_A", "intersection-nonempty": "gene_A"}),
    (2, "read half outside gene_A", [A("r2", 100, 400)], (375, [("M", 50)]),
     {"union": "gene_A", "intersection-strict": "__no_feature", "intersection-nonempty": "gene_A"}),
    (3, "read over exon end and intron of gene_A", [A("r3", 100, 200), A("r3", 300, 400)],
     (175, [("M", 50)]),
     {"union": "gene_A", "intersection-strict": "__no_feature", "intersection-nonempty": "gene_A"}),
    (4, "spliced read over both exons of gene_A", [A("r4", 100, 200), A("r4", 300, 400)],
     (175, [("M", 25), ("N", 100), ("M", 25)]),
     {"union": "gene_A", "intersection-strict": "gene_A", "intersection-nonempty": "gene_A"}),
    (5, "read in gene_A, gene_B elsewhere", [A("r5", 100, 400), B("r5", 500, 800)],
     (120, [("M", 50)]),
     {"union": "gene_A", "intersection-strict": "gene_A", "intersection-nonempty": "gene_A"}),
    (6, "read in gene_A, gene_B starts inside the read", [A("r6", 100, 400), B("r6", 350, 800)],
     (325, [("M", 50)]),
     {"union": "__ambiguous", "intersection-strict": "gene_A", "intersection-nonempty": "gene_A"}),
    (7, "read inside the overlap of gene_A and gene_B", [A("r7", 100, 400), B("r7", 300, 800)],
     (325, [("M", 50)]),
     {"union": "__ambiguous", "intersection-strict": "__ambiguous", "intersection-nonempty": "__ambiguous"}),
    (8, "multimapper (NH=2) over gene_A / gene_B", [A("r8", 100, 400), B("r8", 500, 800)],
     (150, [("M", 50)]),
     {"union": "__alignment_not_unique", "intersection-strict": "__alignment_not_unique",
      "intersection-nonempty": "__alignment_not_unique"}),
]

tmp = tempfile.mkdtemp()
gtf = os.path.join(tmp, "fig.gtf")
features = []
units = []
recs = []
chrom_lens = {}
for row, desc, feats, (start, cigar), exp in ROWS:
    features += feats
    chrom = feats[0][0]
    chrom_lens[chrom] = 2000
    nh = 2 if row == 8 else None
    r = Rec(f"row{row}", chrom, start, cigar, "+", mapq=60, nh=nh)
    r.unit = (r,)
    units.append((r,))
    recs.append(r)
    if row == 8:  # the second location of the multimapper, in gene_B, secondary
        r2 = Rec("row8", chrom, 600, cigar, "+", mapq=3, nh=2, secondary=True)
        r2.unit = (r2,)
        units.append((r2,))
        recs.append(r2)
write_gtf(gtf, features)
name_bam, pos_bam = write_bams(os.path.join(tmp, "fig"), recs, chrom_lens)
sets, ids = per_base_sets(features, ["exon"], ["gene_id"], stranded=True)

all_ok = True
for nonunique in ("none", "all", "fraction"):
    print(f"\n== --nonunique {nonunique}  (--stranded yes, default -a 10, secondary/supplementary ignore)")
    for mode in ("union", "intersection-strict", "intersection-nonempty"):
        cli, _ = run_htseq_count(name_bam, gtf, ["-m", mode, "--nonunique", nonunique, "-s", "yes"])
        port = port_count(units, sets, ids, mode, "yes", nonunique)
        mism = compare(port, cli)
        status = "OK" if not mism else "MISMATCH " + str(mism)
        print(f"  {mode:22s} CLI: gene_A={cli['gene_A']:g} gene_B={cli['gene_B']:g} "
              + " ".join(f"{k[2:]}={cli[k]:g}" for k in SPECIAL if cli[k]) + f"   vs port: {status}")
        all_ok &= not mism

# Per-row check of the figure's stated outcome, via --samout XF tags (nonunique none)
print("\n== per-row assignment (XF tag from --samout) vs the figure, --nonunique none")
import pysam  # noqa: E402
for mode in ("union", "intersection-strict", "intersection-nonempty"):
    samout = os.path.join(tmp, f"fig_{mode}.sam")
    run_htseq_count(name_bam, gtf, ["-m", mode, "-s", "yes", "-o", samout, "-p", "sam"])
    got = {}
    for a in pysam.AlignmentFile(samout, "r", check_sq=False):
        if not a.is_secondary:
            got[a.query_name] = a.get_tag("XF")
    for row, desc, feats, _, exp in ROWS:
        g = got.get(f"row{row}", "(no record)")
        want = exp[mode]
        ok = g == want or (want == "__ambiguous" and g.startswith("__ambiguous"))
        all_ok &= ok
        print(f"  {mode:22s} row {row} {desc:48s} figure: {want:24s} got: {g:30s} {'OK' if ok else 'MISMATCH'}")

print("\nALL FIGURE ROWS AND PORT COMPARISONS AGREE" if all_ok else "\nDISAGREEMENTS FOUND")
