# k10 — naive_bayes / tree / dummy / multiclass / multioutput / semi_supervised: notes

Harness: `k10_naive_bayes_tree_dummy_multiclass_semi.py`; outputs `.out` (1.9.1), `.v1.1.3.out`, `.v1.2.2.out`,
`.v1.3.2.out`, `.v1.5.2.out`. Every check is against an independent truth: `fractions.Fraction` / mpmath
(all five naive Bayes models: sufficient statistics, smoothing, class priors, joint log-likelihood, posterior),
a plain-Python tree builder (`best_splits` / `check_tree`: gini, entropy (log2), variance, weighted-median
absolute error, half Poisson deviance, midpoint thresholds on the float32 copy of X, the weighted impurity
decrease `N_t/N (imp - N_L/N_t imp_L - N_R/N_t imp_R)`, min_samples_split/leaf, min_weight_fraction_leaf,
max_depth, NaN routed left/right/alone), a weakest-link pruning re-implementation from `tree_` arrays, a
best-first re-implementation for `max_leaf_nodes`, hand-computed dummy statistics, one-vs-rest / one-vs-one /
output-code recomposed from separate binary fits, chains recomposed link by link, the harmonic /
`(I - alpha S)^-1 Y` closed forms of label propagation / spreading and a plain re-implementation of the
self-training loop.

Counts: 1.9.1 **161 ok / 5 FAIL**; 1.5.2 157/9; 1.3.2 153/9; 1.2.2 149/6; 1.1.3 148/6.

## FAIL lines

### 1. `GaussianNB(var_smoothing=0.5) partial_fit over two chunks: var_ equals the fit result` — all builds
Measured: `fit` on 8 rows gives `var_ = class variance + epsilon_` exactly (that check passes, exact
Fractions); `partial_fit` on rows 0..3 then 4..7 gives `var_` = [[2.719, 1.969], [4.406, 9.469]] instead of
[[4.367, 3.617], [5.305, 10.367]] (46 % relative), with `class_count_`, `theta_` and `class_prior_` correct.
Library (`sklearn/naive_bayes.py`, `GaussianNB._partial_fit`): line 450
`self.epsilon_ = self.var_smoothing * xp.max(xp.var(X, axis=0))` is executed on the *new chunk* before line 490
`self.var_[:, :] -= self.epsilon_` ("Put epsilon back in each time"), so the smoothing that was added by the
previous call (`epsilon_` of the previous chunk, 1.094 here) is removed with the current chunk's value (2.594),
leaving a negative offset that the Chan/Golub/LeVeque update then scales by `n_past/n_total` before
`self.var_[:, :] += self.epsilon_` (line 523). By hand: class-0 feature-0 variance after chunk 1 is 2/3 +
1.094; the update gives (3(2/3 + 1.094 - 2.594) + 3/4 (2-4)^2)/4 = 0.125 instead of 1.25, plus 2.594. The
documentation says `epsilon_` is the "absolute additive value to variances" and that `partial_fit` is for
"different chunks of a dataset"; nothing says the result depends on the chunking or that the smoothing
subtracted is not the one added. Verdict: **bug** (ordering of the `epsilon_` update; the value subtracted must be
the previously added one). With the default `var_smoothing=1e-9` the error is ~1e-9 relative
(`partial_fit(2 chunks) vs fit: max |theta_/var_ diff| 3.3e-09` in the output, so the default-tolerance check
passes) but the fix is cheap and it matters for large `var_smoothing`. Same on 1.1.3 … 1.9.1.

### 2./3. `DecisionTreeClassifier(class_weight='balanced') … node 11 should be a leaf` and `no single-class node is split further` — all builds
Measured: with `class_weight='balanced'` (weights 60/(2·23) and 60/(2·37)), node 11 holds 4 samples of a single
class (`value = [0, 1]`) but is split into two pure children (zero decrease). Library: `_criterion.pyx` `Gini.node_impurity`
computes `1 - sq_count / (weighted_n_node_samples^2)` in floating point, which for these non-integer weights
gives 1.1e-15, and `_tree.pyx` line 265 `is_leaf = is_leaf or parent_record.impurity <= EPSILON` with
`EPSILON = np.finfo('double').eps` (2.2e-16), so the node is not recognised as pure and the splitter finds a
(useless) split with improvement 0. Documentation (`max_depth`): "nodes are expanded until all leaves are pure".
Verdict: **minor bug / numerical-tolerance gap**: the purity test is absolute machine epsilon on a quantity
that carries rounding of order n·eps; the resulting extra nodes are harmless for prediction but change
`node_count`, `get_n_leaves()` and the pruning path. All other whole-tree checks (unweighted, integer
`sample_weight`, `class_weight={0:1, 1:3}`) pass, so the balanced-weight rounding is the only trigger seen.

