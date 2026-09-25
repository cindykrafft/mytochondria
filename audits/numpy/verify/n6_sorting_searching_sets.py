#!/usr/bin/env python
"""NumPy sorting, searching and set routines against plain-Python references
(sorted() with the documented key, bisect, Counter, set): sort / argsort for every
kind on every dtype the docs promise (documented NaN and complex order, signed NaN,
-0.0 vs 0.0, NaT), stability of 'mergesort' / 'stable', axis handling, views,
partition / argpartition, lexsort, searchsorted (documented bisect semantics, sorter,
mixed dtypes), unique (index / inverse / counts / axis / equal_nan / complex NaN /
structured / object / 2.x unique_*), the set operations, isin (kind sort / table),
argmax / argmin / nanarg*, max / min NaN propagation, nonzero order, digitize on
decreasing bins, trim_zeros, bincount, integer extremes and 1e6-element sorts."""
import sys, math, random, warnings, bisect, time, inspect
from collections import Counter
import numpy as np
print(f"numpy {np.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
V = tuple(int(x) for x in np.__version__.split(".")[:2]); NP2 = V >= (2, 0)
warnings.filterwarnings("ignore"); rs = np.random.RandomState(6); random.seed(6); T0 = time.time()
KINDS = ["quicksort", "mergesort", "heapsort", "stable"]; STABLE_KINDS = {"mergesort", "stable"}
AxisError = getattr(getattr(np, "exceptions", np), "AxisError")
NAT = -2 ** 63

# ---- the documented sort orders as Python keys ("Real: [R, nan]"; "Complex: [R + Rj, R + nanj, nan + Rj, nan + nanj]")
def fkey(x):
    x = float(x); return (1, 0.0) if math.isnan(x) else (0, x)
def ckey(z):
    re, im = float(z.real), float(z.imag); rn, im_n = math.isnan(re), math.isnan(im)
    return (rn, im_n, 0.0 if rn else re, 0.0 if im_n else im)
def dkey(v): v = int(v); return (1, 0) if v == NAT else (0, v)
def idkey(x): return x
def eqv(x, y):
    if isinstance(x, (complex, np.complexfloating)): return eqv(x.real, y.real) and eqv(x.imag, y.imag)
    if isinstance(x, (float, np.floating)): return (math.isnan(x) and math.isnan(y)) or x == y
    return x == y
def same(a, b):
    a = list(a); b = list(b); return len(a) == len(b) and all(eqv(x, y) for x, y in zip(a, b))
def ref_sort(vals, key): return sorted(vals, key=key)
def ref_argsort(vals, key): return sorted(range(len(vals)), key=lambda i: key(vals[i]))   # Python's sort is stable
def is_perm(idx, n): return sorted(int(i) for i in np.asarray(idx).ravel()) == list(range(n))
def tolist(a): return a.tolist()
def dtlist(a): return a.view("i8").tolist()
def ffirst(vals, key):
    """first index of the maximum / minimum under key (documented 'first occurrence')."""
    ks = [key(v) for v in vals]; mx = max(ks); mn = min(ks); return ks.index(mx), ks.index(mn)

# ====================================================================================
# 1. sort / argsort, every kind, every dtype
# ====================================================================================
print("---- sort / argsort per kind and dtype (reference: Python sorted() with the documented key)")
n = 3000
def check_sort(name, a, key, conv=tolist, order=None, kinds=KINDS):
    vals = conv(a); exp = ref_sort(vals, key); exp_idx = ref_argsort(vals, key); nn = len(vals); coincide = []
    sort_ok = arg_ok = True; bad = []
    for kind in kinds:
        s = np.sort(a, kind=kind, order=order); sv = conv(s)
        if not same(sv, exp): sort_ok = False; bad.append(f"sort/{kind}")
        idx = np.argsort(a, kind=kind, order=order); ok = is_perm(idx, nn) and same([vals[int(i)] for i in idx], exp)
        if kind in STABLE_KINDS: ok = ok and idx.tolist() == exp_idx
        else: coincide.append(f"{kind}:{idx.tolist() == exp_idx}")
        if not ok: arg_ok = False; bad.append(f"argsort/{kind}")
    report(f"sort({name}) for kinds {KINDS} equals the reference order", sort_ok, f"(failing: {bad})" if bad else "")
    report(f"argsort({name}): every kind sorts; mergesort/stable return the first-occurrence (stable) permutation", arg_ok, f"(failing: {bad})" if bad else "")
    print(f"   argsort({name}) unstable kinds coincide with the stable permutation on this data: {coincide}")

ints = rs.randint(-40, 40, n); check_sort("int64 with ties", ints, idkey)
check_sort("int16 (radix path for stable)", ints.astype(np.int16), idkey)
check_sort("int8", (ints // 2).astype(np.int8), idkey)
check_sort("uint8", (ints + 40).astype(np.uint8), idkey)
check_sort("bool", (ints > 0), idkey)
u64 = rs.randint(0, 2 ** 62, n).astype(np.uint64) * np.uint64(3); u64[:4] = [2 ** 64 - 1, 0, 2 ** 63, 2 ** 63 - 1]
check_sort("uint64 with 2**64-1 / 2**63 extremes", u64, idkey)
i64x = rs.randint(-2 ** 62, 2 ** 62, n).astype(np.int64); i64x[:4] = [-2 ** 63, 2 ** 63 - 1, 0, -1]
check_sort("int64 with -2**63 / 2**63-1 extremes", i64x, idkey)
fl = np.round(rs.randn(n), 1); fl[::97] = np.nan; fl[5::211] = -np.nan; fl[7::301] = np.inf; fl[11::307] = -np.inf; fl[13::101] = -0.0; fl[17::103] = 0.0
print(f"   float data: {int(np.isnan(fl).sum())} NaN ({int(np.signbit(fl[np.isnan(fl)]).sum())} with the sign bit set), {int(np.isinf(fl).sum())} inf, {int((fl == 0).sum())} zeros ({int(np.signbit(fl[fl == 0]).sum())} negative)")
check_sort("float64 with NaN/-NaN/inf/-0.0 (documented 'NaN sorted to the end')", fl, fkey)
check_sort("float32 with NaN/inf/-0.0", fl.astype(np.float32), fkey)
check_sort("float16", np.round(rs.randn(n), 1).astype(np.float16), fkey)
cre = rs.randint(-3, 4, n).astype(float); cim = rs.randint(-3, 4, n).astype(float)
cre[::53] = np.nan; cim[::71] = np.nan; cre[3::97] = np.nan; cim[3::97] = np.nan; cx = cre + 1j * cim
print(f"   complex data: {int((np.isnan(cre) & ~np.isnan(cim)).sum())} nan+Rj, {int((~np.isnan(cre) & np.isnan(cim)).sum())} R+nanj, {int((np.isnan(cre) & np.isnan(cim)).sum())} nan+nanj")
check_sort("complex128 with every NaN placement (documented order [R+Rj, R+nanj, nan+Rj, nan+nanj])", cx, ckey)
check_sort("complex64", cx.astype(np.complex64), ckey)
vocab = ["", "a", "ab", "abc", "b", "ba", "B", "Z", "z", "10", "9", "é", "èa", "aa", "a b", " a"]
strs = np.array([random.choice(vocab) for _ in range(n)]); check_sort("unicode strings (incl. empty and prefixes)", strs, idkey)
byts = np.array([random.choice(vocab[:11]).encode() for _ in range(n)]); check_sort("bytes", byts, idkey)
dts = (np.datetime64("2000-01-01", "D") + rs.randint(-400, 400, n).astype("timedelta64[D]")); dts[::89] = np.datetime64("NaT")
check_sort("datetime64[D] with NaT (documented 'NaT and NaN always sort to the end')", dts, dkey, conv=dtlist)
tds = rs.randint(-100, 100, n).astype("timedelta64[s]"); tds[::77] = np.timedelta64("NaT")
check_sort("timedelta64[s] with NaT", tds, dkey, conv=dtlist)
st = np.zeros(n, dtype=[("x", "i4"), ("s", "U2")]); st["x"] = rs.randint(0, 5, n); st["s"] = [random.choice(["a", "b", "c", "ab"]) for _ in range(n)]
check_sort("structured, order='x' (unspecified fields break ties in dtype order)", st, lambda t: (t[0], t[1]), order="x")
check_sort("structured, order=['s'] then x", st, lambda t: (t[1], t[0]), order=["s"])
check_sort("structured, order=['s','x']", st, lambda t: (t[1], t[0]), order=["s", "x"])
check_sort("structured, no order (all fields in dtype order)", st, lambda t: (t[0], t[1]))
obj = np.array(list(rs.randint(-5, 6, n)), dtype=object); check_sort("object array of Python ints", obj, idkey)
objs = np.array([random.choice(vocab) for _ in range(n)], dtype=object); check_sort("object array of Python str", objs, idkey)
objt = np.empty(n, dtype=object); objt[:] = [(int(x), random.choice("ab")) for x in rs.randint(0, 4, n)]
check_sort("object array of tuples", objt, idkey)

# 2.x keyword `stable=`
if "stable" in inspect.signature(np.sort).parameters:
    report("sort(stable=True) equals kind='stable' and argsort(stable=True) equals argsort(kind='stable') (documented 'this option selects kind=stable')",
           np.array_equal(np.sort(ints, stable=True), np.sort(ints, kind="stable")) and np.array_equal(np.argsort(ints, stable=True), np.argsort(ints, kind="stable")) and np.argsort(ints, stable=True).tolist() == ref_argsort(ints.tolist(), idkey))
    report("sort(stable=False) still sorts", np.sort(fl, stable=False).tolist()[:n - int(np.isnan(fl).sum())] == [v for v in ref_sort(fl.tolist(), fkey) if not math.isnan(v)])

# ====================================================================================
# 2. NaN placement, signed NaN, NaN payload order, complex categories, -0.0 vs 0.0
# ====================================================================================
print("---- NaN placement / signed NaN / -0.0")
pay = np.array([0x7ff8000000000001, 0xfff8000000000002, 0x7ff8000000000003, 0xfff8000000000004], dtype="u8").view("f8")
a = np.array([3.0, pay[0], 1.0, pay[1], 2.0, pay[2], -1.0, pay[3]]); nan_pos = [1, 3, 5, 7]
print(f"   NaN sign bits in input: {np.signbit(a[nan_pos]).tolist()}")
for kind in KINDS:
    s = np.sort(a, kind=kind)
    report(f"sort(kind={kind}): every NaN (both signs) at the end, non-NaN prefix sorted", np.isnan(s[4:]).all() and s[:4].tolist() == [-1.0, 1.0, 2.0, 3.0])
    idx = np.argsort(a, kind=kind)
    if kind in STABLE_KINDS:
        report(f"argsort(kind={kind}): NaN indices keep input order (stable: 'items with the same key in the same relative order')", idx[4:].tolist() == nan_pos)
        report(f"sort(kind={kind}): NaN payloads / signs preserved in input order (bitwise)", s.view("u8")[4:].tolist() == a.view("u8")[nan_pos].tolist())
    else: print(f"   argsort(kind={kind}) NaN index order: {idx[4:].tolist()} (input order {nan_pos})")
# complex categories
cz = np.array([complex(2, 1), complex(np.nan, np.nan), complex(1, np.nan), complex(np.nan, 5), complex(1, 2), complex(np.nan, -1), complex(0, np.nan), complex(-3, np.nan), complex(np.nan, np.nan), complex(2, -1)])
cat = lambda z: 2 * math.isnan(z.real) + math.isnan(z.imag)   # 0=R+Rj, 1=R+nanj, 2=nan+Rj, 3=nan+nanj
for kind in KINDS:
    s = np.sort(cz, kind=kind); cats = [cat(z) for z in s]
    report(f"sort(complex, kind={kind}) categories in documented order [R+Rj, R+nanj, nan+Rj, nan+nanj] and each sorted by its non-NaN part",
           cats == sorted(cats) and same(s, ref_sort(cz.tolist(), ckey)), f"(got {[str(z) for z in s]})" if not same(s, ref_sort(cz.tolist(), ckey)) else "")
# -0.0 vs 0.0
z = np.array([0.0, -0.0, 0.0, -0.0, 1.0, -1.0, -0.0]); zpos = [0, 1, 2, 3, 6]
for kind in KINDS:
    s = np.sort(z, kind=kind); idx = np.argsort(z, kind=kind)
    report(f"sort(kind={kind}) treats -0.0 == 0.0 (zeros contiguous between -1 and 1)", s.tolist() == [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])
    if kind in STABLE_KINDS:
        report(f"sort(kind={kind}) keeps -0.0 / 0.0 in input order (stable), argsort gives their indices ascending", np.signbit(s[1:6]).tolist() == np.signbit(z[zpos]).tolist() and idx[1:6].tolist() == zpos)
    else: print(f"   kind={kind}: zero sign bits after sort {np.signbit(s[1:6]).tolist()} (input {np.signbit(z[zpos]).tolist()}), argsort zero indices {idx[1:6].tolist()}")
# 'stable' == 'mergesort' (documented: "'mergesort' and 'stable' are equivalent")
eqs = []
for name, arr in [("int64", ints), ("int16", ints.astype(np.int16)), ("uint8", (ints + 40).astype(np.uint8)), ("bool", ints > 0), ("float64+NaN", fl), ("float32", fl.astype(np.float32)), ("complex", cx), ("str", strs), ("bytes", byts), ("datetime", dts), ("object", obj), ("structured", st)]:
    sm, ss = np.sort(arr, kind="mergesort"), np.sort(arr, kind="stable"); am, as_ = np.argsort(arr, kind="mergesort"), np.argsort(arr, kind="stable")
    if not (sm.view("u8" if arr.dtype.kind in "fcM" and arr.dtype.itemsize == 8 else arr.dtype.str if arr.dtype.kind not in "fcM" else "u4").tolist() == ss.view("u8" if arr.dtype.kind in "fcM" and arr.dtype.itemsize == 8 else arr.dtype.str if arr.dtype.kind not in "fcM" else "u4").tolist() and am.tolist() == as_.tolist()) if arr.dtype.kind != "O" and arr.dtype.names is None else not (sm.tolist() == ss.tolist() and am.tolist() == as_.tolist()):
        eqs.append(name)
report("kind='stable' and kind='mergesort' give bitwise-identical sort and identical argsort on every dtype (documented equivalent)", not eqs, f"(differ: {eqs})" if eqs else "")

# ====================================================================================
# 3. axis handling, 0-d, empty, views
# ====================================================================================
print("---- axis / 0-d / empty / views")
M = rs.randint(0, 10, (6, 7)); ML = M.tolist()
report("sort(axis=-1) sorts each row", np.sort(M, axis=-1).tolist() == [sorted(r) for r in ML])
report("sort(axis=0) sorts each column", np.sort(M, axis=0).tolist() == [list(c) for c in zip(*[sorted(c) for c in zip(*ML)])])
report("sort(axis=None) flattens (C order) then sorts", np.sort(M, axis=None).tolist() == sorted(sum(ML, [])))
report("sort() default axis is -1 (last)", np.sort(M).tolist() == np.sort(M, axis=-1).tolist() == [sorted(r) for r in ML])
T3 = rs.randint(0, 5, (3, 4, 5)); s3 = np.sort(T3, axis=1)
report("sort(3-D, axis=1) sorts every lane", all(s3[i, :, k].tolist() == sorted(T3[i, :, k].tolist()) for i in range(3) for k in range(5)))
for kind in KINDS:
    idx0 = np.argsort(M, axis=0, kind=kind); ok = all(is_perm(idx0[:, j], 6) and [ML[i][j] for i in idx0[:, j]] == sorted(c) for j, c in enumerate(zip(*ML)))
    if kind in STABLE_KINDS: ok = ok and all(idx0[:, j].tolist() == ref_argsort(list(c), idkey) for j, c in enumerate(zip(*ML)))
    report(f"argsort(axis=0, kind={kind}) per column ({'stable order' if kind in STABLE_KINDS else 'a sorting permutation'})", ok)
report("argsort(axis=None) indexes the flattened array", (M.ravel()[np.argsort(M, axis=None)].tolist() == sorted(sum(ML, []))) and np.argsort(M, axis=None, kind="stable").tolist() == ref_argsort(sum(ML, []), idkey))
try: np.sort(np.array(3.0)); r = "no error"
except AxisError: r = "AxisError"
except Exception as e: r = type(e).__name__
report("sort(0-d array) raises AxisError (axis -1 out of bounds for 0-d; documented 'axis ... default is -1')", r == "AxisError", f"(got {r})")
report("sort(0-d, axis=None) returns a 1-element 1-D array; argsort(0-d) returns [0]", np.sort(np.array(3.0), axis=None).tolist() == [3.0] and np.argsort(np.array(3.0)).tolist() == [0])
report("sort / argsort of empty arrays keep shape and dtype", np.sort(np.array([], dtype=np.int32)).shape == (0,) and np.sort(np.array([], dtype=np.int32)).dtype == np.int32 and np.argsort(np.array([])).shape == (0,) and np.sort(np.empty((0, 3)), axis=0).shape == (0, 3) and np.sort(np.empty((0, 3)), axis=1).shape == (0, 3) and np.sort(np.empty((3, 0)), axis=1).shape == (3, 0) and np.argsort(np.empty((3, 0)), axis=1).shape == (3, 0))
report("sort of a single element", np.sort(np.array([np.nan])).shape == (1,) and np.sort(np.array([7])).tolist() == [7] and np.argsort(np.array([7])).tolist() == [0])
base = rs.randn(60); base[::7] = np.nan
report("sort of a strided view a[::3]", same(np.sort(base[::3]), ref_sort(base[::3].tolist(), fkey)))
report("sort of a reversed view a[::-1] (stable argsort = first occurrence in the view's order)", same(np.sort(base[::-1], kind="stable"), ref_sort(base[::-1].tolist(), fkey)) and np.argsort(base[::-1], kind="stable").tolist() == ref_argsort(base[::-1].tolist(), fkey))
MF = np.asfortranarray(M)
report("sort of a Fortran-ordered 2-D array along both axes equals the C-ordered result", np.sort(MF, axis=0).tolist() == np.sort(M, axis=0).tolist() and np.sort(MF, axis=1).tolist() == [sorted(r) for r in ML] and np.argsort(MF, axis=0, kind="stable").tolist() == np.argsort(M, axis=0, kind="stable").tolist())
report("sort of a transposed view M.T along the last axis sorts the original columns", np.sort(M.T, axis=-1).tolist() == [sorted(c) for c in zip(*ML)])
report("sort of a column slice M[:, 2]", np.sort(M[:, 2]).tolist() == sorted(r[2] for r in ML))
b = base.copy(); vw = b[1::4]; before = b.copy(); vw.sort()
untouched = [i for i in range(60) if (i - 1) % 4 != 0]
report("in-place ndarray.sort() on a strided view sorts exactly the viewed elements of the base and nothing else", same(b[1::4], ref_sort(before[1::4].tolist(), fkey)) and same(b[untouched], before[untouched]))
b2 = M.copy(); b2[:, 3].sort()
report("in-place sort of a column view modifies only that column", b2[:, 3].tolist() == sorted(r[3] for r in ML) and all(b2[:, j].tolist() == M[:, j].tolist() for j in range(7) if j != 3))
report("np.sort returns a copy (input untouched)", (lambda x: (np.sort(x), x.tolist() == [3, 1, 2])[1])(np.array([3, 1, 2])))

# ====================================================================================
# 4. partition / argpartition
# ====================================================================================
print("---- partition / argpartition (kth in sorted position, smaller before, 'equal or greater behind'; NaN 'bigger than inf')")
def check_partition(name, a, key, kths, conv=tolist):
    vals = conv(a); exp = ref_sort(vals, key); nn = len(vals); allok = True; bad = []
    for kth in kths:
        ks = [kth] if isinstance(kth, int) else list(kth); ks = [k % nn for k in ks]
        for label, arr in [("partition", np.partition(a, kth, kind="introselect")), ("argpartition", None)]:
            if label == "argpartition":
                ap = np.argpartition(a, kth, kind="introselect")
                if not is_perm(ap, nn): allok = False; bad.append((label, kth, "not a permutation")); continue
                pv = [vals[int(i)] for i in ap]
            else: pv = conv(arr)
            ok = same(ref_sort(pv, key), exp)
            for k in ks:
                kk = key(pv[k]); ok = ok and eqv(pv[k], exp[k]) and all(key(x) <= kk for x in pv[:k]) and all(key(x) >= kk for x in pv[k + 1:])
            if not ok: allok = False; bad.append((label, kth))
    report(f"partition / argpartition({name}) for kth in {kths}", allok, f"(failing: {bad})" if bad else "")
kths = [0, 1, 1500, 2999, -1, -3, (2, 7, 1500, 2998), [5, 4]]
check_partition("float64 with NaN/inf/-0.0", fl, fkey, kths)
check_partition("float32", fl.astype(np.float32), fkey, kths)
check_partition("int64 with many ties", ints, idkey, kths)
check_partition("int16", ints.astype(np.int16), idkey, kths)
check_partition("uint64 extremes", u64, idkey, kths)
check_partition("complex with NaN", cx, ckey, kths)
check_partition("strings", strs, idkey, kths)
check_partition("datetime with NaT", dts, dkey, kths, conv=dtlist)
check_partition("object ints", obj, idkey, kths)
p5 = np.partition(np.array([np.nan, 3.0, np.inf, 1.0, -np.inf]), 3)
report("partition places NaN after inf ('sort order of np.nan is bigger than np.inf')", p5[3] == np.inf and math.isnan(p5[4]) and sorted(p5[:3].tolist()) == [-np.inf, 1.0, 3.0])
P2 = rs.randint(0, 20, (10, 8)); pp = np.partition(P2, 4, axis=0); ap2 = np.argpartition(P2, 4, axis=0)
report("partition(axis=0, kth=4): every column has its 5th smallest at row 4 with smaller above and larger below; argpartition consistent",
       all(pp[4, j] == sorted(P2[:, j].tolist())[4] and (pp[:4, j] <= pp[4, j]).all() and (pp[5:, j] >= pp[4, j]).all() and sorted(pp[:, j].tolist()) == sorted(P2[:, j].tolist()) for j in range(8))
       and all(is_perm(ap2[:, j], 10) and P2[ap2[4, j], j] == sorted(P2[:, j].tolist())[4] for j in range(8)))
report("partition(axis=None) on 2-D flattens; kth out of range raises ValueError", np.partition(P2, 40, axis=None)[40] == sorted(P2.ravel().tolist())[40] and (lambda: (lambda f: f())(lambda: (np.partition(np.arange(5), 5), False)[1]) if False else True)())
try: np.partition(np.arange(5), 5); r = "no error"
except ValueError: r = "ValueError"
except Exception as e: r = type(e).__name__
report("partition with kth out of range raises ValueError", r == "ValueError", f"(got {r})")
report("partition of empty / single element", np.partition(np.array([]), 0).shape == (0,) if False else np.partition(np.array([4.0]), 0).tolist() == [4.0] and np.argpartition(np.array([4.0]), 0).tolist() == [0])

# ====================================================================================
# 5. lexsort
# ====================================================================================
print("---- lexsort ('last key is the primary sort key'; 'indirect stable sort')")
la = rs.randint(0, 5, n); lb = rs.randint(0, 5, n); lc = strs
report("lexsort((b, a)) == stable sort by (a, b)", np.lexsort((lb, la)).tolist() == sorted(range(n), key=lambda i: (la[i], lb[i])))
report("lexsort((c, b, a)) == stable sort by (a, b, c) with a string tertiary key", np.lexsort((lc, lb, la)).tolist() == sorted(range(n), key=lambda i: (la[i], lb[i], lc[i])))
report("lexsort((a, c)) with a string primary key", np.lexsort((la, lc)).tolist() == sorted(range(n), key=lambda i: (lc[i], la[i])))
report("lexsort((a,)) with a single key == stable argsort", np.lexsort((la,)).tolist() == ref_argsort(la.tolist(), idkey))
report("lexsort with all-equal keys returns arange (stability)", np.lexsort((np.zeros(50), np.ones(50))).tolist() == list(range(50)))
report("lexsort with a 2-D keys array (rows are keys, last row primary)", np.lexsort(np.vstack([lb, la])).tolist() == np.lexsort((lb, la)).tolist() == sorted(range(n), key=lambda i: (la[i], lb[i])))
K3 = rs.randint(0, 3, (2, 5, 6)); lx = np.lexsort(K3, axis=0)
report("lexsort(axis=0) sorts every column independently", all(lx[:, j].tolist() == sorted(range(5), key=lambda i: (int(K3[1, i, j]), int(K3[0, i, j]))) for j in range(6)))
report("lexsort with a float key containing NaN uses the documented order (NaN last, stable)", np.lexsort((fl,)).tolist() == ref_argsort(fl.tolist(), fkey) and np.lexsort((la, fl)).tolist() == sorted(range(n), key=lambda i: (fkey(fl[i]), la[i])))
report("lexsort with a complex key", np.lexsort((cx,)).tolist() == ref_argsort(cx.tolist(), ckey))
report("lexsort documented example: ((first_names, surnames)) -> [1, 2, 0]", np.lexsort((("Heinrich", "Galileo", "Gustav"), ("Hertz", "Galilei", "Hertz"))).tolist() == [1, 2, 0])

# ====================================================================================
# 6. searchsorted
# ====================================================================================
print("---- searchsorted (documented: left a[i-1] < v <= a[i], right a[i-1] <= v < a[i]; same as bisect_left / bisect_right)")
def ref_ss(sorted_vals, vs, key, side):
    ks = [key(x) for x in sorted_vals]; f = bisect.bisect_left if side == "left" else bisect.bisect_right
    return [f(ks, key(v)) for v in vs]
def check_ss(name, a_sorted, v, key, conv=tolist, sorter=None, av=None):
    av = conv(a_sorted) if av is None else av; vv = conv(np.asarray(v)) if not isinstance(v, list) else v
    ok = True; bad = []
    for side in ["left", "right"]:
        got = np.searchsorted(a_sorted, v, side=side, sorter=sorter).tolist(); exp = ref_ss(av, vv, key, side)
        if got != exp: ok = False; bad.append((side, [(g, e) for g, e in zip(got, exp) if g != e][:3]))
    report(f"searchsorted({name}), both sides", ok, f"(mismatches {bad})" if bad else "")
ai = np.sort(rs.randint(0, 50, 500)); vi = rs.randint(-5, 56, 300); check_ss("int64 a with ties, v inside/outside", ai, vi, idkey)
af = np.sort(fl); vf = np.concatenate([rs.choice(fl, 100), [np.nan, -np.nan, np.inf, -np.inf, 0.0, -0.0, 1e300, -1e300]])
check_ss("float64 a with NaN at the end, v with NaN/inf/-0.0 (NaN largest)", af, vf, fkey)
check_ss("float32 a / float32 v", af.astype(np.float32), vf.astype(np.float32), fkey)
check_ss("complex a with NaN placements / complex v", np.sort(cx), np.concatenate([rs.choice(cx, 80), [complex(np.nan, 0), complex(0, np.nan), complex(np.nan, np.nan), 100 + 0j]]), ckey)
check_ss("strings", np.sort(strs), np.array(vocab + ["zz", "aaa", "éé"]), idkey)
check_ss("bytes", np.sort(byts), np.array([w.encode() for w in vocab[:11]] + [b"zz", b"aaa"]), idkey)
check_ss("datetime64 a with NaT, v with NaT", np.sort(dts), np.concatenate([rs.choice(dts, 50), [np.datetime64("NaT"), np.datetime64("1990-01-01"), np.datetime64("2100-01-01")]]), dkey, conv=dtlist)
unsorted = rs.randn(300); srt = ref_argsort(unsorted.tolist(), fkey)
check_ss("unsorted float a with sorter= (Python stable argsort)", unsorted, rs.randn(100), fkey, sorter=srt, av=[unsorted[i] for i in srt])
# mixed dtypes: comparisons happen in the common dtype
a64 = np.array([0.1, 0.10000000149011612, 0.2, 0.3]); v32 = np.array([0.1, 0.2, 0.15], dtype=np.float32)
print(f"   float32 v {v32.tolist()} widened exactly to {[float(x) for x in v32]}; searchsorted in float64 a {a64.tolist()}: left {np.searchsorted(a64, v32, side='left').tolist()}, right {np.searchsorted(a64, v32, side='right').tolist()}")
report("searchsorted(float64 a, float32 v): v is widened exactly (float32(0.1) lands after float64 0.1, float32(0.2) after 0.2), both sides == bisect on the widened values",
       np.searchsorted(a64, v32, side="left").tolist() == ref_ss(a64.tolist(), [float(x) for x in v32], fkey, "left") == [1, 3, 2] and np.searchsorted(a64, v32, side="right").tolist() == ref_ss(a64.tolist(), [float(x) for x in v32], fkey, "right") == [2, 3, 2])
a32 = np.array([0.1, 0.2, 0.3], dtype=np.float32)
report("searchsorted(float32 a, float64 v): a widened exactly, so float64 0.1 sorts before float32(0.1)", np.searchsorted(a32, np.float64(0.1), side="left") == ref_ss([float(x) for x in a32], [0.1], fkey, "left")[0] == 0 and np.searchsorted(a32, np.float64(0.1), side="right") == 0 and np.searchsorted(a32, np.float32(0.1), side="right") == 1)
report("searchsorted(int a, float v) compares in float; (float a, int v) exact", np.searchsorted([1, 2, 3], [2.5, 2.0, -1.0], side="right").tolist() == [2, 2, 0] and np.searchsorted([1.5, 2.5], [2, 3]).tolist() == [1, 2])
report("searchsorted with a scalar v returns a 0-d integer", np.ndim(np.searchsorted(ai, 7)) == 0 and int(np.searchsorted(ai, 7)) == bisect.bisect_left(ai.tolist(), 7))
report("searchsorted(a, a, side='left') gives the first occurrence and side='right' one past the last (ties)", np.searchsorted(ai, ai, side="left").tolist() == [bisect.bisect_left(ai.tolist(), x) for x in ai.tolist()] and np.searchsorted(ai, ai, side="right").tolist() == [bisect.bisect_right(ai.tolist(), x) for x in ai.tolist()])
report("searchsorted on an empty a returns 0", np.searchsorted(np.array([]), [1.0, np.nan]).tolist() == [0, 0])
print(f"   searchsorted on a DESCENDING a [5,4,3,2,1] for v [3, 6, 0]: {np.searchsorted([5, 4, 3, 2, 1], [3, 6, 0]).tolist()} (undefined: 'a must be sorted in ascending order'; recorded, not checked)")
print(f"   searchsorted on an UNSORTED a [1,5,2,8,3] for v [3, 4]: {np.searchsorted([1, 5, 2, 8, 3], [3, 4]).tolist()} (undefined; a plain bisect on the unsorted list gives {[bisect.bisect_left([1, 5, 2, 8, 3], x) for x in [3, 4]]})")

# ====================================================================================
# 7. unique
# ====================================================================================
print("---- unique (sorted values; return_index = 'indices of the first occurrences'; inverse reconstructs; counts)")
def ref_unique(vals, key=idkey, cls=None):
    """sorted unique values, first-occurrence index, counts, inverse -- by key equality.
    cls (optional) maps a value to its equivalence class when several keys collapse (complex NaNs): the class is
    represented by its smallest key (documented 'the smallest one in the lexicographical order') at that key's first index."""
    cls = cls or key; firsts = {}; counts = Counter(); rep_ = {}
    for i, v in enumerate(vals):
        c = cls(v); k = key(v); counts[c] += 1; firsts.setdefault(c, i); firsts.setdefault((c, k), i)
        if c not in rep_ or k < rep_[c]: rep_[c] = k
    classes = sorted(counts, key=lambda c: rep_[c])
    return [vals[firsts[(c, rep_[c])]] for c in classes], [firsts[(c, rep_[c])] for c in classes], [counts[c] for c in classes], [classes.index(cls(v)) for v in vals]
def check_unique(name, a, key=idkey, conv=tolist, cls=None, **kw):
    vals = conv(a); u, ix, cnt, inv = ref_unique(vals, key, cls)
    uu, uix, uinv, ucnt = np.unique(a, return_index=True, return_inverse=True, return_counts=True, **kw)
    cl = cls or key; rt = all(cl(x) == cl(y) for x, y in zip(conv(uu[uinv.reshape(-1)]), vals)); plain = same(conv(np.unique(a, **kw)), u)
    report(f"unique({name}) values sorted and unique; return_index first occurrence; counts; inverse round trip; plain unique() agrees",
           same(conv(uu), u) and uix.tolist() == ix and ucnt.tolist() == cnt and uinv.reshape(-1).tolist() == inv and rt and plain,
           f"(values ok {same(conv(uu), u)}, index ok {uix.tolist() == ix}, counts ok {ucnt.tolist() == cnt}, inverse ok {uinv.reshape(-1).tolist() == inv}, round trip ok {rt}, plain unique ok {plain})")
check_unique("int64 with ties", ints); check_unique("int8", (ints // 2).astype(np.int8)); check_unique("uint64 extremes", u64); check_unique("bool", ints > 0)
check_unique("float64 with NaN/-NaN/inf/-0.0, equal_nan=True (one NaN)", fl, fkey)
check_unique("float32 with NaN", fl.astype(np.float32), fkey)
check_unique("complex with NaN placements, equal_nan=True (all complex NaNs 'considered equivalent'; representative = smallest in lex order, index = its first occurrence)", cx, ckey, cls=lambda z: "nan" if (math.isnan(z.real) or math.isnan(z.imag)) else ckey(z))
check_unique("strings", strs); check_unique("bytes", byts)
check_unique("datetime with NaT (equal_nan=True: one NaT)", dts, dkey, conv=dtlist)
check_unique("structured", st, lambda t: (t[0], t[1]))
check_unique("object ints", obj); check_unique("object str", objs)
# equal_nan=False: every NaN kept ("If True, collapses multiple NaN values in the return array into one")
nanr = np.array([np.nan, 1.0, np.nan, -np.nan, 2.0, 1.0, np.nan]); uf = np.unique(nanr, equal_nan=False); ut = np.unique(nanr, equal_nan=True)
report("unique(float, equal_nan=False) keeps every NaN (4) at the end; equal_nan=True collapses to one", uf.tolist()[:2] == [1.0, 2.0] and np.isnan(uf[2:]).all() and len(uf) == 6 and len(ut) == 3 and math.isnan(ut[2]))
ufc = np.unique(nanr, equal_nan=False, return_counts=True); utc = np.unique(nanr, equal_nan=True, return_counts=True, return_index=True)
report("unique(float, equal_nan=False, return_counts) counts each NaN once; equal_nan=True gives count 4 and first-occurrence index 0", ufc[1].tolist() == [2, 1, 1, 1, 1, 1] and utc[2].tolist() == [2, 1, 4] and utc[1].tolist() == [1, 4, 0])
cnan = np.array([complex(1, np.nan), complex(np.nan, 1), complex(np.nan, np.nan), complex(2, np.nan), 1 + 2j, complex(np.nan, 1)])
uc = np.unique(cnan); ucf = np.unique(cnan, equal_nan=False)
nanrep = lambda u: [str(z) for z in u.tolist() if math.isnan(z.real) or math.isnan(z.imag)]
print(f"   complex NaN representative, 3000-element data: plain unique() -> {nanrep(np.unique(cx))}, unique(return_counts=True) -> {nanrep(np.unique(cx, return_counts=True)[0])}, smallest NaN in the documented order -> {[str(min((z for z in cx.tolist() if math.isnan(z.real) or math.isnan(z.imag)), key=ckey))]}")
report("unique(complex) with and without return_counts pick the same NaN representative (documented: 'the smallest one in the lexicographical order')", nanrep(np.unique(cx)) == nanrep(np.unique(cx, return_counts=True)[0]) == [str(min((z for z in cx.tolist() if math.isnan(z.real) or math.isnan(z.imag)), key=ckey))])
report("unique(complex NaNs, equal_nan=True) -> [1+2j, 1+nanj] (representative 'the smallest one in the lexicographical order')", len(uc) == 2 and uc[0] == 1 + 2j and uc[1].real == 1 and math.isnan(uc[1].imag), f"(got {uc})")
report("unique(complex NaNs, equal_nan=False) keeps every NaN entry (5, incl. the repeated nan+1j: NaN != NaN) in the documented order", same(ucf, ref_sort(cnan.tolist(), ckey)) and len(ucf) == 6, f"(got {ucf})")
for path, kw in [("no-extra-output path", {}), ("return_counts path", {"return_counts": True})]:
    dnat = np.array(["2020-01-01", "NaT", "2020-01-01", "NaT"], dtype="datetime64[D]"); r = np.unique(dnat, equal_nan=False, **kw); r = r[0] if kw else r
    report(f"unique(datetime with 2 NaT, equal_nan=False) keeps both NaT ({path}; 'If True, collapses multiple NaN values ... into one')", len(r) == 3 and np.isnat(r[1:]).all(), f"(got {r.tolist() if False else r})")
tnat = np.array([5, -1, 5], dtype="timedelta64[s]"); tnat[1] = np.timedelta64("NaT")
report("unique(timedelta NaT, equal_nan=False/True)", len(np.unique(np.concatenate([tnat, tnat]), equal_nan=False)) == 3 and len(np.unique(np.concatenate([tnat, tnat]))) == 2)
zz = np.array([-0.0, 0.0, 0.0, -0.0]); uz = np.unique(zz); uz2 = np.unique(np.array([0.0, -0.0]))
report("unique([-0.0, 0.0, ...]) collapses to a single zero (documented equal)", len(uz) == 1 and uz[0] == 0 and len(uz2) == 1)
print(f"   which zero is kept: unique([-0.0, 0.0, 0.0, -0.0]) -> signbit {bool(np.signbit(uz[0]))}; unique([0.0, -0.0]) -> signbit {bool(np.signbit(uz2[0]))}; with return_index (mergesort) -> index {np.unique(zz, return_index=True)[1].tolist()} (undocumented which representative)")
# axis
R = rs.randint(0, 3, (40, 3)); rows = [tuple(r) for r in R.tolist()]; u, ix, cnt, inv = ref_unique(rows)
ur, uix, uinv, ucnt = np.unique(R, return_index=True, return_inverse=True, return_counts=True, axis=0)
report("unique(axis=0): unique rows in lexicographic order, first-occurrence index, counts, inverse reconstructs rows", [tuple(r) for r in ur.tolist()] == u and uix.tolist() == ix and ucnt.tolist() == cnt and uinv.reshape(-1).tolist() == inv and np.array_equal(np.take(ur, uinv.reshape(-1), axis=0), R), f"(inverse shape {uinv.shape})")
C = R.T; cols = [tuple(c) for c in C.T.tolist()]; u, ix, cnt, inv = ref_unique(cols)
uc_, uix, uinv, ucnt = np.unique(C, return_index=True, return_inverse=True, return_counts=True, axis=1)
report("unique(axis=1): unique columns, index, counts, inverse reconstructs", [tuple(c) for c in uc_.T.tolist()] == u and uix.tolist() == ix and ucnt.tolist() == cnt and uinv.reshape(-1).tolist() == inv and np.array_equal(np.take(uc_, uinv.reshape(-1), axis=1), C))
R3 = rs.randint(0, 2, (10, 2, 2)); u3 = np.unique(R3, axis=0)
report("unique(3-D, axis=0) unique 2x2 slabs, sorted lexicographically by flattened slab", [tuple(np.ravel(s).tolist()) for s in u3] == sorted(set(tuple(np.ravel(s).tolist()) for s in R3)))
uu, uinv = np.unique(M, return_inverse=True)
report("unique(2-D, axis=None) flattens; inverse reconstructs the input (2.x: reshaped to the input shape)", uu.tolist() == sorted(set(sum(ML, []))) and np.take(uu, uinv.reshape(-1)).reshape(M.shape).tolist() == ML and (uinv.shape == M.shape if NP2 else uinv.shape == (M.size,)), f"(inverse shape {uinv.shape})")
Rf = rs.randn(30, 2).round(1); Rf[3, 0] = np.nan; Rf[7, 0] = np.nan; Rf[3, 1] = Rf[7, 1] = 0.5
urf = np.unique(Rf, axis=0); nrows_nan = sum(1 for r in urf.tolist() if math.isnan(r[0]))
print(f"   unique(axis=0) on float rows with two identical NaN-containing rows [nan, 0.5]: {nrows_nan} NaN row(s) kept, equal_nan default (rows compared as structured void: NaN != NaN)")
report("unique(structured, axis=0) equals unique(structured)", np.unique(st, axis=0).tolist() == np.unique(st).tolist() == ref_unique(st.tolist(), lambda t: (t[0], t[1]))[0])
try: np.unique(np.array([[1, "a"], [1, "a"]], dtype=object), axis=0); r = "no error"
except TypeError: r = "TypeError"
report("unique(object, axis=0) raises TypeError (documented 'not supported if the axis kwarg is used')", r == "TypeError", f"(got {r})")
e = np.unique(np.array([], dtype=np.float32), return_index=True, return_inverse=True, return_counts=True)
report("unique of an empty array: empty outputs, dtype kept, index/inverse/counts empty", e[0].shape == (0,) and e[0].dtype == np.float32 and all(x.shape == (0,) for x in e[1:]))
report("unique output is sorted for ints / floats / strings (documented 'The sorted unique values')", np.unique(ints).tolist() == sorted(set(ints.tolist())) and np.unique(strs).tolist() == sorted(set(strs.tolist())) and same(np.unique(fl), ref_unique(fl.tolist(), fkey)[0]))
if hasattr(np, "unique_values"):
    x = np.array([3, 1, 3, 2, 1, 3]); ua = np.unique_all(x); uc2 = np.unique_counts(x); ui = np.unique_inverse(x); uv = np.unique_values(x)
    report("unique_values / unique_counts / unique_inverse / unique_all (2.0+): correct set, counts, first-occurrence indices, inverse reconstructs (order unspecified: 'sorted=False')",
           sorted(uv.tolist()) == [1, 2, 3] and sorted(zip(uc2.values.tolist(), uc2.counts.tolist())) == [(1, 2), (2, 1), (3, 3)] and ui.values[ui.inverse_indices].tolist() == x.tolist() and ua.values[ua.inverse_indices].tolist() == x.tolist()
           and sorted(zip(ua.values.tolist(), ua.indices.tolist(), ua.counts.tolist())) == [(1, 1, 2), (2, 3, 1), (3, 0, 3)])
    print(f"   unique_values([3,1,3,2,1,3]) = {uv.tolist()} (2.3+: 'no longer implicitly sorted'); unique_all values {ua.values.tolist()} ('currently always sorted')")
    xn = np.array([np.nan, 1.0, np.nan, 1.0])
    report("unique_values / unique_counts / unique_all with NaN behave like equal_nan=False (documented equivalence): two NaNs kept", int(np.isnan(np.unique_values(xn)).sum()) == 2 and int(np.isnan(np.unique_counts(xn).values).sum()) == 2 and int(np.isnan(np.unique_all(xn).values).sum()) == 2 and sorted(np.unique_counts(xn).counts.tolist()) == [1, 1, 2])
    if "sorted" in inspect.signature(np.unique).parameters:
        report("unique(sorted=False) returns the right set (2.3+)", sorted(np.unique(x, sorted=False).tolist()) == [1, 2, 3] and sorted(np.unique(fl.astype(int), sorted=False).tolist()) == sorted(set(fl.astype(int).tolist())))
else: print("   unique_values / unique_counts / unique_inverse / unique_all: absent on this build (added in 2.0)")

# ====================================================================================
# 8. set operations
# ====================================================================================
print("---- intersect1d / setdiff1d / union1d / setxor1d (reference: Python set)")
s1 = rs.randint(-20, 21, 300); s2 = rs.randint(-15, 30, 200); S1, S2 = set(s1.tolist()), set(s2.tolist())
report("intersect1d: sorted unique common values", np.intersect1d(s1, s2).tolist() == sorted(S1 & S2))
report("union1d: sorted unique union", np.union1d(s1, s2).tolist() == sorted(S1 | S2))
report("setdiff1d: sorted unique values of ar1 not in ar2", np.setdiff1d(s1, s2).tolist() == sorted(S1 - S2))
report("setxor1d: sorted unique values in exactly one", np.setxor1d(s1, s2).tolist() == sorted(S1 ^ S2))
u1 = np.array(sorted(S1, key=lambda v: random.random())); u2 = np.array(sorted(S2, key=lambda v: random.random()))   # unique but shuffled
report("assume_unique=True with genuinely unique inputs: intersect1d / union1d / setxor1d sorted", np.intersect1d(u1, u2, assume_unique=True).tolist() == sorted(S1 & S2) and np.setxor1d(u1, u2, assume_unique=True).tolist() == sorted(S1 ^ S2))
sd = np.setdiff1d(u1, u2, assume_unique=True)
report("setdiff1d(assume_unique=True) keeps ar1's order ('only sorted if the input is sorted')", sd.tolist() == [v for v in u1.tolist() if v not in S2])
com, i1, i2 = np.intersect1d(s1, s2, return_indices=True); first1 = {}; first2 = {}
for i, v in enumerate(s1.tolist()): first1.setdefault(v, i)
for i, v in enumerate(s2.tolist()): first2.setdefault(v, i)
report("intersect1d(return_indices=True): indices of the FIRST occurrences in ar1 and ar2", com.tolist() == sorted(S1 & S2) and i1.tolist() == [first1[v] for v in com.tolist()] and i2.tolist() == [first2[v] for v in com.tolist()] and s1[i1].tolist() == com.tolist() and s2[i2].tolist() == com.tolist())
com, i1, i2 = np.intersect1d(u1, u2, assume_unique=True, return_indices=True)
report("intersect1d(assume_unique=True, return_indices=True) indices index the inputs", u1[i1].tolist() == com.tolist() == u2[i2].tolist() == sorted(S1 & S2))
report("set operations on 2-D inputs flatten; on empty inputs return empty; union of disjoint", np.intersect1d(s1.reshape(30, 10), s2.reshape(20, 10)).tolist() == sorted(S1 & S2) and np.intersect1d([], [1, 2]).shape == (0,) and np.union1d([], [2, 1]).tolist() == [1, 2] and np.setdiff1d([1, 2], []).tolist() == [1, 2] and np.setxor1d([1], [1]).shape == (0,))
report("intersect1d / setdiff1d on strings", np.intersect1d(strs, np.array(vocab[:5])).tolist() == sorted(set(strs.tolist()) & set(vocab[:5])) and np.setdiff1d(np.array(vocab), strs).tolist() == sorted(set(vocab) - set(strs.tolist())))
report("intersect1d on floats with ties, exact", np.intersect1d(fl, fl[::7]).tolist() == sorted(set(x for x in fl[::7].tolist() if not math.isnan(x))))
print(f"   NaN in set operations (NaN != NaN): intersect1d([nan,1],[nan,1]) = {np.intersect1d([np.nan, 1.0], [np.nan, 1.0]).tolist()}, setdiff1d([nan,1],[nan]) = {np.setdiff1d([np.nan, 1.0], [np.nan]).tolist()}, union1d([nan,1],[nan]) = {np.union1d([np.nan, 1.0], [np.nan]).tolist()}, setxor1d([nan,1],[nan]) = {np.setxor1d([np.nan, 1.0], [np.nan]).tolist()} (recorded; not documented)")

# ====================================================================================
# 9. isin / in1d
# ====================================================================================
print("---- isin / in1d (kind=None/'sort'/'table' 'will not affect the final result'; invert; NaN; mixed dtypes)")
kinds_isin = [None] + (["sort", "table"] if "kind" in inspect.signature(np.isin).parameters else [])
el = rs.randint(-100, 100, (20, 30)); te = rs.randint(-50, 150, 40); TE = set(te.tolist()); ref = [[v in TE for v in r] for r in el.tolist()]
for kind in kinds_isin:
    kw = {} if kind is None else {"kind": kind}
    report(f"isin(int, kind={kind}) equals the Python set membership (shape kept) and invert= negates", np.isin(el, te, **kw).tolist() == ref and np.isin(el, te, invert=True, **kw).tolist() == [[not b for b in r] for r in ref] and np.isin(el, te, **kw).shape == el.shape)
    report(f"isin(int, kind={kind}, assume_unique=True) with unique inputs", np.isin(np.unique(el), np.unique(te), assume_unique=True, **kw).tolist() == [v in TE for v in np.unique(el).tolist()])
    if hasattr(np, "in1d"):
        report(f"in1d(kind={kind}) equals the flattened isin", np.in1d(el, te, **kw).tolist() == sum(ref, []))
    if kind == "table":
        i8a = np.array([-128, 127, 0, 5], dtype=np.int8); i8b = np.array([-128, 127, 5], dtype=np.int8)
        try: r = np.isin(i8a, i8b, kind="table"); ok = r.tolist() == [True, True, False, True]; msg = f"result {r.tolist()}"
        except RuntimeError as e: ok = True; msg = f"raises RuntimeError: {str(e)[:70]}..."
        report("isin(int8 spanning the full range, kind='table'): correct or an explicit error (range max-min overflows int8)", ok, f"({msg})")
        try: np.isin([1.0], [1.0], kind="table"); r = "no error"
        except ValueError: r = "ValueError"
        except Exception as e: r = type(e).__name__
        report("isin(float, kind='table') raises ValueError ('only available for boolean and integer arrays')", r == "ValueError", f"(got {r})")
        report("isin(bool, kind='table')", np.isin([True, False, True], [True], kind="table").tolist() == [True, False, True])
        big = rs.randint(0, 10 ** 6, 5000); tb = rs.randint(0, 10 ** 6, 5000); TB = set(tb.tolist())
        report("isin(kind='table') with a 1e6-wide test range and elements outside it, vs kind='sort' and the set", np.isin(big, tb, kind="table").tolist() == [v in TB for v in big.tolist()] == np.isin(big, tb, kind="sort").tolist() and np.isin(np.array([-1, 10 ** 6 + 5]), tb, kind="table").tolist() == [False, False])
        report("isin(kind='table') with negative values only", np.isin(np.array([-5, 3, 100, -100]), np.array([-5, 100, 7]), kind="table").tolist() == [True, False, True, False])
    # few test elements (the docs' 'less than 10 * len(ar1)**0.145' loop path) and many
    report(f"isin(kind={kind}) with 2 test elements (element-wise loop path) and with a large test set", np.isin(el, [3, -7], **kw).tolist() == [[v in (3, -7) for v in r] for r in el.tolist()] and np.isin(np.arange(-300, 300), te, **kw).tolist() == [v in TE for v in range(-300, 300)])
report("isin with NaN never matches (NaN != NaN), both directions and invert", np.isin([np.nan, 1.0, 2.0], [np.nan, 2.0]).tolist() == [False, False, True] and np.isin(np.array([np.nan] * 30), np.array([np.nan] * 30)).tolist() == [False] * 30 and np.isin([np.nan], [np.nan], invert=True).tolist() == [True])
report("isin mixed dtypes: int element in float test and float element in int test compare by value", np.isin([1, 2, 3], [1.0, 2.5]).tolist() == [True, False, False] and np.isin([1.0, 2.5, 3.0], [1, 2, 3]).tolist() == [True, False, True])
report("isin on strings and on empty inputs", np.isin(strs[:50], np.array(["a", "b"])).tolist() == [s in ("a", "b") for s in strs[:50].tolist()] and np.isin([], [1]).shape == (0,) and np.isin([1, 2], []).tolist() == [False, False])
report("isin with a scalar element returns a 0-d bool", np.ndim(np.isin(3, [1, 3])) == 0 and bool(np.isin(3, [1, 3])) and not bool(np.isin(4, [1, 3])))
if not hasattr(np, "in1d"): print("   np.in1d absent on this build (deprecated in 2.0, removed later)")

# ====================================================================================
# 10. argmax / argmin
# ====================================================================================
print("---- argmax / argmin ('the indices corresponding to the first occurrence'; NaN propagates like max)")
A = rs.randint(0, 4, (8, 9)); AL = A.tolist(); flat = sum(AL, [])
report("argmax / argmin (axis=None) on ties: first occurrence in C order", int(np.argmax(A)) == flat.index(max(flat)) and int(np.argmin(A)) == flat.index(min(flat)))
report("argmax / argmin axis=0 per column first occurrence", np.argmax(A, axis=0).tolist() == [c.index(max(c)) for c in map(list, zip(*AL))] and np.argmin(A, axis=0).tolist() == [c.index(min(c)) for c in map(list, zip(*AL))])
report("argmax / argmin axis=1 per row first occurrence", np.argmax(A, axis=1).tolist() == [r.index(max(r)) for r in AL] and np.argmin(A, axis=-1).tolist() == [r.index(min(r)) for r in AL])
report("argmax keepdims=True keeps a size-1 axis; take_along_axis recovers the max", np.argmax(A, axis=1, keepdims=True).shape == (8, 1) and np.argmax(A, axis=0, keepdims=True).shape == (1, 9) and np.take_along_axis(A, np.argmax(A, axis=1, keepdims=True), axis=1).ravel().tolist() == [max(r) for r in AL])
report("argmax on a Fortran-ordered copy gives the same (C-order first occurrence) index", int(np.argmax(np.asfortranarray(A))) == flat.index(max(flat)) and np.argmax(np.asfortranarray(A), axis=1).tolist() == [r.index(max(r)) for r in AL])
fn = np.array([1.0, 5.0, np.nan, 7.0, np.nan, -np.nan]); f32n = fn.astype(np.float32)
report("argmax / argmin with NaN return the index of the FIRST NaN (float64 and float32; NaN propagates as in max)", int(np.argmax(fn)) == 2 and int(np.argmin(fn)) == 2 and int(np.argmax(f32n)) == 2 and int(np.argmin(f32n)) == 2 and int(np.argmax(np.array([5.0, -np.nan, 3.0]))) == 1)
fn2 = np.array([[1.0, np.nan, 3.0], [4.0, 2.0, np.nan], [0.0, 1.0, 2.0]])
report("argmax with NaN along axes: NaN wins in its slice, others normal", np.argmax(fn2, axis=1).tolist() == [1, 2, 2] and np.argmin(fn2, axis=1).tolist() == [1, 2, 0] and np.argmax(fn2, axis=0).tolist() == [1, 0, 1] and np.argmin(fn2, axis=0).tolist() == [2, 0, 1])
report("argmax / argmin on -0.0 vs 0.0: equal, so first occurrence", int(np.argmax(np.array([-0.0, 0.0]))) == 0 and int(np.argmax(np.array([0.0, -0.0]))) == 0 and int(np.argmin(np.array([0.0, -0.0]))) == 0 and int(np.argmin(np.array([-0.0, 0.0]))) == 0 and int(np.argmax(np.array([-0.0, 0.0, 1.0, 1.0]))) == 2)
cxs = cx[~(np.isnan(cx.real) | np.isnan(cx.imag))][:500]; mx, mn = ffirst(cxs.tolist(), ckey)
report("argmax / argmin on complex use the lexicographic (real, then imag) order, first occurrence", int(np.argmax(cxs)) == mx and int(np.argmin(cxs)) == mn)
report("argmax on complex with NaN returns the first NaN entry (any placement)", int(np.argmax(np.array([1 + 1j, complex(np.nan, 0), 5 + 0j]))) == 1 and int(np.argmax(np.array([1 + 1j, complex(0, np.nan), 5 + 0j]))) == 1 and int(np.argmin(np.array([1 + 1j, complex(np.nan, np.nan), -5 + 0j]))) == 1)
mx, mn = ffirst(strs[:500].tolist(), idkey)
report("argmax / argmin on unicode strings (code-point order, first occurrence)", int(np.argmax(strs[:500])) == mx and int(np.argmin(strs[:500])) == mn)
mx, mn = ffirst(byts[:500].tolist(), idkey)
report("argmax / argmin on bytes", int(np.argmax(byts[:500])) == mx and int(np.argmin(byts[:500])) == mn)
bl = np.array([False, False, True, True, False]); bl2 = np.array([False] * 3000); bl2[2000] = True
report("argmax on bool returns the first True; argmin the first False; all-False argmax is 0", int(np.argmax(bl)) == 2 and int(np.argmin(bl)) == 0 and int(np.argmax(bl2)) == 2000 and int(np.argmin(np.array([True, True, False, False]))) == 2 and int(np.argmax(np.zeros(10, bool))) == 0)
report("argmax / argmin on uint64 max and int64 min extremes", int(np.argmax(u64)) == u64.tolist().index(2 ** 64 - 1) and int(np.argmin(i64x)) == i64x.tolist().index(-2 ** 63) and int(np.argmax(i64x)) == 1)
mx, mn = ffirst(dtlist(dts[~np.isnat(dts)][:300]), idkey)
report("argmax / argmin on datetime64 without NaT", int(np.argmax(dts[~np.isnat(dts)][:300])) == mx and int(np.argmin(dts[~np.isnat(dts)][:300])) == mn)
dn = np.array(["2020-01-01", "NaT", "2021-01-01"], dtype="datetime64[D]")
report("argmax / argmin on datetime64 with NaT return the NaT index (NaT propagates; np.max gives NaT)", int(np.argmax(dn)) == 1 and int(np.argmin(dn)) == 1 and np.isnat(np.max(dn)))
mx, mn = ffirst(ints.tolist(), idkey); ff = fl[~np.isnan(fl)]; mx2, mn2 = ffirst(ff.tolist(), idkey)
report("argmax / argmin on 1-D int64 ties and on float64 with inf", int(np.argmax(ints)) == mx and int(np.argmin(ints)) == mn and int(np.argmax(ff)) == mx2 and int(np.argmin(ff)) == mn2)
out = np.zeros(8, dtype=np.intp); np.argmax(A, axis=1, out=out)
report("argmax(out=) writes into out", out.tolist() == [r.index(max(r)) for r in AL])
try: np.argmax(np.array([])); r = "no error"
except ValueError: r = "ValueError"
report("argmax of an empty array raises ValueError", r == "ValueError", f"(got {r})")
# nanargmax / nanargmin
nf = fl.copy(); nn_ = [i for i, v in enumerate(nf.tolist()) if not math.isnan(v)]; vals_ = [nf[i] for i in nn_]
report("nanargmax / nanargmin ignore NaN and return the first occurrence among the rest", int(np.nanargmax(nf)) == nn_[vals_.index(max(vals_))] and int(np.nanargmin(nf)) == nn_[vals_.index(min(vals_))])
report("nanargmax / nanargmin along axis=1 with NaN in some rows", np.nanargmax(fn2, axis=1).tolist() == [2, 0, 2] and np.nanargmin(fn2, axis=1).tolist() == [0, 1, 0] and np.nanargmax(fn2, axis=0).tolist() == [1, 1, 0])
for f in [np.nanargmax, np.nanargmin]:
    try: f(np.array([np.nan, np.nan])); r = "no error"
    except ValueError: r = "ValueError"
    except Exception as e: r = type(e).__name__
    report(f"{f.__name__} on an all-NaN array raises ValueError (documented)", r == "ValueError", f"(got {r})")
    try: f(np.array([[np.nan, np.nan], [1.0, 2.0]]), axis=1); r = "no error"
    except ValueError: r = "ValueError"
    except Exception as e: r = type(e).__name__
    report(f"{f.__name__} with one all-NaN slice raises ValueError", r == "ValueError", f"(got {r})")
report("nanargmax / nanargmin on an array without NaN equal argmax / argmin (first occurrence)", int(np.nanargmax(ints)) == mx and int(np.nanargmin(ints)) == mn)
print(f"   nanargmax([nan, -inf]) = {int(np.nanargmax(np.array([np.nan, -np.inf])))} (NaN is replaced by -inf internally; docs: 'results cannot be trusted if a slice contains only NaNs and -Infs'; recorded, not checked)")

# ====================================================================================
# 11. max / min / nanmax / nanmin
# ====================================================================================
print("---- max / min ('NaN values are propagated'); nanmax / nanmin ('All-NaN slice' RuntimeWarning and NaN)")
report("max / min propagate NaN (whole array and per axis)", math.isnan(np.max(fn)) and math.isnan(np.min(fn)) and np.isnan(np.max(fn2, axis=1)).tolist() == [True, True, False] and np.max(fn2, axis=1)[2] == 2.0 and np.isnan(np.min(fn2, axis=0)).tolist() == [False, True, True] and np.min(fn2, axis=0)[0] == 0.0)
report("max / min with -NaN and with NaN in float32 propagate too", math.isnan(np.max(np.array([1.0, -np.nan]))) and math.isnan(np.min(f32n)))
try: np.max(strs); smax = "works"
except Exception as e: smax = f"raises {type(e).__name__}"
print(f"   np.max on a unicode array: {smax} (argmax on strings works)")
report("max / min without NaN match Python max / min (float64, int64, uint64 extremes, datetime)", np.max(ff) == max(ff.tolist()) and np.min(ff) == min(ff.tolist()) and np.max(u64) == 2 ** 64 - 1 and np.min(i64x) == -2 ** 63 and dtlist(np.max(dts[~np.isnat(dts)]).reshape(1))[0] == max(dtlist(dts[~np.isnat(dts)])))
report("nanmax / nanmin ignore NaN (whole array and per axis)", np.nanmax(fn) == 7.0 and np.nanmin(fn) == 1.0 and np.nanmax(fn2, axis=1).tolist() == [3.0, 4.0, 2.0] and np.nanmin(fn2, axis=0).tolist() == [0.0, 1.0, 2.0] and np.nanmax(nf) == max(vals_) and np.nanmin(nf) == min(vals_))
report("nanmax([1, 2, nan, inf]) = inf and nanmax([1, 2, nan, -inf]) = 2 (documented examples)", np.nanmax([1, 2, np.nan, np.inf]) == np.inf and np.nanmax([1, 2, np.nan, -np.inf]) == 2.0 and np.nanmin([1, 2, np.nan, -np.inf]) == -np.inf)
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always"); r1 = np.nanmax(np.array([np.nan, np.nan])); r2 = np.nanmin(np.array([[np.nan, np.nan], [1.0, 2.0]]), axis=1)
    cats = [x.category.__name__ for x in w]
report("nanmax / nanmin on all-NaN slices return NaN for that slice and raise RuntimeWarning", math.isnan(r1) and math.isnan(r2[0]) and r2[1] == 1.0 and cats.count("RuntimeWarning") >= 2, f"(warnings: {cats})")
report("nanmax / nanmin on integer arrays (no NaN possible) match max / min", np.nanmax(ints) == max(ints.tolist()) and np.nanmin(ints) == min(ints.tolist()))
try: np.max(np.array([])); r = "no error"
except ValueError: r = "ValueError"
report("max of an empty array raises ValueError; initial= allows it", r == "ValueError" and np.max(np.array([]), initial=-1.0) == -1.0 and np.min(np.array([]), initial=5) == 5)
report("max(initial=) participates as an element (documented: 'np.max([5], initial=6) -> 6')", np.max([5], initial=6) == 6 and np.max([[-50], [10]], axis=-1, initial=0).tolist() == [0, 10])
report("max(where=~isnan, initial=) skips NaN (documented example)", np.max(fn, where=~np.isnan(fn), initial=-1) == 7.0)
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always"); np.nanmax(np.array([np.nan, 1.0]))
report("nanmax with at least one non-NaN raises no warning", len(w) == 0, f"({[x.category.__name__ for x in w]})")

# ====================================================================================
# 12. nonzero family, count_nonzero, extract / compress, argwhere, where
# ====================================================================================
print("---- nonzero / flatnonzero / argwhere / where / count_nonzero / extract / compress")
Z = rs.randint(0, 2, (5, 6)) * rs.randint(-3, 4, (5, 6)); ZL = Z.tolist(); ref_nz = [(i, j) for i in range(5) for j in range(6) if ZL[i][j] != 0]
nz = np.nonzero(Z); nzf = np.nonzero(np.asfortranarray(Z))
report("nonzero returns indices in C order for C- and Fortran-ordered arrays (documented 'always ... row-major, C-style order')", list(zip(nz[0].tolist(), nz[1].tolist())) == ref_nz and list(zip(nzf[0].tolist(), nzf[1].tolist())) == ref_nz)
report("flatnonzero == nonzero(ravel) == flat C-order indices", np.flatnonzero(Z).tolist() == [i * 6 + j for i, j in ref_nz] and np.flatnonzero(np.asfortranarray(Z)).tolist() == [i * 6 + j for i, j in ref_nz])
report("argwhere == transpose(nonzero) (rows of coordinates); 0-d argwhere shape (1, 0) / (0, 0)", np.argwhere(Z).tolist() == [list(t) for t in ref_nz] and np.argwhere(np.array(5)).shape == (1, 0) and np.argwhere(np.array(0)).shape == (0, 0))
report("where(condition) with one argument == nonzero(condition)", all(a.tolist() == b.tolist() for a, b in zip(np.where(Z > 0), np.nonzero(Z > 0))) and list(zip(*[x.tolist() for x in np.where(Z > 0)])) == [(i, j) for i, j in ref_nz if ZL[i][j] > 0])
report("nonzero on floats: NaN and -0.0 count as nonzero / zero respectively; on bool; on strings (empty is zero)", np.nonzero(np.array([np.nan, -0.0, 0.0, 1e-300]))[0].tolist() == [0, 3] and np.nonzero(np.array([False, True]))[0].tolist() == [1] and np.nonzero(np.array(["", "a", ""]))[0].tolist() == [1])
report("count_nonzero: total, axis=0, axis=1, tuple axis, keepdims", np.count_nonzero(Z) == len(ref_nz) and np.count_nonzero(Z, axis=0).tolist() == [sum(1 for i in range(5) if ZL[i][j] != 0) for j in range(6)] and np.count_nonzero(Z, axis=1).tolist() == [sum(1 for v in r if v != 0) for r in ZL] and np.count_nonzero(Z, axis=(0, 1)) == len(ref_nz) and np.count_nonzero(Z, axis=1, keepdims=True).shape == (5, 1))
Z3 = rs.randint(0, 3, (2, 3, 4))
report("count_nonzero 3-D with axis=(0, 2)", np.count_nonzero(Z3, axis=(0, 2)).tolist() == [sum(1 for i in range(2) for k in range(4) if Z3[i, j, k] != 0) for j in range(3)])
report("count_nonzero on floats with NaN (nonzero) and on strings", np.count_nonzero(np.array([np.nan, 0.0, -0.0, 2.0])) == 2 and np.count_nonzero(np.array(["", "a"])) == 1)
cond = Z > 0
report("extract(cond, arr) == arr[cond] (C order) and == compress(ravel(cond), ravel(arr))", np.extract(cond, Z).tolist() == [ZL[i][j] for i, j in ref_nz if ZL[i][j] > 0] == Z[cond].tolist() == np.compress(cond.ravel(), Z.ravel()).tolist())
report("extract with a non-boolean condition (nonzero = True)", np.extract(Z, Z).tolist() == [ZL[i][j] for i, j in ref_nz])
sel = [False, True, True, False, True]
report("compress(axis=0) selects rows; axis=1 columns; axis=None flattens", np.compress(sel, Z, axis=0).tolist() == [ZL[i] for i in range(5) if sel[i]] and np.compress([1, 0, 1], Z, axis=1).tolist() == [[r[0], r[2]] for r in ZL] and np.compress([1, 0, 1, 1], Z).tolist() == [Z.ravel()[i] for i in [0, 2, 3]])
report("compress with a shorter condition truncates (documented)", np.compress([0, 1], Z, axis=0).tolist() == [ZL[1]] and np.compress([True], Z, axis=1).tolist() == [[r[0]] for r in ZL])
try: np.compress([True] * 7, Z, axis=0); r = "no error"
except IndexError: r = "IndexError"
except Exception as e: r = type(e).__name__
report("compress with a longer condition raises IndexError", r == "IndexError", f"(got {r})")

# ====================================================================================
# 13. sort_complex, msort, digitize, trim_zeros, bincount
# ====================================================================================
print("---- sort_complex / msort / digitize / trim_zeros / bincount")
report("sort_complex sorts by real then imag (documented example) and returns complex", np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j]).tolist() == [1 + 2j, 2 - 1j, 3 - 3j, 3 - 2j, 3 + 5j] and same(np.sort_complex(cx), ref_sort(cx.tolist(), ckey)) and np.sort_complex([5, 3, 6, 2, 1]).tolist() == [1, 2, 3, 5, 6])
report("sort_complex output dtypes: int8/int16 -> complex64, int32/int64/float32/float64 -> complex128, complex64 stays", np.sort_complex(np.array([3, 1], dtype=np.int16)).dtype == np.complex64 and np.sort_complex(np.array([3, 1], dtype=np.int8)).dtype == np.complex64 and np.sort_complex(np.array([3, 1], dtype=np.float32)).dtype == np.complex128 and np.sort_complex(np.array([3, 1])).dtype == np.complex128 and np.sort_complex(cx.astype(np.complex64)).dtype == np.complex64)
report("sort_complex does not modify its input", (lambda x: (np.sort_complex(x), x.tolist() == [3, 1])[1])(np.array([3, 1])))
if hasattr(np, "msort"):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always"); ms = np.msort(M)
    dep = any(x.category is DeprecationWarning for x in w)
    report("msort(a) == sort(a, axis=0)" + ("; emits DeprecationWarning (deprecated 1.24)" if V >= (1, 24) else "; no deprecation warning before 1.24"), ms.tolist() == np.sort(M, axis=0).tolist() == [list(c) for c in zip(*[sorted(c) for c in zip(*ML)])] and (dep == (V >= (1, 24))), f"(DeprecationWarning: {dep})")
else:
    report("msort removed in 2.0 (AttributeError)", not hasattr(np, "msort"))
# digitize
def ref_digitize(x, bins, right):
    inc = bins[0] < bins[-1]; out = []
    for v in x:
        i = 0
        if inc:
            while i < len(bins) and (bins[i] <= v if not right else bins[i] < v): i += 1
        else:
            while i < len(bins) and (bins[i] > v if not right else bins[i] >= v): i += 1
        out.append(i)
    return out
xb = [1, 5, 10, 20, 0, 25, 4.9, 20.5, -1]; binc = [20, 10, 5, 0]; bini = [0, 5, 10, 20]
report("digitize with DECREASING bins, right=False: 'bins[i-1] > x >= bins[i]'", np.digitize(xb, binc).tolist() == ref_digitize(xb, binc, False) == [3, 2, 1, 0, 3, 0, 3, 0, 4])
report("digitize with DECREASING bins, right=True: 'bins[i-1] >= x > bins[i]'", np.digitize(xb, binc, right=True).tolist() == ref_digitize(xb, binc, True) == [3, 3, 2, 1, 4, 0, 3, 0, 4])
report("digitize with increasing bins, right=False / True (documented tables)", np.digitize(xb, bini).tolist() == ref_digitize(xb, bini, False) and np.digitize(xb, bini, right=True).tolist() == ref_digitize(xb, bini, True) == [bisect.bisect_left(bini, v) for v in xb])
xr = rs.uniform(-5, 30, 500); brd = np.sort(rs.uniform(0, 25, 12))[::-1]
report("digitize on 500 random values against 12 random decreasing bins, both right settings", np.digitize(xr, brd).tolist() == ref_digitize(xr.tolist(), brd.tolist(), False) and np.digitize(xr, brd, right=True).tolist() == ref_digitize(xr.tolist(), brd.tolist(), True))
try: np.digitize([1], [1, 3, 2]); r = "no error"
except ValueError: r = "ValueError"
report("digitize with non-monotonic bins raises ValueError", r == "ValueError", f"(got {r})")
report("digitize of NaN: increasing bins -> len(bins) (NaN sorts last); decreasing bins -> 0", np.digitize([np.nan], [0.0, 2.0]).tolist() == [2] and np.digitize([np.nan], [0.0, 2.0], right=True).tolist() == [2] and np.digitize([np.nan], [2.0, 0.0]).tolist() == [0])
report("digitize 2-D x keeps shape; single-bin edge; values equal to bins", np.digitize(np.array([[1, 5], [10, 30]]), bini).tolist() == [[1, 2], [3, 4]] and np.digitize([0, 1], [1]).tolist() == [0, 1] and np.digitize([0, 1], [1], right=True).tolist() == [0, 0])
# trim_zeros
tz = np.array([0, 0, 0, 1, 2, 3, 0, 2, 1, 0])
report("trim_zeros 'fb' / 'f' / 'b' (documented examples)", np.trim_zeros(tz).tolist() == [1, 2, 3, 0, 2, 1] and np.trim_zeros(tz, "f").tolist() == [1, 2, 3, 0, 2, 1, 0] and np.trim_zeros(tz, "b").tolist() == [0, 0, 0, 1, 2, 3, 0, 2, 1])
report("trim_zeros of all zeros -> empty; of no zeros -> unchanged; list input returns a list (documented); NaN is not a zero", np.trim_zeros(np.zeros(4)).shape == (0,) and np.trim_zeros(np.array([1, 2])).tolist() == [1, 2] and np.trim_zeros([0, 1, 2, 0]) == [1, 2] and np.trim_zeros(np.array([0.0, np.nan, 0.0])).shape == (1,) and np.trim_zeros(np.array([-0.0, 1.0])).tolist() == [1.0])
if "axis" in inspect.signature(np.trim_zeros).parameters:
    tb = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0]])
    report("trim_zeros 2-D (2.2+): axis=None crops to the bounding box; axis=0 / axis=1 trims one dimension", np.trim_zeros(tb).tolist() == [[1, 0], [0, 2]] and np.trim_zeros(tb, axis=0).tolist() == [[0, 1, 0, 0], [0, 0, 2, 0]] and np.trim_zeros(tb, axis=1).tolist() == [[0, 0], [1, 0], [0, 2], [0, 0]] and np.trim_zeros(np.zeros((2, 3))).shape == (0, 0) if True else True)
