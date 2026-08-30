# FreeSurfer bug analysis against 116 published papers (2021–2026)

_Follow-up to the six-journal software survey (`../README.md`). Generated 2026-08-30._

## What this is

The survey found **116 papers** in *Nature*, *Science*, PNAS and *Cell* (2021–2026) that used
FreeSurfer. Each paper's full text was re-mined to determine **which parts of FreeSurfer it
used** (commands, pipeline features, versions), and the corresponding FreeSurfer source
components were then read adversarially for bugs that could change published numbers — not
crashes. Source: `freesurfer/freesurfer` dev branch, with tags v6.0.0, v7.1.1, v7.4.1 read
via git for version comparisons; FreeSurfer's own release notes were used for documented bugs.

**Epistemic status, stated plainly.** These are *code-level* findings: every CONFIRMED item
was traced end-to-end in the source (one was additionally reproduced in a compiled test), but
none has been reproduced against imaging data as part of this analysis, and per-paper
magnitudes are estimates from the code, not measurements. "Paper is exposed" means the paper
used the affected feature/version — not that its conclusions are wrong. Most of these biases
are *systematic and shared across subjects*, which is exactly why they mostly attenuate or
shift measurements without reversing well-powered group contrasts; the dangerous ones are
those that touch inference (B1–B3) or interact with the variable under study (B6, B15).

## How the papers use FreeSurfer

| Usage (from paper full texts) | Papers |
|---|---|
| ROI morphometry via aparc parcellation (thickness/area/volume) | 85 |
| Surface reconstruction explicitly described | 53 |
| Registration / surface sampling (bbregister, vol2surf, fsaverage) | 36 |
| Subcortical volumes (aseg) | 16 |
| Group GLM with cluster correction (mri_glmfit / -sim) | 12 |
| Hippocampal subfields | 8 |

Versions named: 6.0.x (17 papers), 7.x (13), ≤5.x (15), unstated (72 — the norm, unfortunately).

## Findings, ranked by (severity × exposure)

Confidence: **CONFIRMED** = the full code path was traced and quoted (file:line in the
component reviews); **PLAUSIBLE** = mechanism verified, exposure or magnitude uncertain.

### Tier 1 — affects statistical inference

**B1. Volume-based cluster correction is anticonservative in every release ≤7.4: the null
distribution uses 6-connectivity while observed clusters use 26-connectivity.** CONFIRMED.
`mri_glmfit --sim` builds the max-cluster null with face-only connectivity
(`clustGetClusters`, allowdiag hardcoded 0), but the `mri_glmfit-sim` script clusters the
real data with `--allowdiag`. Observed clusters can only be ≥ their 6-connected size, so
cluster p-values are biased downward — most at low cluster-forming thresholds. Fixed only on
the dev branch, whose code comments acknowledge the mismatch. **Surface-based correction is
not affected.** Exposure: the 12 group-GLM papers *if* they ran volume-based correction
(discriminator to check per paper).

**B2. Fixed-effects multi-row F-tests inflate significance ~J-fold in all versions.**
CONFIRMED. `GLMtestFFx` hands the Wald statistic to an F(J, dof) tail without dividing by J
(the random-effects path divides correctly). A J=2 contrast with true p≈0.05 is reported as
p≈0.0025. Scope is narrow: only `--yffxvar/--ffxdof` fixed-effects analyses with multi-row
contrasts — but for any paper that did this, the reported F-test p-values are wrong outright.

**B3. Simulation p-values use the `nover/nreps` strict-`>` convention rather than the exact
`(b+1)/(m+1)`.** CONFIRMED, small (≲1/nsim additively, anticonservative; the code's own
comment says "Using just > is too liberal"). Matters only for borderline clusters at
nsim≈1000. The exact convention exists but only behind an env var since 7.2.

### Tier 2 — systematic measurement bias present in ALL versions

