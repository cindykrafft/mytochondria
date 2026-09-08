"""Held-up checks for `samtools mpileup`: the depth column against Python under
the default -Q 13, -Q 0, -Q 30, -q, with and without the default read-pair
overlap removal (-x; port of htslib tweak_overlap_quality for indel-free
mates), the deletion/refskip counting rule, BAQ off/on with a matching
reference, and the -d depth cap.  Usage: python heldup_mpileup.py [samtools]
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
random.seed(9)
d = tmpdir()
L = 20000
ref = "".join(random.choice("ACGT") for _ in range(L))
fa = os.path.join(d, "ref.fa")
with open(fa, "w") as f: f.write(">chr1\n" + ref + "\n")
pysam.faidx(fa)
refs = [("chr1", L)]

def read_seq(pos, cig):
    s, p = [], pos
    for n, op in parse_cigar(cig):
        if op in "M=X":
            seg = list(ref[p:p + n])
            for i in range(n):
                if random.random() < 0.02: seg[i] = random.choice("ACGT".replace(seg[i], ""))
            s += seg; p += n
        elif op == "I": s += [random.choice("ACGT") for _ in range(n)]
        elif op == "S": s += [random.choice("ACGT") for _ in range(n)]
        elif op in "DN": p += n
    return "".join(s)

recs = []
for i in range(800):
    pos = random.randrange(0, L - 1000)
    cig = random.choice(["100M", "100M", "100M", "50M2D50M", "40M3I57M", "30M500N70M", "6S94M"])
    mapq = random.choice([0, 10, 30, 60]); flag = random.choice([0, 0, 0, 0x10, 0x400, 0x100])
    recs.append(simple_read(f"s{i}", pos, cig, flag=flag, mapq=mapq, seq=read_seq(pos, cig), qual=[random.choice([5, 12, 13, 20, 30, 40]) for _ in range(qlen(cig))]))
pairs = []
for i in range(400):   # overlapping proper pairs, plain 100M
    pos = random.randrange(0, L - 300); ins = random.randrange(110, 199)
    q1 = [random.choice([5, 12, 20, 30, 40]) for _ in range(100)]; q2 = [random.choice([5, 12, 20, 30, 40]) for _ in range(100)]
    r1 = simple_read(f"p{i}", pos, "100M", flag=0x63, mapq=60, seq=read_seq(pos, "100M"), qual=q1, mtid=0, mpos=pos + ins - 100, tlen=ins)
    r2 = simple_read(f"p{i}", pos + ins - 100, "100M", flag=0x93, mapq=60, seq=read_seq(pos + ins - 100, "100M"), qual=q2, mtid=0, mpos=pos, tlen=-ins)
    recs += [r1, r2]; pairs.append((r1, r2))
bam = write_bam(os.path.join(d, "mp.bam"), recs, refs)

def overlap_adjust(recs):
    """Port of tweak_overlap_quality for indel-free mates: returns a copy of records with adjusted quals."""
    import copy
    recs = copy.deepcopy(recs)
    by = collections.defaultdict(list)
    for r in recs:
        if r["flag"] & 2 and not r["flag"] & 0x904: by[r["name"]].append(r)
    for name, (a, b) in ((n, sorted(v, key=lambda r: r["pos"])) for n, v in by.items() if len(v) == 2):
        if abs(a["tlen"]) >= 2 * len(a["seq"]) and a["mpos"] >= a["pos"] + 100: continue
        # which mate keeps the summed quality: hash of the name (amul) -- we cannot reproduce khash's Wang hash here,
        # but the depth only depends on which *values* survive, not on which mate holds them.
        for p in range(max(a["pos"], b["pos"]), min(a["pos"] + 100, b["pos"] + 100)):
            ia, ib = p - a["pos"], p - b["pos"]
            qa, qb = a["qual"][ia], b["qual"][ib]
            if a["seq"][ia] == b["seq"][ib]:
                a["qual"][ia], b["qual"][ib] = min(200, qa + qb), 0
            elif qa > qb: a["qual"][ia], b["qual"][ib] = int(0.8 * qa), 0
            elif qa < qb: a["qual"][ia], b["qual"][ib] = 0, int(0.8 * qb)
            else: a["qual"][ia], b["qual"][ib] = int(0.8 * qa), 0
    return recs

def mp_truth(recs, min_bq=13, min_mq=0, excl=0x4 | 0x100 | 0x200 | 0x400, orphans=False):
    """mpileup depth: M/=/X bases with qual >= Q; a deleted or skipped position counts when the qual of the
    read's next base (qpos) is >= Q (htslib leaves qpos at the base after the deletion)."""
    dd = collections.Counter()
    for r in recs:
        if r["flag"] & excl or r["mapq"] < min_mq: continue
        if not orphans and r["flag"] & 1 and not r["flag"] & 2: continue
        p, s = r["pos"], 0
        for n, op in parse_cigar(r["cigar"]):
            if op in "M=X":
                for i in range(n):
                    if r["qual"][s + i] >= min_bq: dd[p + i] += 1
                p += n; s += n
            elif op in "DN":
                q = r["qual"][s] if s < len(r["qual"]) else 0
                for i in range(n):
                    if q >= min_bq: dd[p + i] += 1
                p += n
            elif op in "IS": s += n
    return dd

