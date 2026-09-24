"""Held-up check: CollectAlignmentSummaryMetrics (non-bisulfite) against independent counts.

Truth per documented definitions for the PAIR category: TOTAL_READS, PF_READS, PCT_PF_READS_ALIGNED,
PCT_READS_ALIGNED_IN_PAIRS, PF_HQ_ALIGNED_READS (MAPQ >= 20), PF_ALIGNED_BASES, PF_MISMATCH_RATE,
PF_HQ_ERROR_RATE, PF_INDEL_RATE (indel events per aligned base), MEAN_READ_LENGTH, STRAND_BALANCE,
PCT_CHIMERAS (pairs with both MAPQ >= 20 whose insert > 100 kb, mates on different contigs, or
orientation not FR; MQ tag present), PCT_PF_READS_IMPROPER_PAIRS, PCT_SOFTCLIP, PCT_HARDCLIP.
Usage: python heldup_alignment_summary.py [picard.jar]
"""
import os, sys, random, statistics
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(41)
L = 300000
ref = rand_seq(rng, L)
ref2 = rand_seq(rng, L)
fa = write_fasta(os.path.join(d, "ref.fa"), [("chr1", ref), ("chr2", ref2)])
def mut(b): return "ACGT"[("ACGT".index(b) + 1) % 4]

recs = []
truth = dict(total=0, pf=0, aligned=0, in_pairs=0, hq_reads=0, aligned_bases=0, mism=0, hq_bases=0, hq_mism=0, indels=0, lens=[], pos_strand=0, chim_den=0, chim=0, improper=0, soft=0, hard=0, q20=0)
def add(r, mism_positions=(), indel=None, hard=0):
    """r is a record from pair(); mutate bases at read offsets in mism_positions."""
    seq = list(ref[r["pos"]:r["pos"] + 100])
    cig = r["cigar"]
    if indel == "D":   # 50M1D49M: read of 99 bases from a 100-bp reference span
        seq = list(ref[r["pos"]:r["pos"] + 50] + ref[r["pos"] + 51:r["pos"] + 100]); cig = "50M1D49M"
    if indel == "I":   # 50M1I49M
        seq = list(ref[r["pos"]:r["pos"] + 50] + "T" + ref[r["pos"] + 50:r["pos"] + 99]); cig = "50M1I49M"
    for p in mism_positions: seq[p] = mut(seq[p])
    r["seq"] = "".join(seq); r["cigar"] = cig; r["qual"] = [rng.choice((30, 30, 15)) for _ in r["seq"]]
    if hard: r["cigar"] = cig + f"{hard}H"
    return r
i = 0
def mkpair(p1, p2, mapq=60, mism=((), ()), indel=(None, None), tid2=0, orient="FR", hard=0, tlen_override=None):
    global i
    r = pair(f"r{i}", p1, p2, rlen=100, mapq=mapq); i += 1
    add(r[0], mism[0], indel[0], hard); add(r[1], mism[1], indel[1])
    for x in r: x.setdefault("tags", {})["MQ"] = mapq
    if tid2 != 0:
        r[1]["tid"] = tid2; r[0]["mtid"] = tid2; r[0]["tlen"] = r[1]["tlen"] = 0
        r[0]["flag"] &= ~2; r[1]["flag"] &= ~2
    if orient == "RF":
        r[0]["flag"] = 0x1 | 0x10 | 0x40; r[1]["flag"] = 0x1 | 0x20 | 0x80
    if tlen_override:
        r[0]["tlen"] = tlen_override; r[1]["tlen"] = -tlen_override
    return r
for k in range(30):
    p1 = 1000 + k * 2000
    mm = (tuple(rng.sample(range(100), rng.choice((0, 0, 1, 3)))), tuple(rng.sample(range(100), rng.choice((0, 2)))))
    ind = (rng.choice((None, None, "D", "I")), None)
    recs += mkpair(p1, p1 + 250, mapq=rng.choice((60, 60, 60, 10)), mism=mm, indel=ind, hard=(3 if k % 10 == 0 else 0))
