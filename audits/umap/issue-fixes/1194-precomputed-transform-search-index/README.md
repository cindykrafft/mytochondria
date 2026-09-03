# umap-learn #1194: `transform()` refuses a precomputed distance matrix once the training set has 4096 rows

_Prepared 2026-09-03 against `lmcinnes/umap` `master` @ `e78d85af` (2026-08-31, version
string 0.5.12, the same as the latest PyPI release). Not filed; nothing pushed. Branch
`fix/issue-1194-precomputed-transform-search-index`, one commit on top of `e78d85af`,
in `0001-Fix-transform-refusing-precomputed-distances-when-fi.patch`._

## The issue

[#1194 "Error on transform on precomputed distance matrix"](https://github.com/lmcinnes/umap/issues/1194)
(2025-04-02, 0 comments, no assignee). The reporter fits `UMAP(metric="precomputed")` on a
99 877 x 99 877 distance matrix, then calls `transform` with the 123 x 99 877 matrix of
distances from the new samples to the training samples, and gets

    NotImplementedError: No search index available: transforming data into an existing embedding is not supported

They add that "the exact same code on only 4218 rows ... runs just fine. As soon as there
is 4219 rows, the error raises" (their per-run split; the actual cliff is at 4096 training
rows, see below).

## Diagnosis (line numbers on `e78d85af`)

- `umap/umap_.py:313-327` (`nearest_neighbors`): for `metric == "precomputed"` the k-NN
  is read off the matrix and `knn_search_index = None` is returned.
- `umap/umap_.py:2633` vs `2711-2731` (`fit`): training sets with fewer than 4096 rows and
  `force_approximation_algorithm=False` take the "small data" branch, which never sets
  `self._knn_search_index`. Everything else takes the standard branch, which stores the
  three values returned by `nearest_neighbors`, so for a precomputed metric
  `self._knn_search_index = None`.
- `umap/umap_.py:3106-3113` (`transform`): the guard added for #848,
  `if hasattr(self, "_knn_search_index") and self._knn_search_index is None: raise
  NotImplementedError(...)`, runs before the `if self.metric == "precomputed":` branch at
  `3118`, which reads the new-to-training distance matrix and never touches an index.

So `transform` with a precomputed metric works for < 4096 training rows (attribute never
set) and raises for >= 4096 rows (attribute set to `None`), even though the code that
would run is identical. The same happens for any size with
`force_approximation_algorithm=True`, which is what the regression test uses.

The fix guards the check with `self.metric != "precomputed"` (one condition plus a
comment). The #848 behaviour for `precomputed_knn` supplied without an index is unchanged
and still covered by `test_precomputed_knn_on_iris`.

## Reproduction

`repro.py`: 4095- and 4096-point synthetic 5-D data, full Euclidean distance matrix as the
training input, distances from 5 new points as the transform input. Python 3.12 venv
(`uv`), master installed editable; numba 0.67.0, pynndescent 0.6.0, scikit-learn 1.9.0,
numpy 2.5.2, scipy 1.18.1.

Before (`repro.before.out`):

    n=4095: transform OK, shape (5, 2), finite=True
    n=4096: NotImplementedError: No search index available: transforming data into an existing embedding is not supported

After (`repro.after.out`):

    n=4095: transform OK, shape (5, 2), finite=True
    n=4096: transform OK, shape (5, 2), finite=True

## Tests and linter

`pytest -q umap/tests/test_umap_on_iris.py` (the file holding the existing precomputed
transform tests and the #848 test; the new test sits next to them):

| | result |
|---|---|
| unmodified master, whole file | 12 passed (136 s) |
| new test only, against unmodified `umap_.py` | **1 failed**, `NotImplementedError: No search index available ...` at `umap_.py:3109` |
| with the patch, whole file | 13 passed (86 s) |

`black --check umap/umap_.py umap/tests/test_umap_on_iris.py` (black 26.5.1): "2 files
would be left unchanged" (black prints a warning that its default target is Python 3.15
while running under 3.12; it does not affect these files). CONTRIBUTING asks for black
and for the issue number in the PR message; both are in the patch. No changelog
fragment convention exists in this repository (see `../../upstream/README.md`).

## Other candidates considered

Read: the 100 newest open issues, the next 100 by creation date (titles only), and the
bodies of 14 + 18 issues from two keyword searches (transform / unique / inverse_transform
/ precomputed / ZeroDivisionError / verbose / parallel / get_feature_names_out). Issue
comments could not be read from this session.

- **#1280** "Possible index mismatch in `transform()` with `unique=True`" (2026-07-30).
  Real and reproduced here (`alt-1280-repro.py`, `alt-1280-repro.out`: with 300 duplicate
  rows in front of 4500 distinct points, 0 % of the transform graph's strongest columns
  point at the query's training row, and the transformed points land a median 7.1 units
  from the right embedding in an 18.8-unit-wide plot): `transform` looks up neighbour
  indices from the search index built on the de-duplicated data in `self.embedding_`,
  which `fit` expands back to the original row order. Not chosen because open PR
  [#1281](https://github.com/lmcinnes/umap/pull/1281) (2026-08-02) already addresses it.
- **#124** "ZeroDivisionError when verbose=True" (2018-08). Still present:
  `umap/layouts.py:432` does `n % int(n_epochs / 10)`, so `verbose=True` with
  `n_epochs < 10` raises `ZeroDivisionError: integer modulo by zero`; reproduced in this
  session with `UMAP(n_epochs=5, verbose=True)`. Second choice: a crash on an unusual
  setting rather than under ordinary use.
- **#1228** "ZeroDivisionError in `inverse_transform()`" (2025-11, 6 unread comments).
  Reproduction needs MNIST through `fetch_openml` (no network here) and the division
  inside the numba kernel `_optimize_layout_inverse_single_epoch` is not evident from the
  code (`make_epochs_per_sample` never yields 0); not attempted.
- **#1099** strings accepted for `n_neighbors` / `min_dist` (2024-03): a missing type
  check that fails later with an unclear message; not a wrong result, skipped.
- **#1021** "Random state doesn't work with metric='precomputed'" (2023-06) and
  #996 / #854 `KeyError` with `metric="precomputed"`: seen on the second listing page
  after the fix above was under way; bodies not read.

## Caveats

- The minimal reproduction and the test go through the precomputed branch's dense path;
  the sparse-distance path in `transform` (`umap_.py:3125-3150`) sits behind the same guard
  and is exercised by the existing `test_precomputed_sparse_transform_on_iris` only in the
  small-data case. It should be equally freed by the change but was not run at >= 4096
  rows here.
- An alternative the maintainers may prefer: move the guard into the `else:` branch of
  `transform` that actually calls `self._knn_search_index.query(...)` (`umap_.py:3216`),
  so it protects exactly the code that needs the index. That is a slightly larger move
  of the same lines; the patch keeps the guard where #848 put it.
- The reporter's 4218/4219 boundary is not the 4095/4096 one found here; with 0 comments
  it cannot be checked what else differed between their two runs (their fit used a
  different subset each time), but the error message and the size dependence match.
