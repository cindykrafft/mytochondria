# limma audit against 234 published papers (2021–2026)

_Generated 2026-09-13 against the Bioconductor git of `limma` (read through the
`bioc/limma` mirror): `devel` @ `57a8de72` (3.99.0, 2026-08-30, the commit that adds the
4.0.0 C backends) and `RELEASE_3_23` @ `825d1c83` (3.68.5, 2026-08-10, the current release
branch). Focus: the pipeline the cohort runs — `voom`/`voomWithQualityWeights`/`voomLmFit`,
`lmFit` (weights, `block`/`correlation`), `duplicateCorrelation`, `arrayWeights`,
`contrasts.fit`, `eBayes`/`squeezeVar`/`fitFDist*`, `treat`, `topTable`, `decideTests`,
`camera`/`roast`/`fry`, `removeBatchEffect`, `normalizeBetweenArrays` — verified by executing
seven shipped versions against closed forms and independent ports of the published
methods._

## What this is

The six-journal survey found **234 papers** in *Nature* (115), PNAS (97), *Cell* (17),
*Science* (4) and NEJM (1), 2021–2026, that used limma — 147 on RNA-seq counts, 54 naming
voom, 47 on proteomics/methylation/other omics, 46 pseudo-bulk single-cell, 28 blocking or
`duplicateCorrelation`, 14 `removeBatchEffect`, 12 microarrays (all lower bounds, see
below). Its statistical core was read in full on the two commits above and every suspicion
was run through the installed package: R 4.3.3 with limma 3.58.1 (the apt build on this
host), 3.34.0, 3.42.2, 3.62.2 and 3.68.4 (Ubuntu pool source tarballs), 3.68.5 and 3.99.0
(mirror branches), each in its own library (`verify/rlib.sh`), against closed-form linear
algebra, ports written from the papers (Smyth 2004; Law et al 2014; Wu & Smyth 2012;
McCarthy & Smyth 2009; Smyth 2002 / Ritchie et al 2006), lme4 REML fits and edgeR 4.0.16 /
4.10.5, on synthetic data with planted truth.

limma is mature and its authors are statisticians, and that is what the execution shows:
the linear models, contrasts, empirical Bayes moderation, TREAT, BH/decideTests, voom
weights, genewise correlations, camera and the normalisation arithmetic reproduce the
published methods to 1e-8 or better wherever a reference could be computed, and the new
C backends of the coming 4.0.0 return the same numbers as the R code they replace. The two
confirmed items are a convergence criterion that stops one of the two REML array-weight
routines after one or two iterations (live since 2019 and about to become the default path
of `voomLmFit(sample.weights=TRUE)`), and a 2026 offset feature in `voom()` that counts
library sizes twice for the edgeR objects it was written for.

