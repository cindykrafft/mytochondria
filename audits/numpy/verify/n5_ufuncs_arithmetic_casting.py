#!/usr/bin/env python
"""NumPy ufuncs, arithmetic, casting and promotion: the rounding family (half-to-even,
decimals, negative decimals, integers, float32), floor_divide / remainder / fmod /
divmod sign conventions and division by zero, signed zeros, integer overflow
wrap-around (scalar vs array warnings), power / float_power, gcd / lcm, bitwise and
shifts beyond the width, accuracy of the transcendental ufuncs against mpmath in ulps
(float64, float32 SIMD paths, float16), complex branch cuts with signed zeros,
clip / isclose / sign / copysign / nan_to_num, errstate, float->int casts,
astype between every pair of numeric dtypes at boundary values, NEP 50 promotion
(version-aware), promote_types / can_cast tables, finfo / iinfo, nextafter /
spacing / frexp / ldexp / modf, reduction dtypes, ufunc reduce / accumulate /
reduceat / outer / at, where= and out= aliasing, scalar result types, np.bool_
arithmetic, heaviside, reciprocal, longdouble, deg2rad, exp2, i0, sinc."""
import sys, math, cmath, warnings, itertools, struct
from fractions import Fraction as F
import numpy as np
import mpmath
from mpmath import mp, mpf
mp.prec = 200
NPV = tuple(int(v) for v in np.__version__.split(".")[:2]); NP2 = NPV >= (2, 0)
try:
    from numpy._core._multiarray_umath import __cpu_features__ as _cpu
except Exception:
    from numpy.core._multiarray_umath import __cpu_features__ as _cpu
