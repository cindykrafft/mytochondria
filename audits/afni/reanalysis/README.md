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
Phenomics), resting-state fMRI, 3 T. Pilot: 20 CONTROL + 20 SCHZ
(`subjects.tsv`; first 20 eligible of each with rest + T1w and no ghosting flag).

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

*(Batch results and the group contrast follow in this directory when the run
completes.)*
