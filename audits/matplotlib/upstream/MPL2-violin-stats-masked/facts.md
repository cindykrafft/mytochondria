# MPL2 fact sheet: `violin_stats` / `violinplot` keep masked values despite the 3.11 note and docstrings

_Fact sheet, not issue text. Matplotlib does not accept AI-generated issue or PR prose, and AI agents may
not post to the tracker (`doc/devel/contribute.rst` "Use of Generative AI", l. 186–226 on 44f2e00; PR
template: "in your own words (no AI please)"). The facts are for writing the issue and PR yourself.
`repro.py`, its output and `fix.patch` are material to check and attach._

## Affected

- `matplotlib.cbook.violin_stats` with `numpy.ma.MaskedArray` input: a 1-D masked array, a list of
  masked arrays, or a 2-D masked array.
- `Axes.violinplot` (and `pyplot.violinplot`): calls `cbook.violin_stats` (`_axes.py:9111`), so the drawn
  body, the min/max/mean/median lines and the quantile lines include the masked values.
- Not affected: NaN and ±inf, which are dropped as documented (audit m1 "held up").

## Versions affected (how known)

- main @ 44f2e00: by execution on the overlay env (`cbook.py` cmp-identical to the clone): `repro.out`,
  and audit `verify/m1_boxplot_violin_stats.out`, 6 FAIL lines.
- 3.11.2: by execution (`repro.out`, `verify/m1_boxplot_violin_stats.v3.11.2.out`).
- 3.11.0, 3.11.1: by source. `git show v3.11.0:lib/matplotlib/cbook.py` and `v3.11.1` contain the same
  `x = np.asarray(x)` before `delete_masked_points(x)` in `violin_stats`. Not run.
- 3.10 and earlier: no masked handling was documented. On 3.7.1 and 3.5.2 (audit info lines) a masked
  array reached `np.min`/`np.max`/`np.mean`, which respect the mask, but the median, quantiles and KDE
  were wrong (numpy warned "'partition' will ignore the 'mask'"). The 3.11 change turned correct
  min/max lines into wrong ones for masked input.

## Reproducer

- `repro.py` (numpy + matplotlib, Agg, 20 lines): 40 normal values (`default_rng(0)`) plus 50.0, −50.0
  and 3.3, all three masked. Output: `repro.out`, identical on venv-main and venv-rel.

## Observed vs expected (from `repro.out`; expected = `violin_stats` of the 40 unmasked values)

| statistic | observed | expected |
|---|---|---|
| min | −50.0 | −2.3250307746388343 |
| max | 50.0 | 1.4934311452207607 |
| mean | 0.02051693086787936 | −0.06044429931702975 |
| median | −0.12853466294403426 | −0.12907414831840186 |
| quantiles (0.25, 0.75) | [−0.63855154, 0.47623806] | [−0.630913, 0.37410393] |
| `Axes.violinplot` max line y | 50.0 | 1.4934311452207607 |

- Audit harness numbers (other data, `component-reviews/boxplot-violin-stats.md`): min/max −50/50 for
  −2.862/1.527; mean −0.1167 for −0.2079; quantiles [−0.9021, 0.5390] for [−0.9008, 0.4050]. The KDE
  `vals` differ from the clean KDE by a maximum relative difference of 1.00, and the KDE grid spans
  −50 to 50. With a list of masked arrays, the second violin has max 99 where the masked 99 should be
  excluded.

## Documented promise (verbatim, main @ 44f2e00)

- `lib/matplotlib/cbook.py:1500–1502` (`violin_stats`, parameter *X*): "X : 1D array or sequence of 1D
  arrays or 2D array / Sample data that will be used to produce the gaussian kernel density estimates.
  Non-finite and masked values are ignored."
- `lib/matplotlib/axes/_axes.py:9001–9008` (`violinplot`, parameter *dataset*): "dataset : 1D array or
  sequence of 1D arrays or 2D array / The input data. …  Non-finite and masked values are ignored."
  (the quoted sentence is l. 9008).
