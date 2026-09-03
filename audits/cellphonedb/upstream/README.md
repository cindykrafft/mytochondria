# CellPhoneDB upstream filing kit

_Prepared 2026-09-03 against `ventolab/CellphoneDB` `master` @ `dc8abd15` (version string 5.0.1).
**Filed 2026-09-03:** issue [#231](https://github.com/ventolab/CellphoneDB/issues/231) (CPDB1, the
duplicate-permutation finding, which has no patch by design). CPDB2–CPDB6 wait for a maintainer signal. Both fix branches
are pushed to the fork [cindykrafft/CellphoneDB](https://github.com/cindykrafft/CellphoneDB),
each one commit on top of `dc8abd15`:
[`fix/iterations-zero-progress-step`](https://github.com/cindykrafft/CellphoneDB/tree/fix/iterations-zero-progress-step)
(`06575c3`, patch 0001, CPDB5) and
[`fix/scoring-pandas3-index`](https://github.com/cindykrafft/CellphoneDB/tree/fix/scoring-pandas3-index)
(`e481263`, patch 0002, CPDB6)._

## What was read before preparing this (step 4 of the method)

The repository's contributing conventions are **very light**, and that is a finding in itself
for anyone filing here — there is little to comply with and nothing to guess at:

- **`CONTRIBUTING.md`: does not exist.** `find` over the tree for
  `*contribut*`, `*template*`, `*conduct*`, `*changelog*`, `*news*` returns **nothing**.
- **`.github/` contains exactly one file**, `workflows/python-app.yml`. There are no issue
  templates, no `config.yml`, no pull-request template.
- The whole of the stated policy is `README.md:242-244`: "CellphoneDB is an open-source project.
  If you are interested in contributing to this project, please let us know", pointing at the
  readthedocs documentation. There is no results-stability policy of the DESeq2 kind, and no
  statement about what may or may not change numbers.
- **Release notes** are prose in `previous_releases.md` and in the release-notes section of
  `docs/RESULTS-DOCUMENTATION.md`, organised per release, not per PR. There is **no changelog
  fragment convention**, so neither patch adds one; the release-note wording for a
  behaviour-changing fix would be the maintainers' to write.
- **CI** (`.github/workflows/python-app.yml`): Python **3.8**;
  `flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics` (blocking), then
  `flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127` (advisory), then
  `cd cellphonedb/src/tests && pytest method_tests.py`. Both patches were checked against both
  flake8 invocations.
- **`docs/RESULTS-DOCUMENTATION.md`** in full — it is the specification these findings are
  measured against, and the line numbers cited in the issues come from it.
- **Curation vs code:** `docs/RESULTS-DOCUMENTATION.md:427` sends database-content questions to
  <contact@cellphonedb.org> or to the separate `ventolab/cellphonedb-data` repository. All six
  findings here are code, so they belong on this repository's tracker.
- Matthew Rocklin's "Craft Minimal Bug Reports": every reproduction below builds its own data in
  the script (the database included, via the package's own `db_utils.create_db`), contains no line
  that is not needed, ends in an assertion or the real traceback, states expected vs got, and
  records what shrinking the example revealed.
- **Issue tracker searched 2026-09-03** for all six findings. Nothing found for CPDB1, CPDB3,
  CPDB4, CPDB5 or CPDB6. For CPDB2 the near neighbours are #179 "Can Minimum p-value less than
  1e-3" (closed), #60 "Precision of pvalues" (closed), #24, #155 "Exact p-value output file?"
  (open), #121 "Pvalue adjusting" (closed) and #124 — all about the *resolution* of the reported
  p-values, none raising the strict-vs-inclusive rule or `p = 0`.

  **Limitation, and it matters before filing:** from this session only the GitHub issue *search*
  API is available for this repository; the issue-*reading* endpoints are not, and `github.com`
  HTML is blocked. So the issue **titles and bodies** above were read, but **not the maintainers'
  replies**. #179 and #60 are close enough to CPDB2 that their replies must be read first, in case
  the estimator has already been explained there. Do that before opening the CPDB2 issue.

## Contents

| file | what |
|---|---|
| `issue-cpdb1-thread-duplicate-permutations.md` | CPDB1: workers draw identical shuffles; distinct-permutation counts, effective sample size, session re-use |
| `issue-cpdb2-pvalue-strict-inequality.md` | CPDB2: strict `>` drops ties and allows p = 0; exhaustive 1,680-permutation evidence and the real-data 42.6 % figure |
| `issue-cpdb3-method1-threshold-ignored.md` | CPDB3: `threshold` inert in METHOD 1; byte-identical outputs at 0.1 and 0.99 |
| `issue-cpdb4-deconvoluted-subunit-means.md` | CPDB4: subunit rows carry the complex minimum |
| `issue-cpdb5-iterations-zerodivision.md` | CPDB5: `ZeroDivisionError` at `threads=1, iterations <= 50` |
| `issue-cpdb6-scoring-pandas3.md` | CPDB6: scoring fails on pandas >= 3 |
| `0001-fix-do-not-divide-by-a-zero-progress-step-when-itera.patch` | CPDB5 fix + regression test (`git am`-able on `dc8abd15`) |
| `0002-fix-apply-the-gene-name-index-in-scoring-which-panda.patch` | CPDB6 fix + regression test (`git am`-able on `dc8abd15`) |
| `pr-bodies.md` | PR titles and bodies |

## Verification status of the patches

Run in a Python 3.12 venv with master installed editable (`uv pip install -e <clone>`), pandas
3.0.5:

| patch | new test on unmodified `master` | with the patch | flake8 (both CI invocations) |
|---|---|---|---|
| 0001 (CPDB5) | **1 failed** (`ZeroDivisionError: float modulo`) | 1 passed | 0 / 0 |
| 0002 (CPDB6) | **1 failed** (0 rows returned instead of 5) | 1 passed | 0 / 0 |

Both patches were confirmed to apply to a clean `master` with `git am`, independently of each
other. They touch the same anchor in `method_tests.py`, so applying both in sequence needs a
trivial rebase — each is written to go in on its own.

**The project's own test suite could not be run here.** `cellphonedb/src/tests/method_tests.py`
downloads the v4.1.0 database from `github.com/ventolab/cellphonedb-data` in `setUp`, which
returns HTTP 403 from this environment, so all seven existing tests error out before running. The
two new tests were therefore written to need no download — which is also why they can run in CI —
and were executed with and without each patch, as above. Anyone with network access should run
the full `pytest method_tests.py` on each branch before opening the PRs.

## Order of operations

1. **Read the replies on #179 and #60** (not readable from this session). If the strict-inequality
   rule is already explained there, fold that into the CPDB2 issue rather than opening it cold.
2. File CPDB5 and CPDB6 first: both are unambiguous, neither changes a number, and each has a
   tested patch. Open the issue, then the PR referencing it.
3. File CPDB2. It is the finding that touches every published p-value, and it needs a maintainer
   decision (`>=`, or `(b+1)/(m+1)`, or documentation), so it goes as an issue with the
   measurements and no patch.
4. File CPDB1 as an issue with the measurements; offer the `SeedSequence` patch rather than
   pushing one, since the seeding scheme is a design choice.
5. File CPDB3 and CPDB4. Both change what a documented output file contains, so issue first.
6. Record issue and PR numbers, and every maintainer response, in `../README.md` and the
   top-level status table — including anywhere the maintainers' reading overturns one of these.
