# scanpy #3809 — `.obsp["distances"]` holds `n_neighbors` instead of `n_neighbors - 1` neighbors per cell

_Prepared 2026-09-03 against `scverse/scanpy` `main` @ `ec374022` ("ci: fix autofix workflow (#4342)"), Python 3.12 venv with the clone installed editable plus `scikit-misc igraph leidenalg pytest pytest-mock pytest-xdist pytest-rerunfailures pooch` (the project's recipe). Nothing was pushed, filed or posted._

## The issue

- **#3809** — "Unexpected number of non-zero distances when running `sc.pp.neighbors` with `transformer="pynndescent"`" — https://github.com/scverse/scanpy/issues/3809 — opened 2025-09-21, open, 6 comments (not readable from this session), no assignee, label `Area - Topology`. No open PR references it (searched `pynndescent distances 3809` and the open-PR list, 91 PRs).
- **Reporter's claim:** the docs say each row of `adata.obsp["distances"]` has `k - 1` non-zero entries after `sc.pp.neighbors(n_neighbors=k)`; with `transformer="sklearn"` (and `rapids_singlecell` brute force) that holds, with `transformer="pynndescent"` there are `k` entries. Reproduction in the body on a random 5000 × 10000 sparse matrix, PCA, `k = 30`.

## Diagnosis (`ec374022`)

- `src/scanpy/neighbors/__init__.py:158` — the documented contract: "Each row (cell) has `n_neighbors`-1 non-zero entries … (excluding the cell itself)". Added in #2742 (2023-11-17), i.e. *after* the transformer refactor #2536 (2023-08-31), so it is the intended post-refactor behaviour.
- `src/scanpy/neighbors/__init__.py:596-608` — `compute_neighbors` stores `transformer.fit_transform(x)` in `self._distances` (l. 596), extracts `knn_indices, knn_distances` truncated to `n_neighbors` columns including the self column (l. 597, via `_common.py:166-190`), and then **only on the shortcut path** (`if shortcut:` l. 600) rebuilds `self._distances` from those truncated arrays with `keep_self=False` (l. 603-606), giving `n_neighbors - 1` entries per row. For every other transformer the raw transformer output stays in `self._distances`.
- `src/scanpy/neighbors/_common.py:29-71` — `_make_transformer` builds a `PyNNDescentTransformer(n_neighbors=k)` for `transformer="pynndescent"` and for `transformer=None` on the non-shortcut path; pynndescent's transformer returns `k` neighbours *plus* the cell itself (`k + 1` stored entries, `k` non-zero, per row).
- `src/scanpy/neighbors/__init__.py:687-691` — `_handle_transformer`: the shortcut is taken for `transformer="sklearn"` or for `transformer=None` when `metric == "euclidean" and n_obs < 8192`, or `n_obs < 4096`, or `knn=False`. So with default settings the bug fires for **every dataset of ≥ 8192 cells** (and for any non-euclidean metric above 4096 cells), not only when `transformer="pynndescent"` is passed explicitly.
- The connectivities (`umap`, `jaccard`, and `gauss` through `_connectivity.gauss`) are built from the truncated `knn_indices`/`knn_distances`, i.e. from `n_neighbors - 1` neighbours. `.obsp["distances"]` therefore names one neighbour per cell that `.obsp["connectivities"]` never uses.
- Scanpy 1.9.8 (`scanpy/neighbors/__init__.py:355-375` in the wheel, `_get_sparse_matrix_from_indices_distances_umap`) built the matrix from the `n_neighbors` kNN columns including self stored as 0, so this path gave `n_neighbors - 1` non-zero entries in 1.9 — the regression came in with 1.10's transformer refactor (#2536).

## Reproduction (synthetic, `repro.py`)

Random uniform 30-dimensional matrices, `n_neighbors = 15`, three cases: `transformer="sklearn"` (1,500 cells), `transformer="pynndescent"` (1,500 cells) and the default `transformer=None` on 8,500 cells. Per cell: stored and non-zero entries in `distances`, and whether any neighbour in `distances` is missing from `connectivities`.

`repro.before.out` (unmodified `ec374022`):

```
transformer=sklearn      n_obs= 1500: non-zero entries per row 14..14, stored 14..14; 0 of the first 500 cells have a neighbour in `distances` absent from `connectivities`
transformer=pynndescent  n_obs= 1500: non-zero entries per row 16..16, stored 16..16; 348 of the first 500 cells have a neighbour in `distances` absent from `connectivities`
transformer=None         n_obs= 8500: non-zero entries per row 16..16, stored 16..16; 384 of the first 500 cells have a neighbour in `distances` absent from `connectivities`
```

(With uniform random data no two points coincide, so the self entry is the only zero and `getnnz` counts 16 stored entries, of which 15 are the neighbours the reporter counted; the reporter's PCA'd sparse data showed exactly `k`.)

`repro.after.out` (with the patch):

```
transformer=sklearn      n_obs= 1500: non-zero entries per row 14..14, stored 14..14; 0 …
transformer=pynndescent  n_obs= 1500: non-zero entries per row 14..14, stored 14..14; 0 …
transformer=None         n_obs= 8500: non-zero entries per row 14..14, stored 14..14; 0 …
```

## The fix (`0001-fix-keep-n_neighbors-1-neighbors-in-distances-for-al.patch`, branch `fix/issue-3809-distances-n-neighbors`)

`src/scanpy/neighbors/__init__.py`: move the "restrict `self._distances` to the truncated kNN arrays with `keep_self=False`" step out of the `if shortcut:` block so it runs for every transformer when `knn=True`; the shortcut block keeps its diagonal fix and the `knn=False` densification (`knn=False` is only reachable on the shortcut path, `_handle_transformer` raises otherwise). 10 insertions, 5 deletions. Effect on connectivities: `method="umap"` (default) and `"jaccard"` unchanged (built from the truncated arrays already); `method="gauss"` on the non-shortcut path now sees the trimmed matrix and matches the brute-force path (see Caveats for numbers).

`tests/test_neighbors.py`:
- new `test_distances_n_neighbors[pynndescent|sklearn]` (200 random cells, `n_neighbors=5`): asserts `n_neighbors - 1` stored and non-zero entries per row and that every `distances` edge is a `connectivities` edge. On unmodified source: `AssertionError … 200 / 200 mismatched, 6 (ACTUAL), 4 (DESIRED)`. With the fix: passes.
- `test_distances_all`: the `pynndescent` and `KNeighborsTransformer`-instance cases expected all pairwise distances on the 4-point toy data (comments at `tests/test_neighbors.py:183-185` on `ec374022`: "pynndescent returns all distances when data is so small", "Explicit brute force also returns all distances"); they now expect the same kNN matrix (`distances_euclidean`) that the `knn=True` shortcut path is tested against in `test_distances_euclidean`.

`docs/release-notes/3809.fix.md`: towncrier fragment (Bug fixes), named after the issue for now — rename to `<PR number>.fix.md` once the PR exists, as the project's "Check for release notes" workflow requires (same step as for #4337).

| run | result |
|---|---|
| `tests/test_neighbors.py tests/test_neighbors_common.py tests/test_neighbors_key_added.py` on unmodified `ec374022` | 42 passed, 2 skipped (optional deps), 12 subtests passed |
| same, source fix only (old tests) | 2 failed (`test_distances_all[pynndescent]`, `test_distances_all[sklearn]` — the old pass-through expectation), 40 passed, 2 skipped |
| same, full branch | **44 passed, 2 skipped**, 12 subtests passed |
| `ruff check` / `ruff format --check` on the two changed `.py` files | All checks passed / already formatted |
| `git apply --check` of the patch on `ec374022` | clean |

## Other candidates considered (from ~150 open issues listed, 12 bodies read)

- **#2418** `sc.tl.dendrogram` fails when the categorical `groupby` has unused categories (2023, 1 comment) — reproduces on `main` (`KeyError: "['c'] not in index"` from `.loc[categories]` at `_dendrogram.py:153-158`); a crisp one-line fix (`remove_unused_categories`) but a crash rather than a wrong number, so ranked below #3809.
- **#2043** `sc.tl.embedding_density` errors when a category has one observation (2021, 0 comments) — reproduces (`gaussian_kde` `ValueError` on a single sample); the right behaviour for 1–2 cells (NaN, 1.0, or a clear error) is the maintainers' call.
- **#4280** `pp.regress_out` wrong residuals when a covariate barely varies (2026-08, 0 comments, excellent reproducer) — the reporter is already numba-fying the function and explicitly asks whether the maintainers want the change; the fix (`pinv` instead of `inv`) also needs the pinned `regress_test_small.npy` regenerated. Left to that discussion.
- **#3806** custom transformers returning fewer than `k` neighbours fail (2025-09, 2 comments) — a design change (variable-degree kNN graphs), not a fix; **#3930** `pts`/`pts_rest` ordering has an open PR (#3997); **#3025** `paga_path` with a single key crashes on `squeeze()` (plotting, not reproduced synthetically in the time available).

## Caveats

- The 6 comments on #3809 could not be read. The old `test_distances_all` ids show the pass-through was known at least for tiny toy data; if a maintainer has since said the docs should change instead, the alternative is a one-line docstring edit at `__init__.py:158`. The evidence for the code being wrong: the docstring post-dates the refactor, 1.9 behaved as documented, and `distances` disagrees with `connectivities` on the default path for ≥ 8192 cells.
- This changes `.obsp["distances"]` for the pynndescent and custom-transformer paths (one fewer neighbour per row). Measured on 1,500 random cells, `k = 15`, `transformer="pynndescent"` (`gauss_check` run, `ec374022` vs the branch): `method="umap"` connectivities are **bit-identical** before and after (30,518 non-zeros), because `umap` was already built from the truncated arrays. `method="gauss"` connectivities **do change**: `_connectivity.gauss` (`_connectivity.py:87-100`) weights every stored entry of the distance matrix it is given, so before the fix it used all 15 stored neighbours and turned the stored self-zero into a diagonal self-loop of weight 1.0 on every cell (32,922 non-zeros, degree 16–136, 1,500 diagonal entries, 2,004 extra off-diagonal edges); after the fix it uses the same 14 neighbours as `umap` and as the brute-force path (30,518 non-zeros, no diagonal, values on shared edges move by ≤ 0.016 through the symmetrisation). So the patch also fixes an inconsistency for `method="gauss"` on ≥ 8192 cells, and that is the one numerical change downstream of `neighbors` — worth stating in the PR. Anything reading `obsp["distances"]` directly will see the documented `n_neighbors - 1`.
- The reporter's exact script (5000 × 10000 sparse, PCA 100) was reduced to 1,500 and 8,500 dense cells for time; the mechanism does not depend on the representation.
