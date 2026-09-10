# limma statistical core — review

_Audited commits: `bioc/limma` **`devel`** @ `57a8de7296ad733ac25d3e3c01de3fdddcd0a9ae`
(3.99.0, "Add new files for limma 3.99.0.", 2026-08-30) and **`RELEASE_3_23`** @
`825d1c8330d024adb6c54af66d79b0f4ec258530` (3.68.5, 2026-08-10). Every `file:line`
below is on one of those two commits and says which. Executed on R 4.3.3 with seven
limma builds (see `../verify/rlib.sh`): 3.34.0, 3.42.2, 3.58.1 (the apt
`r-bioc-limma` on this host), 3.62.2, 3.68.4 (Ubuntu pool source tarballs), 3.68.5 and
3.99.0 (mirror branches), plus two builds carrying the patch in `../upstream/`._

The scope is the code that produces published numbers: `lmFit` / `lm.series` /
`gls.series`, `eBayes` / `squeezeVar` / `fitFDist` / `fitFDistRobustly` /
`fitFDistUnequalDF1`, `treat`, `topTable`, `decideTests` / `classifyTestsF`,
`voom` / `voomWithQualityWeights` / `voomLmFit`, `arrayWeights`,
`duplicateCorrelation`, `contrasts.fit`, `camera` / `roast` / `fry`,
`normalizeBetweenArrays` / `normalizeCyclicLoess` / `loessFit`, `removeBatchEffect`.

The short version: limma's published arithmetic reproduces. The moderated-t machinery
(Smyth 2004), the voom mean–variance model (Law 2014), `camera`'s variance-inflation
factor (Wu & Smyth 2012), the robust hyperparameter estimator (Phipson 2016), the
`duplicateCorrelation` REML and the new C backends for `lm.series`, `gls.series` and
`duplicateCorrelation` all agree with independent ports or closed forms to between
`1e-13` and machine precision. One thing does not: the Fisher-scoring **convergence
criterion** in the prior-weights branch of `arrayWeights(method="reml")` is divided by
the number of genes a second time, so the iteration stops after one to three steps.

---

## L1 — CONFIRMED (wrong number at master)

**`arrayWeights(..., weights=, method="reml")` stops the REML scoring
(ngenes + prior.n) times too early, so it returns unconverged sample weights; in limma
devel this is the default path of `voomLmFit(sample.weights=TRUE)`.**

### The code

`arrayWeights()` has two REML implementations and dispatches on whether prior
observation weights are present (devel `R/arrayWeights.R:105,107`; release
`R/arrayWeights.R:105,107`):

* no prior weights → `.arrayWeightsREML()`,
* prior weights → `.arrayWeightsPrWtsREML()`.

Both run the same Fisher scoring on the variance parameters `gam`, and both stop when
`crossprod(dl, gamstep)` — the quadratic form of the score against the scoring step, the
usual "approximate log-likelihood improvement" criterion — falls below `tol`, per gene
and per variance parameter.

`.arrayWeightsREML` builds the information matrix and score as **sums** over genes and
then normalises once (devel and release `R/arrayWeightsREML.R:81-82,89`):

```r
info2 <- ngenes*info2 + prior.n*crossprod(Z2)     # scale ~ ngenes
z     <- ngenes*z     + prior.n*(w-1)             # scale ~ ngenes
...
convcrit <- crossprod(dl,gamstep) / ngam / (ngenes+prior.n)
```

`.arrayWeightsPrWtsREML` builds the same quantities as **averages** (release
`R/arrayWeightsPrWtsREML.R:65-66`) and then divides the criterion by `(ngenes+prior.n)`
again (release `R/arrayWeightsPrWtsREML.R:77`):

```r
info2 <- info2 / (ngenes+prior.n)                 # scale ~ 1
z     <- z     / (ngenes+prior.n)                 # scale ~ 1
...
convcrit <- crossprod(dl,gamstep) / (ngenes+prior.n) / ngam
```

