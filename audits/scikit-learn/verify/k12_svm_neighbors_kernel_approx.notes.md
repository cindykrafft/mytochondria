# k12_svm_neighbors_kernel_approx — notes

Harness: `audits/scikit-learn/verify/k12_svm_neighbors_kernel_approx.py`; outputs `k12_svm_neighbors_kernel_approx.out`
(1.9.1 / numpy 2.4.6 / scipy 1.17.1) and `.v1.1.3.out`, `.v1.2.2.out`, `.v1.3.2.out`, `.v1.5.2.out`.

Counts: 1.9.1: 302 ok / 24 FAIL; 1.5.2: 294 ok / 23 FAIL; 1.3.2: 294 ok / 23 FAIL; 1.2.2: 292 ok / 23 FAIL;
1.1.3: 286 ok / 21 FAIL. No section crashed on any build. Runtime about 5 s per build.
Fewer checks on older builds: `dual='auto'` (1.3+), NearestCentroid `priors` / `deviations_` (1.6+),
KernelDensity `'scott'` / `'silverman'` (1.2+), the `probability` deprecation warning (1.9+).
The one FAIL present only on 1.9.1 is the NearestCentroid `priors` docstring (1.6+ only); the two KernelDensity
scaling FAILs are absent on 1.1.3 because the option does not exist there. Every other FAIL is identical on all five
builds, with the same measured numbers.

Built from a partial harness left by an earlier attempt. Every expectation was re-derived. Changes to that draft:
- Each section now draws from its own `RandomState`. In the draft one shared stream was consumed by version-guarded
  code, so the LinearSVR data differed between 1.1/1.2 and 1.3+ and results could not be compared across builds.
- Each section runs inside a crash guard, as in k11.
- Harness bugs fixed:
  - NCA: the draft overwrote `nca.n_iter_ = 1` before comparing it.
  - KernelDensity: Scott and Silverman were tested only in d = 2, where `(d+2)/4 = 1` makes the two rules identical.
  - Nystroem: a "positive semidefinite sigmoid Gram matrix" premise that was false (its minimum eigenvalue was
    -2e-4).
  - The random-projection inverse was gated on 1.4, but `compute_inverse_components` is `versionadded:: 1.1`.
  - SVR KKT tolerance of 1e-7: libsvm caches the kernel as `float`.
  - OneClassSVM counted boundary points (decision value about 0) as training errors.
  - A LinearSVR "intercept_scaling changes the intercept" check that is not guaranteed for a piecewise-linear
    loss. It is replaced by an exact reference at intercept_scaling = 50.
  - The draft's L-BFGS-B box-dual reference can stall. On one data set (seed 51) its duality gap was 1.4, not 0.
    The scan now uses an SLSQP primal QP with slack variables as the reference.
- The draft's `johnson_lindenstrauss_min_dim` check encoded the implementation (floor). The documented inequality is
  now checked as well.

## FAIL lines

### `SVC(sample_weight with zeros): support_ indexes the rows of the X passed to fit ...` (all builds)

**Measured:** SVC(rbf, gamma=0.7, C=1.5) with `sample_weight = 0` on rows [2, 5, 11, 17, 23] of 30. The decision
function equals the fit with those rows removed (ok line). But `support_` = [6, 8, 11, 12, 14, 16, 20, 22, 3, 4, 5,
10, 19, 21, 23] contains 5, 11 and 23, which have zero weight. `support_vectors_ == X[support_]` is False, and
`support_vectors_ == X[rows with nonzero weight][support_]` is True.

**What the library does:** libsvm's `svm_train` calls `remove_zero_weight(&newprob, prob)`
(`sklearn/svm/src/libsvm/svm.cpp`), which compacts the problem to the rows with `W[i] > 0`. `model->sv_ind[p] = perm[i]`
then records positions in that compacted problem. sklearn returns `sv_ind` as `support_` without mapping it back to
the original row numbers.

**What the documentation says:** "support_ : ndarray of shape (n_SV) Indices of support vectors."

**Verdict:** bug. `support_` indexes the wrong array whenever any sample weight is 0. Probably the issue whose title
reads "SVC and OneClassSVM fails to fit or have wrong fitted attributes with null sample weights" (#25380, open,
seen by title only).

### `SVC(kernel='precomputed', sample_weight with zeros) decision_function = the same fit with kernel='rbf' ...` (all builds)

