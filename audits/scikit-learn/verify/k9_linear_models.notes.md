# k9_linear_models — notes

Harness: `audits/scikit-learn/verify/k9_linear_models.py` (245 checks). Outputs: `k9_linear_models.out` (1.9.1),
`.v1.1.3.out`, `.v1.2.2.out`, `.v1.3.2.out`, `.v1.5.2.out`. Source read: scikit-learn main @ 857849927d
(`$S/sk/src`), installed releases under each venv for the version-specific behaviour.

Counts: 1.9.1 — 241 ok / 4 FAIL; 1.5.2 — 236 / 8; 1.3.2 — 235 / 9; 1.2.2 — 235 / 9; 1.1.3 — 233 / 8.
(The difference in totals comes from version-gated checks: `newton-cholesky` only from 1.2, the `multi_class` /
`penalty` deprecation checks, `lasso_path(sample_weight)` only where the signature has it.)

## FAIL lines

### 1. `Lars(n_nonzero_coefs=np.inf)` — docstring says "Use np.inf for no limit", validation rejects it
Measured: constructing/fitting `Lars(n_nonzero_coefs=np.inf)`. Library: `sklearn/linear_model/_least_angle.py`,
`Lars._parameter_constraints`: `"n_nonzero_coefs": [Interval(Integral, 1, None, closed="left")]`, so `np.inf`
(a float) raises `InvalidParameterError: The 'n_nonzero_coefs' parameter of Lars must be an int in the range
[1, inf). Got inf instead.` Documentation (same file, `Lars` docstring): "n_nonzero_coefs : int, default=500 —
Target number of non-zero coefficients. Use ``np.inf`` for no limit." Verdict: documentation/validation
inconsistency (bug): a documented value is refused since the parameter validation was added in 1.2. Builds:
FAIL on 1.2.2, 1.3.2, 1.5.2, 1.9.1; ok on 1.1.3 (no validation, the full path is returned and ends at OLS).

### 2. `LassoLarsIC.noise_variance_` — user guide says RSS/(n − p), code uses n − p − fit_intercept
Measured: default `noise_variance_` on a 50 × 6 problem with intercept: 0.251665 = RSS_OLS/43, whereas
RSS_OLS/(n − p) = RSS/44 = 0.245946. Library: `_least_angle.py`, `LassoLarsIC._estimate_noise_variance`:
`return np.sum((y - y_pred) ** 2) / (X.shape[0] - X.shape[1] - self.fit_intercept)`. Documentation: user guide
`doc/modules/linear_model.rst` (lasso_lars_ic): "σ² = Σ(y_i − ŷ_i)² / (n − p) where p is the number of
features". Verdict: documentation gap (the code's n − p − 1 is the correct unbiased estimator when an intercept
is fitted; the guide should say n − p − fit_intercept). The companion check "= RSS/(n − p − 1)" and the
`fit_intercept=False` check (= RSS/(n − p)) hold. All five builds.

### 3. `LassoLarsCV.mse_path_` documented shape "(n_folds, n_cv_alphas)", actual (n_cv_alphas, n_folds)
Measured: `LassoLarsCV(cv=KFold(3))` on 50 × 6 gives `mse_path_.shape == (19, 3)` with 19 `cv_alphas_`.
Library: `_least_angle.py`, `LarsCV.fit`: `mse_path = np.empty((len(all_alphas), len(cv_paths)))` … `mse_path[:,
index] = np.mean(this_residues, axis=-1)` … `self.mse_path_ = mse_path`. Documentation (`LassoLarsCV`, `LarsCV`
docstrings): "mse_path_ : array-like of shape (n_folds, n_cv_alphas) — the mean square error on left-out for
each fold along the path". Verdict: documentation bug (axes swapped in the docstring). The values themselves
agree with my plain-LARS + interpolation reference (max diff 1e-15). All five builds.

