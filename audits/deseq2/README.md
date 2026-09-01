# DESeq2 audit against 886 published papers (2021–2026)

_Third audit in the series (FreeSurfer, FSL, → DESeq2). Generated 2026-09-01._

## What this is

The six-journal survey found **886 papers** in *Nature*, *Science*, PNAS, *Cell*
and NEJM (2021–2026) that used DESeq2 — more than FreeSurfer, FSL, SPM and AFNI
combined. Each paper's full text was re-mined for **how** it used DESeq2
(`deseq2_profiles.jsonl`: test type, shrinkage estimator, filtering, design
complexity, data domain), and the statistical core (`thelovelab/DESeq2`, ~8,900
lines of R + C++) was read in full against that usage map, with git history used
to date defects to the released versions papers actually pin.

**Method upgrade over the earlier audits:** every suspect was verified before
being written up — compiled-verbatim/faithful-port harnesses as before, plus,
for the first time, **the shipped binary run end-to-end on synthetic data with
known truth** (the container's Bioconductor release, DESeq2 1.42.1, happens to
carry the main defect). Suspicions that quantification killed are reported as
exonerations, not findings.

## How the papers use DESeq2

| Usage (from full texts) | Papers |
|---|---|
| ≥3 replicates stated | 614 |
| featureCounts/HTSeq counts | 326 / tximport (salmon/kallisto/RSEM) 225 |
| Wald named / LRT | 176 / 55 |
| paired design / interaction terms / batch covariates | 168 / 113 / 132 |
| ATAC/ChIP via DESeq2 | 86 |
| single-cell / pseudobulk | 62 |
| lfcShrink (apeglm 20, ashr 14, betaPrior 9) | 31 |
| microbiome (phyloseq/16S) | 17 |
| mention independent filtering / Cook's | 10 / 4 |

**~870 of 886 papers run the silent defaults** — independent filtering, Cook's
outlier gating, outlier replacement. Default-path code carries nearly the whole
cohort, and it is precisely the default chain that survived the audit.

## Findings

**DS1 — CONFIRMED. `results(contrast=)` with observation weights used the wrong
genes' weights, in every release from 1.16.0 (2017) to 1.49.x (2025).**
The weights matrix was taken unfiltered while counts/dispersions/betas had
all-zero genes removed; the C++ silently pairs gene i with gene (i+offset)'s
weights. Reproduced on shipped 1.42.1: lfcSE off by 0.42–2.5×, a third of genes
off >10%, 1.8% of significance calls flip, p-values off up to 12.7× — controls
agree to machine precision. Requires: weights in `assays()` (the zinbwave
single-cell workflow) + a numeric/list/non-reference contrast + ≥1 all-zero gene
(guaranteed in scRNA-seq). Upstream fixed it quietly in Aug 2025 (`abe5994`);
**no erratum or NEWS entry exists** — that is the ask. Cohort exposure: 1 paper
names zinbwave; 62 single-cell papers are candidates.

**DS2 — CONFIRMED behavior change. `lfcThreshold` tests are a different statistic
before and after v1.44.0 (2024).** Old: 2·Φ((T−|LFC|)/SE) capped; new: the more
powerful two-term formula. Same data: p-values differ up to 2×, +19% rejections
at padj<0.05 (T=0.585 sim), 0.8% of calls flip. Both are valid tests; results
simply don't reproduce across the version boundary (`greaterAbs2014` restores the
old one). 5 cohort papers use lfcThreshold explicitly.

**DS3 — note. `greaterAbs`+`useT=TRUE` was broken (loudly) in 1.44–1.52**, fixed
Oct–Nov 2025. Affects glmGamPoi/single-cell threshold tests.

**Verified negligible** (real imprecision, quantified below materiality — details
in `component-reviews/statistical-core.md`): the LRT `reduced=~1` fast path is
not the exact MLE under unequal size factors (LRT inflation ≤1e-2 typical,
test size unchanged to 4 decimals); outlier replacement floors instead of rounds;
dispersion grid-fallback quantization ±5.7% for non-converged genes.

## What held up

The default Wald chain — the code path under ~870 papers — survived: IRLS ridge
fitting exact (QR-augmentation algebra), sandwich SEs consistent across all three
call sites, C++ dispersion derivatives re-derived and matching, Cook's trim
constants correct to 3 digits with 0–0.35% false-flag rate on clean data,
parallel ≡ serial, VST closed form exact, threshold formulas verified
analytically. Null calibration reproduces the known literature values
(FPR ≈ 0.056–0.063 at nominal 0.05, 3v3–10v10) — a documented method property.
One suspicion (UPSHOT p>1) was raised and then withdrawn by proof during review.

## Files

| File | Contents |
|---|---|
| `deseq2_profiles.jsonl` | 886 papers × usage features, versions, cutoffs |
| `deseq2_profile.py` | the mining script |
| `component-reviews/statistical-core.md` | the full review with file:line evidence |
| `verify/ds1_weights_misalignment.R` | DS1 reproduction on shipped 1.42.1 |
| `verify/ds2_threshold_versions.R` | null calibration + DS2 cross-version delta |
| `verify/dsn1_lrt_fastpath.py` | DS-N1 quantification (the exoneration) |
| `verify/heldup_cooks_calibration.py` | Cook's constants + false-flag rate (held up) |

## Filing route

DESeq2 lives on GitHub (`thelovelab/DESeq2`) with a responsive maintainer; the
Bioconductor support site is the user-facing channel. DS1's code fix already
exists upstream, so the filing is: (1) a GitHub issue requesting a NEWS/erratum
entry naming the affected releases and conditions, with the reproduction script
attached; (2) a support-site post so zinbwave-workflow users can check their
analyses; (3) a docs note for DS2 version comparability; (4) a one-line
`round()` PR for the replacement-count truncation.
