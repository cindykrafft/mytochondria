# m3_stackplot_wiggle: notes

This is a follow-up to `m3_hist_hexbin_counts` FAIL 14, `stackplot(baseline='weighted_wiggle')`. It checks that finding
against the published method and against the reference code it came from.

Harness: `audits/matplotlib/verify/m3b_stackplot_wiggle.py`. It runs in under 1 s. Outputs:

| file | build |
|---|---|
| `m3b_stackplot_wiggle.out` | main overlay (3.11.2 + main @ 44f2e00 files, as in the other m-notes) |
| `m3b_stackplot_wiggle.v3.11.2.out` | 3.11.2, numpy 2.5.3, scipy 1.18.1 |

The two outputs are identical. On both builds the harness gives 40 ok and 8 FAIL. `stackplot.py` in 3.11.2 is
byte-identical to main @ 44f2e00. All file:line citations are on 44f2e00 unless a tag is named.

## Sources

**Paper.** L. Byron and M. Wattenberg, "Stacked Graphs – Geometry & Aesthetics", IEEE TVCG 14(6), 2008, sec. 5.1
(pp. 4–5). The PDF is from leebyron.com/streamgraph/. The equations are images, so they were read from the rendered
pages.

- Definitions: the f_i ≥ 0 are the layers, g_0 is the baseline, and g_i = g_0 + Σ_{j=1..i} f_j. Fig. 4 shows f_1 as
  the bottom layer in an ordinary y-up drawing.
- The weighted measure:
  weighted_wiggle(g_0) = Σ_{i=1..n} (½(g_i′ + g_{i−1}′))² f_i = Σ_{i=1..n} (g_0′ + ½f_i′ + Σ_{j=1..i−1} f_j′)² f_i.
- The paper says this is "minimized at each point in [0,1] when"
  g_0′ = −(1/Σf_i) Σ_i (½f_i′ + Σ_{j=1..i−1} f_j′) f_i.
  The printed outer sum starts at i=0. Since f_0 is undefined, this is a typo for i=1.
- The paper says this formula "turns out to be equivalent to the algorithm used in the Streamgraph method".

**Reference code.** `StreamLayout.java` and `LayerLayout.java` from github.com/leebyron/streamgraph_generator (HEAD
e7370a6), the code linked from leebyron.com/streamgraph/.

- `layout()` accumulates `center[i] += (moveUp - 0.5) * increase`, with
  `moveUp = (½·size_j + Σ_{k>j} size_k) / totalSize`.
- It then sets `baseline[i] = center[i] + 0.5f * totalSize`.
- `stackOnBaseline` stacks each layer by *subtracting*: `baseline[j] -= layers[i].size[j]`, then sets `yTop`.
- The sketch (`streamgraph_generator.pde`, `scaleLayers`) maps these values to Processing screen coordinates with a
  positive scale. Screen y grows downwards.
- So `baseline` is the bottom edge on screen, and layer 0 is the bottom layer. In y-up coordinates (Y = −y) the bottom
  edge is **−center − T/2**.

**matplotlib.** `lib/matplotlib/stackplot.py`.

- The docstring (l. 34–43) says:
  - 'wiggle': "Minimizes the sum of the squared slopes."
  - 'weighted_wiggle': "Does the same but weights to account for size of each layer. It is also called
    'Streamgraph'-layout. More details can be found at http://leebyron.com/streamgraph/."
- The code (l. 115–129):

```python
total = np.sum(y, 0)
inv_total = np.zeros_like(total)
mask = total > 0
inv_total[mask] = 1.0 / total[mask]
increase = np.hstack((y[:, 0:1], np.diff(y)))
below_size = total - stack          # stack = cumsum(y) (l. 98) -> sum_{k>j} f_k
below_size += 0.5 * y
move_up = below_size * inv_total
move_up[:, 0] = 0.5
center = (move_up - 0.5) * increase
center = np.cumsum(center.sum(0))
first_line = center - 0.5 * total   # l. 128
stack += first_line
```