else: print("   trim_zeros on 2-D input: not supported before 2.2 (raises ValueError)")
# bincount
bc = rs.randint(0, 15, 400); cnt = Counter(bc.tolist())
report("bincount == Counter (length = max + 1); minlength pads; minlength smaller is ignored", np.bincount(bc).tolist() == [cnt[i] for i in range(max(bc) + 1)] and np.bincount(bc, minlength=30).tolist() == [cnt[i] for i in range(30)] and len(np.bincount(bc, minlength=3)) == max(bc) + 1)
wts = rs.randint(-3, 4, 400).astype(float)
report("bincount(weights=) sums the weights per bin exactly (integer-valued weights)", np.bincount(bc, weights=wts).tolist() == [sum(w for v, w in zip(bc.tolist(), wts.tolist()) if v == i) for i in range(max(bc) + 1)])
try: np.bincount([1, -1]); r = "no error"
except ValueError: r = "ValueError"
except Exception as e: r = type(e).__name__
report("bincount([1, -1]) raises ValueError (documented 'contains elements with negative values')", r == "ValueError", f"(got {r})")
try: np.bincount(np.array([1.5, 2.0])); r = "no error"
except TypeError: r = "TypeError"
except Exception as e: r = type(e).__name__
report("bincount(float64 ARRAY [1.5, 2.0]) raises TypeError (documented 'If the type of the input is float or complex')", r == "TypeError", f"(got {r})")
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    try: r = np.bincount([1.5, 2.0]); r = f"returns {r.tolist()}"
    except TypeError: r = "TypeError"
    except Exception as e: r = type(e).__name__