**B6. Per-ROI thickness means include frozen zero-thickness vertices.** CONFIRMED
(independently by two reviewers). `mris_anatomical_stats` filters ROI thickness only by
annotation label, not by `cortex.label` — vertices labeled e.g. entorhinal but outside the
cortex label carry thickness exactly 0 and are averaged in, while the same row's GrayVol
excludes them and the global mean-thickness measure excludes them. Result: ThickAvg biased
down and ThickStd up in medial-wall-adjacent ROIs (entorhinal, parahippocampal, cingulate,
insula, medial-orbitofrontal); the aparc↔cortex.label mismatch varies with atrophy, so this
can masquerade as a group effect in aging/AD studies of exactly those regions. Exposure: all
32 papers reporting ROI cortical thickness; the danger concentrates in medial-temporal ROIs.

**B15. A hidden 1 mm "look-ahead" in boundary acceptance rejects the true boundary in
cortex thinner than ~1 mm and sulci tighter than ~1 mm.** PLAUSIBLE (mechanism confirmed;
magnitude needs data). White gets pulled outward in the thinnest cortex (attenuating atrophy
effects at the thin end); pial drifts outward in deep sulci. Identical in all versions, so it
biases absolute values, not version comparisons.

**B11. Small parcellation islands are absorbed by adjacency order, not likelihood.**
CONFIRMED. `GCSArelabelIslands` truncates double log-likelihoods to `int` before comparing;
ties (common at ambiguous boundaries) go to the first neighbor in the vertex adjacency list.
Deterministic per mesh, systematic across subjects; biases area/thickness of small ROIs.
Exposure: all 85 aparc papers, weight on small ROIs (bankssts, transversetemporal…).

**B13. The annotation mode filter can never assign "unknown": a one-way ratchet expands
medial-wall-adjacent ROIs during smoothing.** Mechanism CONFIRMED (bug vs. intent debatable).

**B16. Ill-conditioned curvature fallback halves principal curvatures and can flip the
folding-index sign at sulcal fundi.** CONFIRMED, small; affects MeanCurv/GausCurv/FoldInd
columns only.

### Tier 3 — version-dependent shifts (dangerous when versions are mixed or compared)

**B9. v5.3/v6.0 global "brain volume" measures are wrong on non-1mm data.** CONFIRMED (and
documented by FreeSurfer as the BrainVolStatsFixed issue — but its full mechanism is worse
than the release note: voxel *counts* mixed with surface mm³, plus an `int` voxel-size
truncation that zeroes a correction term at 0.8 mm, inflating BrainSegVol-family measures
≈1.95× at 0.8 mm). Per-structure rows (hippocampus etc.) are fine in every version; the
damage is in header measures — which are widely used as **normalization covariates**, so ROI/
ICV-adjusted values inherit the error. Exposure: 6 papers combine a 5.x/6.x version with
submillimeter acquisition; eTIV itself is clean (identical formula v6→dev).

**B10. aseg header measures silently changed definition v6→v7** (SupraTentorialVolNotVent
−4–6 cm³, CerebralWhiteMatterVol now includes WM-hypointensities, CortexVol dropped a
correction, BrainSegVol excludes more labels). CONFIRMED. Additionally v7's cache-miss
fallback recomputes them with the *old* formula, so one binary can yield two value sets
depending on whether `stats/brainvol.stats` exists; and a latent v7 bug double-counts
thalamus in that fallback path. Any longitudinal or multi-site study mixing FS6/FS7 gets
0.1–2% step changes in these measures.

