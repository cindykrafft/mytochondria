# m4_color_mapping: notes

Harness: `audits/matplotlib/verify/m4_color_mapping.py`. Outputs:
- `m4_color_mapping.out`: **main overlay**. This is 3.11.2 with main @ 44f2e00's `cbook.py`, `mlab.py`, `colors.py`, `colorizer.py`, `contour.py`, `stackplot.py` and `axes/_axes.py` copied in. A full build of main is not possible here because its SheenBidi download is blocked. `colors.py` in the overlay is byte-identical to `src/lib/matplotlib/colors.py`. `image.py`, `scale.py`, `ticker.py` and `colorbar.py` are the 3.11.2 copies.
- `.v3.11.2.out`: 3.11.2, numpy 2.5.3, scipy.
- `.v3.7.1.out`: numpy 1.26.4, no scipy.
- `.v3.5.2.out`: numpy 1.23.5, no scipy.

Runtime is 25 to 75 s per build.

Truths:
- `fractions.Fraction` for the linear norms, the TwoSlopeNorm sides, the BoundaryNorm index map, colormap indices and contourf band colours.
- Closed forms (`math.log`, `math.asinh`, `math.sqrt`) for LogNorm, SymLogNorm, AsinhNorm and PowerNorm.
- Plain-Python ports written from the docstrings:
  - BoundaryNorm (left-closed bins, clip, extend, the "linearly interpolating [0, nbins-1] onto [0, ncolors-1]" stretch).
  - The documented `segmentdata` rule for LinearSegmentedColormap ("between x[i] and x[i+1] … linearly interpolated between y1[i] and y0[i+1]", sampled at (i/(N-1))**gamma).
  - SymLogNorm with "linscale … is the number of decades to use for each half of the linear range".
- The colour a reader sees is taken from returned objects:
  - `Colormap.__call__` and `ScalarMappable.to_rgba`.
  - The uint8 RGBA array returned by `AxesImage.make_image` (one row of cells, sampled at the cell centres; 20, 5 and 2 px per cell).
  - Colorbar `QuadMesh` coordinates and facecolors.
  - Contour `Path` vertices, `Path.contains_point` and facecolors.
- The ListedColormaps use byte-exact colours, so an index can be identified exactly.

Expectations that depend on the version:
- PowerNorm below vmin: before 3.9, values below vmin map to 0 (api_changes_3.9.0 "PowerNorm no longer clips values below vmin").
- TwoSlopeNorm autoscale: before 3.8 it clips at vcenter (api_changes_3.8.0 "TwoSlopeNorm now auto-expands to always have two slopes").
- The contour level-count promise is read from each build's own `Axes.contour` docstring: "n+1" on 3.5.2/3.7.1, "n+2" on 3.11.
- AsinhNorm (3.6+) is an information line on 3.5.2.
- `resampled()` (3.6+) is replaced by the same-code `_resample()` on 3.5.2.

## Counts

| build | ok | FAIL |
|---|---|---|
| main overlay (44f2e00 colors/colorizer/contour on 3.11.2) | 190 | 18 |
| 3.11.2 | 190 | 18 |
| 3.7.1 | 187 | 21 |
| 3.5.2 | 182 | 22 |

The 18 FAIL lines are the same on every build. 3.7.1 adds the imshow edge-value bug (2 lines) and the old "n+1" contour wording (1 line). 3.5.2 adds the same three plus LogNorm autoscale with NaN (1 line). Several lines share a root cause. There are 13 distinct issues: 11 on main, 2 that exist only in old builds.

## FAIL lines

### 1. `Normalize()` autoscale with NaN in a plain ndarray (all builds)
**Measured:** `Normalize()(np.array([3., nan, 7.]))` sets vmin = vmax = nan, and every output is NaN, so every value gets the "bad" colour.

**In the code:** `colors.py:Normalize.autoscale_None` (2606/2608: `self.vmin = A.min()`, `self.vmax = A.max()`) takes the NaN-propagating min/max.

**Documentation:** "If either *vmin* or *vmax* is not provided, they default to the minimum and maximum values of the input."

