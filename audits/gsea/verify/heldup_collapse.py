#!/usr/bin/env python3
"""Held-up check: probe-to-gene collapsing (`-collapse Collapse -mode ...` with a .chip
file) for the expression tool and for GSEAPreranked, against the port.

Expression tool: 1,500 symbols carried by 1-4 probes each (2,900 probes), plus 60 probes
with no symbol; modes Max_probe (default), Median_of_probes, Mean_of_probes,
Sum_of_probes, Abs_max_of_probes.  The collapsed dataset is not written to disk, so the
check is on the ranked-gene-list SCORE (Diff_of_Classes, which is linear in the
collapsed values, and Signal2Noise) against metric(collapse(X)) from the port.
Preranked tool: the same modes on a .rnk of probe scores; the collapsed ranked list is
the report's ranked_gene_list file.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C
import gsea_port as P

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
C.banner("heldup_collapse: probe collapsing modes vs port", BUILD)
W = os.path.join(C.SCRATCH, "heldup_collapse", BUILD)
os.makedirs(W, exist_ok=True)

rng = np.random.default_rng(5)
n_sym, nA, nB = 1500, 6, 6
symbols = ["SYM%04d" % i for i in range(n_sym)]
probes, probe_sym = [], []
for s in symbols:
    k = int(rng.integers(1, 5))
    for j in range(k):
        probes.append("%s_at%d" % (s, j))
        probe_sym.append(s)
for j in range(60):
    probes.append("NOSYM_%d_at" % j)
    probe_sym.append(None)
samples = ["A%d" % i for i in range(nA)] + ["B%d" % i for i in range(nB)]
X = np.round(rng.normal(0, 3, size=(len(probes), nA + nB)), 4)      # signed values so Abs_max differs from Max
X[:200, :nA] += 4.0
C.write_gct(os.path.join(W, "probes.gct"), probes, samples, X)
C.write_cls(os.path.join(W, "data.cls"), ["A"] * nA + ["B"] * nB)
C.write_chip(os.path.join(W, "array.chip"), {p: (s if s else "---") for p, s in zip(probes, probe_sym)})  # "---" = no symbol (ChipParser)
gsets = {"SET_%02d" % k: list(rng.choice(symbols, int(rng.integers(15, 100)), replace=False)) for k in range(10)}
C.write_gmt(os.path.join(W, "sets.gmt"), gsets)
print("probes: %d (%d symbols with 1-4 probes, 60 without a symbol)" % (len(probes), n_sym))

print("\n== expression tool, -collapse Collapse: ranked-list SCORE vs metric(port collapse)")
print("   %-18s %-16s %10s %12s %8s" % ("mode", "metric", "symbols", "max|diff|", "order"))
for mode in ("Max_probe", "Median_of_probes", "Mean_of_probes", "Sum_of_probes", "Abs_max_of_probes"):
    col = P.collapse(X, probe_sym, mode)
    for metric, fn in (("Diff_of_Classes", P.diff_of_classes), ("Signal2Noise", P.signal2noise)):
        r = C.run_gsea(BUILD, os.path.join(W, "probes.gct"), os.path.join(W, "data.cls"), os.path.join(W, "sets.gmt"),
                       os.path.join(W, "out_%s_%s" % (mode, metric)), label="c", nperm=10, permute="gene_set",
                       collapse="Collapse", mode=mode, chip=os.path.join(W, "array.chip"), metric=metric)
        assert r.ok(), r.error()
        got = dict(r.ranked)
        exp = {s: fn(v[:nA], v[nA:]) for s, v in col.items()}
        missing = set(exp) - set(got)
        extra = set(got) - set(exp)
        d = max(abs(got[s] - exp[s]) for s in exp if s in got)
        along = np.array([exp[n] for n, _ in r.ranked if n in exp])
        order_ok = (np.diff(along) <= 1e-6).all()   # GSEA orders by float32 scores; accept near-ties either way
        print("   %-18s %-16s %10d %12.2e %8s%s" % (mode, metric, len(got), d, "same" if order_ok else "DIFFERS",
                                                    "" if not (missing or extra) else "  missing %d extra %d" % (len(missing), len(extra))))

print("\n== GSEAPreranked, -collapse Collapse on a .rnk of probe scores")
scores = rng.normal(0, 1, len(probes))
order = np.argsort(-scores, kind="stable")
scores = np.empty_like(scores)
scores[order] = C.strictly_decreasing(rng.normal(0, 1, len(probes)))   # tie-free probe scores
C.write_rnk(os.path.join(W, "probes.rnk"), [probes[i] for i in order], scores[order])
print("   %-18s %10s %12s %8s" % ("mode", "symbols", "max|diff|", "order"))
for mode in ("Max_probe", "Median_of_probes", "Mean_of_probes", "Sum_of_probes", "Abs_max_of_probes"):
    r = C.run_preranked(BUILD, os.path.join(W, "probes.rnk"), os.path.join(W, "sets.gmt"),
                        os.path.join(W, "out_rnk_" + mode), label="c", nperm=10, collapse="Collapse", mode=mode,
                        chip=os.path.join(W, "array.chip"))
    assert r.ok(), r.error()
    got = dict(r.ranked)
    col = P.collapse(scores[:, None], probe_sym, mode)
    exp = {s: float(v[0]) for s, v in col.items()}
    d = max(abs(got[s] - exp[s]) for s in exp)
    along = np.array([exp[n] for n, _ in r.ranked if n in exp])
    order_ok = (np.diff(along) <= 1e-6).all()
    print("   %-18s %10d %12.2e %8s" % (mode, len(got), d, "same" if order_ok else "DIFFERS"))
print("\nDONE")