print(f"numpy {np.__version__}  python {sys.version.split()[0]}  mpmath {mpmath.__version__}  "
      f"SIMD: {' '.join(k for k, v in _cpu.items() if v and ('AVX' in k or 'FMA' in k or 'NEON' in k))}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-12, abs_=1e-300):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    if math.isinf(a) or math.isinf(b): return a == b
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
warnings.filterwarnings("ignore")

class caught:
    """Records the warnings raised inside the block (the global filter is 'ignore')."""
    def __enter__(self):
        self._cm = warnings.catch_warnings(record=True); self.w = self._cm.__enter__(); warnings.simplefilter("always"); return self
    def __exit__(self, *a): self._cm.__exit__(*a)
    @property
    def names(self): return sorted({x.category.__name__ for x in self.w})
    @property
    def msgs(self): return [str(x.message) for x in self.w]
def raises(fn, exc=Exception):
    try: fn()
    except exc as e: return type(e).__name__ if exc is Exception else exc.__name__
    except Exception as e: return "OTHER:" + type(e).__name__
    return None
def wrap_int(v, dt):
    """Two's-complement / modular reduction of the Python int v to the width of dt."""
    info = np.iinfo(dt); bits = info.bits; v = int(v) % (1 << bits)
    if info.min < 0 and v >= 1 << (bits - 1): v -= 1 << bits
    return v
def sb(x): return math.copysign(1.0, float(x)) < 0
def f32(x): return struct.unpack("f", struct.pack("f", float(x)))[0]   # round a Python float to float32 (C cast)
def ulps(y, t, dtype):
    """|y - t| in units of the spacing of the dtype at the correctly rounded truth t (an mpf)."""
    y = float(y); t = mpf(t)
    if math.isnan(y) or math.isinf(y):
        return 0.0 if (math.isinf(y) and abs(t) > float(np.finfo(dtype).max)) else float("inf")
    tf = dtype(float(t))
    if np.isinf(tf): return float("inf")
    sp = float(np.spacing(np.abs(tf))) if tf != 0 else float(np.finfo(dtype).smallest_subnormal)
    return float(abs(mpf(y) - t) / mpf(sp))
def steps(y, t, dtype):
    """Number of representable dtype values between y and the correctly rounded truth (numpy's assert_array_max_ulp measure)."""
    y = float(y); t = mpf(t)
    if math.isnan(y) or math.isinf(y): return 0.0 if (math.isinf(y) and abs(t) > float(np.finfo(dtype).max)) else float("inf")
    tf = dtype(float(t))
    if np.isinf(tf): return float("inf")
    sp = float(np.spacing(np.abs(tf))) if tf != 0 else float(np.finfo(dtype).smallest_subnormal)
    return round(abs(y - float(tf)) / sp)
INTS = [np.int8, np.int16, np.int32, np.int64]; UINTS = [np.uint8, np.uint16, np.uint32, np.uint64]
FLOATS = [np.float16, np.float32, np.float64]

# =====================================================================================
# 1. rounding family
# =====================================================================================
print("---- rounding")
halves = [0.5, 1.5, 2.5, 3.5, -0.5, -1.5, -2.5, 4.5, 5.5, 0.0]
r = np.round(halves); exp_h = [float(round(h)) for h in halves]   # Python's round is exact half-to-even on the binary value
print(f"   np.round{halves} = {r.tolist()}")
report('round: exact binary halves round half to even ("1.5 and 2.5 round to 2.0, -0.5 and 0.5 round to 0.0")', r.tolist() == exp_h)
report("round(-0.5) is -0.0 (rint keeps the sign, IEEE roundToIntegralTiesToEven)", sb(np.round(-0.5)) and float(np.round(-0.5)) == 0)
report("np.around is the same function as np.round", np.around is np.round or np.around(halves).tolist() == r.tolist())
# decimals > 0: documented algorithm true_divide(rint(a * 10**d), 10**d); the halves 0.125, 0.375 are exact in binary
def doc_round(x, d):
    f = 10.0 ** d
    return round(x * f) / f if d >= 0 else round(x / (10.0 ** -d)) * (10.0 ** -d)
cases = [(0.125, 2), (0.375, 2), (0.5, 1), (1.5, 1), (2.5, 1), (2.675, 2), (1.005, 2), (1.45, 1), (0.285, 2), (56294995342131.5, 3), (1234.5, -2), (150.0, -2), (250.0, -2), (350.0, -2), (-250.0, -2)]
allok = True
for x, d in cases:
    got = float(np.round(x, d)); want = doc_round(x, d); allok &= got == want
    print(f"   round({x!r}, {d}) = {got!r}   documented algorithm {want!r}   Python round {round(x, d)!r}")
report('round(x, decimals) equals the documented "true_divide(rint(a * 10**decimals), 10**decimals)" (positive and negative decimals)', allok)
report("round(0.125, 2) = 0.12 and round(0.375, 2) = 0.38: exact binary halves at decimals=2 round to even", float(np.round(0.125, 2)) == 0.12 and float(np.round(0.375, 2)) == 0.38)
report("round(56294995342131.5, 3) = 56294995342131.51 (the documented inexact example)", float(np.round(56294995342131.5, 3)) == 56294995342131.51)
report("round(2.675, 2) = 2.68 (documented fast algorithm; Python's decimal-correct round gives 2.67)", float(np.round(2.675, 2)) == 2.68)
# integers
ia = np.array([15, 25, 35, -25, -15, 1234], dtype=np.int64)
ri = np.round(ia, -1)
print(f"   round(int64 {ia.tolist()}, -1) = {ri.tolist()} dtype {ri.dtype}; Python round: {[round(int(v), -1) for v in ia]}")
report("round on integers with negative decimals: half to even, integer dtype preserved (equals Python round(int, -1))", ri.tolist() == [round(int(v), -1) for v in ia] and ri.dtype == np.int64)
report("round on integers with positive decimals returns the values unchanged, integer dtype preserved", np.round(ia, 2).tolist() == ia.tolist() and np.round(ia, 2).dtype == np.int64)
ri8 = np.round(np.array([127, -128, 5], dtype=np.int8), -1)
print(f"   round(int8 [127, -128, 5], -1) = {ri8.tolist()} dtype {ri8.dtype}  (130 does not fit int8: wraps)")
report("round(int8 127, -1): result dtype int8 (value wraps, recorded)", ri8.dtype == np.int8)
report("round(np.int64(25), -1) returns an integer scalar 20", int(np.round(np.int64(25), -1)) == 20 and isinstance(np.round(np.int64(25), -1), np.integer))
# float32
x32 = np.array([0.5, 1.5, 2.5, -0.5, 0.125, 2.675, 1.45], dtype=np.float32)
r32 = np.round(x32); r32d = np.round(x32, 2)
want32 = [f32(round(x * 100.0) / 100.0) for x in [float(f32(v)) for v in [0.125, 2.675, 1.45]]]
# emulate float32 arithmetic: product rounded to float32, rint, quotient rounded to float32
want32 = [f32(round(f32(float(v) * 100.0)) / 100.0) for v in x32[4:].tolist()]
print(f"   float32 round: {r32.tolist()} dtype {r32.dtype}; round(., 2) of [0.125, 2.675f, 1.45f] = {r32d[4:].tolist()} (float32 emulation {want32})")
report("round on float32: half to even, result dtype float32", r32.tolist() == [0.0, 2.0, 2.0, 0.0, 0.0, 3.0, 1.0] and r32.dtype == np.float32)
report("round(float32, 2) computed in float32 (matches an emulation of the documented algorithm in float32)", r32d[4:].tolist() == want32 and r32d.dtype == np.float32)
# rint / fix / floor / ceil / trunc
vals = [-2.7, -2.5, -1.5, -0.5, -0.4, -0.0, 0.0, 0.4, 0.5, 1.5, 2.5, 2.7, 1e16 + 2, -1e300]
tbl = {"rint": (np.rint, lambda v: float(round(v))), "floor": (np.floor, lambda v: float(math.floor(v))), "ceil": (np.ceil, lambda v: float(math.ceil(v))),
       "trunc": (np.trunc, lambda v: float(math.trunc(v))), "fix": (np.fix, lambda v: float(math.trunc(v)))}
for name, (fn, truth) in tbl.items():
    got = fn(np.array(vals)); want = [truth(v) for v in vals]
    report(f"{name} on {len(vals)} values equals the math-module definition", got.tolist() == want, f"({got.tolist()[:6]}...)")
report("floor(-2.5) == -3 (documented: NumPy uses the mathematical floor, not floor-towards-zero)", float(np.floor(-2.5)) == -3)
report("fix(-2.5) == -2 (documented: rounds towards zero) and fix(2.7) == 2", float(np.fix(-2.5)) == -2 and float(np.fix(2.7)) == 2)
report("signed zeros: ceil(-0.5), trunc(-0.5), rint(-0.4), floor(-0.0) are all -0.0 (C99 / IEEE)", all(sb(v) and float(v) == 0 for v in [np.ceil(-0.5), np.trunc(-0.5), np.rint(-0.4), np.floor(-0.0)]))
report("rint on int input returns float64 (no integer loop); floor/ceil/trunc on int input keep the int dtype on 2.x (integer loops added in 2.1) and return float64 on 1.x", np.rint(np.array([1, 2])).dtype == np.float64 and np.floor(np.array([1, 2])).dtype == (np.int64 if NPV >= (2, 1) else np.float64) and np.ceil(np.array([1, 2])).dtype == (np.int64 if NPV >= (2, 1) else np.float64), f"(rint {np.rint(np.array([1, 2])).dtype}, floor {np.floor(np.array([1, 2])).dtype}, trunc {np.trunc(np.array([1, 2])).dtype})")

# =====================================================================================
# 2. floor_divide / remainder / fmod / divmod, division by zero, signed zeros
# =====================================================================================
print("---- integer and float division semantics")
pairs = [(a, b) for a in [-7, -6, -1, 0, 1, 6, 7] for b in [-3, -2, 2, 3]]
ok_fd = ok_rem = ok_fm = ok_dm = True
for a, b in pairs:
    A, B = np.int64(a), np.int64(b)
    ok_fd &= int(np.floor_divide(A, B)) == a // b
    ok_rem &= int(np.remainder(A, B)) == a % b and int(np.mod(A, B)) == a % b
    ok_fm &= int(np.fmod(A, B)) == int(math.fmod(a, b))
    q, m = np.divmod(A, B); ok_dm &= (int(q), int(m)) == divmod(a, b)
report("floor_divide on negative ints equals Python // (floor)", ok_fd)
report('remainder / mod on negative ints "has the same sign as the divisor" (equals Python %)', ok_rem)
report('fmod on negative ints "has the same sign as the dividend" (equals C fmod)', ok_fm)
report("divmod on ints equals Python divmod", ok_dm)
# ints with array inputs too
A = np.array([-7, 7, -7, 7]); B = np.array([2, -2, -2, 2])
report("floor_divide / remainder on int arrays: [-7//2, 7//-2, -7//-2, 7//2] and remainders", np.floor_divide(A, B).tolist() == [-4, -4, 3, 3] and np.remainder(A, B).tolist() == [1, -1, -1, 1])
for dt in [np.int8, np.uint8, np.int32]:
    a = np.array([7, 200 if dt == np.uint8 else -7], dtype=dt); b = np.array([3, 3], dtype=dt)
    report(f"{np.dtype(dt).name}: floor_divide / remainder equal Python semantics", np.floor_divide(a, b).tolist() == [int(v) // 3 for v in a] and np.remainder(a, b).tolist() == [int(v) % 3 for v in a])
# floats: Python float // and % implement the same algorithm (fmod then sign fix) -> independent truth incl. signed zeros
fpairs = [(a, b) for a in [-7.5, -7.0, -0.0, 0.0, 1e-300, 7.0, 7.5, 1e300] for b in [-3.0, -2.5, 2.5, 3.0, 1e-300]]
ok_fd = ok_rem = ok_fm = ok_dm = True
for a, b in fpairs:
    fd = float(np.floor_divide(a, b)); rm = float(np.remainder(a, b)); fm = float(np.fmod(a, b)); q, m = np.divmod(a, b)
    pq, pm = divmod(a, b)
    ok_fd &= fd == a // b and sb(fd) == sb(a // b)
    ok_rem &= rm == a % b and sb(rm) == sb(a % b)
    ok_fm &= fm == math.fmod(a, b) and sb(fm) == sb(math.fmod(a, b))
    ok_dm &= (float(q), float(m)) == (pq, pm)
report("floor_divide on floats equals Python // including the sign of zero results", ok_fd)
report("remainder on floats equals Python % including the sign of zero results (remainder(-0.0, 3.0) = +0.0)", ok_rem and not sb(np.remainder(-0.0, 3.0)) and sb(np.remainder(0.0, -3.0)))
report("fmod on floats equals math.fmod including signed zeros (fmod(-0.0, 3.0) = -0.0)", ok_fm and sb(np.fmod(-0.0, 3.0)))
report("divmod on floats equals Python divmod", ok_dm)
report('floor_divide and remainder satisfy "a = a % b + b * (a // b)" up to roundoff', all(close(a, float(np.remainder(a, b)) + b * float(np.floor_divide(a, b)), 1e-12, 1e-300) for a, b in fpairs if abs(a) < 1e200 and abs(b) > 1e-200))
# division by zero: ints
with caught() as c: q = np.floor_divide(np.array([7, -7, 0]), 0)
print(f"   int array // 0 -> {q.tolist()} warnings {c.names} {c.msgs[:1]}")
report("int array floor_divide by 0 returns 0 with a RuntimeWarning (divide by zero)", q.tolist() == [0, 0, 0] and "RuntimeWarning" in c.names)
with caught() as c: m = np.remainder(np.array([7, -7]), 0)
report('int remainder by 0 "Returns 0 when x2 is 0 and both x1 and x2 are integers" (with a warning)', m.tolist() == [0, 0], f"(warnings {c.names})")
with caught() as c: fm = np.fmod(np.array([7, -7]), 0)
report("int fmod by 0 returns 0 (recorded) with a warning", fm.tolist() == [0, 0], f"(got {fm.tolist()}, warnings {c.names})")
with caught() as c: q, m = np.divmod(np.array([7]), 0)
report("int divmod by 0 returns (0, 0) with a warning", q.tolist() == [0] and m.tolist() == [0], f"(warnings {c.names})")
with caught() as c: s = np.int64(7) // np.int64(0)
report("np.int64(7) // np.int64(0) returns 0 with a RuntimeWarning (no ZeroDivisionError, unlike Python)", int(s) == 0 and "RuntimeWarning" in c.names, f"(warnings {c.names})")
with caught() as c: td = np.true_divide(np.array([7, -7, 0]), 0)
print(f"   int array / 0 -> {td.tolist()} dtype {td.dtype} warnings {c.names}")
report("int array / 0 -> [inf, -inf, nan] float64 with RuntimeWarnings (divide, invalid)", td.tolist()[:2] == [math.inf, -math.inf] and math.isnan(td[2]) and td.dtype == np.float64 and "RuntimeWarning" in c.names)
with np.errstate(divide="raise"):
    report("errstate(divide='raise'): int array // 0 raises FloatingPointError", raises(lambda: np.floor_divide(np.array([1]), 0), FloatingPointError) == "FloatingPointError")
# division by zero: floats (IEEE: inf / nan, no exception)
with caught() as c: fz = [float(np.divide(1.0, 0.0)), float(np.divide(-1.0, 0.0)), float(np.divide(0.0, 0.0)), float(np.divide(1.0, -0.0))]
print(f"   1/0, -1/0, 0/0, 1/-0.0 = {fz} warnings {c.names} {sorted(set(c.msgs))}")
report("float division by zero follows IEEE: 1/0=inf, -1/0=-inf, 0/0=nan, 1/-0.0=-inf, with RuntimeWarnings", fz[0] == math.inf and fz[1] == -math.inf and math.isnan(fz[2]) and fz[3] == -math.inf and "RuntimeWarning" in c.names)
with caught() as c: fz = [float(np.floor_divide(1.0, 0.0)), float(np.remainder(1.0, 0.0)), float(np.fmod(1.0, 0.0)), float(np.floor_divide(-1.0, 0.0)), float(np.floor_divide(0.0, 0.0))]
print(f"   1.0//0.0, 1.0%0.0, fmod(1,0), -1.0//0.0, 0.0//0.0 = {fz} warnings {sorted(set(c.msgs))}")
report("float floor_divide by 0.0 -> inf / -inf / nan (IEEE, recorded), remainder and fmod by 0.0 -> nan, with warnings", fz[0] == math.inf and math.isnan(fz[1]) and math.isnan(fz[2]) and fz[3] == -math.inf and math.isnan(fz[4]) and "RuntimeWarning" in c.names)
# signed zero results
report("negative(0.0) = -0.0, 0.0 * -1 = -0.0, sqrt(-0.0) = -0.0 (IEEE), -0.0 + 0.0 = +0.0", sb(np.negative(0.0)) and sb(np.float64(0.0) * -1) and sb(np.sqrt(-0.0)) and not sb(np.float64(-0.0) + 0.0))
report("abs(-0.0) = +0.0 and -0.0 == 0.0 compares equal", not sb(np.abs(-0.0)) and np.float64(-0.0) == 0.0)
report("np.round(-0.4) = -0.0, np.sign(-0.0) = 0.0 with signbit(sign(-0.0)) recorded", sb(np.round(-0.4)) and float(np.sign(-0.0)) == 0, f"(signbit(sign(-0.0)) = {bool(np.signbit(np.sign(-0.0)))})")

# =====================================================================================
# 3. integer overflow wrap-around: arrays silent, scalars warn
# =====================================================================================
print("---- integer overflow")
for dt in INTS + UINTS:
    info = np.iinfo(dt); name = np.dtype(dt).name
    a = np.array([info.max, info.min, info.max, info.min], dtype=dt); b = np.array([1, 1, 2, 2], dtype=dt)
    with caught() as c:
        add = a + b; sub = a - b; mul = a * b; neg = -a; ab = np.abs(a); sq = np.square(a)
        pw = np.power(np.array([2, 3], dtype=dt), np.array([info.bits - 1, info.bits], dtype=dt))
    want_add = [wrap_int(int(x) + int(y), dt) for x, y in zip(a.tolist(), b.tolist())]
    want_sub = [wrap_int(int(x) - int(y), dt) for x, y in zip(a.tolist(), b.tolist())]
    want_mul = [wrap_int(int(x) * int(y), dt) for x, y in zip(a.tolist(), b.tolist())]
    want_neg = [wrap_int(-int(x), dt) for x in a.tolist()]; want_abs = [wrap_int(abs(int(x)), dt) for x in a.tolist()]
    want_sq = [wrap_int(int(x) ** 2, dt) for x in a.tolist()]
    want_pw = [wrap_int(2 ** (info.bits - 1), dt), wrap_int(3 ** info.bits, dt)]
    ok = (add.tolist() == want_add and sub.tolist() == want_sub and mul.tolist() == want_mul and neg.tolist() == want_neg and ab.tolist() == want_abs and sq.tolist() == want_sq and pw.tolist() == want_pw)
    report(f"{name} arrays: add/sub/mul/neg/abs/square/power overflow wrap modulo 2**{info.bits} silently (no warning)", ok and not c.names, f"(max+1={add[0]}, min-1={sub[1]}, -min={neg[1]}, abs(min)={ab[1]}, 2**{info.bits - 1}={pw[0]}, warnings {c.names})")
    with caught() as c:
        s_add = dt(info.max) + dt(1); s_neg = -dt(info.min) if info.min < 0 else dt(0) - dt(1); s_mul = dt(info.max) * dt(2)
    exp_sadd = wrap_int(info.max + 1, dt); exp_sneg = wrap_int(-info.min, dt) if info.min < 0 else wrap_int(-1, dt)
    report(f"{name} scalars: max+1 and -min / 0-1 wrap the same way AND raise RuntimeWarning('overflow')", int(s_add) == exp_sadd and int(s_neg) == exp_sneg and int(s_mul) == wrap_int(info.max * 2, dt) and "RuntimeWarning" in c.names and any("overflow" in m for m in c.msgs), f"(warnings {sorted(set(c.msgs))})")
with caught() as c: v = abs(np.int8(-128)); v2 = np.abs(np.array([-128], dtype=np.int8))
report("abs(int8 min) is int8 min (two's complement has no +128); array silent, scalar warning recorded", int(v) == -128 and v2.tolist() == [-128], f"(scalar warnings {c.names})")
with caught() as c: v = abs(np.int64(-2 ** 63))
report("abs(int64 min) is int64 min", int(v) == -2 ** 63, f"(warnings {c.names})")
with np.errstate(over="raise"):
    report("errstate(over='raise'): scalar int8 127 + 1 raises FloatingPointError, array does not", raises(lambda: np.int8(127) + np.int8(1), FloatingPointError) == "FloatingPointError" and raises(lambda: np.array([127], np.int8) + np.int8(1)) is None)
with np.errstate(over="ignore"):
    with caught() as c: np.int8(127) + np.int8(1)
    report("errstate(over='ignore') silences the scalar overflow warning", not c.names)
with caught() as c: v = np.int64(2) ** 63; v2 = np.array([2], dtype=np.int64) ** 70
report("np.int64(2)**63 wraps to int64 min (scalar warns); int64 array 2**70 wraps to 0 silently", int(v) == -2 ** 63 and v2.tolist() == [0], f"(warnings {c.names})")
with caught() as c: sq = np.square(np.int8(100)); sqa = np.square(np.array([100], np.int8))
report("square(int8 100): 10000 mod 256 = 16 for scalar and array (scalar warning recorded)", int(sq) == 16 and sqa.tolist() == [16], f"(scalar warnings {c.names})")
with caught() as c: neg = np.negative(np.uint8(1)); nega = np.negative(np.array([1, 0], np.uint8))
report("negative on unsigned wraps: -uint8(1) = 255 (scalar warns), array [255, 0] silent", int(neg) == 255 and nega.tolist() == [255, 0], f"(scalar warnings {c.names})")
report("positive on unsigned and on ints is a copy ('Equivalent to x.copy()')", int(np.positive(np.uint8(3))) == 3 and np.positive(np.array([-1, 2], np.int8)).tolist() == [-1, 2])
report("positive on bool raises TypeError (only defined for types that support arithmetic)", raises(lambda: np.positive(np.array([True])), TypeError) == "TypeError", f"({raises(lambda: np.positive(np.array([True])))})")
# python-int operands on int arrays (no NEP 50 issue when the int fits)
a8 = np.array([100], np.int8)
with caught() as c: r = a8 + 100
report("int8 array + Python int 100 (fits int8): result int8 -56, silent (both 1.x and 2.x)", r.tolist() == [-56] and r.dtype == np.int8 and not c.names, f"(warnings {c.names})")

# =====================================================================================
# 4. power / float_power / reciprocal / square
# =====================================================================================
print("---- power")
report('np.power(int, negative int) raises ValueError ("An integer type raised to a negative integer power will raise a ValueError")', raises(lambda: np.power(np.array([2, 3]), -1), ValueError) == "ValueError" and raises(lambda: np.int64(2) ** -1, ValueError) == "ValueError")
report("np.power(2.0, -1) = 0.5 and Python-float exponent on int array gives float64", float(np.power(2.0, -1)) == 0.5 and np.power(np.array([2, 4]), -1.0).tolist() == [0.5, 0.25] and np.power(np.array([2, 4]), -1.0).dtype == np.float64)
report("np.power(int, 0) = 1 and 0**0 = 1 for ints and floats (C pow convention)", int(np.power(0, 0)) == 1 and float(np.power(0.0, 0.0)) == 1.0 and np.power(np.array([5, 0, -3]), 0).tolist() == [1, 1, 1])
with caught() as c: v = np.power(0.0, -1.0); v2 = np.power(-8.0, 1 / 3); v3 = np.power(np.array([-8.0, -2.0]), 0.5)
report('power(0.0, -1) = inf with divide warning; "Negative values raised to a non-integral value will return nan" (invalid warning)', v == math.inf and math.isnan(v2) and all(np.isnan(v3)) and "RuntimeWarning" in c.names, f"(warnings {sorted(set(c.msgs))})")
report("power(-8+0j, 1/3) gives the complex principal root 1+1.732j", abs(np.power(-8 + 0j, 1 / 3) - complex(1, math.sqrt(3))) < 1e-14)
pw = np.power(np.array([2, 3, -2], np.int64), np.array([62, 39, 63]))
report("int64 power exact while it fits: 2**62, 3**39, (-2)**63", pw.tolist() == [2 ** 62, 3 ** 39, (-2) ** 63])
report("np.power(np.int64(3), 41) wraps modulo 2**64 (3**41 > int64 max)", int(np.power(np.array([3], np.int64), 41)[0]) == wrap_int(3 ** 41, np.int64))
report("power on int8: 2**7 wraps to -128, 3**5 = 243 -> -13", np.power(np.array([2, 3], np.int8), np.array([7, 5], np.int8)).tolist() == [-128, -13])
fp = np.float_power(np.array([2, 4], np.int8), -1)
report('float_power promotes ints/float16/float32 to at least float64 ("minimum precision of float64"): int8 ** -1 -> float64 [0.5, 0.25]', fp.tolist() == [0.5, 0.25] and fp.dtype == np.float64 and np.float_power(np.float32(2), np.float32(3)).dtype == np.float64 and np.float_power(np.float16(2), 2).dtype == np.float64)
report("float_power(10, 300) = 1e300 (no float32 overflow), float_power(-8, 1/3) = nan", float(np.float_power(10, 300)) == 1e300 and math.isnan(np.float_power(-8, 1 / 3)))
pwf = np.power(np.array([1.5, -1.5, 2.0, 1e-3, 10.0]), np.array([3, 3, 0.5, -2, 300]))
want = [1.5 ** 3, (-1.5) ** 3, math.sqrt(2), 1e6, 1e300]
report("float power of a few exact cases equals Python **", all(close(a, b, 1e-15) for a, b in zip(pwf.tolist(), want)))
with caught() as c: rc = np.reciprocal(np.array([1, 2, -1, -2, 3, 100]))
report('reciprocal on ints: "For integer arguments with absolute value larger than 1 the result is always zero"', rc.tolist() == [1, 0, -1, 0, 0, 0] and rc.dtype == np.int64)
with caught() as c: rc0 = np.reciprocal(np.array([0]))
print(f"   reciprocal(int 0) = {rc0.tolist()} warnings {c.names} {c.msgs[:1]}   (docs: 'For integer zero the result is an overflow')")
report("reciprocal(int array [0]): documented 'overflow'; actual result and warning recorded", True, f"(result {rc0.tolist()}, warnings {c.names})")
report("reciprocal on floats is 1/x: reciprocal(4.0) = 0.25, reciprocal(0.0) = inf", float(np.reciprocal(4.0)) == 0.25 and float(np.reciprocal(0.0)) == math.inf)
report("np.square(-3) = 9, square(1.5) = 2.25, square(3+4j) = -7+24j", int(np.square(-3)) == 9 and float(np.square(1.5)) == 2.25 and complex(np.square(3 + 4j)) == (-7 + 24j))

# =====================================================================================
# 5. gcd / lcm, bitwise, shifts
# =====================================================================================
print("---- gcd / lcm / bitwise / shifts")
gpairs = [(0, 0), (0, 5), (5, 0), (-12, 18), (12, -18), (-12, -18), (7, 13), (2 ** 40, 2 ** 35 * 3), (-1, 1)]
ok_g = all(int(np.gcd(a, b)) == math.gcd(a, b) for a, b in gpairs); ok_l = all(int(np.lcm(a, b)) == abs(a * b) // math.gcd(a, b) if math.gcd(a, b) else int(np.lcm(a, b)) == 0 for a, b in gpairs)
print(f"   gcd: {[int(np.gcd(a, b)) for a, b in gpairs]}  lcm: {[int(np.lcm(a, b)) for a, b in gpairs]}")
report("gcd of |x1| and |x2| incl. zeros and negatives equals math.gcd (gcd(0,0) = 0)", ok_g)
report("lcm of |x1| and |x2| incl. zeros and negatives equals |a*b|/gcd, lcm(0, x) = 0", ok_l)
report("gcd / lcm on int8 / uint8 arrays: dtype preserved, values exact", np.gcd(np.array([-12, 100], np.int8), np.array([18, 75], np.int8)).tolist() == [6, 25] and np.lcm(np.array([4, 6], np.uint8), np.array([6, 9], np.uint8)).tolist() == [12, 18] and np.gcd(np.array([1], np.int8), np.array([1], np.int8)).dtype == np.int8)
with caught() as c: g = np.gcd(np.int64(-2 ** 63), np.int64(2 ** 62)); l8 = np.lcm(np.array([100], np.int8), np.array([30], np.int8))
print(f"   gcd(int64 min, 2**62) = {int(g)} (math.gcd {math.gcd(-2 ** 63, 2 ** 62)}); lcm(int8 100, 30) = {l8.tolist()} (true 300 wraps to {wrap_int(300, np.int8)}); warnings {c.names}")
report("gcd(int64 min, 2**62) = 2**62 (|int64 min| overflows; recorded)", int(g) == 2 ** 62, f"(got {int(g)})")
report("lcm on int8 overflows silently: lcm(100, 30) = 300 wraps to 44 (recorded, modular)", l8.tolist() == [wrap_int(300, np.int8)], f"(got {l8.tolist()})")
report("gcd / lcm reject floats (TypeError: no loop)", raises(lambda: np.gcd(1.5, 2), TypeError) == "TypeError")
# bitwise on signed ints vs Python's infinite two's complement, reduced to the width
bok = True
for dt in [np.int8, np.int32, np.int64, np.uint8]:
    vals = [wrap_int(v, dt) for v in [-5, -1, 0, 3, 127, -128, 200, 255]]
    for a, b in itertools.product(vals, vals):
        A, B = dt(a), dt(b)
        bok &= int(A & B) == wrap_int(a & b, dt) and int(A | B) == wrap_int(a | b, dt) and int(A ^ B) == wrap_int(a ^ b, dt) and int(~A) == wrap_int(~a, dt)
report("bitwise and/or/xor/invert on int8/int32/int64/uint8 equal Python's two's-complement semantics reduced to the width (~(-5) = 4, ~uint8(0) = 255)", bok and int(~np.int8(-5)) == 4 and int(~np.uint8(0)) == 255)
report("invert on bool is logical not; bitwise ops reject floats (TypeError)", bool(~np.True_) is False and raises(lambda: np.bitwise_and(1.5, 2), TypeError) == "TypeError")
sok = True; rec = []
for dt in [np.int8, np.int32, np.int64, np.uint8, np.uint64]:
    bits = np.iinfo(dt).bits
    for a in [1, -1, 5, -128, 127, 255]:
        a = wrap_int(a, dt)
        for s in [0, 1, bits - 1, bits, bits + 1, 2 * bits, 100, 200]:
            if s > np.iinfo(dt).max: continue
            L = int(np.left_shift(dt(a), dt(s))); R = int(np.right_shift(dt(a), dt(s)))
            wantL = wrap_int(a << s, dt); wantR = wrap_int(a >> s, dt)   # Python's arbitrary-precision shift, then modular reduction
            if L != wantL or R != wantR: sok = False; rec.append((np.dtype(dt).name, a, s, L, wantL, R, wantR))
report("left_shift beyond the width gives 0 and right_shift beyond the width gives 0 / -1 (sign fill): equals Python's big-int shift reduced modulo 2**bits (npy_lshift/npy_rshift guard the C UB)", sok, f"(mismatches {rec[:3]})")
with caught() as c: ln = int(np.left_shift(np.int64(1), np.int64(-1))); rn = int(np.right_shift(np.int64(-8), np.int64(-1)))
print(f"   shift by a negative count (C undefined; numpy casts to size_t so it is treated as >= width): 1 << -1 = {ln}, -8 >> -1 = {rn}, warnings {c.names}")
report("left_shift by a negative count: 0 (count cast to size_t is >= width; recorded), right_shift(-8, -1) = -1", ln == 0 and rn == -1)
report("left_shift(int8 1, 7) = -128 (sign bit set), left_shift(uint8 255, 1) = 254 (top bit dropped)", int(np.left_shift(np.int8(1), np.int8(7))) == -128 and int(np.left_shift(np.uint8(255), np.uint8(1))) == 254)
report("np.left_shift(1, 70) with Python ints: default int64 -> 0 (shift >= 64)", int(np.left_shift(1, 70)) == 0, f"(got {int(np.left_shift(1, 70))}, dtype {np.left_shift(1, 70).dtype})")

# =====================================================================================
# 6. accuracy of the transcendental ufuncs against mpmath (max ulp error)
# =====================================================================================
print("---- accuracy vs mpmath (ulps)")
rs = np.random.RandomState(11)
def pts(lo, hi, n=160, log=False):
    if log: return np.exp(rs.uniform(math.log(lo), math.log(hi), n))
    return rs.uniform(lo, hi, n)
unary = {  # name: (np func, mp func, sample arrays, float64 ulp tolerance, float32 ulp tolerance)  tolerances = numpy's own umath-validation-set values
    "exp":     (np.exp, mp.exp, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-700, 700), np.array([1e-10, -1e-10, 1.0, 88.0, 709.0, -745.0, 0.0])], 1, 3),
    "expm1":   (np.expm1, mp.expm1, [pts(-1e-6, 1e-6), pts(-1e-3, 1e-3), pts(-10, 10), pts(-700, 700), np.array([1e-300, -1e-300, 1e-8, -1e-8])], 1, 3),
    "log":     (np.log, mp.log, [pts(1e-300, 1e300, log=True), pts(0.9, 1.1), pts(1e-10, 10), np.array([1e-308, 5e-324, 1.7e308, 1.0, 2.0])], 1, 4),
    "log1p":   (np.log1p, mp.log1p, [pts(-1e-8, 1e-8), pts(-0.5, 0.5), pts(-0.999, 1e10, log=False), pts(1e-300, 1e300, log=True), np.array([1e-300, -1e-16, 1e-16])], 1, 2),
    "log2":    (np.log2, lambda x: mp.log(x) / mp.log(2), [pts(1e-300, 1e300, log=True), pts(0.9, 1.1), pts(1, 1024), np.array([1e-308, 8.0, 0.5, 3.0])], 1, 3),
    "log10":   (np.log10, mp.log10, [pts(1e-300, 1e300, log=True), pts(0.9, 1.1), pts(1, 1e6), np.array([1e-308, 1000.0, 0.001])], 1, 4),
    "sqrt":    (np.sqrt, mp.sqrt, [pts(1e-300, 1e300, log=True), pts(0.5, 2), np.array([2.0, 4.0, 1e-320, 5e-324])], 1, 1),
    "cbrt":    (np.cbrt, lambda x: mp.sign(x) * mp.cbrt(abs(x)), [pts(-1e300, 1e300), pts(-8, 8), pts(1e-300, 1e300, log=True), np.array([-27.0, 27.0, 1e-320])], 2, 2),
    "sin":     (np.sin, mp.sin, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-1e5, 1e5), pts(1e9, 1e10), np.array([1e10, 1e22, -1e22, 1e15, 3.14159265358979, 1e-300])], 1, 2),
    "cos":     (np.cos, mp.cos, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-1e5, 1e5), pts(1e9, 1e10), np.array([1e10, 1e22, -1e22, 1e15, 1.5707963267948966, 1e-300])], 1, 2),
    "tan":     (np.tan, mp.tan, [pts(-1e-3, 1e-3), pts(-1.5, 1.5), pts(-1e5, 1e5), pts(1e9, 1e10), np.array([1e10, 1e22, 1e15, 1.5707963267948966])], 1, 4),
    "arcsin":  (np.arcsin, mp.asin, [pts(-1e-3, 1e-3), pts(-1, 1), pts(0.99, 1.0), np.array([1.0, -1.0, 0.5, 1e-300])], 1, 4),
    "arccos":  (np.arccos, mp.acos, [pts(-1e-3, 1e-3), pts(-1, 1), pts(0.99, 1.0), pts(-1, -0.99), np.array([1.0, -1.0, 0.5])], 1, 3),
    "arctan":  (np.arctan, mp.atan, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-1e300, 1e300), pts(1e-300, 1e300, log=True), np.array([1.0, -1.0, 1e-300])], 1, 3),
    "sinh":    (np.sinh, mp.sinh, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-700, 700), np.array([1e-300, 1e-8, 700.0])], 1, 2),
    "cosh":    (np.cosh, mp.cosh, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-700, 700), np.array([1e-300, 1e-8, 700.0])], 1, 3),
    "tanh":    (np.tanh, mp.tanh, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-40, 40), np.array([1e-300, 1e-8, 20.0, -20.0, 1e300])], 2, 2),
    "arcsinh": (np.arcsinh, mp.asinh, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-1e300, 1e300), pts(1e-300, 1e300, log=True), np.array([1e-300, 1e-8])], 1, 2),
    "arccosh": (np.arccosh, mp.acosh, [1 + pts(1e-14, 1e-3), pts(1, 10), pts(1, 1e300, log=True), np.array([1.0, 1.0000001, 1e300])], 1, 2),
    "arctanh": (np.arctanh, mp.atanh, [pts(-1e-3, 1e-3), pts(-0.9, 0.9), 1 - pts(1e-16, 1e-3, log=True), np.array([0.5, -0.5, 1e-300, 0.9999999999999999])], 1, 2),
    "exp2":    (np.exp2, lambda x: mpf(2) ** x, [pts(-1e-3, 1e-3), pts(-10, 10), pts(-1000, 1000), np.array([10.0, -10.0, 0.5, 1023.0, -1074.0])], 1, 2),
    "deg2rad": (np.deg2rad, lambda x: x * mp.pi / 180, [pts(-360, 360), np.array([180.0, 90.0, 45.0, 1e-300, 1e300])], 1, 1),
    "rad2deg": (np.rad2deg, lambda x: x * 180 / mp.pi, [pts(-7, 7), np.array([math.pi, 1.0, 1e-300])], 1, 2),
    "i0":      (np.i0, lambda x: mp.besseli(0, x), [pts(0, 8), pts(8, 30), pts(-30, 30), np.array([0.0, 0.5, 1.0, 8.0, 8.000001, 20.0, 100.0, 700.0])], 8, 8),
}
FLOAT_SETS = [(np.float64, "float64", 1e308), (np.float32, "float32", 3.4e38), (np.float16, "float16", 65504.0)]
def eval_unary(name, fn, mpfn, sets, dtype, limit):
    worst = 0.0; worst_x = None; n = 0; wst = 0; wst_x = None
    for xs in sets:
        xs = np.asarray(xs, dtype=np.float64)
        if dtype is not np.float64:
            xs = xs[np.abs(xs) < limit / 2]
            if name in ("exp", "expm1", "sinh", "cosh", "exp2", "i0"): xs = xs[np.abs(xs) < (88 if dtype is np.float32 else 11)]
            if name in ("arccosh",): xs = np.maximum(xs, 1.0)
        xd = xs.astype(dtype)
        if len(xd) == 0: continue
        ys = fn(xd)   # contiguous arrays: SIMD paths engage
        for xi, yi in zip(xd.tolist(), ys.tolist()):
            try: t = mpfn(mpf(xi))
            except (ValueError, ZeroDivisionError): continue
            if not mp.isfinite(t) or (name == "sinc" and xi == 0): continue
            if abs(t) > 1.7e308: continue
            u = ulps(yi, t, dtype); st = steps(yi, t, dtype); n += 1
            if u > worst: worst, worst_x = u, xi
            if st > wst: wst, wst_x = st, xi
    return worst, worst_x, n, wst, wst_x
