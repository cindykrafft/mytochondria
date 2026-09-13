# Component: limma statistical core (Bioconductor `devel` @ `57a8de72`, 3.99.0, 2026-08-30; `RELEASE_3_23` @ `825d1c83`, 3.68.5, 2026-08-10)

Read in full on `devel` @ `57a8de72` (the commit that adds the 4.0.0 C backends):
`R/lmfit.R` (`lmFit`, `lm.series`, `gls.series`, `mrlm`), `src/lm.c`, `src/gls.c`, `src/qr.c`,
`R/contrasts.R`, `R/ebayes.R` (`eBayes`, `tmixture.*`), `R/squeezeVar.R`, `R/fitFDist.R`
(+ `trigammaInverse`), `R/fitFDistRobustly.R`, `R/fitFDistUnequalDF1.R`, `R/treat.R`,
`R/voom.R`, `R/voomWithQualityWeights.R`, `R/voomLmFit.R`, `src/poisson.c`,
`R/arrayWeights.R`, `R/arrayWeightsGeneByGene.R`, `R/arrayWeightsREML.R`,
`R/arrayWeightsPrWtsREML.R`, `src/awreml.c`, `R/dups.R` (`duplicateCorrelation`),
`src/dupcor.c`, `R/toptable.R`, `R/decidetests.R` (`decideTests`, `classifyTestsF`),
`R/geneset-camera.R`, `R/geneset-roast.R`, `R/geneset-fry.R`, `R/lmEffects.R`,
`R/removeBatchEffect.R`, `R/norm.R` (`normalizeBetweenArrays`, `normalizeQuantiles`,
`normalizeCyclicLoess`), `R/loessFit.R`, `R/chooseLowessSpan.R`, `R/weightedLowess.R`,
`src/R_exports.c`. The same functions were read on `RELEASE_3_23` @ `825d1c83` where they
differ (`git diff -w --ignore-cr-at-eol`: the C backends, `voomLmFit.R`, `lmfit.R`,
`dups.R`, `arrayWeightsPrWtsREML.R`; `voom.R`, `ebayes.R`, `contrasts.R`, `toptable.R`,
`decidetests.R` and the gene-set code are byte-identical modulo CRLF).

Every suspect was **executed on the shipped code**: R 4.3.3 with seven limma builds in
private libraries (`../verify/rlib.sh`): 3.58.1 (the apt package on this host), 3.34.0,
3.42.2, 3.62.2 and 3.68.4 (Ubuntu pool source tarballs), 3.68.5 (`RELEASE_3_23`) and 3.99.0
(`devel`) from the `bioc/limma` read-only mirror, plus the two patched builds of the kit.
References are closed-form linear algebra in R that does not call the function under test
(per-gene `lm.wfit`/GLS, `C'VC` contrast covariances, BH), independent ports written from
the papers (Smyth 2004 moderated t and hyperparameter moments; Law et al 2014 voom;
Wu & Smyth 2012 camera; McCarthy & Smyth 2009 treat; Ritchie et al 2006 / Smyth 2002 REML
array weights), lme4 REML fits for the genewise correlations, and edgeR 4.0.16 / 4.10.5 for
`voomLmFit`. Harnesses and captured output are in `../verify/`.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### LM1 — CONFIRMED on 3.42.2, 3.58.1, 3.62.2, 3.68.4, 3.68.5 and `devel` (3.34.0 predates the routine): `arrayWeights(method="reml")` with prior weights stops after one or two Fisher-scoring steps because its convergence criterion is divided by `ngenes+prior.n` twice

**Code.** `arrayWeights()` dispatches to `.arrayWeightsREML()` when there are no prior
weights and no missing values, and to `.arrayWeightsPrWtsREML()` when prior weights are
present (`R/arrayWeights.R:87-91, 105-107`; `method="reml"` forces the same split). The two
routines run the same Fisher-scoring iteration (Smyth 2002) but their stopping rules are on
different scales. `.arrayWeightsREML()` sums the per-gene score and information
(`R/arrayWeightsREML.R:81-82`, `info2 <- ngenes*info2 + prior.n*crossprod(Z2)`) and stops on

```r
convcrit <- crossprod(dl,gamstep) / ngam / (ngenes+prior.n)      # R/arrayWeightsREML.R:89
```

