# scikit-learn: PCA, the metrics, clustering, preprocessing and model selection the papers use

_Reviewed 2026-09-25 against `scikit-learn/scikit-learn` `main` @ `857849927d`, executed on the 1.9.1
wheel and on 1.1.3, 1.2.2, 1.3.2 and 1.5.2 (the cohort's most-named 1.x lines), and on the 1.9.1
install with the PCA fix applied. Harnesses and outputs in `../verify/`._

## What the cohort uses (322 papers, `../sklearn_profiles.jsonl`, survey-cache lower bounds)

| use | papers |
|---|---|
| PCA | 55 |
| random forest / extra trees; logistic regression | 23; 23 |
| hierarchical clustering; linear / ridge / lasso / elastic net | 20; 20 |
| gradient boosting; SVM | 19; 18 |
| cross-validation; scalers; accuracy / precision / recall / F1 | 16; 15; 15 |
| k-means; t-SNE / MDS / Isomap; nearest neighbours | 13; 13; 12 |
| DBSCAN / HDBSCAN; NMF; Gaussian mixture | 11; 11; 10 |
| feature importance; silhouette / ARI / NMI; AUC / ROC | 10; 8; 6 |
| version stated | 31 (1.0.2 ×8, 0.21.3 ×6, 1.2.2 ×5, 0.24.2 ×4, 1.3.2 ×3, 1.5.x ×4, 1.6.x ×2, 1.7.2 ×1) |
| alongside | SciPy 111, UMAP 92, NumPy 74, Scanpy 51, Seurat 44 |

## Code read

`sklearn/decomposition/_pca.py` (`_fit`, the `auto` policy, `_fit_full`, `_fit_truncated`),
`sklearn/utils/_array_api.py` (`_cov`), `sklearn/utils/_chunking.py`, `decomposition/_nmf.py`
(`_beta_divergence`, the fit paths that set `reconstruction_err_`), `metrics/_ranking.py`
(`_binary_clf_curve`, `roc_curve`, `roc_auc_score` incl. `max_fpr` and the multiclass averages,
`average_precision_score`), `metrics/_classification.py` (precision / recall / F, `zero_division`,
`matthews_corrcoef`, `cohen_kappa_score`, `balanced_accuracy_score`, `log_loss`),
`metrics/_regression.py`, `metrics/cluster/_supervised.py` (ARI, MI, NMI, AMI with the exact
expected MI, homogeneity family, Fowlkes–Mallows), `metrics/cluster/_unsupervised.py` (silhouette,
Calinski–Harabasz, Davies–Bouldin), `metrics/pairwise.py` (`euclidean_distances`,
`_euclidean_distances_upcast`), `preprocessing/_data.py` and `_discretization.py`,
`cluster/_kmeans.py` (Lloyd / Elkan loops, the final relabelling), `mixture/_gaussian_mixture.py`,
`model_selection/_split.py`, `_search.py`, `_validation.py`, `linear_model/_ridge.py`,
`_logistic.py`, `ensemble/_forest.py`, `calibration.py`, `feature_selection/_univariate_selection.py`,
`neighbors/_kde.py`, `inspection/_permutation_importance.py`, `discriminant_analysis.py`.
Statement of intended behaviour: each docstring and the user guide; the published definitions
(Hand & Till 2001, McClish 1989, Vinh et al. 2010, Rousseeuw 1987) where the docstring cites them.

## Findings

### SK1 — `PCA`'s `covariance_eigh` solver, the `auto` choice for tall dense data since 1.5, loses the variance of features with a common offset

`_fit` selects `covariance_eigh` when `X.shape[1] <= 1_000 and X.shape[0] >= 10 * X.shape[1]` for dense
input (added by #27491 for 1.5, benchmarked as ~10× faster than `full` on 1e6 × 100 float32 data).
`_fit_full`'s branch computes

```python
C = _cov(X, ddof=1, mean=self.mean_, xp=xp)     # X.T @ X - n_samples * mean ⊗ mean, / (n_samples - 1)
```

without centring `X` (so as not to copy it). When the features share an offset μ with spread σ,
`X.T @ X` is dominated by `n μ²` and the subtraction returns `n σ²` with an absolute error of order
`n μ² ε`, i.e. a relative error of order `μ²/σ² · ε`: for float32 (ε ≈ 6e-8) that is 0.6 at μ/σ = 1e3
and already 6e-3 · (a few) at μ/σ = 1e2; for float64 (ε ≈ 1e-16) it reaches 1e-2 at μ/σ = 1e7. The
`full` solver centres first and does not have the term. Measured (`../verify/k7_pca_solver_offsets.py`,
relative error of `explained_variance_` against the exact centred eigendecomposition; `auto` and
`covariance_eigh` give identical numbers):

| dtype, n × d | offset | `covariance_eigh` (= `auto`) | ratio | PC1 scores | `full` / `arpack` / `randomized` |
|---|---|---|---|---|---|
| float32, 20000 × 5 | 1e2 | 3.3e-01 | 3.4e-01 | | 3.8e-06 |
| float32, 20000 × 5 | 1e3 | 8.7e-01 | 5.4e-01 | | 2.4e-06 |
| float32, 20000 × 5 | 1e4 | 4.5e+01 | 1.0 | | 2.2e-04 |
| float64, 20000 × 5 | 1e4 | 1.0e-06 | 1.1e-06 | 7.1e-08 | 5e-15 |
| float64, 20000 × 5 | 1e6 | 1.7e-02 | 1.7e-02 | 3.4e-04 | 1e-12 |
| float64, 20000 × 5 | 1e7 | 2.0e-01 | 1.6e-01 | 3.5e-02 | 4e-12 |
| float64, 20000 × 5 | 1e8 | 8.0e+00 | 1.0 | 3.7e-01 | 1e-10 |
| float64, 400 × 2 | 1e6 / 1e7 / 1e8 | 5.0e-04 / 1.1e-02 / 5.7e-01 | | | ≤ 3e-10 |

The float32 rows are the solver's own use case (the PR's benchmarks are float32; GPU tensors and image,
intensity and single-cell matrices are float32) and values in the hundreds with unit spread are ordinary
data. `StandardScaler` before PCA removes the offset, but PCA on raw or centred-by-the-user-only data is
what the cohort's 55 PCA papers mostly describe, and nothing in the result signals the loss.

Scope: 1.5.0 onwards (`k7 ... .v1.5.2.out` and `.out` for 1.9.1: 42 / 62 checks; `.v1.3.2.out`: 48 / 48,
`auto` → `full`, no such solver). The docstring's caveat ("compared to the `full` solver, this solver
effectively doubles the condition number and is therefore less numerically stable, e.g. on input data
with a large range of singular values") describes the eigendecomposition of a well-formed covariance;
the loss here is in forming it and is governed by mean²/variance, not by the singular-value range.
Reviewer C. Lorentzen wrote in the PR ("Note that this is numerically more unstable than np.cov.",
review thread 42) and the author's stability experiment (comment 28) used zero-mean data; #29534
(open, Bug) is a different instability of the same solver (rank-deficient data with `whiten=True`,
negative eigenvalues; linked PR #34866 closed). No prior report of the offset loss.

Fix (`../upstream/0001-…patch`, verified): for dense input accumulate `(X[batch] - mean_).T @ (X[batch]
- mean_)` over row batches sized by `get_chunk_n_rows` (the working-memory setting), which keeps the
solver's memory footprint (no full centred copy) and removes the term; sparse input keeps the post-hoc
formula (it cannot be centred without densifying). On the patched install `k7` is 62 / 62 (within 5e-6
float32 / 4e-10 float64 of exact, the same as `full`); the regression test fails on `main` in all four
parametrisations and passes with the change for four seeds; the whole `test_pca.py` passes
(`../upstream/test-runs.txt`).

### SK2 — `NMF.reconstruction_err_` is documented as "the beta-divergence" for non-Frobenius losses but is `sqrt(2 · divergence)`

Both `NMF` and `MiniBatchNMF` set the attribute with `_beta_divergence(X, W, H, self._beta_loss,
square_root=True)`, which returns `sqrt(2 · D_β(X, WH))` for every β; the docstring says "Frobenius
norm of the matrix difference, or beta-divergence". For `beta_loss='frobenius'` the two agree; for
`'kullback-leibler'` on a 60 × 20 matrix the attribute is 40.117 where the generalised KL divergence
is 804.557 and `sqrt(2 · 804.557)` = 40.114 (`../verify/k5_precision_and_second_tier.py`; the 3e-3 gap
is `transform` re-solving `W`). Every version checked. #25438 (open, 2023) is about the zero-avoidance
in the β-loss, not this. Docstring patch in `../upstream/0002-…patch`.

### SK3 — note: `euclidean_distances` / `silhouette_score` on float64 data with a large common offset

`euclidean_distances` uses the dot-product expansion `‖x‖² + ‖y‖² − 2 x·y` in float64 (the float32 path
upcasts in chunks). Relative error of the distances on four clusters of unit spread
(`k5_precision_and_second_tier.py`): 1.6e-6 at offset 1e4, 2.8e-2 at 1e6, 1.2 at 1e7, 24 at 1e8;
`silhouette_score` 0.6743 / 0.7169 for a true 0.6741 at 1e7 / 1e8 (`k6`: 0.7230 vs 0.6816 at 1e8).
`KMeans` is unaffected (its own Cython distance path; ARI 1.0 at every offset). The docstring says the
expansion "may not be as accurate as" the direct formula; #31210 (open, 2025, pairwise distances on UMAP
output) and #24502 (RFC on float32) cover the effect. Every version; held.

### N1 — note: `LogisticRegression(penalty=None)` with the default `tol=1e-4`

lbfgs stops after 12 iterations with coefficients 2.7e-3 relative (4.7e-4 absolute) from the exact MLE;
`tol=1e-8` gives 1.9e-7 in 17 iterations (`k5`). The tolerance is documented; a note for readers who
compare with `statsmodels` or R.

### N2 — note: `KBinsDiscretizer(strategy='quantile')` edges since 1.9

The quantile method changed to `averaged_inverted_cdf` (1.9 changelog); 1.1–1.5 used linear
interpolation, so bin edges and codes differ between versions for the same data (`k5`, both accepted).

### N3 — note: `roc_auc_score` with a single class in `y_true`

Returns `nan` with `UndefinedMetricWarning` in 1.9; 1.1–1.5 raised `ValueError` (`k1`). A pipeline that
caught the error now gets a silent `nan` unless it filters warnings.

### N4 — note: `KMeans` centres when the run stops on `tol`

The loop is E M E M … E: when the centre shift falls below `tol` before the labels stop changing,
`cluster_centers_` are the means under the previous labelling while `labels_` come from the final
assignment (2.0e-2 apart on 1.1.3 / 1.2.2 for the `k3` data, where `n_iter_` = 2; 1.3.2+ converge
strictly on the same data after the sample-weighted initialisation change, 2.7e-15). The behaviour is
the one discussed in #16081 (2020, open) and is consistent (`labels_` are the nearest centre, `inertia_`
matches). #34074 (2025, open) reports a related stale-labels case after empty-cluster relocation; not
hit here.

