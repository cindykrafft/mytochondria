# Component: Scrublet doublet-detection core — the original package and Scanpy's port

Audited: `swolock/scrublet` `master` @ `67f8ecb` (2020-12-28, "Update README.md"; the
`src/` tree is byte-identical to the PyPI **0.2.3** wheel of 2020-12-29 — only `setup.py`'s
version string differs, 0.2.2 in git), and `scverse/scanpy` `main` @ `a656a33b`
(2026-08-28, 1.14.0.dev1), `src/scanpy/preprocessing/_scrublet/` (`core.py` 474 lines,
`__init__.py` 567, `pipeline.py` 89, `sparse_utils.py` 61) together with the
`neighbors/_common.py` helpers the port routes its kNN through. Read in full:
`scrublet/scrublet.py` (587 lines) and `scrublet/helper_functions.py` (570); the port's
four files; targeted reads of `neighbors/__init__.py` (`compute_neighbors`,
`_handle_transformer`) and `_utils/random.py`.

Everything below was **executed on the shipped code**: both packages installed editable
into a Python 3.12 venv (numpy 2.5.2, scipy 1.18.1, scikit-learn 1.9.0, scikit-image
0.26.0, annoy 1.17.3, pynndescent 0.6.0), and again in a second venv holding the PyPI
scrublet 0.2.3 wheel and the scanpy 1.12.4 wheel (the latest non-prerelease). Harnesses
and their captured output are in `../verify/` (`*.out` = master venv, `*.release.out` =
release venv). The reference is an independent numpy/scipy port of the published
pipeline (`../verify/reference.py`) run on synthetic counts with labelled heterotypic
doublets (`../verify/synth.py`, 1,500 singlets of six states + 150 true doublets, 2,000
genes), so recall and precision are known.

The paper (Wolock, Lopez & Klein, *Cell Systems* 2019) could not be fetched from this
session (cell.com, bioRxiv, Europe PMC, NCBI and Semantic Scholar are all blocked), so
the closed forms below are derived here and checked against the code, not quoted.

Cohort numbers are lower bounds from the survey cache (see `../README.md`).

## Where the two implementations differ on the same input and seed

`../verify/compare_original_vs_scanpy.py` runs both on the same 1,650-cell matrix with
`random_state=0` and exact neighbours:

| step | original `scr.Scrublet(X).scrub_doublets()` | `sc.pp.scrublet(adata)` | consequence (same input, seed 0) |
|---|---|---|---|
| gene filter | mean-normalise, v-score ≥ 85th percentile, ≥ 3 normalised counts in ≥ 3 cells (`helper_functions.py:256-272`) → 300 genes | `filter_genes(min_cells=3)`, `filter_cells(min_genes=3)`, `normalize_total` (median), `highly_variable_genes` seurat flavour (`__init__.py:192-207`) → 518 genes | different feature sets by design |
| doublet parents | `np.random.seed(s); randint` with replacement (`scrublet.py:283-284`): 3,300 pairs, 1 self-pair (i,i), 3 ordered pairs repeated | `sample_comb` without replacement over the n×n grid (`core.py:222`, `_utils.py:13-23`): 3,300 pairs, 0 self-pairs here, 2 unordered pairs drawn twice | 5 unordered pairs in common; different RNG streams, both allow (i,i) |
| 1e6 normalisation | by the *full-gene* totals stored at construction (`scrublet.py:112`, `helper_functions.py:16-25`) | by the row sums of the HVG-subset matrix (`normalize_total(target_sum=1e6)`, `__init__.py:226-227`) | design |
| `log_transform` | after the 1e6 normalisation, `log10(1+x)` on both (`scrublet.py:225-227`, `helper_functions.py:106-108`) | `log1p` **before** it, on median-normalised obs and raw-sum sims (`__init__.py:220-227`) | **SR3** |
| z-score | population sd (`sparse_var`, ddof 0) | `mean_var(correction=1)`, ddof 1 (`pipeline.py:36`) | uniform factor √((n−1)/n) = 0.999697 on every gene; invariant for PCA + Euclidean kNN (verified, part 4) |
| kNN | k_adj *other* cells (annoy `[1:]` or sklearn `kneighbors()`; `helper_functions.py:410, 417-420`) | `Neighbors` with k_adj, self column kept or dropped (`core.py:346-356`) | **SR1**: k_adj − 1 cells |
| default `expected_doublet_rate` | 0.1 (`scrublet.py:6`) | 0.05 (`__init__.py:33`) | threshold 0.1876 vs 0.0994 at each package's defaults |
| default neighbour search | annoy | sklearn brute (n < 8192, euclidean) else pynndescent; the docstring still says "annoy" (`__init__.py:113`) | design; note |