Because `gamstep = solve(info2, dl)` is invariant to a common rescaling of `info2` and
`z`, and `dl` shrinks by the same factor that `info2` does, the quadratic form
`dl'gamstep` in the second function is already the per-gene quantity that the first
function obtains by dividing by `(ngenes+prior.n)`. Dividing again makes the criterion
exactly `(ngenes+prior.n)` times too small, so `convcrit < tol` fires after one to three
iterations at the `arrayWeights` default `tol = 1e-5`.

In devel the same function is a C kernel (`R/arrayWeightsPrWtsREML.R:15` calls
`awremlfit`), and the C carries the identical arithmetic: `src/awreml.c:357` and
`src/awreml.c:359` divide `info2` and `z` by `denom = ngenes + prior_n`
(`src/awreml.c:253`), and `src/awreml.c:403` then computes

```c
convcrit = num / denom / ngam;
```

against `tol` at `src/awreml.c:423`.

The factor is visible in the traces. On 3000 genes × 9 arrays
(`../verify/l1_arrayweights_reml_convergence.vdevel.out`) the two paths on the *same
data with unit prior weights* print

```
--- .arrayWeightsREML trace (no prior weights), tol=1e-5
1 0.2138735 ... 5 2.762911e-06          # five iterations
--- .arrayWeightsPrWtsREML trace (unit prior weights), tol=1e-5
1 7.10543e-05 ... 2 4.10784e-06         # two iterations
```

The first criterion value differs by 3010 = `ngenes + prior.n`.

### What it does to the numbers

With **unit** prior weights the two functions fit the identical model to the identical
data and must return the identical weights. On devel 3.99.0 they do not
(`../verify/l1_arrayweights_reml_convergence.vdevel.out`):

| | array weights (3000 genes × 9 arrays) |
|---|---|
| `arrayWeights(y, design, method="reml")` | 2.6562 1.0539 0.3775 1.0147 1.0369 0.9507 0.2970 3.3063 0.9632 |
| `arrayWeights(y, design, weights=matrix(1,...), method="reml")` | 2.3519 1.0953 0.3976 1.0514 1.0849 0.9981 0.3096 2.7570 1.0046 |

`max |diff| = 0.549`. An independent REML+prior score, recomputed with an `lm.wfit` loop
over genes at the returned weights, is `2.98e-04` at the first answer and `4.43e-02` at
the second — 149 times further from the stationary point. With genuine (random
exponential) prior weights the default-`tol` answer differs from the converged one
(`tol = 1e-14`) by `max |diff| = 0.891` and its score is `7.50e-02` against `2.69e-06`.

On RNA-seq data with planted sample quality
(`../verify/l1_voom_sample_weights_magnitude.vdevel.out`, 8 samples, ~8000 genes, sd
multipliers 1 1 3 1 1 0.5 1 2):

| | sample weights |
|---|---|
| `method="reml"`, default tol | 1.2619 1.2980 0.3266 1.1983 1.2690 1.5910 1.2103 0.6383 |
| `method="reml"`, converged (`tol=1e-14`) | 1.2600 1.3073 0.3237 1.1938 1.2753 1.6566 1.2058 0.6166 |
| `method="genebygene"` | 1.2051 1.3219 0.3299 1.2231 1.2195 1.7110 1.1945 0.6241 |

`max |default − converged| = 0.0656` (`max |log ratio| = 0.0404`, 4 %), and the
downstream DE counts move: **16 genes at BH < 0.05 and 9 at BH < 0.01 with the
default-tol weights against 18 and 10 with the converged weights** — `genebygene` also
gives 18 and 10. `voomLmFit(sample.weights=TRUE)` on devel returns the default-tol
weights (`max |voomLmFit − converged REML| = 0.0663`).

### Which call paths reach it (executed, `../verify/l1_exposure_default_paths.*.out`)

