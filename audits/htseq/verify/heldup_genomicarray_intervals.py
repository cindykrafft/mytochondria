#!/usr/bin/env python3
"""Held-up checks of the interval machinery under htseq-count, against
brute-force per-base references that do not use HTSeq's data structures:

  A. GenomicArrayOfSets: random overlapping intervals on both strands added
     with `+=`; the set at every base (via `steps()` and via point indexing)
     equals a per-base dictionary; stranded and unstranded arrays; features
     added twice with the same id; adjacent/abutting/nested intervals.
  B. GFF_Reader coordinate conversion: 1-based closed GTF/GFF3 -> 0-based
     half-open; `end_included=False` variant; strand '.'; stranded array
     rejects '.' features (documented ValueError).
  C. GenomicInterval.overlaps / contains / is_contained_in vs brute force,
     including the strand rules ('.' matches either).
  D. StepVector: random set/add operations vs a dense numpy vector, and
     `get_steps` boundaries.
  E. pair_SAM_alignments (name order) and pair_SAM_alignments_with_buffer
     (position order) on a synthetic stream with multimappers, missing mates,
     unmapped mates and chimeric records: both pairers return the same
     multiset of (mate-1 record, mate-2 record) pairs as the generator's truth.
"""
import os
import random
import sys
import tempfile
from collections import Counter, defaultdict

import numpy as np
import pysam
import HTSeq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from htseq_port import Rec, write_bams  # noqa: E402

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0])
rng = random.Random(11)
ok_all = True

# ---------------------------------------------------------------- A
print("\n== A. GenomicArrayOfSets vs per-base dictionary")
for stranded in (True, False):
    gas = HTSeq.GenomicArrayOfSets("auto", stranded=stranded)
    truth = defaultdict(set)
    ivs = []
    for i in range(400):
        chrom = rng.choice(["chr1", "chr2"])
        s = rng.randint(0, 5000)
        e = s + rng.randint(1, 800)
        strand = rng.choice("+-")
        name = f"f{rng.randint(0, 120)}"  # ids repeat -> same feature, several exons
        ivs.append((chrom, s, e, strand, name))
    # abutting and nested cases on purpose
    ivs += [("chr1", 100, 200, "+", "ab1"), ("chr1", 200, 300, "+", "ab2"), ("chr1", 120, 150, "+", "nest"),
            ("chr1", 100, 200, "+", "ab1"), ("chr1", 100, 200, "-", "ab1minus"), ("chr1", 150, 150 + 1, "+", "one")]
    for chrom, s, e, strand, name in ivs:
        gas[HTSeq.GenomicInterval(chrom, s, e, strand)] += name
        for b in range(s, e):
            truth[(chrom, strand if stranded else ".", b)].add(name)
    bad = 0
    n_checked = 0
    for chrom in ("chr1", "chr2"):
        for strand in (("+", "-") if stranded else (".",)):
            iv = HTSeq.GenomicInterval(chrom, 0, 6000, strand)
            dense = {}
            for step_iv, val in gas[iv].steps():
                for b in range(step_iv.start, step_iv.end):
                    dense[b] = set(val)
            for b in range(0, 6000):
                n_checked += 1
                if dense.get(b, set()) != truth.get((chrom, strand, b), set()):
                    bad += 1
            # point indexing
            for b in rng.sample(range(6000), 300):
                p = HTSeq.GenomicPosition(chrom, b, strand)
                if set(gas[p]) != truth.get((chrom, strand, b), set()):
                    bad += 1
    print(f"  stranded={stranded}: {n_checked} bases + 1,200 point lookups checked, mismatches: {bad}")
    ok_all &= bad == 0
# stranded array rejects '.' index; unstranded accepts stranded index
gas = HTSeq.GenomicArrayOfSets("auto", stranded=True)
try:
    gas[HTSeq.GenomicInterval("chr1", 0, 10, ".")] += "x"
    print("  stranded array with '.' interval: accepted (unexpected)")
except KeyError as e:
    print("  stranded array with '.' interval: KeyError as documented ->", e)

# ---------------------------------------------------------------- B
print("\n== B. GFF_Reader coordinate conversion")
tmp = tempfile.mkdtemp()
gtf = os.path.join(tmp, "c.gtf")
open(gtf, "w").write('chr1\tsrc\texon\t1\t1\t.\t+\t.\tgene_id "one";\n'
                     'chr1\tsrc\texon\t101\t200\t.\t-\t.\tgene_id "hundred";\n'
                     'chr1\tsrc\texon\t5\t8\t.\t.\t.\tgene_id "nostrand";\n')
