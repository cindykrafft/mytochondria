# deepTools issue #1423 — computeMatrix crashes on a gzipped BED

**Issue:** [#1423 "Failure to parse (compressed) Bed file in computeMatrix"](https://github.com/deeptools/deepTools/issues/1423),
opened 2026-03-06 (2 comments, not readable from this session). The reporter runs
`computeMatrix reference-point -R peaks.intronic.bed.gz -S ... -p 4` on deepTools 3.5.5 /
Python 3.12 and gets

```
  File ".../deeptools/computeMatrixOperations.py", line 598, in loadBED
    if line.startswith("#") and labelColumn is None:
TypeError: startswith first arg must be bytes or a tuple of bytes, not str
```

and guesses that "whichever library is doing your decompression is passing bytes back".
That guess is right.

_Prepared 2026-09-03 against `deeptools/deepTools` `master` @ `ea0f68bb` (= tag 3.5.6 = PyPI's
latest; no `develop` branch on the remote). Branch `fix/issue-1423-gzipped-bed-sortmatrix`,
one commit `2bc6453`, exists only in the local clone; nothing was filed or pushed._

## Diagnosis (line numbers on `ea0f68bb`)

- `deeptools/computeMatrix.py:227-240`: `--sortRegions` defaults to `keep`; `:418-421`: with
  `keep`, after the matrix is computed `main()` calls
  `cmo.sortMatrix(hm, args.regionsFileName, ...)` to put the rows back in input order.
- `deeptools/computeMatrixOperations.py:691-722` (`sortMatrix`): opens each regions file with
  `dti.openPossiblyCompressed(fname)` — `deeptoolsintervals/parse.py:93-105` returns
  `gzip.open(fname, "rb")` for a gzip file, i.e. a **binary** handle — reads the header lines
  with `dti.getNext(fp)` (`parse.py:15-22`, which decodes bytes), then hands the handle to
  `loadBED(line, fp, ...)`.
- `deeptools/computeMatrixOperations.py:597-598` (`loadBED`): `for line in fp:` followed by
  `line.startswith("#")` — the lines are `bytes` for a gzipped file, so the `str` argument
  raises the `TypeError`. `loadGTF` (`:675-676`) already guards the same loop with
  `if not isinstance(line, str): line = line.decode('ascii')`; `loadBED` never got it.

So the matrix is computed correctly (the deeptoolsintervals parser used for the computation
handles compressed input), and the crash happens just before it is written. It hits every
`computeMatrix` run whose `-R` file is gzipped under the default `--sortRegions keep`
(`--sortRegions no/ascend/descend` avoid the path), and `computeMatrixOperations sort -R
regions.bed.gz`. It is on `master` = 3.5.6 and, by reading, on every release since `keep`
became the default.

## Fix

`deeptools/computeMatrixOperations.py`, `loadBED`: decode non-`str` lines exactly as `loadGTF`
does (two lines). Diff in [`0001-computeMatrix-decode-gzipped-BED-lines-in-sortMatrix.patch`](0001-computeMatrix-decode-gzipped-BED-lines-in-sortMatrix.patch),
which also adds the two tests and a `CHANGES.txt` bullet under an `unreleased` heading.

## Reproduction ([`repro.py`](repro.py))

Self-contained: writes a two-chromosome bigWig with pyBigWig, a three-region BED in
non-genomic order, gzips it, and runs `computeMatrix reference-point` on both files with the
default options (`sys.argv` is set because `main()` prints help when it is empty).

Before ([`repro.before.out`](repro.before.out)), on unmodified `master`:

```
== computeMatrix regions.bed (default --sortRegions keep)
RESULT: ok, region order in the matrix: ['geneC', 'geneA', 'geneB']

== computeMatrix regions.bed.gz (default --sortRegions keep)
Traceback (most recent call last):
  ...
  File ".../deeptools/computeMatrixOperations.py", line 598, in loadBED
    if line.startswith("#") and labelColumn is None:
TypeError: startswith first arg must be bytes or a tuple of bytes, not str
RESULT: crashed
```

After ([`repro.after.out`](repro.after.out)), with the patch:

```
== computeMatrix regions.bed.gz (default --sortRegions keep)
RESULT: ok, region order in the matrix: ['geneC', 'geneA', 'geneB']
```

## Tests

Python 3.12 venv (`uv venv --python /usr/bin/python3.12`; `uv pip install -e src pytest flake8`).

| | new tests | `test_heatmapper.py` + `test_computeMatrixOperations.py` | full suite |
|---|---|---|---|
| unmodified `master` | `test_computeMatrix_gzipped_bed`, `testsortGzippedBED`: **2 failed** (`TypeError`) | 21 passed, 2 failed (the new ones) | 98 passed, 2 failed |
| with the patch | 2 passed | 23 passed | 100 passed, 2 failed |

The two persistent failures are unrelated and identical on both: `test_plotCoverage.py::test_plotCoverage_default`
(pre-existing, also recorded in the audit's `upstream/test-runs.txt`) and `test_tools.py::test_tools`
(`FileNotFoundError: 'alignmentSieve'` — the console scripts are not on `PATH` in this venv).

`flake8` with the CI options (`--ignore=E501,F403,E402,F999,F405,E722,W504,W605`) on the three
changed Python files: 0 findings (14 on `master` overall, none in these files).

- `test_heatmapper.py::test_computeMatrix_gzipped_bed`: gzips the existing `test2.bed`, runs the
  same command as `test_computeMatrix_reference_point`, and checks the matrix equals `master.mat`.
- `test_computeMatrixOperations.py::testsortGzippedBED`: gzips `computeMatrixOperations.bed`,
  runs `computeMatrixOperations sort`, and checks the md5 that the existing `testsort` expects.

## Conventions followed

`.github/CONTRIBUTING.md` (bug branch off `master`, description, tests passing),
`PULL_REQUEST_TEMPLATE.md` (four checkboxes, in [`pr-body.md`](pr-body.md)), `flake8` + `pytest`
as in `.github/workflows/test.yml`, `CHANGES.txt` bullet under `unreleased` (the top heading on
`master` is 3.5.5). The `pyproject.toml` version is untouched. Open PRs checked 2026-09-03: 12,
none touches BED parsing or #1423 (PR #1449 is the audit's DT1 fix). #1423 has no assignee (the `assignee`/`assignees` fields of the search result were empty on 2026-09-03) and no labels, so a PR is appropriate.

## Other candidates considered

The open tracker (162 issues, both pages read with bodies) was screened for wrong numbers,
crashes on valid input and inert options; the DT1–DT9 findings (#1108, #1130, #1118) were skipped.

- **#1346** `plotProfile` on a `--maxThreshold` matrix → `AttributeError: numpy has no attribute
  'warnings'` (numpy ≥ 1.24): genuine crash, but open PRs #1412 and #1393 already replace
  `np.warnings`. Not taken.
- **#1385** `bamCompare` on BAMs with no common chromosomes → `AttributeError: 'list' object has no
  attribute 'name'` (`utilities.py:209`, `bamFileHandles.name` on a list): the "no common
  chromosomes" error message crashes before it prints; a one-line fix, but it only repairs an
  error path on mismatched input. Kept as a fallback.
- **#1267** `bigwigCompare --skipNonCoveredRegions` on sparse (methylation) bigWigs → `[bwClose]`
  truncated-output error, reported on 3.1.3: plausible (probably an empty chromosome/bedGraph after
  skipping), but not reproduced here and the cause is not established from the body alone.
- **#1421** `alignmentSieve` 3.5.6 "Too many open files" from `pysam.samtools.cat` over ~3,000
  temporary chunk files (regression vs 3.5.5): real and worth fixing, but the remedy (batched
  `cat` or a larger default chunk) is a design choice and the reproduction needs a genome-scale
  BAM or a lowered `ulimit`. Left for the maintainers.
- **#1249** `--extendReads` with an estimated fragment length of 0 crashes deep in the counting;
  the estimator (`getFragmentAndReadSize.py`) would need to exclude zero template lengths or bail
  out early — a behaviour decision. **#1194** (`--region` start rounded down to a bin boundary)
  and **#1177/#1268** (`--ATACshift` on fully overlapping pairs) read as design rather than bugs.
- **#1091** `computeMatrix --quiet` does not silence messages: body not retrieved within the
  search budget; `heatmapper.py:404-567` does honour `self.quiet`, so the remaining output is
  probably from deeptoolsintervals.

## Caveats

- The two issue comments could not be read from this session; if a maintainer already proposed a
  different route (e.g. opening the file in text mode in deeptoolsintervals), that is an equally
  valid fix — this patch keeps the change inside deepTools and mirrors what `loadGTF` does.
- The decode uses `'ascii'` for consistency with `loadGTF`; a BED with non-ASCII names would
  still fail on both paths (a separate, pre-existing limitation).
