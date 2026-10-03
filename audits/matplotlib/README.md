# Matplotlib audit against 240 published papers (2021–2026)

_Generated 2026-10-03 against `matplotlib/matplotlib` `main` @ `44f2e00` (run as an overlay on 3.11.2, see below),
executed on the 3.11.2 release and on 3.7.1 and 3.5.2. Focus: the numbers a figure carries — box-plot and violin
statistics, the KDE, Welch spectra and spectrograms, histogram / hist2d / hexbin counts, correlation, stackplot
baselines, pie percentages, error bars, and the mapping from data to colour (norms, colormaps, image pixels,
colorbars, contour levels and fills) — checked against exact recomputations._

## What this is

The six-journal survey found **240 papers** that name Matplotlib (*Nature* 128, PNAS 85, *Cell* 19, *Science* 8;
2021–2026), nearly always beside SciPy (136), NumPy (135) or seaborn (96). Matplotlib draws the figure, but several
of its functions also compute the numbers the reader sees: the quartiles and whiskers of a box plot, the density of
a violin, a power spectral density, a bin count, the colour a value is drawn in. Every such function used by the
cohort was exercised on generated data and compared with a `Fraction` recomputation, a closed form, a plain-Python
port written from the docstring, or (where installed) SciPy, and the drawn artists were read back and compared
with the same truths.

## Scope and versions

| build | what it is | numpy / scipy / python |
|---|---|---|
| **main overlay** | 3.11.2 with `cbook.py`, `mlab.py`, `colors.py`, `colorizer.py`, `contour.py`, `stackplot.py` and `axes/_axes.py` from `main` @ 44f2e00 copied in | 2.5.3 / 1.18.1 / 3.12.3 |
| **3.11.2** | current release | 2.5.3 / 1.18.1 / 3.12.3 |
| **3.7.1** | the version the cohort names most (8 papers) | 1.26.4 / — / 3.11.15 |
| **3.5.2** | joint second most named with 3.5.1 (6 papers each; the 3.5 family is named in 15) | 1.23.5 / — / 3.10.20 |

**Why `main` is an overlay.** A full build of `main` is not possible in this session: the download of its SheenBidi
dependency is blocked. The seven Python files that hold every code path under test were therefore copied from
44f2e00 into a 3.11.2 install; the overlaid `mlab.py`, `axes/_axes.py` and `colors.py` are byte-identical to the
source tree, and the overlay is visible in the outputs (`Axes.psd` has the 3.12 `Funits` parameter; pie
`wedge_labels` exists). `image.py`, `scale.py`, `ticker.py` and `colorbar.py` run as their 3.11.2 copies; the
44f2e00 source of `scale.py` (lines 507–520) and `cbook.safe_masked_invalid` was read and carries the same code
behind MPL19 and MPL31. In all four harness groups the FAIL lines on the overlay and on 3.11.2 are identical:
nothing found here changed between the 3.11.2 release and `main`.

## How the papers use Matplotlib (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 41 (3.7.1 ×8, 3.5.2 ×6, 3.5.1 ×6, 3.3.2 ×5, 3.4.3 ×5, 3.2.1 ×5; families 3.5 ×15, 3.7 ×14, 3.8 ×10, 3.4 ×10, 3.3 ×10) |
| SciPy / NumPy / seaborn / scikit-learn alongside | 136 / 135 / 96 / 59 |
| heatmap / colormap / colour scale | 35 |
| custom code stated | 22 |
| histogram | 14 |
| 3D plotting | 13 |
| violin plot / KDE | 10 |
| scatter / line plots | 9 |
| box plot | 8 |
| contour; error bars / mean ± SEM | 5; 5 |
| log / symlog scale | 4 |
| spectrogram / PSD / spectral | 3 |
| pie / stacked plots; hexbin / 2-D density | 2; 1 |

The profile (`matplotlib_profile.py`, `matplotlib_profiles.jsonl`, `profile_run.log`) ran on the survey's stored
evidence sentences (no route to Europe PMC from this session: 240 of 240 records are `survey_cache`), so the counts
are lower bounds. seaborn ≥ 0.13 calls `cbook.boxplot_stats`, so the box-plot findings also reach seaborn box
plots.

