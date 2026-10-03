# Component: data-to-colour mapping (norms, colormaps, `ScalarMappable` / `imshow` pixels, colorbar bands, `contour` / `contourf` levels and fills)

Harness `verify/m4_color_mapping.py`, notes `verify/m4_color_mapping.notes.md`. Executed on four builds: the **main
overlay** (matplotlib 3.11.2 with `cbook.py`, `mlab.py`, `colors.py`, `colorizer.py`, `contour.py`, `stackplot.py`
and `axes/_axes.py` from `main` @ 44f2e00 copied in; `colors.py` is byte-identical to the source tree; `image.py`,
`scale.py`, `ticker.py` and `colorbar.py` are the 3.11.2 copies; a full build of `main` is blocked because its
SheenBidi download is refused here), **3.11.2** (numpy 2.5.3, scipy), **3.7.1** (numpy 1.26.4, no scipy) and
**3.5.2** (numpy 1.23.5, no scipy). 25 to 75 s per build. For the non-overlaid files, the source copies on 44f2e00
of `scale.py` (lines 507–520) and `cbook.safe_masked_invalid` were read and contain the code behind MPL19 and
MPL31. File:line citations are as the notes give them (44f2e00 for the overlaid files).

Cohort: heatmaps / colormaps / colour scales are named in 35 papers, contours in 5, log / symlog scales in 4 (lower
bounds from the survey cache) — the largest plot-type signal in the profile. Prior reports for every finding:
see `../prior-reports.md` (tracker searched 2026-10-03; one line per finding in the README table).

## Truths

- `fractions.Fraction` for the linear norms, the TwoSlopeNorm sides, the BoundaryNorm index map, colormap indices
  and contourf band colours.
- Closed forms (`math.log`, `math.asinh`, `math.sqrt`) for LogNorm, SymLogNorm, AsinhNorm and PowerNorm.
- Plain-Python ports from the docstrings: BoundaryNorm (left-closed bins, clip, extend, the "linearly interpolating
  [0, nbins-1] onto [0, ncolors-1]" stretch); the `segmentdata` rule for LinearSegmentedColormap sampled at
  (i/(N−1))**gamma; SymLogNorm with "linscale … is the number of decades to use for each half of the linear range".
- The colour a reader sees, taken from returned objects: `Colormap.__call__`, `ScalarMappable.to_rgba`, the uint8
  RGBA array from `AxesImage.make_image` (one row of cells sampled at cell centres; 20, 5 and 2 px per cell),
  colorbar `QuadMesh` coordinates and facecolors, contour `Path` vertices, `contains_point` and facecolors.
  ListedColormaps use byte-exact colours, so an index is identified exactly.

Version-dependent expectations: PowerNorm below vmin maps to 0 before 3.9; TwoSlopeNorm autoscale clips at vcenter
before 3.8; the contour level-count promise is read from each build's own docstring ("n+1" on 3.5.2/3.7.1, "n+2"
on 3.11); AsinhNorm (3.6+) is information on 3.5.2; `resampled()` (3.6+) is replaced by the same-code
`_resample()` on 3.5.2.

## Counts

| build | ok | FAIL |
|---|---|---|
| main overlay (44f2e00 colors/colorizer/contour on 3.11.2) | 190 | 18 |
| 3.11.2 | 190 | 18 |
| 3.7.1 | 187 | 21 |
| 3.5.2 | 182 | 22 |

The same 18 FAIL lines fail on every build (on numpy 1.x MPL18 shows a wraparound instead of an OverflowError).
3.7.1 adds MPL35 (2 lines) and MPL42 (1 line); 3.5.2 adds the same three plus MPL39 (1 line). The 18 on main:
MPL30 1, MPL19 4, MPL1 2, MPL8 2, MPL18 1, MPL7 2, MPL33 1, MPL9 1, MPL10 1, MPL31 1, MPL34 1, MPL32 1. (Notes
FAIL numbers are given in each heading.)

## Findings

### MPL1 (FAIL 6–7) — `BoundaryNorm` with more colours than bins skips the last colour (bug; all builds)

**Measured.** `BoundaryNorm(boundaries, ncolors)` with ncolors > bins, over 2 ≤ ncolors < 200 and 2 ≤ bins < 60:
in 266 of the (ncolors, bins) pairs at least one bin gets a colour index one below the documented linear map; in
233 pairs it is the **last** bin, which gets `ncolors-2` and never `ncolors-1`. Examples: 12 bins over 16 colours
→ top bin 14, not 15; 26 bins over 256 colours → 254, not 255; (27, 24) → 25; (30, 26) → 28.

