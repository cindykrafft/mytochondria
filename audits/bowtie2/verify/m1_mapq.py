"""M1: MAPQ (default calculator, BowtieMapq2) recomputed from AS/XS and the read
lengths with a Python port of unique.h, for unpaired reads and concordant pairs
in end-to-end and local mode, including pairs whose mates differ in length.

Reference: 60 kb of random sequence carrying repeat families: a 300-bp segment
copied once with d substitutions (d = 0, 1, 2, 3, 5, 8, 12, 20), so a read taken
from copy A with m mismatches of its own has a second-best alignment at copy B.
Pairs: a 400-bp fragment duplicated with d substitutions inside both mate spans.
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(11)
G = 60000
ref = list(rand_seq(rng, G))
REP = 300
fams = []   # (d, posA, posB)
cursor = 2000
for d in (0, 1, 2, 3, 5, 8, 12, 20):
    posA = cursor; posB = cursor + 4000
    seg = ref[posA:posA + REP]
    copy = list(seg)
    subpos = rng.sample(range(20, REP - 20), d)   # keep the ends identical
    for p in subpos:
        copy[p] = rng.choice([b for b in "ACGT" if b != copy[p]])
    ref[posB:posB + REP] = copy
    fams.append((d, posA, posB, sorted(subpos)))
    cursor += 7000
refs = "".join(ref)
d = tmpdir()
write_fasta(os.path.join(d, "ref.fa"), [("chr1", refs)])
idx = build_index(os.path.join(d, "ref.fa"), os.path.join(d, "ref"))
print(f"bowtie2 {version()}  reference {G} bp with {len(fams)} repeat families (300 bp x 2)")

def run_block(mode, L, extra):
    args = list(extra) + (["--local"] if mode == "local" else [])
    reads = []; truth = {}
    for fi, (dd, posA, posB, subpos) in enumerate(fams):
        for m in (0, 1, 2, 4, 6):
            for q in (40, 20):
                # read from copy A, starting at offset 10, mismatches at positions not in subpos
                name = f"f{fi}_d{dd}_m{m}_q{q}_L{L}"
                start = posA + 10
                cand = [o for o in range(15, L - 15) if (o + 10) not in subpos]
                offs = rng.sample(cand, m)
                edits = [("mm", o, rng.choice([b for b in "ACGT" if b != refs[start + o]])) for o in offs]
                rd = make_read(name, refs, start, L, fw=(fi % 2 == 0), edits=edits, qual=q, mode=mode)
                reads.append(fq(rd))
                # second best: at copy B the read has m + (subpos within span) mismatches
                nB = sum(1 for p in subpos if 10 <= p < 10 + L)
                truth[name] = dict(m=m, d=dd, nB=nB, q=q, AS=rd["AS"], pos=rd["pos"])
    recs, err = align(idx, unpaired=reads, args=args)
    bad = 0; n = 0; unal = 0
    for r in recs:
        t = truth[r.qname]
        if r.flag & 4:
            unal += 1; continue
        n += 1
        xs = r.tags.get("XS")
        exp = mapq_v2(r.tags["AS"], xs, L, None, mode)
        ok = exp == r.mapq
        if not ok:
            bad += 1
            print(f"   mismatch {r.qname}: AS {r.tags['AS']} XS {xs} MAPQ {r.mapq} port {exp}")
    report(f"{mode} unpaired L={L} {' '.join(extra) or 'default'}: {n} aligned ({unal} unaligned), MAPQ matches the port on {n - bad}/{n}", bad == 0)

for mode in ("e2e", "local"):
    run_block(mode, 100, [])
    run_block(mode, 50, [])
    run_block(mode, 150, ["--very-sensitive"] if mode == "e2e" else ["--very-sensitive-local"])
    run_block(mode, 100, ["--mp", "4,2"])

# ---- concordant pairs: unique fragments and duplicated fragments, equal and unequal mate lengths
def pair_block(mode, L1, L2, dup_d, m1, m2, label):
    args = ["--local"] if mode == "local" else []
    base = 55000  # unique region for the fragment
    # duplicate the fragment? build a private reference per block
    refl = list(refs)
    fraglen = 350
    f0 = 50500
    if dup_d is not None:
        seg = refl[f0:f0 + fraglen]; copy = list(seg)
        # substitutions inside mate 1 span and mate 2 span (away from mate ends)
        subs = rng.sample(range(15, L1 - 15), dup_d // 2) + rng.sample(range(fraglen - L2 + 15, fraglen - 15), dup_d - dup_d // 2)
        for p in subs:
            copy[p] = rng.choice([b for b in "ACGT" if b != copy[p]])
        refl[56000:56000 + fraglen] = copy
    else:
        subs = []
    rs = "".join(refl)
    dd = tmpdir()
    write_fasta(os.path.join(dd, "ref.fa"), [("chr1", rs)])
    ix = build_index(os.path.join(dd, "ref.fa"), os.path.join(dd, "ref"))
    e1 = [("mm", o, rng.choice([b for b in "ACGT" if b != rs[f0 + o]])) for o in rng.sample([o for o in range(15, L1 - 15) if o not in subs], m1)]
    e2 = [("mm", o, rng.choice([b for b in "ACGT" if b != rs[f0 + fraglen - L2 + o]])) for o in rng.sample([o for o in range(15, L2 - 15) if (fraglen - L2 + o) not in subs], m2)]
    p1, p2 = mate_pair("p", rs, f0, fraglen, L1, L2, e1, e2, qual=40, mode=mode)
    recs, err = align(ix, mates=[(fq(p1), fq(p2))], args=args + ["-X", "600"])
    r1 = [r for r in recs if r.flag & 64][0]; r2 = [r for r in recs if r.flag & 128][0]
    assert r1.flag & 2 and r2.flag & 2, (r1, r2)
    AS = r1.tags["AS"] + r2.tags["AS"]
    xs1, xs2 = r1.tags.get("XS"), r2.tags.get("XS")
    XS = (xs1 + xs2) if (xs1 is not None and xs2 is not None) else None
    exp1 = mapq_v2(AS, XS, L1, L2, mode)       # mate 1: rdlen L1, ordlen L2
    exp2 = mapq_v2(AS, XS, L2, L1, mode)       # mate 2: rdlen L2, ordlen L1 (the same number: the formula is symmetric)
    exp2_bug = mapq_v2(AS, XS, L2, L2, mode)   # mate 2 with its own length used for both mates
    tag = "ok" if (r1.mapq == exp1 and r2.mapq == exp2) else ("MATE2-USES-OWN-LENGTH-TWICE" if (r1.mapq == exp1 and r2.mapq == exp2_bug) else "MISMATCH")
    print(f"   {mode:5s} {label:34s} L1={L1:3d} L2={L2:3d} AS1={r1.tags['AS']:4d} AS2={r2.tags['AS']:4d} XS1={str(xs1):5s} XS2={str(xs2):5s}  MAPQ mate1={r1.mapq:3d} mate2={r2.mapq:3d}  port: both={exp1:3d}  mate2-if-own-length-twice={exp2_bug:3d}  -> {tag}")
    return tag

print("\nconcordant pairs (default -X 600):")
tags = []
for mode in ("e2e", "local"):
    tags.append(pair_block(mode, 100, 100, None, 0, 0, "unique, equal lengths, perfect"))
    tags.append(pair_block(mode, 100, 100, None, 3, 2, "unique, equal lengths, 3+2 mm"))
    tags.append(pair_block(mode, 150, 50, None, 0, 0, "unique, unequal lengths, perfect"))
    tags.append(pair_block(mode, 150, 50, None, 3, 2, "unique, unequal 150/50, 3+2 mm"))
    tags.append(pair_block(mode, 150, 75, None, 4, 1, "unique, unequal 150/75, 4+1 mm"))
    tags.append(pair_block(mode, 100, 100, 6, 1, 1, "duplicated (6 subs), equal, 1+1 mm"))
    tags.append(pair_block(mode, 150, 50, 6, 1, 1, "duplicated (6 subs), 150/50, 1+1 mm"))
    tags.append(pair_block(mode, 150, 60, 2, 0, 0, "duplicated (2 subs), 150/60, perfect"))
report("concordant pairs: both mates' MAPQ match the port", all(t == "ok" for t in tags),
       f"({sum(t == 'MATE2-USES-OWN-LENGTH-TWICE' for t in tags)} cases where mate 2's MAPQ equals the port fed mate 2's length for both mates)")
