#!/usr/bin/env python3
"""Brute-force comparison of the shipped featureCounts against fcref.py (an
independent implementation of the documented rules) on random annotations and
random single-end and paired-end BAM records, under a matrix of option sets.

For every option set it compares, per fragment, the `-R CORE` status and the
target list, and, per gene/feature, the count column; every disagreement is
printed with the fragment's records so the cause can be traced in the code.

Usage: python heldup_bruteforce_random.py [seed] [n_frags]
"""
import os
import random
import sys
import tempfile
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib
import fcref

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
NFRAG = int(sys.argv[2]) if len(sys.argv) > 2 else 400
rng = random.Random(seed)
print("featureCounts", fclib.fc_version(), "| seed", seed, "| fragments per file", NFRAG)

CHROMS = {"chr1": 20000, "chr2": 12000}


def random_annotation():
    genes = []
    gid = 0
    for chrom, L in CHROMS.items():
        cur = 100
        while cur < L - 1500:
            n_ex = rng.choice([1, 1, 2, 3, 4])
            strand = rng.choice(["+", "-", "+", "-", "."])
            exons = []
            p = cur
            for _ in range(n_ex):
                el = rng.randint(30, 400)
                exons.append((p, p + el - 1))
                p += el + rng.randint(20, 300)
            genes.append((f"G{gid:03d}", chrom, strand, exons))
            gid += 1
            # next gene: sometimes overlapping the previous one, sometimes far away
            cur = rng.choice([exons[-1][1] - rng.randint(0, 200), exons[0][0] + rng.randint(0, 100), p + rng.randint(0, 600)])
            cur = max(cur, 1)
    # a few duplicated exon lines (as GTFs with several transcripts have)
    for _ in range(4):
        g = rng.choice(genes)
        s, e = rng.choice(g[3])
        g[3].append((s, e + rng.randint(-10, 10)))
    return genes


def random_cigar(kind):
    parts = []
    if kind == "plain":
        parts = [(rng.randint(20, 100), "M")]
    elif kind == "soft":
        parts = [(rng.randint(2, 15), "S"), (rng.randint(20, 80), "M"), (rng.randint(2, 15), "S")]
        if rng.random() < 0.5:
            parts = parts[:2]
        else:
            parts = parts[1:]
    elif kind == "split":
        parts = [(rng.randint(10, 60), "M"), (rng.randint(50, 800), "N"), (rng.randint(10, 60), "M")]
        if rng.random() < 0.3:
            parts += [(rng.randint(50, 400), "N"), (rng.randint(5, 40), "M")]
    elif kind == "indel":
        parts = [(rng.randint(10, 40), "M"), (rng.randint(1, 5), rng.choice("ID")), (rng.randint(10, 40), "M")]
        if rng.random() < 0.4:
            parts += [(rng.randint(1, 3), rng.choice("ID")), (rng.randint(5, 30), "M")]
    return "".join(f"{n}{op}" for n, op in parts)


def random_pos(chrom, cig):
    L = CHROMS[chrom]
    return rng.randint(1, max(1, L - fclib.cigar_ref_len(cig) - 1))


