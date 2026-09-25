# n12_array_manipulation_indexing — notes

Harness: `audits/numpy/verify/n12_array_manipulation_indexing.py`. Outputs: `n12_array_manipulation_indexing.out` (numpy 2.4.6),
`.v1.23.5.out`, `.v1.24.4.out` and `.v1.26.4.out`. Every check compares against one of these:

- a plain-Python reference: nested lists indexed through `itertools.product` (C and F traversal), explicit loops for take / put /
  putmask / place / roll / rot90 / tile / fancy indexing, a 1-D pad reference for every mode applied axis by axis (as the pad Notes
  describe), and the array_split division rule;
- `fractions.Fraction` for linspace / arange spacing, pad mean / median and integer rounding;
- a closed form: ravel_multi_index strides, geomspace `s*(e/s)**(i/(n-1))`, the complex geomspace circle;
- docstring examples and documented invariants.

The pad reference was checked first against all 11 1-D docstring examples.

No scipy anywhere. The harness takes about 0.2 s per build.

Counts: 2.4.6: 357 ok / 2 FAIL. 1.23.5: 345 ok / 7 FAIL. 1.24.4: 347 ok / 5 FAIL. 1.26.4: 350 ok / 3 FAIL.

## FAIL lines

### 1. `pad 1-D float mode='reflect'`: widths larger than the array, one-sided or asymmetric (1.23.5, 1.24.4, 1.26.4)

**What was measured.** `np.pad(v, (25, 1), 'reflect')` with v = [-7, -2, 5, 15, 16] (n = 5). The reference mirrors on the edge value.
For widths > n-1 it keeps reflecting, which gives the period-2(n-1) extension (for `odd`, the point-symmetric extension). The 1.x output
breaks the pattern partway through:

- numpy: `[-2, 5, 15, 16, 15, 5, -2, -7, -2, 5, 15, 16, 15, 16, 15, 5, ...]`
- reference: `[-2, -7, -2, 5, 15, 16, 15, 5, -2, -7, ...]`

The same happens for `(1, 25)`, and for `reflect_type='odd'`. Symmetric widths such as (13, 17) and one-sided (25, 0) agree.

**What the library does.** In 1.x, `numpy/lib/arraypad.py::_set_reflect_both` takes the chunk length from the current valid
region, `old_length = padded.shape[axis] - right_pad - left_pad` then `chunk_length = min(old_length, left_pad)`. After the first
iteration that region already contains the padding from the other side, so it is not a multiple of the period, and the next chunk
reflects a region that includes the other side's pad values.

**Fix.** Released in 2.0.0: gh-25963, backported as gh-26697, "BUG: Fix bug in numpy.pad()". Since then the code rounds
`old_length` down to a multiple of `original_period - 1` (`original_period` for symmetric).

**Documentation.** "Pads with the reflection of the vector mirrored on the first and last values of the vector along each axis."

**Verdict:** bug in 1.x, fixed in 2.0. Present in 1.23.5, 1.24.4 and 1.26.4. Correct in 2.4.6.

### 2. `pad 1-D float mode='symmetric'`: same cause (1.23.5, 1.24.4, 1.26.4)

Measured `(25, 1)` on the same vector:

- numpy: `[5, -2, -7, -7, -2, 5, 15, 16, 16, 16, 16, 15, ...]`
- reference: `[16, 15, 5, -2, -7, -7, ...]`

Note the four repeated 16s in the numpy output. The code path is the same (`_set_reflect_both` with `include_edge=True`) and has the
same fix in 2.0. **Verdict:** bug in 1.x, fixed in 2.0. Correct in 2.4.6.

### 3. `pad 1-D float mode='wrap'`: widths larger than the array (1.23.5, 1.24.4)

**What was measured.** `np.pad(v, (9, 2), 'wrap')`:

- numpy: `[15, 16, -7, -2, -7, -2, 5, 15, 16, ...]`
- reference (periodic): `[-2, 5, 15, 16, -7, -2, 5, ...]`

`(25, 1)` and `(1, 25)` also fail.

**What the library does.** In 1.24.4, `numpy/lib/arraypad.py::_set_wrap_both` uses
`period = padded.shape[axis] - right_pad - left_pad`, which is the valid region including earlier padding, not the original length.

**Fix.** 1.25.0 changed this (gh-22575). The 1.25.0 release note says: "`np.pad` with `mode=wrap` now always fills the space with
strict multiples of original data even if the padding size is larger than initial array."

**Verdict:** bug in 1.23 and 1.24, fixed and documented in 1.25. Correct in 1.26.4 and 2.4.6.

### 4. `pad 2-D reflect / symmetric / wrap incl. widths larger than the axis`: `('wrap', (1, 3))` (1.23.5, 1.24.4)

