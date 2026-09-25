# scikit-learn full inspection: findings ledger

_Full inspection requested 2026-09-25 ("a full inspection of sklearn and numpy since they are so heavily
used"), independent of what the survey papers call. Nine harness groups (`verify/k8` … `k16`, plus the
round-6 `k1` … `k7`) executed on 1.9.1 and on 1.1.3, 1.2.2, 1.3.2 and 1.5.2 against independent truths
(exact rational or mpmath recomputations, closed forms, plain-Python reimplementations of the documented
algorithms). Each group's `verify/<group>.notes.md` has one paragraph per failing check with the source
lines; this page collects the verdicts. "By hand" means the finding was reproduced again outside the
harness before it was recorded here. Nothing is filed; the filing cap (two unanswered filings per
repository) applies._

## Bugs in the current release (1.9.1) and on `main`

| id | finding | builds | by hand | prior report | fix |
|---|---|---|---|---|---|
| SK1 | `PCA` `covariance_eigh` (the `auto` choice for tall dense data since 1.5) loses the variance of offset features: float32 values around 100 give `explained_variance_` 33 % off | 1.5+ | yes | none found | branch, verified |
| SK4 | `SVC(kernel='precomputed')` with zero sample weights predicts from the wrong kernel columns: `support_` indexes libsvm's reduced problem; 4 of 8 test predictions flip, silently | 1.1–1.9 | yes | #25380 (null sample weights, open) to be read | — |
| SK5 | `KernelDensity` / `KDTree` / `BallTree.kernel_density` with the cosine kernel mis-normalised in even dimensions: the 2-D density integrates to 0.363, NaN in 4-D | 1.1–1.9 | yes | none found yet | — |
| SK6 | `r_regression(y, y)` = 1.0000000000000002 for about a quarter of random targets, so `f_regression` gives F = −6.3e16 and p = 1 to a feature equal to (or a multiple of) the target and `SelectKBest(f_regression)` drops it | 1.1–1.9 | yes | #11395 (constant columns) related | — |
| SK7 | `TSNE(method='exact', metric='precomputed').fit(D)` squares the caller's `D` in place; a read-only `D` raises | 1.1–1.9 | yes | none found yet | — |
| SK8 | `GaussianNB.partial_fit` removes the previous chunk's smoothing with the new chunk's `epsilon_` (var_ 2 % off at var_smoothing 0.1) | 1.1–1.9 | yes | #14054 / #24732 to be read | branch, verified |
| SK9 | `DummyRegressor(strategy='median'/'quantile')` with unit sample weights differs from no weights (2.0 vs 2.5 for y = 1..4) | 1.1–1.9 | yes | #32289 related | median branch, verified |
| SK10 | `GaussianProcessClassifier(n_restarts_optimizer>0)` draws restarts as exp(uniform(log bounds)): they start outside the bounds | 1.1–1.9 | yes (code) | none found | branch, verified |
| SK11 | `IsotonicRegression` with one distinct X ignores `out_of_bounds` | 1.1–1.9 | yes | none found | branch, verified |
| SK12 | PLS `intercept_` does not satisfy the documented `y = X @ coef_.T + intercept_` on uncentred X (30–40 % off) | 1.1–1.9 | yes | none found | branch, verified |
| SK13 | `NuSVC(class_weight=...)` has no effect | 1.1–1.9 | harness | #30332 by title | — |
| SK14 | `KernelDensity(bandwidth='scott'/'silverman')` ignores the data scale | 1.3–1.9 | harness | #26658 by title | — |
| SK15 | `Halving*SearchCV` `n_required_iterations_` / `n_possible_iterations_` one short when the ratio is an exact power of the factor (`floor(log(243, 3)) = 4`) | 1.1–1.9 | yes (the rounding) | none found yet | — |
| SK16 | `r_regression` on a constant column returns ±inf (`force_finite` only catches NaN) | 1.1–1.9 | harness | #11395 related | — |
| SK17 | `VarianceThreshold().variances_` reports min(variance, peak-to-peak) | 1.1–1.9 | harness | none found yet | — |
| SK18 | `SelectFromModel(ElasticNetCV(l1_ratio=1)).threshold_` reports the mean while 1e-5 is applied | 1.9 (regression after 1.5.2) | harness | none found yet | — |
| SK19 | `jaccard_score(zero_division=np.nan)` rejected although documented | 1.9 | yes | none found yet | — |
| SK20 | `NeighborhoodComponentsAnalysis.n_iter_` one more than the iterations run | 1.1–1.9 | harness | none found yet | — |
| SK21 | MLP `sgd`/`adam` add the L2 penalty once per mini-batch: `alpha` means α/batch_size relative to `lbfgs` | 1.1–1.9 | harness | none found yet | — |
| SK22 | `SplineTransformer(degree=0, extrapolation='constant')` raises at transform | 1.1–1.9 | harness | none found yet | — |
| SK23 | `normalize(return_norm=True)` reports 1 for an all-zero row | 1.1–1.9 | harness | none found yet | — |
| SK24 | `extract_patches_2d(max_patches=k)` samples with replacement (8 distinct of 12) | 1.1–1.9 | harness | none found yet | — |
| SK25 | `DecisionTreeClassifier(class_weight='balanced')` splits a pure node whose gini rounds to 1.1e-15 | 1.1–1.9 | harness | none found yet | — |
| SK26 | `MinCovDet` 1-D branch is the shortest-half estimator, not the MCD subset; `correct_covariance()` mutates `dist_` | 1.1–1.9 | harness | none found yet | — |
| SK27 | liblinear (`LinearSVC`/`LinearSVR`) stalls at `tol <= 1e-12` on some data | 1.1–1.9 | harness | #22283 by title | — |
| SK28 | `GenericUnivariateSelect(mode='k_best', param=3.0)` raises | 1.1–1.9 | harness | none found yet | — |
| SK29 | Float rounding in `ShuffleSplit`/`train_test_split`/`RFE` sizes (0.07 × 100 → 8) | 1.1–1.9 | harness | none found yet | — |

