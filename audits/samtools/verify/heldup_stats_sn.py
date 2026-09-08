"""Held-up checks for the `samtools stats` SN summary numbers on a synthetic
paired-end library (2,000 pairs, insert sizes N(300, 50) with a long tail,
duplicates, unmapped mates, inter-chromosomal pairs, MQ0, QC-fail, secondary
and supplementary records, NM tags): read counts, bases mapped (cigar),
mismatches and error rate, average length/quality, insert size average and
standard deviation (main-bulk rule), orientation counts, pairs on different
chromosomes, percentage of properly paired reads, and -F/-f/-d filters.
Usage: python heldup_stats_sn.py [samtools]
"""
import math, os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
random.seed(3)
d = tmpdir()
refs = [("chr1", 1_000_000), ("chr2", 200_000)]
recs = []
def rq(n): return [random.choice([2, 15, 25, 30, 35, 40]) for _ in range(n)]
def rseq(n): return "".join(random.choice("ACGTACGTN") for _ in range(n))
for i in range(2000):
    tid = 0
    pos = random.randrange(0, 900_000)
    ins = int(random.gauss(300, 50))
    if random.random() < 0.02: ins = random.randrange(2000, 30000)   # tail
    ins = max(ins, 100)
    l1, l2 = random.choice([100, 100, 100, 90, 75]), random.choice([100, 100, 100, 80, 60])
    nm1, nm2 = random.choice([0, 0, 1, 3]), random.choice([0, 0, 2, 4])
    f1, f2 = 0x1 | 0x40, 0x1 | 0x80
    kind = random.random()
    mapq = random.choice([0, 0, 10, 30, 60, 60])
    if kind < 0.85:      # FR proper pair
        f1 |= 0x2 | 0x20; f2 |= 0x2 | 0x10
        r1 = simple_read(f"p{i}", pos, f"{l1}M", flag=f1, mapq=mapq, qual=rq(l1), seq=rseq(l1), mtid=0, mpos=pos + ins - l2, tlen=ins, tags={"NM": nm1})
        r2 = simple_read(f"p{i}", pos + ins - l2, f"{l2}M", flag=f2, mapq=mapq, qual=rq(l2), seq=rseq(l2), mtid=0, mpos=pos, tlen=-ins, tags={"NM": nm2})
    elif kind < 0.90:    # mate unmapped
        f1 |= 0x8; f2 |= 0x4
        r1 = simple_read(f"p{i}", pos, f"{l1}M", flag=f1, mapq=mapq, qual=rq(l1), seq=rseq(l1), mtid=0, mpos=pos, tlen=0, tags={"NM": nm1})
        r2 = dict(name=f"p{i}", flag=f2, tid=0, pos=pos, mapq=0, cigar=None, seq=rseq(l2), qual=rq(l2), mtid=0, mpos=pos, tlen=0)
    elif kind < 0.95:    # different chromosomes
        f1 |= 0x20; f2 |= 0x10
        p2 = random.randrange(0, 100_000)
        r1 = simple_read(f"p{i}", pos, f"{l1}M", flag=f1, mapq=mapq, qual=rq(l1), seq=rseq(l1), mtid=1, mpos=p2, tlen=0, tags={"NM": nm1})
        r2 = simple_read(f"p{i}", p2, f"{l2}M", flag=f2, tid=1, mapq=mapq, qual=rq(l2), seq=rseq(l2), mtid=0, mpos=pos, tlen=0, tags={"NM": nm2})
    else:                # both unmapped
        f1 |= 0x4 | 0x8; f2 |= 0x4 | 0x8
        r1 = dict(name=f"p{i}", flag=f1, tid=-1, pos=-1, mapq=0, cigar=None, seq=rseq(l1), qual=rq(l1), mtid=-1, mpos=-1, tlen=0)
        r2 = dict(name=f"p{i}", flag=f2, tid=-1, pos=-1, mapq=0, cigar=None, seq=rseq(l2), qual=rq(l2), mtid=-1, mpos=-1, tlen=0)
    if random.random() < 0.08: r1["flag"] |= 0x400; r2["flag"] |= 0x400
    if random.random() < 0.03: r1["flag"] |= 0x200; r2["flag"] |= 0x200
    recs += [r1, r2]
    if kind < 0.85 and random.random() < 0.05:
        recs.append(simple_read(f"p{i}", random.randrange(0, 900_000), f"{l1}M", flag=(f1 | 0x100), mapq=0, qual=rq(l1), seq=rseq(l1), mtid=0, mpos=r1["mpos"], tlen=0, tags={"NM": 5}))
    if kind < 0.85 and random.random() < 0.04:
        recs.append(simple_read(f"p{i}", random.randrange(0, 900_000), f"40M{l2 - 40}H", flag=(f2 | 0x800 | (r2["flag"] & 0x400)), mapq=mapq, qual=rq(40), seq=rseq(40), mtid=0, mpos=r2["mpos"], tlen=0, tags={"NM": 1}))
bam = write_bam(os.path.join(d, "sn.bam"), recs, refs)