End to end at each package's defaults the doublet *calls* agree well (Jaccard 0.986; 144
vs 146 called; recall 0.960 vs 0.973 at precision 1.000) while the *scores* do not
(Spearman 0.432, max |Δ| 0.394) because the singlet scores are discrete and depend on
which simulated doublets exist. Feeding the port the original's gene set and simulated
doublets through `adata_sim` (part 2) brings Spearman to 0.996; the remaining difference
(max |Δ| 0.147, threshold 0.1697 vs 0.1876, observed-score maximum 0.6250 vs 0.7722) is
SR1 alone, reproduced exactly by the port's classifier on the original's PCA manifold
(part 3).

## Findings

### SR1 — CONFIRMED on `main` and 1.12.4: Scanpy's port scores each cell over `k_adj − 1` neighbouring cells, not `k_adj`, and which of two variants applies depends on whether any two points in the manifold coincide

**Code.** `core.py:339-356`:

```python
k_adj = round(k * (1 + n_sim / float(n_obs)))
...
knn.compute_neighbors(k_adj, metric=distance_metric, knn=True, transformer=transformer, method=None, rng=self._rng)
neighbors, _ = _get_indices_distances_from_sparse_matrix(knn.distances, k_adj)
if use_approx_neighbors:
    neighbors = neighbors[:, 1:]
```

and `n = float(k_adj)` feeds `q = (nd + 1) / (n + 2)` (`core.py:369`). `Neighbors`
counts a cell as its own first neighbour: `compute_neighbors` asks the transformer for
`k_adj` neighbours, truncates to `k_adj` columns *including* the cell, and stores the
rest with `keep_self=False` (`neighbors/__init__.py:597-606`), i.e. `k_adj − 1` other
cells per row. `_get_indices_distances_from_sparse_matrix` (`_common.py:166-190`) then
re-adds a self column *unless* `_has_self_column` — an `.any()` over rows
(`_common.py:109-114`) — finds some row whose first stored neighbour is itself. That
happens whenever two points coincide: `_remove_self_column` drops column 0 *by position*
(`_common.py:117-124`), and for one member of each coincident pair column 0 held the
twin, so the row keeps itself. Coincident points are produced by the port's own sampler
(a parent pair drawn as (i,j) and (j,i), or (i,i)) in every run tested. So:

- sklearn/default backend, with a coincident pair anywhere: `neighbors` has `k_adj − 1`
  columns for *every* cell and no self column; without one: `k_adj` columns, the first
  being the cell itself, counted with its own label — `k_adj − 1` other cells either way;
- pynndescent backend: `compute_neighbors` stores the transformer's raw output, whose
  first column is already the cell itself, and `[:, 1:]` removes it — `k_adj − 1` other
  cells.

The original uses `k_adj` other cells on both paths (`helper_functions.py:410`
`get_nns_by_item(iCell, k + 1)[1:]`; `:417-420` `kneighbors()` on the fitted set, which
excludes the query point by index).

**Verified** (`../verify/sr1_scanpy_knn_self_neighbour.py`, both venvs identical). On the
original's PCA manifold (1,650 + 3,300 points, k = 20, k_adj = 60) the port's scores
match the closed form with `k_adj − 1` self-excluded exact neighbours to 3.7e-3
(sklearn/default; the residual is one twin counted in place of its parent) and 5.8e-2
(pynndescent), and the original's to 0 with `k_adj`:

| classifier | max obs score | threshold | called | recall | mean Δ obs | mean Δ sim |
|---|---|---|---|---|---|---|
| original | 0.7722 | 0.1876 | 144 | 0.960 | 0 | 0 |
| port, `use_approx_neighbors` None / False / True | 0.6250 | 0.1697 | 146 | 0.973 | −0.0068 | −0.0535 |

763 of 1,650 observed cells score strictly lower in the port, none higher; 2,852 of
3,300 simulated doublets lower; 2 calls flip. The largest attainable observed score is
0.6250 instead of 0.7722. The mechanism section of the harness shows the 12-point case
(rows 3 and 7 coincide: `Neighbors` stores `[7, 9, 10]` for row 7; the classifier gets
shape (12, 3) with `_has_self_column = True`) and that `sc.pp.scrublet` itself hit the
"k_adj − 1, no self" branch in 7 of 7 seeds at n = 198 … 1,650.

