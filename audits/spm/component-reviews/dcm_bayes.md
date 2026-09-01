# Component review: model inversion & Bayesian machinery (DCM core)

Scope: `spm_nlsi_GN`/`_Newton`/`_LS`, linear-algebra utilities (`spm_logdet`,
`spm_inv`, `spm_pinv`, `spm_sqrtm`, `spm_expm`, `spm_dx`, `spm_diff`,
`spm_vec`/`spm_unvec`, `spm_cat`), the `spm_int` family, `spm_PEB`,
`spm_peb_ppi`, DCM-fMRI models (`spm_fx_fmri`, `spm_gx_fmri`, priors), BMA/
BMR/PEB (`spm_dcm_bma`/`bmr`/`bmr_all`/`peb`/`peb_bmc`), `spm_BMS*`, KL
divergences.
Method: full read; math traced against closed forms; KLs Monte-Carlo
verified; log-det and derivative stencils checked by direct algebra.

## Confirmed

1. **`spm_nlsi_GN.m:500`** — `L(1) = spm_logdet(iS)*nq/2 - …`, but `iS` was
   Kronecker-expanded at line 421, so `spm_logdet(iS)` already equals
   `nq·logdet(iS_small)`: the log-det term is scaled by nq²/2 instead of nq/2.
   Internal-consistency proof: the M-step gradient (`ny/2`; generally
   `trace(PS)*nq/2`) is the derivative of the *corrected* term. Affects any
   inversion with multiple error-covariance blocks — `spm_dcm_erp`/`spm_dcm_ind`
   pass a single Ns×Ns component with multi-channel data, so nq =
   channels·trials > 1 — inflating the h-dependent part of F nq-fold and
   distorting model comparison. fMRI DCM (nq = 1) unaffected. **Moderate-high**
   (SP2; fix staged upstream).
2. **`spm_kl_wishart.m:38`** — KL(Q‖P) uses `LpP` = E_P[log|X|] where every
   expectation must be under Q (`LqQ`). Monte-Carlo (d=3, q=7, p=5): true KL
   6.560, coded 7.681, corrected 6.559. Only in-tree caller `spm_mix`:
   mixture-model evidence and component selection wrong whenever posterior and
   prior scale matrices differ. **Moderate-high** (SP12, with `spm_lg_gamma`).
3. **`spm_dcm_peb.m:593-600`** — the convergence test and `break` are nested
   inside `if verbose`; with verbosity off (batch pipelines) the loop always
   runs 64 Fisher-scoring iterations, so PEB.Ep/Eh/F differ between verbose
   and silent runs of identical data. Reproducibility defect. **Moderate.**
4. **`spm_nlsi_LS.m:208`** — `hE = hE*sparse(nh,1)` zeroes a scalar
   hyperprior (cf. `spm_nlsi_GN:278`, which uses `+`). **Low-moderate.**
5. **`spm_cat.m`** — the documented expansion of scalar-0 partitions is not
   implemented; the header's own example errors (loud). **Low.**

## Plausible

6. `spm_nlsi_LS.m:272` — Gibbs energy profiles the noise precision with
   `ns` (time bins) where the exponent should be `ny = ns·nr`; multi-response
   data under-weights the likelihood by nr.
7. `spm_fx_fmri.m:238-241` — `dfdu` applies the one-state chain rule to the
   two-state model; the erroneous term ∝ x(:,1) vanishes at the expansion
   point x = 0 where all in-tree consumers evaluate. Negligible today.
8. `spm_int_B.m:105-130` — `dJdu{j}*u(j)` should be `*(u(j) − u0(j))`:
   the initial input's Jacobian effect is double-counted when U.u(1,:) ≠ 0.
9. `spm_BMS_bor.m:87-95` — the family-null free energy uses softmax(L)
   weights rather than ∝ f0·exp(L); biased BOR with unequal family sizes
   (copied from the reference VBA implementation, which shares the property;
   the model-null branch is exact, making the two inconsistent).

## Verified correct

`spm_kl_normal`/`spm_kl_gamma`/`spm_kl_dirichlet` (MC to 3-4 decimals);
`spm_logdet`, `spm_inv`, `spm_pinv`, `spm_inv_spd`, `spm_sqrtm`, `spm_svd`,
`spm_orth`, `spm_vec`/`spm_unvec`; `spm_expm` Padé/scaling-squaring; `spm_dx`
augmented-exponential identity; `spm_diff`/`spm_ddiff` stencils (Taylor-
verified); `spm_fx_fmri` hemodynamics and full Jacobian (log-state chain
rules); `spm_gx_fmri` (Stephan 2007 k1/k2/k3 incl. derivatives); `spm_BMS`
(exact Stephan 2009 VB, Beta-CDF exceedance, Rigoux pxp); `spm_BMS_gibbs`,
`spm_dirichlet_exceedance`, `spm_compare_families`,
`spm_log_evidence(_reduce)` (BMR closed form); `spm_PEB` (ReML gradients and
F); `spm_dcm_peb` VL gradients (Friston 2016); bma/bmr/bmr_all/peb_bmc/
average/bpa; `spm_dcm_estimate`, `spm_dcm_fmri_priors`, `spm_peb_ppi`
(Gitelman deconvolution); `spm_softmax`, `spm_psi`; the `spm_int` family
aside from items 7-8.
