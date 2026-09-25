# k11_ensembles — notes

Harness: `audits/scikit-learn/verify/k11_ensembles.py`; outputs `k11_ensembles.out` (1.9.1 / numpy 2.4.6),
`k11_ensembles.v1.1.3.out`, `.v1.2.2.out`, `.v1.3.2.out`, `.v1.5.2.out`.

Counts: 1.9.1: 132 ok / 1 FAIL; 1.5.2: 133 ok / 1 FAIL; 1.3.2: 132 ok / 1 FAIL; 1.2.2: 132 ok / 0 FAIL;
1.1.3: 129 ok / 0 FAIL (fewer checks: no `oob_scores_`, no HGBT `class_weight` / `interaction_cst` / gamma loss,
no RF `monotonic_cst`). Runtime about 4 s per build. The harness sets `OMP_NUM_THREADS=1` before importing
numpy: with the default thread count, one HGBT boosting round on 300 rows took about 2.4 s in this container
(OpenMP oversubscription; `nproc` = 4, 4 threads compete with the harness), 11 ms single-threaded. Results are
unaffected.

## FAIL lines

### `AdaBoost binary decision_function docstring: 'values closer to -1 or 1 ...' -> a unanimous ensemble gives |decision| = 1` (1.9.1, 1.5.2, 1.3.2; ok on 1.2.2 and 1.1.3)

Measured: `AdaBoostClassifier(SAMME, DecisionTreeClassifier(max_depth=1), n_estimators=5, learning_rate=0.7)`
on a binary problem; for the 10 training samples on which all five stumps agree, `decision_function` is
exactly ±2.0 (all builds from 1.3), not ±1.

