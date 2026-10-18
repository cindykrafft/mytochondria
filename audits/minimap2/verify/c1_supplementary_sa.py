"""C1: primary / supplementary / secondary choice and the SA tag (format.c, hit.c).

Reads:
  - chimeras: segment X (800-3000 bp) from one locus joined to segment Y
    (800-3000 bp) from a locus >= 100 kb away, same or opposite strand,
    error-free and ONT-like (map-ont), and 150-bp short-read chimeras 80+70 (sr);
  - reads from an exact two-copy repeat (expect one primary + one secondary,
    MAPQ 0, tp:A:S, s2 == s1 for the primary).
Truth: the two segments' origins. Checks: exactly one primary (no 0x900), the
other segment as 0x800 with hard clips (no -Y), each record carries an SA entry
whose RNAME, POS, strand, MAPQ and NM equal the other record's, the clipped
lengths in the SA CIGAR equal the other record's clips, and placements equal
the planted origins.
"""
import os, sys, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(77)
G = 5000000
ref = list(rand_seq(rng, G))
REPS = []
for i in range(30):
    a = 4000000 + i * 30000; b = a + 12000
    ref[b:b + 4000] = ref[a:a + 4000]; REPS.append((a, b))
refs = "".join(ref)
d = tmpdir(); fa = os.path.join(d, "ref.fa"); write_fasta(fa, [("chr1", refs)])
print(version(), f" reference {G} bp random")


def clips(cigar):
    ops = cigar_ops(cigar)
    l = ops[0][0] if ops[0][1] in "SH" else 0
    r = ops[-1][0] if ops[-1][1] in "SH" else 0
    return l, r


def check(label, args, reads, truth):
    fq = os.path.join(d, label.replace(" ", "_") + ".fq"); write_fastq(fq, reads)
    recs = parse_sam(run(args + ["-t1", fa, fq]))
    by = collections.defaultdict(list)
    for r in recs:
        by[r["qname"]].append(r)
    c = collections.Counter(); ex = []
    for name, (segs) in truth.items():
        rs = [r for r in by[name] if not r["flag"] & 0x104]
        pri = [r for r in rs if not r["flag"] & 0x800]
        sup = [r for r in rs if r["flag"] & 0x800]
        c["reads"] += 1
        if len(pri) != 1: c["not exactly one primary"] += 1; continue
        if len(sup) != 1: c[f"{len(sup)} supplementary"] += 1; continue
        p, s = pri[0], sup[0]
        # placement
        placed = sorted([(r["pos"] - 1, bool(r["flag"] & 16)) for r in (p, s)])
        exp = sorted([(st, rev) for st, rev in segs])
        if all(abs(a[0] - b[0]) <= 20 and a[1] == b[1] for a, b in zip(placed, exp)):
            c["both segments placed at their origins"] += 1
        else:
            ex.append(("placement", name, placed, exp))
        if "H" not in s["cigar"]: c["supplementary without hard clip"] += 1
        for x, y in ((p, s), (s, p)):
            sa = x["tags"].get("SA")
            if not sa: c["missing SA"] += 1; continue
            ent = [e.split(",") for e in sa.strip(";").split(";")]
            if len(ent) != 1: c["SA entries != 1"] += 1; continue
            rn, pos, strand, cig, mq, nm = ent[0]
            fields_ok = (rn == y["rname"] and int(pos) == y["pos"] and (strand == "-") == bool(y["flag"] & 16)
                         and int(mq) == y["mapq"] and int(nm) == y["tags"]["NM"])
            if fields_ok: c["SA RNAME/POS/strand/MAPQ/NM == other record"] += 1
            else: ex.append(("SA fields", name, ent[0], (y["rname"], y["pos"], y["flag"], y["mapq"], y["tags"]["NM"])))
            if clips(cig) == clips(y["cigar"]): c["SA clip lengths == other record"] += 1
            else: ex.append(("SA clips", name, cig, y["cigar"]))
    print(f"\n[{label}] " + "; ".join(f"{k}: {v}" for k, v in c.items()))
    for e in ex[:5]:
        print("   ", e)
    return c


L_reads, L_truth = [], {}
for i in range(120):
    lx, ly = rng.randint(800, 3000), rng.randint(800, 3000)
    x = rng.randint(10000, 1900000); y = rng.randint(2000000, 3900000)
    rx, ry = rng.random() < .5, rng.random() < .5
    sx = refs[x:x + lx]; sy = refs[y:y + ly]
    s = (revcomp(sx) if rx else sx) + (revcomp(sy) if ry else sy)
    if i % 2:
        s = noisy(rng, s, sub=.03, ins=.015, dele=.015)
    L_reads.append((f"chim{i}_{'ont' if i % 2 else 'exact'}", s)); L_truth[L_reads[-1][0]] = [(x, rx), (y, ry)]
check("map-ont chimeras", ["-ax", "map-ont"], L_reads, L_truth)

S_reads, S_truth = [], {}
for i in range(120):
    x = rng.randint(10000, 1900000); y = rng.randint(2000000, 3900000)
    s = refs[x:x + 80] + revcomp(refs[y:y + 70])
    S_reads.append((f"schim{i}", s)); S_truth[f"schim{i}"] = [(x, False), (y, True)]
check("sr chimeras 80+70", ["-ax", "sr"], S_reads, S_truth)

# repeat reads
R_reads = []
for i, (a, b) in enumerate(REPS):
    for k in range(4):
        st = a + rng.randint(0, 4000 - 2000)
        R_reads.append((f"rep{i}_{k}", refs[st:st + 2000]))
fq = os.path.join(d, "rep.fq"); write_fastq(fq, R_reads)
paf = parse_paf(run(["-t1", fa, fq]))
by = collections.defaultdict(list)
for r in paf: by[r["qname"]].append(r)
c = collections.Counter()
for name, rs in by.items():
    P = [r for r in rs if r["tags"]["tp"] == "P"]; S = [r for r in rs if r["tags"]["tp"] == "S"]
    c["reads"] += 1
    if len(P) == 1 and len(S) == 1: c["1 primary + 1 secondary"] += 1
    if all(r["mapq"] == 0 for r in rs): c["all MAPQ 0"] += 1
    if len(P) == 1 and P[0]["tags"].get("s2") == P[0]["tags"]["s1"]: c["primary s2 == s1"] += 1
print("\n[map-ont exact 2-copy repeat, PAF] " + "; ".join(f"{k}: {v}" for k, v in c.items()))
