#!/usr/bin/env python3
"""Held-up check: GSEAPreranked's enrichment score, NES, nominal p, FWER and FDR against
an independent numpy port of Subramanian et al. 2005 and against fgsea, on a synthetic
ranked list with planted signal.

A. ES for the classic (p=0), weighted (p=1, default) and weighted_p2 (p=2) schemes,
   24 gene sets (planted at the top, at the bottom, split, random; sizes 15-400),
   shipped program vs the port (exact arithmetic on the same list) and vs
   fgsea::calcGseaStat (gseaParam = p) on the same list.
B. From the program's own null (RND_ES in edb/results.edb, 1000 gene-set permutations):
   NES, nominal p (strict count, as GSEA defines it), FWER and the FDR q-value recomputed
   with the port's *per-permutation* formula, compared with the report's numbers.
C. Rank-at-max and leading-edge tags against the port's running sum.
"""
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C
import gsea_port as P

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
C.banner("heldup_preranked_core: ES / NES / p / FWER / FDR vs port and fgsea", BUILD)
W = os.path.join(C.SCRATCH, "heldup_preranked_core", BUILD)
os.makedirs(W, exist_ok=True)

rng = np.random.default_rng(20260913)
N = 4000
names = ["gene%04d" % i for i in range(N)]
# correlation-like scores, descending, with a heavier positive tail
scores = C.strictly_decreasing(np.concatenate([rng.normal(0.8, 0.5, 300), rng.normal(0, 0.4, N - 300)]))
C.write_rnk(os.path.join(W, "list.rnk"), names, scores)

sets = {}  # names in upper case: GSEA upper-cases gene-set names in its reports
sets["TOP_15"] = names[:15]
sets["TOP_50_SPREAD"] = names[0:200:4]
sets["TOP_100_DENSE"] = names[10:110]
sets["BOTTOM_15"] = names[-15:]
sets["BOTTOM_60_SPREAD"] = names[N - 400::7][:60]
sets["BOTTOM_200"] = names[-200:]
sets["SPLIT_39"] = names[:20] + names[-19:]   # 20 + 20 would tie the +0.5 / -0.5 classic extremes exactly
sets["SPLIT_UNEVEN"] = names[:30] + names[-10:]
sets["MIDDLE_80"] = names[1900:1980]
sets["UPPER_HALF_300"] = list(rng.choice(names[:2000], 300, replace=False))
sets["LOWER_HALF_300"] = list(rng.choice(names[2000:], 300, replace=False))
for k in range(13):
    n = int(rng.integers(15, 400))
    sets["RANDOM_%02d_n%d" % (k, n)] = list(rng.choice(names, n, replace=False))
# every set also gets a few genes that are not in the ranked list (GSEA restricts to the list)
for k in list(sets):
    sets[k.upper()] = list(sets.pop(k)) + ["absent_%s_%d" % (k, j) for j in range(3)]
C.write_gmt(os.path.join(W, "sets.gmt"), sets)

# ------------------------------------------------------------------ fgsea on the same list
r_script = os.path.join(W, "fgsea_es.R")
with open(r_script, "w") as f:
    f.write(r'''
suppressMessages(library(fgsea))
args <- commandArgs(trailingOnly = TRUE)
rnk <- read.table(args[1], sep = "\t", header = FALSE, stringsAsFactors = FALSE)
stats <- setNames(rnk$V2, rnk$V1)
stats <- sort(stats, decreasing = TRUE)
gmt <- gmtPathways(args[2])
cat("fgsea", as.character(packageVersion("fgsea")), "\n")
for (p in c(0, 1, 2)) {
  for (nm in names(gmt)) {
    idx <- which(names(stats) %in% gmt[[nm]])
    es <- calcGseaStat(stats, selectedStats = idx, gseaParam = p, returnAllExtremes = FALSE)
    cat(sprintf("ES\t%g\t%s\t%.10g\n", p, nm, es))
  }
}
''')
env = dict(os.environ, R_LIBS=os.path.join(C.SCRATCH, "rlib"))
env.pop("JAVA_TOOL_OPTIONS", None)
rp = subprocess.run(["Rscript", r_script, os.path.join(W, "list.rnk"), os.path.join(W, "sets.gmt")],
                    capture_output=True, text=True, env=env)
fg = {}
for line in rp.stdout.splitlines():
    if line.startswith("ES\t"):
        _, p, nm, es = line.split("\t")
        fg[(float(p), nm)] = float(es)
    elif line.startswith("fgsea"):
        print("R reference:", line.strip(), "(R %s)" % subprocess.run(["R", "--version"], capture_output=True, text=True).stdout.split("\n")[0].split()[2])
if not fg:
    print("fgsea not available:", rp.stderr[-500:])

# ------------------------------------------------------------------ A. ES per scheme
print("\n== A. enrichment score, shipped GSEAPreranked vs port vs fgsea (max |diff| over %d sets)" % len(sets))
print("%-14s %5s %14s %14s %8s" % ("scheme", "p", "max|GSEA-port|", "max|GSEA-fgsea|", "sets"))
runs = {}
for scheme, p in (("classic", 0.0), ("weighted", 1.0), ("weighted_p2", 2.0)):
    r = C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "sets.gmt"),
                        os.path.join(W, "out_" + scheme), label=scheme, scoring_scheme=scheme, nperm=1000)
    assert r.ok(), r.error()
    runs[scheme] = r
    d_port, d_fg = 0.0, 0.0
    for nm, genes in sets.items():
        es_port, _ = P.enrichment_score(scores, P.hit_mask(names, genes), p)
        d_port = max(d_port, abs(r.rows[nm]["es"] - es_port))
        if (p, nm) in fg:
            d_fg = max(d_fg, abs(r.rows[nm]["es"] - fg[(p, nm)]))
    print("%-14s %5.1f %14.2e %14s %8d" % (scheme, p, d_port, ("%.2e" % d_fg) if fg else "n/a", len(r.rows)))

