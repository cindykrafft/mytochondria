# scikit-learn audit against 322 published papers (2021–2026)

_Generated 2026-09-25 against `scikit-learn/scikit-learn` `main` @ `857849927d` by reading, executed on
the 1.9.1 wheel and on 1.1.3, 1.2.2, 1.3.2 and 1.5.2, and on 1.9.1 with the PCA fix applied. Focus: the
numbers that reach the papers — PCA, the classification, ranking, regression and clustering metrics,
k-means and the mixture models, the scalers and discretisers, cross-validation and the linear models —
checked against exact recomputations (`fractions.Fraction`, closed forms, `scipy` references)._

## What this is

The six-journal survey found **322 papers** in PNAS, *Nature*, *Cell* and *Science*, 2021–2026, that
name scikit-learn in their methods, usually beside SciPy (111), UMAP (92) or NumPy (74): PCA in 55,
random forests and logistic regression in 23 each, hierarchical clustering and the linear models in 20
each, cross-validation in 16, k-means in 13, NMF in 11, clustering metrics in 8, AUC in 6. Every
function in that list was exercised on generated data and compared with an exact recomputation or the
published definition (`verify/_synth.py`: exact AUC, ROC points, average precision, PRF, MCC, kappa,
balanced accuracy, log loss, R², ARI, MI, NMI, silhouette).

