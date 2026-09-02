# Component: DESeq2 statistical core (v1.53.2 devel, history to 2014)

Read in full: core.R (2938 lines), fitNbinomGLMs.R, src/DESeq2.cpp, wrappers.R,
results.R, lfcShrink.R, parallel.R, expanded.R; targeted reads of methods.R,
helper.R, vst.R, rlog.R. Every suspect quantified before being called a finding
(Python/scipy harnesses + the shipped 1.42.1 binary run on synthetic data).
Git history consulted to date defects to released versions.

## Confirmed findings

**DS1 CONFIRMED (upstream-fixed 2025-08-18, commit abe5994, released 1.49.4 with a NEWS
entry added in 5f5e305 the same day; an earlier draft here wrongly said none existed): observation
weights misaligned in results(contrast=).** `getContrast()` (results.R:786 pre-fix)
subsets counts/dispersions/betas to non-all-zero rows (`objectNZ`) but took the
weights matrix from the UNSUBSET object. The C++ `fitBeta` does no dimension check,
so gene i's counts are paired with gene (i+offset)'s weights, offset = number of
preceding all-zero rows. Introduced 5ff4c17 (2017-02-21) => affected RELEASES
1.16.0 through 1.49.x — every version used by the surveyed papers.
Reproduced on shipped 1.42.1 (2000 genes, 10% all-zero, zinbwave-style weights):
lfcSE ratio contrast/name 0.42–2.54x, 33.8% of genes off >10%, 1.78% of p<0.05
calls flip, worst p-ratio 12.7x. Controls (no zeros / no weights) agree to 7e-16.
Conditions: `assays(dds)$weights` present (zinbwave scRNA-seq workflow — documented
in the DESeq2 vignette era — or any user weights) AND results(contrast=) via the
numeric/list/non-reference-level path AND >=1 all-zero gene (guaranteed in scRNA).
`results(name=)` and reference-level character contrasts were never affected.
Cohort exposure: 1 paper names zinbwave explicitly; 62 single-cell papers are
candidates. Filed as issue #130 requesting a fuller NEWS entry; closed by the maintainer
as already documented (the 1.49.4 entry exists but names neither the release range nor
the weights workflow). Remaining route: a support-site post.

**DS2 CONFIRMED (behavior change, not a bug): lfcThreshold tests changed definition
at 1.43.2 (2024-02-01, commit 0247fd7; first release 1.44.0).** `altHypothesis=
"greaterAbs"` was 2·pnorm((|LFC|−T)/SE) capped at 1 (2014–2023); now it is
Φ((−|LFC|+T)/SE) + Φ((−|LFC|−T)/SE) (more powerful, still valid). Same data, same
call: p-values differ up to 2x (median ratio 1.22), +19% padj<0.05 rejections at
T=0.585 in a realistic simulation, 0.8% of genes flip. `greaterAbs2014` exists for
back-compatibility but is not the default. Papers pinning <=1.42 vs >=1.44 with an
lfcThreshold cannot be numerically reproduced across the boundary without knowing
this. 5 cohort papers use lfcThreshold explicitly.

**DS3 CONFIRMED (loud, fixed): greaterAbs + useT=TRUE broken 1.44–1.52.** The
2024 rewrite captured the vector `df` in a closure misused by mapply (fixed
01c54bb/667c7b9, Oct–Nov 2025). Failure is an error/garbage-shaped output, not a
silent bias; affects glmGamPoi/useT users with a threshold. Note-level.

## Verified negligible (real imprecision, quantified, below materiality)

**DS-N1: LRT reduced=~1 fast path is not the exact MLE.** fitNbinomGLMs.R:104-137
sets the intercept fit to the arithmetic mean of normalized counts — the exact NB
MLE only when all size factors are equal (the (1+α·nf·q) weights then cancel;
verified analytically). With unequal size factors every `nbinomLRT(reduced=~1)`
statistic is inflated by 2·[ll(q̂_MLE) − ll(q̄)]. Quantified: mean inflation
1e-4–7e-3 (p95 <0.03) across α∈[0.05,0.5], size-factor spread up to 3x, µ≥10;
achieved test size identical to 4 decimals. Real, but immaterial.

**DS-N2: replaceOutliers truncates instead of rounding.** core.R:2111-2116 uses
`as.integer(trimmedMean × sf)` — floor, biasing replacement counts low by ~0.5.
One-line `round()` fix; effect negligible except at very low counts.

**DS-N3: dispersion grid fallback quantization.** Non-converged genes get
grid-refit at resolution ~0.115 log-α (±5.7% dispersion; wrappers.R:70-72), and a
line search converging in exactly 1 iteration is counted as NOT converged
(core.R:833 `!(dispIter == 1)`), sending already-converged genes to the grid.
Conservative wobble on few genes.

**DS-N4 cosmetic:** lfcShrink FSOS s-value description overwritten by the generic
label (lfcShrink.R:489-494); UPSHOT p-values provably ≤1 (own suspicion raised
during review, then withdrawn by proof — pairing argument on the interval average).

## What held up (verified, not just read)

- **C++ dispersion machinery**: log_posterior/dlog_posterior algebra re-derived
  term-by-term (matches; constants-in-α dropped legitimately); Cox-Reid term and
  its first two derivatives; Armijo backtracking with correct edge clamps at
  log α = −30/10.
- **fitBeta IRLS**: ridge-via-QR-augmentation solves (X'WX+Λ)β = X'Wz exactly;
  sandwich covariance (X'WX+Λ)⁻¹X'WX(X'WX+Λ)⁻¹ consistent across the C++, the R
  diagnostic helper, and getContrast (identical ridge constants at both call
  sites: 1e-6/log2² = 1/(log2²·1e6)).
- **Cook's outlier machinery**: trimmedCellVariance scale constants match their
  documented derivation to 3 digits (2.042/1.864/1.510 vs 2.04/1.86/1.51);
  false-flag rate on clean NB data 0–0.35% at the qf(.99) cutoff — conservative
  (simulated n=3..10 per group, α=0.05..0.5).
- **parallel.R**: dispersion trend, dispersion prior variance and beta prior
  variance all estimated globally between parallel phases — parallel ≡ serial.
- **results() machinery**: contrast maxit=0 trick reuses stored betas exactly;
  all-zero-contrast zeroing logic; threshold-test formulas (greaterAbs 2014 and
  2024, lessAbs, greater/less, UPSHOT integral identity verified analytically).
- **Default Wald calibration** (context): FPR@0.05 = 0.063/0.056/0.059 at
  3v3/5v5/10v10 on clean NB — the known, published mild anticonservativeness of
  the normal-null Wald; a method property, not a defect.
- **VST closed form** = the textbook asinh-form (algebraic identity checked);
  size-factor median-of-ratios (the finiteness filter provably implies all-positive
  rows for type="ratio"); LRT uses full dnbinom so constants cancel; collapseReplicates
  overflow-guarded by its checksum stopifnot; Hmisc wtd.quantile port faithful.

## Maps to papers

~870 of 886 papers run defaults (only 10 mention independent filtering, 4 Cook's):
default-path findings dominate. DS1: 1 confirmed zinbwave + 62 single-cell
candidates. DS2: 5 explicit lfcThreshold papers + silent users. LRT papers (55)
unaffected in practice (DS-N1 negligible). Wald/default papers: no confirmed
defect — the core default chain survived the audit.
