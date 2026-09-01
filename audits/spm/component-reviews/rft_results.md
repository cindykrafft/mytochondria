# Component review: random field theory, thresholding & results

Scope: `spm_ECdensity`, `spm_EC_density`, `spm_P*`, `spm_uc*`, `spm_resels*`,
`spm_est_smoothness`, `spm_max`/`spm_clusters`, `spm_getSPM`/`spm_list`/
`spm_VOI`/`spm_ROI`/`spm_regions`/`spm_searchlight`/`spm_mip`,
`spm_write_filtered`, `spm_mesh_resels`.
Method: full read; EC/P-value paths transcribed to Python and validated by a
chain of independent identities (T(∞)↔Z, F(1,v)↔T², χ²(1)↔2Z, χ²(k)↔k·F(k,∞)),
a Monte-Carlo simulation of smooth χ² fields on a torus, a numerical
reproduction of `spm_P_RF`, and exact comparison of both FDR branches against
Benjamini-Hochberg. Harnesses: `../reproductions/`.

## Confirmed

1. **`spm_ECdensity.m:48-53`** — χ² EC densities reuse `b ∝ t^((v-1)/2)`
   across EC orders 2-4 where Worsley's formulas need `t^((v-d)/2)` (the F
   branch below decrements its exponent per order; the X branch does not).
   EC(3) inflated by exactly √t, EC(4) by t — proven by (a) χ²₁ vs two-sided
   Gaussian, (b) the v→∞ limit of SPM's own F densities, (c) direct simulation
   (empirical E[EC] 59.5/15.1/3.2 at t=12/16/20 vs corrected 60.5/15.8/3.5 vs
   shipped 209.5/63.1/15.6). Peak FWE for χ² SPMs reported 1.000 where the
   truth is 0.380; cluster extent p 1e-9 where the truth is 0.050. Propagates
   through every STAT=='X' path (`spm_P_RF`, `spm_uc_RF`, cluster/peak FDR,
   `spm_run_setlevel`). **High severity, narrow reach.** Fix + new unit test
   staged upstream (SP1).
2. **`spm_EC_density.m:75`** — the χ² branch passes the χ² value where the
   F-based generic density needs `t/df(2)` (χ²_v = v·F_{v,∞}); wrong by orders
   of magnitude for v > 1. No in-tree callers — latent API defect.
3. **`spm_EC_density.m:98-99`** — silently caps df at 256, so the exact
   Gaussian (Inf-df) branch actually returns F(1,256) densities: +10% at u=3,
   +86% at u=5, diverging at higher u. No in-tree callers.

## Plausible

4. `spm_mesh_resels.m:29-36,57` — the no-residuals default takes the *mean*
   over coordinates of squared differences: edge lengths low by √3, resel
   areas by 3 (SurfStat's fallback uses the Euclidean norm). The residuals
   path used by `spm_spm` is correctly normalised.
5. `spm_write_filtered.m:77` — `Y(OFF) = Z.*(Z > 0)` zeroes negative surviving
   values (reachable for PPM log-odds with a negative threshold).

## Verified correct

Z/T/F EC densities (mutually consistent, Monte-Carlo/textbook exact);
`spm_P_RF` (E[EC] machinery, Poisson clumping, Friston-1994 extent form, D-1
bookkeeping); `spm_P_FDR` both branches, `spm_uc_FDR`, `spm_uc_clusterFDR`,
`spm_uc_peakFDR` (numerically identical to reference BH incl. sentinel/cummin
logic and resel round-trips); `spm_P_Bonf`/`spm_uc_Bonf`/`spm_uc`/`spm_P`
gating; `spm_resels` (Worsley Table I intrinsic volumes);
`spm_est_smoothness` (determinant expansion, n/edf scaling, RESEL→FWHM);
`spm_max`/`spm_clusters` indexing; `spm_getSPM`, `spm_list` (k↔resel
conversions, nonstationary weighting), `spm_VOI` (mm→voxel regridding),
`spm_ROI`, `spm_regions` (eigenvariate SVD), `spm_searchlight`, `spm_mip`.
`spm_Pec_resels` has a sorted-list assumption but is dead code.