## Findings (details and line citations in [`component-reviews/pca-metrics-clustering-preprocessing.md`](component-reviews/pca-metrics-clustering-preprocessing.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **SK1** | **CONFIRMED on 1.5.2 and 1.9.1** (`main` by reading; every release since 1.5.0); not on 1.3.2 and earlier, where `auto` chose `full`; no prior report | now (issue; PR after triage) | `PCA`'s `covariance_eigh` solver, which `svd_solver="auto"` selects for dense data with ≤ 1000 features and ≥ 10× as many samples, forms the covariance as `X.T @ X − n·mean⊗mean` and loses the variance of features with a common offset to cancellation: with unit-scale variation, float32 values around 100 give `explained_variance_` 33 % off, around 1e3 87 % off (ratio 54 %); float64 values around 1e6 1.7 % off, 1e7 20 % (PC1 scores 3.5 %), 1e8 meaningless. The `full` solver (the `auto` choice up to 1.4) is exact in every case. Fix verified: batched centred accumulation with the same memory footprint; `test_pca.py` passes, the new test fails on `main`. |
| **SK2** | **CONFIRMED on every build** | ready (documentation issue or direct doc PR) | `NMF.reconstruction_err_` and `MiniBatchNMF.reconstruction_err_` are documented as "Frobenius norm … or beta-divergence" but are `sqrt(2 · D_β)` for every loss: 40.12 for a KL divergence of 804.56. Docstring patch ready. |
| SK3 | note, documented; open upstream as #31210 (2025) and #24502 | held | `euclidean_distances` (dot-product expansion) on float64 data with a common offset: relative error 1.6e-6 at 1e4, 2.8e-2 at 1e6, 24 at 1e8; `silhouette_score` 0.717 for a true 0.674 at 1e8. `KMeans` unaffected. |
| N1 | note, documented | held | `LogisticRegression(penalty=None)` at the default `tol=1e-4` stops 2.7e-3 relative from the exact MLE (`tol=1e-8`: 1.9e-7). |
| N2 | note, release-noted | held | `KBinsDiscretizer(strategy='quantile')` edges use `averaged_inverted_cdf` since 1.9 (linear before). |
| N3 | note | held | `roc_auc_score` with one class in `y_true` returns `nan` with a warning in 1.9 where 1.1–1.5 raised `ValueError`. |
| N4 | note, documented behaviour (#16081) | held | When `KMeans` stops on `tol`, `cluster_centers_` are the means under the previous labelling (2e-2 apart on 1.1.3 / 1.2.2 for the harness data; 1.3+ converge strictly on it). |

**Held up under execution (all five builds):** every ranking and classification metric checked
(`roc_auc_score` with ties, `ovr` / `ovo`, `max_fpr`; `roc_curve`; `average_precision_score`; PRF with
every `zero_division` rule; MCC; kappa; balanced accuracy; `log_loss`; `confusion_matrix`), the
regression metrics, ARI / MI / NMI / AMI (exact expected MI) / V-measure / Fowlkes–Mallows, silhouette,
Calinski–Harabasz, Davies–Bouldin, `PCA(full / arpack / randomized)` in full, `StandardScaler`,
`MinMaxScaler`, `RobustScaler`, `normalize`, `KMeans` (incl. float32 and offsets), `GaussianMixture`
(four covariance types, BIC), `DBSCAN`, `AgglomerativeClustering` (four linkages vs scipy), `KFold`,
`StratifiedKFold`, `train_test_split`, `cross_val_score`, `GridSearchCV`, `permutation_test_score`,
`calibration_curve`, `LinearRegression`, `Ridge`, `LogisticRegression` probabilities and
`class_weight`, `RandomForest` importances and OOB, `mutual_info_classif`, NMF Frobenius error, LDA,
`f_classif`, `f_regression`, `KernelDensity`, `KBinsDiscretizer`, `QuantileTransformer`,
`PowerTransformer`, `permutation_importance`, `SimpleImputer`, the encoders, `TSNE` guards. Not checked:
SVM, gradient boosting, HDBSCAN / OPTICS, spectral methods, Gaussian processes, the manifold embeddings'
numbers, MLP.

## Verification method

`verify/k1_classification_ranking_metrics.py`, `k2_regression_clustering_metrics.py`,
`k3_pca_scaling_clustering.py`, `k4_model_selection_linear.py`, `k5_precision_and_second_tier.py`,
`k6_offsets_and_misc.py` and `k7_pca_solver_offsets.py` (every PCA solver on 400 × 2 and 20000 × 5 data
with offsets 0 to 1e8 in float64 and 0 to 1e4 in float32). Each runs under the interpreter given; `.out`
is 1.9.1, `.v<version>.out` the older wheels, `k7 … .patched.out` the 1.9.1 install with the fix
(62 / 62; unpatched 42 / 62).

## How the papers use scikit-learn (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 31 (1.0.2 ×8, 0.21.3 ×6, 1.2.2 ×5, 0.24.2 ×4, 1.3.2 ×3; 1.5.x ×4, 1.6.x ×2, 1.7.2 ×1 name a release with SK1) |
| PCA | 55 |
| random forest / extra trees; logistic regression | 23; 23 |
| hierarchical clustering; linear / ridge / lasso / elastic net | 20; 20 |
| gradient boosting; SVM; cross-validation | 19; 18; 16 |
| scalers; accuracy / precision / recall / F1; k-means | 15; 15; 13 |
| manifold (t-SNE / MDS / Isomap); nearest neighbours; DBSCAN / HDBSCAN | 13; 12; 11 |
| NMF; Gaussian mixture; feature importance | 11; 10; 10 |
| silhouette / ARI / NMI; AUC / ROC | 8; 6 |
| co-packages: SciPy 111, UMAP 92, NumPy 74, Matplotlib 59, Scanpy 51, seaborn 50, Seurat 44 | |

The profile (`sklearn_profile.py`, `sklearn_profiles.jsonl`, `profile_run.log`) ran on the survey's
stored evidence sentences (no route to Europe PMC from this session), so the counts are lower bounds.

## Filing channel

scikit-learn's contributing guide carries an **Automated Contributions Policy**: no issues or PRs from
fully automated tools, AI-generated code only after personal review and testing, "do not paste AI
generated text in the description of issues, PRs or in comments", AI use stated in the PR
description (the PR template has a disclosure list); bug reports get the "Needs Triage" label and a PR
is not to be opened until it is removed. The kit in [`upstream/`](upstream/) therefore gives the facts,
reproducers, numbers and patches for the submitter to write from in their own words, and the PR for
SK1 follows the issue's triage. Seven prior threads read in full (see the kit README): none reports
SK1 or SK2. Fork of `scikit-learn/scikit-learn` needed.

## Files

| path | what |
|---|---|
| `component-reviews/pca-metrics-clustering-preprocessing.md` | the review: SK1–SK3, N1–N4, held-up list, version scope |
| `verify/k1_…py` … `k7_…py`, `_synth.py`, `*.out`, `*.v<version>.out`, `k7…patched.out` | harnesses and captured output per build |
| `sklearn_profile.py`, `sklearn_profiles.jsonl`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit: issue fact sheets, two `git am`-able patches, PR bodies, test runs, channel notes |
