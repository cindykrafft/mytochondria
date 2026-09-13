# umap-learn #1277: `random_state` does not make a fit deterministic when the data contains duplicate rows

_Prepared 2026-09-13 against `lmcinnes/umap` `master` @ `3fe6476` (2026-09, version
string 0.5.12; master now includes our #1287 and #1288). Not filed; nothing pushed.
Branch `fix/issue-1277-spectral-init-regular-component` (in the clone at
`scratchpad/umap1194`, one commit `e6a4bb1` on top of `3fe6476`), exported as
`0001-Fix-spectral-init-being-non-deterministic-under-rand.patch`._

## The issue

[#1277 "`random_state` does not make UMAP deterministic when the input contains duplicate
rows"](https://github.com/lmcinnes/umap/issues/1277) (2026-06-11, 0 comments, no
assignee). The reporter fits `UMAP(n_neighbors=15, n_components=5, min_dist=0.0,
metric="cosine", random_state=42)` twice on 4,200 sentence embeddings; with all rows
unique the two results are bit-identical, with 1,500 unique rows + 300 of them repeated
9 more times they differ (`max |diff| = 21.8`, "varies per run, but consistently
nonzero"). Deduplicating restores determinism. They guess pynndescent's tie-breaking.

The guess is wrong: the neighbour graph is identical between the two fits here. The
divergence is in the spectral initialisation.

## Diagnosis (line numbers on `3fe6476`)

- Enough exact copies of one point saturate each other's neighbour lists at distance 0.
  `smooth_knn_dist` then has no non-zero distance for rho (`umap/umap_.py:217-229`, rho
  stays 0) and `compute_membership_strengths` gives every edge weight exactly 1
  (`umap_.py:441`). The copies form (or, after `simplicial_set_embedding` prunes weak
  edges at `umap_.py:1151`, become) their own connected component whose graph is
  complete with all weights 1: a **regular graph**.
- `spectral_layout` (`umap/spectral.py:483`) finds several components, so
  `multi_component_layout` lays out each one; a component with at least `2 * dim`
  vertices goes to `_spectral_layout` (`spectral.py:252-262`).
- `_spectral_layout` calls `scipy.sparse.linalg.eigsh` with `v0=np.ones(n)`
  (`spectral.py:544`; introduced in `3ab97e5`, 2017-11-14, "Fix eigvector solve
  initialisation to help with issue #14", to replace ARPACK's own random start with a
  fixed one). On a regular graph the all-ones vector is an exact eigenvector of the
  normalised Laplacian (`L·1 = 1 - D A D 1 = 0` when all degrees are equal), so the
  Lanczos iteration breaks down at its first step and ARPACK generates a new start
  vector with its own internal generator (`dgetv0`/`dlarnv`, whose seed is Fortran
  `SAVE`d state, advanced by every such restart in the process). `random_state` does not
  reach it. The eigenvectors returned for the degenerate component therefore change from
  call to call, and the SGD turns the different initialisation into embeddings that differ
  by several units.

Measured on master (`diag-*.py`, outputs in `diag-*.out`):

- `diag-stage-bisect.out`: two seeded fits on 1,000 unique + 200 x 4 duplicated rows
  (exact path, n < 4096): `graph_`, `_sigmas`, `_rhos` identical; embeddings differ by
  5.0. `spectral_layout` on the *unpruned* graph is deterministic (it is connected);
  `simplicial_set_embedding` with a fixed array init is deterministic.
- `diag-component.out`: the epoch pruning at `umap_.py:1151` splits off a 10-vertex
  component (two duplicated points x 5 copies); `spectral_layout` on the pruned graph
  differs between calls by 1.7, and only that 10-vertex component's layout changes.
- `diag-arpack-start-vector.out`: `eigsh` alone. Complete graphs K10/K12/K16 with
  `v0 = ones` return different eigenvectors on repeated calls (at dim 5, and K16 also at
  dim 2); on a random 4-regular graph `v0 = ones` raises `ArpackError` (which in UMAP
  triggers the "Spectral initialisation failed" fallback); with `v0` drawn from a seeded
  generator every case is identical across calls. Irregular graphs are identical either
  way. Whether a given regular component misbehaves depends on n, k and ncv (K30/K60
  happened to be stable), and on what ARPACK ran before in the process, which is why the
  reporter saw a different `max |diff|` on each run.

Why the reporter's pynndescent-path case (4,200 rows) is the same bug: the mechanism
is downstream of the neighbour search, and their 10-copy groups at k = 15 give the same
all-weight-1 components. Our synthetic 4,200-row analogue happened to stay connected
after pruning and was deterministic (`probe_1277.out` in the session scratchpad); the
1,800-row analogue with the same duplicate structure reproduces the report.

## The fix

`umap/spectral.py`, `_spectral_layout`, the `eigsh` branch: keep `v0 = ones` unless every
vertex has the same degree (`np.allclose(sqrt_deg, sqrt_deg[0], rtol=1e-8, atol=0.0)`,
using the degree vector the function already has), in which case draw
`v0 = gen.uniform(-1, 1, n)` from the seeded generator that the function already builds
for the lobpcg branch. 14 lines including the comment. Seeded results for every graph
that is not regular are bit-for-bit unchanged.

## Reproduction

`repro.py` (synthetic data made in the script; Python 3.12 venv, master installed
editable; numba 0.67.0, pynndescent 0.6.0, scikit-learn 1.9.0, numpy 2.5.2, scipy
1.18.1). Case A has the issue's shape (1,000 unique 50-d rows + 200 repeated 4 more
times, cosine, `n_components=5`, `random_state=42`; three fits compared); case B is the
minimal trigger (200 random points + 16 copies of one far-away point, `n_neighbors=16`).

Before (`repro.before.out`, run in a worktree at `3fe6476`):

    A (1000 unique + 200 x 4 duplicates): 3 seeded fits identical: False | max |diff| = 7.594
    B (16 copies of one point): 3 seeded fits identical: False | max |diff| = 17.496

After (`repro.after.out`):

    A (1000 unique + 200 x 4 duplicates): 3 seeded fits identical: True | max |diff| = 0.000
    B (16 copies of one point): 3 seeded fits identical: True | max |diff| = 0.000

## Tests and linter

Two tests, in the project's style (plain functions, no fixtures needed):
`test_spectral_layout_regular_graph_is_deterministic` in `umap/tests/test_spectral.py`
(`spectral_layout` on the complete graph of 12 duplicates, dim 5, three calls with
`random_state=42` must agree) and `test_repeated_points_reproducible_with_random_state`
in `umap/tests/test_umap_repeated_data.py` (200 random points + 16 copies of one point,
`n_neighbors=16`, `n_epochs=50`, two seeded fits must be identical).

`pytest -q umap/tests/test_spectral.py umap/tests/test_umap_repeated_data.py
umap/tests/test_umap_ops.py` (the touched files plus the multi-component layout tests):

| | result |
|---|---|
| unmodified master (worktree at `3fe6476`), the three files | 32 passed, 1 skipped (101 s) |
| the two new tests against unmodified `spectral.py` | **2 failed** (`assert np.array_equal(layouts[0], layouts[1])`; `assert np.array_equal(first, second)`) |
| with the patch, the three files | 34 passed, 1 skipped (126 s) |

The skip is the project's own scipy-version guard on `test_tsw_spectral_init`.
`black --check` (26.5.1): `umap/spectral.py` and `umap/tests/test_spectral.py` unchanged;
`umap/tests/test_umap_repeated_data.py` has one pre-existing difference at master (a
double blank line after the imports, lines 3-4, which black 26 collapses and the black of
the last "ran black formatting" commit, 2024-09, kept); the patch leaves it as it is, as
the U1 kit did for `test_umap_nn.py`. No changelog fragment convention exists in this
repository (`../../upstream/README.md`); CONTRIBUTING asks for black and the issue
number in the PR message, both done.

## Other candidates considered

In the order the lead asked for them to be tried:

| candidate | verdict |
|---|---|
| **#1280** "Possible index mismatch in `transform()` with `unique=True`" (2026-07-30, 0 comments) | Real: reproduced in the #1194 kit (`../1194-precomputed-transform-search-index/alt-1280-repro.py`, 0 % of transform neighbours point at the right training row). Not chosen: open PR [#1281](https://github.com/lmcinnes/umap/pull/1281) (2026-08-02, "Fix transform with unique=True", 259 passed) already addresses it. Its approach (transform against the de-duplicated embedding, graph of shape `(n_new, n_unique)`) is a behaviour change for `transform_mode="graph"` users; not ours to second-guess without reading its review thread. |
| **#1224** "transform of a subset differs from transform of all then sub-selecting" (2025-10-20, 0 comments) | Not a bug in umap-learn. `alt-1224-transform-subset.out`: on the exact path the bipartite graph rows and `init_graph_transform` are identical between the two batches; the embedding differs by RMSE 0.39 / max 1.55, the same order as the same subset under a different `transform_seed` (RMSE 0.55 / max 2.28), i.e. the SGD's negative sampling drawn from one seeded stream across the batch. The reporter's numbers (RMSE 0.42, max 2.44) match that noise floor. On the pynndescent path (`alt-1224-pynndescent-query.out`) the graph rows themselves differ for 44 of 600 rows because `NNDescent.query` seeds each row's search from a shared, advancing RNG state: single-row queries match neither batch for 3-4 of 50 rows, and the wrong rows get neighbours from another blob (median distance 35 vs 27 to the true neighbours). That is pynndescent's approximate search, in a different repository. |
| **#1277** (this kit) | Chosen: reproducible wrong result (a seeded fit that is not reproducible) with a local fix. Comment thread: 0 comments. |
| **U3** (audit note: `transform` uses `local_connectivity - 1`, so rho = 0 and the nearest training point is excluded from the sigma sum) | A design choice, not a bug. With rho = 0 the weight to the nearest training point is `exp(-d/sigma) < 1` unless `d = 0`, and `init_graph_transform` (`umap_.py:1400-1450`) relies on exactly that: a weight of 1.0 means "identical to a training point" and snaps the new point onto that point's embedding. Using the paper's rho (nearest non-zero distance) would give every query a weight-1 edge and snap every new point onto its nearest neighbour. The inconsistency with `graph_` for training points is real but changing it is a design decision for the maintainers; left as the audit note. |
| #1108 "Semi-deterministic output even though random_state is set" (2024-04, 5 comments, unread) | Same symptom as #1277 (two fits in one process differ, re-running the program gives the same pair), which is the signature of ARPACK's process-wide restart state, but its 10-point example is deterministic on master here (`alt-1108-example.out`: three all-weight-1 components, none regular). Mentioned in the README only. |
| #544 "Warning about Spectra Embedding breaks Random Seed" (2021-01, 1 comment) | Seeded fits differ only on data slices where the graph is disconnected; `init="random"` fixes it. Plausibly this mechanism (a regular component), but the reporter could not share data or reproduce synthetically; not verifiable. |
| #124 "ZeroDivisionError when verbose=True" (2018, 4 comments) | Still present (`layouts.py:432`, `n % int(n_epochs / 10)` with `n_epochs < 10`); a crash under an unusual setting, kept as the fallback and not needed. |

Also checked: `mcp__github__search_pull_requests` for "random_state spectral duplicate
deterministic eigsh v0" in `lmcinnes/umap` returns no open PR; the "unique transform"
search returns only #1281.

## Caveats

- Issue comments cannot be read from this session (#1277 has none; #1108 has 5 and #544
  one). The thread should be checked before filing.
- The reporter's pynndescent-path, 4,200-row case was not reproduced as such: our
  4,200-row synthetic analogue stayed connected after edge pruning and was deterministic,
  while the 1,800-row analogue with the same duplicate structure reproduces the report.
  Whether a given dataset misbehaves depends on whether the duplicates end up as their own
  component of at least `2 * n_components` vertices and on what ARPACK ran earlier in the
  process, so a bit-identical repeat on someone else's data does not rule the bug out.
- An alternative the maintainers may prefer: always start `eigsh` from a seeded random
  vector (sklearn's `spectral_embedding` does this). It removes the special case but changes
  every seeded result at the eigensolver's tolerance, which the SGD amplifies; the patch
  keeps the all-ones start wherever it works so that existing seeded results are unchanged.
- The regular-graph test uses `rtol=1e-8` on the degree vector. Exactly regular
  components (identical rows, all-weight-1 edges) have zero spread; a nearly regular graph
  leaves ARPACK a tiny but non-zero residual and proceeds deterministically, so the
  tolerance only decides which start vector such a rare graph gets.
- `component_layout` (used when there are more than `2 * dim` components) delegates to
  sklearn's `SpectralEmbedding`, which already seeds its ARPACK start from `random_state`;
  not touched.
