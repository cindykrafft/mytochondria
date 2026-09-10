# limma audit against 234 published papers (2021–2026)

_Generated 2026-09-10 against the Bioconductor git of `limma` (read through the
`bioc/limma` mirror): `devel` @ `57a8de72` (3.99.0, 2026-08-30) and `RELEASE_3_23` @
`825d1c83` (3.68.5, 2026-08-10, the current release branch). Focus: the pipeline the
cohort runs — `lmFit`, `eBayes`/`squeezeVar`/`fitFDist`, `treat`, `topTable`,
`decideTests`, `voom`/`voomWithQualityWeights`/`voomLmFit`, `arrayWeights`,
`duplicateCorrelation`, `contrasts.fit`, `camera`/`roast`/`fry`,
`normalizeBetweenArrays`, `removeBatchEffect` — verified by executing seven shipped
versions against independent ports of the published methods._

## What this is

The six-journal survey found **234 papers** (2021–2026) that used limma — the third
most-used differential-expression package in the cohort after DESeq2 and edgeR, and the
one with the widest reach outside RNA-seq (16 proteomics/metabolomics papers, 10
microarray, 9 methylation, 24 ATAC/ChIP/CUT&RUN). Its statistical core was read in full
on the two commits above and every suspicion was run through the installed package:
R 4.3.3 with limma 3.58.1 (the apt `r-bioc-limma` on this host), 3.34.0, 3.42.2, 3.62.2
and 3.68.4 (Ubuntu pool source tarballs), 3.68.5 and 3.99.0 (mirror branches), each in
its own library (`verify/rlib.sh`), against ports written from the papers (Smyth 2004
moderated t and B-statistic; Law et al 2014 voom; Wu & Smyth 2012 camera; Phipson et al
2016 robust hyperparameters; Smyth 2005 `duplicateCorrelation`, cross-checked against
`statmod::mixedModel2Fit` and `lme4`) or closed-form arithmetic on synthetic data with
planted truth.

limma is written by statisticians and it shows: the moderated-t machinery, the voom
mean–variance model, the gene-set tests, the linear-model C backends new in devel, the
normalisation and the multiple-testing arithmetic all reproduce the published methods
to between `1e-13` and machine precision wherever a reference could be computed. One
thing does not, and it is one term: the Fisher-scoring **convergence criterion** in the
prior-weights branch of `arrayWeights(method="reml")` is divided by the number of genes
a second time, so the iteration stops after one to three steps and returns unconverged
sample weights. It is live on every version the cohort names from 3.42.2 on, it is
today reached only by an explicit `method="reml"` — and in limma devel it becomes the
default sample-weight path of `voomLmFit()`.

## Findings (details and line citations in [`component-reviews/statistical-core.md`](component-reviews/statistical-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **L1** | **CONFIRMED on 3.42.2, 3.58.1, 3.62.2, 3.68.4, 3.68.5 and `devel` 3.99.0; 3.34.0 unaffected** | **now** (before limma 4.0.0 ships) | `.arrayWeightsPrWtsREML` averages the REML information and score over genes and then divides the Fisher-scoring convergence criterion by `(ngenes + prior.n)` a *second* time (release `R/arrayWeightsPrWtsREML.R:65-66,77`; devel C kernel `src/awreml.c:357,359,403`), so the criterion is 3010× too small on 3000 genes and the scoring stops after 1–3 iterations at the default `tol = 1e-5`. `arrayWeights(y, design, weights=matrix(1,...), method="reml")` then differs from `arrayWeights(y, design, method="reml")` on identical data by **0.549** (independent REML score `4.43e-02` against `2.98e-04`); with genuine prior weights it differs from the converged fit by **0.891**. On voom RNA-seq data with planted sample quality the sample weights are off by 4 % and the DE calls change: **16 genes at BH < 0.05 (9 at BH < 0.01) against 18 (10) with converged weights**. `arrayWeights(method="auto")` and `voomWithQualityWeights()` default to `genebygene` and are unaffected; **limma devel's `voomLmFit(sample.weights=TRUE)` calls `method="reml"` and is affected** (`R/voomLmFit.R:238,309`, NEWS 4.0.0). One-term fix with tests for both branches in the [kit](upstream/). |
| N1–N7 | notes | held | `contrasts.fit`'s documented approximation under voom weights is large (`stdev.unscaled` off by up to 20.8 %, 5 genes at BH < 0.05 against 2 from an exact refit); `topTable` `<=` vs `decideTests` `<` at the cutoff (233 vs 232 genes); `zscoreT`'s Hill approximation (`1.8e-04` at df = 4); a dead inner `tol` default; `normalizeCyclicLoess` not converged at the default 3 iterations (residual trend `9.5e-03` against `1.6e-03` at 10); `fitFDistUnequalDF1` is moments not ML (log-lik `1.2e-03` below `optim`); `robust=TRUE` gives one gene `df.prior = 0.203` on clean data. |

