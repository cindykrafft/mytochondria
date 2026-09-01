# Component review: GLM estimation core & design specification

Scope: `spm_spm`, `spm_est_non_sphericity`, `spm_reml*`, `spm_Ce`/`spm_Q`,
`spm_filter`/`spm_dctmtx`, `spm_hrf`/`spm_get_bf`/`spm_get_ons`/
`spm_Volterra`/`spm_fMRI_design`, `spm_SpUtil`/`spm_FcUtil`/`spm_sp`/
`spm_DesMtx`, design/contrast helpers, `spm_ancova`, `spm_orth`,
`spm_fmri_concatenate`, `spm_non_sphericity`/`spm_get_vc`.
Method: full read; linear algebra traced (trRV/trRVRV identities, Hsqr
projections, ReML gradients, DCT filter construction, microtime sampling,
Kronecker orderings — all verified); failures below reproduced numerically.

## Confirmed

1. **`spm_design_contrasts.m:61-66`** — parametric-modulator padding inserts
   `sum(h)` zero columns where the design carries `sum(h)*nbases` (every `U.u`
   column — main effect *and* each modulator column — is convolved with all
   basis functions in `spm_Volterra`). With `nbases > 1` plus any modulation,
   every subsequent condition's automatic-contrast weights shift onto the
   wrong regressors; the final `con(c).c(:,end+1:k)=0` pad hides the length
   mismatch, so no error is raised. Reproduced: 2 conditions × 2 bases + one
   modulator puts the main-effect −1 on `cond1×mod·bf2` instead of `cond2·bf1`.
   Auto-created by `spm_run_fmri_est` whenever `SPM.factor` is set. **High**
   (SP5; fix staged upstream).
2. **`spm_orth.m:31-57`** — 'pad' mode collects column indices on the
   zero-stripped matrix but applies them at original width: an all-zero column
   ahead of non-zero ones shifts later regressors into the wrong (named)
   columns. Triggered via `spm_get_ons.m:115` / `spm_fMRI_design.m:240` by an
   all-zero parametric modulator in one session. Reproduced. **Moderate.**
3. **`spm_SpUtil.m:302`** — `'ConO'` tests orthogonality in `X'X` where its
   own documentation (and `'ConR'`) require `pinv(X'X)`; also an absolute,
   scale-dependent tolerance. Latent (no in-tree caller). **Low.**
4. **`spm_reml_A.m:123`** — `P*(A*Q' + Q'*A)`: the second term should be
   `Q*A'`. Identical for symmetric components, wrong for the asymmetric ones
   the routine ostensibly supports (numerically: coded gradient (73.6, −4.7)
   vs true (27.4, −16.6)). Latent. **Low-moderate.**
5. **`spm_FcUtil.m:243`** — the `'ukX0'` set-action reads a never-assigned
   variable: unconditional crash (loud). **Low.**

## Plausible

6. `spm_contrasts.m:273` — `trMV` stale/undefined in the F branch when `eidf`
   is pre-filled but `Vspm` empty; the standard flow always computes both
   together.
7. `spm_non_sphericity.m:109-113` — a single dependence component (e.g. a
   paired design via the legacy path) is silently replaced with i.i.d.
   sphericity; dfs overstated. Modern `spm_get_vc` path handles it correctly.
8. `spm_get_ons.m:126-127` — every epoch is one microtime bin (`RT/16`) longer
   than specified; longstanding canonical behaviour, only material for
   sub-second durations at long TR.

## Verified correct

`spm_SpUtil` trRV/trRVRV/trMVMV Frobenius identities; `spm_spm`'s `KWVW'K'`
assembly, erdf and Bcov; `spm_filter`/`spm_dctmtx` cutoff-order formula and
derivatives (numerically checked); `spm_hrf` parameterisation and microtime
subsampling; `spm_fMRI_design`'s `(0:k−1)·T + T0 + 32` sampling; `spm_reml`/
`spm_reml_sc` gradients/curvatures and rescaling; `spm_get_vc` Kronecker/Igen
ordering; `spm_make_contrasts`; `spm_ancova`; `spm_FcUtil` Hsqr projection;
`spm_fmri_concatenate` filter/Vi rebuild.