`imshow`, `pcolormesh` and `scatter` are not affected, because they mask non-finite values first (`cbook.safe_masked_invalid`). The problem appears only when a norm is called directly (`cmap(norm(data))`). LogNorm and the other scale-based norms are not affected, because they autoscale on finite transformed values only, except on 3.5.2 (FAIL 13).

**Verdict:** documentation gap / sharp edge. Present on all builds.

### 2–5. SymLogNorm does not use the documented *linscale* (all builds)
**Measured:** the four parameter sets differ from the documented definition by 0.012, 0.054, 0.019 and 0.032 of the colour range.
- linthresh=1, linscale=1, base=10, vmin=-100, vmax=100: `norm(1) = 0.6786`. The documented definition gives 0.6667.
- The colour range used by the linear half (0..linthresh) is 1.111 decades for base 10. For base 2 it is 2.0 decades, for linscale=2 it is 2.222 decades, and for linscale=0.5 with base e it is 0.791 decades.

**In the code:** `scale.py:SymmetricalLogTransform.transform_non_affine` (508: `linscale_adj = self.linscale / (1.0 - 1.0 / self.base)`) scales the linear part by linscale/(1-1/base), not by linscale.

**Documentation:** the SymLogNorm docstring (colors.py:3066-3071), the SymmetricalLogScale docstring (scale.py:602-608) and the colormapnorms tutorial all say: "Its value is the number of decades to use for each half of the linear range. For example, when *linscale* == 1.0 (the default), the space used for the positive and negative halves of the linear range will be equal to one decade". The symlog demo says "the ratio of visual space of the region (0, linthresh) relative to one decade".

The colorbar uses the same transform, so a plot agrees with its own colorbar. A reader who reasons from the documented parameter gets a different mapping.

**Verdict:** documentation/implementation mismatch. The documented meaning of *linscale* is wrong by the factor 1/(1-1/base): 1.11 for base 10 and 2 for base 2. It is not a wrong-colour bug inside a plot. Present on all builds; 3.5.2/3.7.1 have the same factor in `_linscale_adj`.

### 6–7. BoundaryNorm with more colours than bins skips the last colour (all builds)
**Measured:** `BoundaryNorm(boundaries, ncolors)` with ncolors > number of bins. With `bins+1` boundaries:
- In 266 of the (ncolors, bins) pairs with 2 ≤ ncolors < 200 and 2 ≤ bins < 60, at least one bin gets a colour index one below the documented linear map.
- In 233 of those pairs it is the **last** bin. That bin gets `ncolors-2` and never `ncolors-1`.
- Examples: 12 bins with 16 colours → top bin 14, not 15. 26 bins with 256 colours → top bin 254. 51 bins with 256 → 254.

**In the code:** `colors.py:BoundaryNorm.__call__` computes `iret = (self.Ncmap - 1) / (self._n_regions - 1) * iret` (3317) and then truncates with `iret = iret.astype(np.int16)` (3319). For example, (15/11)*11 = 14.999999999999998 is truncated to 14. The exact value is an integer, so floor, round or any other rule gives 15.

**Documentation:** the Notes say: "the color index is chosen by linearly interpolating the ``[0, nbins - 1]`` range onto the ``[0, ncolors - 1]`` range". The code comment says the last region "is mapped to the last color".

The colorbar is drawn from the same norm, so it shows the same (wrong) colour. With a short ListedColormap (12 bins over a 16-colour map) the top bin is drawn in a visibly different colour than intended, and the last colour of the map is never used.

**Verdict:** bug (a wrong index compared with the documented definition; float truncation). The fix is to round, or to compute `(Ncmap-1)*iret // (n_regions-1)` in integers. Present on all builds.

### 8, 15. BoundaryNorm maps NaN to the "over" colour (all builds)
**Measured:**
- `cmap(BoundaryNorm([0, 1, 2.5, 4, 10], 4)(np.array([0.5, nan, 3.])))` gives the last colour for NaN, at index 4 = ncolors, which is "over".
- `ScalarMappable(norm=BoundaryNorm, cmap).to_rgba(np.array([0.5, nan, 3.5]))` gives the over colour (9), not bad (10).

