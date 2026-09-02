# Component review: active inference / MDP code

Scope: `toolbox/DEM/spm_MDP_VB*.m`, `spm_MDP_check`, `spm_MDP_G`,
`spm_MDP_size`, sleep/prune routines; root tensor and information-theory
helpers (`spm_MDP_MI`, `spm_KL_cat`/`spm_KL_dir`, `spm_dir_*`, `spm_cross`,
`spm_dot`, `spm_sdot`, `spm_marginal`, `spm_psi`, `spm_softmax`, `spm_log`,
`spm_kron`, `spm_combinations`, `spm_speye`).
Method: full read; tensor helpers transcribed to numpy and tested against
direct einsum for multiple dimension patterns; information-theory routines
checked against closed forms and Monte Carlo (`../reproductions/audit.py`).

## Confirmed

1. **`spm_MDP_MI.m`** — the Dirichlet gradient `dEda = dEdA.*(1-A)/s` applies
   an elementwise correction where the chain rule through the normalisation
   needs the *scalar* projection `(dEdA − <dEdA,A>)/s`. Numerically: 50-100%
   relative error and wrong sign pattern vs the numerical gradient; the
   projected form matches to 1e-10. Consumer `spm_MDP_VB_prune` ('MI' branch)
   builds reduced priors `rA = pA.*exp(pA.*dEdA)` from the second output, so
   Bayesian model reduction / sleep / structure learning moves priors along a
   wrong direction. **High** for BMR-based structure learning (SP10).
2. **`spm_MDP_VB_X.m:940-946`** — the B-novelty term indexes the *action*
   dimension of `wB{m,f}` with the policy index k (the action prescribed by
   policy k at time j is `V{m}(j,k,f)`, used correctly elsewhere in the file);
   the guard silently drops the term for policies numbered above Nu; and the
   contraction is transposed (`x_j' W x_{j+1}` for `x_{j+1}' W x_j`, W not
   symmetric). The newer `spm_MDP_VB_XXX` indexes correctly. Wrong policy
   values G whenever `b` is learned with a nontrivial policy→action mapping.
   **Moderate-high** (SP9).
3. **`spm_MDP_VB_X.m:1184` and `spm_MDP_VB_XX.m:997`** — `Fc(f)` written with
   a stale factor index inside a loop over modalities g (all modalities
   overwrite one element), and `pC{g}` should be `pC{m,g}` (column-major
   mis-retrieval for multi-agent runs). Output statistic only. **Low-moderate.**
4. **`spm_MDP_VB_XX.m:1173-1179`** (`spm_forwards`) — predicted outcomes at
   t+1 are scored against preferences `C(:,t)`; the recursion preserves the
   one-step lag and `C(:,T)` is never used. Wrong whenever preferences are
   time-varying (e.g. reward-at-final-step tasks). `spm_MDP_VB_X` aligns them
   correctly. **Moderate.**
5. **`spm_MDP_VB_XX.m:828-831`** — a scalar is assigned into `S(m,f)`, but `S`
   is the cell array of state posteriors: "Conversion to cell from double"
   crash. The `factor` field triggering this is set by VB_XX itself for every
   subordinate model in hierarchical/link mode — deep models crash. Loud.
   **High as a broken feature** (part of SP20).
6. **`spm_cross.m`** — strips *interior* singleton dimensions
   (`siz = siz(siz>1)`). With state factors like Ns=[3,1,4] (passes
   `spm_MDP_check`), the a-learning update builds `da` with shape [No,3,4]
   against `a{g}` of [No,3,1,4]; implicit expansion silently reshapes the
   concentration tensor with wrong counts that propagate across trials.
   **Moderate.**
7. **`toolbox/DEM/spm_MDP_size.m:31`** — `size(a{1},2:ndims(A))`: `A` undefined (case
   typo for `a{1}`); the likelihood-only fallback path (models with `a` but no
   `b`/`B`) always crashes. (Part of SP20.)
8. **`spm_MDP_VB.m:475`** — habit exclusion `p(1:end-1)` assumes the habit is
   last in `p`, but `p` was pruned by the Occam window; if the habit was
   eliminated, the highest-numbered *real* policy is dropped instead and its
   action never gets a utility (unselectable after `spm_softmax(alpha*P)`).
   **Moderate.**

## Plausible

9. `spm_MDP_VB_XX` `spm_MDP_get_T` (1349-1355) — an `MDP.V` input collapses
   the policy space to 1 and two-subscript indexing into the 3-D array reads
   wrong action indices.
10. `spm_MDP_VB_XX.m:1052-1060` — `xn` normalisation applies only to the last
    factor (display outputs only).
11. `spm_MDP_VB_sleep.m` REM branch — `MDP.a0{g} = REM(N).a0` nests the whole
    cell array; the next sleep cycle fails.
12. `spm_MDP_VB_X.m:741` (VOX) — `sB{m,f}(:,:)` flattens Ns×Ns×Nu; the
    dimension mismatch is swallowed by a bare `try`.

## Verified correct

`spm_KL_dir` (closed-form Dirichlet KL to 1e-13), `spm_KL_cat`, `spm_dir_H`
(scipy dirichlet entropy), `spm_dir_MI` internals, `spm_MDP_G` (exact
outcome-state mutual information), `spm_dot` (all tested patterns: 4-way
tensors, factor omission, vector mode, DIM bookkeeping), `spm_kron`/
`spm_combinations` ordering vs the column-major conventions in VB_XX,
`spm_softmax`, `spm_psi`, `spm_log`, `spm_dir_norm`, `spm_marginal`,
`spm_sdot`, `spm_MDP_log_evidence` (Dirichlet BMR identity), and the
`spm_wnorm` sign conventions in VB_X/VB_XX (the differing positive-valued
`spm_wnorm` in VB_XXX is self-consistent with its `+` signs).
