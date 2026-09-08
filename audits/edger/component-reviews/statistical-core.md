# Component: edgeR statistical core (Bioconductor `RELEASE_3_23` @ `c4a54bda`, 4.10.5, 2026-09-04; `devel` @ `db4e697f`, 4.99.4, 2026-09-06)

Read in full on the two audited commits: `R/filterByExpr.R`, `R/calcNormFactors.R` and
`R/normLibSizes.R` (TMM, TMMwsp, RLE, upper-quartile), `R/estimateDisp.R` (WLEB),
`R/adjustedProfileLik.R` + `src/compute_apl.c`, `R/glmfit.R` (`glmFit`, `glmLRT`),
`R/glmQLFTest.R` + `src/ql_glm.c` (both QL methods), `R/exactTest.R`,
`R/exactTestDoubleTail.R`, `R/exactTestBetaApprox.R`, `R/q2qnbinom.R`, `R/topTags.R`,
`R/decidetestsDGE.R`, `R/cpm.R`, `R/rpkm.R`, `R/aveLogCPM.R` + `src/compute_cpm.c`,
`src/add_prior_count.c`, `R/predFC.R`, `R/getOffset.R`, `R/scaleOffset.R`,
`R/DGEListFromTximport.R`, `R/residDF.R`, `R/effectiveLibSizes.R`; targeted reads of
`src/glm.c` (Levenberg stopping rule) and `R/mglmOneGroup.R`. The same files were diffed
against the 3.36.0, 4.0.16, 4.4.2 and 4.10.1 sources.

Every suspect was **executed on the shipped code**. R 4.3.3 with six edgeR builds in
private libraries (`../verify/rlib.sh`): 4.0.16 (the apt package on this host, limma
3.58.1), 3.36.0, 4.4.2 and 4.10.1 from the Ubuntu pool source tarballs, 4.10.5 from the
`bioc/edgeR` read-only mirror of the Bioconductor git (`RELEASE_3_23`), 4.99.4 from its
`devel` branch — the last four built against limma 3.68.4 from the pool, 3.36.0 with a
two-macro `FCONE` patch so its C++ compiles on R 4.3. References are numpy/scipy ports
written from the papers (Robinson & Oshlack 2010; Robinson & Smyth 2008; McCarthy, Chen &
Smyth 2012; Lund et al 2012; Chen et al 2016/2025) or closed-form arithmetic in R that
does not call the function under test. Harnesses and captured output are in `../verify/`.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### EG1 — CONFIRMED on the 4.10.0–4.10.1 release tarball (Bioconductor 3.23, 2026-04-28 to 2026-08-09); **already fixed on the release branch** (4.10.5) and `devel`; 3.36.0–4.4.2 unaffected: `cpm()`/`rpkm()` on a DGEList with an offset matrix counted the library sizes twice