### 4. `HuberRegressor(tol=1e-12)` — documented projected-gradient stop is not what ends the iteration
Measured: `HuberRegressor(epsilon=1.35, alpha=0.01, tol=1e-12, max_iter=10000)` on 80 × 3 with 6 outliers
returns after `n_iter_ = 12` with max |∇| = 1.7e-3 (my own L-BFGS-B with `ftol=0, gtol=1e-12` reaches 6e-7 and
an objective lower by 5e-9 absolute, 3e-11 relative; parameters differ in the 6th–7th digit). Library:
`_huber.py`, `HuberRegressor.fit`: `optimize.minimize(_huber_loss_and_gradient, parameters, method="L-BFGS-B",
jac=True, ..., options={"maxiter": self.max_iter, "gtol": self.tol, ...})` — `ftol` is not set, so scipy's
default `ftol = 2.2e-9` (relative objective decrease) terminates first. Documentation: "tol : float, default=1e-05
— The iteration will stop when ``max{|proj g_i | i = 1, ..., n}`` <= ``tol``". Verdict: documentation gap /
minor behaviour issue — `tol` below ~1e-5 has no effect; the solution is still correct to ~1e-5 relative (the
main Huber check against my own optimum, the OLS equivalence, scale invariance and the `outliers_`/`scale_`
identities all hold at that tolerance). All five builds.

### 5. `BayesianRidge.predict(return_std=True)` did not centre X before using `sigma_` (fixed in 1.9)
Measured: `y_std` vs sqrt(1/α + (x − X_offset_) Σ (x − X_offset_)ᵀ) with Σ = `sigma_` = (λI + αX_cᵀX_c)⁻¹ on
the centred design; 1.9.1 matches; 1.1.3–1.5.2 instead match the formula with the *uncentred* x (the harness
prints "uncentred-x formula matches: True"). Library (1.5.2 `_bayes.py`, `BayesianRidge.predict`):
`sigmas_squared_data = (np.dot(X, self.sigma_) * X).sum(axis=1)` with raw X; main: `X = X - self.X_offset_`
before that line. Changelog v1.9: "|Fix| BayesianRidge and ARDRegression now center test features during
predict to correctly compute predictive variance (PR 33918)". Documentation: "y_std: Standard deviation of
predictive distribution of query points". Verdict: bug in 1.1.3, 1.2.2, 1.3.2, 1.5.2, fixed in 1.9.1
(the predictive variance was wrong whenever the training features had a non-zero mean).

### 6. `ARDRegression.predict(return_std=True)` — same centring bug (fixed in 1.9)
Same measurement over the kept (non-pruned) features; 1.5.2 `_bayes.py`, `ARDRegression.predict`:
`X = _safe_indexing(X, indices=col_index, axis=1); sigmas_squared_data = (np.dot(X, self.sigma_) * X).sum(axis=1)`
without subtracting `X_offset_`; main subtracts it. Verdict: bug fixed in 1.9 (PR 33918). Builds: FAIL on
1.1.3, 1.2.2, 1.3.2, 1.5.2; ok on 1.9.1.

### 7. `BayesianRidge` with `sample_weight` — hyper-parameter updates ignored the weights (fixed in 1.7)
Measured: `BayesianRidge(max_iter=5, tol tiny).fit(X, y, sample_weight=sw)` vs my replica of the documented
MacKay updates with the weighted problem (weighted centring, X and y scaled by √sw, α_init = 1/Var_w(y),
n replaced by Σsw in α = (n − γ + 2α₁)/(SSE + 2α₂)). 1.9.1 matches (α_ = 6.08728). Older builds give α_ =
4.64327, which my "legacy" replica reproduces exactly (α_init = 1/var(√sw·y_c) of the rescaled target and n =
number of rows). Library (1.5.2 `_bayes.py` `fit`): `X, y, _ = _rescale_data(X, y, sample_weight)` … `n_samples,
n_features = X.shape` … `alpha_ = 1.0 / (np.var(y) + eps)` … `alpha_ = (n_samples - gamma_ + 2 * alpha_1) /
(rmse_ + 2 * alpha_2)`; main uses `sw_sum = sample_weight.sum()` and the weighted variance. Changelog v1.7:
"|Fix| The update and initialization of the hyperparameters now properly handle sample weights in
BayesianRidge (PR 30644)". Documentation: "sample_weight : Individual weights for each sample". Verdict: bug in
1.1.3–1.5.2, fixed in 1.7. The consequence is the next line:

### 8. `BayesianRidge`: `sample_weight=2` != duplicated rows (1.1.3–1.5.2)
Measured: `coef_`, `alpha_`, `lambda_` of `fit(X, y, sample_weight=2·1)` vs `fit([X; X], [y; y])`. Same root
cause as 7 (n_samples = rows instead of Σsw, variance of the rescaled y). Verdict: bug, fixed in 1.7; ok on
1.9.1.