**In the code:** `BoundaryNorm.__call__` masks only masked entries. `np.digitize(nan, boundaries)` returns `len(boundaries)` (3304). The NaN fails both `xx < vmin` and `xx >= vmax`, so it keeps that index. Normalize keeps NaN as NaN, which the colormap turns into "bad".

**Documentation:** the Colormap docstring says `bad`: "The color for invalid values (NaN or masked)".

Plotting functions mask NaN before the norm sees it. The public `ScalarMappable.to_rgba` path and `cmap(norm(x))` do not.

**Verdict:** bug (NaN drawn as an over-range value). Present on all builds.

### 9. BoundaryNorm with `ncolors` > 32767 (all builds)
**Measured:** `BoundaryNorm(np.arange(41), 40000)([0.5, 39.5, 41.])`.
- numpy 2.x (main, 3.11.2): raises `OverflowError`.
- numpy 1.x (3.7.1, 3.5.2): silently returns `[0, -25537, -25536]`. Those are negative indices, so the colours become "under".

**In the code:** `iret.astype(np.int16)` (3319) and `iret[xx >= self.vmax] = max_col` (3321).

**Documentation:** the docstring says "returns integers or arrays of int16". It sets no upper limit on *ncolors* ("Number of colors in the colormap to be used").

**Verdict:** bug at an extreme parameter (silent wraparound on numpy 1.x, crash on 2.x). It is rare in practice, because a colormap needs more than 32767 entries. Present on all builds.

### 10, 14. Colormap ignores NaN inside a masked array that has a masked element (all builds)
**Measured:**
- `cmap(np.ma.array([0.1, nan, 0.5], mask=[0, 0, 1]))` draws the unmasked NaN in the **first** colour on main/3.11.2, and in the **under** colour on 3.7.1/3.5.2, instead of "bad".
- `ScalarMappable.to_rgba` with Normalize shows the same (FAIL 14: index 7 → colour 0 or 8).
- If the masked array has no masked element, NaN is "bad" correctly (ok line).

**In the code:** `colors.py:Colormap._get_rgba_and_mask` (832: `mask_bad = X.mask if np.ma.is_masked(X) else np.isnan(xa)`) uses either the mask or the NaN test, never both. The NaN then goes through `xa.astype(int)` (835) and becomes INT_MIN. `take(..., mode='clip')` turns that into index 0.

**Documentation:** "bad: The color for invalid values (NaN or masked)".

Plotting functions mask NaN themselves (`safe_masked_invalid`), so `imshow` is fine. Code that builds a masked array and calls the colormap or `to_rgba` is not.

**Verdict:** bug (wrong colour for NaN). Present on all builds.

### 11. `bytes=True` truncates instead of rounding (all builds)
**Measured:** a colour (0.999, 0.7, 0.0019) gives bytes (254, 178, 0). The nearest bytes are (255, 179, 0), and `to_hex` of the same colour is `#ffb200`. For viridis, 379 of the 768 channels come out 1 below the nearest byte.

**In the code:** `colors.py:Colormap._get_rgba_and_mask` (842: `lut = (lut * 255).astype(np.uint8)`). Colours given as 8-bit hex round-trip exactly (ok line).

**Documentation:** "otherwise they will be `numpy.uint8`\s in the interval ``[0, 255]``". No rounding rule is given. `to_hex` rounds.

**Verdict:** documentation gap. The error is at most 1/255 per channel and not visible. Present on all builds.

### 12. `LinearSegmentedColormap(gamma≠1).reversed()` is not the original read backwards (all builds)
**Measured:** for the docstring's example segmentdata with gamma=2 and N=64, `reversed()(i)` differs from `original(N-1-i)` by up to 0.984 in a channel. The reversed map equals f(1 - (i/(N-1))**2), to 5e-16: the gamma warp is applied to the already reversed data, so the warp sits at the other end.

**In the code:** `colors.py:LinearSegmentedColormap.reversed` (1291: `LinearSegmentedColormap(name, data_r, self.N, self._gamma)`) passes the same gamma with the mirrored data.

