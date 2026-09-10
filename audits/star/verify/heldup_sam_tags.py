#!/usr/bin/env python3
"""Held-up check: SAM/BAM record contents against independent recomputation from the
read, the genome and the documented scoring scheme.

Usage: python heldup_sam_tags.py /path/to/STAR [workdir]

Checked per record on the single-end and paired-end GTF runs (all alignments, primary
and secondary): NH = number of alignments of the read; HI = 1..NH; MAPQ 255/3/1/0 for
NH 1/2/3-4/>=5; nM = mismatches (non-N) over both mates; NM = mismatches incl. N +
inserted + deleted bases per mate; MD string per mate; AS = matches - mismatches
+ per-junction term (annotated: +2 sjdbScore; else 0 for GT/AG, -4 GC/AG, -8 AT/AC,
-8 non-canonical) + indels (-2 - 2 x length) + ceil(log2(genomic span) x -0.25 - 0.5),
floored at 0; jM/jI = motif (+20 if annotated) and 1-based intron coordinates; exactly
one primary record per read, and it has the maximal AS; flags 0x1/0x2/0x10/0x20/0x40/0x80,
mate fields and TLEN for pairs; XS under --outSAMstrandField intronMotif from the
junction strands (annotation strand for annotated junctions, motif strand otherwise);
and the coordinate-sorted BAM is a permutation of the unsorted one in non-decreasing
(reference, position) order with unmapped records last.
"""
import sys, os, tempfile, collections, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

star = sys.argv[1]
work = sys.argv[2] if len(sys.argv) > 2 else tempfile.mkdtemp(prefix="star_audit_")
S = Synth(os.path.join(work, "data"))
print("STAR", star_version(star), "| workdir", work)
gdir = run_star_genome(star, os.path.join(work, "genome_gtf"), S.fa, S.gtf)
COMMON = ["--quantMode", "TranscriptomeSAM", "GeneCounts", "--outSAMtype", "BAM", "Unsorted", "SortedByCoordinate",
          "--outSAMattributes", "All", "--outSAMunmapped", "Within"]
runs = collections.OrderedDict([
    ("SE", run_star_map(star, gdir, os.path.join(work, "map_se/"), [S.fq_se], COMMON)),
    ("PE", run_star_map(star, gdir, os.path.join(work, "map_pe/"), [S.fq_1, S.fq_2], COMMON)),
    ("SE intronMotif", run_star_map(star, gdir, os.path.join(work, "map_se_xs/"), [S.fq_se], COMMON + ["--outSAMstrandField", "intronMotif"])),
])
MOT = {("GT", "AG"): 1, ("CT", "AC"): 2, ("GC", "AG"): 3, ("CT", "GC"): 4, ("AT", "AC"): 5, ("GT", "AT"): 6}
JPEN = {0: -8, 1: 0, 2: 0, 3: -4, 4: -4, 5: -8, 6: -8}
annot_strand = {(c, s, e): strand for c, s, e, strand, *_ in S.junctions}

def walk(rec):
    """Per record: mismatches (non-N), mismatches incl N, MD string, ins bases, del bases, junction list, span."""
    g = S.genome[rec.reference_name]; q = rec.query_sequence
    rpos = rec.reference_start; qpos = 0; mm = 0; mmN = 0; md = []; run = 0; ins = 0; dele = 0; juncs = []
    for op, ln in rec.cigartuples:
        if op in (0, 7, 8):
            for i in range(ln):
                r = q[qpos + i]; b = g[rpos + i]
                if r != b or r == "N" or b == "N":
                    mmN += 1; md.append(str(run)); md.append(b); run = 0
                    if r != "N" and b != "N": mm += 1
                else: run += 1
            rpos += ln; qpos += ln
        elif op == 2:
            dele += ln; md.append(str(run) + "^" + g[rpos:rpos + ln]); run = 0; rpos += ln
        elif op == 3:
            juncs.append((rpos + 1, rpos + ln)); rpos += ln
        elif op == 1:
            ins += ln; qpos += ln
        elif op == 4:
            qpos += ln
    md.append(str(run))
    return mm, mmN, "".join(md), ins, dele, juncs, (rec.reference_start, rpos)

def as_of(recs):
    """AS of one alignment given its record(s) (one per mate)."""
    score = 0; jann = []
    lo = min(r.reference_start for r in recs); hi = max(r.reference_end for r in recs)
    for r in recs:
        jm = r.get_tag("jM"); jm = list(jm) if jm != [-1] and jm != -1 else []
        jm = [x for x in jm if x >= 0]
        mm, mmN, md, ins, dele, juncs, span = walk(r)
        nmatch = sum(ln for op, ln in r.cigartuples if op in (0, 7, 8))  # counts N-bases as matches; corrected below
        q = r.query_sequence; g = S.genome[r.reference_name]; rpos = r.reference_start; qpos = 0; nN = 0
        for op, ln in r.cigartuples:
            if op in (0, 7, 8):
                for i in range(ln):
                    if q[qpos + i] == "N" or g[rpos + i] == "N": nN += 1
                rpos += ln; qpos += ln
            elif op in (2, 3): rpos += ln
            elif op in (1, 4): qpos += ln
        score += (nmatch - nN - mm) - mm
        for (s, e), m in zip(juncs, jm):
            score += 2 if m >= 20 else JPEN[m % 20]
        for op, ln in r.cigartuples:
            if op == 1: score += -2 - 2 * ln
            if op == 2: score += -2 - 2 * ln
    score += int(math.ceil(math.log2(hi - lo) * -0.25 - 0.5))
    return max(0, score)

