"""--quantMode TranscriptomeSAM (Aligned.toTranscriptome.out.bam) against an independent projection.

Truth: every alignment in STAR's genomic Aligned.out.sam (all HI values) is projected
onto every GTF transcript it is compatible with, following the manual's description of
the default --quantTranscriptomeSAMoutput BanSingleEnd_BanIndels_ExtendSoftclip:
alignments with indels are dropped, paired-end alignments with one mate are dropped,
soft-clipped ends are extended (their mismatches against the genome counted, and the
alignment dropped when total mismatches exceed min(--outFilterMismatchNmax, floor(0.3
* (Lread - 1))) as in ReadAlign_quantTranscriptome.cpp). Compatibility: each mate's
first block starts inside an exon, each block ends inside its exon, and each N gap
equals a transcript intron exactly. Transcript coordinates are cumulative exon lengths;
for a '-' transcript the position is mirrored (trLen - end), the strand flag is flipped
and the sequence reverse-complemented; a '.' transcript is projected like '+'.

Expected per BAM record: (transcript, POS, reverse flag, read1/read2, SEQ, CIGAR).
NH must equal the number of projected records of the read and exactly one record of each
read must be primary.

Usage: python heldup_transcriptome_sam.py <STAR binary> <work dir>
"""
import os, sys, collections, bisect
import pysam
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _synth as S

star, W = sys.argv[1], sys.argv[2]
g, trs, rs = S.standard_dataset(W)
gidx = S.genome_generate(star, W, os.path.join(W, "gidx"))

gtf_trs = {tid: tr for tid, tr in trs.items() if tr["in_gtf"]}
for tr in gtf_trs.values():
    cum, c = [], 0
    for a, b in tr["exons"]:
        cum.append(c); c += b - a + 1
    tr["cum"] = cum; tr["len"] = c


def extend_softclips(rec):
    """Blocks with soft clips extended, and the extension mismatches (vs genome)."""
    blocks = S.blocks_of(rec)
    ct = rec.cigartuples
    q = rec.query_sequence
    s = g[rec.reference_name]
    nmm = 0
    if ct[0][0] == 4:
        n = ct[0][1]
        st = blocks[0][0] - n
        for i in range(n):
            a, b = q[i], s[st - 1 + i]
            if a != b and a != "N" and b != "N":
                nmm += 1
        blocks[0] = (st, blocks[0][1])
    if ct[-1][0] == 4:
        n = ct[-1][1]
        en = blocks[-1][1]
        for i in range(n):
            a, b = q[len(q) - n + i], s[en + i]
            if a != b and a != "N" and b != "N":
                nmm += 1
        blocks[-1] = (blocks[-1][0], en + n)
    return blocks, nmm


def project_mate(tr, blocks):
    """Transcript-space (start0, end0) of a mate's blocks on transcript tr, or None if incompatible."""
    ex = tr["exons"]
    k = None
    for j, (a, b) in enumerate(ex):
        if a <= blocks[0][0] <= b:
            k = j; break
    if k is None:
        return None
    for i, (bs, be) in enumerate(blocks):
        a, b = ex[k]
        if i > 0:
            if bs != a:                                     # after a junction the block must start at the exon start
                return None
        if be > b:
            return None
        if i + 1 < len(blocks):
            if be != b or k + 1 >= len(ex):                 # junction must end at the exon end
                return None
            k += 1
    start0 = tr["cum"][k - (len(blocks) - 1)] + (blocks[0][0] - ex[k - (len(blocks) - 1)][0])
    end0 = tr["cum"][k] + (blocks[-1][1] - ex[k][0])
    return start0, end0


