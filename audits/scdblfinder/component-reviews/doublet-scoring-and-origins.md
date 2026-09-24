# scDblFinder: artificial doublets, scoring, thresholding and the origin annotation

_Reviewed 2026-09-24 against `plger/scDblFinder` `devel` @ `2d0e5e4` (1.27.6, 2026-07-07) by reading, and
executed on the Bioconductor 3.18 release 1.16.0 (the version installed here, R 4.3.3, xgboost 3.2.1)
and on 1.4.0, 1.8.0 and 1.12.0 built from the release commits; 1.20.0 and `devel` do not install on
this R (they need newer dependencies). The three fix branches were built on 1.16.0 for execution and
prepared against `devel` for filing. Harnesses and outputs in `../verify/`._

## What the cohort uses (179 papers, `../scdblfinder_profiles.jsonl`, survey-cache lower bounds)

| use | papers |
|---|---|
| Seurat framework | 150 |
| Scrublet also used / DoubletFinder also used | 78 / 73 |
| Scanpy framework | 65 |
| multiome / ATAC | 37 |
| snRNA-seq | 37 |
| doublet score or threshold mentioned | 32 |
| doublets removed (stated) | 27 |
| per-sample run stated | 14 |
| doublet rate stated | 6 |
| cluster-based mode stated / doublet origins analysed | 2 / 2 |
| version stated | 6 (1.16.0 ×2, 1.12 ×2, 1.13.13, 1.4.0) |

The typical use is doublet *calling* (score + class, then removal) on 10x data, usually per sample,
alongside one or two other doublet callers. The origin annotation (`scDblFinder.mostLikelyOrigin`,
`scDblFinder.stats`, `plotDoubletMap`) is advertised in the vignette ("Doublet origins and enrichments")
but rarely reported in the cohort.

## Code read

`R/scDblFinder.R` (the driver: feature selection, artificial doublets, PCA, `.evaluateKNN`,
`.scDblscore` with the xgboost loop, thresholding, `.scDblAddCD`), `R/getArtificialDoublets.R`
(`getArtificialDoublets`, `getCellPairs`, `.getMetaCells`, `createDoublets`), `R/doubletThresholding.R`
(`doubletThresholding`, `.optimThreshold`, `.FNR`/`.FDR`/`.FPR`/`.prop.dev`, `.getDoubletStats`,
`.filterUnrecognizableDoublets`, `.estimateHeterotypicDbRate`), `R/misc.R` (`getExpectedDoublets`,
`propHomotypic`, `cxds2`, `.gdbr`, `.getMostLikelyOrigins`, `.defaultProcessing`, `mockDoubletSCE`).
Statement of intended behaviour: the roxygen documentation, the vignette, Germain et al. 2021
(F1000Research) and, for `cxds2`, Bais & Kostka 2020.

## How the pipeline works (for the findings below)

1. Artificial doublets: with `clusters` given, `getCellPairs` draws pairs of cells across clusters in
   proportion to the expected number of heterotypic doublets per cluster pair (`getExpectedDoublets`,
   2·pᵢ·pⱼ·dbr·N); `createDoublets` sums the two cells' counts, with a random 25 % (`adjustSize`) of
   the pairs re-weighted towards the larger-library cluster and 25 % (`halfSize`) halved and Poisson-
   resampled; 10 % of the doublets come from meta-cells and a few triplets are added. The pair's
   cluster combination is the doublet's **origin**, attached by `getArtificialDoublets` to the returned
   columns by position (`oc <- c(oc, as.character(ca$orig.clusters))`).
2. Real cells and artificial doublets are normalised and projected together (PCA, 20 dims). For every
   cell `.evaluateKNN` finds the k nearest neighbours (Annoy) and records the ratio of artificial
   doublets among them at several k, a distance-weighted ratio, the distance to the nearest doublet
   and real cell, the co-expression score `cxds2`, library size and feature counts, and — from the
   neighbouring artificial doublets' origins — the cell's `mostLikelyOrigin` and `originAmbiguous`.
3. A gradient-boosted classifier (xgboost, cross-validated round count) is trained to separate real
   cells from artificial doublets on those features (plus the first PCs), three times, each time
   excluding real cells already looking like doublets and artificial doublets that score below
   `unident.th`; the prediction is the `score`.
4. `doubletThresholding(method="optim")` picks the threshold that minimises deviation² from the
   expected number of doublets (dbr ± dbr.sd, corrected for homotypic doublets) + 2(1−s)·FNR +
   2s·FPR; `class` is `score ≥ threshold`. `.getDoubletStats` tabulates the called doublets by origin
   against the expected counts (`scDblFinder.stats`).

