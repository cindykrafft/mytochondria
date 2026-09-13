#!/usr/bin/env python3
"""GS3: under the default weighted scheme, a gene set whose members present in the list all
have ranking score 0 is reported with a spurious, strongly negative ES/NES and p = 0.

With N_R = sum |r_j|^p = 0 the hit increment of the paper's P_hit is 0/0.  In
`GeneSetScoringTables.Weighted` the hit score is `|score| / totalWeight` = NaN, so in
`KSCore` the running sum becomes NaN at the first hit and every later `Math.abs(...) <
Math.abs(NaN)` comparison is false: the ES that survives is the running sum just before
the first hit, i.e. -(rank of the first member) / (N - N_H), a number that only says where
the block of zeros starts.  The permutation null is built from random sets with normal
weights, so this ES is far outside it: NES around -3, p = 0, FDR = 0, and the set is
listed among the most significant negative sets.  Nothing in the log or report flags it.

Realistic input: a preranked list from DESeq2/edgeR with untested genes given stat 0
(here 30 % of the genes), and a gene set of genes that are all unexpressed in the tissue
(all its present members scored 0).  `classic` (p = 0) is unaffected; the fgsea reference
also computes an order-dependent number for such a set but warns about the ties.
Usage: gs3_zero_weight_set.py [build]
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C
import gsea_port as P

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
C.banner("GS3: all-zero-score gene set under the weighted scheme", BUILD)
W = os.path.join(C.SCRATCH, "gs3", BUILD)
os.makedirs(W, exist_ok=True)

rng = np.random.default_rng(23)
NP_, NZ, NN = 2100, 1500, 1400                 # positive, zero, negative blocks
N = NP_ + NZ + NN
pos = C.strictly_decreasing(np.abs(rng.normal(0, 1.2, NP_)) + 0.001)
neg = -C.strictly_decreasing(np.abs(rng.normal(0, 1.2, NN)) + 0.001)[::-1]   # descending, like the list
scores = np.concatenate([pos, np.zeros(NZ), neg])
names = ["g%04d" % i for i in range(N)]
zero_names = names[NP_:NP_ + NZ]
C.write_rnk(os.path.join(W, "list.rnk"), names, scores)
sets = {
    "ALL_ZERO_20": zero_names[100:120],                                   # 20 members, all scored 0
    "ALL_ZERO_40_LATE": zero_names[1400:1440],                            # 40 members at the end of the zero block
    "ZERO_19_PLUS_1": zero_names[200:219] + [names[NP_ - 1]],             # one member with a small positive score
    "TOP_30": names[:30],
    "BOTTOM_30": names[-30:],
}
for k in range(15):
    sets["RANDOM_%02d" % k] = list(rng.choice(names, int(rng.integers(20, 200)), replace=False))
C.write_gmt(os.path.join(W, "sets.gmt"), sets)
print("list: %d genes, %d scored 0 at ranks %d..%d (%.0f%% of the list)" % (N, NZ, NP_, NP_ + NZ - 1, 100.0 * NZ / N))

for scheme, p in (("weighted", 1.0), ("classic", 0.0)):
    r = C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "sets.gmt"),
                        os.path.join(W, "out_" + scheme), label=scheme, scoring_scheme=scheme, nperm=1000)
    assert r.ok(), r.error()
    print("\n== %s: report rows for the planted sets (port ES from the paper's definition; 'undefined' when N_R = 0)" % scheme)
    print("   %-18s %9s %9s %8s %8s %8s %6s | %s" % ("set", "GSEA ES", "port ES", "NES", "NOM p", "FDR q", "rank", "rank of first member / (N - N_H)"))
    for nm in ("ALL_ZERO_20", "ALL_ZERO_40_LATE", "ZERO_19_PLUS_1", "TOP_30", "BOTTOM_30"):
        hm = P.hit_mask(names, sets[nm])
        with np.errstate(divide="ignore", invalid="ignore"):
            es_port, _ = P.enrichment_score(scores, hm, p)
        first = int(np.argmax(hm))
        row = r.rows[nm]
        print("   %-18s %9.4f %9s %8.3f %8.3f %8.3f %6d | -%d/%d = %.4f" %
              (nm, row["es"], ("undefined" if np.isnan(es_port) else "%.4f" % es_port), row["nes"], row["np"], row["fdr"],
               row["rank_at_max"], first, N - hm.sum(), -first / (N - hm.sum())))
    warn = [l for l in r.log.splitlines() if ("NaN" in l or "infinite" in l.lower() or "tie" in l.lower()) and "gs3" not in l]
    print("   log lines mentioning NaN / infinite / ties: %d" % len(warn))
    neg_rows = sorted(((v["nes"], k) for k, v in r.rows.items() if v["es"] < 0))
    print("   most negative NES in the report: %s" % ", ".join("%s (%.2f)" % (k, v) for v, k in neg_rows[:3]))
print("\nDONE")