# a few named values for the record (weighted)
r = runs["weighted"]
print("\n   weighted ES, selected sets (GSEA / port / fgsea):")
for nm in ("TOP_15", "TOP_100_DENSE", "BOTTOM_15", "BOTTOM_200", "SPLIT_39", "MIDDLE_80",
           [k for k in sets if k.startswith("RANDOM_00")][0]):
    es_port, _ = P.enrichment_score(scores, P.hit_mask(names, sets[nm]), 1.0)
    print("   %-18s %10.6f %10.6f %10s" % (nm, r.rows[nm]["es"], es_port,
                                            ("%.6f" % fg[(1.0, nm)]) if (1.0, nm) in fg else "n/a"))

# ------------------------------------------------------------------ B. statistics from GSEA's own null
print("\n== B. NES / nominal p / FWER / FDR recomputed from the program's RND_ES (edb, 4 dp) vs the report")
for scheme in ("weighted", "classic"):
    r = runs[scheme]
    order = list(r.edb)
    real_es = np.array([r.edb[n]["es"] for n in order])
    null = np.array([r.edb[n]["rnd_es"] for n in order])           # (n_sets, nperm)
    assert null.shape == (len(order), 1000), null.shape
    real_nes = np.array([P.nes(real_es[i], null[i]) for i in range(len(order))])
    null_nes = np.array([P.nes_null(null[i]) for i in range(len(order))])
    rep_nes = np.array([r.rows[n]["nes"] for n in order])
    rep_np = np.array([r.rows[n]["np"] for n in order])
    rep_fwer = np.array([r.rows[n]["fwer"] for n in order])
    rep_fdr = np.array([r.rows[n]["fdr"] for n in order])
    # the report's ES has full precision; the edb ES is rounded, so use the report's ES for NES
    real_es_full = np.array([r.rows[n]["es"] for n in order])
    real_nes_full = np.array([P.nes(real_es_full[i], null[i]) for i in range(len(order))])
    port_np = np.array([P.nominal_p(real_es_full[i], null[i], strict=True) for i in range(len(order))])
    port_np_ties = np.array([P.nominal_p(real_es_full[i], null[i], strict=False) for i in range(len(order))])
    port_fwer = np.array([P.fwer(real_nes_full[i], null_nes) for i in range(len(order))])
    port_fdr_perm = P.fdr_per_permutation(real_nes_full, null_nes)
    port_fdr_pool = P.fdr_pooled(real_nes_full, null_nes)
    print("   %-12s max|NES diff| %.2e   max|p diff| (strict) %.2e  (with ties) %.2e   max|FWER diff| %.2e"
          % (scheme, np.nanmax(np.abs(rep_nes - real_nes_full)), np.nanmax(np.abs(rep_np - port_np)),
             np.nanmax(np.abs(rep_np - port_np_ties)), np.nanmax(np.abs(rep_fwer - port_fwer))))
    print("   %-12s max|FDR diff| per-permutation formula %.2e ; paper's pooled formula %.2e (mean %.2e)"
          % ("", np.nanmax(np.abs(rep_fdr - port_fdr_perm)), np.nanmax(np.abs(rep_fdr - port_fdr_pool)),
             np.nanmean(np.abs(rep_fdr - port_fdr_pool))))
    print("   %-12s sets with FDR<0.25: report %d, per-permutation %d, pooled %d ; nominal p<0.05: %d / port %d"
          % ("", (rep_fdr < 0.25).sum(), (port_fdr_perm < 0.25).sum(), (port_fdr_pool < 0.25).sum(),
             (rep_np < 0.05).sum(), (port_np < 0.05).sum()))

# ------------------------------------------------------------------ C. rank at max / leading edge
print("\n== C. RANK AT MAX and leading-edge 'tags' vs the port's running sum (weighted)")
print("   (GSEA reports RANK AT MAX as the 0-based position for a positive ES and as N minus that position")
print("    for a negative ES, i.e. counted from the bottom of the list: GeneSetSignalImpl.getRankAtMax)")
r = runs["weighted"]
bad = 0
for nm, genes in sets.items():
    hm = P.hit_mask(names, genes)
    rs = P.running_sum(scores, hm, 1.0)
    i = int(np.argmax(np.abs(rs)))
    es = rs[i]
    if es >= 0:
        tags = hm[: i + 1].sum() / hm.sum()
    else:
        tags = hm[i:].sum() / hm.sum()
    rep = r.rows[nm]
    rep_tags = int(rep["leading_edge"].split("tags=")[1].split("%")[0]) / 100.0
    expect_rank = i if es >= 0 else N - i
    if rep["rank_at_max"] != expect_rank or abs(rep_tags - tags) > 0.006:
        bad += 1
        print("   MISMATCH %s: rank_at_max %d vs port %d; tags %.2f vs %.2f" % (nm, rep["rank_at_max"], expect_rank, rep_tags, tags))
print("   sets checked: %d, mismatches: %d" % (len(sets), bad))
print("\nDONE")
