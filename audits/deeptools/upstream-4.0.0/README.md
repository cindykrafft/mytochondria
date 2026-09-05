# deepTools upstream filing kit — 4.0.0 tree

**Default branch: `master`** (`deeptools/deepTools`), now at `4db9d816` ("4.0.0 cleanup
(#1450)", 2026-09-04): the squash-merge of the 4.0.0 rewrite — a Rust backend (`src/*.rs`,
pyo3/maturin, crate `hp`) behind the `bamCoverage`, `bamCompare`, `computeMatrix`,
`alignmentSieve` and `multiBamSummary` entry points (`deeptools.<tool>2:main` in
`pyproject.toml`; the 3.5.6 Python implementations survive as `<tool>_old`), the Python
package moved to `pydeeptools/deeptools/`. PyPI's latest release is still 3.5.6, so the
3.5.6 kit in [`../upstream/`](../upstream/) remains the record for what users run today;
upstream will only take fixes against this tree, and none of the eight 3.5.6 patches
applies to it.

_Prepared 2026-09-05. 4.0.0 built from `4db9d816` with `maturin develop --release` (cargo
1.94.1, crates.io reachable through the proxy) into a Python 3.12 venv (numpy 2.5.2, pysam
0.24.0, pyBigWig 0.3.25, scipy 1.18.1, matplotlib 3.11.1). **Nothing has been filed or
pushed.** The six fix branches exist only in the local clone; the `git am`-able patches are
in this directory (findings) and in
[`../issue-fixes/1423-gzipped-bed-sortmatrix/v4.0.0/`](../issue-fixes/1423-gzipped-bed-sortmatrix/v4.0.0/)
(the issue fix)._

## Re-verification of the ten items on `4db9d816` (by execution)

Every 3.5.6 harness in [`../verify/`](../verify/) was run unchanged against the 4.0.0 build
(the deepTools executables come from the venv's `bin/`); outputs are the `*.v4.0.0.out`
files there. Two 4.0.0-specific scripts were added where the old harness could not reach
(`dt7b_samflagexclude1024_v4.py`) or where the numbers needed a second look
(`dt2b_plotpca_table_v4.py`, `note_v4_bamcompare_operations.py`).

| finding | status on 4.0.0 | where the logic lives now (`4db9d816`) | evidence |
|---|---|---|---|
| **DT1** `bamCompare --skipZeroOverZero` | **SURVIVES in part**: the coordinate shift is gone (0 of 400 bins misplaced, with or without the option); but a skipped bin between two bins of equal value is written with that value — the second symptom of #1108/#1130 — because the default collapse (`src/bamcompare.rs:380-394`, `coalesce`) merges equal neighbours without checking that they touch. `--no_collapse` correct. | Rust: `src/bamcompare.rs:352-353` (skip), `:380-394` (collapse) | `../verify/dt1_skipzerooverzero_coordinates.v4.0.0.out` (the "189 wrong" there are the 2-decimal output rounding, identical with and without the option); `mcve_outputs.txt` (`chr1 0 300 0` for a 0-100 / 200-300 pair) |
| **DT2** `plotPCA --log2` / `--rowCenter` inert | **FIXED BY 4.0.0** as stated: plotPCA was re-implemented (`CHANGES.txt`), the transforms act on the matrix the SVD sees, every option set now changes the output. But see "new on 4.0.0" below: the table/plot no longer contain sample loadings. | Python: `pydeeptools/deeptools/correlation.py:444-520` (`plot_pca`) | `../verify/dt2_plotpca_log2_rowcenter.v4.0.0.out`, `../verify/dt2b_plotpca_table_v4.v4.0.0.out` |
| **DT3** `--removeOutliers` median instead of MAD | **SURVIVES** (line unchanged) | Python: `pydeeptools/deeptools/correlation.py:109-111` | `../verify/dt3_removeoutliers_mad.v4.0.0.out`: 0 of 25 planted bins flagged, Pearson 0.998 |
| **DT4** `--MNase` four bases for odd fragments | **SURVIVES**: the Rust port made the four bases explicit (`frag_start..frag_start + 4`) | Rust: `src/filtering.rs:293-300` (`manipulate_record`) | `../verify/dt4_mnase_center.v4.0.0.out`: 4 of 6 fragments wrong, all the odd ones; `mcve_outputs.txt` |
| **DT5** BPM ≡ CPM | **SURVIVES** (formula carried over verbatim) | Rust: `src/normalization.rs:30-35` | `../verify/dt5_bpm_equals_cpm.v4.0.0.out`: BPM and CPM tracks identical, sum 2.98e6 / 6.98e6 vs the documented 1e6 |
| **DT6** `--smoothLength` truncated at chunk edges | **FIXED BY 4.0.0**: `bam_pileup` smooths over a whole region and `parse_regions`/`region_divider` never split a chromosome (only `--region` bounds it), so the window is one-sided only at chromosome (or `--region`) ends | Rust: `src/covcalc.rs:506-529` (smoothing), `:80-94` and `:1630-1661` (regions) | `../verify/dt6_smoothlength_chunk_edges.v4.0.0.out`: 0 of 60,000 bins differ from the chromosome-wide sliding mean, with and without `--region` |
| **DT7** `--ignoreDuplicates` left out of the denominator | **NOT APPLICABLE**: the option was removed from bamCoverage/bamCompare (`CHANGES.txt`; `parserCommon.py:82` commented out; the harness fails at argparse). The documented replacement, `--samFlagExclude 1024` on marked duplicates, is counted after `filter_record`, so the CPM factor and the readCount factors use the deduplicated count (166.67 = 1e6/6000 on a 40 %-duplicate sample; factors 1:1 against a duplicate-free sample of equal depth). `--exactScaling` is gone too. | Rust: `src/covcalc.rs:435-502` (`mapped_reads` after `filter_record`) | `../verify/dt7_ignoreduplicates_scaling.v4.0.0.out` (argparse error), `../verify/dt7b_samflagexclude1024_v4.v4.0.0.out` |
| **DT8** multiBigwigSummary zoom-level summaries | **SURVIVES, and worse**: the call is unchanged, and the bigWigs 4.0.0 writes (bigtools) carry zoom spans of 640 and 2560 bp instead of 944/3776, so every bin or region of ≥ 1280 bp is a zoom summary: 10-kb bins median 1.4 % and up to 156 % off (110 of 200 bins by > 1 %), 2-kb bins up to 263 %, and 20 of 200 peak-sized BED regions (those ≥ 1.3 kb) off by up to 126 % — 0 on 3.5.6 tracks | Python: `pydeeptools/deeptools/getScorePerBigWigBin.py:110` (`bwh.stats(chrom, exon[0], exon[1])`) | `../verify/dt8_multibigwigsummary_zoom.v4.0.0.out` |
| **DT9** plotFingerprint over-counts a fragment's last bin | **SURVIVES** (`sumCoveragePerBin.py` byte-identical to 3.5.6; plotFingerprint is still Python) | Python: `pydeeptools/deeptools/sumCoveragePerBin.py:169-199` | `../verify/heldup_fingerprint.v4.0.0.out`: `-n 1000` (step = bin) 560 of 1,000 bins over-counted, totals 1.94×; `-n 2000` exact; all metrics equal the independent formulas on both paths |
| **#1423** computeMatrix on a gzipped BED | **FIXED BY 4.0.0 for `computeMatrix`** (Rust reads gz itself; `CHANGES.txt`, `test_computeMatrix_referencepoint.py` gz cases); **SURVIVES for `computeMatrixOperations sort`** and `computeMatrix_old` (`loadBED` unchanged) | Python: `pydeeptools/deeptools/computeMatrixOperations.py:597-598`, `:691-727` | `../issue-fixes/1423-gzipped-bed-sortmatrix/v4.0.0/repro.before.out` |

Also re-run: the held-up fingerprint metrics (AUC, X-intercept, elbow, JSD, CHANCE,
synthetic JSD) still equal the independent formulas on 4.0.0.

## Patches (one commit each on `4db9d816`, `git am`-able)

| patch | branch | commit | finding | kind | new test fails on `4db9d816`? |
|---|---|---|---|---|---|
| `0001-bamCompare-do-not-collapse-across-a-bin-skipped-by-s.patch` | `fix4/bamcompare-skipzerooverzero-gap` | `57c38f0b` | DT1 (comment for #1108/#1130) | Rust (`src/bamcompare.rs`, one condition) + pytest | yes (`test_bam_compare_ZoverZ_interior_bins`: `3R 0 200 0` ≠ `0-60`, `70-200`) |
| `0002-bamCoverage-MNase-three-centre-bases-for-odd-fragmen.patch` | `fix4/mnase-odd-fragment-centre` | `acfed5b7` | DT4 (comment for #1118) | Rust (`src/filtering.rs`, `+ 4` → `+ 3`) + 2 cargo tests + pytest | yes (cargo: `left: Some([173, 174, 175, 176])`; pytest on `test_paired2.bam`) |
| `0003-plotCorrelation-use-the-median-absolute-deviation-in.patch` | `fix4/plotcorrelation-mad-outliers` | `abfe4a29` | DT3 | Python (`correlation.py`, one line) + pytest in `test_plotcorrelation.py` | yes |
| `0004-multiBigwigSummary-compute-bin-means-from-the-exact-.patch` | `fix4/multibigwigsummary-exact-stats` | `cd84ae6f` | DT8 | Python (`getScorePerBigWigBin.py`, `exact=True`) + new pytest + corrected `test_multiBigwigSummary_gtf` expectations | yes (2 failed) |
| `0005-plotFingerprint-credit-only-the-covered-bases-of-a-f.patch` | `fix4/sumcoverage-partial-bins` | `12a443fc` | DT9 | Python (`sumCoveragePerBin.py`) + new `test_sumCoveragePerBin.py` | yes |
| `../issue-fixes/1423-gzipped-bed-sortmatrix/v4.0.0/0001-*.patch` | `fix4/issue-1423-sort-gzipped-bed` | `265aaa21` | #1423 (sort path) | Python (`computeMatrixOperations.py`, two lines) + pytest | yes |

DT5 has an updated issue text (`issue-dt5-bpm-is-cpm.md`, citing `src/normalization.rs`)
and no patch — code-or-documentation decision for the maintainers, as before. DT2, DT6
and DT7 need nothing on 4.0.0. The 3.5.6 Python patches 0003/0006/0007 and the #1423 patch
re-applied cleanly with the `deeptools/` → `pydeeptools/deeptools/` path rewrite except for
their `CHANGES.txt` hunk (the file's top heading is now `4.0.0`) and the #1423 test in the
removed `test_heatmapper.py`; they were rebuilt as fresh commits rather than rebased so the
messages and bullets describe the 4.0.0 situation.

Every patch appends its bullet to the `4.0.0` section of `CHANGES.txt` (that is
`pyproject.toml`'s version, unreleased; there is no `unreleased` heading in the file). The
bullets are the only textual conflict between the patches. `pyproject.toml`, `Cargo.toml`
and `galaxy/wrapper/deepTools_macros.xml` versions are untouched (CI's
`scripts/check_version_sync.py` compares them).

## Test runs (`test-runs.txt`)

Unmodified `4db9d816`: `pytest pydeeptools/deeptools/test/` **232 passed, 0 failed**
(86 s; the 3.5.6 pre-existing `test_plotCoverage_default` failure is gone); `cargo test`
**48 passed**.

| patch | new test(s) on unmodified `4db9d816` | `cargo test` with the patch | touched pytest modules with the patch | full pytest suite with the patch | doctests | flake8 (3.5.6 CI options) on changed `.py` |
|---|---|---|---|---|---|---|
| 0001 (DT1, Rust) | 1 failed | 48 passed | `test_bamCoverage_and_bamCompare.py`: 22 passed | 233 passed | — | 0 |
| 0002 (DT4, Rust) | cargo 1 failed (+1 passed: the even case); pytest 1 failed | **50 passed** | `test_bamCoverage_and_bamCompare.py`: 22 passed | 233 passed | — | 0 |
| 0003 (DT3) | 1 failed | (unchanged) | `test_plotcorrelation.py` + `test_plotPCA.py`: 21 passed | 233 passed | `correlation.py`: 1 passed | 0 |
| 0004 (DT8) | 2 failed | (unchanged) | `test_bigwigCompare_and_multiBigwigSummary.py`: 8 passed | 233 passed | `getScorePerBigWigBin.py`: 3 passed | 0 |
| 0005 (DT9) | 1 failed | (unchanged) | `test_sumCoveragePerBin.py` + `test_plotFingerprint.py`: 4 passed | 233 passed | `sumCoveragePerBin.py`: 1 passed | 0 |
| #1423 | 1 failed | (unchanged) | `test_computeMatrixOperations.py`: 8 passed | 233 passed | — | 0 |

(4.0.0's CI — `test_pytest.yml`, `test_rust.yml` — runs `pixi run test` = `pytest
pydeeptools/deeptools/test/` on Python 3.12–3.14 and `cargo test`; it has no flake8 step
any more. flake8 was still run with the 3.5.6 options for information.) The Rust-patched
builds were also run through the original harnesses: `dt4_mnase_center.py` reports 0 of 6
fragments wrong with 0002, and `mcve_dt1_skipzerooverzero_gap.py` passes its assertion with
0001.

## What was read before preparing this (step 4 of the method)

- `.github/CONTRIBUTING.md`, `ISSUE_TEMPLATE.md`, `PULL_REQUEST_TEMPLATE.md`: unchanged
  from 3.5.6 (fork, bug branch, description, tests passing; four-item issue checklist;
  four PR checkboxes).
- `.github/workflows/test_pytest.yml` (pixi build + `pytest -v`, wheel build/install, and
  `scripts/check_version_sync.py`), `test_rust.yml` (`cargo build`, `cargo test` on
  stable), `test_planemo.yml` (galaxy wrappers), `wheels.yml`. No flake8.
- `CHANGES.txt` 4.0.0 section: the entries that decide DT2 (plotPCA re-implemented, "proper
  handling of --transpose, --log2/--rowCenter and --ntop"), DT7 (`--ignoreDuplicates`
  removed, use `--samFlagExclude`; `--exactScaling` removed), #1423 (gzipped BED/GTF
  supported in the Rust tools), and "large scale values precision slightly altered with new
  backend (f32 vs f64)".
- `pyproject.toml` (`[project.scripts]`: which entry point is Rust-backed and which is the
  `_old` Python path), `Cargo.toml`, `src/lib.rs`, `src/tests/mod.rs`.
- The Rust sources for the findings: `src/bamcoverage.rs`, `src/bamcompare.rs`,
  `src/covcalc.rs` (`parse_regions`, `bam_pileup`, `region_divider`), `src/filtering.rs`,
  `src/normalization.rs`, `src/calc.rs`, `src/filehandler.rs` (`write_covfile`,
  `open_bed_or_gtf_reader`), `src/computematrix.rs` (group labels, `sortregions`).
- The Python modules still on the path: `correlation.py`, `plotPCA.py`,
  `getScorePerBigWigBin.py`, `sumCoveragePerBin.py`, `plotFingerprint.py`,
  `computeMatrixOperations.py`, `computeMatrix2.py`, `bamCoverage2.py`, `bamCompare2.py`,
  `parserCommon.py` (help texts), and the test modules the patches touch.
- The issue tracker was not re-searched from this session (no network access to GitHub
  here beyond the git proxy); the 2026-09-03 search in `../upstream/README.md` stands:
  DT1 = #1108/#1130, DT4 = #1118, #1423 for the issue fix, nothing for the others. Check
  the tracker for anything opened since 2026-09-03 — in particular whether the 4.0.0
  merge closed or touched #1108/#1130/#1118/#1423 — before posting.

## New on 4.0.0, outside the ten items (observed while re-verifying)

These are wrong numbers or breaks introduced by the rewrite, seen by execution on
`4db9d816`. **Items 1–4 are now kitted in [`new/`](new/)** (2026-09-05): items 1, 2 and 4
with fix branches, patches, tests that fail on `4db9d816` and MCVEs; item 3 as a measured
note with the defect-vs-design call (no patch). Item 5 is DT8's row above (patch 0004). The
text below is the original observation.

1. **`bamCompare --operation first|second|add|mean` produce the log2 track.** `calc_ratio`
   (`src/calc.rs:209-259`) has arms for `log2`, `ratio`, `reciprocal_ratio` and `subtract`
   and a catch-all `_` that computes log2; the CLI still offers all eight operations. On
   `testA.bam`/`testB.bam` the four outputs are byte-identical to `--operation log2`
   (`../verify/note_v4_bamcompare_operations.v4.0.0.out`). Wrong number under an offered
   option; a small patch (four arms) is straightforward. In the same function
   `reciprocal_ratio` is inverted against 3.5.6's definition (`getRatio.py`: a/b if a/b ≥ 1
   else −b/a): the Rust arm returns b/a for a/b ≥ 1 and −a/b otherwise (2/3 → −0.67 where
   3.5.6 gives −1.5; the doctest values 2.0 / −2.0 become 0.5 / −0.5).
2. **plotPCA's table and plot no longer contain sample loadings.** `plot_pca` now writes
   `Wt = U * S` (the PC scores of the *rows*, i.e. of the selected bins) and emits row `i`
   of that as "Component i" across the sample columns, and plots `Wt[PC1-1, :]` against
   `Wt[PC2-1, :]` — the first two selected bins' scores across components, one point per
   *component* labelled as a sample. Verified by reproducing the arithmetic in numpy
   (`../verify/dt2b_plotpca_table_v4.py`): every table row equals `(U*S)[i, :]`, none
   equals `Vt` (the loadings 3.5.6 wrote). `--transpose` is right (`Wt.T` gives each
   sample's projection). The default plotPCA — the mode 19 cohort papers used — is
   therefore drawing the wrong quantity on the current master. Eigenvalues are now
   `S²/(n−1)` instead of `S²` (a definition change, fine).
3. **Output values are rounded to two decimals.** `src/bamcoverage.rs:274-282` and
   `calc_ratio` round every emitted value to `round(x·100)/100` (f32). For deep libraries
   and small bins normalised values fall below 0.01 (CPM of one read at 2×10⁸ mapped reads
   is 0.005, RPGC of one read in a 1-bp bin at 1× coverage is 1.0 but at 10-bp bins with
   low depth …), and log2 ratios lose everything past the second decimal (the DT1 harness's
   189 "wrong" bins). `CHANGES.txt` calls this "precision slightly altered (f32 vs f64)".
4. **`computeMatrixOperations sort` cannot sort a single-BED matrix from the Rust
   `computeMatrix`** unless the BED is named `genes.bed`: the Rust side labels the group by
   the file stem (`src/computematrix.rs:150-160`), the sort expects `genes`
   (`computeMatrixOperations.py:699-700`). Noted at the end of the #1423 PR body.
5. **multiBigwigSummary's zoom problem got a wider reach** because bigtools writes finer
   zoom levels (DT8 row above): peak-sized regions from 1.3 kb are now affected.

## Contents

| file | what |
|---|---|
| `comment-dt1-1108-1130.md` | comment for #1108/#1130 on the 4.0.0 tree: shift fixed, gap-bridging remains, MCVE, fix |
| `comment-dt4-1118.md` | comment for #1118: `src/filtering.rs` cause, MCVE, one-token fix |
| `issue-dt5-bpm-is-cpm.md` | bug report for the 4.0.0 tree: BPM track is the CPM track (`src/normalization.rs`), two possible fixes, no patch |
| `mcve_dt1_skipzerooverzero_gap.py`, `mcve_dt4_mnase.py`, `mcve_outputs.txt` | the reproductions embedded in the two comments and their output on 4.0.0 |
| `0001-*.patch` … `0005-*.patch` | fix + regression test + `CHANGES.txt` bullet, `git am`-able on `4db9d816` |
| `pr-bodies.md` | PR titles and bodies in the template's checkbox form |
| `test-runs.txt` | the pytest / cargo / doctest / flake8 numbers above, as captured |

The DT2, DT3, DT8 and DT9 issue texts of the 3.5.6 kit (`../upstream/issue-dt*.md`) still
describe the cause correctly; before filing DT3/DT8/DT9 against 4.0.0, replace the file
paths (`pydeeptools/deeptools/...`), the version line (4.0.0 @ `4db9d816`, plus 3.5.6 as
the released version), and for DT8 the numbers by the 4.0.0 row above.

## Order of operations (unchanged in spirit from `../upstream/README.md`)

1. Post `comment-dt1-1108-1130.md` on #1108 (link #1130) and `comment-dt4-1118.md` on
   #1118; open PRs 1 and 2 from patches 0001/0002, referencing those numbers.
2. Open the DT8, DT3, DT9 issues (in that order of impact, DT8 first since 4.0.0 widened
   it), then PRs 4, 3, 5 with the issue numbers filled into `pr-bodies.md` and the
   `CHANGES.txt` bullets. Open DT5 as an issue only.
3. The #1423 PR from `../issue-fixes/1423-gzipped-bed-sortmatrix/v4.0.0/`, with its
   comment on the thread.
4. The "new on 4.0.0" items 1 and 2 (kitted in [`new/`](new/)) change numbers under default
   or offered settings on the tree upstream is about to release and rank above DT3/DT9;
   item 4 follows them, item 3 is an issue without a patch. See `new/README.md`.
