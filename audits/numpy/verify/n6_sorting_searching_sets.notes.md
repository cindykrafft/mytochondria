# n6_sorting_searching_sets — notes

Harness: `audits/numpy/verify/n6_sorting_searching_sets.py`; outputs `n6_sorting_searching_sets.out` (numpy 2.4.6),
`.v1.23.5.out`, `.v1.24.4.out`, `.v1.26.4.out`. Every check is against a plain-Python reference: `sorted()` /
`sorted(range(n), key=...)` with the documented key (NaN last; complex `[R+Rj, R+nanj, nan+Rj, nan+nanj]`; NaT last),
`bisect`, `Counter`, `set`, first-occurrence dicts, or a documented invariant (partition, digitize tables).
Whole harness ~40 s per build (the 1e6 section is ~35 s of it).

Counts: 2.4.6 — 271 ok / 4 FAIL; 1.23.5 — 258 ok / 1 FAIL; 1.24.4 — 271 ok / 1 FAIL; 1.26.4 — 271 ok / 1 FAIL.

## FAIL lines

### 1. `unique(complex with NaN placements, equal_nan=True)` — plain `unique()` picks a different NaN representative (2.4.6 only)

Measured: a 3000-element complex128 array with NaNs in the real part, the imaginary part and both. With
`return_index/inverse/counts` the result matches the reference (values, first-occurrence index, counts, inverse);
the plain `np.unique(cx)` call returns the same values except for the NaN class, where it returns `nan+nanj`
while the reference (and the other call) returns `nan-3j`, the smallest NaN in the documented lexicographic order.
Library: since 2.3 (`gh-26018`, "np.unique now tries to use a hash table") the no-extra-output path in
`numpy/lib/_arraysetops_impl.py::_unique1d` calls `_unique_hash(ar_, equal_nan=equal_nan)` and sorts the
result; complex dtypes were added to that path in 2.4.0 (`gh-29537`). In `numpy/_core/src/multiarray/unique.cpp`,
`equal_complex` returns `equal_nan` for any pair of NaN-containing values and `hash_complex` gives every NaN the
same hash, so `std::unordered_set::insert` keeps the *first encountered* NaN (`nan+nanj` is at index 0 in this
data), not the smallest one. The sort path (used whenever an index, inverse or count is requested, and on 1.x)
takes `aux[aux_firstnan]`, the smallest in sort order.
Documentation (`np.unique`, Notes, versionchanged 1.21): "For complex arrays all NaN values are considered
equivalent ... As the representant for the returned array the smallest one in the lexicographical order is
chosen". Verdict: minor bug / documentation gap in 2.4.x — the documented representative is not honoured on the
hash path, and the same call with and without `return_counts` disagrees (FAIL 2 below). Shown by 2.4.6; 1.23.5,
1.24.4, 1.26.4 return the documented `nan-3j` on both paths.

### 2. `unique(complex) with and without return_counts pick the same NaN representative` (2.4.6 only)

Same root cause as 1: `np.unique(cx)` gives `nan+nanj`, `np.unique(cx, return_counts=True)[0]` gives `nan-3j`.
Verdict: consistency bug, 2.4.6 only.

### 3. `unique(datetime with 2 NaT, equal_nan=False)` collapses the NaTs on the no-extra-output path (2.4.6 only)

Measured: `np.unique(np.array(['2020-01-01','NaT','2020-01-01','NaT'], dtype='datetime64[D]'), equal_nan=False)`
returns `['2020-01-01', 'NaT']` (2 elements) on 2.4.6; the same call with `return_counts=True` returns three
elements (`'2020-01-01', 'NaT', 'NaT'`), as do all 1.x builds for both call forms (float NaN behaves correctly
on every build: `equal_nan=False` keeps all NaNs). Library: `unique.cpp` registers
`{NPY_DATETIME, unique_numeric<npy_uint64, hash_integer<npy_uint64>, equal_integer<npy_uint64>, ...>}`;
`equal_integer` is `return *lhs == *rhs;` and `hash_integer` hashes the raw bytes — both ignore `equal_nan`, so
two NaT values (identical int64 bit pattern) are always merged. The sort path uses `aux[1:] != aux[:-1]`, and
`NaT != NaT` is True, so it keeps them when `equal_nan=False` (and its explicit `dtype.kind in "cfmM"` branch
collapses them only when `equal_nan=True`). Documentation: `equal_nan : bool — If True, collapses multiple NaN
values in the return array into one`; the sort path treats NaT as the datetime NaN and 1.x always did.
Verdict: bug (the `equal_nan=False` contract is broken for datetime64 on the hash path, and the two paths
of one function disagree). Shown by 2.4.6 only.

### 4. `bincount(float LIST [1.5, 2.0]) raises TypeError` — it silently truncates instead (all four builds)

