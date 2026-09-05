**Filed 2026-09-05:** item 1 as issue [#1457](https://github.com/deeptools/deepTools/issues/1457) + PR [#1458](https://github.com/deeptools/deepTools/pull/1458); item 2 as issue [#1459](https://github.com/deeptools/deepTools/issues/1459) + PR [#1460](https://github.com/deeptools/deepTools/pull/1460). Items 3 and 4 held.

# deepTools 4.0.0 — the four defects introduced by the rewrite (filing kit)

_Prepared 2026-09-05 against `deeptools/deepTools` `master` @ `4db9d816` ("4.0.0 cleanup
(#1450)", 2026-09-04), the squash-merge of the Rust-backend rewrite; PyPI still ships 3.5.6,
so none of this reaches a released version yet — which is the point of filing now. Build:
`maturin develop --release` (cargo 1.94.1) into a Python 3.12.3 venv (numpy 2.5.2, scipy
1.18.1, pysam 0.24.0, pyBigWig 0.3.25, matplotlib 3.11.1). Every item below was reproduced by
execution with a synthetic script in this directory; the three kitted ones have a fix branch
in the local clone, a `git am`-able patch here, a test that fails on `4db9d816`, and passing
`cargo test` / pytest runs (`test-runs.txt`). **Nothing has been committed to this
repository's history, pushed, filed or posted.** The tracker was searched on 2026-09-05
(four `search_issues` queries, one per item); the nearest prior issues are listed per item._

These four were first seen while re-verifying the ten 3.5.6 items on 4.0.0
([`../README.md`](../README.md), "New on 4.0.0"); items 1 and 2 change numbers under the
default or an offered option and rank above the held 3.5.6 items (DT3/DT9) in filing order.

| # | item | call | evidence (before → after) | patch / branch | nearest prior issue |
|---|---|---|---|---|---|
| 1 | `bamCompare --operation first\|second\|add\|mean` write the **log2** track; `reciprocal_ratio` inverted | **defect** (offered options, wrong numbers) | `mcve_bamcompare_operations.py`, `.before.out` (5 of 8 operations wrong), `.after.out` (0); `../../verify/note_v4_bamcompare_operations.v4.0.0.out` | `0001-bamCompare-operations.patch`, `fix4/bamcompare-operations` (`37ff4a55`), Rust `src/calc.rs` + cargo tests + pytest | none (0 hits for bamCompare operations on the Rust backend) |
| 2 | plotPCA default table/plot hold **per-bin PC scores (`U*S` rows)**, not the per-sample loadings | **defect** (default mode of the tool 19 cohort papers used; `--transpose` right) | `mcve_plotpca_loadings.py`, `.before.out` (rows = `(U*S)[i,:]`, norms 1.5–1.9, no row separates the planted groups), `.after.out` (rows = `V^T`, norms 1, PC1 separates them); `../../verify/dt2b_plotpca_table_v4.v4.0.0.out` | `0002-plotPCA-loadings.patch`, `fix4/plotpca-loadings` (`1c44afdd`), Python `correlation.py` + tests + regenerated golden PNG/TSV | #1215 (multiBamSummary + plotPCA normalisation; unrelated) |
| 3 | bamCoverage / bamCompare / multiBamSummary round every value to **two decimals** | **defect in effect, fix is a design decision** — note only, no patch (below) | `note_output_rounding.py`, `note_output_rounding.4.0.0.out` | none | none (0 hits) |
| 4 | `computeMatrixOperations sort` cannot sort a single-BED Rust-`computeMatrix` matrix unless the BED is `genes.bed` | **defect** (tool cannot consume the other tool's default output), small fix | `mcve_computematrixoperations_sort_group.py`, `.before.out` (exit 1, "missing the 'genes' region group"), `.after.out` (sorted) | `0003-computeMatrixOperations-sort-group.patch`, `fix4/computematrixoperations-sort-group` (`8fb70660`), Python `computeMatrixOperations.py` + pytest | none directly (#1037 dataRange features, #1200 computeMatrix IndexError; #1423 is the gzipped-BED crash in the same function, kitted in `../../issue-fixes/1423-gzipped-bed-sortmatrix/v4.0.0/`) |

## 1. `bamCompare --operation` (Rust, `src/calc.rs:111-169`)

`calc_ratio` matches `log2`, `ratio`, `reciprocal_ratio`, `subtract` and a catch-all `_`
that computes log2; `bamCompare2.py:118` still offers all eight choices, so `first`,
`second`, `add` and `mean` write the log2 track (with pseudocount). The `reciprocal_ratio`
arm (`:137-148`) returns b/a for a/b ≥ 1 and −a/b otherwise — the inverse of the documented
and 3.5.x rule a/b if a/b ≥ 1 else −b/a (3/2 → 0.67 instead of 1.5; 2/3 → −0.33 instead
of −3). Fix: four explicit arms (scaled signals, no pseudocount, as 3.5.x and the
`--pseudocount` help), the two reciprocal branches swapped, catch-all → `panic!`. The
existing `test_calc_ratio` pinned the inverted value (−0.27 for 6/22) and is corrected to
−3.67; two cargo tests and one pytest (all five operations on `testA`/`testB`) added.
Caveat flagged in the issue, not changed: the `subtract` arm adds both pseudocounts before
subtracting (invisible at the default `--pseudocount 1`, a shift of p1 − p2 otherwise).

## 2. plotPCA loadings (Python, `pydeeptools/deeptools/correlation.py:507-520`)

`plot_pca` sets `Wt = U * S` for both layouts — the PC scores of the *rows* (selected
bins) — and `plotPCA.py:222` writes row `i` of it as "Component i" under the sample names,
while `:543` scatters `Wt[PC1-1, :]` against `Wt[PC2-1, :]`. In the default layout the
documented quantity ("the loadings for each sample in each principal component") is `Vt`,
which 3.5.6 wrote. Fix: `Wt = Vt` untransposed, `(U * S).T` transposed (unchanged), and
the "not enough principal components to plot N samples" exit removed (each component row
has one loading per sample). The existing image tests could not catch this: the corrected
plots are 6.8/5.7 RMS from the goldens at a tolerance of 50; the golden PNGs/TSVs are
regenerated in the patch. The numeric tests had avoided the coordinates as "not
reproducible across platforms" — true of bin scores (BLAS-dependent bin selection), not of
the PC1 loadings, which the new test pins against a numpy SVD.

## 3. Two-decimal rounding of every output value — note, no patch

`src/bamcoverage.rs:274-282`, every arm of `calc_ratio` (`src/calc.rs`) and
`src/multibamsummary.rs:307` write `round(x·100)/100` in f32. The rounding is absolute,
not relative, so it is invisible for raw counts and RPGC-scale values but not for CPM at
depth or for log2 ratios: with one 50-bp read per bin, `--scaleFactor 0.034` (the CPM
factor at ~29 M mapped reads) is written as 0.03 (12 % low), 0.012 as 0.01 (17 %), 0.004
(250 M reads) and 0.001 as 0 (100 %); a log2 ratio of 1.03-fold, 0.04264, becomes 0.04;
`bamCoverage_old` writes 0.034 / 0.0426443 (`note_output_rounding.4.0.0.out`). At 10-bp
bins and 30 M reads every single-read bin carries a 10 % error, and low-coverage tracks of
deep libraries lose their single-read bins altogether. `CHANGES.txt` announces only "large
scale values precision slightly altered with new backend (f32 vs f64)", which is the f32
storage bigtools uses anyway, not this. **Call:** the numbers are wrong in a way users will
not expect, but the remedy is a design choice for the maintainers — drop the rounding (the
bigWig stores f32 regardless), round to significant digits (3.5.x wrote 6–7), or make it an
option — and the existing pytest expectations pin the two-decimal values (`-0.58`, `0.67`,
`-1.87`, `0.27`, …), so any change is not a small patch. Filed as a note with the measured
table; suggested text in the issue order below.

## 4. `computeMatrixOperations sort` and the single group label (Python, `computeMatrixOperations.py:698-700`)

The Rust `computeMatrix` names a BED's group by the file stem
(`src/computematrix.rs:152-160`); `sortMatrix` still assumes `genes` for a single sort
file (what the Python `computeMatrix` wrote) and exits at its sanity check. **Call:**
defect — a shipped tool cannot consume the other's default output — and the file-stem
label is the more useful one on plots (`CHANGES.txt`: "plot labels now show sample names
only per default"), so the Python side adapts: when the matrix has exactly one group, use
its label as the default group (five lines; `genes` fallback kept for `computeMatrix_old`
matrices). The test builds a matrix with the Rust `computeMatrix` from the shipped
`input_computeMatrix_regions1.bed` and sorts it with a reversed copy under another name.

## Contents

| file | what |
|---|---|
| `issue-bamcompare-operations.md`, `issue-plotpca-loadings.md`, `issue-computematrixoperations-sort-group.md` | issue texts (Title line first, the four-item issue checklist, MCVE, output, cause with `file:line`, fix) |
| `pr-body.md` | PR titles and bodies (Title line, `Fixes #NNN.`, the four PR checkboxes) for patches 0001–0003 |
| `0001-bamCompare-operations.patch`, `0002-plotPCA-loadings.patch`, `0003-computeMatrixOperations-sort-group.patch` | one commit each on `4db9d816`, each `git am`-able alone on a clean tree (0002 carries the two regenerated PNGs as binary hunks); stacked, they conflict only in the `CHANGES.txt` bullet, like the patches of `../` |
| `mcve_*.py` + `.before.out` / `.after.out` | the reproductions embedded in the issues, run on the unmodified build and on the patched one |
| `note_output_rounding.py`, `note_output_rounding.4.0.0.out` | item 3's measurement |
| `test-runs.txt` | the before/after test numbers, flake8 deltas, `git am` check |

## Order of operations

1. Items 1 and 2 first (wrong numbers under default/offered settings on the branch being
   released): open the two issues, then PRs A and B from patches 0001/0002 with the issue
   numbers filled into `pr-body.md` and `Fixes #NNN.`. They rank above DT3/DT9 of
   [`../README.md`](../README.md).
2. Item 4 as issue + PR C (0003); mention that it shares `sortMatrix` with the #1423 PR.
3. Item 3 as a plain issue (no patch) after a maintainer signal, quoting the measured table
   and offering the three remedies.
4. The per-repository cap of the method (two filings until a maintainer responds) applies
   across this kit and [`../`](../).
