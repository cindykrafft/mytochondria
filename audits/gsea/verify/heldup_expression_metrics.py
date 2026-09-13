#!/usr/bin/env python3
"""Held-up check: the expression-based `Gsea` tool's ranking metrics and its two
permutation nulls against the port, on synthetic data with planted signal.

A. Ranking metrics on a 3,000-gene x (8 vs 10)-sample dataset: Signal2Noise (default),
   tTest, Ratio_of_Classes, log2_Ratio_of_Classes, Diff_of_Classes, and Signal2Noise with
   `-median true`.  The ranked-gene-list file's SCORE column vs the port, including
   150 planted low-variance genes that exercise the documented minimum-sigma rule
   (sigma >= 0.2 * |mean|, or 0.2 when the mean is 0) and 30 genes with a zero mean.
B. Gene-set permutation on that dataset: ES of the report vs the port on the same
   ranked list; NES / p / FWER / FDR recomputed from the program's RND_ES.
C. Phenotype permutation: the null is a relabelling of samples that keeps class sizes.
   On null data (no signal, 8 vs 10, 100 random sets, 1,000 permutations) the fraction of
   sets with nominal p < 0.05 and the KS distance of the p-values from uniform; on the
   signal dataset the planted sets come out with the expected signs.
"""
import os
import sys

import numpy as np
from scipy import stats as sps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C
import gsea_port as P

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
C.banner("heldup_expression_metrics: ranking metrics, gene-set and phenotype permutation", BUILD)
W = os.path.join(C.SCRATCH, "heldup_expr", BUILD)
os.makedirs(W, exist_ok=True)

rng = np.random.default_rng(31)
G, nA, nB = 3000, 8, 10
names = ["G%04d" % i for i in range(G)]
samples = ["A%d" % i for i in range(nA)] + ["B%d" % i for i in range(nB)]
labels = ["A"] * nA + ["B"] * nB
X = rng.lognormal(mean=5, sigma=0.6, size=(G, nA + nB))          # positive expression values
# planted signal: 100 genes up in A, 100 genes down in A
up, down = list(range(0, 100)), list(range(100, 200))
X[up, :nA] *= 2.5
X[down, :nA] /= 2.5
# low-variance genes (the minimum-sigma rule bites): 150 genes with tiny spread
lowvar = list(range(200, 350))
X[lowvar] = 100.0 + rng.normal(0, 0.5, size=(150, nA + nB))
X[lowvar[:50], :nA] += 3.0
# zero-mean genes (centred data, as after per-gene standardisation)
zeromean = list(range(350, 380))
X[zeromean] = rng.normal(0, 1e-3, size=(30, nA + nB))
X[zeromean] -= X[zeromean].mean(axis=1, keepdims=True)
X[zeromean[:10], :nA] += 0.5
X[zeromean[:10], nA:] -= 0.4
X = np.round(X, 5)
C.write_gct(os.path.join(W, "data.gct"), names, samples, X)
C.write_cls(os.path.join(W, "data.cls"), labels)

sets = {"UP_IN_A": names[0:100:2], "DOWN_IN_A": names[100:200:2], "LOWVAR_SHIFTED": names[200:250],
        "LOWVAR_FLAT": names[250:350], "ZEROMEAN": names[350:380]}
for k in range(20):
    n = int(rng.integers(15, 200))
    sets["RANDOM_%02d" % k] = list(rng.choice(names, n, replace=False))
C.write_gmt(os.path.join(W, "sets.gmt"), sets)

A, B = X[:, :nA], X[:, nA:]
port_metric = {
    "Signal2Noise": lambda a, b: P.signal2noise(a, b),
    "tTest": lambda a, b: P.ttest(a, b),
    "Ratio_of_Classes": lambda a, b: P.ratio_of_classes(a, b),
    "log2_Ratio_of_Classes": lambda a, b: P.log2_ratio_of_classes(a, b),
    "Diff_of_Classes": lambda a, b: P.diff_of_classes(a, b),
}


def median_s2n(a, b):
    return (np.median(a) - np.median(b)) / (P._sd(a) + P._sd(b))