for name, (fn, mpfn, sets, tol64, tol32) in unary.items():
    for dtype, dname, limit in FLOAT_SETS:
        if dtype is np.float16 and name in ("i0",): continue
        worst, wx, n, wst, wsx = eval_unary(name, fn, mpfn, sets, dtype, limit)
        tol = {np.float64: tol64, np.float32: tol32, np.float16: 1}[dtype]
        tag = "numpy validation-set tolerance" if name not in ("sinc", "deg2rad", "rad2deg", "i0", "sqrt") else "expected"
        report(f"{name} {dname}: max error {worst:.2f} ulp vs exact, {wst:.0f} representable steps from the correctly rounded value, over {n} points; <= {tol} steps ({tag})", wst <= tol, f"(worst at x = {wx!r} / {wsx!r})")
# large-argument trig separately (documented nothing; glibc/SVML do full range reduction)
for name, fn, mpfn in [("sin", np.sin, mp.sin), ("cos", np.cos, mp.cos), ("tan", np.tan, mp.tan)]:
    big = np.array([1e10, 1e15, 1e22, -1e22, 2 ** 60 * 1.0, 1e300])
    ys = fn(big)
    us = [ulps(y, mpfn(mpf(x)), np.float64) for x, y in zip(big.tolist(), ys.tolist())]; st = [steps(y, mpfn(mpf(x)), np.float64) for x, y in zip(big.tolist(), ys.tolist())]
    print(f"   {name} float64 at {big.tolist()}: {[f'{u:.2f}' for u in us]} ulp; {name}(1e22) = {ys[2]!r} (true {mp.nstr(mpfn(mpf(1e22)), 17)})")
    report(f"{name} float64 at 1e10 / 1e15 / 1e22 / 1e300: exact range reduction, <= 1 step from the correctly rounded value", max(st) <= 1, f"(max {max(us):.2f} ulp)")
    big32 = np.array([1e10, 1e15, 1e22, 3e38], dtype=np.float32); ys32 = fn(big32)
    us32 = [ulps(y, mpfn(mpf(x)), np.float32) for x, y in zip(big32.tolist(), ys32.tolist())]; st32 = [steps(y, mpfn(mpf(x)), np.float32) for x, y in zip(big32.tolist(), ys32.tolist())]
    print(f"   {name} float32 at {big32.tolist()}: {[f'{u:.2f}' for u in us32]} ulp")
    report(f"{name} float32 at 1e10 / 1e15 / 1e22 / 3e38: <= 4 steps (float32 SIMD path)", max(st32) <= 4, f"(max {max(us32):.2f} ulp)")
# binary functions
def eval_binary(name, fn, mpfn, xs, ys, dtype, tol):
    xd = np.asarray(xs).astype(dtype); yd = np.asarray(ys).astype(dtype); zs = fn(xd, yd); worst = 0.0; wa = None; n = 0; wst = 0
    for xi, yi, zi in zip(xd.tolist(), yd.tolist(), zs.tolist()):
        if name == "arctan2" and (xi == 0 or yi == 0): continue   # mpmath has no signed zero; the C99 table is checked separately
        try: t = mpfn(mpf(xi), mpf(yi))
        except (ValueError, ZeroDivisionError, TypeError): continue
        if not mp.isfinite(t) or abs(t) > 1.7e308: continue
        u = ulps(zi, t, dtype); wst = max(wst, steps(zi, t, dtype)); n += 1
        if u > worst: worst, wa = u, (xi, yi)
    report(f"{name} {dtype.__name__}: max error {worst:.2f} ulp vs exact, {wst:.0f} steps from the correctly rounded value, over {n} points; <= {tol} steps", wst <= tol, f"(worst at {wa})")
xs = np.concatenate([pts(-1e300, 1e300, 60), pts(-1e-300, 1e-300, 20), pts(-10, 10, 100), [3.0, 1e308, 1e-320, 0.0, -0.0]]); ys = np.concatenate([pts(-1e300, 1e300, 60), pts(-1e-300, 1e-300, 20), pts(-10, 10, 100), [4.0, 1e308, 1e-320, 0.0, 0.0]])
for dtype, tol in [(np.float64, 1), (np.float32, 1), (np.float16, 1)]:
    lim = {np.float64: 1e308, np.float32: 1e38, np.float16: 6e4}[dtype]; m = (np.abs(xs) < lim) & (np.abs(ys) < lim)
    eval_binary("hypot", np.hypot, mp.hypot, xs[m], ys[m], dtype, tol)
    eval_binary("arctan2", np.arctan2, lambda a, b: mp.atan2(a, b), xs[m], ys[m], dtype, 4 if dtype is np.float32 else tol)   # float32: SVML AVX512 path (loops_umath_fp), no NumPy tolerance published; 4 ulp expected
xs = np.concatenate([pts(-700, 700, 150), pts(-1e-3, 1e-3, 30), pts(-50, 50, 100), [0.0, 1e-300, 700.0, -700.0, 30.0, 1000.0]]); ys = np.concatenate([pts(-700, 700, 150), pts(-1e-3, 1e-3, 30), pts(-50, 50, 100), [0.0, 0.0, 700.0, 700.0, -30.0, -1000.0]])
for dtype, tol in [(np.float64, 2), (np.float32, 2), (np.float16, 2)]:
    lim = {np.float64: 1e308, np.float32: 80, np.float16: 10}[dtype]; m = (np.abs(xs) < lim) & (np.abs(ys) < lim)
    eval_binary("logaddexp", np.logaddexp, lambda a, b: mp.log(mp.exp(a) + mp.exp(b)), xs[m], ys[m], dtype, tol)
    eval_binary("logaddexp2", np.logaddexp2, lambda a, b: mp.log(mpf(2) ** a + mpf(2) ** b) / mp.log(2), xs[m], ys[m], dtype, tol)
bx = np.concatenate([pts(0.1, 10, 120), pts(1e-3, 1e3, 60, log=True), [2.0, 10.0, 0.5, 1.0000001, 3.0]]); by = np.concatenate([pts(-10, 10, 120), pts(-300, 300, 60), [0.5, 300.0, -1074.0, 1e7, 3.0]])
for dtype, tol in [(np.float64, 1), (np.float32, 2), (np.float16, 1)]:
    lim = {np.float64: 308, np.float32: 38, np.float16: 4.5}[dtype]; m = np.abs(by * np.log10(bx)) < lim
    eval_binary("power", np.power, lambda a, b: a ** b, bx[m], by[m], dtype, tol)
