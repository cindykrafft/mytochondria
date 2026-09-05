# #1423 on the 4.0.0 tree (`4db9d816`, 2026-09-04)

_Re-verified 2026-09-05 against `deeptools/deepTools` `master` @ `4db9d816` ("4.0.0 cleanup
(#1450)"), built with `maturin develop --release` into a Python 3.12 venv (cargo 1.94, crates.io
through the proxy). The 3.5.6 kit in the parent directory stays as the record for PyPI's current
release; its patch no longer applies (the package moved to `pydeeptools/deeptools/` and
`computeMatrix` is Rust-backed). Branch `fix4/issue-1423-sort-gzipped-bed` exists only in the local
clone; nothing was filed or pushed._

## Status: half fixed by 4.0.0, half survives

| path | 3.5.6 | 4.0.0 (`4db9d816`) |
|---|---|---|
| `computeMatrix ... -R regions.bed.gz` (the command in the issue) | crash (`TypeError` in `loadBED`) | **fixed**: the `deeptools.computeMatrix2` entry point calls `hp.r_computematrix`, which reads gzipped BED/GTF through `flate2::MultiGzDecoder` (`src/filehandler.rs:64-75`) and does its own `--sortRegions keep`; the project's `test_computeMatrix_referencepoint.py` already covers gz inputs. `CHANGES.txt` 4.0.0 lists it. |
| `computeMatrixOperations sort -R regions.bed.gz` | crash | **survives**: `pydeeptools/deeptools/computeMatrixOperations.py:597-598` (`loadBED`) is unchanged, `sortMatrix` (`:691-727`) still opens the file with `dti.openPossiblyCompressed` and hands the binary handle to `loadBED`; same `TypeError: startswith first arg must be bytes or a tuple of bytes, not str` |
| `computeMatrix_old` (the 3.5.6 Python path, kept "during the transition") | crash | crash (same code) |

## Reproduction ([`repro.py`](repro.py), adapted from the 3.5.6 one)

Builds a bigWig and a three-region BED named `genes.bed` (see the caveat below), gzips it,
runs the Rust-backed `computeMatrix` on the plain BED, then `computeMatrixOperations sort`
with the plain and the gzipped BED.

Before ([`repro.before.out`](repro.before.out)), unmodified `4db9d816`:

```
== computeMatrix (Rust backend) genes.bed (default --sortRegions keep)
RESULT: ok, region order in the matrix: ['geneC', 'geneA', 'geneB']
== computeMatrixOperations sort -R genes.bed
RESULT: ok, region order after sort: ['geneC', 'geneA', 'geneB']
== computeMatrixOperations sort -R genes.bed.gz
TypeError: startswith first arg must be bytes or a tuple of bytes, not str
RESULT: crashed
```

After ([`repro.after.out`](repro.after.out)), with the patch: all three `RESULT: ok`.

(An earlier run of the same script with the Rust `computeMatrix` on the gzipped BED directly
also gave `RESULT: ok` — that is the "fixed" half.)

## Fix ([`0001-computeMatrixOperations-decode-gzipped-BED-lines-in-.patch`](0001-computeMatrixOperations-decode-gzipped-BED-lines-in-.patch))

The same two lines as the 3.5.6 patch, in `pydeeptools/deeptools/computeMatrixOperations.py`
`loadBED`: decode non-`str` lines as `loadGTF` does. The test half is reduced to
`test_computeMatrixOperations.py::testsortGzippedBED` (sort on a gzipped copy of
`computeMatrixOperations.bed`, same md5 as `testsort`); the 3.5.6 patch's `computeMatrix` test on
a gzipped `test2.bed` is dropped because that path no longer goes through `loadBED` (and
`test_heatmapper.py` no longer exists — the Rust `computeMatrix` tests live in
`test_computeMatrix_referencepoint.py`, which already has gz cases). A `CHANGES.txt` bullet is
appended to the `4.0.0` section (4.0.0 is not released; there is no `unreleased` heading to use).

## Tests (Python 3.12 venv, 4.0.0 built with maturin)

| | new test | `test_computeMatrixOperations.py` | full suite |
|---|---|---|---|
| unmodified `4db9d816` | `testsortGzippedBED`: **1 failed** (`TypeError`) | 7 passed + the new one failing | 232 passed (no failures) |
| with the patch | 1 passed | 8 passed | 233 passed |

`flake8` with the 3.5.6 CI options on the two changed `.py` files: 0 findings (4.0.0's CI has no
flake8 step; `pixi run test` = `pytest pydeeptools/deeptools/test/`). `cargo test` is untouched
(Python-only patch).

## Conventions followed

`.github/CONTRIBUTING.md` (unchanged in 4.0.0), `PULL_REQUEST_TEMPLATE.md` (four checkboxes, in
[`pr-body.md`](pr-body.md)), `pytest` as in `.github/workflows/test_pytest.yml`, `CHANGES.txt`
bullet. The `pyproject.toml`/`Cargo.toml` versions are untouched (`scripts/check_version_sync.py`
in CI compares them with the galaxy wrapper). The issue-thread comment is in
[`comment.md`](comment.md).

## Caveat found on the way (not part of #1423, not patched)

The Rust `computeMatrix` labels a single region file's group by the file *stem*
(`src/computematrix.rs:150-160`: `regions` for `regions.bed`, `regions.bed` for
`regions.bed.gz`), while `computeMatrixOperations sort` with one `-R` file expects the group to
be called `genes` (`sortMatrix`, `defaultGroup = "genes"`, `:699-700`), so sorting a single-BED
4.0.0 matrix fails with "The computeMatrix output is missing the 'genes' region group" unless the
BED happens to be named `genes.bed` — which is why `repro.py` names it so. `computeMatrix_old`
labels the group `genes`. Mentioned at the end of the PR body.
