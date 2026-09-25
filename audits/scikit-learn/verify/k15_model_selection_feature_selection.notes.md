# k15 — model_selection (splitters, validation, search, halving, threshold tuning) and feature_selection: notes

Harness: `k15_model_selection_feature_selection.py`; outputs `.out` (1.9.1), `.v1.1.3.out`, `.v1.2.2.out`,
`.v1.3.2.out`, `.v1.5.2.out` (each run takes 2–5 s). Every check is against an independent truth: the documented
examples of the user guide and docstrings (LOO, LPO, RepeatedKFold, ShuffleSplit, StratifiedShuffleSplit, GroupKFold,
StratifiedGroupKFold, LeavePGroupsOut, PredefinedSplit, TimeSeriesSplit, ParameterSampler, chi2, the successive-halving
examples); plain-Python reference implementations written from the documented algorithm (greedy GroupKFold, the
StratifiedGroupKFold greedy of the user-guide implementation notes, TimeSeriesSplit index ranges, BH step-up in
`Fraction`s, SelectPercentile's linear percentile in `Fraction`s, the KSG and Ross nearest-neighbour MI estimators with
the documented 1e-10 noise replicated, RFE / RFECV / SFS greedy loops on hand-written OLS, TunedThresholdClassifierCV's
fold curves with an exact balanced accuracy); closed forms in `Fraction` / mpmath (chi2 statistic and
`gammainc` p-value, Pearson r, uncentred F with an mpmath `betainc` p-value, population variances); hand-set
coefficients for SelectFromModel / RFE importances; recording estimators that log which sample ids / targets they are
trained on (same-shuffling across GridSearchCV candidates, learning-curve prefixes, within-group permutations, halving
subsamples). Each `section()` re-seeds its own RandomState so every build sees the same data.

Counts: 1.9.1 **208 ok / 29 FAIL**; 1.5.2 207/27; 1.3.2 197/26; 1.2.2 196/25; 1.1.3 194/26. Older builds skip what
they do not have: `TunedThresholdClassifierCV` / `FixedThresholdClassifier` (1.5+), `GroupKFold(shuffle)` (1.6+),
`check_cv(shuffle, random_state)` (not in 1.5.2), `cross_validate(return_indices)` (1.3+), `RFECV.cv_results_['n_features']`
(1.5+). Version-aware expectations: `SelectKBest(k > n_features)` raises before the change to a warning (≤ 1.3.2 raise,
1.5.2+ warn); `mutual_info_classif` did not scale X in 1.1.x (replicated); SFS "tol must be positive for forward" only
from 1.2; GroupKFold tie order only fixed (stable argsort) from 1.6 — before that only the fold loads are compared.

## FAIL lines