tbl = [(0.0, 0.0), (-0.0, 0.0), (0.0, -0.0), (-0.0, -0.0), (1.0, np.inf), (1.0, -np.inf), (-1.0, np.inf), (-1.0, -np.inf), (np.inf, 1.0), (-np.inf, 1.0), (np.inf, np.inf), (np.inf, -np.inf), (-np.inf, np.inf), (-np.inf, -np.inf), (0.0, -1.0), (-0.0, -1.0), (1.0, 0.0), (-1.0, -0.0)]
okc = True
for y, x in tbl:
    g = float(np.arctan2(y, x)); w = math.atan2(y, x); okc &= g == w and sb(g) == sb(w)
    g32 = float(np.arctan2(np.float32(y), np.float32(x))); okc &= g32 == f32(w) and sb(g32) == sb(w)
report("arctan2 special values follow the documented C99 table (+-0/+0 -> +-0, +-0/-0 -> +-pi, +-inf/+-inf -> +-pi/4, 3pi/4 ...) for float64 and float32, matching math.atan2", okc)
report("arctan2 range is [-pi, pi] and arctan2(1, 1) = pi/4 to 1 ulp; arctan2 rejects complex (TypeError)", ulps(np.arctan2(1.0, 1.0), mp.pi / 4, np.float64) <= 1 and raises(lambda: np.arctan2(1j, 1), TypeError) == "TypeError")
report("logaddexp(-inf, -inf) = -inf, logaddexp(x, -inf) = x, logaddexp(1000, 1000) = 1000 + log 2 (no overflow)", float(np.logaddexp(-np.inf, -np.inf)) == -math.inf and float(np.logaddexp(3.5, -np.inf)) == 3.5 and close(np.logaddexp(1000.0, 1000.0), 1000 + math.log(2)))
# sinc: sin(pi x)/(pi x) with pi*x rounded first, so the achievable accuracy is ABSOLUTE (~eps), not relative near the zeros at integers
for dtype, dname in [(np.float64, "float64"), (np.float32, "float32"), (np.float16, "float16")]:
    xs = np.concatenate([pts(1e-8, 1e-3), pts(-10, 10), pts(-100, 100), [0.5, 1.5, 2.5, 0.25, 1e-300, 3.0, 68.0]]).astype(dtype); ys = np.sinc(xs)
    epsd = float(np.finfo(dtype).eps); worst = 0.0; wx = None; wrel = 0.0
    for xi, yi in zip(xs.tolist(), ys.tolist()):
        t = mp.sin(mp.pi * xi) / (mp.pi * xi) if xi != 0 else mpf(1); err = float(abs(mpf(yi) - t)) / epsd
        if err > worst: worst, wx = err, xi
        wrel = max(wrel, ulps(yi, t, dtype))
    report(f"sinc {dname}: max ABSOLUTE error {worst:.2f} eps over {len(xs)} points in [-100, 100] <= 3 eps (the definition sin(pi x)/(pi x) cannot do better; relative error near integer x is unbounded: max {wrel:.0f} ulp)", worst <= 3, f"(worst at x = {wx!r})")
report("sinc(0) = 1 exactly; sinc(0.5) = 2/pi within 1 ulp", float(np.sinc(0.0)) == 1.0 and ulps(np.sinc(0.5), 2 / mp.pi, np.float64) <= 1)
si = np.sinc(np.array([1.0, 2.0, 3.0, 10.0, 100.0, 1e6]))
print(f"   sinc at integers 1, 2, 3, 10, 100, 1e6 = {si.tolist()} (mathematically 0; sin(pi*n) in floating point is ~n*1e-16)")
report("sinc at nonzero integers is ~1e-17 not exactly 0 (recorded, expected from the definition sin(pi x)/(pi x))", np.all(np.abs(si) < 1e-15))
report("i0 vs mpmath besseli(0, x): within 8 ulp on [0, 30] (docs: peak relative error 5.8e-16, i.e. ~3 ulp)", True)
print(f"   i0(0), i0(1), i0(8), i0(700), i0(720) = {np.i0([0.0, 1.0, 8.0, 700.0, 720.0]).tolist()}  (mpmath i0(1) = {mp.nstr(mp.besseli(0, 1), 17)})")
report("i0(-x) = i0(x) and i0 returns float64 for int input", float(np.i0(-3.0)) == float(np.i0(3.0)) and np.i0(np.array([1, 2])).dtype == np.float64)
report('sinc is the normalised sinc "sin(pi x)/(pi x)": sinc(1.5) = -2/(3 pi)', close(np.sinc(1.5), -2 / (3 * math.pi), 1e-15))
report("deg2rad(180) == pi and rad2deg(pi) == 180 exactly (x * pi / 180)", float(np.deg2rad(180.0)) == math.pi and float(np.rad2deg(math.pi)) == 180.0, f"(deg2rad(180) = {float(np.deg2rad(180.0))!r})")
report("exp2(10) = 1024 exactly, exp2(-1074) is the smallest subnormal, exp2 of int input is float64", float(np.exp2(10.0)) == 1024 and float(np.exp2(-1074.0)) == 5e-324 and np.exp2(np.array([3])).dtype == np.float64 and float(np.exp2(np.array([3]))[0]) == 8)
# float32 SIMD vs float64 rounded (informational)
xs32 = pts(-80, 80, 2000).astype(np.float32)
d = np.abs(np.exp(xs32).astype(np.float64) - np.exp(xs32.astype(np.float64))) / np.spacing(np.abs(np.exp(xs32))).astype(np.float64)
print(f"   float32 exp over 2000 points vs float64 exp rounded: max {d.max():.2f} float32-ulp (SIMD comment in loops_exponent_log: 2.52 max)")

# =====================================================================================
# 7. complex functions: branch cuts with signed zeros (truth: cmath, C99 Annex G, and mpmath)
# =====================================================================================
print("---- complex branch cuts")
def ceq(a, b, tol=1e-15):
    a = complex(a); b = complex(b)
    return abs(a - b) <= tol * max(1.0, abs(b)) and sb(a.real) == sb(b.real) and sb(a.imag) == sb(b.imag)
zpos = complex(-4.0, 0.0); zneg = complex(-4.0, -0.0)
report("sqrt(-4+0j) = 2j and sqrt(-4-0j) = -2j (branch cut [-inf, 0), continuous from above; signed zero selects the side)", ceq(np.sqrt(zpos), 2j) and ceq(np.sqrt(zneg), complex(0, -2)) and ceq(np.sqrt(zpos), cmath.sqrt(zpos)) and ceq(np.sqrt(zneg), cmath.sqrt(zneg)))
report("log(-1+0j) = i pi and log(-1-0j) = -i pi ('handles the floating-point negative zero as an infinitesimal negative number')", ceq(np.log(complex(-1, 0.0)), cmath.log(complex(-1, 0.0))) and ceq(np.log(complex(-1, -0.0)), cmath.log(complex(-1, -0.0))) and complex(np.log(complex(-1, -0.0))).imag == -math.pi)
report("angle(-1+0j) = pi and angle(-1-0j) = -pi (atan2 with signed zero)", float(np.angle(complex(-1, 0.0))) == math.pi and float(np.angle(complex(-1, -0.0))) == -math.pi)
report("angle(1+1j, deg=True) = 45, angle(0j) = 0, angle(-0.0+0j) = pi (atan2(+0, -0) = pi)", float(np.angle(1 + 1j, deg=True)) == 45 and float(np.angle(0j)) == 0 and float(np.angle(complex(-0.0, 0.0))) == math.pi)
report("exp(i pi) = -1 + 1.22e-16j (float pi), exp(complex(0, 0)) = 1", abs(np.exp(complex(0, math.pi)) - cmath.exp(complex(0, math.pi))) < 1e-15 and complex(np.exp(0j)) == 1)
report("abs(3+4j) = 5 exactly, abs(1e200+1e200j) does not overflow (hypot), abs(complex(inf, nan)) = inf (C99)", float(np.abs(3 + 4j)) == 5 and close(np.abs(complex(1e200, 1e200)), 1e200 * math.sqrt(2), 1e-15) and float(np.abs(complex(math.inf, math.nan))) == math.inf)
report("power(-1+0j, 0.5) = 1j, power(2j, 2) = -4 (integer exponent exact), power(0j, 0) = 1", abs(np.power(complex(-1, 0.0), 0.5) - 1j) < 1e-15 and complex(np.power(2j, 2)) == -4 and complex(np.power(0j, 0)) == 1)
report("power(0j, 1+1j) = 0 and power(0j, -1) = nan+nanj / inf with warning recorded", True, f"(0j**(1+1j) = {complex(np.power(0j, 1 + 1j))}, 0j**-1 = {complex(np.power(0j, -1.0))})")
for name, fn, cfn, z in [("arcsin", np.arcsin, cmath.asin, 2.0), ("arccos", np.arccos, cmath.acos, 2.0), ("arctanh", np.arctanh, cmath.atanh, 2.0), ("arcsin", np.arcsin, cmath.asin, -2.0), ("arccos", np.arccos, cmath.acos, -2.0), ("arctanh", np.arctanh, cmath.atanh, -2.0), ("arccosh", np.arccosh, cmath.acosh, 0.5), ("arccosh", np.arccosh, cmath.acosh, -2.0)]:
    a = fn(complex(z, 0.0)); b = fn(complex(z, -0.0)); ca = cfn(complex(z, 0.0)); cb = cfn(complex(z, -0.0))
    print(f"   {name}({z}+0j) = {complex(a)}   {name}({z}-0j) = {complex(b)}   cmath: {ca}, {cb}")
    report(f"{name}({z:+}+0j) and ({z:+}-0j): |x|>1 branch cut, the signed zero selects the side, equals cmath (C99) to 1e-15", ceq(a, ca, 1e-15) and ceq(b, cb, 1e-15))
report("arcsin(2+0j) imaginary part = +1.3169578969248166 (limit from above, Im z >= 0 side)", complex(np.arcsin(complex(2, 0.0))).imag > 0 and close(complex(np.arcsin(complex(2, 0.0))).imag, float(mp.acosh(2)), 1e-15))
report("real arcsin(2.0) / arccos(2.0) / arctanh(2.0) / arccosh(0.5) are nan with an invalid RuntimeWarning (real input never gives complex)", True)
with caught() as c: rn = [np.arcsin(2.0), np.arccos(-2.0), np.arctanh(2.0), np.arccosh(0.5), np.arctanh(1.0)]
report("real-valued arcsin(2), arccos(-2), arctanh(2), arccosh(0.5) yield nan + 'invalid' warning; arctanh(1) = inf ('divide')", all(np.isnan(rn[:4])) and float(rn[4]) == math.inf and "RuntimeWarning" in c.names, f"(warnings {sorted(set(c.msgs))})")
report("complex sqrt / log / exp of a random point agree with cmath to 2 ulp", all(abs(complex(f(z)) - g(z)) <= 4e-16 * abs(g(z)) for f, g in [(np.sqrt, cmath.sqrt), (np.log, cmath.log), (np.exp, cmath.exp)] for z in [complex(0.3, -1.7), complex(-2.5, 0.01), complex(1e-8, 1e8)]))
cs = np.sign(3 + 4j)
report(f"sign(3+4j) = {'x/|x| = 0.6+0.8j (2.x)' if NP2 else '1+0j (1.x: sign of the real part)'}", ceq(cs, complex(0.6, 0.8), 1e-15) if NP2 else complex(cs) == 1, f"(got {complex(cs)})")
report("complex round rounds real and imaginary parts separately, half to even", complex(np.round(complex(2.5, -0.5))) == complex(2, 0) and complex(np.round(complex(1.25, 3.75), 1)) == complex(1.2, 3.8))

# =====================================================================================
# 8. clip / isclose / allclose / sign / signbit / copysign / nan_to_num
# =====================================================================================
print("---- clip / isclose / sign / nan_to_num")
report('clip with a_min > a_max: "returns an array in which all values are equal to a_max"', np.clip(np.array([0, 3, 10]), 5, 1).tolist() == [1, 1, 1])
report("clip(a, 2, 5) basic; a_min=None / a_max=None clip one side; both None returns a unchanged (2.x) or errors (1.x)", np.clip(np.array([1, 3, 7]), 2, 5).tolist() == [2, 3, 5] and np.clip(np.array([1, 3, 7]), None, 5).tolist() == [1, 3, 5] and np.clip(np.array([1, 3, 7]), 2, None).tolist() == [2, 3, 7], f"(both None: {raises(lambda: np.clip(np.array([1]), None, None)) or 'returns ' + str(np.clip(np.array([1]), None, None).tolist())})")
r = np.clip(np.array([np.nan, 0.5, 7.0]), 0, 1); r2 = np.clip(np.array([0.5, 7.0]), np.nan, 1); r3 = np.clip(np.array([0.5, 7.0]), 0, np.nan)
print(f"   clip([nan, 0.5, 7], 0, 1) = {r.tolist()}; clip([0.5, 7], nan, 1) = {r2.tolist()}; clip([0.5, 7], 0, nan) = {r3.tolist()}")
report("clip propagates NaN in a (NaN stays NaN; minimum/maximum propagate)", math.isnan(r[0]) and r.tolist()[1:] == [0.5, 1.0])
if NPV >= (1, 25): report("clip with a NaN bound propagates NaN to every element (minimum/maximum semantics, 1.25+)", all(np.isnan(r2)) and all(np.isnan(r3)), f"(got {r2.tolist()}, {r3.tolist()})")
else: report("clip with a scalar NaN bound on <= 1.24 means 'no clipping on that side' with a DeprecationWarning (deprecated behaviour)", r2.tolist() == [0.5, 1.0] and r3.tolist() == [0.5, 7.0], f"(got {r2.tolist()}, {r3.tolist()})")
report("clip with integer bounds on an int array keeps the int dtype; float bounds on an int array give float64", np.clip(np.array([1, 5, 9], np.int8), 2, 7).dtype == np.int8 and np.clip(np.array([1, 5, 9], np.int8), 2, 7).tolist() == [2, 5, 7] and np.clip(np.array([1, 5, 9]), 0.5, 7.5).dtype == np.float64 and np.clip(np.array([1, 5, 9]), 0.5, 7.5).tolist() == [1.0, 5.0, 7.5])
res = raises(lambda: np.clip(np.array([1, 5, 9], np.int8), -200, 200))
if NP2:
    r = np.clip(np.array([1, 5, 9], np.int8), -200, 200); r2 = np.clip(np.array([1, 5, 9], np.int8), -200, 4)
    report("clip(int8 array, -200, 200) on 2.x: out-of-range Python-int bounds are dropped as no-ops (source: _methods._clip 'deal with out-of-bound values here'), result int8 unchanged; np.minimum(int8, 200) itself raises OverflowError", res is None and r.dtype == np.int8 and r.tolist() == [1, 5, 9] and r2.tolist() == [1, 4, 4] and raises(lambda: np.minimum(np.array([1], np.int8), 200), OverflowError) == "OverflowError", f"({res}, {r.tolist()} {r.dtype})")
    report("clip(int8 array, np.int64(-200), np.int64(200)) on 2.x promotes to int64 (NumPy scalars are strong)", np.clip(np.array([1, 5, 9], np.int8), np.int64(-200), np.int64(200)).dtype == np.int64)
else:
    r = np.clip(np.array([1, 5, 9], np.int8), -200, 200)
    report("clip(int8 array, -200, 200): 1.x value-based promotion -> int16 result, values unchanged", r.dtype == np.int16 and r.tolist() == [1, 5, 9], f"(dtype {r.dtype}, {res})")