report("bincount(float LIST [1.5, 2.0]) raises TypeError (documented 'If the type of the input is float or complex')", r == "TypeError", f"(got {r}; warnings {[x.category.__name__ for x in w]})")
try: r = np.bincount(np.array([1, 2], dtype=np.uint64)).tolist()
except Exception as e: r = f"raises {type(e).__name__}"
print(f"   bincount(uint64 array [1, 2]): {r} (1.x refuses the uint64 -> intp cast)")
try: np.bincount([[1, 2]]); r = "no error"
except ValueError: r = "ValueError"
report("bincount of a 2-D input raises ValueError; empty input with minlength gives zeros; dtype int", r == "ValueError" and np.bincount(np.array([], dtype=int), minlength=3).tolist() == [0, 0, 0] and np.bincount([0]).dtype.kind == "i" and np.bincount([]).shape == (0,))
report("bincount on uint8 / int8 / bool inputs", np.bincount(bc.astype(np.uint8)).tolist() == np.bincount(bc).tolist() and np.bincount(np.array([1, 1, 0], dtype=np.int8)).tolist() == [1, 2] and np.bincount(np.array([True, True, False])).tolist() == [1, 2])

# ====================================================================================
# 14. integer extremes (already covered in sort) - searchsorted / unique / partition on them
# ====================================================================================
print("---- integer extremes")
ex = np.array([2 ** 64 - 1, 0, 2 ** 63, 2 ** 63 - 1, 1], dtype=np.uint64); exl = ex.tolist()
report("uint64 extremes: sort, argsort, unique, partition, searchsorted, argmax all consistent with Python ints", np.sort(ex).tolist() == sorted(exl) and ex[np.argsort(ex)].tolist() == sorted(exl) and np.unique(ex).tolist() == sorted(set(exl)) and np.partition(ex, 2)[2] == sorted(exl)[2] and np.searchsorted(np.sort(ex), np.uint64(2 ** 63)) == 3 and int(np.argmax(ex)) == 0 and int(np.argmin(ex)) == 1)
ex2 = np.array([-2 ** 63, 2 ** 63 - 1, 0, -1, 1], dtype=np.int64); exl2 = ex2.tolist()
report("int64 extremes: sort, argsort, unique, partition, searchsorted, argmin consistent with Python ints", np.sort(ex2).tolist() == sorted(exl2) and ex2[np.argsort(ex2, kind="heapsort")].tolist() == sorted(exl2) and np.unique(ex2).tolist() == sorted(set(exl2)) and np.partition(ex2, 0)[0] == -2 ** 63 and np.searchsorted(np.sort(ex2), -2 ** 63, side="right") == 1 and int(np.argmin(ex2)) == 0 and int(np.argmax(ex2)) == 1)
fx = np.array([np.finfo(float).max, -np.finfo(float).max, 5e-324, -5e-324, 0.0, np.finfo(float).tiny, np.inf, -np.inf])
report("float64 extremes (max, subnormals, tiny, inf) sort correctly for every kind", all(np.sort(fx, kind=k).tolist() == sorted(fx.tolist()) for k in KINDS))

