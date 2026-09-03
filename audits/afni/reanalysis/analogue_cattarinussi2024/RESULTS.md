# Results: AFNI pipeline analogous to Cattarinussi et al. 2024, both 3dReHo builds

Pre-specified in PLAN.md (with amendment 1) before any result was seen. Sample after motion exclusion
(3 mm / 3 deg; 5 excluded, 0 for alignment): 60 CONTROL, 47 SCHZ (df 105). Group mask (>= 90 % of subject
masks): 57,207 voxels. Raw outputs: `results/`.

## Per participant (unsmoothed ReHo before z-normalisation; `results/subjects_summary_dpabi.tsv`)

| | CONTROL (n = 60) | SCHZ (n = 47) | p |
|---|---|---|---|
| age | 30.5 ± 8.8 | 36.5 ± 8.8 | 0.001 |
| sex F / M | 28 / 32 | 12 / 35 | 0.028 |
| mean motion (enorm, mm) | 0.103 ± 0.049 | 0.179 ± 0.112 | < 0.001 |
| residual SD handed to 3dReHo | 0.329 ± 0.042 | 0.357 ± 0.067 | 0.008 |
| pre-fix zeroed voxels | 9.6 % | 7.7 % | 0.12 |
| pre-fix / post-fix whole-brain mean | 0.333 | 0.361 | 0.024 |
| pre-fix vs post-fix map correlation | 0.54 | 0.53 | 0.72 |

Without censoring, patients' residual amplitude is *higher* than controls' (motion), the opposite of the
censored afni_proc pipeline, so the amplitude-dependent bias now favours the patients. Global mean ReHo,
SCZ − CONTROL: pre-fix +0.0002 (t = 0.04, p = 0.97, d = 0.01); released code (hist) −0.016
(t = −4.97, p < 0.001, d = −0.96); post-fix −0.017 (t = −3.64, p < 0.001, d = −0.71). The schizophrenia
reduction in global ReHo is absent under the 4c2bd54 build and present under the fixed build.

## Cluster-level inference (z-ReHo smoothed 4 mm; 3dttest++ -Clustsim, voxel p < .001 / .01, cluster FWE .05)

| build | p < .001 clusters (Neuromorphometrics label at peak, sign) | p < .01 clusters |
|---|---|---|
| pre-fix (4c2bd54) | 5: L calcarine (−, 75), L calcarine/occipital pole (−, 42), R temporal-pole white matter (+, 40), R superior frontal (+, 37), L cerebellum (+, 33) | 6: L calcarine (−, 518), R cerebellum (+, 156), R postcentral (−, 155), L cerebellum (+, 150), L superior frontal (+, 146), R hippocampus (+, 136) |
| post-fix (26.2.06) | 2: L cuneus/occipital pole (−, 33), L calcarine (−, 33) | 1: L cuneus/calcarine (−, 313) |
| released (hist) | 1: L angular gyrus (+, 29) | 1: same (+, 93) |

Between builds: t-map correlation pre vs post 0.57; sign flips 30 % of voxels; |t| > 3.39 sets share 38 of 576
voxels; corrected clusters share 42 of 251 voxels at p < .001 (the calcarine cluster) and 160 of 1,414 at p < .01.

## Scoring against the nine regions Cattarinussi 2024 report (pre-specified)

| build | mean t of the reported sign | corrected cluster of the reported sign, p < .001 | p < .01 |
|---|---|---|---|
| pre-fix | 9 / 9 | 2 / 9 (R temporal pole, L cerebellum) | 4 / 9 (+ R postcentral, R hippocampus) |
| post-fix | 8 / 9 | 0 / 9 | 0 / 9 |
| released | 7 / 9 | 0 / 9 | 0 / 9 |

Both builds reproduce the occipital SCZ < HC decrease (our peaks fall in calcarine cortex / cuneus /
occipital pole rather than in the superior and inferior occipital gyri as labelled, so the strict region
score does not credit it). Only the pre-fix build reproduces the SCZ > HC increases (temporal pole,
hippocampus, cerebellum) at corrected level. The fixed build reproduces no increase.