What the library does: since 1.3 (`_weight_boosting.py`, `AdaBoostClassifier.decision_function`)
```
pred = sum(np.where((estimator.predict(X) == classes).T, w, -1 / (n_classes - 1) * w) for ...)
pred /= self.estimator_weights_.sum()
if n_classes == 2:
    pred[:, 0] *= -1
    return pred.sum(axis=1)
```
For K = 2 the two class scores are ±w each, so after flipping column 0 the row sum is 2 * sum_i w_i s_i / sum w
with s_i = ±1: the binary decision is the *difference* of the two SAMME class scores and lies in [-2, 2]. This
comes from PR 26521 (1.3 changelog: "Fix a bug in AdaBoostClassifier with algorithm='SAMME' where the
decision function of each weak learner should be symmetric (i.e. the sum of the scores should sum to zero for a
sample)"). Before 1.3 the SAMME branch was `pred = sum((estimator.predict(X) == classes).T * w ...)`, whose
binary reduction is sum w_i s_i / sum w in [-1, 1]; that older form matched the docstring, which is why the check
is ok on 1.1.3 and 1.2.2. The harness verifies the actual formula on every build (`AdaBoost binary:
decision_function = 2 * sum alpha_i * ...` / `1 * ...`) and `predict_proba = softmax([-d, d]/2)` is consistent
with it in both eras.

What the documentation says (`decision_function` and `staged_decision_function` docstrings, unchanged since
before 1.3): "For binary classification, values closer to -1 or 1 mean more like the first or second class in
`classes_`, respectively."

Verdict: documentation gap (the docstring was not updated when PR 26521 doubled the binary range; the
multiclass docstring says nothing about the range). Not a numerical bug: `predict`, `predict_proba` and the
multiclass scores are self-consistent and match the SAMME paper.

## Observations recorded as `ok` lines or informational prints (worth knowing)

- `GradientBoostingClassifier.train_score_`: binary `log_loss` gives the binomial deviance 2 * log loss
  (`_gb.py` `_fit_stages`: `factor = 2` for `HalfSquaredError` and `HalfBinomialLoss`, "we keep backward
  compatibility"), but the multiclass `log_loss` gives 1 * mean multinomial log loss (factor 1). The docstring
  only says "the loss of the model at iteration i", so this is documented-as-vague rather than wrong; the
  factor differs between the binary and the multiclass case of the same `loss='log_loss'`. Same in 1.1.3
  (`_gb_losses.BinomialDeviance.__call__` has `-2 * np.mean(...)`, `MultinomialDeviance.__call__` has no 2).
- `AdaBoostClassifier` SAMME multiclass `decision_function` changed in 1.3 (see above); `estimator_weights_`,
  `estimator_errors_` and the sample-weight recursion are identical across all builds.
- HGBT binning: thresholds are `np.percentile(..., method='midpoint')` up to 1.5.2 and
  `'averaged_inverted_cdf'` in 1.9.1 (1.9 changelog: "the bin edges are set to weight-aware quantiles computed
  using the averaged inverted CDF method"); the two methods give different thresholds on the same data (printed).
  With n > 200 000 the mapper uses `rng.choice(n, 200000, replace=False)` up to 1.5.2 and `replace=True` in
  1.9.1 (to implement sample_weight frequency semantics); both were replicated exactly from
  `RandomState(random_state).randint(uint32 max)`. Note that with n > 10 000 `early_stopping='auto'` is on, so
  the mapper is fitted on the 90 % training split unless `early_stopping=False`.
- HGBT categorical cardinality: 10 categories with `max_bins=10` are accepted and `max_bins=9` raises, i.e.
  "at most max_bins" as the docstring says; the user guide (`ensemble.rst`, categorical support section) says
  "The cardinality of each categorical feature must be less than the `max_bins` parameter", which is off by one.
  A negative category value at predict time is treated as missing on all builds.
- `RandomForest*` in 1.9.1: `class_weight` (and `sample_weight`) is folded into the probabilities of the
  bootstrap draw (`_forest.py`: "Combined _sample_weight = sample_weight * expanded_class_weight ... used in
  _parallel_build_trees to draw indices"), and the trees receive plain multiplicities; the 1.9 changelog states
  this for `sample_weight` only. Before 1.9 `class_weight='balanced'` multiplies the tree sample weights
  (verified per leaf). `class_weight='balanced_subsample'` multiplies per-tree weights computed on the bootstrap
  sample in all builds. `tree_.n_node_samples[0]` is the number of distinct drawn rows in 1.9.1 (72 of 120),
  n before.
- Forest `max_samples` float: `round(n * max_samples)` up to 1.5.2, `max(int(max_samples * n), 1)` in 1.9.1
  (105 rows x 0.35 -> 37 vs 36). The docstring says "draw `max_samples * X.shape[0]` samples" and does not
  fix the rounding.
- `GradientBoosting*` `n_iter_no_change`: the validation split equals
  `train_test_split(X, y, test_size=validation_fraction, random_state=RandomState(seed))` (the first draws of
  the fit's RNG); the stopping rule was reproduced from the staged validation MSE on all builds.
- `GradientBoosting*` stage-0 in-bag mask with `subsample < 1` is the first `uniform(n)` draw of
  `RandomState(seed)` with the `_random_sample_mask` acceptance rule; it was replicated and used to verify
  `oob_improvement_[0]` and `train_score_[0]` (in-bag only). Later stages consume the same RNG through the tree
  fits and were not replicated (only the documented recurrence `oob_improvement_[i] = oob_scores_[i-1] -
  oob_scores_[i]` and `oob_score_ = oob_scores_[-1]` were checked, 1.3+).
- `staged_decision_function` of the boosting classifiers yields arrays of shape (n, 1) for binary problems
  while `decision_function` returns (n,), as documented ("shape (n_samples, k) ... k == 1").
- The GB Huber leaf update `median + mean(clip(r - median, -delta, delta))` holds with either the lower
  (inverted-cdf, what the code uses through `_weighted_percentile` since the sample weights are never None) or
  the linear median for the leaf sizes that occurred (printed per leaf); `delta` was checked with n = 21 and
  alpha = 0.9 where the linear and inverted-cdf 0.9-quantiles coincide.

## What held up (all builds unless noted)

GradientBoosting: `init_` = mean / median / alpha-quantile / class prior log-odds (half log-odds for
`exponential`, softmax = priors for K=3); `init='zero'` and a custom `init`; stage-1 tree fitted to y - init
(squared error leaf = mean residual); line-search leaf values for absolute_error (argmin of sum |r - v|),
quantile (argmin pinball), huber (Friedman formula), log_loss (sum(y-p)/sum(p(1-p))), exponential
(sum(y* e^{-y* raw})/sum(e^{-y* raw})), multinomial ((K-1)/K factor); `learning_rate` scaling; `staged_predict`
= init + lr * cumulative sum; `train_score_` for squared_error / absolute_error / quantile / huber (delta from
the pre-stage residuals) / binary log_loss (2 x) / multiclass (1 x) / exponential; `subsample` in-bag weight
sums; `oob_improvement_[0]`, `oob_scores_` recurrence (1.3+); early stopping split and rule;
`feature_importances_` = normalised mean of per-tree unnormalised impurity decreases; multiclass
`predict_proba = softmax(decision_function)`; `random_state` reproducibility.

HistGradientBoosting: bin thresholds (version-aware percentile method; midpoints for <= max_bins distinct
values; NaN ignored for thresholds and mapped to bin max_bins; `thr[i-1] < x <= thr[i]` mapping); 200k
subsample; categorical unknown category == NaN prediction (with and without missing values in training),
cardinality > max_bins raises; `monotonic_cst` (regressor and binary classifier, grids over 15 anchors);
`interaction_cst=[[0],[1]]` gives an additive model (1.2+); `early_stopping='auto'` iff n > 10000;
`train_score_` = -(half squared error) with scoring='loss' and the `_should_stop` rule; hand-computed first
Newton step (best-gain stump, leaf = -G/(H + l2)) for squared_error with l2 = 0 and 3.5, min_samples_leaf = 6,
sample_weight, absolute_error (median line search), quantile (0.7-quantile line search), poisson, gamma (1.3+),
binary log_loss, multiclass K=3 (softmax of log prior + per-class stump), tolerance 1e-6 because gradients and
hessians are float32; `class_weight` dict and 'balanced' == equivalent `sample_weight` (1.2+); duplicated rows
== sample_weight 2 with min_samples_leaf=1; reproducibility.

AdaBoost: SAMME stumps refit with the tracked weights; `estimator_errors_`, `estimator_weights_`
(lr * (log((1-err)/err) + log(K-1))), weight recursion; decision_function / staged_decision_function /
predict_proba = softmax(d/(K-1)) (version-aware form); `algorithm` history (SAMME.R default with unit
estimator weights before 1.6; parameter gone in 1.9.1). AdaBoost.R2 linear / square / exponential error,
beta, weights, weight recursion, weighted-median prediction; reproducibility.

Bagging: `max_samples` float/int, `max_features` float, with/without replacement, trees fitted on exactly the
drawn rows and features, `oob_decision_function_` / `oob_score_` / `oob_prediction_` recomputed from
`estimators_samples_`, predict_proba averaging; reproducibility.

Voting: hard tie -> lowest label, weighted hard votes, soft weighted average, regressor weighted mean and
transform. Stacking: defaults (LogisticRegression / RidgeCV, 5-fold, predict_proba), meta-features =
cross_val_predict with StratifiedKFold(5) / KFold(5) without shuffle and the first probability column dropped
for binary (final estimator refit reproduces coef_/intercept_/alpha_), transform / passthrough / multiclass /
stack_method='predict' shapes, estimators_ refit on the full data.

IsolationForest: `max_samples_` = min(256, n); trees on 256 rows without replacement, depth <= 8;
`score_samples` = -2^(-E[h]/c(256)) with path lengths and c(n) recomputed by walking the trees (7870 of 9600
sample-tree pairs land in unsplit leaves with > 2 samples, so the c(n_leaf) adjustment is exercised);
`offset_ = -0.5`; `decision_function = score_samples - offset_`; `predict`; contamination=0.1 offset = 10th
percentile; max_samples=64 normalisation; reproducibility.

RandomTreesEmbedding: sparse CSR one-hot of the leaf per tree with sum(leaves) columns, dense option, no
bootstrap.

RandomForest / ExtraTrees: bootstrap multiplicities per leaf (from `estimators_samples_` 1.4+, else
`RandomState(tree.random_state).randint`); OOB decision function / score / prediction recomputed;
predict = argmax mean proba (differs from the majority vote on 5 of 120 samples); `feature_importances_` =
mean of per-tree normalised importances, per-tree importances recomputed from `tree_` arrays; `max_samples`
int and float (version-aware rounding); `balanced_subsample` and `balanced` (version-aware);
`min_impurity_decrease` formula on every split; `monotonic_cst` (1.4+); `warm_start` keeps the first trees;
ExtraTrees whole-sample fits and thresholds inside the node's feature range, ET bootstrap OOB; reproducibility.

## Not checked and why

- GB in-bag masks for stages >= 1 with `subsample < 1` (the tree fits consume the same RandomState); only the
  documented recurrence between `oob_scores_` and `oob_improvement_` was checked there.
- GB `n_iter_no_change` for the classifier (stratified split) and HGBT early stopping with a validation split
  (the split comes from the estimator's derived seed) — only the regressor / training-data rule was checked.
- HGBT deeper trees (only stumps were hand-computed; deeper trees would need a full histogram grower
  reimplementation), HGBT `interaction_cst` beyond additivity, HGBT with sparse or float32 input.
- AdaBoost.R2 bootstrap draws (`random_state.choice(p=sample_weight)` inside the library) — the fitted
  estimators were taken as given and only the error / weight recursion and the median were recomputed.
- Bagging / IsolationForest with `sample_weight` (1.8 changed the semantics to weighted draws) and
  `bootstrap_features=True`; IsolationForest with `max_features < 1` or `bootstrap=True`.
- Multi-output forests, `warm_start` for GB / HGBT, GB `loss_` attribute semantics (only its presence is
  printed), `GradientBoosting*` with sparse input, `RandomTreesEmbedding` with `sparse_output=False` on
  sparse input.