`.arrayWeightsPrWtsREML()` first divides the accumulated score and information by
`ngenes+prior.n` (3.68.5 `R/arrayWeightsPrWtsREML.R:65-66`; `devel` `src/awreml.c:357-359`)
and then divides the same product by it again:

```r
convcrit <- crossprod(dl,gamstep) / (ngenes+prior.n) / ngam     # 3.68.5 R/arrayWeightsPrWtsREML.R:77
convcrit = num / denom / ngam;                                    /* devel src/awreml.c:403, denom = ngenes+prior_n (l.253) */
```

Since `solve()` is scale-invariant the step `gamstep` is identical in both routines, so for
the same state the prior-weights criterion is exactly `ngenes+prior.n` times smaller and
the default `tol=1e-5` (`R/arrayWeights.R:1`) is met after one or two iterations. The
`devel` C backend (`src/awreml.c`, 2026) reproduces the 2019 R code faithfully, including
this.

**Verified** (`../verify/lm1_arrayweights_prwts_convergence.R`, nine `.out` files). 10,000
genes, 8 arrays, true precisions 4:2:1:0.5, no prior weights versus a weight matrix of ones
(the same model):

| | 3.42.2, 3.58.1, 3.62.2, 3.68.4, 3.68.5, devel | patched 3.68.5 / devel |
|---|---|---|
| REML, no weights (5 iterations) | 2.8765 1.4413 0.6935 0.3530 2.7960 1.4000 0.7246 0.3474 | same |
| REML, weights = 1 | 2.4544 1.4716 0.7435 0.3750 2.4129 1.4355 0.7750 0.3699 (2 iterations) | equal to 1.8e-14 (5 iterations) |
| max relative difference | 0.1468 | 2.2e-14 |
| iteration-1 `convcrit`, REML / prior-weights | 0.176843 / 1.76666e-05, ratio 10010.00 = ngenes+prior.n | — |
| same with `tol` divided by ngenes+prior.n | equal to REML to 1.8e-14 | — |

End to end, `voomWithQualityWeights(method="reml")` on 8,000 simulated genes with two
low-quality samples returns sample weights 0.0991 2.2100 2.1469 2.0679 0.1004 2.1569
2.1343 2.2235 at the default tolerance against 0.0888 2.3114 2.2198 2.1118 0.0906 2.2398
2.2131 2.3159 converged (max relative difference 0.117), and 137 genes at adj.P < 0.05
against 183 (of 800 true). The patch removes the extra division; with it the two routines
agree to rounding on equal weights and the 5-iteration solution is returned.

**Reach.** Today the path is reached only by `arrayWeights(..., method="reml")` on an
object carrying weights (a voom `EList`) or `voomWithQualityWeights(method="reml")` (its
default is `"genebygene"`, `R/voomWithQualityWeights.R:1`); `method="auto"` picks
gene-by-gene whenever weights are present. On `devel`, however, the new
`voomLmFit(sample.weights=TRUE)` calls `arrayWeights(..., method="reml")` with the voom
weights whenever no df are lost to exact zeros (`R/voomLmFit.R:238, 309`; `changelog.txt`
3.99.0: "calls arrayWeights() with method="reml" if there is no loss of df"), so at the
4.0.0 release (2026-10-30) the under-converged path becomes the default sample-weight
estimator of the function the help pages now steer voom users to. Section D of the harness
shows `devel voomLmFit(sample.weights=TRUE)` producing 0.09131 2.24221 2.21891 2.14128
0.09201 2.18609 2.25710 2.26420 on the same counts (its two-pass scheme partly compensates;
0.069 from the converged single-pass weights). edgeR 4.0.16's `voomLmFit` uses
`method="auto"` and is not affected (`../verify/heldup_voom.vdevel.out`, section D:
sample weights agree to 1e-3 between the two implementations in that setting).

Cohort: 2 papers name sample-specific quality weights and 54 name voom (lower bounds).
Filed first in the kit.

### LM2 — CONFIRMED on 3.68.4, 3.68.5 and `devel` (`voom()`) and on edgeR 4.10.5 (`voomLmFit()`); 3.58.1, 3.62.2 and edgeR 4.0.16 unaffected (no offset support): `voom()` counts the library sizes twice when a DGEList carries an edgeR-style offset matrix

