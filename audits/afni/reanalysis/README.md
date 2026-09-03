# Reanalysis: AFNI PR #944 (3dReHo tie handling) on open data

**Question.** How much do published-style ReHo results change between the AFNI
`3dReHo` that every paper before 2026-08-28 ran and the fixed one (PR #944)?

**Why this design.** None of the five papers exposed to the ReHo tie bug (see
`../README.md`, "Exposed (5)") shares its imaging data. Three of them run the
same pipeline: `afni_proc.py` with its default `scale` block (percent signal
change) followed by `3dReHo`, then a group contrast. That pipeline is run here
on an open dataset with a clinical contrast, so the comparison is of the
*published design*, not of the papers' own numbers.

**Dataset.** OpenNeuro ds000030 (UCLA Consortium for Neuropsychiatric
Phenomics), resting-state fMRI, 3 T. Pilot: 20 CONTROL + 20 SCHZ that
pass the pipeline, later enlarged to 40 CONTROL + 33 SCHZ (see *Enlarged sample*
below). Pilot lists: 20 CONTROL + 20 SCHZ that
pass the pipeline (`subjects.tsv` lists the first 20 eligible of each with rest + T1w;
`subjects_spare.tsv` the top-up pool used when a subject failed censoring, see
Exclusions below).

**Pipeline.** `scripts/run_subject.sh`: `afni_proc.py` blocks
despike/tshift/align/tlrc/volreg/blur(4 mm)/mask/**scale**/regress, MNI152
2009 template, bandpass 0.01–0.1 Hz, motion (0.3 mm) and outlier censoring,
demeaned motion + derivatives regressors → `errts.*.tproject` in percent-signal
units. Then `3dReHo -nneigh 27` on the *identical* `errts` with

- `bin/3dReHo_prefix` — built from afni/afni commit `4c2bd54`, the commit
  immediately before the fix;
- `bin/3dReHo_postfix` — built from afni/afni master `d202535` (AFNI_26.2.06),
  bit-identical on synthetic data to AFNI's own precompiled Sep 1 2026 build.

The only difference between arms is PR #944. `scripts/group_analysis.sh`:
per-subject summaries and `3dttest++` SCHZ vs CONTROL under each arm.

**Validation subject (sub-10159, CONTROL).**

| quantity | value |
|---|---|
| errts SD in mask (units 3dReHo saw) | 0.43 |
| mean ReHo, pre-fix | 0.223 |
| mean ReHo, post-fix | 0.609 |
| mean relative error (NaN read as 0) | **61 %** (max 96 %) |
| voxels returned as NaN by the pre-fix build | 7.5 % |

The pipeline's bandpassed percent-signal residuals have SD ≈ 0.4 — inside the
bug's worst regime (`../reproductions/reho_tie_sim.py` predicts ~54 % at scale
0.5), so the published design sits near the maximum of the error curve.

## Results (40 subjects: 20 CONTROL + 20 SCHZ)

Everything below is in `results/`: `subjects_summary_v2.tsv` (one row per
subject), the two group-analysis logs, the SCZ-vs-CONTROL t-maps under each
arm as NIfTI, the group masks, and `figure1.png`.

> **Correction (2026-09-02).** The first version of this section, pushed
> earlier the same day, had two errors, both now fixed. (1) The group contrast
> had been run with `3dttest++ -setA SCZ file1 file2 …`, which 3dttest++ parses
> as its *long form* (label/dataset pairs), so only every second file — 10
> subjects per group — entered the test. The script now uses the short form and
> the t-maps and counts below are for 20 vs 20. (2) The per-subject statistics
> had been computed with AFNI tools, which silently read NaN as 0; the pre-fix
> 3dReHo turns out to return NaN in a large fraction of voxels (below), and that
> is now reported explicitly. The qualitative conclusions did not change; most
> numbers did.

### The three builds, and which comparison isolates PR #944

`src/ptaylor/rsfc.c` changed three times in 2026:

| build | source | tie detection | trailing tie run | zero denominator |
|---|---|---|---|---|
| `3dReHo_hist` | `29384a2^` — every AFNI release through 26.2.03 | integer-truncated | never closed | cannot occur |
| `3dReHo_prefix` | `4c2bd54` — master for one day (2026-08-27) | integer-truncated | closed (`29384a2`, authored 2023, merged 2026-08-27) | NaN |
| `3dReHo_preguard` | `4c2bd54` + `74a90ac` | integer-truncated | closed | **W = 0** |
| `3dReHo_postfix` | `d202535` = AFNI 26.2.06 | float (`94ee52b`, **PR #944**) | closed | W = 0 (`74a90ac`) |

The comparison that isolates PR #944 alone is **`3dReHo_preguard` vs `3dReHo_postfix`**:
same tail handling, same divide-by-zero guard, the only difference being whether ties
are detected on truncated integers or on the floats. On the synthetic volumes
(`scripts/synth_arm_check.py`) `3dReHo_preguard` is identical, to the last bit, to
`3dReHo_prefix` with NaN replaced by 0 — which is also exactly how every AFNI program
reads a NaN. **The results below are therefore that comparison**: "pre-fix (NaN as 0)"
= `3dReHo_preguard` = arm A, "post-fix" = arm B, and the per-subject table for it is
`results/subjects_summary_AB.tsv`.

What the published papers ran is `3dReHo_hist` (no release before 26.2.04 closes the
trailing run). In that build a series lying inside one integer bin gets no tie
correction and comes out exactly right, so the error curve is non-monotonic and there
are no zeroed voxels; on band-passed synthetic input it returns 0.77 of the correct
value at SD 0.35 and 0.38 at SD 0.5 (`../reproductions/README.md`). A `hist` vs
`postfix` pass on the same 40 subjects was started and stopped after three subjects;
`scripts/run_subject.sh` now runs all four builds so it can be resumed.

**Exclusions.** 52 subjects were attempted to reach 20 per group. Twelve
failed the pipeline's own regression step because motion/outlier censoring
(0.3 mm / 5 % outliers) left fewer time points than the 108 nuisance
regressors — 4 of 24 CONTROL and 8 of 28 SCHZ attempted
(`results/excluded_subjects.txt`). That is a property of a 148-TR run with
bandpass regressors, not of either 3dReHo build; it is noted because it makes
the SCHZ group the more-censored one, which matters below.

### Who the 40 are

`results/demographics_qc.tsv` (age and sex from `participants.tsv`; motion = mean
Euclidean norm of the frame-to-frame motion derivative from `motion_*_enorm.1D`):

| | CONTROL (n = 20) | SCHZ (n = 20) | p |
|---|---|---|---|
| age, years (range) | 32.4 ± 8.6 (21–49) | 36.0 ± 9.7 (22–49) | 0.21 |
| sex F / M | 8 / 12 | 6 / 14 | 0.74 (Fisher) |
| motion, all volumes (mm) | 0.103 ± 0.036 | 0.123 ± 0.045 | 0.11 |
| motion, retained volumes | 0.093 ± 0.028 | 0.105 ± 0.034 | 0.24 |
| volumes censored | 5.0 % | 8.8 % | 0.10 |

No significant group difference, but SCHZ moves more and loses more volumes, which
is what makes the amplitude-dependent bias below group-dependent.

### Per subject (arm A vs B): a sixth of the brain zeroed, a third of the correct value elsewhere

| quantity (mean over 40 subjects, range) | value |
|---|---|
| errts SD in mask (the units 3dReHo saw) | 0.35 (0.14 – 0.52) |
| **voxels where arm A returns 0** (NaN before the guard commit) | **17 %** (2 % – 69 %) |
| in the remaining voxels: A/B ratio | 0.31 (0.24 – 0.40) |
| in the remaining voxels: relative error | **70 %** (60 % – 76 %) |
| relative error over all voxels (zeros count as 100 %) | 75 % (61 % – 92 %) |
| spatial correlation of A and B maps | **0.60** (0.31 – 0.76) |

The pre-fix tie correction can zero its own denominator; when it does, the
voxel is NaN. Every AFNI program that reads such a map converts NaN to 0
silently (verified: `3dTcat` of three pre-fix maps holding 18,995 NaNs writes
none; `3dttest++` output reproduces, to the last digit, a t-test in which
those voxels are 0). So in a published AFNI pipeline the pre-fix ReHo map was
0 in one voxel in six on average, and one third of the correct value in the
rest. The maps are only moderately correlated with the correct ones
(r = 0.60): the bug reorders voxels, it does not merely rescale them.

Both effects track each subject's residual amplitude, exactly as the
tie-frequency mechanism predicts (`../reproductions/reho_tie_sim.py`): the
NaN fraction correlates r = −0.88 with errts SD across subjects (the two
most-censored SCHZ subjects, SD 0.14 and 0.18, are 69 % and 58 % NaN), and map
fidelity correlates r = +0.68. Because residual SD and censoring differ between
the clinical groups (SCHZ residual SD 0.334 ± 0.082 vs CONTROL 0.370 ± 0.057;
NaN fraction 20 % vs 14 %; censoring 8.8 % vs 5.0 %), the pre-fix bias is
group-dependent, i.e. it is not guaranteed to cancel in a between-group
contrast.

### Group contrast: SCZ vs CONTROL under each binary

`3dttest++`, two-sample, 20 vs 20, same subjects, same mask, the *only*
difference being which 3dReHo produced the input maps (pre-fix NaNs enter as
0, as they would in any AFNI pipeline).

| | intersection mask (8,657 vox) | 90 %-coverage mask (25,227 vox) |
|---|---|---|
| voxels \|t\| > 3.57 (p < .001), pre-fix / post-fix | 0 / 12 | 49 / 57 |
| overlap of those sets (pre ∩ post / pre ∪ post) | 0 / 12 | 2 / 104 |
| voxels \|t\| > 1.96 (p < .05), pre-fix / post-fix | 767 / 920 | 2,849 / 4,470 |
| overlap of the p < .05 sets (Jaccard) | 324 / 1,363 (0.24) | 1,632 / 5,687 (0.29) |
| spatial correlation of t-maps, pre vs post | 0.66 | 0.68 |
| voxels where t changes sign | 21 % | 18 % |
| mean \|t_pre − t_post\| | 0.66 | 0.69 |

The two t-maps share less than half their variance; the sign of the group
difference flips in about one voxel in five; **the p < .001 sets have
essentially no overlap** (0 of 12; 2 of 104), and even the liberal p < .05
sets agree on only a quarter of their union.

**Cluster-level inference.** To mirror a published design, `3dttest++ -Clustsim`
(sign-flip randomisation, 10,000 iterations, NN1, bi-sided) gave cluster-size
thresholds at α = 0.05 for cluster-forming p = 0.001 and 0.01 under each build and
mask, and `3dClusterize` extracted survivors (`results/cluster_inference/`). **No
cluster survives under either build** at n = 20 + 20: in the 90 %-coverage mask the
largest p < .001 clusters are 21 (before) and 20 (after) voxels against thresholds of
24, and the largest p < .01 clusters 114 and 138 against 151 and 179. The pilot is
underpowered for a corrected whole-brain finding in either arm, so the fix's effect
here is on the content of the maps, not on whether a corrected result exists; the
uncorrected comparisons above are the appropriate description of that effect.

Whole-brain mean ReHo, the simplest ReHo statistic papers report:

| SCZ − CONTROL, global mean ReHo | pre-fix (NaN as 0) | pre-fix (valid voxels only) | post-fix |
|---|---|---|---|
| difference | −0.024 | −0.020 | −0.038 |
| Student t (df 38) | −1.74, p = 0.090 | −1.84, p = 0.074 | −2.25, p = 0.031 |
| Cohen's d | | −0.58 | −0.71 |

Same subjects, same residuals: the global SCZ < CONTROL reduction in ReHo is
significant with the fixed code and not with the code every paper ran. This
is a 40-subject pilot, so the crossing of p = 0.05 is illustrative rather than
a claim about schizophrenia; the robust findings are the NaN fraction, the
per-subject error sizes, and the poor overlap of the significant voxel sets.

### Enlarged sample: 40 CONTROL + 33 SCHZ

After the pilot the batch was extended (`scripts/run_ext.sh`; everything under
`results/enlarged_sample/`) to every remaining ds000030 SCHZ participant with a
resting run and a T1w, and to a further 20 controls. Of the 22 SCHZ candidates, 13
passed, 8 failed censoring (fewer retained volumes than regressors) and one,
sub-50085, was deferred after the container rebooted twice while it was being
processed. Of the 29 spare controls, 3 have no T1w on the OpenNeuro bucket, 3
failed censoring, 3 were not needed, and the first 20 that passed were kept. The
enlarged sample is 73 (df 71); `results/enlarged_sample/subjects_summary_ext.tsv`
has every per-subject value, and the "original 40" rows of that script reproduce
the pilot tables above exactly.

| | CONTROL (n = 40) | SCHZ (n = 33) | p |
|---|---|---|---|
| age, years (range) | 29.4 ± 7.9 (21–49) | 35.9 ± 9.2 (22–49) | 0.002 |
| sex F / M | 18 / 22 | 8 / 25 | 0.087 (Fisher) |
| motion, all volumes (mm) | 0.094 ± 0.036 | 0.125 ± 0.040 | 0.001 |
| motion, retained volumes | 0.086 ± 0.029 | 0.107 ± 0.030 | 0.004 |
| volumes censored | 4.5 % | 9.6 % | 0.002 |
| residual SD handed to 3dReHo | 0.374 ± 0.051 | 0.319 ± 0.076 | < 0.001 |

The groups now differ in age, motion, censoring and, most relevantly, residual
amplitude: the extension SCHZ participants are older and move more than the
pilot's. No covariate is used, as in the pilot; the comparison of interest is
still between builds on identical inputs, and the amplitude difference is the
mechanism by which the pre-fix error becomes group-dependent.

**Per subject.** The pre-fix build returns NaN in 17.9 % of in-mask voxels on
average (range 1.8–69.3 %), more in SCHZ (23.1 ± 15.6 %) than in CONTROL
(13.6 ± 7.5 %; p = 0.001); over the valid voxels it returns 0.30 of the correct
value with a relative error of 0.70; the two maps correlate 0.58 per subject
(SCHZ 0.55, CONTROL 0.61; p = 0.003).

**Group contrast, uncorrected** (`3dttest++`, 33 vs 40, same subjects, same mask):

| | intersection mask (6,488 vox) | 90 %-coverage mask (24,403 vox) |
|---|---|---|
| voxels \|t\| > 3.43 (p < .001), pre-fix / post-fix | 83 / 28 | 215 / 93 |
| overlap of those sets (pre ∩ post / pre ∪ post) | 7 / 104 | 15 / 293 |
| voxels \|t\| > 1.96 (p < .05), pre-fix / post-fix | 1,621 / 1,622 | 6,016 / 5,112 |
| overlap of the p < .05 sets (Jaccard) | 928 / 2,315 (0.40) | 2,807 / 8,321 (0.34) |
| spatial correlation of t-maps, pre vs post | 0.64 | 0.63 |
| voxels where t changes sign | 11 % | 12 % |

**Cluster-level inference** (`3dttest++ -Clustsim`, 10,000 sign-flip randomisations,
NN1, bi-sided, α = 0.05; `results/enlarged_sample/cluster_inference/`). With 73
participants a published design now finds corrected clusters under both builds,
all SCHZ < CONTROL, **but not the same ones**:

| mask | cluster-forming p | build | size threshold | surviving clusters (voxels; peak label) | shared voxels, pre ∩ post / pre ∪ post |
|---|---|---|---|---|---|
| 90 %-coverage | 0.001 | pre-fix | 24 | 3 (91): precuneus 38, right fusiform / cerebellum VI 28, precuneus / mid-cingulate 25 | 0 / 120 |
| | | post-fix | 24 | 1 (29): right middle temporal gyrus | |
| | 0.01 | pre-fix | 145 | 3 (1,289): precuneus 793, SMA 295, right lingual / cerebellum 201 | 102 / 1,719 |
| | | post-fix | 172 | 2 (532): cerebellar vermis VI 274, right middle temporal gyrus 258 | |
| intersection | 0.001 | pre-fix | 14 | 3 (61): vermis III / lingual 21, posterior cingulate 20, precuneus 20 | 0 / 61 |
| | | post-fix | 14 | 0 (largest 11) | |
| | 0.01 | pre-fix | 79 | 3 (524): posterior cingulate 245, precuneus 150, vermis / lingual 129 | 146 / 610 |
| | | post-fix | 72 | 2 (232): posterior cingulate 151, precuneus 81 | |

Labels are the CA_ML_18_MNI (Macro Labels) atlas at the peak (MNI 2009c space).
At the conventional p < .001 forming threshold the two builds' corrected results
share **no voxel** in either mask: the code every paper ran reports reduced ReHo in
schizophrenia in precuneus, posterior cingulate and fusiform cortex; the fixed code
reports it in right middle temporal gyrus, or nothing. At p < .01 the midline
posterior-cingulate / precuneus cluster is found by both builds (146 of 610 voxels
shared in the intersection mask), while the SMA and right-lingual clusters exist
only before the fix and the vermis cluster only after it.

**Global mean ReHo** with 73:

| SCZ − CONTROL, global mean ReHo | pre-fix (NaN as 0) | pre-fix (valid voxels only) | post-fix |
|---|---|---|---|
| difference | −0.031 | −0.022 | −0.040 |
| Student t (df 71) | −3.46, p = 0.001 | −3.13, p = 0.003 | −3.60, p = 0.001 |
| Cohen's d | −0.81 | −0.74 | −0.85 |

The global reduction is now significant under every reading, so the pilot's
p = 0.05 crossing was a matter of sample size rather than of build; the effect
size is a fifth larger with the fixed code. What the enlarged sample adds is
the cluster-level result: at the sample size and thresholds the exposed studies
use, the before- and after-fix pipelines each produce a publishable corrected
finding, and the findings are anatomically different.

### Reading this fairly

- This is the *published design* (afni_proc.py with the default `scale`
  block → 3dReHo → group t-test), not any paper's own data; none of the five
  exposed papers shares its data. The magnitude of the effect on their
  numbers will depend on their residual scale and sample size, but all three
  that used this pipeline sit in the same errts-SD regime as this dataset.
- Both arms are AFNI's own code; the post-fix binary is bit-identical to
  AFNI's shipped AFNI_26.2.06 build on test data. Nothing in the pipeline
  before 3dReHo differs between arms.
- The exclusion rate (12/52) is high because the run is short (148 TRs) and
  the bandpass adds ~80 regressors; it is the same for both arms.
- The exposure criterion in `../README.md` (errts SD roughly 0.4–3) was
  conservative: these subjects sit mostly *below* 0.4 and are the worst hit.
  Some of the 52 papers cleared there may deserve a second look.

### Reproducing

`subjects.tsv` + `subjects_spare.tsv` list every subject attempted;
`scripts/run_subject.sh` processes one subject end to end from the OpenNeuro
S3 bucket (no credentials needed, ~9 min/subject on 4 cores);
`scripts/supervisor.sh` runs the batch and top-up;
`scripts/group_analysis.sh` produces the group maps and logs;
`scripts/subject_stats_v2.py` the per-subject table (nibabel, NaN-aware);
`scripts/cluster_inference.sh` + `scripts/cluster_extract.sh` the cluster-level inference;
`scripts/run_ext.sh` (+ `janitor_ext.sh`, `janitor2_ext.sh`, `stop_all.sh`) the extension
batch, `scripts/group_analysis_ext.sh` its group maps and cluster inference, and
`scripts/subject_stats_ext.py` its demographics and per-subject table;
`scripts/make_figure1.py` the summary figure `results/figure1.png` (panel A: one
subject's before/after maps; B: per-subject map fidelity vs residual SD; C: the
SCZ-vs-CONTROL t-maps under each build); `scripts/make_mechanism_figure.py` the
error-vs-input-scale figure `results/mechanism.png` (simulation curves from
`../reproductions/reho_tie_sim.py` with the 40 subjects overlaid).
The two 3dReHo builds come from `afni/afni` at `4c2bd54` and `d202535` via
`make ptaylor_all`.