**Code.** In the 4.10.1 tarball `R/cpm.R:82-94` (`cpm.default`, "Last modified 12 Apr
2026") row-centres a supplied `offset` and *adds* it to `log(lib.size)`:

```r
offset.prior <- offset - rowMeans(offset)
...
lib.size <- exp(matrix(log(lib.size),nrow(y),ncol(y),byrow=TRUE) + offset.prior)
```

while `cpm.DGEList` (line 9-11) passes both `lib.size * norm.factors` and `y$offset`.
edgeR's convention for `y$offset` is that it *replaces* the log library sizes:
`getOffset()` returns it verbatim for `glmFit`, `scaleOffset()` centres offsets on
`mean(log(lib.size))`, and the pre-4.10 `cpm.DGEList` (4.4.2 `R/cpm.R:10-17`) warned
"Offset may not reflect library sizes" when the offset's range did not overlap
`log(lib.size)`. With an offset `log(L_j) + d_gj`, 4.10.1 therefore divides by
`L_j^2/geomean(L) · exp(d_gj)`.

**Verified** (`../verify/eg1_cpm_offset.R`, six `.out` files): with an offset exactly equal
to `log(lib.size)` (which `scaleOffset()` leaves unchanged and which `glmFit` treats as no
offset at all — its fitted values divided by `exp(offset)` are constant within genes to
1.1e-15 on every version), 4.10.1's `cpm()` differs from `counts/L·1e6` by a factor
`geomean(L)/L_j` per column (medians 2, 1, 0.5, 2, 1, 0.5 for a four-fold library-size
range), `cpm(log=TRUE)` by up to 0.9994 log2 units and `rpkm()` by up to 8.8×. With a
gene-specific (cqn/EDASeq-style) offset the same factor appears. On 3.36.0, 4.0.16, 4.4.2,
4.10.5 and 4.99.4 the values equal `counts/exp(offset)·1e6` to 2.2e-16 and the
log-CPM prior-count formula to 4.4e-15.

**Upstream state.** The release-branch log shows the change entering as 4.9.6
(`2054923`, 2026-04-13, "cpm() and rpkm() now support prior offsets") and being reverted
on 2026-08-09 (`1da6863`, "Restoring previous behavior in that offset matrix input to
cpm() take precedence over lib.size and offset.prior"); 4.10.5 `R/cpm.R:9-11, 88` now
returns `cpm(y$counts, offset=y[["offset"]])` and uses `exp(offset)` as the library
sizes. Neither the change nor the revert has an `inst/NEWS.Rd` entry (the 4.10.x section
lists only 4.10.0 items); the commit message is the maintainers' statement. Exposure:
anyone who stored an offset matrix in a DGEList (cqn, EDASeq, RUVSeq, csaw, the new
`DGEListFromTximport` with `countsFromAbundance != "no"` sets `offset.prior`, not
`offset`) and ran `cpm()`/`rpkm()` under edgeR 4.10.0–4.10.2 between late April and
August 2026. Nothing to file: fixed. Held; recorded so that a 2026 paper reporting
offset-normalised log-CPM under 4.10.0/4.10.1 can be checked.

### EG2 — CONFIRMED on 4.4.2 and 4.10.1 (the 4.4.0 C rewrite through 4.10.3); **fixed on the release branch** (4.10.4, 2026-08-29) and `devel`; 3.36.0 and 4.0.16 unaffected: `aveLogCPM(y, offset=<matrix>)` returned a wrong value for the first gene

**Code.** `src/compute_cpm.c:145` in 4.4.2 and 4.10.1:

```c
if((tag >= 1) && (!repeat_row)){
    compute_offsets(priors,offsets,tag,log_in,log_out,pptr,optr);
}
```

When `offset` is a full matrix (`repeat_row` false) the prior/offset vectors for gene 0
are never filled, so the first gene is fitted with zeroed offsets (library size 1) and
prior count 0. 4.10.5 `src/compute_cpm.c:145` reads `if(!repeat_row)` (commit
`f8bb002`, "Fix bug in aveLogCPM() when offset matrix is provided"; no NEWS entry).

**Verified** (`../verify/eg1_cpm_offset.R`, part C): `aveLogCPM(y, offset=log L)` vs
`aveLogCPM(y, lib.size=L)` differ by 21.2 log2 units on 4.4.2 and 4.10.1 (range of the
offset version 0.93..26.77 against 1.09..9.15) and by 0 on 3.36.0, 4.0.16, 4.10.5 and
4.99.4. Reach: only calls that hand `aveLogCPM()` a full offset matrix — `aveLogCPM()` on
a `DGEGLM` fitted from a DGEList that carries `y$offset`, or the default method with
`offset=`. The `DGEList` method (`R/aveLogCPM.R:4-24`) uses `lib.size * norm.factors`
even when `y$offset` exists, so `estimateDisp()` and `glmQLFit()` on a DGEList are not
reached. One gene's `logCPM` column. Fixed; held.

### EG3 — CONFIRMED on every version executed (3.36.0, 4.0.16, 4.4.2, 4.10.1, 4.10.5 and `devel` 4.99.4): a gene with exactly `min.count` reads in the median-size library sits exactly on `filterByExpr()`'s CPM cutoff and is dropped for 12–17 % of library sizes

**Code.** `R/filterByExpr.R:62-65` (4.10.5; `devel` identical):

```r
CPM.Cutoff <- min.count/MedianLibSize*1e6
CPM <- cpm(y,lib.size=lib.size)
tol <- 1e-14
keep.CPM <- rowSums(CPM >= CPM.Cutoff) >= (MinSampleSize - tol)
```

The help page (`man/filterByExpr.Rd`, Details) defines the rule as "CPM >= CPM.cutoff in
MinSampleSize samples, where CPM.cutoff = min.count / median(lib.size) * 1e6". With an
odd number of samples the median library size *is* one of the libraries, so a gene with
exactly `min.count` reads there has CPM mathematically equal to the cutoff and must count.
But `cpm()` computes `y*1e6/lib.size` in C (`src/compute_cpm.c:87`, 4.4.0 onwards;
`y*(1e6/lib.size)` in the 4.0.16 C++), while the cutoff is `(min.count/lib.size)*1e6` in
R. The two round to different last bits for a large fraction of library sizes, and the
existing `tol` guards only the sample count, not the CPM comparison.

**Verified** (`../verify/eg3_filterbyexpr_boundary.R`, six `.out` files):

| | 3.36.0, 4.0.16 (C++) | 4.4.2, 4.10.1, 4.10.5, devel (C) |
|---|---|---|
| library sizes (of 200,000 random) for which a count of exactly 10 fails `cpm() >= 10/L*1e6` | 34,377 (17.19 %) | 24,875 (12.44 %) |
| same for `min.count` 5 / 15 / 20 | 17.2 / 17.0 / 17.2 % | 12.4 / 12.9 / 12.4 % |
| 40 simulated data sets (5–11 samples, 20,000 genes, defaults): genes at the margin (exactly `min.count` reads in the median library and exactly `MinSampleSize` libraries at or above the cutoff) | 1,589 | 1,589 |
| of these, dropped by `filterByExpr` although the documented rule keeps them | 150 | 148 |
| disagreements with the rule not explained by the margin | 0 | 0 |

Minimal example: `L = (1e6, 1000010, 3e6)`, gene `(5, 10, 5)`, `group = (1, 2, 1)`
(`MinSampleSize` 1, total 20 ≥ 15): `cpm()` gives 9.9999000009999897, the cutoff is
9.9999000009999914, `filterByExpr` returns `FALSE` on all six versions; the same gene with
11 reads is kept. The independent port of the rule (`../verify/heldup_filterbyexpr.R`)
agrees with `filterByExpr` on every other gene decision of 150 random calls (group,
design, matrix, explicit `lib.size`, `large.n`/`min.prop` forms), and every one of its
disagreements is a gene with exactly `min.count` reads in the median-size library.

**Magnitude.** Roughly 4 of 20,000 genes per data set in the simulation (0.2 % of genes are
at the margin, 9.3 % of those are dropped); it changes the retained gene count that papers
report and, through BH, the adjusted p-values in the fourth digit. It only bites with an
odd number of samples. A defect in the arithmetic of a documented rule, not a design
choice, with a one-line fix: `CPM >= CPM.Cutoff*(1-tol)` (the same `tol` the function
already uses for the sample count), or compute the cutoff through `cpm()` itself. The
patch in `../upstream/` (with a boundary case added to `tests/edgeR-Tests.R`) makes the
example return `TRUE TRUE` and leaves the project's saved test output otherwise
unchanged (`R CMD Rdiff` 0 lines on `devel` and `RELEASE_3_23`).

## Notes (design choices, documentation, statistical properties — not defects)

**N1 — TMM trimming with tied M or A values.** `.calcFactorTMM`
(`R/calcNormFactors.R:142-150`) trims by `rank()` with `ties.method="average"`, so a block
of genes sharing an M (or A) value that straddles the 30 % (5 %) boundary is kept or
dropped as a whole; count data produce ~1,000 such tie blocks per 4,000 genes. The
factors move by up to 9.5e-4 relative to a port that breaks ties in order
(`../verify/heldup_tmm_port.py`); with average ranks the port agrees to 4.7e-15. Because
`A` is computed as `(log2(obs/N)+log2(ref/N))/2`, which pairs of counts tie in `A` depends on
the last bit of that expression. `TMMwsp` orders ties deterministically
(`order(M, M.shrunk)`) and weights by `(1+1e-6)/(v+1e-6)`, so on zero-free data with the
same reference it differs from `TMM` by up to 2.0e-3. Documented behaviour of a
rank-based trim; recorded because 62 cohort papers name TMM.

**N2 — exact test: which tail is doubled, and `dispersion=0`.**
`exactTestDoubleTail` (`R/exactTestDoubleTail.R:44-68`) doubles the tail on the side of
`s1` relative to its null mean `n1·s/(n1+n2)`; when that tail exceeds 0.5 (the mean and
the median of the skewed conditional law fall on different sides of `s1`) it returns
`p = 1` where "twice the smaller tail" gives ≥ 0.986 (27 of 398 genes;
`../verify/heldup_exact_test.py`); the code carries a comment asking exactly this
question. For genes with `s1` equal to its null mean both give 1. Irrelevant to any
threshold. For `dispersion = 0` the function delegates to `binomTest`, whose rejection
region is "sum of probabilities ≤ the observed" (the code says so), giving p-values that
differ from doubled binomial tails by up to 0.24; reachable only by passing a dispersion
of exactly zero.

**N3 — `topTags(p.value=)` keeps `FDR <= p.value`, `decideTests(p.value=)` calls
`FDR < p.value`** (`R/topTags.R:58`, `R/decidetestsDGE.R:18`). A gene whose adjusted p
equals the threshold exactly is in one list and not the other
(`../verify/note_toptags_decidetests.R`). Measure-zero in practice; cosmetic.

**N4 — `glmQLFit()` results still depend on whether `estimateDisp()` was run first.**
NEWS 4.10.0: "glmQLFit() with legacy=FALSE no longer automatically estimates the NB
dispersion from trended values found in the DGEList object … The results will now be the
same whether the DGEList contains dispersion estimates or not." On 4.10.1 and 4.10.5 the
NB dispersion is indeed the same (0.10307 either way; on 4.4.2 it was 0.1191 after
`estimateDisp` vs 0.10307 without), but `estimateDisp` also stores `y$AveLogCPM` computed
at the common dispersion (`R/estimateDisp.R:25`) while `glmQLFit` on a fresh DGEList
computes it at the default 0.05 (`R/glmQLFTest.R:22`); the covariate differs by up to
0.113 log2 units and the QL p-values by up to 10 % (max |log10 ratio| 0.040; same 15 genes
at BH < 0.05). Giving both objects the same `AveLogCPM` makes the p-values identical
(`../verify/note_glmqlfit_disp_source.R`). The NEWS sentence is nearly, not exactly, true;
the User's Guide pipeline (`estimateDisp` then `glmQLFit`) is one of the two paths.

**N5 — QL calibration by simulation** (`../verify/sim_ql_calibration.R`, NB data with a
dispersion trend, full pipeline `filterByExpr → normLibSizes → estimateDisp → test`, BH):
in a typical regime (BCV ≈ 0.2) the default 4.x QL is well calibrated (raw p < 0.05 on
null data: 5.2 % at 3 vs 3, 5.1 % at 2 vs 2; empirical FDR at BH 5 % with 10 % DE genes:
4.7 %, 5.3 %, 4.9 % for 3v3, 2v2, 5v5) with slightly more power than the legacy method
(79.4 % vs 78.1 % at 3v3) while `glmLRT` and `exactTest` exceed the nominal FDR (8.2 %,
7.7 %); in a moderate regime (BCV ≈ 0.4) the same holds (5.0 % null rate, FDR 4.9 %). In a
harsh regime (median count 20, BCV 0.45–1, 16 replicates) the default QL is liberal: 7.1 %
of null genes at p < 0.05 (legacy 4.2 %), empirical FDR 8.4 % at 3v3 and 11.1 % at 5v5
(legacy 2.7 % / 2.3 %, LRT 17.6 % / 8.9 %). One simulation design, not a code defect,
and the regime is harsher than most bulk experiments; recorded because it is the one
place where the executed defaults did not meet their nominal level, and it belongs in a
support-site question rather than a bug report.

**N6 — dispersion grid interpolation.** `estimateDisp` evaluates the APL on 21 points
spaced a factor 2 apart (`R/estimateDisp.R:81-82`) and maximises a cubic spline through
them. Against a fine-grid maximiser of the same objective the common dispersion is 7.4e-4
off in relative terms and the tagwise dispersions a median 5.4e-4 (max 2.2e-3) log2 units
(`../verify/heldup_apl_disp.py`). Documented (`grid.length`, `grid.range`); a design
choice.

**N7 — Levenberg fit tolerance.** For non-oneway designs `glmFit` uses `mglmLevenberg`
(`src/glm.c:584-732`: Levenberg–Marquardt-damped Fisher scoring that stops when the
cross-product of the step with the score, `divergence = Σ dl·dβ`, falls below `tol = 1e-6`,
when the deviance is negligible, or on failure). Against a fully converged reference the log-likelihood at edgeR's
coefficients is lower by at most 1.6e-6, the LR statistic differs by ≤ 3.3e-6 and the
p-value by ≤ 4.7e-6; one gene of 2,000 (mean count 1,937, a flat direction of its
likelihood) has a coefficient 2.3e-3 off, the median is 6.4e-6
(`../verify/heldup_glm_lrt_ql.py`). The oneway shortcut is converged (APL to 1.7e-8).

**N8 — release-branch behaviour changes without a release NEWS entry.** Besides EG1/EG2:
`estimateDisp()` on the release branch now "uses classic model only if the design and
offset matrices are both absent" (`R/estimateDisp.R:87`, commit `bc2f1e1`, 4.10.3); the
sentence appears in the `devel` NEWS under 5.0.0 but not in the 4.10.x section. Recorded
as fact; whether to announce it is the maintainers' call (the DESeq2 round showed that a
"missing NEWS" claim is not something to file).

## Withdrawn (own suspicions killed by execution)

- **W1 — `$offset` partial matching.** R's `y$offset` partially matches `offset.prior`
  when no `offset` element exists, which is why 4.10.1's `getOffset()` (`R/getOffset.R:22`,
  `y$offset.prior <- y$offset - m`, a typo) happened to return the right matrix. Every
  place on 4.10.5 that could confuse the two on a DGEList uses `hasName()`/`[["offset"]]`
  (`R/cpm.R:9-11`, `R/rpkm.R:29`, `R/effectiveLibSizes.R:9`, `R/getOffset.R:9`); the typo
  lines are commented out. No wrong number.
