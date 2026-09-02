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
(guaranteed in scRNA-seq). Upstream fixed it in Aug 2025 (`abe5994`, released
as 1.49.4) **with a NEWS entry** under 1.49.4: "The wrong weights matrix was
being used when recomputing the SE within results() for the numeric-style
contrast. Fixed." An earlier version of this page, and the issue filed upstream,
claimed no NEWS entry existed. That was wrong: the audit checked the fix
commit's diff, which does not touch NEWS, and missed the same-day version-bump
commit (`5f5e305`) that added the entry. The entry does not name the affected
release range (1.16.0–1.49.x) or the weights/zinbwave workflow, which is why a
user of that workflow is unlikely to find it; the maintainer closed the request
as already documented. Cohort exposure: 1 paper names zinbwave; 62 single-cell
papers are candidates.

**DS2 — CONFIRMED behavior change. `lfcThreshold` tests are a different statistic
before and after v1.44.0 (2024).** Old: 2·Φ((T−|LFC|)/SE) capped; new: the more
powerful two-term formula. Same data: p-values differ up to 2×, +19% rejections
at padj<0.05 (T=0.585 sim), 0.8% of calls flip. Both are valid tests; results
simply don't reproduce across the version boundary (`greaterAbs2014` restores the
old one). This is documented in NEWS under 1.44.0, naming `greaterAbs2014`; the
upstream visibility request was closed as already documented. 5 cohort papers
use lfcThreshold explicitly.

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

## Filing outcome (2026-09-01) and what went wrong

Four items were filed on `thelovelab/DESeq2`: issue #130 (NEWS/erratum for
DS1), issue #133 (visibility for DS2), and issue #131 + PR #132 (the one-line
`round()` change). The maintainer closed all four within two hours, pointing to
the project's pinned policy (issue #1): the DS1 and DS2 changes were already in
NEWS, and the PR "would change DESeq2 results and so won't be taken on."

He was right on each point. The audit's process failures, recorded here so the
next audit does not repeat them:

- **It misread the repository's own history.** The claim that no NEWS entry
  existed for DS1 came from inspecting the fix commit alone. The entry was added
  in the adjacent version-bump commit. NEWS itself was never grepped.
- **It did not read the contribution guidelines.** DESeq2's pinned issue #1
  (since 2017) and `CONTRIBUTING.md` (July 2026) both say non-minor PRs should
  be discussed on the Bioconductor support site first, and the maintainer will
  not take changes that alter results without prior discussion. The audit's own
  review rated the rounding bias "verified negligible" and still sent a
  results-changing PR cold. That is a cost to the maintainer with no benefit.
- **It treated a GitHub repo like every other GitHub repo.** For Bioconductor
  packages the support site is the primary channel; GitHub is for browsing and
  discussed PRs.

Nothing further is filed. A support-site notice for zinbwave/weights users was
drafted (`upstream/support-post-zinbwave.md`) and stays unposted: the
maintainer has reviewed the finding and judged the NEWS entry sufficient, and
with one cohort paper naming zinbwave the exposure does not warrant going
around that judgment. The reproduction script is public here for anyone who
needs to check an old analysis. The rounding change is withdrawn: the effect
was measured as negligible and the project's policy is to keep results stable.
