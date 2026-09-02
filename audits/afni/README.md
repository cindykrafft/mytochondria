# AFNI correctness audit, and its exposure in 39 + 57 published papers

_Companion to `../freesurfer/` and `../fsl/`. Audit conducted 2026-08-27 against
`afni/afni` master @ `0488c9e`; ReHo exposure analysis extended 2026-08-29._

## What this is

Unlike the FreeSurfer and FSL entries, this audit ran in the other direction. Rather
than starting from the survey cohort and reading only what those papers used, nine
parallel subsystem audits swept the parts of AFNI where a correctness bug most
directly changes a published number: the statistical distribution library and p-value
machinery, group statistics in C, cluster-extent inference, the single-subject GLM,
registration/motion/interpolation and NIfTI I/O, resting-state and connectivity tools,
the R-based group programs, core dataset arithmetic, and the Python pipeline plus
DTI/PCA tools. Nine component reviews with file:line evidence live in
`component-reviews/`.

The survey cohort was then used the usual way, as the exposure denominator: the
six-journal survey found **39 papers** in PNAS (38) and *Nature* (1), 2021–2025, that
used AFNI. Each full text was re-mined for which AFNI programs it ran
(`afni_papers.tsv`), and per-paper exposure joined in `afni_paper_exposure.tsv`.

One finding, AF1 (`3dReHo`), turned out to have real published exposure, so it got a
second and much wider literature pass of its own — 398 Europe PMC records, 310 full
texts retrieved, **57 papers adjudicated individually**. That analysis is the second
half of this page.

**Epistemic status.** Code-level findings. "CONFIRMED" means the correct mathematics
was derived independently and, in most cases, reproduced numerically in isolation:
standalone C harnesses compiled from the actual translation units, comparison against
SciPy reference distributions, fuzz tests against sorted references, Monte-Carlo
simulation of random-field and ARMA models. None was reproduced by running shipped
AFNI binaries on imaging data. AFNI has many deliberate conventions; those were
separated from genuine defects and are listed apart. "Exposed" means a paper used the
affected feature or version — not that its conclusions are wrong.

## Tally

| | |
|---|---|
| Confirmed, real potential to have affected published numbers | 9 |
| Confirmed, narrower exposure | 15 |
| Likely bugs and consequential convention/doc inconsistencies | 12 |
| High-stakes code paths verified correct, most of them numerically | 40+ |

## How the papers use AFNI

| Feature | Papers |
|---|---|
| Single-subject GLM (3dDeconvolve/3dREMLfit) | 10 |
| Slice timing (3dTshift) | 10 |
| Percent signal change scaling | 9 |
| Registration/alignment (align_epi_anat/3dAllineate/3dQwarp) | 5 |
| Motion correction (3dvolreg) | 4 |
| Surface analysis (SUMA) | 4 |
| Smoothing (3dmerge/3dBlurToFWHM/3dBlurInMask) | 3 |
| afni_proc.py / ROI extraction / group mixed effects / group t-tests | 2 each |
| Cluster-extent inference (3dClustSim/3dFWHMx) / bandpass (3dTproject) | 2 / 2 |

Explicit commands, top of list: `3dDeconvolve` 8, `3dTshift` 7, `3dDespike` 4,
`3dvolreg` 4, `SUMA` 4, `3dREMLfit` 3, `3dQwarp` 3. Versions named: `20160207` (4),
then 18.0.05, 18.3.01, 21.1.10, 16.2.07, 2016.09.04.1341 — most papers state none.

17 of the 39 ran at least one program carrying a finding; per-paper conditions are in
`afni_paper_exposure.tsv`.

## Tier 1 — confirmed, high impact

**AF1. `3dReHo`'s Kendall's W tie detection truncates floats to integers.**
CONFIRMED, numerically reproduced, **and the one finding with documented published
exposure.** `src/ptaylor/rsfc.c:63-118`. Ranks come from a true float sort, but tie
*detection* compares int-truncated values (`int *sorted` receiving
`THD_get_voxel()` floats), so distinct values sharing an integer part are treated as
tied: their ranks collapse to a group average and the tie-correction term is
spuriously inflated. Raw EPI (hundreds to thousands) is essentially unaffected;
percent-signal-change data — exactly what `afni_proc.py`'s default `scale` block
produces — is of order 1. Measured relative error: 1.4% at data scale 3, **20.4% at
scale 1**, 54% at scale 0.5. Two further properties make it more than a rescaling:

- **AF1b** — a tie run reaching the end of the sorted array is never finalized, so
  input that fits entirely inside one integer bin gets *no* correction and comes out
  exactly right. The error curve is therefore non-monotonic.
- **AF1c** — the number of spurious ties tracks each voxel's own amplitude, so the
  statistic becomes partly a measure of BOLD variance. Two simulated groups with
  identical true ReHo and a 25% amplitude difference separate at **Cohen's d ≈ 2.7**.

