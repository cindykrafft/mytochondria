"""Mapped-read filters (--outFilterMismatchNmax, --outFilterMismatchNoverLmax,
--outFilterScoreMinOverLread / --outFilterMatchNminOverLread, --outFilterMultimapNmax,
--outFilterType BySJout) and every number in Log.final.out.

Truth for the filters: reads of the single-exon gene G17 carry k = 0..20 planted
mismatches (20 reads per k, 100 bp, --alignEndsType EndToEnd so nothing is soft-clipped).
ReadAlign_mappedFilter.cpp tests, in order: score < int(0.66 * 99) = 65 or matches < 65
-> "too short"; mismatches > 10 or mismatches / mapped length > 0.3 -> "too many
mismatches"; loci > --outFilterMultimapNmax -> "too many loci". A 100-bp end-to-end read
with k mismatches scores 100 - 2k - 2 (the log2 length term is -2), so k <= 10 maps,
11 <= k <= 16 is "too many mismatches" and k >= 17 is "too short". The uT:A tag of the
unmapped records (0 other, 1 short, 2 mismatches, 3 multi) gives STAR's reason.

Truth for Log.final.out: recomputed from the SAM (unique reads only for the mapped-length,
splice, mismatch and indel lines, as the manual states) and the FASTQ.

Usage: python heldup_filters_logfinal.py <STAR binary> <work dir>
"""
import os, sys, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _synth as S

star, W = sys.argv[1], sys.argv[2]
g, trs, rs = S.standard_dataset(W)
gidx = S.genome_generate(star, W, os.path.join(W, "gidx"))
annot = S.gtf_junctions(trs)

rng = random.Random(11)
mm = []
for k in range(0, 21):
    for i in range(20):
        s = rng.randrange(140001, 140401)
        seq = list(g["chrA"][s - 1:s + 99])
        for p in rng.sample(range(0, 100), k):
            seq[p] = rng.choice([b for b in "ACGT" if b != seq[p]])
        mm.append(("mm%02d_%02d" % (k, i), "".join(seq), "I" * 100))
with open(os.path.join(W, "mm.fq"), "w") as fh:
    for n, s, q in mm:
        fh.write("@%s\n%s\n+\n%s\n" % (n, s, q))


def classes(outdir):
    out = collections.defaultdict(collections.Counter)
    for name, recs in S.read_sam(os.path.join(outdir, "Aligned.out.sam")).items():
        k = int(name[2:4])
        m = [r for r in recs if not r.is_unmapped]
        if m:
            out[k]["mapped(nM=%d)" % m[0].get_tag("nM")] += 1
        else:
            out[k]["unmapped uT=%s" % recs[0].get_tag("uT")] += 1
    return out


def show(outdir, label, expect, nmax):
    """expect(k) is the outcome at the simulated locus; STAR may instead find an alternative
    alignment with fewer mismatches (an indel placement) or no seed at all ('other', uT=0), so
    only outcomes the filter rules exclude count as differences: mapped with nM > nmax, or a
    read with k <= nmax planted mismatches reported as 'too short' / 'too many mismatches'."""
    print("\n== %s ==" % label)
    c = classes(outdir)
    bad = 0
    for k in sorted(c):
        e = expect(k)
        impossible = [key for key in c[k] if (key.startswith("mapped") and int(key[10:-1]) > nmax) or (k <= nmax and key in ("unmapped uT=1", "unmapped uT=2"))]
        bad += len(impossible)
        print("  k=%2d  %-52s at the simulated locus: %-14s %s" % (k, dict(c[k]), e, "" if not impossible else "<-- IMPOSSIBLE " + str(impossible)))
    lf = S.log_final(outdir)
    print("  Log.final.out: unique %s, too many mismatches %s, too short %s, other %s" % (lf["Uniquely mapped reads number"],
          lf["Number of reads unmapped: too many mismatches"], lf["Number of reads unmapped: too short"], lf["Number of reads unmapped: other"]))
    return bad


