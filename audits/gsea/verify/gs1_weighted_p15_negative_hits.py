#!/usr/bin/env python3
"""GS1: under the `weighted_p1.5` scoring scheme, a hit with a negative rank metric adds
(almost) nothing to the running sum.

GeneSetScoringTables.WeightedOnePointFive.getHitScore (master dc35c76, line 228) computes
Math.pow(score, 1.5) on the signed score: for a negative score that is NaN, the hit score
becomes 0.000001, while the normalising total (line 210) uses Math.pow(Math.abs(score), 1.5).
So for a set whose members sit in the negative half of the list the running sum only ever
descends: ES -> about -1 and the ES peak moves to the end of the list.

Truth: the paper's ES with p = 1.5 uses |r_j|^p for every hit (ref_gsea.enrichment_score).
The same list under `weighted` (p = 1) and `weighted_p2` (p = 2, score*score) is fine.

Synthetic data: 8,000 normal scores; DOWN_MID = 40 genes drawn from ranks 6,500-7,500
(negative scores, not at the very bottom, so the true |ES| is well below 1); UP_MID the
mirror image; MIXED = 20 top + 20 bottom genes.
Run: python3 gs1_weighted_p15_negative_hits.py   (GSEA_CP selects the jar)
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsea_cli as G  # noqa: E402
import ref_gsea as R  # noqa: E402
import synth  # noqa: E402

W = "/tmp/gseawork/gs1_p15"
os.makedirs(W, exist_ok=True)
names, sc, rng = synth.ranked_list(N=8000, seed=3)
N = len(names)
gs = {
    "DOWN_MID": list(rng.choice(names[6500:7500], 40, replace=False)),
    "UP_MID": list(rng.choice(names[500:1500], 40, replace=False)),
    "MIXED": list(rng.choice(names[:300], 20, replace=False)) + list(rng.choice(names[-300:], 20, replace=False)),
    "RANDOM": list(rng.choice(names, 60, replace=False)),
}
G.write_rnk(f"{W}/list.rnk", names, sc)
G.write_gmt(f"{W}/sets.gmt", gs)
print("jar/classpath:", G.GSEA_CP)
print(f"N = {N}; scores of DOWN_MID members: max = {sc[np.isin(names, gs['DOWN_MID'])].max():.3f} (all negative)")

fails = 0
for scheme, p in (("weighted", 1.0), ("weighted_p2", 2.0), ("weighted_p1.5", 1.5)):
    d = G.run_preranked(f"{W}/list.rnk", f"{W}/sets.gmt", f"{W}/out_{scheme}", nperm=100,
                        extra=["-scoring_scheme", scheme])
    edb = G.parse_edb(d)
    tsv = G.parse_report_tsv(d)
    print(f"\nscheme = {scheme} (p = {p})")
    for k in gs:
        es_ref, i_ref, _ = R.enrichment_score(sc, np.isin(names, gs[k]), p)
        es_g = float(tsv[k]["ES"])
        i_g = edb[k]["rank_at_es"]
        ok = abs(es_g - es_ref) < 1e-4 and i_g == i_ref
        fails += (not ok)
        print(f"  {k:9s} ES gsea = {es_g:8.4f}  ES ref = {es_ref:8.4f}  rank-at-ES gsea = {i_g:5d} ref = {i_ref:5d}  "
              f"NES = {float(tsv[k]['NES']):7.3f}  {'ok' if ok else 'MISMATCH'}")
print("\nmismatching (scheme, set) pairs:", fails)