`arrayWeights(method="auto")` — the default — routes prior weights to `genebygene`
(devel `R/arrayWeights.R:87-91`; the help page states this,
`man/arrayWeights.Rd`, Details), and `voomWithQualityWeights()` defaults to
`method="genebygene"` (`R/voomWithQualityWeights.R:1`). So on released limma the wrong
criterion is reached only by an **explicit** `method="reml"`:

| build | `arrayWeights(v, design)` default | `voomLmFit(sample.weights=TRUE)` |
|---|---|---|
| 3.42.2, 3.58.1, 3.68.5 | `== genebygene` (unaffected) | edgeR's, `== voomWithQualityWeights(genebygene)` to 2e-4 (unaffected) |
| devel 3.99.0 | `== genebygene` (unaffected) | limma's, `== voomWithQualityWeights(method="reml")` to 0.0000 — **affected** |

That is the change that makes this worth reporting now: limma devel's NEWS for 4.0.0
(`inst/NEWS.Rd`, lines 7-17) moves `voomLmFit()` into limma and says "For the purpose of
estimating sample weights, voomLmFit() calls arrayWeights() with `method="reml"` if there
is no loss of df due to exact zero fitted values"; `R/voomLmFit.R:238` and
`R/voomLmFit.R:309` are those calls. In 4.0.0 the unconverged branch therefore becomes
the default sample-weight estimator of the package's recommended RNA-seq entry point.
On this data set that moves the sample weights by up to 0.083 relative to the
`genebygene` weights the same call returns today.

### Version scope (executed, one `.out` per version — not inferred)

| version | `max |unit-weights − no-weights|` | `max |reml default − converged|` (voom data) | verdict |
|---|---|---|---|
| 3.34.0 (pool tarball; cohort names 3.34.9, 3.34.5) | 0.000e+00 | 0.0000 | **unaffected** |
| 3.42.2 (pool tarball; cohort) | 5.493e-01 | 0.0657 | **affected** |
| 3.58.1 (apt build; cohort, 5 papers) | 5.493e-01 | 0.0657 | **affected** |
| 3.62.2 (pool tarball; cohort) | 5.493e-01 | — | **affected** |
| 3.68.4 (pool tarball, Bioc 3.23) | 5.493e-01 | — | **affected** |
| 3.68.5 (`RELEASE_3_23` @ `825d1c83`, current release) | 5.493e-01 | 0.0656 | **affected** |
| 3.99.0 (`devel` @ `57a8de72`) | 5.493e-01 | 0.0656 | **affected** |
| 3.99.0 + patch | 8.882e-16 | 0.0045 | fixed |
| 3.68.5 + patch | 8.882e-16 | — | fixed |

3.34.0 is unaffected because it has no separate prior-weights REML branch. The comment
header of `R/arrayWeightsPrWtsREML.R` reads "Created 12 Feb 2019 from
`.arrayWeightsREML`", which places the split in the 3.40.0 rewrite that `inst/NEWS.Rd`
describes; **that is by reading** — 3.36–3.40 were not built here, and the executed
boundary is "unaffected at 3.34.0, affected at 3.42.2".

### Fix

One term, in both implementations: use the same per-gene criterion as
`.arrayWeightsREML`. Patches for `devel` (C) and `RELEASE_3_23` (R), each with a test,
are in `../upstream/`. With the patch the two paths agree to `8.9e-16`, the weighted
path's default-`tol` answer sits `3.8e-3` from the converged one (the unweighted path's
own default-`tol` error on the same data is `5.3e-4`), and `voomLmFit` on devel returns
converged weights (`max |voomLmFit − converged| = 0.0046`, DE counts back to 18/10).

---

## Notes (design, documentation, cosmetic — not "wrong number at master")

