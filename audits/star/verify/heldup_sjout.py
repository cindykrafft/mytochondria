#!/usr/bin/env python3
"""Held-up check: SJ.out.tab against an independent port built from STAR's own BAM.

Usage: python heldup_sjout.py /path/to/STAR [workdir]

Port: for every read, every N operation of every alignment record (primary and
secondary) gives a junction (intron start/end, 1-based); the overhang of one read is
min(M-run left of the N, M-run right of the N) (M runs are delimited by I/D/N/S); the same
junction seen twice from one read (overlapping mates, several alignments) is one read
with the larger overhang; a read counts as unique if NH==1, multi otherwise. Junctions
are collapsed (sum counts, max overhang), the motif is read from the genome (GT/AG=1,
CT/AC=2, GC/AG=3, CT/GC=4, AT/AC=5, GT/AT=6, else 0), strand 0/1/2 from the motif,
annotated=1 if the junction is in the GTF (or, in 2-pass mode, in the 1st-pass
SJ.out.tab). Then the documented defaults of --outSJfilterOverhangMin 30 12 12 12,
--outSJfilterCountUniqueMin 3 1 1 1, --outSJfilterCountTotalMin 3 1 1 1,
--outSJfilterDistToOtherSJmin 10 0 5 10 and --outSJfilterIntronMaxVsReadN 50000 100000
200000 are applied (annotated junctions bypass all of them); with --outFilterType
BySJout the distance filter is skipped at the second stage as the code does.
"""
import sys, os, tempfile, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

star = sys.argv[1]
work = sys.argv[2] if len(sys.argv) > 2 else tempfile.mkdtemp(prefix="star_audit_")
S = Synth(os.path.join(work, "data"))
print("STAR", star_version(star), "| workdir", work)
g_gtf = run_star_genome(star, os.path.join(work, "genome_gtf"), S.fa, S.gtf)
g_nogtf = run_star_genome(star, os.path.join(work, "genome_nogtf"), S.fa, None)

COMMON = ["--outSAMtype", "BAM", "Unsorted", "--outSAMattributes", "All", "--outSAMunmapped", "Within"]
runs = collections.OrderedDict([
    ("SE gtf",              (g_gtf,   run_star_map(star, g_gtf,   os.path.join(work, "sj_se_gtf/"),    [S.fq_se], COMMON), True)),
    ("PE gtf",              (g_gtf,   run_star_map(star, g_gtf,   os.path.join(work, "sj_pe_gtf/"),    [S.fq_1, S.fq_2], COMMON), True)),
    ("SE no-gtf 1-pass",    (g_nogtf, run_star_map(star, g_nogtf, os.path.join(work, "sj_se_nogtf/"),  [S.fq_se], COMMON), False)),
    ("PE no-gtf 1-pass",    (g_nogtf, run_star_map(star, g_nogtf, os.path.join(work, "sj_pe_nogtf/"),  [S.fq_1, S.fq_2], COMMON), False)),
    ("SE no-gtf 2-pass",    (g_nogtf, run_star_map(star, g_nogtf, os.path.join(work, "sj_se_nogtf_2p/"), [S.fq_se], COMMON + ["--twopassMode", "Basic"]), False)),
    ("SE gtf 2-pass",       (g_gtf,   run_star_map(star, g_gtf,   os.path.join(work, "sj_se_gtf_2p/"),  [S.fq_se], COMMON + ["--twopassMode", "Basic"]), True)),
    ("SE no-gtf BySJout",   (g_nogtf, run_star_map(star, g_nogtf, os.path.join(work, "sj_se_nogtf_bysj/"), [S.fq_se], COMMON + ["--outFilterType", "BySJout"]), False)),
    ("SE gtf uniqueReads",  (g_gtf,   run_star_map(star, g_gtf,   os.path.join(work, "sj_se_gtf_uniq/"), [S.fq_se], COMMON + ["--outSJfilterReads", "Unique"]), True)),
])

OVERHANG_MIN = [30, 12, 12, 12]; CU_MIN = [3, 1, 1, 1]; CT_MIN = [3, 1, 1, 1]; DIST_MIN = [10, 0, 5, 10]; INTRON_MAX = [50000, 100000, 200000]
MOT = {("GT", "AG"): 1, ("CT", "AC"): 2, ("GC", "AG"): 3, ("CT", "GC"): 4, ("AT", "AC"): 5, ("GT", "AT"): 6}

def motif_of(chrom, s, e):
    g = S.genome[chrom]
    return MOT.get((g[s - 1:s + 1], g[e - 2:e]), 0)