**Measured:** the rbf Gram matrix passed as `kernel='precomputed'`, with the same zero weights, gives decision values
[1.75, 1.52, -0.84, 1.90, -0.70, -0.85, -0.44, -0.89]. The `kernel='rbf'` fit on the same weights, which equals the
dropped-rows fit, gives [-0.60, -0.86, 0.94, -0.65, 0.84, 0.47, 0.10, 1.48]. All 8 predicted labels differ.

**What the library does:** this is a consequence of the `support_` bug above. Training is correct, because each node
keeps its original column index (`node[i].ind = i`, `libsvm_helper.c`), and the kernel is
`case PRECOMPUTED: return x->values[y->ind];`. At predict time `model->SV[i].ind = support[i]`
(`libsvm_helper.c`, `set_model`), so the test-kernel columns are chosen by positions in the compacted problem, which
are the wrong columns.

**What the documentation says:** sample weights "Rescale C per sample". Nothing warns that zero weights are
incompatible with `precomputed`.

**Verdict:** bug. The predictions are silently wrong, which makes this the most serious finding in this group.

### `SVC(probability=True) binary predict_proba[:, 0] = 1/(1+exp(probA_ * d + probB_)) ...` (all builds)

**Measured:** over 900 grid points, `predict_proba` deviates from the Platt sigmoid built from `probA_`, `probB_` and
the decision value by up to 3.9e-3. The next check reproduces `predict_proba` to 1e-10 by feeding the 2x2 table
`[[0, s], [1-s, 0]]` to libsvm's Wu–Lin–Weng pairwise-coupling iteration, which stops at `max_error < 0.005/k`
(ok line).

**What the library does:** `svm_predict_probability` (`svm.cpp`) always calls
`multiclass_probability(nr_class, pairwise_prob, prob_estimates)`, including when `nr_class == 2`. For k = 2 the exact
coupling solution is the sigmoid itself: minimising `(r10 p0 - r01 p1)^2` subject to `p0 + p1 = 1` gives `p0 = r01`.
The early-stopped iteration leaves an error of up to about 0.005/2.

**What the documentation says:** `probB_`: "Platt scaling uses the logistic function
`1 / (1 + exp(decision_value * probA_ + probB_))`". The `probA_` entry of `SVC` breaks off mid-sentence after
"uses the logistic function" (a small docstring glitch). In 1.9, `probability` and `probA_`/`probB_` are deprecated.

**Verdict:** documentation gap, not a numerical bug. The documented formula holds only to within the coupling
tolerance (up to 4e-3).

### `NuSVC(class_weight={3: 1, 7: 5}) changes the fit ...` (all builds)

**Measured:** max |decision difference| from the unweighted fit is 0.00e+00. `sample_weight = 2` on class 7 does
change the fit (difference 0.72).

**What the library does:** `svm_train` computes `weighted_C[j] *= param->weight[i]` and passes it to
`svm_train_one(&sub_prob, param, weighted_C[i], weighted_C[j], ...)`. There, `case NU_SVC:` calls
`solve_nu_svc(prob, param, alpha, &si, blas_functions)` and ignores `Cp`/`Cn`. `solve_nu_svc` uses only
`C[i] = prob->W[i]`, the per-sample weights.

**What the documentation says:** the NuSVC docstring: "class_weight : {dict, 'balanced'} Set the parameter C of class
i to class_weight[i]*C for SVC."