**N1 — `contrasts.fit()` under voom weights: the documented approximation is large enough
to change DE calls.** `man/contrasts.fit.Rd:35-40` says plainly that with a
non-orthogonal design and precision weights or missing values the unscaled standard
deviations "are approximate rather than exact" and that "the approximation is usually
acceptable". Measured on a 3-group voom fit
(`../verify/heldup_voom.vdevel.out`): relative error of `stdev.unscaled` max **0.208**,
99th percentile 0.099, median 0.021; moderated t up to 17.2 % off; p-values up to
`10^0.706` (5.1×) off. For the contrast `B+C−2A` that is **5 genes at BH < 0.05 from
`contrasts.fit` against 2 from an exact refit** (3 differences). Unweighted, and
`lmFit(contrasts=)` on devel, are exact (`2.2e-16`, `8.9e-16`). This is a documented
design choice with a documented escape (redefine the design matrix), so it is a NOTE —
but the size of the approximation is worth a sentence on the help page, and devel's new
`lmFit(contrasts=)` / `voomLmFit(contrasts=)` path is the exact alternative.

**N2 — `topTable` uses `<=` at the p-value cutoff, `decideTests` uses `<`.** With
`p.value` set to an attained adjusted p (0.050424) `topTable` keeps 233 genes and
`decideTests` flags 232 (`../verify/heldup_decidetests_arrayweights.vdevel.out`). A
boundary convention, only reachable when the cutoff is exactly an attained value. The
same mismatch exists between `topTags` and `decideTests` in edgeR (audit `edger`, N3).

**N3 — `zscoreT`'s Hill approximation.** Default `method="hill"` in the gene-set tests
is accurate to `1.8e-04` at df = 4, `3.1e-06` at df = 8 and `1.7e-08` at df = 30 over
t ∈ [−8, 8] against the exact `qnorm(pt(...))`; `method="bailey"` is 100× worse
(`2.0e-02` at df = 4). Design choice, correctly defaulted
(`../verify/heldup_genesets.vdevel.out`).

**N4 — `.arrayWeightsPrWtsREML`'s own default `tol` is 1e-6, `arrayWeights`' is 1e-5.**
The inner default is dead: `arrayWeights()` always passes its own `tol`. Cosmetic
(devel and release `R/arrayWeightsPrWtsREML.R:1`, `R/arrayWeights.R:1`).

**N5 — `normalizeCyclicLoess` at the default `iterations=3` is not converged.** With
planted column distortions up to 0.31, the residual trend at the adaptive span (0.395)
is `3.82e-02` after 1 iteration, `9.50e-03` after 3 (the default) and `1.63e-03` after
10 (`../verify/heldup_normalize_batch.vdevel.out`). A speed/accuracy default, not an
error; `method="affy"` and `"pairs"` at 3 iterations give `1.08e-02` and `6.28e-03`.

**N6 — `fitFDistUnequalDF1` is a moment estimator, not ML, and `squeezeVar` still takes
the legacy moment path for equal df.** On planted `df2 = 6`, `scale = 0.20` data limma
returns `df2 = 6.0123`, `scale = 0.20171`; an `optim` ML fit returns `6.0121`, `0.20158`
with a log-likelihood `1.15e-03` higher (`../verify/heldup_fitfdist_unequal.vdevel.out`).
Documented behaviour of the method, and the difference is far below the sampling error.

**N7 — `robust=TRUE` assigns very small `df.prior` to a few genes on clean data.** With
no outliers planted, the robust fit gives `df.prior` median 4.020 (truth 4) but a minimum
of 0.203, at one gene out of 5000; with 100 planted outlier genes it correctly gives all
100 of them the smallest `df.prior` (median 0.264 against 3.573)
(`../verify/heldup_ebayes_core.vdevel.out`). That is what the winsorised-moment
estimator of Phipson et al (2016) is designed to do; recorded so that a user who sees one
tiny `df.prior` on clean data knows it is expected.

---

## Withdrawn (own suspicions killed by execution)