**Documentation:** "Return a reversed instance of the Colormap." With gamma=1 the reversed map is the exact mirror (ok line).

**Verdict:** bug for gamma ≠ 1. A `*_r` map built from a gamma-corrected map shows different colours for the same data than the original read backwards. Present on all builds.

### 13. `LinearSegmentedColormap.resampled()` drops gamma (all builds)
**Measured:** `LinearSegmentedColormap(cdict, gamma=2).resampled(8)` gives entries f(i/7) instead of f((i/7)**2) (maxdiff 0.49). The new map has `_gamma = 1.0`.

**In the code:** `colors.py:LinearSegmentedColormap.resampled` (1255: `LinearSegmentedColormap(self.name, self._segmentdata, lutsize)`) does not pass gamma. Under, over and bad are carried over.

**Documentation:** "Return a new colormap with *lutsize* entries."

`plt.get_cmap(name, lut)` and `contourf`/`BoundaryNorm` workflows that resample a user's gamma-corrected map therefore change its colours.

**Verdict:** bug. Present on all builds; 3.5.2 has the same code as `_resample`.

### 16. `imshow`: ±inf cells are drawn transparent, not in the over/under colour (all builds)
**Measured:** `imshow([[1, nan, 3, inf, -inf, masked]], vmin=0, vmax=8)` makes the +inf and -inf cells transparent ("bad"), like NaN. `Colormap`/`Normalize` called directly map +inf to "over" and -inf to "under" (ok line).

**In the code:** `cbook.safe_masked_invalid` (719: `np.ma.masked_where(~(np.isfinite(x)), x)`), used by `image._normalize_image_array` and `Colorizer.set_array`, masks all non-finite values.

**Documentation:** the Colormap docstring says `bad` is "The color for invalid values (NaN or masked)", and `over` is "The color for high out-of-range values". No plotting docstring says that ±inf counts as invalid.

**Verdict:** documentation gap. Masking ±inf is defensible, but it is undocumented, and an infinite value disappears instead of saturating. Present on all builds.

### 17. Automatic contour levels are not multiples of their step when the data span is small compared with their magnitude (all builds)
**Measured:** 34 of 300 random ranges. In every case the step mantissa is 1.5, 3 or 6, and the data sit far from 0 relative to their span. Examples:
- Z near -1e4: -10000, -9985, -9970 (step 15).
- Z near 1e6: 999850, 1000000, 1000150 (step 150).
- Z in about [13.03, 13.1]: 13.03, 13.045, 13.06 (step 0.015).
- 17.338, 17.344, … (step 0.006).

The levels are evenly spaced (ok line), but they are not integer multiples of the step. For example, 13.045/0.015 = 869.67.

**In the code:** `ticker.py:MaxNLocator._raw_ticks` (2268: `scale, offset = scale_range(vmin, vmax, nbins)`, 2305: `best_vmin = (_vmin // step) * step`) puts the ticks on a grid anchored at a round offset, not at 0.

**Documentation:** the MaxNLocator *steps* docstring says: "Sequence of acceptable tick multiples … ``20, 40, 60`` … would be possible sets of ticks because they are multiples of 2".

**Verdict:** documentation gap. The levels are multiples of the step relative to a round offset. For mantissas 1, 2, 2.5 and 5 that grid coincides with absolute multiples; for 1.5, 3 and 6 it does not. This is harmless for the colours. Present on all builds.

### 18. contourf: a plateau exactly at `levels[0]` is unfilled when `min(Z) < levels[0]` (all builds)
**Measured:** Z is 0 on a plateau, -1 on one edge and 2 on another, with levels [0, 1, 2]. The plateau point is in no filled band. With `extend='min'` it falls in the **under** band and is drawn in the under colour. When `min(Z) == levels[0]` the plateau is filled in the lowest band (ok line).

**In the code:** `contour.py:ContourSet._get_lowers_and_uppers` (956: `if self.zmin == lowers[0]:` lowers the first boundary) closes the lowest interval only when the data minimum equals the first level. Otherwise contourpy's `lower < Z <= upper` excludes Z == levels[0].

