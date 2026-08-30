# Numerical reproductions: B1, B4, B6

_Follow-up to `../README.md`. Each finding was code-level CONFIRMED there; this directory
reproduces the three highest-value ones numerically. Generated 2026-08-30._

## Summary of outcomes

| Finding | Outcome | Headline number |
|---|---|---|
| B4 projfrac endpoint drop | **Reproduced** with the verbatim compiled loop | canonical `0 1 0.1` samples depths 0–0.9; effective mean depth 0.45, not 0.5 |
| B1 cluster connectivity mismatch | **Reproduced** by Monte Carlo | achieved FWER 0.19 at nominal 0.05 (CDT z=2.3, FWHM 1.5 vox); 0.096 at FWHM 2.0 |
| B6 ROI thickness zeros | **Reproduced on the exposed path; standard aparc exonerated** | Schaefer→subject: worst parcel −0.247 mm; standard aparc: zero exposure by construction |

One finding got *smaller* through reproduction (B6 for standard aparc — an important
correction), one got a bonus confirmation (B3's p-value convention shows up empirically in
the B1 control condition). Details and caveats below.

---

## B4 — `--projfrac-avg` drops its deepest sample (`b4_loop.c`)

The projection loop from `mri_vol2surf.cpp` (lines 203/207/596–598/635, identical v6.0.0 →
dev) was copied verbatim — same `static float` declarations, same `sscanf("%f")` parsing,
same `for (ProjFrac=Min; ProjFrac <= Max; ProjFrac += Delta)` — and compiled.

| Invocation | Samples taken | Max depth sampled | Effective mean depth | Bias |
|---|---|---|---|---|
| `--projfrac-avg 0 1 0.1` (FreeSurfer's documented example) | 10 | **0.900** | **0.450** | −0.05 × thickness |
| `--projfrac-avg 0.2 0.8 0.1` | 6 of 7 | **0.700** | **0.450** | −0.05 × thickness |
| `--projfrac-avg 0 1 0.05` | 20 | 0.950 | 0.475 | −0.025 × thickness |
| `--projfrac-avg 0.1 0.9 0.1` | 8 | 0.800 | 0.450 | −0.05 × thickness |
| `--projfrac-avg 0 1 0.2` | 6 | 1.000 | 0.500 | none |
| `--projfrac-avg 0 1 0.25` | 5 | 1.000 | 0.500 | none |

Mechanism confirmed exactly as predicted: float accumulation (`0.1f` sums to 1.00000012 > 1)
excludes the endpoint for some deltas and not others — the semantics of the flag depend on
the delta chosen. For any signal varying linearly across cortical depth with white→pial
amplitude A, the reported "average across cortex" is displaced by −0.05·A toward white
matter, identically at every vertex of every subject. The same loop drives
`--projfrac-max` (max over a range missing its top) and `mri_surf2vol --fill-projfrac`.

## B1 — volume cluster correction: 6-connectivity null vs 26-connectivity data (`b1_sim.py`)

`clustGrowOneVoxel` accepts a neighbor iff `|dc|+|dr|+|ds| == 1` when `AllowDiag=0` (the
`mri_glmfit --sim` null path) and any of the 26 neighbors when `AllowDiag=1` (the
`mri_glmfit-sim` real-data path). These are exactly `scipy.ndimage`
`generate_binary_structure(3,1)` and `np.ones((3,3,3))`; the simulation mirrors mc-full on a
one-sided test: Gaussian noise fields (64×64×40), Gaussian-smoothed, standardized; 5,000
fields build the null max-cluster CSD per connectivity, 5,000 further null fields play "the
data"; the shipped v6/v7.1 p convention (`nover/nreps`, strict >) is applied.

Achieved family-wise error at nominal α = 0.05 (SE ≈ 0.003):

| Smoothness | CDT | Shipped (26-data vs 6-null) | Matched 26/26 | Matched 6/6 | p assigned at the true 5% critical size |
|---|---|---|---|---|---|
| FWHM 1.5 vox | z=2.3 | **0.193** | 0.057 | 0.058 | **0.008** |
| FWHM 2.0 vox | z=2.3 | **0.096** | 0.050 | 0.045 | 0.022 |
| FWHM 2.5 vox | z=2.3 | **0.084** | 0.057 | 0.057 | 0.033 |
| FWHM 1.5 vox | z=3.1 | 0.129 | 0.129 | 0.090 | 0.027 |
| FWHM 2.0 vox | z=3.1 | 0.053 | 0.053 | 0.047 | 0.035 |
| FWHM 2.5 vox | z=3.1 | 0.059 | 0.059 | 0.053 | 0.044 |

Read-out:

- **At CDT z=2.3 the mismatch alone doubles to nearly quadruples the false-positive rate**
  (0.084–0.193 vs ~0.05 matched), worst at low smoothness — i.e. minimally smoothed,
  high-resolution fMRI, exactly the modern trend. A cluster sitting at the *true* 5%
  critical size is reported as p = 0.008–0.033.
- At CDT z=3.1 the null and data critical sizes coincide (clusters too small for diagonal
  bridging to matter) and the mismatch contributes nothing.
- **Bonus: the z=3.1 / FWHM 1.5 row empirically confirms B3.** There the *matched* 26/26
  correction is itself inflated to 0.129 — pure p-convention effect: with tiny, heavily
  tied cluster sizes, `nover/nreps` with strict > under-reports p. The code comment "Using
  just > is too liberal" is quantitatively right.

Caveats: synthetic stationary fields on a box (edge attenuation from constant-padded
smoothing affects both pipelines equally); one-sided positive test; FWHM 1.5–2.5 voxels ≈
4.5–7.5 mm at 3 mm EPI. Absolute FWERs on real brain masks will differ; the
shipped-vs-matched contrast is the finding and is insensitive to these choices.

## B6 — ROI thickness means and frozen zero vertices (`b6_thickness.py`, `b6_custom_annot.py`)

Run on **bert**, FreeSurfer's own regression-test subject (from the project's git-annex,
sha256-verified), which ships with a reference `aparc.stats` table produced by the real
`mris_anatomical_stats` binary.