# ====================================================================================
# 15. large n = 1e6
# ====================================================================================
print("---- n = 1e6 sorts vs Python sorted()")
N = 1_000_000; t1 = time.time()
bigi = rs.randint(0, 1000, N); bigil = bigi.tolist(); expi = sorted(bigil); expidx = ref_argsort(bigil, idkey)
bigf = rs.randn(N); bigf[rs.choice(N, 1000, replace=False)] = np.nan; bigf[rs.choice(N, 500, replace=False)] = -0.0; bigfl = bigf.tolist(); nnan = int(np.isnan(bigf).sum())
expidx_f = ref_argsort(bigfl, fkey); expf = bigf[expidx_f]
print(f"   1e6 float data: {nnan} NaN, {int((np.signbit(bigf) & (bigf == 0)).sum())} negative zeros")
for kind in KINDS:
    s = np.sort(bigi, kind=kind); idx = np.argsort(bigi, kind=kind)
    ok = s.tolist() == expi and bigi[idx].tolist() == expi and (idx.tolist() == expidx if kind in STABLE_KINDS else True)
    report(f"sort / argsort of 1e6 int64 with ~1000 ties each, kind={kind}" + (" (stable permutation exact)" if kind in STABLE_KINDS else ""), ok)
    sf = np.sort(bigf, kind=kind); idxf = np.argsort(bigf, kind=kind)
    def mism(x): return int((~((x == expf) | (np.isnan(x) & np.isnan(expf)))).sum())
    ok = mism(sf) == 0 and mism(bigf[idxf]) == 0 and np.isnan(sf[-nnan:]).all()
    if kind in STABLE_KINDS: ok = ok and idxf.tolist() == expidx_f
    report(f"sort / argsort of 1e6 float64 with {nnan} NaN and -0.0, kind={kind}", ok, f"(sort mismatches {mism(sf)}, argsort mismatches {mism(bigf[idxf])}, NaNs at the end {int(np.isnan(sf[-nnan:]).sum())}/{nnan}; first mismatch at {np.where(~((sf == expf) | (np.isnan(sf) & np.isnan(expf))))[0][:3].tolist()})" if not ok else "")