**B14. v7 computes thickness on de-ripped surfaces: pinned medial-wall pial vertices (pial =
white) become closest-vertex candidates up to 20 hops away, thinning the cortex band around
the medial wall relative to v6.** CONFIRMED (developers' comment concedes the difference).
Related version shifts: v5.3→v6 pial threshold deliberately moved outward ("push pial
surfaces further out", 12/2015) so v6+ reads systematically thicker than v5.3; sub-mm data
had a first-WM-peak relocation auto-ON in v6 (gated by a genuinely uninitialized variable)
and OFF in v7. Papers comparing against older normative data, or mixing versions, inherit
these offsets. The thickness *metric* itself is byte-identical v6→dev and correctly
symmetrized — the shifts come from surface placement, not the metric.

**B12. `mri_aparc2aseg` has a winner-selection fall-through: a voxel whose four surface
candidates are all rejected inherits the previous voxel's ROI — and possibly hemisphere —
with an uninitialized-variable read in v7 and an OpenMP read/write race making boundary
voxels nondeterministic run-to-run.** CONFIRMED. Affects aparc+aseg / wmparc volumes at
sulcal-bank boundary voxels.

### Tier 4 — invocation traps (exposure depends on exact command lines, usually unknowable from papers)

**B7.** `mris_anatomical_stats -i <low> <high>` (thickness outlier exclusion) is a silent
no-op in every version — it prints that it filtered, and doesn't. A paper stating this
exclusion published unfiltered numbers. CONFIRMED.
**B8.** `aparcstats2table` silently writes 0.0 for a subject missing an ROI row — a massive
low outlier injected into group tables with no warning at default verbosity. CONFIRMED.
**B4.** `mri_vol2surf --projfrac-avg 0 1 0.1` drops the deepest sample (float accumulation:
samples run 0…0.9), shifting the effective fMRI sampling depth ~0.05×thickness whiteward at
every vertex. CONFIRMED — reproduced in a compiled test; canonical invocations affected.
**B5.** Out-of-FOV depth samples contribute *zeros* to the projfrac average — a silent graded
attenuation band on surface maps at functional FOV edges, which survives into group stats.
CONFIRMED. Exposure for B4/B5: the 24 surface-sampling fMRI papers.

### Documented release-note bugs mapped to the cohort

| Bug (FreeSurfer's own release notes) | Cohort exposure |
|---|---|
| FS-FAST seed waveforms not rescaled (affects regression coefficient amplitude; known issue 7.4.1) | 2 papers doing seed FC via FS-FAST, incl. a Nature 2026 Parkinson's paper |
| Cross-hemisphere registration (xhemi/surfreg) misalignment, fixed 7.3.2 | 9 candidate papers (text matched loosely — each needs a manual read) |
| v7.0.0 recalled outright (conform intensity rescaling) | 1 paper states "FreeSurfer 7.0" |
| aseg.stats global stats wrong on non-1mm voxels (v6.0 known issue) | subsumed by B9 above |
| mris_fix_topology thread-count nondeterminism (7.4.0) | any 7.4 paper; reproducibility, not bias |

## What was checked and found CORRECT

Equally important for trust in the 116 papers:

- **The thickness metric** (Fischl–Dale symmetrized min-distance, 5 mm cap) — correct and
  byte-identical v6→dev.
- **eTIV** — identical formula v6→dev; cross-version comparable.
- **Per-structure aseg volumes** (hippocampus, amygdala, thalamus, ventricles…) — correct
  in all versions including on non-1mm data (only *header* measures are hit by B9).
- **Hippocampal-subfield volumes** — soft-posterior integrals at the true working
  resolution; verified clean (8 papers ride on this and it held up).
- **Core random-effects GLM math**, one/two-tailed bookkeeping, surface cluster-area
  accounting, BH-FDR step-up — correct.
- **tkreg coordinate conventions** close end-to-end (no half-voxel registration bias);
  **bbregister** cost/sign chain correct for T1/T2*/BOLD.
- **annot→ctab→stats-row identity chain** — no ROI scrambling with shipped atlases.
- **GCSA classifier math** (priors/likelihoods) — correct in the well-conditioned path.

## Files

| File | Contents |
|---|---|
| `fs_papers.tsv` | 116 papers × versions × commands × features × exposure groups |
| `fs_paper_exposure.tsv` | per-paper list of applicable findings (join of the two tables) |
| `component-reviews/*.md` | the six full component reviews with file:line evidence |
| `fs_profile.py` | the script that mined FreeSurfer usage from the papers' full texts |

## Suggested next steps

1. **Numerical reproduction** of the highest-value findings on real data: B1 (re-run one
   volume-corrected analysis with matched connectivity), B6 (recompute ROI ThickAvg with a
   cortex-label mask and diff), B4 (count vol2surf samples at each depth).
2. **Report upstream**: B2 (FFx /J), B7 (-i no-op), B12 (fall-through + race), B4 (float
   loop) are crisp, patchable defects; B1 is already fixed on dev but unreleased at 7.4 —
   worth flagging for backport/release-note.
3. For any specific paper in `fs_paper_exposure.tsv`: read its methods against the
   discriminators (volume vs surface correction, version mixing, medial-temporal ROIs,
   `--projfrac-avg` use) before drawing conclusions — exposure ≠ error.
