#!/usr/bin/env python3
"""N-note: tied rank-metric values are ordered by input order (stable sort), so the same
data in a different row/line order gives a different ES for a set whose members sit in
the tie block.  Measured on GseaPreranked with a ranked list in which 2,000 of 8,000
genes share the score 0 (as a count-based Signal2Noise list does when both class means
are 0): the .rnk with the tie block in one order vs. reversed.

Run: python3 note_ties_input_order.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsea_cli as G  # noqa: E402
import ref_gsea as R  # noqa: E402

W = "/tmp/gseawork/note_ties"
os.makedirs(W, exist_ok=True)
rng = np.random.default_rng(7)
N = 8000
names = [f"g{i:05d}" for i in range(N)]
sc = rng.normal(size=N)
sc[3000:5000] = 0.0                      # a tie block of 2,000 genes at score 0
order = np.argsort(-sc, kind="stable")
names = [names[i] for i in order]
sc = sc[order]
tie = [nm for nm, s in zip(names, sc) if s == 0.0]
gs = {"IN_TIE_EARLY": tie[:40], "IN_TIE_LATE": tie[-40:], "SPREAD": list(rng.choice(names, 50, replace=False))}
G.write_gmt(f"{W}/sets.gmt", gs)

results = {}
for label, tie_order in (("as_written", tie), ("tie_block_reversed", tie[::-1])):
    nm = [x for x, s in zip(names, sc) if s > 0] + tie_order + [x for x, s in zip(names, sc) if s < 0]
    d = dict(zip(names, sc))
    sv = np.array([d[x] for x in nm])
    G.write_rnk(f"{W}/{label}.rnk", nm, sv)
    run = G.run_preranked(f"{W}/{label}.rnk", f"{W}/sets.gmt", f"{W}/out_{label}", nperm=100)
    tsv = G.parse_report_tsv(run)
    edb = G.parse_edb(run)
    rn, rs = G.parse_edb_rnk(run)
    results[label] = {k: (float(tsv[k]["ES"]), float(tsv[k]["NES"]), edb[k]["rank_at_es"]) for k in gs}
    print(f"{label}: tie block kept in file order = {rn[2000:2005] == nm[2000:2005]}; "
          f"positions of the first/last IN_TIE_EARLY member: {rn.index(tie[0])}/{rn.index(tie[39])}")
    for k in gs:
        mask = np.isin(nm, gs[k])
        if np.abs(sv[mask]).sum() == 0:
            # sum of |score| over the members is 0: the paper's P_hit is 0/0; the Java table returns
            # NaN hit points, the running sum turns NaN at the first member and the reported ES is
            # the depth reached before it (= -(rank of first member)/(N - Nh))
            es_ref = float("nan")
            depth = -(np.flatnonzero(mask)[0]) / (len(nm) - mask.sum())
            note = f"undefined (0/0); depth before first member = {depth:.4f}"
        else:
            es_ref, i_ref, _ = R.enrichment_score(sv, mask, 1.0)
            note = f"{es_ref:.4f}"
        print(f"   {k:13s} ES = {results[label][k][0]:8.4f} (paper's ES on this order: {note}) NES = {results[label][k][1]:7.3f} rank-at-ES = {results[label][k][2]}")
for k in gs:
    a, b = results["as_written"][k], results["tie_block_reversed"][k]
    print(f"{k:13s}: ES {a[0]:.4f} vs {b[0]:.4f}  (delta {abs(a[0]-b[0]):.4f}); NES {a[1]:.3f} vs {b[1]:.3f}")
