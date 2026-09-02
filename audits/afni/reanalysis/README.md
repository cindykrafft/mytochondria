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
`scripts/make_figure1.py` the summary figure `results/figure1.png` (panel A: one
subject's before/after maps; B: per-subject map fidelity vs residual SD; C: the
SCZ-vs-CONTROL t-maps under each build); `scripts/make_mechanism_figure.py` the
error-vs-input-scale figure `results/mechanism.png` (simulation curves from
`../reproductions/reho_tie_sim.py` with the 40 subjects overlaid).
The two 3dReHo builds come from `afni/afni` at `4c2bd54` and `d202535` via
`make ptaylor_all`.