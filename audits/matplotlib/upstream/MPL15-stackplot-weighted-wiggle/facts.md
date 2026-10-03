# MPL15 fact sheet: `stackplot(baseline='weighted_wiggle')` lays out the layers as if their order were reversed

_Fact sheet, not issue text. Matplotlib does not accept AI-generated issue or PR prose, and AI agents may
not post to the tracker (`doc/devel/contribute.rst` "Use of Generative AI", l. 186–226 on 44f2e00; PR
template: "in your own words (no AI please)"). The facts are for writing the issue and PR yourself.
`repro.py`, its output and `fix.patch` are material to check and attach. Derivation and full numbers:
`../../verify/m3_stackplot_wiggle.notes.md` (harness `../../verify/m3b_stackplot_wiggle.py`)._

## Affected

- `matplotlib.stackplot.stackplot` / `Axes.stackplot` / `pyplot.stackplot` with
  `baseline='weighted_wiggle'`. The baseline (`first_line`) is wrong, and so is the vertical position of
  every layer. Layer thicknesses are still drawn correctly.
- Not affected: `'zero'`, `'sym'`, `'wiggle'`. The unweighted `'wiggle'` is oriented for the drawn
  order (notes §7). So the two wiggle options currently use opposite layer orientations.
- Exactly right only where the reversal makes no difference: a single layer, a palindromic layer order,
  or all layers proportional to one profile (notes §4).

## Versions affected (how known)

- main @ 44f2e00 and 3.11.2: by execution (`repro.out`, both builds; harness `m3b`, 40 ok / 8 FAIL on
  both). `stackplot.py` in 3.11.2 is byte-identical to main.
- 3.7.1 and 3.5.2: by execution in the audit (`verify/m3_hist_hexbin_counts.v3.7.1.out`, `.v3.5.2.out`).
  These give the same baseline `[-2, -1.625, -2.375, -3.7639, -4.0972, -4.7222, -6]` and "equals the
  reversed-order minimiser: True".
- Source: `first_line = center - 0.5 * total` is in v1.3.0, v2.0.0, v3.5.2, v3.7.1, v3.11.2 and main
  (`git show <tag>:lib/matplotlib/stackplot.py`). So every release since 1.3.0 (2013) is affected.

## Reproducer

- `repro.py` (numpy + matplotlib, Agg, 22 lines). It reads the drawn baseline from the first
  `PolyCollection` and compares it with the Byron & Wattenberg per-step minimiser. It also computes the
  weighted wiggle Σ_k Σ_i f_i(x_k)·(Δ midline_i)² for both. Output: `repro.out`, identical on venv-main
  and venv-rel.

## Observed vs expected (from `repro.out`)

| layers (layer 0 = bottom) | observed baseline | expected baseline (minimiser) | weighted wiggle observed / expected |
|---|---|---|---|
| [1, 3], [1, 1] | [−1.0, −1.75] | [−1.0, −2.25] | 1.75 / 0.75 |
| [1,1,2,3,3,2,1], [1,2,3,5,4,2,2], [2,1,1,1,2,4,6] | [−2.0, −1.625, −2.375, −3.7639, −4.0972, −4.7222, −6.0] | [−2.0, −2.375, −3.625, −5.2361, −4.9028, −3.2778, −3.0] | 84.3542 / 13.8819 |

- In both cases the observed baseline is exactly the minimiser for the reversed layer order
  (`repro.out`: "observed == minimiser for the reversed layer order: True").
- Exact values (Fraction arithmetic, notes §2): 3×7 case matplotlib −2, −13/8, −19/8, −271/72, −295/72,
  −85/18, −6; minimiser −2, −19/8, −29/8, −377/72, −353/72, −59/18, −3. Maximum difference 3, for a
  maximum total thickness of 9.
- 400 random integer cases (notes §5): matplotlib equals the minimiser in 0 of 400. The ratio of its
  weighted wiggle to the minimum is 1.02 to 212, median 5.24. The worst baseline offset is 0.96 × the
  maximum total thickness.
- Not a discretisation artefact (notes §6). On smooth layers f₁ = 1 + 2x (bottom), f₂ = 1, matplotlib's
  g₀(1) − g₀(0) converges to −0.65343 (−1 + ln2/2, the reversed order), not to the paper's −1.34657
  (−1 − ln2/2).

## Documented promise (verbatim, main @ 44f2e00)

- `lib/matplotlib/stackplot.py:40`: "``'wiggle'``: Minimizes the sum of the squared slopes."
- `lib/matplotlib/stackplot.py:41–43`: "``'weighted_wiggle'``: Does the same but weights to account for
  size of each layer. It is also called 'Streamgraph'-layout. More details can be found at
  http://leebyron.com/streamgraph/."