**W1 — "the patch does not actually converge the weighted path."** The first version of
the patch's test asserted `max |log(aw2/aw3)| < 1e-3` between the default `tol` and
`tol = 1e-7` on 500 genes with random prior weights, and the *patched* build failed it at
`4.4e-03`. Execution showed the threshold was wrong, not the fix: on the same data the
*unweighted* `.arrayWeightsREML` path — which has always used the correct criterion —
has its own default-`tol` error of `5.3e-04` at 500 genes, and the patched weighted path
sits at `4.4e-03` against `9.99e-02` unpatched, i.e. it now behaves like the unweighted
path and 23× better than before. The test threshold was corrected to `0.02` (unpatched
`0.0999`, patched `0.0044`; `../upstream/…devel.patch`, `tests/arrayweights-reml.R`).

**W2 — "every voom sample-weight path is affected."** Suspected that
`voomWithQualityWeights()` and `arrayWeights()` on a voom `EList` run the broken branch,
because both carry observation weights. Executed on five versions
(`../verify/l1_exposure_default_paths.*.out`): `method="auto"` sends prior weights to
`genebygene` and `voomWithQualityWeights()` defaults to `method="genebygene"`, so the
released default paths are unaffected. Only an explicit `method="reml"`, and limma
devel's `voomLmFit()`, reach it. The finding's exposure statement was rewritten to say
so.

---

## What held up (executed, not just read)

All figures below are from the `.out` files named; each harness ran on devel 3.99.0 and
on 3.42.2, 3.58.1 and 3.68.5 (some also 3.34.0).

* **Moderated t and the hyperparameters** (`heldup_ebayes_core.*.out`). An independent
  port of Smyth (2004) written from the paper: `fitFDist` returns `df.prior = 4.000740`
  and `s2.prior = 0.089410` against the port's identical values (planted truth 4 and
  0.0900, difference `8.3e-17`); `eBayes` `s2.post` `2.2e-16`, moderated `t` `4.3e-14`,
  `df.total` exact, p `6.7e-16`; the B-statistic `7.1e-15` at three `var.prior` values,
  and `var.prior` itself `3.6e-14`; the moderated F `3.1e-13` with `F.p.value` equal to
  `pf(F, 2, df.total)` to `1.2e-15` and, for a single coefficient, `F == t^2`
  (`2.8e-13`); `treat` p `2.2e-16`; `squeezeVar` `var.post` `2.2e-16`; the `trend=TRUE`
  loess prior `1.8e-15`; the winsorised moments used by `robust=TRUE` match numerical
  quadrature to `6.7e-16` at df2 = 4, 20 and Inf; genes with 0 residual df get NA t and p
  and are excluded from BH, which then equals `p.adjust` over the rest to `0.0e+00`.
* **`topTable`** (`heldup_ebayes_core.*.out`): `adj.P.Val` equals `p.adjust(..., "BH")`
  over all genes to `1.6e-15`, `logFC` exactly, the confidence interval equals
  `qt(0.975, df.total) * se` to `1.8e-15`, sorting by `B` and the `p.value` filter use
  `<=`.
* **`fitFDistUnequalDF1` and `squeezeVar` with unequal df**
  (`heldup_fitfdist_unequal.*.out`): `df.prior` from `squeezeVar` equals
  `fitFDistUnequalDF1` exactly, `var.post` reproduces the formula to `0.0e+00`, and with
  60 planted outliers the robust variant recovers `df2 = 5.312` (truth 6, non-robust
  4.663) and puts 53 of the 60 outliers below the median shrunken df.
* **`voom`** (`heldup_voom.*.out`): `E`, the precision weights and `targets$lib.size`
  reproduce an independent port of Law et al (2014) to `0.0e+00` / `1.1e-15` at a fixed
  span and at the adaptive span (limma's span 0.462456 against the rule's 0.46246);
  `voomWithQualityWeights` equals the documented two-pass recipe exactly
  (`weights 0.0e+00`, `sample.weights 0.0e+00`).
