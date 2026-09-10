#!/usr/bin/env python3
"""Held-up check and note: --quantMode TranscriptomeSAM (Aligned.toTranscriptome.out.bam)
against an independent projection of STAR's genome alignments onto the annotated
transcripts, plus a truth-based count of the reads the default soft-clip extension
removes from the transcriptome BAM.

Usage: python heldup_transcriptome.py /path/to/STAR [workdir]

Port of the documented default --quantTranscriptomeSAMoutput
BanSingleEnd_BanIndels_ExtendSoftclip: alignments with an insertion or deletion are
skipped; single-mate alignments of pairs are skipped; soft clips are extended to the
read ends along the genome and the extra mismatches added to nM; if the total exceeds
min(10, 0.3 x (read length - 1)) the alignment is skipped; every transcript that
contains every (extended) block inside one exon, with each N gap equal to one of the
transcript's introns, receives one record per mate at the transcript coordinate of the
block (reverse-complemented coordinates and strand on '-' transcripts). Records are
compared as (read, mate, transcript, 1-based position, strand, CIGAR).
"""
import sys, os, tempfile, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

star = sys.argv[1]
work = sys.argv[2] if len(sys.argv) > 2 else tempfile.mkdtemp(prefix="star_audit_")
S = Synth(os.path.join(work, "data"))
ver = star_version(star)
print("STAR", ver, "| workdir", work)
gdir = run_star_genome(star, os.path.join(work, "genome_gtf"), S.fa, S.gtf)
COMMON = ["--quantMode", "TranscriptomeSAM", "GeneCounts", "--outSAMtype", "BAM", "Unsorted", "SortedByCoordinate",
          "--outSAMattributes", "All", "--outSAMunmapped", "Within"]
def _vt(v):
    import re
    return tuple(int(x) for x in re.findall(r"\d+", v)[:3])
old = _vt(ver) < (2, 7, 11)      # 2.7.10x and older spell the option --quantTranscriptomeBan
SOFTCLIP_OK = ["--quantTranscriptomeBan", "Singleend"] if old else ["--quantTranscriptomeSAMoutput", "BanSingleEnd"]
runs = collections.OrderedDict([
    ("SE", run_star_map(star, gdir, os.path.join(work, "map_se/"), [S.fq_se], COMMON)),
    ("PE", run_star_map(star, gdir, os.path.join(work, "map_pe/"), [S.fq_1, S.fq_2], COMMON)),
])
ctrl = collections.OrderedDict([
    ("SE softclip-allowed", run_star_map(star, gdir, os.path.join(work, "map_se_trsoft/"), [S.fq_se], COMMON + SOFTCLIP_OK)),
    ("PE softclip-allowed", run_star_map(star, gdir, os.path.join(work, "map_pe_trsoft/"), [S.fq_1, S.fq_2], COMMON + SOFTCLIP_OK)),
])

# transcripts by chromosome: (tid, strand, exons[(s0,e0excl)], cum[], length)
TR = collections.defaultdict(list)
for tid, (gid, chrom, strand, exs) in S.transcripts.items():
    ex0 = [(s - 1, e) for s, e in exs]; cum = []; c = 0
    for s, e in ex0: cum.append(c); c += e - s
    TR[chrom].append((tid, strand, ex0, cum, c))

def extended_blocks(rec):
    """Blocks after soft-clip extension: [(ref_s, ref_e)], plus extra mismatches in the extension."""
    bl = blocks_of(rec); ct = rec.cigartuples; g = S.genome[rec.reference_name]; q = rec.query_sequence
    extra = 0; bl = [[s, e] for s, e, qs in bl]
    if ct[0][0] == 4:
        L = ct[0][1]; s0 = bl[0][0]
        for i in range(1, L + 1):
            r = q[L - i]; b = g[s0 - i]
            if r != b and r != "N" and b != "N": extra += 1
        bl[0][0] -= L
    if ct[-1][0] == 4:
        L = ct[-1][1]; e0 = bl[-1][1]; qe = len(q) - L
        for i in range(L):
            r = q[qe + i]; b = g[e0 + i]
            if r != b and r != "N" and b != "N": extra += 1
        bl[-1][1] += L
    return [tuple(b) for b in bl], extra

