#!/usr/bin/env python3
"""Held-up check: plink2 --make-king-table / --king-cutoff against a port of the
KING-robust estimator (Manichaikul et al. 2010, eq. 11), and plink 1.9 --genome
against a first-principles port of the PLINK 1.07 method-of-moments IBD
estimator (expected IBS-sharing probabilities for two individuals drawn without
replacement from the observed allele pool, Z0/Z1/Z2 by successive solution,
the documented clamping, PI_HAT = Z1/2 + Z2).

Data: unrelated founders plus planted parent-offspring, full-sib and
half-sib pairs (kinship 1/4, 1/4, 1/8; PI_HAT 1/2, 1/2, 1/4).
"""
import os, sys, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import write_pedmap, run, read_table, fnum, PLINK19, PLINK2, version

rng = np.random.default_rng(3)
m = 3000
p = rng.uniform(0.05, 0.5, m)
def founder():
    return (rng.random((2, m)) < p).astype(np.int8)     # two haplotypes
def child(a, b):
    return np.stack([a[rng.integers(0, 2, m), np.arange(m)], b[rng.integers(0, 2, m), np.arange(m)]])
haps = [founder() for _ in range(40)]
# relatives: 40,41 = parents of 42 and 43 (full sibs); 44 = child of 40 and 45 (half-sib of 42)
haps.append(founder())                        # 40
haps.append(founder())                        # 41
haps.append(child(haps[40], haps[41]))        # 42
haps.append(child(haps[40], haps[41]))        # 43
haps.append(founder())                        # 44 (unrelated mate)
haps.append(child(haps[40], haps[44]))        # 45 half-sib of 42/43, child of 40
n = len(haps)
g = np.stack([h.sum(0) for h in haps]).astype(np.int8)
g[rng.random((n, m)) < 0.02] = -1
obs = g >= 0

def king(i, j):
    k = obs[:, i] & obs[:, j]
    a, b = g[k, i], g[k, j]
    het_i, het_j = (a == 1).sum(), (b == 1).sum()
    hethet = ((a == 1) & (b == 1)).sum()
    ibs0 = ((a == 0) & (b == 2)).sum() + ((a == 2) & (b == 0)).sum()
    return 0.5 - (4 * ibs0 + (het_i - hethet) + (het_j - hethet)) / (4 * min(het_i, het_j))
    # == (hethet - 2 ibs0)/(2 min) + 1/2 - (het_i + het_j)/(4 min)

def genome_expectations():
    """Per-variant expected IBS-state probabilities under Z0 (e00,e01,e02) and Z1 (e11,e12),
    averaged over polymorphic variants with > 3 observed alleles (PLINK 1.07 preCalcGenomeIBD),
    written from first principles (sampling alleles without replacement)."""
    e = np.zeros(5); cnt = 0
    for j in range(m):
        k = obs[:, j]
        N = 2 * k.sum(); X = int(g[k, j].sum()); Y = N - X          # X = ALT copies
        if N <= 3 or X == 0 or Y == 0:
            continue
        d4 = N * (N - 1) * (N - 2) * (N - 3); d3 = N * (N - 1) * (N - 2)
        e00 = 2 * X * (X - 1) * Y * (Y - 1) / d4
        e01 = 4 * X * Y * ((X - 1) * (X - 2) + (Y - 1) * (Y - 2)) / d4
        e02 = (X * (X - 1) * (X - 2) * (X - 3) + Y * (Y - 1) * (Y - 2) * (Y - 3) + 4 * X * (X - 1) * Y * (Y - 1)) / d4
        e11 = 2 * X * Y * ((X - 1) + (Y - 1)) / d3
        e12 = (X * (X - 1) * (X - 2) + Y * (Y - 1) * (Y - 2) + X * (X - 1) * Y + Y * (Y - 1) * X) / d3
        e += (e00, e01, e02, e11, e12); cnt += 1
    return e / cnt