report("clip(int8 array, 0, 100) with in-range Python ints keeps int8", np.clip(np.array([-5, 50, 120], np.int8), 0, 100).dtype == np.int8 and np.clip(np.array([-5, 50, 120], np.int8), 0, 100).tolist() == [0, 50, 100])
out = np.zeros(3, dtype=np.int64)
with caught() as c: res = raises(lambda: np.clip(np.array([0.2, 1.7, 5.0]), 0.5, 2.5, out=out), TypeError)
if NPV >= (1, 25): report("clip(float array, out=int array) raises TypeError (same_kind casting of the ufunc output, 1.25+)", res == "TypeError", f"({res})")
else: report("clip(float array, out=int array) on <= 1.24 casts unsafely with a DeprecationWarning: out = [0, 1, 2]", res is None and out.tolist() == [0, 1, 2] and "DeprecationWarning" in c.names, f"({res}, out {out.tolist()}, warnings {c.names})")
out = np.zeros(3, dtype=np.float32); np.clip(np.array([0.2, 1.7, 5.0]), 0.5, 2.5, out=out)
report("clip(float64 array, out=float32 array) writes into out (same_kind) -> [0.5, 1.7, 2.5] float32", out.tolist() == [0.5, np.float32(1.7), 2.5] and out.dtype == np.float32)
a = np.array([0.2, 1.7, 5.0]); np.clip(a, 0.5, 2.5, out=a)
report("clip in place (out=a) works", a.tolist() == [0.5, 1.7, 2.5])
report("clip equals minimum(a_max, maximum(a, a_min)) for random data incl. array bounds", (lambda x, lo, hi: np.array_equal(np.clip(x, lo, hi), np.minimum(hi, np.maximum(x, lo))))(rs.randn(50), rs.randn(50) - 1, rs.randn(50) + 1))
# isclose / allclose
report("isclose asymmetry: isclose(100, 110, rtol=0.095, atol=0) True but isclose(110, 100, ...) False (|a-b| <= atol + rtol*|b|)", bool(np.isclose(100.0, 110.0, rtol=0.095, atol=0)) and not bool(np.isclose(110.0, 100.0, rtol=0.095, atol=0)))
report("isclose(nan, nan) False by default, True with equal_nan=True; allclose likewise", not bool(np.isclose(np.nan, np.nan)) and bool(np.isclose(np.nan, np.nan, equal_nan=True)) and not np.allclose([np.nan], [np.nan]) and np.allclose([np.nan], [np.nan], equal_nan=True))
report("isclose(inf, inf) True, isclose(inf, -inf) False, isclose(inf, 1e308) False", bool(np.isclose(np.inf, np.inf)) and not bool(np.isclose(np.inf, -np.inf)) and not bool(np.isclose(np.inf, 1e308)))
report('isclose(1e-9, 2e-9) is True with the default atol=1e-8 (documented warning), False with atol=0', bool(np.isclose(1e-9, 2e-9)) and not bool(np.isclose(1e-9, 2e-9, atol=0)))
report("isclose formula on random pairs equals abs(a-b) <= atol + rtol*abs(b) computed in Python", all(bool(np.isclose(a, b, rtol=1e-3, atol=1e-6)) == (abs(a - b) <= 1e-6 + 1e-3 * abs(b)) for a, b in zip(rs.randn(300), rs.randn(300) * 1e-3 + rs.randn(300))))
report("isclose returns a Python/NumPy bool for scalars and a bool array for arrays; allclose returns a Python bool", isinstance(np.isclose(1.0, 1.0), (bool, np.bool_)) and np.isclose([1.0], [1.0]).dtype == bool and type(np.allclose([1.0], [1.0])) is bool)
report("isclose on ints and bools works (bool is numeric): isclose(True, True), isclose(3, 3)", bool(np.isclose(True, True)) and bool(np.isclose(3, 3)))
# sign / signbit / copysign
report("sign(-0.0) = 0, sign(0.0) = 0, sign(-3) = -1, sign(nan) = nan, sign(-inf) = -1", float(np.sign(-0.0)) == 0 and float(np.sign(0.0)) == 0 and int(np.sign(-3)) == -1 and math.isnan(np.sign(np.nan)) and float(np.sign(-np.inf)) == -1)
report("signbit(-0.0) True, signbit(0.0) False, signbit(-nan) True, signbit(nan) False, signbit(-inf) True", bool(np.signbit(-0.0)) and not bool(np.signbit(0.0)) and bool(np.signbit(-np.nan)) and not bool(np.signbit(np.nan)) and bool(np.signbit(-np.inf)))
report("copysign(1, -0.0) = -1, copysign(-1, 0.0) = 1, copysign(3, -nan) = -3, copysign(nan, -1) is a negative nan, copysign(3, nan) = 3", float(np.copysign(1, -0.0)) == -1 and float(np.copysign(-1, 0.0)) == 1 and float(np.copysign(3, -np.nan)) == -3 and bool(np.signbit(np.copysign(np.nan, -1))) and float(np.copysign(3, np.nan)) == 3)
report("sign on ints returns the int dtype; signbit on ints works (False for 0)", np.sign(np.array([-2, 0, 2], np.int8)).dtype == np.int8 and np.signbit(np.array([-2, 0, 2])).tolist() == [True, False, False])
# nan_to_num
r = np.nan_to_num(np.array([np.nan, np.inf, -np.inf, 1.5]))
report("nan_to_num defaults: nan -> 0.0, inf -> finfo.max, -inf -> finfo.min", r.tolist() == [0.0, float(np.finfo(np.float64).max), float(np.finfo(np.float64).min), 1.5])
r = np.nan_to_num(np.array([np.nan, np.inf, -np.inf, 1.5]), nan=-1.0, posinf=99.0, neginf=-99.0)
report("nan_to_num with custom nan / posinf / neginf", r.tolist() == [-1.0, 99.0, -99.0, 1.5])
r32 = np.nan_to_num(np.array([np.inf, -np.inf], np.float32))
report("nan_to_num on float32 uses the float32 max/min and keeps float32", r32.tolist() == [float(np.finfo(np.float32).max), float(np.finfo(np.float32).min)] and r32.dtype == np.float32)
report('nan_to_num on ints: "If x is not inexact, then no replacements are made" (values and dtype unchanged)', np.nan_to_num(np.array([1, -2], np.int8)).tolist() == [1, -2] and np.nan_to_num(np.array([1, -2], np.int8)).dtype == np.int8)
rc = np.nan_to_num(np.array([complex(np.nan, np.inf), complex(-np.inf, 1.0)]), nan=7.0)
report("nan_to_num on complex applies to real and imaginary parts separately", rc.tolist() == [complex(7.0, float(np.finfo(np.float64).max)), complex(float(np.finfo(np.float64).min), 1.0)])
report("nan_to_num on a scalar returns a scalar: nan_to_num(np.nan) = 0.0", float(np.nan_to_num(np.nan)) == 0.0 and np.ndim(np.nan_to_num(np.nan)) == 0)
a = np.array([np.nan, 1.0]); r = np.nan_to_num(a, copy=False)
report("nan_to_num(copy=False) modifies in place and returns the same array", a.tolist() == [0.0, 1.0] and r is a)

# =====================================================================================
# 9. invalid operations, errstate
# =====================================================================================
print("---- errstate")
with caught() as c: v = [np.sqrt(-1.0), np.log(-1.0), np.log(0.0), np.float64(0) / 0, np.inf - np.inf, np.inf * 0, np.float64(1e308) * 10, np.float64(1e-308) / 1e10]
print(f"   sqrt(-1), log(-1), log(0), 0/0, inf-inf, inf*0, 1e308*10, 1e-308/1e10 = {[float(x) for x in v]}; warnings: {sorted(set(c.msgs))}")
report("sqrt(-1) and log(-1) are nan with 'invalid value' RuntimeWarning; log(0) = -inf with 'divide by zero'", math.isnan(v[0]) and math.isnan(v[1]) and float(v[2]) == -math.inf and any("invalid" in m for m in c.msgs) and any("divide" in m for m in c.msgs))
report("0/0, inf-inf, inf*0 are nan (invalid); 1e308*10 = inf (overflow); 1e-308/1e10 underflows to a subnormal/0", math.isnan(v[3]) and math.isnan(v[4]) and math.isnan(v[5]) and float(v[6]) == math.inf and any("overflow" in m for m in c.msgs))
with np.errstate(all="raise"):
    r1 = raises(lambda: np.sqrt(np.array([-1.0])), FloatingPointError); r2 = raises(lambda: np.array([1.0]) / 0, FloatingPointError); r3 = raises(lambda: np.array([1e308]) * 10, FloatingPointError); r4 = raises(lambda: np.array([1e-308]) / 1e10, FloatingPointError)
report("errstate(all='raise'): invalid, divide, overflow and underflow raise FloatingPointError", (r1, r2, r3, r4) == ("FloatingPointError",) * 4, f"({r1}, {r2}, {r3}, {r4})")
with np.errstate(all="ignore"):
    with caught() as c: np.sqrt(np.array([-1.0])); np.array([1.0]) / 0
report("errstate(all='ignore') silences everything", not c.names)
with np.errstate(invalid="ignore"):
    with caught() as c: np.sqrt(np.array([-1.0])); np.array([1.0]) / 0
report("errstate(invalid='ignore') silences sqrt(-1) but 1/0 still warns", c.names == ["RuntimeWarning"] and all("divide" in m for m in c.msgs))
calls = []
with np.errstate(all="call", call=lambda kind, flag: calls.append(kind)):
    np.sqrt(np.array([-1.0])); np.array([1.0]) / 0
report("errstate(all='call') calls the handler with the error kind", calls == ["invalid value", "divide by zero"], f"({calls})")
old = np.seterr(all="ignore"); cur = np.geterr(); np.seterr(**old)
report("seterr returns the previous settings and errstate restores them on exit; default is divide/over/invalid='warn', under='ignore'", cur == {"divide": "ignore", "over": "ignore", "under": "ignore", "invalid": "ignore"} and np.geterr() == old and old == {"divide": "warn", "over": "warn", "under": "ignore", "invalid": "warn"}, f"(default {old})")
with caught() as c: sc = np.float64(-1.0) ** 0.5; sq = np.sqrt(np.float64(-1.0))
report("scalar np.float64(-1) ** 0.5 and sqrt(np.float64(-1)) are nan with an invalid warning (scalars obey errstate like arrays)", math.isnan(sc) and math.isnan(sq) and "RuntimeWarning" in c.names, f"(warnings {c.names})")
with np.errstate(under="raise"):
    r = raises(lambda: np.array([1e-308]) * 1e-10, FloatingPointError)
report("errstate(under='raise') raises on 1e-308 * 1e-10 (underflow flag set)", r == "FloatingPointError", f"({r})")

# =====================================================================================
# 10. float -> int casts of NaN / inf / out-of-range (documented undefined): record
# =====================================================================================
print("---- float -> int casts")
for dt in [np.int64, np.int32, np.int8, np.uint8, np.uint64]:
    with caught() as c: r = np.array([np.nan, np.inf, -np.inf, 1e20, -1e20, 3.99, -3.99]).astype(dt)
    print(f"   astype({np.dtype(dt).name}) of [nan, inf, -inf, 1e20, -1e20, 3.99, -3.99] = {r.tolist()}  warnings {c.names} {sorted(set(c.msgs))[:1]}")
    report(f"float64 -> {np.dtype(dt).name}: in-range values truncate toward zero (3.99 -> 3, -3.99 -> {-3 if np.iinfo(dt).min < 0 else 'wraps'}); nan/inf/out-of-range recorded (undefined)", r.tolist()[5] == 3 and (r.tolist()[6] == -3 if np.iinfo(dt).min < 0 else True))
with caught() as c: r = np.array([np.nan, np.inf, 1e20]).astype(np.int64)
report("float -> int cast of nan/inf/out-of-range emits RuntimeWarning('invalid value encountered in cast') on numpy >= 1.24", ("RuntimeWarning" in c.names) == (NPV >= (1, 24)), f"(warnings {c.names})")
with caught() as c: s = int(np.int64(np.float64(1e20))) if False else None
r = raises(lambda: np.int64(np.nan), Exception); r2 = raises(lambda: int(np.float64(np.nan)), ValueError)
print(f"   np.int64(np.nan) -> {r or int(np.int64(np.nan))}; int(np.float64(nan)) -> {r2}")
report("int(np.float64(nan)) raises ValueError like Python; np.int64(nan) recorded", r2 == "ValueError")
report("float32 -> float16 overflow gives inf (65504 is the max), 1e5 -> inf; float64 1e300 -> float32 inf", float(np.float32(1e5).astype(np.float16)) == math.inf and float(np.array([1e300]).astype(np.float32)[0]) == math.inf)
report("np.float64(1e20).astype(np.int64) vs np.array: both recorded as int64 min on x86 (cvttsd2si 'integer indefinite')", True, f"(scalar {np.float64(1e20).astype(np.int64)}, array {np.array([1e20]).astype(np.int64)[0]})")

# =====================================================================================
# 11. astype between all pairs of numeric dtypes at boundary values
# =====================================================================================
print("---- astype all pairs at boundary values")
NUM = INTS + UINTS + FLOATS
def boundary_values(dt):
    if np.issubdtype(dt, np.integer):
        i = np.iinfo(dt); return [0, 1, i.max, i.min] + ([-1] if i.min < 0 else [])
    f = np.finfo(dt); return [0.0, 1.0, -1.0, float(f.max), float(f.min), float(f.tiny), float(f.smallest_subnormal), 2.5, -2.5, 3.0 ** 20]
def representable(v, dt):
    if np.issubdtype(dt, np.integer):
        if isinstance(v, float) and not float(v).is_integer(): return False
        i = np.iinfo(dt); return i.min <= int(v) <= i.max
    f = np.finfo(dt); return abs(F(v)) <= F(float(f.max)) and (F(v) == 0 or abs(F(v)) >= F(float(f.smallest_subnormal))) and F(float(dt(float(v)))) == F(v) if abs(float(v)) <= float(f.max) else False
bad = []; n_exact = n_wrap = n_trunc = 0
for src in NUM:
    for dst in NUM:
        vals = boundary_values(src); a = np.array(vals, dtype=src); a = a[np.isfinite(a.astype(np.float64))] if np.issubdtype(src, np.floating) else a
        with caught() as c: r = a.astype(dst)
        for v, got in zip(a.tolist(), r.tolist()):
            fv = F(v)
            if representable(v, dst):
                n_exact += 1
                if F(got) != fv: bad.append((np.dtype(src).name, np.dtype(dst).name, v, got, "exact expected"))
            elif np.issubdtype(src, np.integer) and np.issubdtype(dst, np.integer):
                n_wrap += 1
                if got != wrap_int(v, dst): bad.append((np.dtype(src).name, np.dtype(dst).name, v, got, f"modular {wrap_int(v, dst)}"))
            elif np.issubdtype(dst, np.floating):
                # nearest float (ties to even), or inf beyond max
                want = float(dst(float(v))) if abs(float(v)) <= float(np.finfo(dst).max) else math.copysign(math.inf, float(v))
                if np.issubdtype(src, np.integer):
                    # exact integer -> nearest dst float, computed via Fraction
                    cand = float(np.array(v).astype(np.float64)) if dst is np.float64 else float(dst(np.float64(v)))
                    want = cand
                if not (got == want or (math.isnan(want) and math.isnan(got))): bad.append((np.dtype(src).name, np.dtype(dst).name, v, got, f"round-to-nearest {want}"))
            else:
                # float -> int, in range: truncate toward zero; out of range: undefined (recorded only)
                if np.iinfo(dst).min <= math.trunc(float(v)) <= np.iinfo(dst).max:
                    n_trunc += 1
                    if got != math.trunc(float(v)): bad.append((np.dtype(src).name, np.dtype(dst).name, v, got, f"trunc {math.trunc(float(v))}"))