tot = 0
o = S.run_star(star, gidx, os.path.join(W, "f_mm"), [os.path.join(W, "mm.fq")], quant=(), extra=["--alignEndsType", "EndToEnd"])
tot += show(o, "EndToEnd, defaults (--outFilterMismatchNmax 10, --outFilterMismatchNoverLmax 0.3, --outFilterScoreMinOverLread 0.66)",
            lambda k: "mapped" if k <= 10 else "unmapped uT=2" if k <= 16 else "unmapped uT=1", 10)
o = S.run_star(star, gidx, os.path.join(W, "f_mm05"), [os.path.join(W, "mm.fq")], quant=(), extra=["--alignEndsType", "EndToEnd", "--outFilterMismatchNoverLmax", "0.05"])
tot += show(o, "EndToEnd, --outFilterMismatchNoverLmax 0.05 (5/100 allowed, 6/100 not)",
            lambda k: "mapped" if k <= 5 else "unmapped uT=2" if k <= 16 else "unmapped uT=1", 5)
o = S.run_star(star, gidx, os.path.join(W, "f_mm_n3"), [os.path.join(W, "mm.fq")], quant=(), extra=["--alignEndsType", "EndToEnd", "--outFilterMismatchNmax", "3"])
tot += show(o, "EndToEnd, --outFilterMismatchNmax 3", lambda k: "mapped" if k <= 3 else "unmapped uT=2" if k <= 16 else "unmapped uT=1", 3)
o = S.run_star(star, gidx, os.path.join(W, "f_mm_local"), [os.path.join(W, "mm.fq")], quant=())
print("\n== Local (default) alignment of the same reads: mismatches near the ends are soft-clipped instead ==")
for k, c in sorted(classes(o).items()):
    print("  k=%2d  %s" % (k, dict(c)))

# --outFilterMultimapNmax boundary: 5-locus reads (multi5) and 2-locus reads (T13)
print("\n== --outFilterMultimapNmax boundary (nTr > Nmax -> 'too many loci') ==")
for nmax in (1, 2, 4, 5):
    o = S.run_star(star, gidx, os.path.join(W, "f_mult%d" % nmax), [os.path.join(W, "se.fq")], quant=(), extra=["--outFilterMultimapNmax", str(nmax)])
    c = collections.Counter()
    for name, recs in S.read_sam(os.path.join(o, "Aligned.out.sam")).items():
        kind = "multi5" if name.startswith("m5_") else "G13(x2)" if name.endswith("_T13") else None
        if kind:
            m = [r for r in recs if not r.is_unmapped]
            c[(kind, "NH=%d" % m[0].get_tag("NH") if m else "unmapped uT=%s" % recs[0].get_tag("uT"))] += 1
    lf = S.log_final(o)
    print("  Nmax=%d: %s; Log.final.out too many loci = %s" % (nmax, dict(sorted(c.items())), lf["Number of reads mapped to too many loci"]))

# Log.final.out numbers recomputed from the SAM on the standard SE reads + indel reads + mismatch reads
allfq = os.path.join(W, "all.fq")
with open(allfq, "w") as out:
    for f in ("se.fq", "mm.fq"):
        out.write(open(os.path.join(W, f)).read())
    for i in range(40):
        s = rng.randrange(140001, 140380); seq = g["chrA"][s - 1:s + 119]; p = 50
        d = [1, 2, 3, 5][i % 4]
        read = (seq[:p] + seq[p + d:])[:100] if i % 2 == 0 else (seq[:p] + "".join(rng.choice("ACGT") for _ in range(d)) + seq[p:])[:100]
        out.write("@lfindel_%03d\n%s\n+\n%s\n" % (i, read, "I" * 100))