Two of my own suspicions were withdrawn by execution (that the patch left the weighted
path unconverged — the test threshold was wrong, not the fix; and that every voom
sample-weight path is affected — the released defaults route to `genebygene`). Both are
recorded in the review.

**Held up under execution** (all on devel 3.99.0, all also on 3.42.2, 3.58.1 and 3.68.5,
two also on 3.34.0): `fitFDist` returns `df.prior = 4.000740` and `s2.prior = 0.089410`
against an independent Smyth-2004 port's identical values (planted truth 4 and 0.0900);
`eBayes` `s2.post`, moderated `t`, `df.total`, p, the B-statistic and `var.prior` all
reproduce the port to `≤ 7.1e-15`; the moderated F equals `t^2` for one coefficient
(`2.8e-13`) and its p equals `pf` to `1.2e-15`; `treat` `2.2e-16`; the `trend=TRUE` loess
prior `1.8e-15`; the winsorised moments behind `robust=TRUE` match quadrature to
`6.7e-16` and correctly give all 100 planted outlier genes the smallest `df.prior`;
`topTable`'s `adj.P.Val` equals `p.adjust(...,"BH")` to `1.6e-15` and its confidence
interval equals `qt(0.975, df.total)*se` to `1.8e-15`; genes with 0 residual df get NA
and are excluded from BH; `voom`'s `E`, weights and adaptive span reproduce a Law-2014
port to `1.1e-15` and `voomWithQualityWeights` equals the documented two-pass recipe
exactly; `lm.series` and `gls.series` (including the new C backends and their
`nthreads=4` paths) equal a per-gene `lm.wfit`/GLS reference to `≤ 4e-15` in
coefficients, `stdev.unscaled`, `sigma`, `df.residual` and NA pattern, with
rank-deficient per-gene designs handled; `duplicateCorrelation` equals a `statmod`
reference to `1.55e-15` and `lme4` REML to `1.17e-06`, and its trimmed-Fisher consensus
rule to `1.11e-16`; `camera` equals a Wu–Smyth port to `6.0e-10`, `fry` to `3.3e-16`,
`roast` exactly on a matched RNG stream, and all three are calibrated under the null
(2.5–4.0 % at α = 0.05); `normalizeQuantiles`, `loessFit` (against `stats::lowess`,
`0.00e+00`) and `removeBatchEffect` (against the closed form, `0.0e+00`) reproduce;
`decideTests`' `separate`, `global`, `hierarchical` and `nestedF` all have **0**
mismatches against independent implementations; `arrayWeights` *without* prior weights
recovers planted `1/sd^2` to `max |log ratio| = 0.080`.

**Not audited**: two-colour reading and background correction, `normalizeWithinArrays`,
`diffSplice`, `romer`/`mroast`, `goana`/`kegga` beyond the project's own tests,
`propTrueNull`, `vooma`, `genas`, plotting, devel's new `poisfit`.