- `doc/api/prev_api_changes/api_changes_3.11.0/behavior.rst:108–112`: heading "Axes.violinplot and
  cbook.violin_stats ignore non-finite values", text "`~matplotlib.axes.Axes.violinplot` and
  `matplotlib.cbook.violin_stats` now ignore masked and non-finite (NaN and inf) values."
- The same note is still in `doc/api/next_api_changes/behavior/violinplot_empty.rst:1–4` on 44f2e00,
  although it was already published in the 3.11.0 notes.

## Code location and cause (main @ 44f2e00)

- `lib/matplotlib/cbook.py:1591`: `x = np.asarray(x)`. This converts a `MaskedArray` to a plain ndarray
  of its data, and the mask is lost.
- `lib/matplotlib/cbook.py:1592`: `x, = delete_masked_points(x)`. This function reads masks only from
  `MaskedArray` arguments (`cbook.py:1014–1027`). After l. 1591 it sees none and removes only non-finite
  values.
- The mask does reach l. 1591: `_reshape_2D` (`cbook.py:1425–1482`) keeps ndarray subclasses (2-D:
  `X.transpose()` and `np.reshape`; lists: `np.asanyarray`).
- Origin: both lines and the release note come from commit 5c55704c1 (2026-05-28, "Fix violinplot crash
  on empty datasets (#31700) (#31707)"). It was backported as 22d11871d (PR #31774, auto-backport to
  v3.11.x) and released in v3.11.0 (69c7534c7, 2026-06-11).
- The test added in that PR (`test_violinplot_empty_dataset`, `test_axes.py:10498`) covers empty and
  all-NaN datasets only. On 44f2e00 no test calls `violin_stats` directly, and no test passes a masked
  array to `violinplot`.

## Proposed fix (`fix.patch`, against 44f2e00)

- `cbook.py:1591`: `x = np.asanyarray(x)` (keeps the mask for `delete_masked_points`). One line.
- Test: `test_violin_stats_ignores_masked` in `lib/matplotlib/tests/test_cbook.py`, parametrised over 1-D,
  list and 2-D masked input. It compares every returned statistic (min, max, mean, median, coords, vals,
  quantiles) with `violin_stats` of the unmasked values. It fails on unpatched main (3/3) and passes with
  the patch.
- Test runs: `tests.txt`. test_cbook + test_axes: A 22 failed / 969 passed / 64 skipped; B 19 / 972 / 64.
  The only difference is the 3 new cases, and all violinplot tests pass in both runs. Audit harness m1:
  164/12 → 170/6, and all six MPL2 FAIL lines are gone.
- Overlay caveat: tested on 3.11.2 with main's `cbook.py`, not on a build of main (SheenBidi download
  blocked).
- Alternative the reviewers may prefer: drop the conversion (`delete_masked_points` accepts lists and
  arrays itself). Not tested here.

## Related threads (from `../../prior-reports.md`, searched 2026-10-03)

- No prior report of the masked-array failure found.
- PR #31707 "Fix violinplot crash on empty datasets (#31700)", merged 2026-05-28:
  https://github.com/matplotlib/matplotlib/pull/31707. Origin of both the claim and the line. In the
  rendered conversation, no reviewer mentions masked arrays.
- PR #32428 "DOC: Improve violin/violin_stats/violinplot docs" (timhoffm), open since 2026-10-02:
  https://github.com/matplotlib/matplotlib/pull/32428. **Correction 2026-10-04 (PR #32428 read in full, transcript https://claude.ai/artifact/XNouacZdAvDV4YcbDgqZuv):** the PR does not repeat the masked-values claim. It changes only `axes/_axes.py`, adding "Notes" sections that relate `violinplot`, `violin_stats` and `violin` (Closes #32409, KDE weights). It does not touch `cbook.py` or any line about masked or non-finite values. The existing sentences (`cbook.py:1502`, `_axes.py:9008`) are unchanged context. Nobody in the thread mentions masked arrays. Open, author timhoffm (MEMBER), one review by story645 (MEMBER) with two suggestions. (The earlier summary below, that it edits these docstrings, was wrong.) Earlier note: per the prior-report
  search, repeats the "masked values are ignored" claim. A fix or an issue should mention it. The patch
  touches only code line 1591, not the docstrings, but check for a merge conflict once #32428 lands.