- Reference behind the link: L. Byron and M. Wattenberg, "Stacked Graphs – Geometry & Aesthetics",
  IEEE TVCG 14(6), 2008, §5.1. It gives g₀′ = −(1/Σf_i) Σ_i (½f_i′ + Σ_{j<i} f_j′) f_i, with f₁ the
  bottom layer (the printed outer sum starts at i=0, a typo for i=1). The paper says this formula is
  equivalent to the Streamgraph algorithm.
- Byron's reference code (`StreamLayout.java`, github.com/leebyron/streamgraph_generator @ e7370a6)
  equals the paper's minimiser exactly in Fraction arithmetic once its y-down screen coordinates are
  mapped to y-up (notes §0).

## Code location and cause (main @ 44f2e00)

- `lib/matplotlib/stackplot.py:115–129` (the `weighted_wiggle` branch). Line 128 is
  `first_line = center - 0.5 * total`.
- `center` (l. 121–127) is Byron's `center` accumulation, which is in y-down screen coordinates. For y-up
  axes the bottom edge is `-center - 0.5 * total`. The port changed `+ 0.5 * totalSize` to
  `- 0.5 * total` but kept `+center`, flipping only one of the two signs (notes, Derivation).
- Two-layer closed form (notes §3): at a step, matplotlib − minimiser = (f₂·d₁ − f₁·d₂)/T. The two agree
  only when both layers change in proportion to their thickness.
- History:
  - l. 115, 116 and 128 come from 24f537f (Till Stensitzki, 2013-01-10, "[ENH] added baseline feature to
    stacked graph", PR #1517), a statement-by-statement translation of `StreamLayout.layout()`.
  - l. 121–127 come from 339ca4e (Damon McDougall, 2013-01-17, "Vectorise the loops"), which kept the
    semantics.
  - First tag: v1.3.0.

## Proposed fix (`fix.patch`, against 44f2e00)

- `stackplot.py:128`: `first_line = -center - 0.5 * total`, plus a two-line comment that `center`
  follows the y-down convention of Byron's code.
- Test: `test_stackplot_weighted_wiggle_baseline` in `lib/matplotlib/tests/test_axes.py`, after
  `test_stackplot_baseline`. It computes the minimiser from the formula and also asserts the
  hand-checkable values [−2, −19/8, −29/8, −377/72, −353/72, −59/18, −3]. It fails on unpatched main
  (6 of 7 values differ, max abs diff 3) and passes with the patch.
- **Existing image test that pins the old output:** `test_stackplot_baseline[png]` (`test_axes.py:3485–3508`,
  baseline `lib/matplotlib/tests/baseline_images/test_axes/stackplot_test_baseline.png`).
  - With the fix it fails with RMS 42.636.
  - The diff image shows changes only in the bottom-right panel (`baseline='weighted_wiggle'`); the
    'zero', 'sym' and 'wiggle' panels are unchanged.
  - The PR has to regenerate that png. It was not deleted or skipped here.
- Test runs: `tests.txt`. test_axes: A 19 failed / 859 passed / 59 skipped; B 19 / 859 / 59.
  - Only in A: the new test.
  - Only in B: `test_stackplot_baseline[png]`, as expected.
  - Failing in both: 18 overlay failures.
- Independent check: the installed baseline equals the minimiser in 0/393 random cases before the patch
  and 393/393 after. The smooth case converges to −1.346561 at n = 10001 (continuous −1.346574).
- Gallery: `galleries/examples/lines_bars_and_markers/stackplot_demo.py:74` uses `baseline='wiggle'`, and
  no gallery or tutorial file on 44f2e00 uses `'weighted_wiggle'`, so no gallery image changes.
- Overlay caveat: tested on 3.11.2 with main's `stackplot.py` (byte-identical to 3.11.2's), not on a
  build of main (SheenBidi download blocked).
- Not included: MPL14, integer layers truncating `1/total` to 0 at `stackplot.py:118`
  (`inv_total = np.zeros_like(total)` is integer for integer input; a1dbd55, 2016, since 2.0.0).
  - It is a separate bug in the same block.
  - The new test uses float layers, so it does not depend on MPL14.
  - Possible companion fix: give `inv_total` a float dtype, e.g. that of `stack`. Not tested here.

## Related threads (from `../../prior-reports.md`, searched 2026-10-03)

- No prior report found (issue queries "stackplot weighted_wiggle baseline wrong streamgraph",
  "stackplot weighted_wiggle int dtype"; PR query `stackplot wiggle`).
- PR #1517 "ENH: Add baseline feature to stackplot" (Tillsten, 2012–2013), origin:
  https://github.com/matplotlib/matplotlib/pull/1517. The page shows no discussion of the formula or of
  screen versus data orientation.