def project(rec_blocks, chrom):
    """Transcripts compatible with these genomic blocks -> {tid: (tstart0_plus, tend0_plus_excl)}"""
    out = {}
    for tid, strand, ex0, cum, tlen in TR[chrom]:
        ok = True; k = None; tpos = []
        for i, (bs, be) in enumerate(rec_blocks):
            # exon containing the block start
            kk = next((j for j, (s, e) in enumerate(ex0) if s <= bs < e), None)
            if kk is None or be > ex0[kk][1]: ok = False; break
            if i > 0:
                # gap between blocks must be exactly the intron between exon k and exon kk=k+1
                if kk != k + 1 or rec_blocks[i - 1][1] != ex0[k][1] or bs != ex0[kk][0]: ok = False; break
            k = kk
            tpos.append((cum[kk] + bs - ex0[kk][0], cum[kk] + be - ex0[kk][0]))
        if ok: out[tid] = (tpos[0][0], tpos[-1][1], strand, tlen)
    return out

def port(genome_bam):
    exp = set(); reasons = collections.Counter(); reads_with = set(); reads_seen = set()
    for qname, recs in bam_by_read(genome_bam).items():
        mapped = [r for r in recs if not r.is_unmapped]
        if not mapped: continue
        reads_seen.add(qname)
        by_hi = collections.defaultdict(list)
        for r in mapped: by_hi[r.get_tag("HI")].append(r)
        for hi, rs in by_hi.items():
            if any(op in (1, 2) for r in rs for op, ln in r.cigartuples): reasons["indel"] += 1; continue
            if rs[0].is_paired and len(rs) == 1: reasons["single mate"] += 1; continue
            ext = []; extra = 0
            for r in rs:
                b, x = extended_blocks(r); ext.append(b); extra += x
            Lread = sum(r.infer_read_length() for r in rs) + (1 if len(rs) == 2 else 0)
            if rs[0].get_tag("nM") + extra > min(10, int(0.3 * (Lread - 1))): reasons["too many mismatches after extension"] += 1; continue
            chrom = rs[0].reference_name
            projs = [project(b, chrom) for b in ext]
            common = set(projs[0]); [common.intersection_update(p) for p in projs[1:]]
            if not common:
                clipped = any(r.cigartuples[0][0] == 4 or r.cigartuples[-1][0] == 4 for r in rs)
                unclipped_ok = bool(set.intersection(*[set(project(blocks := [(s, e) for s, e, q in blocks_of(r)], chrom)) for r in rs]))
                reasons["no compatible transcript" + (" (soft-clipped; compatible before extension)" if clipped and unclipped_ok else (" (soft-clipped)" if clipped else ""))] += 1
                continue
            reads_with.add(qname)
            for tid in common:
                for r, pj in zip(rs, projs):
                    ts, te, strand, tlen = pj[tid]
                    if strand == "-": ts, te = tlen - te, tlen - ts
                    rev = r.is_reverse != (strand == "-")
                    mate = 1 if r.is_read1 else (2 if r.is_read2 else 0)
                    exp.add((qname, mate, tid, ts + 1, rev, "%dM" % (te - ts)))
    return exp, reasons, reads_with, reads_seen

def star_records(tr_bam):
    got = set(); reads = set()
    with pysam.AlignmentFile(tr_bam, "rb") as bf:
        for r in bf:
            if r.is_unmapped: continue
            mate = 1 if r.is_read1 else (2 if r.is_read2 else 0)
            got.add((r.query_name, mate, r.reference_name, r.reference_start + 1, r.is_reverse, r.cigarstring)); reads.add(r.query_name)
    return got, reads