**Verdict:** bug, or at least a documentation bug: a documented parameter is silently ignored. Matches the open issue
titled "NuSVC argument `class_weight` is not used" (#30332, seen by title only).

### `OneClassSVM offset_ is a Python/numpy scalar as documented ('offset_ : float')` (all builds)

**Measured:** `offset_` is `array([1.39345727])`, of shape (1,).

**What the library does:** `_classes.py`, `OneClassSVM.fit`: `self.offset_ = -self._intercept_`, and `_intercept_`
has shape (1,).

**What the documentation says:** "offset_ : float". The documented relations `decision_function = score_samples -
offset_` and `offset_ = -intercept_` hold (ok lines).

**Verdict:** documentation gap, a minor type mismatch. Other outlier detectors (IsolationForest, LOF) store a float.

### The three liblinear stall lines (all builds, identical numbers)

The lines are:
- `LinearSVR(epsilon_insensitive) / LinearSVC(hinge) with tol=1e-12, max_iter=200000 reach the optimum ... on all of
  60 random data sets`
- `LinearSVR(epsilon_insensitive) on data set 32: every tol in 1e-8 ... 1e-14 ...`
- `LinearSVC(hinge) on data set 14: every tol in 1e-8 ... 1e-14 ...`

**Measured:** 60 random data sets are fitted at `tol=1e-12`, `max_iter=200000`. Each is compared with an SLSQP
solution of the primal QP with slack variables. Results:
- LinearSVR does not reach the optimum on 1 of 60 (seed 32: excess primal 0.0169).
- LinearSVC(hinge) does not reach it on 2 of 60 (seed 14: excess 0.0438; seed 16: excess 0.0048).
- All three fail runs hit `n_iter_ = 200000` with a ConvergenceWarning.

The tolerance sweep on seed 32 shows:

| tol | n_iter_ | excess primal |
|---|---|---|
| 1e-8 | 865 | 4.5e-9 |
| 1e-10 | 974 | 1.3e-11 |
| 1e-11 | 1028 | 3.1e-12 |
| 1e-12 | 200000 | 1.69e-2 |
| 1e-14 | 200000 | 1.69e-2 |

The solver sits at a fixed, non-optimal point:
- On seed 32 the excess is the same at `max_iter = 1000` and 200000.
- On the draft's data set (a probe outside the harness) the objective at tol = 1e-12 was 4.91105262 for every
  `max_iter` from 300 to 200000, and for 4 of 5 `random_state` values. The optimum was 4.88029214. The LinearSVC seed 14 sweep has the same shape: 1e-11 converges at 1904
iterations with excess 5e-12; 1e-12 gives excess 0.0438.

**What the library does:** `solve_l2r_l1l2_svr` and `solve_l2r_l1l2_svc` (`sklearn/svm/src/liblinear/linear.cpp`) are
dual coordinate descent with shrinking. Three features of that code combine:
- Coordinates are skipped when `if(fabs(d) < 1.0e-12) continue;`.
- The stopping test is `Gnorm1_new <= eps*Gnorm1_init`, where `Gnorm1_new` is summed over the *active* (unshrunk) set.
- Shrunk variables are only re-activated (`active_size = l`) after that test passes.

With `eps = 1e-12` the remaining violations on the active set can stay above `eps*Gnorm1_init` while every step is
below the 1e-12 skip threshold. The loop then never unshrinks, and the shrunk variables that would need to move are
never revisited. This mechanism is inferred from reading the code, not instrumented. The observed fixed point that is
independent of `max_iter` fits it.

**What the documentation says:** `tol`: "Tolerance for stopping criteria." `max_iter`: "The maximum number of
iterations to be run." A ConvergenceWarning is raised.

**Verdict:** solver bug in the upstream liblinear logic, affecting only very tight tolerances. At tol <= 1e-12 a
tighter tolerance can return a worse model (up to 0.8% above the optimum here) than tol = 1e-11. It is flagged only
by the ConvergenceWarning. The default tol = 1e-4 is not affected in this way. It is related to the open issue titled
"LinearSVC with hinge loss and L2 penalty, solver='liblinear' seems to get stuck compared to other solvers" (#22283,
seen by title only).

Separately, the scan showed that some data sets simply need many iterations: seed 29 needs 7400 and seed 37 needs
38500 at any tol <= 1e-8. They reach the optimum with the large max_iter. With the default `max_iter=1000` they stop
with a ConvergenceWarning at an excess of about 4e-4 and 8e-6.

### `NearestNeighbors kneighbors on X + 1e+06 (all three algorithms) = exact neighbours of X, distances within 1e-6` (all builds)

**Measured:** data in [0, 1]^2, shifted by a constant. The distances that `algorithm='brute'` returns err by:
- 4.6e-7 at offset 1e4;
- 3.1e-3 at offset 1e6, which is 1–3% of the distances;
- `kd_tree` and `ball_tree` err by 1.6e-12 and 1.25e-10, the float64 rounding of the shifted data.

Neighbour indices were still correct on this data.

**What the library does:** brute-force Euclidean k-NN uses the expanded form `||x||^2 - 2 x.y + ||y||^2`, in
`ArgKmin` / `euclidean_distances`. With norms of about 1e12 this cancels catastrophically.

**What the documentation says:** `euclidean_distances` warns: "this is not the most precise way of doing this
computation, because this equation potentially suffers from 'catastrophic cancellation'". The neighbors estimators
and the user guide say nothing about it.

**Verdict:** documented limitation of the underlying formula, and a documentation gap for the neighbors API. Users
with large offsets should centre their data or use a tree algorithm.

### The cosine-kernel lines (all builds)

The lines are:
- `KDTree/BallTree.kernel_density(cosine, 2-D) = ...`
- `cosine kernel normalisation in d=2 ...` and `in d=4 ...`
- `KDTree.kernel_density(cosine, 4-D) = exact ...`
- `KernelDensity(kernel='cosine').score_samples = log of the normalised cosine KDE ...`

**Measured:** `sklearn.neighbors._kd_tree.kernel_norm(1, d, 'cosine')` compared with the exact value
`1 / (S_{d-1} (2h/pi)^d ∫_0^{pi/2} u^{d-1} cos u du)` (mpmath):

| d | library | exact |
|---|---|---|
| 1 | 0.785398 | 0.785398 |
| 2 | 0.25 | 0.687985 |
| 3 | 0.659873 | 0.659873 |
| 4 | nan | 0.683859 |
| 5 | 0.758166 | 0.758166 |

- 2-D `kernel_density`: 1.0404 against 2.8632 exact, a ratio of 0.3634 = 0.25/0.688.
- 4-D `kernel_density`: nan against [3.08, 5.61, 3.44].
- `KernelDensity(kernel='cosine').score_samples` in 2-D is wrong by the same factor.
- All five other kernels match in d = 1..5 to 1e-10, and cosine matches in odd d.

**What the library does:** `_log_kernel_norm` in `sklearn/neighbors/_binary_tree.pxi.tp`:
```
elif kernel == COSINE_KERNEL:
    # this is derived from a chain rule integration
    factor = 0
    tmp = 2. / PI
    for k in range(1, d + 1, 2):
        factor += tmp
        tmp *= -(d - k) * (d - k - 1) * (2. / PI) ** 2
    factor = log(factor) + logSn(d - 1)
```
This is the integration-by-parts expansion of I_{d-1} = ∫_0^{pi/2} u^{d-1} cos u du using
I_n = (pi/2)^n - n(n-1) I_{n-2}. The expansion terminates at I_0 = 1 for odd d. For even d it terminates at
I_1 = pi/2 - **1**, and the loop drops the "-1" boundary term.
- d = 2: factor = 2/pi, but the correct value is 2/pi - 4/pi^2. The norm is 1/(2/pi · 2pi) = 0.25 instead of 0.688.
- d = 4: factor = 2/pi - 6(2/pi)^3 < 0, so `log` returns nan.

**What the documentation says:** the user guide lists the cosine kernel `K(x; h) ∝ cos(pi x / 2h)` if x < h.
`KernelDensity.score_samples` returns "Log-likelihood of each sample in `X`. These are normalized to be probability
densities".

**Verdict:** bug. The cosine kernel density is wrong in every even dimension: too small by a factor that depends on d
(0.363 in 2-D), and nan in 4-D, 6-D and so on. No open issue was found by title search.

### `NearestCentroid default class_prior_ = class proportions ...` (1.9.1 only; `priors` is 1.6+)

**Measured:** default `class_prior_` is [1/3, 1/3, 1/3]. The class proportions are [4/15, 5/15, 6/15].

**What the library does:** the signature has `priors="uniform"`, and `fit` sets
`self.class_prior_ = np.asarray([1 / n_classes] * n_classes)`.

**What the documentation says:** `priors : {"uniform", "empirical"} or array-like ..., default="uniform". The class
prior probabilities. By default, the class proportions are inferred from the training data.` The docstring contradicts
itself.

**Verdict:** documentation bug. The second sentence describes `"empirical"`, not the default.

### `NCA n_iter_ 'counts the number of iterations performed by the optimizer' = number of callback invocations` (all builds)

**Measured:**
- The callback was invoked 47 times, with iteration numbers 1..47 (ok line).
- scipy's own L-BFGS-B on the same objective reports `nit = 47` and 47 callbacks.
- `n_iter_` = 48.

**What the library does:** `_nca.py`. `fit` sets `self.n_iter_ = 0`. `_loss_grad_lbfgs` starts with
`if self.n_iter_ == 0: self.n_iter_ += 1`, which is there for the verbose header. `_callback` then does
`self.n_iter_ += 1` after each iteration. The first function evaluation therefore adds one count that is not an
iteration.

**What the documentation says:** "n_iter_ : int Counts the number of iterations performed by the optimizer."

**Verdict:** bug, off by one and minor.

### `KernelDensity(bandwidth='scott'/'silverman'), d=1 / d=3: data multiplied by 10 -> bandwidth_ multiplied by 10` (1.2.2 and later; the option does not exist in 1.1.3)

**Measured:** on data standardised to unit sample variance, `bandwidth_` equals the factors below exactly (ok lines):
- Scott: n^(-1/(d+4)).
- Silverman: (4/(d+2))^(1/(d+4)) n^(-1/(d+4)).

On the same data times 10, `bandwidth_` is unchanged (0.4670 and 0.4947 in 1-D), while the rules give 4.670 and 4.947.

**What the library does:** `_kde.py`, `fit`: `self.bandwidth_ = X.shape[0] ** (-1 / (X.shape[1] + 4))` for Scott,
and `(X.shape[0] * (X.shape[1] + 2) / 4) ** (-1 / (X.shape[1] + 4))` for Silverman. There is no data-scale factor.
scipy's `gaussian_kde` multiplies the same factor by the data covariance.

**What the documentation says:** user guide: "use Scott's and Silverman's estimation methods". Scott (1992) gives
h_j = sigma_j n^(-1/(d+4)), and Silverman (1986, eq. 4.14) applies to data scaled to unit variance. The docstring
gives no formula.

**Verdict:** bug, or at least a documentation gap. `bandwidth_` is right only for unit-variance data. Matches the open
issue titled "Automatic bandwidth calculation valid only for normalized data" (#26658, seen by title only).

### `Nystroem(kernel='sigmoid', n_components=n_samples): ... = K exactly` and `Nystroem(kernel='sigmoid', n_components=6): Z Z^T = K[:, m] pinv(K[m, m]) K[m, :]` (all builds)

**Measured:**
- sigmoid(gamma=0.3, coef0=0.2) on 20 points in [0, 1]^3: the Gram matrix is indefinite (minimum eigenvalue
  -0.0216), and `Z Z^T` differs from K by 6.3e-3.
- `Z Z^T` equals |K| = Q|Λ|Q^T to 5.5e-13 (ok line).
- On data with a positive-definite sigmoid Gram matrix, Nystroem reproduces K to 4e-16 (ok line).
- rbf, poly, chi2 and precomputed match exactly, and `K_nm pinv(K_mm) K_mn` holds for them.

**What the library does:** `kernel_approximation.py`, `Nystroem.fit`: `U, S, V = svd(basis_kernel);
S = clip(S, 1e-12, None); normalization_ = U / sqrt(S) @ V`. For a symmetric indefinite K11 = QΛQ^T this gives
Q|Λ|^{-1/2} sign(Λ) Q^T, so Z Z^T = K_n1 |K11|^{-1} K_1n. The result is the matrix absolute value, not K11^{-1}.

**What the documentation says:** docstring: "Constructs an approximate feature map for an arbitrary kernel". User
guide: the feature map gives K21 K11^{-1} K21^T, with `normalization_` = K11^{-1/2`. `'sigmoid'` is a listed kernel.

**Verdict:** documentation gap. No real feature map can reproduce an indefinite kernel, and the documented identity
cannot hold. The implementation silently approximates |K| instead. The docs should say that the kernel must be
positive semidefinite (sigmoid usually is not). The two lines have the same cause.

### `johnson_lindenstrauss_min_dim(n, eps) satisfies the documented condition 'n_components >= 4 log(n_samples) / (eps^2 / 2 - eps^3 / 3)'` (4 lines, all builds)

**Measured:**

| n | eps | bound | returned |
|---|---|---|---|
| 100 | 0.1 | 3947.29 | 3947 |
| 1000 | 0.5 | 331.57 | 331 |
| 100000 | 0.1 | 9868.22 | 9868 |
| 5 | 0.9 | 39.74 | 39 |

Every returned value is one below the documented bound.

**What the library does:** `random_projection.py`: `return (4 * np.log(n_samples) / denominator).astype(np.int64)`,
which truncates.

**What the documentation says:** "The minimum number of components to guarantee the eps-embedding is given by:
n_components >= 4 log(n_samples) / (eps^2 / 2 - eps^3 / 3)". Returns: "The minimal number of components to
guarantee with good probability an eps-embedding". The docstring's own examples (663, [663, 11841, 1112658],
[7894, 9868, 11841]) show the truncated values, and a separate ok line confirms that the function reproduces them.

**Verdict:** minor off-by-one bug, or a documentation inconsistency: the function should return the ceiling. The
docstring contradicts its own examples. `GaussianRandomProjection(n_components='auto')` inherits the value.

## What held up (all builds unless noted)

- **SVC, decision values:**
  - `decision_function = dual_coef_ @ K(SV, x) + intercept_` for linear, poly, rbf, sigmoid and precomputed kernels,
    with the kernels coded independently.
  - `gamma='scale'` = 1/(n_features · X.var()), exact Fraction, and `gamma='auto'` = 1/n_features.
  - Binary sign convention (positive means `classes_[1]`); support vectors grouped by class with `n_support_`.
  - `coef_ = dual_coef_ @ support_vectors_`; empty `support_vectors_` for precomputed.
- **SVC, dual problem:**
  - KKT conditions of the documented dual within 1e-6: 0 <= alpha <= C · class_weight · sample_weight, with bounded
    SVs exactly at C_i; `sum y alpha = 0`; complementary slackness.
  - Duality gap <= 1e-7. `class_weight='balanced'` = n/(2 · count).
  - Hard-margin closed form on a toy problem (w = (0, 1), b = -1, alphas 1/4, 1/4, 1/2).
- **SVC, other properties:**
  - `shrinking` and `cache_size` do not change the solution; `fit_status_ = 1` at `max_iter=1`.
  - Sparse input equals dense input. A 1e4 offset gives the same fit.
  - A single class, or NaN in X, raises. Zero sample weights give the same decision function as dropping the rows.
  - The `probability` FutureWarning is emitted on 1.9.
- **SVC multiclass:**
  - The ovo decision functions recomputed from the documented `dual_coef_` layout, to 1e-8.
  - Votes, and the tie rule ("first class among the tied classes").
  - The ovr transformation `votes + conf/(3(|conf|+1))`, which keeps the vote order; `break_ties` = argmax of the ovr
    output; `break_ties` with ovo raises.
  - Binary `predict_proba` reproduced exactly by libsvm's coupling iteration.
  - Multiclass `predict_proba` within 5e-3 of the exact Wu–Lin–Weng QP solution.
- **NuSVC, SVR, NuSVR, OneClassSVM:**
  - NuSVC: the nu bounds (margin errors <= nu <= fraction of SVs) for nu = 0.2, 0.5 and 0.7; infeasible nu raises;
    `sample_weight` is used.
  - SVR: the epsilon tube and sign of `dual_coef_`, |dual_coef_| <= C · sample_weight, and predict from the dual.
  - NuSVR: the nu bounds.
  - OneClassSVM: the nu bounds (counting only strict training errors), `decision = score_samples - offset_`,
    `offset_ = -intercept_`, `score_samples = dual_coef_ @ K`, and `sum dual_coef_ = nu · n`.
- **LinearSVC:**
  - The squared-hinge primal at intercept_scaling 1 and 10 matches L-BFGS to 1e-8, with dual = True/False agreement.
  - `dual='auto'` picks the documented solver (1.3+); dual = True/False agree on wide data.
  - `intercept_scaling=100` moves the intercept towards the unregularised value.
  - The hinge primal at tol = 1e-10 is within 1e-7 of the box-QP dual.
  - The l1 penalty objective matches a split-variable reference; l1 with hinge raises.
  - ovr rows equal the separate binary fits.
  - crammer_singer matches an SLSQP solution of the Crammer–Singer QP (objective to 1e-10).
  - `fit_intercept=False`, and `class_weight` as a per-class C.
- **LinearSVR:**
  - The epsilon-insensitive primal matches the box-QP dual; the squared loss matches L-BFGS with dual = True/False
    agreement.
  - `intercept_scaling=50` matches an exact reference.
  - The tol sweep on the section's own data converges.
- **l1_min_c:**
  - The squared-hinge value 0.5/den and the log value 2/den, with the intercept term |sum y| · intercept_scaling.
  - At 0.99 · l1_min_c the l1 LinearSVC and LogisticRegression models are all-zero; at 1.01 · l1_min_c they are not.
  - All-zero X raises.
- **k-nearest neighbours:**
  - kneighbors equals a plain-Python brute-force reference for p = 1, 2, 3, inf, weighted Minkowski and precomputed,
    with distances sorted.
  - Uniform and distance-weighted `predict_proba` and regression; the zero-distance rule (from a source comment).
  - Vote ties go to the smallest label; multi-output; float32; the `n_neighbors` errors; `kneighbors(None)` excludes
    self.
- **Radius neighbours:**
  - Class counts; `outlier_label` None raises, 'most_frequent' works, and an unknown label gives zero probabilities
    with a warning.
  - The regressor returns NaN with a warning for an empty neighbourhood; distance weights.
  - Boundary points are included, for all three algorithms.
- **Graphs, algorithms and trees:**
  - `kneighbors_graph` and `radius_neighbors_graph` in both modes, with `include_self` True, False and 'auto'.
  - brute, kd_tree, ball_tree and auto agree with each other and with the reference, including p = 1 and inf and a
    grid with many tied distances.
  - `sort_results`. KDTree/BallTree `query`, `query_radius` (including <= at a tie) and `two_point_correlation`
    (single-tree and dual-tree).
  - `kernel_density` for gaussian, tophat, epanechnikov, exponential and linear in 1-D and 2-D, and their
    normalisation constants for d = 1..5 (mpmath), plus `return_log` and depth-first.
- **LocalOutlierFactor:**
  - LOF recomputed from the k-distance and reachability definitions (1e-8).
  - `offset_ = -1.5` for 'auto', and the percentile rule for a numeric contamination.
  - novelty `score_samples`, `decision_function` and `predict`.
  - `n_neighbors > n` clipping; duplicates giving LOF = 1; precomputed metric.
  - The documented method availability for novelty=True/False.
- **NearestCentroid:**
  - Centroids (Fraction), Euclidean predict, the ESL 18.4/18.5 shrinkage recomputed, and manhattan medians.
  - 1.6+: `deviations_` shrunk and unshrunk, `within_class_std_dev_`, the ESL 18.2 discriminant with priors, and
    normalisation of priors.
- **NCA:** objective and finite-difference gradient at init and at the solution; callback semantics; transform.
- **KernelDensity:**
  - Normalised `score_samples` for the five correct kernels; `sample_weight`.
  - Gaussian `sample` moments and tophat `sample` support; the NotImplementedError for other kernels.
  - Scott/Silverman factors on unit-variance data.
- **Kernel approximation:**
  - Nystroem is exact for rbf, poly, chi2, precomputed, callable, default gamma, a positive-definite sigmoid and new
    points. With 6 components it equals `K_nm pinv(K_mm) K_mn` for the PSD kernels. `n_components > n` gives a
    warning.
  - RBFSampler: transform formula, weight and offset distributions, kernel approximation, `gamma='scale'` (1.2+).
  - SkewedChi2Sampler: transform, weight distribution (variance 1/4) and kernel approximation.
  - AdditiveChi2Sampler: exact transform for 1–4 steps with the default intervals, convergence at 15 steps, the
    missing-interval error, and sparse input.
  - PolynomialCountSketch: expectation of the kernel, and TensorSketch recomputed with numpy's FFT.
- **Random projection:**
  - The JL value equals the floor of the formula and the docstring examples.
  - Gaussian entries are N(0, 1/k); distances are preserved.
  - Sparse projection: default density 1/sqrt(n_features) and entries ±sqrt(1/(density · k)), including Achlioptas
    density 1/3 and dense density 1; the sparse/dense output options.
  - `inverse_components_ = pinv(components_)` and `inverse_transform` (1.1+).

## Not checked, and why

- **libsvm internals:** Platt `probA_`/`probB_` training (5-fold internal CV with a random shuffle) and the exact
  cross-validated targets. Only the use of `probA_`/`probB_` at predict time is checked.
- **Kernel-approximation constants:** the quality of the RBF/SkewedChi2/PolynomialCountSketch approximations is
  checked only in expectation or at Monte-Carlo tolerance.
- **The liblinear stall mechanism:** inferred from reading the source, not instrumented. liblinear cannot be rebuilt
  or traced from these venvs.
- **LinearSVC(crammer_singer):** checked against a general-purpose SLSQP solution, not a dedicated QP solver. The
  constraints are satisfied to 1e-7 and the objectives agree to 1e-10.
- **Mahalanobis, haversine and other non-Minkowski metrics:** not covered. The task scoped the neighbors checks to
  minkowski p and precomputed.
- **Sparse input to the neighbors estimators, and `n_jobs` parallelism:** not covered.
- **GitHub issues:** issue numbers were matched by title through the GitHub search. The session could not open the
  sklearn issues, so their contents are not verified.