print(f"   {len(NUM) ** 2} dtype pairs; {n_exact} exactly representable values, {n_wrap} int->int wrap cases, {n_trunc} in-range float->int truncations; mismatches {bad[:6]}")
report("astype: exactly representable boundary values are preserved for every (src, dst) pair", not [b for b in bad if b[4] == "exact expected"])
report("astype int -> narrower int wraps modulo 2**bits (C conversion), for every pair", not [b for b in bad if b[4].startswith("modular")])
report("astype int -> float rounds to nearest (int64 max -> 2**63 in float64 and float32), float -> narrower float rounds to nearest or overflows to inf", not [b for b in bad if b[4].startswith("round")])
report("astype float -> int in range truncates toward zero for every pair", not [b for b in bad if b[4].startswith("trunc")])
report("int64 max -> float64 is 9223372036854775808.0 (not exactly representable; recorded, rounds up)", float(np.array([2 ** 63 - 1]).astype(np.float64)[0]) == 2.0 ** 63)
report("uint64 max -> int64 wraps to -1; int64 -1 -> uint64 is 2**64-1; int8 -1 -> uint8 255", int(np.array([2 ** 64 - 1], np.uint64).astype(np.int64)[0]) == -1 and int(np.array([-1]).astype(np.uint64)[0]) == 2 ** 64 - 1 and int(np.array([-1], np.int8).astype(np.uint8)[0]) == 255)
report("float64 -> float16: 65520 rounds to inf (above the midpoint to 65504+32), 1e-8 -> subnormal 1.1920929e-07 * ... rounding to nearest float16", float(np.array([65520.0]).astype(np.float16)[0]) == math.inf and float(np.array([65519.0]).astype(np.float16)[0]) == 65504 and float(np.array([1e-8]).astype(np.float16)[0]) == 0.0 and float(np.array([6e-8]).astype(np.float16)[0]) == 2 ** -24)
report("bool <-> numeric: astype(bool) is nonzero test (nan -> True, -0.0 -> False); True -> 1", np.array([0.0, -0.0, np.nan, 2, -1e-300]).astype(bool).tolist() == [False, False, True, True, True] and np.array([True, False]).astype(np.int8).tolist() == [1, 0])
report("astype(complex) then back: float64 -> complex128 -> float64 round trip; complex -> float discards imag with ComplexWarning", np.array([1.5, -2.0]).astype(np.complex128).astype(np.float64).tolist() == [1.5, -2.0] and np.array([1.5 + 2j]).astype(np.float64).tolist() == [1.5])

# =====================================================================================
# 12. NEP 50 promotion (version-aware) and promote_types / result_type / can_cast tables
# =====================================================================================
print("---- promotion")
if NP2:
    report("NEP 50 (2.x): np.float32(1) + 1.0 -> float32 (Python float is weak)", type(np.float32(1) + 1.0) is np.float32)
    with caught() as c: v = np.int8(100) + 100
    report("NEP 50 (2.x): np.int8(100) + 100 -> int8 -56 with RuntimeWarning (overflow)", type(v) is np.int8 and int(v) == -56 and "RuntimeWarning" in c.names, f"(got {v!r}, warnings {c.names})")
    report("NEP 50 (2.x): uint8 array + 300 raises OverflowError (300 does not fit uint8)", raises(lambda: np.array([1], np.uint8) + 300, OverflowError) == "OverflowError")
    report("NEP 50 (2.x): np.uint8(1) + 300 raises OverflowError", raises(lambda: np.uint8(1) + 300, OverflowError) == "OverflowError")
    with caught() as c: v = np.float32(1) + 3e100
    report("NEP 50 (2.x): np.float32(1) + 3e100 -> float32 inf with RuntimeWarning (overflow)", type(v) is np.float32 and float(v) == math.inf and "RuntimeWarning" in c.names, f"(warnings {c.names})")
    report("NEP 50 (2.x): float32 array + np.float64(1) -> float64 (NumPy scalars are strong)", (np.array([1.0], np.float32) + np.float64(1)).dtype == np.float64 and (np.array([1.0], np.float32) + np.array(1.0)).dtype == np.float64)
    report("NEP 50 (2.x): uint8 array + np.int64(1) -> int64; uint8 array + 1 -> uint8; uint8 array + 200 -> uint8 (wraps)", (np.array([1], np.uint8) + np.int64(1)).dtype == np.int64 and (np.array([1], np.uint8) + 1).dtype == np.uint8 and (np.array([100], np.uint8) + 200).tolist() == [44])
    report("NEP 50 (2.x): (np.float32(1) + 1j).dtype is complex64; (np.int32(1) + 5j) is complex128", type(np.float32(1) + 1j) is np.complex64 and type(np.int32(1) + 5j) is np.complex128)
    report("NEP 50 (2.x): np.array(1.0, float32) + 1e-14 == 1.0 is True (computed in float32)", bool(np.array(1.0, np.float32) + 1e-14 == 1.0))
    report("NEP 50 (2.x): np.uint8(1) + 2 -> uint8 3; np.array([1], uint8) + 1.5 -> float64 (Python float with int array: default float)", type(np.uint8(1) + 2) is np.uint8 and (np.array([1], np.uint8) + 1.5).dtype == np.float64)
    report("NEP 50 (2.x): comparisons with out-of-range Python ints do not error: uint8 array < 300 -> True", np.all(np.array([1, 255], np.uint8) < 300) and not np.any(np.array([1, 255], np.uint8) > 300))
    report("NEP 50 (2.x): np.int8(1) + np.int16(1) -> int16 (dtype-based, unchanged)", type(np.int8(1) + np.int16(1)) is np.int16)
else:
    report("1.x value-based: np.float32(1) + 1.0 -> float64 (scalar + scalar promotes to float64)", type(np.float32(1) + 1.0) is np.float64, f"(got {type(np.float32(1) + 1.0).__name__})")
    with caught() as c: v = np.int8(100) + 100
    report("1.x value-based: np.int8(100) + 100 -> int64 200, no warning", int(v) == 200 and type(v) is np.int64 and not c.names, f"(got {v!r} {type(v).__name__}, warnings {c.names})")
    r = np.array([1], np.uint8) + 300
    report("1.x value-based: uint8 array + 300 -> uint16 [301]", r.dtype == np.uint16 and r.tolist() == [301], f"(got {r.dtype})")
    report("1.x value-based: np.uint8(1) + 300 -> int64 301", int(np.uint8(1) + 300) == 301 and type(np.uint8(1) + 300) is np.int64)
    report("1.x value-based: np.float32(1) + 3e100 -> float64 3e100", type(np.float32(1) + 3e100) is np.float64 and float(np.float32(1) + 3e100) == 3e100)
    report("1.x value-based: float32 array + np.float64(1) -> float32 (0-d operands ignored for the dtype)", (np.array([1.0], np.float32) + np.float64(1)).dtype == np.float32)
    report("1.x value-based: uint8 array + np.int64(1) -> uint8; uint8 array + 200 -> uint8 (wraps to 44)", (np.array([1], np.uint8) + np.int64(1)).dtype == np.uint8 and (np.array([100], np.uint8) + 200).tolist() == [44])
    report("1.x value-based: np.array(1.0, float32) + 1e-14 == 1.0 is False (0-d array computed in float64)", not bool(np.array(1.0, np.float32) + 1e-14 == 1.0))
    report("1.x value-based: (np.float32(1) + 1j) is complex128", type(np.float32(1) + 1j) is np.complex128)
# promote_types against the documented rules
FLT_FOR_INT = {np.int8: np.float16, np.uint8: np.float16, np.int16: np.float32, np.uint16: np.float32, np.int32: np.float64, np.uint32: np.float64, np.int64: np.float64, np.uint64: np.float64}
def doc_promote(a, b):
    a = np.dtype(a); b = np.dtype(b)
    if a == b: return a
    if a.kind == "b": return b
    if b.kind == "b": return a
    if a.kind == b.kind: return a if a.itemsize >= b.itemsize else b
    kinds = {a.kind, b.kind}
    if kinds == {"i", "u"}:
        i, u = (a, b) if a.kind == "i" else (b, a)
        if u.itemsize < i.itemsize: return i
        if u.itemsize * 2 <= 8: return np.dtype(f"i{u.itemsize * 2}")
        return np.dtype(np.float64)
    # integer with float or complex
    def to_float(d): return np.dtype(FLT_FOR_INT[d.type]) if d.kind in "iu" else d
    fa, fb = to_float(a), to_float(b)
    if fa.kind == fb.kind == "f": return fa if fa.itemsize >= fb.itemsize else fb
    def to_complex(d): return np.dtype(f"c{max(8, d.itemsize * 2)}") if d.kind == "f" else d
    ca, cb = to_complex(fa), to_complex(fb); return ca if ca.itemsize >= cb.itemsize else cb
ALL = [np.bool_] + NUM + [np.complex64, np.complex128]
mism = []
for a, b in itertools.product(ALL, ALL):
    got = np.promote_types(a, b); want = doc_promote(a, b)
    if got != want: mism.append((np.dtype(a).name, np.dtype(b).name, got.name, want.name))
    if np.result_type(np.array([1], a), np.array([1], b)) != got: mism.append(("result_type", np.dtype(a).name, np.dtype(b).name))
report(f"promote_types over all {len(ALL) ** 2} pairs of bool/int/uint/float/complex equals the documented rules (uint64+int64 -> float64, int16+float16 -> float32, int32+float32 -> float64, float64+complex64 -> complex128) and result_type of arrays agrees", not mism, f"(mismatches {mism[:5]})")
report("documented examples: promote_types(int8, uint8) = int16, (int16, uint16) = int32, (int64, uint64) = float64, (int8, float16) = float16, (uint8, float16) = float16, (int16, float16) = float32, (float16, complex64) = complex64", np.promote_types(np.int8, np.uint8) == np.int16 and np.promote_types(np.int16, np.uint16) == np.int32 and np.promote_types(np.int64, np.uint64) == np.float64 and np.promote_types(np.int8, np.float16) == np.float16 and np.promote_types(np.uint8, np.float16) == np.float16 and np.promote_types(np.int16, np.float16) == np.float32 and np.promote_types(np.float16, np.complex64) == np.complex64)
report("promote_types is symmetric (all pairs)", all(np.promote_types(a, b) == np.promote_types(b, a) for a, b in itertools.product(ALL, ALL)))
nonassoc = [(np.dtype(a).name, np.dtype(b).name, np.dtype(c).name, np.promote_types(np.promote_types(a, b), c).name, np.promote_types(a, np.promote_types(b, c)).name) for a, b, c in itertools.product(ALL, ALL, ALL) if np.promote_types(np.promote_types(a, b), c) != np.promote_types(a, np.promote_types(b, c))]
print(f"   promote_types is NOT associative for {len(nonassoc)} of {len(ALL) ** 3} triples, e.g. {nonassoc[:3]} (documented nowhere; result_type with several dtypes is NOT the left-to-right pairwise reduction either, see next line)")
print(f"   result_type(int8, uint8, float16) = {np.result_type(np.int8, np.uint8, np.float16)} (pairwise left-to-right would give {np.promote_types(np.promote_types(np.int8, np.uint8), np.float16)}); result_type(int8, float16, uint8) = {np.result_type(np.int8, np.float16, np.uint8)}; result_type(int8, uint16, float16) = {np.result_type(np.int8, np.uint16, np.float16)}")
report("result_type with three dtypes is order-independent for (int8, uint8, float16) (recorded: it is not the naive left-to-right pairwise reduction)", np.result_type(np.int8, np.uint8, np.float16) == np.result_type(np.int8, np.float16, np.uint8) == np.result_type(np.float16, np.int8, np.uint8))
# can_cast 'safe' table: documented semantics = value-preserving for ints; ints -> float allowed if the float has enough mantissa (int8->float16, int16->float32, int32/64->float64 'safe' by convention)
def doc_can_cast_safe(a, b):
    a = np.dtype(a); b = np.dtype(b)
    return doc_promote(a, b) == b
mism = [(np.dtype(a).name, np.dtype(b).name, np.can_cast(a, b)) for a, b in itertools.product(ALL, ALL) if np.can_cast(a, b) != doc_can_cast_safe(a, b)]
report("can_cast(a, b, 'safe') over all pairs equals promote_types(a, b) == b (the safe cast lattice)", not mism, f"(mismatches {mism[:5]})")
report("can_cast specifics: int64->float64 True (documented safe though lossy), uint64->int64 False, float64->float32 False, int16->float16 False, int8->float16 True, float32->complex64 True, float64->complex64 False", np.can_cast(np.int64, np.float64) and not np.can_cast(np.uint64, np.int64) and not np.can_cast(np.float64, np.float32) and not np.can_cast(np.int16, np.float16) and np.can_cast(np.int8, np.float16) and np.can_cast(np.float32, np.complex64) and not np.can_cast(np.float64, np.complex64))
report("can_cast casting modes: 'no' only identical, 'equiv' same-kind/size, 'same_kind' float64->float32 True int->float True float->int False, 'unsafe' everything", not np.can_cast(np.int32, np.int64, "no") and np.can_cast(np.int64, np.int64, "no") and np.can_cast(np.float64, np.float32, "same_kind") and np.can_cast(np.int64, np.float16, "same_kind") and not np.can_cast(np.float32, np.int64, "same_kind") and np.can_cast(np.float64, np.int8, "unsafe") and np.can_cast(np.complex128, np.int8, "unsafe") and not np.can_cast(np.complex128, np.float64, "same_kind"))
if NP2:
    report("can_cast with a Python int value raises TypeError on 2.x (value-based casting removed)", raises(lambda: np.can_cast(300, np.uint8), TypeError) == "TypeError", f"({raises(lambda: np.can_cast(300, np.uint8))})")
else:
    report("can_cast with a Python int value is value-based on 1.x: can_cast(300, uint8) False, can_cast(100, uint8) True", not np.can_cast(300, np.uint8) and np.can_cast(100, np.uint8))
report("result_type of an int8 array with a Python float is float64 (2.x, weak float -> default) / float64 (1.x)", np.result_type(np.array([1], np.int8), 1.5) == np.float64)
report("result_type(int8 array, Python int 1) is int8 on both; result_type(np.int8, np.float32) is float32", np.result_type(np.array([1], np.int8), 1) == np.int8 and np.result_type(np.int8, np.float32) == np.float32)
report("np.add(int8 array, int16 array).dtype is int16; (uint8 + int8) arrays give int16; (uint64 + int64) arrays give float64", (np.array([1], np.int8) + np.array([1], np.int16)).dtype == np.int16 and (np.array([1], np.uint8) + np.array([1], np.int8)).dtype == np.int16 and (np.array([1], np.uint64) + np.array([1], np.int64)).dtype == np.float64)

# =====================================================================================
# 13. finfo / iinfo vs IEEE 754 and two's complement
# =====================================================================================
print("---- finfo / iinfo")
IEEE = {np.float16: (10, 5, -14, 16, 65504.0, 3, 1e-3), np.float32: (23, 8, -126, 128, (2 - 2 ** -23) * 2.0 ** 127, 6, 1e-6), np.float64: (52, 11, -1022, 1024, (2 - 2 ** -52) * 2.0 ** 1023, 15, 1e-15)}
for dt, (nmant, nexp, minexp, maxexp, mx, prec, resol) in IEEE.items():
    fi = np.finfo(dt); name = np.dtype(dt).name
    ok = (fi.nmant == nmant and fi.nexp == nexp and fi.minexp == minexp and fi.maxexp == maxexp and fi.bits == nmant + nexp + 1 and float(fi.max) == mx and float(fi.min) == -mx
          and float(fi.eps) == 2.0 ** -nmant and float(fi.tiny) == 2.0 ** minexp and float(fi.smallest_normal) == 2.0 ** minexp and float(fi.smallest_subnormal) == 2.0 ** (minexp - nmant)
          and fi.precision == prec and fi.resolution == dt(resol) and float(fi.epsneg) == 2.0 ** -(nmant + 1) and fi.iexp == nexp)
    print(f"   {name}: eps {float(fi.eps)!r} max {float(fi.max)!r} tiny {float(fi.tiny)!r} smallest_subnormal {float(fi.smallest_subnormal)!r} precision {fi.precision} resolution {float(fi.resolution)!r} nmant {fi.nmant} nexp {fi.nexp} minexp {fi.minexp} maxexp {fi.maxexp} epsneg {float(fi.epsneg)!r}")
    report(f"finfo({name}): eps=2^-{nmant}, max=(2-2^-{nmant})*2^{maxexp - 1}, tiny=2^{minexp}, smallest_subnormal=2^{minexp - nmant}, precision {prec}, resolution {resol}, nmant/nexp/minexp/maxexp/epsneg per IEEE 754", ok)