Measured: `np.bincount([1.5, 2.0])` returns `[0, 1, 1]` on every build (1.5 truncated to 1); on 2.4.6 a
`DeprecationWarning` ("Non-integer input passed to bincount ... Deprecated NumPy 2.1") is emitted, on 1.x nothing.
`np.bincount(np.array([1.5, 2.0]))` (an ndarray) raises TypeError on every build, as documented. Library:
`numpy/_core/src/multiarray/compiled_base.c::arr_bincount`: "Accepting arbitrary lists that are cast to
NPY_INTP, possibly losing precision because of unsafe casts, is deprecated. We continue to use
PyArray_ContiguousFromAny(list, NPY_INTP, 1, 1) to convert the input during the deprecation period"; 2.1.0
release notes, gh-27076: "such inputs are silently cast to integers with no warning about loss of precision".
Documentation: `Raises: TypeError — If the type of the input is float or complex`. Verdict: documented behaviour
not honoured for list input; a known, deprecated (2.1) hole rather than a new bug — on 1.23–1.26 a paper that
passes a Python list of floats gets silently truncated counts with no warning. Shown by all four builds.

Side note recorded in the output: `np.bincount(np.array([1, 2], dtype=np.uint64))` raises TypeError on 1.x
(uint64 → intp cast refused) and works on 2.4.6.

## What held up (all four builds unless noted)

- `sort` / `argsort` for quicksort, mergesort, heapsort, stable on int64/int16/int8/uint8/bool, uint64 with
  2^64−1 and 2^63, int64 with −2^63 and 2^63−1, float64/float32/float16 with NaN, −NaN, ±inf, ±0.0, complex128/64
  with every NaN placement, unicode (empty strings, prefixes, non-ASCII), bytes, datetime64 and timedelta64 with
  NaT, structured arrays with `order='x'`, `order=['s']`, `order=['s','x']` and no order (unspecified fields break
  ties in dtype order), object arrays of ints, str and tuples — every kind returns the reference order;
  mergesort/stable return exactly Python's stable first-occurrence permutation; quicksort/heapsort do not
  (recorded per dtype: they coincide with the stable order only on the tie-free extreme-value arrays).
- NaN placement: both NaN signs and four distinct NaN payloads sort to the end for every kind; stable/mergesort
  keep NaN entries (indices and bit patterns) in input order; complex NaN categories come out in the documented
  order with each category sorted by its non-NaN part. −0.0 == 0.0 for every kind; stable/mergesort keep the
  zeros' input order (quicksort/heapsort reorder them; the exact arrangement differs between builds — recorded,
  not a contract).
- `kind='stable'` and `kind='mergesort'` give bitwise-identical sorts and identical argsorts on 12 dtypes
  (incl. the int16/uint8/bool radix path); `stable=True/False` (2.x) matches.
- axis −1 / 0 / None, 3-D lanes, argsort along axis 0 per kind, `axis=None` on 2-D, 0-d (AxisError; `axis=None`
  works; `argsort` gives `[0]`), empty and single-element arrays, shapes `(0,3)`/`(3,0)`, strided / reversed /
  Fortran / transposed / column views, in-place `ndarray.sort()` on a strided view and on a column view touching
  only the viewed elements, `np.sort` returning a copy.
- `partition` / `argpartition` (introselect) with kth 0, 1, n/2, n−1, −1, −3, a tuple and a list of kth on
  float64 (NaN after inf), float32, int64/int16 ties, uint64 extremes, complex with NaN, strings, datetime with
  NaT, object; axis=0 on 2-D; axis=None; kth out of range → ValueError.
- `lexsort`: last key primary, 2- and 3-key, string primary/tertiary, single key == stable argsort,
  all-equal keys → arange, 2-D keys array, `axis=0`, float key with NaN, complex key, the docstring example.
- `searchsorted` both sides == `bisect` on the documented key for int ties, float with NaN/inf/−0.0 in `a` and
  `v`, float32, complex with NaN, strings, bytes, datetime with NaT, `sorter=` from a Python stable argsort,
  float32 `v` in float64 `a` (v widened exactly: float32(0.2) lands after 0.2), float64 `v` in float32 `a`,
  int/float mixes, scalar `v`, `a` as `v` (first / one-past-last), empty `a`. Descending and unsorted `a` are
  undefined — outputs recorded (`[0, 5, 0]` and `[3, 5]`).