**Cause.** `colors.py:BoundaryNorm.__call__`: `iret = (self.Ncmap - 1) / (self._n_regions - 1) * iret` (3317),
then `iret = iret.astype(np.int16)` (3319). (15/11)·11 = 14.999999999999998 truncates to 14; the exact value is an
integer, so floor, round or any other rule gives 15. Fix: round, or `(Ncmap-1)*iret // (n_regions-1)` in integers.

**Documentation.** Notes: "the color index is chosen by linearly interpolating the ``[0, nbins - 1]`` range onto
the ``[0, ncolors - 1]`` range"; the code comment says the last region "is mapped to the last color".

**Verdict.** The colorbar is drawn from the same norm and shows the same wrong colour, so plot and colorbar agree
with each other but not with the definition. With a short ListedColormap (12 bins over 16 colours) the top bin is
visibly a different colour than intended, and the last colour of the map is never used.

### MPL7 (FAIL 10, 14) — a NaN inside a masked array that has a masked element is drawn in a data colour, not "bad" (bug; all builds)

**Measured.** `cmap(np.ma.array([0.1, nan, 0.5], mask=[0, 0, 1]))`: the unmasked NaN gets colour 0 (the **first**
colour) on main/3.11.2 and colour 8 (**under**) on 3.7.1/3.5.2, instead of bad (10). `ScalarMappable.to_rgba` with
Normalize(0, 8) and 8 colours shows the same at index 7: got [0, 0, 1, 7, 7, 9, 8, **0**, 10] on main/3.11.2,
[0, 0, 1, 7, 7, 9, 8, **8**, 10] on 3.7.1/3.5.2. With no masked element, NaN is "bad" correctly (ok line).

**Cause.** `colors.py:Colormap._get_rgba_and_mask` (832: `mask_bad = X.mask if np.ma.is_masked(X) else
np.isnan(xa)`) uses either the mask or the NaN test, never both; the NaN goes through `xa.astype(int)` (835) to
INT_MIN, and `take(..., mode='clip')` makes it index 0.

**Documentation.** "bad: The color for invalid values (NaN or masked)". Plotting functions mask NaN themselves
(`safe_masked_invalid`), so `imshow` is fine; code that builds a masked array and calls the colormap or `to_rgba`
is not.

### MPL8 (FAIL 8, 15) — `BoundaryNorm` maps NaN to the "over" colour (bug; all builds)

**Measured.** `cmap(BoundaryNorm([0, 1, 2.5, 4, 10], 4)(np.array([0.5, nan, 3.])))` gives NaN index 4 = ncolors
("over"; RGBA (1.0, 1.0, 0.0, 1.0) in the harness map). `ScalarMappable(norm=BoundaryNorm, cmap).to_rgba([0.5, nan,
3.5])` gives [0, 9, 3]: over (9), not bad (10).

**Cause.** `BoundaryNorm.__call__` masks only masked entries; `np.digitize(nan, boundaries)` returns
`len(boundaries)` (3304), and NaN fails both `xx < vmin` and `xx >= vmax`, so it keeps that index. Normalize keeps
NaN as NaN, which the colormap turns into "bad". Plotting functions mask NaN first; `to_rgba` and `cmap(norm(x))`
do not.

### MPL9 (FAIL 12) — `LinearSegmentedColormap(gamma≠1).reversed()` is not the original read backwards (bug; all builds)

For the docstring's example segmentdata with gamma=2 and N=64, `reversed()(i)` differs from `original(N-1-i)` by
up to 0.984 in a channel. The reversed map equals f(1 − (i/(N−1))**2) to 5e-16: the gamma warp is applied to the
already reversed data. `colors.py:LinearSegmentedColormap.reversed` (1291) passes the same gamma with the mirrored
data. Documentation: "Return a reversed instance of the Colormap." With gamma=1 the reversed map is the exact
mirror (ok line).

### MPL10 (FAIL 13) — `LinearSegmentedColormap.resampled()` drops gamma (bug; all builds)

