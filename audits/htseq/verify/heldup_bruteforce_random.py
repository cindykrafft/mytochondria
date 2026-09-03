#!/usr/bin/env python3
"""Held-up check: the shipped `htseq-count` against the independent per-base
port on random synthetic data with known truth.

Data (seeded): 3 chromosomes; genes with 1-4 exons on both strands, some
overlapping each other on the same and on the opposite strand, some sharing a
gene_id across exons; single-end and paired-end reads with soft clips,
insertions, deletions, spliced N gaps, MAPQ in {0, 3, 10, 60, 255}, NH tags
(unique NH=1, multimappers NH=2 with a secondary record, NH=3 with only the
primary present), unmapped reads, pairs with one unmapped mate (placed at the
mate), pairs with a mate missing from the file, chimeric reads with a
supplementary record, and mates on different chromosomes.

For every combination of -m, -s, --nonunique (none/all/fraction), -a,
--secondary-alignments and --supplementary-alignments the CLI is run on the
name-sorted file (-r name) and the coordinate-sorted file (-r pos) and both are
compared with the port. --nonunique random is checked for its conservation
property only (every ambiguous unit adds exactly one count to one feature).

Two ports are compared: the documented semantics, and the same port with
HC2 modelled (an unmapped mate record's MAPQ field, 0, is compared with -a
like an aligned one). If every run agrees with the second, HC2 is the only
divergence from the documentation on this data.
"""
import os
import random
import sys
import tempfile
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import HTSeq  # noqa: E402
from htseq_port import (Rec, SPECIAL, compare, per_base_sets, port_count,  # noqa: E402
                        run_htseq_count, write_bams, write_gtf)

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0])
rng = random.Random(20260903)
CHROMS = {"chr1": 60000, "chr2": 40000, "chr3": 20000}


def make_features():
    feats = []
    gid = 0
    for chrom, L in CHROMS.items():
        pos = 200
        while pos < L - 3000:
            gid += 1
            strand = rng.choice("+-")
            nex = rng.randint(1, 4)
            p = pos
            for _ in range(nex):
                el = rng.randint(50, 400)
                feats.append((chrom, p, p + el, strand, "exon", {"gene_id": f"G{gid}", "gene_name": f"N{gid}"}))
                p += el + rng.randint(30, 300)
            # sometimes an overlapping gene on the other strand, sometimes same strand
            if rng.random() < 0.35:
                gid += 1
                s2 = rng.choice(["+", "-", strand])
                o = pos + rng.randint(-100, 300)
                feats.append((chrom, max(o, 0), max(o, 0) + rng.randint(80, 600), s2, "exon",
                              {"gene_id": f"G{gid}", "gene_name": f"N{gid}"}))
            # a non-exon feature that -t exon must ignore
            if rng.random() < 0.2:
                feats.append((chrom, pos, p, strand, "gene", {"gene_id": f"G{gid}", "gene_name": f"N{gid}"}))
            pos = p + rng.randint(0, 800)
    return feats


def rand_cigar(readlen):
    """A CIGAR consuming `readlen` query bases, with optional S/I/D/N."""
    ops = []
    left = readlen
    if rng.random() < 0.15:
        s = rng.randint(1, 8)
        ops.append(("S", s))
        left -= s
    right_clip = rng.randint(1, 8) if rng.random() < 0.15 else 0
    left -= right_clip
    while left > 0:
        m = min(left, rng.randint(5, 40))
        ops.append(("M", m))
        left -= m
        if left > 0:
            r = rng.random()
            if r < 0.15:
                ops.append(("N", rng.randint(40, 600)))
            elif r < 0.25:
                ops.append(("D", rng.randint(1, 5)))
            elif r < 0.35:
                i = min(left - 1, rng.randint(1, 4))
                if i > 0:
                    ops.append(("I", i))
                    left -= i
    if right_clip:
        ops.append(("S", right_clip))
    return ops


def rand_mapq():
    return rng.choice([0, 3, 10, 60, 255, 255, 60, 60])


