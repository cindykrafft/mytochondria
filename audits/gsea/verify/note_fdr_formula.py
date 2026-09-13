#!/usr/bin/env python3
"""NOTE: the FDR q-value numerator is a mean of per-permutation fractions, not the pooled
fraction the paper states; and the nominal p counts strictly more extreme null values
while the FDR numerator counts ties.

Subramanian 2005 (Methods, 'Multiple hypothesis testing'): for NES* >= 0 the FDR is
'the ratio of the percentage of all (S, pi) with NES(S, pi) >= 0, whose NES(S, pi) >=
NES*, divided by the percentage of observed S with NES(S) >= 0, whose NES(S) >= NES*'.
GSEA (`SkewCorrectedFdrStruc`) computes, for each permutation column separately,
#{S: NES(S, pi) >= NES*} / #{S: NES(S, pi) >= 0}, and averages those fractions over the
columns (skipping columns with no positive value).  The two agree when every column has
the same number of positive NES values, and differ (slightly) otherwise.

Quantified here on GSEA's own null (RND_ES from edb/results.edb): a preranked run with
120 gene sets and 1,000 gene-set permutations.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C
import gsea_port as P

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
C.banner("note_fdr_formula: per-permutation vs pooled FDR numerator; strict nominal p", BUILD)
W = os.path.join(C.SCRATCH, "note_fdr", BUILD)
os.makedirs(W, exist_ok=True)

rng = np.random.default_rng(17)
N = 4000
names = ["g%04d" % i for i in range(N)]
scores = C.strictly_decreasing(np.concatenate([rng.normal(1.0, 0.5, 200), rng.normal(0, 0.5, N - 200)]))
C.write_rnk(os.path.join(W, "list.rnk"), names, scores)
sets = {}
for k in range(120):
    n = int(rng.integers(15, 300))
    if k < 20:      # planted, weakly: half the members from the top 300
        g = list(rng.choice(names[:300], n // 2, replace=False)) + list(rng.choice(names[300:], n - n // 2, replace=False))
    elif k < 30:
        g = list(rng.choice(names[-600:], n, replace=False))
    else:
        g = list(rng.choice(names, n, replace=False))
    sets["S%03d" % k] = g
C.write_gmt(os.path.join(W, "sets.gmt"), sets)
r = C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "sets.gmt"), os.path.join(W, "out"),
                    label="fdr", nperm=1000)
assert r.ok(), r.error()

order = list(r.edb)
null = np.array([r.edb[n]["rnd_es"] for n in order])
es = np.array([r.rows[n]["es"] for n in order])
nes = np.array([P.nes(es[i], null[i]) for i in range(len(order))])
null_nes = np.array([P.nes_null(null[i]) for i in range(len(order))])
rep_fdr = np.array([r.rows[n]["fdr"] for n in order])
rep_np = np.array([r.rows[n]["np"] for n in order])
q_perm = P.fdr_per_permutation(nes, null_nes)
q_pool = P.fdr_pooled(nes, null_nes)
npos = (null_nes >= 0).sum(axis=0)
print("sets: %d (%d with ES >= 0); positive NES per permutation column: min %d, median %d, max %d"
      % (len(order), (es >= 0).sum(), npos.min(), int(np.median(npos)), npos.max()))
print("report FDR vs port per-permutation formula: max |diff| %.2e (rounding of RND_ES to 4 dp)" % np.nanmax(np.abs(rep_fdr - q_perm)))
d = q_pool - q_perm
print("pooled (paper) minus per-permutation (GSEA): max |diff| %.4f, mean |diff| %.4f, over sets with q < 0.5: max %.4f"
      % (np.nanmax(np.abs(d)), np.nanmean(np.abs(d)), np.nanmax(np.abs(d[q_perm < 0.5])) if (q_perm < 0.5).any() else 0))
print("sets with FDR < 0.25: report %d, pooled %d; < 0.05: report %d, pooled %d"
      % ((rep_fdr < 0.25).sum(), (q_pool < 0.25).sum(), (rep_fdr < 0.05).sum(), (q_pool < 0.05).sum()))
worst = np.nanargmax(np.abs(d))
print("largest difference: %s NES %.3f, GSEA q %.4f, pooled q %.4f" % (order[worst], nes[worst], q_perm[worst], q_pool[worst]))

# nominal p: strict (GSEA) vs ties counted
p_strict = np.array([P.nominal_p(es[i], null[i], strict=True) for i in range(len(order))])
p_ties = np.array([P.nominal_p(es[i], null[i], strict=False) for i in range(len(order))])
print("\nnominal p: report vs strict count max |diff| %.2e; strict vs ties-counted max |diff| %.2e; sets with p = 0 exactly: %d of %d"
      % (np.nanmax(np.abs(rep_np - p_strict)), np.nanmax(np.abs(p_strict - p_ties)), (rep_np == 0).sum(), len(order)))
print("(with 1,000 permutations a strict count reports p = 0 rather than the 1/(n+1) floor some tools use; documented GSEA behaviour)")
print("\nDONE")
