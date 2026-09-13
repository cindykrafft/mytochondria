#!/usr/bin/env python3
"""NOTE: tied ranking scores keep their input order, and nothing warns.

GSEAPreranked sorts the .rnk with a stable sort (`DoubleElementComparator` returns 0 for
equal values; `Arrays.parallelSort`/`Collections.sort` are stable), so genes with the same
score stay in file order.  A gene set whose members sit inside a block of tied scores
(typical for RNA-seq statistics with many exact zeros) therefore gets an ES that depends
on the order of the lines in the file, and the run reports nothing about ties.

Two .rnk files with identical (gene, score) pairs, differing only in the order of the
lines inside a tie block of 1,200 genes scored 0.3 (and a block of 300 zeros); a set of
40 genes at the front of the block in file 1 and at its end in file 2; fgsea on the same data for comparison
(it warns about ties in fgseaSimple and gives the same order-dependent ES).  A set whose
members all have score 0 (N_R = 0) is a separate matter: the hit increment is 0/0, the
running sum turns NaN at the first hit, and GSEA reports the running sum just before that
hit as the ES, with an NES and p as if it meant something.
"""
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C
import gsea_port as P

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
C.banner("note_ties: tied scores keep file order, no warning", BUILD)
W = os.path.join(C.SCRATCH, "note_ties", BUILD)
os.makedirs(W, exist_ok=True)

rng = np.random.default_rng(3)
NP_, NT, NZ, NN = 900, 1200, 300, 600          # positive block, tie block at 0.3, zero block, negative block
N = NP_ + NT + NZ + NN
pos = C.strictly_decreasing(np.abs(rng.normal(0, 1, NP_)) + 0.31)
neg = -C.strictly_decreasing(np.abs(rng.normal(0, 1, NN)) + 0.01)[::-1]   # descending, like the list
names = ["g%04d" % i for i in range(N)]
tie_names = names[NP_:NP_ + NT]
zero_names = names[NP_ + NT:NP_ + NT + NZ]
scores1 = np.concatenate([pos, np.full(NT, 0.3), np.zeros(NZ), neg])
order1 = names[:NP_] + tie_names + zero_names + names[NP_ + NT + NZ:]
order2 = names[:NP_] + tie_names[::-1] + zero_names[::-1] + names[NP_ + NT + NZ:]
C.write_rnk(os.path.join(W, "order1.rnk"), order1, scores1)
C.write_rnk(os.path.join(W, "order2.rnk"), order2, scores1)
sets = {"TIED_40": tie_names[:40],            # 40 members inside the block tied at 0.3
        "ZERO_40": zero_names[:40],           # 40 members with score exactly 0 (N_R = 0)
        "TOP_30": names[:30], "MIXED_60": names[:30] + tie_names[:30]}
C.write_gmt(os.path.join(W, "sets.gmt"), sets)
print("%d genes: %d tied at score 0.3 (ranks %d..%d) and %d at score 0 (ranks %d..%d); both blocks are reversed between the two files"
      % (N, NT, NP_, NP_ + NT - 1, NZ, NP_ + NT, NP_ + NT + NZ - 1))

for f in ("order1", "order2"):
    r = C.run_preranked(BUILD, os.path.join(W, f + ".rnk"), os.path.join(W, "sets.gmt"),
                        os.path.join(W, "out_" + f), label=f, nperm=100)
    assert r.ok(), r.error()
    rl = [n for n, _ in r.ranked]
    print("\n== %s.rnk: GSEA keeps the tie block in file order: %s" % (f, rl[NP_:NP_ + 5] == (order1 if f == "order1" else order2)[NP_:NP_ + 5]))
    warn = [l for l in r.log.splitlines() if "tie" in l.lower() and "note_ties" not in l]   # the run's own path contains "ties"
    print("   log lines mentioning ties or duplicates: %d" % len(warn))
    for nm in sets:
        with np.errstate(divide="ignore", invalid="ignore"):
            es_port, _ = P.enrichment_score(scores1, P.hit_mask(rl, sets[nm]), 1.0)
        print("   %-16s ES %8.4f (port on GSEA's order %8.4f) NES %7.3f p %.3f rank_at_max %d" %
              (nm, r.rows[nm]["es"], es_port, r.rows[nm]["nes"], r.rows[nm]["np"], r.rows[nm]["rank_at_max"]))

# fgsea on both files
r_script = os.path.join(W, "ties.R")
with open(r_script, "w") as fh:
    fh.write(r'''
suppressMessages(library(fgsea))
args <- commandArgs(trailingOnly = TRUE)
gmt <- gmtPathways(args[3])
for (f in args[1:2]) {
  rnk <- read.table(f, sep = "\t", header = FALSE, stringsAsFactors = FALSE)
  stats <- setNames(rnk$V2, rnk$V1)
  stats <- stats[order(-stats)]  # stable, like GSEA
  for (nm in c("TIED_40", "ZERO_40")) {
    idx <- which(names(stats) %in% gmt[[nm]])
    es <- calcGseaStat(stats, selectedStats = idx, gseaParam = 1)
    cat(sprintf("fgsea calcGseaStat %s on %s: ES = %.4f\n", nm, basename(f), es))
  }
  w <- tryCatch({ withCallingHandlers({ fgseaSimple(gmt, stats, nperm = 100); "no warning" },
       warning = function(w) { invokeRestart("muffleWarning") }) }, error = function(e) conditionMessage(e))
  res <- withCallingHandlers(fgseaSimple(gmt, stats, nperm = 100), warning = function(w) { cat("fgsea warning:", conditionMessage(w), "\n"); invokeRestart("muffleWarning") })
}
''')
env = dict(os.environ, R_LIBS=os.path.join(C.SCRATCH, "rlib"))
env.pop("JAVA_TOOL_OPTIONS", None)
rp = subprocess.run(["Rscript", r_script, os.path.join(W, "order1.rnk"), os.path.join(W, "order2.rnk"),
                     os.path.join(W, "sets.gmt")], capture_output=True, text=True, env=env)
print("\n== fgsea 1.39.4 on the same files")
print("\n".join("   " + l for l in rp.stdout.splitlines() if l.strip()))
if rp.returncode:
    print(rp.stderr[-800:])
print("\nDONE")