* **`lmFit` and the new C backends** (`heldup_lmfit_c_backend.*.out`): `lm.series` and
  `gls.series` with missing values, with probe weights, and with per-gene rank-deficient
  designs equal a per-gene `lm.wfit` / generalised-least-squares reference to `≤ 4e-15`
  in coefficients, `stdev.unscaled`, `sigma` and `df.residual`, with identical NA
  patterns; `cov.coefficients` equals `chol2inv` of the shared design exactly; the
  `contrasts=` argument is exact per gene under weights; `nthreads=4` is bit-identical
  to `nthreads=1`.
* **`duplicateCorrelation`** (`heldup_duplicatecorrelation.*.out`): the genewise
  intra-block correlations equal a `statmod::mixedModel2Fit` reference to `1.55e-15`
  (median `2.74e-16`) and an independent `lme4` REML fit to `1.17e-06` over 33 interior
  genes; the consensus equals `tanh(mean(atanh(rho), trim=0.15))` to `1.11e-16`
  (0.3938 against planted 0.4); with weights and NAs, `1.32e-14` with no NA-pattern
  mismatches; the `ndups=2` and `block=` forms agree exactly; `nthreads=4` identical.
* **Gene-set tests** (`heldup_genesets.*.out`): `camera`'s variance-inflation factor and
  p-value equal a port of Wu & Smyth (2012) to `6.0e-10` with the same `Direction`, and
  `FDR` is BH over the sets; `fry` equals its port to `3.3e-16`; `roast` reproduces
  exactly when the RNG stream is matched; under the null `camera` rejects 3.5 % / 2.5 %
  and `roast` 4.0 % at α = 0.05 over 200 independent-gene sets.
* **Normalisation and batch removal** (`heldup_normalize_batch.*.out`):
  `normalizeQuantiles` equals a closed-form reference to `0.0e+00` with and without ties
  and preserves NA positions and within-column monotonicity;
  `normalizeBetweenArrays(method="quantile")` is the same function; `loessFit`
  unweighted equals `stats::lowess` at the same span to `0.00e+00`;
  `removeBatchEffect` equals the closed form to `0.0e+00` with and without a design, and
  refitting on the corrected data returns batch coefficients of `5.2e-15` with the design
  coefficients unchanged to `7.1e-15`.
* **`decideTests`** (`heldup_decidetests_arrayweights.*.out`): `separate`, `global`,
  `hierarchical` and `nestedF` all reproduce independent implementations with **0**
  mismatches, `classifyTestsF`'s F equals `t' R^-1 t / 2` to `2.3e-13`, and `lfc=1`
  equals the separate result masked by `|logFC| > 1`.
* **`arrayWeights` without prior weights** (`heldup_decidetests_arrayweights.*.out`):
  against planted `1/sd^2` of `2.718 1.000 0.368 1.000 1.000 1.000 0.301 3.320 1.000`,
  `method="reml"` recovers them to `max |log ratio| = 0.080` and `genebygene` to `0.174`;
  both have geometric mean 1 to `6e-18`; `var.group` gives weights constant within group.

## Not audited

Two-colour array reading and background correction (`read.maimages`,
`backgroundCorrect`, `normexp*`, `nec`), within-array normalisation
(`normalizeWithinArrays`), `diffSplice` / `topSplice`, `romer` / `mroast`,
`goana` / `kegga` / `topGO` beyond what the project's own `tests/limma-Tests.R` covers,
`propTrueNull` / `convest`, `vooma` / `voomaLmFit`, `genas`, `plotSA` / `plotMD` and all
plotting, the `poisfit` C routine new in devel, `weightedLowess` internals beyond
`loessFit`, and the OpenMP paths beyond a 4-thread bit-identity check on `lm.series`,
`gls.series` and `duplicateCorrelation`.