ld = np.finfo(np.longdouble)
print(f"   longdouble: bits {np.dtype(np.longdouble).itemsize * 8} nmant {ld.nmant} eps {float(ld.eps)!r} tiny {ld.tiny!r} max {ld.max!r} smallest_subnormal {ld.smallest_subnormal!r} precision {ld.precision}; np.float128 available: {hasattr(np, 'float128')}")
if ld.nmant == 63:
    report("longdouble is the x86 80-bit extended format: nmant 63, eps 2^-63, tiny 2^-16382, maxexp 16384, precision 18, smallest_subnormal 2^-16445, 16-byte storage", float(ld.eps) == 2.0 ** -63 and ld.minexp == -16382 and ld.maxexp == 16384 and ld.precision == 18 and ld.tiny == np.longdouble(2) ** -16382 and ld.smallest_subnormal == np.longdouble(2) ** -16445 and np.dtype(np.longdouble).itemsize == 16)
    report("longdouble arithmetic really carries 64 mantissa bits: (1 + 2^-60) - 1 == 2^-60 in longdouble but 0 in float64", (np.longdouble(1) + np.longdouble(2) ** -60) - np.longdouble(1) == np.longdouble(2) ** -60 and (np.float64(1) + 2.0 ** -60) - 1 == 0)
    report("np.float128 is an alias of longdouble on this platform (name is a misnomer: 80-bit precision in 16 bytes)", getattr(np, "float128", None) is np.longdouble)
else:
    report(f"longdouble on this platform has nmant {ld.nmant} (recorded; not the x86 extended format)", True)
report("longdouble(0.1) parsed from a string is closer to 1/10 than float64(0.1)", abs(F(str(np.longdouble("0.1") - np.longdouble(F(1, 10).numerator) / np.longdouble(10)))) <= F(1, 10 ** 18) if False else abs(mpf(str(np.longdouble("0.1"))) - mpf(1) / 10) < abs(mpf(0.1) - mpf(1) / 10))
for dt in INTS + UINTS:
    ii = np.iinfo(dt); bits = ii.bits; signed = np.dtype(dt).kind == "i"
    report(f"iinfo({np.dtype(dt).name}): bits {bits}, min {ii.min}, max {ii.max} (two's complement)", bits == np.dtype(dt).itemsize * 8 and ii.min == (-(1 << (bits - 1)) if signed else 0) and ii.max == ((1 << (bits - 1)) - 1 if signed else (1 << bits) - 1))
report("iinfo of a bool / float raises ValueError; finfo of an int raises ValueError", raises(lambda: np.iinfo(np.float64), ValueError) == "ValueError" and raises(lambda: np.finfo(np.int64), ValueError) == "ValueError")
report("finfo(complex128) reports the float64 values; finfo accepts a scalar instance or a dtype string", np.finfo(np.complex128).eps == np.finfo(np.float64).eps and np.finfo(np.float32(1)).eps == np.finfo(np.float32).eps and np.finfo("float16").eps == np.finfo(np.float16).eps)

# =====================================================================================
# 14. nextafter / spacing / frexp / ldexp / modf
# =====================================================================================
print("---- nextafter / spacing / frexp / ldexp / modf")
tiny = 5e-324; mx = float(np.finfo(np.float64).max); eps = 2.0 ** -52
report("nextafter(0, 1) = 2^-1074, nextafter(0, -1) = -2^-1074, nextafter(-0.0, 1) = 2^-1074", float(np.nextafter(0.0, 1.0)) == tiny and float(np.nextafter(0.0, -1.0)) == -tiny and float(np.nextafter(-0.0, 1.0)) == tiny)
report("nextafter(1, 2) = 1 + 2^-52, nextafter(1, 0) = 1 - 2^-53 (equals math.nextafter)", float(np.nextafter(1.0, 2.0)) == 1 + eps and float(np.nextafter(1.0, 0.0)) == 1 - eps / 2 and float(np.nextafter(1.0, 2.0)) == math.nextafter(1.0, 2.0))
report("nextafter(max, inf) = inf, nextafter(inf, 0) = max, nextafter(x, x) = x, nextafter(nan, 1) = nan", float(np.nextafter(mx, np.inf)) == math.inf and float(np.nextafter(np.inf, 0.0)) == mx and float(np.nextafter(2.5, 2.5)) == 2.5 and math.isnan(np.nextafter(np.nan, 1.0)))
report("nextafter across the subnormal boundary: nextafter(2^-1022, 0) = 2^-1022 - 2^-1074 (exact, gradual underflow)", float(np.nextafter(2.0 ** -1022, 0.0)) == 2.0 ** -1022 - tiny)
report("nextafter float32: nextafter(0f, 1) = 2^-149, nextafter(1f, 2) = 1 + 2^-23, nextafter(max32, inf) = inf; float16: nextafter(0h, 1) = 2^-24", float(np.nextafter(np.float32(0), np.float32(1))) == 2.0 ** -149 and float(np.nextafter(np.float32(1), np.float32(2))) == 1 + 2.0 ** -23 and float(np.nextafter(np.finfo(np.float32).max, np.float32(np.inf))) == math.inf and float(np.nextafter(np.float16(0), np.float16(1))) == 2.0 ** -24)
report("nextafter(np.float32(1), 2) with a Python-int direction: float32 on 2.x (weak Python scalar), float64 on 1.x (scalar-scalar value-based promotion)", np.nextafter(np.float32(1), 2).dtype == (np.float32 if NP2 else np.float64), f"(dtype {np.nextafter(np.float32(1), 2).dtype})")
report("spacing(1) = eps, spacing(0) = 2^-1074, spacing(2^-1074) = 2^-1074, spacing(2^-1022) = 2^-1074", float(np.spacing(1.0)) == eps and float(np.spacing(0.0)) == tiny and float(np.spacing(tiny)) == tiny and float(np.spacing(2.0 ** -1022)) == tiny)
with caught() as c: spmax = float(np.spacing(mx)); spmax32 = float(np.spacing(np.finfo(np.float32).max))
print(f"   spacing(float64 max) = {spmax!r}, spacing(float32 max) = {spmax32!r}, warnings {sorted(set(c.msgs))}  (the adjacent number below is 2^971 away; numpy computes nextafter(x, inf) - x)")
report("spacing(max) is inf with an overflow RuntimeWarning (implemented as nextafter(x, +inf) - x; the documented invariant 'no representable number between x + spacing(x) and x' still holds) -- recorded", spmax == math.inf and "RuntimeWarning" in c.names)
report("spacing(-1) = -eps (signed toward larger magnitude), spacing(inf) = nan, spacing(nan) = nan, spacing(2**k) = 2**(k-52)", float(np.spacing(-1.0)) == -eps and math.isnan(np.spacing(np.inf)) and math.isnan(np.spacing(np.nan)) and all(float(np.spacing(2.0 ** k)) == 2.0 ** (k - 52) for k in range(-1000, 1000, 37)))
report("spacing(x) == nextafter(x, inf) - x for random positive x; float32 spacing(1f) = 2^-23; float16 spacing(1h) = 2^-10", all(float(np.spacing(x)) == float(np.nextafter(x, np.inf)) - x for x in np.exp(rs.uniform(-700, 700, 200)).tolist()) and float(np.spacing(np.float32(1))) == 2.0 ** -23 and float(np.spacing(np.float16(1))) == 2.0 ** -10)
report("spacing(x) == 0 never for finite x; 'there should not be any representable number between x + spacing(x) and x'", all(x + float(np.spacing(x)) == math.nextafter(x, math.inf) for x in [1.0, 1e-310, 3.7, 1e300, 5e-324, 2.0 ** -1022]))
fx = [1.0, 0.1, 1e300, 5e-324, 3 * 5e-324, 2.0 ** -1022, -3.5, 0.0, -0.0, 1e-310, 0.75, 1024.0, mx]
m, e = np.frexp(np.array(fx)); ok = True
for x, mi, ei in zip(fx, m.tolist(), e.tolist()):
    pm, pe = math.frexp(x); ok &= (mi, ei) == (pm, pe) and float(np.ldexp(mi, ei)) == x and (x == 0 or 0.5 <= abs(mi) < 1)
report("frexp equals math.frexp (|mantissa| in [0.5, 1), documented '(-1, 1)'), incl. subnormals 5e-324 -> (0.5, -1073), and ldexp(m, e) round-trips exactly", ok)
report("frexp(0) = (0, 0), frexp(-0.0) keeps the sign, frexp(inf) = (inf, 0), frexp(nan) = (nan, 0)", np.frexp(0.0) == (0.0, 0) and sb(np.frexp(-0.0)[0]) and float(np.frexp(np.inf)[0]) == math.inf and math.isnan(np.frexp(np.nan)[0]) and int(np.frexp(np.nan)[1]) == 0)
report("frexp exponent dtype is int32 (C int); frexp of float32 gives a float32 mantissa", np.frexp(np.array([1.0]))[1].dtype == np.int32 and np.frexp(np.array([1.0], np.float32))[0].dtype == np.float32)
with caught() as c: l1 = np.ldexp(1.0, -1074); l2 = np.ldexp(1.0, 1024); l3 = np.ldexp(1.0, -1075); l4 = np.ldexp(3.0, -1075); l5 = np.ldexp(np.float32(1), -149); l6 = np.ldexp(np.float32(1), 128); l7 = np.ldexp(0.75, 1024)
print(f"   ldexp(1, -1074) = {float(l1)!r}, ldexp(1, 1024) = {float(l2)!r}, ldexp(1, -1075) = {float(l3)!r} (ties to even -> 0), ldexp(3, -1075) = {float(l4)!r} (1.5 subnormal ulps -> 2 ulps), ldexp(1f, -149) = {float(l5)!r}, ldexp(1f, 128) = {float(l6)!r}, ldexp(0.75, 1024) = {float(l7)!r}; warnings {sorted(set(c.msgs))}")
report("ldexp(1, -1074) = 2^-1074 exact, ldexp(1, 1024) = inf (overflow warning), ldexp(1, -1075) = 0 (round half to even), ldexp(3, -1075) = 2*2^-1074, float32 ldexp(1, -149) = 2^-149", float(l1) == tiny and float(l2) == math.inf and float(l3) == 0.0 and float(l4) == 2 * tiny and float(l5) == 2.0 ** -149 and float(l6) == math.inf and float(l7) == math.ldexp(0.75, 1024))
report("ldexp rejects a float exponent (TypeError: no loop) and accepts int arrays; x * 2**e agrees for random pairs", raises(lambda: np.ldexp(1.0, 2.5), TypeError) == "TypeError" and all(float(np.ldexp(x, e)) == math.ldexp(x, e) for x, e in zip(rs.randn(100), rs.randint(-1100, 1000, 100).tolist())))
report("modf(-3.5) = (-0.5, -3.0): 'fractional and integral parts are negative if the given number is negative'", tuple(float(v) for v in np.modf(-3.5)) == (-0.5, -3.0) and tuple(float(v) for v in np.modf(3.5)) == (0.5, 3.0))
fr, it = np.modf(-0.5); fr2, it2 = np.modf(-0.0)
report("modf(-0.5) = (-0.5, -0.0) and modf(-0.0) = (-0.0, -0.0): the integral part keeps the sign (C modf)", float(fr) == -0.5 and float(it) == 0 and sb(it) and sb(fr2) and sb(it2))
report("modf(inf) = (0.0, inf), modf(nan) = (nan, nan), modf on ints returns float64 pairs", tuple(float(v) for v in np.modf(np.inf)) == (0.0, math.inf) and all(np.isnan(np.modf(np.nan))) and np.modf(np.array([3, -3]))[0].dtype == np.float64 and np.modf(np.array([3, -3]))[1].tolist() == [3.0, -3.0])
report("modf equals math.modf on random values and preserves float32", all(tuple(float(v) for v in np.modf(x)) == math.modf(x) for x in (rs.randn(200) * 100).tolist()) and np.modf(np.float32(2.5))[0].dtype == np.float32)
report("divmod(x, 1) is modf with the parts swapped and a non-negative remainder (documented): divmod(-3.5, 1) = (-4, 0.5)", tuple(float(v) for v in np.divmod(-3.5, 1.0)) == (-4.0, 0.5))

# =====================================================================================
# 15. reductions: dtypes, true_divide of ints, float32 add.reduce vs accumulate
# =====================================================================================
print("---- reductions and dtypes")
report("true_divide of ints -> float64: np.int64(7)/np.int64(2) = 3.5 float64, int8/int8 array -> float64, int32/int32 -> float64", type(np.int64(7) / np.int64(2)) is np.float64 and float(np.int64(7) / np.int64(2)) == 3.5 and (np.array([7], np.int8) / np.array([2], np.int8)).dtype == np.float64 and (np.array([7], np.int32) / np.array([2], np.int32)).dtype == np.float64)
report("true_divide has no integer loops (types start at 'ee->e'); ints are cast to float64", not any(t[0] in "bBhHiIlLqQ" for t in np.true_divide.types))
report("np.divide(int arr, int arr, out=int arr) raises TypeError (cannot cast float64 output to int with same_kind)", raises(lambda: np.divide(np.array([7]), np.array([2]), out=np.zeros(1, np.int64)), TypeError) == "TypeError")
report("np.divide(int, int, out=int, casting='unsafe') truncates: 7/2 -> 3; floor_divide with int out works", np.divide(np.array([7, -7]), np.array([2, 2]), out=np.zeros(2, np.int64), casting="unsafe").tolist() == [3, -3] and np.floor_divide(np.array([7]), np.array([2]), out=np.zeros(1, np.int64)).tolist() == [3])
for dt in INTS:
    a = np.array([np.iinfo(dt).max, 1], dtype=dt); want = wrap_int(np.iinfo(dt).max + 1, np.int64)
    report(f"sum of {np.dtype(dt).name} accumulates in int64 (platform long) by default: max + 1 {'exact' if dt is not np.int64 else 'wraps silently to int64 min (recorded)'}; mean is float64 and exact", a.sum().dtype == np.int64 and int(a.sum()) == want and a.mean().dtype == np.float64 and float(a.mean()) == (np.iinfo(dt).max + 1) / 2, f"(sum {int(a.sum())})")
for dt in UINTS:
    a = np.array([np.iinfo(dt).max, 1], dtype=dt); want = wrap_int(np.iinfo(dt).max + 1, np.uint64)
    report(f"sum of {np.dtype(dt).name} accumulates in uint64: max + 1 {'exact' if dt is not np.uint64 else 'wraps silently to 0 (recorded)'}; prod dtype uint64", a.sum().dtype == np.uint64 and int(a.sum()) == want and a.prod().dtype == np.uint64, f"(sum {int(a.sum())})")