def genome(i, j, e):
    e00, e01, e02, e11, e12 = e
    k = obs[:, i] & obs[:, j]
    a, b = g[k, i], g[k, j]
    nn = k.sum()
    d = np.abs(a - b)
    ibs0, ibs1 = (d == 2).sum(), (d == 1).sum()
    ibs2 = nn - ibs0 - ibs1
    z0 = ibs0 / (e00 * nn)
    z1 = (ibs1 - z0 * e01 * nn) / (e11 * nn)
    z2 = (ibs2 - nn * (z0 * e02 + z1 * e12)) / nn
    if z0 > 1: z0, z1, z2 = 1, 0, 0
    elif z1 > 1: z1, z0, z2 = 1, 0, 0
    elif z2 > 1: z2, z1, z0 = 1, 0, 0
    elif z0 < 0:
        s = 1 / (z1 + z2); z1 *= s; z2 *= s; z0 = 0
    if z1 < 0:
        s = 1 / (z0 + z2); z0 *= s; z2 *= s; z1 = 0
    if z2 < 0:
        s = 1 / (z0 + z1); z0 *= s; z1 *= s; z2 = 0
    return z0, z1, z2, z1 / 2 + z2, ibs0, ibs1, ibs2

print(version(PLINK19)); print(version(PLINK2))
with tempfile.TemporaryDirectory() as tmp:
    pre = write_pedmap(os.path.join(tmp, "d"), g)
    run(PLINK2, ["--pedmap", pre, "--make-king-table", "--king-table-filter", "-1", "--out", os.path.join(tmp, "k")])
    t = read_table(os.path.join(tmp, "k.kin0"))
    worst = 0.0; nrow = 0
    for a, b, v in zip(t["IID1"], t["IID2"], t["KINSHIP"]):
        i, j = int(a[1:]) - 1, int(b[1:]) - 1
        worst = max(worst, abs(fnum(v) - king(i, j))); nrow += 1
    print(f"plink2 --make-king-table: {nrow} pairs, max |KINSHIP - KING-robust port| = {worst:.2e}")
    pairs = {("I41", "I43"): "parent-offspring", ("I43", "I44"): "full sibs", ("I43", "I46"): "half sibs", ("I1", "I2"): "unrelated"}
    for a, b, v in zip(t["IID1"], t["IID2"], t["KINSHIP"]):
        key = (a, b) if (a, b) in pairs else (b, a)
        if key in pairs:
            print(f"   {key[0]}-{key[1]} {pairs[key]:17s}: KINSHIP {fnum(v):+.4f}")
    run(PLINK2, ["--pedmap", pre, "--king-cutoff", "0.177", "--out", os.path.join(tmp, "kc")])
    removed = [l.split()[-1] for l in open(os.path.join(tmp, "kc.king.cutoff.out.id")) if not l.startswith("#")]
    print(f"plink2 --king-cutoff 0.177 removed {len(removed)} samples: {removed} (planted relatives: I41..I46; 1st-degree pairs I41-I43, I41-I44, I42-I43, I42-I44, I43-I44, I41-I46, I45-I46)")
    # --genome
    e = genome_expectations()
    run(PLINK19, ["--file", pre, "--genome", "--out", os.path.join(tmp, "g")])
    t = read_table(os.path.join(tmp, "g.genome"))
    worst = {c: 0.0 for c in ("Z0", "Z1", "Z2", "PI_HAT", "IBS0", "IBS1", "IBS2")}
    for r in range(len(t["IID1"])):
        i, j = int(t["IID1"][r][1:]) - 1, int(t["IID2"][r][1:]) - 1
        z0, z1, z2, pi, ibs0, ibs1, ibs2 = genome(i, j, e)
        for c, ref in zip(worst, (z0, z1, z2, pi, ibs0, ibs1, ibs2)):
            worst[c] = max(worst[c], abs(fnum(t[c][r]) - ref))
        key = (t["IID1"][r], t["IID2"][r])
        if key in pairs:
            print(f"   {key[0]}-{key[1]} {pairs[key]:17s}: Z0 {t['Z0'][r]} Z1 {t['Z1'][r]} Z2 {t['Z2'][r]} PI_HAT {t['PI_HAT'][r]}  (port: {z0:.4f} {z1:.4f} {z2:.4f} {pi:.4f})")
    print("plink 1.9 --genome: max |column - first-principles port| over all pairs:", {c: f"{v:.1e}" for c, v in worst.items()}, "(Z/PI_HAT printed to 4 decimals)")
