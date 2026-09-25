# k13 — preprocessing / feature_extraction / impute / compose / pipeline: notes

Harness: `k13_preprocessing_extraction_impute_compose.py`; outputs `.out` (1.9.1), `.v1.1.3.out`, `.v1.2.2.out`,
`.v1.3.2.out`, `.v1.5.2.out` (each run takes about 3 s). Every check is against an independent truth: exact
`fractions.Fraction` products for `PolynomialFeatures`; a plain-Python Cox–de Boor B-spline evaluator (values and
derivatives, Lagrange extrapolation of the boundary polynomial piece, periodic wrapping) for `SplineTransformer`;
docstring / user-guide examples for the encoders and vectorizers; the documented Micci-Barreca shrinkage formulas
(including the empirical-Bayes `m = sigma_i^2 / tau^2`) recomputed in Fractions and a fold-by-fold cross-fitting
re-implementation for `TargetEncoder`; `(X - mean)(X - mean)^T` for `KernelCenterer`; an mpmath golden-section
maximiser of the Yeo–Johnson profile log-likelihood for `PowerTransformer`; `sqrt(2) erfinv(2p - 1)` (mpmath) for
the normal quantiles of `QuantileTransformer` and `RobustScaler(unit_variance)`; regex / string reference
tokenizers and mpmath tf-idf; `sklearn.utils.murmurhash3_32` (the documented hash) for `HashingVectorizer` /
`FeatureHasher`; exact patch enumeration and Fraction averaging for the image functions; the documented
`nan_euclidean` distance and donor rule for `KNNImputer`; exact normal-equation OLS chained imputation for
`IterativeImputer`; manual chaining for `ColumnTransformer` / `Pipeline` / `FeatureUnion`.

Counts: 1.9.1 **435 ok / 8 FAIL**; 1.5.2 430/9; 1.3.2 427/9; 1.2.2 399/8; 1.1.3 394/8 (older builds skip the
features they do not have: `TargetEncoder` (1.3+), `SplineTransformer(sparse_output)` (1.3+ in these builds),
`OrdinalEncoder` infrequent categories (1.3+), `feature_name_combiner` (1.3+), `keep_empty_features` (1.2+),
`handle_unknown='warn'` (1.6+), `ColumnTransformer(verbose_feature_names_out=str/callable)` (1.6+),
`SimpleImputer(strategy=callable)` (1.5+), `MaxAbsScaler(clip)` (1.6+)).

## FAIL lines

### 1. `SplineTransformer(degree=0, extrapolation='constant')`: transform raises `ValueError: shape mismatch` — all builds
Measured: fit on 13 points with `n_knots=4`, then `transform` of values above the last knot. The dense path
(`sklearn/preprocessing/_polynomial.py`, `SplineTransformer.transform`, lines 1176–1181 in main, 990 in 1.1.3)
executes `XBS[above_xmax_mask, ((feature_idx + 1) * n_splines - degree):((feature_idx + 1) * n_splines)] = f_max[-degree:]`;
with `degree = 0` the column slice is empty but `f_max[-0:]` is the whole array of `n_splines` values, so numpy
raises `ValueError: shape mismatch: value array of shape (3,) could not be broadcast to indexing result of shape (2,0)`.
Values *below* the first knot do not raise but come out as all zeros (`XBS[below_xmin_mask, start:start + 0] = f_min[:0]`
is a no-op after the row was zeroed), which is not "the value of the splines at minimum ... used as constant
extrapolation" either. The docstring allows `degree` "non-negative integer" and `extrapolation='constant'` is the
default, so `SplineTransformer(degree=0)` fails on any test point outside the training range. Verdict: **bug**
(degree 0 needs the `degree == 0` special case that `'linear'` already has: `if degree <= 1: degree += 1`). Same in
1.1.3, 1.2.2, 1.3.2, 1.5.2, 1.9.1. All other 15 (degree, extrapolation) combinations, including degree 0 with
`linear` / `continue` / `periodic`, match the Cox–de Boor reference to 1e-16.