## Findings (details and line citations in [`component-reviews/statistical-core.md`](component-reviews/statistical-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **LI1** | **CONFIRMED on 3.42.2, 3.58.1, 3.62.2, 3.68.4, 3.68.5 and `devel`**; 3.34.0 predates the routine; fixed by the kit patches on both branches | now (first) | `arrayWeights(method="reml")` with prior weights (`.arrayWeightsPrWtsREML`) divides its convergence criterion by `ngenes+prior.n` twice, so it is exactly `ngenes+prior.n` times smaller than the criterion of the weight-free routine for the same state (iteration-1 values 1.767e-5 vs 0.1768, ratio 10010.00 for 10,000 genes) and the default `tol=1e-5` stops it after 2 iterations instead of 5. With a weight matrix of ones — the same model — the weights differ from the weight-free REML solution by up to 14.7 % (2.454 vs 2.877 for a true 2.83); `voomWithQualityWeights(method="reml")` on data with two poor samples returns weights up to 11.7 % from converged and 137 instead of 183 genes at adj.P < 0.05. The `devel` C backend reproduces it, and `devel`'s `voomLmFit(sample.weights=TRUE)` now routes to this path by design (`method="reml"` when no df are lost to zeros), making it the default of the 4.0.0 pipeline. One-line fix on each branch with a test in the [kit](upstream/). |
| **LI2** | **CONFIRMED on 3.68.4, 3.68.5 and `devel` (`voom()`) and on edgeR 4.10.5 (`voomLmFit`)**; 3.58.1, 3.62.2 and edgeR 4.0.16 unaffected (no offset support); `devel` `voomLmFit` unaffected; documented behaviour | now (second) | `voom()` (3.68.0, April 2026) row-mean corrects a DGEList's edgeR-style `offset` and adds it to `log(lib.size)`; an edgeR offset already contains the log library sizes (`scaleOffset`, `glmFit`, `cpm`), so the effective library size becomes `lib.size²/geomean`. The trivial offset `log(lib.size)` shifts `E` by −log2(lib.size/geomean) per column (1.5, −0.5, 0.5, −1.5 for a four-fold to eight-fold range) instead of being a no-op; with one group sequenced 2.5× deeper every logFC shifts by −1.507 and 5,374 genes are called "down" at adj.P < 0.05 against 37 in the reference run (500 true). `devel`'s `voomLmFit` reads the same slot as `exp(offset)` (NEWS 4.0.0), so the two functions disagree on the same object. Patch for `devel` aligning `voom()` with `voomLmFit()`, help page and test, in the kit. |
| N1–N9 | notes | held | `fitFDistUnequalDF1` bounds df.prior to (2, 9998) (true 0.5–1.5 come back as 2.000x with the prior scale 1.3–10× too high); the documented `contrasts.fit` approximation under voom weights (sd 4.6 % high at the median, up to 21 %; 5 vs 15 genes at FDR 0.05 in one contrast; exact in `devel`'s `lmFit(contrasts=)`); `<` vs `<=` and `>` vs `>=` at the thresholds; F-test df2 uncapped (4.4e-3 in p when df.prior > pooled df); roast's Bailey t-to-z approximation (2.6e-2 at df 3); the unequal-df robust estimator does not shrink df.prior for hypervariable genes in a simulation where the legacy one does; voom's trend x-axis under offsets; fry vs roast at finite prior df; `devel` vs edgeR 4.0.16 `voomLmFit` differences of order 1e-2 from the adaptive span. |

Four own suspicions were withdrawn by execution (the `contrasts.fit` probe on an orthogonal
design; the shared-Cholesky shortcut in `src/gls.c`; the unscaled `Z` in `src/dupcor.c`,
which follows `statmod`; a scalar `df.prior` misread as `NA`). They are recorded in the
review.

**Held up under execution** (`devel` and 3.68.5; most also on 3.58.1): `lmFit` with weights
and missing values equals per-gene weighted least squares to 3.9e-14; `contrasts.fit`
without weights is exact; `eBayes` equals the Smyth 2004 port to all printed digits in
df.prior/s2.prior and to 1.4e-12 in t, the B-statistic and moderated F equal their closed
forms, null coefficients are calibrated (5.53 % below 0.05, KS p 0.70); `treat` is exact;
`topTable` adjusts with BH over all genes before thinning and its confidence intervals are
exact; `decideTests` separate/global/hierarchical equal ports; `voom` equals the Law 2014
port to 8.9e-16 in weights; `voomWithQualityWeights` combines the two weight sets exactly;
`duplicateCorrelation` equals lme4 REML to a median 1.4e-5 per gene and the consensus rule
exactly, and the `devel` C backend returns the same genewise values as the 3.68.5 statmod
code; `lmFit(block=, correlation=)` equals the GLS closed form to 2.8e-14 with weights and
NAs; `camera` equals the Wu & Smyth port to 1.4e-8 relative; `fry`'s directional p equals
its closed form; `normalizeQuantiles` and `removeBatchEffect` equal ports exactly; robust
eBayes shrinks df.prior for planted outliers monotonically with no false discoveries; the
project's own `tests/limma-Tests.R` gives the same 76 pre-existing `Rdiff` lines with and
without the patches and the five new `devel` C tests pass on the patched build. Not audited:
`arrayWeights(method="genebygene")` internals, `mrlm`, `romer`/`goana`/`kegga`,
`diffSplice`, two-colour and background code, plotting.

## How the papers use limma (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| RNA-seq counts input | 147 |
| DESeq2 also used / edgeR also used | 69 / 64 |
| voom named | 54 |
| batch / covariate / blocking in the design | 48 |
| proteomics / methylation / ATAC / other omics | 47 |
| pseudo-bulk / single-cell | 46 |
| adjusted p / FDR / BH | 44 (cutoffs: 0.05 ×16, 0.10 ×1) |
| `duplicateCorrelation` / block / paired / random effect | 28 |
| limma version stated | 22 in the cache text, 51 with a survey-recorded version (3.46.0 ×6, 3.58.1 ×5, 3.34.9 ×3, 3.48.3 ×3, 3.50.0 ×3, 3.62.2 ×2, 3.60.x ×6, 3.54.x ×4; every named version is 3.x) |
| `lmFit` / `eBayes` named | 22 |
| log fold-change cutoff | 16 (1 ×3) |
| `removeBatchEffect` | 14 |
| microarray input | 12 |
| `normalizeBetweenArrays` / quantile normalisation | 7 |
| trend / robust eBayes | 6 |
| gene-set tests (camera/roast/fry/romer/goana) | 3 |
| `voomWithQualityWeights` / sample quality weights | 2 |
| `treat`, `contrasts.fit`/`makeContrasts` named | 1 / 1 |

Exposure by finding: LI1 needs `arrayWeights(method="reml")` on weighted data or
`voomWithQualityWeights(method="reml")` today (2 cohort papers name quality weights; the
cache does not record the method), and will need only `voomLmFit(sample.weights=TRUE)` from
limma 4.0.0 (Bioconductor 3.24, October 2026); LI2 needs limma 3.68.x (April 2026 onwards —
only the 34 papers from 2026 could have used it, none of which names 3.68) or edgeR 4.10.x
and a DGEList carrying an `offset` element (cqn, EDASeq, RUVSeq, csaw, `scaleOffset`; none
identifiable from the cache).

**Profiling caveat.** As for the Seurat, Scanpy and edgeR audits, this session had no route
to Europe PMC, so `limma_profile.py` ran in `--offline` mode over the survey's stored
evidence snippets; every record in `limma_profiles.jsonl` is `source: survey_cache` and
every count above is a lower bound. Rerun without `--offline` from a host with Europe PMC
access to replace them with full-text records.

## Filing channel (read before anything is sent)

- limma is a Bioconductor package: its git lives at `git.bioconductor.org` (not reachable
  from this session; `bioc/limma` on GitHub is a read-only mirror with issues disabled),
  there is no `CONTRIBUTING`, no issue or PR template and no linter. `vignettes/intro.Rmd`
  line 39: "Further questions about the package should be directed to the Bioconductor
  support site"; `DESCRIPTION` names the maintainer (Gordon Smyth, `smyth@wehi.edu.au`) and
  the author of the 4.0.0 C code (Lizhong Chen). The channel is therefore a support-site
  post tagged `limma` with a reproducible example and the patch attached as a diff, or the
  same by e-mail — never a cold PR. The support site is not reachable from this session and
  must be searched before posting.
- The project's changelog is `inst/doc/changelog.txt` (dated entries per version, written
  by the maintainers) with a release summary in `inst/NEWS.Rd`; its tests are
  `tests/limma-Tests.R` with `limma-Tests.Rout.save` (`R CMD Rdiff`) and, on `devel`,
  stand-alone `stopifnot` scripts (`tests/lm-series-c.R` etc.) — the patches add two such
  scripts.