- `unique`: sorted values, first-occurrence `return_index`, counts, inverse round trip on int64/int8/uint64/bool,
  float64/float32 with NaN (one NaN, index of the first NaN), strings, bytes, datetime with NaT, structured,
  object ints and str; `equal_nan=False` keeps every float NaN and every complex NaN (with counts 1);
  `equal_nan=True` collapses complex NaNs to the documented smallest one on the sort path; −0.0/0.0 → one zero
  (which one is kept is undocumented: the first in the input on the sort path — recorded); `axis=0` rows,
  `axis=1` columns, 3-D `axis=0`, 2-D `axis=None` (2.x inverse reshaped to the input shape, 1.x flat),
  structured with `axis=0`, object with axis → TypeError, empty input, timedelta NaT; on 2.4.6 `unique_values`
  (unsorted), `unique_counts`, `unique_inverse`, `unique_all` (sorted, first-occurrence indices, NaNs kept
  separate as documented), `unique(sorted=False)`.
- `intersect1d` (incl. `assume_unique`, `return_indices` = first occurrences in both inputs), `union1d`,
  `setdiff1d` (sorted by default; input order with `assume_unique=True`), `setxor1d`, 2-D and empty inputs,
  strings, floats. NaN never matches itself in any set operation (recorded).
- `isin` / `in1d` (1.x) for kind None / 'sort' / 'table' (1.24+) against `set` membership on 2-D int input,
  `invert`, `assume_unique`, the 2-element loop path and a 600-element element array, negative-only table,
  1e6-wide table range with out-of-range probes, bool table, float table → ValueError, int8 full-range table →
  explicit RuntimeError, NaN never matches, int/float mixes by value, strings, empty, scalar element.
- `argmax` / `argmin`: first occurrence on ties (flat, axis 0/1, keepdims, Fortran copy, `out=`), first NaN wins
  (float64/float32, per axis), −0.0/0.0 first occurrence, complex lexicographic and complex NaN, unicode, bytes,
  bool (first True / first False), uint64/int64 extremes, datetime (NaT wins), empty → ValueError;
  `nanargmax`/`nanargmin` ignore NaN, per axis, all-NaN array and all-NaN slice → ValueError.
- `max`/`min` propagate NaN (whole, per axis, −NaN, float32); `nanmax`/`nanmin` ignore NaN, documented ±inf
  examples, all-NaN slice → NaN + RuntimeWarning (none when a value exists), empty → ValueError, `initial=`
  semantics, `where=`.
- `nonzero` in C order on C- and Fortran-ordered input, `flatnonzero`, `argwhere` (0-d shapes), `where(cond)`,
  `count_nonzero` with axis / tuple axis / keepdims / NaN / strings, `extract` == `arr[cond]` ==
  `compress(ravel)`, `compress` along axes with truncation and IndexError on a longer condition.
- `sort_complex` order and output dtypes (int8/16 → complex64, others → complex128, complex64 kept); `msort`
  (no warning on 1.23, DeprecationWarning on 1.24/1.26, removed on 2.4.6); `digitize` on decreasing bins for
  both `right` settings against the documented tables (fixed and 500 random values), increasing bins,
  non-monotonic → ValueError, NaN (→ len(bins) increasing / 0 decreasing), 2-D `x`; `trim_zeros` 'fb'/'f'/'b',
  all zeros, list input, NaN, −0.0, 2-D with `axis` (2.4.6); `bincount` vs `Counter`, `minlength`, weights,
  negative → ValueError, float ndarray → TypeError, 2-D → ValueError, empty, uint8/int8/bool.
- Integer and float extremes across sort / argsort / unique / partition / searchsorted / argmax.
- n = 1e6: int64 with ~1000 ties and float64 with 1000 NaN and 500 −0.0 for all four kinds equal Python's
  `sorted()` (stable kinds: the exact stable permutation), 1e6 float32, 1e6 int16 (radix), 2e5 strings, plus
  partition / searchsorted / unique with counts on the 1e6 data.

## Not checked and why

- `np.max`/`np.min` on unicode arrays: the `maximum` ufunc has no string loop on any build (UFuncTypeError);
  recorded, `argmax` on strings is checked instead.
- `np.sort(descending=)` and `np.top_k`: only on numpy main, not in the 2.4.6 release.
- StringDType (`np.dtypes.StringDType`) in `unique`/`sort`, masked arrays, `np.ma` sorting: outside the task list.
- `nanargmax` on a slice of only NaN and −inf: the docs say the result "cannot be trusted"; the value (0) is
  recorded, not judged.
- `searchsorted` on descending / unsorted `a` and NaN in set operations: undefined / undocumented; recorded only.
- Which of −0.0 / 0.0 `unique` keeps and which permutation quicksort/heapsort produce on ties: undocumented;
  recorded per build (they differ between builds as the quicksort implementation changed).
- On 1.23.5 the `RandomState.choice(replace=False)` stream differs, so the 1e6 float data has 999 NaNs there
  (a NaN position was overwritten by −0.0); the check counts NaNs from the data, so it is unaffected.