def truth(recs, flag_filter=0, flag_require=0):
    t = collections.Counter()
    isz = collections.Counter(); orient = collections.Counter()
    for r in recs:
        f = r["flag"]
        if flag_require and (f & flag_require) != flag_require: t["filtered"] += 1; continue
        if flag_filter and (f & flag_filter): t["filtered"] += 1; continue
        if f & 0x100: t["secondary"] += 1; continue
        if f & 0x800: t["supplementary"] += 1
        n = len(r["seq"])
        if f & 0x400: t["dup reads"] += 1; t["dup bases"] += n
        orig = not (f & 0x800)
        if orig:
            t["sequences"] += 1; t["total length"] += n
            t["qsum"] += sum(r["qual"])
            if f & 0x200: t["qcfail"] += 1
            if f & 0x1: t["paired tech"] += 1
            if f & 0x40: t["1st"] += 1
            if f & 0x80: t["2nd"] += 1
            t["maxlen"] = max(t["maxlen"], n)
            if f & 0x4: t["unmapped"] += 1
            else:
                t["bases mapped"] += n
                if r["mapq"] == 0: t["mq0"] += 1
                if f & 0x1 and not f & 0x8:
                    t["mapped and paired"] += 1
                    if f & 0x2: t["properly paired"] += 1
                    if r["tid"] != r["mtid"]: t["anomalous"] += 1
                    iz = min(abs(r["tlen"]), 8000)
                    if iz > 0 or r["tid"] == r["mtid"]:
                        isz[iz] += 1
                        fwd = not f & 0x10; mfwd = not f & 0x20
                        if fwd == mfwd: orient["other"] += 1
                        else:
                            is_fst = 1 if f & 0x40 else -1; is_fwd = 1 if fwd else -1
                            pf = r["mpos"] - r["pos"]
                            if is_fst * pf > 0: orient["inward" if is_fst * is_fwd > 0 else "outward"] += 1
                            elif is_fst * pf < 0: orient["outward" if is_fst * is_fwd > 0 else "inward"] += 1
                            else: orient["inward"] += 1
                else: t["single mapped"] += 1
        if not f & 0x4:
            t["mismatches"] += r["tags"]["NM"]
            t["cigar bases"] += sum(k for k, op in parse_cigar(r["cigar"]) if op in "MI=X")
    # insert size: each pair counted twice, halved; main bulk 0.99
    counts = {k: v // 2 for k, v in isz.items()}
    nis = sum(counts.values())
    bulk = 0; avg = 0.0; ibulk = 0; nbulk = nis
    for k in sorted(counts):
        bulk += counts[k]; avg += k * counts[k]
        if bulk / nis > 0.99: ibulk = k + 1; nbulk = bulk; break
    avg /= nbulk
    sd = math.sqrt(sum(counts[k] * (k - avg) ** 2 for k in counts if 1 <= k < ibulk) / nbulk)
    t.update(dict(isize_avg=avg, isize_sd=sd, inward=orient["inward"] // 2, outward=orient["outward"] // 2, other=orient["other"] // 2))
    return t

def check(label, extra, **kw):
    out, err, rc = run("stats", *extra, bam)
    S = sn(out); T = truth(recs, **kw)
    exp = {
        "raw total sequences": T["sequences"] + T["filtered"], "filtered sequences": T["filtered"], "sequences": T["sequences"],
        "1st fragments": T["1st"], "last fragments": T["2nd"], "reads mapped": T["mapped and paired"] + T["single mapped"],
        "reads mapped and paired": T["mapped and paired"], "reads unmapped": T["unmapped"], "reads properly paired": T["properly paired"],
        "reads paired": T["paired tech"], "reads duplicated": T["dup reads"], "reads MQ0": T["mq0"], "reads QC failed": T["qcfail"],
        "non-primary alignments": T["secondary"], "supplementary alignments": T["supplementary"], "total length": T["total length"],
        "bases mapped": T["bases mapped"], "bases mapped (cigar)": T["cigar bases"], "bases duplicated": T["dup bases"], "mismatches": T["mismatches"],
        "error rate": f"{T['mismatches'] / T['cigar bases']:e}", "average length": f"{T['total length'] / T['sequences']:.0f}",
        "maximum length": T["maxlen"], "average quality": f"{T['qsum'] / T['total length']:.1f}",
        "insert size average": f"{T['isize_avg']:.1f}", "insert size standard deviation": f"{T['isize_sd']:.1f}",
        "inward oriented pairs": T["inward"], "outward oriented pairs": T["outward"], "pairs with other orientation": T["other"],
        "pairs on different chromosomes": T["anomalous"] // 2,
        "percentage of properly paired reads (%)": f"{100 * T['properly paired'] / T['sequences']:.1f}",
    }
    bad = 0
    print(f"\n--- stats {' '.join(extra)}  [{label}]")
    for k, v in exp.items():
        got = S.get(k)
        ok = str(got) == str(v) or (isinstance(v, str) and "e" in v and abs(float(got) - float(v)) <= 2e-6 * float(v))
        bad += not ok
        print(f"  {'OK ' if ok else 'BAD'} {k:42s} samtools {got:>14}  truth {v}")
    print("  wrong:", bad)
check("all reads", [])
check("-F DUP,QCFAIL", ["-F", "0x600"], flag_filter=0x600)
check("-d (remove dups)", ["-d"], flag_filter=0x400)
check("-f PROPER_PAIR", ["-f", "0x2"], flag_require=0x2)