- PR #13651 "Box plot and violin plot now ignore masked points", open (draft, orphaned) since
  2019-03-11: https://github.com/matplotlib/matplotlib/pull/13651. An earlier attempt at masked
  handling in `_reshape_2D`, which efiring objected to.
- #13533 "Boxplotting Masked Arrays", closed via PR #27605 (box plot only, 3.9):
  https://github.com/matplotlib/matplotlib/issues/13533. Box plots ignore masks since 3.9, so violins
  doing the same is consistent.
- #30355 "[Bug]: violinplot with nan values fails silently", open:
  https://github.com/matplotlib/matplotlib/issues/30355 (NaN only; looks stale since #31707).
- PR #30932 "Warn and ignore NaN values in violinplot", open:
  https://github.com/matplotlib/matplotlib/pull/30932 (NaN only). The prior-report search paraphrases
  timhoffm there: silently dropping NaNs "is the way to go". That quote is not verbatim.

## Issue template (`.github/ISSUE_TEMPLATE/bug_report.yml` on 44f2e00) and the facts for each field

| field (required?) | fact that fills it |
|---|---|
| title (prefilled `[Bug]: `) | yours |
| Bug summary (required) | masked entries of a MaskedArray are used by `violin_stats`/`violinplot` (min/max/mean/median/quantiles/KDE), against the 3.11 note and both docstrings |
| Code for reproduction (required) | `repro.py` (the template's AI-guidance link anchor `#restrictions-on-generative-ai-usage` does not exist in `contribute.rst` on 44f2e00) |
| Actual outcome (required) | "observed" column / `repro.out` |
| Expected outcome (required) | "expected" column: the statistics of the unmasked values; quotes from cbook.py:1502, _axes.py:9008, behavior.rst:111–112 |
| Additional information: conditions | any MaskedArray input (1-D, list of, 2-D); NaN/inf are fine |
| Additional information: earlier versions | 3.11.0–3.11.2 and main (source + execution); ≤3.10 promised nothing, and its min/max/mean were right while its median/quantiles/KDE were wrong |
| Additional information: why | cbook.py:1591 `np.asarray` drops the mask before `delete_masked_points` (1592); introduced in #31707 |
| Additional information: fix | `np.asanyarray` (`fix.patch`); mention #32428 |
| Operating system | Ubuntu 24.04.4 LTS (Linux 6.18 container) |
| Matplotlib Version (required) | 3.11.2 (and main @ 44f2e00 as an overlay on 3.11.2) |
| Matplotlib Backend | agg |
| Python version | 3.12.3 |
| Jupyter version | not used |
| Installation | pip (wheel, installed with uv pip) |

## PR facts (template: "PR summary", "AI Disclosure", quality checks)

- Closes: the issue number once opened. Mention #31707 (origin) and #32428 (open doc PR on the same
  functions).
- Change: one line in `cbook.violin_stats` plus one parametrised test. No image baseline changes.
- Quality checks: tested (new test fails before, passes after); example N/A. Release note: the 3.11.0
  note already promises this behaviour, so the fix brings the code in line with it.

## AI disclosure facts (for the "AI Disclosure" section, in your words)

- Finding: located by the audit harness `verify/m1_boxplot_violin_stats.py`, written with Claude Code
  (Anthropic). It compares `violin_stats` on masked input with the statistics of the unmasked values.
- Reproducer `repro.py`: written by Claude Code.
- Patch and test: written by Claude Code. The test runs in `tests.txt` were run by Claude Code against
  an overlay of main's `cbook.py` on 3.11.2.
- This fact sheet: Claude Code. The issue and PR text: yours.
- Policy points that apply: understand and verify the AI output before submitting; the policy also
  lists "simultaneously contributing to several projects" as an unacceptable use. The audit README
  limits filing to two Matplotlib findings at a time.

## Weak points

- The fix is trivial and the bug is recent. A maintainer may fold it into #32428, or into the open NaN
  threads, instead of taking a separate PR.
- Masked input to `violinplot` is probably uncommon (the cohort profile counts violin/KDE use in 10
  papers, not masked input).
