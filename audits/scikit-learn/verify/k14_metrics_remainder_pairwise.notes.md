# k14: sklearn.metrics remainder, pairwise and scorers — notes

Harness: `k14_metrics_remainder_pairwise.py`. Outputs: `.out` is sklearn 1.9.1 with numpy 2.4.6 and scipy 1.17.1. The `.v1.1.3`, `.v1.2.2`, `.v1.3.2` and `.v1.5.2` outputs use scipy 1.13.1.
Every check compares against one of these: a Fraction or mpmath recomputation of the documented formula, a plain-Python reference (scipy's documented boolean-distance formulas, EMI for AMI, Hand–Till OvO, and so on), or a documented invariant. The scorer checks use fixed-output estimators (outputs are tables indexed by `X[:, 0]`), so every scorer value has an exact truth.

| build | ok | FAIL |
|---|---|---|
| 1.9.1 | 603 | 4 |
| 1.5.2 | 588 | 2 |
| 1.3.2 | 570 | 4 |
| 1.2.2 | 546 | 2 |
| 1.1.3 | 536 | 2 |

The counts differ by build because version-gated APIs are only checked where they exist.

## FAIL lines

**1. `jaccard_score accepts zero_division=np.nan as its docstring lists` (1.9.1 only).**
- **Measured:** `jaccard_score(YT, YP, average="samples", zero_division=np.nan)`.
- **Library:** raises `InvalidParameterError`. The `@validate_params` block of `jaccard_score` (installed 1.9.1 `sklearn/metrics/_classification.py` lines 1050–1055; main `_classification.py` lines 1051–1054) still allows only `"zero_division": [Options(Real, {0, 1}), StrOptions({"warn"})]`.
- **Docs:** the docstring of the same function (installed line 1137, main line 1136) reads `zero_division : {"warn", 0.0, 1.0, np.nan}, default="warn"`. The downstream code would handle NaN: `_prf_divide`, reached through `_check_zero_division`, returns `np.nan` for it.
- **Builds:** in 1.3.2 and 1.5.2 the docstring still said `"warn", {0.0, 1.0}` and the validator agreed, so those builds pass.
- **Verdict:** a documentation/validation mismatch in 1.9.1 and main. The docstring advertises an option that the parameter validator rejects. Either the docstring is wrong or the validator is. The same docstring also misstates when the zero division happens: "when there are no negative values in predictions and labels". A zero division actually happens when the union of true and predicted positives is empty.

**2. `pairwise_distances accepts metric='sokalmichener' listed in its docstring (or the docstring notes its removal)` (1.9.1 with scipy 1.17.1).**
- **Library:** `pairwise.py` (installed lines 685–687) adds `"sokalmichener"` to `_VALID_METRICS` only `if sp_base_version < parse_version("1.17")`. The comment there reads "Deprecated in SciPy 1.15 and removed in SciPy 1.17". With scipy 1.17 the name is therefore rejected by parameter validation.
- **Docs:** the docstrings of `pairwise_distances` (line 758), `pairwise_distances_argmin_min` / `pairwise_distances_argmin` (line 906) and `pairwise_distances_chunked` (line 2349) still list `'sokalmichener'` among the valid scipy metrics. They carry removal notes only for `'kulsinski'` and `'matching'`.
- **Builds:** on 1.1.3 and 1.2.2 (with scipy 1.13) the analogous `'kulsinski'` case is printed as an environment artifact, not a FAIL, because those releases predate scipy's removal.
- **Verdict:** documentation gap in 1.9.1: the docstring's metric list is stale for scipy ≥ 1.17. Related oddities, printed informationally:
  - `'wminkowski'` is still in `_VALID_METRICS` (line 681), so validation accepts it, but scipy then fails with "Unknown Distance Metric".
  - `'matching'` is in `_VALID_METRICS` unconditionally, although the comment says it was removed in SciPy 1.9. It works only because scipy 1.17 still accepts it as an alias of hamming.

**3. `user guide: the scorer table 'shows all possible values' -> every get_scorer_names() entry appears in it` (checked on 1.9.1 only).**
- **Library:** `get_scorer_names()` returns `matthews_corrcoef`, `positive_likelihood_ratio` and `neg_negative_likelihood_ratio`. All three were checked exactly and are correct.
- **Docs:** the table in `doc/modules/model_evaluation.rst` (main, from line 205: "the table below shows all possible values") does not contain them.
- **Scope:** the table is from the main branch, since the installed wheels do not ship the rst. For that reason the check is gated to the 1.9 build. On older builds the names outside the table are printed.
- **Verdict:** documentation gap. The scorers work; the table is incomplete.

**4. `roc_auc_score(multi_class='ovo', average='weighted') = the user guide's formula …` (all builds).**
- **Docs:** the user guide (main `model_evaluation.rst` line 1683 onward) defines the prevalence-weighted OvO AUC as `1/(c(c-1)) Σ_{j<k} p(j∪k) (AUC(j|k) + AUC(k|j))`.
- **Library:** `_average_multiclass_ovo_score` (`sklearn/metrics/_base.py`) computes `prevalence[ix] = np.average(ab_mask)` and returns `np.average(pair_scores, weights=prevalence)`. That is a normalised weighted mean, `Σ p·s / Σ p`, with `s = (AUC(j|k)+AUC(k|j))/2`. The harness confirms this exactly: 0.501852.
- **The two disagree:** for c classes, `Σ_pairs p(j∪k) = c − 1`, so the two differ by the factor c/2. For c = 3 the literal formula gives 0.334568. The literal formula also gives 2/c for a perfect classifier, so it is clearly missing its normalisation.
- **Verdict:** a documentation error in the user-guide formula. The implementation is the sensible, normalised one. It is reported against every build because the behaviour is the same everywhere; the formula checked is the main-branch text.

**5. `get_scorer('top_k_accuracy')(est, X, y) = exact metric …` (1.1.3, 1.2.2, 1.3.2).**
- **Measured:** the named scorer on a 3-class fixed classifier.
- **Library:** on these builds it raises `ValueError: multiclass format is not supported`. The scorer is `make_scorer(top_k_accuracy_score, greater_is_better=True, needs_threshold=True)` (1.3.2 `_scorer.py` line 791). `_ThresholdScorer._score` rejects any target that is not binary or multilabel: `if y_type not in ("binary", "multilabel-indicator"): raise ValueError(...)` (line 451).
- **Why it matters:** for binary targets, `top_k_accuracy` with the scorer's default k = 2 is identically 1.0. So on these versions the named scorer is useless for binary targets and unusable for multiclass ones, although the scoring table lists `'top_k_accuracy'` as a scorer.
- **Fix:** 1.4 replaced `needs_threshold` with `response_method=("decision_function", "predict_proba")` (1.4 changelog, PR 26840). 1.5.2 and 1.9.1 give the exact value.
- **Verdict:** a bug in 1.1–1.3, fixed in 1.4.

**6. `f1_score(average='samples', zero_division=1) …` and `… zero_division=np.nan …` (1.3.2 only).**
- **Measured:** expected 0.624524 but got 0.649524; for NaN, expected 0.594080 but got 0.709063.
- **Library:** 1.3.2 `_precision_recall_fscore_support` computes `denom = beta2 * precision + recall; mask = np.isclose(denom, 0) | ...; f_score[mask] = zero_division_value`. A sample with tp = 0 but fp > 0 and fn > 0 has precision = recall = 0, so denom = 0 and F is set to the zero_division value (1, or NaN, which is then excluded from the average) instead of 0.
- **Minimal case:** `f1_score([[1,0,1]], [[0,1,0]], average='samples', zero_division=1)` returns 1.0 on 1.3.2.
- **Docs:** the 1.3 docstring says zero_division applies "when all predictions and labels are negative".
- **Fix:** 1.4 changelog: "f1_score now provides correct values when handling various cases in which division by zero occurs by using a formulation that does not depend on the precision and recall values" (PR 27577). 1.1.3 and 1.2.2 pass because they did not have this formulation. 1.5.2 and 1.9.1 pass.
- **Verdict:** a bug in 1.3.x, fixed in 1.4.

**7. `d2_log_loss_score(labels=[0,1,2]) when y_true lacks a class …` (1.5.2).**
- **Library:** raises `ValueError: The number of classes in labels is different from that in y_pred`. In 1.5.2 `d2_log_loss_score` builds the null model from `np.unique(y_true)` only, giving 2 columns, then calls `log_loss(..., labels=labels)` with 3 labels (`_classification.py` line 3362).
- **Docs:** the docstring promises the `labels` parameter for exactly this case.
- **Fix:** 1.7 changelog: "d2_log_loss_score now properly handles the case when `labels` is passed and not all of the labels are present in `y_true`" (PR 30903). 1.9.1 matches the exact value, -1.474329.
- **Verdict:** a bug in 1.5–1.6, fixed in 1.7. The function does not exist before 1.5.

## Expectations fixed while re-verifying the inherited partial harness

These were harness errors, not library failures.
- **MSLE targets in (-1, 0):** the partial derived its expectation from the docstring text, which says nothing about the domain. It is now version-aware per the 1.6 changelog ("now check whether the inputs are within the correct domain for y=log(1+x)"). Pre-1.6 rejects negative values; 1.6+ accepts x > −1. The value is checked exactly.
- **`d2_pinball_score` null quantile:** the partial expected inverted_cdf before 1.8. The source of 1.1–1.5 uses `np.percentile` (numpy "linear") for unweighted input and `_weighted_percentile` (inverted_cdf) for weighted input. The 1.9 changelog records the switch to `averaged_inverted_cdf` in both cases. The expectations follow that.
- **Random data by build:** the partial drew all its data from one generator, and version-gated blocks consumed draws, so the data differed by build. Each section now reseeds its generator, so data are identical across builds.
- **`consensus_score` reference:** it divided 0/0 for empty biclusters, and 1.2.2 and 1.3.2 crashed. Biclusters are now generated non-empty.
- **`calinski_harabasz_score` with zero within-cluster dispersion returning 1.0:** undocumented, so it is now informational only.

## What held up (exact or to a documented tolerance, on every build where the API exists)

**Classification**
- `fbeta_score` for beta in {0.5, 1, 2}, plus beta=0 (precision only) and beta=inf (recall only, 1.3+).
- The 'samples' average with zero_division 0, 1 and NaN (NaN excluded, 1.4+), with and without sample weights.
- PRF with `labels` subsets, absent labels, and `pos_label` with string labels.
- `jaccard_score`: every average, labels, zero_division 0 and 1, and sample weights.
- `hamming_loss`, `zero_one_loss` and subset accuracy, all with weights.
- `brier_score_loss`: binary, pos_label inference, string labels, multiclass and `scale_by_half` (1.7+), and `d2_brier_score`.
- `hinge_loss`: binary, and multiclass Crammer–Singer with `labels`.
- `top_k_accuracy_score`, including the documented tie rule (highest index first), binary thresholds, and labels.
- `classification_report` numbers: accuracy, micro, macro, weighted and samples averages.
- `multilabel_confusion_matrix`: samplewise, labels order, weights and multiclass.
- `class_likelihood_ratios`, including zero denominators and `replace_undefined_by` (1.7+).
- `d2_log_loss_score`.
- Weighted MCC, weighted kappa (none, linear, quadratic) and weighted balanced accuracy, including the adjusted form.
- `log_loss`: labels, normalize, the eps history (1e-15 before 1.2, then finfo eps, and float32 eps), and renormalisation before 1.5.

**Ranking**
- DCG and NDCG averaged over all tie permutations, with k and log_base.
- `label_ranking_average_precision_score`, `label_ranking_loss` and `coverage_error`, each with ties and weights.
- `det_curve` points, including the 1.7+ infinite threshold, drop_intermediate and pos_label.
- Multilabel AUC and AP with macro, micro, samples and weighted averages.

**Regression**
- MSLE and RMSLE.
- Median absolute error: weighted averaged_inverted_cdf from 1.8 and inverted_cdf before; multioutput.
- `max_error` and pinball loss.
- Tweedie deviance for powers −1, 0, 1, 1.5, 2 and 3, with its domain checks and degree-(2−p) homogeneity.
- `d2_tweedie_score`, `d2_pinball_score` and `d2_absolute_error_score`.
- MAPE with a zero target (eps = 2^-52).
- `r2_score` and `explained_variance_score` with weights, multioutput and force_finite.
- RMSE multioutput.

**Clustering**
- `contingency_matrix` with eps, sparse output and dtype.
- `pair_confusion_matrix` and the rand identity.
- `consensus_score` against a brute-force Hungarian matching and with a callable similarity.
- V-measure with beta.
- The single-cluster and n_labels = n_samples errors.
- `silhouette_score` with sample_size and random_state, including the precomputed metric.

**Pairwise distances**
- Every sklearn and scipy real-valued metric against plain-Python formulas: euclidean, l2, sqeuclidean, manhattan, l1, cityblock, chebyshev, minkowski with p and w, cosine, correlation, braycurtis (scipy), canberra with 0/0 terms, hamming, seuclidean with V, and mahalanobis with VI.
- The default V and VI from X when Y=None, including with n_jobs=2.
- `haversine_distances`, and every `nan_euclidean_distances` rule, including the docstring example, all-missing rows and missing_values.
- Every boolean metric scipy still provides, with non-zero entries treated as True.
- Y=None symmetry with an exactly-zero diagonal where it is documented or implied, n_jobs equality, CSR equality, callable and precomputed metrics.
- `pairwise_distances_argmin` / `argmin_min`, including axis=0 and metric_kwargs.
- `pairwise_distances_chunked`: chunk size bounded by working_memory, `reduce_func` start offsets, tuple returns, the wrong-length error, and seuclidean V computed globally.
- `paired_distances`.

**Kernels, `euclidean_distances`, cosine**
- Every kernel in `PAIRWISE_KERNEL_FUNCTIONS` with default gamma = 1/n_features. `chi2` uses its documented default gamma = 1.
- Explicit parameters, `filter_params`, callables, precomputed input, n_jobs and CSR input.
- `euclidean_distances` with given norms, in all accepted shapes, and the formula when wrong norms are passed in float64.
- Cosine clipping to [0, 2] and an exact zero diagonal.

**`DistanceMetric`**
- Every documented identifier and alias: euclidean, l2, manhattan, cityblock, l1, chebyshev, infinity, minkowski, p, minkowski with w, and minkowski with p=1 and p=2 (which return the Manhattan and Euclidean classes).
- seuclidean, mahalanobis with V and with VI, hamming, canberra, braycurtis (its own documented `Σ|x−y|/(Σ|x|+Σ|y|)`), haversine, and the eight boolean classes including kulsinski's documented formula.
- pyfunc.
- Minkowski with 0 < p < 1 from 1.3.1. The class docstring says "versionchanged 1.4.0", but 1.3.2 already accepts it, per the 1.3 changelog.
- `dist_to_rdist` / `rdist_to_dist` round trips and the reduced forms d², d^p and sin²(d/2).
- The float32 classes (1.3+).

**Scorers**
- All 52–58 names of `get_scorer_names()` on every build, each against an exact truth. This includes the neg_* sign flip, the clustering scorers (AMI through an exact mpmath EMI), and the *_samples scorers on a multilabel fixed estimator.
- sample_weight passthrough.
- `make_scorer`: kwargs, `greater_is_better`, and the response_method order of preference (or needs_proba / needs_threshold before 1.4).
- `check_scoring`: default `score`, TypeError when the estimator has no `score`, `allow_none`, and list and dict multi-metric scoring where documented.
- `get_scorer` on a callable, on None, on an unknown name, and returning a copy.
- `cross_validate` multi-metric results per fold.

## Informational findings (no FAIL, recorded for the audit)

- **braycurtis:** `DistanceMetric.get_metric('braycurtis')` uses `Σ|x−y|/(Σ|x|+Σ|y|)`, while `pairwise_distances(metric='braycurtis')` defers to scipy's `Σ|x−y|/Σ|x+y|`. Both match their own documentation. On signed data they differ, for example 1.0 vs 3.75 on the first pair, so tree-based and brute neighbour searches with this metric can disagree on signed features.
- **seuclidean / mahalanobis with Y:** `pairwise_distances(X, Y, metric='seuclidean'|'mahalanobis')` without V or VI raises "The 'V' parameter is required … when Y is passed". Scipy's own default would use `vstack(X, Y)`. This is undocumented in the sklearn docstring.
- **Zero-row cosine:** `cosine_similarity` gives 0 for a zero row (undocumented).
- **`calinski_harabasz_score`:** returns 1.0 when the within-cluster dispersion is zero (undocumented).
- **`det_curve`:** the 1.7 changelog says an extra threshold at infinity is now returned. In fact it is kept only when no finite threshold reaches fpr = 0, which matches the docstring example. The check encodes that.

## Not checked, and why

- **scipy boolean metrics removed from scipy:** 'kulsinski' on 1.1.3 and 1.2.2 (scipy 1.13 removed it after those releases) is printed as an environment artifact. 'sokalmichener' via `pairwise_distances` on 1.9.1 is covered only by the docstring FAIL, since scipy 1.17 has no implementation left to compare against.
- **User guide tables:** the scoring table and the OvO formula are only available from the main-branch rst, because the installed wheels ship no docs. The table-completeness check is therefore gated to 1.9.
- **Array API dispatch and GPU namespaces:** not exercised.
- **`adjusted_mutual_info_score`:** checked only through the scorer, with a single `average_method` (arithmetic). The other averages are in k2.
- **`pairwise_distances_argmin` tie-breaking:** not documented, so it is printed (it matches np.argmin, first index) rather than asserted.