- Layer 0 is drawn between `first_line` and `stack[0]` (l. 132). It is the bottom layer, as in the paper and in Byron.

## Derivation

Write T = Σ_i f_i, d_i = f_i(x_k) − f_i(x_{k−1}), and Δg = g_0(x_k) − g_0(x_{k−1}). Discretise the way both matplotlib
and Byron do: each step is weighted by f_i(x_k) and derivatives become first differences. The objective is then

J = Σ_k Σ_i f_i(x_k) · (Δg_k + ½d_i + Σ_{j<i} d_j)².

The midline of layer i moves by Δg + ½d_i + Σ_{j<i} d_j. J is a sum of one convex quadratic per step, each in its own
Δg_k, and J does not depend on g_0(x_0). So the per-step minimiser is also the global minimiser over all baselines with
g_0(x_0) fixed:

Δg_k = −(1/T) Σ_i f_i (½d_i + Σ_{j<i} d_j) = −(1/T) Σ_j d_j (½f_j + Σ_{i>j} f_i) = −Σ_j moveUp_j · d_j.

The middle step swaps the order of summation. The last expression is Byron's `moveUp`. Byron's y-up bottom edge,
−center − T/2, has the per-step change −Σ_j (moveUp_j − ½)d_j − ½ΔT = −Σ_j moveUp_j d_j. That is the paper's
minimiser, so the paper's statement that the formula equals the Streamgraph algorithm holds exactly.

matplotlib computes `first_line = +center − T/2`, which changes per step by Σ_j moveUp_j d_j − ΔT = −Σ_j (1 −
moveUp_j) d_j. Here 1 − moveUp_j = (½f_j + Σ_{i<j} f_i)/T, which is the weight for the *reversed* stacking order. So:

- matplotlib's baseline is exactly the B&W minimiser for the layers stacked in reverse order (layer 0 on top), but the
  layers are drawn in the original order.
- Equivalently, it is −(top edge of the correct layout). The mirror image of the reversed-order streamgraph is drawn
  with the original order.
- The 2013 code is a line-for-line translation of `StreamLayout.layout()` (see History). It keeps the screen-coordinate
  `center` but changes `+ 0.5*totalSize` to `- 0.5 * total`. Only one of the two signs needed for the y-down → y-up
  flip was changed.

For two layers the difference at a step is closed-form: mpl − minimiser = (f_2·d_1 − f_1·d_2)/T. The two agree only when
both layers change in proportion to their thickness.

## Numbers (exact, Fraction; from `m3b_stackplot_wiggle.out`)

**§0. Byron's code matches the paper.** The literal Fraction port of `StreamLayout` + `stackOnBaseline`, mapped to
y-up, equals the B&W per-step minimiser exactly in all 4 test cases. Its layer tops equal minimiser + cumulative sums,
which confirms that layer 0 is the bottom layer.

**§1. The port matches the installed code.** The Fraction port of stackplot.py l. 116–128 reproduces the installed
`Axes.stackplot` baseline (read from the drawn `PolyCollection`) to 1e-12 in all 4 cases.

**§2. matplotlib against the minimiser.** J is the weighted wiggle above, for the order as drawn.

| layers (layer 0 first = bottom) | B&W minimiser g_0 | matplotlib g_0 | max abs diff / max T | J mpl | J min | ratio |
|---|---|---|---|---|---|---|
| [1,3], [1,1] | −1, −9/4 | −1, −7/4 | 1/2 / 4 | 7/4 | 3/4 | 2.33 |
| [1,1], [1,3] | −1, −7/4 | −1, −9/4 | 1/2 / 4 | 7/4 | 3/4 | 2.33 |
| m3 example, 3×7 | −2, −19/8, −29/8, −377/72, −353/72, −59/18, −3 | −2, −13/8, −19/8, −271/72, −295/72, −85/18, −6 | 3 / 9 | 4049/48 = 84.35 | 1999/144 = 13.88 | 6.08 |
| 4×5 (see .out) | −4, −3.318, −4.256, −5.827, −8.127 | −4, −7.682, −3.744, −1.173, −1.873 | 6.25 / 11 | 594.49 | 49.17 | 12.09 |