allok = True
for name, prefix in runs.items():
    exp, reasons, reads_with, reads_seen = port(prefix + "Aligned.out.bam")
    got, reads_got = star_records(prefix + "Aligned.toTranscriptome.out.bam")
    print("\n== %s: transcriptome records STAR %d / port %d; reads with >=1 record STAR %d / port %d (genome-mapped reads %d)" % (
        name, len(got), len(exp), len(reads_got), len(reads_with), len(reads_seen)))
    only_s = got - exp; only_p = exp - got
    if only_s or only_p:
        print("  only in STAR: %d" % len(only_s)); [print("    ", r) for r in sorted(only_s)[:8]]
        print("  only in port: %d" % len(only_p)); [print("    ", r) for r in sorted(only_p)[:8]]
        # ST1: are the differences exactly the strand flags of records on the strand-less transcript T14?
        flip = {(q, m, t, p, not rev, c) for q, m, t, p, rev, c in only_s}
        st1_only = all(r[2] == "T14" for r in only_s | only_p) and flip == only_p
        print("  differences confined to the strand flag of records on the strand-less transcript T14 (finding ST1): %s" % st1_only)
        allok &= st1_only
    else:
        print("  identical record sets")
    print("  genome alignments without a transcriptome record, by port reason:")
    for k, v in sorted(reasons.items(), key=lambda x: -x[1]): print("     %-70s %d" % (k, v))
    # multi-transcript reads: NH and one primary
    nh_bad = 0; prim_bad = 0; n_multi = 0
    per = collections.defaultdict(list)
    with pysam.AlignmentFile(prefix + "Aligned.toTranscriptome.out.bam", "rb") as bf:
        for r in bf:
            if not r.is_unmapped: per[r.query_name].append(r)
    for q, rs in per.items():
        nrec = len({(r.reference_name, r.get_tag("HI")) for r in rs})
        if nrec > 1: n_multi += 1
        if any(r.get_tag("NH") != nrec for r in rs): nh_bad += 1
        prim = {(r.reference_name, r.get_tag("HI")) for r in rs if not r.is_secondary}
        if len(prim) != 1: prim_bad += 1
    print("  reads on >1 transcript %d; NH != number of transcript alignments: %d; reads without exactly one primary: %d" % (n_multi, nh_bad, prim_bad))
    allok &= (nh_bad == 0 and prim_bad == 0)

# note: the soft-clip extension and reads whose true junction overhang is short
print("\n== note: simulated single-end reads by true junction overhang (min distance from a read end to an exon boundary inside the read)")
def true_overhang(t):
    gid, chrom, strand, exs = S.transcripts[t["tid"]]
    L = 100; p = t["tpos"]; bounds = []; c = 0
    for s, e in exs:
        c += e - s + 1; bounds.append(c)
    inside = [b for b in bounds[:-1] if p < b < p + L]
    if not inside: return None
    return min(min(b - p, p + L - b) for b in inside)
for label, pfx in [("default (ExtendSoftclip)", runs["SE"]), ("soft clips allowed", ctrl["SE softclip-allowed"])]:
    got, reads_got = star_records(pfx + "Aligned.toTranscriptome.out.bam")
    gen = bam_by_read(pfx + "Aligned.out.bam")
    tab = collections.defaultdict(lambda: [0, 0, 0])   # overhang -> [reads, genome-unique-mapped, in transcriptome BAM]
    for q, t in S.truth.items():
        if t["lib"] != "se" or t["kind"] != "tr": continue
        oh = true_overhang(t)
        key = oh if oh is None or oh > 12 else oh
        key = "none" if oh is None else (">12" if oh > 12 else str(oh))
        tab[key][0] += 1
        mapped = [r for r in gen.get(q, []) if not r.is_unmapped]
        if mapped and mapped[0].get_tag("NH") == 1: tab[key][1] += 1
        if q in reads_got: tab[key][2] += 1
    print("  %s:" % label)
    print("     %-10s %8s %14s %16s" % ("overhang", "reads", "genome-unique", "in trscript BAM"))
    for k in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", ">12", "none"]:
        if k in tab: print("     %-10s %8d %14d %16d" % (k, *tab[k]))
    short = [tab[k] for k in ("1", "2") if k in tab]
    print("     overhang 1-2 nt: %d reads, %d in the transcriptome BAM" % (sum(x[0] for x in short), sum(x[2] for x in short)))
# how the control run differs
for name, pfx in ctrl.items():
    got, reads_got = star_records(pfx + "Aligned.toTranscriptome.out.bam")
    base = runs[name.split()[0]]
    got0, reads0 = star_records(base + "Aligned.toTranscriptome.out.bam")
    print("  %s: %d reads in the transcriptome BAM (default run: %d); %d reads present only with soft clips allowed" % (name, len(reads_got), len(reads0), len(reads_got - reads0)))

print("\nRESULT:", "transcriptome records equal the port apart from ST1 (strand-less transcript), if present" if allok else "DIFFERENCES FOUND beyond ST1")
