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
| mean relative error | **61 %** (max 96 %) |

The pipeline's bandpassed percent-signal residuals have SD ≈ 0.4 — inside the
bug's worst regime (`../reproductions/reho_tie_sim.py` predicts ~54 % at scale
0.5), so the published design sits near the maximum of the error curve.

## Results (40 subjects: 20 CONTROL + 20 SCHZ)

Everything below is in `results/`: `subjects_summary.tsv` (one row per
subject), the two group-analysis logs, the SCZ-vs-CONTROL t-maps under each
arm as NIfTI, and the group masks.

**Exclusions.** 52 subjects were attempted to reach 20 per group. Twelve
failed the pipeline's own regression step because motion/outlier censoring
(0.3 mm / 5 % outliers) left fewer time points than the 108 nuisance
regressors — 4 of 24 CONTROL and 8 of 28 SCHZ attempted
(`results/excluded_subjects.txt`). That is a property of a 148-TR run with
bandpass regressors, not of either 3dReHo build; it is noted because it makes
the SCHZ group the more-censored one, which matters below.

### Per subject: the pre-fix bug is large, and it is not a constant factor

| quantity (mean over 40 subjects, range) | value |
|---|---|
| errts SD in mask (the units 3dReHo saw) | 0.35 (0.14 – 0.52) |
| mean ReHo, pre-fix | 0.158 |
| mean ReHo, post-fix | 0.481 |
| pre/post ratio | 0.33 (0.26 – 0.42) |
| mean relative error, pre vs post | **57 %** (23 % – 65 %) |
| spatial correlation of pre-fix and post-fix ReHo maps | **0.60** (0.31 – 0.76) |

Every subject's pre-fix ReHo map is roughly one third of the correct value,
and the maps are only moderately correlated with the correct ones (r = 0.60):
the bug does not merely rescale ReHo, it reorders voxels. The size of the error
tracks each subject's residual amplitude — correlation of relative error with
errts SD across subjects is r = 0.78, and of the spatial correlation with errts
SD r = 0.68 — exactly as the tie-frequency mechanism predicts
(`../reproductions/reho_tie_sim.py`). Subjects with small residual SD (the two
most-censored SCHZ subjects, SD 0.14 and 0.18) have the *smallest* relative
error (23 %, 31 %) but the *lowest* map fidelity (r = 0.35, 0.31).

Because the error depends on a quantity that differs between clinical groups
(SCHZ residual SD 0.334 ± 0.082 vs CONTROL 0.370 ± 0.057; SCHZ mean censoring
8.8 % vs 5.0 %), the pre-fix bias is group-dependent, i.e. it is not
guaranteed to cancel in a between-group contrast.

### Group contrast: SCZ vs CONTROL under each binary

`3dttest++`, two-sample, same subjects, same mask, the *only* difference being
which 3dReHo produced the input maps.

| | intersection mask (8,657 vox) | 90 %-coverage mask (25,227 vox) |
|---|---|---|
| voxels \|t\| > 3.57 (p < .001), pre-fix | 12 | 25 |
| voxels \|t\| > 3.57 (p < .001), post-fix | 33 | 82 |
| overlap of those sets (pre ∩ post / pre ∪ post) | 1 / 44 | 1 / 106 |
| voxels \|t\| > 1.96 (p < .05), pre / post | 726 / 1,097 | 2,848 / 3,415 |
| spatial correlation of t-maps, pre vs post | 0.66 | 0.68 |
| voxels where t changes sign | 19 % | 19 % |
| mean \|t_pre − t_post\| | 0.66 | 0.65 |

The two t-maps share only two thirds of their variance; the sign of the group
difference flips in about one voxel in five; and **the p < .001 maps have
essentially no overlap** — one voxel in common out of 44 (106) that pass in
either arm. Under the fixed binary the contrast has roughly 2.5–3× as many
suprathreshold voxels, consistent with the pre-fix maps being noisier
(lower fidelity) rather than merely rescaled.

Whole-brain mean ReHo, the simplest ReHo statistic papers report:

| SCZ − CONTROL, global mean ReHo | pre-fix | post-fix |
|---|---|---|
| difference | −0.020 | −0.038 |
| Student t (df 38) | −1.84, p = 0.074 | −2.25, p = 0.031 |
| Cohen's d | −0.58 | −0.71 |

Same subjects, same residuals: the global SCZ < CONTROL reduction in ReHo is
significant with the fixed code and not with the code every paper ran. This
is a 40-subject pilot, so the crossing of p = 0.05 is illustrative rather than
a claim about schizophrenia; the robust findings are the per-subject error
sizes and the poor overlap of the significant voxel sets.

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

### Reproducing

`subjects.tsv` + `subjects_spare.tsv` list every subject attempted;
`scripts/run_subject.sh` processes one subject end to end from the OpenNeuro
S3 bucket (no credentials needed, ~9 min/subject on 4 cores);
`scripts/supervisor.sh` runs the batch and top-up;
`scripts/group_analysis.sh` produces everything in `results/`. The two 3dReHo
builds come from `afni/afni` at `4c2bd54` and `d202535` via
`make ptaylor_all`.
