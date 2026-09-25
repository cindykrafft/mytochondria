# n13_dtypes_datetime_strings_io_ma — notes

Harness: `audits/numpy/verify/n13_dtypes_datetime_strings_io_ma.py` (about 300 checks; the 1.x builds run fewer
because the `np.strings` / StringDType / NEP 51 checks exist only in 2.x). Truths: a plain-Python proleptic
Gregorian calendar (`days_from_civil` / `civil_from_days`, H. Hinnant) cross-checked against
`datetime.date.toordinal` and `calendar.isleap`; `fractions.Fraction` for exact unit arithmetic; a plain-Python
business-day calendar (weekmask plus holiday set, every roll mode written out); Python's `str` / `bytes` methods;
`decimal.Decimal` (2000 digits, ROUND_HALF_EVEN) for float formatting; a hand-written `.npy` header parser and
writer, `struct.pack` and `zipfile` for the binary formats; `ctypes.Structure` for C struct layout; plain-Python
dict joins for `join_by`; Fraction statistics and a Fraction normal-equation solver for `np.ma`. The harness sets
`TZ=IST-5:30` (a fixed +05:30 zone that glibc parses without tzdata) before importing numpy, so that
`timezone='local'` has a known offset. No scipy anywhere.

Builds: numpy 2.4.6 (`.out`), 1.23.5, 1.24.4, 1.26.4 (`.v<ver>.out`). Runtime about 1 s per build.
Also run for reference only (no `.out` deliverable): the numpy main dev build in `$S/np/venv-dev`
(2.6.0.dev0+git20260925.5551144). That run is quoted below where it shows whether a FAIL is already fixed on main.

Counts: 2.4.6: 285 ok / 20 FAIL. 1.26.4: 260 ok / 15 FAIL. 1.24.4: 259 ok / 16 FAIL. 1.23.5: 259 ok / 16 FAIL.
(main dev: 293 ok / 12 FAIL.)

## FAIL lines

### `FAIL a 2020 timestamp written with >= 10 fraction digits (ps/fs/as, ...) is stored exactly or raises, never a silently different date`: all builds (and main)

