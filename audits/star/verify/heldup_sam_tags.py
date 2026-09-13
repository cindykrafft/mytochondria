"""SAM records: NH/HI/MAPQ/AS/nM/jM/jI/XS, flags, primary choice, and alignment accuracy.

Truth, per alignment of STAR's Aligned.out.sam:
  NH  = number of distinct HI values of the read; HI runs 1..NH;
  MAPQ = 255 (NH 1), 3 (NH 2), 1 (NH 3-4), 0 (NH >= 5) as documented;
  exactly one alignment per read is primary and its AS is the read's maximum;
  nM  = mismatches between the read and the genome over the M blocks of all mates
        (an N in the read or genome is not a mismatch);
  AS  = sum over M bases (+1 match, -1 mismatch) + per junction (+2 --sjdbScore if the
        intron is in the GTF, else --scoreGap 0 plus --scoreGapNoncan -8 / --scoreGapGCAG -4 /
        --scoreGapATAC -8 by motif) + per deletion (-2 - 2*len) + per insertion (-2 - 2*len)
        + int(ceil(log2(genomic span) * -0.25 - 0.5)), floored at 0 (stitchAlignToTranscript.cpp,
        stitchWindowAligns.cpp:222 and parametersDefault);
  jM  = motif code + 20 if annotated, jI = intron start/end (1-based), -1 when unspliced;
  XS  (with --outSAMstrandField intronMotif) = + for motifs 1/3/5, - for 2/4/6 (for a
        junction in the GTF the annotated strand, which STAR uses in place of the motif; a
        GTF junction with strand '.' falls back to the motif),
        absent when unspliced; alignments whose only junctions are unannotated non-canonical
        are suppressed.
Alignment accuracy: the primary alignment's blocks equal the simulated blocks.

Usage: python heldup_sam_tags.py <STAR binary> <work dir>
"""
import os, sys, math, collections, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _synth as S

star, W = sys.argv[1], sys.argv[2]
g, trs, rs = S.standard_dataset(W)
gidx = S.genome_generate(star, W, os.path.join(W, "gidx"))
annot = S.gtf_junctions(trs)
JPEN = {0: -8, 1: 0, 2: 0, 3: -4, 4: -4, 5: -8, 6: -8}