`LinearSegmentedColormap(cdict, gamma=2).resampled(8)` gives entries f(i/7) instead of f((i/7)**2), maxdiff 0.490;
the new map has `_gamma = 1.0`. `colors.py:LinearSegmentedColormap.resampled` (1255) does not pass gamma (under,
over and bad are carried over). Documentation: "Return a new colormap with *lutsize* entries."
`plt.get_cmap(name, lut)` and contourf/BoundaryNorm workflows that resample a gamma-corrected map change its colours.
3.5.2 has the same code as `_resample`.

### MPL18 (FAIL 9) — `BoundaryNorm` with `ncolors` > 32767 (bug at an extreme parameter; all builds)

`BoundaryNorm(np.arange(41), 40000)([0.5, 39.5, 41.])`, documented [0, 39999, 40000]: numpy 2.x (main, 3.11.2)
raises `OverflowError`; numpy 1.x (3.7.1, 3.5.2) silently returns [0, −25537, −25536], negative indices drawn as
"under". Cause: `iret.astype(np.int16)` (3319) and `iret[xx >= self.vmax] = max_col` (3321). The docstring says
"returns integers or arrays of int16" and sets no limit on *ncolors*. Rare in practice (a colormap with more than
32767 entries).

### MPL19 (FAIL 2–5) — `SymLogNorm` uses linscale/(1−1/base), not the documented *linscale*, for the linear range (documentation gap: documentation/implementation mismatch; all builds)

**Measured.**

| parameters | norm values (matplotlib) | documented definition | maxdiff | linear half vs one decade |
|---|---|---|---|---|
| linthresh=1, linscale=1, base=10 | [0.0, 0.3214, 0.5, 0.6786, 0.8393, 1.0] | [0.0, 0.3333, 0.5, 0.6667, 0.8333, 1.0] | 0.0119 | 1.1111 (documented 1) |
| linthresh=1, linscale=1, base=2 | [0.0, 0.375, 0.5, 0.625, 0.6875, 1.0] | [0.0, 0.4286, 0.5, 0.5714, 0.6429, 1.0] | 0.0536 | 2.0000 (documented 1) |
| linthresh=0.5, linscale=2, base=10 | [0.0, 0.3649, 0.6105, 0.8562, 0.9667, 1.0] | [0.0, 0.3837, 0.6163, 0.8488, 0.965, 1.0] | 0.0189 | 2.2222 (documented 2) |
| linthresh=2, linscale=0.5, base=2.718 | [0.0, 0.3118, 0.3885, 0.4651, 0.562, 1.0] | [0.0, 0.3305, 0.3818, 0.4331, 0.5358, 1.0] | 0.0320 | 0.7910 (documented 0.5) |

**Code.** `scale.py:SymmetricalLogTransform.transform_non_affine` (508: `linscale_adj = self.linscale / (1.0 -
1.0 / self.base)`); 3.5.2/3.7.1 have the same factor in `_linscale_adj`.

**Documentation.** SymLogNorm (colors.py:3066–3071), SymmetricalLogScale (scale.py:602–608) and the colormapnorms
tutorial: "Its value is the number of decades to use for each half of the linear range. For example, when
*linscale* == 1.0 (the default), the space used for the positive and negative halves of the linear range will be
equal to one decade"; the symlog demo says "the ratio of visual space of the region (0, linthresh) relative to one
decade".

**Verdict.** The documented meaning is off by 1/(1−1/base): 1.11 for base 10, 2 for base 2. The colorbar uses the
same transform, so a plot agrees with its own colorbar; a reader reasoning from the documented parameter gets a
different mapping. Not a wrong-colour bug inside a plot.

### MPL30 (FAIL 1) — `Normalize()` autoscale on a plain ndarray containing NaN (documentation gap / sharp edge; all builds)

`Normalize()(np.array([3., nan, 7.]))` sets vmin = vmax = nan and every output is NaN, so every value is drawn
"bad". `colors.py:Normalize.autoscale_None` (2606/2608: `self.vmin = A.min()`, `self.vmax = A.max()`). The
docstring: "If either *vmin* or *vmax* is not provided, they default to the minimum and maximum values of the
input." `imshow`, `pcolormesh` and `scatter` are not affected (they mask non-finite values first); only direct
calls (`cmap(norm(data))`). LogNorm and the other scale-based norms autoscale on finite transformed values, except
on 3.5.2 (MPL39).

