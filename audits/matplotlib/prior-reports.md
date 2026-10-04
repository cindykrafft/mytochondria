# Matplotlib audit: prior reports on the matplotlib/matplotlib tracker

Searched 2026-10-03, against main @ 44f2e00. The findings come from `verify/m1_boxplot_violin_stats.notes.md`,
`verify/m2_spectral.notes.md`, `verify/m3_hist_hexbin_counts.notes.md` and `verify/m4_color_mapping.notes.md`. This
search was read-only: nothing was commented on, reacted to, opened or edited.

## Method and limits

- **Issue searches.** `search_issues` (GitHub MCP, semantic, scoped to matplotlib/matplotlib) was run with at least
  two phrasings per finding.
- **PR searches.** `search_pull_requests` was run with GitHub keyword syntax, usually on the function or variable name
  (`repo:matplotlib/matplotlib <name>`). That is the "code-search-style" query.
- **No `issue_read` / `pull_request_read`.** Both return "Access denied: repository matplotlib/matplotlib is not
  configured for this session", and `gh api` is refused for the same reason. Threads were therefore read through their
  public github.com pages (WebFetch), which has two consequences:
  - **PR conversation pages render in full.** All maintainer quotes below come from PR pages and are given verbatim,
    with author and date.
  - **Issue comment threads do not render.** Only the issue body is visible. Where an issue has comments that could
    not be read, the section says so. #24822 (5 comments), #26280 (1), #21382 and #7237 (4) are the ones that matter.
- **Local history.** The local clone of main (full history) was used for `git blame` / `git log` on the lines that
  cause each finding. This shows which PR introduced a line and whether a "fix" actually changed it.
- **Search limits.** Semantic issue search returns at most about 10 hits. Keyword PR search misses PRs whose titles do
  not contain the term. A finding marked "no prior report" means none was found with these queries, not that none
  exists.

The verdicts used are **no prior report**, **already reported (open)**, **already fixed** and **declined/intentional**.
Two findings need a qualifier: hexbin marginals was reported earlier and closed without a fix, and the hexbin
`get_offsets` finding was introduced by a fix.

---

## Present on main

### M1-1. `whis` text says "below"/"above", but the fences are inclusive (documentation)

- **Queries:**
  - issues: "boxplot whisker datum exactly on fence inclusive docstring highest datum below"
  - issues: "boxplot whisker ends at quartile not a data point"
  - issues: "boxplot whis percentiles whiskers not at percentile value"
  - PRs: `boxplot_stats whisker`
