# MPL4 fact sheet: `hexbin(marginals=True)` without `C` draws every marginal bar as 1

_Fact sheet, not issue text. Matplotlib does not accept AI-generated issue or PR prose, and AI agents may
not post to the tracker (`doc/devel/contribute.rst` "Use of Generative AI", l. 186–226 on 44f2e00; PR
template: "in your own words (no AI please)"). The facts are for writing the issue and PR yourself.
`repro.py`, its output and `fix.patch` are material to check and attach._

## Affected

- `Axes.hexbin(x, y, marginals=True)` with `C=None` (the default call) and the default
  `reduce_C_function=np.mean`. `pyplot.hexbin` is affected the same way.
- The marginal bars `collection.hbar` and `collection.vbar` (`get_array()`) and their colours. The
  hexagon counts themselves are correct.
- Not affected: calls that pass `C` (the marginals are then the per-strip `reduce_C_function` of C,
  which the audit checks pass), and `C=None` with an explicit `reduce_C_function=np.sum` (the workaround).

## Versions affected (how known)

- main @ 44f2e00: by execution on the overlay env (`axes/_axes.py` cmp-identical to the clone):
  `repro.out`, and audit `verify/m3_hist_hexbin_counts.out` items 8–9.
- 3.11.2, 3.7.1, 3.5.2: by execution in the audit (`verify/m3_hist_hexbin_counts.v*.out`, same FAIL
  lines); 3.11.2 also by `repro.out`.