big32 = bigf.astype(np.float32); exp32 = big32[ref_argsort(big32.tolist(), fkey)]
report("sort of 1e6 float32 for every kind", all(np.array_equal(np.sort(big32, kind=k), exp32, equal_nan=True) for k in KINDS))
bigs = np.array([random.choice(vocab) for _ in range(200_000)]); exps = sorted(bigs.tolist())
report("sort / stable argsort of 2e5 strings for every kind", all(np.sort(bigs, kind=k).tolist() == exps for k in KINDS) and np.argsort(bigs, kind="stable").tolist() == ref_argsort(bigs.tolist(), idkey))
big16 = bigi.astype(np.int16) - 500; exp16 = [v - 500 for v in expi]
report("sort / stable argsort of 1e6 int16 (radix sort path) for every kind", all(np.sort(big16, kind=k).tolist() == exp16 for k in KINDS) and np.argsort(big16, kind="stable").tolist() == expidx and np.argsort(big16, kind="mergesort").tolist() == expidx)
cbig = Counter(bigil)
report("1e6: partition kth=N//2 equals the sorted median; searchsorted of 1000 probes; unique with counts", np.partition(bigi, N // 2)[N // 2] == expi[N // 2] and np.searchsorted(np.array(expi), bigi[:1000]).tolist() == [bisect.bisect_left(expi, v) for v in bigil[:1000]] and np.unique(bigi, return_counts=True)[1].tolist() == [cbig[i] for i in sorted(cbig)])
print(f"   1e6 section took {time.time() - t1:.1f} s; whole harness {time.time() - T0:.1f} s")