## Reading

The pre-specified hypothesis of interest was that the fixed build would agree with the independent
DPABI analysis better than the defective one. It does not: on this scoring the defective build agrees
better. Two facts constrain the interpretation. (1) The regions where only the pre-fix build agrees
(temporal pole, orbitofrontal, hippocampus, cerebellum) are the regions of lowest signal and highest
residual variance, and the pre-fix statistic is a function of residual amplitude (r = −0.91 across
participants between its relative error and residual SD). (2) In this sample patients move much more
than controls (0.18 vs 0.10 mm), neither this pipeline nor the target paper censors or covaries motion,
and the published analysis was unadjusted. A pre-fix increase in those regions is therefore what an
amplitude confound would produce, and its agreement with the target paper may reflect a shared
motion sensitivity rather than the target being right. A labelled post-hoc follow-up with mean motion
as a covariate (`group_covmotion_dpabi.sh`) tests this; its result is appended below when available.

## Post-hoc follow-ups (not pre-specified; labelled as such)

**1. Mean head motion as a covariate** (`group_covmotion_dpabi.sh`, `results/followup_motion_covariate.log`).
Nothing changes: pre-fix 5 / 6 clusters at p < .001 / .01 with the same peaks and sizes; post-fix 2 / 1.
A linear mean-motion covariate does not account for the pre-fix increases.

**2. Whole-brain residual SD as a covariate** (`group_covsd_dpabi.sh`, `results/followup_sd_covariate.log`).
Pre-fix clusters again unchanged (5 / 6). Expected in hindsight: the maps are z-normalised per subject,
so a global amplitude covariate cannot remove a *regional* amplitude effect.

**3. Where do the two builds disagree? Voxelwise residual amplitude** (`results/ttest_residualSD_SCZvCON.nii.gz`).
Each subject's residual-SD map was z-normalised within the mask and smoothed 4 mm like the ReHo maps, and
SCZ vs CONTROL tested voxelwise (no cluster inference; used only as a map).

| | correlation across the 57k-voxel mask |
|---|---|
| t(residual SD, SCZ − CON) vs t(pre-fix z-ReHo) | **0.76** |
| t(residual SD, SCZ − CON) vs t(post-fix z-ReHo) | 0.38 |
| t(residual SD) vs [t(pre-fix) − t(post-fix)] | 0.45 |

| pre-fix corrected clusters | mean t(residual SD) inside |
|---|---|
| SCZ > HC clusters, p < .001 (110 vox: temporal pole, superior frontal, cerebellum) | **+2.5** |
| SCZ < HC clusters, p < .001 (117 vox: calcarine) | −3.4 |
| rest of mask | −0.2 |
| post-fix corrected clusters, p < .001 (66 vox: calcarine / cuneus) | −3.2 |

The pre-fix group map is largely a map of where patients' residual amplitude differs from controls'
(r = 0.76), and its SCZ > HC clusters, the ones that matched the target paper, sit precisely where
patients' residual amplitude is higher (temporal pole, orbitofrontal, hippocampus, cerebellum: the
low-signal regions). The fixed build's map is much less amplitude-bound (r = 0.38) and shows no increase
there. This is the defect's mechanism operating at the group level: on unscrubbed data with a
higher-motion patient group, the truncated-tie ReHo turns a regional amplitude difference into an
apparent synchrony increase. The occipital decrease, found by both builds and by the target paper, sits
where patients' residual amplitude is *lower*; it is the one result all three analyses share.

**Conclusion.** The pre-specified score favoured the defective build; the follow-up shows why: its extra
agreement with the target paper is in regions where the defect is driven by amplitude, not synchrony.
Whether the target paper's increases in those regions are themselves amplitude-driven cannot be decided
from here (DPABI's ReHo does not have this defect, but the paper neither scrubbed nor covaried motion);
what can be said is that on identical residuals the fixed build does not produce them.