- **W2 — TMM disagreed with the port by 1.2e-3.** The port's tie handling, not edgeR's (N1).
- **W3 — tagwise dispersions "0.27 log2 units off the exact maximiser".** The reference
  linearly interpolated the shared likelihood; with a fine grid the difference is 5.4e-4 (N6).
- **W4 — GLM coefficients 2.3e-3 off.** Partly the reference's own convergence (fixed by a
  trust-region polish); the residual is edgeR's tolerance (N7), and edgeR's deviance is
  never below the reference's optimum by more than 4.7e-13 in log-likelihood.

## What held up (executed, not just read)

- **TMM / RLE / upper-quartile** (`../verify/heldup_tmm_port.py`): factors from
  `normLibSizes()` equal the Robinson–Oshlack port (reference = library whose upper
  quartile is closest to the mean; M/A on library-size-scaled counts; 30 %/5 % trims by
  average rank; inverse delta-method-variance weights; geometric-mean scaling) to 4.7e-15
  on 8 random data sets with 15 % DE genes and 5 % zeros, with and without weighting and
  with a fixed reference; RLE (median ratio to the geometric mean over genes with no zero)
  and upper-quartile to 6.1e-15. `calcNormFactors()` is the same code with a rename message.
- **`filterByExpr()`** apart from EG3: the port of the documented rule (group, design via
  `1/max(hat)`, matrix input, explicit `lib.size`, `large.n`/`min.prop`) agrees on every
  decision that is not the EG3 boundary in 150 random calls; the `DGEList` method uses
  `lib.size * norm.factors` as documented (`heldup_filterbyexpr.R`).