**Status.** A wrong number at master in the sense that the port does not implement its
own `n_neighbors`/`k_adj` (documented as Scrublet's rule, `__init__.py:119-122`), and a
non-robustness: adding one coincident point changes every cell's score. The effect on
calls is small here (2 of 1,650; recall moved 0.960 → 0.973, i.e. not worse) — recorded
for fidelity, not for damage. Present in `main` and 1.12.4 by execution; by reading, the
`Neighbors`-based classifier dates from the external port (#1555, 2020-12) and the
pynndescent `[:, 1:]` from #2896 (1.11.0). Related prior report: #2244 (identical cells
get no neighbours in `pp.neighbors`, open since 2022) describes the same duplicate
handling from the graph side; no report of the scrublet consequence.

**Fix.** Ask `Neighbors` for `k_adj + 1`, drop the prepended self column when present
(`../upstream/scanpy/0001-*.patch`, with a test that compares against
`sklearn.neighbors.NearestNeighbors` on manifolds with and without a coincident pair:
4 passed on the branch, all 4 fail on unmodified `main` with max |Δ| 0.180). Scores
change slightly for every user; the pinned expectations in `test_scrublet` /
`test_scrublet_batched` need regenerating (the pbmc3k download is blocked here).

### SR2 — CONFIRMED on `master` = 0.2.3 (and, as metadata only, in the port): `subsample_counts` inflates the simulated doublets' total counts when `synthetic_doublet_umi_subsampling < 1`

**Code.** `helper_functions.py:177-182`:

```python
E.data = np.random.binomial(np.round(E.data).astype(int), rate)
current_totals = E.sum(1).A.squeeze()
unsampled_orig_totals = original_totals - current_totals
unsampled_downsamp_totals = np.random.binomial(np.round(unsampled_orig_totals).astype(int), rate)
final_downsamp_totals = current_totals + unsampled_downsamp_totals
```

`E` holds only the genes kept by the filter (`scrublet.py:220-224`), `original_totals`
the parents' full-gene totals (`scrublet.py:288-291`). Thinning first and then
subtracting means the counts just removed from the kept genes are drawn a second time:
E[total] = rate·T + rate·(1 − rate)·F (T full total, F kept-gene total) instead of
rate·T. These totals then normalise the simulated doublets to 1e6 (`scrublet.py:225`,
`helper_functions.py:21-24`), scaling every simulated profile down. The port's
`sparse_utils.py:52-58` is the same code, but its result only lands in
`adata_sim.obs["n_counts"]` (`__init__.py:564`); `normalize_total` recomputes row sums.

**Verified** (`../verify/sr2_subsample_totals.py`, both venvs): constructed case F = 1,000,
T = 4,000, rate 0.5 → shipped mean total 2250.3, fixed 2000.0, closed form 2,250 vs
2,000. Pipeline at rate 0.8: simulated totals are 1.0559 × (0.8 × parents' totals)
(fixed: 1.0000); mean simulated score +0.0465, observed +0.0067, threshold 0.1876 vs
0.1701, 1 call flips, recall 0.980 vs 0.973. Port: `obs["n_counts"]` is 1.2000 × the row
sums with all genes kept (factor 1 + (1 − rate)), scores unaffected.

**Status.** Wrong number, non-default option (default 1.0), small effect on this data.
Fix: measure the unselected part before thinning (`../upstream/scrublet/0001-*.patch`;
new test fails on master with mean 2250 vs 2000, passes with the patch). No prior issue.

### SR3 — CONFIRMED on `main` and 1.12.4 (undocumented behaviour difference): `sc.pp.scrublet(log_transform=True)` transforms observed and simulated cells on different scales, before the common normalisation

**Code.** `__init__.py:200-227`: `ad_obs` is `normalize_total`-ed (median target) and
subset to HVGs; `ad_sim` is built from the raw layer; then

```python
if log_transform:
    pp.log1p(ad_obs)
    pp.log1p(ad_sim)
pp.normalize_total(ad_obs, target_sum=1e6)
pp.normalize_total(ad_sim, target_sum=1e6)
```

so the log is taken of median-scaled counts for observed cells and of raw summed counts
for simulated ones, and the 1e6 normalisation is then applied to log values. The original
normalises both to 1e6 first and logs both (`scrublet.py:225-227`). The docstring
(`__init__.py:103`) says only "use `log1p` to log-transform the data prior to PCA".

**Verified** (`../verify/sr3_scanpy_log_transform_order.py`, both venvs). At the moment
`log1p` is applied the per-cell sums over the 518 HVGs are 1137.6 (observed) vs 2565.3
(simulated). A doublet made from a cell added to itself must coincide with that cell
under any common per-cell transform; relative distance between the two: port
`log_transform=False` 1.2e-7, **`log_transform=True` 0.189 max / 0.0817 mean**, original
0 for both settings. On the labelled data the measured damage is small: port recall
0.940 / 0.947 (seeds 1, 2) with the log vs 0.980 / 0.987 without, precision 1.000
throughout; the original's own `log_transform=True` is much worse on this data
(recall 0.153 / 0.213, threshold at 0.58) — that is the original's threshold finder
on a differently shaped histogram, not the port's problem, and it is why the
non-default log option was not pursued further there.

**Status.** Undocumented behaviour difference from the original (the two populations
should receive one transform); not a wrong number at the default. Fix: normalise first,
then log both (`../upstream/scanpy/0002-*.patch`; test on counts made in the test
passes on the branch, fails on `main` with 278 of 300 scores off by up to 0.255).
By reading, present since the external port (#1555). No prior issue (#16 on the
scrublet tracker asks about `log_transform` in the original).

### SR4 — CONFIRMED on `master` = 0.2.3: `scrub_doublets(mean_center=True, normalize_variance=False)` raises `TypeError`

**Code.** `helper_functions.py:46-51`: `self._E_obs_norm - gene_means` with a CSC matrix
and an `np.matrix` of means returns an `np.matrix`; `pipeline_pca`
(`helper_functions.py:79-90`) passes it to `sklearn.decomposition.PCA`, which raises
`TypeError: np.matrix is not supported`. `pipeline_zscore` (`:60-66`) wraps the same
expression in `np.array(...)` and is fine; so are the two TruncatedSVD paths.

**Verified** (`../verify/sr4_mean_center_np_matrix.py`, both venvs; traceback in the
`.out`): the (True, False) combination fails, the other three run;
`../verify/sr4_sklearn_versions.out`: PCA rejects the `np.matrix` in scikit-learn 1.4.2,
1.5.2, 1.6.1, 1.7.2 and 1.9.0 (older versions not executed). The port's
`pipeline.mean_center` converts to CSC (`pipeline.py:18-22`) and runs.

**Status.** Crash on a non-default, documented option. One-line fix
(`../upstream/scrublet/0002-*.patch`, test fails on master, passes with the patch).
No prior issue (#58 asks what `normalize_variance` does).

### SR5 — NOTE (design/documentation): the doublet score is a monotone transform of the neighbour fraction that reaches 1 only when *no* observed cell is among the neighbours

`scrublet.py:389-390` (identical in `core.py:369-370`):

```python
q = (nd + 1) / (N + 2)
Ld = q * rho / r / (1 - rho - q * (1 - rho - rho / r))
```

Algebraically `Ld = odds / (1 + odds)` with `odds = q·ρ / (r·(1 − ρ)·(1 − q))` (max
|Δ| 4.4e-16, `heldup_reference_port.out` part D). Under the mixture model in which
observed cells are (1 − ρ) singlets + ρ doublets and simulated doublets sit at density
r times the doublet density, the fraction of simulated neighbours in a pure doublet
state is `q = r/(ρ + r)`, where the code's score is `1/(2 − ρ)` = 0.5263 at ρ = 0.1, not
1; the code's score is 1 only at q = 1. So the score is a probability under a model that
treats every observed neighbour as a singlet, and it is reported as "between 0 and 1"
(README). This does not affect calls — the threshold is found on the same scale — and
the paper's derivation could not be checked from here. Recorded so that users reading
scores as calibrated doublet probabilities know the scale.

### SR6 — NOTE (documentation): the v-score noise fit uses the 0.1th percentile, i.e. essentially the per-bin minimum

`get_vscores(..., fit_percentile=0.1)` passes `p = 0.1` to `np.percentile`
(`helper_functions.py:204, 235`), the 0.1th percentile, not the 10th. On 2,000 genes in
50 bins it equals the exact bin minimum in 5 of 45 non-empty bins and lies within the
interpolation of the two smallest values elsewhere (part B). Fitting the lower envelope
of the Fano-factor cloud may be the intent (the same code ships in the Klein lab's
SPRING); the parameter name reads as a fraction. Either way the fit is deterministic and
the shipped and reference results agree to 1e-14.

### SR7 — NOTE (by execution, scope beyond scrublet): `Neighbors` stores a cell as its own neighbour when another cell coincides with it

Shown in the SR1 mechanism section: for 12 points with rows 3 and 7 equal,
`Neighbors.compute_neighbors(4)` stores `[7, 9, 10]` for row 7 — a self-edge in the
graph that `sc.pp.neighbors` builds on such data. Cause: `_remove_self_column` drops
column 0 by position (`_common.py:117-124`). Issue #2244 reports the same duplicate
cells from the other side (no neighbours). Not checked further.

### SR8 — NOTE (design): `simulate_doublets` reseeds the global numpy RNG

`scrublet.py:283` and `helper_functions.py:177` call `np.random.seed(random_state)`;
after any run `np.random.rand()` returns 0.622268 regardless of the caller's prior state
(part C). Reproducible by design, but it silently resets the user's session RNG, and the
binomial thinning restarts the same stream the pair draw consumed. The port uses a
`Generator` (`core.py:186`).

### Withdrawn

- **W1** — suspected that the port's ddof = 1 z-score would move the kNN. It rescales
  every gene by the same 0.999697 (part 4 of the comparison); scores identical to the
  ddof = 0 pipeline up to SR1.
- **W2** — suspected `sparse_var`'s `E[x²] − E[x]²` would lose precision on 1e6-scaled
  values. Max relative difference from `np.var` is 2.4e-15 (part A).
- **W3** — suspected that SR3 would wreck detection in the port. Measured: recall 0.94
  vs 0.98; so it is filed as a behaviour difference, not a wrong-number finding.
- **W4** — my first reading of SR1 had the sklearn path *always* counting the cell
  itself. Execution showed that variant only when no two points coincide; the port's own
  pipeline took the other branch in every seed. Folded into SR1 as stated.

## What held up (executed, not just read)

All in `../verify/heldup_reference_port.py` unless stated; both venvs give identical output.

- **Whole pipeline vs the independent port** (exact neighbours): gene filter identical
  (300 genes), parents identical, k = 20 and k_adj = 60 by the documented formulas,
  observed and simulated scores and standard errors **max |Δ| = 0**, PCA coordinates
  agree with a full SVD to 9e-12 after sign alignment, threshold equals
  `skimage.filters.threshold_minimum` of the simulated scores, `detected_` /
  `detectable_` / `overall_doublet_rate_` and `z_scores_` match their definitions
  (0.087273, 0.833333, 0.104727). Against truth: 144 called, recall 0.960, precision 1.000.
- **Helpers**: `tot_counts_norm`, `sparse_var`, `sparse_zscore`, `sparse_multiply` equal
  dense numpy (≤ 4e-12); `subsample_counts(rate=1)` is a pass-through.
- **v-scores**: `get_vscores` and `filter_genes` equal the reference fit (b = 0.0876563,
  a = 0.145575; v-scores to 1.4e-14); the model FF = (1 + a)(1 + b) + b·μ and
  `v = FF/model` are as in Klein et al. 2015.
- **Score and error closed forms**: `se_q = √(q(1 − q)/(N + 3))` is the sd of
  Beta(nd + 1, N − nd + 1) (1.4e-17); `se_Ld` equals first-order propagation
  `√((∂L/∂q·se_q)² + (∂L/∂ρ·se_ρ)²)` by finite differences (2.2e-10) — the partial
  derivatives `(ρ/r)(1 − ρ)/den²` and `(q/r)(1 − q)/den²` are what the code encodes.
- **Input handling**: dense, CSC, CSR and float32 inputs give bit-identical scores;
  user-supplied `total_counts` equal to the row sums reproduces the default; the same
  `random_state` reproduces the run bit for bit; a different seed changes the parents
  and scores (max |Δ| 0.249) but 99.9 % of calls.
- **annoy (the default)** vs exact neighbours: median |Δscore| 0.003, max 0.2, calls
  identical (1.0000), identical threshold, identical recall/precision; deterministic
  under `random_state` (`annoy_index.set_seed`, `helper_functions.py:402`).
- **Threshold fallback**: with unimodal simulated scores `call_doublets` returns
  `None`, sets `predicted_doublets_ = None`, leaves `threshold_` unset, and prints the
  documented warning; the port maps that to `predicted_doublet = False` for every cell
  (`__init__.py:483-492`).
- **Port core given the original's matrices**: Spearman 0.996 with the original; the
  only remaining difference is SR1.

## Not checked here

The plotting and embedding helpers (`plot_histogram`, `plot_embedding`, `get_umap`,
`get_tsne`, force layout), `rank_enriched_genes`, the loading helpers, the port's
`batch_key` path beyond its existing tests, `scanpy.pl.scrublet_score_distribution`,
pynndescent's own accuracy, `skimage.filters.threshold_minimum` internals (only its
output was checked), and the paper's stated derivation of the score (unreachable).