### 9. GLM `score(X, y, sample_weight)` — D² wrong with weights in 1.1.3, 1.2.2, 1.3.2 (fixed by 1.5.2)
Measured: `PoissonRegressor.score(X, y, sample_weight=sw)` = 0.7231 on the old builds vs the documented
D² = 1 − Σ sw d(y, μ)/Σ sw d(y, ȳ_w) = 0.1111 (1.5.2 and 1.9.1 return 0.1111). Library (1.3.2
`_glm/glm.py`, `_GeneralizedLinearRegressor.score`): `constant = np.mean(base_loss.constant_to_optimal_zero(
y_true=y))` then `constant *= sample_weight.shape[0] / np.sum(sample_weight)` — the per-sample constant that
turns the half-loss into the deviance is averaged without the weights, while `deviance` and `deviance_null`
are weighted means, so `1 - (deviance + constant)/(deviance_null + constant)` is wrong; 1.5.2 uses
`np.average(base_loss.constant_to_optimal_zero(y_true=y, sample_weight=None), weights=sample_weight)`.
Documentation: "D² = 1 − D(y_true, y_pred)/D_null … The mean ȳ is averaged by sample_weight." Verdict: bug in
1.1.3–1.3.2, silently fixed by 1.5.2 (no changelog entry found). Unweighted D² is correct on every build.

## What held up (all five builds unless noted)
- **ElasticNet/Lasso**: KKT of the documented objective at tol=1e-12 (violations ~1e-13) for four
  (alpha, l1_ratio) pairs, equality with a plain-numpy coordinate descent, intercept = ȳ − x̄ᵀw, `dual_gap_` =
  my primal−dual gap / n (Lasso), ElasticNet `dual_gap_` = formulation-A gap / n on all builds (both formulas
  coincide at convergence), `dual_gap_ ≤ tol·‖y_c‖²/n`, `l1_ratio=0` = ridge with penalty n·alpha, positive=True
  KKT, alpha=0 = OLS with the advisory warning, warm_start (0 extra iterations, then correct new optimum),
  precompute=True / user Gram, sample_weight = weighted objective with weights rescaled to sum n
  (sample_weight=2 == duplicates == single copy; integer weights == duplicated rows), sparse csr (with and
  without weights), float32 dtype, multi-output rows.
- **Path functions**: `lasso_path`/`enet_path`/`lars_path` fit *no intercept* and work on the raw data
  (their docstrings do not say so — a minor documentation gap, recorded as an ok line with the numbers);
  grid = max|Xᵀy|/(n·l1_ratio) geometric to eps·alpha_max, coef exactly 0 at alpha_max and non-zero at the next
  point, user alphas sorted decreasing, `positive=True` grid = max(0, max Xᵀy)/n from 1.7 (older: unsigned
  alpha_max, leading all-zero points — documented "alpha_max which results in coef=0" holds either way),
  `sample_weight` grid uses Σsw, path coefficients satisfy the KKT at every grid alpha.
- **LARS**: `lars_path(method='lar')` alphas (= max|Xᵀr|/n) and coefficients at every node equal a plain-numpy
  LARS written here, same active-set order, ends at OLS; `method='lasso'` (with a variable drop) equals my
  LARS-lasso; every lasso node satisfies the Lasso KKT; `LassoLars(alpha)` between nodes equals `Lasso(alpha)`
  by CD; `alpha_min` truncation/interpolation; `positive=True` satisfies the positive-Lasso KKT; `Lars(
  n_nonzero_coefs=2)`; `fit_intercept=False` = plain LARS on raw data; `LassoLars(alpha=0)` = OLS.
  (`normalize=False` is passed on 1.1.3 where the Lars family/OMP still defaulted to `normalize=True`.)
- **LassoLarsIC**: criterion_ = n log(2πσ²) + RSS/σ² + {2, log n}·df with df = number of non-zeros, argmin;
  noise_variance_ = RSS/(n−p−1) (see FAIL 2), = RSS/(n−p) without intercept; n ≤ p+1 raises.
- **LassoLarsCV / LarsCV**: `mse_path_` values = per-fold plain-LARS path interpolated at `cv_alphas_`
  (max diff 1e-15), alpha_ = argmin of the fold mean, refit = `LassoLars(alpha_)`, `cv_alphas_` = np.unique.