## How the papers use limma (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| edgeR also used (TMM / `calcNormFactors`) | 70 |
| batch / covariate in the design | 69 |
| DESeq2 also used | 69 |
| voom (any variant) | 54 |
| pseudo-bulk / single-cell | 46 |
| adjusted p / FDR / BH | 44 (cutoffs: 0.05 ×16, 0.10 ×1) |
| `lmFit` / `eBayes` / `topTable` named | 35 |
| ATAC / ChIP / CUT&RUN | 24 |
| R version stated | 23 |
| limma version stated | 22 |
| log fold-change cutoff | 16 (1 ×3, 2 ×1) |
| proteomics / metabolomics | 16 |
| `removeBatchEffect` | 14 |
| Bioconductor version stated | 11 |
| microarray (Affy / Illumina / Agilent) | 10 |
| methylation / EPIC / 450K | 9 |
| `robust` / `trend` eBayes | 9 |
| `duplicateCorrelation` / block | 7 |
| quantile / cyclic-loess normalisation | 7 |
| `voomWithQualityWeights` / `voomLmFit` | 2 |
| `contrasts.fit` / `makeContrasts` | 2 |
| `goana` / `kegga` | 2 |
| `camera` / `roast` / `fry` / `romer` | 1 |
| `treat` / fold-change threshold test | 1 |

Versions named: 3.46.0 ×6, 3.58.1 ×5, 3.34.9 ×3, 3.48.3 ×3, 3.50.0 ×3, 3.62.2 ×2,
3.60.3 ×2, 3.60.6 ×2, 3.54.2 ×2, 3.50.3 ×2, 3.42.2 ×2, 3.40.6 ×2, 3.38.3 ×2, 3.60.2 ×2,
then singletons down to 3.5.4.

**Exposure by finding.** L1 needs `arrayWeights(..., weights=, method="reml")`, which no
released default path takes: the two papers naming `voomWithQualityWeights` /
`voomLmFit` were on released limma, where those functions use `genebygene`. Its
importance is forward-looking — limma devel 4.0.0 (NEWS date 2026-10-30) makes
`method="reml"` the default sample-weight estimator inside `voomLmFit()`, the package's
recommended RNA-seq entry point, so the finding is worth filing *before* that release
rather than after. N1 (`contrasts.fit` under voom weights, non-orthogonal contrasts)
touches the 2 papers naming `contrasts.fit`/`makeContrasts` together with voom, and
silently more: `contrasts.fit` after `voom` is the standard limma idiom and the survey
cache does not record it.

**Profiling caveat.** As for the Scanpy, edgeR and Seurat audits, this session had no
route to Europe PMC, so `limma_profile.py` ran in `--offline` mode over the survey's
stored evidence snippets; every record in `limma_profiles.jsonl` is
`source: survey_cache` and every count above is a **lower bound**. Rerun without
`--offline` from a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- limma is a Bioconductor package. Its canonical git is `git.bioconductor.org` (not
  reachable from this session); **`github.com/bioc/limma` is a read-only mirror with no
  issue tracker and no pull requests**. There is no `CONTRIBUTING`, no issue or PR
  template, no `.github/` directory, no linter and no changelog convention beyond the
  maintainer-written `inst/NEWS.Rd`. `vignettes/intro.Rmd:39`: "Further questions about
  the package should be directed to the Bioconductor support site".