def random_records(paired):
    recs = []
    truth = []  # (name, [records]) per fragment
    for i in range(NFRAG):
        name = f"r{i:05d}"
        kind = rng.choice(["plain", "plain", "plain", "soft", "split", "split", "indel"])
        mapq = rng.choice([60, 60, 60, 30, 10, 5, 1, 0, 255])
        nh = rng.choice([1, 1, 1, 1, 2, 3])
        dup = rng.random() < 0.08
        chrom = rng.choice(list(CHROMS))
        if not paired:
            frag = []
            if rng.random() < 0.05:
                frag.append(dict(name=name, flag=4 | (1024 if dup else 0), chrom=None, readlen=50))
            else:
                for k in range(nh):
                    cig = random_cigar(kind)
                    c = chrom if k == 0 else rng.choice(list(CHROMS))
                    r = fclib.single(name, c, random_pos(c, cig), cig, rev=rng.random() < 0.5, mapq=mapq,
                                     tags={"NH": nh} if nh > 1 else {},
                                     extra_flag=(1024 if dup else 0) | (256 if k > 0 else 0))
                    frag.append(r)
            recs += frag
            truth.append((name, frag))
        else:
            frag = []
            u = rng.random()
            if u < 0.04:   # both unmapped
                frag = [dict(name=name, flag=1 | 4 | 8 | 64 | (1024 if dup else 0), chrom=None, readlen=50),
                        dict(name=name, flag=1 | 4 | 8 | 128, chrom=None, readlen=50)]
            elif u < 0.14:  # one end unmapped, mate record present
                cig = random_cigar(kind)
                p = random_pos(chrom, cig)
                rev = rng.random() < 0.5
                which = rng.random() < 0.5
                m = dict(name=name, flag=1 | 8 | (16 if rev else 0) | (64 if which else 128) | (1024 if dup else 0),
                         chrom=chrom, pos=p, cigar=cig, mapq=mapq, mchrom=chrom, mpos=p, tlen=0,
                         tags={"NH": nh} if nh > 1 else {})
                um = dict(name=name, flag=1 | 4 | (32 if rev else 0) | (128 if which else 64), chrom=chrom, pos=p,
                          mapq=0, mchrom=chrom, mpos=p, tlen=0, readlen=50)
                frag = [m, um]
            elif u < 0.19:  # single-end read inside a paired-end file
                cig = random_cigar(kind)
                frag = [fclib.single(name, chrom, random_pos(chrom, cig), cig, rev=rng.random() < 0.5, mapq=mapq,
                                     extra_flag=(1024 if dup else 0))]
            else:
                for k in range(nh):
                    cig1, cig2 = random_cigar(kind), random_cigar(rng.choice(["plain", "plain", "split", "soft"]))
                    c1 = chrom if k == 0 else rng.choice(list(CHROMS))
                    c2 = c1 if rng.random() < 0.9 else rng.choice(list(CHROMS))
                    p1 = random_pos(c1, cig1)
                    if c2 == c1:
                        p2 = min(max(1, p1 + rng.randint(-150, 400)), CHROMS[c2] - fclib.cigar_ref_len(cig2) - 1)
                    else:
                        p2 = random_pos(c2, cig2)
                    r1rev = rng.random() < 0.5
                    r2rev = (not r1rev) if rng.random() < 0.85 else r1rev
                    pr = fclib.pair(name, c1, p1, cig1, p2, cig2, r1_rev=r1rev, r2_rev=r2rev, mapq=mapq,
                                    tags={"NH": nh, "HI": k + 1} if nh > 1 else {},
                                    extra_flag=(256 if k > 0 else 0), chrom2=c2)
                    if dup:
                        pr[rng.randrange(2)]["flag"] |= 1024
                    if rng.random() < 0.15:  # mates with different MAPQ
                        pr[1]["mapq"] = rng.choice([0, 3, 60])
                    frag += pr
            recs += frag
            truth.append((name, frag))
    rng.shuffle(recs)
    # featureCounts walks a pair's two records with the record that comes LATER
    # in the file first (the pairer hands over the current record and the
    # mate it had stored); the labels of fragments failing two filters depend
    # on that order, so keep each fragment's records in reverse file order.
    order = {id(r): i for i, r in enumerate(recs)}
    truth = [(name, sorted(frag, key=lambda r: -order[id(r)])) for name, frag in truth]
    return recs, truth


def to_reads(frag, opt):
    reads = [fcref.Read(r, opt.get("ext5", 0), opt.get("ext3", 0), opt.get("read2pos", 0)) for r in frag]
    return reads


def reference(truth, ann, opt):
    """Per-fragment expectations, mirroring how featureCounts groups records."""
    pe = opt.get("pe")
    counts = defaultdict(int)
    per_align = defaultdict(list)  # name -> list of (status, {name: units})
    for name, frag in truth:
        if not pe:
            for rec in frag:
                sopt = dict(opt, pe=False)
                st, inc = fcref.assign([fcref.Read(rec, opt.get("ext5", 0), opt.get("ext3", 0), opt.get("read2pos", 0))], ann, sopt)
                per_align[name].append((st, inc))
                for k, v in inc.items():
                    counts[k] += v
        else:
            # group the fragment's records into alignment pairs by HI tag / order
            groups = defaultdict(list)
            for rec in frag:
                groups[rec.get("tags", {}).get("HI", 0)].append(rec)
            for hi, g in groups.items():
                reads = to_reads(g, opt)
                if len(reads) == 1:
                    r = reads[0]
                    # a single-end record in paired mode: the missing mate is an unmapped placeholder
                    ph = fcref.Read(dict(name=name, flag=4 | 128, chrom=None, mapq=0), 0, 0, 0)
                    reads = [r, ph]
                st, inc = fcref.assign(reads, ann, dict(opt, code_order=True))
                per_align[name].append((st, inc))
                for k, v in inc.items():
                    counts[k] += v
    return per_align, counts