# extra reads with indels from the single-exon gene G17 (chrA 140001-140500)
rng = random.Random(5)
indel = []
for i in range(60):
    s = rng.randrange(140001, 140380)
    seq = g["chrA"][s - 1:s + 119]
    if i % 2 == 0:
        d = [1, 2, 3, 5][i // 2 % 4]; p = 40 + rng.randrange(0, 30)
        read = (seq[:p] + seq[p + d:])[:100]; kind = "del%d" % d
    else:
        d = [1, 2, 3][i // 2 % 3]; p = 40 + rng.randrange(0, 30)
        read = (seq[:p] + "".join(rng.choice("ACGT") for _ in range(d)) + seq[p:])[:100]; kind = "ins%d" % d
    indel.append(("indel_%03d_%s" % (i, kind), read, "I" * 100))
with open(os.path.join(W, "indel.fq"), "w") as fh:
    for n, s, q in indel:
        fh.write("@%s\n%s\n+\n%s\n" % (n, s, q))


def expected_as(mates):
    score = 0
    lo, hi = 10**12, 0
    for r in mates:
        q = r.query_sequence; s = g[r.reference_name]
        qpos, rpos = 0, r.reference_start
        for op, ln in r.cigartuples:
            if op in (0, 7, 8):
                for i in range(ln):
                    a, b = q[qpos + i], s[rpos + i]
                    if a != "N" and b != "N":
                        score += 1 if a == b else -1
                lo = min(lo, rpos + 1); hi = max(hi, rpos + ln)
                qpos += ln; rpos += ln
            elif op == 4:
                qpos += ln
            elif op == 1:
                score += -2 - 2 * ln; qpos += ln
            elif op == 2:
                score += -2 - 2 * ln; rpos += ln
            elif op == 3:
                key = (r.reference_name, rpos + 1, rpos + ln)
                score += 2 if key in annot else JPEN[S.motif_code(g, *key)]
                rpos += ln
    score += math.ceil(math.log2(hi - lo + 1) * -0.25 - 0.5)
    return max(0, score)


def check(outdir, label, paired=False, xs=False):
    reads = S.read_sam(os.path.join(outdir, "Aligned.out.sam"))
    c = collections.Counter()
    ex = []
    for name, recs in reads.items():
        al = S.alignments(recs)
        if not al:
            continue
        nh = len(al)
        c["alignments"] += len(al)
        if sorted(al) == list(range(1, nh + 1)):
            c["HI consecutive 1..NH"] += 1
        prim = [hi for hi, m in al.items() if not m[0].is_secondary]
        maxas = max(m[0].get_tag("AS") for m in al.values())
        if len(prim) == 1 and al[prim[0]][0].get_tag("AS") == maxas:
            c["one primary with max AS"] += 1
        else:
            c["primary wrong"] += 1
        for hi, mates in al.items():
            r0 = mates[0]
            c["NH ok" if r0.get_tag("NH") == nh else "NH wrong"] += 1
            mq = 255 if nh == 1 else 3 if nh == 2 else 1 if nh <= 4 else 0
            c["MAPQ ok" if all(r.mapping_quality == mq for r in mates) else "MAPQ wrong"] += 1
            nm = sum(S.mismatches(g, r) for r in mates)
            if all(r.get_tag("nM") == nm for r in mates):
                c["nM ok"] += 1
            else:
                c["nM wrong"] += 1
            e = expected_as(mates)
            if all(r.get_tag("AS") == e for r in mates):
                c["AS ok"] += 1
            else:
                c["AS wrong"] += 1
                if len(ex) < 5:
                    ex.append((name, hi, [r.cigarstring for r in mates], r0.get_tag("AS"), e))
            for r in mates:
                js = S.junctions_of(r)
                jm = list(r.get_tag("jM")); ji = list(r.get_tag("jI"))
                if not js:
                    c["jM/jI ok" if jm == [-1] and ji == [-1] else "jM/jI wrong"] += 1
                else:
                    ejm = [S.motif_code(g, r.reference_name, s, e) + (20 if (r.reference_name, s, e) in annot else 0) for s, e, l, rt in js]
                    eji = [x for s, e, l, rt in js for x in (s, e)]
                    c["jM/jI ok" if jm == ejm and ji == eji else "jM/jI wrong"] += 1
                if xs:
                    mot = {S.motif_code(g, r.reference_name, s, e) for s, e, l, rt in js}
                    exs = None
                    if js:
                        strands = set()
                        for s, e, l, rt in js:
                            key = (r.reference_name, s, e)
                            m = S.motif_code(g, *key)
                            if key in annot and {st for st in annot[key] if st != "."}:
                                strands |= {st for st in annot[key] if st != "."}
                            else:                           # unannotated, or annotated with strand '.': motif strand
                                strands.add(("+" if m % 2 == 1 else "-") if m else None)
                        strands.discard(None)               # a junction without strand does not veto the others
                        if strands == {"+"}:
                            exs = "+"
                        elif strands == {"-"}:
                            exs = "-"
                    got = r.get_tag("XS") if r.has_tag("XS") else None
                    if got == exs:
                        c["XS ok"] += 1
                    else:
                        c["XS wrong"] += 1
                        if len(ex) < 8:
                            ex.append((name, hi, r.cigarstring, "XS", got, exs, sorted(mot)))
            if paired and len(mates) == 2:
                m1, m2 = mates
                c["pair flags ok" if (m1.is_read1 != m2.is_read1 and m1.is_reverse != m2.is_reverse and m1.is_proper_pair and m2.is_proper_pair
                                      and m1.next_reference_start == m2.reference_start and m2.next_reference_start == m1.reference_start) else "pair flags wrong"] += 1
        # accuracy of the primary alignment for simulated transcript reads
        t = rs.truth.get(name)
        if t and t["kind"] in ("tx", "pe") and nh > 1:
            loci = {(r.reference_name, r.reference_start // 2000) for m in al.values() for r in m}
            if len(loci) == 1:
                c["reads with NH>1 whose alignments are at one locus (spliced vs clipped variants)"] += 1
        if t and t["kind"] in ("tx", "pe") and nh == 1:
            mates = al[prim[0]] if len(prim) == 1 else []
            blocks = []
            for r in mates:
                blocks += S.blocks_of(r)
            truth = t.get("blocks") or t.get("fragment")
            if paired:
                # fragment truth: the union of mate blocks must lie in the fragment blocks and cover its ends
                inside = all(any(a >= fa and b <= fb for fa, fb in truth) for a, b in blocks)
                ends = min(a for a, b in blocks) == truth[0][0] and max(b for a, b in blocks) == truth[-1][1]
                c["primary alignment at the simulated locus" if inside and ends else "primary alignment differs from simulation"] += 1
            else:
                if blocks == truth:
                    c["primary alignment at the simulated locus"] += 1
                else:
                    minb = min(b - a + 1 for a, b in truth)
                    c["primary alignment differs from simulation: simulated overhang < 8 bases" if minb < 8 else
                      "primary alignment differs from simulation: overhang >= 8 (%s)" % ("non-canonical unannotated junction" if t["tid"] == "T16" else "other")] += 1
    print("\n== %s ==" % label)
    for k in sorted(c):
        print("  %-44s %d" % (k, c[k]))
    for e in ex:
        print("  example:", e)
    return c["AS wrong"] + c["nM wrong"] + c["NH wrong"] + c["MAPQ wrong"] + c["jM/jI wrong"] + c["primary wrong"] + c["XS wrong"] + c["pair flags wrong"]


tot = 0
o = S.run_star(star, gidx, os.path.join(W, "tag_se"), [os.path.join(W, "se.fq")], quant=())
tot += check(o, "single-end, defaults")
o = S.run_star(star, gidx, os.path.join(W, "tag_pe"), [os.path.join(W, "pe_1.fq"), os.path.join(W, "pe_2.fq")], quant=())
tot += check(o, "paired-end, defaults", paired=True)
o = S.run_star(star, gidx, os.path.join(W, "tag_indel"), [os.path.join(W, "indel.fq")], quant=())
tot += check(o, "single-end reads with 1-5 bp deletions / 1-3 bp insertions")
cig = collections.Counter(r.cigarstring for recs in S.read_sam(os.path.join(o, "Aligned.out.sam")).values() for r in recs if not r.is_unmapped)
print("  indel-read CIGARs:", dict(cig.most_common(12)))
o = S.run_star(star, gidx, os.path.join(W, "tag_se_xs"), [os.path.join(W, "se.fq")], quant=(), attrs=("NH", "HI", "AS", "nM", "jM", "jI", "XS"), extra=["--outSAMstrandField", "intronMotif"])
tot += check(o, "single-end, --outSAMstrandField intronMotif", xs=True)
# G16 (unannotated non-canonical junction) reads: spliced in the default run, suppressed with intronMotif
def spliced_g16(outdir):
    n = 0
    for name, recs in S.read_sam(os.path.join(outdir, "Aligned.out.sam")).items():
        if name.endswith("_T16") and any((not r.is_unmapped) and "N" in r.cigarstring for r in recs):
            n += 1
    return n
print("  G16 reads with a spliced alignment: default run %d, intronMotif run %d (the manual: undefined-strand alignments are suppressed)" % (
    spliced_g16(os.path.join(W, "tag_se")), spliced_g16(os.path.join(W, "tag_se_xs"))))
# primary choice among equal-score multimappers (G13 on chrA vs G13copy on chrB): which locus is primary, and is it deterministic
def primary_locus(outdir):
    cnt = collections.Counter()
    for name, recs in S.read_sam(os.path.join(outdir, "Aligned.out.sam")).items():
        if name.endswith("_T13"):
            for r in recs:
                if not r.is_unmapped and not r.is_secondary:
                    cnt[(r.reference_name, r.get_tag("HI"))] += 1
    return dict(cnt)
o2 = S.run_star(star, gidx, os.path.join(W, "tag_se2"), [os.path.join(W, "se.fq")], quant=())
print("  primary locus of the 300 G13/G13copy multimappers (chrom, HI): run 1 %s; run 2 %s" % (primary_locus(os.path.join(W, "tag_se")), primary_locus(o2)))
o3 = S.run_star(star, gidx, os.path.join(W, "tag_se_rand"), [os.path.join(W, "se.fq")], quant=(), extra=["--outMultimapperOrder", "Random"])
print("  with --outMultimapperOrder Random --runRNGseed 777: %s" % primary_locus(o3))
o4 = S.run_star(star, gidx, os.path.join(W, "tag_se_mult1"), [os.path.join(W, "se.fq")], quant=(), extra=["--outSAMmultNmax", "1"])
n1 = collections.Counter()
for name, recs in S.read_sam(os.path.join(o4, "Aligned.out.sam")).items():
    if name.endswith("_T13"):
        m = [r for r in recs if not r.is_unmapped]
        n1[(len(m), m[0].get_tag("NH") if m else None, m[0].is_secondary if m else None)] += 1
print("  with --outSAMmultNmax 1, G13 reads: (records, NH, secondary) -> count %s" % dict(n1))
print("\nTOTAL tag/flag mismatches: %d" % tot)