## Findings

### SD1 — with the default `adjustSize`, half of the artificial doublets carry another pair's origin, so `scDblFinder.mostLikelyOrigin` is mostly wrong

`createDoublets` (`getArtificialDoublets.R`) builds the size-adjusted doublets separately and appends
them:

```r
wAd <- sample.int(nrow(dbl.idx), size=round(adjustSize*nrow(dbl.idx)))
wNad <- setdiff(seq_len(nrow(dbl.idx)),wAd)
x1 <- x[,dbl.idx[wNad,1],drop=FALSE]+x[,dbl.idx[wNad,2],drop=FALSE]
if(length(wAd)>1){
  dbl.idx <- as.data.frame(dbl.idx[wAd,,drop=FALSE])
  ...
  x1 <- cbind(x1,x2)
}
```

so column *i* of the result is pair *i* only up to the first adjusted pair. `getArtificialDoublets`
assigns the origins in the input order. With the default `adjustSize=0.25` (`getArtificialDoublets`'s
default, used by `scDblFinder()` whenever `clusters` are given), on three well-separated clusters
**48.8 % of the 650 cross-cluster artificial doublets have counts that match a different pair of
clusters than their label** (`../verify/d2_artificial_doublet_origins.out`; 0 % with `adjustSize=0`;
0 % with the corrected function). The origins feed `.evaluateKNN`, so on a simulated capture (five cell
types, 3,218 cells, 218 doublets, clusters given) **`scDblFinder.mostLikelyOrigin` is right for 24.4 % of
the heterotypic doublets** (`d3_end_to_end_origins.out`); with the order kept it is right for 100 %
and `originAmbiguous` drops from 2.8 % to 0. The doublet calls do not depend on the origins: the
same simulation gives identical calls (0 of 3,218 differ; recall 0.807, no false positive, AUC 1.000)
and a score correlation of 0.9988 between the two runs, the residual difference coming from
`.filterUnrecognizableDoublets`, which uses the labels to drop "unrecognisable" combinations from
training.

Two more consequences of the same reassignment of `dbl.idx`: the halving step samples from the
adjusted subset only, so `ceiling(halfSize × |adjusted|)` doublets are halved instead of
`ceiling(halfSize × pairs)` (5 instead of 20 of 40 pairs in `d1_deterministic_pieces.out`); and when
exactly one pair is selected (4–5 pairs at `adjustSize=0.25`) the `length(wAd)>1` guard drops it, after
which the halving indexes past the end ("subscript out of bounds"). Reachable through
`getArtificialDoublets(propRandom=…)` with a handful of random doublets, or direct calls.