**Documentation:** the contour Notes (contour.py:1735-1741) say: "contourf fills intervals that are closed at the top; that is, for boundaries z1 and z2, the filled region is z1 < Z <= z2 except for the lowest interval, which is closed on both sides (i.e. it includes the lowest value)."

**Verdict:** documentation ambiguity / gap. "The lowest value" is honoured only when it is also the data minimum. A field that sits exactly on `levels[0]` (for example 0 with some negative values elsewhere) is left blank, or drawn as "under" with `extend='min'`. Present on all builds.

### 19–20. 3.5.2 and 3.7.1 only: imshow draws a value exactly on a BoundaryNorm boundary in the wrong colour
**Measured:**
- Boundaries are [0, 0.1, 0.2, 0.3, 0.7, 1.1, 1.3, 2.9, 3.0] with 8 colours, and each cell holds a boundary value.
- The image array `make_image` returns gives colours [0, 1, 2, **2**, **3**, 5, 6, 7] for the values 0 … 2.9, at both 20 px and 2 px per cell. The documented colours are [0, 1, 2, 3, 4, 5, 6, 7].
- The value one ulp below 0.1 is drawn in colour **1**; it should be 0.
- `im.to_rgba(data)` gives the correct colours on the same build, so the error comes from `_make_image`. Old `image.py:_make_image` rescales the data into [0.1, 0.9] before resampling and scales it back afterwards (`A_scaled -= a_min`, `/= ((a_max - a_min) / frac)`, `+= offset`). The round trip moves values off exact boundaries.
- The same data shifted by +1000 happened to come out right.

**Documentation:** the BoundaryNorm docstring says "Bins are left-closed and right-open; i.e., the n-th bin is ``boundaries[n] <= value < boundaries[n + 1]``". The main/3.11.2 `_make_image` has no such rescaling, and all those lines pass there. The fix is in the 3.10/3.11 image rework. The exact PR was not pinned; 3.10.0's "#28122 Disable clipping in Agg resamplers" is a candidate.

**Verdict:** bug in the cohort's most-cited version 3.7.1, and in 3.5.2: a heatmap cell whose value sits on a level boundary is drawn in the neighbouring class's colour, and the colorbar disagrees with the cell. Fixed in 3.11.2.

### 21. 3.5.2 and 3.7.1 only: automatic contour level count exceeds the documented "n+1"
**Measured:** 15 cases out of 348. Examples: `contourf(Z, 1)` with Z in [0, 10] gives 3 levels. `contourf(Z, 4)` on [0, 10] gives 0, 2, …, 10, which is 6 levels, all inside the data range.

**In the code:** `contour.py` uses `MaxNLocator(N + 1)`, which allows up to N+2 levels inside the limits.

**Documentation:** the 3.5.2/3.7.1 docstring says: "tries to automatically choose no more than *n+1* 'nice' contour levels between minimum and maximum". The 3.11 docstring says *n+2*, and that holds on 3.11.2 and main (ok line).

On every build the total number of levels returned, including the one just below min(Z) and the one just above max(Z), reaches n+3 in 93 of 300 random ranges. This is recorded as an information line.

**Verdict:** documentation error in the old releases, corrected later. The colours are unaffected.

### 22. 3.5.2 only: `LogNorm()` autoscale with NaN in a plain ndarray raises
**Measured:** `LogNorm()(np.array([nan, 1, 10, 100]))` raises `ValueError: Invalid vmin or vmax`.

**In the code:** 3.5.2 `LogNorm.autoscale_None` masks only `A <= 0`, so vmin becomes nan. 3.7.1 and later autoscale on finite transformed values (`np.extract(np.isfinite(self._trf.transform(A)), A)`, colors.py:2982) and pass.

**Verdict:** bug in 3.5.2, fixed by 3.7.1. Plotting functions mask NaN first, so only direct calls are affected.