### MPL31 (FAIL 16) — `imshow` draws ±inf cells transparent, not in the over/under colour (documentation gap; all builds)

`imshow([[1, nan, 3, inf, -inf, masked]], vmin=0, vmax=8)` gives [1, transparent, 3, transparent, transparent,
transparent]: +inf and −inf are stored as masked, like NaN. `Colormap`/`Normalize` called directly map +inf to over
and −inf to under (ok line). `cbook.safe_masked_invalid` (719: `np.ma.masked_where(~(np.isfinite(x)), x)`), used
by `image._normalize_image_array` and `Colorizer.set_array`, masks all non-finite values. The Colormap docstring
reserves `bad` for "invalid values (NaN or masked)" and `over` for "high out-of-range values"; no plotting
docstring says ±inf counts as invalid. Defensible, but an infinite value disappears instead of saturating.

### MPL32 (FAIL 18) — `contourf`: a plateau exactly at `levels[0]` is unfilled when `min(Z) < levels[0]` (documentation gap / ambiguity; all builds)

Z = 0 on a plateau, −1 on one edge, 2 on another, levels [0, 1, 2]: the plateau point is in no filled band
([False, False]); with `extend='min'` it falls in the under band and is drawn in the under colour (8). When
`min(Z) == levels[0]` the plateau is filled in the lowest band (ok line). `contour.py:ContourSet._get_lowers_and_uppers`
(956: `if self.zmin == lowers[0]:`) closes the lowest interval only when the data minimum equals the first level;
otherwise contourpy's `lower < Z <= upper` excludes Z == levels[0]. The Notes (contour.py:1735–1741): "the filled
region is z1 < Z <= z2 except for the lowest interval, which is closed on both sides (i.e. it includes the lowest
value)". A field sitting exactly on `levels[0]` (for example 0 with negative values elsewhere) is left blank.

### MPL33 (FAIL 11) — `Colormap(..., bytes=True)` truncates instead of rounding (documentation gap; all builds)

The colour (0.999, 0.7, 0.0019) gives bytes (254, 178, 0); 255·c = [254.745, 178.5, 0.484], nearest
(255, 179, 0); `to_hex` of the same colour is #ffb200. For viridis, 379 of 768 channels come out 1 below the
nearest byte. `colors.py:Colormap._get_rgba_and_mask` (842: `lut = (lut * 255).astype(np.uint8)`). Documentation:
"otherwise they will be `numpy.uint8`\s in the interval ``[0, 255]``", no rounding rule. At most 1/255 per channel,
not visible; 8-bit hex colours round-trip exactly (ok line).

### MPL34 (FAIL 17) — automatic contour levels are not integer multiples of their step when the span is small relative to the magnitude (documentation gap; all builds)

34 of 300 random ranges, e.g. [−10000, −9985, −9970, −9955] (step 15), [999850, 1000000, 1000150, 1000300] (step
150), 13.03, 13.045, 13.06 (step 0.015; 13.045/0.015 = 869.67), 17.338, 17.344 (step 0.006). Every case has a step
mantissa of 1.5, 3 or 6. Levels are evenly spaced (ok line). `ticker.py:MaxNLocator._raw_ticks` (2268:
`scale, offset = scale_range(vmin, vmax, nbins)`; 2305: `best_vmin = (_vmin // step) * step`) anchors the grid at a
round offset; for mantissas 1, 2, 2.5 and 5 that coincides with absolute multiples, for 1.5, 3 and 6 it does not.
The MaxNLocator *steps* docstring: "Sequence of acceptable tick multiples … ``20, 40, 60`` … multiples of 2".
Harmless for the colours. `ticker.py` ran as the 3.11.2 copy on the main overlay.

### MPL35 (FAIL 19–20) — 3.5.2 and 3.7.1: `imshow` draws a value exactly on a `BoundaryNorm` boundary in the wrong colour (old-release only bug; fixed by 3.11.2)