### 1. `KFold(shuffle=False, random_state=0)` raises — all builds
Measured: constructing `KFold(4, shuffle=False, random_state=0)`. The `KFold` docstring says of `random_state`: "When
`shuffle` is True, `random_state` affects the ordering of the indices ... Otherwise, this parameter has no effect."
`_BaseKFold.__init__` (`sklearn/model_selection/_split.py`, line 367 in 1.9.1) raises
`ValueError("Setting a random_state has no effect since shuffle is False. You should leave random_state to its default (None), or set shuffle=True.")`.
Verdict: **documentation gap** — the behaviour is deliberate (the error message explains it) but the parameter doc
should say that a non-None value is refused, not that it is ignored. (StratifiedKFold's docstring already says "Otherwise,
leave `random_state` as `None`".)

### 2. GroupKFold docstring: "samples ... approximately the same in each test fold when `shuffle` is True" — 1.9.1 (shuffle is 1.6+)
Measured: groups of sizes 10, 10, 1, 1 with `GroupKFold(2, shuffle=True, random_state=s)` for s = 0..11: fold sample
counts differ by 18 of 22 samples in 7 of 12 seeds. Code (`GroupKFold._iter_test_indices`): with `shuffle=True` the
unique groups are permuted and cut by `np.array_split(unique_groups, self.n_splits)` — equal *numbers of groups*, no
size balancing; the greedy "largest group into the lightest fold" balancing is the `shuffle=False` branch. The user guide
states it correctly ("attempts to place the same number of samples in each fold when shuffle=False, when shuffle=True it
attempts to place an equal number of distinct groups in each fold"); the class docstring (line 539–540) has the two
modes swapped. Verdict: **documentation error** (docstring).

### 3. StratifiedGroupKFold docstring: GroupKFold balances "the number of distinct groups" — all builds
Measured: one group of 10 samples + ten groups of 1, `GroupKFold(2)` (default): test folds hold 1 and 10 distinct groups
(10 samples each). The StratifiedGroupKFold docstring (line 904–906) says GroupKFold "attempts to create balanced folds
such that the number of distinct groups is approximately the same in each fold". The default GroupKFold balances sample
counts (see 2). Verdict: **documentation error**; true only of `shuffle=True` (1.6+).

### 4–6. Float `test_size` / `train_size` rounding: 0.07 → 8, 0.29 → 28, 0.14 → 15 of 100 — all builds
Measured: `ShuffleSplit(test_size=0.07)` on 100 samples gives 8 test samples; `ShuffleSplit(train_size=0.29)` gives 28
training samples; `train_test_split(test_size=0.14)` gives 15 test samples. `_validate_shuffle_split` (`_split.py`
lines 2486 / 2491) computes `n_test = ceil(test_size * n_samples)` and `n_train = floor(train_size * n_samples)`; in
binary floating point `0.07*100 = 7.000000000000001`, `0.14*100 = 14.000000000000002`, `0.29*100 = 28.999999999999996`.
The docs say the float is "the proportion of the dataset to include" (GroupShuffleSplit adds "(rounded up)"); 7 % of
100 is 7. For n ≤ 200 and two-decimal proportions there are 22 such (proportion, n) pairs for the ceiling alone
(e.g. 0.28 × 25, 0.56 × 50, 0.14 × 150). Verdict: **bug (low severity)**: the rounding is applied to the rounded
product; a tolerance (e.g. `ceil(x - 1e-9)`) or exact decimal arithmetic would give the documented proportion. Same root
cause as 23 below.

### 7. TimeSeriesSplit Notes formula read literally — all builds
Measured: n = 11, n_splits = 5: training sizes 6, 7, 8, 9, 10 = `i * (n // 6) + n % 6`. The Notes (line 1231) write
the size as ``i * n_samples // (n_splits + 1) + n_samples % (n_splits + 1)``, a code literal which, evaluated with
Python precedence (`(i * n_samples) // (n_splits + 1)`), gives 6, 8, 10, 12, 14. The companion check with the
parenthesised reading passes. Verdict: **documentation gap** (missing parentheses in a code literal).

### 8. TimeSeriesSplit `test_size` docstring: n_samples // (n_splits+1) "is the maximum allowed value with gap=0" — all builds
Measured: n = 13, n_splits = 3: default test_size = 3, but `test_size=4` is accepted and yields 3 valid splits with
training sizes 1, 5, 9. `_split` only refuses `n_samples - gap - test_size * n_splits <= 0`, so the maximum with gap 0 is
`(n_samples - 1) // n_splits` (= 4 here). Verdict: **documentation error** (the claim holds only when n_samples is a
multiple of n_splits+1 plus a small remainder).

### 9. `cross_validate(return_indices=True)`: "a list of integer-dtyped NumPy arrays" — 1.3.2, 1.5.2, 1.9.1
Measured: `ret["indices"]["train"]` is a `tuple` of arrays. `_validation.py` line 415:
`ret["indices"]["train"], ret["indices"]["test"] = zip(*indices)`. Content is correct. Verdict: **documentation gap
(cosmetic)**: tuple vs documented list (matters only for code that appends to or type-checks the container).

### 10. learning_curve: float train_sizes are "a fraction of the maximum size of the training set" — all builds
Measured: `KFold(5)` on 103 samples (training folds of 82, 82, 82, 83, 83); `train_sizes=[..., 1.0]` gives 82, and an
absolute 83 is refused with ValueError. `_validation.py` line 2036: `n_max_training_samples = len(cv_iter[0][0])` —
the *first* fold's training size; the source comment even notes "it is not guaranteed that we use all of the available
training data". Verdict: **documentation gap**: the doc should say "of the first split's training-set size".

### 11. Successive-halving user-guide table `n_candidates_{i+1} = n_candidates_i // factor` — all builds
Measured: 70 candidates, `min_resources=3`, `factor=2`, `max_resources=96`: `n_resources_` = [3, 6, 12, 24, 48, 96]
(matches the table) but `n_candidates_` = [70, 35, 18, 9, 5, 3], not the table's [70, 35, 17, 8, 4, 2].
`_run_search` keeps `n_candidates_to_keep = ceil(n_candidates / self.factor)` (`_search_successive_halving.py` line 367).
The user guide (`doc/modules/grid_search.rst`, "Amount of resource and number of candidates at each iteration") gives
the floor formula twice and the floor table, while the `n_remaining_candidates_` docstring (`ceil(n_candidates[-1] /
factor)`) and the user guide's own aggressive-elimination example ([6, 3, 2]) use the ceiling. Verdict: **documentation
error** (user guide).

### 12. "the amount of resources used at each iteration is always a multiple of min_resources" — all builds
Measured: `factor=1.5`, `min_resources=4`: `n_resources_` = [4, 6, 9, 13, 20, 30, 45]. `n_resources =
int(self.factor**power * self.min_resources_)` (line 325); `factor` is documented as "int or float". Verdict:
**documentation gap**: the multiple-of property holds only for integer factors.

### 13–15. `n_required_iterations_` / `n_possible_iterations_` off by one at exact powers — all builds
Measured: 243 = 3^5 candidates, factor 3, resource budget 1..243: `n_required_iterations_ = 5` and
`n_possible_iterations_ = 5` (both should be 6); the search runs 5 iterations (243, 81, 27, 9, 3) and its last iteration
evaluates 3 = `factor` candidates, contradicting the `n_required_iterations_` docstring ("required to end up with less
than `factor` candidates at the last iteration"). Code (lines 265 and 282): `1 + floor(log(len(candidate_params),
self.factor))` and `1 + floor(log(self.max_resources_ // self.min_resources_, self.factor))`; `math.log(243, 3) =
4.999999999999999`. Other exact powers hit the same way: 3^10, 9^5, 9^10, 10^3, 10^6, 10^9 (e.g. 1000 candidates with
factor 10). With `min_resources='exhaust'` the wrong `n_required` also makes `min_resources_` a factor 3 too large.
Verdict: **bug** (floating-point `log` then `floor`; an integer loop `while factor**k <= n` fixes it). Note that the
third line would also fail for non-powers because the kept count is ceil-rounded (8 candidates, factor 3 → 8, 3),
so the "less than factor" wording is itself only approximately true.

### 16. Halving `random_state`: "used for subsampling the dataset when resources != 'n_samples'. Ignored otherwise" — all builds
Measured: `HalvingGridSearchCV(..., resource='n_samples', random_state=0)` vs `random_state=1` (recording estimator):
different training subsamples. The only subsampling happens *when* `resource == 'n_samples'`: `_SubsampleMetaSplitter`
calls `resample(train_idx, replace=False, random_state=self.random_state, n_samples=int(self.fraction * len(train_idx)))`
(line 34). With any other resource no subsampling happens and `random_state` is unused (HalvingGridSearchCV) or only
used for candidate sampling (HalvingRandomSearchCV). Verdict: **documentation error** (condition inverted; line 544).

### 17. `FixedThresholdClassifier(threshold='auto')` at P = 0.5 — 1.5.2, 1.9.1
Measured: a LogisticRegression with coef 1, intercept 0 at x = 0 (P(y=1) = 0.5 exactly): the base `predict` gives 0
(sklearn's default rule is decision > 0; the user guide: "a positive class is predicted when the conditional probability
P(y|X) is greater than 0.5"), `FixedThresholdClassifier(threshold='auto')` gives 1. `predict` sets
`decision_threshold = 0.5` (`_classification_threshold.py` line 376) and `_threshold_scores_to_class_labels`
(`metrics/_scorer.py` line 1063) uses `y_score >= threshold`. The docstring presents 'auto' as "the default threshold".
Verdict: **documentation gap / edge-case inconsistency** (`>=` vs the base estimator's `>`; only exact ties differ).

### 18–19. `r_regression` of a constant non-zero feature returns ±inf — all builds
Measured: a column of 5.0 (also 1.0, 3.0, 7.0; a column of 0.1 or 1000 behaves as documented): `r_regression` returns
`inf` with `force_finite=True` (documented: "forced to a minimal correlation of 0.0") and `inf` with
`force_finite=False` (documented: `np.nan`). Code (`_univariate_selection.py` lines 380–392): the moment formula
`X_norms = np.sqrt(row_norms(X.T, squared=True) - n_samples * X_means**2)` is exactly 0 while the numerator
`safe_sparse_dot(y_centred, X)` is `5 * sum(y - mean(y))`, a rounding residue ~1e-15, so the division gives ±inf; the
force_finite branch only replaces `np.isnan`. (Other constants give a tiny negative moment → sqrt → nan → handled.)
`f_regression` squares it and ends with nan → 0/1, so only `r_regression` (and `SelectKBest(r_regression)`, which would
rank the constant feature first) is affected. Verdict: **bug**.

### 20–22. `r_regression` above 1 → `f_regression` gives negative F and p = 1 for a perfect predictor — all builds
Measured on 50 random targets y (n = 30) with features [y, −2y]: |r| = 1.0000000000000002 for 19 targets; for those,
`f_regression` returns F = −6.3e16 and p = 1.0 (and for another 15, a finite F ≈ 1e17 instead of `finfo.max`). The
docstring: a perfectly correlated feature "is expected to be np.inf. When force_finite=True, the F-statistic is set to
np.finfo(dtype).max and the associated p-value is set to 0.0". Code (lines 507–513): `f_statistic = corr_coef_squared /
(1 - corr_coef_squared) * deg_of_freedom` with `corr_coef_squared` slightly above 1 → negative F → `stats.f.sf` = 1; the
`mask_inf` fix-up never sees it. Consequence (line 3 of the group): `SelectKBest(f_regression, k=1)` on [noise, y]
selects the *noise* feature. Verdict: **bug** (clip r to [−1, 1], or treat `1 - r² <= 0` as infinite). In the harness
the same 50 targets are used on every build, so the counts are identical.

### 23. SelectFdr at the exact Benjamini–Hochberg boundary — all builds
Measured: m = 19 p-values, the largest equal to alpha = 0.05 and the others under their bounds; BH (p_(m) ≤ m·α/m = α)
keeps all 19, `SelectFdr(alpha=0.05)` keeps 18. `_get_support_mask` (line 973) compares with
`float(self.alpha) / n_features * np.arange(1, n_features + 1)`, and `(0.05/19)*19 = 0.049999999999999996`. 40 random
p-value sets and a genuine step-up case agree with the exact reference. Verdict: **floating-point boundary artefact
(negligible)**; `sv * n_features <= alpha * rank` would be exact at this boundary.

### 24. `GenericUnivariateSelect(mode='k_best', param=3.0)` raises TypeError — all builds
Measured: `get_support()` raises `TypeError: slice indices must be integers`. The docstring types `param` as '"all",
float or int' and the constraint is `Interval(Real, 0, None)`; `_make_selector` passes it unchecked via
`selector.set_params(**{possible_params[0]: self.param})` (line 1153) and `SelectKBest._get_support_mask` slices
`argsort(...)[-self.k:]` (line 800). Verdict: **bug (validation gap)**: an integral float should be converted or
rejected with a clear message.

### 25. `VarianceThreshold().variances_` is not the variance when threshold = 0 — all builds
Measured: column [0, 10, 0, 10] (variance 25): `variances_` = 10. With `threshold == 0` the fit replaces the attribute:
`compare_arr = np.array([self.variances_, peak_to_peaks]); self.variances_ = np.nanmin(compare_arr, axis=0)` (line
122) — the peak-to-peak trick meant to make constant columns exactly 0 overwrites every column whose range is smaller
than its variance (any range > 4 in a two-valued column). Selection is unaffected (both are > 0 iff non-constant), but
the documented attribute "variances_: Variances of individual features" is wrong. Verdict: **bug** (store the variance,
use the min only for the mask).

### 26. VarianceThreshold: "variance lower than this threshold will be removed" — all builds
Measured: a column with variance exactly 0.25 and `threshold=0.25` is removed. `_get_support_mask` returns
`self.variances_ > self.threshold` (line 135), so variance == threshold is removed, while the doc (line 26) only removes
variances *lower* than the threshold. Verdict: **documentation gap** (boundary: "lower than or equal to").

### 27. RFE(step=0.29) on 100 features removes 28, not 29 — all builds
Measured: first elimination removes 28 features (a second iteration removes 1 to reach 71). `step = int(max(1,
self.step * n_features))` (`_rfe.py` line 312) with `0.29*100 = 28.999999999999996`. The doc: "percentage (rounded
down) of features to remove". Verdict: **floating-point artefact, low severity** (same root cause as 4–6).

### 28. SelectFromModel(ElasticNetCV(l1_ratio=1.0)): `threshold_` disagrees with the applied threshold — 1.9.1 only
Measured: `threshold_` = 2.18 (= mean |coef|) while `get_support()` keeps all 9 features with |coef| ≥ 1e-5 (only 4
are ≥ the mean). In 1.9.1 `_calculate_threshold` detects the L1 case for ElasticNetCV / LogisticRegressionCV only via the
*fitted* attribute `l1_ratio_` (line 41: `hasattr(estimator, "l1_ratio_") and np.isclose(estimator.l1_ratio_, 1.0)`);
`_get_support_mask` passes the fitted `estimator_`, but the `threshold_` property passes the unfitted constructor
argument: `return _calculate_threshold(self.estimator, scores, self.threshold)` (line 403). In 1.5.2 the check also
accepted the constructor parameter `l1_ratio`, so both agreed (1.1.3–1.5.2 pass). Verdict: **bug (regression after
1.5)**; `threshold_` should use `self.estimator_`. The LogisticRegressionCV branch (`l1_ratio_`) has the same shape (not run).

### 29. SFS `n_features_to_select='auto'`, `tol=None`: "half of the features" depends on direction — all builds
Measured: 5 features: forward keeps 2, backward keeps 3. `fit` sets `n_features_to_select_ = n_features // 2` (line
253) and, for 'auto', uses it as the number of *iterations* in both directions (line 276), so backward removes 2 and
keeps `n - n // 2`. Verdict: **documentation gap** (rounding for odd n unspecified and direction-dependent); for an int
or float `n_features_to_select` both directions keep the same count.

### 1.1.3 only: `error_score=nan` ranks every candidate −2147483648
Measured: one of three GridSearchCV candidates fails (nan mean): `rank_test_score` = [−2147483648] × 3. 1.1.3
`_search.py` line 969: `np.asarray(rankdata(-array_means, method="min"), dtype=np.int32)` — `rankdata` propagates nan
with the installed SciPy 1.13 and the cast yields INT_MIN for all. `best_index_ = rank.argmin()` (line 735) is then
always 0 whatever the scores: one failed fit makes the search pick the first candidate. Fixed in 1.2 (nan means are
replaced by `nanmin - 1` before ranking; 1.2.2+ pass). Verdict: **bug, fixed in 1.2** (the severity depends on the SciPy
paired with 1.1.x).

## What held up (all builds unless noted)
- LeaveOneOut / LeavePOut (user-guide order, C(n, p), errors); KFold shuffle = one `RandomState.shuffle` then
  consecutive folds, int seed reproducible, RandomState instance re-shuffles per call; RepeatedKFold (user-guide
  example, one RNG across repetitions, partitions); RepeatedStratifiedKFold per-class balance.
- GroupKFold: both documented examples, greedy LPT assignment recomputed (distinct sizes; ties from 1.6), 1.6+ shuffle =
  `permutation` + `array_split`; StratifiedGroupKFold: both examples, the greedy of the implementation notes recomputed
  on 120 samples / 25 groups, label invariance, shuffle partition.
- LeaveOneGroupOut / LeavePGroupsOut (sorted labels, combinations, counts, errors); PredefinedSplit (-1 always train,
  sorted fold ids).
- ShuffleSplit examples and size rules (ceil test / floor train / complement / default 0.1), StratifiedShuffleSplit
  docstring example and per-class floor/ceil allocation, GroupShuffleSplit (test_size counts groups, rounded up,
  default 0.2).
- TimeSeriesSplit: all three documented examples and exact index ranges for 5 configurations with max_train_size /
  test_size / gap.
- check_cv defaults (None → KFold(5), stratified only for classifier + binary/multiclass y, iterable wrapper, instance
  passthrough, 1.9.1 shuffle/random_state); GridSearchCV with an unseeded shuffled KFold uses the same folds for every
  candidate (user guide).
- cross_validate (multi-metric keys, train scores, return_estimator, dict scorers, numeric / 'raise' / nan error_score
  incl. train scores, return_indices content); cross_val_predict (order restored, sorted class columns, missing class
  → 0 / finfo.min, binary decision_function shape, non-partition error).
- learning_curve (floor of fraction, clipping, dedup warning, prefix training, incremental learning chunks and equal
  scores, shuffle replication, return_times); validation_curve against closed-form ridge.
- permutation_test_score with groups: within-group permutations replicated exactly; p-value formula.
- ParameterGrid order / len / getitem / list of dicts; ParameterSampler docstring example, without-replacement, warning,
  exact replication of mixed draws; RandomizedSearchCV candidates, refit callable (no best_score_), min-rank ties, nan
  ranked last (1.2+), multi-metric refit=str recomputed per fold, refit=False, refit=True error.
- Successive halving: user-guide resource schedules (70-candidate table resources, [20, 40, 80], exhaust [250, 500,
  1000], aggressive elimination [20, 20, 40] / [6, 3, 2]), exhaust = highest multiple ≤ max, 'smallest' = 2·n_splits
  (· n_classes) or 1, ceil keep rule, top-k survival, n_candidates='exhaust', best of last iteration, resource injected
  into params, subsample size int(n_res / n · |train|), non-constant cv refused.
- TunedThresholdClassifierCV (1.5+): default cv curve recomputed exactly (fold thresholds, `>=`, balanced accuracy,
  linear interpolation, mean, first argmax), cv=float single stratified split, explicit thresholds, prefit, refit errors;
  FixedThresholdClassifier with float thresholds, decision_function, pos_label (int and str).
- chi2 docstring example (doctest precision), exact chi2 statistic and p-value, sparse = dense, binary target;
  r_regression and r_regression(center=False) exact; f_regression(center=False) F and p exact; constant feature in
  f_regression → 0 / 1.
- SelectKBest ties / 'all' / 0 / NaN; SelectPercentile rounding (distinct scores: > linear percentile, count within
  floor/ceil) and ties capped at int(n·p/100); SelectFpr strict; SelectFwe Bonferroni; SelectFdr = exact BH step-up on
  40 random sets; GenericUnivariateSelect modes.
- mutual_info_regression (k = 3 and 5) = plain-Python KSG, continuous mutual_info_classif = plain-Python Ross (singleton
  class dropped), discrete feature in regression = Ross, to 1e-9 relative, on every build (1.1.x without X scaling).
- VarianceThreshold example, population variances, NaN, sparse; RFE support/ranking for four (n, step) settings, float
  n_features_to_select and step, 2-D coef (sum of squares), callable importance_getter, refit; RFECV cv_results_,
  n_features_, smallest-count tie rule, final RFE; SelectFromModel thresholds ('mean', 'median', scaled, float, None →
  1e-5 for Lasso), max_features (int, callable, with threshold), prefit without refit, norm_order 1/2/inf, getter
  callable and attribute path; SequentialFeatureSelector forward / backward / auto+tol (positive and negative) greedy
  recomputed with hand-written OLS CV; SelectorMixin API (get_support, transform dense/sparse, inverse_transform,
  get_feature_names_out).

## Not checked, and why
- Exact index draws of `sample_without_replacement`, `_approximate_mode` tie breaking, RepeatedStratifiedKFold and
  StratifiedGroupKFold(shuffle=True): only the documented properties are checked (the exact streams are
  implementation details with no documented algorithm to recompute).
- Metadata routing (`params=` / `set_*_request`) and `n_jobs > 1` are not exercised.
- `HalvingRandomSearchCV` with `resource='n_samples'` beyond the random_state finding; `LogisticRegressionCV` in
  SelectFromModel (same code path as ElasticNetCV, not run separately).
- `mutual_info_*` on sparse input and `copy=False`; `TunedThresholdClassifierCV` with `scoring` dicts / constrained
  metrics; `learning_curve` error_score in the incremental path.