- **OMP**: greedy argmax|Xᵀr| + least squares on the active set for k = 1, 2, 3 (`n_iter_` = k), default
  k = max(int(0.1p), 1), `tol` stops at ‖r‖² ≤ tol with `n_nonzero_coefs_ = None`, precompute path, k = p = OLS,
  multi-target.
- **BayesianRidge**: 7 and 3 documented MacKay/Tipping updates replicated exactly (default and custom
  α/λ initial values and gamma hyper-parameters), converged fixed point, `sigma_` = (λI + αXᵀX)⁻¹,
  `predict(return_std)` (1.9.1), sample_weight replica (1.9.1), sample_weight=2 == duplicates (1.9.1),
  `scores_` length max_iter+1, n < p case.
- **ARDRegression**: 6 documented updates replicated (coef_, alpha_, per-feature lambda_, sigma_),
  threshold_lambda pruning (coef exactly 0, sigma_ over kept features), converged run = replica with the same
  stopping rule, `return_std` on 1.9.1, Woodbury branch n < p.
- **HuberRegressor**: minimiser of the documented objective (objective within 1e-8 of my own tight optimum),
  `outliers_` = |r| > ε·scale_, scale_ = √(Σ_in r²/(n − n_out ε²)), alpha=0 & huge ε = OLS with scale_ = RMS,
  scale invariance, weighted objective, sample_weight=2 == duplicates, ε < 1 raises.
- **QuantileRegressor (highs)**: for q = 0.5, 0.2, 0.9 the pinball loss equals the brute-force minimum over
  all lines through two data points and the quantile property #(r<0) ≤ qn ≤ #(r≤0) holds; alpha > 0 objective
  (1/n)ΣPB + alpha‖w‖₁ equals my own linprog formulation; sample_weight=2 == duplicates == single copy; zero
  weights drop rows; huge alpha → coef 0, intercept = median; sparse X.
- **GLMs**: Poisson/Gamma/Tweedie(1.5) with alpha=0 equal my Newton–Raphson MLE; penalised gradient of
  1/(2n)Σd + α/2‖w‖² vanishes (Poisson, Gamma, Tweedie 1.5, 3); score = D² with the documented unit deviances;
  power=1 == Poisson, power=2 == Gamma; power=0 = ridge with the 1/(2n) scaling and identity link (link auto);
  power=0 with log link; negative y / zero y raise; sample_weight = weighted average objective, sample_weight=2
  == duplicates == single copy; weighted D² (1.5.2, 1.9.1); newton-cholesky = lbfgs; no intercept.
  `TweedieRegressor(power=0.5)` fits silently on every build although the docs say no distribution exists
  (recorded as ok because no error is promised; the generic deviance is minimised).
- **SGD**: one-epoch/multi-epoch plain-Python replica of the Cython loop matches to 1e-10 for every regression
  loss × penalty (16 combinations), invscaling, optimal (Bottou t₀ heuristic, regressor and classifier),
  average=True and average=50, sample_weight, class_weight, all five classifier losses, OvA multiclass;
  `t_` = n_iter_·n + 1; predict_proba for log_loss and modified_huber; documented defaults (alpha=1e-4 …);
  penalty=None with small constant eta approaches OLS and penalty='l2' averaged approaches the 1/n·½(·)² +
  α/2‖w‖² minimiser within 1e-2.
- **PassiveAggressive / Perceptron**: PA-I/PA-II one-step updates from zero (τ = min(C, loss/‖x‖²), τ =
  loss/(‖x‖² + 1/(2C)); the intercept is updated by the same τ and is *not* part of ‖x‖²), passive second
  step, regressor with ε-insensitive loss, Perceptron 2-epoch replica and one-step update.
- **RANSAC**: default min_samples = p+1, residual_threshold = MAD, inlier_mask_/n_trials_/estimator_ equal a
  plain re-implementation of the documented loop (3 seeds/configurations incl. relative min_samples,
  stop_probability, max_trials, stop_n_inliers); refit on the consensus set; N = ceil(log(1−p)/log(1−eᵐ)) bound;
  squared_error ≡ absolute_error with the squared threshold; residual == threshold is an inlier.
- **TheilSen**: 1-D no-intercept = median of slopes; 12 × 2 with intercept = spatial median of all C(12,3)
  subset fits by my own Weiszfeld iteration (and its distance sum is minimal); breakdown_ formula;
  n_subsamples = n = OLS; max_subpopulation.
