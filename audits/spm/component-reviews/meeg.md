# Component review: M/EEG signal processing

Scope: preprocessing (`spm_eeg_filter`/`downsample`/`epochs`/`bc`),
averaging (`spm_eeg_average*`, `spm_robust_average`, `spm_robust_glm`,
`spm_eeg_grandmean`, `spm_eeg_merge`/`fuse`), montage/planar, time-frequency
(`spm_eeg_tf*`, the four `specest` plugins, `spm_eeg_morlet`, `spm_eeg_cfc`),
all artefact detectors, regressors, spatial confounds, coordinate transforms,
and the `@meeg` computational methods.
Method: full read; key findings reproduced numerically; writer/reader event
conventions traced through convert → epochs → detectors → consumers.

## Confirmed

1. **`@meeg/badsamples.m:39-40`** — artefact events are mapped to samples via
   `trialonset + time(this)`, but `time(this)` includes the peristimulus
   `timeOnset` while every detector writes event times relative to trial onset
   *without* it (e.g. `spm_eeg_artefact_jump:126`,
   `D.time(idx+1)-D.time(1)+trialonset` — the timeOnset terms cancel). The
   bad-sample window is shifted by the full baseline (`timeOnset·fs` samples)
   on any epoched dataset. Corrupts `spm_eeg_artefact` mark-mode
   classification, `removebad` averaging masks, `spm_eeg_cfc` weighting,
   DAiSS robust covariance. **High** (SP3; fix staged upstream). Note:
   `removebad` defaults off in averaging, so the main reach is automatic
   artefact classification.
2. **`spm_eeg_downsample.m:115`** — stamps `S.fsample_new` (requested) where
   the achieved rate `fsample_new` — computed at line 52 and *printed* at
   line 61 — belongs; `ft_preproc_resample` rounds the decimation factor, so
   non-integer ratios store a wrong rate (1000→180 request = 166.7 Hz actual).
   **High for non-integer ratios** (SP4; fix staged upstream).
3. **`spm_robust_glm.m:95`** — `res = res.*H` multiplies residuals by leverage
   h_ii (≈p/n ≪ 1) instead of dividing by √(1−h_ii)
   (`spm_eeg_robust_averaget:21` does it right): standardised residuals shrink
   below any threshold and no observation is ever down-weighted — robust GLM
   degenerates to OLS. Reproduced. Scope: only `toolbox/mixture/spm_glm.m`
   calls it; the mainstream robust-averaging path uses `spm_robust_average`
   (verified correct). (SP19.)
4. **`spm_eeg_grandmean.m:245,261`** — `indtrial` silently drops missing/bad
   conditions, so per-file trial indices misalign with the condition list:
   the wrong condition's data is averaged in, then an out-of-bounds crash.
   Contradicts the documented behaviour. **Moderate.**
5. **`spm_eeg_montage.m:84-90`** — branch senses swapped: a string *matching*
   an online-montage name errors; a non-match is tried as a file. The
   documented name-based API always fails. **Moderate.**
6. **`spm_eeg_cfc.m:544`** — `sig_conf` vs the defined `sig_cnf`: crash at the
   output stage, after the whole GLM has run, whenever confounds are given.
   **Moderate.**
7. **`spm_eeg_cfc.m:63-66`** — `cnt` incremented twice per confound; `S1` gets
   gaps → crash with ≥2 confounds, wrong regressor association with 1.
   **Moderate.**
8. **`spm_eeg_regressors_tfphase.m:144 vs 200-206`** — data concatenated
   cos-first but named sin-first: `Beta_sin`/`Beta_cos` swapped and any
   preferred phase from `atan2(Bsin,Bcos)` is 90° wrong (the combined PAC
   r-value is unaffected). **Moderate.**
9. **`spm_eeg_merge.m:283`** — `strrep` handed a 1×1 cell (`clb(ind(j))` for
   `clb{ind(j)}`): the documented `#labelorg#` recoding (the help's own
   example) corrupts condition labels. **Moderate.**
10. **`spm_eeg_spatial_confounds.m:81`** — `eyes` transformed in place inside
    the modality loop; a second modality's eye leadfields are computed at
    double-transformed (meaningless) locations. **Moderate.**
11. **`spm_eeg_combineplanar.m:197`** — combined-channel 2D coordinate
    averages `chanind(1,:)` with itself (copy-paste; should be `(2,:)`).
    **Low.**
12. **`spm_eeg_artefact_threshchan.m:114`** — missing `sum()`: an `if` on a
    0/1 *vector* divided by nsamples; the whole-channel marking branch can
    essentially never trigger. **Low.**
13. **`spm_eeg_artefact_zscore.m:113`** — `bad(end)` (linear, last trial)
    instead of `bad(end,i)`: end-of-trial artefact runs get empty-duration
    events or spurious offsets. **Low-moderate.**
14. **`spm_eeg_artefact_jump.m:101-113`** (same in threshchan) — the
    documented `S.excwin == 0` option leaves `excwin` undefined → crash on the
    first detected jump. **Low-moderate** (part of SP20).
15. **`spm_eeg_average_TF.m:44`** — `S.robust.removebad` dereferenced without
    a default → crash on direct calls (works only via the `spm_eeg_average`
    redirect). **Low** (part of SP20).

## Plausible

16. jump/threshchan excision kernels use `5e-4*excwin*fs` with `'same'`
    convolution — half the width the sibling detectors apply for the same
    parameter (likely factor-2).
17. One-sample event-time disagreement between detector families
    (`onset/fs` vs `(onset−1)/fs`).
18. `spm_eeg_specest_mtmfft.m:110` — `res.time = [1 1]*mean(time)` yields
    `fsample = 1/0 = Inf` on the output dataset.
19. flat/nans whole-channel event duration adds 1 *second* instead of one
    sample.
20. `spm_eeg_inv_icp.m:86` — `(norm(M)-1) < 1e-3` is blind to pure rotations.
21. eyeblink/saccade/heartbeat duration clipping compares against 0 instead
    of trial onset.

## Verified correct

`spm_eeg_tf_rescale` (LogR/Rel/Diff/zscore), `spm_eeg_morlet` frequency
mapping/normalisation and specest group-delay compensation,
`spm_robust_average` weight math, `spm_eeg_bc`, `spm_eeg_filter` (Nyquist
checks, twopass), `spm_eeg_epochs`/`spm_eeg_definetrial` sample arithmetic,
`spm_eeg_inv_headcoordinates` (CTF axes), `spm_eeg_inv_rigidreg` (Kabsch with
reflection guard), `spm_eeg_inv_transform_points`, CTF movement regressors.