## Information lines (not FAIL)
- contourf colours each band by its layer midpoint, as the `_process_colors` docstring says. With unequal levels [0, 1, 2.5, 6, 10] and 4 listed colours, bands 0 and 1 both get colour 0 and colour 2 is never used. This is checked against the Fraction port (ok), but a reader cannot tell those two bands apart, neither in the plot nor on the colorbar.
- PowerNorm below vmin gives 0 on 3.5.2/3.7.1, so it is drawn in the lowest colour, not the under colour. On 3.11 the value is negative, so it is drawn "under". Both are as documented for their versions.
- TwoSlopeNorm before 3.8 clips the autoscaled range at vcenter, and the expectation follows that.
- `LogNorm(clip=True)` maps negative values to 0, the lowest colour, not to bad. This follows the clip documentation ("below vmin → 0").
- A discontinuous segmentdata sampled exactly at a jump returns y0, the value approached from the left. The docs do not define this point.
- `contourf` of a constant field returns 8 levels within 1e-12 of the constant.

## What held up (all builds unless noted)
- **Normalize:**
  - The documented example, with and without clip.
  - 400 random (v - vmin)/(vmax - vmin) values against Fraction, with a maximum error of 1.1e-16.
  - vmin == vmax maps to 0. vmin > vmax raises ValueError.
  - Autoscale on lists and on masked arrays ignores masked values. The mask is preserved. NaN stays NaN when vmin/vmax are given.
  - `inverse` round-trips, and an unscaled inverse raises.
  - The dtype rules in `process_value` hold for int8/int16/uint8 → float32, int32/int64 → float64, and float32/float64 preserved.
  - Large offsets are exact: 1e6 + k in float64 and float32, and int64 2**40 + k.
  - ±inf maps to ±inf.
- **LogNorm:**
  - The closed form holds, including values out of range.
  - Non-positive values are masked.
  - Autoscale ignores non-positive, NaN and masked values (NaN: 3.7.1+).
  - clip, inverse, and vmin == vmax all behave as documented.
- **SymLogNorm:** linear inside ±linthresh; equal steps per factor of base; antisymmetric for vmin = -vmax; inverse round-trips; clip works.
- **AsinhNorm** (3.6+) matches the documented a0·asinh(a/a0) for three widths, and inverse round-trips.
- **FuncNorm:** values, inverse and autoscale.
- **PowerNorm:** the Notes formula for gamma 2 and 0.5; above vmax; below vmin (version-aware); clip; inverse; masked autoscale; vmin == vmax.
- **TwoSlopeNorm:**
  - The documented example.
  - 200 random two-sided values against Fraction.
  - Out-of-range values give ±inf, so they are drawn under/over.
  - Autoscale expansion (3.8+) and clipping (before 3.8).
  - Ordering validation, the mask, and inverse.
- **CenteredNorm:** the documented example; the autoscale halfrange, including with masked values; clip; changing vcenter keeps halfrange.
- **BoundaryNorm:**
  - Values exactly on boundaries go to the upper bin (left-closed), for ncolors 4/5/7/16/256.
  - extend='min'/'max'/'both' with 6, 9 and 256 colours.
  - clip=True, with ncolors equal to the bins and with ncolors greater than the bins.
  - A single bin maps to the middle colour.
  - The three documented ValueErrors are raised.
  - The mask is preserved, and a scalar input returns a Python int.
- **NoNorm:** values pass through unchanged, and integers index the colormap directly.
- **Colormap:**
  - floor(x·N) with x == 1 → N-1, for N = 1, 2, 5, 8 and 256, both at band edges (dyadic N) and inside bands.
  - Out-of-range values: -1e-300 → under, -0.0 → first, 1+ulp → over, ±inf → over/under, NaN → bad.
  - `with_extremes` sets under, over and bad. A masked value → bad.
  - int64 and uint8 indices, with N and above → over and -1 → under. float32 input works.
  - `alpha=` sets alpha, and a bad colour stays transparent.
  - A scalar input returns a tuple.
  - Hex colours round-trip exactly through `bytes=True`.
  - viridis maps 0, 0.5 and 1 to `colors[0]`, `colors[128]` and `colors[255]`.