recs += mkpair(70000, 70250, tid2=1)                       # inter-chromosomal: chimera
recs += mkpair(72000, 72250, orient="RF")                  # RF orientation: chimera
recs += mkpair(74000, 74250, mapq=60, tlen_override=150000)  # insert reported > 100 kb: chimera
recs += mkpair(76000, 76250, mapq=10, tid2=1)              # low MAPQ chimera: not in the denominator
# an unmapped pair and a QC-fail pair
u = pair(f"r{i}", 80000, 80250, rlen=100); i += 1
for x in u: x["flag"] |= 0x200
recs += u
bam = write_bam(os.path.join(d, "asm.bam"), recs, [("chr1", L), ("chr2", L)])
out = os.path.join(d, "asm.txt")
run("CollectAlignmentSummaryMetrics", "-I", bam, "-O", out, "-R", fa)
m = [x for x in parse_metrics(out)[0] if x["CATEGORY"] == "PAIR"][0]

# truth
T = truth
refs = {0: ref, 1: ref2}
for r in recs:
    T["total"] += 1
    if r["flag"] & 0x200: continue
    T["pf"] += 1; T["lens"].append(len(r["seq"]))
    T["hard"] += sum(n for n, op in parse_cigar(r["cigar"]) if op == "H")
    T["aligned"] += 1
    T["soft"] += sum(n for n, op in parse_cigar(r["cigar"]) if op == "S")
    if not r["flag"] & 0x10: T["pos_strand"] += 1
    if not r["flag"] & 2: T["improper"] += 1
    T["in_pairs"] += 1
    hq = r["mapq"] >= 20
    if hq: T["hq_reads"] += 1
    if r["tags"]["MQ"] >= 20 and hq:
        T["chim_den"] += 1
        chim = (r["tid"] != r["mtid"]) or abs(r["tlen"]) > 100000 or bool(r["flag"] & 0x10) == bool(r["flag"] & 0x20)
        # orientation: RF when the forward read is to the right of the reverse read
        if r["tid"] == r["mtid"] and r["flag"] & 0x40 and r["flag"] & 0x10 and not r["flag"] & 0x20: chim = True   # read1 reverse, read2 forward, read1 leftmost -> RF
        if r["tid"] == r["mtid"] and r["flag"] & 0x80 and r["flag"] & 0x20 and not r["flag"] & 0x10: chim = True
        if chim: T["chim"] += 1
    # bases
    rseq = refs[r["tid"]]
    pos = r["pos"]; off = 0
    for n, op in parse_cigar(r["cigar"]):
        if op == "M":
            for j in range(n):
                T["aligned_bases"] += 1
                mm = rseq is not None and r["seq"][off + j] != rseq[pos + j]
                if mm: T["mism"] += 1
                if hq:
                    T["hq_bases"] += 1
                    if mm: T["hq_mism"] += 1
                    if r["qual"][off + j] >= 20: T["q20"] += 1
            pos += n; off += n
        elif op == "I": T["indels"] += 1; off += n
        elif op == "D": T["indels"] += 1; pos += n
        elif op == "S": off += n
exp = dict(TOTAL_READS=T["total"], PF_READS=T["pf"], PCT_PF_READS_ALIGNED=T["aligned"] / T["pf"], PCT_READS_ALIGNED_IN_PAIRS=T["in_pairs"] / T["aligned"],
           PF_HQ_ALIGNED_READS=T["hq_reads"], PF_ALIGNED_BASES=T["aligned_bases"], PF_MISMATCH_RATE=T["mism"] / T["aligned_bases"],
           PF_HQ_ERROR_RATE=T["hq_mism"] / T["hq_bases"], PF_INDEL_RATE=T["indels"] / T["aligned_bases"], MEAN_READ_LENGTH=statistics.fmean(T["lens"]),
           STRAND_BALANCE=T["pos_strand"] / T["aligned"], PCT_CHIMERAS=T["chim"] / T["chim_den"], PCT_PF_READS_IMPROPER_PAIRS=T["improper"] / T["aligned"],
           PCT_SOFTCLIP=T["soft"] / sum(T["lens"]), PCT_HARDCLIP=T["hard"] / sum(T["lens"]), PF_HQ_ALIGNED_Q20_BASES=T["q20"])
bad = 0
for k, v in exp.items():
    g = m[k]; ok = abs(float(g) - float(v)) < 1e-5; bad += not ok
    print(f"  {k:28s} picard {g!s:12s} truth {round(v, 6)!s:12s} {'ok' if ok else 'MISMATCH'}")
print("  mismatches:", bad)