Fixed upstream: **[afni/afni PR #944](https://github.com/afni/afni/pull/944)**,
merged 2026-08-28 (commit `a0a9530`).
Harness: `reproductions/reho_tie_sim.py`.

**AF2. `3dttest++ -paired -zskip` silently zeroes valid voxels.** CONFIRMED with a
compiled harness (correct answer t = 5.0, program outputs 0). `3dttest++.c:4848`: a
missing `!IS_PAIRED` guard lets the A-set-only zskip reduction overwrite the
pair-aligned arrays; the paired test then detects a length mismatch and writes
mean = 0, t/z = 0 — false negatives at exactly the partial-coverage voxels `-zskip`
exists to rescue. Exposure window May 2021 onwards.

**AF3. `3dMEMA -missing_data`: two degrees-of-freedom bugs.** CONFIRMED.
`3dMEMA.R:2516-2517, 2547`. A double negative inflates voxelwise DF by twice the
group-1 missing count; and under `-unequal_variance`, group-2 t-statistics are
CDF-converted with group-1's DF. Anticonservative p-values at missing-data voxels.

**AF4. `3dLMEr` with both `-gltCode` and `-glfCode` stamps statistics on the wrong
sub-bricks.** CONFIRMED. `3dLMEr.R:1401-1402`: the GLF stat-type index omits a factor
of 2 on `num_glt`, so a Z of 3 displays p ≈ 0.22 instead of 0.0027 and GLF bricks lose
their statistical type. Stored values are right; every p-value read off them is wrong.

**AF5. `3dMVM -robust` GLT z-conversion omits the /2 for two-sided p.** CONFIRMED.
`3dMVM.R:1253` uses `qnorm(p)` where the same authors' correct `qnorm(p/2)` appears
elsewhere in the tree. Conservative — findings stand, effects may have been missed.

**AF6. NIfTI sequential-descending slice timing is silently discarded, making slice-
timing correction a no-op.** CONFIRMED. `thd_niftiread.c:653` compares `kk >=
slice_end` instead of `slice_start`, so every slice offset stays zero and `3dTshift`
"succeeds" without correcting. Up to ~1 TR of uncorrected misalignment, including for
files AFNI itself writes.

**AF7. `3dROIstats -sigma`'s Bessel correction is an integer-division no-op.**
CONFIRMED. `3dROIstats.c:1183, 1195`: `voxels[i]/(voxels[i]-1)` in `long` arithmetic
is 1 for every N ≥ 2, so the reported SD is the population SD — biased low by
√((N−1)/N), −5.1% at N=10 — and inconsistent with `3dmaskave -sigma`, which is right.

**AF8. `3dcalc`'s `atanh()` silently returns its input outside the domain.**
CONFIRMED. `parser.f:1062-1065`: `atanh(1) = 1`, likewise `asin`/`acos`/`acosh`. A
deliberate anti-NaN design, undocumented. Fisher r→z via `3dcalc -expr 'atanh(a)'` is
a standard connectivity step, and r = ±1 voxels get z = ±1.0.

**AF9. ACF "effective FWHM" is √2 (~41%) larger than kernel FWHM by construction.**
CONFIRMED numerically (8 mm kernel → 11.31 reported). `mri_fwhm.c:1211-1218`. The help
attributes the gap to "long tails", conflating a real tail effect with a hard-wired
definition change; `3dBlurToFWHM -acf -FWHM G` therefore delivers only ≈G/√2 of
kernel-equivalent smoothing. **`3dClustSim -acf` cluster p-values are unaffected** —
only (a,b,c) are passed and the simulation reproduces the ACF itself.

## Tier 2 — confirmed, narrower exposure

`3dttest++ -BminusA` with `-nomeans/-notests` negates the wrong slots, inverting
direction (AF10) · a stale private t→z copy in `3dttest++`/`3dGroupInCorr` saturates
at z = 13.0 (AF11) · `3dTstat -DW` seeds its denominator with the raw first sample,
`-tdiff` subtracts the wrong line, `-nzmean` writes NaN for all-zero voxels, and a
25-byte label buffer can overrun (AF12) · `3dTshift -no_detrend` demeans the wrong
array, striping every second voxel (AF12b) · `3dBrickStat -automask` truncates its
scan to the first *count* voxels, dropping roughly half the brain, and `-absolute`
applies integer `abs()` to a double (AF13) · `3dDWItoDT`'s nonlinear path NaNs on a
zero-gradient row (AF14) · `1dgenARMA11 -arma31/-arma51` truncates its cutoff test
with integer `abs()` (AF15) · `3dpc` sub-brick labels overstate variance by ~0.5
points (AF16) · an ETAC realloc copy-paste aliases `tfs` into `fps` (AF16b) ·
`3dmaskave -perc 100` reads one past the sorted array and `-perc 50 ≠ -median`
(AF20) · RGB→gray uses 0.144 for blue and multiplies by 255 twice (AF21).

Full evidence in `component-reviews/`.

## Tier 3 — likely bugs and consequential conventions

`3dTproject` removes passband-edge bins that `3dBandpass`/`1dBport` keep, ~4 DOF
(AF18) · `3dDWItoDT`'s default nonlinear fit has an H₋ off-diagonal sign error that
can stall above the true minimum (AF14b) · the `3dANOVA` family and legacy `3dttest`
accumulate raw-score sums of squares in single precision (AF17) · `3dRSFC` drops the
top frequency bin for odd N (AF19) · `3dTrackID` can write NaN per-bundle stdevs
(AF22) · `timing_tool.py` overwrites rather than accumulates within-TR fractions and
skips single-event files (AF23) · `3dDespike` uses 1.2533×MAD instead of 1.4826×MAD,
so the documented 2.5σ/4σ cuts really act at ~2.11σ/3.38σ · GLTs omitting a covariate
evaluate at the sample mean, not `-qVarCenters` · `3dMEMA`'s I² and `3dMVM -wsE2`
minor defects.

## Tier 4 — latent, dormant, dead code

No wrong numbers in shipped use, but landmines: `remla.c`'s ARMA(3,1)/(5,1)
root-to-coefficient formulas use the *sum* instead of the *product* of roots (compiled
into `3dREMLfit`, never called) · `3dClustSim -tdof` thresholds t values at Gaussian
quantiles · `wsinc5` with `AFNI_WSINC5_RADIUS=20` sums 41 taps where 40 are
initialized · `AFNI_dicomm_to_xyz` applies the forward instead of inverse permutation
(zero callers) · `#if 0` cluster finders with a wrong bounds test · the pure-R
`AFNIio.R` fallback reads bytes as signed · several unreachable `afni_util.py` paths.

## What held up

The reassuring part, and the highest-stakes machinery in the package:

- **The complete `mri_stats.c` p-value library** against SciPy — t, F, correlation,
  chi-square, normal, beta, binomial, gamma, Poisson and inverses, to reference
  precision including extreme tails.
- **The entire post-2015 ACF cluster-inference pipeline**: 3dFWHMx ACF fitting, the
  Monte-Carlo-validated ACF random-field generator, 3dClustSim sidedness and alpha
  tables with no off-by-one, matching NN cluster definitions in simulation and data.
- **`3dDeconvolve`**: design matrix, Legendre baselines, censoring/DF bookkeeping,
  GLT t/F, and the BLOCK/SPM/TENT/CSPLIN bases against closed forms. **`3dREMLfit`**'s
  live ARMA(1,1) path, validated by direct simulation.
- **`3dvolreg`** motion conventions and shear decomposition (300,000 random cases, max
  error ~1e-8); NIfTI qform/sform L-R handling — no flip risk; all interpolation
  kernels.
- **`3dttest++`** core t/Welch/covariate formulas and its permutation machinery; the
  2005-era `3dANOVA3` type 4/5 contrast fixes.
- **Kendall tau-b** (fuzzed against SciPy), Spearman tie handling, Pearson/partial
  correlation, Fisher-z conventions in the C tools.
- **`afni_proc.py` numerics**: percent-signal-change scaling, motion enorm, censor
  bookkeeping, outlier logic, TSNR.

## AF1 in the literature: a dedicated exposure audit

AF1 was the only finding worth a full literature pass, because its trigger — the
numeric scale of the file handed to `3dReHo` — is a property of ordinary pipelines
rather than a rare flag.

**Method.** Europe PMC full-text search for `3dReHo` and variants (70 records), ReHo ×
`afni_proc.py` (14) and ReHo × AFNI (382); 398 unique records, 310 full texts
retrieved via the Europe PMC OA endpoint and PMC article pages; plus all 205 works
citing Taylor & Saad 2013, screened for ReHo. **57 papers** named `3dReHo` or ran AFNI
ReHo and were adjudicated one by one against the criterion below.

**The criterion.** From `reproductions/reho_tie_sim.py`: a study is exposed if the
per-voxel time-series SD, *in the units of the file passed to `3dReHo`*, falls roughly
between **0.4 and 3**. Percent-signal-change data (SD ≈ 0.5–2) and z-scored data
(SD = 1) sit inside it. Native scanner units, grand-mean scaling to 10,000, and
L2-normalised series all fall outside.

**Exposed (5).**

| Paper | Journal | Evidence | Regime |
|---|---|---|---|
| Huang et al. 2018 (PMID 29386261) | *J Neurosci* | "the time course per voxel of each run was normalized to zero mean and unit variance (z-value)" → `3dReHo` | SD = 1, worst |
| Campbell et al. 2020 (PMID 31672663) | *NeuroImage* | same pipeline, same wording | SD = 1, worst |
| PMID 35687994 | *NeuroImage: Clinical* | "Voxel-wise signal was scaled to a mean value of 100" → "AFNI's 3dReHo" | mean 100 |
| PMID 32845057 | *Hum Brain Mapp* | `afni_proc.py` full pipeline (default blocks include `scale`) + `3dReHo` | mean 100 |
| PMID 35470550 | *Addiction Biology* | all-AFNI `afni_proc.py` pipeline; ReHo the primary outcome, 27-voxel neighbourhood | mean 100 |

The last two are inferred from `afni_proc.py` defaults rather than an explicit
statement, and are the ones an email to the authors would settle. A sixth, Fujimoto
et al. 2026 (*Nature Communications*, "converted to percent signal change" → `3dReHo`
on run residuals) was identified in the first screening pass but could not be
re-located in the Europe PMC full-text index for this one; it is carried here
unverified.

**Reclassified out.** Skipper et al. 2022 (*Cerebral Cortex*, PMID 34585723)
normalised its ReHo input "to have a sum of squares of one". An earlier pass called
that the maximal-tie regime; it is the opposite. L2 normalisation bounds every value
in [−1, 1], which puts the whole series in one integer bin, which by AF1b receives no
tie correction at all — the result is exactly correct. Recording this because it is
the clearest case in this repository of a reproduction *shrinking* a finding.

**Cleared (52).** Every major wrapper pipeline turned out to be safe, which clears a
large share of the field at once: **XCP-D** denoises with `standardize=False` and
keeps native units (its mean-centring and variance-normalisation apply to ALFF only);
**ENIGMA HALFpipe**, **PhiPipe** and **CCS** all grand-mean scale to 10,000;
**C-PAC** and **DPARSF/DPABI** do not call `3dReHo` at all. This also revises the
first screening pass, which had listed XCP-D as multiplying downstream exposure.

**Could not be read (11).** Paywalled, no PMC deposit; publisher pages returned
403/404 to automated fetching. Listed with PMIDs in the exposure notes. For each the
single question is what units the file passed to `3dReHo` had.

**Blind spot.** Full-text search reaches only open-access and PMC-deposited work, and
methods sections almost never state numeric scale. A paper in a fully paywalled
journal that cites only Zang 2004 and says "ReHo was computed in AFNI" is invisible to
every route used here. "Zero confirmed" for the other findings means zero *documented*
affected configurations, not zero uses — command flags are rarely written into methods
sections at all.

## AF1 on open data: the published design, re-run under both builds

With PR #944 merged, `reanalysis/` re-runs the exposed papers' design —
`afni_proc.py` with the default `scale` block, `3dReHo`, a two-sample group
contrast — on OpenNeuro ds000030 (20 CONTROL + 20 SCHZ) with the pre-fix and
post-fix 3dReHo on identical residuals. Pre-fix ReHo maps carry a 57 % mean
error (range 23–65 %, tracking each subject's residual SD at r = 0.78) and
correlate only r = 0.60 with the correct maps; the SCZ-vs-CONTROL t-maps from
the two builds correlate 0.66, disagree in sign at 19 % of voxels, and their
p < .001 sets share one voxel in 44. Details, per-subject table, t-maps and
scripts in [`reanalysis/README.md`](reanalysis/README.md).

## Files

| File | Contents |
|---|---|
| `afni_papers.tsv` | 39 survey papers × versions × commands × features |
| `afni_paper_exposure.tsv` | per-paper applicable findings (conditions in parentheses) |
| `component-reviews/*.md` | the nine subsystem reviews with file:line evidence |
| `afni_profile.py` | the script that mined AFNI usage from paper full texts (self-seeding from `survey/data/`; writes `afni_profiles.jsonl`) |
| `build_tables.py` | joins the profiles into the two tables above |
| `reproductions/` | the AF1 harness and its checked-in results |
| `upstream/` | what has been filed, and what is ready to file |
| `reanalysis/` | the ds000030 pre-fix vs post-fix 3dReHo pilot: scripts, subject lists, results |

## Filing route

AFNI takes issues and pull requests on GitHub and reports on the AFNI Message Board —
both open, unlike FSL's. AF1 is fixed by
[PR #944](https://github.com/afni/afni/pull/944), merged 2026-08-28. The rest are written
up and ready;
see `upstream/README.md` for the queue and the fix shapes.

## Scope

AFNI is millions of lines across ~600 programs. Coverage went deep on the subsystems
most likely to affect published numbers; SUMA, InstaCorr, the GUI rendering path,
physiological-noise regression and most smaller programs received light or no
coverage. More findings certainly remain.