# ------------------------------------------------------------------ A. metrics
print("\n== A. ranked-list SCORE vs port (max |diff| over %d genes; ranking order compared as a permutation)" % G)
print("   %-24s %12s %12s %8s   %s" % ("metric", "max|diff|", "max rel", "order", "example low-variance gene"))
runs = {}
for metric, fn in list(port_metric.items()) + [("Signal2Noise -median", median_s2n)]:
    params = dict(metric=metric.split()[0], nperm=100, permute="gene_set")
    if "median" in metric:
        params["median"] = "true"
    r = C.run_gsea(BUILD, os.path.join(W, "data.gct"), os.path.join(W, "data.cls"), os.path.join(W, "sets.gmt"),
                   os.path.join(W, "out_" + metric.replace(" -", "_")), label="m", **params)   # no "-" in paths
    assert r.ok(), r.error()
    runs[metric] = r
    got = dict(r.ranked)
    exp = {names[i]: fn(A[i], B[i]) for i in range(G)}
    both_nan = sum(1 for n in names if np.isnan(got[n]) and np.isnan(exp[n]))
    one_nan = sum(1 for n in names if np.isnan(got[n]) != np.isnan(exp[n]))
    d = np.array([got[n] - exp[n] for n in names if not np.isnan(exp[n])])
    rel = np.array([abs(got[n] - exp[n]) / max(abs(exp[n]), 1e-12) for n in names if not np.isnan(exp[n])])
    # the list is ordered by GSEA's float32 scores; accept it if the port's scores are non-increasing along it
    # up to 1e-6 (near-ties among the flat genes are ordered by float rounding)
    along = np.array([exp[n] for n, _ in r.ranked if not np.isnan(exp[n])])
    order_ok = (np.diff(along) <= 1e-6).all()
    i = lowvar[60]
    print("   %-24s %12.2e %12.2e %8s   %s: GSEA %.5f port %.5f (sd_A %.3f sd_B %.3f, 0.2|mean| = %.2f)%s"
          % (metric, np.abs(d).max(), rel.max(), "same" if order_ok else "DIFFERS", names[i], got[names[i]],
             exp[names[i]], A[i].std(ddof=1), B[i].std(ddof=1), 0.2 * abs(A[i].mean()),
             "" if not (both_nan or one_nan) else "  [NaN in both: %d, in one only: %d]" % (both_nan, one_nan)))
i = zeromean[20]
print("   zero-mean gene %s under Signal2Noise: GSEA %.5f, port %.5f (mean_A %.1e; floor sigma = 0.2)"
      % (names[i], dict(runs["Signal2Noise"].ranked)[names[i]], P.signal2noise(A[i], B[i]), A[i].mean()))

# ------------------------------------------------------------------ B. gene-set permutation on the ranked list
print("\n== B. gene-set permutation (Signal2Noise, weighted, 1000 perms): ES vs port; NES/p/FWER/FDR from RND_ES")
r = C.run_gsea(BUILD, os.path.join(W, "data.gct"), os.path.join(W, "data.cls"), os.path.join(W, "sets.gmt"),
               os.path.join(W, "out_gs"), label="gs", nperm=1000, permute="gene_set")
assert r.ok(), r.error()
rl_names = [n for n, _ in r.ranked]
rl_scores = np.array([s for _, s in r.ranked])
dmax = 0.0
for nm, genes in sets.items():
    es_port, _ = P.enrichment_score(rl_scores, P.hit_mask(rl_names, genes), 1.0)
    dmax = max(dmax, abs(r.rows[nm]["es"] - es_port))
print("   max |ES GSEA - port| over %d sets: %.2e" % (len(sets), dmax))
order = list(r.edb)
null = np.array([r.edb[n]["rnd_es"] for n in order])
es_full = np.array([r.rows[n]["es"] for n in order])
nes_port = np.array([P.nes(es_full[i], null[i]) for i in range(len(order))])
null_nes = np.array([P.nes_null(null[i]) for i in range(len(order))])
print("   max|NES diff| %.2e  max|p diff| %.2e  max|FWER diff| %.2e  max|FDR diff| (per-permutation formula) %.2e"
      % (np.nanmax(np.abs(nes_port - [r.rows[n]["nes"] for n in order])),
         np.nanmax(np.abs([P.nominal_p(es_full[i], null[i]) for i in range(len(order))] - np.array([r.rows[n]["np"] for n in order]))),
         np.nanmax(np.abs([P.fwer(nes_port[i], null_nes) for i in range(len(order))] - np.array([r.rows[n]["fwer"] for n in order]))),
         np.nanmax(np.abs(P.fdr_per_permutation(nes_port, null_nes) - np.array([r.rows[n]["fdr"] for n in order])))))
