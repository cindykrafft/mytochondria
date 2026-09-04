# SPM bug analysis — full-codebase audit

_Companion to `../freesurfer/` and `../fsl/`. Generated 2026-09-01._

## What this is

Unlike the FreeSurfer and FSL entries, this project was **not driven by the six-journal
survey**: instead of starting from papers and reviewing the components they used, the
whole of SPM (`spm/spm` development version, commit `530ec52`, 2026-08-23) was divided
into eleven subsystems and each was read adversarially in full — statistical
distributions, random field theory and results, the GLM estimation core, spatial
preprocessing, image/file I/O, the C/MEX sources, DCM/Bayesian inversion, numeric and
mesh utilities, M/EEG processing, the spatial toolboxes (FieldMap, DARTEL/Shoot,
Longitudinal, OldNorm/OldSeg, Spatial), and the active-inference/MDP code. Suspect math
was transcribed to Python and checked against NumPy/SciPy or closed forms before being
reported. Literature exposure was assessed *afterwards*, for the top findings only —
so there is no `spm_papers.tsv`/exposure join here; per-paper exposure tables in the
style of the other two audits remain future work.

**Headline count: 83 confirmed defects** (each producing wrong numbers, wrong geometry,
a crash, or silent data corruption on a concrete input) plus ~38 lower-confidence
"plausible" findings tracked in the component reviews. Triage: **5 high priority,
15 medium, 63 low** — ranked by how often the code path runs in real pipelines and
whether it fails silently, *not* by raw formula severity.

**Epistemic status.** Code-level findings, several verified beyond reading: the
chi-squared EC density defect was reproduced three independent ways including a
Monte-Carlo simulation of smooth chi-squared random fields, and its fix has since been
**regression-tested by executing the real MATLAB code** in GNU Octave (the new unit
test fails 12/23 assertions on the pre-fix code, 0/23 on the fixed code — see
`reproductions/`). The KL/tensor/distribution findings were verified against
scipy/closed forms; the `spm_nlsi_GN` finding is confirmed by internal inconsistency
with its own M-step gradient. The SP3 and SP4 fixes have since been **reproduced on
SPM's own MMN tutorial dataset by executing the real M/EEG code** in Octave
(`reproductions/mmn_realdata/`), which also *shrank* both findings' reach — recorded
there rather than papered over — and SP3 was then **measured on ERP CORE (39
participants, two paradigms)**, where response-locked epochs turn the shipped artefact
marking into a no-op and change the group ERN by a quarter
(`reproductions/erpcore_realdata/`). Fixes 2 and 5 have **not** been executed in MATLAB.
"Exposed" means a study ran the affected code path — not that its conclusions are
wrong.

**The most reassuring result frames everything below:** the single most common SPM
workflow held up. A standard fMRI GLM — default HRF, realign → coreg → normalise →
smooth, T/F contrasts, RFT/FDR thresholding — was traced end to end and verified
correct (`spm_spm`, ReML/Satterthwaite machinery, T/F EC densities, both FDR
procedures, the NIfTI quaternion core, `spm_matrix`/`spm_imatrix`). The defects
cluster in the tiers out from that: specific statistic types, optional features,
particular toolboxes, rare formats, and edge cases.

## Findings, ranked by (severity × how often the path runs)

Confidence: **CONFIRMED** = traced end-to-end and/or reproduced numerically
(file:line evidence in `component-reviews/`); **PLAUSIBLE** = mechanism verified,
exposure or magnitude uncertain.

### Tier 1 — high priority (silent, on a traveled path or breaking a flagship method)

**SP1. Chi-squared EC densities use the wrong power of t at dimensions 2 and 3.**
CONFIRMED (three ways, incl. Monte Carlo; fix regression-tested in Octave).
`spm_ECdensity.m:48-53` reuses a single `t^((v-1)/2)` factor across EC orders where
Worsley's densities need `t^((v-d)/2)`; EC(3) is inflated by √t and EC(4) by t. RFT
inference on χ² statistic images is invalid in both directions: peak FWE far too
conservative (p reported 1.000 where the true value is 0.38), cluster extent grossly
anticonservative (1e-9 where the truth is 0.05). T/F fields unaffected; standard
conjunction analysis (min-statistic) *not* exposed. Reach is narrow — χ² SPMs are rare
in applied work, and no high-citation empirical SPM{χ²} paper was found — which is the
honest reason this severe defect ranks with, not above, the rest of the tier.