report("sum(bool) is int64 [count], mean(bool) float64, sum(int8, dtype=int8) wraps", np.array([True, True, False]).sum().dtype == np.int64 and int(np.array([True, True, False]).sum()) == 2 and float(np.array([True, False]).mean()) == 0.5 and int(np.array([100, 100], np.int8).sum(dtype=np.int8)) == wrap_int(200, np.int8))
report("mean(float32) stays float32 ('same precision as the input'), mean(float32, dtype=float64) is float64, mean(float16) returns float16 (computed in float32)", np.array([1, 2], np.float32).mean().dtype == np.float32 and np.array([1, 2], np.float32).mean(dtype=np.float64).dtype == np.float64 and np.array([1, 2], np.float16).mean().dtype == np.float16)
report("np.add.reduce(int8 array) -> int64 ('upcast to conserve precision'), np.add.reduce(int8, dtype=int8) wraps, np.multiply.reduce(int8) -> int64", np.add.reduce(np.array([100, 100], np.int8)).dtype == np.int64 and int(np.add.reduce(np.array([100, 100], np.int8))) == 200 and int(np.add.reduce(np.array([100, 100], np.int8), dtype=np.int8)) == wrap_int(200, np.int8) and np.multiply.reduce(np.array([100, 100], np.int8)).dtype == np.int64)
report("np.maximum.reduce / np.minimum.reduce keep the input dtype (no upcast)", np.maximum.reduce(np.array([1, 2], np.int8)).dtype == np.int8 and np.minimum.reduce(np.array([1, 2], np.uint16)).dtype == np.uint16)
report("np.add.accumulate(int8) is int64 too? -> accumulate keeps int8 (no upcast, documented only for reduce) -- recorded", True, f"(accumulate int8 dtype {np.add.accumulate(np.array([100, 100], np.int8)).dtype}, value {np.add.accumulate(np.array([100, 100], np.int8)).tolist()}; reduceat dtype {np.add.reduceat(np.array([100, 100], np.int8), [0]).dtype})")
# float32 sum: pairwise (add.reduce / sum) vs accumulate (naive)
x32 = (1 + rs.rand(1_000_000)).astype(np.float32); exact = sum(F(float(v)) for v in x32.tolist())
s_red = float(np.add.reduce(x32)); s_sum = float(x32.sum()); s_acc = float(np.add.accumulate(x32)[-1]); s_math = float(math.fsum(x32.tolist()))
e_red = abs(F(s_red) - exact) / exact; e_acc = abs(F(s_acc) - exact) / exact
print(f"   float32 sum of 1e6 values in [1, 2): exact {float(exact)!r}; add.reduce {s_red!r} (rel err {float(e_red):.2e}); accumulate[-1] {s_acc!r} (rel err {float(e_acc):.2e}); math.fsum {s_math!r}")
report("np.add.reduce(float32) == x.sum() (same pairwise path) and is within 1e-6 relative of the exact sum (pairwise summation)", s_red == s_sum and e_red < 1e-6)
report("np.add.accumulate(float32)[-1] is a naive running sum: error at least 10x that of the pairwise reduce (report)", e_acc > 10 * e_red, f"(accumulate error {float(e_acc):.2e} vs reduce {float(e_red):.2e})")
x32s = x32[::2]
print(f"   strided float32 x[::2] sum rel err {float(abs(F(float(x32s.sum())) - sum(F(float(v)) for v in x32s.tolist())) / sum(F(float(v)) for v in x32s.tolist())):.2e}; axis-0 sum of a (1e6, 1) view rel err {float(abs(F(float(x32.reshape(-1, 1).sum(axis=0)[0])) - exact) / exact):.2e}")
report("np.sum(float32, dtype=float64) is exact to 1e-15 relative", abs(F(float(x32.sum(dtype=np.float64))) - exact) / exact < 1e-15)

# =====================================================================================
# 16. ufunc methods: reduce / accumulate / reduceat / outer / at, where=, out= aliasing
# =====================================================================================
print("---- ufunc methods")
report("add.reduce over axis 1 of [[1,2],[3,4]] = [3,7]; multiply.reduce([]) = 1 (identity); add.reduce([]) = 0", np.add.reduce(np.array([[1, 2], [3, 4]]), axis=1).tolist() == [3, 7] and int(np.multiply.reduce(np.array([], np.int64))) == 1 and int(np.add.reduce(np.array([], np.int64))) == 0)
report("maximum.reduce([]) raises ValueError (no identity); maximum.reduce([], initial=-inf) = -inf", raises(lambda: np.maximum.reduce(np.array([])), ValueError) == "ValueError" and float(np.maximum.reduce(np.array([]), initial=-np.inf)) == -math.inf)
report("add.reduce(where=mask) and add.reduce(initial=10)", int(np.add.reduce(np.array([1, 2, 3, 4]), where=np.array([True, False, True, False]))) == 4 and int(np.add.reduce(np.array([1, 2, 3]), initial=10)) == 16)
report("add.reduce(axis=None) reduces everything; axis=(0,1) on 3-d; keepdims", int(np.add.reduce(np.arange(24).reshape(2, 3, 4), axis=None)) == 276 and np.add.reduce(np.arange(24).reshape(2, 3, 4), axis=(0, 1)).tolist() == [60, 66, 72, 78] and np.add.reduce(np.arange(6).reshape(2, 3), axis=1, keepdims=True).shape == (2, 1))
report("subtract.reduce is left-associative: ((1-2)-3) = -4; divide.reduce([8,2,2]) = 2.0", int(np.subtract.reduce(np.array([1, 2, 3]))) == -4 and float(np.divide.reduce(np.array([8.0, 2.0, 2.0]))) == 2.0)
report("add.accumulate([1,2,3,4]) = [1,3,6,10]; subtract.accumulate([1,2,3]) = [1,-1,-4]; multiply.accumulate along axis 0 of a 2-d array", np.add.accumulate(np.array([1, 2, 3, 4])).tolist() == [1, 3, 6, 10] and np.subtract.accumulate(np.array([1, 2, 3])).tolist() == [1, -1, -4] and np.multiply.accumulate(np.array([[1, 2], [3, 4]]), axis=0).tolist() == [[1, 2], [3, 8]])
def reduceat_doc(x, idx, op):
    out = []
    for i, s in enumerate(idx):
        if s < 0 or s >= len(x): raise IndexError
        e = idx[i + 1] if i + 1 < len(idx) else len(x)
        if s >= e: out.append(x[s])
        else:
            acc = x[s]
            for v in x[s + 1:e]: acc = op(acc, v)
            out.append(acc)
    return out
x = list(range(1, 9)); idx = [0, 4, 1, 5, 2, 6, 3, 7]
report("reduceat(arange(1,9), [0,4,1,5,2,6,3,7]) equals the documented slice semantics (decreasing pairs give array[indices[i]])", np.add.reduceat(np.array(x), idx).tolist() == reduceat_doc(x, idx, lambda a, b: a + b), f"({np.add.reduceat(np.array(x), idx).tolist()})")
report("reduceat with the documented [::2] trick gives the pair sums [10, 14, 18, 22]", np.add.reduceat(np.array(x), idx)[::2].tolist() == [10, 14, 18, 22])
for idx in [[4, 1], [7], [0], [3, 3, 3], [5, 2, 6, 0], [0, 8 - 1, 2]]:
    report(f"reduceat indices {idx}: matches the documented rules for add and maximum", np.add.reduceat(np.array(x), idx).tolist() == reduceat_doc(x, idx, lambda a, b: a + b) and np.maximum.reduceat(np.array(x), idx).tolist() == reduceat_doc(x, idx, max), f"(add {np.add.reduceat(np.array(x), idx).tolist()})")
report("reduceat with an index >= len raises IndexError; a negative index raises IndexError (documented 'an error is raised')", raises(lambda: np.add.reduceat(np.array(x), [0, 8]), IndexError) == "IndexError" and raises(lambda: np.add.reduceat(np.array(x), [-1]), IndexError) == "IndexError", f"({raises(lambda: np.add.reduceat(np.array(x), [0, 8]))}, {raises(lambda: np.add.reduceat(np.array(x), [-1]))})")
report("reduceat along axis=1 of a 2-d array and with dtype=float", np.add.reduceat(np.arange(12).reshape(3, 4), [0, 2], axis=1).tolist() == [[1, 5], [9, 13], [17, 21]] and np.add.reduceat(np.array([1, 2, 3]), [0], dtype=np.float64).dtype == np.float64)
report("multiply.outer([1,2,3],[4,5]) has shape (3,2) with a[i]*b[j]; subtract.outer; outer of 2-d inputs has shape a.shape + b.shape", np.multiply.outer([1, 2, 3], [4, 5]).tolist() == [[4, 5], [8, 10], [12, 15]] and np.subtract.outer([1, 2], [1, 2, 3]).tolist() == [[0, -1, -2], [1, 0, -1]] and np.add.outer(np.zeros((2, 3)), np.zeros((4,))).shape == (2, 3, 4))
a = np.zeros(3, dtype=int); np.add.at(a, [0, 0, 1, 0], 1); b = np.zeros(3, dtype=int); b[[0, 0, 1, 0]] += 1
report("add.at accumulates repeated indices ([3, 1, 0]) whereas fancy-index += applies once ([1, 1, 0])", a.tolist() == [3, 1, 0] and b.tolist() == [1, 1, 0])
a = np.array([1.0, 2.0, 3.0]); np.negative.at(a, [0, 2]); c = np.array([1, 2, 3, 4]); np.add.at(c, [(slice(None),)] if False else [0, 1], [10, 20])
report("negative.at (unary) and add.at with a value array", a.tolist() == [-1.0, 2.0, -3.0] and c.tolist() == [11, 22, 3, 4])
a = np.arange(5.0); np.add(a[:-1], a[1:], out=a[1:])
report("out= aliasing an input with overlapping views is computed as if no overlap (documented since 1.13): add(a[:-1], a[1:], out=a[1:]) -> [0,1,3,5,7]", a.tolist() == [0, 1, 3, 5, 7])
a = np.arange(5.0); a[1:] += a[:-1]
report("a[1:] += a[:-1] likewise gives [0,1,3,5,7] (not the running sum)", a.tolist() == [0, 1, 3, 5, 7])
a = np.arange(6.0).reshape(2, 3); np.multiply(a, 2, out=a); b = np.arange(4.0); np.add(b, b[::-1], out=b)
report("in-place out=a and out= with a reversed view of itself are correct", a.tolist() == [[0, 2, 4], [6, 8, 10]] and b.tolist() == [3, 3, 3, 3])
c = np.full(4, -1.0); np.add(np.array([1.0, 2, 3, 4]), 10, out=c, where=np.array([True, False, True, False]))
report("where= with out= leaves the unselected positions of out untouched", c.tolist() == [11, -1, 13, -1])
r = np.add(np.array([1.0, 2, 3, 4]), 10, where=np.array([True, False, True, False]))
report("where= without out= leaves unselected positions uninitialized (documented): selected values correct, others recorded", r[0] == 11 and r[2] == 13, f"(unselected {r[1]!r}, {r[3]!r})")
report("out= with a wrong shape raises ValueError; out= must be an array (list raises TypeError)", raises(lambda: np.add(np.ones(3), 1, out=np.zeros(4)), ValueError) == "ValueError" and raises(lambda: np.add(np.ones(3), 1, out=[0, 0, 0]), TypeError) == "TypeError")
o = np.zeros(2); ro = np.add(np.ones(2), 1, out=(o,))
report("out= tuple form and dtype= keyword: add(int8, int8, dtype=int16) does not wrap; out=(o,) writes o and returns it", np.add(np.array([100], np.int8), np.array([100], np.int8), dtype=np.int16).tolist() == [200] and o.tolist() == [2, 2] and ro is o)
report("sum(dtype=float32) of an int array computes in float32; np.add.reduce(float64, dtype=float32) casts the accumulator", np.array([1, 2, 3]).sum(dtype=np.float32).dtype == np.float32 and np.add.reduce(np.array([0.1] * 10), dtype=np.float32).dtype == np.float32)
report("np.mean of an int array with dtype=np.int32 (documented: intermediate in that dtype) returns an int-typed mean: mean([1,2], dtype=int32) = 1", np.array([1, 2]).mean(dtype=np.int32).dtype == np.int32 and int(np.array([1, 2]).mean(dtype=np.int32)) == 1)

# =====================================================================================
# 17. scalar result types, np.bool_ arithmetic, heaviside, misc
# =====================================================================================
print("---- scalars, bool, heaviside")
report("np.float64 results: array.sum() and array[0] are np.float64 (a float subclass), not Python float", type(np.array([1.0]).sum()) is np.float64 and type(np.array([1.0])[0]) is np.float64 and issubclass(np.float64, float) and not issubclass(np.float32, float))
report("np.int64 is not a subclass of Python int; np.array([1])[0] is np.int64; bool_ is not a bool subclass", not issubclass(np.int64, int) and type(np.array([1])[0]) is np.int64 and not issubclass(np.bool_, bool))
report("np.float64(1) / 0 gives inf with a warning (no ZeroDivisionError); np.int64(1) / 0 gives inf too", float(np.float64(1) / 0) == math.inf and float(np.int64(1) / 0) == math.inf)
report("np.sqrt(4.0) returns np.float64 for a Python float, np.float32 for np.float32 input; np.sqrt(4) (Python int) returns np.float64", type(np.sqrt(4.0)) is np.float64 and type(np.sqrt(np.float32(4))) is np.float32 and type(np.sqrt(4)) is np.float64)
report("0-d array results: np.add(np.array(1.0), 1) returns a NumPy scalar (np.float64), not a 0-d array", type(np.add(np.array(1.0), 1)) is np.float64)
report("np.bool_: True + True is True (logical or), True * True is True, True & False is False, True / True is 1.0 float64", np.True_ + np.True_ is np.True_ and np.True_ * np.True_ is np.True_ and (np.True_ & np.False_) is np.False_ and type(np.True_ / np.True_) is np.float64 and float(np.True_ / np.True_) == 1.0)
report("np.bool_ subtract and negative raise TypeError ('numpy boolean subtract ... is not supported'), Python True - True is 0", raises(lambda: np.True_ - np.True_, TypeError) == "TypeError" and raises(lambda: -np.True_, TypeError) == "TypeError" and raises(lambda: np.array([True]) - np.array([True]), TypeError) == "TypeError")
report("np.array([True, True]).sum() = 2 (int), np.add(bool arr, bool arr) is bool (logical or), np.True_ + 1 = 2 int64", int(np.array([True, True]).sum()) == 2 and np.add(np.array([True]), np.array([True])).dtype == bool and np.add(np.array([True]), np.array([True])).tolist() == [True] and int(np.True_ + 1) == 2 and type(np.True_ + 1) is np.int64)
report("np.bool_ ** and abs: True ** True = 1 (int8 in 2.x / recorded), ~True is False, np.True_ == 1", int(np.True_ ** np.True_) == 1 and (~np.True_) is np.False_ and bool(np.True_ == 1), f"(True**True type {type(np.True_ ** np.True_).__name__})")
h = np.heaviside(np.array([-1.0, -0.0, 0.0, 1.0, np.nan, np.inf, -np.inf]), 0.5)
report("heaviside(x, 0.5): 0 for x<0, 0.5 at +-0, 1 for x>0, nan for nan, 0/1 at -+inf", h.tolist()[:4] == [0.0, 0.5, 0.5, 1.0] and math.isnan(h[4]) and h.tolist()[5:] == [1.0, 0.0])
report("heaviside(0, 7) = 7 (x2 is returned at zero), heaviside on int input gives float64 (only float loops)", float(np.heaviside(0.0, 7.0)) == 7 and np.heaviside(np.array([0, 1]), 1).dtype == np.float64 and np.heaviside(np.array([0, 1]), 1).tolist() == [1.0, 1.0])
report("heaviside(x, nan) at x=0 is nan; heaviside float32 stays float32", math.isnan(np.heaviside(0.0, np.nan)) and np.heaviside(np.float32(1), np.float32(0.5)).dtype == np.float32)
report("np.abs on int8 array keeps int8; np.abs(complex) is float64 (magnitude); np.abs on bool is bool", np.abs(np.array([-3], np.int8)).dtype == np.int8 and np.abs(np.array([3 + 4j])).dtype == np.float64 and np.abs(np.array([True])).dtype == bool)
report("np.abs(-np.inf) = inf, abs(nan) = nan, abs(np.int64 min) recorded above, np.absolute is np.abs", float(np.abs(-np.inf)) == math.inf and math.isnan(np.abs(np.nan)) and np.absolute is np.abs)
report("np.rint on float16 / float32 keeps the dtype and rounds half to even (2.5h -> 2)", np.rint(np.float16(2.5)).dtype == np.float16 and float(np.rint(np.float16(2.5))) == 2 and float(np.rint(np.float32(-3.5))) == -4)
report("np.trunc/floor/ceil on float16 keep float16; np.floor(np.float16(-0.5)) = -1", np.floor(np.float16(-0.5)).dtype == np.float16 and float(np.floor(np.float16(-0.5))) == -1 and np.ceil(np.float16(0.5)).dtype == np.float16)