In all four cases the following hold exactly:

- matplotlib == the minimiser for the reversed order;
- matplotlib == −(top of Byron's layout);
- J_mpl(drawn order) == J_min(reversed order).

**§3. Two-layer steps.** The closed form (f_2 d_1 − f_1 d_2)/T holds exactly for 5 cases. One example: f_1 = 4→1 and
f_2 = 1→4. The minimiser keeps both midlines flat (J = 0), but matplotlib gives J = 45.

**§4. Where matplotlib is right.** These cases all agree exactly:

- a single layer;
- a palindromic layer order (L0 == L2);
- all layers proportional to one profile.

These are the cases where the reversal makes no difference.

**§5. Random cases.** 400 random integer cases (2–5 layers, 3–8 points, values 0..9):

- matplotlib equals the minimiser in **0 of 400**;
- J_mpl/J_min ranges from 1.02 (min) through 5.24 (median) and 17.8 (90th percentile) to 212 (max);
- the worst baseline offset is 0.96 × the maximum total thickness;
- J_mpl is never below J_min, which is a sanity check on the minimiser.

**§6. Not a discretisation choice.**

- matplotlib is not the minimiser for any of the three weight choices f(x_k), f(x_{k−1}) and the average. On the m3
  example J is 84.35/83.35/83.85 for matplotlib against 13.88/12.58/13.31 for the minimiser.
- On smooth layers f_1 = 1 + 2x (bottom) and f_2 = 1, the continuous B&W solution is g_0(1) − g_0(0) = −1 − ln2/2 =
  −1.34657. The reversed order gives −1 + ln2/2 = −0.65343.
- matplotlib gives −0.66561, −0.65467, −0.65355 and −0.65344 at n = 11, 101, 1001 and 10001. It converges to the
  reversed-order value, so the gap (ln 2 here) does not shrink with grid refinement.

**§7. 'wiggle' is not reversed.** matplotlib's unweighted 'wiggle' (l. 109–113,
g_0 = −(1/m) Σ (m − i − ½) f_i) is the midline minimiser for the drawn order. It is not the reversed one, and it equals
the integral of the unit-weight per-step minimiser. So the two wiggle options use opposite layer orientations, and only
'weighted_wiggle' is reversed.

## Verdict

**Bug: wrong numbers against matplotlib's own docstring and the cited method.** This is not a documented variant and
not a harness error.

- **Docstring.** It promises the squared-slope minimisation weighted by layer size and points to Byron's Streamgraph
  page. matplotlib's baseline minimises that measure for the reversed layer order. For the order it draws, it is worse
  than the minimiser in every non-symmetric case tried: 400/400 random cases, with J up to 212× the minimum.
- **Not a variant.** Nothing in the docstring, the code comments, the tests or the history documents a reversed or
  mirrored layout.
  - The only test is the image comparison `test_stackplot_baseline` (lib/matplotlib/tests/test_axes.py:3484–3508,
    `stackplot_test_baseline.png`). It pins the current output. A fix would need that baseline image regenerated.
  - The only related issue found was #6313, the all-zero column fixed in 2016. The search was read-only, on
    matplotlib/matplotlib issues for "weighted_wiggle"/"streamgraph".
- **Not a harness error.**
  - The m3 truth is the paper's formula.
  - The paper's formula equals Byron's reference code exactly (§0).
  - The Fraction port of stackplot.py reproduces the installed build (§1).
  - The finding reproduces with three discretisations and survives grid refinement (§6).
- **Cause.** stackplot.py:128 `first_line = center - 0.5 * total`. For y-up axes it should be
  `-center - 0.5 * total`. The sign of the accumulated `center` was not flipped when the y-down reference code was
  ported.
