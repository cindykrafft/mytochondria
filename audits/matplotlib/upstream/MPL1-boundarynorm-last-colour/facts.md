# MPL1 fact sheet: `BoundaryNorm` with more colours than bins never reaches the last colour

_Fact sheet, not issue text. Matplotlib does not accept AI-generated issue or PR prose, and AI agents may
not post to the tracker (`doc/devel/contribute.rst` "Use of Generative AI", l. 186–226 on 44f2e00; PR
template: "Describe what issue is resolved and why you chose this solution in your own words (no AI
please)"). The facts are for writing the issue and PR yourself. `repro.py`, its output and `fix.patch` are
material to check and attach, not text to paste._

## Affected

- `matplotlib.colors.BoundaryNorm.__call__`, when `ncolors > number of regions` (regions = bins plus one
  for each `extend` side). Through it: every artist drawn with a `BoundaryNorm` (`imshow`, `pcolormesh`,
  `scatter`, `contourf` with a norm) and the colorbar bands, which use the same norm.
- Not affected: `ncolors == regions` (no stretch), the single-region case (own branch,
  `colors.py:3311–3313`), and values `>= boundaries[-1]` (set to `max_col` afterwards, l. 3321).

## Versions affected (how known)

- main @ 44f2e00: by execution on the overlay env (`colors.py` is cmp-identical to the clone):
  `repro.out`, and audit harness `verify/m4_color_mapping.out` FAIL 6–7.
- 3.11.2 release: by execution (`repro.out`, `verify/m4_color_mapping.v3.11.2.out`).
- 3.7.1 and 3.5.2: by execution in the audit (`verify/m4_color_mapping.v3.7.1.out`, `.v3.5.2.out`, same
  FAIL lines).
- Source: the line `iret = (self.Ncmap - 1) / (self._n_regions - 1) * iret` is in v3.5.2, v3.7.1 and
  v3.11.2 (`git show <tag>:lib/matplotlib/colors.py`). Before a5f531791 (2020) the same float product
  was written `(iret * scalefac).astype(np.int16)` with `scalefac = (self.Ncmap - 1) / divsor`, so the
  truncation is older than that commit. Not traced further back.

## Reproducer

- `repro.py` (numpy + matplotlib, Agg, 20 lines). Output on both builds: `repro.out` (identical on
  venv-main and venv-rel).

## Observed vs expected (from `repro.out`)