- **Nearest threads:**
  - #25134 "[Doc]: pyplot.boxplot whisker length wrong docs". Closed, 2023-02-02 → 2023-02-07.
    https://github.com/matplotlib/matplotlib/issues/25134. **Related.** It fixed the `Axes.boxplot` summary
    sentence (commit a0a6bdb04, PR #25135, "to the farthest data point lying within 1.5x the IQR"). That is the
    inclusive wording that passes in the audit. The `whis` parameter text in `cbook.boxplot_stats` and `Axes.boxplot`
    ("highest datum below", "lowest datum above") was not touched.
  - The inclusive comparisons `x[x <= hival]` / `x[x >= loval]` date to #2643 (2014). Their present form comes from
    d3cd57a20 (2019, a refactor).
- **Maintainer statement:** none on fence inclusivity.
- **Verdict: no prior report.** #25134/#25135 is a direct precedent for this kind of wording fix, and the new text
  should match the wording already in the summary.

### M1-2. Whiskers clamped to Q1/Q3, so a whisker end can be a non-datum (documentation)

- **Queries:**
  - issues: "boxplot whisker drawn inside box sparse data clamp q1 q3 whislo whishi"
  - issues: "boxplot whisker ends at quartile not a data point"
  - PRs: `boxplot_stats whisker`
- **Nearest threads:**
  - PR #16244 "Fix Boxplot Outlier and Whisker Calculation". Closed unmerged, 2020-01-16.
    https://github.com/matplotlib/matplotlib/pull/16244. **Related.** It proposed different whisker/outlier
    arithmetic and was withdrawn. The maintainer reply states the intended contract: a whisker end is a datum.
  - PR #2643 "ENH/REF: Overhauled boxplots". Merged 2014-01-24. **Origin.** The clamp
    (`if len(wiskhi) == 0 or np.max(wiskhi) < q3: stats['whishi'] = q3`) is commit da97eab4f (2014-01-18, "cleanup up
    typos and minor tweaks based on dev team input"). The PR conversation as rendered does not discuss the clamp.
- **Maintainer statement:** phobson (maintainer), PR #16244, 2020-01-16:
  > "At the moment, I don't agree with this change. My understanding, based on the last time I read Tukey's paper, is
  > that whiskers show the last points in the dataset within the high & low values. Your example produces a whisker
  > that does not have a corresponding value in the dataset."

  The clamp also produces whisker ends that have no corresponding value in the dataset. So the maintainer's stated
  rule supports the audit's reading, and the clamp is an undocumented exception to it.
- **Verdict: no prior report.**

### M1-3. `whis=(lo, hi)`: whiskers sit at the extreme datum inside the percentiles, not at the percentiles (documentation)

- **Queries:**
  - issues: "boxplot whis percentiles whiskers not at percentile value"
  - issues: "boxplot whisker ends at quartile not a data point"
  - PRs: `boxplot_stats whisker`
- **Nearest threads:** none specific. #25134 (above) is related wording work. #1455 "Boxplot: allow whiskers to always
  cover entire range" (closed 2014) is the origin of the percentile option and is different.
- **Verdict: no prior report.** It can be filed together with M1-1 and M1-2 as one docstring fix for the `whis`
  paragraph.

### M1-4. `+inf` next to a quartile gives Q3 = IQR = whishi = NaN and a spurious flier (bug; numpy root cause)

- **Queries:**
  - issues: "boxplot infinite values inf nan quartile percentile"
  - PRs: `boxplot inf`
  - numpy/numpy issues: "percentile with inf returns nan lerp weight zero"
- **Nearest threads:**
  - matplotlib: none. The hits (#30355 violin NaN, #20512, #19409) are different.
  - numpy #12282 "np.percentile returns different median from np.median when inf is present". **Open**, 2018-10-28.
    https://github.com/numpy/numpy/issues/12282. **Same root cause** (`np.percentile([inf, 5, 4], 50)` → nan, from
    the a + (b−a)·t interpolation).
- **Verdict: no prior report in matplotlib. The root cause is already reported (open) in numpy (#12282).** A
  matplotlib report should point to numpy #12282. It should ask for documented non-finite handling in
  `boxplot_stats`, such as dropping ±inf like `violin_stats` now does, or a note.

### M1-5. `violin_stats` / `violinplot` do not ignore masked values despite the 3.11 note and docstrings (bug, regression in the claim)

- **Queries:**
  - issues: "violinplot masked array masked values not ignored"
  - PRs: `violin_stats`
  - PRs: `violinplot masked nan`
  - PRs: `boxplot inf`, which surfaced #13651
- **Nearest threads:**
  - PR #31707 "Fix violinplot crash on empty datasets (#31700)". Merged 2026-05-28, backported to 3.11.x.
    https://github.com/matplotlib/matplotlib/pull/31707. **Origin.** `git blame` attributes both
    `x = np.asarray(x)` and `x, = delete_masked_points(x)` in `violin_stats` (cbook.py:1591–1592) to this PR
    (commit 5c55704c1). The PR also added the release note "now ignore masked and non-finite (NaN and inf) values"
    (`api_changes_3.11.0/behavior.rst`, also still in `next_api_changes/behavior/violinplot_empty.rst`). In the
    rendered conversation, no reviewer mentions masked arrays, and the added test covers empty datasets only.
  - PR #13651 "Box plot and violin plot now ignore masked points". **Open** (draft, orphaned), 2019-03-11.
    https://github.com/matplotlib/matplotlib/pull/13651. **Related.** It is the earlier attempt at masked handling
    for both plots, done in `_reshape_2D`; efiring objected to changing `_reshape_2D`.
  - #13533 "Boxplotting Masked Arrays". Closed via PR #27605 (boxplot only, 3.9). **Related.**
  - #30355 "[Bug]: violinplot with nan values fails silently". **Open**, 2025-07-25.
    https://github.com/matplotlib/matplotlib/issues/30355. **Related** (NaN, not masks). It looks stale now: #31707
    already drops NaN on main.
  - PR #30932 "Warn and ignore NaN values in violinplot". **Open**, 2026-01-04. **Related** (NaN only).
  - PR #32428 "DOC: Improve violin/violin_stats/violinplot docs". **Open**, opened 2026-10-02 by timhoffm.
    **Related.** It edits these docstrings right now. A masked-array fix or a docstring correction would collide
    with it.
- **Maintainer statement:** timhoffm on PR #30932, as paraphrased by the page summary and not verbatim: silently
  dropping NaNs "is the way to go".
- **Verdict: no prior report** of the masked-array failure. The claim and the bug arrived in the same merged PR
  (#31707), so the report should cite #31707 and its release note. The one-line fix is `np.asanyarray` or no
  conversion. Mention #32428 so the doc PR does not repeat the claim. **Correction 2026-10-04 (PR #32428 read in full, transcript https://claude.ai/artifact/XNouacZdAvDV4YcbDgqZuv):** the PR does not repeat the masked-values claim. It changes only `axes/_axes.py`, adding "Notes" sections that relate `violinplot`, `violin_stats` and `violin` (Closes #32409, KDE weights). It does not touch `cbook.py` or any line about masked or non-finite values. The existing sentences (`cbook.py:1502`, `_axes.py:9008`) are unchanged context. Nobody in the thread mentions masked arrays. Open, author timhoffm (MEMBER), one review by story645 (MEMBER) with two suggestions.

---

### M2-F1. psd/csd/specgram one-sided doubling keyed to NFFT parity instead of pad_to parity (bug)

- **Queries:**
  - issues: "psd pad_to one-sided Nyquist doubling" (0 hits)
  - issues: "mlab _spectral_helper scaling odd NFFT"
  - issues: "psd last frequency bin wrong factor of two when pad_to differs from NFFT parseval"
  - PRs: `_spectral_helper pad_to`
  - PRs: `psd Nyquist pad_to`
  - PRs: `spectral_helper`
- **Nearest threads:**
  - #24822 "[Bug]: Possible problem with parameter `NFFT` and `pad_to` of `mlab._spectral_helper`". **Open**,
    2022-12-27, label `topic: spectral`, 5 comments (unreadable).
    https://github.com/matplotlib/matplotlib/issues/24822. **Same.** Point 2 of the body says the Nyquist handling
    uses `NFFT/2` instead of `pad_to/2`, and quotes the exact `if not NFFT % 2: slc = slice(1, -1, None)` block.
    Point 1, the window for signals shorter than NFFT, is a separate claim that this audit did not test.
  - #4324 "Inconsistency in function PSD when the NFFT parameter is an odd number". Closed 2015-04-12.
    https://github.com/matplotlib/matplotlib/issues/4324. **Origin.** It was fixed by PR #4326 (tacaswell, merged
    2015-04-12), which introduced the `NFFT % 2` slice (commit 17bc283f8, "BUG : fix scaling issue with mlab.psd and
    odd NFFT"). The PR page does not mention `pad_to`, so the parity was keyed to NFFT without considering padding.
  - #24821 / PR #25122: same reporter, the window-normalisation bug (the 3.5.2-only F9). **Different.** It was fixed
    and merged 2023-02-07, and the PR discussion does not mention #24822.
- **Maintainer statement:** none readable. The #24822 comments do not render, and no PR references #24822.
- **Verdict: already reported (open), #24822.** Nearly four years later there is no linked PR. The audit adds the
  exact affected bins, the Parseval ratios and the SciPy cross-check. A comment on #24822 or a small PR
  (`if not pad_to % 2`) would be more useful than a new issue.

### M2-F2. `detrend_linear` fits a conjugated slope to complex input (bug)

- **Queries:**
  - issues: "detrend_linear complex input wrong slope conjugate"
  - issues: "mlab detrend linear np.cov complex data" (0)
  - issues: "detrend complex" (0)
  - PRs: `detrend_linear`
  - PRs: `detrend complex`
- **Nearest threads:** PR #2522 "Add additional spectrum-related plots and improve underlying structure" (merged 2013).
  This is the **origin**: `b = C[0, 1]/C[0, 0]` is commit 109187e4a (Todd Jennings, 2013-10-06). PRs #9151 / #22920
  (mlab deprecations) and #15765 (docstring rewording) are **different**.
- **Verdict: no prior report.**

### M2-F3. `detrend_linear([x])` returns NaN (bug, minor)

- **Queries:**
  - issues: "detrend_linear single element returns nan" (0)
  - issues: "detrend linear one sample nan RuntimeWarning invalid value divide"
  - PRs: `detrend_linear`
- **Nearest threads:** none relevant. The hits are unrelated RuntimeWarning issues.
- **Verdict: no prior report.** Fold it into the M2-F2 report, since it is the same two lines.

### M2-F4. `scale_by_freq=False` returns a power spectrum (window normalised by (Σw)²), not "density not divided by Fs" (documentation)

- **Queries:**
  - issues: "scale_by_freq False documentation window normalization power spectrum" (rate-limited, then reissued
    as "psd scale_by_freq")
  - PRs: `scale_by_freq`
- **Nearest threads:**
  - #4328 "Incorrect and Inconsistent output of function PSD when scale_by_freq=False". Closed 2015-07-16.
    https://github.com/matplotlib/matplotlib/issues/4328. **Origin.** The reporter asks for the MATLAB `pwelch
    'power'` convention, `scale = 1.0 / win.sum()**2`.
  - PR #4593 "FIX: Correct output of mlab._spectral_helper when scale_by_freq=False" (e-q). Merged 2015-07-16.
    https://github.com/matplotlib/matplotlib/pull/4593. It implemented that convention deliberately. The test
    asserting Pxx(True) == Pxx(False) was changed to use a flat window, because equality "only holds true for flat
    windows". The docstring was not changed.
  - #7237 "mlab.psd behaviour has changed in 1.5.x, psd depends on window size NFFT?". Closed 2023-01-28, label
    Documentation, 4 comments (unreadable). https://github.com/matplotlib/matplotlib/issues/7237. **Same doc
    complaint.** The reporter found that `scale_by_freq=False` results shift with NFFT and that this is undocumented.
    It is not known whether it was closed by a doc change: no commit references #7237, and no mlab doc commit lands
    around 2023-01-28.
  - #862 "The y-axis label of figures created with psd() should not say 'Density' when scale_by_freq=False". Closed
    2014. **Related.**
- **Verdict: declined/intentional for the numbers** (#4328/#4593). **The doc gap was reported before (#7237) and
  closed without a visible doc fix.** A doc-only PR stating "power spectrum, normalised by (Σw)²" is low-risk and
  should cite #4328, #4593 and #7237.

### M2-F5. `mlab.csd` docstring says Pxy is "real valued" (documentation)

- **Queries:**
  - issues: "csd docstring Pxy real valued but returns complex" (0)
  - issues: "cross spectral density csd complex"
  - PRs: `csd docstring`
- **Nearest threads:**
  - #9751 "inconsistency in the algorithm for calculating cross spectral densities". Closed 2017. **Different**
    (algorithm question).
  - PRs #21191 / #21215 "Fix (very-)edge case(s) in csd()" (2021). **Different.**
- **Verdict: no prior report.** This is a trivial doc fix.

### M2-F6. specgram detrends in every mode; the Notes say detrend applies only to mode='psd' (documentation)

- **Queries:**
  - issues: "specgram detrend applied in magnitude mode docstring says only psd"
  - issues: "specgram detrend mode"
  - PRs: `specgram detrend`
- **Nearest threads:** #13540 "Docs for matplotlib.pyplot.specgram() reference an unsupported mode setting" (closed
  2019). **Different** (a different line of the same Notes). The current sentence was last touched by 17b3c44f6
  (oscargus, 2022-04-04, "Improve mlab documentation").
- **Verdict: no prior report.**

### M2-F7. `Axes.psd` / `Axes.csd` with `return_line=True` return a list, documented as a Line2D (documentation / API inconsistency)

- **Queries:**
  - issues: "psd return_line returns list instead of Line2D"
  - issues: "return_line psd csd"
  - issues: "psd return line Line2D list unpack"
  - PRs: `return_line`
- **Nearest threads:** none relevant. #3465 (psd with sliced array, 2014) is different. The
  `line = self.plot(...)` line dates to #2522 (2013).
- **Verdict: no prior report.**
- **Note.** Fixing the code (`line, = self.plot(...)`) changes a return type, so maintainers may prefer a doc fix.

### M2-F8. `Axes.specgram` image rows are offset from `freqs` by up to half a bin; y extent is `[freqs[0], freqs[-1]]` with no half-bin padding (display bug)

- **Queries:**
  - issues: "specgram image extent frequency axis off by half bin"
  - issues: "specgram extent pixel centers frequencies"
  - PRs: `specgram extent`
- **Nearest threads:**
  - #7666 "Default scaling of x-axis in specgram() is incorrect". Closed 2016-12-31.
    https://github.com/matplotlib/matplotlib/issues/7666. **Related.**
  - PR #7692 "Corrected default values of xextent in specgram(). Fixes Bug #7666". Merged 2016-12-29.
    https://github.com/matplotlib/matplotlib/pull/7692. **Related.** It added the half-column padding on the time
    axis only. The page shows no discussion of the frequency extent.
  - #17878 "flipping of imshow in specgram" (closed 2020). **Different** (origin).
  - The y-extent line itself dates to 2007 (e5c556bb0).
- **Verdict: no prior report.** PR #7692 is the precedent: the same reasoning, applied to y.

---

### M3-1. `hist2d(density=True or weights, cmin/cmax)` thresholds the returned values, not counts (documentation)

- **Queries:**
  - issues: "hist2d cmin density True compares densities not counts"
  - issues: "hist2d cmin cmax weights"
  - PRs: `hist2d cmin`
  - PRs: `cmin cmax`
- **Nearest threads:**
  - #11070 "Add a 'density' kwarg to hist2d" (closed 2019). **Related.** It added `density` without revisiting the
    `cmin` text.
  - The `h[h < cmin] = None` line dates to 2012 (3e04d9aa6).
- **Verdict: no prior report.**

### M3-5. `hexbin(bins=int)`: the first class holds only the minimum count (documentation gap / questionable)

- **Queries:**
  - issues: "hexbin bins integer sequence lower bound searchsorted wrong class" (rate-limited, then reissued as
    "hexbin bins sequence lower bound")
  - issues: "hexbin marginals reduce_C_function mean density"
  - PRs: `hexbin bins`
  - PRs: `hexbin bins searchsorted` (0)
- **Nearest threads:**
  - PR #27441 "Fix some minor issues with hexbin bins argument". Merged 2023-12-05. **Different.** It covers NumPy
    array input and the colorbar label, with no discussion of class boundaries.
  - #26202 "hexbin incorrect bin sizes". Closed as not planned, 2024. **Different** (hexagon geometry).
  - The `bins -= 1 ... searchsorted` code dates to 2008 (0e32f3849).
- **Verdict: no prior report.**

### M3-6. `hexbin(bins=[...])`: a count equal to a listed "lower bound" lands in the class below (bug vs docstring)

- **Queries:** the same as M3-5. The search for "hexbin bins sequence lower bound" returned #32077, #30764, #26202,
  #20877 and others, none of them on class assignment.
- **Nearest threads:** none relevant (see M3-5).
- **Verdict: no prior report.** File it with M3-5. Both are the one `searchsorted(side='left')` line.

### M3-7. `hexbin(xscale/yscale='log').get_offsets()` returns log10 exponents, docstring says "in data coordinates" (documentation / API inconsistency)

- **Queries:**
  - issues: "hexbin log scale get_offsets returns log10 values not data coordinates"
  - issues: "hexbin xscale log offsets exponent coordinates"
  - PRs: `hexbin offsets`
- **Nearest threads:**
  - #18045 "Cannot access hexbin data when `xscale='log'` and `yscale='log'` are set". Closed, 2020-07-23 →
    2024-04-17. https://github.com/matplotlib/matplotlib/issues/18045. **Same area.** The reporter got
    `[[0, 0]]` from `get_offsets()` (the ≤3.7 behaviour the audit saw).
  - PR #27818 "Set polygon offsets for log scaled hexbin" (dstansby). Merged 2024-04-17.
    https://github.com/matplotlib/matplotlib/pull/27818. **This fix introduced the current state.** In one commit
    (ecb4d656c) it added "in data coordinates" to the docstring and a test, `test_hexbin_log_offsets`, which asserts
    log-space offsets: data `geomspace(1, 100)` gives offsets `[[0,0],[0,2],[1,0],...]`. The review comments did not
    render.
  - #32156 / PR #32000: PDF culling of hexbin offsets (3.11). **Different.**
- **Verdict: already fixed** (offsets now exist). However, the merged test locks in log10 offsets while the same PR's
  docstring promises data coordinates. The exponent behaviour looks intentional, so file this as a docstring
  correction ("in the scaled (log10) coordinates when xscale/yscale='log'") and cite #27818. Do not file it as a bug.

### M3-8/9. `hexbin(marginals=True)` with `C=None`: every marginal bar is 1 (bug)

- **Queries:**
  - issues: "hexbin marginals all same color constant when C is None"
  - issues: "hexbin marginals reduce_C_function mean density"
  - PRs: `hexbin marginals`
- **Nearest threads:**
  - PR #9171 "BUG: Fix implementation of marginals in pyplot.hexbin" (adeak). Closed unmerged, 2017-09-08 →
    2018-01-09. https://github.com/matplotlib/matplotlib/pull/9171. **Same.** The description reads: the feature
    "gives a constant 1 density (interspersed with nans) when the `C` optional keyword is not passed".
  - PR #18875 "Improvements and bugfixes for hexbin marginals" (MihaiBabiac). Closed unmerged, 2020-11-02 →
    2024-01-06. https://github.com/matplotlib/matplotlib/pull/18875. **Same.** Item 5 of its description: with no C
    the code applies `np.mean` to ones, giving "binary values in the marginal".
  - PR #21039 "Fix `hexbin` marginals and log scaling" (dstansby). Merged 2021-09-24. **Did not fix this.** Commit
    7c800f96d rewrote `coarse_bin` but kept `if C is None: C = np.ones(len(x))` with the default
    `reduce_C_function=np.mean`.
  - #21353 "[MNT]: Deprecate hexbin marginals?" (dstansby). Closed 2021-12-21. **Related.** It cites "lots of
    possible issues with the current implementation". The marginals were not deprecated.
- **Maintainer statements:**
  - tacaswell, PR #9171, 2017-09-24:
    > "the current behavior is also broken and the proposed behavior is less wrong."

    and proposed to
    > "raise an error if marginals are asked for in the `C is None` case"
  - jklymak, PR #9171, 2018-01-09:
    > "I'm closing as per @adeak's comment above."
  - dstansby, PR #18875, 2024-01-06:
    > "Apart from the new error in the PR I opened, I think the rest of the issues were fixed (possibly by #21039?) at
    > some point between this PR being opened and now, so I'll close this PR. Feel free to open new issues about the
    > hexbin marginals if I've got that wrong!"
- **Verdict: reported before and closed without a fix.** The last maintainer closed it on the mistaken belief that
  #21039 had fixed it, and explicitly invited a new issue. It is not declined. **Worth filing.** The report should
  cite #9171, #18875 and #21039, show that the `C = np.ones` + `np.mean` path is unchanged on main, and offer
  tacaswell's 2017 options: count-based marginals for C=None, or an error.

### M3-10. `xcorr`/`acorr(normed=True)` with complex input: zero lag ≠ 1, because `np.dot(x, x)` is not Σ|x|² (bug)

- **Queries:**
  - issues: "xcorr complex normed"
  - issues: "acorr xcorr normalization complex signal zero lag not 1"
  - issues: "xcorr complex conjugate normalization vdot"
  - PRs: `xcorr`
- **Nearest threads:**
  - #1835 "docstrings of cross-correlation functions (acorr and xcorr) need clarification" (closed 2017). **Related**
    (docs).
  - PR #12004 "Update acorr and xcorr docs to match numpy docs" (merged 2018). **Related.** It added the
    conj-definition wording and does not discuss normalisation.
  - #15021 "xcorr ... outputs values larger than 1 when passed boolean arrays" (closed 2019). **Different input**,
    same symptom class.
- **Verdict: no prior report.**

### M3-11/12. `acorr`/`xcorr` on int16 (narrow integer) input: wrapped sums, NaN with normed=True (bug)

- **Queries:**
  - issues: "acorr integer array TypeError cannot cast ufunc divide"
  - issues: "acorr int16 audio overflow wrong values"
  - PRs: `acorr`
  - PRs: `xcorr`
- **Nearest threads:**
  - PR #25832 "[BUG] Prevent under the hood downcasting of values". Merged 2023-05-15, backported as #25892.
    https://github.com/matplotlib/matplotlib/pull/25832. **Related.** It fixed the int crash (the old-only
    M3-13) by changing `correls /=` to `correls = correls /`. CI then hit an integer-overflow warning on Windows,
    which the PR sidestepped by making the test use int64 instead of casting to float.
  - #15021 (boolean arrays, closed 2019). **Related.**
- **Maintainer statements, PR #25832:**
  - tacaswell, 2023-05-09:
    > "I am very confused why this is only happening on windows, but this looks like a real warning from numpy and our
    > tests are set to fail on any warning."
  - The author's reply, 2023-05-10 (not a maintainer):
    > "This may be due to the system default long in Windows vs Linux. So, trying explicit `int64` now."
- **Verdict: no prior report.** The overflow mechanism was observed in #25832's CI and worked around in the test
  rather than in the code. Cite it in the report.

### M3-14. `stackplot(baseline='weighted_wiggle')` minimises the weighted wiggle for the reversed layer order (bug)

- **Queries:**
  - issues: "stackplot weighted_wiggle baseline wrong streamgraph"
  - issues: "stackplot weighted_wiggle int dtype"
  - PRs: `stackplot wiggle`
- **Nearest threads:**
  - PR #1517 "ENH: Add baseline feature to stackplot" (Tillsten, 2012–2013). **Origin.** Ported from Byron's
    streamgraph. The page shows no discussion of the formula or of screen versus data orientation. The
    `center = (move_up - 0.5) * increase` line is 339ca4e63 (2013).
  - #6313 "weighted_wiggle stackplot fails when all lines are zero at same x" (closed 2019) and PR #6358 (2016).
    **Different** (division by zero).
  - #22393 "stackplot creates artifacts when height of input is zero" (closed as not planned). **Different.**
- **Verdict: no prior report.**

### M3-15. `stackplot(baseline='weighted_wiggle')` with integer layers truncates 1/total to 0 (bug, regression since 2.0)

- **Queries:**
  - issues: "stackplot integer input baseline truncation"
  - issues: "stackplot weighted_wiggle int dtype"
  - PRs: `stackplot wiggle`
- **Nearest threads:** #6313 (above) is **related**. `git blame`: `inv_total = np.zeros_like(total)` is a1dbd55ac
  (Elliott Sales de Andrade, 2016-10-23, "Avoid divide-by-zero in stackplot", first in v2.0.0). It replaced
  `np.where(total > 0, 1./total, 0)`, which promoted to float. **The integer truncation is a regression introduced in
  2.0.0.**
- **Verdict: no prior report.** The fix is a one-liner (`np.zeros_like(total, dtype=float)`). It is independent of
  M3-14.

---

### M4-1. `Normalize()` autoscale with NaN in a plain ndarray gives vmin = vmax = NaN (documentation gap / sharp edge)

- **Queries:**
  - issues: "Normalize autoscale NaN vmin vmax nan all bad color"
  - issues: "Normalize with nan in array returns all nan"
  - PRs: `autoscale_None nan`
- **Nearest threads:**
  - #28405 "[Bug]: Normalize.autoscale gets broken by np.nan values". **Open**, 2024-06-16, 0 comments.
    https://github.com/matplotlib/matplotlib/issues/28405. **Same** (same reproducer, 3.9.0).
  - PR #28406 "Ignore np.nan values in Normalize.autoscale()". **Open**, 2024-06-16, awaiting the author.
    https://github.com/matplotlib/matplotlib/pull/28406. **Same.**
  - PR #4824 "Two bugs in colors.BoundaryNorm". Merged 2015-08-08. **Related** (general NaN-at-norm-level policy).
- **Maintainer statements:**
  - greglucas, PR #28406, 2024-06-23:
    > "I agree this is a bit of an annoyance, but I also wonder if this would be a bit of a whack-a-mole to try and fix
    > everywhere." ... "I wonder if it would be easier to use `A = cbook.safe_masked_invalid(A)` above this so we are
    > entering without any of the invalid possibilities." ... "FYI: It looks like there have been some
    > micro-optimizations in this area, so maybe people do not want the extra speed penalty to support this?"
  - timhoffm, PR #28406, 2024-10-07:
    > "I believe we need a clear understanding and documentation, what `A` can be." ... "Typically in colormapping
    > scenarios, `A` is the array `ScalarMappable._A`, and `set_array()` already runs through
    > `cbook.safe_masked_invalid(A)`." ... "So if I'm not mistaken, at the bare minimum it should be sufficient to
    > document that A is not expected to have invalid values." ... "It's t.b.d. whether we want to make that
    > (relatively rare) case be more comfortable as well. And that decision includes a look at the performance
    > tradeof."
  - efiring, PR #4824, 2015-07-31:
    > "Nans are presently not supported in the Normalize API. Obviously, this could be changed. It would impose a
    > performance penalty for large arrays. ... But Normalize is at a lower level, so we could leave it as-is and just
    > say it is the caller's responsibility to clean up the input."
- **Verdict: already reported (open), #28405 / #28406.** Maintainers lean towards documenting "no invalid values"
  rather than changing the code. Do not file a new issue. At most, comment on #28405 that the docstring still says
  vmin/vmax "default to the minimum and maximum values of the input".

### M4-2..5. SymLogNorm / symlog scale do not use the documented *linscale* (factor 1/(1−1/base)) (documentation/implementation mismatch)

- **Queries:**
  - issues: "SymLogNorm linscale number of decades documentation wrong"
  - issues: "symlog linscale base linscale_adj"
  - PRs: `linscale`
- **Nearest threads:**
  - #26280 "[Bug]: linscale parameter to SymmetricalLogScale behaves incorrectly". **Open**, 2023-07-09, label
    `topic: transforms and scales`, 1 comment (unreadable).
    https://github.com/matplotlib/matplotlib/issues/26280. **Same.** It quotes "the number of decades to use for
    each half of the linear range" and states that `transform_non_affine` breaks it, including at the defaults. It
    proposes two corrected transforms. It is filed against the scale, but SymLogNorm uses the same transform
    (`make_norm_from_scale`).
  - PR #29347 "DOC: Explain parameters linthresh and linscale of symlog scale" (timhoffm). Merged 2024-12-21.
    **Related.** It rewrote the symlog demo text ("ratio of visual space ... relative to one decade") without
    resolving the factor. It came from #29335.
  - #2288 "Symmetric Log scale: linscale < 1 ?" (2013, closed). **Related** (history of linscale semantics).
  - PR #30993 (2026-02-05, perf). It touched the `linscale_adj` line without changing the math.
- **Maintainer statement:** none readable.
- **Verdict: already reported (open), #26280.** The audit adds the SymLogNorm side and exact numbers for base 2, e
  and 10. Comment on #26280 or link to it; do not open a duplicate. A fix needs a decision: change the docs to
  "linscale·base/(base−1) decades", or change the transform (a behaviour change for every symlog plot).

### M4-6/7. BoundaryNorm with ncolors > nbins never uses the last colour (float truncation) (bug)

- **Queries:**
  - issues: "BoundaryNorm last color never used ncolors greater than bins int16 truncation"
  - issues: "BoundaryNorm wrong color index rounding floating point"
  - PRs: `BoundaryNorm` (38 hits scanned)
  - PRs: `BoundaryNorm int16`
- **Nearest threads:**
  - #21911 "[ENH]: BoundaryNorm should not need to know colormap length" (jklymak). **Open**, 2021-12-10.
    https://github.com/matplotlib/matplotlib/issues/21911. **Related.** It is about the stretch itself and does not
    mention truncation.
  - #31195 "[ENH]: Design considerations for discrete colormapping" (timhoffm). **Open**, 2026-02-24. **Related**
    (redesign).
  - PR #32196 "Clarify interval semantics in BoundaryNorm documentation". Merged 2026-08-10. **Different**
    (right-open last bin).
  - PR #1260 "Fix BoundaryNorm interpolation with numpy 1.7rc" (2012). **Different** (casting, not rounding).
  - PR #17830 / commit a5f531791 (2020, "pick the middle color only 1 region"). Last touch of the `astype(np.int16)`
    line.
- **Verdict: no prior report.** It is concrete, small and fixable (round, or integer arithmetic). **Worth filing**,
  and it fits under #31195's redesign discussion.

### M4-8/15. BoundaryNorm maps NaN to the "over" index (bug)

- **Queries:**
  - issues: "BoundaryNorm nan mapped to over color instead of bad"
  - issues: "BoundaryNorm NaN digitize"
  - PRs: `BoundaryNorm nan`
- **Nearest threads:** PR #4824 "Two bugs in colors.BoundaryNorm" (fmaussion). Merged 2015-08-08.
  https://github.com/matplotlib/matplotlib/pull/4824. **Related.** NaN handling in BoundaryNorm was discussed and
  deliberately left out.
- **Maintainer statements, PR #4824:**
  - efiring, 2015-07-31: see M4-1 ("Nans are presently not supported in the Normalize API ... it is the caller's
    responsibility to clean up the input.").
  - fmaussion (PR author), 2015-08-03:
    > "`BoundaryNorm` is different from all other classes in that in returns integers and not floats. It will produce
    > warnings if run on non-masked NaN values, but I think it's ok like this."
- **Verdict: no prior report** of NaN being coloured as "over". The 2015 position (callers must mask NaN) makes a
  code change less likely, but the outcome is not a warning: NaN is silently drawn as over-range. That is worth
  reporting, together with M4-1's documentation request.

### M4-9. BoundaryNorm with ncolors > 32767: int16 wraparound (numpy 1.x) / OverflowError (numpy 2.x) (bug, extreme parameter)

- **Queries:**
  - issues: "BoundaryNorm int16 overflow large number of colors"
  - PRs: `BoundaryNorm int16`
  - plus the M4-6 queries
- **Nearest threads:** #22728 "[ENH]: Higher bitdepth turbo colormap" (open) is related only in the sense that
  colormaps with more than 256 entries are wanted. No int16 report.
- **Verdict: no prior report.** It is low priority. Mention it inside the M4-6 report, since it is the same
  `astype(np.int16)` line.

### M4-10/14. Colormap ignores NaN inside a masked array that has any masked element (bug)

- **Queries:**
  - issues: "colormap masked array with nan unmasked value drawn first color instead of bad"
  - issues: "Colormap __call__ masked nan mask_bad"
  - issues: "to_rgba masked array containing nan wrong color"
  - PRs: `colormap nan masked bad`
- **Nearest threads:**
  - #9892 "colormaps (cm) do not properly handle NaN values". Closed 2019 (v3.2.0). **Related**: plain-array NaN,
    which passes now.
  - #31008 "Discussion: Use of masked arrays internally". **Open**, 2026-01-21. **Related** (general).
  - #17323 (pcolor NaN colour leak). **Different.**
  - `mask_bad = X.mask if np.ma.is_masked(X) else np.isnan(xa)` is commit 04e708882 (Antony Lee, 2023-01-14,
    "Simplify handling of out-of-bound values `Colormap.__call__`"). That commit changed the wrong colour from
    "under" (≤3.7) to "first", but the either/or logic was not new.
- **Verdict: no prior report.** The fix is a one-liner (`X.mask | np.isnan(xa)`).

### M4-11. `bytes=True` truncates instead of rounding (documentation gap)

- **Queries:**
  - issues: "colormap bytes=True truncates instead of rounding uint8"
  - issues: "to_rgba bytes rounding 255 off by one"
  - issues: "rounding versus truncation of RGB values uint8 colormap"
  - PRs: `"bytes=True" round`
- **Nearest threads:**
  - #20459 "Colormaps are not matching with reference pngs". **Open**, 2021-06-17.
    https://github.com/matplotlib/matplotlib/issues/20459. **Same root cause** (viridis last colour `#fde724` vs
    `#fde725`).
  - #17410 "Inconsistent conversion from normalized to 8-bit RGBA tuples". Closed as duplicate, 2020-05-14.
    https://github.com/matplotlib/matplotlib/issues/17410. **Same** (Colormap `bytes=True` truncates, `to_hex`
    rounds).
  - PR #31134 "WIP: Experimenting with rounding vs truncating RGB values" (ayshih). **Open draft**, 2026-02-11.
    https://github.com/matplotlib/matplotlib/pull/31134. **Same.** Rounding colormap bytes breaks 58+ image tests;
    truncating in `rgb2hex` breaks 12 SVG tests. anntzer is reported to favour rounding (paraphrased by the page
    summary).
- **Verdict: already reported (open), #20459 / PR #31134.** Do not file. At most add a doc note on `bytes=True`.

### M4-12. `LinearSegmentedColormap(gamma≠1).reversed()` is not the original read backwards (bug)

- **Queries:**
  - issues: "LinearSegmentedColormap gamma lost resampled reversed"
  - issues: "colormap gamma parameter ignored when resampling get_cmap lut"
  - PRs: `LinearSegmentedColormap gamma`
  - PRs: `colormap reversed gamma`
- **Nearest threads:** #31939 "Regression in 3.11.0 with LinearSegmentedColormap" (closed, `from_list` parsing).
  **Different.** Nothing on gamma.
- **Verdict: no prior report.**

### M4-13. `LinearSegmentedColormap.resampled()` drops gamma (bug)

- **Queries:**
  - the same as M4-12
  - PRs: `resampled gamma`
- **Nearest threads:** none.
- **Verdict: no prior report.** File it with M4-12 (one issue, two one-line fixes in `colors.py`).

### M4-16. `imshow`/`set_array` mask ±inf as "bad" (transparent) instead of over/under (documentation gap)

- **Queries:**
  - issues: "imshow inf values shown as bad color transparent instead of over under"
  - issues: "safe_masked_invalid masks infinity colormap over color"
  - issues: "imshow np.inf"
  - PRs: `safe_masked_invalid inf`
  - PRs: `imshow infinite values`
- **Nearest threads:**
  - #18735 "imshow padding around NaN values" (closed 2021). **Different.**
  - PR #9629 "Make pcolor(mesh) preserve all data" (2017–2020). **Different.**
  - Nothing on ±inf → bad.
- **Verdict: no prior report.** This is a doc gap; a behaviour change is unlikely to be wanted.

### M4-17. Automatic contour levels (MaxNLocator) are multiples of the step only relative to an offset (documentation gap)

- **Queries:**
  - issues: "MaxNLocator ticks not multiples of step offset large values"
  - issues: "MaxNLocator steps docstring multiples ticks not multiple"
  - issues: "contour levels odd values not round numbers 1.5 step"
  - PRs: `MaxNLocator scale_range offset`
- **Nearest threads:**
  - PR #5768 "Fix floating point inaccuracies in axes limits; partial work on offset value selection" (merged 2016).
    **Related.**
  - #30996 "[Doc]: contour and contourf levels default not specified". Closed 2026-01-29 via #31013 / #31016.
    **Related**: level count, not multiples.
- **Verdict: no prior report.** Priority is low; the colours are unaffected.

### M4-18. contourf leaves a plateau exactly at `levels[0]` unfilled when `min(Z) < levels[0]` (documentation ambiguity / bug)

- **Queries:**
  - issues: "contourf values equal to lowest level not filled when data minimum below"
  - issues: "contourf lowest interval closed both sides zmin levels[0]"
  - PRs: `_get_lowers_and_uppers`
- **Nearest threads:**
  - #21382 "Data 0 cannot be plotted by matplotlib.pyplot just because some data is less than 0". **Open**,
    2021-10-19, labels `status: confirmed bug`, `topic: contour`, milestone "future releases".
    https://github.com/matplotlib/matplotlib/issues/21382. **Same.** It points at the
    `if self.zmin == lowers[0]` check in `_get_lowers_and_uppers` (code from 2010, 5a9d580b8).
  - PR #31903 "FIX: fill contourf minimum region when it falls just below the lowest level (#21382)". Closed
    unmerged, 2026-07-23. https://github.com/matplotlib/matplotlib/pull/31903. **Same** (tolerance approach,
    rejected).
  - PR #31902 (duplicate, closed 2026-06-15). **Same.**
- **Maintainer statement:** scottshambaugh, PR #31903, 2026-07-07:
  > "I don't think a tolerance is the right way to solve this, which was already addressed by this maintainer comment
  > in the original issue: #21382 (comment)"

  The link goes to https://github.com/matplotlib/matplotlib/issues/21382#issuecomment-3498835642. That comment's text
  could not be retrieved.
- **Verdict: already reported (open), #21382 (confirmed bug).** Do not file. If anything, add the exact-zero plateau
  case to #21382; the reporter's case is near-zero.

---

## Present only on old releases (not searched further; fixes identified)

| finding | builds | fixed by |
|---|---|---|
| M1 (3.5.2): empty input lacks the `iqr` key | 3.5.2 | PR #23494 (commit 5f7f6a898, 2022-07-28, "Fix empty data statistics in boxplot_stats"), first in v3.6.0 |
| M2-F9: power normalisation used \|window\| | 3.5.2 (and 3.6.x) | Issue #24821 → PR #25122, merged 2023-02-07 (3.7.0) |
| M3-2/3: `hexbin mincnt` docstring "more than" vs inclusive code | 3.5.2, 3.7.1 | PR #21381 (3.8.0, "made consistently inclusive"), then PR #27179 (3.8.1, restore the default with C) |
| M3-4: `hexbin bins='log'` docstring says log10(i+1) | 3.5.0 to at least 3.7.1 | Code changed in PR #21038/#21039 (3.5.0). The docstring was reported in #30764 and fixed by PR #30774 (commit 00b862f0b, 2025-11-21) |
| M3-13: `acorr(int array, normed=True)` raises UFuncTypeError | 3.5.2, 3.7.1 | PR #25832, merged 2023-05-15, backported as #25892 (3.7.2) |
| M3-16..25: pie float32 percentages | 3.5.2, 3.7.1 | The `np.asarray(x, np.float32)` cast was removed in PR #30733 ("introduce PieContainer and pie_label", commit a97c66521), first in v3.11.0 |
| M4-19/20: imshow draws boundary values in the neighbouring BoundaryNorm colour | 3.5.2, 3.7.1 | Fixed by the 3.10/3.11 image-resampling rework. The exact PR was not pinned here; the notes' candidate is #28122 (not verified) |
| M4-21: contour docstring "n+1" levels | 3.5.2, 3.7.1 | Issue #30996 → PRs #31013/#31016 (2026-01) |
| M4-22: `LogNorm()` autoscale with NaN raises | 3.5.2 | PR #21989 "Autoinfer norm bounds" (commit a5abb464d), first in v3.6.0 |

---

## Summary table (findings present on main)

| id | finding | type | nearest thread(s) | verdict |
|---|---|---|---|---|
| M1-1 | `whis` text "below/above" vs inclusive fences | doc | #25134 / #25135 (summary line fixed, `whis` text not) | no prior report |
| M1-2 | whisker clamped to Q1/Q3, so not a datum | doc | PR #16244 (phobson: whiskers are data points) | no prior report |
| M1-3 | `whis=(lo,hi)` whiskers at extreme datum, not at percentile | doc | none | no prior report |
| M1-4 | +inf next to a quartile gives NaN Q3/IQR and a spurious flier | bug (numpy root) | numpy #12282 (open) | no prior report in mpl; root cause reported (open) in numpy |
| M1-5 | violin ignores masks despite the 3.11 note | bug | PR #31707 (introduced it); #13651 (open, orphaned); doc PR #32428 (open) | no prior report |
| M2-F1 | psd/csd/specgram doubling keyed to NFFT parity, not pad_to | bug | **#24822 (open)**; origin #4324/#4326 | already reported (open) |
| M2-F2 | `detrend_linear` complex: conjugated slope | bug | none (origin #2522) | no prior report |
| M2-F3 | `detrend_linear([x])` → NaN | bug (minor) | none | no prior report |
| M2-F4 | `scale_by_freq=False` = power spectrum, undocumented | doc | #4328/#4593 (intentional); #7237 (doc complaint, closed) | declined/intentional (numbers); doc gap raised before, unfixed |
| M2-F5 | `mlab.csd` says "real valued" | doc | none | no prior report |
| M2-F6 | specgram Notes: detrend "only psd" | doc | #13540 (different line) | no prior report |
| M2-F7 | `return_line` gives a list, not a Line2D | doc/API | none | no prior report |
| M2-F8 | specgram y extent lacks half-bin padding | display bug | #7666/#7692 (x only) | no prior report |
| M3-1 | hist2d cmin/cmax applied to density/weights | doc | #11070 (related) | no prior report |
| M3-5 | hexbin `bins=int`: minimum alone in class 0 | doc/questionable | #27441 (different) | no prior report |
| M3-6 | hexbin `bins=[...]`: bound goes to lower class | bug | none | no prior report |
| M3-7 | hexbin log `get_offsets` are exponents vs "data coordinates" | doc/API | #18045 → PR #27818 (test asserts log10) | already fixed (offsets); doc contradiction introduced by the fix |
| M3-8/9 | hexbin marginals with C=None all 1 | bug | PRs #9171, #18875 (closed unmerged); #21039 did not fix | reported before, closed without fix (believed fixed) |
| M3-10 | xcorr/acorr normed complex ≠ 1 | bug | #1835, #12004 (docs) | no prior report |
| M3-11/12 | acorr int16 overflow / NaN | bug | PR #25832 (overflow seen in CI, sidestepped) | no prior report |
| M3-14 | weighted_wiggle uses reversed layer order | bug | PR #1517 (origin) | no prior report |
| M3-15 | weighted_wiggle int truncation | bug (regression since 2.0) | commit a1dbd55 / #6313 | no prior report |
| M4-1 | Normalize autoscale with NaN | doc gap | **#28405 + PR #28406 (open)** | already reported (open) |
| M4-2..5 | SymLogNorm linscale factor 1/(1−1/base) | doc/impl mismatch | **#26280 (open)**; PR #29347 (demo docs) | already reported (open) |
| M4-6/7 | BoundaryNorm skips last colour (truncation) | bug | #21911, #31195 (related) | no prior report |
| M4-8/15 | BoundaryNorm NaN → over | bug | PR #4824 (2015: NaN is caller's job) | no prior report (maintainer stance may push to docs) |
| M4-9 | BoundaryNorm int16 for >32767 colours | bug (extreme) | none | no prior report |
| M4-10/14 | Colormap: NaN in masked array with a mask | bug | #9892 (plain NaN, fixed) | no prior report |
| M4-11 | `bytes=True` truncates | doc gap | **#20459 (open)**, #17410 (dup), PR #31134 (draft) | already reported (open) |
| M4-12 | LSC `reversed()` with gamma ≠ 1 | bug | none | no prior report |
| M4-13 | LSC `resampled()` drops gamma | bug | none | no prior report |
| M4-16 | imshow masks ±inf as bad | doc gap | none | no prior report |
| M4-17 | MaxNLocator multiples relative to an offset | doc gap | #5768, #30996 (related) | no prior report |
| M4-18 | contourf plateau at levels[0] unfilled | bug/doc | **#21382 (open, confirmed bug)**; PR #31903 rejected | already reported (open) |