OPTION_SETS = {
    "default": {},
    "-O": {"O": 1},
    "-s 1": {"strand": 1},
    "-s 2": {"strand": 2},
    "-M": {"M": 1},
    "-M --fraction": {"M": 1, "fraction": 1},
    "--primary": {"primary": 1},
    "-M --primary": {"M": 1, "primary": 1},
    "-O --fraction": {"O": 1, "fraction": 1},
    "-M -O --fraction": {"M": 1, "O": 1, "fraction": 1},
    "-Q 10": {"Q": 10},
    "-Q 30 -s 2": {"Q": 30, "strand": 2},
    "--ignoreDup": {"ignoreDup": 1},
    "--splitOnly": {"splitOnly": 1},
    "--nonSplitOnly": {"nonSplitOnly": 1},
    "--minOverlap 10": {"minOverlap": 10},
    "--fracOverlap 0.5": {"fracOverlap": 0.5},
    "--fracOverlap 1": {"fracOverlap": 1.0},
    "--largestOverlap": {"largestOverlap": 1},
    "-O --largestOverlap": {"O": 1, "largestOverlap": 1},
    "--nonOverlap 5": {"nonOverlap": 5},
    "--fracOverlapFeature 0.5": {"fracOverlapFeature": 0.5},
    "--nonOverlapFeature 20": {"nonOverlapFeature": 20},
    "--minOverlap 10 --largestOverlap -O --fraction": {"minOverlap": 10, "largestOverlap": 1, "O": 1, "fraction": 1},
    "-f": {"f": 1},
    "-f -O": {"f": 1, "O": 1},
    "-f -O --fraction --largestOverlap": {"f": 1, "O": 1, "fraction": 1, "largestOverlap": 1},
    "--read2pos 5": {"read2pos": 5},
    "--read2pos 3 -s 1": {"read2pos": 3, "strand": 1},
    "--readExtension5 20": {"ext5": 20},
    "--readExtension3 20 -s 2": {"ext3": 20, "strand": 2},
}
PE_ONLY = {
    "-B": {"B": 1},
    "-C": {"C": 1},
    "-B -C -s 2": {"B": 1, "C": 1, "strand": 2},
    "-P -B -d 50 -D 300": {"P": 1, "B": 1, "d": 50, "D": 300},
    "-P -B -C -d 100 -D 250 -Q 10": {"P": 1, "B": 1, "C": 1, "d": 100, "D": 250, "Q": 10},
}


def cli_args(opt):
    a = []
    if opt.get("pe"):
        # releases before 2.0.2 have no --countReadPairs: `-p` alone counts fragments there
        a += ["-p"] if os.environ.get("FC_OLD_PE") else ["-p", "--countReadPairs"]
    elif opt.get("p_only"):
        a += ["-p"]
    for k, flag in [("O", "-O"), ("M", "-M"), ("primary", "--primary"), ("fraction", "--fraction"),
                    ("ignoreDup", "--ignoreDup"), ("splitOnly", "--splitOnly"), ("nonSplitOnly", "--nonSplitOnly"),
                    ("largestOverlap", "--largestOverlap"), ("f", "-f"), ("B", "-B"), ("C", "-C"), ("P", "-P")]:
        if opt.get(k):
            a.append(flag)
    for k, flag in [("strand", "-s"), ("Q", "-Q"), ("minOverlap", "--minOverlap"), ("fracOverlap", "--fracOverlap"),
                    ("nonOverlap", "--nonOverlap"), ("fracOverlapFeature", "--fracOverlapFeature"),
                    ("nonOverlapFeature", "--nonOverlapFeature"), ("read2pos", "--read2pos"),
                    ("ext5", "--readExtension5"), ("ext3", "--readExtension3"), ("d", "-d"), ("D", "-D")]:
        if opt.get(k) is not None and opt.get(k) != 0:
            a += [flag, str(opt[k])]
    return a