- #6313 "weighted_wiggle stackplot fails when all lines are zero at same x" (closed 2019) and PR #6358
  (2016): https://github.com/matplotlib/matplotlib/issues/6313,
  https://github.com/matplotlib/matplotlib/pull/6358. Different (division by zero); they added the
  `d[50, :] = 0` row in `test_stackplot_baseline`.
- #22393 "stackplot creates artifacts when height of input is zero" (closed as not planned):
  https://github.com/matplotlib/matplotlib/issues/22393. Different.

## Issue template (`.github/ISSUE_TEMPLATE/bug_report.yml` on 44f2e00) and the facts for each field

| field (required?) | fact that fills it |
|---|---|
| title (prefilled `[Bug]: `) | yours |
| Bug summary (required) | `weighted_wiggle` baseline is the Streamgraph minimiser for the layers in reverse order, while the layers are drawn in the given order; its weighted wiggle is larger than the minimum in every non-symmetric case |
| Code for reproduction (required) | `repro.py` (the template's AI-guidance link anchor `#restrictions-on-generative-ai-usage` does not exist in `contribute.rst` on 44f2e00) |
| Actual outcome (required) | "observed" rows / `repro.out` |
| Expected outcome (required) | "expected" rows: the B&W 2008 §5.1 minimiser with layer 0 at the bottom; stackplot.py:41–43 quote and the reference |
| Additional information: conditions | any non-symmetric input; exact only for one layer, palindromic order, or proportional layers |
| Additional information: earlier versions | every release since 1.3.0 (source); executed on 3.5.2, 3.7.1, 3.11.2, main |
| Additional information: why | stackplot.py:128 keeps Byron's y-down `+center` (port in 24f537f, 2013) |
| Additional information: fix | `-center - 0.5 * total` (`fix.patch`); regenerate `stackplot_test_baseline.png` |
| Operating system | Ubuntu 24.04.4 LTS (Linux 6.18 container) |
| Matplotlib Version (required) | 3.11.2 (and main @ 44f2e00 as an overlay on 3.11.2) |
| Matplotlib Backend | agg |
| Python version | 3.12.3 |
| Jupyter version | not used |
| Installation | pip (wheel, installed with uv pip) |

## PR facts (template: "PR summary", "AI Disclosure", quality checks)

- Closes: the new issue. Cite B&W 2008 §5.1 and Byron's `StreamLayout.java`.
- Change: one sign on `stackplot.py:128` plus a comment, one new test, and a regenerated
  `stackplot_test_baseline.png` (which the PR must include; not produced here).
- Quality checks: tested (new test fails before, passes after). Example N/A (the gallery uses 'wiggle').
  Release note: the output of every non-symmetric `weighted_wiggle` plot changes after 13 years.
  `doc/api/next_api_changes/behavior/` is where Matplotlib records behaviour changes (e.g.
  `violinplot_empty.rst`); whether this needs one is for you or the reviewers to decide.

## AI disclosure facts (for the "AI Disclosure" section, in your words)

- Finding: flagged by the audit harness `verify/m3_hist_hexbin_counts.py`. The follow-up harness
  `verify/m3b_stackplot_wiggle.py` checks it against the paper and Byron's reference code. Both were
  written with Claude Code (Anthropic), which also read the paper's equations from the rendered PDF
  pages and ported `StreamLayout.java` to Python.
- Reproducer `repro.py`: written by Claude Code.
- Patch and test: written by Claude Code. The test runs and the random-case check in `tests.txt` were
  run by Claude Code against an overlay on 3.11.2. The baseline image was not regenerated.
- This fact sheet: Claude Code. The issue and PR text: yours.
- Policy points that apply: understand and verify the AI output. The derivation in
  `m3_stackplot_wiggle.notes.md` is the part a reviewer will probe, so be ready to explain it yourself.
  "Simultaneously contributing to several projects" is listed as unacceptable, and the audit README
  limits filing to two Matplotlib findings at a time.

## Weak points

- The docstring's own promise is loose ("Does the same but weights to account for size of each
  layer"). The precise claim rests on the linked reference and on 'wiggle' being "the same" for the
  drawn order. A reviewer could call the current layout a valid but different weighting.
  - Counter-facts: it is worse than the minimiser in every non-symmetric case tested (400/400). It is
    exactly the reversed-order minimiser. 'wiggle' uses the drawn order.
- The change alters long-standing output (since 2013), and the reviewers may want a behaviour-change
  note and a regenerated baseline image.
- The visual difference is a different silhouette, not wrong layer thicknesses. On the
  `test_stackplot_baseline` data the fixed panel resembles 'sym' more than the old one did.