- The channel is therefore a **Bioconductor support-site post tagged `limma`**
  (https://support.bioconductor.org) with a reproducible example and the patch attached
  as a diff, or the same by e-mail to the maintainer named in `DESCRIPTION` (Gordon
  Smyth, `smyth@wehi.edu.au`). Never a cold PR — the mirror cannot take one.
- **The support site is unreachable from this session** (as are CRAN, Bioconductor and
  `git.bioconductor.org`), so it could not be searched for prior reports. It must be
  searched for "arrayWeights" and "sample weights" before the post goes out.
- `mcp__github__search_issues` was run with three phrasings; it returned nothing about
  limma (limma has no GitHub tracker). No fork `cindykrafft/limma` exists, so no
  `upstream-declines-ai-contributions` topic applies.
- **The kit is in [`upstream/`](upstream/)**: the L1 support-site post with a minimal
  example run on 3.68.5 and 3.99.0, and two `git am`-able patches (fix + test, and the
  saved test output on the release branch) against `devel` and `RELEASE_3_23`. There is
  **no PR body**, because there is no repository that accepts one.

## Files

| file | what |
|---|---|
| `limma_profile.py`, `limma_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/statistical-core.md` | the review: L1, N1–N7, withdrawn W1–W2, held-up list, not-audited list |
| `verify/rlib.sh` | version selector for the seven builds and the two patched ones |
| `verify/l1_arrayweights_reml_convergence.R` (+ `.out` ×9) | L1: the two REML paths traced and compared, an independent REML+prior score, the effect of `tol`; on 7 versions and both patched builds |
| `verify/l1_voom_sample_weights_magnitude.R` (+ `.out` ×6) | L1 magnitude: voom RNA-seq with planted sample quality, sample weights and DE counts against the converged fit and `genebygene` |
| `verify/l1_exposure_default_paths.R` (+ `.out` ×6) | L1 exposure: which shipped call paths reach the branch (`auto`, `voomWithQualityWeights`, `voomLmFit`) |
| `verify/heldup_ebayes_core.R` (+ `.out` ×4) | held-up: `fitFDist`, `squeezeVar`, `eBayes`, B-statistic, F, `treat`, `topTable`, `trend`, `robust`, NA handling |
| `verify/heldup_fitfdist_unequal.R` (+ `.out` ×4) | held-up / N6: `fitFDistUnequalDF1`, `squeezeVar` with unequal df, the robust variant |
| `verify/heldup_voom.R` (+ `.out` ×5) | held-up / N1: voom port, adaptive span, `voomWithQualityWeights`, `contrasts.fit` under weights |
| `verify/heldup_lmfit_c_backend.R` (+ `.out` ×4) | held-up: `lm.series` / `gls.series` with NAs, weights, rank deficiency, contrasts, threads |
| `verify/heldup_duplicatecorrelation.R` (+ `.out` ×4) | held-up: genewise and consensus correlation vs `statmod` and `lme4` |
| `verify/heldup_genesets.R` (+ `.out` ×5) | held-up / N3: `camera`, `fry`, `roast`, `zscoreT`, null calibration |
| `verify/heldup_normalize_batch.R` (+ `.out` ×4) | held-up / N5: quantile and cyclic-loess normalisation, `loessFit`, `removeBatchEffect` |
| `verify/heldup_decidetests_arrayweights.R` (+ `.out` ×4) | held-up / N2: the four `decideTests` methods, `classifyTestsF`, `arrayWeights` without prior weights |
| `upstream/` | filing kit: support-site post, patches for `devel` and `RELEASE_3_23`, documents read |

Harnesses need the builds described in `verify/rlib.sh` (sources from
`archive.ubuntu.com/ubuntu/pool/universe/r/r-bioc-limma/`, mirror branches from
`github.com/bioc/limma`; `R CMD INSTALL --no-docs --library=<lib>`), R 4.3.3 and the apt
`r-cran-statmod` 1.5.0, `r-cran-lme4` 1.1.35.1 and `r-bioc-edger` 4.0.16. Europe PMC,
CRAN, Bioconductor, `git.bioconductor.org` and `support.bioconductor.org` were all
unreachable; the Bioconductor git was read through the GitHub mirror.

## Next steps

1. Search the Bioconductor support site for prior reports of `arrayWeights` /
   sample-weight convergence, then post `upstream/issue-l1-arrayweights-reml-convergence.md`
   with the `RELEASE_3_23` patch attached and the `devel` one linked, tag `limma`.
   It is worth doing before limma 4.0.0 ships (NEWS date 2026-10-30), because that
   release makes the affected branch `voomLmFit`'s default.
2. Record the post URL and every maintainer reply here and in the top-level status
   table. Nothing else goes out until they reply (filing cap: two unanswered per
   repository).
3. If they respond, raise N1 (the size of the `contrasts.fit` approximation under voom
   weights, with the harness) as a help-page question, and N2 as a one-line convention
   note shared with edgeR's N3.
4. Extend the review to `diffSplice`, `romer` and `vooma`, and rerun the profiler
   without `--offline` when Europe PMC is reachable.
