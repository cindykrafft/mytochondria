# Pre-specified plan: AFNI pipeline made analogous to Cattarinussi et al. 2024 (ds000030 ReHo)

Written before any result of this pipeline was seen. Target: Cattarinussi, Di Camillo, Grimaldi et al.,
Eur Arch Psychiatry Clin Neurosci 2024, doi 10.1007/s00406-024-01838-4 (DPABI + SPM12, ds000030).
Their published pipeline, and the AFNI analogue used here:

| step | Cattarinussi 2024 (as published) | this pipeline | note |
|---|---|---|---|
| sample | 40 SCZ, 59 HC (of 50 / 130); HC with lifetime psychiatric dx, and anyone with medical illness, substance use, MDD, anxiety, ADHD history excluded; 10 excluded for head motion | all 50 SCHZ; HC by identifier until 59 pass; ds000030 phenotype tables used for the same exclusions where the columns exist | selection rule fixed here |
| discarded volumes | not stated (DPARSF default 10) | 10 | |
| slice timing | not stated (DPARSF default on) | on (tshift) | |
| despike | none | none | previously on |
| realignment | SPM realign | 3dvolreg to MIN_OUTLIER | |
| motion exclusion | "excessive head motion", threshold unstated | max abs translation > 3 mm or rotation > 3 deg (the DPARSF-era convention) | fixed here |
| normalisation | DARTEL, 3 mm iso | affine to MNI152 2009 (afni_proc -tlrc), 3 mm iso | nonlinear (-tlrc_NL_warp) not run for time; noted as a difference |
| units | raw (DPABI keeps scanner units) | percent signal change (afni_proc scale) | deliberately kept: this is the regime that triggers the 3dReHo defect and the one every afni_proc user is in; the fixed build is unaffected by units |
| nuisance | Friston-24 + mean WM + mean CSF; no GSR; no scrubbing | 3dTproject: Friston-24 (6 params, squares, lag-1, lag-1 squares) + eroded-WM and eroded-CSF means (afni_proc -mask_segment_anat); no GSR; no censoring | previously 12 motion + censoring at 0.3 mm |
| detrend | DPARSF detrend | polort 1 | |
| band-pass | not stated (DPARSF ReHo default 0.01-0.08 Hz, before ReHo) | 0.01-0.08 Hz in 3dTproject, before ReHo | previously 0.01-0.1 |
| smoothing | 4 mm FWHM applied to the ReHo map | 4 mm FWHM (3dmerge) applied to the ReHo map | previously 4 mm on the time series before ReHo |
| ReHo | KCC, 27 voxels, z-normalised across the brain per subject | 3dReHo -nneigh 27 from both builds on the identical residuals; z-normalised within the subject's brain mask | z-normalisation is new |
| group model | one-way ANOVA (SCZ, BD, HC), pairwise t-tests; no covariates stated | 3dttest++ two-sample SCZ vs HC, no covariates | |
| correction | voxel p < 0.001, cluster FWE 0.05 (SPM RFT) | voxel p < 0.001, cluster FWE 0.05 by 3dttest++ -Clustsim (10,000 sign-flips), NN1, bi-sided; p < 0.01 reported too | |
| mask | SPM implicit | voxels in >= 90 % of subject masks | |

Outcome measures, fixed in advance: for each build, the corrected clusters and their labels; whether the
published pattern (SCZ < HC: L superior occipital, R inferior occipital, R postcentral; SCZ > HC: R anterior
orbital, L posterior orbital, bilateral temporal pole, R hippocampus, L cerebellum) is reproduced, scored as
the fraction of those nine regions containing a corrected cluster of the same sign; uncorrected agreement
with the same regions at |t| > 3.4 (voxel p < .001); and, between builds, the same overlap statistics as before.
Both builds are reported whatever the outcome.
