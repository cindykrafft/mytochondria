# scikit-learn full inspection: findings ledger

_Full inspection requested 2026-09-25 ("a full inspection of sklearn and numpy since they are so heavily
used"), independent of what the survey papers call. Nine harness groups (`verify/k8` … `k16`, plus the
round-6 `k1` … `k7`) executed on 1.9.1 and on 1.1.3, 1.2.2, 1.3.2 and 1.5.2 against independent truths
(exact rational or mpmath recomputations, closed forms, plain-Python reimplementations of the documented
algorithms). Each group's `verify/<group>.notes.md` has one paragraph per failing check with the source
lines; this page collects the verdicts. "By hand" means the finding was reproduced again outside the
harness before it was recorded here. Nothing is filed yet; see "Filing order" below._

## Bugs in the current release (1.9.1) and on `main`

| id | finding | builds | by hand | prior report | fix |
|---|---|---|---|---|---|
| SK1 | `PCA` `covariance_eigh` (the `auto` choice for tall dense data since 1.5) loses the variance of offset features: float32 values around 100 give `explained_variance_` 33 % off | 1.5+ | yes | none found | branch, verified |
| SK4 | `SVC(kernel='precomputed')` with zero sample weights predicts from the wrong kernel columns: `support_` indexes libsvm's reduced problem; 4 of 8 test predictions flip, silently | 1.1–1.9 | yes | **known root cause**: #25380 (open, Bug): with zero weights libsvm's `remove_zero_weight` leaves `support_` indexing the reduced problem, diagnosed by a maintainer; fix PR #27763 open. The precomputed-kernel misprediction is not mentioned there | possible comment on #25380 or #27763 with the precomputed case as a test (PR #27763's review threads to be read first) |
| SK5 | `KernelDensity` / `KDTree` / `BallTree.kernel_density` with the cosine kernel mis-normalised in even dimensions: the 2-D density integrates to 0.363, NaN in 4-D | 1.1–1.9 | yes | none (four phrasings); #25623 and #26658 are the bandwidth-scale reports, a different defect | queued (second, after SK6) |
| SK6 | `r_regression(y, y)` = 1.0000000000000002 for about a quarter of random targets, so `f_regression` gives F = −6.3e16 and p = 1 to a feature equal to (or a multiple of) the target and `SelectKBest(f_regression)` drops it | 1.1–1.9 | yes | none for r > 1; #11395 (constant columns, open) and its PR #34834 (open, 2026-08-28) clamp the centred squared norms at zero, which does not touch a correlation of 1 + 2^-52 | queued; the text must link #11395 / #34834 |
| SK7 | `TSNE(method='exact', metric='precomputed').fit(D)` squares the caller's `D` in place; a read-only `D` raises | 1.1–1.9 | yes | none (three phrasings); #31907 (HDBSCAN mutates a precomputed matrix, closed) is the sibling fix | queued |
| SK8 | `GaussianNB.partial_fit` removes the previous chunk's smoothing with the new chunk's `epsilon_` (var_ 2 % off at var_smoothing 0.1) | 1.1–1.9 | yes | **known**: #14054 (open, help wanted: `var_smoothing` undocumented, `epsilon_` redefined at each `partial_fit`) and #24732 (open, Bug: rethinking the smoothing, the subtraction noted) | branch, verified: can be offered on #24732 once SK1/SK2 are answered |
| SK9 | `DummyRegressor(strategy='median'/'quantile')` with unit sample weights differs from no weights (2.0 vs 2.5 for y = 1..4) | 1.1–1.9 | yes | none specific; #32289 (open, `_weighted_percentile(average=True)` with float weights; maintainers see no bug) is adjacent, and the fix relies on `average=True` giving the unweighted median for integer weights, which that thread confirms | median branch, verified |
| SK10 | `GaussianProcessClassifier(n_restarts_optimizer>0)` draws restarts as exp(uniform(log bounds)): they start outside the bounds | 1.1–1.9 | yes (code) | none found | branch, verified |
| SK11 | `IsotonicRegression` with one distinct X ignores `out_of_bounds` | 1.1–1.9 | yes | none found | branch, verified |
| SK12 | PLS `intercept_` does not satisfy the documented `y = X @ coef_.T + intercept_` on uncentred X (30–40 % off) | 1.1–1.9 | yes | none found | branch, verified |
| SK13 | `NuSVC(class_weight=...)` has no effect | 1.1–1.9 | harness | **known**: #30332 (open); a contributor says the user guide states NuSVC ignores `class_weight`, another that the guide sentence is itself wrong | nothing to file |
| SK14 | `KernelDensity(bandwidth='scott'/'silverman')` ignores the data scale | 1.3–1.9 | harness | **known**: #26658 and #25623 (both open, Bug; maintainers agree, approach discussed) | nothing to file |
| SK15 | `Halving*SearchCV` `n_required_iterations_` / `n_possible_iterations_` one short when the ratio is an exact power of the factor (`floor(log(243, 3)) = 4`) | 1.1–1.9 | yes (the rounding) | none (three phrasings) | queued |
| SK16 | `r_regression` on a constant column returns ±inf (`force_finite` only catches NaN) | 1.1–1.9 | harness | **known**: #11395; PR #34834 clamps the squared norms, which covers it | nothing to file |
| SK17 | `VarianceThreshold().variances_` reports min(variance, peak-to-peak) | 1.1–1.9 | harness | none (searched 2026-09-25); #15118 is a feature request | queued |
| SK18 | `SelectFromModel(ElasticNetCV(l1_ratio=1)).threshold_` reports the mean while 1e-5 is applied | 1.9 (regression after 1.5.2) | harness | none found yet | — |
| SK19 | `jaccard_score(zero_division=np.nan)` rejected although documented | 1.9 | yes | none; #27563 / #22625 added `nan` to the other metrics | queued (small) |
| SK20 | `NeighborhoodComponentsAnalysis.n_iter_` one more than the iterations run | 1.1–1.9 | harness | none | queued |
| SK21 | MLP `sgd`/`adam` add the L2 penalty once per mini-batch: `alpha` means α/batch_size relative to `lbfgs` | 1.1–1.9 | harness | none; #21891 is the same scaling question for `SGDRegressor` | queued |
| SK22 | `SplineTransformer(degree=0, extrapolation='constant')` raises at transform | 1.1–1.9 | harness | none | queued |
| SK23 | `normalize(return_norm=True)` reports 1 for an all-zero row | 1.1–1.9 | harness | none found yet | — |
| SK24 | `extract_patches_2d(max_patches=k)` samples with replacement (8 distinct of 12) | 1.1–1.9 | harness | none found yet | — |
| SK25 | `DecisionTreeClassifier(class_weight='balanced')` splits a pure node whose gini rounds to 1.1e-15 | 1.1–1.9 | harness | none found yet | — |
| SK26 | `MinCovDet` 1-D branch is the shortest-half estimator, not the MCD subset; `correct_covariance()` mutates `dist_` | 1.1–1.9 | harness | none found yet | — |
| SK27 | liblinear (`LinearSVC`/`LinearSVR`) stalls at `tol <= 1e-12` on some data | 1.1–1.9 | harness | **known**: #22283 (open) | nothing to file |
| SK28 | `GenericUnivariateSelect(mode='k_best', param=3.0)` raises | 1.1–1.9 | harness | none found yet | — |
| SK29 | Float rounding in `ShuffleSplit`/`train_test_split`/`RFE` sizes (0.07 × 100 → 8) | 1.1–1.9 | harness | none found yet | — |