This is FAIL 3 on a (2, 3) array padded `(1, 3)`: axis 0 gets width 1 and 3 on an axis of length 2. In the last row, numpy repeats
row 1 where the periodic reference has row 0. Same code and same fix (gh-22575). **Verdict:** bug in 1.23 and 1.24, fixed in 1.25.

### 5. `mgrid[0:1:3.5j]` stop inclusive (1.23.5 only)

**What was measured.** 1.23.5 gives `[0.0, 0.4, 0.8]`; the expected result is `[0, 0.5, 1]`.

**What the library does.** In 1.23.5, the 1-D branch of `numpy/lib/index_tricks.py::nd_grid.__getitem__` does
`step = abs(step); length = int(step); step = (key.stop-start)/float(step-1)`. It counts `int(3.5) = 3` points but divides by
3.5 - 1 = 2.5, not by 3 - 1. The multi-dimensional branch correctly uses `step = int(abs(step))`.

**Documentation.** "the integer part of its magnitude is interpreted as specifying the number of points to create between the start
and stop values, where the stop value **is inclusive**."

**Fix.** 1.24.0, gh-16971 ("BUG: Fix three complex- & float128-related issues with nd_grid").

**Verdict:** bug in 1.23.5 only. Integer magnitudes such as `5j` work in every build.

### 6. `ogrid[0:1:3.5j]` (1.23.5 only)

Same code path and same fix as FAIL 5. The measured output is the same, `[0.0, 0.4, 0.8]`. **Verdict:** bug in 1.23.5.

### 7. `2.x NEP 50: where(c, uint8 array, 300) / (int8 array, -129) raise OverflowError` (2.4.6)

**What was measured.** Out-of-range Python ints are silently truncated:

- `np.where([T, F, T], np.array([1, 2, 3], np.uint8), 300)` returns `uint8 [1, 44, 3]`: 300 becomes 44.
- `np.where(c, int8 array, -129)` returns `int8 [1, 127, 3]`: -129 becomes 127.

In the same build, `np.array([1], np.uint8) + 300`, `np.full(3, 300, dtype=np.uint8)` and `np.copyto(uint8, 300)` all raise
`OverflowError: Python integer 300 out of bounds for uint8`.

**What the library does.** In 2.0 to 2.4, `PyArray_Where` (`numpy/_core/src/multiarray/multiarraymodule.c`) resolves the weak dtype
(uint8) but then casts the Python int with the iterator's `NPY_UNSAFE_CASTING`. Main commit 2430050aaa (gh-30803) adds
`npy_update_operand_for_scalar(&ax, x, common_dt, NPY_SAFE_CASTING)` for Python-literal operands. The 2.5.0 release notes say:
"Previously, if the x or y argument of numpy.where was a Python integer that was out of range of the output type, it would be
silently truncated. Now, an OverflowError will be raised instead." I checked the dev build (2.6.0.dev0) and it raises
`OverflowError`.

**Documentation.** NEP 50, adopted in 2.0, [T4]/[T5]: "new behaviour raises an error for the same reason", and "300 cannot be
converted to uint8".

**Verdict:** bug in 2.0 to 2.4 (silent wrong values), fixed in 2.5.0. 1.x uses value-based casting instead and correctly returns
`uint16 [1, 300, 3]`, which the 1.x branch of the harness checks.

### 8. `shares_memory max_work=0` is not "equivalent to may_share_memory()" (all builds)

**What was measured.** With `max_work=0`, `np.shares_memory(x[::2], x[1::2])` and `np.shares_memory(x[:6], x[4:])` both raise
`numpy.exceptions.TooHardError: Exceeded max_work`. `np.may_share_memory` returns True for both. Disjoint extents return False from
both functions.

**What the library does.** `numpy/_core/src/common/mem_overlap.c::solve_may_share_memory` has
`if (max_work == 0) { /* Too much work required, give up */ return MEM_OVERLAP_TOO_HARD; }`.
`array_shares_memory_impl` in `multiarraymodule.c` then raises `TooHardError` when `raise_exceptions` is set, which it is for
`shares_memory`. `may_share_memory` calls the same code with `raise_exceptions=0`, where `/* Don't know, so say yes */` returns True.

**Documentation.**

- 2.x: "max_work=0 — Only the memory bounds of a and b are checked. This is equivalent to using `may_share_memory()`."
- 1.x: "max_work=MAY_SHARE_BOUNDS — Only the memory bounds of a and b are checked." `MAY_SHARE_BOUNDS` is 0.

Both docstrings also list "Raises TooHardError: Exceeded max_work", so the exception is sanctioned in general. Neither says that
`max_work=0` raises whenever the bounds overlap, and the 2.x text says it behaves like `may_share_memory`.