- Reported in 2017 (PR #9171) and 2020 (PR #18875); unchanged since (see Related threads).

## Reproducer

- `repro.py` (numpy + matplotlib, Agg, 17 lines): 600 standard-normal points (`default_rng(0)`),
  `gridsize=(6, 3)`, `extent=(-4, 4, -4, 4)`, `marginals=True`, no C. The expected values are the
  per-strip point counts from `np.histogram`. Output: `repro.out`, identical on venv-main and venv-rel.

## Observed vs expected (from `repro.out`)

| bars | observed | expected (points per strip) |
|---|---|---|
| hbar (6 x strips) | [1.0, 1.0, 1.0, 1.0, 1.0, 1.0] | [5, 44, 264, 234, 51, 2] |
| vbar (6 y strips) | [1.0, 1.0, 1.0, 1.0, 1.0, 1.0] | [2, 48, 262, 244, 42, 2] |

- Audit harness numbers (other data): hbar [1, 1, 1, 1, 1, 1] for column counts [21, 89, 196, 184, 90,
  20]; vbar likewise.
- Effect: every marginal bar has the same value, so the default colour mapping draws all bars in one
  colour and the marginals carry no information.

## Documented promise (verbatim, main @ 44f2e00)

- `lib/matplotlib/axes/_axes.py:5615–5618`: "marginals : bool, default: *False* / If marginals is *True*,
  plot the marginal density as colormapped rectangles along the bottom of the x-axis and left of the
  y-axis."
- `lib/matplotlib/axes/_axes.py:5554–5557`: "C : array-like, optional / If given, these values are
  accumulated in the bins. Otherwise, every point has a value of 1. Must be of the same length as *x*
  and *y*."
- `lib/matplotlib/axes/_axes.py:5544–5545`: "If *C* is *None*, the value of the hexagon is determined by
  the number of points in the hexagon."
- `lib/matplotlib/axes/_axes.py:5667–5669`: "reduce_C_function : callable, default: `numpy.mean` / The
  function to aggregate *C* within the bins. It is ignored if *C* is not given." In fact, with C absent
  it is still applied to the marginals (`np.mean` gives 1, `np.sum` gives counts).

## Code location and cause (main @ 44f2e00)

- `lib/matplotlib/axes/_axes.py:5770–5776`: the `C is None` branch counts the hexagons with `np.bincount`
  and then sets `C = np.ones(len(x))` (l. 5776).
- `lib/matplotlib/axes/_axes.py:5903–5909`: the marginal loop computes, per strip,
  `values[i] = reduce_C_function(ci) if len(ci) > 0 else np.nan` (l. 5909). The default
  `reduce_C_function=np.mean` (signature, l. 5539) gives the mean of ones, which is 1 in every non-empty
  strip.
- Blame: l. 5776 and 5909 are ee206a16bd (Antony Lee, 2021-09-13, a refactor). The marginals were
  rewritten in 7c800f96d (David Stansby, 2021-09-10, "Fix hexbin marginals", PR #21039), which kept the
  `C = np.ones` + `reduce_C_function` path.
- Tests: both existing tests that use marginals pass `reduce_C_function=np.sum` with C=None, which is the
  workaround. These are `test_hexbin_log` (`test_axes.py:1067–1082`, edited in 7c800f96d) and
  `test_hexbin_linear` (`test_axes.py:1104–1113`, 1d12b60546, 2022, issue #21165). So the default call
  path has no test.

## Proposed fix (`fix.patch`, against 44f2e00)

- In the `C is None` branch, after `C = np.ones(len(x))`, add `reduce_C_function = np.sum` with the
  comment "Every point has a value of 1, so the marginals count points." That is 2 added lines.
  - Each marginal bar becomes the number of points in its strip, which matches the C docstring ("every
    point has a value of 1") and the hexagon values (counts).
  - The override is consistent with "It is ignored if *C* is not given".
- The two existing marginal image tests (`test_hexbin_log`, `test_hexbin_linear`) already pass
  `np.sum`, so their output and baseline images do not change. Both pass in A and B.
- Test: `test_hexbin_marginals_count_without_C` in `lib/matplotlib/tests/test_axes.py`. It uses 500
  clipped normal points, `gridsize=(6, 3)` and `extent=(-4, 4, -4, 4)`, and compares hbar/vbar with
  `np.histogram` counts. It fails on unpatched main (hbar [1, 1, …] against [4, 40, 200, 206, …]) and
  passes with the patch.
- Test runs: `tests.txt`. test_axes: A 19 failed / 859 passed / 59 skipped; B 18 / 860 / 59. The only
  difference is the new test. Audit harness m3: 165/11 → 166/10. The hbar FAIL is gone; the vbar FAIL
  remains for the separate reason under "Side observations".
- Other option, which tacaswell named in 2017 (PR #9171): raise an error for `marginals=True` with
  C=None. Not implemented here.
- Overlay caveat: tested on 3.11.2 with main's `axes/_axes.py`, not on a build of main (SheenBidi
  download blocked).

## Related threads (from `../../prior-reports.md`, searched 2026-10-03)

- PR #9171 "BUG: Fix implementation of marginals in pyplot.hexbin" (adeak), closed unmerged on
  2018-01-09: https://github.com/matplotlib/matplotlib/pull/9171. Its description says the feature
  "gives a constant 1 density (interspersed with nans) when the `C` optional keyword is not passed".
  - tacaswell, 2017-09-24: "the current behavior is also broken and the proposed behavior is less
    wrong." He also proposed to "raise an error if marginals are asked for in the `C is None` case".
  - jklymak, 2018-01-09: "I'm closing as per @adeak's comment above."
- PR #18875 "Improvements and bugfixes for hexbin marginals" (MihaiBabiac), closed unmerged on
  2024-01-06: https://github.com/matplotlib/matplotlib/pull/18875. Item 5 of its description: with no C
  the code applies `np.mean` to ones, giving "binary values in the marginal".
  - dstansby, 2024-01-06: "Apart from the new error in the PR I opened, I think the rest of the issues
    were fixed (possibly by #21039?) at some point between this PR being opened and now, so I'll close
    this PR. Feel free to open new issues about the hexbin marginals if I've got that wrong!"
- PR #21039 "Fix `hexbin` marginals and log scaling" (dstansby), merged 2021-09-24:
  https://github.com/matplotlib/matplotlib/pull/21039. It did not change the C=None path, and its test
  uses the `np.sum` workaround.
- #21353 "[MNT]: Deprecate hexbin marginals?" (dstansby), closed 2021-12-21:
  https://github.com/matplotlib/matplotlib/issues/21353. It cites "lots of possible issues with the
  current implementation"; the marginals were not deprecated.
- Status: reported before and closed without a fix. The last maintainer closed it believing #21039 had
  fixed it, and invited a new issue.

## Side observations (found while writing the test; not fixed by `fix.patch`; not searched on the tracker)

- **vbar drops points at the minimum y.** `_axes.py:5903`, `bin_idxs = np.searchsorted(bin_edges, z) - 1`,
  puts a value equal to `bin_edges[0]` at index −1, so the loop never counts it. The x range is padded
  by `1e-9 * (xmax - xmin)` (l. 5748–5750); the y range is not, so every point with `y == min(y)` is
  left out of `vbar`. This happens with or without C.
  - Executed on main overlay and 3.11.2: 4 points, 2 of them at min y, `C=np.ones(4)`,
    `reduce_C_function=np.sum`, `gridsize=2` → hbar [2.0, 2.0], vbar [2.0] (2 of 4 points).
  - Audit m3 after the fix: vbar [2, 27, …] against y counts [3, 27, …].
  - The new regression test passes an explicit `extent` so that it does not depend on this.
- **`on_changed` callback typo.** `_axes.py:5927–5931` calls `hbar.set_cmap` twice and `vbar.set_clim`
  twice (ee206a16bd, 2021-09). So after `hb.set_cmap('magma'); hb.set_clim(0, 50)` the hbar has magma
  with clim (None, None), and the vbar keeps viridis with clim (0.0, 50.0) (executed on the main
  overlay).

## Issue template (`.github/ISSUE_TEMPLATE/bug_report.yml` on 44f2e00) and the facts for each field

| field (required?) | fact that fills it |
|---|---|
| title (prefilled `[Bug]: `) | yours |
| Bug summary (required) | `hexbin(..., marginals=True)` without C: every hbar/vbar value is 1.0 (mean of ones), so the marginals show no density |
| Code for reproduction (required) | `repro.py` (the template's AI-guidance link anchor `#restrictions-on-generative-ai-usage` does not exist in `contribute.rst` on 44f2e00) |
| Actual outcome (required) | the "observed" rows / `repro.out` |
| Expected outcome (required) | the per-strip counts, from the marginals docstring ("marginal density") and the C docstring ("every point has a value of 1"); quotes above |
| Additional information: conditions | C=None with the default `reduce_C_function`; passing `reduce_C_function=np.sum` gives counts |
| Additional information: earlier versions | 3.5.2, 3.7.1, 3.11.2, main; reported in #9171 (2017) and #18875 (2020); #18875 closed 2024-01-06 assuming #21039 fixed it |
| Additional information: why | `_axes.py:5776` `C = np.ones(len(x))` + `_axes.py:5909` `reduce_C_function(ci)` with default `np.mean` |
| Additional information: fix | `reduce_C_function = np.sum` in the C=None branch (`fix.patch`), or tacaswell's 2017 alternative of an error |
| Operating system | Ubuntu 24.04.4 LTS (Linux 6.18 container) |
| Matplotlib Version (required) | 3.11.2 (and main @ 44f2e00 as an overlay on 3.11.2) |
| Matplotlib Backend | agg |
| Python version | 3.12.3 |
| Jupyter version | not used |
| Installation | pip (wheel, installed with uv pip) |

## PR facts (template: "PR summary", "AI Disclosure", quality checks)

- Closes: the new issue. Reference #9171, #18875 (dstansby's invitation) and #21039.
- Change: 2 added lines in `Axes.hexbin` plus one test. No baseline image changes, because the existing
  marginal image tests already used `np.sum`.
- Quality checks: tested (new test fails before, passes after); example N/A. Release note: for you or
  the reviewers to decide. The default marginals change from constant to counts.
- Whether to include the two side observations: your call. They are separate defects in the same
  block. Every dataset has at least one point at min(y), so on a linear y scale with no `extent` a
  vbar fix adds at least one point to the lowest vbar strip (on a log y scale the lower edge is
  `10**log10(min y)`, which can differ from min y by rounding; not checked). That includes `test_hexbin_log` and
  `test_hexbin_linear`; whether their images change beyond tolerance was not checked.

## AI disclosure facts (for the "AI Disclosure" section, in your words)

- Finding: located by the audit harness `verify/m3_hist_hexbin_counts.py`, written with Claude Code
  (Anthropic). It compares the marginal bars with per-strip counts.
- Reproducer `repro.py`: written by Claude Code.
- Patch and test: written by Claude Code. The test runs in `tests.txt` were run by Claude Code against
  an overlay of main's `axes/_axes.py` on 3.11.2. The side observations were found and executed by
  Claude Code.
- This fact sheet: Claude Code. The issue and PR text: yours.
- Policy points that apply: understand and verify the AI output; "simultaneously contributing to
  several projects" is listed as unacceptable. The audit README limits filing to two Matplotlib findings
  at a time.

## Weak points

- Two earlier PRs on this were closed unmerged. In 2021, #21353 asked whether to deprecate the marginals
  altogether, so maintainers may prefer an error or a deprecation to a fix.
- Marginal counts per strip are much larger than per-hexagon counts. If the user passes a shared `norm`
  instance, hexagons and bars share its limits. The same is true today when C is given with `np.sum`.