- **Effect.** A streamgraph whose thick layers sit at the bottom wiggles as if they were on top. The silhouette and the
  layer thicknesses are still drawn correctly: thicknesses are preserved, and that check passes in m3.

Independent of this, the integer-input truncation (m3 FAIL 15) is a separate bug in the same block.
`inv_total = np.zeros_like(total)` (l. 118) is integer for integer layers.

## History (blame on 44f2e00, git log --follow)

- **l. 115, 116 and 128** (`first_line = center - 0.5 * total`) come from **24f537f**, Till Stensitzki, 2013-01-10,
  "[ENH] added baseline feature to stacked graph". That commit's `weighted_wiggle` is an explicit triple loop. It
  translates `StreamLayout.layout()` statement for statement: `center[i] = center[i-1]`, `belowSize`, `increase`, and
  `moveUp = 0.5` at i=0. It ends with `first_line = center - 0.5 * total`. The docstring added in the same commit
  pointed to http://www.leebyron.com/else/streamgraph/. The first tags containing it are v1.3.0rc1 and v1.3.0.
- **l. 121–127** come from **339ca4e**, Damon McDougall, 2013-01-17, "Vectorise the loops". This is a semantics-preserving
  vectorisation that keeps the same sign.
- **l. 117 and 124** come from **102872a**, a merge of #6358 (E. G. Patrick Bos, 2016) fixing #6313: the division by
  zero when all layers are 0 at one x.
- **l. 118–120** come from **a1dbd55**, Elliott Sales de Andrade, 2016-10-23, "Avoid divide-by-zero in stackplot". It
  replaced `np.where(total > 0, 1./total, 0)` (float) with `np.zeros_like(total)`, and this introduced the integer
  truncation of m3 FAIL 15. First tag: v2.0.0rc1 / v2.0.0.
- **l. 98**, the float `stack` buffer, comes from **e81b280** (2017-01-13, first in v2.1.0).

## Versions affected

- **Source checked** via `git show <tag>:lib/matplotlib/stackplot.py`: v1.3.0, v2.0.0, v3.5.2, v3.7.1, v3.11.2 and main
  @ 44f2e00. Every one has `first_line = center - 0.5 * total`.
  - From `stack = np.cumsum(...)` to `stack += first_line`, the baseline code in v3.5.2 and v3.7.1 is textually
    identical to main (diff empty).
  - v3.11.2 `stackplot.py` is byte-identical to main.
- **Runtime checked:**
  - main overlay and 3.11.2 by this harness;
  - 3.5.2 and 3.7.1 through the committed `m3_hist_hexbin_counts.v3.5.2.out` / `.v3.7.1.out`. These show the same
    baseline `[-2, -1.625, -2.375, -3.7639, -4.0972, -4.7222, -6]` and the same "equals the reversed-order minimiser:
    True".
- **Affected:** every release from 1.3.0 (2013) to main @ 44f2e00. The integer truncation (m3 FAIL 15) affects 2.0.0
  onwards.

## Reproduction of the existing harnesses (this session)

The environments were rebuilt in the scratch dir after the container reset:

- `venv-rel`: matplotlib 3.11.2, numpy 2.5.3, scipy 1.18.1, Python 3.12.3.
- `venv-main`: the same packages, installed with `--link-mode=copy`, with main @ 44f2e00's `cbook.py`, `mlab.py`,
  `colors.py`, `colorizer.py`, `contour.py`, `stackplot.py` and `axes/_axes.py` copied in. A `cmp` against the clone
  confirmed the copies.

m1–m4 were re-run on both. All eight outputs are byte-identical to the committed `.out` and `.v3.11.2.out` files, with
the same ok/FAIL counts:

| harness | ok / FAIL |
|---|---|
| m1 | 164/12 |
| m2 | 258/24 |
| m3 | 165/11 on main, 164/11 on 3.11.2 |
| m4 | 190/18 |

The committed files were therefore left unchanged.