Versions: the code dates from 2020-10-07 (commit 92c038e, before 1.4.0); measured on 1.4.0 (38.8 %
mislabelled — that version's pair sampling differs), 1.8.0, 1.12.0 and 1.16.0 (48.8 % each);
unchanged on `devel`.

Fix (`fix/artificial-doublet-order`, `../upstream/0001-…patch`): sum every pair in the input order,
replace the adjusted ones in place (`x1[,wAd] <- x2`, scaling with `Matrix::Diagonal` so one pair
works), and count the halving over all pairs. Verified on the 1.16.0 build with the change
(`*.patched.out`): 0 % mislabelled, `mostLikelyOrigin` 100 %, halving 20 of 40, 4 pairs → 4 doublets;
the package's 17 testthat tests pass.

### SD2 — with `clusters` given as a factor, `scDblFinder.stats` reports 0 observed doublets for every combination and `scDblFinder.cluster` holds the integer codes

`scDblFinder.R`:

```r
d$cluster <- NA
d[colnames(sce),"cluster"] <- clusters
```

Assigning a factor into a logical `NA` column stores its integer codes. The artificial doublets'
origins are built from the level names ("A+B"), so in `.getDoubletStats` the expected combinations are
named "1+2", "1+3", … while the called doublets' origins are "A+B", …: `observed` is 0 everywhere,
`FNR` and `difficulty` are `NA`, and `plotDoubletMap` has nothing to show; the `scDblFinder.cluster`
column returned to the user holds 1, 2, 3 instead of the labels. Character labels (cell-type names or
Seurat's "0", "1", …) and integer labels work (`../verify/d4_stats_cluster_labels.out`: `sum(observed)` =
80 = the called doublets for character and integer input, 0 for the same labels as a factor). A colData
column of cell types is very often a factor, and the package's own `mockDoubletSCE()$cluster` is one.
Versions: 1.8.0, 1.12.0, 1.16.0, `devel` (1.4.0's stats differ in shape and were not assessed). Fix
(`fix/factor-cluster-labels`, `0002-…patch`): convert a factor to character before the assignment;
`d4_stats_cluster_labels.patched.out` 4/4.

### SD3 — `doubletThresholding(method="dbr")` returns `NaN` on the documented minimal input

The documentation: `d` is "minimally containing a `score` column"; method `dbr` is "strictly based on
the expected doublet rate". `.estimateHeterotypicDbRate` corrects `dbr` for homotypic doublets using the
artificial doublets' scores when there is no `cluster` column; with no artificial rows the proportion
is 0/0 and the threshold is `NaN` (`d1_deterministic_pieces.out`), so every call is `NA`. With a
`cluster` column the threshold is the 1 − dbr·(1 − Σpᵢ²) quantile, as intended. Versions: 1.8.0,
1.12.0, 1.16.0, `devel` (since b248ee3, 2021-07-26). Fix (`fix/dbr-threshold-without-artificial`,
`0003-…patch`): return the given rate when there are no artificial doublets.

### N1 — the default `dbr.sd` is stated three ways

`scDblFinder()`'s documentation: "If NULL, will be 40 % of `dbr`"; the vignette: "a default standard
deviation of 0.015"; the code (`.scDblscore`): `0.3*gdbr + 0.025` (0.04 at 5 %). `doubletThresholding()`
called directly does use 0.4·dbr. Documentation note.

### N2 — a failed classifier training falls back to the seed score without a warning

`.scDblscore` wraps the xgboost training in `tryCatch(..., error=function(e) d$score)`: if training
fails (as it does with an incompatible xgboost API) the returned `score` is the previous iteration's
value, at worst the initial `(cxds + kNN ratio)/2`, with no message. On this R the 1.16.0 build runs
with xgboost 3.2.1 through deprecation warnings only (`devel` has been adapted); an installation where
the call errors would silently produce a different scoring. Robustness note.

## Held up

| what | harness | result |
|---|---|---|
| `getExpectedDoublets`: 2·pᵢ·pⱼ·dbr·N per heterotypic pair, pᵢ²·dbr·N homotypic, total dbr·N, default dbr = 0.01·N/1000 | `d1` | exact (1.8.0+; 1.4.0's formula differs) |
| `propHomotypic` = Σpᵢ²; `.defaultKnnKs` = {3,10,15,20,25,50,kmax} capped at max(⌈√(n/2)⌉, 25) | `d1` | exact |
| `cxds2` against an explicit double-loop port (binarisation, top genes by p(1−p), upper-tail binomial log-p, −xᵀSx, min–max) with and without excluded cells, sparse and dense input, sparse and low-sparsity data | `d1` | 1e-16 |
| `doubletThresholding` "dbr" (with clusters) and "griffiths"; `.optimThreshold` = `optimize()` over the ported cost at stringency 0.5 and 0.7, and the tabulated costs | `d1` | 1e-6 / exact |
| `createDoublets` without size adjustment: one column per pair, exact sums, integer counts when `resamp = halfSize` | `d1` | exact |
| end to end on simulated doublets (5 types, 6.8 % doublets, clusters given): AUC 1.000, recall 0.81, FDR 0.00, called rate 5.5 % for a 6.8 % truth with the default dbr of 3.2 % | `d3` | as expected for the design |
| `scDblFinder.stats$observed` with character and integer labels | `d4` | equals the called doublets |
| the package's testthat suite (17 tests) on the installed and the patched 1.16.0 | `test-runs.txt` | 17/17 both |

Not checked: `multiSampleMode` other than the default split, `knownDoublets`, `clustCor`,
`aggregateFeatures`/ATAC, `computeDoubletDensity`, `findDoubletClusters` (rewritten on `devel`
without `scran::findMarkers`), `recoverDoublets`, `directDblClassification`.

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| SD1 | 1.4.0, 1.8.0, 1.12.0, 1.16.0 (executed), `devel` (same code) | 1.16.0 + `fix/artificial-doublet-order`; any run with `adjustSize=0` or without `clusters` |
| SD2 | 1.8.0, 1.12.0, 1.16.0 (executed), `devel` (same code) | 1.16.0 + `fix/factor-cluster-labels`; character or integer labels |
| SD3 | 1.8.0, 1.12.0, 1.16.0 (executed), `devel` (same code) | 1.16.0 + `fix/dbr-threshold-without-artificial`; input with a `cluster` column |