**Step 1 — the reimplementation is exact.** Reproducing the accumulation at
`mris_anatomical_stats.cpp:839–848` (filter on annotation index only) matches the reference
table on all 34 ROIs: NumVert exactly, ThickAvg and ThickStd to ≤ 0.0005 mm.

**Step 2 — standard aparc: zero exposure, and the reason is structural.** On bert, *no*
aparc-labeled vertex lies outside `cortex.label`. This is not luck:
`mris_ca_label -l cortex.label` (standard in recon-all) force-relabels every vertex outside
the cortex label to `unknown` (`relabel_unknowns_with_cortex_label`,
`mris_ca_label.cpp:538–610`), so standard Desikan/Destrieux annotations nest inside the
cortex label by construction. **This downgrades B6's exposure for the standard pipeline
from what the code reading alone suggested** — the ROI loop's missing cortex mask is real
but neutralized upstream.

**Step 3 — the exposed path is custom parcellations, and it reproduces there.** Mapping the
published Schaefer2018-200 fsaverage annotation to bert by nearest-neighbor on the
registration sphere (what `mri_surf2surf --sval-annot` does — no cortex-label constraint
ever runs on this path) and feeding it to the same validated accumulation:

| Parcel (lh) | nvert | outside cortex.label | zero-thickness | shipped mean | cortex-masked mean | bias |
|---|---|---|---|---|---|---|
| Cont_Cing_2 | 359 | 38 | 35 | 2.309 | 2.556 | **−0.247 mm** |
| Cont_Cing_1 | 596 | 36 | 32 | 2.810 | 2.974 | **−0.164 mm** |
| Limbic_OFC_2 | 2505 | 66 | 45 | 2.891 | 2.963 | −0.072 mm |
| Default_PHC_1 | 1412 | 131 | 2 | 2.500 | 2.523 | −0.023 mm |

9 of 100 parcels are biased on this one healthy subject; the worst deficits (−0.16 to
−0.25 mm) exceed typical published group differences in cortical thickness (0.05–0.2 mm)
and land on cingulate/limbic parcels overhanging the medial wall — regions of interest in
exactly the aging/psychiatric literatures that use these parcellations. Temporal-pole
parcels show a small opposite sign (their outside-cortex vertices carry nonzero thickness),
confirming the mechanism rather than a uniform offset.

Single healthy subject; per-subject magnitudes will vary with the annot↔cortex-label
mismatch, which is the atrophy-covariance concern from the main report.

## Reproducing

```
cc -O0 -o b4_loop b4_loop.c && ./b4_loop 0 1 0.1
python3 b1_sim.py > b1_results.json            # needs numpy, scipy; ~30 min
python3 b6_thickness.py                        # needs nibabel + the bert testdata
python3 b6_custom_annot.py                     # + fsaverage lh.sphere.reg + Schaefer annot
```

Data: `mris_anatomical_stats/testdata.tar.gz` (bert) and `fsaverage.tar.gz` from the
FreeSurfer git-annex at
`https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/repo/annex.git/annex/objects/<hashDirLower>/<key>/<key>`
(sha256 embedded in the key; both verified); Schaefer2018 annotation from the CBIG
repository.