## Filing order (2026-09-25)

Prior reports were checked by searching the tracker (ten topics, three or four phrasings each, and
searches for SK17–SK22). The matching threads were read in full through a helper session (artifact
"Mytochondria threads scikit-learn triage": #25380, #16298, #30332, #26658, #22283, #11395, #14054,
#24732, #32289, #26520, #25623, #12408).

The cap is already filled by the round-6 pair in the kit, which the full inspection does not displace:
**SK1** (PCA `covariance_eigh`, issue first, PR after triage) and **SK2** (NMF docstring). Both are
still unfiled. The full inspection queues these behind them, in order, one at a time as earlier
filings are answered:

1. **SK6**: `f_regression` p = 1 for a feature equal to the target. It is silent, it reaches
   `SelectKBest` in every feature-selection pipeline, and #34834 does not cover it.
2. **SK5**: the cosine-kernel KDE is mis-normalised in even dimensions.
3. **SK7**: TSNE squares a caller's precomputed matrix in place.
4. The fixes already on branches: SK12 (PLS `intercept_`), SK10 (GPC restarts), SK11 (isotonic, one
   distinct X), SK9 (DummyRegressor median), SK8 (as an offer on #24732).
5. The small ones: SK19, SK20, SK17, SK15, SK22, SK21, SK23–SK29.

SK4 is a possible comment on #25380 / PR #27763, which has not been drafted: PR #27763's review
threads have not been read yet. Nothing to file for SK13, SK14, SK16 and SK27 (already reported).
scikit-learn's Automated Contributions Policy applies to every one of these, as to SK1/SK2: fact
sheets that the submitter rewrites, and no code PR before "Needs Triage" is removed.

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