Measured: `np.datetime64('2020-03-04T05:06:07.1234567890')` picks the unit `ps`, as documented ("The unit for internal
storage is automatically selected from the form of the string"). It stores −3121623215564649976, where the true count
is 1583298367123456789000 ps (> 2**63), and prints as `1969-11-25T20:52:56.784435350024`. With 13 digits (`fs`) it
prints `1969-12-31T22:51:16.53…`. With 16 digits (`as`) it prints `1970-01-01T00:00:08.60…`. The same string with a
1970-01-01 date is stored exactly.
Library: `numpy/_core/src/multiarray/datetime.c`, `NpyDatetime_ConvertDatetimeStructToDatetime64`, does plain int64
arithmetic with no overflow check, e.g. `case NPY_FR_ps: ret = ((((days * 24 + dts->hour) * 60 + dts->min) * 60 +
dts->sec) * 1000000 + dts->us) * 1000000 + dts->ps;` (signed overflow, which is undefined behaviour in C).
Docs: the unit table gives the ps/fs/as span as "[1969 AD, 1970 AD]". Nothing says that parsing a string outside the
span of the inferred unit gives a wrapped value.
Verdict: **bug**. Unit inference picks a unit that cannot hold the date, and the value then wraps silently to an
unrelated date. Present on every build and still on main.

### `FAIL dates outside the documented ns span [1678, 2262] (and ps span) are rejected or exact, not wrapped (constructor and astype)`: all builds (and main)

Measured: `np.datetime64('2263-01-01', 'ns')` gives `1678-06-12T00:25:26.290448384`,
`np.datetime64('1677-01-01', 'ns')` gives `2261-07-22T23:34:33.709551616`, and `np.datetime64('1971-01-01', 'ps')`
gives `1969-10-30…`. On 2.4.6 and 1.x, `np.datetime64('2263-01-01').astype('M8[ns]')` also wraps. Only the D→ps cast
raised `OverflowError`.
Library: the constructor goes through the same unchecked `NpyDatetime_ConvertDatetimeStructToDatetime64` as above.
The astype path is the unit-scaling cast in `datetime.c`, which has no overflow check in the released builds.
Docs: the "Time span (absolute)" column gives ns as "[1678 AD, 2262 AD]".
Verdict: **bug** (silent wrap-around). On main, `astype` now raises `OverflowError` for all three dates (the dev run
prints `EXC OverflowError`). The constructor still wraps, so the check still FAILs on main.

### `FAIL one second past the 's' range raises instead of silently becoming NaT (2**63 wraps to the NaT sentinel -2**63)`: all builds (and main)

Measured: `np.datetime64('292277026596-12-04T15:30:07', 's')` is exactly 2**63−1 (checked ok). One second later the
value wraps to −2**63, which is the NaT sentinel, so the result is `NaT`, with no error or warning.
Library: same unchecked conversion as above.
Docs: the 's' span is "[2.9e11 BC, 2.9e11 AD]"; NaT is documented only as a parsed or explicit value.
Verdict: **bug** (edge of the int64 range). A valid-looking timestamp becomes missing data silently.

### `FAIL datetime64(2**63-1, 'Y') (year 1970+2**63-1 > int64 max, inside the documented 'Y' span of +-9.2e18 years) prints its year`: all builds (and main)

Measured: `str(np.datetime64(v, 'Y'))` equals `str(1970 + v)` for v = 10**18 and v = 2**63−1−1970 (ok). For
v = 2**63−1 it prints `'-9223372036854773839'`; the true year is 9223372036854777777.
Library: `datetime.c`, `NpyDatetime_ConvertDatetime64ToDatetimeStruct`: `case NPY_FR_Y: out->year = 1970 + dt;`,
which overflows int64 for the top 1970 values.
Docs: the 'Y' span is "[9.2e18 BC, 9.2e18 AD]".
Verdict: **bug** at the extreme edge of the range (low practical impact).

### `FAIL str() of a datetime64 with a negative year keeps 4 year digits after the sign (ISO 8601 expanded form, like the input '-0001')`: all builds (and main)

Measured: `str(np.datetime64('-0001-03-01'))` is `'-001-03-01'`, `-0004-02-29` prints `'-004-02-29'`, and
`-0100-02-28` prints `'-100-02-28'`. `-9999-01-01` and positive years are fine. The stored values equal the
proleptic Gregorian `days_from_civil` (checked ok), and the printed string parses back to the same date (checked ok).
Library: `numpy/_core/src/multiarray/datetime_strings.c`, `make_iso_8601_datetime`:
`snprintf(substr, sublen, "%04" NPY_INT64_FMT, dts->year)`. The `%04` width counts the minus sign.
Docs: datetimes are "ISO 8601"; years BC use astronomical numbering. ISO 8601 expanded years are a sign plus at least
four digits.
Verdict: **cosmetic bug** (non-ISO output for years −999..−1; round-trips inside numpy).

### `FAIL timedelta64 // int follows floor_divide ('largest integer smaller or equal', == Python timedelta // int)`: all builds (and main)

Measured: for `m8[us]` values [−7, −1, −13, …] divided by 2, `//` gives [−3, 0, −6], but floor gives [−4, −1, −7].
The scalar `np.timedelta64(-7, 'us') // 2` is also −3. `timedelta // timedelta` does floor correctly (checked ok for
11 values × 8 divisors, including remainder and divmod), so the integer divisor path is the odd one out.
Library: `numpy/_core/code_generators/generate_umath.py`, `'floor_divide'`:
`TypeDescription('m', FullTypeDescr, 'mq', 'm', cfunc_alias='divide', dispatch='loops_arithmetic_timedelta')`. The
m8 // int64 loop is the true-division loop `TIMEDELTA_mq_m_divide` in `loops_arithmetic_timedelta.dispatch.cpp`,
which computes `in1 / in2` (C truncation) and, on the SIMD path, `simd_trunc_divide_s64`.
Docs: the `floor_divide` docstring says "Return the largest integer smaller or equal to the division of the inputs. It
is equivalent to the Python // operator". Python's `timedelta(microseconds=-7) // 2` is −4 µs.
Verdict: **bug** (wrong rounding for negative timedeltas; the same `//` with a timedelta divisor floors). Present on
every build and on main.

### `FAIL np.char.upper / swapcase / title: 'Calls str.upper element-wise' also when the mapping lengthens the string` and the same line for `np.strings`: all builds (np.strings: 2.4.6; both on main)

Measured: on the default `U1` dtype, `upper(['ß', 'ﬁ', 'ŉ'])` gives `['S', 'F', 'ʼ']`; Python gives
`['SS', 'FI', 'ʼN']`. `swapcase('ß')` gives `'S'`, and `title('ﬁx')` (U2) gives `'Fi'`; Python gives `'Fix'`. With a
wide enough dtype the results are right (the U60 generic run passes all case-mapping calls, including 'straße' →
'STRASSE').
Library: `numpy/_core/strings.py` (2.x) and `defchararray.py` (1.x): `upper` is
`_vec_string(a_arr, a_arr.dtype, 'upper')`. It calls `str.upper` but writes into an array of the input's dtype, so a
longer result is truncated.
Docs: "Calls `str.upper` element-wise"; returns "Output array of `StringDType`, `bytes_` or `str_` dtype". Nothing
about truncation.
Verdict: **documentation gap / silent truncation**. Full Unicode case mapping can lengthen a string, and the
fixed-width result silently loses characters. StringDType does not have this problem (its generic run passes
upper/title/swapcase).

### `FAIL np.strings on StringDType: the same 70 calls equal Python str methods`: 2.4.6 (and main)

Measured: the only differing call is `lstrip('ǆ ')`. With StringDType it leaves `' '` and `'  padded  '` unchanged,
where Python strips the spaces; the fixed-width `U` path is correct. A probe shows the pattern: stripping fails
whenever a multi-byte UTF-8 character comes *before* an ASCII character in `chars` (`'é '` fails, `' é'` works). The
same failure hits `rstrip` / `strip` (`'aé '.rstrip('é ')` returns `'aé '`; Python returns `'a'`).
Library: `numpy/_core/src/umath/string_buffer.h`, `string_lrstrip_chars`: for UTF-8, when the current character is
one byte, it searches `CheckedIndexer<char> ind(buf2.buf, len2); res = find_char<char>(ind, len2, *traverse_buf);`
with `len2 = buf2.num_codepoints()`. That means it scans only the first *code-point-count* bytes of the UTF-8
`chars` buffer. For `'é '` (3 bytes, 2 code points), the space in byte 3 is never seen.
Docs: `np.strings.lstrip`: "Calls `str.lstrip` element-wise … chars … characters to be removed".
Verdict: **bug** in StringDType strip with a non-ASCII `chars` argument. Present in 2.4.6 and in main.

### `FAIL np.strings.partition / rpartition accept a plain str separator for a StringDType array`: 2.4.6 only

Measured: `np.strings.partition(stringdtype_array, ' ')` raises
`UFuncTypeError(<ufunc '_partition'>, (StringDType, StrDType, …))`. Passing the separator as a StringDType array
works, and `add` / `replace` / `find` accept a plain `str` operand.
Docs: "sep : array-like, with `StringDType`, `bytes_`, or `str_` dtype".
Verdict: **bug** (missing promotion), fixed on main: the dev run passes. It is probably part of "ENH: add NEP-50 style
semantics for string scalars and StringDType (#32040)" (not verified which commit).

### `FAIL na_object=nan comparisons: == and < False, != True ...` and `FAIL na_object=None: a missing entry is not equal to the empty string`: 2.4.6 only

Measured (2.4.6): for `arr = ['hello', nan, 'world']` with `StringDType(na_object=np.nan)`, `arr != 'hello'` gives
`[False, False, True]` and `arr != arr` gives `[False, False, False]`, so a NaN-like missing value is neither `==` nor
`!=`. With `na_object=None`, `[None, ''] == ''` gives `[True, True]`: the missing value compares equal to the empty
string.
Docs: the main-branch user guide (`basics.strings.rst`) says "equality and ordered comparisons involving a NaN-like
sentinel return False, while inequality returns True" (`arr != "hello"` → `[False, True, True]`). That text and the
fix arrived together in "ENH: fixes for StringDType sorting and comparisons for missing data (#32564)" (2026-09-17,
not in any release tag). Its upcoming-changes note says "Previously, both equality and inequality returned False …
Comparisons also correctly distinguish None-like missing values from empty strings."
Verdict: **bug in the released 2.4.6, acknowledged and fixed upstream** (main passes both checks).

### `FAIL 'S' -> StringDType with invalid UTF-8 bytes: 'a UnicodeDecodeError is raised during the cast'`: 2.4.6 only

Measured: `np.array([b'\xff', b'ok']).astype(StringDType())` succeeds. `np.strings.str_len` of the result then returns
`[0, 2]`, and the error appears only later, on `tolist()` / `repr` (`UnicodeDecodeError`). So the array stores invalid
UTF-8.
Docs: `basics.strings.rst`: "The bytes stored in a `numpy.bytes_` array must be valid UTF-8, and a
`UnicodeDecodeError` is raised during the cast if they are not."
Library (main): `stringdtype/casts.cpp`, `fixed_width_bytes_to_string` now validates with
`num_codepoints_for_utf8_bytes(...)` and raises. The check was added by "BUG: validate UTF-8 and harden StringDType
bounds handling (#32296)", which is on main only.
Verdict: **bug in 2.4.6 (docs promise validation), fixed on main.**

### `FAIL np.char.replace / np.strings.replace with old / new longer than the array itemsize == str.replace` and `FAIL np.char.partition / np.strings.partition ... separator longer than the array itemsize`: 2.4.6 only

Measured (2.4.6): `replace(['a', 'ab'], 'abc', 'x')` gives `['a', 'x']`: `'abc'` was truncated to the array's `U2`,
so `'ab'` matched and was replaced. `replace(['ab'], 'b', 'xyzw')` gives `['axy']`; Python gives `'axyzw'`.
`replace([b'a'], b'abc', b'x')` gives `[b'x']`. `partition(['ab'], 'abc')` gives `('', 'ab', '')`, and
`rpartition` gives the same; Python gives `('ab', '', '')` and `('', '', 'ab')`. `np.char.replace` / `np.char.partition`
delegate to `np.strings` in 2.x, so both namespaces fail. On 1.26.4 the `np.char` results are correct.
Library (2.4.6 `numpy/_core/strings.py`): `old = old_arr.astype(old_dtype or a_dt, copy=False)` /
`new = new_arr.astype(new_dtype or a_dt, copy=False)`, and in `partition` / `rpartition`
`sep = sep_arr.astype(a_arr.dtype, copy=False)`. These cast the pattern to the *input's itemsize*, which truncates it.
Fixed on main by "BUG: fix np.strings.replace truncating old/new to a's itemsize (#32519)" (`a_dt.char` instead of
`a_dt`).
Docs: "For each element in `a`, return a copy of the string with occurrences of substring `old` replaced by `new`."
Verdict: **bug (silently wrong results) in 2.0–2.4.x, regression against 1.x, fixed on main.** Note that the generic
U60 run cannot see it: the bug only appears when the pattern is longer than the array's itemsize, which is common for
tight inferred dtypes.

### `FAIL np.char.ljust / rjust / center with width < len(s) return s unchanged (str.ljust semantics)`, `FAIL np.char on unicode (...)` / `FAIL np.char on bytes (...)` and the two `... with the tight inferred itemsize` lines: 1.23.5, 1.24.4, 1.26.4

Measured (1.x): `np.char.ljust(['abcdef'], 2)` gives `'ab'`, `rjust(.., 3)` gives `'abc'` and `center(.., 4)` gives
`'abcd'`. Python returns `'abcdef'` unchanged. In the generic runs, 9 unicode and 7 bytes calls differ, all of them
`ljust` / `rjust` / `center` / `zfill` with a width smaller than some element (`zfill(6)` of `'hello world'` gives
`'hello '`). These are the only generic differences on 1.x. The unicode count includes `center(12, 'é')`, which the
bytes run skips.
Library (1.26.4 `numpy/core/defchararray.py`, `ljust`): `size = int(numpy.max(width_arr.flat))` then
`_vec_string(a_arr, type(a_arr.dtype)(size), 'ljust', (width_arr, fillchar))`. The output width is `max(width)`, not
`max(width, len)`, so the result of `str.ljust` is truncated. `zfill` has the same `size = int(numpy.max(width_arr.flat))`.
Docs: "Calls `str.ljust` element-wise."
Verdict: **bug in 1.x, fixed in 2.0** (`np.strings.ljust`: `width = np.maximum(str_len(a), width)`; all 2.x runs pass).
The five FAIL lines on each 1.x build are the same root cause.

### `FAIL documented: tzinfo ZoneInfo('US/Eastern') crosses the DST boundary (-0400 -> -0500)`: 1.23.5, 1.24.4, 1.26.4

Measured: `np.datetime_as_string(d, timezone=ZoneInfo('US/Eastern'))` raises `ValueError: fromutc: dt.tzinfo is not self`
on 1.x. On 2.4.6 it gives the documented `['2002-10-27T00:30-0400', '2002-10-27T01:30-0400', '2002-10-27T01:30-0500',
'2002-10-27T02:30-0500']`.
Library (≤ 2.3): `get_tzoffset_from_pytzinfo` called `timezone_obj.fromutc(naive_datetime)` (the pytz convention).
Main and 2.4 call `dt.astimezone(timezone_obj)` on a UTC-aware datetime ("TST: migrating from pytz to zoneinfo +
tzdata", commit 21c2e707da, first in v2.4.0).
Docs (1.26.4 docstring): "timezone : {'naive', 'UTC', 'local'} or tzinfo … If a tzinfo object, then do as with
'local'". The example uses `pytz`.
Verdict: **bug in 1.x (a standard-library tzinfo is rejected although "tzinfo" is documented), fixed in 2.4.0.**
Harness note: this machine's tzdata has no `US/Eastern` link, so on every build the harness uses the identical zone
`America/New_York` and says so in the output. The 1.x error comes from `fromutc` and does not depend on the zone name.

### `FAIL busday_count == valid days in [begin, end); when end < begin, minus the valid days in (end, begin]`: 1.23.5, 1.24.4

Measured: for reversed ranges the 1.23/1.24 count is off by one whenever `enddates` or `begindates` is a valid day.
Example: begin 2011-09-26 (Monday), end 2011-09-25 (Sunday), weekdays mask: 1.24 gives 0, and the documented rule
gives −1.
Docs: "Counts the number of valid days between `begindates` and `enddates`, not including the day of `enddates`. If
`enddates` specifies a date value that is earlier than the corresponding `begindates` date value, the count will be
negative."
Library: fixed in 1.25 (`datetime_busday.c`: "we swapped date_begin and date_end, so we need to correct for the
original date_end that should not be included. gh-23197": `date_begin++; date_end++;`). The 1.25.0 release notes say
"Previously, the `enddates` was included, even though the documentation states it is always excluded" (gh-23229).
Verdict: **bug in ≤ 1.24, fixed in 1.25** (1.26.4 and 2.4.6 pass on 1,800 random pairs).

### `FAIL int8 masked array with the default fill value: filled() gives 999999 (the documented int default) or refuses, not a wrapped in-range value`: all builds (and main)

Measured: `ma.array([1, 2], mask=[0, 1], dtype=np.int8).fill_value` reports `999999` (as int64), but `.filled()` returns
`[1, 63]`: 999999 mod 256 = 63. No warning is raised. Passing the same value explicitly,
`ma.array(..., dtype=np.int8, fill_value=999999)`, raises `TypeError: Cannot convert fill_value 999999 to dtype int8`
on 2.4.6.
Library: `numpy/ma/core.py`, `_check_fill_value`: for `fill_value is None` it returns `default_fill_value(ndtype)`
without casting it to the dtype (only unsigned kinds are adjusted). `MaskedArray.filled` then does
`np.copyto(result, fill_value, where=m)`, and the default `same_kind` casting from int64 to int8 wraps.
Docs: `default_fill_value` table: "int 999999". Nothing covers integer dtypes that cannot hold it.
Verdict: **bug / documentation gap**. The default sentinel for int8 (by the same arithmetic, int16 would get
999999 mod 65536 = 16959; not run) silently becomes an ordinary in-range value, so filled data cannot be told apart from real data, while the same explicit value is
rejected.

### `FAIL ma.cov(2-D x) with different row masks: off-diagonal == covariance over the columns unmasked in both rows`: all builds (and main)

Measured: x = [[1, 2, 3, 4, --], [--, 1, 4, 3, 6]]. `ma.cov(x)[0, 1]` = 0.375. The covariance over the three
jointly observed columns is 1.0.
Library: `numpy/ma/extras.py`, `_covhelper`: `x -= x.mean(axis=rowvar)[tup]` centres each row on the mean of *its own*
unmasked values, and `cov` divides `dot(filled(x, 0), filled(x.T, 0))` by `dot(xnotmask, xnotmask.T) - ddof` (the
joint count). The common-mask step ("if y.shape == x.shape: common_mask = np.logical_or(xmask, ymask)") runs only when
`y` is given. Accordingly `ma.cov(x, y)` with separate 1-D inputs is exactly the pairwise-complete covariance (checked
ok).
Docs: "allow_masked : If True, masked values are propagated pair-wise: if a value is masked in `x`, the corresponding
value is masked in `y`", and "Except for the handling of missing data this function does the same as `numpy.cov`".
Neither says that with a single 2-D `x` each variable keeps its own mean.
Verdict: **documentation gap** (the single-array estimator is a hybrid: own means, joint counts) that feeds the next
FAIL.

### `FAIL ma.corrcoef(2-D x) stays within [-1, 1] (a Pearson coefficient)`: 2.4.6 (and main); ok on 1.x

Measured: `ma.corrcoef([[4, -2, 4], [--, -3, 4]])[0, 1]` = 1.2247 on 2.4.6. The two jointly observed columns
(−2, −3) and (4, 4) have r = 1, and 1.23.5 / 1.24.4 / 1.26.4 return 1.0. A random search found values up to 2.84.
Library: since 2.1.0 `corrcoef` is `corr = cov(x, y, rowvar, …); std = ma.sqrt(ma.diagonal(corr)); corr /=
ma.multiply.outer(std, std)`. The hybrid covariance above (own means, joint counts) is divided by standard deviations
computed over each variable's own observations, so Cauchy–Schwarz no longer bounds the ratio. Up to 1.26 the
denominator was computed pairwise (`mask_cols(vstack((x[i], x[j]))).var(axis=1)`), which kept |r| ≤ 1.
Docs: the 2.1.0 release notes (gh-26285) say "`ma.corrcoef` may return a slightly different result … in cases where
the observations between a pair of variables are not aligned".
Verdict: **bug (regression in 2.1)**. The change is announced as "slightly different", but it produces correlation
coefficients outside [−1, 1] whenever the masks of two rows differ.

## Things recorded as `ok` or printed that deserve a note

- Timezone-offset strings (`'2020-01-01T00:00+0100'`) are still converted to UTC. 1.x emits `DeprecationWarning`;
  2.x emits `UserWarning` (2.0.0 release note gh-24193: "now issues a UserWarning rather than a DeprecationWarning").
  The check is version-aware. `arrays.datetime.rst` still says "deprecated:: 1.11.0 … will raise an error in the
  future", which contradicts the 2.0 change (documentation lag).
- Timedelta division by a zero timedelta: `/` gives inf, `%` gives NaT, `//` gives 0, each with a RuntimeWarning.
  Python raises ZeroDivisionError. Recorded, since none of this is documented. `NaT // x` also gives 0 with an
  "invalid" warning.
- `timedelta64 / int` (true division) returns a timedelta truncated toward zero (−7 µs / 2 gives −3 µs). Python's
  `timedelta / 2` rounds half-even and gives −4 µs. This is only printed: numpy documents no rounding for m8 / int.
- NaT handling of the busday functions: `is_busday(NaT)` is False, while `busday_offset(NaT, …)` and
  `busday_count(NaT, …)` raise ValueError. Only NaT *holidays* are documented (ignored, checked ok).
- `.item()` outside Python's datetime range returns the raw int count (year 10000 gives 2932897 days, year 0 gives
  −719163). The docs' conversion table does not mention this case. Recorded ok as consistent with the source
  (`convert_datetime_to_pyobject` falls back to int).
- `np.char.startswith(['abc'], ('a', 'x'))` broadcasts the tuple as an array of prefixes (`[True, False]`). This
  differs from `str.startswith`'s any-of semantics, but it matches the documented "prefix : array_like".
- `np.char.equal` strips trailing whitespace (documented numarray compatibility); ndarray `==` does not.
- Printing: a default array `repr` is not an `eval` round trip (precision 8, `maxprec`: 5 of 3,004 random doubles
  survive). With `floatmode='unique'` the round trip is bit-exact for float64 and float32. The scalar `str()` is
  always shortest (== Python `repr` for every value tested).
- `StringDType.astype(np.str_)` (unsized) raises TypeError on 2.4.6. The size-inferring cast shown in the main-branch
  user guide arrived with #32097 on main, so only the explicit-size cast is checked.
- `np.strings.str_len` on a NaN-like or None missing value raises `ValueError: The length of a null string is
  undefined`. Printed only; the docs say nothing.
- `ma.array([1, 2], mask=[1, 1]).argmax()` gives 0 (undocumented choice for an all-masked input).
- `savetxt(header='a,b\nsecond', newline='\r\n')`: the `\n` inside the header is written as given and followed by the
  comment prefix; only the line ends that numpy writes use `newline`. Expected from the source (`header.replace('\n',
  '\n' + comments)`), and the docs define `newline` as the row separator.

## What held up (all four builds unless stated)

- datetime64: unit inference for Y/M/D/h/m/s/ms/us/ns strings; stored values in 9 units for 7 timestamps (pre-1970,
  year 1, 1600-02-29, 9999-12-31) equal floor((t − epoch)/unit); the week unit is Thursday-anchored; all 801 years
  1600–2400 agree with `calendar.isleap` (day counts and Feb-29 parsing); 3,000 random dates in 1..9999 equal
  `toordinal() − 719163`, and `str` equals `isoformat`, `tolist` equals `date`; astronomical years (0 and −4 leap,
  −100 not) equal `days_from_civil`; the documented 1600 − 0000 and leap-second examples; invalid dates raise.
- Unit arithmetic: timedelta addition promotes to the finer unit with exact values for 10 unit pairs; D − s gives s;
  Y/M against D raise TypeError; the unsafe Y/M → D cast equals floor(n·146097/400) and floor(n·146097/4800) days
  (the documented 400-year average), including negatives; M8[M] ± k months for 1990–2030; D/s → W/h conversions floor
  toward −inf; `promote_types` for Y/M, D/W and 7D/3D.
- NaT: != / == / ordering semantics, propagation through arithmetic, min / max / maximum; sort and argsort put NaT
  last.
- datetime_as_string: documented examples, 'UTC' → Z, 'local' under a fixed +05:30 TZ equals Python `astimezone`,
  ZoneInfo DST offsets (2.4.6), pre-epoch floor to D, `casting='safe'` error, NaT.
- Business days: `is_busday`, `busday_count` and `busday_offset` in all 7 roll modes agree with the plain-Python
  calendar for 6 weekmasks × 300 dates × 25 random holidays (count only from 1.26 on, see FAIL); all documented
  examples; the five weekmask spellings agree; abbreviations are case-sensitive; holidays in any order with NaT
  ignored; busdaycalendar normalisation; argument conflicts and all-zero weekmask raise.
- Timedelta `//`, `%`, `divmod` and `/` between timedeltas equal Python int floor semantics and correctly rounded
  ratios; `datetime_data`; the `m8[25s]` multiple unit; `.item()` follows the documented type table and is exact at
  Python's limits (date(1,1,1), datetime max, ±999,999,999 days).
- Strings: 70 unicode and 65 bytes method calls (case maps on non-ASCII, justification with non-ASCII fill, zfill with
  signs, strip with chars, find / rfind / count / index / rindex with negative and out-of-range start/end,
  startswith / endswith with ranges, replace with count 0 / 1 / −1 / 2 and empty `old`, split / rsplit with maxsplit,
  partition / rpartition, all nine `is*` predicates on unicode spaces (U+001C, U+00A0, U+3000, U+200B), superscripts,
  vulgar fractions, Arabic-Indic digits and titlecase digraphs, expandtabs, splitlines) equal Python on 2.4.6 in both
  `np.char` and `np.strings`, at wide and tight itemsizes; str_len, add, multiply (0 / −1 / 3), encode / decode
  including errors='replace', `mod` formatting, join, translate, `np.strings.slice`; fixed-width rules (trailing
  spaces kept, trailing NULs dropped, interior NULs kept, chararray rstrip, code-point ordering, silent truncation on
  assignment); StringDType: coerce, casts to fixed width with an explicit size, V5 bytes, NaN sort order, isnan,
  string-sentinel semantics, None sort error.
- Text I/O: `savetxt('%.18e')` → `loadtxt` is bit-exact for 3,013 doubles (random bit patterns, subnormals, ±0, ±inf,
  nan) and for float32; the written text equals Python's `'%.18e' % x`; loadtxt comments (single, list, None),
  skiprows counting comments, usecols (negative, int), dict and callable converters, unpack, quotechar with doubled
  quotes, max_rows not counting comments or blank lines, ndmin, structured dtype, complex, encoding, wrong column
  count; savetxt fmt sequence / multi-format string / header / footer / comments / newline / complex / structured;
  genfromtxt names=True, dtype=None inference, default fillers (−1, nan), per-column missing_values and
  filling_values, usemask, skip_header / skip_footer, fixed-width delimiters with autostrip, usecols by name,
  invalid_raise both ways, structured dtype, names string, defaultfmt, exact `%.18e` parsing, inline comments.
- Binary I/O: `.npy` headers for 23 dtypes (including '>i4', '>f8', longdouble, clongdouble, M8[ns], m8[s], V4) follow
  the v1.0 spec exactly (magic, uint16 length, sorted dict literal, '\n' terminator, 64-byte alignment); data is the
  C-order bytes, equal to `struct.pack` for int32; Fortran order is stored column-major and reloaded F-contiguous;
  shapes (), (0,), (0,3); nested structured dtype with a subarray; object arrays and `allow_pickle` on both save and
  load; a hand-written big-endian Fortran file loads; unicode field names switch to v3.0 and a 3,000-field header to
  v2.0; mmap_mode='r'; savez / savez_compressed member names, ZIP_STORED vs ZIP_DEFLATED with identical members,
  NpzFile laziness / `.files` / `.f` / `.npy` suffix / close / arr_0 conflict / pickled members; tofile / fromfile
  (count, offset, text sep / format); frombuffer (offset, count, read-only on bytes, writeable view on bytearray,
  size error); fromstring text mode; binary mode and bad data are version-aware (DeprecationWarning ≤ 2.2, ValueError
  from 2.3).
- Printing: every floatmode, suppress_small, threshold / edgeitems, sign, legacy '1.13' / '1.21' / '1.25' (NEP 51
  scalar repr), printoptions context and set_printoptions; shortest float32 strings for 2,991 random float32 are
  minimal-length and round-trip; `format_float_positional` / `format_float_scientific` with `unique=False` equal the
  Decimal half-even rounding (about 3,600 positional and 3,000 scientific cases); trim modes, padding, min_digits, exp_digits,
  fractional=False, exact large integers.
- Structured arrays: align=True offsets, itemsize and alignment equal `ctypes.Structure` for 300 random nested
  layouts with subarrays; packed offsets; dict-form offsets; dtype equality rules; titles; field views; padded
  multi-field views and repack_fields; positional assignment; nested and subarray access; recfunctions
  (structured_to_unstructured incl. nested, unstructured_to_structured, append_fields with masking, merge_arrays
  padding −1 and flatten, join_by inner / outer / leftouter against dict joins with a1/a2 renaming, drop / rename,
  stack_arrays); recarray attribute access, attribute-name precedence, np.rec.array, views, nested recarrays.
- np.ma: sum / mean / var(ddof=1) / std / median / weighted average / min / max / count over 60 random masked 2-D
  arrays on axis None/0/1 equal Fraction truths on the unmasked data, and fully masked slices give `masked`; average
  `returned=True`; even-count median; int mean dtype; prod and cumsum; union mask propagation; domain masking for
  log / divide / sqrt / arccos with no warnings, plus plain `np.log` on a MaskedArray; the fill-value table; filled /
  compressed; masked_where / invalid / equal / values / inside / outside / greater / less_equal; cov / corrcoef of
  (x, y) as pairwise-complete statistics; sort with endwith; argsort; argmax / argmin skipping masked values; unique;
  concatenate / stack / vstack / hstack / column_stack, and the documented loss of masks in plain `np.concatenate`;
  slice mask views in both directions; hard / soft masks; nomask; polyfit on jointly unmasked points (1-D and 2-D y)
  equal to the exact least-squares fit.

## Not checked, and why

- Leap seconds, TAI and the 'now' / 'today' values: the docs declare the first two unsupported, and 'now' / 'today'
  depend on the clock (only their units are checked).
- `datetime_as_string` with pytz: pytz is not installed in any venv; ZoneInfo covers the tzinfo path.
- Locale-dependent behaviour of the bytes case functions ("For 8-bit strings, this method is locale-dependent"): the
  harness runs in the C locale only.
- `np.load` of files written by other numpy versions, and memmap writes; `genfromtxt` with `converters` on bytes, and
  the `loadtxt` legacy (1.22) parser.
- `np.ma` data values at masked positions: the docs say they "should not" be relied on.
- The main-branch dev build is not a deliverable build. It is quoted only to classify FAILs as fixed or still present
  upstream.