## Verification method

Four harness groups in [`verify/`](verify/), sharing `_synth.py` (Agg backend, version banner, `report`/`close`
helpers). Each runs under the interpreter given; `.out` is the main overlay, `.v<version>.out` the releases, and
`.notes.md` has one paragraph per failing check with the source lines.

| group | what it checks | main overlay | 3.11.2 | 3.7.1 | 3.5.2 |
|---|---|---|---|---|---|
| `m1_boxplot_violin_stats` | `boxplot_stats`, `violin_stats`, `GaussianKDE`, `boxplot`/`bxp`/`violinplot` | 164 ok / 12 FAIL | 164 / 12 | 144 / 6 | 142 / 8 |
| `m2_spectral` | `psd`, `csd`, `cohere`, `specgram`, `*_spectrum`, detrend/window helpers, Axes wrappers | 258 / 24 | 258 / 24 | 234 / 20 | 233 / 21 |
| `m3_hist_hexbin_counts` | `hist`, `stairs`, `hist2d`, `hexbin`, `acorr`/`xcorr`, `stackplot`, `pie`, `errorbar` | 165 / 11 | 164 / 11 | 149 / 25 | 148 / 25 |
| `m4_color_mapping` | every norm, colormaps, `to_rgba`, `imshow` pixels, colorbar bands, contour levels and fills | 190 / 18 | 190 / 18 | 187 / 21 | 182 / 22 |
| **total** | | **777 / 65** | **776 / 65** | **714 / 72** | **705 / 76** |

The older builds run fewer checks where a feature or SciPy is missing; expectations that changed between versions
(masked handling in box plots from 3.9 and violins from 3.11, hexbin `mincnt` from 3.8, PowerNorm below vmin from
3.9, TwoSlopeNorm autoscale from 3.8, the contour level-count wording) follow each build's own documentation.

## Findings (details and file:line evidence in [`component-reviews/`](component-reviews/))

Kinds: **bug** (a wrong number, colour or crash against the documented definition), **documentation gap** (the code
is defensible but the documentation says something else or nothing), **old-release only** (fixed by the current
release), **harness expectation** (the harness asked for more than is promised). "All four" = main overlay, 3.11.2,
3.7.1, 3.5.2. The "Prior report" column is filled by the parallel tracker search (`prior-reports.md`).

