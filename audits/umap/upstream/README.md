# umap-learn upstream filing kit

_Prepared 2026-09-03 against `lmcinnes/umap` `master` @ `e78d85af` (2026-08-31, version
string 0.5.12, the same as the latest PyPI release). **Filed 2026-09-03:** issue [#1286](https://github.com/lmcinnes/umap/issues/1286) and
PR [#1287](https://github.com/lmcinnes/umap/pull/1287). The fix
branch [`fix/smooth-knn-dist-disconnected-floor`](https://github.com/cindykrafft/umap/tree/fix/smooth-knn-dist-disconnected-floor)
(`54e0d23`, patch 0001, one commit on top of `e78d85af`) is pushed to the fork
[cindykrafft/umap](https://github.com/cindykrafft/umap)._

## What was read before preparing this (step 4 of the method)

- `CONTRIBUTING.md` (the only contributing document in the repository): issues are
  welcome; check the FAQ and do a cursory search of existing issues first; reproduction
  instructions are "helpful, but not necessary"; code contributions by fork + PR,
  "if you are fixing a known issue please add the issue number to the PR message";
  run `black` before submitting (CI checks it). No results-stability policy.
- No `.github/` directory: **no issue template and no PR template**. The issue text below
  therefore follows the shape of the scanpy kit (summary, expected/got, minimal sample,
  output, versions) rather than a form.
- `doc/faq.rst` ("UMAP disconnects some points from the manifold"): the paragraph that
  introduces `disconnection_distance` and recommends setting it by hand "to prevent data
  in particularly sparse regions of their space from becoming connected"; quoted in the
  issue because it is the documented route to the defect.
- `doc/release_notes.rst`: per-minor-release feature lists (0.2 - 0.5), no per-PR
  changelog and no fragment convention, so the patch carries **no changelog entry**.
- `doc/reproducibility.rst` and `doc/transform.rst` for the held-up checks and the
  transform note (`transform` on the identical training matrix returns `embedding_`).
- `umap/tests/test_umap_nn.py` (the existing `smooth_knn_dist` tests, whose
  `1 + log2(k)` row-sum check the new unit test mirrors) and
  `umap/tests/test_umap_ops.py` (`test_disconnected_data*`, next to which the new
  `UMAP`-level test sits).
- Git history: the floor code is unchanged since `b429d2c` (2019-05-02, first in 0.3.9);
  `disconnection_distance` arrived with `2fb643b`/`c82a134` (2020-11-16/17, first in
  0.5.0), which is when the two started interacting.
- Issue tracker searched 2026-09-03 (`mcp__github__search_issues`, lmcinnes/umap) for
  disconnection_distance + sigma/inf/membership, smooth_knn_dist, duplicates, sparse vs
  dense, transform vs fit, reproducibility. No prior report of U1. Nearest: #523 (the
  request that became `disconnection_distance`), #410/#141 (questions about
  `smooth_knn_dist`), #1277 (non-determinism with duplicate rows, a pynndescent
  tie-breaking matter, not this), #1224 (`transform` of a subset differs from the full
  transform; related to the transform note but not filed here).
- Matthew Rocklin's "Craft Minimal Bug Reports": `mcve_u1.py` makes its data in the
  script, has no line that is not needed, ends in an assertion, and the issue text states
  expected vs got, carries the complete traceback and says what shrinking revealed (any
  row with an `inf` suffices; the finite-neighbour count, metric and search path do not
  matter).

## Contents

| file | what |
|---|---|
| `issue-u1-disconnected-sigma-inf.md` | the bug report, with `mcve_u1.py` inline |
| `mcve_u1.py`, `mcve_u1.out`, `mcve_u1_0.5.12.out`, `mcve_u1_patched.out` | the minimal reproduction and its output on master, on the 0.5.12 wheel, and with the patch |
| `0001-Fix-smooth_knn_dist-giving-sigma-inf-for-points-with.patch` | fix + two tests, `git am`-able against `e78d85af` |
| `pr-body.md` | PR title and body |

## Verification status of the patch

Python 3.12 venvs (`uv`), master installed editable (`venv`), the fix worktree installed
editable (`venv_fix`); `pytest -q umap/tests/test_umap_nn.py umap/tests/test_umap_ops.py`:

| | result |
|---|---|
| unmodified master, the two touched test files | 25 passed, 7 skipped (167 s) |
| new tests only, run against unmodified master | **2 failed** (`assert np.all(np.isfinite(sigmas))`, `assert np.all(np.isfinite(model._sigmas))`) |
| with the patch, the two touched test files | 27 passed, 7 skipped (70 s) |

The 7 skips are the project's own `@pytest.mark.skip` NN-descent accuracy tests.
`black --check` (26.5.1): `umap/umap_.py` and `umap/tests/test_umap_ops.py` unchanged;
`umap/tests/test_umap_nn.py` has one pre-existing blank-line difference at master (line
12) that black 26 would collapse; the patch does not touch it.

## Order of operations

1. Open the issue from `issue-u1-disconnected-sigma-inf.md` (paste a fresh run of
   `mcve_u1.py`).
2. Push `fix/smooth-knn-dist-disconnected-floor` to a fork, open the PR with
   `pr-body.md`, filling in the issue number (CONTRIBUTING asks for it).
3. Record numbers and any maintainer response in `../README.md` and the top-level table.