def make_reads(n_units, paired):
    """paired=False: single-end records only; True: paired-end only (htseq-count
    decides the mode from the first record and rejects mixed files)."""
    recs, units = [], []
    uid = 0

    def new_single(name, chrom=None, start=None, cigar=None, **kw):
        r = Rec(name, chrom, start, cigar, **kw)
        return r

    for _ in range(n_units):
        uid += 1
        name = f"u{uid}"
        chrom = rng.choice(list(CHROMS))
        L = CHROMS[chrom]
        if not paired:
            # single-end
            sub = rng.random()
            if sub < 0.06:
                r = new_single(name)
                recs.append(r); units.append((r,))
            elif sub < 0.14:
                # multimapper NH=2 with a secondary record: two counting units (one per record)
                for k in range(2):
                    r = new_single(name, chrom, rng.randint(0, L - 800), rand_cigar(rng.randint(30, 100)),
                                   strand=rng.choice("+-"), mapq=rng.choice([0, 1, 3]), nh=2, secondary=(k == 1))
                    recs.append(r); units.append((r,))
            elif sub < 0.20:
                # NH=3 but only the primary present
                r = new_single(name, chrom, rng.randint(0, L - 800), rand_cigar(rng.randint(30, 100)),
                               strand=rng.choice("+-"), mapq=rand_mapq(), nh=3)
                recs.append(r); units.append((r,))
            elif sub < 0.28:
                # chimeric: primary + supplementary at another place (BWA style, no NH)
                r = new_single(name, chrom, rng.randint(0, L - 800), rand_cigar(rng.randint(30, 100)),
                               strand=rng.choice("+-"), mapq=rand_mapq())
                c2 = rng.choice(list(CHROMS))
                r2 = new_single(name, c2, rng.randint(0, CHROMS[c2] - 800), [("H", 30), ("M", 25)],
                                strand=rng.choice("+-"), mapq=rand_mapq(), supplementary=True)
                recs += [r, r2]; units += [(r,), (r2,)]
            else:
                r = new_single(name, chrom, rng.randint(0, L - 800), rand_cigar(rng.randint(30, 100)),
                               strand=rng.choice("+-"), mapq=rand_mapq(), nh=1 if rng.random() < 0.7 else None)
                recs.append(r); units.append((r,))
        else:
            # paired-end
            sub = rng.random()
            st = rng.choice("+-")
            ms = "-" if st == "+" else "+"
            nh = 1 if rng.random() < 0.7 else None
            s1 = rng.randint(0, L - 2000)
            c1 = rand_cigar(rng.randint(30, 100))
            r1 = Rec(name, chrom, s1, c1, st, mapq=rand_mapq(), nh=nh, paired=True, which=1)
            if sub < 0.06:
                # both unmapped
                r1 = Rec(name, paired=True, which=1)
                r2 = Rec(name, paired=True, which=2)
                r1.mate_unmapped = r2.mate_unmapped = True
                recs += [r1, r2]; units.append((r1, r2))
                continue
            if sub < 0.14:
                # mate 2 unmapped, placed at mate 1
                r2 = Rec(name, paired=True, which=2)
                r2.placed_at = (chrom, s1)
                r2.mate_chrom, r2.mate_start, r2.mate_strand = chrom, s1, st
                r1.mate_unmapped = True
                r1.mate_chrom, r1.mate_start = chrom, s1
                r1.mate_strand = "+"
                recs += [r1, r2]; units.append((r1, r2))
                continue
            if sub < 0.20:
                # mate 2 missing from the file entirely (mate flagged as mapped)
                r1.mate_chrom, r1.mate_start, r1.mate_strand = chrom, s1 + 300, ms
                r1.tlen = 350
                recs.append(r1); units.append((r1,))
                continue
            if sub < 0.26:
                # mates on different chromosomes
                c2 = rng.choice([c for c in CHROMS if c != chrom])
                s2 = rng.randint(0, CHROMS[c2] - 800)
                r2 = Rec(name, c2, s2, rand_cigar(rng.randint(30, 100)), ms, mapq=rand_mapq(), nh=nh,
                         paired=True, which=2)
                r1.mate_chrom, r1.mate_start, r1.mate_strand = c2, s2, ms
                r2.mate_chrom, r2.mate_start, r2.mate_strand = chrom, s1, st
                r1.tlen = r2.tlen = 0
                recs += [r1, r2]; units.append((r1, r2))
                continue
            if sub < 0.34:
                # multimapping pair NH=2: primary pair + secondary pair
                for k in range(2):
                    sa = rng.randint(0, L - 2000)
                    sb = sa + rng.randint(-50, 800)
                    sb = max(sb, 0)
                    ra = Rec(name, chrom, sa, rand_cigar(rng.randint(30, 100)), st, mapq=rng.choice([0, 3]),
                             nh=2, paired=True, which=1, secondary=(k == 1))
                    rb = Rec(name, chrom, sb, rand_cigar(rng.randint(30, 100)), ms, mapq=rng.choice([0, 3]),
                             nh=2, paired=True, which=2, secondary=(k == 1))
                    ra.mate_chrom, ra.mate_start, ra.mate_strand = chrom, sb, ms
                    rb.mate_chrom, rb.mate_start, rb.mate_strand = chrom, sa, st
                    lo = min(sa, sb); hi = max(ra.ref_end(), rb.ref_end())
                    t = hi - lo
                    ra.tlen, rb.tlen = (t, -t) if sa <= sb else (-t, t)
                    recs += [ra, rb]; units.append((ra, rb))
                continue
            # ordinary proper pair, sometimes overlapping mates, sometimes far apart
            s2 = s1 + rng.randint(-40, 1500)
            s2 = max(s2, 0)
            r2 = Rec(name, chrom, s2, rand_cigar(rng.randint(30, 100)), ms, mapq=rand_mapq(), nh=nh,
                     paired=True, which=2)
            if rng.random() < 0.1:  # improper pair: same strand
                r2.strand = st
                ms2 = st
            else:
                ms2 = ms
            r1.mate_chrom, r1.mate_start, r1.mate_strand = chrom, s2, ms2
            r2.mate_chrom, r2.mate_start, r2.mate_strand = chrom, s1, st
            lo = min(s1, s2); hi = max(r1.ref_end(), r2.ref_end())
            t = hi - lo
            r1.tlen, r2.tlen = (t, -t) if s1 <= s2 else (-t, t)
            if rng.random() < 0.08:
                # chimeric mate 1 with a supplementary record pointing at mate 2
                c3 = rng.choice(list(CHROMS))
                rs = Rec(name, c3, rng.randint(0, CHROMS[c3] - 800), [("H", 20), ("M", 30)], rng.choice("+-"),
                         mapq=rand_mapq(), paired=True, which=1, supplementary=True)
                rs.mate_chrom, rs.mate_start, rs.mate_strand = chrom, s2, ms2
                recs.append(rs); units.append((rs,))
            recs += [r1, r2]; units.append((r1, r2))
    return recs, units