def recompute(outdir, nreads, sumlen):
    reads = S.read_sam(os.path.join(outdir, "Aligned.out.sam"))
    U = M = 0; unm = collections.Counter()
    mapped_bases = mism = 0; spl = collections.Counter(); spl_annot = 0
    delN = delL = insN = insL = 0
    for name, recs in reads.items():
        al = S.alignments(recs)
        if not al:
            unm[recs[0].get_tag("uT")] += 1; continue
        if len(al) > 1:
            M += 1; continue
        U += 1
        for r in list(al.values())[0]:
            mism += r.get_tag("nM") if r is list(al.values())[0][0] else 0
            for op, ln in r.cigartuples:
                if op == 0:
                    mapped_bases += ln
                elif op == 2:
                    delN += 1; delL += ln
                elif op == 1:
                    insN += 1; insL += ln
            for s, e, l, rt in S.junctions_of(r):
                key = (r.reference_name, s, e)
                spl[S.motif_code(g, *key)] += 1
                spl_annot += key in annot
    pct = lambda x: "%.2f%%" % (100.0 * x / nreads)
    exp = {
        "Number of input reads": str(nreads),
        "Average input read length": str(sumlen // nreads),
        "Uniquely mapped reads number": str(U),
        "Uniquely mapped reads %": pct(U),
        "Average mapped length": "%.2f" % (mapped_bases / U),
        "Number of splices: Total": str(sum(spl.values())),
        "Number of splices: Annotated (sjdb)": str(spl_annot),
        "Number of splices: GT/AG": str(spl[1] + spl[2]),
        "Number of splices: GC/AG": str(spl[3] + spl[4]),
        "Number of splices: AT/AC": str(spl[5] + spl[6]),
        "Number of splices: Non-canonical": str(spl[0]),
        "Mismatch rate per base, %": "%.2f%%" % (100.0 * mism / mapped_bases),
        "Deletion rate per base": "%.2f%%" % (100.0 * delL / mapped_bases),
        "Deletion average length": "%.2f" % (delL / delN if delN else 0),
        "Insertion rate per base": "%.2f%%" % (100.0 * insL / mapped_bases),
        "Insertion average length": "%.2f" % (insL / insN if insN else 0),
        "Number of reads mapped to multiple loci": str(M),
        "% of reads mapped to multiple loci": pct(M),
        "Number of reads mapped to too many loci": str(unm["3"]),
        "% of reads mapped to too many loci": pct(unm["3"]),
        "Number of reads unmapped: too many mismatches": str(unm["2"]),
        "% of reads unmapped: too many mismatches": pct(unm["2"]),
        "Number of reads unmapped: too short": str(unm["1"]),
        "% of reads unmapped: too short": pct(unm["1"]),
        "Number of reads unmapped: other": str(unm["0"]),
        "% of reads unmapped: other": pct(unm["0"]),
    }
    return exp


def check_log(outdir, label, nreads, sumlen):
    lf = S.log_final(outdir)
    exp = recompute(outdir, nreads, sumlen)
    bad = 0
    print("\n== Log.final.out: %s ==" % label)
    for k, v in exp.items():
        got = lf[k]
        flag = "" if got == v else "   <-- DIFFERS"
        bad += got != v
        print("  %-48s STAR %-12s truth %-12s%s" % (k, got, v, flag))
    print("  lines differing: %d of %d" % (bad, len(exp)))
    return bad


n = sum(1 for l in open(allfq)) // 4
o = S.run_star(star, gidx, os.path.join(W, "f_log_se"), [allfq], quant=(), extra=["--outFilterMultimapNmax", "4"])
tot += check_log(o, "single-end (standard + mismatch + indel reads, --outFilterMultimapNmax 4)", n, 100 * n)
o = S.run_star(star, gidx, os.path.join(W, "f_log_pe"), [os.path.join(W, "pe_1.fq"), os.path.join(W, "pe_2.fq")], quant=())
tot += check_log(o, "paired-end (read length = sum of mates)", len(rs.pe1), 150 * len(rs.pe1))
o = S.run_star(star, gidx, os.path.join(W, "f_log_sjout"), [allfq], quant=(), extra=["--outFilterType", "BySJout"])
tot += check_log(o, "single-end, --outFilterType BySJout (reads held for the 2nd stage must be counted once)", n, 100 * n)
print("\nTOTAL differences: %d" % tot)