### 2. `SplineTransformer(degree=0, extrapolation='constant', sparse_output=True)`: rows below the first knot are all zero — 1.3.2, 1.5.2, 1.9.1
Measured: the sparse path does not raise (`XBS_sparse[above_xmax_mask, -0:] = f_max[-0:]` assigns the full
`f_max = [0, 0, 1]` to every column, which happens to be the right answer above the range), but below the range
`XBS_sparse[below_xmin_mask, :0] = f_min[:0]` is a no-op and the rows stay `[0, 0, 0]` instead of `[1, 0, 0]`
(line 1159). Documentation: same sentence as above. Verdict: **bug** (same root cause; silently wrong rather
than raising). Not testable on 1.1.3/1.2.2 where `sparse_output` does not exist.

### 3. `OneHotEncoder(max_categories=3)` with b, c, d tied at 10: user-guide tie sentence — all builds
Measured: `X = 20×'a' + 10×'b' + 10×'c' + 10×'d'`, `max_categories=3` gives `infrequent_categories_ = ['b', 'c']`
and keeps `a`, `d`. This matches the example printed in the user guide (`doc/modules/preprocessing.rst` line 869,
`[array(['b', 'c'], dtype=object)]`), so the *example* check passes. But the sentence introducing the example
(lines 865–868: "If there are infrequent categories with the same cardinality at the cutoff of `max_categories`,
then the first `max_categories` are taken based on lexicon ordering ... 'b' and 'c' are infrequent because they
have a higher lexicon order") contradicts it: `d` has the highest lexicon order and is *kept*. Library
(`_encoders.py`, `_BaseEncoder._identify_infrequent`, line 327): `smallest_levels = np.argsort(category_count,
kind="mergesort")[:-frequent_category_count]`, i.e. a stable ascending sort of the counts; among ties the
*earlier* categories in `categories_` order are dropped first and the *last* ones are kept. Verdict:
**documentation error** (the rule is "ties at the cutoff are resolved by keeping the later categories in
lexicographic order"; the text says the opposite). Same on all builds.

### 4./5. `OneHotEncoder(min_frequency=6, drop=['a'])` with `'a'` infrequent — all builds (4); 1.3.2, 1.5.2, 1.9.1 (5)
Measured: fitting raises. On 1.1.3/1.2.2 it is `ValueError: Unable to drop category 'a' from feature 0 because it
is infrequent`; on 1.3.2, 1.5.2 and 1.9.1 it is `AttributeError: 'str' object has no attribute 'item'`. Library
(`_encoders.py`, `OneHotEncoder._map_drop_idx_to_infrequent`, lines 806–811): the intended path is
`raise ValueError(f"Unable to drop category {categories[drop_idx].item()!r} from feature ...")`; `categories` is an
object array here so `categories[drop_idx]` is a Python `str`, which has no `.item()`, and the message
construction itself raises `AttributeError` (the `.item()` call was added in 1.3; it works for numeric categories,
verified: `drop=[3]` with numeric infrequent category 3 raises the intended `ValueError`). Documentation
(`drop_idx_` attribute docstring, line 641–644): "If infrequent categories are enabled ... and `drop_idx[i]`
corresponds to an infrequent category, then the entire infrequent category is dropped" — i.e. the docstring
promises exactly the behaviour the code refuses. Verdict: **bug** (wrong exception type for string categories,
1.3+) and **documentation/implementation contradiction** (the docstring describes dropping the infrequent group;
the code explicitly forbids it — one of the two must change).

### 6. `normalize(X, return_norm=True)`: norm of an all-zero row reported as 1.0 — all builds
Measured: rows `[3, -4, 0]`, `[0, 0, 0]`, ... give `norms = [5, 1, sqrt3, sqrt10.5]`. Library (`_data.py`,
`normalize`, line 2082): `norms = _handle_zeros_in_scale(norms, copy=False)` replaces zero norms by 1 *before*
returning them, so the returned array is the divisor actually used (`X == Z * norms[:, None]` holds exactly; that
companion check passes). Documentation: `return_norm : bool ... Whether to return the computed norms.` The
"computed norm" of a zero vector is 0. Verdict: **documentation gap** (minor: say "the norms used for scaling;
zero norms are reported as 1").

### 7./8. `extract_patches_2d(max_patches=...)` samples patch positions with replacement — all builds
Measured on a 5×6 image with (2, 3) patches (16 possible): `max_patches=100` returns 16 patches of which only 10
are distinct; `max_patches=12` returns 8 distinct patches of 12 (random_state=0). Library
(`feature_extraction/image.py`, lines 450–451): `i_s = rng.randint(i_h - p_h + 1, size=n_patches)`,
`j_s = rng.randint(i_w - p_w + 1, size=n_patches)` — independent draws with replacement; and
`_compute_n_patches` (lines 284–285) maps `max_patches >= all_patches` to `all_patches` but the random path is still
taken, so asking for "at most all patches" does not return all patches. Documentation: "max_patches: The maximum
number of patches to extract ... If `max_patches` is None it corresponds to the total number of patches that can
be extracted" and Returns: "`n_patches` is either `max_patches` or the total number of patches that can be
extracted". Nothing says the sample is drawn with replacement or that duplicates are returned. Verdict:
**documentation gap / questionable design** (duplicates waste the patch budget; `max_patches >= total` should
arguably return the ordered full set). Same on all builds; `PatchExtractor` inherits it.

### 9. `PowerTransformer` on float32 input: lambdas_ differ from the float64 MLE by 1.1e-4 — 1.1.3, 1.2.2, 1.3.2, 1.5.2 (1.9.1 ok)
Measured: `lambdas_ = [-0.42437177, 0.80783039]` on the float32 copy vs `[-0.42448068, 0.80761873]` on float64
(my mpmath MLE agrees with the float64 values to 2e-8); the unstandardised transform differs by 2.6e-4 relative.
Library (1.5.2 `_data.py`, `PowerTransformer._yeo_johnson_optimize`): the profile likelihood
`-n/2 log(var(x_trans)) + (lambda-1) sum(sign(x) log1p|x|)` is evaluated in the input dtype and minimised with
`optimize.brent(..., brack=(-2, 2))`, whose stopping test is defeated by float32 rounding of the objective. 1.9.1
delegates to `scipy.stats.yeojohnson(x, lmbda=None)` (`_yeo_johnson_optimize`, main) and its `_fit` computes the
moments with `dtype=np.float64`; there the float32 result agrees to 1e-7. Documentation promises nothing about
float32 precision. Verdict: **precision limitation of the old builds, fixed by 1.9.1** (not a bug against the
docs; recorded because the 1e-4 error in lambda propagates to the transform).

### 10. `PowerTransformer(yeo-johnson)` on a constant column raises `scipy.optimize BracketError` — 1.1.3, 1.2.2 (1.3.2+ ok)
Measured: `PowerTransformer().fit([[1.0], [1.0], [1.0]])` raises `BracketError: The algorithm terminated without
finding a valid bracket` from `optimize.brent` (the negative log-likelihood is `+inf`/`nan` for every lambda when
`var(x_trans) == 0`, see the `x_trans_var < x_tiny` guard in the old `_neg_log_likelihood`). From 1.3 the
optimiser handles this and 1.9.1 returns `lambdas_ = [1.0]` and an all-zero transform. Documentation: no statement
about constant features, but a scaler-like transformer that crashes on a constant column is not expected
behaviour. Verdict: **bug in 1.1/1.2, fixed in 1.3**.

## What held up (selection; see the .out files for the ~435 lines)
* `PolynomialFeatures`: column order `[1, a, b, c, a^2, ab, ac, b^2, bc, c^2]`, `powers_`, `interaction_only`,
  `include_bias`, `degree=(min, max)` incl. the documented `min_degree 0 == 1`, `n_output_features_ = C(n+d, d)`,
  csr/csc input, float32 dtype, `order='F'`, `get_feature_names_out` — all exact.
* `SplineTransformer`: basis values inside the range equal Cox–de Boor to 1e-16 for degrees 0–3, uniform /
  quantile / array knots, `n_features_out_`, partition of unity, `include_bias=False` (last spline dropped),
  the four extrapolation modes (except the degree-0 constant case above), periodic wrapping with non-uniform
  knots, `extrapolation='error'` (boundary values accepted), sparse output equal to dense, float32.
* `Binarizer` strictness (`> threshold` → 1, `== threshold` → 0), sparse rule; `LabelBinarizer` (multiclass /
  binary single column / `neg_label`,`pos_label` / sparse / inverse threshold `(pos+neg)/2` and strictness /
  multilabel input); `label_binarize` (`pos_label=0` switch); `MultiLabelBinarizer` (order, warning text,
  sparse, inverse); `OrdinalEncoder` (order, dtype, unknown value / NaN, `encoded_missing_value`, None vs nan as
  documented, infrequent categories with the user-guide examples, inverse to `'infrequent_sklearn'`).
* `OneHotEncoder`: docstring examples, `drop='if_binary'`, `drop=array`, `drop='first'` single category,
  `min_frequency` int/float thresholds exactly at the boundary (`count == min_frequency` frequent,
  `count < min_frequency * n` infrequent), `min_frequency` + `max_categories` precedence, `max_categories=1`,
  `handle_unknown='infrequent_if_exist'` with and without an infrequent group, `'warn'`, drop after grouping,
  `feature_name_combiner`, `sparse_output`, `dtype`, given categories, missing values.
* `TargetEncoder` (1.3+): `encodings_` equal the documented shrinkage formula for `smooth` 0 / 1 / 5 / `'auto'`
  (binary and continuous), `target_mean_`, unseen → target mean, `fit().transform()` = plain lookup,
  `fit_transform` = fold-by-fold cross fitting (KFold contiguous folds, StratifiedKFold folds, shuffled KFold with a
  seed), the stored full-data `encodings_`, multiclass ordering `f0_c0, f0_c1, ...`, `target_type='auto'`,
  the 1.9 `FutureWarning` for `shuffle`/`random_state`.
* `MaxAbsScaler` (partial_fit, csr/csc, zero column, clip, NaN), `Normalizer` l1/l2/max, `KernelCenterer`
  (fit and new data, exact), `FunctionTransformer` (inverse, `check_inverse` warning, `validate`, kw_args,
  feature names), Yeo–Johnson `lambdas_` (mpmath MLE, 2e-8) and the piecewise transform / standardisation /
  inverse / NaN handling, `QuantileTransformer` normal output = `Phi^-1` of the empirical CDF with the
  `1e-7` clip bounds (`±5.199338`), out-of-range mapping, subsample determinism, `add_dummy_feature`
  (dense / csr / csc / coo), all function forms equal the classes, `RobustScaler` `quantile_range` /
  `unit_variance` (`Phi^-1(0.9) - Phi^-1(0.1)`), `StandardScaler(with_mean=False)` on sparse (exact variance).
* Text: docstring examples, regex reference tokenizer, `lowercase`, `stop_words='english'` (frozenset of 318,
  removed before n-grams), word / char / char_wb n-grams (padding, short-word rule), `min_df` / `max_df`
  int and float boundaries, `max_features` (top frequencies; tie at the cutoff resolved alphabetically —
  undocumented, printed), `binary`, given vocabulary (list / dict / gaps), callable analyzer, `strip_accents`
  ascii / unicode, capturing-group token pattern, dtype, inverse_transform, error cases; tf-idf for all 12
  (`smooth_idf`, `sublinear_tf`, `norm`) combinations to 1e-12, `TfidfVectorizer` = Count + Transformer;
  `HashingVectorizer` / `FeatureHasher` columns and signs recomputed with `murmurhash3_32` (dict / pair /
  string input, `alternate_sign`, `binary`, l2 norm, docstring example, zero values dropped, utf-8);
  `DictVectorizer` (one-hot of strings, sort / no sort, separator, inverse, unseen features, sequences of strings,
  `restrict`).
* Image: patch count / order / channels, `max_patches` int / float / determinism, reconstruction exact incl.
  perturbed overlapping patches, `PatchExtractor`, `grid_to_graph` (4- and 6-connectivity + self loops),
  `img_to_graph` gradient weights, masks.
* Impute: `KNNImputer` for `n_neighbors` 1–3 × uniform / distance recomputed exactly, new rows, all-NaN rows →
  column means, more neighbours than donors, `add_indicator`, `keep_empty_features`, float32, `missing_values=-1`;
  `MissingIndicator` (`missing-only` / `all`, `error_on_new`, sparse); `SimpleImputer` most_frequent ties →
  smallest (numeric and strings), constant defaults, strings, `keep_empty_features`, callable strategy,
  sparse mean with explicit zeros; `IterativeImputer` (`max_iter=0` = initial strategy, one and two rounds of
  exact chained OLS for every `imputation_order`, ascending / descending tie order, random order permutations,
  `skip_complete` in fit and transform, per-feature clipping, the documented stopping criterion reproduced for
  four tolerances, `ConvergenceWarning`, `sample_posterior` determinism / no early stopping, single feature,
  `add_indicator`, `keep_empty_features`, `fill_value`).
* Compose / pipeline: `ColumnTransformer` output order, remainder drop / passthrough / estimator, selection by
  index / slice / bool / callable, `transformer_weights`, `sparse_threshold` rule at density 0.4 for four
  thresholds, all-dense ignore, feature names (verbose True / False / template / callable, remainder prefix,
  duplicate error), `'drop'` / `'passthrough'` transformers, `make_column_transformer` naming;
  `TransformedTargetRegressor` (func / inverse_func and transformer paths against exact OLS, prediction = exact
  inverse, `check_inverse` warning, validation errors, score); `Pipeline` (chain = manual, predict_proba /
  decision_function passthrough, slicing / indexing, `score` with `sample_weight` = weighted accuracy, passthrough /
  None steps, nested `set_params`, joblib memory caching reuses the fitted transformer with identical results,
  feature names, inverse_transform, TypeError for a bad step); `FeatureUnion` (order, weights, names, drop /
  passthrough, sparse stacking); `make_pipeline` / `make_union` naming with `-1`/`-2` suffixes.

## Not checked and why
* `ColumnTransformer` selection by column name, `make_column_selector(dtype_include=...)` and
  `set_output(transform='pandas')`: all require a DataFrame; pandas is not installed in any of the five
  environments (the harness prints a note). The numpy-array error for string selectors is checked.
* `TargetEncoder` on 1.1.3 / 1.2.2, `OrdinalEncoder` infrequent categories before 1.3, `SplineTransformer`
  sparse output where the parameter does not exist, `handle_unknown='warn'` before 1.6, string/callable
  `verbose_feature_names_out` before 1.6, callable `SimpleImputer` strategy before 1.5: skipped by version guards.
* `TargetEncoder` binary cross fitting uses the library's `StratifiedKFold(5)` (unshuffled) only to obtain the
  fold indices (the continuous case uses hand-built contiguous folds); the encodings themselves are recomputed.
* `CountVectorizer(max_features)` tie order at the cutoff is not documented; the harness prints the measured
  order (alphabetical first, from the pre-sort + `argsort` in `_limit_features`) without judging it.
* `SplineTransformer` exterior knot positions (spaced like the first / last knot interval) are taken from the
  source comment, not the docstring, which only says "`degree` number of knots are added"; the B-spline values
  on the base interval depend on them.
* `HashingVectorizer` / `FeatureHasher` collisions are verified against `sklearn.utils.murmurhash3_32` because
  that is the documented hash; the hash function itself is not re-implemented.