Boundaries [0, 0.1, 0.2, 0.3, 0.7, 1.1, 1.3, 2.9, 3.0] with 8 colours, each cell on a boundary: `make_image` gives
colours [0, 1, 2, **2**, **3**, 5, 6, 7] for 0 … 2.9 at both 20 px and 2 px per cell, documented [0, 1, 2, 3, 4, 5,
6, 7]; the value one ulp below 0.1 is drawn in colour **1** where it should be 0 (full line: [0, 1, 2, 2, 3, 5, 6,
7, 1, 3, 'over']). `im.to_rgba(data)` gives the right colours on the same build, so the error is in old
`image.py:_make_image`, which rescales into [0.1, 0.9] before resampling and back afterwards (`A_scaled -= a_min`,
`/= ((a_max - a_min) / frac)`, `+= offset`), moving values off exact boundaries. The same data shifted by +1000
happened to come out right. BoundaryNorm documents "Bins are left-closed and right-open". main/3.11.2 have no such
rescaling and pass ([0, 1, 2, 3, 4, 5, 6, 7, 0, 3, 'over'] at offsets 0 and 1000). The fixing PR was not pinned;
3.10.0's "#28122 Disable clipping in Agg resamplers" is a candidate. A heatmap cell on a level boundary is drawn in
the neighbouring class's colour in the cohort's most-cited version (3.7.1), and the colorbar disagrees with the
cell.

### MPL39 (FAIL 22) — 3.5.2 only: `LogNorm()` autoscale with NaN in a plain ndarray raises (old-release only; fixed by 3.7.1)

`LogNorm()(np.array([nan, 1, 10, 100]))` raises `ValueError: Invalid vmin or vmax`: 3.5.2 `LogNorm.autoscale_None`
masks only `A <= 0`, so vmin becomes nan. 3.7.1 and later autoscale on finite transformed values
(`np.extract(np.isfinite(self._trf.transform(A)), A)`, colors.py:2982). Only direct calls are affected.

### MPL42 (FAIL 21) — 3.5.2 and 3.7.1: automatic contour level count exceeds the documented "n+1" (old-release only, documentation)

15 of 348 cases (300 random ranges + 48 round ranges), e.g. `contourf(Z, 1)` on [0, 10] gives 3 levels;
`contourf(Z, 4)` gives 0, 2, …, 10 (6 levels, all inside the data range). `contour.py` uses `MaxNLocator(N + 1)`,
which allows up to N+2 levels inside the limits. The 3.11 docstring says *n+2*, which holds on 3.11.2 and main
(0 exceed). On every build the total returned, including the levels just outside the data, reaches n+3 in 93 of
300 random ranges (information line). Colours unaffected.

## What held up (all builds unless noted)

- **Normalize.** The documented example with and without clip; 400 random (v − vmin)/(vmax − vmin) against
  Fraction (max abs error 1.11e-16); vmin == vmax → 0; vmin > vmax raises; autoscale on lists and masked arrays,
  mask preserved, NaN stays NaN with vmin/vmax given; `inverse` round-trips, unscaled inverse raises; `process_value`
  dtype rules (int8/int16/uint8 → float32, int32/int64 → float64, floats preserved); offsets 1e6 + k in float64
  and float32 and int64 2**40 + k exact; ±inf → ±inf.
- **LogNorm** closed form including out-of-range values; non-positive values masked; autoscale ignores
  non-positive, NaN (3.7.1+) and masked values; clip, inverse, vmin == vmax.
- **SymLogNorm** linear inside ±linthresh, equal steps per factor of base, antisymmetric for vmin = −vmax, inverse,
  clip. **AsinhNorm** (3.6+) matches a0·asinh(a/a0) for three widths. **FuncNorm** values, inverse, autoscale.
  **PowerNorm** Notes formula for gamma 2 and 0.5, above vmax, below vmin (version-aware), clip, inverse, masked
  autoscale, vmin == vmax.
- **TwoSlopeNorm** documented example, 200 random two-sided values against Fraction, out-of-range → ±inf, autoscale
  expansion (3.8+) and clipping (before 3.8), validation, mask, inverse. **CenteredNorm** example, autoscale
  halfrange including masked values, clip, changing vcenter keeps halfrange.
- **BoundaryNorm** values exactly on boundaries go to the upper bin (left-closed) for ncolors 4/5/7/16/256;
  extend 'min'/'max'/'both' with 6, 9 and 256 colours; clip=True with ncolors equal to and greater than the bins;
  a single bin maps to the middle colour; the three documented ValueErrors; mask preserved; scalar → Python int.
  **NoNorm** passes values through and indexes the colormap directly.
