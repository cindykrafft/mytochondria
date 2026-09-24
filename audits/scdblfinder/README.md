# scDblFinder audit against 179 published papers (2021–2026)

_Generated 2026-09-24 against `plger/scDblFinder` `devel` @ `2d0e5e4` (1.27.6, 2026-07-07) by reading,
executed on the Bioconductor release 1.16.0 installed here (R 4.3.3) and on 1.4.0, 1.8.0 and 1.12.0
built from their release commits. Focus: the artificial-doublet generator, the kNN and co-expression
features, the classifier loop, the thresholding and the origin annotation — verified on simulated
captures with known doublets and known origins, and on ports of the deterministic pieces._

## What this is

The six-journal survey found **179 papers** in PNAS, *Nature*, *Cell* and *Science*, 2021–2026, that
used scDblFinder to call doublets in single-cell data — the survey's most-used doublet caller, run
inside Seurat (150) or Scanpy (65) workflows, usually per sample and often beside Scrublet (78) or
DoubletFinder (73). The R sources were read on `devel` and the pipeline was exercised on simulated
data: exact recomputations of the expected-doublet arithmetic, a double-loop port of the `cxds2`
co-expression score, ports of the thresholding rules, and end-to-end runs on captures with a known
doublet set and known cell-type origins.

## Findings (details and line citations in [`component-reviews/doublet-scoring-and-origins.md`](component-reviews/doublet-scoring-and-origins.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **SD1** | **CONFIRMED on 1.4.0, 1.8.0, 1.12.0, 1.16.0**; same code on `devel` | now (issue + PR) | With `clusters` given, `createDoublets` returns the size-adjusted 25 % of the artificial doublets after the others, but `getArtificialDoublets` attaches the origin labels in the input order: 48.8 % of the cross-cluster artificial doublets carry another pair's label, and `scDblFinder.mostLikelyOrigin` is right for 24 % of the heterotypic doublets on a simulated capture (100 % with the order kept). The doublet calls do not change. Also: only a quarter of the intended doublets are halved, and a run that selects exactly one pair for adjustment drops it and fails. |
| **SD2** | **CONFIRMED on 1.8.0, 1.12.0, 1.16.0**; same code on `devel` | now (issue + PR) | With `clusters` given as a factor (a colData column of cell types; the package's own `mockDoubletSCE()$cluster`), the cluster column of the results table holds the integer codes while the origins use the level names: `metadata(sce)$scDblFinder.stats` reports 0 observed doublets for every combination with `NA` FNR and difficulty, `plotDoubletMap` has nothing to show, and `scDblFinder.cluster` in the output holds 1, 2, 3 instead of the labels. Character and integer labels work. |
| **SD3** | **CONFIRMED on 1.8.0, 1.12.0, 1.16.0**; same code on `devel` | ready (third, issue + PR) | `doubletThresholding(d, dbr=x, method="dbr")` on the documented minimal input (a table with only a `score` column) returns `NaN`, so every call is `NA`: the homotypic correction divides by the number of artificial doublets, of which there are none. |
| N1 | note, documented three ways | held | The default `dbr.sd` is "40 % of dbr" in the function documentation, "0.015" in the vignette, and `0.3·dbr + 0.025` in `scDblFinder()`'s code. |
| N2 | note, robustness | held | A failed classifier training silently returns the previous score (`tryCatch(..., error=function(e) d$score)`); on this R the 1.16.0 build runs against xgboost 3.2 through deprecation warnings only, and `devel` has adapted. |

**Held up under execution:** `getExpectedDoublets` (2·pᵢ·pⱼ·dbr·N; default 1 % per 1,000 cells),
`propHomotypic`, the default k set, `cxds2` against an explicit port to 1e-16 (sparse and dense input,
with and without excluded cells), the "dbr" (with clusters) and "griffiths" thresholds, the "optim"
threshold as `optimize()` over the ported cost, `createDoublets`' sums and integer bookkeeping without
size adjustment, the per-combination statistics with character and integer labels, and the end-to-end
run (five cell types, 6.8 % doublets: AUC 1.000, recall 0.81, no false positive). The package's 17
testthat tests pass on the installed and the patched 1.16.0. Not checked: multi-sample modes beyond
the default split, `knownDoublets`, ATAC / `aggregateFeatures`, `computeDoubletDensity`,
`findDoubletClusters`, `recoverDoublets`.

## Verification method

`verify/d1_deterministic_pieces.R` (ports of the closed-form pieces, `cxds2`, the thresholds and
`createDoublets`), `d2_artificial_doublet_origins.R` (three well-separated clusters: does each
artificial doublet's expression match its origin label? with the default, with `adjustSize=0`, and with
the corrected function), `d3_end_to_end_origins.R` (simulated capture with known doublets and origins:
calls, AUC, `mostLikelyOrigin` accuracy, stats table, installed vs corrected generator),
`d4_stats_cluster_labels.R` (the stats table with cell-type names, numeric strings, integers and a
factor). Each takes a library path; `.out` is the installed 1.16.0, `.v<version>.out` the release
builds, `.patched.out` the 1.16.0 build carrying the three fixes.

## How the papers use scDblFinder (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 6 (1.16.0 ×2, 1.12 ×2, 1.13.13, 1.4.0) |
| Seurat / Scanpy / Bioconductor framework | 150 / 65 / 21 |
| Scrublet / DoubletFinder / other caller also used | 78 / 73 / 6 |
| 10x Chromium stated; multiome or ATAC; nuclei | 31; 37; 37 |
| doublet score or threshold mentioned | 32 |
| doublets removed (stated) | 27 |
| per-sample run stated | 14 |
| doublet rate stated | 6 |
| cluster-based mode / origins analysed | 2 / 2 |

The profile (`scdblfinder_profile.py`, `scdblfinder_profiles.jsonl`, `profile_run.log`) ran on the
survey's stored evidence sentences (no route to Europe PMC from this session), so the counts are lower
bounds; the survey's own version column for this package is polluted by neighbouring tools' versions
and is not used.

## Filing channel

`plger/scDblFinder` (Bioconductor package; issues on GitHub). Contributor guidance and prior threads
as read for the kit are in [`upstream/README.md`](upstream/README.md). Kit in [`upstream/`](upstream/).

## Files

| path | what |
|---|---|
| `component-reviews/doublet-scoring-and-origins.md` | the review: SD1–SD3, N1–N2 with code citations, the pipeline walk-through, held-up list, version scope |
| `verify/d1_deterministic_pieces.R` … `d4_stats_cluster_labels.R`, `createDoubletsFixed.R` | harnesses and the corrected generator they load |
| `verify/*.out`, `*.v<version>.out`, `*.patched.out` | captured output per build |
| `scdblfinder_profile.py`, `scdblfinder_profiles.jsonl`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit: issue texts, PR bodies, the three patches, test record |

## Next steps

1. Fork `plger/scDblFinder`; push `fix/artificial-doublet-order`, `fix/factor-cluster-labels`,
   `fix/dbr-threshold-without-artificial`.
2. File SD1 and SD2 (issue + PR each) from the kit; SD3 when one of them has a reply.
3. Record numbers and responses here and in the top-level status table.
