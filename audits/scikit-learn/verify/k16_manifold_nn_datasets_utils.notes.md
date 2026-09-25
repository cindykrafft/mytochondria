# k16 — manifold, neural_network, datasets, utils: notes

Harness: `k16_manifold_nn_datasets_utils.py`; outputs `.out` (1.9.1 / numpy 2.4.6 / scipy 1.17.1), `.v1.1.3.out`,
`.v1.2.2.out` (numpy 1.24.4, scipy 1.13.1), `.v1.3.2.out`, `.v1.5.2.out` (numpy 1.26.4, scipy 1.13.1). Each run takes
3–8 s. Every `section()` re-seeds its own RandomState, so every build sees the same data.

Truths used: plain-Python reference implementations written from the documented algorithm (brute-force kNN + Dijkstra for
Isomap geodesics; classical MDS by `numpy.linalg.eigh`; the SMACOF Guttman transform and a hand-written PAV isotonic fit
for non-metric MDS; LLE barycentre weights from the documented regularised system `(C + reg*trace(C) I) w = 1`; the LTSA
alignment matrix; the normalised / unnormalised graph Laplacian; the t-SNE perplexity binary search, joint P, KL(P||Q) and
its gradient; trustworthiness by explicit ranks; the MLP forward pass and the user-guide loss formulas plus central
finite differences; the RBM free energy by enumerating all hidden states in mpmath; MurmurHash3_x86_32 in pure Python,
anchored on the published test vectors; BFS for graph hop counts), closed forms (Fractions for class weights and
incremental variances, mpmath chi-square quantiles / densities and truncated-Poisson means for the statistical checks),
and the docstring examples. Statistical checks use explicit standard errors (4.5 SE) rather than ad-hoc tolerances.

Counts: 1.9.1 **283 ok / 12 FAIL**; 1.5.2 271/18; 1.3.2 266/18; 1.2.2 269/15; 1.1.3 263/13. Version-aware expectations:
`normalized_stress` (1.2+; metric + normalized raises on 1.2–1.6, allowed 1.7+; default `'auto'` from 1.4);
`ClassicalMDS` (1.8+); MDS constructor (`metric_mds=` / `metric='precomputed'` 1.8+, `metric=bool` / `dissimilarity=`
before); t-SNE `init='pca'` rescaled to std 1e-4 and `learning_rate_` only from 1.2 (1.1.3: unscaled PCA, checked as
such); `max_iter` vs `n_iter`; the 1.7+ non-metric first iteration using the scaled dissimilarities (replicated); MLP
`n_iter_` per call from 1.3 (1.3 changelog, PR 25443); `sample_weight` in MLP / `resample` / `compute_class_weight`
where present; `check_array` `ensure_all_finite` vs `force_all_finite`, `force_writeable` (1.5+), `ensure_non_negative`;
`make_sparse_spd_matrix` `dim` → `n_dim` and `sparse_format` (1.4+); `make_sparse_coded_signal(data_transposed=False)`
on 1.1/1.2.

## FAIL lines

