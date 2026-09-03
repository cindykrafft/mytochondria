# PR titles and bodies

## Scrublet (no template; plain body)

### PR 1 — `fix/subsample-counts-totals` — "Fix inflated total counts of UMI-subsampled synthetic doublets"

Fixes #<SR2 issue>.

`subsample_counts` thinned the counts of the genes kept for scoring first and only then
took `original_totals - current_totals` as the part of each total still to be
subsampled, so the counts just removed from the kept genes were drawn a second time:
E[total] = rate·T + rate·(1 − rate)·F instead of rate·T. The synthetic doublets were
then normalised to 1e6 with the inflated totals. This measures the unselected part
before thinning. Only `synthetic_doublet_umi_subsampling < 1` is affected.

Adds `tests/test_subsample_counts.py` (pytest; the repository had no tests): the
first test fails on master (mean 2250 vs 2000) and passes here.

### PR 2 — `fix/mean-center-np-matrix` — "Fix TypeError in scrub_doublets(mean_center=True, normalize_variance=False)"

Fixes #<SR4 issue>.

`pipeline_mean_center` stored `csc_matrix - np.matrix`, an `np.matrix`, which
`sklearn.decomposition.PCA` rejects (`np.matrix is not supported`, scikit-learn ≥ 1.4 at
least). Convert to an ndarray as `pipeline_zscore` already does. Adds
`tests/test_mean_center.py`, which fails on master and passes here.

## Scanpy (`.github/pull_request_template.md`)

### PR 1 — `fix/scrublet-knn-neighbour-count` — "fix: score scrublet doublets over k_adj neighbors, not k_adj - 1"

- [x] Closes #<SR1 issue>
- [x] Tests included: `test_scrublet_knn_uses_k_adj_neighbors` (4 cases: with/without a
  coincident pair × sklearn/default backend), compared against
  `sklearn.neighbors.NearestNeighbors`; all four fail on `main`.
- [ ] Release notes not necessary because: — (fragment
  `docs/release-notes/+scrublet-knn-neighbour-count.fix.md` included; rename to
  `<PR>.fix.md`)

`Neighbors` counts a cell as its own first neighbour, so `compute_neighbors(k_adj)`
returned `k_adj - 1` other cells; the classifier then either counted the cell itself
(sklearn/default) or dropped the column (pynndescent), and when the manifold contained
coincident points (a parent pair drawn twice, or a cell paired with itself)
`_has_self_column` made it skip the self column for every cell. In all cases the score
was over `k_adj - 1` cells divided by `k_adj`. Ask for `k_adj + 1` and drop the self
column.

Doublet scores change slightly for every user (all observed scores can only go up; the
automatic threshold moves). The pinned expectations in `test_scrublet` and
`test_scrublet_batched` need regenerating — I could not download `pbmc3k` from the
environment this was prepared in. Related: #2244.

### PR 2 — `fix/scrublet-log-transform-order` — "fix: log-transform scrublet's observed and simulated cells after the common normalisation"

- [x] Closes #<SR3 issue>
- [x] Tests included: `test_scrublet_log_transform_consistent` (counts generated in
  the test, no download; mirrors `test_scrublet_data`); fails on `main`.
- [ ] Release notes not necessary because: — (fragment
  `docs/release-notes/+scrublet-log-transform-order.fix.md` included)

With `log_transform=True`, `log1p` ran while the observed matrix was median-normalised
and the simulated doublets were raw summed counts, and the 1e6 normalisation was then
applied to log values. Normalise both first, then log both, as the original Scrublet
does. Only `log_transform=True` runs change.