**SP2. `spm_nlsi_GN` free energy: log-det term overcounted by a factor of n_q.**
CONFIRMED. At `spm_nlsi_GN.m:500` the precision `iS` has already been
Kronecker-expanded, so `spm_logdet(iS)*nq/2` applies the n_q factor twice (n_q²/2 for
n_q/2). The M-step gradient (`ny/2`) is the derivative of the *corrected* term, so
objective and gradient currently disagree. Affects any inversion with more than one
error-covariance block — **DCM for evoked/induced responses** (n_q = channels×trials) —
where the hyperparameter-dependent part of F is inflated n_q-fold and can alter model
rankings, the primary output. fMRI DCM (n_q = 1) unaffected. Exposure anchors: David
et al. 2006 *NeuroImage* (~730 cites, the DCM-ERP methods origin) and Garrido et al.
2007 *PNAS* (feedback loops via DCM model comparison of MMN).

**SP3. `@meeg/badsamples` double-counts the peristimulus baseline when mapping
artefact events to samples.** CONFIRMED. The detectors write event times relative to
trial onset *without* `timeOnset` (the terms cancel in `D.time(idx+1)-D.time(1)`); the
reader adds `time(this)`, which *includes* it. Every bad-sample window on epoched data
is shifted by the baseline length (e.g. 25 samples for a 100 ms baseline at 250 Hz):
clean data excluded, artefact partially retained, silently. Reaches artefact `'mark'`
mode (bad-channel classification), `removebad` averaging masks, CFC weighting and other
epoched-data consumers; **not** the default `'reject'` mode, and not continuous data
(timeOnset = 0). **Reproduced on SPM's MMN tutorial data with the real code**
(`reproductions/mmn_realdata/`): masks shifted by exactly the 100 ms baseline, pre-fix
excluding only 24 % of true artefact samples while 71 % of what it excluded was clean —
yet the final robust-averaged MMN moved only ≈1.5 % RMS, because robust weights cushion
the mask. **Then measured on ERP CORE, 39 participants, two paradigms**
(`reproductions/erpcore_realdata/`): the shift equals the distance from epoch start to
time zero, so on response-locked epochs starting at −600 ms the shipped code pushes 97 %
of the detector's windows out of the epoch and excludes 0.5 % of the artefact it found;
the same rejection settings kept 98 % of trials before the fix and 49 % after, six
participants who have no clean error trials were silently given an ERN, and the group
ERN amplitude was −10.4 µV before vs −8.3 µV after (paired p = 0.003, n = 30). Robust
averaging with remove-bad-data was again cushioned (r = 0.99). Exposure anchor: Litvak
et al. 2011 (the SPM8 M/EEG reference paper, ~1000 cites, documents this exact
machinery). Merged upstream as PR #163.

**SP4. `spm_eeg_downsample` stamps the requested, not the achieved, sampling rate.**
CONFIRMED. The achieved rate is computed and *printed* (lines 52-61) but line 115
stores `S.fsample_new`. Fires only when the user explicitly selects `method='decimate'`
or `'downsample'` with a non-integer ratio (`ft_preproc_resample` then rounds the
factor); the default `'resample'` and the no-toolbox `'fft'` fallback are exact, which
narrows the reach from the project's first framing. **Reproduced with the real code on
SPM's MMN tutorial data** (`reproductions/mmn_realdata/`): 512→200 Hz with `decimate`,
pre-fix prints 170.7 Hz and stamps 200 Hz, so the 915 s recording is reported as 781 s
and a real 275 ms MMN peak would be reported at 235 ms; merged upstream as PR #165.

**SP5. `spm_design_contrasts` pads parametric-modulation columns without the
basis-function factor.** CONFIRMED (numerically). Line 63 inserts `sum(h)` zero
columns where the design carries `sum(h)·nbases` (every `U.u` column is convolved with
all basis functions in `spm_Volterra`), so automatic factorial contrasts slide onto the
wrong regressors whenever `nbases > 1` *and* modulators are present; the trailing
zero-pad hides the mismatch, so the wrong F/T maps arrive without any error.

### Tier 2 — medium priority (common feature, conditional trigger; or important narrower method)