for f in HTSeq.GFF_Reader(gtf):
    print(f"  GTF {f.attr['gene_id']:9s} -> {f.iv}  length {f.iv.length}")
for f in HTSeq.GFF_Reader(gtf, end_included=False):
    print(f"  end_included=False {f.attr['gene_id']:9s} -> {f.iv}")
gff3 = os.path.join(tmp, "c.gff3")
open(gff3, "w").write('chr1\tsrc\texon\t101\t200\t.\t+\t.\tID=e1;Parent=g1\n')
for f in HTSeq.GFF_Reader(gff3):
    print(f"  GFF3 {f.attr} -> {f.iv}")
try:
    HTSeq.make_feature_genomicarrayofsets(HTSeq.GFF_Reader(gtf), "gene_id", feature_type=["exon"], stranded=True)
    print("  stranded=True with a '.' feature: accepted (unexpected)")
except ValueError as e:
    print("  stranded=True with a '.' feature: ValueError as documented ->", str(e)[:70], "...")
r = HTSeq.make_feature_genomicarrayofsets(HTSeq.GFF_Reader(gtf), "gene_id", feature_type=["exon"], stranded=False)
print("  stranded=False: features", sorted(r["attributes"]),
      "base 0 ->", set(r["features"][HTSeq.GenomicPosition("chr1", 0, ".")]),
      "base 4..7 ->", [set(r["features"][HTSeq.GenomicPosition("chr1", b, ".")]) for b in (3, 4, 7, 8)])

# ---------------------------------------------------------------- C
print("\n== C. overlaps / contains / is_contained_in vs brute force (20,000 random pairs)")
bad = Counter()
n_zero = 0
for _ in range(20000):
    c1, c2 = rng.choice(["chr1", "chr1", "chr2"]), rng.choice(["chr1", "chr1", "chr2"])
    s1, s2 = rng.randint(0, 50), rng.randint(0, 50)
    a = HTSeq.GenomicInterval(c1, s1, s1 + rng.randint(0, 30), rng.choice("+-."))
    b = HTSeq.GenomicInterval(c2, s2, s2 + rng.randint(0, 30), rng.choice("+-."))
    strand_ok = a.strand == "." or b.strand == "." or a.strand == b.strand
    same = a.chrom == b.chrom and strand_ok
    bases_a = set(range(a.start, a.end))
    bases_b = set(range(b.start, b.end))
    ov = same and bool(bases_a & bases_b)
    cont = same and a.start <= b.start and b.end <= a.end
    if a.overlaps(b) != ov:
        bad["overlaps (zero-length interval involved)" if (a.length == 0 or b.length == 0) else "overlaps"] += 1
    if a.contains(b) != cont:
        bad["contains"] += 1
    if b.is_contained_in(a) != cont:
        bad["is_contained_in"] += 1
print("  mismatches:", dict(bad) or "none")
z, w = HTSeq.GenomicInterval("chr1", 5, 5, "."), HTSeq.GenomicInterval("chr1", 3, 10, ".")
print("  zero-length: [5,5).overlaps([3,10)) =", z.overlaps(w), "; [3,3).overlaps([3,10)) =",
      HTSeq.GenomicInterval("chr1", 3, 3).overlaps(w), "but [3,10).overlaps([3,3)) =",
      w.overlaps(HTSeq.GenomicInterval("chr1", 3, 3)), "(note: asymmetric; no zero-length intervals arise in htseq-count)")
ok_all &= not any(k == "overlaps" for k in bad)

# ---------------------------------------------------------------- D
print("\n== D. StepVector set/add vs dense numpy (int typecode, 3,000 random ops)")
sv = HTSeq.StepVector.StepVector.create(length=5000, typecode="i")
dense = np.zeros(5000, dtype=int)
for _ in range(3000):
    s = rng.randint(0, 4999)
    e = rng.randint(s + 1, 5000)
    v = rng.randint(-3, 3)
    if rng.random() < 0.5:
        sv[s:e] = v
        dense[s:e] = v
    else:
        sv[s:e] += v
        dense[s:e] += v
arr = np.array(list(sv))
steps = list(sv.get_steps())
print("  equal to dense:", bool((arr == dense).all()), "| steps contiguous and cover [0,5000):",
      steps[0][0] == 0 and steps[-1][1] == 5000 and all(a[1] == b[0] for a, b in zip(steps, steps[1:])),
      "| consecutive steps differ:", all(a[2] != b[2] for a, b in zip(steps, steps[1:])))