features = make_features()
tmp = tempfile.mkdtemp()
gtf = os.path.join(tmp, "rand.gtf")
write_gtf(gtf, features)
n_exons = sum(1 for f in features if f[4] == "exon")
print(f"features: {len(features)} lines, {n_exons} exons, {len({f[5]['gene_id'] for f in features})} gene_ids")
datasets = {}
for label, paired, n in (("single-end", False, 1500), ("paired-end", True, 1500)):
    recs, units = make_reads(n, paired)
    name_bam, pos_bam = write_bams(os.path.join(tmp, label), recs, CHROMS)
    datasets[label] = (recs, units, name_bam, pos_bam)
    print(f"{label}: records {len(recs)}, counting units {len(units)} "
          f"({sum(1 for u in units if len(u) == 2)} pairs, {sum(1 for u in units if len(u) == 1)} singles/lone mates)")

total_runs = 0
total_mism = 0
total_mism_hc2 = 0
n_doc_mism = []
summary = []
for label, (recs, units, name_bam, pos_bam) in datasets.items():
    print(f"\n== {label}")
    for stranded in ("yes", "no", "reverse"):
        sets, ids = per_base_sets(features, ["exon"], ["gene_id"], stranded=(stranded != "no"))
        for mode in ("union", "intersection-strict", "intersection-nonempty"):
            for nonunique in ("none", "all", "fraction"):
                for sec, supp, minaqual in (("ignore", "ignore", 10), ("score", "score", 10),
                                            ("score", "ignore", 0), ("ignore", "score", 30)):
                    port = port_count(units, sets, ids, mode, stranded, nonunique, minaqual, sec, supp)
                    port_hc2 = port_count(units, sets, ids, mode, stranded, nonunique, minaqual, sec, supp,
                                          unmapped_mate_mapq=0)
                    extra = ["-m", mode, "-s", stranded, "--nonunique", nonunique, "-a", str(minaqual),
                             "--secondary-alignments", sec, "--supplementary-alignments", supp]
                    orders = (("name", name_bam), ("pos", pos_bam)) if label == "paired-end" else (("name", name_bam),)
                    for order, bam in orders:
                        cli, err = run_htseq_count(bam, gtf, extra + ["-r", order])
                        mism = compare(port, cli, tol=1e-6)
                        mism2 = compare(port_hc2, cli, tol=1e-6)
                        total_runs += 1
                        if mism:
                            total_mism += 1
                            n_doc_mism.append((label, stranded, mode, nonunique, sec, supp, minaqual, order,
                                               len(mism), mism[:3]))
                        if mism2:
                            total_mism_hc2 += 1
                            print(f"MISMATCH (even modelling HC2) {label} -s {stranded} -m {mode} --nonunique "
                                  f"{nonunique} -a {minaqual} sec={sec} supp={supp} -r {order}: {mism2[:6]}")
                        summary.append((label, stranded, mode, nonunique, sec, supp, minaqual, order, len(mism),
                                        len(mism2),
                                        round(sum(float(v) for k, v in cli.items() if not k.startswith("__")), 3),
                                        {k[2:]: int(cli[k]) for k in SPECIAL}))
    print(f"  runs so far: {total_runs}; runs with any mismatch vs the documented port: {total_mism}; "
          f"vs the port modelling HC2 (unmapped mate's MAPQ 0 compared with -a): {total_mism_hc2}")