## Documentation errors and gaps (current release)

AdaBoost binary `decision_function` range (branch ready); NMF `reconstruction_err_` (branch ready, SK2);
OAS "omitting the 2/p terms" justification; `Lars` rejects the documented `np.inf`; `LassoLarsIC` noise
variance n − p − 1; `LassoLarsCV.mse_path_` shape; HuberRegressor `tol`; OneHotEncoder infrequent tie rule
and dropping an infrequent category; `pairwise_distances` still lists `sokalmichener`; the scorer table
omits three scorers; the user guide's weighted one-vs-one AUC formula lacks its normalisation;
`KFold(shuffle=False, random_state=…)` raises; GroupKFold / StratifiedGroupKFold balancing statements;
TimeSeriesSplit formula and max `test_size`; `cross_validate` return_indices type; learning_curve float
sizes; halving table floor vs ceil, float factor, random_state condition; `FixedThresholdClassifier`
boundary; VarianceThreshold "lower than"; SFS `auto` with `tol=None`; SVC binary Platt coupling;
NearestCentroid priors default; `OneClassSVM.offset_` type; Nystroem on indefinite kernels; JL bound
rounding; brute-force neighbours at large offsets; multi-output MLP `loss_`; MLP `t_`; `make_classification`
truncation; `make_sparse_uncorrelated` noise; `make_gaussian_quantiles` remainder; `type_of_target`
single-row and sequence-of-sequences cases; GBC `train_score_` factor; HGBT categorical cardinality wording;
RandomForest `class_weight` in the bootstrap (1.9 changelog); forest `max_samples` rounding change.

## Fixed in a later release (recorded, nothing to file)

Tree missing-value splits (1.8/1.9), multi-output `friedman_mse` (removed 1.9), `top_k_accuracy` scorer (1.4),
`f1_score` 'samples' zero_division (1.4), `d2_log_loss_score` labels (1.7), `rank_test_score` with NaN
(1.2), smacof stress and non-metric symmetry (1.7), KMeans `tol` stop (1.3).

## Held up

See the "held up" section of each group's notes: every metric, every pairwise distance and kernel, every
splitter and search schedule, the linear models' KKT conditions, the trees against a plain-Python builder,
the boosting stages, the forests' bootstrap and OOB, the naive Bayes posteriors, the GP posteriors and
likelihoods, the manifold reconstructions, the MLP gradients, the dataset generators and the utilities.