### 1. smacof (metric): returned stress is the stress of the previous iterate — 1.1.3, 1.2.2, 1.3.2, 1.5.2 (fixed in 1.7)
Measured: `smacof(D, init=X0, max_iter=1, metric=True)` returns X1 = exact Guttman transform of X0 (checked, 2e-16), but
stress 36.81074 = raw stress of the *init* X0; the raw stress of the returned X1 is 25.56908. With the default eps and a
random init the gap is 0.58206 vs 0.57670. Old code (`sklearn/manifold/_mds.py`, `_smacof_single`, 1.5.2 lines 147/155):
`stress = ((dis.ravel() - disparities.ravel()) ** 2).sum() / 2` is computed from `dis = euclidean_distances(X)` *before*
`X = 1.0 / n_samples * np.dot(B, X)`. Docs: "The final value of the stress ... of the disparities and the distances".
Verdict: **bug, fixed in 1.7** (whatsnew 1.7, PR 30514: "the returned stress value now corresponds to the returned
embedding"). 1.9.1 holds exactly (25.56908069 both ways; converged runs to 1e-10).

### 2. smacof non-metric step uses a non-symmetric disparity matrix — 1.1.3–1.5.2 (fixed in 1.7)
Measured: `smacof(D, init=X0, max_iter=1, metric=False)` vs a reference Guttman step against disparities = PAV fit of
d(X0) on the δ order, symmetrised and normalised to Σ_{i<j} d̂² = n(n−1)/2: max |ΔX| 0.26 on ≤1.6, 1e-16 on 1.9.1 (with the
1.7+ "first iteration uses the scaled δ" convention replicated). Old code (1.5.2 line 139): `disparities = dis_flat.copy()`
then only the upper-triangle entries are replaced by the isotonic fit, so the lower triangle holds the current distances,
and the Guttman `B` matrix is built from this non-symmetric matrix. User guide: isotonic regression of d on δ "yielding
disparities"; the disparities are a symmetric quantity. Verdict: **bug, fixed in 1.7** ("MDS now correctly handles
non-metric MDS", PR 30514). Consequence visible below: old builds converge to Kruskal Stress-1 0.278 on this example where
1.9.1 reaches 0.095 (and 0.0068 from another path).

### 3. smacof non-metric normalized stress > 1 and ≠ Kruskal Stress-1 — 1.2.2, 1.3.2, 1.5.2 (fixed in 1.7)
Measured: `normalized_stress=True, max_iter=1` returns 1.56288 (a "Stress-1" above 1); at convergence 0.195948 vs Kruskal's
Stress-1 of the returned configuration (optimal PAV disparities) 0.278128. Old code (1.5.2 line 149):
`stress = np.sqrt(stress / ((disparities.ravel() ** 2).sum() / 2))` — divides by the disparities (not the configuration
distances, and summed over the half-replaced full matrix) and uses the previous iterate (item 1). User guide formula:
sqrt(Σ(d̂ − d(Z))² / Σ d(Z)²); Kruskal's ratio cannot exceed 1 because the zero fit is monotone. Verdict: **bug, fixed in 1.7**
("The formula for normalized stress was adjusted to follow the original definition by Kruskal", PR 31117). 1.9.1: exact
match to the user-guide formula at max_iter=2; converged value within 4e-4 of Kruskal's (0.09511 vs 0.09468: the returned
value uses the previous iterate's disparities, which the 1e-3 check accepts).

### 4. non-metric MDS is not invariant to a monotone transform of δ — 1.9.1 only
Measured: converged non-metric smacof from the same init on δ and on δ³: Procrustes residual 0.267; Kruskal Stress-1 of the
two configurations *for the same ordering* 0.0947 vs 0.0068. On 1.1.3–1.5.2 the two runs are identical (residual 1e-16).
Code (1.9.1 `_smacof_single`, line 156): `if it < 1: disparities_flat = dissimilarities_flat_w` — the first iteration
uses the (scaled) raw dissimilarities, "following the R implementation", so the path and the local optimum reached depend
on the δ values, not only their ranks. User guide: non-metric MDS "focuses on the ordination of the data ... since we only
care about relative ordering, our objective should be invariant". The objective is invariant; the optimiser's path is not.
Verdict: **documented-intent gap, deliberate 1.7 change (not a bug)**; worth one sentence in the user guide (the δ run
stops in a local optimum 14× worse than a configuration the same objective admits).

### 5–6. LLE with eigen_solver='arpack' returns the trivial constant eigenvector — 1.3.2, 1.5.2 (numpy 1.26.4 + scipy 1.13.1)
Measured: standard LLE, 40 points, k=6: ARPACK embedding column sums (−6.3246, 0) — i.e. the first column is the constant
vector ±1/√n; projector distance to the dense solution 1.41; `reconstruction_error_` 3.9e-7 (below the true λ2+λ3 =
2.17e-6). Calling `eigsh(M, 3, sigma=0.0, ...)` directly gives eigenvalues [−5.1e-7, 1.5e-18, 3.9e-7] although M is PSD
with true spectrum [3e-16, 3.9e-7, 1.78e-6, …]: a spurious negative eigenpair from shift-invert at σ = 0, where M is
exactly singular (M·1 = 0). `null_space` (`_locally_linear.py` line 178 / 189): `eigsh(M, k + k_skip, sigma=0.0, ...)`,
`return eigen_vectors[:, k_skip:], np.sum(eigen_values[k_skip:])` then skips the spurious pair and keeps the constant
vector. With the same data it happens for 8 of 30 `random_state` seeds on 1.5.2, none on 1.2.2 (numpy 1.24.4) or 1.9.1
(scipy 1.17.1), and the default `'auto'` solver switches to arpack for n > 200. Docs: "Warning: ARPACK can be unstable for
some problems. It is best to try several random seeds". Verdict: **bug (robustness), environment-dependent**; the
failure is silent (no warning, plausible-looking error value). `spectral_embedding` avoids the same trap with
`sigma=-1e-5` (`_spectral_embedding.py` line 376); the same shift, or dropping the eigenvector closest to constant, would
fix it.

### 7. TSNE(metric='precomputed', method='exact').fit(D) squares the caller's matrix in place — all builds
Measured: after `fit(D)` the caller's `D` equals `D**2` (max change 218). `method='barnes_hut'` leaves D intact. Code
(`_t_sne.py` `_fit`, lines 912 / 936): `distances = X` (the validated input, no copy) and then
`if self.metric != "euclidean": distances **= 2`. Scikit-learn convention: estimators must not modify their input (the common check
`check_inplace_ensure_writeable` in `utils/estimator_checks.py` asserts `assert_allclose(X, X_copy)` after `fit`, but it
feeds a feature matrix, not a precomputed distance matrix, so this path is never exercised).
Verdict: **bug** (silent data corruption; a second fit on the same D squares it again → a different embedding).

### 8. same: a read-only precomputed D raises — all builds
Measured: `D.setflags(write=False)`; `TSNE(method='exact', metric='precomputed').fit(D)` → `ValueError('output array is
read-only')` from the same in-place `**=`. Verdict: **bug** (same root cause as 7; memory-mapped or joblib-shared inputs
are read-only).

### 9. MLPRegressor multi-output loss_ is also averaged over outputs — all builds
Measured: 2-output regressor (lbfgs): `loss_` 0.0763922 = Σ(ŷ−y)²/(2·n·n_outputs) + α/(2n)‖W‖²; the user-guide formula
Loss = 1/(2n) Σ_i ‖ŷ_i − y_i‖²₂ + α/(2n)‖W‖² gives 0.0847960. Code (`neural_network/_base.py`, `squared_loss`, line 188):
`0.5 * np.average((y_true - y_pred) ** 2, weights=sample_weight, axis=0).mean()`. Single-output (all four activations)
and all classifier losses match the documented formulas to 1e-10. Verdict: **documentation gap** — the effective L2
strength relative to the data term shrinks by a factor n_outputs, which the user guide does not say.

### 10. MLP mini-batch loss_ counts the L2 penalty once per batch — all builds
Measured: SGD with `batch_size=13` (4 batches of 52 samples), `learning_rate_init=1e-14` so the weights are frozen:
`loss_` 1.396008 = data term + 4·α/(2n)‖W‖²; the documented loss at those weights is 0.734649 (a full-batch epoch
matches exactly). Code (`_multilayer_perceptron.py`): `_backprop` adds `(0.5 * self.alpha) * values / sw_sum` with
`sw_sum` = batch size (line 361), then `accumulated_loss += batch_loss * (batch_slice.stop - batch_slice.start)` (734),
`self.loss_ = accumulated_loss / X_train.shape[0]` (743). The gradients use the same per-batch scaling
(`coef_grads += alpha * coefs_; /= sw_sum`), so the objective SGD/Adam actually minimise has penalty α/(2·batch_size)‖W‖²
instead of α/(2n)‖W‖², i.e. the same `alpha` regularises n/batch_size times more strongly with sgd/adam than with lbfgs
once n > batch_size (default batch_size=min(200, n)). Docs: `loss_` "The current loss computed with the loss function";
user guide penalty α/(2n)‖W‖². Verdict: **bug or at least an undocumented inconsistency** between solvers
(reported loss curve and effective regularisation both depend on batch_size).

### 11. MLPRegressor `t_` "Mathematically equals n_iters * X.shape[0]" — 1.3.2, 1.5.2, 1.9.1
Measured: `fit(max_iter=5)` then one `partial_fit`: `t_` 318 = 6·53 (cumulative), `n_iter_` 1 (the current call only), so
`n_iter_ * X.shape[0]` = 53. Code: `self.n_iter_ = 0` at the start of every `_fit_stochastic` (line 702) while
`self.t_ += n_samples` accumulates (745). The per-call `n_iter_` is the documented 1.3 change (whatsnew 1.3, PR 25443), and
the harness expects it (separate ok line); the MLPRegressor `t_` docstring (line 1590) was not updated. 1.1.3/1.2.2 hold.
Verdict: **documentation error** (introduced by the 1.3 change; MLPClassifier's `t_` doc has no such sentence).

### 12. make_classification: "More than n_samples samples may be returned if the sum of weights exceeds 1" — all builds
Measured: `weights=[0.7, 0.7], n_samples=100` returns exactly 100 samples with class counts 65/35 (not 70/70). Code
(`_samples_generator.py` line 279): `X = np.zeros((n_samples, n_features))`; cluster sizes `int(n_samples * w / k)` sum to
140, and the slices `X[start:stop]` beyond row 100 are silently truncated, so the last cluster(s) — here class 1 — lose
samples. Docstring line 144. Verdict: **documentation error** (and a silent class imbalance the user did not ask for; an
error or a warning would be better).

### 13. make_sparse_uncorrelated adds N(0,1) noise not in the documented formula — all builds
Measured: y − (X0 + 2X1 − 2X2 − 1.5X3) has std 1.0017 (20 000 samples). Code (lines 1685–1686):
`y = generator.normal(loc=(X[:, 0] + 2 * X[:, 1] - 2 * X[:, 2] - 1.5 * X[:, 3]), scale=np.ones(n_samples))`. Docstring:
`y(X) = X[:, 0] + 2 * X[:, 1] - 2 * X[:, 2] - 1.5 * X[:, 3]` with no noise term and no `noise` parameter. Verdict:
**documentation gap** (the Celeux et al. model has unit-variance noise; the docstring should say `+ N(0, 1)`).

### 14. make_gaussian_quantiles: remainder all goes to the last class — all builds
Measured: `n_samples=11, n_classes=4` → class counts 2/2/2/5. Code (lines 2105/2110): `step = n_samples // n_classes` and
`np.repeat(n_classes - 1, n_samples - step * n_classes)`. Docstring (line 2042): "The total number of points equally
divided among classes" (class description: "roughly equal numbers of samples"). For large n the effect is ≤ n_classes−1
samples (3000/3 → 1000 each, ok). Verdict: **minor doc/implementation gap** (make_blobs distributes the remainder one per
cluster; the same would match "equally divided").

### 15–16. type_of_target on a single-row 2-D array — all builds
Measured: `[[1.5, 2.5]]` → `'continuous-multioutput'`, `[[1, 2, 3]]` → `'multiclass-multioutput'`. Returns section:
"'continuous-multioutput': y is a 2d array of floats ... and both dimensions are of size > 1"; "'multiclass-multioutput':
... both dimensions are of size > 1"; 'continuous'/'multiclass' require 1-d or a column vector, so the documented answer
is 'unknown'. Code (`utils/multiclass.py` line 422): `if y.ndim == 2 and y.shape[1] > 1: suffix = "-multioutput"` — only
the column count is tested. (The docstring's own example `[[1, 2]]` → 'multilabel-indicator' is consistent with the
multilabel definition and passes.) Verdict: **documentation imprecision** — the "both dimensions > 1" clause should read
"more than one column".

### 17. type_of_target(sequence of sequences) raises instead of returning 'unknown' — all builds
Measured: `[[1, 2], [3]]` → `ValueError("You appear to be using a legacy multi-label data representation. Sequence of
sequences are no longer supported ...")` (line 396). Returns section (line 297): "'unknown': y is array-like but none of the
above, such as a 3d array, sequence of sequences, or an array of non-sequence objects". The other two examples (3-d,
object array) do return 'unknown'. Verdict: **documentation error** (deliberate error for the legacy format; the doc list
should drop "sequence of sequences" or mention the error).

## What held up (all builds unless noted)
- smacof/MDS: the Guttman transform step exactly; MDS == smacof with the same init; `dissimilarity_matrix_` (Euclidean in
  plain Python; precomputed = input); non-symmetric input raises; 2-D-embeddable data → stress 1e-10; 1.7+ metric
  Stress-1 formula; normalized_stress defaults ('auto' semantics 1.4+); `ClassicalMDS` (1.8+) = classical MDS.
- Isomap: `dist_matrix_` = plain-Python Dijkstra on the symmetrised kNN graph (9e-16); FW = D; embedding = classical MDS of
  the geodesics; `reconstruction_error()` = the docstring's ‖K(D) − K(D_fit)‖_F/n both via eigenvalues and literally from
  the embedding's distances; `transform` of training points = `embedding_`; `transform` of new points = the documented
  geodesic extension + kernel-PCA projection; both-n_neighbors-and-radius raises.
- LLE: standard weights = the regularised local system (3e-14), rows sum to 1 on the kNN support; embedding = eigenvectors
  2..d+1 of (I−W)ᵀ(I−W); `reconstruction_error_` = their eigenvalue sum; LTSA embedding and error = the hand-built
  alignment matrix; hessian / modified run and return orthonormal, constant-orthogonal columns; the documented hessian
  bound `n_neighbors > n_components(1 + (n_components+1)/2)` exactly at the boundary for d = 1, 2, 3; modified,
  n_neighbors ≥ n, n_components > n_features raise; `transform` = barycentre weights × embedding.
- SpectralEmbedding: rbf affinity with gamma = 1/n_features (+ `gamma_`); embedding = normalised-Laplacian eigenvectors /
  √degree (self-loops ignored) to 6e-15; precomputed = rbf; `drop_first=False` constant first column; `norm_laplacian=False`
  = unnormalised Laplacian; nearest-neighbour affinity with n_neighbors = max(n/10, 1), self included, 0.5(A + Aᵀ).
- TSNE: every conditional row reaches entropy log(perplexity) within the documented 1e-5; rows = plain-Python binary
  search; joint P symmetrised and normalised; Barnes-Hut P on the min(n−1, 3·perp+1) neighbours; exact KL and gradient =
  plain-Python formulas; BH at angle 0 = exact gradient (float32); `kl_divergence_` (exact) = KL of the returned embedding
  (rel 3e-5 on 1.9.1, 1.3e-5 on older builds); BH `kl_divergence_` within 1.4 % (0.6 % older) of its exact KL; exact vs
  BH final KL within 12 %, trustworthiness ≥ 0.976 for both;
  `init='pca'` rescaled to PC1 std 1e-4 (1.2+) / unscaled (1.1); `learning_rate_` = max(N/early_exaggeration/4, 50);
  precomputed Euclidean distances reproduce the default run exactly.
- trustworthiness = the Venna–Kaski formula with explicit ranks (k = 1, 5, 10), T(X, X) = 1, the n/2 guard, precomputed.
- MLP: predict / predict_proba = recomputed forward pass (logistic, softmax, multilabel, all four activations); lbfgs
  `loss_` = documented log-loss / squared loss + α/(2n)‖W‖² at the returned weights (single output); `_backprop` loss and
  gradients = central finite differences (≤ 3e-8 rel) for squared, softmax and binary cross-entropy; early-stopping
  validation set = ceil(0.2·53) = 11 samples, `t_` counts training samples only, `best_loss_` None; `n_iter_`, `t_`,
  `loss_curve_` over a fixed run; partial_fit bookkeeping (version-aware); full-batch epoch loss = loss at the epoch's
  starting weights; integer `sample_weight` = row repetition (1.7+).
- BernoulliRBM: transform = sigmoid(v Wᵀ + b_h); `score_samples` = n_features · log σ(F(ṽ) − F(v)) with the free energy
  enumerated in mpmath (2e-15), and its average over 400 random flips = the pseudo-likelihood (max z 2.7); float32 kept;
  sparse = dense.
- datasets: make_classification column structure (redundant = exact linear combinations, repeated = exact copies, noise
  independent), balanced/weighted class counts, hypercube centroids at ±class_sep, flip_y fraction, shift-then-scale,
  guards; make_regression (y = Xw + bias exactly, n_informative nonzeros in (0, 100), noise std, low-rank profile,
  multi-target); friedman1/2/3 formulas and ranges; make_blobs counts / means / stds / center_box; moons and circles
  radii, counts, tuple n_samples; s-curve and swiss-roll parametrisations and the swiss-roll hole; hastie rule and the
  chi²(10) median 9.34; gaussian-quantile nesting and chi² boundaries (within 4.5 SE); make_low_rank_matrix singular values
  exactly; spd / sparse-spd positive definite, norm_diag, sparse_format; multilabel label-count and document-length
  truncated Poisson means, distributions, sparse / list outputs; biclusters / checkerboard block structure and noise;
  make_sparse_coded_signal; load_iris / digits (incl. n_class) / wine / breast_cancer / diabetes / linnerud shapes, class
  counts, names; diabetes scaled = (raw − mean)/(std·√n) to 3e-17 with unit column sums of squares.
- utils: randomized_svd exact on rank-5 data (tall and wide) with the documented sign convention; weighted_mode docstring
  examples, ties, axis=1; safe_sparse_dot; row_norms; stable_cumsum; softmax vs mpmath incl. overflow-safe shift and
  copy=False; density; cartesian (+ dtype promotion 1.2+); fast_logdet vs mpmath and the −inf cases;
  compute_class_weight / compute_sample_weight ('balanced' in Fractions, dicts, sample_weight, multi-output products,
  bootstrap indices, guards); resample (bootstrap, replace=False, stratify, sample_weight 1.7+), shuffle incl. sparse;
  gen_batches / gen_even_slices docstring examples and an exhaustive partition check; Bunch; mean_variance_axis /
  incr_mean_variance_axis vs dense incl. weights, docstring examples, NaN handling, axis=1; check_array dtype preservation,
  finiteness options, force_writeable, ensure_2d / allow_nd / min samples / complex / sparse / order / copy; the eleven
  type_of_target docstring examples and the documented edge cases; single_source_shortest_path_length vs BFS incl. cutoff;
  murmurhash3_32 = pure-Python MurmurHash3_x86_32 for str / bytes / int32 / arrays, signed and unsigned, four seeds.

## Informational (printed, not reported)
- make_classification `n_repeated`: source columns are drawn by `((n - 1) * uniform + 0.5).astype(int)`, so the first and
  last informative/redundant columns are chosen half as often (350/658/632/360 of 2000). The docstring only says "drawn
  randomly", so this is not reported as a failure.
- make_spd_matrix is symmetric only to 1.2e-14 (`U diag Vt` from an SVD, not `U diag Uᵀ`); `np.array_equal(S, S.T)` is
  False. Checked at 1e-12.

## Not checked, and why
- MDS `n_jobs > 1`, SpectralEmbedding `eigen_solver='amg'` (pyamg not installed), `lobpcg` on large graphs.
- t-SNE `metric` other than Euclidean / precomputed, `n_components > 3` with BH (refused by design), `angle` effects beyond
  0 and 0.5 (the 0.5 gradient error, 0.9 %, is printed only).
- `load_*(as_frame=True)` and the fetch_* loaders (pandas not installed / network).
- MLP `early_stopping` for the regressor split (the validation R² does not expose the split size), `learning_rate`
  schedules, and `n_iter_no_change` stopping details.