for nm in ("UP_IN_A", "DOWN_IN_A", "LOWVAR_SHIFTED", "LOWVAR_FLAT", "ZEROMEAN"):
    print("   %-16s ES %8.4f NES %7.3f p %.3f FDR %.3f" % (nm, r.rows[nm]["es"], r.rows[nm]["nes"], r.rows[nm]["np"], r.rows[nm]["fdr"]))

# ------------------------------------------------------------------ C. phenotype permutation
print("\n== C. phenotype permutation (Signal2Noise, 1000 perms)")
r = C.run_gsea(BUILD, os.path.join(W, "data.gct"), os.path.join(W, "data.cls"), os.path.join(W, "sets.gmt"),
               os.path.join(W, "out_ph"), label="ph", nperm=1000, permute="phenotype")
assert r.ok(), r.error()
order = list(r.edb)
null = np.array([r.edb[n]["rnd_es"] for n in order])
es_full = np.array([r.rows[n]["es"] for n in order])
nes_port = np.array([P.nes(es_full[i], null[i]) for i in range(len(order))])
null_nes = np.array([P.nes_null(null[i]) for i in range(len(order))])
print("   signal data: max|NES diff| %.2e  max|p diff| %.2e  max|FDR diff| %.2e"
      % (np.nanmax(np.abs(nes_port - [r.rows[n]["nes"] for n in order])),
         np.nanmax(np.abs([P.nominal_p(es_full[i], null[i]) for i in range(len(order))] - np.array([r.rows[n]["np"] for n in order]))),
         np.nanmax(np.abs(P.fdr_per_permutation(nes_port, null_nes) - np.array([r.rows[n]["fdr"] for n in order])))))
for nm in ("UP_IN_A", "DOWN_IN_A", "LOWVAR_SHIFTED", "LOWVAR_FLAT"):
    print("   %-16s ES %8.4f NES %7.3f p %.3f FDR %.3f FWER %.3f" % (nm, r.rows[nm]["es"], r.rows[nm]["nes"], r.rows[nm]["np"], r.rows[nm]["fdr"], r.rows[nm]["fwer"]))
# the same-ES-under-relabelling property: a permutation null column is an ES of the real sets on a relabelled dataset;
# check one thing the port can compute exactly: the null ES of a set is bounded like an ES (|ES| <= 1)
print("   null ES range over all sets and permutations: [%.3f, %.3f]" % (null.min(), null.max()))

# null data calibration
Xn = np.round(rng.lognormal(mean=5, sigma=0.6, size=(G, nA + nB)), 5)
C.write_gct(os.path.join(W, "null.gct"), names, samples, Xn)
nsets = {"RND_%03d" % k: list(rng.choice(names, int(rng.integers(15, 200)), replace=False)) for k in range(100)}
C.write_gmt(os.path.join(W, "null_sets.gmt"), nsets)
for permute in ("phenotype", "gene_set"):
    r = C.run_gsea(BUILD, os.path.join(W, "null.gct"), os.path.join(W, "data.cls"), os.path.join(W, "null_sets.gmt"),
                   os.path.join(W, "out_null_" + permute), label="n", nperm=1000, permute=permute)
    assert r.ok(), r.error()
    pv = np.array([r.rows[n]["np"] for n in nsets])
    ks = sps.kstest(pv, "uniform")
    print("   null data, %-10s: %d sets, p<0.05 in %d (%.3f), p<0.25 in %d (%.3f), KS D=%.3f p=%.2f, FDR<0.25 in %d"
          % (permute, len(pv), (pv < 0.05).sum(), (pv < 0.05).mean(), (pv < 0.25).sum(), (pv < 0.25).mean(), ks.statistic, ks.pvalue,
             sum(r.rows[n]["fdr"] < 0.25 for n in nsets)))
print("\nDONE")