- **`cpm()`, `rpkm()`, `aveLogCPM()`** without offsets (`heldup_cpm_avelogcpm.py`): log-CPM
  equals `log2((y + p_j)/(L_j + 2 p_j)·1e6)` with `p_j = prior.count·L_j/mean(L)` to
  5.2e-14 (prior 2 and 0.5); RPKM = CPM/(length/1000) to 5e-15; `aveLogCPM` equals the
  one-group NB maximum-likelihood mean on prior-augmented counts with augmented offsets to
  2.5e-11 (dispersion 0.05 and 0.3) and 6.2e-14 (Poisson).
- **Exact test** (`heldup_exact_test.py`): `exactTestDoubleTail` equals a scipy
  enumeration of the conditional NB law to 2.2e-15 on 371 of 398 genes (the other 27 are
  N2, all with p ≥ 0.986); relative agreement 1.4e-14 on every p < 0.05; the beta
  approximation above `big.count = 900` is within 0.2 % of the enumeration at p ≈ 1e-3 and
  0.03 % at p ≈ 6e-5; `exactTest()` end to end with equal library sizes reproduces the
  enumeration to 1.7e-15 and its `logFC` is `log2` of the prior-augmented group means
  (0.125 per library, scaled) to 7.3e-15.
- **Cox–Reid APL and `estimateDisp`** (`heldup_apl_disp.py`): `adjustedProfileLik` equals
  NB log-likelihood − ½ log det(XᵀWX) at the NB MLE to 1.7e-8 (oneway) / 8e-6 (Levenberg
  design, N7) at five dispersions; the common dispersion is exactly `maximizeInterpolant`
  of the port's grid; `prior.df` equals `limma::squeezeVar` on independently computed
  deviances at the common dispersion (21.2953 both); tagwise dispersions equal WLEB on the
  port grid to 8.6e-10 (`trend.method="none"`) and, with the default locfit trend, trended
  and tagwise to 2e-10 / 6.6e-10 using the port likelihoods and edgeR's own `locfitByCol`.