allok = True
for name, prefix in runs.items():
    print("\n== %s" % name)
    bad = collections.Counter(); n = collections.Counter()
    reads = bam_by_read(prefix + "Aligned.out.bam")
    for qname, recs in reads.items():
        mapped = [r for r in recs if not r.is_unmapped]
        if not mapped: continue
        nh = mapped[0].get_tag("NH")
        by_hi = collections.defaultdict(list)
        for r in mapped: by_hi[r.get_tag("HI")].append(r)
        n["reads"] += 1
        if sorted(by_hi) != list(range(1, nh + 1)) or any(r.get_tag("NH") != nh for r in mapped): bad["NH/HI"] += 1
        prim = [hi for hi, rs in by_hi.items() if not rs[0].is_secondary]
        ass = {hi: rs[0].get_tag("AS") for hi, rs in by_hi.items()}
        if len(prim) != 1: bad["primary count"] += 1
        elif ass[prim[0]] != max(ass.values()): bad["primary not best AS"] += 1
        for hi, rs in by_hi.items():
            n["alignments"] += 1
            mapq = 255 if nh == 1 else (3 if nh == 2 else (1 if nh <= 4 else 0))
            if any(r.mapping_quality != mapq for r in rs): bad["MAPQ"] += 1
            exp_as = as_of(rs)
            if ass[hi] != exp_as: bad["AS"] += 1; n["AS examples"] < 3 and (n.update({"AS examples": 1}), print("   AS example", qname, hi, [r.cigarstring for r in rs], "STAR", ass[hi], "port", exp_as))
            nm_tot = 0
            for r in rs:
                mm, mmN, md, ins, dele, juncs, span = walk(r)
                nm_tot += mm
                if r.get_tag("NM") != mmN + ins + dele: bad["NM"] += 1
                if r.get_tag("MD") != md: bad["MD"] += 1
                jm = r.get_tag("jM"); jm = [] if list(jm) == [-1] else list(jm)
                ji = r.get_tag("jI"); ji = [] if list(ji) == [-1] else list(ji)
                if len(jm) != len(juncs): bad["jM length"] += 1
                if ji != [x for s, e in juncs for x in (s, e)]: bad["jI"] += 1
                for (s, e), m in zip(juncs, jm):
                    mot = MOT.get((S.genome[r.reference_name][s - 1:s + 1], S.genome[r.reference_name][e - 2:e]), 0)
                    ann = (r.reference_name, s, e) in S.annot_sj
                    if m != mot + (20 if ann else 0): bad["jM motif"] += 1
                if r.is_paired:
                    if not (r.flag & 1) or not ((r.is_read1 and r.flag & 0x40) or (r.is_read2 and r.flag & 0x80)): bad["pair flags"] += 1
                if "intronMotif" in name:
                    strands = set()
                    for (s, e), m in zip(juncs, jm):
                        if m >= 20: strands.add(annot_strand[(r.reference_name, s, e)])
                        else: strands.add("+" if m % 2 == 1 else ("-" if m > 0 else "."))
                    xs = r.get_tag("XS") if r.has_tag("XS") else None
                    exp = None if not strands else ("+" if strands == {"+"} else ("-" if strands == {"-"} else "?"))
                    if xs != exp: bad["XS"] += 1
                    if juncs: n["spliced records (XS run)"] += 1
            if any(r.get_tag("nM") != nm_tot for r in rs): bad["nM"] += 1
            if len(rs) == 2:
                a, b = sorted(rs, key=lambda r: r.reference_start)
                if not (a.flag & 2 and b.flag & 2): bad["proper pair flag"] += 1
                if a.next_reference_start != b.reference_start or b.next_reference_start != a.reference_start: bad["mate pos"] += 1
                tlen = max(a.reference_end, b.reference_end) - a.reference_start
                if a.template_length != tlen or b.template_length != -tlen: bad["TLEN"] += 1
                if a.is_reverse == b.is_reverse or a.mate_is_reverse != b.is_reverse: bad["mate strand flags"] += 1
            elif len(rs) == 1 and rs[0].is_paired:
                n["single-mate alignments"] += 1
                if not rs[0].mate_is_unmapped: bad["single-mate 0x8"] += 1
    print("  reads %d, alignments %d, single-mate alignments %d, spliced records checked for XS %d" % (n["reads"], n["alignments"], n["single-mate alignments"], n["spliced records (XS run)"]))
    print("  discrepancies:", dict(bad) if bad else "none")
    allok &= not bad
    # sorted BAM
    if name != "SE intronMotif":
        uns = collections.Counter(); srt = collections.Counter(); order_ok = True; last = (-1, -1); unmapped_seen = False; nrec = 0
        with pysam.AlignmentFile(prefix + "Aligned.out.bam", "rb") as bf:
            for r in bf: uns[(r.query_name, r.flag, r.reference_id, r.reference_start, r.cigarstring)] += 1
        with pysam.AlignmentFile(prefix + "Aligned.sortedByCoord.out.bam", "rb") as bf:
            for r in bf:
                nrec += 1
                srt[(r.query_name, r.flag, r.reference_id, r.reference_start, r.cigarstring)] += 1
                if r.is_unmapped and r.reference_id < 0: unmapped_seen = True; continue
                if unmapped_seen: order_ok = False
                key = (r.reference_id, r.reference_start)
                if key < last: order_ok = False
                last = key
        print("  sorted BAM: %d records, same multiset as unsorted: %s, non-decreasing (ref,pos) with unplaced last: %s" % (nrec, uns == srt, order_ok))
        allok &= (uns == srt) and order_ok

print("\nRESULT:", "every record field checked agrees" if allok else "DIFFERENCES FOUND")