**Verdict:** documentation gap. The behaviour is deliberate, and the equivalence sentence (2.x) and the bounds-only description (1.x)
are inaccurate. Present in all four builds. A finite `max_work=1` solves the interleaved case exactly (False), and that check passes.

## What held up (all builds unless noted)

- **reshape.**
  - C/F orders against plain traversal.
  - 'A' on Fortran, C and non-contiguous inputs.
  - -1 inference and its errors.
  - The view when C-contiguous.
  - 2.1+: `copy=`. 2.4: `newshape=` removed.
- **ravel / flatten.** Order K on six non-contiguous and negative-stride views matches the documented rule: memory order, but
  negative strides are not reversed. C/F/A orders; view-vs-copy.
- **np.resize.** Cyclic repetition, including the empty-array → zeros case. **ndarray.resize:** zero-fill, shrink, refcheck and
  view errors, and on a Fortran array "flattened in the order the data are stored in memory" plus the docstring example.
- **Broadcasting.**
  - `broadcast_shapes` on 12 cases, with ValueError where the rule fails.
  - `broadcast_to`: read-only, stride 0, errors.
  - `broadcast_arrays`: values; tuple in 2.x and list in 1.x; the DeprecationWarning on write (still present in 2.4.6).
- **take / put.** take with raise/wrap/clip, including negatives and the documented "clip disables negative indexing"; take with
  2-D indices along an axis. put with cyclic `v`.
- **putmask vs place.** The two differ as documented: putmask is positional (`values[n % len]`), place is sequential.
- **take_along_axis / put_along_axis.** Sorting and argmax idioms, axis=None; the 2.3+ default axis=-1.
- **choose, compress.** choose raise/wrap/clip, including the docstring examples and broadcasting. compress truncation rule;
  IndexError for a True beyond the axis.
- **pad.**
  - All 11 1-D docstring examples, the 2-D 'minimum' example and the callable examples.
  - Every mode against the reference on 11 widths, including one-sided widths larger than n. This passes on 2.4.6 for all modes,
    and on 1.x for everything but reflect/symmetric/wrap.
  - Integer mean/median rounded half-to-even; integer linear_ramp floored (linspace rule).
  - 2-D per-axis, per-side constant / end values / stat_length, with corners computed from the earlier axes (documented).
  - 3-D wrap and symmetric; 'empty'; float32 preserved.
  - Errors: negative width, empty axis, unsupported keyword.
  - 2.4: dict `pad_width`.
- **roll.** Shifts larger than n, tuples, repeated axis (sum), axis=None.
- **rot90, flip, tile, repeat.** rot90 for k in -5..7, `axes=(1,0)` reversal, 3-D; flip*; tile with rank promotion in either
  direction; repeat per element, zero repeats, errors.
- **Grids.** meshgrid xy/ij, sparse, copy=False views, 3-D shapes; mgrid/ogrid with complex steps inclusive and real steps
  exclusive; indices (dense and sparse); ix_ with booleans.
- **linspace.**
  - Endpoints exact; within 0.92 ulp of max(|start|, |stop|) against Fraction.
  - num=1: step NaN with endpoint, `stop - start` without.
  - num=0 / negative num; integer dtype floors (1.20+); float32; array endpoints with axis; complex.
- **arange.**
  - Length is `ceil((stop-start)/step)` in float. `np.arange(1, 1.3, 0.1)` has 4 elements with last = 1.3000000000000003 > 1.3,
    which is the documented hazard.
  - Values equal `start + i*(dtype(start+step) - dtype(start))`, as documented in the Warnings section.
  - The `dtype=int` docstring examples; exact int64 near 2**53; float32.
- **logspace / geomspace.** logspace exact powers; base array (1.25+; pre-1.25 rejects it). geomspace endpoints exact, including
  negative and decreasing ranges; interior within 3.3e-15; the integer-truncation docstring example; complex line and circle; zero
  → ValueError.
- **insert / delete / append.**
  - insert: positions refer to the original array, scalar-vs-sequence axis semantics, negative and out-of-range indices.
  - Boolean obj: a mask in 2.1.2+, cast to 0/1 before, both as documented in `versionchanged 2.1.2`.
  - delete: slices, negative and repeated indices, boolean masks, IndexError; append.
- **split family.** The array_split size rule for n = 0..13 and k = 1..6; split equal-division error and index lists past the end;
  h/v/dsplit and their dimension errors; views.