ok_all &= bool((arr == dense).all())

# ---------------------------------------------------------------- E
print("\n== E. pairing: name order vs position order vs generator truth")
CHROMS = {"chr1": 50000, "chr2": 30000}
recs, truth_pairs = [], Counter()
for i in range(1500):
    name = f"p{i}"
    chrom = rng.choice(list(CHROMS))
    L = CHROMS[chrom]
    kind = rng.random()
    st = rng.choice("+-")
    ms = "-" if st == "+" else "+"
    s1 = rng.randint(0, L - 3000)
    if kind < 0.08:  # both unmapped
        r1, r2 = Rec(name, paired=True, which=1), Rec(name, paired=True, which=2)
        r1.mate_unmapped = r2.mate_unmapped = True
        recs += [r1, r2]
        truth_pairs[(name, None, None)] += 1
        continue
    r1 = Rec(name, chrom, s1, [("M", 50)], st, paired=True, which=1)
    if kind < 0.16:  # mate unmapped, placed
        r2 = Rec(name, paired=True, which=2)
        r2.placed_at = (chrom, s1)
        r2.mate_chrom, r2.mate_start, r2.mate_strand = chrom, s1, st
        r1.mate_unmapped, r1.mate_chrom, r1.mate_start = True, chrom, s1
        recs += [r1, r2]
        truth_pairs[(name, (chrom, s1), None)] += 1
        continue
    if kind < 0.22:  # mate missing from file
        r1.mate_chrom, r1.mate_start, r1.mate_strand = chrom, s1 + 400, ms
        r1.tlen = 450
        recs.append(r1)
        truth_pairs[(name, (chrom, s1), None)] += 1
        continue
    nmap = 2 if kind < 0.35 else 1
    for k in range(nmap):
        sa = s1 if k == 0 else rng.randint(0, L - 3000)
        sb = max(0, sa + rng.randint(-40, 900))
        ra = Rec(name, chrom, sa, [("M", 50)], st, mapq=3 if nmap > 1 else 60, nh=nmap, paired=True, which=1,
                 secondary=(k > 0))
        rb = Rec(name, chrom, sb, [("M", 50)], ms, mapq=3 if nmap > 1 else 60, nh=nmap, paired=True, which=2,
                 secondary=(k > 0))
        ra.mate_chrom, ra.mate_start, ra.mate_strand = chrom, sb, ms
        rb.mate_chrom, rb.mate_start, rb.mate_strand = chrom, sa, st
        t = max(sa, sb) + 50 - min(sa, sb)
        ra.tlen, rb.tlen = (t, -t) if sa <= sb else (-t, t)
        recs += [ra, rb]
        truth_pairs[(name, (chrom, sa), (chrom, sb))] += 1
    if kind > 0.9:  # add a supplementary record of mate 1 elsewhere
        rs = Rec(name, "chr2", rng.randint(0, 20000), [("H", 20), ("M", 30)], "+", paired=True, which=1,
                 supplementary=True)
        rs.mate_chrom, rs.mate_start, rs.mate_strand = chrom, r1.mate_start if r1.mate_start else s1, ms
        recs.append(rs)
        truth_pairs[(name, ("chr2", rs.start), None)] += 1
name_bam, pos_bam = write_bams(os.path.join(tmp, "pairs"), recs, CHROMS)


def key(a):
    return None if a is None or not a.aligned else (a.iv.chrom, a.iv.start)


for label, bam, fn in (("name", name_bam, lambda it: HTSeq.pair_SAM_alignments(it, primary_only=False)),
                       ("pos", pos_bam, lambda it: HTSeq.pair_SAM_alignments_with_buffer(it, primary_only=False))):
    import warnings
    got = Counter()
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        for a1, a2 in fn(HTSeq.BAM_Reader(bam)):
            nm = (a1 or a2).read.name
            got[(nm, key(a1), key(a2))] += 1
    diff = (truth_pairs - got) + (got - truth_pairs)
    print(f"  -r {label}: pairs yielded {sum(got.values())} vs truth {sum(truth_pairs.values())}; "
          f"differences: {len(diff)}; warnings: {[str(x.message)[:60] for x in w][:2]}")
    ok_all &= len(diff) == 0
print("\nALL HELD UP" if ok_all else "\nSOME CHECKS FAILED")