**SP6.** `spm_dicom_convert.m:572` pairs PixelSpacing with the wrong direction
cosines — in-plane voxel sizes swapped for non-square pixels (the spectroscopy path
swaps them back with a "for some reason" comment). CONFIRMED.
**SP7.** `spm_file_merge.m:105` sign error (`-mn/dmn`, datatype minimum is negative)
clips negative intensities merging 3D→4D integer volumes. CONFIRMED, reproduced.
**SP8.** `spm_preproc_write8.m:428-429` returns `wc`/`mwc` in swapped slots, breaking
Segment's multi-iteration group-template path and `'inmem'` warped tissues. CONFIRMED.
**SP9.** `spm_MDP_VB_X.m:940-946` indexes the action dimension of the B-novelty term
with the *policy* index and transposes the contraction; the exploration bonus is wrong
whenever transitions (`b`) are learned. CONFIRMED. Anchor: the `spm_MDP_VB_X` engine of
Friston et al. 2017 *Neural Computation* (process theory).
**SP10.** `spm_MDP_MI.m` gradient uses an elementwise term where the chain rule needs
the scalar ⟨dEdA,A⟩ — 50–100% error, wrong sign pattern; steers `spm_MDP_VB_prune`
structure learning the wrong way. CONFIRMED numerically. Anchor: Smith et al. 2020
(structure learning via BMR).
**SP11.** `spm_dcm_peb.m:593-600` nests the convergence `break` inside `if verbose`:
with printing off, PEB always runs 64 iterations and results depend on a display
preference. CONFIRMED. Anchor: Friston et al. 2016 (PEB); default verbose=true is safe.
**SP12.** `spm_lg_gamma.m:25` sums *ascending* gamma arguments where the multivariate
gamma descends (its own out-of-range guard only makes sense for the descending form);
`spm_kl_wishart.m:38` additionally uses E_P[log|X|] where KL(Q‖P) needs E_Q. Both
CONFIRMED numerically (scipy `multigammaln`; Wishart MC: true KL 6.560, coded 7.681).
Corrupts mixture-model/MAR evidence.
**SP13.** `spm_wft.m:28`/`spm_iwft.m:18` — `'` (conjugate) for `.'`: the windowed-FT
pair is phase-inconsistent; round-trip destroys the signal (sine → −sin/2). CONFIRMED.
**SP14.** `spm_morlet_conv.m:34` off-by-one shifts the smoothed cross-spectral density
down one frequency bin on every call. CONFIRMED.
**SP15.** `spm_powell.m:123-125` bracket step-clamp has the wrong sign for descending
line searches (the common case): legitimate parabolic steps clamped, runaways passed.
Degrades MI coregistration; brackets remain valid, so results degrade rather than
break. CONFIRMED, reproduced on a quadratic.
**SP16.** `toolbox/Spatial/spm_smooth_extrap.m:57-59` FFT-smoothing grid is
half-a-voxel off-centre for odd dimensions — the smoothed voxel-displacement map (and
hence the unwarped EPI) shifts ~0.5 voxel along odd axes. CONFIRMED numerically.
**SP17.** `spm_mesh_distmtx.m:37-40` halves boundary-edge lengths on open meshes;
feeds source-reconstruction patch setup. CONFIRMED.
**SP18.** `spm_deformations.m` — missing det<0 sign fix on sn.mat import (present in
the OldNorm reference implementation), and the multi-volume mask is overwritten rather
than intersected. Both CONFIRMED.
**SP19.** `spm_robust_glm.m:95` multiplies residuals by leverage instead of dividing
by √(1−h): no observation is ever down-weighted and "robust" GLM degenerates to OLS.
CONFIRMED numerically — but scoped: only `toolbox/mixture/spm_glm.m` calls it;
mainstream robust averaging uses `spm_robust_average`, which verified correct.
**SP20.** Mode-breaking crashes (loud, so lower urgency): hierarchical `spm_MDP_VB_XX`
(cell/scalar collision), `toolbox/DEM/spm_MDP_size` (case typo, likelihood-only path dead),
`spm_eeg_cfc` confound output (`sig_conf` undefined; double-incremented counter),
documented `excwin==0` artefact option, `spm_eeg_average_TF` missing default.
All CONFIRMED.

### Tier 3 — low priority (63 defects; full lists with file:line in `component-reviews/`)

| Group | ≈ | Representative |
|---|---|---|
| Distribution edge cases | 10 | `spm_ncFcdf` series truncation (noncentrality ≳62 → ~0), `spm_Gcdf` upper tail at x≤0, `spm_Pcdf` non-integer x |
| Rare datatypes / formats | 8 | `spm_getdata.c` int64 byte-swap via a `double` temp (garbage voxels), big-endian GIfTI swap dead (`strncpm` typo), MINC per-frame offset, PAR/REC slice permutation inverted |
| Latent / no live caller | 9 | `spm_SpUtil('ConO')` wrong metric, `spm_reml_A` asymmetric derivative, `spm_FcUtil('ukX0')` undefined variable |
| C / MEX edge cases | 4 | `spm_get_lm.c` origin-neighbour `>0` vs `>=0`, `spm_unlink.c` unsigned wraparound |
| I/O & tabular minor | 8 | `@nifti` `end_slice` typo, header extensions dropped on write, CSV quote corruption, `spm_read_vols` two-arg mask hits wrong volumes |
| Mesh & numeric utilities | 13 | Laplacian sign flip between options, voxelise crops top slab, even-kernel circular convmtx |
| M/EEG conventions | 7 | tfphase sin/cos regressors swapped (phases 90° off), grandmean condition misalignment, planar-combine coordinate copy-paste |
| Spatial / preprocessing minor | 4 | `spm_realign` custom-`lkp` zoom perturbation, `save crap.mat` debug leftover on a live path |

## What was checked and found CORRECT

Equally important for reading the findings in proportion:

- **Z, T and F EC densities**, `spm_P_RF` (unified formula and Poisson clumping), both
  **FDR procedures** (exact BH), Bonferroni, `spm_resels`, `spm_est_smoothness`.
- **The GLM core**: `spm_spm`'s whitening/df machinery, trRV/trRVRV Satterthwaite
  identities, ReML gradients/curvatures, `spm_hrf` and filter construction, microtime
  onset handling, `spm_get_vc` Kronecker orderings.
- **NIfTI quaternion↔matrix round-trip** (<3e-12 over 20,000 rotations) and the
  0-based/1-based voxel conventions everywhere traced; `spm_write_vol` scaling.
- **`spm_matrix`/`spm_imatrix`** round-trips incl. negative determinants; reslice
  shear decomposition; slice-timing Fourier phase (even/Nyquist handling).
- **DCM machinery**: hemodynamic Balloon equations and Jacobians, `spm_gx_fmri`
  (Stephan 2007 coefficients), `spm_BMS` (exact Stephan 2009), `spm_PEB`, BMR closed
  form, KL of normal/gamma/Dirichlet, `spm_expm`/`spm_dx`/`spm_diff` stencils.
- **M/EEG**: `spm_robust_average` (the mainstream robust-averaging path),
  `tf_rescale` formulas, Morlet frequency mapping, Kabsch rigid registration,
  epoching arithmetic.
- **`spm_dot`/`spm_kron` tensor conventions** (einsum-verified across dimension
  patterns), `spm_KL_dir`/`spm_dir_H` against scipy.
- **B-spline tables, DARTEL/Shoot integration, Longitudinal registration core,
  OldNorm det<0 handling**; shoot boundary wrapping and OpenMP regions in `src/`.

## Literature exposure (assessed for Tier 1 + selected Tier 2 only)

Method→code links, with honesty flags; none is a claim that a result is wrong.

| Finding | Anchor | Confidence |
|---|---|---|
| SP2 | Garrido et al. 2007 *PNAS*; David et al. 2006 *NeuroImage* | high — exact method+trigger |
| SP3 | Litvak et al. 2011 (SPM8 M/EEG reference) + any epoched auto-artefact pipeline | high for the path |
| SP5 | Henson et al. 2002 *Cereb Cortex* (factorial + derivatives) | medium — modulator+auto-contrast use unverified |
| SP4 | — | trigger (non-integer ratio) not recoverable from published metadata |
| SP1 | Worsley 1994 (theory only) | no applied SPM{χ²} paper found; exposure genuinely thin |
| SP9/SP10 | Friston et al. 2017 *Neural Comp.*; Smith et al. 2020 | high for simulations learning `b` / using BMR pruning |

## Upstream status

Five fixes plus a new unit test are implemented and pushed to the `cindykrafft/spm`
fork (`upstream/README.md` has the branch/compare table and issue/PR bodies). **Two
are merged upstream**: SP3 ([PR #163](https://github.com/spm/spm/pull/163)) and SP4
([PR #165](https://github.com/spm/spm/pull/165)), both merged 2026-09-02. SP1
([#158](https://github.com/spm/spm/issues/158) / [PR #159](https://github.com/spm/spm/pull/159),
shipping `tests/test_spm_ECdensity.m` — the function previously had **no test
coverage**; it fails 12/23 assertions on the pre-fix code and 0/23 on the fix) and
SP2 ([#160](https://github.com/spm/spm/issues/160) / [PR #161](https://github.com/spm/spm/pull/161))
are open, as is SP5 ([#167](https://github.com/spm/spm/issues/167) / [PR #168](https://github.com/spm/spm/pull/168), filed 2026-09-02).

## Files

| File | Contents |
|---|---|
| `component-reviews/*.md` | the eleven subsystem reviews with file:line evidence (all 83 confirmed + plausible findings) |
| `reproductions/` | verification harnesses: SciPy transcriptions, the χ² Monte-Carlo, the Octave old-vs-new regression of the SP1 fix, and the real-data runs of the merged fixes (SPM's MMN tutorial data; ERP CORE, 39 participants) |
| `upstream/` | filing kit: fix branches, compare URLs, issue and PR bodies |

## Suggested next steps

1. Run SP2–SP5 through real MATLAB (`spm_tests` plus targeted checks) before filing
   their PRs; state in each PR what testing was done.
2. All five issues + PRs are filed (`upstream/README.md`); follow up on maintainer
   review of SP1, SP2 and SP5.
3. Extend the survey join: mine the six-journal corpus for SPM usage the way
   `fs_profile.py`/`fsl_profile.py` did, and build `spm_papers.tsv` /
   `spm_paper_exposure.tsv` so Tier 2 findings get per-paper exposure.
4. Medium tier is patch-ready material for a second submission wave (SP6-SP8 and SP12
   are crisp one-liners).
