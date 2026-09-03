# Scrublet / Scanpy-port upstream filing kit

_Prepared 2026-09-03 against `swolock/scrublet` `master` @ `67f8ecb` (= PyPI 0.2.3) and
`scverse/scanpy` `main` @ `a656a33b`. **Nothing has been filed.** The two Scanpy patches are pushed to the fork
[cindykrafft/scanpy](https://github.com/cindykrafft/scanpy) as `fix/scrublet-knn-neighbour-count` (`336bf96`)
and `fix/scrublet-log-transform-order` (`a6d16cd`), each one commit on `a656a33b`, ruff-clean; the
Scrublet-original patches stay as `git format-patch` output because that repository is unmaintained
(last commit 2020-12-28) and will not be filed._

## What was read before preparing this (step 4 of the method)

### Scrublet

- `README.md` (the only project document): quick start, best practices, install from
  PyPI or source, links to old versions. No `CONTRIBUTING.md`, no `.github/` directory,
  no issue or PR template, no changelog or NEWS, no `tests/`, no CI configuration
  (`find` over the clone, 2026-09-03). `setup.py` pins nothing and lists `annoy`,
  `umap-learn`, `numba`, `cython` as requirements.
- Git history: 39 commits, last 2020-12-28 ("Use arpack for PCA and fix plotting bug",
  then a README edit); PyPI releases 0.2 (2019-04-18), 0.2.1 (2019-07-03), 0.2.2 and
  0.2.3 (both 2020-12-29). The 0.2.3 wheel's source equals master's.
- Issue tracker searched 2026-09-03 for `subsample`, `total counts`, `mean_center`,
  `normalize_variance`, `np.matrix`, `threshold_minimum`, `expected_doublet_rate`,
  score formula: no prior report of SR2 or SR4. Nearest: #58 "Question
  normalize_variance" (open, 2023), #16 "Unimodal distributions, log transformation, and
  homogeneous data sets" (open, 2020, 0 comments), #39 threshold on non-bimodal
  histograms (open, 2022). Open issues from 2020 onward have no maintainer replies.
- Consequence for the kit: plain issue texts (no template fields), each a Minimal
  Complete Verifiable Example in Rocklin's sense (synthetic data made in the script,
  nothing that is not needed, complete traceback where there is one, expected vs got,
  what shrinking revealed), and a patch that adds a small `tests/` file because there is
  no suite to extend. The project's non-existent linter and test runner could not be
  run; the new tests were run with pytest 9 in the audit venv.

### Scanpy

- `CONTRIBUTING.md`: search first; minimal complete verifiable example (links Rocklin);
  `sc.logging.print_versions()`.
- `.github/ISSUE_TEMPLATE/bug-report.yml`: three checkboxes (not already reported;
  exists on the latest version; optionally on `main`), "What happened?", "Minimal code
  sample" that must carry inline script metadata so `uv run issue.py` reproduces it
  against `main`, "Error output", "Versions". `config.yml`: how-to questions go to
  Discourse. Both issue texts below follow these fields.
- `docs/dev/code.md`, `documentation.md`, `testing.md`: fork, branch, tests via
  `hatch test`/pytest, Ruff formatting and linting (`hatch check fmt --fix`, `hatch
  check code --fix`; `tool.ruff.lint` in `pyproject.toml`, including the `TID251` ban on
  constructing `scipy.sparse.*_matrix` without `# noqa: TID251`), a towncrier fragment
  per PR in `docs/release-notes/` named `+<name>.fix.md` until the PR number exists
  (`fragment.fix.name = "Bug fixes"`), `{smaller}` author credit.
- `.github/pull_request_template.md`: "Closes #", tests included or why not, release
  notes not necessary because… The scanpy audit's kit records that the "Check for
  release notes" workflow looks for `<PR>.fix.md` and that "Check title, milestone, and
  labels" fails on every external PR until a maintainer assigns a milestone.
- Issue tracker searched 2026-09-03 (`scrublet neighbors self k_adj`, `scrublet
  log_transform normalize_total order`, `scrublet subsample total_counts`, `neighbors
  duplicate identical cells`): no prior report of SR1 or SR3. Related: #2244 "Scanpy
  neighbors bug with identical/almost identical cells" (open, 2022 — duplicate cells get
  zero neighbours; the same `_remove_self_column` by position is behind SR1's branch),
  #3068 "Broken Scrublet Test" (open, 2024 — `test_scrublet_data` differs by one cell at
  1e-15 on CI), #1644/#1645 (closed, threshold ignored / dense input).