### 4. `DecisionTreeRegressor(friedman_mse) multi-output chooses the same root split as squared_error` — 1.1.3, 1.2.2, 1.3.2, 1.5.2 (skipped by design on 1.9.1 where friedman_mse is mapped to squared_error)
Measured on a 6×2 two-output dataset: feature 0 separates the output means by (+20, −20) (cancelling), feature 1
by (+1, +1); `squared_error` splits on feature 0 (decrease 400 per output), `friedman_mse` on feature 1.
Library (1.5.2 `tree/_criterion.pyx`, `FriedmanMSE.proxy_impurity_improvement`): sums the per-output sums first,
`total_sum_left += self.sum_left[k]` … `diff = (weighted_n_right * total_sum_left - weighted_n_left * total_sum_right)`,
`return diff * diff / (weighted_n_left * weighted_n_right)`, i.e. it maximises `(Σ_k Δmean_k)^2 · n_L n_R`, while
`MSE.proxy_impurity_improvement` maximises `Σ_k (sum_left_k^2/n_L + sum_right_k^2/n_R)` ∝ `Σ_k Δmean_k^2`.
For a single output the two rank splits identically (verified: identical trees at max_depth=3; the full trees
differ only at 2-sample nodes with tied features, printed as "differing nodes"). The 1.9 deprecation message
(`tree/_classes.py` line 1348: "It maps to `squared_error` as both were always equivalent") and the changelog
are therefore **wrong for multi-output regression**: on ≤1.8 `friedman_mse` chose different splits than
`squared_error` when `n_outputs > 1`, and users upgrading to 1.9 get different trees silently (only the
FutureWarning). Verdict: **documentation gap** (the deprecation note should say "equivalent for a single output";
a multi-output friedman_mse tree cannot be reproduced on 1.9).

