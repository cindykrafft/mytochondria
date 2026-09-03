#!/usr/bin/env python3
"""Held-up check: --indep-pairwise and --r2 / --ld against numpy.

r^2 reference: squared Pearson correlation of the 0/1/2 genotype vectors over
samples non-missing at BOTH variants (pairwise-complete), which is what both
versions document for --indep-pairwise and for --r2 on unphased hard calls.
Pruning reference: an independent port of the documented greedy window scan
(window of W variants, step S, remove the variant with the smaller MAF of each
pair with r^2 > t, then slide) run on the same r^2 matrix.
"""
import os, sys, tempfile, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import write_pedmap, run, read_table, fnum, PLINK19, PLINK2, version

rng = np.random.default_rng(11)
n, m = 400, 120
# correlated genotypes: haplotype blocks
hap = (rng.random((2 * n, m)) < 0.3).astype(np.int8)
for j in range(1, m):
    keep = rng.random(2 * n) < 0.85
    hap[keep, j] = hap[keep, j - 1] if j % 7 else hap[keep, j]
g = (hap[0::2] + hap[1::2]).astype(np.int8)
g[rng.random((n, m)) < 0.04] = -1
obs = g >= 0

def r2(i, j):
    k = obs[:, i] & obs[:, j]
    x, y = g[k, i].astype(float), g[k, j].astype(float)
    if x.std() == 0 or y.std() == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1] ** 2)

R2 = np.full((m, m), np.nan)
for i in range(m):
    for j in range(i + 1, m):
        R2[i, j] = R2[j, i] = r2(i, j)
alt_ct = np.where(obs, g, 0).sum(0); nm2 = 2 * obs.sum(0)
freq = alt_ct / nm2
maf = np.minimum(freq, 1 - freq)

def prune(W, S, t):
    """Port of the documented --indep-pairwise scan (variant-count window)."""
    removed = np.zeros(m, bool)
    start = 0
    while True:
        end = min(start + W, m)
        changed = True
        while changed:
            changed = False
            for i in range(start, end):
                if removed[i]:
                    continue
                for j in range(i + 1, end):
                    if removed[j]:
                        continue
                    v = R2[i, j]
                    if v == v and v > t:
                        # remove the one with the smaller MAF; tie -> the later one (both versions)
                        drop = i if maf[i] < maf[j] else j
                        removed[drop] = True
                        changed = True
                        if drop == i:
                            break
        if end == m:
            break
        start += S
    return removed

print(version(PLINK19)); print(version(PLINK2))
with tempfile.TemporaryDirectory() as tmp:
    pre = write_pedmap(os.path.join(tmp, "d"), g)
    for W, S, t in ((50, 5, 0.5), (50, 5, 0.2), (20, 10, 0.8), (100, 25, 0.4)):
        ref = prune(W, S, t)
        for label, exe, args, fn in (
            ("plink 1.9", PLINK19, ["--file", pre, "--indep-pairwise", str(W), str(S), str(t), "--out", os.path.join(tmp, "p19")], os.path.join(tmp, "p19.prune.out")),
            ("plink2", PLINK2, ["--pedmap", pre, "--indep-pairwise", str(W), str(S), str(t), "--out", os.path.join(tmp, "p2")], os.path.join(tmp, "p2.prune.out")),
        ):
            run(exe, args)
            out = {int(l.strip()[3:]) - 1 for l in open(fn) if l.strip()}
            refset = {i for i in range(m) if ref[i]}
            print(f"--indep-pairwise {W} {S} {t} {label:10s}: pruned {len(out)}, port {len(refset)}, symmetric difference {len(out ^ refset)}")
    # --r2 values: plink 1.9 --r2 inter-chr with all pairs; plink2 --r2-unphased
    run(PLINK19, ["--file", pre, "--r2", "inter-chr", "--ld-window-r2", "0", "--out", os.path.join(tmp, "r19")])
    t = read_table(os.path.join(tmp, "r19.ld"))
    worst = 0.0; nn = 0
    for a, b, v in zip(t["SNP_A"], t["SNP_B"], t["R2"]):
        i, j = int(a[3:]) - 1, int(b[3:]) - 1
        if R2[i, j] == R2[i, j]:
            worst = max(worst, abs(fnum(v) - R2[i, j])); nn += 1
    print(f"plink 1.9 --r2 inter-chr: {nn} pairs, max |R2 - numpy pairwise-complete r2| = {worst:.2e} (6 s.f. printed)")
    r = run(PLINK2, ["--pedmap", pre, "--r2-unphased", "inter-chr", "--ld-window-r2", "0", "--out", os.path.join(tmp, "r2")], check=False)
    fn = os.path.join(tmp, "r2.vcor")
    if r.returncode == 0 and os.path.exists(fn):
        t = read_table(fn)
        worst = 0.0; nn = 0
        for a, b, v in zip(t["ID_A"], t["ID_B"], t["UNPHASED_R2"]):
            i, j = int(a[3:]) - 1, int(b[3:]) - 1
            if R2[i, j] == R2[i, j]:
                worst = max(worst, abs(fnum(v) - R2[i, j])); nn += 1
        print(f"plink2 --r2-unphased inter-chr: {nn} pairs, max |UNPHASED_R2 - numpy r2| = {worst:.2e}")
    else:
        print("plink2 --r2-unphased:", (r.stderr + r.stdout).strip().splitlines()[-1])
    # --ld on one pair (both)
    i, j = 3, 4
    r = run(PLINK19, ["--file", pre, "--ld", f"snp{i+1}", f"snp{j+1}", "--out", os.path.join(tmp, "l19")], check=False)
    line = [l for l in r.stdout.splitlines() if "R-sq" in l]
    print(f"plink 1.9 --ld snp{i+1} snp{j+1}: {line[0].strip() if line else 'n/a'}   numpy r2 = {R2[i, j]:.6f}")
    r = run(PLINK2, ["--pedmap", pre, "--ld", f"snp{i+1}", f"snp{j+1}", "--out", os.path.join(tmp, "l2")], check=False)
    line = [l for l in r.stdout.splitlines() if "r^2" in l]
    print(f"plink2 --ld snp{i+1} snp{j+1}: {line[0].strip() if line else 'n/a'}   numpy r2 = {R2[i, j]:.6f}")