print(f"\nCLI runs: {total_runs}; mismatching vs documented port: {total_mism}; "
      f"mismatching vs port modelling HC2: {total_mism_hc2}")
print("\nRuns mismatching the documented port (all paired-end; first 3 differing keys as (key, port, cli)):")
for row in n_doc_mism[:12]:
    print("  ", row)
print(f"   ... {len(n_doc_mism)} such runs; they all use -a > 0 (with -a 0 the unmapped mate's MAPQ 0 passes):",
      all(r[6] > 0 for r in n_doc_mism))
print("\nSample rows (dataset, stranded, mode, nonunique, sec, supp, -a, order, n_mismatch_doc, n_mismatch_hc2, "
      "sum(feature counts), specials):")
for row in summary[::17]:
    print("  ", row)
recs, units, name_bam, pos_bam = datasets["paired-end"]

# --nonunique random: conservation only
print("\n== --nonunique random (conservation: feature sum == unique + ambiguous, both orders)")
sets, ids = per_base_sets(features, ["exon"], ["gene_id"], stranded=True)
for mode in ("union", "intersection-nonempty"):
    for order, bam in (("name", name_bam), ("pos", pos_bam)):
        none, _ = run_htseq_count(bam, gtf, ["-m", mode, "-s", "yes", "--nonunique", "none", "-r", order])
        uniq = sum(v for k, v in none.items() if not k.startswith("__"))
        amb = none["__ambiguous"]
        cli, _ = run_htseq_count(bam, gtf, ["-m", mode, "-s", "yes", "--nonunique", "random", "-r", order])
        s = sum(v for k, v in cli.items() if not k.startswith("__"))
        print(f"  {mode:22s} -r {order}: feature sum {s:g} == unique {uniq:g} + ambiguous {amb:g}"
              f" -> {'OK' if abs(s - (uniq + amb)) < 1e-9 else 'MISMATCH'}; "
              f"__ambiguous reported {cli['__ambiguous']:g}")

# multiple -i and --additional-attr and -t multiple types: port with gene_id:gene_name id and exon+gene types
print("\n== -i gene_id -i gene_name (joined id) and -t exon -t gene, union, stranded yes, -r name")
sets2, ids2 = per_base_sets(features, ["exon", "gene"], ["gene_id", "gene_name"], stranded=True)
port = port_count(units, sets2, ids2, "union", "yes", "none", unmapped_mate_mapq=0)
cli, _ = run_htseq_count(name_bam, gtf, ["-m", "union", "-s", "yes", "-i", "gene_id", "-i", "gene_name",
                                          "-t", "exon", "-t", "gene", "--additional-attr", "gene_name"])
mism = compare(port, cli)
print(f"  ids in output: {sum(1 for k in cli if not k.startswith('__'))} (port {len(ids2)}); mismatches: {mism[:5]}")

print("\n== --feature-query 'gene_name == \"N7\"'  (only that gene's exons are features)")
sets3, ids3 = per_base_sets([f for f in features if f[5]["gene_name"] == "N7"], ["exon"], ["gene_id"], True)
n7_chroms = {f[0] for f in features if f[5]["gene_name"] == "N7"}
port = port_count(units, sets3, ids3, "union", "yes", "none", unmapped_mate_mapq=0)
port_uc = port_count(units, sets3, ids3, "union", "yes", "none", unmapped_mate_mapq=0, feature_chroms=n7_chroms)
cli, _ = run_htseq_count(name_bam, gtf, ["-m", "union", "-s", "yes", "--feature-query", 'gene_name == "N7"'])
print(f"  N7 lies on {sorted(n7_chroms)}; counts: { {k: v for k, v in cli.items() if not k.startswith('__')} }")
print(f"  mismatches vs port: {compare(port, cli)}")
print(f"  mismatches vs port that also models the UnknownChrom rule (a pair with a mate on a chromosome without "
      f"features is __no_feature as a whole): {compare(port_uc, cli)}")
print("\n(the last two checks use the port modelling HC2, on the paired-end data)")
print("\nDONE; mismatching vs documented port:", total_mism, "; vs port modelling HC2:", total_mism_hc2)
