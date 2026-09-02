# Scanpy upstream filing kit

_Prepared 2026-09-02 against `scverse/scanpy` `main` @ `a656a33b`. Nothing filed yet.
Both fix branches are pushed to the fork [cindykrafft/scanpy](https://github.com/cindykrafft/scanpy):
[`fix/rank-genes-groups-ttest-log-space`](https://github.com/cindykrafft/scanpy/tree/fix/rank-genes-groups-ttest-log-space) (SC1, `08d3cc7`) and
[`fix/score-genes-equal-frequency-bins`](https://github.com/cindykrafft/scanpy/tree/fix/score-genes-equal-frequency-bins) (SC2, `a49d862`), each one commit on top of `a656a33b`._

## What was read before preparing this (step 4 of the method)

- `CONTRIBUTING.md`: search the tracker first; minimal complete verifiable example;
  environment via `sc.logging.print_versions()`.
- `.github/ISSUE_TEMPLATE/bug-report.yml` (fields reproduced in the issue texts) and
  `config.yml` (analysis questions go to Discussions, not issues).
- `docs/dev/code.md` and `docs/dev/documentation.md`: fork, `fix/*` branch, tests
  passing, release-note fragment via towncrier (`fragment.fix.name = "Bug fixes"` in
  `pyproject.toml`; fragments live in `docs/release-notes/`), Ruff formatting.
- `.github/pull_request_template.md`: "Closes #", tests included or why not, release
  note or why not.
- `NEWS`/release notes 1.12.3 (PR #4204), 1.13.0a1 (PR #4037), 1.13.0a2.
- Matthew Rocklin's "Craft Minimal Bug Reports" (linked from the bug-report form; read
  from a copy supplied by the user): both samples use random data made in the script,
  contain no line that is not needed to reproduce, end in an assertion or error, carry
  the complete traceback, state expected vs got, and record what shrinking the example
  revealed (SC1: any log1p matrix reproduces it, wilcoxon unaffected; SC2: the exact
  rounding condition on N). Each was run on `main` and on 1.12.4.
- Issue tracker searched 2026-09-02 for both findings (`mean_in_log_space`, t-test /
  exponentiation; `score_genes` bins / controls / top genes): no prior report of
  either. Nearest: #1454, #967 (log-input assumption), #3169, #2153 (other
  `score_genes` bugs, closed).

No results-stability policy of the DESeq2 kind exists; behaviour-changing bug fixes are
routine in the changelog. Both fixes change numbers, so each gets an issue first and a
PR that references it.

## Contents

| file | what |
|---|---|
| `issue-sc1-ttest-scale.md` | bug report for SC1, template fields, reproduction on `pbmc68k_reduced` |
| `issue-sc2-score-genes-bins.md` | bug report for SC2, template fields, closed-form bin table, reproduction |
| `0001-fix-run-t-test-on-log-values-regardless-of-mean_in_l.patch` | SC1 fix + test + release-note fragment (`git am`-able against `a656a33b`) |
| `0002-fix-build-n_bins-equal-frequency-expression-bins-in-.patch` | SC2 fix + regression test + seed pin + release-note fragment |
| `pr-bodies.md` | PR titles and bodies following the template |

## Verification status of the patches

Run in a Python 3.12 venv with master installed editable (`uv pip install -e <clone>
scikit-misc igraph leidenalg pytest pytest-mock pytest-xdist pytest-rerunfailures
pooch`):

| patch | new test on unmodified `main` | test file with patch |
|---|---|---|
| 0001 | `test_mean_in_log_space_does_not_change_ttest`: **2 failed** (both methods) | `tests/test_rank_genes_groups.py`: 40 passed, 35 skipped, 1 xfailed (the skips need optional deps: dask, illico) |
| 0002 | `test_bins_are_equal_frequency`: not run on main (it would fail: 1-gene top bin at N = 18,000) | `tests/test_score_genes.py`: 30 passed, **1 failed** — `test_score_with_reference`, whose pinned pickle must be regenerated (see `pr-bodies.md`); the `paul15` download is blocked from this environment, so it could not be regenerated here |

Ruff: `ruff check` and `ruff format --check` pass on the changed files of both
branches (the project's `pyproject.toml` configuration).

## Order of operations

1. Open the SC1 issue, then the SC2 issue (texts above; paste the reproduction
   output from a fresh run).
2. Open PR 1 from the fork's `fix/rank-genes-groups-ttest-log-space` (the patch is
   already on it); rename the fragment to `<PR>.fix.md` once the PR number exists.
3. On the fork's `fix/score-genes-equal-frequency-bins`, regenerate
   `tests/_data/score_genes_reference_paul2015.pkl` with the snippet in
   `pr-bodies.md`, commit it, rename the fragment, open PR 2.
4. Record issue and PR numbers, and every maintainer response, in
   `../README.md` and the top-level status table.