## Held up under execution (all five builds unless stated)

Ranking and classification metrics (`k1`): `roc_auc_score` with ties (Mann–Whitney), `roc_curve` with
and without `drop_intermediate`, `auc`, `average_precision_score` (step-wise), `precision_recall_curve`
end points, degenerate score vectors, precision / recall / F1 for `micro`, `macro`, `weighted` with every
`zero_division` rule, `matthews_corrcoef`, `cohen_kappa_score` (none / linear / quadratic),
`balanced_accuracy_score` with and without `adjusted`, `accuracy_score`, `confusion_matrix` orientation
and normalisation, `log_loss` (and its clipping), `roc_auc_score` `ovr` / `ovo` macro and weighted
(Hand & Till), `max_fpr` (McClish). Regression and clustering metrics (`k2`): `r2_score` (constant
`y_true`, both multioutput rules), MAE, MSE, RMSE, MAPE, `explained_variance_score`, ARI, `rand_score`,
MI, NMI (four averages), AMI with the exact hypergeometric expectation, homogeneity / completeness /
V-measure, Fowlkes–Mallows, `silhouette_score` and `silhouette_samples` (incl. singleton clusters and
`precomputed`), Calinski–Harabasz, Davies–Bouldin. PCA, scaling, clustering (`k3`): `PCA(full)`
eigenvalues, ratios, components, transform / inverse, `n_components` as an int, a float (the
"greater than" boundary) and with `arpack` / `randomized`, `noise_variance_`, `whiten`, float32 input;
`StandardScaler` (ddof 0, constant features, `partial_fit`), `MinMaxScaler`, `RobustScaler`, `normalize`;
`KMeans` labels / inertia / score / transform incl. float32 and a 1e4 offset; `GaussianMixture` score,
responsibilities and BIC for the four covariance types; `DBSCAN` boundary rules; `AgglomerativeClustering`
(single / complete / average / ward) against `scipy.cluster.hierarchy`. Model selection and linear models
(`k4`): `KFold` and `StratifiedKFold` sizes, `train_test_split` sizes and stratification,
`cross_val_score`, `GridSearchCV` mean and std, `permutation_test_score` p-value, `calibration_curve`
(both strategies), `LinearRegression`, `Ridge` (absolute `alpha`, `sample_weight` = duplication),
`LogisticRegression` probabilities / softmax / `class_weight='balanced'`, `RandomForest` importances,
OOB score and probability averaging, `mutual_info_classif`. Second tier (`k5`): `KMeans` at every offset,
NMF Frobenius error, LDA (two solvers), `f_classif`, `f_regression`, `KernelDensity` normalisation,
`KBinsDiscretizer`, `QuantileTransformer`, `PowerTransformer` (Box–Cox MLE), `permutation_importance`.
Miscellany (`k6`): `roc_curve`'s first threshold, `cross_val_predict(predict_proba)` with a class absent
from a fold, `SimpleImputer`, `LabelEncoder`, `OneHotEncoder(drop='first')`, `TSNE` guards. Not checked:
SVM, gradient boosting, `HDBSCAN`, `OPTICS`, spectral methods, Gaussian processes, the manifold
embeddings' numbers, `MLPClassifier`, `SHAP` (external).

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| SK1 | 1.5.2, 1.9.1 (and `main` by reading; every release since 1.5.0) | 1.1.3, 1.2.2, 1.3.2 (`auto` → `full`), patched |
| SK2, SK3, N1 | 1.1.3, 1.2.2, 1.3.2, 1.5.2, 1.9.1 | — (SK2: patched docstring) |
| N2, N3 | 1.9.1 differs from 1.1.3–1.5.2 | — |
| N4 | 1.1.3, 1.2.2 on the harness data (`tol` stop) | 1.3.2, 1.5.2, 1.9.1 (strict convergence on the same data) |