def expected_records(recs, paired):
    """Set of expected transcriptome records for one genomic alignment (list of mate records)."""
    out = set()
    if any(op in (1, 2) for r in recs for op, ln in r.cigartuples):
        return out                                          # BanIndels
    if paired and len(recs) != 2:
        return out                                          # BanSingleEnd
    Lread = sum(len(r.query_sequence) for r in recs) + (1 if paired else 0)
    mates = []
    nmm = 0
    for r in recs:
        blocks, x = extend_softclips(r)
        nmm += x + r.get_tag("nM") if r is recs[0] else x
        mates.append((r, blocks))
    if nmm > min(10, int(0.3 * (Lread - 1))):
        return out
    chrom = recs[0].reference_name
    a_start = min(b[0][0] for r, b in mates); a_end = max(b[-1][1] for r, b in mates)
    for tid, tr in gtf_trs.items():
        if tr["chrom"] != chrom or a_start < tr["exons"][0][0] or a_end > tr["exons"][-1][1]:
            continue
        proj = [project_mate(tr, b) for r, b in mates]
        if any(p is None for p in proj):
            continue
        for (r, blocks), (s0, e0) in zip(mates, proj):
            L = e0 - s0 + 1
            seq = r.query_sequence
            if tr["strand"] == "-":
                pos = tr["len"] - e0                      # 1-based mirrored start
                rev = not r.is_reverse; seq = S.rc(seq)
            else:
                pos = s0 + 1; rev = r.is_reverse
            out.add((tid, pos, rev, r.is_read1 if paired else True, seq, "%dM" % L))
    return out


def check(outdir, paired, label):
    reads = S.read_sam(os.path.join(outdir, "Aligned.out.sam"))
    exp = {}
    for name, recs in reads.items():
        e = set()
        for hi, al in S.alignments(recs).items():
            e |= expected_records(al, paired)
        if e:
            exp[name] = e
    got = collections.defaultdict(set)
    nh_ok = nh_bad = prim_bad = 0
    prim = collections.Counter(); nrec = collections.Counter()
    with pysam.AlignmentFile(os.path.join(outdir, "Aligned.toTranscriptome.out.bam"), "rb") as fh:
        for r in fh:
            if r.is_unmapped:
                continue                                    # --outSAMunmapped Within also writes unmapped reads here
            got[r.query_name].add((r.reference_name, r.reference_start + 1, r.is_reverse, r.is_read1 if paired else True, r.query_sequence, r.cigarstring))
            nrec[r.query_name] += 1
            if not r.is_secondary:
                prim[r.query_name] += 1
            if r.get_tag("NH") * (2 if paired else 1) != 0:
                pass
    # NH check: NH = number of transcript alignments = records / mates
    with pysam.AlignmentFile(os.path.join(outdir, "Aligned.toTranscriptome.out.bam"), "rb") as fh:
        for r in fh:
            if r.is_unmapped:
                continue
            if r.get_tag("NH") == nrec[r.query_name] // (2 if paired else 1):
                nh_ok += 1
            else:
                nh_bad += 1
    for name, n in prim.items():
        if n != (2 if paired else 1):
            prim_bad += 1
    names = sorted(set(exp) | set(got))
    ok = bad = 0
    by_tid = collections.Counter(); by_tid_bad = collections.Counter()
    examples = []
    for name in names:
        e, gt = exp.get(name, set()), got.get(name, set())
        tids = {x[0] for x in e | gt}
        for t in tids:
            by_tid[t] += 1
        if e == gt:
            ok += 1
        else:
            bad += 1
            for t in tids:
                by_tid_bad[t] += 1
            if len(examples) < 4:
                examples.append((name, sorted(e - gt), sorted(gt - e)))
    print("\n== %s ==" % label)
    print("reads with transcriptome records (expected or got): %d; reads matching the projection exactly: %d; differing: %d" % (len(names), ok, bad))
    print("records with NH equal to the record count: %d; NH wrong: %d; reads whose primary count is not 1: %d" % (nh_ok, nh_bad, prim_bad))
    print("per transcript (reads touching it: differing / total):")
    for t in sorted(by_tid):
        print("  %-8s strand %s  %4d / %4d" % (t, gtf_trs[t]["strand"], by_tid_bad[t], by_tid[t]))
    for name, miss, extra in examples:
        print("  example %s:\n    expected-not-got %s\n    got-not-expected %s" % (name, [x[:4] + (x[4][:12] + "...", x[5]) for x in miss], [x[:4] + (x[4][:12] + "...", x[5]) for x in extra]))
    return bad


tot = 0
o = S.run_star(star, gidx, os.path.join(W, "tr_se"), [os.path.join(W, "se.fq")])
tot += check(o, False, "single-end, defaults")
o = S.run_star(star, gidx, os.path.join(W, "tr_pe"), [os.path.join(W, "pe_1.fq"), os.path.join(W, "pe_2.fq")])
tot += check(o, True, "paired-end, defaults")
print("\nTOTAL reads differing from the projection: %d" % tot)