- **RidgeCV**: LOO closed form equals an explicit leave-one-out loop (single target, multi-target with and
  without alpha_per_target incl. `cv_results_` shapes, fit_intercept=False, gcv_mode svd/eigen, n < p);
  scoring=None → −MSE; scoring='r2' → alpha by R² of the LOO predictions (cv_results_ holds predictions in the
  original y scale on 1.9.1, in the centred-y scale on ≤1.5.2 — "standardized per point prediction values" is
  loose but not wrong); sample_weight: cv_results_[i] = sw_i·e_i² of the weighted LOO; cv=KFold → R² per fold;
  store with cv != None raises.
- **LassoCV / ElasticNetCV**: alphas_ grid from the full centred data; `mse_path_` = fold MSE of my plain CD
  at each grid alpha (max diff ~1e-9), alpha_/l1_ratio_ = argmin, refit; user alphas sorted; positive.
- **MultiTask**: row-wise L21 KKT for MultiTaskLasso and MultiTaskElasticNet (violations ~1e-13), joint row
  sparsity, single task = Lasso, alpha_max = max_j ‖(X_cᵀY_c)_j‖₂/n.
- **Ridge solvers**: svd, cholesky, lsqr, sparse_cg, sag, saga equal the closed form (dense and sparse);
  lbfgs with positive=True satisfies the NNLS KKT; positive=True with solver='auto' works.
- **LogisticRegression**: KKT of (1/S)Σ s_i logloss + r(w)/(SC) for l2 (lbfgs, newton-cg, newton-cholesky, sag,
  saga, liblinear), l1 (saga, liblinear), elasticnet (saga) — liblinear checked with the intercept penalised
  through the synthetic feature (intercept_scaling 1 and 5); penalty=None MLE; sample_weight and
  class_weight × sample_weight; sample_weight=2 == duplicates == C doubled; multinomial KKT with 4 solvers
  (newton-cholesky is OvR before 1.6 as then documented, verified row-wise); liblinear multiclass raises from
  1.8 / OvR before; multi_class deprecation (1.5–1.7) / removal (1.8+); penalty deprecation (1.8+); warm_start;
  predict_proba/log_proba; sparse saga; fit_intercept=False.
- **LogisticRegressionCV**: Cs_ = logspace(−4, 4, Cs); scores_ = my per-fold accuracies of LogisticRegression
  on each StratifiedKFold(4) training fold; refit=True → C_ = argmax of the fold mean and coef_ = refit on all
  data; refit=False → mean of the fold-best Cs and of the fold coefficients; scoring='neg_log_loss'; multiclass
  scores_ repeated per class; coefs_paths_ shape.

## Not checked, and why
- `RANSACRegressor`, `TheilSenRegressor`, `LassoCV`/`RidgeCV` under "sample_weight == duplicated rows": the
  random subsampling / CV folds make duplication and weighting legitimately different procedures, so there is no
  documented equivalence to test; `SGD*` likewise (the weight multiplies the update of one visit, a duplicate
  is visited twice).
- `Lars`/`LassoLars`/`OMP`/`ARDRegression`/`MultiTask*` have no `sample_weight` parameter.
- `SGDClassifier` `early_stopping`/`adaptive` schedule and `n_iter_no_change` were not replicated (they depend
  on the internal validation split); only the documented formulas for constant/invscaling/optimal were.
- The `optimal` schedule's t₀ heuristic is "documented" only in the code (`typw = sqrt(1/sqrt(alpha))`, …); the
  check records that formula and is not a documentation check.
- `RidgeCV` with `sample_weight` and a scorer, and `alpha_per_target` with `cv != None`, were not exercised.
- LogisticRegressionCV with `l1_ratios` (elasticnet grids) was not exercised because 1.9.1 changes the attribute
  layout (`use_legacy_attributes`) and the older builds need `penalty='elasticnet'`; the l2 grid covers the
  documented mechanics.
- Solver-tolerance limits: lbfgs-based fits (LogisticRegression on 1.3.2, GLMs on 1.1.3) stop at KKT violations
  of ~1e-7–1e-6 regardless of `tol`, so the KKT thresholds are 1e-5 (logistic) and 1e-6 (GLM); these are far
  below the coefficient scale and do not hide a wrong optimum.
