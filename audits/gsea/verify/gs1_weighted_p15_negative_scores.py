#!/usr/bin/env python3
"""GS1: under `-scoring_scheme weighted_p1.5`, a gene-set member with a *negative* ranking
metric contributes a hit weight of 1e-6 instead of |r|^1.5 / N_R.

`GeneSetScoringTables.WeightedOnePointFive.getHitScore` computes `Math.pow(score, 1.5)`
without an absolute value; for score < 0 that is NaN and the code substitutes 0.000001f.
The normaliser N_R, computed in the constructor, does use |score|^1.5.  The result: the
running sum for a set enriched at the bottom of the list barely rises at its hits, so its
ES collapses towards zero (or towards the miss penalty), and any set with members on the
negative side is mis-scored.  weighted_p2 (score*score) and weighted (|score|) are fine.

The harness runs GSEAPreranked on a synthetic list (half the genes negative) with sets
planted at the top, at the bottom and split, under weighted_p1.5, weighted_p2 and
weighted, and compares the ES with the port's |r|^p definition.
Usage: gs1_weighted_p15_negative_scores.py [build]     (master, v4.4.0, v4.3.2, v4.1.0, v4.0.3)
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C
import gsea_port as P

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
C.banner("GS1: weighted_p1.5 hit weights for negative scores", BUILD)
W = os.path.join(C.SCRATCH, "gs1", BUILD)
os.makedirs(W, exist_ok=True)

rng = np.random.default_rng(7)
N = 3000
names = ["g%04d" % i for i in range(N)]
scores = C.strictly_decreasing(rng.normal(0, 1, N))   # no ties, also after GSEA reads them as float32
C.write_rnk(os.path.join(W, "list.rnk"), names, scores)
sets = {  # GSEA upper-cases gene-set names in its reports
    "TOP_40": names[:40],
    "TOP_100_spread": names[0:600:6],
    "BOTTOM_40": names[-40:],
    "BOTTOM_100_spread": names[N - 600::6],
    "SPLIT_20_20": names[:20] + names[-20:],
    "NEG_SIDE_RANDOM_80": list(rng.choice(names[N // 2:], 80, replace=False)),
    "POS_SIDE_RANDOM_80": list(rng.choice(names[: N // 2], 80, replace=False)),
    "RANDOM_100": list(rng.choice(names, 100, replace=False)),
}
sets = {k.upper(): v for k, v in sets.items()}
C.write_gmt(os.path.join(W, "sets.gmt"), sets)
print("list: %d genes, %d with score < 0 (ranks %d..%d)" % (N, (scores < 0).sum(), int(np.argmax(scores < 0)), N - 1))

for scheme, p in (("weighted_p1.5", 1.5), ("weighted_p2", 2.0), ("weighted", 1.0)):
    r = C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "sets.gmt"),
                        os.path.join(W, "out_" + scheme), label=scheme, scoring_scheme=scheme, nperm=1000)
    assert r.ok(), r.error()
    print("\n== %s (p = %.1f): ES shipped vs port |r|^p, then NES / nominal p / FDR as reported" % (scheme, p))
    print("   %-20s %10s %10s %9s | %8s %8s %8s" % ("set", "GSEA ES", "port ES", "diff", "NES", "NOM p", "FDR q"))
    worst = 0.0
    for nm, genes in sets.items():
        es_port, _ = P.enrichment_score(scores, P.hit_mask(names, genes), p)
        row = r.rows[nm]
        d = row["es"] - es_port
        worst = max(worst, abs(d))
        print("   %-20s %10.5f %10.5f %9.5f | %8.3f %8.3f %8.3f" % (nm, row["es"], es_port, d, row["nes"], row["np"], row["fdr"]))
    print("   max |GSEA - port| = %.2e  -> %s" % (worst, "AFFECTED" if worst > 1e-3 else "unaffected"))

# what the shipped weights are, spelled out for BOTTOM_40 under p = 1.5
genes = sets["BOTTOM_40"]
hm = P.hit_mask(names, genes)
w = np.abs(scores[hm]) ** 1.5
print("\nBOTTOM_40 under weighted_p1.5: N_R = sum |r|^1.5 over hits = %.4f; per-hit weights should be %.4f..%.4f;"
      % (w.sum(), (w / w.sum()).min(), (w / w.sum()).max()))
print("with the shipped 1e-6 per hit the 40 hits add %.2e in total, while %d misses subtract %.4f each"
      % (40 * 1e-6, N - 40, 1.0 / (N - 40)))
print("\nDONE")
