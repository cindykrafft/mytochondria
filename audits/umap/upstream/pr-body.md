# PR body (lmcinnes/umap has no PR template; CONTRIBUTING.md: reference the issue number, run `black`)

**Branch:** `fix/smooth-knn-dist-disconnected-floor` (one commit on top of `e78d85af`;
patch `0001-Fix-smooth_knn_dist-giving-sigma-inf-for-points-with.patch`)

**Title:** Fix smooth_knn_dist giving sigma = inf for points with a disconnected neighbour

Fixes #<U1 issue>.

Neighbours pruned by `disconnection_distance` (and `inf` entries of a precomputed distance
matrix) reach `smooth_knn_dist` as `knn_dists = inf`. The `MIN_K_DIST_SCALE` floor was
computed from `np.mean(ith_distances)`, which is `inf` for such rows, so the floor replaced
the searched sigma with `inf` and `compute_membership_strengths` gave every remaining edge of
the point a membership strength of exactly 1.0. The global `mean_distances` was `inf` as well
as soon as any row contained an `inf`, which did the same to every row with `rho == 0`.

This excludes non-finite distances from `rho` and from both means. Rows without a pruned
neighbour are unchanged (bit-identical sigma on the audit's test data).

Tests:
- `test_umap_nn.py::test_smooth_knn_dist_disconnected_neighbors`: a row with three `inf`
  entries keeps a finite sigma, rho is still the nearest finite neighbour, and the kernel
  over the finite neighbours sums to log2(k); rows without `inf` are unchanged.
- `test_umap_ops.py::test_disconnection_distance_keeps_sigma_finite`: an 8-point cluster
  next to a 300-point cluster with `disconnection_distance=5.0`, on the exact and the
  pynndescent path: finite `_sigmas`, each cluster point keeps its 7 in-cluster edges with
  graded strengths rather than all 1.0.

Both new tests fail on unmodified master (2 failed) and pass with this change;
`umap/tests/test_umap_nn.py` + `umap/tests/test_umap_ops.py`: 25 passed / 7 skipped before,
27 passed / 7 skipped after. `black --check` passes on the changed files.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01TaHntBDKuZJpMAAMenkC44