def junctions_of_record(rec):
    """[(intron_start1, intron_end1, overhang)] from one record."""
    out = []; rpos = rec.reference_start; runs = []   # runs: (kind, ref_start, ref_end, length)
    for op, ln in rec.cigartuples:
        if op in (0, 7, 8): runs.append(("M", rpos, rpos + ln, ln)); rpos += ln
        elif op == 3: runs.append(("N", rpos, rpos + ln, ln)); rpos += ln
        elif op == 2: runs.append(("D", rpos, rpos + ln, ln)); rpos += ln
        elif op == 1: runs.append(("I", rpos, rpos, ln))
        elif op == 4: runs.append(("S", rpos, rpos, ln))
    for i, (k, a, b, ln) in enumerate(runs):
        if k == "N":
            left = runs[i - 1][3]; right = runs[i + 1][3]      # STAR blocks: the M runs next to the gap
            out.append((a + 1, b, min(left, right)))
    return out

def port(bam, annotated, stage2_dist_skip=False, unique_only=False):
    per_j = collections.defaultdict(lambda: [0, 0, 0])   # (chrom,s,e) -> [unique, multi, maxoverhang]
    for qname, recs in bam_by_read(bam).items():
        mapped = [r for r in recs if not r.is_unmapped]
        if not mapped: continue
        nh = mapped[0].get_tag("NH")
        if unique_only and nh > 1: continue
        seen = {}
        for r in mapped:
            for s, e, oh in junctions_of_record(r):
                key = (r.reference_name, s, e)
                seen[key] = max(seen.get(key, 0), oh)
        for key, oh in seen.items():
            per_j[key][0 if nh == 1 else 1] += 1
            per_j[key][2] = max(per_j[key][2], oh)
    rows = []
    for (chrom, s, e), (cu, cm, oh) in per_j.items():
        m = motif_of(chrom, s, e); ann = 1 if (chrom, s, e) in annotated else 0
        strand = 0 if m == 0 else (1 if m % 2 == 1 else 2)
        rows.append([chrom, s, e, strand, m, ann, cu, cm, oh])
    # count / overhang / intron-length filter
    def keep1(r):
        chrom, s, e, strand, m, ann, cu, cm, oh = r
        if ann: return True
        k = (m + 1) // 2; n = cu + cm; gap = e - s + 1
        return ((cu >= CU_MIN[k] or n >= CT_MIN[k]) and oh >= OVERHANG_MIN[k] and (n > len(INTRON_MAX) or gap <= INTRON_MAX[n - 1]))
    rows = [r for r in rows if keep1(r)]
    if stage2_dist_skip:
        return sorted(rows, key=lambda r: (S_chrom_order(r[0]), r[1], r[2]))
    # distance-to-other-junction filter (donor = intron start, acceptor = intron end), per chromosome in genome order
    gpos = lambda r: (S_chrom_order(r[0]), r[1])
    rows.sort(key=lambda r: (S_chrom_order(r[0]), r[1], r[2] - r[1]))
    def coord(r): return CHR_OFFSET[r[0]] + r[1] - 1
    keep = [True] * len(rows)
    for i, r in enumerate(rows):
        if r[5]: continue
        k = (r[4] + 1) // 2
        d = min(coord(r) - (coord(rows[i - 1]) if i > 0 else -10**9), (coord(rows[i + 1]) if i + 1 < len(rows) else 10**12) - coord(r))
        if d < DIST_MIN[k]: keep[i] = False
    acc = sorted(range(len(rows)), key=lambda i: CHR_OFFSET[rows[i][0]] + rows[i][2])
    for j, i in enumerate(acc):
        r = rows[i]
        if r[5]: continue
        k = (r[4] + 1) // 2
        a = CHR_OFFSET[r[0]] + r[2]
        d = min(a - (CHR_OFFSET[rows[acc[j - 1]][0]] + rows[acc[j - 1]][2] if j > 0 else -10**9),
                (CHR_OFFSET[rows[acc[j + 1]][0]] + rows[acc[j + 1]][2] if j + 1 < len(acc) else 10**12) - a)
        if d < DIST_MIN[k]: keep[i] = False
    return [r for i, r in enumerate(rows) if keep[i]]

CHR_ORDER = list(CHR_LEN)
def S_chrom_order(c): return CHR_ORDER.index(c)
CHR_OFFSET = {}; off = 0
for c in CHR_ORDER: CHR_OFFSET[c] = off; off += CHR_LEN[c] + 1000000   # separate chromosomes generously

