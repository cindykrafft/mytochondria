# Reproductions

Verification harnesses for the SPM audit (`../README.md`). Two kinds live
here: SciPy/NumPy transcriptions used *during* the audit to confirm findings,
and the post-fix **Octave regression that executes the real MATLAB code** of
the SP1 fix.

## SP1 — chi-squared EC densities (`spm_ECdensity`)

The finding was established three independent ways and the fix then
regression-tested against the actual shipped code:

| File | What it does | Result |
|---|---|---|
| `ec_check.py`, `ec2_check.py` | faithful transcription of `spm_ECdensity`; cross-checks Z/T/F/X branches via the identities T(∞)↔Z, F(1,v)↔T², χ²₁↔2Z, χ²ₖ↔k·F(k,∞) | buggy EC(3)/EC(4) off by exactly √t / t; Z/T/F consistent |
| `sim_chi2.py` | Monte-Carlo simulation of smooth χ²₄ random fields on a 256² torus (300 realisations, FWHM 8), empirical E[EC] vs formulas | empirical 59.5/15.1/3.2 at t=12/16/20; corrected formula 60.5/15.8/3.5; shipped 209.5/63.1/15.6 |
| `impact_check.py` | end-to-end `spm_P_RF` impact quantification (peak FWE, cluster extent) with whole-brain resels | peak p 1.000 shipped vs 0.380 corrected at u=40 (χ²₁₀); extent p 1e-9 vs 0.050 |
| `verify_ec.py` | fixed-vs-buggy vs the F-limit reference, the check run before committing the fix | fixed matches to reference tolerance; buggy reproduces √t / t |
| `regression_ec.m` (+ `tern.m`) | **Octave, real MATLAB code**: identities A (χ²₁=Z², 10 decimal places) and B (F-limit at df=10⁸), bit-identity of the untouched Z/T/F branches and χ² orders 0-1, end-to-end `spm_P_RF` | ALL CHECKS PASSED on the fixed code |
| `driver.m` | the exact assertions of the new `tests/test_spm_ECdensity.m`, runnable against either code version (shadow the fixed file with the pre-fix one) | pre-fix: 12/23 assertions fail; fixed: 0/23 |
| `conv_check.m` | shows the residual new-vs-F-limit deviation scales as 1/V (1.4e-3 → 1.5e-6 for V=10⁵→10⁸) | the deviation is the *reference's* finite-df error, not the fix's |

To run the Octave pieces: `addpath` a checkout of the fixed SPM
(`cindykrafft/spm`, branch `fix/ecdensity-chi2`), extract the pre-fix file
with `git show 530ec52:spm_ECdensity.m`, and follow the comments in
`driver.m`. Octave 8.4 suffices — the code path is pure MATLAB
(`gammaln`/`gammainc`/`betainc` only).

## Other findings verified numerically during the audit

| File | Finding | Result |
|---|---|---|
| `kl_wishart.py` | SP12: `spm_kl_wishart` uses E_P[log\|X\|] where KL(Q‖P) needs E_Q | Monte-Carlo true KL 6.560; coded formula 7.681; corrected 6.559 |
| `mdp_tensor_checks.py` | MDP review: `spm_dot`/`spm_cross`/`spm_MDP_G`/`spm_KL_dir`/`spm_dir_H`/`spm_MDP_MI` vs einsum/scipy/MC | `spm_dot` and the KL/entropy helpers verified correct; `spm_MDP_MI`'s gradient 50-100% off (SP10); `spm_cross` interior-singleton stripping reproduced |

## What is *not* preserved

The eleven subsystem reviewers wrote many further ad-hoc verification
scripts (distribution CDFs vs scipy, `spm_hilbert`/`spm_conv` identities,
Powell bracket reproduction, `spm_file_merge` scale-factor arithmetic,
`spm_smooth_extrap` half-voxel shift, design-contrast misalignment, and
others cited in the component reviews). Only the attributable harnesses
above were retained; results are recorded in `../component-reviews/` with
the numbers they produced. Re-deriving any of them from the file:line
evidence is mechanical.

**Status note:** SP1 is the only fix executed against real MATLAB code so
far (in Octave). SP2-SP5's fixes are verified by tracing and the offline
numerics above but have not been run in MATLAB — do that before filing
their PRs (see `../upstream/`).
