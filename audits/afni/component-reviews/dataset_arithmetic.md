# Component: dataset arithmetic & summary statistics
`3dcalc`/`parser.f`, `3dTstat`, `3dROIstats`, `3dmaskave`, `3dBrickStat`, `edt_coerce.c`

AF7 CONFIRMED, numerically reproduced. `src/3dROIstats.c:1183, 1195`:
   `voxels[i]/(voxels[i]-1)` in `long` arithmetic equals 1 for every N >= 2, so the
   Bessel correction is a no-op and the reported per-ROI SD is the population SD,
   not the intended sample SD.
   Impact: every published ROI SD from `-sigma`/`-nzsigma` is biased low by
   sqrt((N-1)/N) -- -5.1% at N=10, -29% at N=2 -- and inconsistent with
   `3dmaskave -sigma`, which is correct.

AF8 CONFIRMED. `src/parser.f:1062-1065`: for |x| >= 1 the expression parser leaves
   the value untouched, so `atanh(1) = 1`. The same holds for `asin`, `acos`,
   `acosh`. A deliberate anti-NaN design, but undocumented.
   Impact: Fisher r->z via `3dcalc -expr 'atanh(a)'` is a standard connectivity step;
   voxels at r = +/-1 (the seed voxel itself, or short-scaled correlation data
   hitting +/-1.0 exactly) get z = +/-1.0 instead of a large value -- silently
   underestimated, then folded into group statistics.

AF12 CONFIRMED (3dTstat cluster). `src/3dTstat.c`:
   - `:1114` `-DW`: the Durbin-Watson denominator is seeded with the raw first
     sample (`den = ts[0]^2`, undetrended); with fMRI baselines around 1000 the
     statistic collapses toward 0 regardless of actual autocorrelation, so published
     `-DW` values on non-demeaned data are essentially meaningless.
   - `:863-880` `-tdiff`: `get_linear_trend` returns (intercept-at-0,
     slope-per-index) but the removal formula expects (mean, slope-per-second): the
     wrong line is subtracted, `-tdiff -slope` is unit-inconsistent with plain
     `-slope`, and `-tdiff -mean` reports an intercept, not a mean.
   - `:1228-1231` `-nzmean`: the guard tests `npts` instead of `nzpts`, so all-zero
     voxels write 0.0/0 = NaN outside the mask and silently poison downstream sums.
   - `:796` a `char tmpstr[25]` label buffer can be overrun by long method names
     (stack smash, labels/UB only; later widened upstream, confirming the defect).

AF13 CONFIRMED. `src/3dBrickStat.c`:
   - `:496-501, 725-731` with `-automask` the voxel loop stops at linear index =
     number-of-mask-voxels, silently dropping roughly the upper half of the brain in
     storage order for `-mean/-sum/-var/-stdev/-min/-max`. Percentiles are safe.
   - `:798` `-absolute` applies integer `abs()` to a double, truncating magnitudes
     before the statistics -- the mean |r| of a correlation map comes out about 0.

AF20 CONFIRMED. `src/3dmaskave.c:679, 741, 802` and `src/mri_percents.c:739-743,
   968-971`: `-perc 100` reads one past the sorted array, and `-perc 50` returns the
   upper middle order statistic while `-median` averages the two middles, despite the
   help equating them. The same one-past-end interpolation exists in `mri_quantile`.

AF21 CONFIRMED. `src/edt_coerce.c:55`: RGB->gray weights blue 0.144 instead of 0.114
   and multiplies the 0-255 result by 255 again (gray values to ~65,790). Rare in
   quantitative fMRI, and inconsistent with the correct RGB->gray paths elsewhere.

CONVENTIONS worth knowing (checked, deliberate, but they move numbers): AFNI's FDR
q-values are adaptively scaled below textbook Benjamini-Hochberg, up to ~4x, via an
m0/m estimate (`AFNI_DONT_ADJUST_FDR=YES` disables); the gamma-stat "SCALE" aux
parameter is really a *rate*, per cdflib's convention; `3dBrickStat`'s median is
nearest-rank while 3dTstat/3dROIstats/3dmaskave/3dcalc average the two middles;
detrended `-sigma`/`-tsnr` in 3dTstat divides by N-1 despite removing 2 DOF;
`THD_pval_to_stat` returns the p-value itself when stat-aux data is missing.

VERIFIED CORRECT: the median/percentile core (`qmed_float` fuzz-tested, 0
mismatches) and datum-conversion rounding.