| case | observed indices | expected indices (docstring's linear map, floor) |
|---|---|---|
| 12 bins, 16 colours | `[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]` | `[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 15]` |
| 26 bins, 256 colours | `[…, 234, 244, 254]` | `[…, 234, 244, 255]` |

- Drawn colour of the top bin (viridis resampled to 16): RGBA `[0.8249, 0.8847, 0.1062, 1.0]`; the last
  colour is `[0.9932, 0.9062, 0.1439, 1.0]`. With 256 colours: `[0.9839, 0.9049, 0.1369, 1.0]` against
  `[0.9932, 0.9062, 0.1439, 1.0]`.
- Arithmetic: `15 / 11 * 11 = 14.999999999999998`, truncated to 14 by `astype(np.int16)`. The exact
  value is the integer 15, so any rounding rule gives 15.
- Extent (audit grid 2 ≤ ncolors < 200, 2 ≤ bins < 60, bins < ncolors; 9773 pairs): 266 pairs have at
  least one bin one index low, 233 of them in the last bin. Other pairs: (27, 24) → 25 for 26;
  (30, 26) → 28 for 29.
- With `ncolors=256` (the usual `cmap.N`), 32 of the region counts 2–255 miss colour 255: 26, 30, 51, 54,
  59, 92, 94, 101, 104, 106, 107, 117, 118, 122, 183, 186, 187, 188, 192, 201, 204, 207, 208, 211, 213,
  218, 222, 233, 234, 235, 236, 243.
- Gallery example hit by it: `galleries/examples/color/colorbar_histogram.py` uses
  `bins = 30` and `BoundaryNorm(bin_edges, cmap.N)` with `RdYlBu_r` (N = 256). Run on 3.11.2 + overlay:
  of the 970 cells in the top bin, 969 get index 254. The one cell equal to `Z.max()` gets 256 ("over"),
  which `RdYlBu_r` draws in its last colour 255. So the top bin shows two colours.
- Colorbar: drawn from the same norm, so it shows the same wrong colour. Plot and colorbar agree with
  each other but not with the docstring (audit `component-reviews/color-mapping.md`, MPL1).

## Documented promise (verbatim, main @ 44f2e00)

- `lib/matplotlib/colors.py:3254–3257` (`BoundaryNorm.__init__` Notes): "If there are fewer bins
  (including extensions) than colors, then the color index is chosen by linearly interpolating the
  ``[0, nbins - 1]`` range onto the ``[0, ncolors - 1]`` range, effectively skipping some colors in the
  middle of the colormap."
- `lib/matplotlib/colors.py:3305–3309` (code comment): "if we have more colors than regions, stretch the
  region index computed above to full range of the color bins.  This will make use of the full range
  (but skip some of the colors in the middle) such that the first region is mapped to the first color
  and the last region is mapped to the last color."

## Code location and cause (main @ 44f2e00)

- `lib/matplotlib/colors.py:3317`: `iret = (self.Ncmap - 1) / (self._n_regions - 1) * iret` (float
  product).
- `lib/matplotlib/colors.py:3319`: `iret = iret.astype(np.int16)` truncates toward zero. When the exact
  product is an integer and the float result is one ulp below it, the index drops by one. For the last
  region the exact product is always `ncolors - 1`.
- Blame: both lines are a5f531791 (Thomas A Caswell, 2020-07-04, "ENH: pick the middle color only 1
  region with BoundaryNorm", merged in PR #17830). It restructured an existing float product and kept
  the truncation.

## Proposed fix (`fix.patch`, against 44f2e00)

- `colors.py:3317`: `iret = (self.Ncmap - 1) * iret // (self._n_regions - 1)`. This is the floor of the
  exact linear map, computed in integers (`np.digitize` returns integers). It changes the result only
  where the float product fell just below an integer, so every existing `test_BoundaryNorm` expectation
  still holds.
- Not changed: the `int16` cast at 3319 (MPL18, `ncolors > 32767`) and NaN → "over" (MPL8). Both are
  separate audit findings.
- Test: `test_BoundaryNorm_interpolation_reaches_last_color` in `lib/matplotlib/tests/test_colors.py`,
  parametrised over (16, 12), (256, 26), (27, 24), (30, 26). It fails on unpatched main (4/4) and passes
  with the patch.
- Test runs: `tests.txt`. 7 modules: A 32 failed / 1553 passed / 145 skipped; B 28 / 1557 / 145. The
  only difference is the 4 new cases. The 28 failures in both runs come from the overlay (3.12 test
  files on 3.11.2 modules) and are listed there. Audit harness m4: 190/18 → 192/16, and the two MPL1
  FAIL lines are gone.
- Overlay caveat: tested on 3.11.2 with main's `colors.py`, not on a build of main (SheenBidi download
  blocked).

## Related threads (from `../../prior-reports.md`, searched 2026-10-03)

- No prior report of the truncation found (two issue phrasings; PR searches `BoundaryNorm` (38 hits)
  and `BoundaryNorm int16`).
- #21911 "[ENH]: BoundaryNorm should not need to know colormap length" (jklymak), open since
  2021-12-10: https://github.com/matplotlib/matplotlib/issues/21911. About the stretch itself; does not
  mention truncation.
- #31195 "[ENH]: Design considerations for discrete colormapping" (timhoffm), open since 2026-02-24:
  https://github.com/matplotlib/matplotlib/issues/31195. A redesign discussion that this could be
  linked to.
- PR #32196 "Clarify interval semantics in BoundaryNorm documentation", merged 2026-08-10:
  https://github.com/matplotlib/matplotlib/pull/32196. Different topic (right-open last bin).
- PR #1260 (2012), https://github.com/matplotlib/matplotlib/pull/1260, about casting with numpy 1.7rc
  (different). PR #17830, https://github.com/matplotlib/matplotlib/pull/17830, last touched the lines.

## Issue template (`.github/ISSUE_TEMPLATE/bug_report.yml` on 44f2e00) and the facts for each field

| field (required?) | fact that fills it |
|---|---|
| title (prefilled `[Bug]: `) | yours |
| Bug summary (required, "1-2 short sentences") | BoundaryNorm with ncolors > regions: the last region gets `ncolors - 2` (e.g. 12 bins / 16 colours → 14, 26 / 256 → 254), against the Notes' linear map and the code comment "the last region is mapped to the last color" |
| Code for reproduction (required) | `repro.py`; the template asks AI-assisted reporters to read the generative-AI section (its link anchor `#restrictions-on-generative-ai-usage` does not exist in `contribute.rst` on 44f2e00; the section is "Use of Generative AI") |
| Actual outcome (required) | the `observed` lines and RGBA from `repro.out` |
| Expected outcome (required) | the `expected` lines: last index `ncolors - 1`; colours.py:3254–3257 and 3305–3309 quotes |
| Additional information: conditions | ncolors > regions and `(ncolors-1)/(regions-1)*(regions-1)` rounds below `ncolors-1` in float; 32 of 254 region counts for N=256; gallery `colorbar_histogram.py` (30 bins) |
| Additional information: earlier versions | same on 3.5.2, 3.7.1, 3.11.2, main; float-truncation form predates 2020 |
| Additional information: why | colors.py:3317 float product + 3319 truncating `astype(np.int16)` |
| Additional information: fix | integer floor `(Ncmap - 1) * iret // (n_regions - 1)` (`fix.patch`) |
| Operating system | Ubuntu 24.04.4 LTS (Linux 6.18 container) |
| Matplotlib Version (required) | 3.11.2 (and main @ 44f2e00 as an overlay on 3.11.2) |
| Matplotlib Backend | agg |
| Python version | 3.12.3 |
| Jupyter version | not used |
| Installation | pip (wheel, installed with uv pip) |

## PR facts (template `.github/PULL_REQUEST_TEMPLATE.md`: "PR summary", "AI Disclosure", quality checks)

- Closes: the issue number once you have opened it.
- Change: one line in `BoundaryNorm.__call__` (float product → integer floor) plus one parametrised
  test. No API change and no image baseline changes in the modules run.
- Quality checks: tested (new test, fails before, passes after); example N/A; release note: for you or
  the reviewers to decide (colours change only where the old index was one low).

## AI disclosure facts (for the "AI Disclosure" section, in your words)

- Finding: located by an audit harness (`verify/m4_color_mapping.py`) written with Claude Code
  (Anthropic). The harness compares `BoundaryNorm` against an exact recomputation of the docstring's
  linear map.
- Reproducer: `repro.py` written by Claude Code.
- Patch and test: the one-line change and `test_BoundaryNorm_interpolation_reaches_last_color` written
  by Claude Code. The test runs in `tests.txt` were also run by Claude Code, against an overlay of main's
  `colors.py` on 3.11.2 (not a source build).
- This fact sheet: Claude Code. The issue and PR text: yours.
- Policy points that apply (`contribute.rst` "Use of Generative AI"). Unacceptable: "Using AI output
  without ensuring that you fully understand the output or without verifying that it is the correct
  approach". Also unacceptable: "Increasing breadth of contributions, i.e. simultaneously contributing
  to several projects". The audit README also limits filing to two Matplotlib findings at a time.

## Weak points

- With 256-colour maps the wrong colour is the neighbouring entry: for viridis, RGBA
  `[0.9839, 0.9049, 0.1369]` against `[0.9932, 0.9062, 0.1439]`. The visible case is a short
  `ListedColormap` (12 bins over 16 colours) or a qualitative map.
- Maintainers are discussing a redesign of discrete colour mapping (#21911, #31195). The fix may be
  pulled into that discussion rather than merged alone.