- **Colormap.** floor(x·N) with x == 1 → N−1 for N = 1, 2, 5, 8, 256; −1e-300 → under, −0.0 → first, 1+ulp →
  over, ±inf → over/under, NaN → bad; `with_extremes`; masked → bad; int64/uint8 indices; float32 input; `alpha=`
  with bad staying transparent; scalar → tuple; hex colours round-trip through `bytes=True`; viridis 0, 0.5, 1 →
  `colors[0]`, `colors[128]`, `colors[255]`.
- **LinearSegmentedColormap** matches the segmentdata rule (maxdiff < 1e-12) for the docstring example and a
  discontinuous map with N = 2, 5, 11, 256 and gamma 1, 2, 0.5; `from_list` (even and anchored);
  `reversed()`/`resampled()` with gamma 1; under/over swapped on reversal. **ListedColormap** `resampled(k)` samples
  at j/(k−1) and keeps under/over/bad; `reversed()` swaps under/over and keeps bad.
- **End to end.** `ScalarMappable.to_rgba` follows the left-closed edge rule (vmax → last colour). `imshow`
  `make_image` pixels with Normalize(vmin, vmin+8) and 8 colours: edge values in the upper band, vmax in the last
  colour, out-of-range in under/over, for float64 and float32, offsets 0, 1e6, 1024 (float32) and 1e12, at 20, 5
  and 2 px per cell; on main/3.11 also for BoundaryNorm values exactly on non-dyadic boundaries and one ulp below,
  at offsets 0 and 1000; NaN and masked cells transparent.
- **Colorbar.** BoundaryNorm band edges equal the boundaries, band colours equal each bin's documented colour,
  ticks at the boundaries, also with 256 colours and extend='both'; Normalize band edges vmin + k(vmax−vmin)/N with
  band colours equal to the data colours; LogNorm bands at the decades; contourf band edges equal the levels and
  band colours equal the filled bands.
- **contour/contourf.** Automatic levels span the data, are evenly spaced and within the documented count on 3.11;
  NaN in Z ignored for the levels; extend='both' trims levels inside the data; bands on a ramp cover exactly
  [lᵢ, lᵢ₊₁]; "z1 < Z <= z2" on interior and top levels; the lowest interval closed when min(Z) == levels[0]; band
  colours follow the midpoint rule; 5 colours over 5 equal bands; `colors=` cycling; extend='both' under/over
  colours and ranges; extend='neither' leaves the outside unfilled; `colors=` with len == bands + 2; line contour
  colours equal Normalize(levels[0], levels[−1]) of the level.

## Information lines (not FAIL)

- contourf colours each band by its layer midpoint (as `_process_colors` says): with levels [0, 1, 2.5, 6, 10] and 4
  listed colours, bands 0 and 1 both get colour 0 and colour 2 is never used; a reader cannot tell those two bands
  apart in the plot or on the colorbar.
- PowerNorm below vmin gives 0 on 3.5.2/3.7.1 (lowest colour) and a negative value on 3.11 (under); both as
  documented for their versions. TwoSlopeNorm before 3.8 clips the autoscaled range at vcenter.
- `LogNorm(clip=True)` maps negative values to 0 (lowest colour, not bad), as the clip documentation says.
- A discontinuous segmentdata sampled exactly at a jump returns y0. `contourf` of a constant field returns 8 levels
  within 1e-12 of the constant.

## Not checked, and why

`MultiNorm`, `MultivarColormap`, `BivarColormap` (3.10/3.11 multivariate API, outside the cohort's versions);
non-'nearest' image interpolation (no closed-form truth without porting Agg's filters); `pcolormesh`/`pcolor`/
`scatter` per-artist geometry (same `Colorizer.to_rgba` path, checked); log-scale contour levels and `tricontourf`
(time budget); colorbar extend-triangle colours; `LightSource`, HSV conversions and `to_rgba` string parsing; which
MaxNLocator step gets chosen (its default `steps` are not stated in the docstring).

## Notes against outputs

`m4_color_mapping.notes.md` summarises its FAILs as "13 distinct issues: 11 on main, 2 that exist only in old
builds". Its own sections give 12 distinct issues on main (FAIL 1, 2–5, 6–7, 8/15, 9, 10/14, 11, 12, 13, 16, 17,
18) and 3 old-build-only ones (19–20, 21, 22), and the `.out` files bear that out; this review follows the
sections (MPL1, 7–10, 18, 19, 30–34 on main; MPL35, 39, 42 old-only).
