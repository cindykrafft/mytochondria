#!/usr/bin/env python
"""NumPy datetime64 / timedelta64, string routines (np.char legacy, np.strings 2.0+,
StringDType), text and binary I/O, printing, structured arrays and np.ma, each against
an independent truth (n5 covered numeric casting / promotion and finfo / iinfo).

datetime64 / timedelta64: unit inference from ISO strings (Y M D h m s ms us ns ps fs as),
the week unit (epoch Thursday 1970-01-01), day counts against a plain-Python proleptic
Gregorian days_from_civil and datetime.date.toordinal over years -9999..9999 and every year
1600-2400 against calendar.isleap, unit conversion (floor toward -inf for negative values),
the documented Y/M -> D 'unsafe' average-year conversion, resolution promotion, month
arithmetic, NaT semantics (comparisons, sorting, propagation), datetime_as_string (unit,
'UTC', 'local' under a fixed POSIX TZ, zoneinfo tzinfo, casting), is_busday / busday_count /
busday_offset with every roll mode, weekmask spellings and holidays against a plain-Python
business-day calendar, busdaycalendar, datetime_data, timedelta true/floor division, remainder,
divmod against Python int arithmetic, .item() conversion table at Python's range limits, and
overflow of the fine units and of large years.

Strings: np.char.* and np.strings.* against the Python str / bytes methods on ASCII,
non-ASCII (titlecase digraphs, sharp s, ligatures, Arabic-Indic digits, vulgar fractions,
unicode whitespace) and bytes; fixed-width storage rules (trailing NULs dropped, trailing
spaces kept, chararray / char.equal rstrip), StringDType and na_object semantics.

I/O: savetxt / loadtxt / genfromtxt round trips and options, %.18e exactness, .npy header
format (parsed by hand), save / load every dtype, allow_pickle, Fortran order, savez /
savez_compressed / NpzFile against zipfile, tofile / fromfile / frombuffer / fromstring,
array2string / set_printoptions / legacy modes, shortest repr round trip, float32 shortest
strings, format_float_positional / scientific against decimal.Decimal.

Structured arrays: fields, nested dtypes, align=True layout against ctypes.Structure,
recfunctions, recarray, dtype equality. np.ma: reductions against plain Python on the unmasked
data, mask propagation, domain masking, fill values, masked_* constructors, cov / corrcoef,
median, sort, argmax, concatenate / stack, count, mask sharing / hard masks, polyfit, unique.
No scipy anywhere."""
import os, time
os.environ["TZ"] = "IST-5:30"          # fixed UTC+05:30, no DST, parsed by glibc without tzdata
time.tzset()
import sys, math, warnings, itertools, random, io, tempfile, struct, calendar, decimal, zipfile, ast, ctypes
import datetime as dt
from fractions import Fraction as F
from decimal import Decimal as D
import numpy as np
import mpmath
NPV = tuple(int(v) for v in np.__version__.split(".")[:2]); NP2 = NPV >= (2, 0)
print(f"numpy {np.__version__}  python {sys.version.split()[0]}  mpmath {mpmath.__version__}  TZ={os.environ['TZ']}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-12, abs_=1e-300):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    if math.isinf(a) or math.isinf(b): return a == b
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
warnings.filterwarnings("ignore")
class caught:
    def __enter__(self):
        self._cm = warnings.catch_warnings(record=True); self.w = self._cm.__enter__(); warnings.simplefilter("always"); return self
    def __exit__(self, *a): self._cm.__exit__(*a)
    @property
    def names(self): return sorted({x.category.__name__ for x in self.w})
def raises(fn, exc=Exception):
    try: fn()
    except exc as e: return type(e).__name__
    except Exception as e: return None
    return None
rng = random.Random(20260925)
decimal.getcontext().prec = 2000; decimal.getcontext().Emin = -999999; decimal.getcontext().Emax = 999999

# ------------------------------------------------------------------ datetime helpers (plain Python truths)
def days_from_civil(y, m, d):
    """Days since 1970-01-01 in the proleptic Gregorian calendar (astronomical years), H. Hinnant's algorithm."""
    y -= m <= 2
    era = y // 400; yoe = y - era * 400
    doy = (153 * (m + (-3 if m > 2 else 9)) + 2) // 5 + d - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe - 719468
def civil_from_days(z):
    z += 719468; era = z // 146097; doe = z - era * 146097
    yoe = (doe - doe // 1460 + doe // 36524 - doe // 146096) // 365
    y = yoe + era * 400; doy = doe - (365 * yoe + yoe // 4 - yoe // 100); mp_ = (5 * doy + 2) // 153
    d = doy - (153 * mp_ + 2) // 5 + 1; m = mp_ + (3 if mp_ < 10 else -9)
    return y + (m <= 2), m, d
def isleap(y): return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
EPOCH_ORD = dt.date(1970, 1, 1).toordinal()
PER_SEC = {"s": 1, "ms": 10**3, "us": 10**6, "ns": 10**9, "ps": 10**12, "fs": 10**15, "as": 10**18}
def i64(x): return int(np.asarray(x).view(np.int64))
NAT = -2**63

print("---- datetime64: unit inference and values in every unit")
cases = [("2020", "Y"), ("2020-03", "M"), ("2020-03-04", "D"), ("2020-03-04T05", "h"), ("2020-03-04T05:06", "m"),
         ("2020-03-04T05:06:07", "s"), ("2020-03-04T05:06:07.1", "ms"), ("2020-03-04T05:06:07.123", "ms"),
         ("2020-03-04T05:06:07.1234", "us"), ("2020-03-04T05:06:07.123456", "us"), ("2020-03-04T05:06:07.1234567", "ns"),
         ("2020-03-04T05:06:07.123456789", "ns"), ("1969-07-20T20:17:40.5", "ms")]
ok_inf = True
for s, u in cases:
    v = np.datetime64(s); unit = np.datetime_data(v.dtype)[0]
    if unit != u: ok_inf = False; print(f"   {s!r}: inferred {unit}, expected {u}")
report("datetime64(str): unit 'automatically selected from the form of the string' (Y, M, D, h, m, s; 1-3 fraction digits ms, 4-6 us, 7-9 ns)", ok_inf)
def truth_value(y, mo, d, h, mi, s, frac, unit):
    """Integer count of `unit` since the epoch, floor toward -inf (the stored value), frac a Fraction of a second."""
    days = days_from_civil(y, mo, d)
    if unit == "Y": return y - 1970
    if unit == "M": return (y - 1970) * 12 + mo - 1
    if unit == "W": return days // 7
    if unit == "D": return days
    secs = F(days * 86400 + h * 3600 + mi * 60 + s) + frac
    if unit == "h": return math.floor(secs / 3600)
    if unit == "m": return math.floor(secs / 60)
    return math.floor(secs * PER_SEC[unit])
stamps = [(2020, 3, 4, 5, 6, 7, F(123456789, 10**9)), (1969, 7, 20, 20, 17, 40, F(5, 10)), (1600, 2, 29, 23, 59, 59, F(999999, 10**6)),
          (1, 1, 1, 0, 0, 0, F(0)), (9999, 12, 31, 23, 59, 59, F(0)), (1969, 12, 31, 23, 59, 59, F(999, 1000)), (1970, 1, 1, 0, 0, 0, F(1, 10**6))]
bad = []
for (y, mo, d, h, mi, s, fr) in stamps:
    fs = f"{y:04d}-{mo:02d}-{d:02d}T{h:02d}:{mi:02d}:{s:02d}"
    for unit in ["Y", "M", "W", "D", "h", "m", "s", "ms", "us"]:
        base = np.datetime64(fs + (".%09d" % (fr * 10**9) if fr else ""), "ns") if 1678 < y < 2262 else np.datetime64(fs + (".%06d" % (fr * 10**6) if fr else ""), "us")
        got = i64(base.astype(f"M8[{unit}]")); exp = truth_value(y, mo, d, h, mi, s, fr if 1678 < y < 2262 else F(math.floor(fr * 10**6), 10**6), unit)
        if got != exp: bad.append((fs, unit, got, exp))
    got_d = i64(np.datetime64(fs[:10], "D"))
    if 1 <= y <= 9999 and got_d != dt.date(y, mo, d).toordinal() - EPOCH_ORD: bad.append((fs, "D-ordinal", got_d))
print(f"   {len(stamps)} timestamps x 9 units, mismatches: {bad[:4]}")
report("astype to Y/M/W/D/h/m/s/ms/us gives floor((t - 1970-01-01)/unit) (truncation toward -inf before the epoch)", not bad)
w = np.datetime64("2020-01-02", "W")
print(f"   datetime64('2020-01-02','W') = {w} (int {i64(w)}); days {days_from_civil(2020, 1, 2)} // 7 = {days_from_civil(2020, 1, 2) // 7}; 1970-01-01 is a {calendar.day_name[dt.date(1970, 1, 1).weekday()]}")
report("week unit: value = days // 7 since 1970-01-01, so weeks start on Thursday (2020-01-02 is a Thursday -> itself)", i64(w) == days_from_civil(2020, 1, 2) // 7 and str(w) == "2020-01-02"
       and str(np.datetime64("2020-01-01", "W")) == "2019-12-26" and str(np.datetime64("1969-12-31").astype("M8[W]")) == "1969-12-25")
report("datetime64('2020-03-04T05:06', 'D') truncates to the day; ('2020-03-04', 'Y') to the year", str(np.datetime64("2020-03-04T05:06", "D")) == "2020-03-04" and str(np.datetime64("2020-03-04", "Y")) == "2020")
report("documented examples: datetime64(1,'Y') == '1971'; datetime64('2005-02','D') == '2005-02-01'; '2005' == '2005-01-01'; '2010-03-14T15' == '2010-03-14T15:00:00.00'",
       str(np.datetime64(1, "Y")) == "1971" and str(np.datetime64("2005-02", "D")) == "2005-02-01" and bool(np.datetime64("2005") == np.datetime64("2005-01-01"))
       and bool(np.datetime64("2010-03-14T15") == np.datetime64("2010-03-14T15:00:00.00")))
arrg = np.array(["2001-01-01T12:00", "2002-02-03T13:56:03.172"], dtype=np.datetime64)
report("generic-unit array from strings picks the finest unit present ('datetime64[ms]' in the documented example)", np.datetime_data(arrg.dtype)[0] == "ms"
       and i64(arrg[1]) == truth_value(2002, 2, 3, 13, 56, 3, F(172, 1000), "ms"))
report("'NAT' in any case parses to NaT; 'now'/'today' give s / D units", all(np.isnat(np.datetime64(s_, "D")) for s_ in ["NaT", "nat", "nAt", "NAT"]) and np.datetime_data(np.datetime64("now").dtype)[0] == "s"
       and np.datetime_data(np.datetime64("today").dtype)[0] == "D")
report("invalid dates raise ValueError: month 13, Feb 30, 1900-02-29, leap second 23:59:60 (documented shortcoming)",
       all(raises(lambda s_=s_: np.datetime64(s_), ValueError) for s_ in ["2020-13-01", "2020-02-30", "1900-02-29", "2016-12-31 23:59:60.450"]))
# fine units: 10+ fraction digits select ps/fs/as whose span is a few days / hours around 1970
fine = {}
for s_, frac_digits in [("2020-03-04T05:06:07.1234567890", 10), ("1970-01-01T00:00:01.1234567890", 10), ("2020-03-04T05:06:07.1234567890123", 13), ("2020-03-04T05:06:07.1234567890123456", 16)]:
    try:
        v = np.datetime64(s_); unit = np.datetime_data(v.dtype)[0]
        exp = truth_value(int(s_[:4]), int(s_[5:7]), int(s_[8:10]), int(s_[11:13]), int(s_[14:16]), int(s_[17:19]), F(int(s_[20:]), 10**frac_digits), unit)
        fine[s_] = (unit, i64(v), exp, str(v))
    except Exception as e:
        fine[s_] = ("EXC", type(e).__name__, None, str(e)[:60])
for k_, v_ in fine.items(): print(f"   datetime64({k_!r}) -> unit {v_[0]}, stored {v_[1]}, exact count {v_[2]}, prints {v_[3]!r}")
report("10 fraction digits -> 'ps' unit; a 1970-01-01 timestamp in ps is stored exactly", fine["1970-01-01T00:00:01.1234567890"][0] == "ps" and fine["1970-01-01T00:00:01.1234567890"][1] == fine["1970-01-01T00:00:01.1234567890"][2])
okfine = all(v_[0] == "EXC" or (v_[1] == v_[2] and -2**63 < v_[2] < 2**63) for v_ in fine.values())
report("a 2020 timestamp written with >= 10 fraction digits (ps/fs/as, documented span [1969, 1970]) is stored exactly or raises, never a silently different date", okfine)
ov = []
for s_, u in [("2263-01-01", "ns"), ("1677-01-01", "ns"), ("1971-01-01", "ps")]:
    try:
        v = np.datetime64(s_, u); exp = truth_value(int(s_[:4]), int(s_[5:7]), int(s_[8:10]), 0, 0, 0, F(0), u)
        ov.append((s_, u, str(v), i64(v) == exp))
    except Exception as e: ov.append((s_, u, "EXC " + type(e).__name__, True))
    try:
        v2 = np.datetime64(s_).astype(f"M8[{u}]"); ov.append((s_ + " astype", u, str(v2), i64(v2) == truth_value(int(s_[:4]), int(s_[5:7]), int(s_[8:10]), 0, 0, 0, F(0), u)))
    except Exception as e: ov.append((s_ + " astype", u, "EXC " + type(e).__name__, True))
for o in ov: print(f"   {o[0]} [{o[1]}] -> {o[2]}  (exact: {o[3]})")
report("dates outside the documented ns span [1678, 2262] (and ps span) are rejected or exact, not wrapped (constructor and astype)", all(o[3] for o in ov))
smax = np.datetime64("292277026596-12-04T15:30:07", "s"); sover = np.datetime64("292277026596-12-04T15:30:08", "s")
print(f"   max 's' datetime {smax} (int {i64(smax)} = 2**63-1: {i64(smax) == 2**63 - 1}); one second later -> {sover}")
report("'292277026596-12-04T15:30:07' is the largest 's' datetime (2**63-1 s after the epoch, exact)", i64(smax) == 2**63 - 1)
report("one second past the 's' range raises instead of silently becoming NaT (2**63 wraps to the NaT sentinel -2**63)", not np.isnat(sover), f"(got {sover!r})")
ybad = []
for v in [10**18, 2**63 - 1 - 1970, 2**63 - 1]:
    s_ = str(np.datetime64(v, "Y")); ybad.append((v, s_, str(1970 + v)))
for yv in ybad: print(f"   datetime64({yv[0]}, 'Y') prints {yv[1]!r}; year 1970+v = {yv[2]}")
report("datetime64(v, 'Y') prints the year 1970 + v for v up to 2**63-1-1970", ybad[0][1] == ybad[0][2] and ybad[1][1] == ybad[1][2])
report("datetime64(2**63-1, 'Y') (year 1970+2**63-1 > int64 max, inside the documented 'Y' span of +-9.2e18 years) prints its year", ybad[2][1] == ybad[2][2])

print("---- datetime64: calendar against Python (leap years 1600-2400, ordinals, negative years)")
badleap = []
for y in range(1600, 2401):
    n = i64(np.datetime64(f"{y + 1}-01-01") - np.datetime64(f"{y}-01-01"))
    feb29 = raises(lambda: np.datetime64(f"{y}-02-29"), ValueError) is None
    if n != 365 + calendar.isleap(y) or feb29 != calendar.isleap(y): badleap.append(y)
report("years 1600..2400: days in year = 365 + calendar.isleap(y) and 'YYYY-02-29' parses iff leap", not badleap, str(badleap[:5]))
dates = [dt.date(rng.randint(1, 9999), rng.randint(1, 12), 1) + dt.timedelta(days=rng.randint(0, 27)) for _ in range(3000)]
arr = np.array([d_.isoformat() for d_ in dates], dtype="M8[D]")
report("3000 random dates in 1..9999: int value == date.toordinal() - 719163 and str == isoformat",
       arr.astype(np.int64).tolist() == [d_.toordinal() - EPOCH_ORD for d_ in dates] and [str(x) for x in arr] == [d_.isoformat() for d_ in dates])
report("the same 3000 dates: .tolist() returns the datetime.date objects", arr.tolist() == dates)
negs = [(-1, 3, 1), (0, 2, 29), (-4, 2, 29), (-9999, 1, 1), (-100, 2, 28), (0, 1, 1), (10000, 1, 1), (123456, 7, 8)]
bn = []
for (y, m, d_) in negs:
    s_ = (f"-{-y:04d}" if y < 0 else f"{y:04d}") + f"-{m:02d}-{d_:02d}"
    v = i64(np.datetime64(s_)); rt = civil_from_days(v)
    if v != days_from_civil(y, m, d_) or rt != (y, m, d_): bn.append((s_, v, days_from_civil(y, m, d_)))
report("astronomical years (0 = 1 BC, leap; -4 leap; -100 not leap) and years > 9999: value == proleptic Gregorian days_from_civil",
       not bn and raises(lambda: np.datetime64("-0100-02-29"), ValueError) is not None and raises(lambda: np.datetime64("-0001-02-29"), ValueError) is not None, str(bn[:3]))
strs = [(s_, str(np.datetime64(s_))) for s_ in ["-0001-03-01", "-0004-02-29", "-0100-02-28", "-9999-01-01", "0000-01-01", "10000-01-01"]]
print("   str() of negative / large years: " + ", ".join(f"{a!r}->{b!r}" for a, b in strs))
report("str() of a datetime64 with a negative year keeps 4 year digits after the sign (ISO 8601 expanded form, like the input '-0001')", all(a == b for a, b in strs))
rt_ok = all(i64(np.datetime64(b)) == i64(np.datetime64(a)) for a, b in strs)
report("str() output of negative years parses back to the same date (round trip)", rt_ok)
a0 = np.datetime64("0000-01-01", "us"); b0 = np.datetime64("1600-01-01", "us")
report("documented: 1600-01-01 - 0000-01-01 = 50491123200000000 us (584388 days x 86400 s)", i64(b0 - a0) == 50491123200000000 == (days_from_civil(1600, 1, 1) - days_from_civil(0, 1, 1)) * 86400 * 10**6)
report("documented: (2021-01-01 12:56:23.423 - 2001-01-01)/1 s = 631198583.423 (no leap seconds)",
       float((np.datetime64("2021-01-01 12:56:23.423") - np.datetime64("2001-01-01")) / np.timedelta64(1, "s")) == 631198583.423)

print("---- datetime64: arithmetic, resolution promotion, Y/M units")
pairs = [("D", "h"), ("h", "m"), ("m", "s"), ("s", "ms"), ("ms", "us"), ("us", "ns"), ("W", "D"), ("Y", "M"), ("W", "h"), ("D", "s")]
okp = True
for u1, u2 in pairs:
    r = np.timedelta64(3, u1) + np.timedelta64(5, u2); ru = np.datetime_data(r.dtype)[0]
    fac = {"Y": 12, "M": 1}.get(u1) if u1 in "YM" else None
    if u1 in ("Y", "M"): exp = 3 * 12 + 5
    else:
        secs = {"W": 604800, "D": 86400, "h": 3600, "m": 60, "s": 1}
        tosec = lambda u: F(secs[u]) if u in secs else F(1, PER_SEC[u])
        exp = 3 * tosec(u1) / tosec(u2) + 5
    if ru != u2 or i64(r) != exp: okp = False; print(f"   {u1}+{u2}: {r}")
report("timedelta64 addition promotes to the finer unit and the value is exact (Y+M -> M, W+D -> D, D+s -> s, ...)", okp)
r1 = np.datetime64("2020-03-01") - np.datetime64("2020-02-28T12:00:00")
report("datetime64[D] - datetime64[s] -> timedelta64[s], exact (2020 leap: 1.5 days = 129600 s)", np.datetime_data(r1.dtype)[0] == "s" and i64(r1) == 129600)
r2 = np.datetime64("2009") + np.timedelta64(20, "D")
report("documented: datetime64('2009') + 20 D = '2009-01-21' (result in D)", str(r2) == "2009-01-21" and np.datetime_data(r2.dtype)[0] == "D")
report("documented: 1 W / 1 D = 7.0 and 1 W % 10 D = 7 D", float(np.timedelta64(1, "W") / np.timedelta64(1, "D")) == 7.0 and np.timedelta64(1, "W") % np.timedelta64(10, "D") == np.timedelta64(7, "D"))
report("promote_types: m8[Y]+m8[M] -> m8[M]; M8[D]+M8[W] -> M8[D]; m8[7D]+m8[3D] -> m8[D] (gcd of multiples)",
       np.promote_types("m8[Y]", "m8[M]") == np.dtype("m8[M]") and np.promote_types("M8[D]", "M8[W]") == np.dtype("M8[D]") and np.promote_types("m8[7D]", "m8[3D]") == np.dtype("m8[D]"))
report("Y/M are nonlinear: m8[Y] + m8[D] and m8[M] + m8[D] raise TypeError (no common divisor)",
       raises(lambda: np.timedelta64(1, "Y") + np.timedelta64(1, "D"), TypeError) and raises(lambda: np.timedelta64(1, "M") + np.timedelta64(1, "D"), TypeError))
report("documented: np.timedelta64(timedelta64(1,'Y'), 'D') raises TypeError 'same_kind'; timedelta64(1Y, 'M') = 12 M",
       raises(lambda: np.timedelta64(np.timedelta64(1, "Y"), "D"), TypeError) and np.timedelta64(np.timedelta64(1, "Y"), "M") == np.timedelta64(12, "M"))
yd = {n_: i64(np.timedelta64(n_, "Y").astype("m8[D]")) for n_ in [1, -1, 4, 100, 400, 7]}
md = {n_: i64(np.timedelta64(n_, "M").astype("m8[D]")) for n_ in [1, -1, 12, 4800, 5]}
exy = {n_: math.floor(F(n_ * 146097, 400)) for n_ in yd}; exm = {n_: math.floor(F(n_ * 146097, 4800)) for n_ in md}
print(f"   astype('m8[D]'): Y {yd}  truth floor(n*146097/400) {exy};  M {md}  truth floor(n*146097/4800) {exm}")
report("unsafe Y/M -> D uses 'averaged values from the 400 year leap-year cycle' (146097/400 and /4800 days), floored", yd == exy and md == exm)
report("month arithmetic: datetime64[D] + timedelta64[M] raises (no implicit M->D); M8[M] '2020-01' + 1 M = '2020-02'; Y + M -> M",
       raises(lambda: np.datetime64("2020-01-31") + np.timedelta64(1, "M"), TypeError) is not None
       and str(np.datetime64("2020-01-31").astype("M8[M]") + np.timedelta64(1, "M")) == "2020-02" and str(np.datetime64("2020", "Y") + np.timedelta64(1, "M")) == "2020-02")
mm_ok = True
for y in range(1990, 2031):
    for m in range(1, 13):
        for k in [1, 13, -1, -25]:
            r = np.datetime64(f"{y}-{m:02d}", "M") + np.timedelta64(k, "M")
            tot = y * 12 + m - 1 + k; exp = f"{tot // 12:04d}-{tot % 12 + 1:02d}"
            if str(r) != exp: mm_ok = False
report("M8[M] + k months for 1990..2030, k in {1, 13, -1, -25} equals (12y + m - 1 + k) divmod 12", mm_ok)
report("M8[M] -> M8[D] gives the 1st of the month; '2020-01-31' -> M -> +1 M -> D = '2020-02-01' (no end-of-month clipping)",
       str((np.datetime64("2020-01-31").astype("M8[M]") + np.timedelta64(1, "M")).astype("M8[D]")) == "2020-02-01")
cd = np.array([-1, -7, -8, 6, 7], "m8[D]").astype("m8[W]").astype(np.int64).tolist(); ch = np.array([-1, -3599, -3600, -3601, 3599], "m8[s]").astype("m8[h]").astype(np.int64).tolist()
print(f"   m8[D] [-1,-7,-8,6,7] -> W {cd};  m8[s] [-1,-3599,-3600,-3601,3599] -> h {ch}")
report("timedelta64 unit conversion floors toward -inf like datetime64 (-1 D -> -1 W, -3601 s -> -2 h)", cd == [x // 7 for x in [-1, -7, -8, 6, 7]] and ch == [x // 3600 for x in [-1, -3599, -3600, -3601, 3599]])

print("---- datetime64: NaT")
nat = np.datetime64("NaT", "D"); d1 = np.datetime64("2020-01-01")
report("NaT != NaT is True, NaT == NaT False, NaT < x and x < NaT False (datetime and timedelta)",
       bool(nat != nat) and not bool(nat == nat) and not bool(nat < d1) and not bool(d1 < nat) and not bool(nat >= d1)
       and bool(np.timedelta64("NaT", "s") != np.timedelta64("NaT", "s")) and not bool(np.timedelta64("NaT", "s") <= np.timedelta64(5, "s")))
report("documented: NaT - datetime = NaT timedelta; datetime + NaT timedelta = NaT", np.isnat(nat - d1) and np.isnat(d1 + np.timedelta64("nat", "D")))
sa = np.array(["2020-01-01", "NaT", "2019-01-01", "NaT", "1969-01-01"], "M8[D]")
report("np.sort puts NaT at the end (1.18 release note) and argsort agrees", [str(x) for x in np.sort(sa)] == ["1969-01-01", "2019-01-01", "2020-01-01", "NaT", "NaT"]
       and sa[np.argsort(sa, kind="stable")].astype(np.int64).tolist() == np.sort(sa).astype(np.int64).tolist())
report("min/max and np.maximum propagate NaT like NaN; np.isnat marks it", np.isnat(sa.min()) and np.isnat(sa.max()) and np.isnat(np.maximum(nat, d1))
       and np.isnat(sa).tolist() == [False, True, False, True, False])
report("timedelta: x / NaT = nan; NaT * 2 = NaT", math.isnan(float(np.timedelta64(7, "s") / np.timedelta64("NaT", "s"))) and np.isnat(np.timedelta64("NaT", "s") * 2))

print("---- datetime_as_string")
dd = np.arange("2002-10-27T04:30", 4 * 60, 60, dtype="M8[m]")
report("documented example: arange 4 steps of 60 m and timezone='UTC' appends 'Z'",
       np.datetime_as_string(dd, timezone="UTC").tolist() == ["2002-10-27T04:30Z", "2002-10-27T05:30Z", "2002-10-27T06:30Z", "2002-10-27T07:30Z"])
report("documented: unit='h' -> '2002-10-27T04'; unit='s' -> '...:00'; unit='h', casting='safe' raises TypeError",
       np.datetime_as_string(dd, unit="h").tolist()[0] == "2002-10-27T04" and np.datetime_as_string(dd, unit="s").tolist()[0] == "2002-10-27T04:30:00"
       and raises(lambda: np.datetime_as_string(dd, unit="h", casting="safe"), TypeError))
loc = np.datetime_as_string(dd, timezone="local").tolist()
exp_loc = [(dt.datetime(2002, 10, 27, 4, 30 + 60 * k - 60 * k, tzinfo=dt.timezone.utc) + dt.timedelta(hours=k)).astimezone(dt.timezone(dt.timedelta(hours=5, minutes=30))).strftime("%Y-%m-%dT%H:%M%z") for k in range(4)]
print(f"   timezone='local' (TZ=IST-5:30): {loc}; Python astimezone: {exp_loc}")
report("timezone='local': 'convert to the local timezone first, and suffix with a +-#### offset' (fixed +0530)", loc == exp_loc)
try:
    from zoneinfo import ZoneInfo
    try: zi = ZoneInfo("US/Eastern")
    except Exception: zi = ZoneInfo("America/New_York"); print("   (tzdata here has no 'US/Eastern' link; using the identical zone 'America/New_York')")
    ze = np.datetime_as_string(dd, timezone=zi).tolist()
    print(f"   ZoneInfo('US/Eastern'): {ze}")
    report("documented: tzinfo ZoneInfo('US/Eastern') crosses the DST boundary (-0400 -> -0500)", ze == ["2002-10-27T00:30-0400", "2002-10-27T01:30-0400", "2002-10-27T01:30-0500", "2002-10-27T02:30-0500"])
except Exception as e:
    print(f"   ZoneInfo path raised {type(e).__name__}: {str(e)[:120]}")
    report("documented: tzinfo ZoneInfo('US/Eastern') crosses the DST boundary (-0400 -> -0500)", False, f"raised {type(e).__name__}")
neg = np.array(["1969-12-31T23:59:59", "1969-12-31T00:00:01", "1970-01-01T00:00:00"], "M8[s]")
report("datetime_as_string(unit='D') of pre-epoch instants floors to the calendar day", np.datetime_as_string(neg, unit="D").tolist() == ["1969-12-31", "1969-12-31", "1970-01-01"])
fr = np.array(["2020-01-01T00:00:00.5", "1969-12-31T23:59:59.25"], "M8[ms]")
report("datetime_as_string default unit shows the stored precision; 'auto' drops trailing zero groups",
       np.datetime_as_string(fr).tolist() == ["2020-01-01T00:00:00.500", "1969-12-31T23:59:59.250"] and np.datetime_as_string(np.datetime64("2020-01-01T00:00:00.000"), unit="auto") == "2020-01-01")
report("datetime_as_string(NaT) == 'NaT'", np.datetime_as_string(np.datetime64("NaT", "s")) == "NaT")
with caught() as c:
    tzp = np.datetime64("2020-01-01T00:00+0100")
print(f"   parsing '2020-01-01T00:00+0100' -> {tzp}, warnings {c.names}")
report("timezone offsets in strings are still converted to UTC (deprecated since 1.11: warns)", str(tzp) == "2019-12-31T23:00" and bool(c.names))
exp_w = "UserWarning" if NP2 else "DeprecationWarning"
report(f"... the warning is a {exp_w} (DeprecationWarning before 2.0; 2.0 release note gh-24193: 'now issues a UserWarning')", exp_w in c.names, f"(got {c.names})")
print("   note: arrays.datetime.rst still says 'deprecated:: 1.11.0 ... will raise an error in the future'")

print("---- business days against a plain-Python calendar")
WD = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
def weekday(days): return (days + 3) % 7  # 1970-01-01 is Thursday (3)
def valid(days, wm, hol): return wm[weekday(days)] and days not in hol
def py_roll(days, roll, wm, hol):
    if valid(days, wm, hol): return days
    if roll == "raise": raise ValueError
    if roll == "nat": return None
    fwd = days
    while not valid(fwd, wm, hol): fwd += 1
    bwd = days
    while not valid(bwd, wm, hol): bwd -= 1
    month = lambda x: civil_from_days(x)[:2]
    if roll in ("forward", "following"): return fwd
    if roll in ("backward", "preceding"): return bwd
    if roll == "modifiedfollowing": return fwd if month(fwd) == month(days) else bwd
    if roll == "modifiedpreceding": return bwd if month(bwd) == month(days) else fwd
def py_offset(days, n, roll, wm, hol):
    x = py_roll(days, roll, wm, hol)
    if x is None: return None
    step = 1 if n > 0 else -1
    for _ in range(abs(n)):
        x += step
        while not valid(x, wm, hol): x += step
    return x
def py_count(b, e, wm, hol):
    if e >= b: return sum(valid(x, wm, hol) for x in range(b, e))
    return -sum(valid(x, wm, hol) for x in range(e + 1, b + 1))   # 'not including the day of enddates': (end, begin]
masks = ["1111100", "1111110", "0000011", "1010101", "0000100", "1111111"]
base = days_from_civil(2011, 1, 1)
okb = {"is_busday": True, "count": True, "offset": True}
bad_off = []
for wm in masks:
    wml = [c_ == "1" for c_ in wm]
    hol_days = sorted({base + rng.randint(0, 400) for _ in range(25)})
    hol = np.array(hol_days, dtype="M8[D]")
    holset = set(hol_days)
    ds = np.array([base + rng.randint(-30, 430) for _ in range(300)], dtype="M8[D]")
    dsi = ds.astype(np.int64).tolist()
    if np.is_busday(ds, weekmask=wm, holidays=hol).tolist() != [valid(x, wml, holset) for x in dsi]: okb["is_busday"] = False
    es = np.array([x + rng.randint(-60, 60) for x in dsi], dtype="M8[D]")
    if np.busday_count(ds, es, weekmask=wm, holidays=hol).tolist() != [py_count(b, e, wml, holset) for b, e in zip(dsi, es.astype(np.int64).tolist())]: okb["count"] = False
    for roll in ["nat", "forward", "following", "backward", "preceding", "modifiedfollowing", "modifiedpreceding"]:
        offs = [rng.randint(-40, 40) for _ in dsi]
        got = np.busday_offset(ds, offs, roll=roll, weekmask=wm, holidays=hol)
        exp = [py_offset(x, n, roll, wml, holset) for x, n in zip(dsi, offs)]
        gl = [None if np.isnat(g) else i64(g) for g in got]
        if gl != exp:
            okb["offset"] = False; bad_off.append((wm, roll, [(civil_from_days(x), n, g, e) for x, n, g, e in zip(dsi, offs, gl, exp) if g != e][:2]))
report("is_busday == plain-Python (weekday valid in weekmask and not a holiday) for 6 weekmasks x 300 dates with 25 random holidays", okb["is_busday"])
report("busday_count == valid days in [begin, end); when end < begin, minus the valid days in (end, begin] ('not including the day of enddates'), 6 weekmasks x 300 pairs", okb["count"])
report("busday_offset: roll first (nat / forward / following / backward / preceding / modifiedfollowing / modifiedpreceding), then count offset valid days", okb["offset"], str(bad_off[:2]))
report("busday_offset(roll='raise') on a weekend raises ValueError (documented 'Non-business day date')", raises(lambda: np.busday_offset("2011-06-25", 2), ValueError))
report("documented examples: '2011-10' 0 fwd -> 2011-10-03; '2012-03' -1 fwd -> 2012-02-29; 3rd Wed Jan 2011 -> 2011-01-19; Mother's day 2012 -> 2012-05-13",
       str(np.busday_offset("2011-10", 0, roll="forward")) == "2011-10-03" and str(np.busday_offset("2012-03", -1, roll="forward")) == "2012-02-29"
       and str(np.busday_offset("2011-01", 2, roll="forward", weekmask="Wed")) == "2011-01-19" and str(np.busday_offset("2012-05", 1, roll="forward", weekmask="Sun")) == "2012-05-13")
report("documented: busday_count('2011','2012') = 260, weekmask='Sat' -> 53; 2011-07-11..18 = 5 and reversed = -5",
       int(np.busday_count("2011", "2012")) == 260 and int(np.busday_count("2011", "2012", weekmask="Sat")) == 53
       and int(np.busday_count("2011-07-11", "2011-07-18")) == 5 and int(np.busday_count("2011-07-18", "2011-07-11")) == -5)
wms = ["1111100", [1, 1, 1, 1, 1, 0, 0], [True] * 5 + [False] * 2, "Mon Tue Wed Thu Fri", "MonTue Wed  Thu\tFri"]
week = np.arange("2011-07-11", "2011-07-25", dtype="M8[D]")
report("weekmask spellings '1111100', [1,1,1,1,1,0,0], bools, 'Mon Tue Wed Thu Fri', 'MonTue Wed  Thu\\tFri' agree",
       len({tuple(np.is_busday(week, weekmask=w_).tolist()) for w_ in wms}) == 1)
report("weekmask abbreviations are case-sensitive ('mon' raises ValueError); a length-6 weekmask raises",
       raises(lambda: np.is_busday(week, weekmask="mon Tue"), ValueError) is not None and raises(lambda: np.is_busday(week, weekmask="111110"), ValueError) is not None)
report("holidays: any order, NaT ignored (documented)", np.busday_count("2011-07-01", "2011-08-01", holidays=["2011-07-04", "NaT", "2011-07-01"]) == np.busday_count("2011-07-01", "2011-08-01", holidays=["2011-07-01", "2011-07-04"]) == 19)
bc = np.busdaycalendar(weekmask="1111100", holidays=["2011-07-04", "2011-07-02", "2011-07-04", "NaT", "2011-07-01"])
print(f"   busdaycalendar normalised holidays: {bc.holidays.tolist()}  weekmask {bc.weekmask.tolist()}")
report("busdaycalendar: holidays normalised (sorted, unique, NaT and weekend dates dropped); busdaycal= equals weekmask/holidays", bc.holidays.astype(str).tolist() == ["2011-07-01", "2011-07-04"]
       and np.busday_count("2011-06-01", "2011-09-01", busdaycal=bc) == np.busday_count("2011-06-01", "2011-09-01", holidays=["2011-07-04", "2011-07-01"]))
report("busdaycal together with weekmask raises ValueError ('neither weekmask nor holidays may be provided')", raises(lambda: np.busday_count("2011-06-01", "2011-09-01", weekmask="1111100", busdaycal=bc), ValueError) is not None
       or raises(lambda: np.busday_count("2011-06-01", "2011-09-01", holidays=["2011-07-05"], busdaycal=bc), ValueError) is not None)
report("all-zero weekmask raises ValueError (no valid days)", raises(lambda: np.busday_offset("2011-06-01", 1, weekmask="0000000"), ValueError) is not None)
nb = (bool(np.is_busday(np.datetime64("NaT", "D"))), raises(lambda: np.busday_offset("NaT", 1)), raises(lambda: np.busday_count("NaT", "2020-01-01")))
print(f"   NaT inputs: is_busday -> {nb[0]}, busday_offset -> {nb[1]}, busday_count -> {nb[2]}  (undocumented)")

print("---- datetime_data, timedelta division / floor division / remainder")
report("datetime_data: M8[25s] -> ('s', 25); m8[D] -> ('D', 1); M8 -> ('generic', 1)",
       np.datetime_data(np.dtype("m8[25s]")) == ("s", 25) and np.datetime_data(np.dtype("m8[D]")) == ("D", 1) and np.datetime_data(np.dtype("M8")) == ("generic", 1))
m25 = np.array([1, 2], "m8[25s]") + np.array([1, 1], "m8[s]")
report("m8[25s] + m8[s] -> m8[s], values 26 and 51 s", np.datetime_data(m25.dtype) == ("s", 1) and m25.astype(np.int64).tolist() == [26, 51])
vals = [-7, -6, -1, 0, 1, 5, 7, 13, -13, 10**15 + 3, -(10**15 + 3)]; divs = [2, -2, 3, -3, 7, 1, -1, 10**6 + 1]
tdv = np.array(vals, "m8[us]")
okd = {"fdiv": True, "mod": True, "divmod": True, "true": True}
for dv in divs:
    q = (tdv // np.timedelta64(dv, "us")).tolist(); r = (tdv % np.timedelta64(dv, "us")).astype(np.int64).tolist()
    tq = (tdv / np.timedelta64(dv, "us")).tolist(); dq, drm = np.divmod(tdv, np.timedelta64(dv, "us"))
    if q != [v // dv for v in vals]: okd["fdiv"] = False
    if r != [v % dv for v in vals]: okd["mod"] = False
    if dq.tolist() != q or drm.astype(np.int64).tolist() != r: okd["divmod"] = False
    if tq != [float(F(v, dv)) for v in vals]: okd["true"] = False
report("timedelta // timedelta == Python int floor division (negative operands floor toward -inf)", okd["fdiv"])
report("timedelta % timedelta == Python int % (result has the sign of the divisor)", okd["mod"])
report("divmod(timedelta, timedelta) == (//, %)", okd["divmod"])
report("timedelta / timedelta == correctly rounded float of the exact ratio", okd["true"])
qi = {dv: (tdv // dv).astype(np.int64).tolist() for dv in [2, -2, 3, 7]}
bad_qi = {dv: [(v, g, v // dv) for v, g in zip(vals, qi[dv]) if g != v // dv][:3] for dv in qi}
print(f"   m8[us] // int examples (value, got, floor): {dict((k, v) for k, v in bad_qi.items() if v)}")
pyq = [(dt.timedelta(microseconds=v) // 2) // dt.timedelta(microseconds=1) for v in vals]
report("timedelta64 // int follows floor_divide ('largest integer smaller or equal', == Python timedelta // int)", all(not v for v in bad_qi.values()) and qi[2] == pyq)
sq = [i64(np.timedelta64(v, "us") // 2) for v in [-7, -1]]
print(f"   scalar np.timedelta64(-7,'us') // 2 = {sq[0]}, (-1) // 2 = {sq[1]}; Python -7 // 2 = {-7 // 2}")
tdiv = (tdv / 2).astype(np.int64).tolist()
print(f"   m8[us] / 2 -> {tdiv[:6]} (dtype {(tdv / 2).dtype}); Python timedelta / 2 (round-half-even us) -> {[(dt.timedelta(microseconds=v) / 2) // dt.timedelta(microseconds=1) for v in vals][:6]}")
with caught() as c:
    z1 = np.timedelta64(1, "s") // np.timedelta64(0, "s"); z2 = np.timedelta64(1, "s") % np.timedelta64(0, "s"); z3 = np.timedelta64(1, "s") / np.timedelta64(0, "s")
print(f"   division by a zero timedelta: // -> {z1}, % -> {z2}, / -> {z3}; warnings {c.names}")
report("division by zero timedelta: / -> inf, % -> NaT, // -> 0, with RuntimeWarning (no ZeroDivisionError, unlike Python)", math.isinf(float(z3)) and np.isnat(z2) and int(z1) == 0 and "RuntimeWarning" in c.names)

print("---- .item() / tolist() conversion table")
tbl = [(np.datetime64("NaT", "D"), type(None)), (np.timedelta64("NaT", "D"), type(None)), (np.timedelta64(123, "ns"), int), (np.datetime64("2020-01-01T00:00:00.123456789"), int),
       (np.datetime64("2025-01-01T12:00:00.123456"), dt.datetime), (np.datetime64("2020-01-01T05", "h"), dt.datetime), (np.timedelta64(10, "D"), dt.timedelta),
       (np.timedelta64(3, "h"), dt.timedelta), (np.datetime64("2020-01-02", "W"), dt.date), (np.datetime64("2020-06", "M"), dt.date), (np.datetime64("2020", "Y"), dt.date),
       (np.timedelta64(3, "Y"), int), (np.timedelta64(3, "M"), int), (np.timedelta64(1, "W"), dt.timedelta)]
badt = [(repr(v), type(v.item()).__name__, t_.__name__) for v, t_ in tbl if type(v.item()) is not t_]
report("item() follows the documented table (NaT->None; ns/ps/fs/as->int; us..h->datetime/timedelta; D/W->date/timedelta; Y/M->date/int)", not badt, str(badt))
report("item() values: 2025-01-01T12:00:00.123456 exact; 123 ns -> 123; 1 W -> timedelta(days=7); 2020-06 M -> date(2020,6,1)",
       np.datetime64("2025-01-01T12:00:00.123456").item() == dt.datetime(2025, 1, 1, 12, 0, 0, 123456) and np.timedelta64(123, "ns").item() == 123
       and np.timedelta64(1, "W").item() == dt.timedelta(days=7) and np.datetime64("2020-06", "M").item() == dt.date(2020, 6, 1))
lim = [(np.datetime64("0001-01-01T00:00:00.000000"), dt.datetime(1, 1, 1)), (np.datetime64("9999-12-31T23:59:59.999999"), dt.datetime(9999, 12, 31, 23, 59, 59, 999999)),
       (np.datetime64("0001-01-01"), dt.date(1, 1, 1)), (np.datetime64("9999-12-31"), dt.date(9999, 12, 31)),
       (np.timedelta64(999999999, "D"), dt.timedelta(days=999999999)), (np.timedelta64(-86399999999999999, "us"), dt.timedelta(days=-1000000, microseconds=1))]
report("item() at Python's limits: date(1,1,1), datetime max 9999-12-31T23:59:59.999999, timedelta(days=999999999) and -1e6 days + 1 us are exact", all(v.item() == e for v, e in lim))
outr = [(np.datetime64("10000-01-01"), days_from_civil(10000, 1, 1)), (np.datetime64("0000-12-31"), days_from_civil(0, 12, 31)), (np.timedelta64(10**9, "D"), 10**9),
        (np.datetime64("10000-01-01T00:00:00", "us"), days_from_civil(10000, 1, 1) * 86400 * 10**6)]
print("   out of Python's range: " + ", ".join(f"{v!r}.item() -> {v.item()!r}" for v, _ in outr))
report("outside Python's datetime range item() returns the raw int count of units (years 0 and 10000, 1e9 days)", all(type(v.item()) is int and v.item() == e for v, e in outr))

print("---- strings: np.char / np.strings against Python str and bytes methods")
USTR = ["hello world", "Hello World", "HELLO", "", " ", "abc123", "ǆungla", "ǅ", "Ǆ", "straße", "ﬁx", "ΣΑΣ σας", "they're bill's",
        "a\tb\tc", "  padded  ", "²³", "½", "٣٤", "　x　", "\x1c\x1dz", "x​y", "ŉ", "abcabcabc", "αβγ", "日本語", "\U0001F600smile",
        "xxaxx", "-42", "+7", "a,b,,c", "a b  c", "Title Case Words", "123", "1.5", "MiXeD cAsE", "\xa0nbsp\xa0", "ǈǉǊ", "İi"]
BSTR = [b"hello world", b"Hello World", b"HELLO", b"", b" ", b"abc123", b"abc\xe9", b"  padded  ", b"xxaxx", b"-42", b"a,b,,c", b"a b  c",
        b"Title Case Words", b"\xff\xfeAB", b"a\tb", b"123", b"\x1c\x1dz", b"MiXeD"]
UA = np.array(USTR, dtype="U60"); BA = np.array(BSTR, dtype="S40")
namespaces = [("np.char", np.char)] + ([("np.strings", np.strings)] if hasattr(np, "strings") else [])
def as_list(r):
    if isinstance(r, tuple): return [list(t) for t in zip(*[x.tolist() for x in r])]
    return r.tolist()
def pycall(s, fn, args):
    try:
        r = getattr(s, fn)(*args); return list(r) if isinstance(r, tuple) else r
    except Exception as e: return "EXC:" + type(e).__name__
def npcall(ns, fn, arr, args):
    try: return as_list(getattr(ns, fn)(arr, *args))
    except Exception as e: return "EXC:" + type(e).__name__
calls_u = [("upper", ()), ("lower", ()), ("capitalize", ()), ("title", ()), ("swapcase", ()),
           ("center", (25, "*")), ("center", (12, "é")), ("center", (0,)), ("ljust", (14, "-")), ("rjust", (14, "ü")), ("ljust", (3,)), ("rjust", (2, "x")), ("center", (3, "#")),
           ("zfill", (6,)), ("zfill", (1,)), ("strip", ()), ("lstrip", ()), ("rstrip", ()), ("strip", ("xa",)), ("lstrip", ("ǆ ",)), ("rstrip", ("s'",)),
           ("find", ("a",)), ("find", ("b", 2)), ("find", ("c", -3)), ("find", ("", 3)), ("find", ("", 50)), ("rfind", ("a",)), ("rfind", ("b", 0, 4)), ("rfind", ("", -2)),
           ("index", ("",)), ("rindex", ("", 0, 100)), ("count", ("a",)), ("count", ("", )), ("count", ("", 1, 3)), ("count", ("bc", 1, -1)), ("count", ("ab", -100, 100)),
           ("startswith", ("he",)), ("startswith", ("", 5)), ("startswith", ("l", 2, 3)), ("endswith", ("d",)), ("endswith", ("ld", 0, -1)), ("endswith", ("", 100)),
           ("replace", ("a", "XY")), ("replace", ("a", "", 1)), ("replace", ("", "-")), ("replace", ("ab", "é", 2)), ("replace", ("l", "LL", 0)), ("replace", ("", "_", 2)),
           ("split", ()), ("split", (",",)), ("split", (" ", 1)), ("rsplit", ()), ("rsplit", (",", 1)), ("rsplit", ("a", 1)),
           ("partition", (" ",)), ("partition", ("a",)), ("rpartition", (" ",)), ("rpartition", ("a",)),
           ("isalpha", ()), ("isdigit", ()), ("isnumeric", ()), ("isdecimal", ()), ("isspace", ()), ("istitle", ()), ("isupper", ()), ("islower", ()), ("isalnum", ()),
           ("expandtabs", ()), ("expandtabs", (3,)), ("splitlines", ())]
calls_b = [(fn, tuple(x.encode("latin-1") if isinstance(x, str) and fn not in () else x for x in args)) for fn, args in calls_u
           if fn not in ("isnumeric", "isdecimal") and all(not isinstance(x, str) or x.isascii() or x in ("é", "ü") for x in args)]
calls_b = [(fn, args) for fn, args in calls_b if not (fn in ("center", "ljust", "rjust") and len(args) > 1 and args[1] in (b"\xe9", b"\xfc"))]
calls_b = [(fn, args) for fn, args in calls_b if not (fn in ("lstrip",) and args and args[0] == "ǆ ".encode("utf-8"))]
for nsname, ns in namespaces:
    for kind, arr, pys, calls in [("unicode", UA, USTR, calls_u), ("bytes", BA, BSTR, calls_b)]:
        fails = []
        for fn, args in calls:
            if not hasattr(ns, fn): continue
            args = tuple(a.encode("utf-8") if (kind == "bytes" and isinstance(a, str)) else a for a in args)
            got = npcall(ns, fn, arr, args)
            exp = [pycall(s, fn, args) for s in pys]
            if isinstance(got, str) or got != exp:
                diffs = [(s, g, e) for s, g, e in zip(pys, got, exp) if g != e] if not isinstance(got, str) else [got]
                fails.append((fn, args, diffs[:2]))
        for f_ in fails: print(f"   {nsname} {kind}: {f_[0]}{f_[1]} differs: {f_[2]}")
        report(f"{nsname} on {kind} ({len(pys)} strings incl. titlecase digraphs, sharp s, ligature, unicode spaces/digits): {len(calls)} method calls equal Python's {'str' if kind == 'unicode' else 'bytes'} methods element-wise", not fails, f"({len(fails)} calls differ)")
# the same calls on the default (tight) itemsize np.array(strings) infers: output sizes must still be computed from the operation
UAn = np.array(USTR); BAn = np.array(BSTR)
print(f"   tight dtypes: {UAn.dtype} / {BAn.dtype}")
for nsname, ns in namespaces:
    for kind, arr, pys, calls in [("unicode", UAn, USTR, calls_u), ("bytes", BAn, BSTR, calls_b)]:
        fails = []
        for fn, args in calls:
            if not hasattr(ns, fn) or fn in ("upper", "swapcase", "title", "capitalize", "lower"): continue   # length-changing case maps: separate check below
            args = tuple(a.encode("utf-8") if (kind == "bytes" and isinstance(a, str)) else a for a in args)
            got = npcall(ns, fn, arr, args); exp = [pycall(s, fn, args) for s in pys]
            if isinstance(got, str) or got != exp:
                fails.append((fn, args, ([(s, g, e) for s, g, e in zip(pys, got, exp) if g != e] if not isinstance(got, str) else [got])[:2]))
        for f_ in fails: print(f"   {nsname} {kind} (tight dtype): {f_[0]}{f_[1]} differs: {f_[2]}")
        report(f"{nsname} on {kind} with the tight inferred itemsize ({arr.dtype}): the non-case-mapping calls still equal Python (output width computed from the operation)", not fails, f"({len(fails)} calls differ)")
for nsname, ns in namespaces:
    rp1 = ns.replace(np.array(["a", "ab"]), "abc", "x").tolist(); rp2 = ns.replace(np.array(["ab"]), "b", "xyzw").tolist(); rp3 = ns.replace(np.array([b"a"]), b"abc", b"x").tolist()
    print(f"   {nsname}.replace(['a','ab'], 'abc', 'x') -> {rp1}; replace(['ab'], 'b', 'xyzw') -> {rp2}; replace([b'a'], b'abc', b'x') -> {rp3}")
    report(f"{nsname}.replace with old / new longer than the array itemsize == str.replace (['a','ab'] unchanged; 'ab' -> 'axyzw')", rp1 == ["a", "ab"] and rp2 == ["axyzw"] and rp3 == [b"a"])
    pt1 = as_list(ns.partition(np.array(["ab"]), "abc")); pt2 = as_list(ns.rpartition(np.array(["ab"]), "abc"))
    print(f"   {nsname}.partition(['ab'], 'abc') -> {pt1}; rpartition -> {pt2}; Python {list('ab'.partition('abc'))} / {list('ab'.rpartition('abc'))}")
    report(f"{nsname}.partition / rpartition with a separator longer than the array itemsize == str.partition ('ab' has no 'abc')", pt1 == [["ab", "", ""]] and pt2 == [["", "", "ab"]])
# truncation when the case mapping lengthens the string
for nsname, ns in namespaces:
    t1 = ns.upper(np.array(["ß", "ﬁ", "ŉ"])).tolist(); t2 = ns.swapcase(np.array(["ß"])).tolist(); t3 = ns.title(np.array(["ﬁx"])).tolist()
    print(f"   {nsname}.upper(['ß','ﬁ','ŉ']) (dtype U1) -> {t1}  Python {[s.upper() for s in ['ß', 'ﬁ', 'ŉ']]}; swapcase('ß') -> {t2}; title('ﬁx') (U2) -> {t3} Python {'ﬁx'.title()!r}")
    report(f"{nsname}.upper / swapcase / title: 'Calls str.upper element-wise' also when the mapping lengthens the string (U1 input 'ß' -> 'SS')", t1 == ["SS", "FI", "ʼN"] and t2 == ["SS"] and t3 == ["Fix"])
for nsname, ns in namespaces:
    lj = ns.ljust(np.array(["abcdef"]), 2).tolist(); rj = ns.rjust(np.array(["abcdef"]), 3).tolist(); ce = ns.center(np.array(["abcdef"]), 4).tolist()
    print(f"   {nsname}.ljust('abcdef', 2) -> {lj}, rjust(.., 3) -> {rj}, center(.., 4) -> {ce}; Python returns 'abcdef' unchanged")
    report(f"{nsname}.ljust / rjust / center with width < len(s) return s unchanged (str.ljust semantics)", lj == rj == ce == ["abcdef"])
print("---- strings: fixed-width storage rules")
report("np.array(['a  ']) keeps trailing spaces (dtype U3, value 'a  ')", np.array(["a  "])[0] == "a  " and np.array(["a  "]).dtype == np.dtype("U3"))
report("trailing NULs are not part of the value: np.array(['a\\x00\\x00'])[0] == 'a' (dtype still U3), same for bytes", np.array(["a\x00\x00"])[0] == "a" and np.array(["a\x00\x00"]).dtype == np.dtype("U3")
       and np.array([b"a\x00"])[0] == b"a")
report("interior NULs are kept: str_len('a\\x00b') = 3, str_len('ab\\x00') = 2", np.char.str_len(np.array(["a\x00b", "ab\x00"])).tolist() == [3, 2])
report("np.char.strip('\\x00a\\x00') = '\\x00a' (the trailing NUL is already gone; NUL is not whitespace)", np.char.strip(np.array(["\x00a\x00"])).tolist() == ["\x00a"])
report("chararray: 'values automatically have whitespace removed from the end when indexed'", np.char.array(["a  ", "b\t"])[0] == "a" and np.char.array(["a  ", "b\t"])[1] == "b")
report("np.char.equal / not_equal: 'performed by first stripping whitespace characters from the end'; ndarray == does not strip",
       np.char.equal(np.array(["a"]), np.array(["a  "])).tolist() == [True] and np.char.not_equal(np.array(["a"]), np.array(["a  "])).tolist() == [False]
       and (np.array(["a"]) == np.array(["a  "])).tolist() == [False])
report("comparison of U arrays is by code point, like Python ('B' < 'a' < 'é' < '日'); 'ab' < 'abc'", (np.array(["B", "a", "é", "ab"]) < np.array(["a", "é", "日", "abc"])).tolist() == [True] * 4)
report("assigning a longer string to a U3 array truncates silently to 3 code points", (lambda x: (x.__setitem__(0, "abcdef"), x[0])[1])(np.array(["xyz"])) == "abc")
print("---- strings: str_len, add, multiply, encode/decode, mod, join, startswith tuple")
for nsname, ns in namespaces:
    report(f"{nsname}.str_len == len() for every test string (code points, astral plane counts 1)", ns.str_len(UA).tolist() == [len(s) for s in USTR] and ns.str_len(BA).tolist() == [len(s) for s in BSTR])
    report(f"{nsname}.add == + and multiply by 0, -1, 3 == Python s * n (negative -> '')", ns.add(UA, UA[::-1]).tolist() == [a + b for a, b in zip(USTR, USTR[::-1])]
           and all(ns.multiply(UA, n).tolist() == [s * n for s in USTR] for n in [0, -1, 3]))
    enc = ns.encode(UA, "utf-8"); report(f"{nsname}.encode('utf-8') == str.encode and decode round-trips", enc.tolist() == [s.encode("utf-8") for s in USTR] and ns.decode(enc, "utf-8").tolist() == USTR)
    report(f"{nsname}.encode('ascii') of non-ASCII raises UnicodeEncodeError; decode with errors='replace' matches Python", raises(lambda: ns.encode(np.array(["é"]), "ascii"), UnicodeEncodeError) is not None
           and ns.decode(np.array([b"\xff\xfeAB"]), "utf-8", "replace").tolist() == [b"\xff\xfeAB".decode("utf-8", "replace")])
    fm = ns.mod(np.array(["%d apples", "%.2f", "%5s|", "%x", "%r"]), np.array([3.9, 2.5, 7, 255, 1], dtype=object)).tolist()
    report(f"{nsname}.mod == Python %-formatting element-wise ('%d' of 3.9 -> '3', '%.2f', '%5s', '%x', '%r')", fm == [a % b for a, b in zip(["%d apples", "%.2f", "%5s|", "%x", "%r"], [3.9, 2.5, 7, 255, 1])])
report("np.char.join(sep, seq) == sep.join(seq) where seq is each string (joins the characters)", np.char.join(np.array(["-", ", ", "é"]), np.array(["abc", "xy", "日本"])).tolist() == ["a-b-c", "x, y", "日é本"])
sw = np.char.startswith(np.array(["abc"]), ("a", "x")).tolist()
print(f"   np.char.startswith(['abc'], ('a','x')) -> {sw} (Python 'abc'.startswith(('a','x')) -> True)")
report("startswith with a tuple of prefixes broadcasts it as an array of prefixes (documented 'prefix: array_like'), unlike str.startswith's any-of", sw == [True, False])
report("isnumeric / isdecimal on bytes raise TypeError ('only available for Unicode')", raises(lambda: np.char.isnumeric(np.array([b"1"])), TypeError) is not None and raises(lambda: np.char.isdecimal(np.array([b"1"])), TypeError) is not None)
report("np.char.index / rindex raise ValueError when the substring is absent (like str.index)", raises(lambda: np.char.index(np.array(["abc"]), "d"), ValueError) is not None and raises(lambda: np.char.rindex(np.array(["abc"]), "d"), ValueError) is not None)
report("np.char.translate with a mapping == str.translate", np.char.translate(np.array(["abcabc", "xyz"]), {97: "X", 98: None}).tolist() == ["XcXc", "xyz"])
if hasattr(np, "strings"):
    report("np.strings.slice(a, 1, 4) == s[1:4] and slice(a, None, None, -1) == s[::-1] (2.3+)" if hasattr(np.strings, "slice") else "np.strings.slice absent",
           (np.strings.slice(UA, 1, 4).tolist() == [s[1:4] for s in USTR] and np.strings.slice(UA, None, None, -1).tolist() == [s[::-1] for s in USTR]) if hasattr(np.strings, "slice") else True)

if NP2:
    print("---- StringDType (2.0+)")
    from numpy.dtypes import StringDType
    SA = np.array(USTR, dtype=StringDType())
    fails = []
    for fn, args in calls_u:
        ns_ = np.strings if hasattr(np.strings, fn) else np.char   # split / rsplit / splitlines live only in np.char
        nargs = tuple(np.array(a_, dtype=StringDType()) for a_ in args) if fn in ("partition", "rpartition") else args
        got = npcall(ns_, fn, SA, nargs); exp = [pycall(s, fn, args) for s in USTR]
        if isinstance(got, str) or got != exp: fails.append((fn, args, got if isinstance(got, str) else [(s, g, e) for s, g, e in zip(USTR, got, exp) if g != e][:2]))
    for f_ in fails: print(f"   StringDType: {f_[0]}{f_[1]} differs: {f_[2]}")
    report(f"np.strings on StringDType: the same {len(calls_u)} calls equal Python str methods (no width limit, so lengthening case maps are exact)", not fails)
    ps_ = raises(lambda: np.strings.partition(SA, " "))
    print(f"   np.strings.partition(StringDType array, ' ') -> {ps_ or 'ok'}; with sep as a StringDType array it works")
    report("np.strings.partition / rpartition accept a plain str separator for a StringDType array (sep: 'array-like, with StringDType, bytes_, or str_ dtype'; add/replace/find accept it)",
           ps_ is None and raises(lambda: np.strings.rpartition(SA, "a")) is None)
    report("StringDType keeps trailing NULs and trailing spaces (variable width, UTF-8)", np.array(["a\x00", "b  "], dtype=StringDType()).tolist() == ["a\x00", "b  "])
    sda = np.array(["hello", "world!!"], dtype=StringDType())
    try: inf_dt = sda.astype(np.str_).dtype
    except Exception as e: inf_dt = type(e).__name__
    print(f"   StringDType.astype(np.str_) -> {inf_dt} (the size-inferring cast is documented in the main-branch user guide; release notes do not list it before 2.5)")
    report("StringDType -> 'U4' truncates (documented 'An explicit size can still be passed, truncating entries')", sda.astype("U4").tolist() == ["hell", "worl"] and sda.astype("U7").tolist() == ["hello", "world!!"])
    report("StringDType(coerce=False) rejects non-strings with ValueError; default coerces 1 -> '1'", raises(lambda: np.array([1, "a"], dtype=StringDType(coerce=False)), ValueError) is not None
           and np.array([1, 3.4], dtype=StringDType()).tolist() == ["1", "3.4"])
    dn = StringDType(na_object=np.nan); an = np.array(["hello", np.nan, "world"], dtype=dn)
    ad = (an + an).tolist()
    report("na_object=nan: arr + arr -> ['hellohello', nan, 'worldworld'] (NaN-like propagates)", ad[0] == "hellohello" and ad[2] == "worldworld" and isinstance(ad[1], float) and math.isnan(ad[1]))
    so = np.sort(an).tolist()
    report("na_object=nan sorts to the end", so[:2] == ["hello", "world"] and math.isnan(so[2]))
    print(f"   na_object=nan: arr != 'hello' -> {(an != 'hello').tolist()}, arr != arr -> {(an != an).tolist()}, arr == arr -> {(an == an).tolist()}")
    report("na_object=nan comparisons: == and < False, != True ('arr != \"hello\"' -> [False, True, True]; main-branch docs, gh-32564)", (an != "hello").tolist() == [False, True, True] and (an == an).tolist() == [True, False, True]
           and (an < "zzz").tolist() == [True, False, True])
    enone = (np.array([None, ""], dtype=StringDType(na_object=None)) == "").tolist()
    print(f"   na_object=None: [None, ''] == '' -> {enone}")
    report("na_object=None: a missing entry is not equal to the empty string ([None, ''] == '' -> [False, True]; gh-32564 'distinguish None-like missing values from empty strings')", enone == [False, True])
    report("np.isnan marks nan-like missing entries", np.isnan(an).tolist() == [False, True, False])
    sl = raises(lambda: np.strings.str_len(an))
    print(f"   np.strings.str_len on a nan-like missing entry -> {sl or np.strings.str_len(an).tolist()}")
    dnn = StringDType(na_object=None); anone = np.array(["this array has", None, "as an entry"], dtype=dnn)
    report("na_object=None: arr[1] is None; np.sort raises ValueError ('Cannot compare null that is not a nan-like value')", anone[1] is None and raises(lambda: np.sort(anone), ValueError) is not None)
    ds_ = StringDType(na_object="__NA__"); ast_ = np.array(["x", "__NA__", "yy"], dtype=ds_)
    print(f"   string sentinel: {ast_.tolist()}  upper -> {np.strings.upper(ast_).tolist()}  str_len -> {np.strings.str_len(ast_).tolist()}")
    report("string sentinel: missing entries 'treated as if they have a value given by the string sentinel' (str_len = len('__NA__') = 6)", np.strings.str_len(ast_).tolist() == [1, 6, 2])
    report("np.empty(3, StringDType()) is three empty strings", np.empty(3, dtype=StringDType()).tolist() == ["", "", ""])
    report("StringDType -> 'S4' of a non-ASCII string raises UnicodeEncodeError (documented: non-ASCII characters 'are rejected')", raises(lambda: np.array(["é"], dtype=StringDType()).astype("S4"), UnicodeEncodeError) is not None)
    try:
        bad_cast = np.array([b"\xff", b"ok"]).astype(StringDType()); cast_res = "no error; str_len -> %s; tolist -> %s" % (np.strings.str_len(bad_cast).tolist(), raises(lambda: bad_cast.tolist()))
    except Exception as e: cast_res = "raised " + type(e).__name__
    print(f"   np.array([b'\\xff', b'ok']).astype(StringDType()): {cast_res}")
    report("'S' -> StringDType with invalid UTF-8 bytes: 'a UnicodeDecodeError is raised during the cast'", cast_res.startswith("raised UnicodeDecodeError"))
    report("StringDType -> V5 stores the UTF-8 bytes ('hello' -> b'hello')", np.array(["hello"], dtype=StringDType()).astype("V5")[0].tobytes() == b"hello")

print("---- text I/O: savetxt / loadtxt")
V123 = NPV >= (1, 23)
def bits(x): return struct.unpack("<Q", struct.pack("<d", float(x)))[0]
specials = [0.0, -0.0, 5e-324, 2.2250738585072014e-308, 2.225073858507201e-308, 1.7976931348623157e308, -1.7976931348623157e308, 0.1, 1 / 3, math.pi, 1e-300, 123456789.123456789, float("inf"), float("-inf"), float("nan")]
vals = specials + [struct.unpack("<d", struct.pack("<Q", rng.getrandbits(64)))[0] for _ in range(3000)]
vals = [v for v in vals if not math.isnan(v)] + [float("nan")]
X = np.array(vals).reshape(-1, 1)
buf = io.StringIO(); np.savetxt(buf, X); txt = buf.getvalue()
first = txt.splitlines()[0]
report("savetxt default fmt '%.18e' (first line == '%.18e' % 0.0), one row per line", first == "%.18e" % 0.0 and len(txt.splitlines()) == len(vals))
Y = np.loadtxt(io.StringIO(txt))
okbits = all((math.isnan(a) and math.isnan(b)) or bits(a) == bits(b) for a, b in zip(vals, Y.tolist()))
report(f"savetxt('%.18e') -> loadtxt round trip is bit-exact for {len(vals)} doubles (random bit patterns, subnormals, +-0, +-inf, nan, max)", okbits)
report("the written text equals Python's '%.18e' % x for every value (inf/nan spelled 'inf'/'nan')", txt.splitlines() == ["%.18e" % v for v in vals])
X32 = np.array([struct.unpack("<f", struct.pack("<I", rng.getrandbits(32)))[0] for _ in range(500)], dtype=np.float32)
X32 = X32[np.isfinite(X32)]
b32 = io.StringIO(); np.savetxt(b32, X32); Y32 = np.loadtxt(io.StringIO(b32.getvalue()), dtype=np.float32)
report("float32 via '%.18e' and loadtxt(dtype=float32) is bit-exact", Y32.tobytes() == X32.tobytes())
src = "# header comment\n1 2 3\n\n4\t5   6  # trailing comment\n  7 8 9\n"
report("loadtxt: default whitespace delimiter (tabs, runs of spaces, leading space), '#' comments and blank lines skipped",
       np.loadtxt(io.StringIO(src)).tolist() == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
report("loadtxt: comments=['#', '//'] (several markers) and comments=None", np.loadtxt(io.StringIO("1,2 // c\n# x\n3,4\n"), delimiter=",", comments=["#", "//"]).tolist() == [[1, 2], [3, 4]]
       and np.loadtxt(io.StringIO("1,2\n3,4\n"), delimiter=",", comments=None).tolist() == [[1, 2], [3, 4]])
report("loadtxt: skiprows 'including comments' (skiprows=2 skips a comment and the first data row)", np.loadtxt(io.StringIO("# c\n1 2\n3 4\n5 6\n"), skiprows=2).tolist() == [[3, 4], [5, 6]])
report("loadtxt: usecols=(0, -1) and usecols=1 (int -> 1-D)", np.loadtxt(io.StringIO("1 2 3\n4 5 6\n"), usecols=(0, -1)).tolist() == [[1, 3], [4, 6]]
       and np.loadtxt(io.StringIO("1 2 3\n4 5 6\n"), usecols=1).tolist() == [2, 5])
report("loadtxt: converters={0: fromhex-like} and unpack=True -> columns", [c.tolist() for c in np.loadtxt(io.StringIO("0x1p-1 2\n0x1.8p1 4\n"), converters={0: lambda s: float.fromhex(s if isinstance(s, str) else s.decode())}, unpack=True)] == [[0.5, 3.0], [2, 4]])
if V123:
    report("loadtxt (1.23+): converters may be a single callable applied to every column", np.loadtxt(io.StringIO("1,2\n3,4\n"), delimiter=",", converters=lambda s: float(s) * 10).tolist() == [[10, 20], [30, 40]])
    q = 'a,"b, with comma",3\n"x ""quoted""",y,4\n'
    got_q = np.loadtxt(io.StringIO(q), delimiter=",", quotechar='"', dtype=str).tolist()
    report("loadtxt quotechar='\"' (1.23+): delimiters inside quotes are data, doubled quote \"\" is a literal quote", got_q == [["a", "b, with comma", "3"], ['x "quoted"', "y", "4"]], f"(got {got_q})")
    report("loadtxt max_rows (1.23+ doc): 'empty rows ... comment lines are not counted towards max_rows, while such lines are counted in skiprows'",
           np.loadtxt(io.StringIO("# c\n1 2\n\n# d\n3 4\n5 6\n"), max_rows=2).tolist() == [[1, 2], [3, 4]])
report("loadtxt ndmin: one row -> shape (3,) by default, (1, 3) with ndmin=2; one value -> shape ()", np.loadtxt(io.StringIO("1 2 3\n")).shape == (3,)
       and np.loadtxt(io.StringIO("1 2 3\n"), ndmin=2).shape == (1, 3) and np.loadtxt(io.StringIO("7\n")).shape == ())
sd = np.loadtxt(io.StringIO("M 21 72.5\nF 35 58.25\n"), dtype={"names": ("sex", "age", "weight"), "formats": ("U1", "i4", "f8")})
report("loadtxt structured dtype (documented example: sex/age/weight)", sd.dtype.names == ("sex", "age", "weight") and sd.tolist() == [("M", 21, 72.5), ("F", 35, 58.25)])
report("loadtxt complex: '1+2j' and '(3-4j)' parse to complex", np.loadtxt(io.StringIO("1+2j (3-4j)\n"), dtype=complex).tolist() == [1 + 2j, 3 - 4j])
with tempfile.TemporaryDirectory() as td:
    pth = os.path.join(td, "l1.txt"); open(pth, "wb").write("é,1\nü,2\n".encode("latin-1"))
    gl = np.loadtxt(pth, delimiter=",", dtype=str, encoding="latin-1").tolist()
report("loadtxt(encoding='latin-1') decodes the file bytes", gl == [["é", "1"], ["ü", "2"]])
report("loadtxt: a row with the wrong number of columns raises ValueError", raises(lambda: np.loadtxt(io.StringIO("1 2\n3\n")), ValueError) is not None)
b = io.StringIO(); np.savetxt(b, np.array([[1, 2.5], [3, 4.25]]), fmt=["%d", "%.3f"], delimiter=",", header="a,b\nsecond", footer="end", newline="\r\n")
report("savetxt fmt sequence, delimiter, newline='\\r\\n' ends each row, header/footer prefixed by '# ' (a '\\n' inside the header is kept and followed by the prefix)", b.getvalue() == "# a,b\n# second\r\n1,2.500\r\n3,4.250\r\n# end\r\n", repr(b.getvalue()))
b = io.StringIO(); np.savetxt(b, np.array([[1, 2.5]]), fmt="Iter %d -- %10.5f", delimiter=",")
report("savetxt with a full multi-format string: 'delimiter is ignored'", b.getvalue() == "Iter 1 --    2.50000\n")
b = io.StringIO(); np.savetxt(b, np.array([1.5, 2.0]), fmt="%g", header="h", comments="%% ")
report("savetxt 1-D input writes one value per line; comments= replaces the '# ' prefix", b.getvalue() == "%% h\n1.5\n2\n")
b = io.StringIO(); np.savetxt(b, np.array([[1 + 2j, -3.5 - 0.25j]]), fmt="%.2e")
exp_c = " (1.00e+00+2.00e+00j)  (-3.50e+00-2.50e-01j)\n"
report("savetxt complex with a single fmt writes ' (%s+%sj)' % (fmt, fmt) per value", b.getvalue() == exp_c, repr(b.getvalue()))
b = io.StringIO(); np.savetxt(b, np.array([(1, 2.5, "x")], dtype=[("a", "i4"), ("b", "f8"), ("c", "U3")]), fmt="%s")
report("savetxt of a structured array writes one field per column", b.getvalue() == "1 2.5 x\n")

print("---- text I/O: genfromtxt")
g = np.genfromtxt(io.StringIO("name,age,score\nann,31,1.5\nbob,,2.25\ncid,40,N/A\n"), delimiter=",", names=True, dtype=None, encoding="utf-8", missing_values="N/A")
print(f"   genfromtxt(names=True, dtype=None): dtype {g.dtype}, rows {g.tolist()}")
report("genfromtxt names=True takes the field names from the first line; dtype=None infers str / int / float per column", g.dtype.names == ("name", "age", "score")
       and g.dtype["name"].kind == "U" and g.dtype["age"].kind == "i" and g.dtype["score"].kind == "f")
report("genfromtxt default fillers: missing int -> -1, missing float -> nan (documented defaults)", g["age"].tolist() == [31, -1, 40] and g["score"][0] == 1.5 and g["score"][1] == 2.25 and math.isnan(g["score"][2]))
g2 = np.genfromtxt(io.StringIO("1,N/A,3\n4,5,???\n"), delimiter=",", missing_values={1: "N/A", 2: "???"}, filling_values={1: -99, 2: -77})
report("genfromtxt missing_values / filling_values per column", g2.tolist() == [[1, -99, 3], [4, 5, -77]])
gm = np.genfromtxt(io.StringIO("1,,3\n4,5,\n"), delimiter=",", usemask=True)
report("genfromtxt usemask=True returns a MaskedArray masking the missing entries", isinstance(gm, np.ma.MaskedArray) and gm.mask.tolist() == [[False, True, False], [False, False, True]])
g3 = np.genfromtxt(io.StringIO("junk\njunk2\n1 2\n3 4\n5 6\nfooter\n"), skip_header=2, skip_footer=1)
report("genfromtxt skip_header / skip_footer", g3.tolist() == [[1, 2], [3, 4], [5, 6]])
g4 = np.genfromtxt(io.StringIO("  1  2.5abc\n 10 -3.0xyz\n"), delimiter=[3, 5, 3], dtype=None, encoding="utf-8", autostrip=True)
print(f"   fixed-width delimiter=[3,5,3] autostrip: {g4.tolist()}")
report("genfromtxt delimiter as a sequence of field widths (fixed-width columns), autostrip=True", g4.tolist() == [(1, 2.5, "abc"), (10, -3.0, "xyz")])
g5 = np.genfromtxt(io.StringIO("a b c\n1 2 3\n4 5 6\n"), names=True, usecols=("a", "c"))
report("genfromtxt usecols by field names", g5.dtype.names == ("a", "c") and g5.tolist() == [(1, 3), (4, 6)])
with caught() as c:
    g6 = np.genfromtxt(io.StringIO("1 2\n3 4 5\n6 7\n"), invalid_raise=False)
report("genfromtxt invalid_raise=False skips the bad row with a ConversionWarning", g6.tolist() == [[1, 2], [6, 7]] and "ConversionWarning" in c.names)
report("genfromtxt invalid_raise=True (default) raises ValueError on the bad row", raises(lambda: np.genfromtxt(io.StringIO("1 2\n3 4 5\n")), ValueError) is not None)
g7 = np.genfromtxt(io.StringIO("1 2\n3 4\n"), dtype=[("x", int), ("y", float)])
report("genfromtxt with a structured dtype and no names: fields named from the dtype", g7.dtype.names == ("x", "y") and g7.tolist() == [(1, 2.0), (3, 4.0)])
g8 = np.genfromtxt(io.StringIO("1 2 3\n"), dtype=None, names="a,b,c", defaultfmt="var_%i")
report("genfromtxt names='a,b,c' as a comma-separated string", g8.dtype.names == ("a", "b", "c"))
g9 = np.genfromtxt(io.StringIO("1 2\n"), dtype=[int, int], defaultfmt="var_%02i")
report("genfromtxt defaultfmt names unnamed fields ('var_00', 'var_01')", g9.dtype.names == ("var_00", "var_01"))
gx = np.genfromtxt(io.StringIO("%.18e\n" % 0.1 + "%.18e\n" % 5e-324))
report("genfromtxt parses '%.18e' text back bit-exactly (0.1, 5e-324)", gx.tolist() == [0.1, 5e-324])
gc = np.genfromtxt(io.StringIO("1,2 # c\n3,4\n"), delimiter=",")
report("genfromtxt strips inline comments after data", gc.tolist() == [[1, 2], [3, 4]])

print("---- binary I/O: .npy format parsed by hand, save / load")
def parse_npy(raw):
    assert raw[:6] == b"\x93NUMPY", raw[:8]
    major, minor = raw[6], raw[7]
    if major == 1: hl = struct.unpack("<H", raw[8:10])[0]; start = 10
    else: hl = struct.unpack("<I", raw[8:12])[0]; start = 12
    hdr = raw[start:start + hl].decode("latin1" if major < 3 else "utf8")
    return (major, minor), hdr, ast.literal_eval(hdr), raw[start + hl:], start + hl
dts = ["?", "i1", "u1", "<i2", "<u2", "<i4", "<u4", "<i8", "<u8", "<f2", "<f4", "<f8", "<c8", "<c16", "<U7", "S5", "<M8[ns]", "<m8[s]", "V4", ">i4", ">f8", "<g", "<G"]
rs = np.random.RandomState(7)
okhdr, okdata, okload = [], [], []
for dstr in dts:
    d = np.dtype(dstr)
    if d.kind in "iu": a = rs.randint(np.iinfo(d).min, np.iinfo(d).max, size=(3, 4), dtype=d.newbyteorder("=")).astype(d)
    elif d.kind == "b": a = rs.rand(3, 4) > 0.5
    elif d.kind == "f": a = (rs.randn(3, 4) * 1e3).astype(d)
    elif d.kind == "c": a = (rs.randn(3, 4) + 1j * rs.randn(3, 4)).astype(d)
    elif d.kind == "U": a = np.array([["é", "日本", "", "abcdefg"]] * 3, dtype=d)
    elif d.kind == "S": a = np.array([[b"ab", b"", b"xyz\x01", b"12345"]] * 3, dtype=d)
    elif d.kind == "M": a = np.array(rs.randint(-10**18, 10**18, size=(3, 4)), dtype=d)
    elif d.kind == "m": a = np.array(rs.randint(-10**9, 10**9, size=(3, 4)), dtype=d)
    else: a = np.frombuffer(rs.bytes(48), dtype=d).reshape(3, 4)
    bio = io.BytesIO(); np.save(bio, a); raw = bio.getvalue()
    ver, hdr, hd, data, off = parse_npy(raw)
    good_hdr = ver == (1, 0) and off % 64 == 0 and hdr.endswith("\n") and np.dtype(hd["descr"]) == a.dtype and hd["fortran_order"] is False and tuple(hd["shape"]) == a.shape and list(hd.keys()) == sorted(hd.keys())
    okhdr.append(good_hdr or dstr); okdata.append(data == a.tobytes() or dstr)
    bio.seek(0); b_ = np.load(bio)
    okload.append((b_.dtype == a.dtype and b_.shape == a.shape and b_.tobytes() == a.tobytes()) or dstr)
report(f"np.save header for {len(dts)} dtypes: '\\x93NUMPY' v1.0, little-endian uint16 HEADER_LEN, dict literal with sorted keys descr/fortran_order/shape, '\\n'-terminated, total divisible by 64",
       all(x is True for x in okhdr), str([x for x in okhdr if x is not True]))
report("np.save data section == the array's contiguous bytes (C order) for every dtype", all(x is True for x in okdata), str([x for x in okdata if x is not True]))
report("np.load round trip preserves dtype (incl. byte order '>i4', '>f8', longdouble, M8/m8 units, V4), shape and bytes", all(x is True for x in okload), str([x for x in okload if x is not True]))
aint = np.array([[1, -2, 3], [2**31 - 1, -2**31, 0]], dtype="<i4"); bio = io.BytesIO(); np.save(bio, aint)
report("int32 data bytes equal struct.pack('<6i', ...) (independent encoding)", parse_npy(bio.getvalue())[3] == struct.pack("<6i", 1, -2, 3, 2**31 - 1, -2**31, 0))
af = np.asfortranarray(np.arange(12, dtype="<f8").reshape(3, 4)); bio = io.BytesIO(); np.save(bio, af); _, _, hd, data, _ = parse_npy(bio.getvalue())
bio.seek(0); lf = np.load(bio)
report("Fortran-ordered input: fortran_order True, data in column-major order, load returns an F-contiguous equal array",
       hd["fortran_order"] is True and data == struct.pack("<12d", *[float(4 * r + c) for c in range(4) for r in range(3)]) and lf.flags.f_contiguous and lf.tolist() == af.tolist())
ansl = np.arange(20, dtype="<i2").reshape(4, 5)[::2, 1::2]; bio = io.BytesIO(); np.save(bio, ansl); _, _, hd, data, _ = parse_npy(bio.getvalue())
report("non-contiguous slice is saved in C order with fortran_order False", hd["fortran_order"] is False and data == struct.pack("<4h", 1, 3, 11, 13))
for shp in [(), (0,), (0, 3), (1, 1, 1)]:
    a = np.full(shp, 2.5); bio = io.BytesIO(); np.save(bio, a); _, _, hd, data, _ = parse_npy(bio.getvalue()); bio.seek(0); l_ = np.load(bio)
    report(f"shape {shp}: header shape {tuple(hd['shape'])}, data {len(data)} bytes = prod(shape) * 8 ('shape=() means there is 1 element'), load shape preserved",
           tuple(hd["shape"]) == shp and len(data) == math.prod(shp) * 8 and l_.shape == shp)
sdt = np.dtype([("id", "<i4"), ("pos", [("x", "<f4"), ("y", "<f4")]), ("tag", "S3"), ("v", "<f8", (2,))])
sa = np.array([(1, (0.5, -1.5), b"ab", (1.0, 2.0)), (2, (2.5, 3.5), b"xyz", (3.0, 4.0))], dtype=sdt)
bio = io.BytesIO(); np.save(bio, sa); _, _, hd, _, _ = parse_npy(bio.getvalue()); bio.seek(0); ls = np.load(bio)
report("nested structured dtype with a subarray field: descr == dtype.descr and load round-trips values", np.dtype(hd["descr"]) == sdt and ls.dtype == sdt and ls.tobytes() == sa.tobytes() and ls["pos"]["y"].tolist() == [-1.5, 3.5])
aobj = np.array([1, "a", None, {"k": 2}], dtype=object); bio = io.BytesIO(); np.save(bio, aobj); bio.seek(0)
e1 = raises(lambda: np.load(bio), ValueError); bio.seek(0); lo = np.load(bio, allow_pickle=True)
report("object array: np.load default allow_pickle=False raises ValueError; allow_pickle=True returns the objects", e1 == "ValueError" and lo.tolist() == aobj.tolist())
report("np.save(object array, allow_pickle=False) raises ValueError", raises(lambda: np.save(io.BytesIO(), aobj, allow_pickle=False), ValueError) is not None)
hand_hdr = "{'descr': '>u2', 'fortran_order': True, 'shape': (2, 3), }"
pad = 64 - (10 + len(hand_hdr) + 1) % 64
hh = (hand_hdr + " " * pad + "\n").encode("latin1")
hand = b"\x93NUMPY\x01\x00" + struct.pack("<H", len(hh)) + hh + struct.pack(">6H", 1, 4, 2, 5, 3, 6)
lh = np.load(io.BytesIO(hand))
report("np.load of a hand-written v1.0 file (big-endian '>u2', fortran_order True, shape (2,3)) gives [[1,2,3],[4,5,6]]", lh.tolist() == [[1, 2, 3], [4, 5, 6]] and lh.dtype == np.dtype(">u2"))
bio = io.BytesIO(); np.save(bio, np.zeros(2, dtype=[("é", "<i4")])); ver_u = parse_npy(bio.getvalue())[0]
report("a non-latin-1... unicode field name 'é' is latin-1 encodable -> v1.0; '日' needs utf-8 -> format v3.0 (documented)", ver_u == (1, 0)
       and (lambda b2: (np.save(b2, np.zeros(2, dtype=[("日", "<i4")])), parse_npy(b2.getvalue())[0])[1])(io.BytesIO()) == (3, 0))
bigd = np.dtype([(f"field_{i:05d}", "<f8") for i in range(3000)])
bio = io.BytesIO(); np.save(bio, np.zeros(1, dtype=bigd)); verbig, _, hdb, _, offb = parse_npy(bio.getvalue())
report("header > 65535 bytes (3000 fields) switches to format v2.0 with a uint32 HEADER_LEN, still 64-aligned", verbig == (2, 0) and offb % 64 == 0 and np.dtype(hdb["descr"]) == bigd)
with tempfile.TemporaryDirectory() as td:
    p_ = os.path.join(td, "m.npy"); arr_m = np.arange(24, dtype="<f4").reshape(4, 6); np.save(p_, arr_m)
    mm = np.load(p_, mmap_mode="r"); okmm = isinstance(mm, np.memmap) and mm.tolist() == arr_m.tolist() and not mm.flags.writeable; del mm
    p2 = os.path.join(td, "noext"); np.save(p2, arr_m); okext = os.path.exists(p2 + ".npy")
report("np.load(mmap_mode='r') returns a read-only memmap with the same values; np.save appends '.npy' to a bare filename", okmm and okext)

print("---- savez / savez_compressed / NpzFile")
with tempfile.TemporaryDirectory() as td:
    p1 = os.path.join(td, "a.npz"); p2 = os.path.join(td, "b.npz")
    xa, ya = np.arange(10), np.linspace(0, 1, 7)
    np.savez(p1, xa, ya, named=np.array(["s", "t"]))
    np.savez_compressed(p2, xa, ya, named=np.array(["s", "t"]))
    with zipfile.ZipFile(p1) as z1, zipfile.ZipFile(p2) as z2:
        n1 = sorted(z1.namelist()); c1 = {i.compress_type for i in z1.infolist()}; c2 = {i.compress_type for i in z2.infolist()}
        mem_ok = all(parse_npy(z1.read(n))[3] == np.load(io.BytesIO(z1.read(n))).tobytes() for n in n1)
        same = all(z1.read(n) == z2.read(n) for n in n1)
    report("savez: positional arrays named arr_0, arr_1, keywords by name, members '<name>.npy' in a zip", n1 == ["arr_0.npy", "arr_1.npy", "named.npy"] and mem_ok)
    report("savez stores members uncompressed (ZIP_STORED); savez_compressed uses ZIP_DEFLATED; the member .npy bytes are identical",
           c1 == {zipfile.ZIP_STORED} and c2 == {zipfile.ZIP_DEFLATED} and same)
    with np.load(p1) as npz:
        lazy = type(npz).__name__ == "NpzFile" and sorted(npz.files) == ["arr_0", "arr_1", "named"] and "arr_0" in npz and "arr_0.npy" not in npz.files
        vals_ok = npz["arr_0"].tolist() == xa.tolist() and npz["arr_1"].tolist() == ya.tolist() and npz.f.named.tolist() == ["s", "t"]
        both = npz["arr_0.npy"].tolist() == xa.tolist() if raises(lambda: npz["arr_0.npy"]) is None else False
    report("np.load(.npz) returns a lazy NpzFile: .files lists names without '.npy', 'in', item and .f attribute access load arrays", lazy and vals_ok)
    report("NpzFile also accepts the member name with the '.npy' suffix", both)
    report("savez with a positional array and keyword 'arr_0' raises ValueError ('Cannot use un-named variables and keyword arr_0')",
           raises(lambda: np.savez(os.path.join(td, "c.npz"), xa, arr_0=ya), ValueError) is not None)
    np.savez(os.path.join(td, "o.npz"), o=np.array([None, 1], dtype=object))
    with np.load(os.path.join(td, "o.npz")) as npo:
        report("an object member of an .npz raises ValueError on access with the default allow_pickle=False", raises(lambda: npo["o"], ValueError) is not None)
    npz2 = np.load(p1); npz2.close(); closed_err = raises(lambda: npz2["arr_0"])
    report("accessing a closed NpzFile raises", closed_err is not None, f"({closed_err})")

print("---- tofile / fromfile / frombuffer / fromstring")
with tempfile.TemporaryDirectory() as td:
    pb = os.path.join(td, "raw.bin"); arr = np.array([1.5, -2.25, 1e300, 5e-324], dtype="<f8"); arr.tofile(pb)
    rawb = open(pb, "rb").read()
    report("tofile writes the raw bytes (struct.pack('<4d')), no header", rawb == struct.pack("<4d", 1.5, -2.25, 1e300, 5e-324))
    report("fromfile(dtype) reads them back; count=2 and offset=8 bytes select elements 1..2", np.fromfile(pb, dtype="<f8").tolist() == arr.tolist()
           and np.fromfile(pb, dtype="<f8", count=2, offset=8).tolist() == [-2.25, 1e300])
    pt = os.path.join(td, "t.txt"); np.array([1.5, 2.0, 3.25]).tofile(pt, sep=",", format="%.2f")
    report("tofile(sep=',', format='%.2f') writes text; fromfile(sep=',') reads it", open(pt).read() == "1.50,2.00,3.25" and np.fromfile(pt, sep=",").tolist() == [1.5, 2.0, 3.25])
bb = struct.pack("<5i", 10, 20, 30, 40, 50)
fb = np.frombuffer(bb, dtype="<i4", count=2, offset=8)
report("frombuffer(offset=8 bytes, count=2) -> [30, 40]; read-only view of an immutable bytes object", fb.tolist() == [30, 40] and not fb.flags.writeable)
ba = bytearray(bb); fbw = np.frombuffer(ba, dtype="<i4"); fbw[0] = 99
report("frombuffer of a bytearray is a writeable view sharing memory (writing element 0 changes the bytearray)", ba[:4] == struct.pack("<i", 99))
report("frombuffer with a size not a multiple of the itemsize raises ValueError", raises(lambda: np.frombuffer(b"\x00" * 7, dtype="<i4"), ValueError) is not None)
report("fromstring text mode: '1, 2,3' with sep=',' -> [1, 2, 3]; sep=' ' splits on any whitespace", np.fromstring("1, 2,3", sep=",").tolist() == [1, 2, 3] and np.fromstring("1 2\n3\t4", sep=" ").tolist() == [1, 2, 3, 4])
with caught() as c:
    r_bin = raises(lambda: np.fromstring(b"\x01\x00\x00\x00", dtype="<i4"))
if NPV >= (2, 3):
    report("fromstring binary mode (sep='') raises ValueError in 2.3+ ('The binary mode of fromstring now errors, use frombuffer')", r_bin == "ValueError")
else:
    report("fromstring binary mode (sep='') still works but emits DeprecationWarning (deprecated 1.14)", r_bin is None and "DeprecationWarning" in c.names)
with caught() as c:
    r_bad = raises(lambda: np.fromstring("1,2,x", sep=","))
if NPV >= (2, 3):
    report("fromstring('1,2,x', sep=',') raises ValueError in 2.3+ ('error on bad data')", r_bad == "ValueError")
else:
    report("fromstring('1,2,x', sep=',') returns [1, 2] with DeprecationWarning 'could not be read to its end'", r_bad is None and "DeprecationWarning" in c.names)

print("---- printing: array2string / set_printoptions / repr round trips")
A3 = np.array([0.1, 0.25, 1 / 3])
report("floatmode='fixed' precision=3 -> '[0.100 0.250 0.333]' (always exactly precision digits)", np.array2string(A3, precision=3, floatmode="fixed") == "[0.100 0.250 0.333]")
report("floatmode='unique' ignores precision: shortest repr of each value", np.array2string(A3, precision=3, floatmode="unique") == "[0.1                0.25               0.3333333333333333]")
report("floatmode='maxprec' -> at most precision digits, per element '[0.1   0.25  0.333]'", np.array2string(A3, precision=3, floatmode="maxprec") == "[0.1   0.25  0.333]")
report("floatmode='maxprec_equal' -> same digit count for all '[0.100 0.250 0.333]'", np.array2string(A3, precision=3, floatmode="maxprec_equal") == "[0.100 0.250 0.333]")
report("suppress_small=True prints 1e-10 as 0. next to 1; default switches to scientific", np.array2string(np.array([1e-10, 1.0]), suppress_small=True) == "[0. 1.]"
       and np.array2string(np.array([1e-10, 1.0])) == "[1.e-10 1.e+00]")
report("threshold=5, edgeitems=2 summarises arange(10) as '[0 1 ... 8 9]'", np.array2string(np.arange(10), threshold=5, edgeitems=2) == "[0 1 ... 8 9]")
report("sign='+' and sign=' '", np.array2string(np.array([1.0, -0.5]), sign="+") == "[+1.  -0.5]" and np.array2string(np.array([1.0, -0.5]), sign=" ") == "[ 1.  -0.5]")
report("legacy='1.13' reproduces the old sign padding '[ 1.   0.5]' (modern '[1.  0.5]')", np.array2string(np.array([1.0, 0.5]), legacy="1.13") == "[ 1.   0.5]" and np.array2string(np.array([1.0, 0.5])) == "[1.  0.5]")
if NPV >= (1, 22):
    with np.printoptions(legacy="1.21"): r121 = repr(np.array([(1, 2.0)], dtype=[("a", "i4"), ("b", "f8")]))
    print(f"   legacy='1.21' structured repr: {r121!r}")
    report("legacy='1.21' is accepted (1.22+)", "array(" in r121)
if NP2:
    with np.printoptions(legacy="1.25"): r125 = repr(np.float64(1.5))
    report("NEP 51 (2.0): repr(np.float64(1.5)) == 'np.float64(1.5)'; legacy='1.25' restores '1.5'", repr(np.float64(1.5)) == "np.float64(1.5)" and r125 == "1.5")
else:
    report("1.x: repr(np.float64(1.5)) == '1.5'", repr(np.float64(1.5)) == "1.5")
old = np.get_printoptions()
with np.printoptions(precision=2, threshold=3):
    inside = np.array2string(np.array([1 / 3, 2 / 3, 1.0, 2.0]))
report("np.printoptions(precision=2, threshold=3) applies inside the block and restores the previous options on exit", inside == "[0.33 0.67 1.   2.  ]" and np.get_printoptions() == old, f"(inside: {inside!r})")
np.set_printoptions(precision=4)
p4 = str(np.array([math.pi])); np.set_printoptions(**old)
report("set_printoptions(precision=4) -> str(array([pi])) == '[3.1416]'", p4 == "[3.1416]")
report("str of nan/inf array '[ nan  inf -inf]'", np.array2string(np.array([np.nan, np.inf, -np.inf])) == "[ nan  inf -inf]")
xs = [struct.unpack("<d", struct.pack("<Q", rng.getrandbits(64)))[0] for _ in range(3000)] + [5e-324, 1e-310, 0.1, 1e16, 1e-5, 9007199254740993.0, 1.7976931348623157e308]
xs = [v for v in xs if math.isfinite(v)]
ns_ = {"array": np.array, "np": np, "nan": np.nan, "inf": np.inf, "float32": np.float32}
report("repr of an array with more than threshold=1000 elements is summarised with '...' (documented default)", "..." in repr(np.array(xs)))
with np.printoptions(threshold=sys.maxsize):
    ra = repr(np.array(xs)); back = eval(ra, ns_)
nexact = int(np.sum(back == np.array(xs)))
print(f"   default precision=8 / floatmode='maxprec': eval(repr(a)) reproduces {nexact} of {len(xs)} values exactly (repr is not a round trip by default)")
with np.printoptions(threshold=sys.maxsize, floatmode="unique"):
    ra = repr(np.array(xs)); back = eval(ra, ns_)
    ra32 = repr(np.array(xs[:500], dtype=np.float32)); back32 = eval(ra32, ns_)
report(f"with floatmode='unique' (and threshold=sys.maxsize), eval(repr(a)) is bit-exact for all {len(xs)} float64 values ('unique': shortest repr that uniquely identifies)", back.tobytes() == np.array(xs).tobytes())
report("... and for a float32 array (repr carries dtype=float32)", back32.dtype == np.float32 and back32.tobytes() == np.array(xs[:500], dtype=np.float32).tobytes())
report("str(np.float64(x)) == Python repr(x) (shortest round-trip digits, same exponent style) for every value", all(str(np.float64(v)) == repr(v) for v in xs))
def f32(x):
    try: return struct.unpack("<f", struct.pack("<f", x))[0]
    except OverflowError: return math.copysign(math.inf, x)
def shortest32(x):
    """Fewest significant decimal digits whose value rounds (float32 RNE) back to x; tries the correctly rounded n-digit value and its neighbours."""
    dx = D(x)
    for n in range(1, 10):
        q = dx.scaleb(-dx.adjusted()).quantize(D(10) ** -(n - 1), rounding=decimal.ROUND_HALF_EVEN).scaleb(dx.adjusted())
        step = D(10) ** (q.adjusted() - (n - 1))
        for cand in (q, q - step, q + step):
            if f32(float(cand)) == x and len(cand.normalize().as_tuple().digits) <= n: return n
    return 9
f32v = [struct.unpack("<f", struct.pack("<I", rng.getrandbits(32)))[0] for _ in range(3000)] + [f32(0.1), f32(1 / 3), 1.4e-45, 3.4028234663852886e38, 16777217.0]
f32v = [f32(v) for v in f32v if math.isfinite(v) and v != 0]
bad32 = []
for v in f32v:
    s_ = str(np.float32(v)); nd = len(D(s_).normalize().as_tuple().digits)
    if f32(float(s_)) != v or nd != shortest32(v): bad32.append((v, s_, nd, shortest32(v)))
report(f"str(np.float32(x)) round-trips and uses the minimal number of digits for {len(f32v)} random float32 (Dragon4 'unique')", not bad32, str(bad32[:3]))
fbad = []
for v in xs[:600] + [0.125, 0.375, 2.5, 0.5, 1.5, 1e-5]:
    for p in [0, 1, 3, 7, 17, 25]:
        got = np.format_float_positional(v, precision=p, unique=False)
        dv = D(v).quantize(D(10) ** -p, rounding=decimal.ROUND_HALF_EVEN) if abs(v) < 1e30 else None
        if dv is None: continue
        exp = format(dv, "f"); exp = exp + "." if "." not in exp else exp
        if exp.startswith("-") and D(exp) == 0: exp = exp  # sign of zero kept
        if got.lstrip("-") != exp.lstrip("-") or (got.startswith("-") != (math.copysign(1, v) < 0)): fbad.append((v, p, got, exp))
report("format_float_positional(unique=False, precision=p) == exact binary value rounded half-even at p decimals ('unbiased rounding', Decimal truth)", not fbad, str(fbad[:3]))
sbad = []
for v in xs[:600] + [0.125, 2.5e10, 1.5e-300]:
    for p in [0, 1, 4, 16, 20]:
        got = np.format_float_scientific(v, precision=p, unique=False)
        dv = D(v); e = dv.adjusted()
        mant = dv.scaleb(-e).quantize(D(10) ** -p, rounding=decimal.ROUND_HALF_EVEN)
        if abs(mant) >= 10: mant = (mant / 10).quantize(D(10) ** -p, rounding=decimal.ROUND_HALF_EVEN); e += 1
        ms = format(mant, "f"); ms = ms + "." if "." not in ms else ms
        exp = f"{ms}e{'+' if e >= 0 else '-'}{abs(e):02d}"
        if got != exp: sbad.append((v, p, got, exp))
report("format_float_scientific(unique=False, precision=p) == Decimal mantissa rounded half-even to p digits, exponent at least 2 digits", not sbad, str(sbad[:3]))
report("format_float_positional trim: 1.0 -> 'k' '1.', '.' '1.', '0' '1.0', '-' '1' (documented modes)",
       [np.format_float_positional(1.0, trim=t_) for t_ in "k.0-"] == ["1.", "1.", "1.0", "1"])
report("pad_left=4, pad_right=3 -> '   1.5  '; min_digits=4 -> '1.5000'; exp_digits=3 -> '1.e+005'; fractional=False precision=4 -> '123.5'",
       np.format_float_positional(1.5, pad_left=4, pad_right=3) == "   1.5  " and np.format_float_positional(1.5, min_digits=4) == "1.5000"
       and np.format_float_scientific(1e5, exp_digits=3) == "1.e+005" and np.format_float_positional(123.456, precision=4, unique=False, fractional=False) == "123.5")
report("format_float_positional(2.0**70 + 2**20, precision=0, unique=False) prints the exact integer; unique 1e23 prints '1' followed by 23 zeros",
       np.format_float_positional(2.0**70 + 2**20, precision=0, unique=False) == str(2**70 + 2**20) + "." and np.format_float_positional(1e23) == "1" + "0" * 23 + ".")
report("format_float_positional(unique=True, precision=3) rounds the shortest repr: 1/3 -> '0.333', 0.1 -> '0.1'", np.format_float_positional(1 / 3, precision=3) == "0.333" and np.format_float_positional(0.1, precision=3) == "0.1")
report("float16 / float32 inputs use their own shortest digits (np.float32(0.1) -> '0.1', np.float16(0.1) -> '1.e-01' scientific)",
       np.format_float_positional(np.float32(0.1)) == "0.1" and np.format_float_scientific(np.float16(0.1)) == "1.e-01" and np.format_float_positional(np.float16(0.1)) == "0.1")

print("---- structured arrays: layout against ctypes, fields, assignment")
CT = {"i1": ctypes.c_int8, "u1": ctypes.c_uint8, "i2": ctypes.c_int16, "u2": ctypes.c_uint16, "i4": ctypes.c_int32, "u4": ctypes.c_uint32,
      "i8": ctypes.c_int64, "u8": ctypes.c_uint64, "f4": ctypes.c_float, "f8": ctypes.c_double, "b1": ctypes.c_bool}
def rand_fields(depth=0):
    fs = []
    for i in range(rng.randint(1, 5)):
        r = rng.random()
        if r < 0.15 and depth < 2: fs.append((f"s{depth}{i}", rand_fields(depth + 1), None))
        else:
            t = rng.choice(list(CT)); n = rng.choice([None, None, None, 2, 3])
            fs.append((f"f{depth}{i}", t, n))
    return fs
def np_desc(fs): return [(nm, np_desc(t) if isinstance(t, list) else "<" + t if t not in ("i1", "u1", "b1") else t) + ((n,) if n else ()) for nm, t, n in fs]
def np_desc_al(fs): return np.dtype([(nm, np_desc_al(t) if isinstance(t, list) else ("<" + t if t not in ("i1", "u1", "b1") else t)) + ((n,) if n else ()) for nm, t, n in fs], align=True)
def ct_struct(fs, name="S"):
    fl = []
    for nm, t, n in fs:
        c_ = ct_struct(t, name + nm) if isinstance(t, list) else CT[t]
        fl.append((nm, c_ * n if n else c_))
    return type(name, (ctypes.Structure,), {"_fields_": fl})
def packed_layout(fs):
    off = 0; res = {}
    for nm, t, n in fs:
        sz = packed_layout(t)[1] if isinstance(t, list) else np.dtype(t).itemsize
        res[nm] = off; off += sz * (n or 1)
    return res, off
okal, okpk = True, True
for trial in range(300):
    fs = rand_fields()
    dal = np_desc_al(fs); cs = ct_struct(fs)
    offs = {nm: dal.fields[nm][1] for nm, _, _ in fs}; coffs = {nm: getattr(cs, nm).offset for nm, _, _ in fs}
    if offs != coffs or dal.itemsize != ctypes.sizeof(cs) or dal.alignment != ctypes.alignment(cs): okal = False; print(f"   align mismatch {fs}: np {offs} {dal.itemsize}, ctypes {coffs} {ctypes.sizeof(cs)}")
    dpk = np.dtype(np_desc(fs)); pl, psz = packed_layout(fs)
    if {nm: dpk.fields[nm][1] for nm, _, _ in fs} != pl or dpk.itemsize != psz: okpk = False
report("align=True: field offsets, itemsize and alignment equal the C layout of the same ctypes.Structure (300 random nested/subarray layouts)", okal)
report("default (packed) structured dtypes: offsets are cumulative sums of itemsizes, no padding (300 layouts)", okpk)
d1 = np.dtype([("a", "i1"), ("b", "<f8")]); d1a = np.dtype([("a", "i1"), ("b", "<f8")], align=True)
report("documented example: [('a','i1'),('b','f8')] has itemsize 9 packed, 16 with align=True (b at offset 8)", d1.itemsize == 9 and d1a.itemsize == 16 and d1a.fields["b"][1] == 8 and d1a.isalignedstruct)
dx = np.dtype({"names": ["x", "y"], "formats": ["<i4", "<f4"], "offsets": [0, 8], "itemsize": 16})
report("dict form with explicit offsets/itemsize: padding respected (itemsize 16, y at 8)", dx.itemsize == 16 and dx.fields["y"][1] == 8)
report("dtype equality: same names/formats/order equal; different names, order or byte order not equal", np.dtype([("a", "<i4"), ("b", "<f8")]) == np.dtype([("a", "<i4"), ("b", "<f8")])
       and np.dtype([("a", "<i4"), ("b", "<f8")]) != np.dtype([("x", "<i4"), ("b", "<f8")]) and np.dtype([("a", "<i4"), ("b", "<f8")]) != np.dtype([("b", "<f8"), ("a", "<i4")])
       and np.dtype([("a", "<i4")]) != np.dtype([("a", ">i4")]))
report("align=True dtype != the packed dtype with the same fields (different offsets/itemsize)", d1 != d1a)
dt_t = np.dtype([(("Title of a", "a"), "<i4"), ("b", "<f8")]); at = np.zeros(2, dtype=dt_t); at["Title of a"] = 7
report("field titles: a field is reachable by name and by title", at["a"].tolist() == [7, 7] and dt_t.names == ("a", "b"))
s3 = np.zeros(3, dtype=[("x", "<i4"), ("y", "<f8"), ("z", "<f4")]); s3["x"] = [1, 2, 3]; s3["y"] = [0.5, 1.5, 2.5]; s3["z"] = [9, 8, 7]
v = s3["y"]; v[0] = 100
report("single-field access returns a view (writing it changes the array)", s3["y"][0] == 100)
mf = s3[["x", "z"]]
report("multi-field index a[['x','z']] (1.16+) is a view keeping the original offsets and itemsize ('padded' view)", mf.dtype.itemsize == s3.dtype.itemsize and mf.dtype.fields["z"][1] == 12 and np.shares_memory(mf, s3))
from numpy.lib import recfunctions as rfn
rp = rfn.repack_fields(mf)
report("recfunctions.repack_fields removes the padding (itemsize 8)", rp.dtype.itemsize == 8 and rp.tolist() == [(1, 9.0), (2, 8.0), (3, 7.0)])
t1 = np.zeros(2, dtype=[("a", "<i4"), ("b", "<f8")]); t2 = np.array([(5, 1.5), (6, 2.5)], dtype=[("p", "<i8"), ("q", "<f4")]); t1[:] = t2
report("assignment between structured arrays is by field position, not name (1.14+), with casting", t1.tolist() == [(5, 1.5), (6, 2.5)])
t1[0] = (7, 8.5); t1[1] = 3
report("assigning a tuple sets fields in order; assigning a scalar sets every field", t1.tolist() == [(7, 8.5), (3, 3.0)])
report("structured == compares field-wise element by element", (np.array([(1, 2.0), (1, 3.0)], dtype=[("a", "i4"), ("b", "f8")]) == np.array([(1, 2.0), (1, 2.0)], dtype=[("a", "i4"), ("b", "f8")])).tolist() == [True, False])
ns = np.array([(1, (2.0, 3)), (4, (5.0, 6))], dtype=[("id", "i4"), ("pt", [("x", "f8"), ("k", "i2")])])
report("nested dtype: a['pt']['x'] and a[1]['pt']['k'] reach the inner fields", ns["pt"]["x"].tolist() == [2.0, 5.0] and ns[1]["pt"]["k"] == 6)
sub = np.zeros(2, dtype=[("v", "<f8", (2, 3))])
report("subarray field shape: a['v'].shape == (2, 2, 3)", sub["v"].shape == (2, 2, 3))

print("---- numpy.lib.recfunctions")
su = np.array([(1.0, 2.0, (3.0, 4.0)), (5.0, 6.0, (7.0, 8.0))], dtype=[("x", "<f4"), ("y", "<f8"), ("z", "<f4", (2,))])
uu = rfn.structured_to_unstructured(su)
report("structured_to_unstructured flattens fields and subarrays in order, promoting to a common dtype (f4, f8 -> f8)", uu.tolist() == [[1, 2, 3, 4], [5, 6, 7, 8]] and uu.dtype == np.float64)
report("structured_to_unstructured(dtype=int)", rfn.structured_to_unstructured(su, dtype=np.int32).tolist() == [[1, 2, 3, 4], [5, 6, 7, 8]])
nest = np.array([(1, (2, 3))], dtype=[("a", "i4"), ("b", [("c", "i4"), ("d", "i4")])])
report("structured_to_unstructured on a nested dtype flattens depth-first", rfn.structured_to_unstructured(nest).tolist() == [[1, 2, 3]])
back_s = rfn.unstructured_to_structured(np.array([[1, 2, 3, 4]], dtype=float), np.dtype([("x", "<f4"), ("y", "<f8"), ("z", "<f4", (2,))]))
report("unstructured_to_structured is the inverse", back_s["z"].tolist() == [[3, 4]] and back_s["y"].tolist() == [2])
base = np.array([(1, 10.0), (2, 20.0), (3, 30.0)], dtype=[("id", "<i8"), ("v", "<f8")])
ap = rfn.append_fields(base, "w", np.array([7, 8]), usemask=True)
print(f"   append_fields(base, 'w', [7, 8]) (default usemask=True): {type(ap).__name__}, w data {ap['w'].tolist()}")
report("append_fields default usemask=True returns a MaskedArray; the shorter new field is padded and masked", isinstance(ap, np.ma.MaskedArray) and ap["w"].mask.tolist() == [False, False, True] and ap["w"][:2].tolist() == [7, 8])
ap2 = rfn.append_fields(base, ["w", "t"], [np.array([7, 8, 9]), np.array(["a", "b", "c"])], usemask=False)
report("append_fields(usemask=False) with two fields: plain ndarray, values appended", not isinstance(ap2, np.ma.MaskedArray) and ap2.dtype.names == ("id", "v", "w", "t") and ap2.tolist() == [(1, 10.0, 7, "a"), (2, 20.0, 8, "b"), (3, 30.0, 9, "c")])
mg = rfn.merge_arrays((np.array([1, 2, 3]), np.array([10.5, 20.5])), usemask=False)
print(f"   merge_arrays(([1,2,3],[10.5,20.5]), usemask=False): {mg.tolist()} dtype {mg.dtype}")
report("merge_arrays pads the shorter array with the default fill_value -1 ('fill_value: Filling value used to pad missing data on the shorter arrays')", mg.tolist() == [(1, 10.5), (2, 20.5), (3, -1.0)] and mg.dtype.names == ("f0", "f1"))
mgf = rfn.merge_arrays((base, np.array([(5,), (6,), (7,)], dtype=[("k", "i4")])), flatten=True, usemask=False)
report("merge_arrays(flatten=True) concatenates the fields", mgf.dtype.names == ("id", "v", "k") and mgf.tolist() == [(1, 10.0, 5), (2, 20.0, 6), (3, 30.0, 7)])
r1 = np.array([(1, 10.0), (3, 30.0), (4, 40.0), (7, 70.0)], dtype=[("key", "<i8"), ("a", "<f8")])
r2 = np.array([(4, 400.0, 1), (1, 100.0, 2), (9, 900.0, 3)], dtype=[("key", "<i8"), ("a", "<f8"), ("b", "<i8")])
jin = rfn.join_by("key", r1, r2, jointype="inner", usemask=False)
d1_ = {k: a for k, a in r1.tolist()}; d2_ = {k: (a, b_) for k, a, b_ in r2.tolist()}
exp_in = [(k, d1_[k], d2_[k][0], d2_[k][1]) for k in sorted(set(d1_) & set(d2_))]
report("join_by inner: rows for common keys, sorted by key, colliding field 'a' renamed a1 / a2 (r1postfix='1', r2postfix='2')", jin.dtype.names == ("key", "a1", "a2", "b") and jin.tolist() == exp_in)
jout = rfn.join_by("key", r1, r2, jointype="outer")
keys_o = sorted(set(d1_) | set(d2_))
okout = jout["key"].tolist() == keys_o and all((jout["a1"].mask[i] == (k not in d1_)) and (jout["a2"].mask[i] == (k not in d2_)) for i, k in enumerate(keys_o)) \
    and all(jout["a1"][i] == d1_[k] for i, k in enumerate(keys_o) if k in d1_) and all(jout["b"][i] == d2_[k][1] for i, k in enumerate(keys_o) if k in d2_)
report("join_by outer: union of keys sorted, fields of the missing side masked", okout)
jlo = rfn.join_by("key", r1, r2, jointype="leftouter")
report("join_by leftouter: exactly the keys of r1, r2 fields masked where absent", jlo["key"].tolist() == sorted(d1_) and jlo["b"].mask.tolist() == [k not in d2_ for k in sorted(d1_)])
report("drop_fields / rename_fields", rfn.drop_fields(base, "v").dtype.names == ("id",) and rfn.rename_fields(base, {"v": "value"}).dtype.names == ("id", "value"))
st = rfn.stack_arrays((np.array([(1, 2.0)], dtype=[("a", "i8"), ("b", "f8")]), np.array([(3,)], dtype=[("a", "i8")])), usemask=True)
report("stack_arrays: records concatenated, missing field masked", st["a"].tolist() == [1, 3] and st["b"].mask.tolist() == [False, True])

print("---- recarray")
ra = np.rec.fromarrays([np.array([1, 2, 3]), np.array([0.5, 1.5, 2.5]), np.array(["a", "b", "c"])], names="x,y,size")
report("np.rec.fromarrays: attribute access r.x, r.y; records support r[1].y", ra.x.tolist() == [1, 2, 3] and ra.y.tolist() == [0.5, 1.5, 2.5] and ra[1].y == 1.5)
report("a field named like an ndarray attribute ('size'): r.size is the attribute, r['size'] the field (documented precedence)", ra.size == 3 and ra["size"].tolist() == ["a", "b", "c"])
rr = np.rec.array([(1, 2.0), (3, 4.0)], formats="i4,f8", names="p,q")
report("np.rec.array(list of tuples, formats, names)", rr.p.tolist() == [1, 3] and rr.q.dtype == np.float64 and isinstance(rr, np.recarray))
plain = np.zeros(2, dtype=[("u", "i4")]); rv = plain.view(np.recarray); rv.u = [5, 6]
report("view(np.recarray) shares data: assigning r.u writes the base array", plain["u"].tolist() == [5, 6])
report("a nested field accessed as an attribute is itself a recarray", isinstance(np.rec.array(ns).pt, np.recarray) and np.rec.array(ns).pt.x.tolist() == [2.0, 5.0])

print("---- np.ma: reductions against plain Python on the unmasked data")
ma = np.ma
def pmean(v): return sum(F(x) for x in v) / len(v)
def pvar(v, ddof=0):
    m = pmean(v); return sum((F(x) - m) ** 2 for x in v) / (len(v) - ddof)
def pmedian(v):
    s_ = sorted(F(x) for x in v); n = len(s_)
    return s_[n // 2] if n % 2 else (s_[n // 2 - 1] + s_[n // 2]) / 2
okr = {"sum": True, "mean": True, "var": True, "std": True, "median": True, "average": True, "min": True, "max": True, "prod": True, "count": True, "allmasked": True}
for trial in range(60):
    r_, c_ = rng.randint(1, 6), rng.randint(1, 9)
    data = [[rng.choice([rng.randint(-50, 50), rng.uniform(-1e3, 1e3)]) for _ in range(c_)] for _ in range(r_)]
    mask = [[rng.random() < 0.35 for _ in range(c_)] for _ in range(r_)]
    w = [[rng.randint(1, 5) for _ in range(c_)] for _ in range(r_)]
    A = ma.array(data, mask=mask, dtype=float); W = np.array(w, dtype=float)
    for ax in (None, 0, 1):
        if ax is None: groups = [[data[i][j] for i in range(r_) for j in range(c_) if not mask[i][j]]]; wg = [[w[i][j] for i in range(r_) for j in range(c_) if not mask[i][j]]]
        elif ax == 0: groups = [[data[i][j] for i in range(r_) if not mask[i][j]] for j in range(c_)]; wg = [[w[i][j] for i in range(r_) if not mask[i][j]] for j in range(c_)]
        else: groups = [[data[i][j] for j in range(c_) if not mask[i][j]] for i in range(r_)]; wg = [[w[i][j] for j in range(c_) if not mask[i][j]] for i in range(r_)]
        def res(x): return [x] if ax is None else list(x)
        got = {"sum": res(A.sum(axis=ax)), "mean": res(A.mean(axis=ax)), "var": res(A.var(axis=ax, ddof=1)), "std": res(A.std(axis=ax)), "median": res(ma.median(A, axis=ax)),
               "average": res(ma.average(A, axis=ax, weights=W)), "min": res(A.min(axis=ax)), "max": res(A.max(axis=ax)), "count": res(A.count(axis=ax))}
        for gi, (g, wgi) in enumerate(zip(groups, wg)):
            if not g:
                for k in ("sum", "mean", "median", "average", "min", "max"):
                    if got[k][gi] is not ma.masked and not (np.ma.is_masked(got[k][gi])): okr["allmasked"] = False
                continue
            chk = {"sum": sum(F(x) for x in g), "mean": pmean(g), "median": pmedian(g), "average": sum(F(x) * wv for x, wv in zip(g, wgi)) / sum(wgi), "min": min(g), "max": max(g)}
            for k, tv in chk.items():
                if np.ma.is_masked(got[k][gi]) or not close(got[k][gi], tv, 1e-12, 1e-9): okr[k] = False
            if len(g) > 1 and (np.ma.is_masked(got["var"][gi]) or not close(got["var"][gi], pvar(g, 1), 1e-10, 1e-9)): okr["var"] = False
            if np.ma.is_masked(got["std"][gi]) or not close(got["std"][gi], math.sqrt(pvar(g)), 1e-10, 1e-9): okr["std"] = False
            if got["count"][gi] != len(g): okr["count"] = False
report("MaskedArray.sum over the unmasked values (axis None/0/1, 60 random masks) == exact Fraction sum", okr["sum"])
report("mean == Fraction mean of the unmasked values", okr["mean"])
report("var(ddof=1) == unbiased variance of the unmasked values (n = unmasked count per slice)", okr["var"])
report("std == sqrt(population variance) of the unmasked values", okr["std"])
report("np.ma.median == median of the unmasked values (even counts average the two middle values)", okr["median"])
report("np.ma.average(weights=W) == sum(w x)/sum(w) over unmasked positions only", okr["average"])
report("min / max ignore masked values", okr["min"] and okr["max"])
report("count(axis) == number of unmasked entries", okr["count"])
report("fully masked slices give the masked constant for sum/mean/median/average/min/max", okr["allmasked"])
avw, sw_ = ma.average(ma.array([1.0, 2.0, 3.0, 4.0], mask=[0, 1, 0, 0]), weights=[1, 5, 2, 2], returned=True)
report("np.ma.average(returned=True): the weight sum counts only unmasked positions (1+2+2 = 5), average = (1 + 6 + 8)/5 = 3", float(sw_) == 5.0 and float(avw) == 3.0)
report("np.ma.median of even count [1,2,3,4] = 2.5; all-masked -> masked; per-row with different counts", float(ma.median(ma.array([1.0, 2, 3, 4]))) == 2.5
       and ma.median(ma.array([1, 2], mask=[1, 1])) is ma.masked and ma.median(ma.array([[1, 2, 3, 4], [5, 6, 7, 8]], mask=[[0, 0, 0, 1], [0, 1, 1, 0]]), axis=1).tolist() == [2.0, 6.5])
mi = ma.array([1, 2, 3, 4], mask=[0, 0, 1, 0], dtype=np.int32)
report("mean of an int32 masked array is float64 (7/3); var over the unmasked ints", mi.mean().dtype == np.float64 and close(mi.mean(), F(7, 3)) and close(mi.var(), pvar([1, 2, 4])))
report("prod ignores masked values; cumsum keeps the mask positions and skips masked values in the running total",
       int(ma.array([2, 3, 5], mask=[0, 1, 0]).prod()) == 10 and ma.array([1, 2, 3, 4], mask=[0, 1, 0, 0]).cumsum().filled(-1).tolist() == [1, -1, 4, 8])

print("---- np.ma: mask propagation, domains, fill values")
a1 = ma.array([1.0, 2.0, 3.0, 4.0], mask=[0, 1, 0, 0]); a2 = ma.array([1.0, 1.0, 0.0, 2.0], mask=[0, 0, 1, 0])
report("binary ops: result mask = union of the operand masks (+, *, **, comparisons)", all((op(a1, a2)).mask.tolist() == [False, True, True, False] for op in [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: x ** y, lambda x, y: x < y]))
with caught() as c:
    lg = ma.log(ma.array([-1.0, 0.0, 1.0, 2.0])); dv_ = ma.divide(ma.array([1.0, 1.0, 1.0]), ma.array([0.0, 2.0, 0.0])); sq = ma.sqrt(ma.array([-4.0, 4.0])); ac = ma.arccos(ma.array([2.0, 0.5]))
report("documented: ma.log([-1, 0, 1, 2]) masks the out-of-domain -1 and 0 and gives [--, --, 0.0, log 2]", lg.mask.tolist() == [True, True, False, False] and lg[3] == math.log(2) and lg[2] == 0.0)
report("ma.divide masks division by zero; ma.sqrt masks negatives; ma.arccos masks |x| > 1", dv_.mask.tolist() == [True, False, True] and dv_[1] == 0.5 and sq.mask.tolist() == [True, False] and ac.mask.tolist() == [True, False])
report("the np.ma domain functions raise no RuntimeWarning", "RuntimeWarning" not in c.names)
lg2 = np.log(ma.array([-1.0, 0.0, 1.0]))
report("np.log (plain ufunc) on a MaskedArray: 'entries of the output masked array are masked wherever ... the input fall outside the validity domain'", isinstance(lg2, ma.MaskedArray) and lg2.mask.tolist() == [True, True, False])
report("integer division by zero in np.ma masks the entry", ma.array([4, 5]) // ma.array([0, 2]) is not None and (ma.array([4, 5]) // ma.array([0, 2])).mask.tolist() == [True, False])
fv = {"bool": ma.array([True]).fill_value, "int": ma.array([1]).fill_value, "float": ma.array([1.0]).fill_value, "complex": ma.array([1j]).fill_value,
      "object": ma.array([1], dtype=object).fill_value, "U": ma.array(["a"]).fill_value, "S": ma.array([b"a"]).fill_value, "f4": ma.array([1.0], dtype=np.float32).fill_value}
report("default fill_value table: bool True, int 999999, float 1e20, complex 1e20+0j, object '?', string 'N/A'",
       fv["bool"] == True and fv["int"] == 999999 and fv["float"] == 1e20 and fv["complex"] == 1e20 + 0j and fv["object"] == "?" and fv["U"] == "N/A" and fv["S"] == b"N/A" and fv["f4"] == 1e20)
report("structured default fill value is per field ((999999, 1e20))", ma.array([(1, 2.0)], dtype=[("a", "i8"), ("b", "f8")]).fill_value.tolist() == (999999, 1e20))
i8f = ma.array([1, 2], mask=[0, 1], dtype=np.int8)
with caught() as c:
    try: i8filled = i8f.filled().tolist()
    except Exception as e: i8filled = type(e).__name__
print(f"   int8 masked array: fill_value {i8f.fill_value!r}, filled() -> {i8filled} (999999 does not fit int8; warnings {c.names})")
report("int8 masked array with the default fill value: filled() gives 999999 (the documented int default) or refuses, not a wrapped in-range value", i8filled != [1, 63], f"(filled() -> {i8filled})")
report("filled() uses fill_value; filled(0); compressed() returns the unmasked values in C order as 1-D",
       a1.filled().tolist() == [1.0, 1e20, 3.0, 4.0] and a1.filled(0).tolist() == [1.0, 0.0, 3.0, 4.0] and ma.array([[1, 2], [3, 4]], mask=[[0, 1], [1, 0]]).compressed().tolist() == [1, 4])
report("masked_where(cond, a) masks where cond; masked_invalid masks nan and +-inf", ma.masked_where(np.array([1, 5, 3]) > 2, [1, 5, 3]).mask.tolist() == [False, True, True]
       and ma.masked_invalid(np.array([1.0, np.nan, np.inf, -np.inf])).mask.tolist() == [False, True, True, True])
me = ma.masked_equal([1, 2, 1], 1)
report("masked_equal: masks x == value and sets fill_value to value (documented)", me.mask.tolist() == [True, False, True] and me.fill_value == 1)
mv = ma.masked_values([1.0, 1.1, 1.0000001, 2.0], 1.0)
report("masked_values uses isclose (rtol 1e-5, atol 1e-8): 1.0000001 masked, 1.1 not; fill_value set to value", mv.mask.tolist() == [True, False, True, False] and mv.fill_value == 1.0)
report("masked_inside is inclusive of both endpoints; masked_outside masks strictly outside", ma.masked_inside([1, 2, 3, 4], 2, 3).mask.tolist() == [False, True, True, False]
       and ma.masked_outside([1, 2, 3, 4], 2, 3).mask.tolist() == [True, False, False, True] and ma.masked_inside([1, 2, 3, 4], 3, 2).mask.tolist() == [False, True, True, False])
report("masked_greater / masked_less_equal", ma.masked_greater([1, 2, 3], 2).mask.tolist() == [False, False, True] and ma.masked_less_equal([1, 2, 3], 2).mask.tolist() == [True, True, False])

print("---- np.ma: cov / corrcoef")
xs_, ys_ = [rng.uniform(-5, 5) for _ in range(12)], [rng.uniform(-5, 5) for _ in range(12)]
mx_ = [rng.random() < 0.25 for _ in range(12)]; my_ = [rng.random() < 0.25 for _ in range(12)]
pairs_ = [(x, y) for x, y, a, b_ in zip(xs_, ys_, mx_, my_) if not a and not b_]
def pcov(pr):
    mx = pmean([p[0] for p in pr]); my = pmean([p[1] for p in pr]); return sum((F(a) - mx) * (F(b_) - my) for a, b_ in pr) / (len(pr) - 1)
cxy = ma.cov(ma.array(xs_, mask=mx_), ma.array(ys_, mask=my_))
report("ma.cov(x, y) with different masks: 'a common mask is allocated', each entry is the covariance over the jointly unmasked pairs",
       close(cxy[0, 1], pcov(pairs_), 1e-10) and close(cxy[0, 0], pcov([(a, a) for a, _ in pairs_]), 1e-10) and close(cxy[1, 1], pcov([(b_, b_) for _, b_ in pairs_]), 1e-10))
rxy = ma.corrcoef(ma.array(xs_, mask=mx_), ma.array(ys_, mask=my_))
report("ma.corrcoef(x, y) == Pearson r over the jointly unmasked pairs", close(rxy[0, 1], float(pcov(pairs_)) / math.sqrt(float(pcov([(a, a) for a, _ in pairs_]) * pcov([(b_, b_) for _, b_ in pairs_]))), 1e-10))
report("ma.cov with allow_masked=False and masked data raises ValueError", raises(lambda: ma.cov(ma.array(xs_, mask=mx_), allow_masked=False), ValueError) is not None)
X2 = ma.array([[1.0, 2, 3, 4, 5], [2, 1, 4, 3, 6]], mask=[[0, 0, 0, 0, 1], [1, 0, 0, 0, 0]])
c2 = ma.cov(X2)
pr01 = [(X2.data[0][k], X2.data[1][k]) for k in range(5) if not X2.mask[0][k] and not X2.mask[1][k]]
print(f"   ma.cov(2-row x, rows masked at different columns)[0,1] = {float(c2[0, 1])}; pairwise-complete covariance over columns 1..3 = {float(pcov(pr01))}")
report("ma.cov(2-D x) with different row masks: off-diagonal == covariance over the columns unmasked in both rows ('masked values are propagated pair-wise')", close(c2[0, 1], pcov(pr01), 1e-12))
Xc = ma.array([[4.0, -2, 4], [2, -3, 4]], mask=[[0, 0, 0], [1, 0, 0]]); rc = ma.corrcoef(Xc)
print(f"   ma.corrcoef([[4,-2,4],[--,-3,4]]) = {float(rc[0, 1])!r}; the two jointly observed columns (-2,-3),(4,4) have r = 1")
report("ma.corrcoef(2-D x) stays within [-1, 1] (a Pearson coefficient)", abs(float(rc[0, 1])) <= 1 + 1e-12)

print("---- np.ma: sort, argmax, unique, concatenate / stack, count")
sx = ma.array([3.0, 1.0, 2.0, 5.0, 0.5], mask=[0, 1, 0, 1, 0])
report("ma.sort puts masked values last (endwith=True default); endwith=False puts them first", ma.sort(sx).compressed().tolist() == [0.5, 2.0, 3.0] and ma.sort(sx).mask.tolist() == [False, False, False, True, True]
       and ma.sort(sx, endwith=False).mask.tolist() == [True, True, False, False, False])
report("argsort: masked entries last, unmasked in increasing order", sx.argsort().tolist()[:3] == [4, 2, 0] and set(sx.argsort().tolist()[3:]) == {1, 3})
report("argmax / argmin ignore masked values (masked max 5.0 at index 3 is skipped)", int(sx.argmax()) == 0 and int(sx.argmin()) == 4)
print(f"   all-masked argmax -> {ma.array([1, 2], mask=[1, 1]).argmax()} (fill with the minimum; undocumented result)")
uq = ma.unique(ma.array([1, 2, 5, 2, 4, 3], mask=[0, 0, 1, 0, 1, 0]))
report("np.ma.unique: 'Masked values are considered the same element (masked)' -> [1, 2, 3, --]", uq.compressed().tolist() == [1, 2, 3] and uq.mask.tolist() == [False, False, False, True])
ca = ma.concatenate([ma.array([1, 2], mask=[0, 1]), ma.array([3, 4], mask=[1, 0])])
report("ma.concatenate preserves the masks", ca.mask.tolist() == [False, True, True, False])
pc = np.concatenate([ma.array([1, 2], mask=[0, 1]), ma.array([3])])
report("np.concatenate on MaskedArrays returns a MaskedArray but 'the input masks are not preserved' (documented; use ma.concatenate)", isinstance(pc, ma.MaskedArray) and not pc.mask.any())
stk = ma.stack([ma.array([1, 2], mask=[0, 1]), ma.array([3, 4], mask=[1, 0])])
report("ma.stack / ma.vstack / ma.hstack / ma.column_stack preserve masks", stk.mask.tolist() == [[False, True], [True, False]] and ma.vstack([ma.array([1, 2], mask=[0, 1]), ma.array([3, 4])]).mask.tolist() == [[False, True], [False, False]]
       and ma.hstack([ma.array([1], mask=[1]), ma.array([2])]).mask.tolist() == [True, False] and ma.column_stack([ma.array([1, 2], mask=[1, 0]), ma.array([3, 4])]).mask.tolist() == [[True, False], [False, False]])
report("count() over all axes and count(axis=0)", ma.array([[1, 2], [3, 4]], mask=[[0, 1], [1, 1]]).count() == 1 and ma.array([[1, 2], [3, 4]], mask=[[0, 1], [1, 1]]).count(axis=0).tolist() == [1, 0])

print("---- np.ma: mask sharing, hard masks, polyfit")
x5 = ma.array([1, 2, 3, 4, 5], mask=[0, 1, 0, 0, 1]); mx5 = x5[:3]; mx5[1] = -1
report("documented slice example: assigning through a slice unmasks in the original (mask is a view): x.mask -> [F,F,F,F,T], x.data -> [1,-1,3,4,5]",
       x5.mask.tolist() == [False, False, False, False, True] and x5.data.tolist() == [1, -1, 3, 4, 5])
x6 = ma.array([1, 2, 3, 4], mask=[0, 0, 0, 1]); v6 = x6[1:3]; v6[0] = ma.masked
report("masking through a slice also propagates to the original (x[1] becomes masked)", x6.mask.tolist() == [False, True, False, True])
xh = ma.array([1, 2, 3], mask=[0, 0, 1], hard_mask=True); xh[-1] = 5
hard_ok = xh.mask.tolist() == [False, False, True]; xh.soften_mask(); xh[-1] = 5
report("hard mask: assignment to a masked entry silently keeps it masked; after soften_mask() it unmasks (documented example)", hard_ok and xh.tolist() == [1, 2, 5] and not xh.hardmask)
xh2 = ma.array([1, 2, 3], mask=[0, 0, 1]); xh2.harden_mask(); xh2[:] = 9
report("harden_mask(): a slice assignment writes only the unmasked entries", xh2.data.tolist() == [9, 9, 3] and xh2.mask.tolist() == [False, False, True])
xn = ma.array([1, 2, 3], mask=[0, 0, 1]); xn.mask = ma.nomask
report("assigning nomask to .mask unmasks everything", xn.mask.tolist() == [False, False, False] and xn.tolist() == [1, 2, 3])
xs2 = ma.array([1, 2, 3], mask=[0, 1, 0]); cp = ma.array(xs2, copy=True); cp[1] = 7
report("ma.array(x, copy=True) owns its mask: unmasking the copy leaves x masked", xs2.mask.tolist() == [False, True, False])
def lstsq_exact(xv, yv, deg):
    n = deg + 1
    A_ = [[sum(F(x) ** (i + j) for x in xv) for j in range(n)] for i in range(n)]; b_ = [sum(F(y) * F(x) ** i for x, y in zip(xv, yv)) for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A_[r][col] != 0); A_[col], A_[piv] = A_[piv], A_[col]; b_[col], b_[piv] = b_[piv], b_[col]
        for r in range(n):
            if r != col and A_[r][col] != 0:
                f_ = A_[r][col] / A_[col][col]; A_[r] = [a - f_ * c for a, c in zip(A_[r], A_[col])]; b_[r] -= f_ * b_[col]
    return [b_[i] / A_[i][i] for i in range(n)][::-1]
xp = [float(i) for i in range(15)]; yp = [2 + 0.5 * x - 0.1 * x * x + rng.uniform(-1, 1) for x in xp]
mxp = [i in (2, 7) for i in range(15)]; myp = [i in (4, 11, 12) for i in range(15)]
keep = [i for i in range(15) if not mxp[i] and not myp[i]]
cfp = ma.polyfit(ma.array(xp, mask=mxp), ma.array(yp, mask=myp), 2)
ce = lstsq_exact([xp[i] for i in keep], [yp[i] for i in keep], 2)
report("np.ma.polyfit: 'Any masked values in x is propagated in y, and vice-versa' -> equals the exact LS fit on the 10 jointly unmasked points", all(close(a, b_, 1e-9) for a, b_ in zip(cfp, ce)))
Y2 = ma.array(np.column_stack([yp, [2 * v for v in yp]]), mask=np.column_stack([myp, [False] * 15]))
cf2 = ma.polyfit(ma.array(xp, mask=mxp), Y2, 1)
keep2 = [i for i in range(15) if not mxp[i] and not myp[i]]
ce2 = lstsq_exact([xp[i] for i in keep2], [2 * yp[i] for i in keep2], 1)
print(f"   2-D y, mask only in column 0: column-1 coefficients {cf2[:, 1].tolist()} vs LS on rows kept by the union mask {[float(c) for c in ce2]}")
report("np.ma.polyfit with 2-D y: a row masked in any column is dropped for all columns (documented '2D y ... masked rows')", all(close(a, b_, 1e-9) for a, b_ in zip(cf2[:, 1], ce2)))
print("---- done")
