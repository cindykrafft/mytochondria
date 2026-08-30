# Pull request bodies

One section per pushed branch. Open the PR from the compare URL in
README.md, paste the matching title and body. All branches are single
commits off current dev (f991feb).

---

## PR 1 — `fix/fsglm-ffx-fstat`

**Title:** fsglm: divide FFx multi-row contrast statistic by J before the F CDF

`GLMtestFFx` computes `gamma' * inv(gCVM) * gamma` and hands it directly to
`sc_cdf_fdist_Q(., J, ffxdof)`. That quantity is a Wald statistic,
distributed as `J * F(J, dof)` under the null, so multi-row (F) contrasts in
fixed-effects analyses report p-values inflated roughly J-fold: with J=2, a
contrast at true p=0.05 is reported as p=0.0025. Single-row contrasts are
unaffected, and the random-effects path (`GLMtest`) already folds J into its
denominator (`dtmp = rvar * C[n]->rows`, fsglm.cpp:611-621).

This one-line change divides the Wald statistic by `C[n]->rows`.

Validation: Monte Carlo calibration (200,000 null draws; 3-group design,
J=2 equality contrast, heteroscedastic known variances as in the FFx
model): null rejection at alpha=0.05 is **0.224** before this change and
**0.050** after. The same code (no /J) is present in v6.0.0
(`utils/fsglm.c`), v7.1.1, v7.4.1 and dev.

Caveat: validated on extracted logic; I could not build the full tree in
the authoring environment (no ITK), so please compile before merging.

---

## PR 2 — `fix/vol2surf-projfrac-endpoint`

**Title:** mri_vol2surf, mri_surf2vol: do not drop the final projection sample

The projection loops accumulate a float (`ProjFrac += ProjFracDelta`) and
test `<= ProjFracMax`. Accumulated rounding error pushes the final value
above the max by ~1e-7 for many (min,max,delta) triplets, silently dropping
the deepest sample:

| invocation | samples taken | max depth | effective mean depth |
|---|---|---|---|
| `--projfrac-avg 0 1 0.1` (the documented example) | 10 | 0.9 | 0.45 |
| `--projfrac-avg 0.2 0.8 0.1` | 6 of 7 | 0.7 | 0.45 |
| `--projfrac-avg 0 1 0.2` | all | 1.0 | 0.50 (unaffected) |

So the sampling profile is displaced toward the white surface by
0.05 x thickness at every vertex, and whether that happens depends on the
delta chosen (0.2/0.25 are exact in binary and exempt). The same pattern in
`mri_surf2vol --fill-projfrac` skips the outermost (pial-most) fill pass
with the default 0 1 0.05 range. `--projfrac-max` averages/maxes over the
same truncated range.

The fix steps with an integer index (`nprojmax = round((max-min)/delta)+1`)
and derives each ProjFrac by multiplication. The averaging divisor (nproj)
continues to match the samples taken, so unaffected invocations produce
byte-identical output.

Validation: both loops (before/after) extracted into a standalone compiled
harness; previously `0 1 0.1` -> 10 samples ending at 0.9; now 11 samples
ending at 1.0, mean depth exactly 0.5, for every range tested. Full-tree
compilation not run in the authoring environment (no ITK).

Note this intentionally changes numerical output for the affected deltas -
that is the bug being fixed - so a regression-test reference update will be
needed for any test pinned to the truncated sampling.

---

## PR 3 — `fix/gcsa-island-loglikelihood`

**Title:** gcsa: compare island-relabeling log-likelihoods as doubles

`GCSAreclassifyLabel` (the island-absorption step run by every
`mris_ca_label` postprocess) stores the return of
`gcsaNbhdGibbsLogLikelihood` - a double - in an `int` before comparing
candidate labels. Adjacent labels' log-likelihoods typically differ by well
under 1.0 exactly where relabeling matters, so the truncation destroys the
comparison and islands are absorbed into whichever neighboring label comes
first in the vertex adjacency list rather than the maximum-likelihood one.
Deterministic per mesh, arbitrary across subjects; falls hardest on small
parcels (bankssts, transversetemporal) whose islands are most frequent.

The sibling `GCSAreclassifyMarked` already declares `double ll, max_ll`
(gcsa.cpp:1303); this change aligns `GCSAreclassifyLabel` with it. Present
in v6.0.0, v7.1.1, v7.4.1 and dev.

Expect small parcellation differences on regression subjects wherever an
island tie previously resolved by adjacency order - those diffs are the fix
working.

---

## PR 4 — `fix/anatomical-stats-thickness-range`

**Title:** mris_anatomical_stats: make the -i thickness range actually filter

`-i <low> <high>` parses its arguments and prints "only considering
thicknesses in the range [low,high]" but never applies the filter: its
intended consumer, `MRIScomputeCurvatureStats`, is declared, defined and
never called (checked in v6.0.0, v7.1.1 and dev). A study passing -i for
outlier exclusion got unfiltered ThickAvg/ThickStd while the program stated
otherwise.

This change applies the range in the per-ROI thickness accumulation, the
per-ROI variance pass, and the -cortex MeanThickness measure, with separate
counters so NumVert/SurfArea keep reporting full vertex counts. With the
default range (0, 20) every vertex passes and output is byte-identical, so
only -i users see a change - the documented one.

An alternative, if the option is considered abandoned, is to remove -i and
error out when passed; either resolves the silent no-op. Happy to rework in
that direction if preferred.

---

## PR 5 — `fix/aparc2aseg-stale-state`

**Title:** mri_aparc2aseg: reset winner-selection state for every voxel

`annot`, `annotid`, `hemi` and `dmin` are declared once per column, and the
four closest-surface winner blocks use strict comparisons. A voxel whose
candidates are all rejected (all four distances forced to 1e15 by the
sulcal-bank dot checks, or a hemisphere disabled) executes no winner block
and silently inherits the previous voxel's annotation, hemisphere and
distance - an unrelated ROI, possibly a ctx-lh label on an rh voxel -
depending only on scan order. At the first such voxel of a column,
`annotid` is read uninitialized. These are exactly the ambiguous
sulcal-bank voxels the dot checks target.

The change initializes the four variables at the top of each voxel
iteration; a no-winner voxel then flows into the existing "annotation is
none -> unknown" handling (annotid = -1) instead of copying stale state.
Voxels with a legitimate winner are unaffected (the winning block
overwrites all four variables).

A related but separate problem - the `MRIneighbors(ASeg, ...)` gating reads
the segmentation the same parallel loop is rewriting in place (scan-order
dependence + OpenMP race) - is deliberately NOT addressed here; it needs a
two-pass/snapshot restructure and is filed as its own issue.

---

_All five branches: authored with the audit documented in
`doc/software-survey/freesurfer-analysis/` of the companion repo; each
commit message carries the full analysis._

---
_Generated by [Claude Code](https://claude.ai/code)_
