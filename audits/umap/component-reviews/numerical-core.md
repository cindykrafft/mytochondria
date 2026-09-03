# Component: umap-learn numerical core (`master` @ `e78d85af`, 2026-08-31, version string 0.5.12)

Read in full: `umap/umap_.py` `smooth_knn_dist` (lines 144-254), `nearest_neighbors`
(257-351), `compute_membership_strengths` (354-441), `fuzzy_simplicial_set` (444-627),
`reset_local_connectivity` and `reprocess_row` (716-787), `make_epochs_per_sample` (916-936),
`init_graph_transform` (1388-1438), `find_ab_params` (1456-1471), `UMAP._validate_parameters`
(1815-2117), `UMAP.fit` (2402-2956), `UMAP.transform` (3045-3322); `umap/spectral.py` (573
lines); `umap/sparse.py` set operations and the euclidean / manhattan / cosine / correlation
metrics; `umap/distances.py` euclidean, cosine, correlation; `umap/utils.py`
`fast_knn_indices`. Every suspicion was **executed on the shipped code**: master installed
editable into a Python 3.12 venv (numpy 2.5.2, scipy 1.18.1, numba 0.67.0, pynndescent
0.6.0, scikit-learn 1.9.0), harnesses in `../verify/` with captured output; the confirmed
finding was also run on the 0.5.12 wheel (the latest PyPI release, whose version string
master still carries) and on the 0.5.3 wheel (Python 3.12, numpy 1.x, scikit-learn 1.5).
References: the paper's definition of rho and sigma solved with `scipy.optimize.brentq`,
numpy for the fuzzy union, `scipy.linalg.eigh` for the spectral layout,
`scipy.optimize.least_squares` for the `a, b` curve fit, `scipy.spatial.distance.cdist` and
`sklearn.neighbors.NearestNeighbors` for distances and neighbours.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`). Note
that most of the 1,111 cohort papers reached UMAP through R (`uwot`, via Seurat, Monocle,
ArchR, Signac) or through Scanpy, which calls `fuzzy_simplicial_set` and
`simplicial_set_embedding` with its own neighbour lists and never enters `UMAP.fit`'s
pruning; the finding below therefore concerns direct users of `umap.UMAP`.

## Findings

### U1 — CONFIRMED on master, 0.5.12 and 0.5.3 (by git history, every release since 0.5.0): `smooth_knn_dist` returns sigma = inf for every point with a disconnected neighbour, and all of that point's remaining edges get membership strength 1.0

**Code.** `UMAP.fit` marks every neighbour at distance `>= disconnection_distance` with
`knn_dists = np.inf` and `knn_indices = -1` before building the fuzzy graph
(`umap/umap_.py:2594-2596` sparse precomputed path, `2674` small-data path, `2741-2743`
standard path), and `nearest_neighbors(metric="precomputed")` keeps `inf` entries of a
distance matrix the same way (`324`). Inside `smooth_knn_dist` the binary search handles
those entries correctly (an `inf` distance contributes `exp(-inf) = 0` to the sum,
`223-228`). The floor applied afterwards does not:

```python
# umap/umap_.py:196
mean_distances = np.mean(distances)
# umap/umap_.py:245-252
if rho[i] > 0.0:
    mean_ith_distances = np.mean(ith_distances)
    if result[i] < MIN_K_DIST_SCALE * mean_ith_distances:
        result[i] = MIN_K_DIST_SCALE * mean_ith_distances
else:
    if result[i] < MIN_K_DIST_SCALE * mean_distances:
        result[i] = MIN_K_DIST_SCALE * mean_distances
