#!/usr/bin/env python3
"""TM1 — ILLUMINACLIP palindrome mode charges int(Q/10) per mismatch instead of Q/10.

The manual ("The Adapter Fasta"): "Each matching base adds just over 0.6, while each
mismatch reduces the alignment score by Q/10." Simple mode does that in floating point
(IlluminaClippingTrimmer.java:556, `-quals[recPos] / 10.0f`); palindrome mode divides two
ints (`:494`, `:496`, `-qual1 / 10`), so a mismatch at Q9 costs nothing, at Q19 costs 1
instead of 1.9, at Q39 costs 3 instead of 3.9. This harness runs the shipped build on
synthetic read pairs whose insert, mismatch positions and qualities are known and compares
the clip decision with the documented rule and with a port of the integer rule.

Usage: python3 tm1_palindrome_penalty.py <trimmomatic.jar | build-dir> [adapters-dir]
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_ref as T

build = T.build_from_arg(sys.argv[1])
adir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(sys.argv[1].rstrip("/")), "adapters")
AD = os.path.join(adir, "TruSeq3-PE.fa")
P1, P2 = dict(T.load_fasta(AD))["PrefixPE/1"], dict(T.load_fasta(AD))["PrefixPE/2"]
STEP = "ILLUMINACLIP:%s:2:30:10" % AD
print("build:", " ".join(build)); print("adapters:", AD, "prefix lengths", len(P1), len(P2))

def make_pair(rng, R, L, mism):
    """mism: list of (read1 position within the fragment, quality) for read-1 errors."""
    frag = T.rand_seq(rng, L)
    r1 = (frag + T.revcomp(P2) + T.rand_seq(rng, R))[:R]
    r2 = (T.revcomp(frag) + T.revcomp(P1) + T.rand_seq(rng, R))[:R]
    q1, q2 = [40] * R, [40] * R
    r1 = list(r1)
    for p, q in mism:
        r1[p] = T.mutate(rng, r1[p]); q1[p] = q
    return "".join(r1), q1, r2, q2

def decisions(res, names):
    out = {}
    for n in names:
        if n in res["1P"]: out[n] = ("both", len(res["1P"][n][0]), len(res["2P"][n][0]))
        elif n in res["1U"]: out[n] = ("fwd-only", len(res["1U"][n][0]), 0)
        elif n in res["2U"]: out[n] = ("rev-only", 0, len(res["2U"][n][0]))
        else: out[n] = ("dropped", 0, 0)
    return out

# ---------------------------------------------------------------- A. one pair, the MCVE
rng = random.Random(1)
R, L = 50, 42
r1, q1, r2, q2 = make_pair(rng, R, L, [(3, 19), (8, 19)])
sd, n = T.palindrome_score(r1, q1, r2, q2, P1, P2, L, "doc")
sc, _ = T.palindrome_score(r1, q1, r2, q2, P1, P2, L, "code")
print("\nA. 2x%d pair, insert %d, two read-1 mismatches at Q19: aligned bases %d" % (R, R and L, n))
print("   documented score = %.3f (< 30: keep both reads untouched)" % sd)
print("   integer-penalty score = %.3f (>= 30: clip read 1 to %d, drop read 2)" % (sc, L))
res, log, d = T.run_pe(build, [("mcve", r1, q1)], [("mcve", r2, q2)], [STEP])
print("   shipped:", decisions(res, ["mcve"])["mcve"], "|", T.summary_line(log, True))
print("   documented rule ->", T.palindrome_clip(r1, q1, r2, q2, P1, P2, 2, 30),
      " integer rule ->", T.palindrome_clip(r1, q1, r2, q2, P1, P2, 2, 30, penalty="code"))

# ---------------------------------------------------------------- B. grid over mismatch quality and count
print("\nB. 2x50 pairs, insert 42 (58 aligned bases; columns: documented score, integer-penalty score, clip decision of each rule and of the shipped build, 200 pairs per row):")
print("   %-6s %-3s %-9s %-9s %-14s %-14s %s" % ("Qmm", "m", "doc", "int", "doc-rule", "int-rule", "shipped (200 pairs each)"))
rows = []
reads1, reads2, meta = [], [], []
for qmm in (2, 9, 10, 15, 19, 20, 25, 29, 30, 35, 39, 40):
    for m in (1, 2, 3):
        for k in range(200):
            rng = random.Random(1000 * qmm + 10 * m + k)
            pos = rng.sample(range(0, 18), m)          # fragment positions, away from the seed window
            r1, q1, r2, q2 = make_pair(rng, 50, 42, [(p, qmm) for p in pos])
            name = "q%d_m%d_%d" % (qmm, m, k)
            reads1.append((name, r1, q1)); reads2.append((name, r2, q2)); meta.append((qmm, m, name, r1, q1, r2, q2))
res, log, d = T.run_pe(build, reads1, reads2, [STEP])
dec = decisions(res, [x[2] for x in meta])
from collections import defaultdict
agg = defaultdict(lambda: [0, 0, 0, 0, 0.0, 0.0])
for qmm, m, name, r1, q1, r2, q2 in meta:
    sd, _ = T.palindrome_score(r1, q1, r2, q2, P1, P2, 42, "doc")
    sc, _ = T.palindrome_score(r1, q1, r2, q2, P1, P2, 42, "code")
    ddoc = T.palindrome_clip(r1, q1, r2, q2, P1, P2, 2, 30) is not None
    dint = T.palindrome_clip(r1, q1, r2, q2, P1, P2, 2, 30, penalty="code") is not None
    ship = dec[name][0] != "both"
    a = agg[(qmm, m)]
    a[0] += ddoc; a[1] += dint; a[2] += ship; a[3] += (ship == dint); a[4] = sd; a[5] = sc
disagree_total = 0
for (qmm, m), a in sorted(agg.items()):
    flag = " <-- differs" if a[0] != a[2] else ""
    print("   Q%-4d %-3d %-9.2f %-9.2f clip %-4d/200 clip %-4d/200 clip %-4d/200, =int %d/200%s" % (qmm, m, a[4], a[5], a[0], a[1], a[2], a[3], flag))
    disagree_total += abs(a[0] - a[2])
print("   pairs where the shipped decision differs from the documented rule:", disagree_total, "of", len(meta))

# ---------------------------------------------------------------- C. simulation with an Illumina-like quality profile
def sim_pairs(rng, R, npairs, ins_lo, ins_hi):
    reads1, reads2, meta = [], [], []
    for k in range(npairs):
        L = rng.randint(ins_lo, ins_hi)
        frag = T.rand_seq(rng, L)
        t1 = (frag + T.revcomp(P2) + T.rand_seq(rng, R))[:R]
        t2 = (T.revcomp(frag) + T.revcomp(P1) + T.rand_seq(rng, R))[:R]
        out = []
        for t in (t1, t2):
            seq, quals = list(t), []
            for i in range(R):
                # quality decays along the read; binned like a NovaSeq/HiSeq run
                base_q = rng.choice([37, 37, 37, 32, 27, 22, 14, 11, 2]) if i > R * 0.6 else rng.choice([40, 40, 37, 37, 37, 32, 27])
                quals.append(base_q)
                if rng.random() < 10 ** (-base_q / 10.0):
                    seq[i] = T.mutate(rng, seq[i])
            out.append(("".join(seq), quals))
        name = "s%d" % k
        reads1.append((name, out[0][0], out[0][1])); reads2.append((name, out[1][0], out[1][1]))
        meta.append((name, L))
    return reads1, reads2, meta

print("\nC. simulated libraries (insert uniform, per-base error rate 10^(-Q/10)):")
for R, lo, hi, npairs in ((50, 20, 70, 4000), (75, 20, 95, 4000), (100, 20, 120, 4000), (150, 20, 170, 3000)):
    rng = random.Random(R)
    reads1, reads2, meta = sim_pairs(rng, R, npairs, lo, hi)
    res, log, d = T.run_pe(build, reads1, reads2, [STEP])
    dec = decisions(res, [m[0] for m in meta])
    r1d = {n: (s, q) for n, s, q in reads1}; r2d = {n: (s, q) for n, s, q in reads2}
    n_doc = n_int = n_ship = n_ship_eq_int = n_ship_eq_doc = n_flip = 0
    flips = []
    for name, L in meta:
        s1, q1 = r1d[name]; s2, q2 = r2d[name]
        ddoc = T.palindrome_clip(s1, q1, s2, q2, P1, P2, 2, 30)
        dint = T.palindrome_clip(s1, q1, s2, q2, P1, P2, 2, 30, penalty="code")
        ship = dec[name]
        shipclip = None if ship[0] == "both" and ship[1] == R and ship[2] == R else ship[1]
        n_doc += ddoc is not None; n_int += dint is not None; n_ship += shipclip is not None
        n_ship_eq_int += (shipclip == dint); n_ship_eq_doc += (shipclip == ddoc)
        if (ddoc is None) != (dint is None):
            n_flip += 1; flips.append((name, L, ddoc, dint, shipclip))
    print("   2x%-4d %d pairs: clipped by documented rule %d, by integer rule %d, by shipped %d; shipped == integer port %d/%d, == documented %d/%d; decision flips doc vs int %d"
          % (R, npairs, n_doc, n_int, n_ship, n_ship_eq_int, npairs, n_ship_eq_doc, npairs, n_flip))
    for f in flips[:3]:
        print("      e.g.", f)
