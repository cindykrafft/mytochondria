# Component review: spatial preprocessing

Scope: `spm_realign`/`spm_reslice`/`spm_coreg`, `spm_slice_timing`,
smoothing (`spm_smooth`/`spm_smoothkern`/`spm_conv*`), affine utilities
(`spm_matrix`/`spm_imatrix`/`spm_get_space`/`spm_get_bbox`), `spm_powell`,
unwarping (`spm_uw_*`), `spm_deformations`, segmentation
(`spm_preproc*`, `spm_maff8`, priors), `spm_mask`/`spm_imcalc`.
Method: full read; geometry/algebra traced; key claims reproduced
numerically (kernel identities, Powell bracket behaviour on a quadratic).

## Confirmed

1. **`spm_preproc_write8.m:428-429`** — the `wc`/`mwc` return slots are
   swapped relative to both call sites in `spm_preproc_run`: the
   multi-iteration group-template path reads empties (crash or empty
   template), and the `'inmem'` action fills the wrong output with modulated
   data. Default single-iteration file-writing segmentation is unaffected.
   **Moderate-high for those paths** (SP8).
2. **`spm_uw_apply.m:369` + `spm_uw_get_image_def.m:103-109`** — with the
   Jacobian option jm=1 ("static field only"), an empty `ddef_array` is passed
   and treated as "please recompute", so the movement-interaction modulation
   the user deselected is applied anyway. jm=2/3 behave as labelled.
   **Moderate.**
3. **`spm_deformations.m:120-133`** (`get_sn2def`) — missing the
   `if det(M(1:3,1:3))<0, vxg(1) = -vxg(1)` sign fix present in the reference
   implementation (`toolbox/OldNorm/spm_write_sn.m:471`): sn.mat import with a
   left-handed template and custom bb/vox produces an x-mirrored/mispositioned
   deformation. **Moderate** (part of SP18).
4. **`spm_deformations.m:386-421`** (`pull_def`) — the common out-of-FOV mask
   is *assigned*, not intersected, across volumes: only the last
   distinct-header volume's mask survives, contradicting the batch help.
   Wrong masking for multi-orientation pulls. **Moderate** (part of SP18).
5. **`spm_powell.m:123-125`** (`bracket`) — the "very conservative" step clamp
   has the wrong sign whenever the line search proceeds downward (very common:
   whenever f(p+xi) > f(p)): every legitimate parabolic step is discarded for
   a maximal golden-ratio extrapolation, and runaway steps pass unclamped.
   Reproduced on f(x)=(x+3)². Returned brackets remain valid, so this degrades
   (wasted evaluations; possible different local minimum in MI coregistration)
   rather than breaks. **Low-moderate** (SP15).
6. **`spm_realign.m:474`** (`make_A`) — `pt(lkp(i)) = pt(i)+1e-6` should read
   `pt(lkp(i))+1e-6`: with a custom `flags.lkp` including zoom parameters
   (e.g. [1 2 3 7 8 9]) the "perturbed" zoom becomes 1e-6 instead of 1+1e-6 —
   the derivative column is garbage and that parameter silently fails to
   register. Default lkp unaffected. **Low.**
7. **`spm_sample_priors8.m:44 vs 69`** — non-finite voxels get `bg2` in the
   no-derivative branch but `bg1` in the derivative branch: the objective is
   inconsistent with its own gradient at those voxels. **Low.**
8. **Debug leftovers on live paths** — `spm_deformations.m:899` `save
   crap.mat` (saves the *entire workspace* on every `def2sparse` run);
   `spm_preproc_run.m:159` `save SS.mat SS M1`. **Low.**

## Plausible

9. `spm_uw_estimate.m:542 vs 584` — AtA built in the `P(1).mat` frame, Aty in
   the `ds.M` frame; they disagree exactly in the documented multi-session use
   (`par.M` = first scan of the first series). The shipped batch avoids it.
10. `spm_uw_estimate.m:596`/`make_ref` — derivatives on the irregular
    estimation grid contracted without `diag(1./ss)` (ss = [1.1 1.1 0.9]):
    the GN Jacobian is anisotropically mis-scaled ~10%.
11. `spm_preproc8.m:459` — `vr0(N,N)` for `vr0(n,n)`: every channel's
    histogram-smoothing regularisation uses the last channel's variance
    (multi-channel non-parametric mode only).
12. `spm_uw_estimate.m:801-803` — FOV mask compares every scan against
    `P(1).dim`.
13. `spm_preproc.m:224` — `vr(lkp(K))*8` indexes per-Gaussian variances with
    a class number; currently dead code (`finalit` is followed by `break`).

## Verified correct

`spm_smoothkern` (matches the analytic Gaussian⊛B-spline at t=0/1 to ~1e-16);
`spm_matrix` analytic derivative block (central differences to 1e-9);
`spm_imatrix`↔`spm_matrix` round-trip incl. negative determinants (≤3e-15);
`spm_reslice`/`shear_decomp` (A = S0·S1·S2·S3 to 5e-14); `spm_slice_timing`
Fourier phase (band-limited shifts, even-length/Nyquist and conjugate
symmetry correct); `spm_get_closest_affine`; `spm_maff8` P2M/M2P round-trip;
`spm_mask`/`spm_imcalc` plane-transform composition.