```

`np.mean` of a row containing `inf` is `inf`; `MIN_K_DIST_SCALE * inf` is `inf`;
`result[i] < inf` is always true; sigma becomes `inf`. `compute_membership_strengths`
(`430-433`) then computes `exp(-((d - rho) / inf)) = 1.0` for every finite neighbour. The
global `mean_distances` is `inf` as soon as any row has an `inf`, which does the same to
every row with `rho == 0` (all finite neighbours identical to the point; harmless for them,
since those neighbours get 1.0 from the `d - rho <= 0` branch anyway). Also, `rho` itself
is taken from `non_zero_dists` (`205`, `218`), which includes `inf`, so a row whose only
non-zero neighbours are pruned gets `rho = inf`. The floor code is unchanged since
`b429d2c` (2019-05-02, first in 0.3.9); `disconnection_distance` arrived with
`2fb643b`/`c82a134` (2020-11-16/17, first in 0.5.0), which is when the two began to
interact.

**Verified** (`../verify/u1_disconnected_sigma_inf.py`; 8-point cluster next to a
300-point cluster in 5-d, k = 15, `disconnection_distance = 5`, so each cluster point's
neighbour list holds 7 finite and 7 pruned entries; reference sigma from the paper's
equation over the finite neighbours, floor on the finite distances):

| | shipped (master, 0.5.12, 0.5.3) | reference |
|---|---|---|
| sigma of the 8 cluster points | `inf` ×8 | 0.176 – 0.621 |
| rho | identical (max diff 0) | |
| rows without a pruned neighbour, max \|sigma diff\| | 1.68e-06 | |
| point 0's strengths to its 7 kept neighbours | 1, 1, 1, 1, 1, 1, 1 | 1, 0.770, 0.694, 0.555, 0.405, 0.341, 0.142 |
| cluster edges with weight exactly 1.0 | 56 of 56 | 8 of 56 |
| reference kernel row sums (target log2 15 = 3.9069) | | 3.907 ×8 |

Through `UMAP.fit` on the same data the four routes all give 8 rows with `_sigmas == inf`
and 56 of 56 in-cluster `graph_` entries equal to 1.0: the exact path (n < 4096), the
pynndescent path (`force_approximation_algorithm=True`), `metric="precomputed"` with
`disconnection_distance`, and `metric="precomputed"` with `inf` entries in the matrix
(`nearest_neighbors` path; the small-data precomputed path rejects `inf` input at
sklearn's finite check). The control fit without disconnection has 0 such rows and 10 of
56 unit edges (the reciprocal nearest neighbours). `transform()` is not affected in the
same way: it sets pruned indices to -1 but leaves the distances finite (`3225`), so its
8 query rows carry 8 unit entries of 64 (the self edges).

**How often it fires.** With euclidean (default `disconnection_distance = inf`) never;
with cosine/correlation (default 2) only for exactly antipodal vectors, which do not
appear in nearest-neighbour lists; with the bounded metrics whose default is 1
(`jaccard`, `dice`, `hellinger`, `bit_jaccard`), whenever a point's k nearest include a
row at the maximal distance, i.e. sharing no feature. On 1,000 × 600 random binary rows
of density 0.005 with `metric="jaccard"` and otherwise default settings: 548 rows had a
pruned neighbour, 600 rows got `sigma = inf` (the extra 52 through the global mean), 87 of
those have fewer than log2(15) finite neighbours (no finite sigma exists by the
definition; unbounded is the right answer there), the other 513 have a well-defined
finite sigma and got `inf`; in those rows 4,531 of 4,855 graph entries are exactly 1.0. On
400 × 40 rows of density 0.06 nothing was pruned and nothing fired. On 0.5.3 (older
pynndescent) the same data gives 923 / 975 / 546 / 429 and 3,403 of 3,445. With a
user-set `disconnection_distance`, which `doc/faq.rst` recommends "to prevent data in
particularly sparse regions of their space from becoming connected", it fires for every
point whose neighbour list straddles the threshold.

**Consequence.** The point is attached with full strength to everything it keeps, which
is the failure mode the FAQ paragraph introducing `disconnection_distance` set out to
avoid ("all k-nearest neighbours … will all be considered maximally similar"), now applied
to the point's genuine neighbours; the local structure within small, partly disconnected
groups is flattened. The effect on final coordinates was not measured here (the layout is
stochastic); the graph weights are the published-number path.

**Fix shape** (`../upstream/0001-*.patch`): exclude non-finite distances from `rho` and
from both means. Rows without a pruned neighbour are bit-identical on master (max
\|sigma diff\| 0.0 in Part D of the harness, 1.91e-06 on 0.5.3); the fixed function
matches the reference to 2.19e-06 on the rows that used to be `inf`. Two tests added;
both fail on unmodified master.

**Upstream.** No prior report (tracker searched 2026-09-03; nearest #523, the request
that became the feature, and #410/#141 on `smooth_knn_dist` generally). No cohort paper
can be shown to be exposed from the survey cache: none mentions `disconnection_distance`,
and the papers running umap-learn directly with a bounded metric cannot be identified
from evidence snippets. Filing: issue then PR, per `CONTRIBUTING.md` (no templates).

### U2 — NOTE (design consequence of the definition; documented remedy `unique=True`, with an understated threshold): three duplicates of a point at k = 15 collapse its sigma to the floor and zero its edges to all but its nearest distinct neighbour

`smooth_knn_dist` excludes zero distances when choosing rho (`205-214`) but counts every
neighbour with `d <= rho` as 1.0 in the cardinality sum (`223-228`). With m identical
rows the sum is at least m + 1 for any sigma, against a target of log2(k) = 3.907, so for
m ≥ 3 no sigma satisfies the equation, the bisection halves sigma 64 times and the floor
`1e-3 × mean(row)` is returned. Measured (`../verify/note_duplicates_sigma_collapse.py`,
500 Gaussian points in 8-d, point 0 replicated m times):

| m | sigma(point 0) | floor | kernel sum | weights to the distinct neighbours (by distance) |
|---|---|---|---|---|
| 0 | 0.5966 | 0.0024 | 3.907 | 1, 0.33, 0.32, 0.29, 0.27, 0.25 |
| 1 | 0.4733 | 0.0022 | 2.907 | 1, 0.25, 0.23, 0.21, 0.19, 0.17 |
| 2 | 0.3377 | 0.0020 | 3.907 | 1, 0.14, 0.13, 0.11, 0.10, 0.09 |
| 3 | 0.00185 | 0.00185 | 4.000 | 1, 0, 0, 0, 0, 0 |
| 10 | 0.00061 | 0.00061 | 10.000 | 1, 0, 0, 0 |

(The m = 1 row converges to 2.907 rather than 3.907 because the duplicate occupies
column 0 in place of the point itself and is skipped by the `range(1, k)` loop.) Through
`UMAP.fit`, with m = 4 point 0 keeps weights > 0.01 to its 4 copies and 3 distinct rows;
with m = 10 to 10 copies and 1 distinct row; with `unique=True` to 15 distinct rows in
every case. This is what the paper's definition gives and the package offers `unique`
for it; the docstring's condition, "If you have more duplicates than you have
`n_neighbors`" (`1663-1667`), understates when it matters: at k = 15, 3 copies suffice,
and 1–2 copies already halve the weights on the distinct neighbours. Cytometry inputs
(26 cohort papers), whose integer-valued channels produce identical rows, are the data
type this touches; the survey cache cannot say which of them ran umap-learn.

### U3 — NOTE (undocumented behaviour): `transform` builds a different local graph than `fit`, also for training points

`transform` calls `smooth_knn_dist` with `local_connectivity - 1` (`3226-3230`), so rho
is 0, and the `range(1, k)` loop (`223`) skips the query's nearest training point, which
in `fit` is the self entry. Measured (`../verify/note_transform_vs_fit_graph.py`; 1,200
points, k = 15, `transform_mode="graph"` on the first 200 training rows): the self edge
gets weight 1.0 (which `init_graph_transform` uses to place the point on its own
embedding, `1420`), but the strengths to the other 14 neighbours differ from the
unsymmetrised fit membership matrix by up to 0.703 (mean 0.152, correlation 0.870);
the nearest distinct neighbour has weight 1.0 in 200 of 200 fit rows and 0 of 200
transform rows; sigma is 1.7–2.5 in transform against 0.19–0.46 in fit for the same
points. Only the identical full training matrix short-circuits to `graph_`/`embedding_`
(`3085`; `doc/transform.rst` documents that case). The transform of the same subset is
bit-identical on repeat (`transform_seed`), and its coordinates differ from
`embedding_[:200]` by a median of 0.23 (max 1.12) on an embedding of range 22 × 6.
Recorded as a design choice with no documentation; issue #1224 (subset vs full
transform) is adjacent but about the embedding, not the graph.

### W1 — WITHDRAWN: `random_state` does not disable parallelism (open issue #1080)

Suspected from the issue; on master `_validate_parameters` sets `self.n_jobs = 1` when a
seed is given (`2014`). `../verify/heldup_reproducibility.py`: `n_jobs` 1 and 4 give
bit-identical `graph_` and `embedding_` on both the exact (N = 2,000) and pynndescent
(N = 6,000) paths, and a repeat seeded run is bit-identical; two unseeded runs differ
(embedding max diff 6.78 / 4.82) as documented. Issue #1080 is stale relative to master.

### W2 — WITHDRAWN: the sparse metric implementations differ from the dense ones

`../verify/heldup_sparse_vs_dense.py` on 120 × 60 vectors with 60 % zeros, all-zero rows
and duplicates: sparse vs dense euclidean and manhattan 0.0, cosine 2.2e-16, correlation
2.4e-08; all four within 6.7e-07 of scipy on finite pairs. Where scipy returns NaN
(zero or constant rows) dense and sparse agree on 0 for two zero rows and 1 for one zero
row — a convention, applied consistently. `UMAP.fit` on dense vs CSR through the exact
path gives the same edge set and weights within 4.95e-06 (euclidean) / 4.41e-06
(cosine). On the pynndescent path (N = 5,000) the two inputs take different NN-descent
code paths and 5,406 of ~131,000 edges (euclidean) / 2,476 of ~92,000 (cosine) are
present in one graph only; that is the approximation, not the metrics, and the same
holds between two unseeded dense runs.

## What held up (executed, not just read)

- **sigma and rho** (`../verify/heldup_core_vs_reference.py`, 800 points, k = 15):
  `smooth_knn_dist` matches `brentq` on the paper's equation to a relative 4.6e-06
  (local_connectivity 1.0) and 6.1e-06 (1.5, the interpolated rho matching to 1.2e-07);
  kernel row sums over the non-self neighbours lie in [3.90688, 3.90690] against log2 15 =
  3.90689; the floor was inactive in all 800 rows.
- **Symmetrisation.** `graph_` is exactly symmetric (max \|G − Gᵀ\| = 0.0), in [0, 1], and
  equals `A + Aᵀ − A∘Aᵀ` computed in numpy to 9.9e-08; `set_op_mix_ratio` 0.5 and 0.0
  match the documented mix to 3.7e-08 and 2.9e-08; the unsymmetrised matrix has a zero
  diagonal and exactly one unit entry per row (the rho neighbour).
- **`find_ab_params`** equals an independent least-squares fit of the same curve to four
  decimals for six (spread, min_dist) settings including min_dist = 0 and 0.99; the
  default gives a = 1.5769, b = 0.8951.
- **Spectral initialisation.** On a connected graph the two returned vectors span the
  same subspace as the dense `eigh` eigenvectors 2 and 3 of the normalized Laplacian
  (principal angles 6.4e-06 and 1.6e-05 degrees; Rayleigh quotients 0.10571 and 0.12136
  equal to the eigenvalues). On a two-component graph the layout is finite and the
  components sit at ±1 along the first axis (the unit-vector meta-embedding for
  n_components ≤ 2·dim, `spectral.py:229`).
- **`metric="precomputed"`** on the exact distances reproduces the euclidean fit
  (graph 2.9e-06, sigma 1.9e-06, rho 2.4e-07); `fast_knn_indices` returns the same
  neighbours as sklearn with self in column 0.
- **Reproducibility across `n_jobs`** (W1) and **sparse vs dense** (W2) as above.
- **`transform`** of the same points is bit-identical on repeat; the full training matrix
  returns `graph_`/`embedding_` itself.

## Not audited here

`umap/layouts.py` (the SGD, negative sampling, the `optimize_layout_*` kernels — the
stochastic part the brief excluded), densMAP, ParametricUMAP, AlignedUMAP, the supervised
path (`discrete_metric_simplicial_set_intersection`, `general_simplicial_set_intersection`,
`reset_local_connectivity`), `inverse_transform`, `update()`, the `tswspectral`/LOBPCG
path (used above 2,000,000 vertices), the remaining ~40 metrics, pynndescent internals,
`transform`'s epoch choice (100 epochs for ≤ 10,000 query rows, else 30; `3259-3262`), and
plotting.