- No fork `cindykrafft/limma` exists (GitHub repository search 2026-09-13), so no
  `upstream-declines-ai-contributions` topic applies. The GitHub tracker search
  (`mcp__github__search_issues`, two phrasings) found nothing relevant; limma has no GitHub
  tracker.
- **The kit is in [`upstream/`](upstream/)**: two support-site posts (LI1 first, LI2 second —
  the two-filing cap), three `git am`-clean patches (LI1 against `devel` and
  `RELEASE_3_23`, LI2 against `devel`), each with a test that fails on the unmodified code,
  and the list of documents read. Nothing has been filed.

## Files

| file | what |
|---|---|
| `limma_profile.py`, `limma_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/statistical-core.md` | the review: LI1–LI2, N1–N9, withdrawn W1–W4, held-up list, not-audited list |
| `verify/rlib.sh` | version selector for the seven builds and the two patched builds |
| `verify/lm1_arrayweights_prwts_convergence.R` (+ `.v<version>.out` ×9) | LI1: equal-weights equivalence, iteration traces, `voomWithQualityWeights` and `voomLmFit` end to end; patched builds |
| `verify/lm2_voom_offset_double_count.R` (+ `.out` ×6), `verify/lm2_edger_voomlmfit.R` (+ `.out` ×2) | LI2: minimal example, two-group effect, cqn-style offset, `voomLmFit`; edgeR 4.0.16 / 4.10.5 |
| `verify/heldup_lmfit_ebayes.R` (+ `.out` ×3) | held-up: `lmFit` vs WLS, `contrasts.fit`, `eBayes` vs the Smyth 2004 port, B-statistic, moderated F, `treat`, `topTable`, `decideTests`; N3, N4 |
| `verify/heldup_voom.R` (+ `.out` ×5) | held-up: `voom` vs the Law 2014 port, `voomWithQualityWeights`, `devel` vs edgeR `voomLmFit`; N9 |
| `verify/heldup_dupcor_gls.R` (+ `.out` ×2) | held-up: `duplicateCorrelation` vs lme4, consensus rule, C vs R, `gls.series` vs GLS closed form |
| `verify/heldup_camera_fry.R` (+ `.out` ×3) | held-up: `camera` vs the Wu & Smyth port, `fry` vs `roast`, `zscoreT`; N5, N8 |
| `verify/heldup_norm_batch.R` (+ `.out` ×3) | held-up: `normalizeQuantiles`, `removeBatchEffect`, `normalizeCyclicLoess` |
| `verify/heldup_robust_ebayes.R` (+ `.out` ×3) | held-up / N6: robust eBayes on planted outliers, both estimators |
| `verify/note_fitfdist_unequal_bounds.R` (+ `.out` ×3) | N1 |
| `verify/note_contrasts_fit_weights.R` (+ `.out` ×3) | N2 |
| `upstream/` | filing kit: support-site posts, patches for `devel` and `RELEASE_3_23`, PR-body sections, documents read |