allok = True
for name, (gdir, prefix, has_gtf) in runs.items():
    annotated = set(S.annot_sj) if has_gtf else set()
    if "2-pass" in name:
        for r in read_sj(prefix + "_STARpass1/SJ.out.tab"):
            annotated.add((r[0], r[1], r[2]))
    star_rows = read_sj(prefix + "SJ.out.tab")
    port_rows = port(prefix + "Aligned.out.bam", annotated, stage2_dist_skip=("BySJout" in name), unique_only=("uniqueReads" in name))
    sset = set(tuple(r) for r in star_rows); pset = set(tuple(r) for r in port_rows)
    print("\n== %s: SJ.out.tab %d rows, port %d rows" % (name, len(star_rows), len(port_rows)))
    only_s = sorted(sset - pset); only_p = sorted(pset - sset)
    if only_s or only_p:
        allok = False
        print("  only in STAR: %d" % len(only_s)); [print("    ", r) for r in only_s[:12]]
        print("  only in port: %d" % len(only_p)); [print("    ", r) for r in only_p[:12]]
    else:
        print("  identical (all 9 columns of every row)")
    by_m = collections.Counter((r[4], r[5]) for r in star_rows)
    print("  rows by (motif, annotated):", dict(sorted(by_m.items())))
    print("  unique/multi read totals: %d / %d; max overhang %d" % (sum(r[6] for r in star_rows), sum(r[7] for r in star_rows), max(r[8] for r in star_rows)))
    if "2-pass" in name:
        p1 = read_sj(prefix + "_STARpass1/SJ.out.tab")
        novel_p1 = [r for r in p1 if r[5] == 0]
        print("  1st pass: %d junctions, %d unannotated; 2nd pass rows with annotated=1: %d of %d (pass-1 novel junctions are re-labelled annotated)" % (
            len(p1), len(novel_p1), sum(r[5] for r in star_rows), len(star_rows)))
    if "BySJout" in name:
        # the reads kept must only contain junctions in the SJ.out.tab set
        sjset = {(r[0], r[1], r[2]) for r in star_rows}
        bad = 0; nsp = 0
        for qname, recs in bam_by_read(prefix + "Aligned.out.bam").items():
            for r in recs:
                if r.is_unmapped: continue
                for s, e, oh in junctions_of_record(r):
                    nsp += 1
                    if (r.reference_name, s, e) not in sjset: bad += 1
        print("  BySJout: %d junction crossings in the BAM, %d not in SJ.out.tab" % (nsp, bad))

# how the filters act, on the no-GTF single-end run: which raw junctions were removed and why
print("\n== filter accounting on 'SE no-gtf 1-pass' (raw junctions from the BAM before the filters)")
prefix = runs["SE no-gtf 1-pass"][1]
raw = collections.defaultdict(lambda: [0, 0, 0])
for qname, recs in bam_by_read(prefix + "Aligned.out.bam").items():
    mapped = [r for r in recs if not r.is_unmapped]
    if not mapped: continue
    nh = mapped[0].get_tag("NH"); seen = {}
    for r in mapped:
        for s, e, oh in junctions_of_record(r):
            seen[(r.reference_name, s, e)] = max(seen.get((r.reference_name, s, e), 0), oh)
    for key, oh in seen.items():
        raw[key][0 if nh == 1 else 1] += 1; raw[key][2] = max(raw[key][2], oh)
kept = {(r[0], r[1], r[2]) for r in read_sj(prefix + "SJ.out.tab")}
why = collections.Counter()
for (chrom, s, e), (cu, cm, oh) in raw.items():
    m = motif_of(chrom, s, e); k = (m + 1) // 2
    if (chrom, s, e) in kept: why[("kept", "motif %d" % m)] += 1; continue
    reasons = []
    if not (cu >= CU_MIN[k] or cu + cm >= CT_MIN[k]): reasons.append("count<%d" % CU_MIN[k])
    if oh < OVERHANG_MIN[k]: reasons.append("overhang %d<%d" % (oh, OVERHANG_MIN[k]))
    if not reasons: reasons.append("distance-to-other-junction")
    why[("removed", "motif %d: " % m + ",".join(reasons))] += 1
for k, v in sorted(why.items()): print("   %-60s %d" % (" ".join(k), v))
truth_j = {(c, s, e) for c, s, e, *_ in S.junctions}
print("   true junctions %d, in SJ.out.tab %d, missing %s" % (len(truth_j), len(truth_j & kept), sorted(truth_j - kept)))

print("\nRESULT:", "SJ.out.tab equals the port on every run" if allok else "DIFFERENCES FOUND")