- **`glmFit`/`glmLRT`/`predFC`** (`heldup_glm_lrt_ql.py`): deviance, LR and p equal the
  NB-GLM port within the Levenberg tolerance (N7); the shrunk coefficients are the port's
  fit on `y + p_j` with offsets `log(L_j + 2 p_j)` (same tolerance) and `logFC` is exactly
  `coef/log(2)` (4.3e-14).
- **Legacy QL** (`legacy=TRUE`): `df.residual.zeros` equals `n − p` minus exact zeros with
  the design-rank adjustment on every gene; `s2.post`/`df.prior` equal `limma::squeezeVar`
  called directly (0 difference); `F = (LR/df)/s2.post`, `df.total = min(df.prior + df,
  Σdf)` and `p = pf()` to 6e-13 / 0 / 2e-15 on 4.10.5 and 4.0.16.
- **New QL** (`legacy=FALSE`, default since 4.2.0): `top.proportion` equals
  `chooseLowessSpan(G·√df, 20, 0.02)` (0.1815), the NB dispersion equals
  `estimateGLMCommonDisp` on that top fraction (0.61785), the average QL dispersion is
  floored at 1 as coded, F/`df.total`/p recompute from the fit's adjusted deviance and df
  to 3.4e-13 / 3.9e-14 / 2e-15, adjusted df lie in (0, n − p], adjusted deviances are
  non-negative; `poisson.bound` is inert under `legacy=FALSE` as its help page says.
- **`topTags`/`decideTests`**: BH over all tested genes (`p.adjust` on the whole table,
  `R/topTags.R:41`), sort by p then |logFC|, the `p.value` filter on adjusted p, `lfc` on
  the shrunk logFC with sign, a warning when a multi-coefficient table is sorted by logFC.
- **Calibration** in typical and moderate dispersion regimes (N5).

## Not audited

`glmTreat`, `diffSplice`/`diffSpliceDGE`, `voomLmFit`, the gene-set methods (`camera`,
`fry`, `roast`, `goana`, `kegga`), the quantification readers (`catchSalmon`,
`catchKallisto`, `catchRSEM`, `catchOarfish`, `DGEListFromTximport` beyond the offset
convention), `processAmplicons`, `estimateDisp(robust=TRUE)` and observation weights,
`TMMwsp` beyond its agreement with TMM on zero-free data, the `SummarizedExperiment`
methods beyond dispatch, the `devel`-only 5.0 additions (`binQLFit`, OpenMP threading),
and all plotting.