def mp_rows(*args):
    out, err, rc = run("mpileup", *args, bam)
    if rc: print("  mpileup failed:", err.strip()[:200])
    return {int(l.split("\t")[1]) - 1: int(l.split("\t")[3]) for l in out.splitlines()}

def compare(label, args, truth):
    got = mp_rows(*args)
    exp = {p: v for p, v in truth.items() if v > 0}
    bad = sum(1 for p in set(got) | set(exp) if got.get(p, 0) != exp.get(p, 0))
    print(f"  {'OK ' if not bad else 'BAD'} mpileup {label:34s}: {len(got)} rows, total depth {sum(got.values())}, truth rows {len(exp)} total {sum(exp.values())}, mismatching positions {bad}")
    return bad

print("\n--- depth column vs Python")
adj = overlap_adjust(recs)
tot = 0
tot += compare("(defaults: -Q 13, overlaps removed)", [], mp_truth(adj))
tot += compare("-x (no overlap removal)", ["-x"], mp_truth(recs))
tot += compare("-x -Q 0", ["-x", "-Q", "0"], mp_truth(recs, min_bq=0))
tot += compare("-x -Q 30", ["-x", "-Q", "30"], mp_truth(recs, min_bq=30))
tot += compare("-Q 30 (overlaps removed)", ["-Q", "30"], mp_truth(adj, min_bq=30))
tot += compare("-x -q 30", ["-x", "-q", "30"], mp_truth(recs, min_mq=30))
tot += compare("-x --ff UNMAP,SECONDARY", ["-x", "--ff", "UNMAP,SECONDARY"], mp_truth(recs, excl=0x104))
tot += compare("-x -B -f ref.fa (BAQ off)", ["-x", "-B", "-f", fa], mp_truth(recs))
got_baq = mp_rows("-x", "-f", fa); got_nobaq = mp_rows("-x", "-B", "-f", fa)
diff = sum(1 for p in set(got_baq) | set(got_nobaq) if got_baq.get(p, 0) != got_nobaq.get(p, 0))
print(f"  note: default BAQ (-f, no -B) changes the depth at {diff} of {len(got_nobaq)} positions (BAQ lowers qualities near indels/mismatches; design)")
print("  mismatching positions in total (excluding the BAQ note):", tot)

print("\n--- -d depth cap: 10,000 identical 100M reads at one position")
big = [simple_read(f"b{i}", 5000, "100M", qual=30, seq=ref[5000:5100]) for i in range(10000)]
bam = write_bam(os.path.join(d, "big.bam"), big, refs)
for args in (["-x"], ["-x", "-d", "0"], ["-x", "-d", "100"], ["-x", "-d", "20000"]):
    got = mp_rows(*args)
    print(f"  mpileup {' '.join(args):14s}: depth at 5001 = {got.get(5000)}, at 5100 = {got.get(5099)}  (true depth 10000)")