- No results-stability policy of the DESeq2 kind; behaviour-changing fixes are routine
  in the changelog. Both fixes change numbers, so each gets an issue first and a PR that
  references it.

## Contents

| file | what |
|---|---|
| `scrublet/issue-sr2-subsample-totals.md` | plain issue text for SR2 with MCVE and the closed form |
| `scrublet/issue-sr4-mean-center-np-matrix.md` | plain issue text for SR4 with MCVE and traceback |
| `scrublet/0001-Fix-inflated-total-counts-of-UMI-subsampled-syntheti.patch` | SR2 fix + `tests/test_subsample_counts.py` (`git am` against `67f8ecb`) |
| `scrublet/0002-Fix-TypeError-in-scrub_doublets-mean_center-True-nor.patch` | SR4 fix + `tests/test_mean_center.py` |
| `scanpy/issue-sr1-knn-neighbour-count.md` | bug report for SR1 in the template's fields, `uv run`-able reproducer |
| `scanpy/issue-sr3-log-transform-order.md` | bug report for SR3 in the template's fields |
| `scanpy/0001-fix-score-scrublet-doublets-over-k_adj-neighbors-not.patch` | SR1 fix + test + fragment (`git am` against `a656a33b`) |
| `scanpy/0002-fix-log-transform-scrublet-s-observed-and-simulated-.patch` | SR3 fix + test + fragment |
| `pr-bodies.md` | PR titles and bodies following each project's convention |

## Verification status of the patches

Python 3.12 venv, editable installs of both clones, pytest 9, ruff 0.16.5.

| patch | new test on unmodified code | with the patch | linter |
|---|---|---|---|
| scrublet 0001 (SR2) | **2 failed**: `test_subsampled_totals_scale_with_rate` (mean 2250.3 vs 2000 expected) and `test_subsampled_counts_are_thinned` (the returned totals differ from the thinned row sums even with every gene kept) | 2 passed | project has none |
| scrublet 0002 (SR4) | `test_scrub_doublets_mean_center_without_variance_normalisation` **fails** (`TypeError: np.matrix is not supported`) | 1 passed | project has none |
| scanpy 0001 (SR1) | `test_scrublet_knn_uses_k_adj_neighbors[distinct/coincident × False/None]`: **4 failed** on `main` (39–66 % of scores off, max 0.180) | 4 passed | `ruff check` and `ruff format --check` clean on `core.py`, `tests/test_scrublet.py` |
| scanpy 0002 (SR3) | `test_scrublet_log_transform_consistent`: **fails** on `main` (278 of 300 scores off, max 0.255) | 1 passed | clean on `__init__.py`, `tests/test_scrublet.py` |

The rest of scanpy's `tests/test_scrublet.py` (24 tests) could not run here: every
one of them loads `pbmc3k` via `exampledata.scverse.org`, which the session's proxy
refuses (`403 Forbidden`); on unmodified `main` the file gives 15 failed, 9 errors for
that reason alone. Because SR1 changes every score slightly, the pinned expectations in
`test_scrublet` (`[13, 138]`, `0.149254`; `[180]`, `0.219178`) and `test_scrublet_batched`
will need regenerating on a host that can fetch the data — the PR body says so. The SR3
test was deliberately written on counts generated inside the test so that it runs
without a download.

## Order of operations

1. Open the two scrublet issues; then two PRs from the patches (branches
   `fix/subsample-counts-totals`, `fix/mean-center-np-matrix` in the local clone).
   Do not expect a reply; the record is the point.
2. Open the SR1 issue on scanpy, then the PR from `fix/scrublet-knn-neighbour-count`;
   rename `docs/release-notes/+scrublet-knn-neighbour-count.fix.md` to `<PR>.fix.md`
   once the number exists; regenerate the pinned test values. Mention #2244 as related.
3. Open the SR3 issue, then the PR from `fix/scrublet-log-transform-order`; rename the
   fragment likewise.
4. Record issue and PR numbers and every maintainer response in `../README.md` and the
   top-level status table.