### 5./6. `DummyRegressor(median): sample_weight=ones gives the same median (2.5) as no sample_weight` and `DummyRegressor(quantile=0.25): sample_weight=ones equals no sample_weight (1.75)` — all builds
Measured on y = [1, 2, 3, 4]: median 2.5 without weights, 2.0 with `sample_weight=ones`; quantile 0.25: 1.75 vs
1.0. Library (`dummy.py`, `DummyRegressor.fit`): `np.median` / `np.percentile` (linear interpolation) when
`sample_weight is None`, else `_weighted_percentile(y, sample_weight, percentile_rank=…)` whose docstring
(`utils/stats.py`) states it is the "inverted_cdf" method: "'inverted_cdf' takes the exact data point … would give
'2'". The docstring of `DummyRegressor` only says "median of the training set" / "quantile of the training set".
The 1.8 changelog fixed the same inconsistency for `metrics.median_absolute_error` ("now uses
`_averaged_weighted_percentile` … gives results equivalent to `numpy.median` if equal weights used") but not for
`DummyRegressor`. Verdict: **bug / documentation gap**: unit weights are not a no-op (the general sklearn
sample-weight invariance), and the weighted quantile definition (inverted CDF, no interpolation) differs from the
unweighted one (linear interpolation) without being documented. The integer-weight ↔ repeated-rows check
(`sample_weight=[1,2,1,1]` → 2.0) passes, i.e. the weighted path is self-consistent, it is just a different
estimator than the unweighted path.

### 7. `missing values: a feature constant on the non-missing rows but with NaNs is still split` — 1.3.2, 1.5.2
Measured: X = [1, 1, 1, nan, nan], y = [0, 0, 0, 1, 1] gives a single-node tree (`threshold −2`), predicting 0 for
everything; 1.9.1 splits with `threshold = inf` and predicts [0,0,0,1,1]. User guide (Missing Values Support):
"The splitter also checks the split where all the missing values go to one child and non-missing values go to the
other". Library ≤1.7: `_splitter.pyx` treats the feature as constant when `max − min <= FEATURE_THRESHOLD` regardless
of missing values; 1.9.1 adds `and n_missing == 0` to that test. Changelog 1.8: "Fix … for nodes containing
near-constant feature values and missing values. Beforehand, trees were cut short if a constant feature was found,
even if there was more splitting that could be done on the basis of missing values" (:pr:`32274`).
Verdict: **bug, fixed in 1.8**; documented behaviour on 1.8+.

### 8. `DecisionTreeClassifier with 15% NaN: every split is the best …` — 1.3.2, 1.5.2
Measured (1.5.2): node 10 has library impurity 0.5 and `value [0.5, 0.5]` while the rows that the tree's own
thresholds route there are all of one class (reference impurity 0, value [0, 1]); on 1.3.2 additionally node 5
chooses `f1 <= 0.725, missing left` while the unique maximal-decrease split by hand (0.01296) is `f1 <= 0.508, missing right`, and
node 6 impurity 0.219 vs 0.320. Changelog 1.8: "Fix decision tree splitting with missing values present in some
features. In some cases the last non-missing sample would not be partitioned correctly" (:pr:`32351`) and the
constant-feature fix above; 1.9: "Fixed feature-wise NaN detection in trees. Features could be seen as NaN-free
for some edge-case patterns, which led to not considering splits with NaNs assigned to the left node".
On 1.9.1 the same check (60 rows, 15 % NaN, depth 4) passes exactly. Verdict: **bugs, fixed in 1.8/1.9**.

### 9. `DecisionTreeRegressor(poisson) with NaN in X: node impurities …` — 1.3.2, 1.5.2
Measured: node 2 impurity 0.315 vs 0.201 by hand, node 5 0.457 vs 0.530, node 8 left unsplit although a split with
decrease 0.042 exists. Changelog 1.9 (:pr:`32119`): "Fix calculation of node impurity in `tree.DecisionTreeRegressor`
… when missing values are present for the Poisson criterion. The Poisson criterion was returning invalid impurities".
Passes on 1.9.1 (impurities non-negative and equal to the half deviance by hand). Verdict: **bug, fixed in 1.9**.

## Things worth recording that are not FAILs

* `LabelSpreading(kernel="knn")`: the closed form only matches when `S = D^-1/2 W D^-1/2` uses the *column* sums
  (in-degree) of the asymmetric kNN connectivity graph, zero diagonal, and degree 1 for a point that is nobody's
  neighbour — that is what `scipy.sparse.csgraph.laplacian(normed=True)` (default `axis=0`) does in `_build_graph`.
  With row degrees the result is off by 5e-2. The user guide only says "normalized graph Laplacian"; a note that the
  kNN graph is asymmetric and normalised by in-degree would help (documentation gap, not a bug).
* `LabelPropagation(kernel="knn")` counts the point itself among its `n_neighbors` neighbours (self-loop), so each
  row of T has weight `1/n_neighbors` on itself; the harmonic closed form matches to 1e-15 with that convention.
* `friedman_mse` on 1.9.1: FutureWarning and identical tree to `squared_error` (deprecation mapping works).
* `tree_.value` holds weighted class fractions from 1.4 on and weighted counts before (both checked);
  `export_text(show_weights=True)` prints `value * weighted_n_node_samples`, i.e. weighted counts on every build.
* `DecisionTreeClassifier` ties between two thresholds of one feature keep the lowest threshold (strict `>` on the
  proxy); across features the winner depends on the random feature order, so the reference accepts any of the
  maximal-decrease splits.
* `ccp_alpha` exactly equal to a path alpha prunes that link (documented "stops when … greater than ccp_alpha"); both
  the exact and the in-between alphas reproduce the path impurities on all builds.
* `MultinomialNB(alpha=0, force_alpha=True)` gives `-inf` log-probabilities for unseen features (documented "no
  smoothing"); `force_alpha=False` clips to 1e-10 with a warning (1.2+), and 1.1.3 clips unconditionally.
* `OneVsOneClassifier`: on a triangle of blobs two grid points get cyclic votes (1,1,1) and are decided by the
  summed confidences exactly as documented (`votes + conf/(3(|conf|+1))`).

## What held up (161 checks on 1.9.1)
GaussianNB (theta_/var_/epsilon_/class_prior_ exact; priors; sample_weight = repeated rows; partial_fit at default
smoothing; predict_proba / predict_log_proba to 1e-9 against mpmath including a point with log p ≈ −1e4; float32;
1e6 offset), MultinomialNB (counts, alpha scalar/array, fit_prior, class_prior, force_alpha, sample_weight,
partial_fit, negative counts rejected, posterior), ComplementNB (norm False/True, feature_all_, no prior in the
score, predict/predict_proba), BernoulliNB (binarize 0/0.5/None, absent-feature penalty), CategoricalNB
(category_count_, min_categories scalar/array with the enlarged smoothing denominator, partial_fit, posterior,
unseen category → IndexError). Trees: gini/entropy/log_loss whole-tree equality with the reference on 10-row and
60-row data, log2 entropy, threshold ties, min_samples_split (int/float), min_samples_leaf, max_depth,
min_weight_fraction_leaf, class_weight dict, max_features=1, apply/decision_path/predict_proba from an
independent traversal, feature_importances_ from `tree_`, pruning path and ccp_alpha for classifier and regressor,
max_leaf_nodes best-first (3/5/8 leaves), squared_error / absolute_error / poisson with and without weights, median
midpoint rule, negative Poisson targets rejected, multi-output values, friedman_mse mapping (1.9) / single-output
equivalence (older), monotonic_cst (classifier, regressor, multiclass rejected), ExtraTree thresholds within
[min, max) and not midpoints, ExtraTree leaf fractions, export_text weights and regressor values, the three
user-guide missing-value examples, NaN whole-tree check, NaN apply, ExtraTree with NaN (1.6+), Poisson with NaN
(1.9+). Dummy: all five classifier strategies incl. predict_proba, stratified/uniform frequencies, score with
sample_weight, weighted prior, multi-output; regressor mean/median/quantile/constant, weighted mean, weighted
median vs repeated rows, R^2 score, multi-output. Multiclass: OvR recomposition, probability normalisation,
multilabel marginals, OvO pairwise fits / votes / confidences / cyclic ties, OutputCode code book (±1 and 0/1),
estimators and nearest-code decoding. Multioutput: MultiOutputClassifier/Regressor vs separate fits, ClassifierChain
fit/predict/predict_proba/chain_method='predict_proba'/cv/random order, RegressorChain. Semi-supervised:
LabelPropagation rbf and knn closed forms, clamping, predict_proba, iteration count vs a re-implementation,
ConvergenceWarning; LabelSpreading alpha 0.2/0.8 rbf and knn closed forms, transduction accuracy;
SelfTrainingClassifier threshold / k_best / max_iter=None rounds, labeled_iter_, termination_condition_, k_best too
large.

## Not checked / limitations
* Sparse inputs everywhere; callable kernels for label propagation; `DummyClassifier` sparse targets.
* The node-level mechanics of `monotonic_cst` (only the documented global monotonicity on a grid); combining
  `monotonic_cst` with NaN (1.9).
* The distribution of ExtraTree random thresholds (only the documented range) and the "best of the random splits"
  choice, which cannot be reproduced without the internal RNG stream.
* `CategoricalNB` takes a scalar `alpha` only (docs: "alpha : float"); per-feature alpha arrays were checked for
  MultinomialNB only. `OutputCodeClassifier` decoding was checked with decision_function estimators only.
* Tree checks compare against the reference on the float32 copy of X; ties across features are accepted as any
  maximal-decrease split because the feature visiting order is random (documented).
* The old `absolute_error` criterion (≤1.7) with sample weights was not exercised at its known-buggy points (1.8
  changelog: "would sometimes make sub-optimal splits"); with the final seeds the weighted MAE check passes on all
  builds, but an earlier seed showed a child-impurity mismatch on ≤1.5.2 consistent with that fixed bug.
