# Bug report: `pp.scrublet` scores each cell over `k_adj - 1` neighbours, not `k_adj`

_Fields of `.github/ISSUE_TEMPLATE/bug-report.yml`._

**Please make sure these conditions are met**

- [x] I have checked that this issue has not already been reported.
- [x] I have confirmed this bug exists on the latest version of scanpy. (1.12.4)
- [x] (optional) I have confirmed this bug exists on the main branch of scanpy. (`a656a33b`)

**What happened?**

Scrublet's classifier scores a cell by the number of simulated doublets among its
`k_adj = round(k * (1 + n_sim/n_obs))` nearest *other* cells and divides by `k_adj`
(`q = (nd + 1) / (k_adj + 2)`). `Scrublet._nearest_neighbor_classifier` asks
`Neighbors.compute_neighbors(k_adj)` for those neighbours, but `Neighbors` counts a cell
as its own first neighbour, so only `k_adj - 1` other cells come back. Then:

- when no two points of the manifold coincide, `_get_indices_distances_from_sparse_matrix`
  prepends a self column: the cell is counted as its own neighbour with its own label
  (sklearn / default backend) or dropped (`neighbors[:, 1:]`, pynndescent) — `k_adj - 1`
  other cells either way, while `n = float(k_adj)`;
- when any two points coincide (a parent pair drawn as (i,j) and (j,i), or as (i,i) —
  which `sample_comb` produced in every run I tried at n = 200 … 1,650),
  `_has_self_column` is true for one row (the twin's row kept itself because
  `_remove_self_column` drops column 0 by position), no self column is prepended for
  *anyone*, and every cell is scored over `k_adj - 1` cells. (On the pynndescent
  backend the raw transformer output is stored with the cell itself first, and
  `[:, 1:]` removes it: `k_adj - 1` there too.)

Either way the port is not the algorithm it documents (`n_neighbors`: "Number of
neighbors used to construct the KNN graph"), all observed scores are biased down (763 of
1,650 lower, none higher, on the same PCA manifold as the original package; the
maximum attainable score is 0.625 instead of 0.772), the automatic threshold moves
(0.1697 vs 0.1876), and the score of every cell changes discontinuously when one
coincident pair appears. On my labelled simulation the effect on calls is small
(2 of 1,650 flip). Related: #2244 (duplicate cells in `pp.neighbors`).

**Minimal code sample**

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "scanpy@git+https://github.com/scverse/scanpy.git@main",
#   "scikit-learn",
# ]
# ///
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scanpy.preprocessing._scrublet.core import Scrublet

rng = np.random.default_rng(0)
n_obs, n_sim, k = 150, 300, 6
mo, ms = rng.normal(size=(n_obs, 5)), rng.normal(size=(n_sim, 5)) + 0.5
ms[1] = ms[0]  # one coincident pair, as a parent pair drawn twice would give

scrub = Scrublet(counts_obs=np.ones((n_obs, 2)), n_neighbors=k, expected_doublet_rate=0.1, rng=0)
scrub.set_manifold(mo, ms)
scrub.calculate_doublet_scores(use_approx_neighbors=False)

# Scrublet's rule: k_adj nearest *other* cells
k_adj = round(k * (1 + n_sim / n_obs))
X = np.vstack([mo, ms]); labels = np.r_[np.zeros(n_obs), np.ones(n_sim)]
nd = labels[NearestNeighbors(n_neighbors=k_adj).fit(X).kneighbors(return_distance=False)].sum(1)
q = (nd + 1) / (k_adj + 2); rho, r = 0.1, n_sim / n_obs
expected = q * rho / r / (1 - rho - q * (1 - rho - rho / r))
got = np.r_[scrub.doublet_scores_obs_, scrub.doublet_scores_sim_]
np.testing.assert_allclose(got, expected)
```

Expected: the assertion passes (it does with `k_adj` other cells). Got:

```
AssertionError:
Not equal to tolerance rtol=1e-07, atol=0
Mismatched elements: 295 / 450 (65.6%)
Max absolute difference among violations: 0.18018018
```

Delete the line `ms[1] = ms[0]` and 176 of 450 still mismatch (max 0.180): that is the
"cell counted as its own neighbour" variant. Shrinking to 12 points shows the mechanism:
`Neighbors.compute_neighbors(4)` stores `[7, 9, 10]` for a row 7 that coincides with row 3.

**Error output**

(above)

**Versions**

<details>

```
# audit venv, scanpy main @ a656a33b (print_versions/print_header emit nothing at default verbosity; from importlib.metadata)
Python 3.12.3 (Linux-6.18.44-fc-v24-x86_64-with-glibc2.39)
scanpy         1.14.0.dev1+ga656a33b0
anndata        0.13.3.post0
numpy          2.5.2
scipy          1.18.1
scikit-learn   1.9.0
pynndescent    0.6.0
scikit-image   0.26.0
annoy          1.17.3
pandas         3.0.5
numba          0.67.0
```

</details>

**Proposed fix** (PR to follow): ask `Neighbors` for `k_adj + 1`, drop the self column
when it is prepended, and score over exactly `k_adj` cells; test against
`NearestNeighbors` with and without a coincident pair. Scores change slightly for
every user; the pinned values in `test_scrublet` / `test_scrublet_batched` need
regenerating.