- **Stacking.**
  - The stack family; column_stack; dstack of 1-D.
  - row_stack: DeprecationWarning in 2.x, silent in 1.x.
  - concatenate: axis=None; `dtype`/`casting` (same_kind error, unsafe truncation, `'no'`); out and dtype conflict.
  - block, including depth errors; atleast_1d/2d/3d shapes, returning a tuple in 2.x and a list in 1.x.
- **Axis manipulation.** expand_dims with tuples and errors; squeeze errors; moveaxis, swapaxes, rollaxis and transpose values and
  errors.
- **Triangles and diagonals.**
  - triu/tril for k in -4..5, including 3-D and 1-D input; tri.
  - diag/diagflat offsets; diagonal is a read-only view (also through `np.diag`); 3-D diagonal.
  - fill_diagonal: tall with wrap=False and wrap=True (the 7×3 docstring pattern), wide, cyclic values, 3-D, and the non-cube error.
- **Index conversion.** ravel_multi_index and unravel_index: the docstring examples, wrap/clip × C/F against closed-form strides,
  round-trips, errors, 2.x `dims` removal.
- **Advanced indexing.**
  - "Advanced indices separated by a slice go first" for arrays and for integers; adjacent ones stay in place; the documentation's
    example shapes.
  - Boolean masks with fewer dimensions give rows in C order.
  - `x[[1,1,3,1]] += 1` increments once; `np.add.at` and `np.multiply.at` accumulate; unary `ufunc.at`.
  - Negative, out-of-bounds, empty and float index arrays; copy vs view.
- **nonzero, argwhere, where.** nonzero on 0-d warns in 1.x and raises ValueError in 2.1+; argwhere 0-d shapes (1, 0) and (0, 0);
  where dtype promotion.
- **apply_along_axis.** Shapes for scalar, 1-D and 2-D results; empty-axis error.
- **vectorize and frompyfunc.**
  - vectorize calls the function one extra time without `otypes` or `cache`. That matches the docstring, which says `cache=True`
    avoids "calling the function twice".
  - The first-call type-inference pitfall is documented and reproduced: `[0, 1, 2]` instead of `[0, 1.5, 2.5]`.
  - otypes, excluded (by name and by position), signature, empty input.
  - frompyfunc returns object arrays and keeps Fractions exact.
- **Memory and comparison helpers.**
  - copyto: casting rules and `where`. shares_memory / may_share_memory: exact vs bounds.
  - trim_zeros, including the 2.2+ N-D form. sliding_window_view: shapes, axis, read-only default and write-through.
  - as_strided; array_equal with equal_nan; array_equiv.

## Recorded, not judged (no documented expectation)

- **Repeated-index assignment.** `x[[1,1,3,1]] = [10,20,30,40]` gives x[1] = 40, so the last value wins on every build. The docs say
  "there is in general no guarantee for the iteration order", so the check only requires one of the assigned values. put_along_axis
  with repeated indices also ends with the last value.
- **apply_along_axis output dtype.** The output buffer takes the dtype of the first call's result. When the first call returns int 0
  and later calls return floats, the result is `[0, 2, 4]` int64 and the fractions are silently dropped. Recorded as the pitfall; the
  docstring does not mention it.
- **Minor behaviours without a documented expectation:**

  | Call | Result |
  |---|---|
  | `np.pad` callable | Invoked once per 1-D line of the full padded array, including pad columns (11 calls for (2,3) padded ((1,2),(3,0))) |
  | `pad` reflect / symmetric of a length-1 array | Edge value repeated |
  | `insert` with a boolean mask of another length (2.x) | Accepted |
  | `compress` with a condition longer than the axis but False beyond it | Accepted |
  | `choose` with 40 choices | ValueError on 1.23.5 (the old 32-argument limit); fine on 2.x |
  | `copyto(uint8, 300)` | Wraps to 44 on 1.x; OverflowError on 2.x |
  | `geomspace(-1, 1, 3)` | `[-1, nan, 1]` with no error |
  | `array_equal` with `equal_nan=True` | Treats `nan+1j` and `1+nanj` as equal |

- **`np.linspace(inf, inf, 3)`** returns `[nan, nan, inf]` on every build. linspace does not document infinite endpoints. Main fixed
  this on 2026-06-13 (commit 4d6c7be1f4, "BUG: fix linspace returning NaN for equal infinite endpoints (gh-26699)"), and the
  2.6.0.dev build returns `[inf, inf, inf]`. Informational only.

## What could not be checked

- pad 'empty' values are undefined by definition; only the shape and the interior are checked.
- vectorize, apply_along_axis and frompyfunc performance claims were not checked.
- as_strided's `check_bounds` keyword exists in main only, not in any tested build.
- The shares_memory worst case (NP-hard) was not timed.
- The broadcast_arrays write deprecation is only checked as "warns". The documented future change (read-only) has not happened in
  2.4.6.