| id | component | finding | kind | magnitude | builds affected | status | prior report |
|---|---|---|---|---|---|---|---|
| MPL1 | colour mapping | `BoundaryNorm` with more colours than bins truncates the stretched index to int16, so the last bin gets `ncolors−2` and the map's last colour is never used | bug | 266 of the tested (ncolors, bins) pairs off by one index, 233 of them in the last bin; 12 bins over 16 colours → top bin 14, not 15; 26 bins over 256 → 254 | all four | confirmed by execution; colorbar shows the same wrong colour | search pending |
| MPL2 | box / violin | `violin_stats` / `violinplot` keep masked values (`np.asarray` drops the mask) although the 3.11 release note and both docstrings say they are ignored | bug | three masked values: min/max −50/50 for −2.862/1.527, mean −0.1167 for −0.2079, quantiles [−0.9021, 0.5390] for [−0.9008, 0.4050]; max line drawn at 50 | main, 3.11.2 (on 3.7.1/3.5.2 median, quantiles and KDE were wrong instead, undocumented then) | confirmed by execution | search pending |
| MPL3 | spectral | one-sided `psd`/`csd`/`specgram` double the last bin by NFFT parity instead of pad_to parity | bug | last bin ×2 (odd NFFT, even pad_to) or ×½ (even NFFT, odd pad_to); psd maxabsdiff 3.530 on scale 24.04 at 99/128; Parseval ratio 1.011018 at 63/64, 0.998926 at 64/65; SciPy disagrees in that bin | all four | confirmed by execution and against SciPy | search pending |
| MPL4 | hexbin | `hexbin(marginals=True)` with `C=None` averages ones, so every marginal bar is 1 | bug | hbar [1, 1, 1, 1, 1, 1] for column counts [21, 89, 196, 184, 90, 20]; vbar likewise | all four | confirmed by execution | search pending |
| MPL5 | hexbin | `hexbin(bins=<sequence>)`: a count equal to a listed "lower bound" goes to the bin below | bug | bins=[1, 4, 8]: count 4 classed with 2–3, count 8 with 5–6 | all four | confirmed by execution | search pending |
| MPL6 | box plot | `boxplot_stats` with +inf next to a quartile index returns NaN Q3, IQR and upper whisker and makes a finite value a flier (root cause `np.percentile`, NP4 in the numpy audit) | bug | [1, 2, 3, 4, inf]: q3 = iqr = whishi = nan (Q3 should be 4), fliers [1.0] | all four | confirmed by execution | search pending |
| MPL7 | colour mapping | a NaN inside a masked array that has a masked element is drawn in a data colour, not "bad" | bug | first colour on main/3.11.2, under colour on 3.7.1/3.5.2 (`cmap` and `to_rgba`) | all four | confirmed by execution | search pending |
| MPL8 | colour mapping | `BoundaryNorm` maps NaN to the "over" colour | bug | NaN → index ncolors (over) in `cmap(norm(x))` and `to_rgba` | all four | confirmed by execution | search pending |
| MPL9 | colour mapping | `LinearSegmentedColormap(gamma≠1).reversed()` applies the gamma to the reversed data, so it is not the original read backwards | bug | up to 0.984 in a channel (gamma=2, N=64) | all four | confirmed by execution | search pending |
| MPL10 | colour mapping | `LinearSegmentedColormap.resampled()` drops gamma | bug | maxdiff 0.490 (gamma=2, 8 entries); new `_gamma` 1.0 | all four | confirmed by execution | search pending |
| MPL11 | correlation | `acorr`/`xcorr` on int16 samples accumulate in int16 | bug | normed=False [22302, −97, −14889, 22590] for [5035415326, 6674972575, 7785006551, 8234555454]; normed=True all NaN (main, 3.11.2) or UFuncTypeError (3.7.1, 3.5.2) | all four | confirmed by execution | search pending |
| MPL12 | correlation | `xcorr`/`acorr(normed=True)` on complex input divides by Σx² rather than Σ\|x\|² | bug | zero-lag value 1.342 − 2.301j instead of 1 | all four | confirmed by execution | search pending |
| MPL13 | spectral | `detrend_linear` fits a conjugated slope to complex data | bug | residual of an exact complex line 33.0 (should be 0); `psd(detrend='linear')` of complex input maxabsdiff 0.3159 on scale 2.319 | all four | confirmed by execution | search pending |
| MPL14 | stackplot | `weighted_wiggle` with integer layers truncates 1/total to 0 | bug | int64 layers give [−2, −2, −4, −7, …] for the float [−2, −1.625, −2.375, −3.764, …] | all four | confirmed by execution (independent of MPL15) | search pending |
| MPL15 | stackplot | `weighted_wiggle` minimises the weighted wiggle of the layers in reverse order (per the m3 notes) | bug (as recorded) | weighted squared midline slopes 84.35 against 13.88 for the minimiser | all four | **re-verification pending** (against Byron & Wattenberg 2008) | search pending |
| MPL16 | spectral | `Axes.specgram` image rows are offset from their frequencies (y extent not padded by half a bin) | bug (display) | row centres up to 0.1923 from `freqs` with df = 0.390625; returned arrays correct | all four | confirmed by execution | search pending |
| MPL17 | spectral | `detrend_linear` of a single value returns NaN | bug (edge case) | `detrend_linear([5.0])` = [nan], should be [0] | all four | confirmed by execution | search pending |
| MPL18 | colour mapping | `BoundaryNorm` with `ncolors` > 32767 overflows its int16 index | bug (extreme parameter) | OverflowError on numpy 2.x; silent [0, −25537, −25536] (drawn "under") on numpy 1.x | all four | confirmed by execution | search pending |
| MPL19 | colour mapping | `SymLogNorm`/symlog give the linear range linscale/(1−1/base) decades, not the documented *linscale* | documentation gap | linear half = 1.1111 decades at linscale=1, base 10 (2.0 at base 2); norm(1) = 0.6786 for 0.6667; maxdiff 0.0119–0.0536 of the colour range | all four (main by reading `scale.py`) | confirmed; plot and colorbar agree | search pending |
| MPL20 | spectral | `scale_by_freq=False` also changes the window normalisation (Σw² → (Σw)²), not only "not dividing by Fs" | documentation gap | Pxx(False)/Pxx(True) = 0.11811 with Hann, NFFT=128, Fs=10 (documented reading: 10) | all four | confirmed by execution | search pending |
| MPL21 | spectral | `specgram` detrends in every mode; its Notes say detrend applies only to mode='psd' | documentation gap | magnitude-mode DC bin 0.0392532 (detrended) where the Notes imply 39.9387 | all four | confirmed by execution | search pending |
| MPL22 | spectral | `mlab.csd` documents Pxy as "real valued" | documentation gap | complex128, max \|imag\| 5.134 | all four | confirmed by execution | search pending |
| MPL23 | spectral | `Axes.psd`/`Axes.csd` with `return_line=True` return a list, documented as a `Line2D` | documentation gap (API) | type, not numbers | all four | confirmed by execution | search pending |
| MPL24 | hist2d | `hist2d(density=True, cmin=…)` thresholds densities, documented as counts | documentation gap | 20 of 20 cells NaN where 1 cell has a count below cmin=14 | all four | confirmed by execution | search pending |
| MPL25 | hexbin | `hexbin(bins=<int>)` puts the minimum count alone in the first class | documentation gap | k=3 on counts 1..77: classes 7/22/5 against 26/4/4 equal-width | all four | confirmed by execution | search pending |
| MPL26 | hexbin | `hexbin(xscale='log').get_offsets()` are not centres in data coordinates | documentation gap (API) | log10(x) (0.0058 for 1.0135) on main/3.11.2; a single [[0, 0]] on 3.7.1/3.5.2; counts correct | all four | confirmed by execution | search pending |
| MPL27 | box plot | `whis` text says "highest datum below" / "lowest datum above"; fences are inclusive | documentation gap | data on both fences: whiskers −2 and 6, no fliers (strict reading: 1 and 3, two fliers) | all four | confirmed by execution | search pending |
| MPL28 | box plot | whisker ends are clamped to Q1/Q3, so a returned `whislo`/`whishi` can be a non-datum | documentation gap | whishi 2.5 (= Q3) where the highest datum inside the fence is 0; whis=0.25: 3.5/8.5 for 4/8 | all four | confirmed by execution | search pending |
| MPL29 | box plot | `whis=(lo, hi)` puts the whiskers at the most extreme data inside the percentiles, not at the percentiles | documentation gap | whis=(5, 95) on 1..20: 2 and 19 for 1.95 and 19.05 | all four | confirmed by execution | search pending |
| MPL30 | colour mapping | `Normalize()` autoscale on an ndarray with NaN sets vmin = vmax = nan (direct calls only) | documentation gap | every value drawn "bad" | all four | confirmed by execution | search pending |
| MPL31 | colour mapping | `imshow` masks ±inf, drawing it transparent instead of over/under | documentation gap | +inf and −inf cells transparent | all four | confirmed by execution | search pending |
| MPL32 | contour | `contourf`: a plateau exactly at `levels[0]` is unfilled when min(Z) < levels[0], against "the lowest interval … includes the lowest value" | documentation gap | plateau in no band; with `extend='min'` drawn in the under colour | all four | confirmed by execution | search pending |
| MPL33 | colour mapping | `Colormap(bytes=True)` truncates rather than rounds | documentation gap | (0.999, 0.7, 0.0019) → (254, 178, 0), nearest (255, 179, 0); 379 of 768 viridis channels 1 low | all four | confirmed by execution | search pending |
| MPL34 | contour | automatic levels are multiples of their step relative to a round offset, not of the step itself ("acceptable tick multiples") | documentation gap | 34 of 300 random ranges, e.g. 13.03, 13.045, 13.06; colours unaffected | all four (main runs 3.11.2's `ticker.py`) | confirmed on 3.11.2 and older | search pending |
| MPL35 | colour mapping | `imshow` with `BoundaryNorm` draws a value exactly on a boundary in the neighbouring colour (old `_make_image` rescaling) | old-release only (bug) | colours [0, 1, 2, 2, 3, 5, 6, 7] for [0 … 7]; 1 ulp below 0.1 in colour 1; colorbar disagrees with the cell | 3.7.1, 3.5.2 | fixed by 3.11.2 (PR not pinned; #28122 candidate) | search pending |
| MPL36 | spectral | `psd(scale_by_freq=False)` normalised by \|window\| | old-release only (bug) | maxabsdiff 0.4505 on scale 1.415 for a window with negative lobes | 3.5.2 | fixed in 3.7.0 (PR #25122, issue #24821) | search pending |
| MPL37 | correlation | `acorr`/`xcorr(normed=True)` raise on any integer array (in-place division) | old-release only (crash) | UFuncTypeError for int64 [3, 1, 4, 1, 5, 9, 2, 6] | 3.7.1, 3.5.2 | passes on 3.11.2 and main | search pending |
| MPL38 | box plot | `boxplot_stats([])` has no `'iqr'` key | old-release only (bug) | KeyError for code reading `stats['iqr']` | 3.5.2 | fixed by 3.7.1 | search pending |
| MPL39 | colour mapping | `LogNorm()` autoscale with NaN in an ndarray raises | old-release only (bug) | ValueError: Invalid vmin or vmax | 3.5.2 | fixed by 3.7.1 | search pending |
| MPL40 | hexbin | `mincnt` documented as "more than"; the `C=None` branch is inclusive | old-release only (documentation) | mincnt=2: 27 cells shown for 26; mincnt=3: 26 for 21 | 3.7.1, 3.5.2 | fixed in 3.8.0 (made consistently inclusive, docstring "at least") | search pending |
| MPL41 | hexbin | `bins='log'` documented as log10(i+1); behaviour is LogNorm (zero counts "bad") since 3.5.0 | old-release only (documentation) | 12 zero-count cells "bad" | 3.7.1, 3.5.2 | current docstring correct | search pending |
| MPL42 | contour | automatic level count documented as "no more than n+1" | old-release only (documentation) | 15 of 348 cases exceed it, e.g. `contourf(Z, 4)` on [0, 10] gives 6 levels | 3.7.1, 3.5.2 | 3.11 docstring says n+2, which holds | search pending |
| MPL43 | pie | pie percentages and angles computed in float32 | old-release only; harness expectation (9-digit formats) | '16.666667163' for '16.666666667'; callable receives 20.000000298023224; rel ~1e-7; rel 1e-6 check passes | 3.7.1, 3.5.2 | float64 on 3.11.2 and main | search pending |

**Summary.** On `main` (= 3.11.2 for every path here): 18 bugs (MPL1–MPL18; 17 present in every build back to 3.5.2,
MPL2 introduced with the 3.11 masked-handling change; MPL15 awaiting re-verification) and 16 documentation gaps
(MPL19–MPL34). Nine more (MPL35–MPL43) exist only in 3.7.1 and/or 3.5.2. The heaviest for the cohort are MPL1 and
MPL7/MPL8 (heatmaps and colour scales, 35 papers), MPL35 on the most-cited version 3.7.1, MPL2/MPL6 (violin / KDE
in 10 papers, box plots in 8), and MPL3 (spectra, 3).

## What held up

**Under execution on all four builds** unless noted: `boxplot_stats` quartiles (H&F-7), IQR, inclusive fences,
whiskers, fliers, the asymptotic notch and the percentile-bootstrap notch (same resamples), autorange, lists / 2-D /
labels / masked input (3.9+); `Axes.boxplot`/`bxp` drawn coordinates; `GaussianKDE` Scott and Silverman factors,
ddof=1 covariance and evaluation against a direct sum to about 1e-15 in 1-D, 2-D and 3-D (and against SciPy);
`violin_stats` grid, KDE, mean / median / min / max / quantiles, NaN and ±inf dropped (3.11+); `violinplot` lines and
body outlines to about 1e-15. `psd`, `csd`, `cohere`, `specgram` (all five modes) and the `*_spectrum` functions
against an explicit-DFT Welch reference to about 1e-13 whenever NFFT and pad_to share parity, Parseval exact,
closed forms (A²/2, A/2, phase), white-noise levels, SciPy agreement, the detrend and window helpers and the Axes
wrappers. `hist` edges, half-open counts, density, weights, cumulative, stacked, multiple datasets, NaN, float32,
int8, 1e9 offsets and drawn geometry; `stairs`; `hist2d` counts, density, weights, range, cmin/cmax on counts;
`hexbin` grid and counts against an exact point-in-drawn-hexagon test, conservation, C reductions, `mincnt` (3.8+),
log scales; `acorr`/`xcorr` on real float input; stackplot 'zero', 'sym', 'wiggle' and thickness preservation;
`pie` percentages (exact on 3.11+, float32 precision before); `errorbar` bars, limits, NaN and `errorevery`. Every
norm (Normalize, LogNorm, SymLogNorm's shape, AsinhNorm, FuncNorm, PowerNorm, TwoSlopeNorm, CenteredNorm,
BoundaryNorm's edge rule and extend, NoNorm) against Fraction or closed forms; Colormap indexing and
under/over/bad; LinearSegmentedColormap against the segmentdata rule; ListedColormap resample/reverse; `imshow`
pixels at 20, 5 and 2 px per cell with offsets to 1e12; colorbar band edges and colours for BoundaryNorm,
Normalize, LogNorm and contourf; contour level spacing, band membership, midpoint colours, `colors=` and `extend`.

**Not checked:** seaborn itself, `pcolormesh`/`scatter` per-artist geometry, non-'nearest' image interpolation,
log-scale contour levels and `tricontourf`, the multivariate colour API (3.10/3.11), rendered pixels beyond the norm
position, datetime input to `hist`, the 32-bit stride path, and the statistical coverage of the bootstrap notch.

## Filing

Nothing is filed. Matplotlib's contribution policy forbids AI-generated issue and pull-request text and AI agents
interacting on the tracker, and a pull request must carry an AI Disclosure section. The upstream kit will therefore
be **fact sheets** — the reproducer, the measured and documented numbers, the file:line on `main`, and the
suggested fix — for the owner to write the issue or PR from in their own words; nothing goes to the tracker from
this session. At most two findings are filed at a time. The order waits for `prior-reports.md` (the parallel
tracker search) and for the MPL15 re-verification; MPL35–MPL43 are fixed in the current release and are not filed.

## Files

| path | what |
|---|---|
| `component-reviews/boxplot-violin-stats.md` | MPL2, MPL6, MPL27–MPL29, MPL38; held-up list (m1) |
| `component-reviews/spectral.md` | MPL3, MPL13, MPL16, MPL17, MPL20–MPL23, MPL36; held-up list (m2) |
| `component-reviews/hist-hexbin-counts.md` | MPL4, MPL5, MPL11, MPL12, MPL14, MPL15, MPL24–MPL26, MPL37, MPL40, MPL41, MPL43; held-up list (m3) |
| `component-reviews/color-mapping.md` | MPL1, MPL7–MPL10, MPL18, MPL19, MPL30–MPL35, MPL39, MPL42; held-up list (m4) |
| `verify/m1_…py` … `m4_…py`, `_synth.py`, `*.out`, `*.v<version>.out`, `*.notes.md` | harnesses, captured output per build, per-FAIL notes |
| `matplotlib_profile.py`, `matplotlib_profiles.jsonl`, `profile_run.log` | cohort profile |
| `prior-reports.md` | tracker search for prior reports (parallel task; fills the "Prior report" column) |
| `README-row.md` | draft row for the top-level README table |