def compare(label, opt, truth, ann, wd, bam, gtf):
    counts, summary, details, log = fclib.run_fc(gtf, bam, cli_args(opt), workdir=wd)
    per_align, ref_counts = reference(truth, ann, opt)
    # 1. summary rows sum to the number of fragments/alignments featureCounts saw
    n_units = sum(len(v) for v in per_align.values())
    tot = fclib.summary_total(summary)
    # 2. statuses: featureCounts prints one CORE line per alignment (pair); compare multisets per read name
    mism = []
    core_by_name = defaultdict(list)
    with open(os.path.join(wd, os.path.basename(bam) + ".featureCounts")) as f:
        for line in f:
            t = line.rstrip("\n").split("\t")
            core_by_name[t[0]].append((t[1], t[3] if len(t) > 3 and t[3] != "NA" else ""))
    feature_level = opt.get("f")
    for name, exp in per_align.items():
        got = core_by_name.get(name, [])
        if feature_level:
            # in -f mode the CORE target column carries the gene_id of the feature, not the feature
            exp_s = sorted((st, ",".join(sorted(ann.feats[int(k[5:]) - 1][5] for k in inc))) for st, inc in exp)
        else:
            exp_s = sorted((st, ",".join(sorted(inc))) for st, inc in exp)
        got_s = sorted((st, ",".join(sorted(tg.split(","))) if tg else "") for st, tg in got)
        if exp_s != got_s:
            mism.append((name, exp_s, got_s))
    # 3. counts
    cmism = []
    allkeys = set(counts) | set(ref_counts)
    for k in allkeys:
        e = ref_counts.get(k, 0) / fcref.NH_INT
        g = counts.get(k, 0.0)
        if abs(e - g) > 0.011:
            cmism.append((k, round(e, 3), g))
    status = "OK" if not mism and not cmism and tot == n_units else "MISMATCH"
    print(f"[{label}] {' '.join(cli_args(opt)) or '(defaults)'}: summary total {tot} vs {n_units} units; "
          f"status/target mismatches {len(mism)}/{len(per_align)}; count mismatches {len(cmism)}/{len(allkeys)} -> {status}")
    return mism, cmism, summary


def main():
    wd = tempfile.mkdtemp(prefix="fcbrute_")
    genes = random_annotation()
    ann_g = fcref.Ann(genes, feature_level=False)
    ann_f = fcref.Ann(genes, feature_level=True)
    gtf = os.path.join(wd, "ann.gtf")
    fclib.write_gtf(gtf, genes)
    print(f"annotation: {len(genes)} genes, {sum(len(g[3]) for g in genes)} exon lines")
    all_mism = {}
    modes = ("SE", "PE") if os.environ.get("FC_OLD_PE") else ("SE", "PE", "PE-as-reads")
    for mode in modes:
        paired = mode == "PE"
        if mode != "PE-as-reads":
            recs, truth = random_records(mode == "PE")
            bam = os.path.join(wd, f"{mode}.bam")
            fclib.make_bam(bam, CHROMS, recs)
        else:
            # the paired-end file counted read by read: `-p` without --countReadPairs (2.0.2+)
            truth = [(n, [r]) for n, frag in truth for r in frag]
        print(f"\n== {mode}: {len(recs)} records, {len(truth)} fragments/records")
        sets = dict(OPTION_SETS)
        if paired:
            sets.update(PE_ONLY)
        if mode == "PE-as-reads":
            sets = {k: v for k, v in sets.items() if k in ("default", "-s 1", "-s 2", "-M --fraction", "-Q 10", "--ignoreDup", "--fracOverlap 0.5", "-O")}
        for label, o in sets.items():
            opt = dict(o)
            opt["pe"] = paired
            opt["p_only"] = mode == "PE-as-reads"
            ann = ann_f if opt.get("f") else ann_g
            mism, cmism, summary = compare(label, opt, truth, ann, wd, bam, gtf)
            if mism or cmism:
                all_mism[(mode, label)] = (mism, cmism)
                for name, e, g in mism[:6]:
                    print("    status:", name, "expected", e, "got", g)
                    for r in dict(truth)[name]:
                        print("        ", {k: v for k, v in r.items() if k != "tags"} | {"tags": r.get("tags", {})})
                for k, e, g in cmism[:6]:
                    print("    count:", k, "expected", e, "got", g)
    print("\nOption sets with any disagreement:", len(all_mism))
    for k in all_mism:
        print("  ", k)


if __name__ == "__main__":
    main()