Harnesses need the builds described in `verify/rlib.sh` (sources from
`archive.ubuntu.com/ubuntu/pool/universe/r/r-bioc-limma/`, mirror branches from
`github.com/bioc/limma`; `R CMD INSTALL --no-docs --library=<lib>`), R 4.3.3 with statmod
1.5.0, lme4 1.1-35.1 and edgeR 4.0.16 from apt, and the edgeR 4.10.5 build of the edgeR
audit for `lm2_edger_voomlmfit.R`. Europe PMC, CRAN, Bioconductor and `git.bioconductor.org`
were unreachable; the Bioconductor git was read through the GitHub mirror.

## Next steps

1. Search the Bioconductor support site for "arrayWeights reml" and "voom offset", then post
   LI1 from the kit with the `RELEASE_3_23` patch attached (and the `devel` one linked);
   record the post URL and every maintainer reply here and in the top-level table.
2. When LI1 has an answer, post LI2 (the semantics question: `voom()` vs the new
   `voomLmFit()` reading of a DGEList offset) with the `devel` patch.
3. If the maintainers respond, raise N1 (the df.prior floor of the unequal-df estimator) and
   N2 (a help-page sentence on the approximation for voom users) as questions.
4. Full-text profiling when Europe PMC is reachable (which papers used quality weights or
   offsets decides the exposure).
