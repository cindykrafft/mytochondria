#!/usr/bin/env python3
"""TM1 and TM2 through the command line only, for every version built or downloaded.

Usage: python3 version_scope_cli.py <trimmomatic.jar | build-dir> <adapters-dir>
Prints one 'affected'/'unaffected' verdict per finding, from the outputs only.
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_ref as T

build = T.build_from_arg(sys.argv[1]); adir = sys.argv[2]
AD = os.path.join(adir, "TruSeq3-PE.fa"); recs = dict(T.load_fasta(AD)); P1, P2 = recs["PrefixPE/1"], recs["PrefixPE/2"]
print("build:", " ".join(build)); print("adapters:", AD, "prefix lengths", len(P1), len(P2))

def make_pair(rng, R, L, mism):
    frag = T.rand_seq(rng, L)
    r1 = list((frag + T.revcomp(P2) + T.rand_seq(rng, R))[:R]); r2 = (T.revcomp(frag) + T.revcomp(P1) + T.rand_seq(rng, R))[:R]
    q1, q2 = [40] * R, [40] * R
    for p, q in mism: r1[p] = T.mutate(rng, r1[p]); q1[p] = q
    return "".join(r1), q1, r2, q2

# TM1: 200 2x50 pairs, insert 42, two read-1 mismatches at Q19 (documented score 29.9 < 30: no clip)
reads1, reads2, meta = [], [], []
for k in range(200):
    rng = random.Random(19000 + 20 + k)
    r1, q1, r2, q2 = make_pair(rng, 50, 42, [(p, 19) for p in rng.sample(range(0, 18), 2)])
    reads1.append(("m%d" % k, r1, q1)); reads2.append(("m%d" % k, r2, q2)); meta.append((r1, q1, r2, q2))
doc = sum(T.palindrome_clip(*m, P1, P2, 2, 30) is not None for m in meta)
res, log, d = T.run_pe(build, reads1, reads2, ["ILLUMINACLIP:%s:2:30:10" % AD])
clipped = sum(1 for n, s, q in reads1 if n not in res["1P"])
print("TM1: pairs clipped by the shipped build %d/200 (documented rule: %d/200) -> %s" % (clipped, doc, "affected" if clipped > doc else "unaffected"))
# control: same pairs with the mismatches at Q20 (penalty 2 under both rules -> documented 29.7, no clip either way)
reads1c, reads2c = [], []
for k in range(200):
    rng = random.Random(19000 + 20 + k)
    r1, q1, r2, q2 = make_pair(rng, 50, 42, [(p, 20) for p in rng.sample(range(0, 18), 2)])
    reads1c.append(("c%d" % k, r1, q1)); reads2c.append(("c%d" % k, r2, q2))
res, log, d = T.run_pe(build, reads1c, reads2c, ["ILLUMINACLIP:%s:2:30:10" % AD])
print("TM1 control (mismatches at Q20): clipped %d/200 (both rules: 0)" % sum(1 for n, s, q in reads1c if n not in res["1P"]))

# TM2: 300-nt Q40 read
seq = T.rand_seq(random.Random(7), 300); q = [40] * 300
got = {}
for step in ("MAXINFO:40:0.5", "MAXINFO:247:0.1", "MAXINFO:248:0.1", "MAXINFO:250:0.1", "MAXINFO:500:0.2", "MAXINFO:800:0.5"):
    res, log, d = T.run_se(build, [("r", seq, q)], [step])
    got[step] = len(res["r"][0]) if "r" in res else 0
print("TM2: surviving length of a 300-nt all-Q40 read:", got, "->", "affected" if any(v != 300 for v in got.values()) else "unaffected")