**Code.** Offset support entered `voom()` in 3.68.0 (2026-04-11, `R/voom.R:10`). A
`DGEList` offset is picked up automatically (`R/voom.R:22`), row-mean corrected and
*added* to `log(lib.size)`:

```r
offset.prior <- offset - rowMeans(offset)                          # R/voom.R:58
lib.size.matrix <- exp(log(lib.size.matrix)+offset.prior)          # R/voom.R:66
```

In edgeR an offset matrix is the log *effective* library size — `scaleOffset()` puts it on
the scale of `log(lib.size)`, and `glmFit()` and (since 4.10.5, the edgeR audit's EG1 revert)
`cpm()` use `exp(offset)` in place of the library sizes. Row-centring such an offset removes
its per-gene mean but not its per-column `log(L_j)`, so `voom()` uses
`L_j · L_j/geomean(L) · exp(d_gj − mean_j d_gj)`: the library sizes squared. The help page
documents the construction (`man/voom.Rd:30-36, 105-106`: an edgeR-style offset "will be
row-mean corrected and treated as a prior offset matrix"), so this is documented
behaviour — but it is wrong for the object it is documented for, and `devel`'s
`voomLmFit()` takes the opposite reading of the same DGEList slot: "If not NULL, then the
library sizes will be set to `exp(offset)`" (`man/voomLmFit.Rd:61-65`,
`R/voomLmFit.R:122`; NEWS 4.0.0: "voomLmFit() now gives priority to `offset` over
`offset.prior` or `lib.size`"). edgeR 4.10.5's `voomLmFit` still carries the `voom()`
construction (deparsed in `../verify/lm2_edger_voomlmfit.R`).

**Verified** (`../verify/lm2_voom_offset_double_count.R`, six `.out` files;
`lm2_edger_voomlmfit.R`, two). The trivial edgeR offset — `y$offset = log(lib.size)`,
what `scaleOffset(y, 0)` stores — must be a no-op:

| library sizes 1e6, 4e6, 2e6, 8e6 | `voom(DGEList)$E − voom(counts, lib.size)$E` per column |
|---|---|
| 3.68.4, 3.68.5, devel, edgeR 4.10.5 `voomLmFit` | 1.5, −0.5, 0.5, −1.5 log2 units = −log2(lib.size/geomean) |
| library sizes actually used / lib.size | 0.354, 1.414, 0.707, 2.828 = lib.size/geomean |
| 3.58.1, 3.62.2, edgeR 4.0.16, devel `voomLmFit`, patched devel | 0 (8.9e-16) |

With 6,000 simulated genes and group 2 sequenced 2.5× deeper (an offset carrying only the
column sums), the group logFC of every gene is shifted by −1.5068 (median; range −1.5746
to −1.4243; log2 of the groups' library-size ratio 1.5119) and 5,374 genes are called at
adj.P < 0.05, all "down", against 37 in the reference run (500 true). With a cqn/EDASeq-style
offset `log(lib.size) + d_gj` the returned `E` equals
`log2((counts+0.5)/(lib.size²/geomean · exp(d) + 1)·1e6)` to 5.3e-15 and differs from
`log2((counts+0.5)/(exp(offset)+1)·1e6)` by up to 1.114; passing the same `d` as
`offset.prior` reproduces the edgeR reading exactly. The devel patch makes `voom()` use
`exp(offset)` as `voomLmFit()` does (`../verify/lm2_voom_offset_double_count.vdevel-patched.out`:
0 difference, 37 vs 37 genes).

**Reach.** Any `voom(y, design)` on a DGEList whose `offset` element was set by
`scaleOffset()`, cqn, EDASeq/RUVSeq or csaw workflows, on limma 3.68.x (Bioconductor 3.23,
since 2026-04-28) — and `edgeR::voomLmFit` 4.10.x on the same objects; explicit
`offset.prior` users are unaffected. The cohort cache cannot identify offset users (none of
the 234 evidence snippets names cqn or EDASeq). Filed second in the kit, as a request to
align `voom()` with the new `voomLmFit()` semantics.

## Notes (design choices, documented approximations, cosmetic)

- **N1 — `fitFDistUnequalDF1` bounds `df.prior` to (2, 9998).** The estimator used by
  `squeezeVar`/`eBayes` whenever the residual df are unequal (`R/squeezeVar.R:25, 38` — any
  missing value, or `voomLmFit` rows with structural zeros) maximises a profile likelihood
  over `optimize(minusTwiceLogLik, c(1/2, 0.9998))` with `df2/2 = par/(1−par)`
  (`R/fitFDistUnequalDF1.R:98-99`). `../verify/note_fitfdist_unequal_bounds.R`: with planted
  prior df 0.5 / 1 / 1.5 the new estimator returns 2.0006 / 2.0004 / 2.0005 with prior scale
  0.501 / 0.102 / 0.063 for a true 0.05 (the legacy moment estimator: 0.4927 / 0.9927 /
  1.4956, scale 0.0494 / 0.0501 / 0.0503); median posterior-variance ratio new/legacy 1.39 /
  1.11 / 1.04; a gene with variance 5× the prior at true d0 = 0.5 gets a t-statistic 0.835
  of the legacy one. For true d0 ≥ 2 the two agree (3: 2.976 vs 2.961; 20: 20.46 vs 21.14),
  and true Inf comes back as 8134.8 (legacy Inf). Undocumented; a design choice for the
  maintainers to name (prior df below 2 are rare in practice).
- **N2 — `contrasts.fit` approximation under precision weights**, documented
  (`man/contrasts.fit.Rd:35-39`). On a non-orthogonal design (three groups plus a batch
  column) with voom weights from strongly unequal library sizes,
  `../verify/note_contrasts_fit_weights.R`: the approximate `stdev.unscaled` exceeds the
  exact `sqrt(diag(C'(X'WX)⁻¹C))` by a median 4.6 % (quantiles 1 %: 1.011, 99 %: 1.157, max
  1.2095), moderated t are 0.83–1.00 of exact, and 5 genes reach adj.P < 0.05 against 15
  exactly; coefficients are exact; on a one-way design the approximation is exact (2.2e-16).
  `devel`'s `lmFit(contrasts=)` and `voomLmFit(contrasts=)` return the exact values
  (2.2e-16). Worth a sentence in the voom help pages once 4.0.0 is out.
- **N3 — `<` vs `<=`.** `decideTests.MArrayLM` uses `p < p.value` (`R/decidetests.R:123, 129`)
  while `decideTests.default` (`:89`) and `topTable` (`R/toptable.R:115, 234`) use `<=`; the
  logFC cutoff is `> lfc` in `decideTests` (`:165`) and `.topTableF` (`R/toptable.R:111`)
  but `>= lfc` in `.topTableT` (`:234`). Only exact ties matter
  (`../verify/heldup_lmfit_ebayes.R`, section F, shows the default method at an exact 0.05).
- **N4 — moderated F df.** `eBayes` caps the t-test df at the pooled residual df
  (`R/ebayes.R:64`) but `classifyTestsF` uses `df.prior + df.residual` uncapped for the
  F-test (`R/decidetests.R:190`, `R/ebayes.R:22-26`). Reachable only when `df.prior` is
  finite and exceeds the pooled df: a 12-gene fit with df.prior 164.3 uses df2 = 171.3 for F
  and 84 for t, moving F p-values by up to 4.4e-3 (`heldup_lmfit_ebayes`, section G).
- **N5 — `roast`'s Bailey t-to-z approximation** (`.zscoreTBailey`, `R/geneset-roast.R:270-272,
  380`, the default `approx.zscore=TRUE, legacy=FALSE`) is off by up to 2.6e-2 at df = 3,
  7.4e-3 at df = 10 and 1.1e-4 at df = 100 against `qnorm(pt())`; Hill's approximation used by
  `camera` is within 7.9e-4 / 4.7e-7 / 4.0e-11 (`heldup_camera_fry`, section C). The same
  transform is applied to observed and rotated statistics, so it is self-consistent.
- **N6 — robust estimation on the unequal-df path.** With 200 planted 30×-variance genes,
  `eBayes(robust=TRUE)` (legacy path) gives them df.prior 0.852 (median) against 4.22 for
  the rest and squeezes their variances to 0.879 of the sample value; `legacy=FALSE,
  robust=TRUE` returns a single df.prior 3.542 (no gene-specific shrinkage, its right-outlier
  test fires on none of them) and squeezes them to 0.640, the same as the non-robust 0.641
  (`heldup_robust_ebayes`, section C). Two different robust estimators, both documented as
  such; no false discoveries in either.
- **N7 — voom trend x-axis under offsets** (by reading). `voom.R:96` and `voomLmFit.R:195`
  place the mean-variance trend at `Amean + mean(log2(lib.size+1)) − log2(1e6)` with the
  column-sum library sizes even when an offset matrix sets the effective library sizes, so
  the lowess curve is translated along x by the mean log difference between the two; `voom`
  and `voomLmFit` agree on this, and offsets scaled by `scaleOffset()` make the difference
  small. Not executed beyond the kit test (which supplies `lib.size` alongside `offset` for
  the weights comparison).
- **N8 — `fry` vs `roast`** agree for the directional test only in the limit the code
  states (`R/geneset-fry.R:235-236`: `nrot=Inf` and `prior.df=Inf`): 0.848 vs 0.858 and
  0.285 vs 0.303 with finite prior df and 49,999 rotations; the beta-approximated mixed
  p-values differ more (0.0101 vs 0.0758). Documented approximation.
- **N9 — `devel` `voomLmFit` vs edgeR 4.0.16 `voomLmFit`** on counts with structural zeros
  differ by up to 3.8e-2 in coefficients, 1.6e-2 in sigma and 3.3e-2 in weights
  (`heldup_voom`, section D), consistent with the adaptive span default (0.442 here vs
  edgeR 4.0.16's fixed 0.5) and the new C Poisson zero detection; df.residual agree exactly.
  Not pursued further.

## Withdrawn (own suspicions killed by execution)

- **W1** — a first probe of the `contrasts.fit` approximation on a one-way design found no
  error at all: the approximation is exact whenever the coefficients are independent, as the
  help page says; only a non-orthogonal design shows it (N2).
- **W2** — on reading `src/gls.c:99-148` I doubted the shortcut that whitens weighted complete
  genes with the shared factor of the correlation matrix; `chol(D⁻¹CD⁻¹) = chol(C)D⁻¹` holds
  and the kernel equals the per-gene GLS closed form to 2.8e-14 with weights and NAs
  (`heldup_dupcor_gls`, section C).
- **W3** — the C `dupcor.c` scales `y` and `X` by `sqrt(w)` but not `Z`, which looked like a
  transcription error; `statmod::mixedModel2Fit` (the 3.68.5 reference) does the same, and
  the two builds return identical genewise correlations with weights and NAs.
- **W4** — an apparent `NA` df.prior on the robust unequal-df path was my harness indexing a
  scalar `df.prior` as a vector.

## What held up (executed, not just read)

All on `devel` and 3.68.5 unless stated; `../verify/heldup_*.R` with `.out` files.

- **lmFit** with a probe-weight matrix and 200 missing values equals per-gene weighted least
  squares to 3.9e-14 (coefficients), 1.2e-15 (`stdev.unscaled`), 4.4e-15 (sigma) with exact
  df; the `devel` C kernel and the 3.68.5 R loop give the same numbers.
- **contrasts.fit** without weights is exact on a non-orthogonal design (coefficients 0,
  `stdev.unscaled` vs `sqrt(diag(C'VC))` 0, `cov.coefficients` 5.6e-17).
- **eBayes** (equal df, the legacy path that `voom`+`lmFit` takes) equals the Smyth 2004 port:
  df.prior 3.908572 and s2.prior 0.048335 to all printed digits (true 4, 0.05), s2.post
  3.0e-14, t 1.4e-12, p 3.4e-15, df.total = min(df.residual+df.prior, pooled); the B-statistic
  equals the closed form given `var.prior` (0); the moderated F equals `b'V⁻¹b/(r·s2.post)`
  (8.5e-14) with p from `pf(·, r, df.prior+df.residual)` (7.8e-16); null coefficients are
  calibrated (5.53 % below 0.05 over 3,000 genes, KS p 0.698); `trend=TRUE` equals
  `trend=Amean`, prior scale 0.0463–0.0560; `legacy=TRUE` is byte-identical to the default,
  and the new estimator on the same data gives 3.9233 / 0.048389.
- **treat** p-values and t-statistics equal the McCarthy–Smyth formulas exactly.
- **topTable** adjusts with BH over all genes before thinning (0 difference to `p.adjust`),
  `p.value=` filtering keeps the unfiltered adjusted values, sort by B is monotone,
  `confint=TRUE` equals `logFC ± qt(0.975, df.total)·se` (4.4e-16).
- **decideTests** `separate`, `global`, `hierarchical` equal ports (per-column BH; BH over the
  matrix; F-selection then per-gene BH at the reduced cutoff); `nestedF` calls are confined
  to the F-selected set.
- **voom** equals the Law et al 2014 port (with limma's span rule and all-zero genes excluded
  from the trend) to 0 in `E` and 8.9e-16 relative in weights on 3.58.1–devel, with and
  without supplied library sizes; **voomWithQualityWeights** is exactly
  `t(aw · t(voom(weights=aw₁)$weights))` with the second-pass `arrayWeights`.
- **duplicateCorrelation** genewise correlations equal lme4 REML `σ²_b/(σ²_b+σ²_e)` to a
  median 1.35e-5 (max 7.5e-3) on the 302 of 400 genes interior for both; 89 genes lme4 puts at
  its boundary 0 are negative in limma (statmod's estimator allows that); consensus 0.3936 for
  a true 0.40 equals `tanh(mean(atanh(ρ), trim=0.15))`; with weights and NAs, and with
  `ndups=2`, the `devel` C backend returns the same genewise values as the 3.68.5
  statmod code to all printed digits (consensus 0.3146384760 / 0.9158357731).
- **gls.series** (`lmFit(block=, correlation=)`) equals the per-gene GLS closed form with
  weights and NAs (2.8e-14 / 1.0e-15 / 2.2e-15), on the fast path (8.9e-15) and with array
  weights (1.1e-16).
- **camera** equals the Wu & Smyth 2012 port with an exact t-to-z transform to 2.4e-9 in
  p-value (1.4e-8 relative) with estimated inter-gene correlations and 3.2e-7 relative at the
  default 0.01; the VIF/correlation of an 80-gene set with a planted common factor is
  reproduced (0.0007 here, p 0.762); `use.ranks=TRUE` at correlation 0 equals the
  normal-approximation Wilcoxon on the eBayes t (5.199e-35 vs 5.194e-35); FDR is BH.
- **fry** directional p equals `2·pt(−|t|, df.residual)` from the effects matrix, and
  `zscoreT(approx=FALSE)` is exact to 3.6e-15.
- **normalizeQuantiles** equals a port in all three modes (no ties, `ties=TRUE` with average
  ranks, `ties=FALSE`, and with NAs: 0); **removeBatchEffect** equals the closed form
  (0), leaves the group coefficient unchanged (6.2e-15) and zeroes the refitted batch
  coefficients (4.5e-15); the 3.66.0 covariate centring is visible on 3.58.1 (1.78 vs the
  centred form, 0 vs the uncentred one); **normalizeCyclicLoess(method="fast")** reduces
  the largest loess trend against the row mean from 12.9 to 0.09 (`pairs` 1.01, `affy` 0.96
  after three iterations on a one-column quadratic distortion).
- **robust eBayes** (legacy): with no outliers robust ≈ non-robust (df.prior 3.76–4.96 vs
  4.92, scale 0.03978 vs 0.03974); with outliers df.prior is monotone in the F tail
  probability, 0.852 for the hypervariable genes; no false discoveries.
- **The project's own tests**: `tests/limma-Tests.R` compared with `R CMD Rdiff` gives the
  same 76 differing lines on `devel`, `RELEASE_3_23` and both patched builds (pre-existing
  platform differences in the normexp/normalizeWithinArrays sections); the five new `devel`
  C test files pass on the patched build.

## Not audited

`arrayWeights(method="genebygene")` internals (Ritchie 2006) beyond its use as a reference;
`mrlm` (MASS::rlm robust fits); `fitFDistRobustly`'s Winsorised-moment estimator as a port
(sanity only); `romer`, `goana`/`kegga`, `diffSplice`/`topSplice`; `normalizeWithinArrays`,
background correction and two-colour code; `normalizeCyclicLoess` beyond the trend check;
`voomLmFit`'s Poisson zero detection against edgeR's `glmFit` beyond the section-D
comparison; the OpenMP thread paths beyond the project's own `nthreads=2` tests; the
`dgesv` failure branch of `src/awreml.c:384-398` (by reading, a singular step would be
applied before `status=1` is returned — no singular case was constructed); `plotSA`,
`plotMDS` and all plotting.