- **LinearSegmentedColormap:**
  - Matches the documented segmentdata rule exactly (maxdiff < 1e-12) for the docstring example and for a discontinuous map, with N = 2, 5, 11, 256 and gamma 1, 2, 0.5.
  - `from_list` with evenly spaced colours and with (value, colour) anchors.
  - `reversed()` with gamma 1, and under/over are swapped on reversal.
  - `resampled()` with gamma 1.
- **ListedColormap:** `resampled(k)` samples the original at j/(k-1), and keeps under/over/bad. `reversed()` reverses the colours, swaps under/over and keeps bad.
- **End to end:**
  - `ScalarMappable.to_rgba` follows the left-closed edge rule; vmax → last colour.
  - imshow `make_image` pixels, with Normalize(vmin, vmin+8) and 8 colours: values exactly on colour edges land in the upper band, vmax in the last colour, and out-of-range cells in under/over. This holds for float64 and float32, offsets 0, 1e6, 1024 (float32) and 1e12, at 20, 5 and 2 px per cell. On main/3.11 the same holds for BoundaryNorm values exactly on non-dyadic boundaries and one ulp below them, at offsets 0 and 1000.
  - NaN and masked cells are transparent.
- **Colorbar:**
  - With BoundaryNorm, the band edges equal the boundaries, each band has the documented colour of its bin, and the ticks sit at the boundaries. This also holds with 256 colours and extend='both' (stretched indices).
  - With Normalize and 5 colours, the band edges are vmin + k(vmax-vmin)/N, and every band's colour equals the data colour for values in that band.
  - With LogNorm, the band edges are at the decades.
  - With contourf, the band edges equal the levels and the band colours equal the filled bands.
- **contour/contourf:**
  - Automatic levels span the data, are evenly spaced, and stay within the documented count on 3.11. NaN in Z is ignored for the levels.
  - extend='both' moves the trimmed levels inside the data.
  - Bands on a ramp cover exactly [l_i, l_{i+1}].
  - "z1 < Z <= z2": a plateau on an interior level belongs to the lower band, and a plateau on the top level belongs to the top band. The lowest interval is closed when min(Z) == levels[0].
  - Band colours follow the midpoint rule.
  - A 5-colour map over 5 equal bands gives colour i to band i.
  - `colors=` cycles through the colours in order.
  - extend='both' uses the under/over colours, and the extension bands cover the right x-ranges. extend='neither' leaves the outside unfilled.
  - With `colors=`, len == bands + 2 and extend='both', the first and last colours are used for under and over.
  - Line contour colours equal Normalize(levels[0], levels[-1]) of the level.

## Not checked, and why
- `MultiNorm`, `MultivarColormap`, `BivarColormap`: multivariate API added in 3.10/3.11, outside the cohort's versions and outside the heatmap question here.
- Non-'nearest' image interpolation (e.g. 'bilinear', 'antialiased'): the blended colours have no closed-form truth without porting Agg's filters. Only 'nearest' cell centres were judged.
- `pcolormesh`/`pcolor`/`scatter` colour paths: they use the same `Colorizer.to_rgba` (checked) after `safe_masked_invalid`. The per-artist geometry was not re-checked.
- Log-scale contour levels (`LogLocator` with `locator=` or LogNorm), and `tricontourf`: not reached in the time budget. The fill rule is the same contourpy call.
- The colours of the colorbar extend triangles: only the band colours inside the colorbar were checked.
- `LightSource` shading, `rgb_to_hsv`/`hsv_to_rgb`, and `to_rgba` string parsing: colour-space conversions, not data-to-colour mapping.
- MaxNLocator's default `steps` (1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10) are not stated in its docstring. Which step gets chosen is therefore recorded, not judged.
- Main is an overlay. `scale.py` (the SymLogNorm transform), `image.py` (`_make_image`), `ticker.py` and `colorbar.py` run as their 3.11.2 copies on the "main" build. I read the `src` copies of `scale.py` (lines 507-520) and `cbook.safe_masked_invalid` on 44f2e00, and they contain the same code that causes FAILs 2–5 and 16.
