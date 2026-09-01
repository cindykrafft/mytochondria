# Component review: numeric utilities & mesh functions

Scope: signal/matrix utilities (`spm_wft`/`spm_iwft`, `spm_morlet_conv`,
`spm_timeseries_resample`, `spm_phase_shuffle`, `spm_convmtx`, `spm_dwtmtx`,
`spm_conv`, `spm_hilbert`, `spm_dftmtx`, `spm_interp`, `spm_sptop`,
`spm_str_manip`, `spm_diag`, `spm_speye`, `spm_trace`, `spm_argmax`,
`spm_minmax`, …) and the `spm_mesh_*` family.
Method: full read; suspicious math transcribed to numpy/scipy and tested
(FFT identities, scipy.signal.hilbert, mesh formulas on unit solids).

## Confirmed

1. **`spm_wft.m:28` / `spm_iwft.m:18`** — `'` (conjugate transpose) where
   `.'` was meant: `spm_wft` demodulates with e^{+iωt} and returns conjugated
   coefficients while `spm_iwft` synthesises assuming the standard convention.
   Round trip destroys the signal (cosine → +cos/2 but sine → −sin/2; random
   band-limited signal reconstructs with corr ≈ −0.01; with the conjugation
   removed, corr 0.996). Any consumer of `angle(C)` gets reversed phases;
   affects `spm_phase_shuffle`'s windowed branch. **High** among utility
   findings (SP13).
2. **`spm_morlet_conv.m:34`** — `h(iw + nw - i)` peaks one bin off (columns of
   H peak at row i+1): `G*H` both smooths and *shifts the cross-spectral
   density down one frequency bin* on every call (`spm_csd_int`,
   `spm_gen_fmri`). Fix: `h(iw + nw + 1 - i)`. Also: help says wnum default 2,
   code uses 8. **Moderate-high** (SP14).
3. **`spm_timeseries_resample.m:23-33`** — output length off by one (N+1 when
   downsampling to even N; N−1 upsampling from even N0) and the returned
   `alpha` does not match the data actually returned — silently wrong
   effective sampling rate for consumers. **Moderate.**
4. **`spm_phase_shuffle.m:34`** — `abs(s)` at the DC/Nyquist bins: a
   negative-mean channel's surrogate gets a sign-flipped baseline (input mean
   −5.10 → surrogate +5.10). **Moderate.**
5. **`spm_convmtx.m:49-56`** — `'circular'` folds `fix((len−n)/2)` rows from
   each end; even-length kernels lose one wrap row and the result is not
   circulant (kernel [1 2 3 4]: one column sums 6 instead of 10).
   `spm_morlet` always builds an even kernel (small effect there). **Low-mod.**
6. **`spm_dwtmtx.m:60-67`** — the thinning option builds a length-N mask but
   indexes basis *columns* (≈N/K): crash for any K > 1; the feature only
   works for K=1 by coincidence. **Moderate (unusable).**
7. **`spm_mesh_laplacian.m:30 vs 49-56`** — 'graph' returns D−A (PSD,
   positive diagonal); the 'mesh' cotangent branch assembles the opposite sign
   convention (verified: quadratic form +8.5 vs −2.25 on the same mesh).
   Switching the option silently flips every eigenvalue. **Moderate.**
8. **`spm_mesh_distmtx.m:37-40`** — each edge inserted once per incident face
   then symmetrised by (D+D')/2: boundary edges of *open* meshes come out at
   half their true length (single 3-4-5 triangle → 1.5, 2.0, 2.5). Feeds
   `spm_eeg_invert` patch setup on open cortical meshes. **Moderate** (SP17).
9. **`spm_mesh_voxelise.m:37-39`** — `dim = ceil(diff(bb)./vx)` without +1:
   the last voxel maps strictly below bb(2,:), so the top slab of the mesh is
   outside the grid on every axis. **Low-moderate.**
10. **`spm_sptop.m:38-41`** — vector-kernel centring `fix(length/2)` shifts
    odd-length kernels by one sample (impulse at 5 → peak at 6); the
    scalar-sigma branch is correct. Latent (in-tree caller passes c=1).
    **Low.**
11. **`spm_str_manip.m:149-154`** — the 'k' truncation returns n+1 characters
    (`l-c+2` vs the correct `l-c+3` used by `spm_file` 'short'). **Low.**
12. **`spm_diag.m:40`** — non-square cell arrays error (mask built at
    `max(m,n)` square); builtin `diag`, which this generalises, handles them.
    **Low (crash).**
13. **`spm_mesh_inside.m:36`** — `ray.vec = XYZ' + [0 0 1]'` is a *point*, not
    a direction; for the query (0,0,−1) the direction is the zero vector and
    the point is always classified outside. **Low.**

## Plausible

14. `spm_mesh_normals.m:72` — fallback orientation test counts *nonzero* dot
    products, not positive ones ("always flip"); wrong for near-planar meshes.
15. `spm_trace.m:13` — `A'.*B` conjugates: wrong for complex inputs (all
    current callers real).
16. `spm_argmax.m:61-83` — rejected Gauss-Newton steps are never actually
    reverted (`p` not resynced from `P.x`); `P.x` unset if the first
    evaluation is NaN.
17. `spm_minmax.m:59-65` — histogram bin indices treated as intensities;
    both returned limits biased high by 1-2 bins (self-described heuristic).
18. `spm_speye.m:36-37` — the c=2 option transposes the sparse dimensions;
    m≠n calls error.

## Verified correct

`spm_conv` (matches scipy 'reflect' exactly), `spm_hilbert`
(machine-precision vs scipy, even and odd n), `spm_hanning`, `spm_dftmtx`,
`spm_orthpoly`, `spm_detrend`, `spm_en`, `spm_meanby`, `spm_interp` (DCT
scaling exact), `spm_polymtx`, `spm_morlet` (its `K'` conjugation is
load-bearing and correct), `spm_smohist`, `spm_hist_smooth`, `spm_kron`/
`spm_combinations`/`spm_permute_kron` (consistent house convention),
`spm_cov2corr`, `spm_length`, `spm_squeeze`, `spm_sum`, `spm_diag_array`,
`spm_cell_swap`, `spm_data_id`, `spm_sixel`, `spm_fileparts`, `spm_file`,
`spm_XYZreg`, `spm_rand_mar`, `spm_rand_power_law`; mesh: area (Kahan-stable
Heron), adjacency, edges, euler, curvature, clusters, get_lm, max, smooth,
mass_matrix, refine, sphere, polyhedron, project, contour/isoline (edge
tables verified algebraically), ray_intersect (Möller-Trumbore), to_grid
(conservation exact on closed meshes).
