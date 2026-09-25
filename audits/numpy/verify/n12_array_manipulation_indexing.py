#!/usr/bin/env python
"""NumPy array manipulation and indexing against plain-Python references (nested lists,
itertools.product over index tuples, explicit loops, fractions.Fraction) and against the
documented invariants / docstring examples.  Covers reshape (C/F/A, -1), ravel / flatten
(order K on non-contiguous and negative-stride views), np.resize vs ndarray.resize,
broadcasting (broadcast_to / broadcast_arrays / broadcast_shapes and their errors),
take / put / putmask / place (mode raise / wrap / clip), take_along_axis / put_along_axis,
choose, compress, pad (every mode, per-side values, stat_length, reflect_type, pad widths
larger than the array, N-D corner rule, callable, dict pad_width on 2.4+), roll, rot90,
flip*, tile, repeat, meshgrid, mgrid / ogrid, linspace, arange, logspace, geomspace,
insert / delete / append, split / array_split / h- v- dsplit, the stack family and
row_stack deprecation, concatenate (axis=None, dtype, casting), block, atleast_*d,
expand_dims, squeeze, moveaxis / swapaxes / rollaxis / transpose, triu / tril / tri,
diag / diagflat / diagonal (read-only view), fill_diagonal (wrap), indices / ix_,
ravel_multi_index / unravel_index, advanced indexing (placement rule, boolean masks
with fewer dimensions, repeated indices, ufunc.at), nonzero on 0-d, argwhere, where,
apply_along_axis, vectorize, frompyfunc, copyto, shares_memory / may_share_memory,
trim_zeros, sliding_window_view, as_strided, array_equal / array_equiv.
No scipy anywhere (the numpy 1.x builds have none)."""
import sys, math, itertools, warnings, time, inspect, operator
from fractions import Fraction as F
import numpy as np

print(f"numpy {np.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""):
    detail = "" if detail in ("[]", "()") else detail
    print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def info(msg): print("   " + msg)
V = tuple(int(x) for x in np.__version__.split(".")[:2]); NP2 = V >= (2, 0)
AxisError = getattr(getattr(np, "exceptions", np), "AxisError")
T0 = time.time()
rs = np.random.RandomState(12)

def raises(f, exc=Exception):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore"); f()
    except exc:
        return True
    except Exception:
        return False
    return False
def exc_name(f):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore"); f()
    except Exception as e:
        return type(e).__name__
    return None
def warns(f, cat):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always"); r = f()
    return any(issubclass(x.category, cat) for x in w), r
def quiet(f):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore"); return f()

# ---- plain-Python nested-list helpers ------------------------------------------------
def cidx(shape): return list(itertools.product(*[range(s) for s in shape]))
def fidx(shape): return [t[::-1] for t in itertools.product(*[range(s) for s in shape[::-1]])]
def get(nl, idx):
    for i in idx: nl = nl[i]
    return nl
def build(shape, fn, pre=()):
    if len(shape) == 0: return fn(pre)
    return [build(shape[1:], fn, pre + (i,)) for i in range(shape[0])]
def shape_of(nl):
    s = []
    while isinstance(nl, list):
        s.append(len(nl)); nl = nl[0] if nl else None
    return tuple(s)
def flat_c(nl, shape): return [get(nl, i) for i in cidx(shape)]
def from_flat_c(flat, shape):
    it = iter(flat); return build(shape, lambda _: next(it))
def from_flat_f(flat, shape):
    d = dict(zip(fidx(shape), flat)); return build(shape, lambda i: d[i])
def eq(a, b):
    """numpy result vs nested-list reference: same shape and same values (NaN == NaN)."""
    a = np.asarray(a)
    if a.shape != shape_of(b) and not (a.ndim == 0 and not isinstance(b, list)): return False
    al = a.tolist()
    def same(x, y):
        if isinstance(x, list): return isinstance(y, list) and len(x) == len(y) and all(same(p, q) for p, q in zip(x, y))
        if isinstance(x, float) and isinstance(y, (float, F, int)) and math.isnan(x): return isinstance(y, float) and math.isnan(y)
        return x == y
    return same(al, b)
def close_list(a, b, rel=1e-13, abs_=0.0):
    a = np.asarray(a, dtype=complex).ravel().tolist(); b = [complex(x) for x in b]
    return len(a) == len(b) and all(abs(x - y) <= max(rel * max(abs(x), abs(y)), abs_) for x, y in zip(a, b))
A234 = np.arange(24).reshape(2, 3, 4); L234 = A234.tolist()

# ====================================================================================
print("---- reshape / ravel / flatten / resize")
# ====================================================================================
src = np.arange(24).reshape(4, 6)
for shp in [(2, 12), (3, 2, 4), (24,), (1, 24, 1)]:
    rc = np.reshape(src, shp, order="C"); rf = np.reshape(src, shp, order="F")
    ok_c = eq(rc, from_flat_c(flat_c(src.tolist(), (4, 6)), shp))
    ok_f = eq(rf, from_flat_f([get(src.tolist(), i) for i in fidx((4, 6))], shp))
    report(f"reshape (4,6)->{shp} order='C' reads/writes C order, order='F' reads/writes F order", ok_c and ok_f)
fsrc = np.asfortranarray(src)
report("reshape order='A': F order for a Fortran-contiguous input ('A' means F order if a is Fortran *contiguous* in memory)",
       eq(np.reshape(fsrc, (3, 8), order="A"), np.reshape(src, (3, 8), order="F").tolist()) and eq(np.reshape(src, (3, 8), order="A"), np.reshape(src, (3, 8), order="C").tolist()))
report("reshape order='A' on a non-contiguous (neither C nor F) view uses C order",
       eq(np.reshape(src[:, ::2], (4, 3), order="A"), from_flat_c(flat_c(src[:, ::2].tolist(), (4, 3)), (4, 3))))
report("reshape -1 inference: (-1, 4) of 24 -> (6, 4); (2, -1, 3) -> (2, 4, 3)", np.reshape(src, (-1, 4)).shape == (6, 4) and src.reshape(2, -1, 3).shape == (2, 4, 3))
report("reshape: two -1 raise ValueError ('One shape dimension can be -1')", raises(lambda: src.reshape(-1, -1), ValueError))
report("reshape: incompatible size raises ValueError", raises(lambda: src.reshape(5, 5), ValueError) and raises(lambda: src.reshape(-1, 5), ValueError))
report("reshape -1 of an empty array with a zero dimension: (0, -1) raises (ambiguous), (-1, 3) of shape (0, 6) -> (0, 3)",
       raises(lambda: np.zeros((0, 6)).reshape(0, -1), ValueError) and np.zeros((0, 6)).reshape(-1, 3).shape == (0, 3))
tmp = src.copy(); v = tmp.reshape(2, 12); v[0, 0] = -1
report("reshape of a C-contiguous array is a view (np.shares_memory)", np.shares_memory(tmp, v) and tmp[0, 0] == -1)
if V >= (2, 1):
    report("2.1+: reshape(copy=False) on a non-viewable layout raises ValueError; copy=True never shares",
           raises(lambda: np.reshape(src.T, (24,), copy=False), ValueError) and not np.shares_memory(np.reshape(src, (24,), copy=True), src))
if V >= (2, 4):
    report("2.4: the deprecated 'newshape' keyword of np.reshape is removed (TypeError)", raises(lambda: np.reshape(src, newshape=(24,)), TypeError))
elif V >= (2, 1):
    w, _ = warns(lambda: np.reshape(src, newshape=(24,)), DeprecationWarning)
    report("2.1-2.3: np.reshape(newshape=) warns DeprecationWarning", w)

# ravel / flatten, order K
def ref_order_K(a):
    """documented: 'K' reads elements in the order they occur in memory, except for reversing the data
    when strides are negative -> iterate axes sorted by |stride| (largest first), in the view's logical direction."""
    shp, st = a.shape, a.strides
    perm = sorted(range(a.ndim), key=lambda k: -abs(st[k]))
    lst = a.tolist(); out = []
    for t in itertools.product(*[range(shp[k]) for k in perm]):
        idx = [0] * a.ndim
        for k, i in zip(perm, t): idx[k] = i
        out.append(get(lst, idx))
    return out
base = np.arange(60).reshape(3, 4, 5)
views = {"transpose(2,0,1)": base.transpose(2, 0, 1), "F-copy": np.asfortranarray(base), "[:, ::2, 1:]": base[:, ::2, 1:],
         "[::-1] (negative stride)": base[::-1], "T[:, ::-1]": base.T[:, ::-1], "swapaxes(0,2)[::2]": base.swapaxes(0, 2)[::2]}
for nm, vw in views.items():
    exp = ref_order_K(vw)
    report(f"ravel(order='K') / flatten('K') of {nm}: memory order, negative strides keep their logical order", vw.ravel("K").tolist() == exp and vw.flatten("K").tolist() == exp)
    report(f"ravel C / F / A of {nm} = plain C / F traversal", vw.ravel("C").tolist() == flat_c(vw.tolist(), vw.shape)
           and vw.ravel("F").tolist() == [get(vw.tolist(), i) for i in fidx(vw.shape)]
           and vw.ravel("A").tolist() == (vw.ravel("F").tolist() if (vw.flags.f_contiguous and not vw.flags.c_contiguous) else vw.ravel("C").tolist()))
info(f"arange(6)[::-1].ravel('K') = {np.arange(6)[::-1].ravel('K').tolist()} (documented: negative strides are not reversed)")
c = np.arange(6).reshape(2, 3)
report("ravel of a contiguous array returns a view; flatten always returns a copy",
       np.shares_memory(c.ravel(), c) and not np.shares_memory(c.flatten(), c) and not np.shares_memory(np.asfortranarray(c).flatten("K"), c))
fc = np.asfortranarray(c)
report("ravel(order='F') of a Fortran-contiguous array shares memory, ravel('C') does not", np.shares_memory(fc.ravel("F"), fc) and not np.shares_memory(fc.ravel("C"), fc))

# resize
def ref_np_resize(flat, n): return [flat[i % len(flat)] for i in range(n)] if flat else [0] * n
x = np.array([[1, 2, 3], [4, 5, 6]])
for shp in [(3, 4), (1, 5), (7,), (2, 3), (0,)]:
    n = int(np.prod(shp))
    report(f"np.resize({x.shape}->{shp}) 'filled with repeated copies of a' in C order", eq(np.resize(x, shp), from_flat_c(ref_np_resize(flat_c(x.tolist(), x.shape), n), shp)))
report("np.resize of an empty array returns zeros of the new shape", eq(np.resize(np.array([], dtype=float), (2, 2)), [[0.0, 0.0], [0.0, 0.0]]))
report("np.resize negative size raises ValueError", raises(lambda: np.resize(x, (-1, 3)), ValueError))
y = np.array([[1, 2, 3], [4, 5, 6]]); y.resize((3, 4), refcheck=False)
report("ndarray.resize enlarging 'missing entries are filled with zeros' (C order)", eq(y, from_flat_c([1, 2, 3, 4, 5, 6] + [0] * 6, (3, 4))))
y = np.array([[1, 2, 3], [4, 5, 6]]); y.resize((2, 2), refcheck=False)
report("ndarray.resize shrinking keeps the first elements in C order", eq(y, [[1, 2], [3, 4]]))
yy = np.arange(6); vv = yy[:2]
report("ndarray.resize raises ValueError when another array references it (refcheck=True)", raises(lambda: yy.resize(10), ValueError))
report("ndarray.resize on a non-owning view raises ValueError", raises(lambda: vv.resize(3), ValueError))
del vv
yf = np.asfortranarray(np.array([[1, 2, 3], [4, 5, 6]]))
yf.resize((3, 3), refcheck=False)
report("ndarray.resize of a Fortran array: data 'flattened (in the order that the data are stored in memory), resized, and reshaped' (F order, zero-filled)",
       eq(yf, from_flat_f([1, 4, 2, 5, 3, 6, 0, 0, 0], (3, 3))), str(yf.tolist()))
ydoc = np.array([[0, 1], [2, 3]], order="F"); ydoc.resize((2, 1))
report("ndarray.resize docstring: [[0,1],[2,3]] order='F' resized to (2,1) -> [[0],[2]]", ydoc.tolist() == [[0], [2]])

# ====================================================================================
print("---- broadcasting")
# ====================================================================================
def ref_bshape(*shapes):
    nd = max(len(s) for s in shapes); out = []
    for k in range(nd):
        dims = [s[len(s) - nd + k] if len(s) - nd + k >= 0 else 1 for s in shapes]
        non1 = {d for d in dims if d != 1}
        if len(non1) > 1: return None
        out.append(non1.pop() if non1 else 1)
    return tuple(out)
cases = [[(3,), (4, 1)], [(5, 1, 4), (3, 1)], [(0,), (3, 1)], [(1,), (0,)], [(2, 3), (3, 2)], [(8, 1, 6, 1), (7, 1, 5)], [(), (2, 2)],
         [(256, 256, 3), (3,)], [(15, 3, 5), (15, 1, 5), (3, 5), (3, 1)], [(2, 1), (8, 4, 3)], [(0, 1), (1, 0)], [(3,), (4,)]]
ok_all = True; bad = []
for c_ in cases:
    exp = ref_bshape(*c_)
    got = np.broadcast_shapes(*c_) if exp is not None else None
    if exp is None:
        if not raises(lambda: np.broadcast_shapes(*c_), ValueError): ok_all = False; bad.append(c_)
    elif got != exp: ok_all = False; bad.append((c_, got, exp))
report("broadcast_shapes: trailing-dimension rule ('equal, or one of them is 1'), ValueError otherwise, on 12 cases", ok_all, str(bad))
report("broadcast_shapes accepts ints as 1-tuples and no argument gives ()", np.broadcast_shapes(3, (2, 1)) == (2, 3) and np.broadcast_shapes() == ())
bt = np.broadcast_to(np.arange(3), (2, 3))
report("broadcast_to: values repeated along the new axis and the view is read-only", eq(bt, [[0, 1, 2], [0, 1, 2]]) and not bt.flags.writeable and raises(lambda: bt.__setitem__((0, 0), 5), ValueError))
report("broadcast_to: incompatible shape raises ValueError; shape shorter than ndim raises ValueError",
       raises(lambda: np.broadcast_to(np.arange(3), (4,)), ValueError) and raises(lambda: np.broadcast_to(np.zeros((2, 3)), (3,)), ValueError))
report("broadcast_to: scalar to () and negative dimension raises ValueError", np.broadcast_to(5, ()).shape == () and raises(lambda: np.broadcast_to(1, (-1,)), ValueError))
report("broadcast_to shares memory with the input (stride 0 on the new axis)", np.shares_memory(bt, bt.base if bt.base is not None else bt) and bt.strides[0] == 0)
ba = np.broadcast_arrays(np.array([[1, 2, 3]]), np.array([[4], [5]]))
report("broadcast_arrays (docstring example) values", eq(ba[0], [[1, 2, 3], [1, 2, 3]]) and eq(ba[1], [[4, 4, 4], [5, 5, 5]]))
report(f"broadcast_arrays returns a {'tuple (2.0+)' if NP2 else 'list (1.x)'}", isinstance(ba, tuple if NP2 else list))
w, _ = warns(lambda: np.broadcast_arrays(np.zeros(3), np.zeros((2, 1)))[0].__setitem__((0, 0), 1), DeprecationWarning)
report("broadcast_arrays: writing to a result emits the deprecation warning ('deprecated:: 1.17 ... if written to, a deprecation warning will be emitted')", w)
report("broadcast_arrays: incompatible shapes raise ValueError", raises(lambda: np.broadcast_arrays(np.zeros(3), np.zeros(4)), ValueError))
b = np.broadcast(np.zeros((2, 1)), np.zeros(3))
report("np.broadcast object: shape / size / nd / numiter", b.shape == (2, 3) and b.size == 6 and b.ndim == 2 and b.numiter == 2)
xx = np.arange(3); yy2 = np.arange(4).reshape(4, 1)
report("arithmetic broadcasting (4,1)+(3,) = outer sum", eq(xx + yy2, [[i + j for j in range(3)] for i in range(4)]))

# ====================================================================================
print("---- take / put / putmask / place / take_along_axis / put_along_axis / choose / compress")
# ====================================================================================
a = np.arange(10, 16)          # [10..15]
n = 6
idx = [0, -1, 5, 7, -8, 13]
report("take mode='wrap' wraps every index modulo n (incl. negatives)", np.take(a, idx, mode="wrap").tolist() == [10 + (i % n) for i in idx])
report("take mode='clip' clips to [0, n-1] ('clipping to the range'; 'this disables indexing with negative numbers')", np.take(a, idx, mode="clip").tolist() == [10 + min(max(i, 0), n - 1) for i in idx])
report("take mode='raise' (default): negative indices in range allowed, out-of-range raises IndexError",
       np.take(a, [-1, -6]).tolist() == [15, 10] and raises(lambda: np.take(a, [6]), IndexError) and raises(lambda: np.take(a, [-7]), IndexError))
M = np.arange(24).reshape(2, 3, 4)
tk = np.take(M, [[2, 0], [1, 1]], axis=1)
report("take axis=1 with 2-D indices: out[i, j, k, l] = a[i, ind[j,k], l] (shape Ni + Nj + Nk)",
       tk.shape == (2, 2, 2, 4) and eq(tk, build((2, 2, 2, 4), lambda t: L234[t[0]][[[2, 0], [1, 1]][t[1]][t[2]]][t[3]])))
report("take axis=None works on the flattened array", np.take(M, [23, 0, 5]).tolist() == [23, 0, 5])
report("take on an empty index list returns an empty array of shape (0,)", np.take(a, []).shape == (0,))
def ref_put(arr, ind, v, mode):
    arr = list(arr); n_ = len(arr)
    for k, i in enumerate(ind):
        if mode == "wrap": i = i % n_
        elif mode == "clip": i = min(max(i, 0), n_ - 1)
        arr[i] = v[k % len(v)]
    return arr
for mode in ("wrap", "clip"):
    p = np.arange(6); np.put(p, [1, -1, 8, -9], [100, 200], mode=mode)
    report(f"put mode='{mode}' with v shorter than ind ('it will be repeated as necessary')", p.tolist() == ref_put(range(6), [1, -1, 8, -9], [100, 200], mode))
p = np.arange(6); np.put(p, [-2], [99])
report("put mode='raise': negative index counts from the end; out-of-range raises IndexError", p.tolist() == [0, 1, 2, 3, 99, 5] and raises(lambda: np.put(np.arange(6), [6], [1]), IndexError))
p2 = np.arange(6).reshape(2, 3); np.put(p2, [0, 4], [-1, -2])
report("put acts on the flattened target ('a.flat[ind] = v')", p2.tolist() == [[-1, 1, 2], [3, -2, 5]])
x = np.arange(6).reshape(2, 3); np.putmask(x, x > 2, x ** 2)
report("putmask docstring example ([[0,1,2],[9,16,25]])", x.tolist() == [[0, 1, 2], [9, 16, 25]])
mask = [False, True, True, False, True, False, True]
pm = np.zeros(7, dtype=int); np.putmask(pm, mask, [10, 20, 30])
report("putmask repeats values POSITIONALLY: 'a.flat[n] = values[n]' -> values[n % len(values)]", pm.tolist() == [10 * (1 + (i % 3)) if m else 0 for i, m in enumerate(mask)], str(pm.tolist()))
pl = np.zeros(7, dtype=int); np.place(pl, mask, [10, 20, 30])
k_ = iter(itertools.cycle([10, 20, 30]))
report("place uses vals SEQUENTIALLY: 'the first N elements of vals', repeated when shorter", pl.tolist() == [next(k_) if m else 0 for m in mask], str(pl.tolist()))
report("place with an empty vals and a non-empty mask raises ('this sequence must be non-empty')", raises(lambda: np.place(np.zeros(3), [True, False, False], []), ValueError))
pl2 = np.zeros(3); np.place(pl2, [False] * 3, [])
report("place with empty vals and an all-False mask is a no-op", pl2.tolist() == [0.0] * 3)
report("putmask with values the same size as a: values[n] used at masked n (a[mask] = values would differ)",
       (lambda z: (np.putmask(z, [True, False, True], [7, 8, 9]), z.tolist())[1])(np.zeros(3, int)) == [7, 0, 9])
# take_along_axis / put_along_axis
B = rs.randint(0, 50, size=(4, 5)); BL = B.tolist()
ai = np.argsort(B, axis=1, kind="stable")
report("take_along_axis(a, argsort(a, axis=1), axis=1) = row-wise sorted (reference sorted())", eq(np.take_along_axis(B, ai, axis=1), [sorted(r) for r in BL]))
ai0 = np.argsort(B, axis=0, kind="stable")
report("take_along_axis axis=0 = column-wise sorted", eq(np.take_along_axis(B, ai0, axis=0), [list(r) for r in zip(*[sorted(c_) for c_ in zip(*BL)])]))
mx = np.expand_dims(np.argmax(B, axis=1), 1)
report("take_along_axis with keepdims argmax picks the row maxima", eq(np.take_along_axis(B, mx, axis=1), [[max(r)] for r in BL]))
report("take_along_axis axis=None on flattened input with 1-D indices", np.take_along_axis(B, np.array([0, 19, 7]), axis=None).tolist() == [BL[0][0], BL[3][4], BL[1][2]])
report("take_along_axis: indices of different ndim raise ValueError", raises(lambda: np.take_along_axis(B, np.array([0, 1]), axis=1), ValueError))
C = B.copy(); np.put_along_axis(C, mx, -1, axis=1)
report("put_along_axis writes -1 at the row argmax (first occurrence)", eq(C, [[(-1 if j == r.index(max(r)) else v) for j, v in enumerate(r)] for r in BL]))
C = B.copy(); np.put_along_axis(C, np.array([[0, 0]] * 4), [[1, 2]] * 4, axis=1)
info(f"put_along_axis with repeated index [0,0] <- [1,2]: row 0 col 0 = {C[0, 0]} (no documented order; 2 = last-wins observed)")
if V >= (2, 3):
    report("2.3+: take_along_axis axis defaults to -1", eq(np.take_along_axis(B, ai), [sorted(r) for r in BL]))
# choose
ch = [[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]]
report("choose docstring example ([20, 31, 12, 3])", np.choose([2, 3, 1, 0], ch).tolist() == [20, 31, 12, 3])
report("choose mode='clip' ([20, 31, 12, 3] for [2, 4, 1, 0])", np.choose([2, 4, 1, 0], ch, mode="clip").tolist() == [20, 31, 12, 3])
report("choose mode='wrap' ([20, 1, 12, 3] for [2, 4, 1, 0])", np.choose([2, 4, 1, 0], ch, mode="wrap").tolist() == [20, 1, 12, 3])
report("choose mode='wrap' negative index -1 selects the last choice; 'clip' maps negatives to 0",
       np.choose([-1, 0, 0, 0], ch, mode="wrap").tolist()[0] == 30 and np.choose([-1, 0, 0, 0], ch, mode="clip").tolist()[0] == 0)
report("choose mode='raise' raises ValueError for an out-of-range choice", raises(lambda: np.choose([2, 4, 1, 0], ch), ValueError))
aa = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
report("choose broadcasting (docstring: [[10,-10,10],[-10,10,-10],[10,-10,10]])", np.choose(aa, (-10, 10)).tolist() == [[10, -10, 10], [-10, 10, -10], [10, -10, 10]])
info("choose(0, 40 choices): " + str(exc_name(lambda: np.choose(0, [np.array(i) for i in range(40)])) or "ok"))
# compress
cc = np.array([[1, 2], [3, 4], [5, 6]])
report("compress docstring examples (axis=0, axis=1, axis=None)", np.compress([0, 1], cc, axis=0).tolist() == [[3, 4]]
       and np.compress([False, True, True], cc, axis=0).tolist() == [[3, 4], [5, 6]] and np.compress([False, True], cc, axis=1).tolist() == [[2], [4], [6]]
       and np.compress([False, True], cc).tolist() == [2])
report("compress: condition shorter than the axis -> 'output is truncated to the length of the condition'", np.compress([True], np.arange(5)).tolist() == [0])
report("compress: condition longer than the axis with a True beyond it raises IndexError", raises(lambda: np.compress([0, 0, 0, 0, 0, 1], np.arange(5)), IndexError))
info(f"compress: condition longer than the axis but False beyond it -> {quiet(lambda: np.compress([0, 1, 0, 0, 0, 0], np.arange(5)).tolist())}")

# ====================================================================================
print("---- pad (plain-Python 1-D reference applied axis by axis, per the Notes)")
# ====================================================================================
def pair(v, ax, nd):
    """normalise pad_width / stat_length / constant_values / end_values per the docstring rules."""
    if v is None: return (None, None)
    if isinstance(v, dict): return v.get(ax, (0, 0)) if not isinstance(v.get(ax, (0, 0)), int) else (v[ax], v[ax])
    if np.ndim(v) == 0: return (v, v)
    v = list(v)
    if np.ndim(v) == 1:
        return (v[0], v[0]) if len(v) == 1 else (v[0], v[1])
    return tuple(v[0]) if len(v) == 1 else tuple(v[ax])
def rnd_half_even(x):  # x a Fraction -> nearest int, ties to even (np.round)
    return int(round(x))
def pad1d(v, b, c, mode, is_int, **kw):
    n = len(v)
    if mode == "constant":
        cb, ca = kw["cv"]; return [cb] * b + v + [ca] * c
    if mode == "edge": return [v[0]] * b + v + [v[-1]] * c
    if mode == "linear_ramp":
        eb, ea = kw["ev"]
        def ramp(start, stop, num):   # linspace(start, stop, num, endpoint=False), floored for int dtypes
            vals = [F(start) + (F(stop) - F(start)) * i / num for i in range(num)]
            return [math.floor(q) for q in vals] if is_int else [float(q) for q in vals]
        return ramp(eb, v[0], b) + v + ramp(ea, v[-1], c)[::-1]
    if mode in ("maximum", "minimum", "mean", "median"):
        sb, sa = kw["sl"]; sb = n if sb is None else min(sb, n); sa = n if sa is None else min(sa, n)
        def stat(ch):
            if mode == "maximum": return max(ch)
            if mode == "minimum": return min(ch)
            fr = [F(x) for x in ch]
            if mode == "mean": s = sum(fr) / len(fr)
            else:
                srt = sorted(fr); m = len(srt); s = srt[m // 2] if m % 2 else (srt[m // 2 - 1] + srt[m // 2]) / 2
            return rnd_half_even(s) if is_int else float(s)
        return [stat(v[:sb])] * b + v + [stat(v[n - sa:])] * c
    if mode in ("reflect", "symmetric"):
        odd = kw.get("rt", "even") == "odd"; cur = list(v)
        if n == 1: return [v[0]] * b + v + [v[0]] * c   # documented? (see label)
        step = n - 1 if mode == "reflect" else n
        rem = b
        while rem > 0:
            k = min(rem, step); e = cur[0]
            ch = (cur[1:k + 1] if mode == "reflect" else cur[0:k])[::-1]
            if odd: ch = [2 * e - x for x in ch]
            cur = ch + cur; rem -= k
        rem = c
        while rem > 0:
            k = min(rem, step); e = cur[-1]
            ch = (cur[len(cur) - k - 1:len(cur) - 1] if mode == "reflect" else cur[len(cur) - k:])[::-1]
            if odd: ch = [2 * e - x for x in ch]
            cur = cur + ch; rem -= k
        return cur
    if mode == "wrap": return [v[(i - b) % n] for i in range(b)] + v + [v[i % n] for i in range(c)]
    raise ValueError(mode)
def pad_ref(arr, pw, mode, **kw):
    arr = np.asarray(arr); is_int = arr.dtype.kind in "iu"; cur = arr.tolist() if arr.ndim else arr.item(); shape = list(arr.shape)
    for ax in range(arr.ndim):
        b, c = pair(pw, ax, arr.ndim)
        kk = {}
        if mode == "constant": kk["cv"] = pair(kw.get("constant_values", 0), ax, arr.ndim)
        if mode == "linear_ramp": kk["ev"] = pair(kw.get("end_values", 0), ax, arr.ndim)
        if mode in ("maximum", "minimum", "mean", "median"): kk["sl"] = pair(kw.get("stat_length"), ax, arr.ndim)
        if "reflect_type" in kw: kk["rt"] = kw["reflect_type"]
        newshape = list(shape); newshape[ax] += b + c
        d = {}
        others = [range(s) for k, s in enumerate(shape) if k != ax]
        for o in itertools.product(*others):
            line = []
            for i in range(shape[ax]):
                t = list(o); t.insert(ax, i); line.append(get(cur, t))
            pl_ = pad1d(line, b, c, mode, is_int, **kk)
            for i, val in enumerate(pl_):
                t = list(o); t.insert(ax, i); d[tuple(t)] = val
        shape = newshape; cur = build(tuple(shape), lambda t: d[t])
    return cur
a5 = [1, 2, 3, 4, 5]
doc_ex = [((2, 3), "constant", dict(constant_values=(4, 6)), [4, 4, 1, 2, 3, 4, 5, 6, 6, 6]),
          ((2, 3), "edge", {}, [1, 1, 1, 2, 3, 4, 5, 5, 5, 5]),
          ((2, 3), "linear_ramp", dict(end_values=(5, -4)), [5, 3, 1, 2, 3, 4, 5, 2, -1, -4]),
          ((2,), "maximum", {}, [5, 5, 1, 2, 3, 4, 5, 5, 5]), ((2,), "mean", {}, [3, 3, 1, 2, 3, 4, 5, 3, 3]),
          ((2,), "median", {}, [3, 3, 1, 2, 3, 4, 5, 3, 3]),
          ((2, 3), "reflect", {}, [3, 2, 1, 2, 3, 4, 5, 4, 3, 2]), ((2, 3), "reflect", dict(reflect_type="odd"), [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]),
          ((2, 3), "symmetric", {}, [2, 1, 1, 2, 3, 4, 5, 5, 4, 3]), ((2, 3), "symmetric", dict(reflect_type="odd"), [0, 1, 1, 2, 3, 4, 5, 5, 6, 7]),
          ((2, 3), "wrap", {}, [4, 5, 1, 2, 3, 4, 5, 1, 2, 3])]
ok_doc = all(np.pad(a5, pw, m, **kw).tolist() == exp for pw, m, kw, exp in doc_ex)
ok_ref = all(pad_ref(a5, pw, m, **kw) == exp for pw, m, kw, exp in doc_ex)
report("pad: all 11 1-D docstring examples reproduced by numpy", ok_doc)
report("pad: the plain-Python reference reproduces the same 11 docstring examples (reference sanity)", ok_ref)
report("pad 2-D 'minimum' docstring example ((3,2),(2,3)) = reference", eq(np.pad([[1, 2], [3, 4]], ((3, 2), (2, 3)), "minimum"), pad_ref([[1, 2], [3, 4]], ((3, 2), (2, 3)), "minimum")))
# random 1-D float vectors, every mode, many widths incl. larger than the array
vec = [float(x) for x in rs.randint(-20, 20, size=5)]
MODES1 = [("constant", [dict(constant_values=(-7.5, 2.25))]), ("edge", [{}]), ("linear_ramp", [dict(end_values=(3.0, -9.0)), {}]),
          ("maximum", [{}, dict(stat_length=2), dict(stat_length=(1, 3)), dict(stat_length=99)]),
          ("minimum", [{}, dict(stat_length=(2, 4))]), ("mean", [{}, dict(stat_length=3), dict(stat_length=(1, 2))]),
          ("median", [{}, dict(stat_length=4), dict(stat_length=(2, 3))]),
          ("reflect", [{}, dict(reflect_type="odd")]), ("symmetric", [{}, dict(reflect_type="odd")]), ("wrap", [{}])]
WIDTHS = [(0, 0), (1, 0), (0, 2), (3, 4), (4, 4), (5, 5), (9, 2), (13, 17), (25, 1), (1, 25), (25, 0)]
for mode, kws in MODES1:
    fails = []; ncmp = 0
    for kw in kws:
        for pw in WIDTHS:
            got = np.pad(np.array(vec), pw, mode, **kw).tolist(); exp = pad_ref(vec, pw, mode, **kw); ncmp += 1
            good = len(got) == len(exp) and all(abs(g - e) <= 1e-12 * max(1, abs(e)) for g, e in zip(got, exp))
            if not good:
                fails.append((kw.get("reflect_type", ""), pw))
                if len(fails) == 1:
                    info(f"{mode} {kw} {pw}: numpy    {[int(g) if g == int(g) else g for g in got]}")
                    info(f"{mode} {kw} {pw}: reference {[int(e) if e == int(e) else e for e in exp]}")
    extra = {"reflect": " ('mirrored on the first and last values', periodic for widths > n-1)", "symmetric": " ('mirrored along the edge', periodic for widths > n)",
             "wrap": " (1.25 release note: 'always fills the space with strict multiples of original data')"}.get(mode, "")
    report(f"pad 1-D float mode='{mode}'{extra}: {ncmp} option x width cases (widths up to 25 on n=5, one-sided) = reference", not fails, f"failing (reflect_type, width): {fails}")
info(f"vector {vec}; reflect (13,17) = {np.pad(np.array(vec), (13, 17), 'reflect').tolist()[:8]}...")
info(f"reflect odd (9,2) = {np.pad(np.array(vec), (9, 2), 'reflect', reflect_type='odd').tolist()}")
# integer dtype: mean / median rounding and linear_ramp flooring
iv = [1, 2, 4, 8, 9]
fails = []
for mode, kw in [("mean", {}), ("mean", dict(stat_length=2)), ("median", dict(stat_length=(2, 4))), ("linear_ramp", dict(end_values=(0, 20))), ("linear_ramp", dict(end_values=(-7, 3)))]:
    for pw in [(3, 3), (1, 6), (7, 2)]:
        got = np.pad(np.array(iv), pw, mode, **kw).tolist(); exp = pad_ref(iv, pw, mode, **kw)
        if got != exp: fails.append((mode, kw, pw, got, exp))
report("pad int dtype: mean/median rounded half-to-even (np.round), linear_ramp floored (linspace int dtype rounds towards -inf)", not fails, str(fails[:3]))
info(f"mean of [1,2] -> {np.pad(np.array([1, 2, 4]), (1, 0), 'mean', stat_length=2).tolist()[0]} (1.5 -> 2), of [1,2,4] (7/3) -> {np.pad(np.array([1, 2, 4]), (1, 0), 'mean').tolist()[0]}")
# N-D: corners from previous axes; per-side constant values
m23 = rs.randint(-9, 9, size=(2, 3)).astype(float)
fails = []; fails_w = []
for mode, kw in [("constant", dict(constant_values=((1, 2), (3, 4)))), ("constant", dict(constant_values=(5, 6))), ("edge", {}),
                 ("linear_ramp", dict(end_values=((1, 2), (-3, 4)))), ("maximum", dict(stat_length=((1, 2), (2, 1)))), ("mean", {}),
                 ("median", dict(stat_length=1)), ("minimum", {}), ("reflect", {}), ("reflect", dict(reflect_type="odd")),
                 ("symmetric", {}), ("symmetric", dict(reflect_type="odd")), ("wrap", {})]:
    for pw in [((1, 2), (3, 0)), 2, ((4, 5), (7, 6)), (1, 3), ((0, 1), (6, 0))]:
        got = np.pad(m23, pw, mode, **kw); exp = pad_ref(m23, pw, mode, **kw)
        if not (got.shape == shape_of(exp) and np.allclose(got, np.array(exp), rtol=1e-12, atol=0)):
            (fails_w if mode in ("reflect", "symmetric", "wrap") else fails).append((mode, kw.get("reflect_type", ""), pw))
report("pad 2-D constant / edge / linear_ramp / stat modes (per-axis per-side values): 'corners calculated by using padded values from the first axis' = reference", not fails, str(fails[:5]))
report("pad 2-D reflect / symmetric / wrap incl. widths larger than the axis = reference (axis-by-axis)", not fails_w, str(fails_w[:6]))
report("pad constant corners: later axis wins ([[3,1,4],[3,0,4],[3,2,4]] for constant_values=((1,2),(3,4)))",
       np.pad(np.zeros((1, 1), int), 1, constant_values=((1, 2), (3, 4))).tolist() == [[3, 1, 4], [3, 0, 4], [3, 2, 4]])
m3 = rs.randint(0, 9, size=(2, 2, 3))
report("pad 3-D 'wrap' and 'symmetric' = reference", eq(np.pad(m3, ((1, 2), (0, 3), (2, 1)), "wrap"), pad_ref(m3, ((1, 2), (0, 3), (2, 1)), "wrap"))
       and eq(np.pad(m3, 2, "symmetric"), pad_ref(m3, 2, "symmetric")))
p32 = np.pad(np.array([1, 2, 4], np.float32), 2, "mean")
report("pad float32 input keeps float32; mean = float32(7/3)", p32.dtype == np.float32 and p32[0] == np.float32(7 / 3))
e = np.pad(np.arange(4.0), (2, 3), "empty")
report("pad 'empty': shape grows and the original values sit in the middle (pad values undefined)", e.shape == (9,) and e[2:6].tolist() == [0.0, 1.0, 2.0, 3.0])
def pad_with(vector, pad_width, iaxis, kwargs):
    pv = kwargs.get("padder", 10); vector[:pad_width[0]] = pv; vector[-pad_width[1]:] = pv
a6 = np.arange(6).reshape(2, 3)
report("pad callable (docstring pad_with example, default and padder=100)", np.pad(a6, 2, pad_with).tolist() == [[10] * 7, [10] * 7, [10, 10, 0, 1, 2, 10, 10], [10, 10, 3, 4, 5, 10, 10], [10] * 7, [10] * 7]
       and np.pad(a6, 2, pad_with, padder=100)[2].tolist() == [100, 100, 0, 1, 2, 100, 100])
seen = []
np.pad(a6, ((1, 2), (3, 0)), lambda v_, pw_, ax_, kw_: seen.append((ax_, tuple(pw_), len(v_), v_.tolist())))
report("pad callable receives (vector, iaxis_pad_width, iaxis, kwargs); vector = a 1-D line of the padded array, 'already padded with zeros'",
       sorted(set(t[:3] for t in seen)) == [(0, (1, 2), 5), (1, (3, 0), 6)] and all(t[3][:t[1][0]] == [0] * t[1][0] for t in seen if t[0] == 0), str(sorted(set(t[:3] for t in seen))))
info(f"pad callable call count for (2,3) padded ((1,2),(3,0)): {len(seen)} (axis 0: {sum(t[0] == 0 for t in seen)} columns of the padded array incl. the pad columns; axis 1: {sum(t[0] == 1 for t in seen)} rows); the count is not documented")
report("pad: negative pad width raises ValueError", raises(lambda: np.pad(np.arange(3), -1), ValueError))
report("pad: stat modes on an empty axis raise, constant on empty works", np.pad(np.zeros(0), 2).tolist() == [0.0] * 4 and raises(lambda: np.pad(np.zeros(0), 2, "maximum"), ValueError))
report("pad: 'reflect' / 'wrap' on an empty axis with nonzero width raise ValueError", raises(lambda: np.pad(np.zeros(0), 1, "reflect"), ValueError) and raises(lambda: np.pad(np.zeros(0), 1, "wrap"), ValueError))
report("pad: unsupported keyword for the mode raises ValueError (e.g. stat_length with 'edge')", raises(lambda: np.pad(np.arange(3), 1, "edge", stat_length=1), ValueError))
info(f"pad reflect of a length-1 array (not documented): {np.pad(np.array([7]), (2, 3), 'reflect').tolist()}, symmetric odd: {np.pad(np.array([7]), 2, 'symmetric', reflect_type='odd').tolist()}")
if V >= (2, 4):
    a16 = np.arange(1, 7).reshape(2, 3)
    report("2.4: pad_width as a dict (docstring examples {1:(1,2)}, {-1:2}, {0:(3,0), 1:2})",
           np.pad(a16, {1: (1, 2)}).tolist() == [[0, 1, 2, 3, 0, 0], [0, 4, 5, 6, 0, 0]] and np.pad(a16, {-1: 2}).tolist() == [[0, 0, 1, 2, 3, 0, 0], [0, 0, 4, 5, 6, 0, 0]]
           and np.pad(a16, {0: (3, 0), 1: 2}).shape == (5, 7))

# ====================================================================================
print("---- roll / rot90 / flip / tile / repeat")
# ====================================================================================
x = np.arange(10)
report("roll 1-D: out[(i+shift) % n] = x[i] for shifts 2, -2, 13, -23, 0", all(np.roll(x, s).tolist() == [x.tolist()[(i - s) % 10] for i in range(10)] for s in (2, -2, 13, -23, 0)))
x2 = np.arange(10).reshape(2, 5); X2 = x2.tolist()
report("roll axis=None flattens, rolls and restores the shape (docstring: roll(x2, 1) -> [[9,0,1,2,3],[4,5,6,7,8]])", np.roll(x2, 1).tolist() == [[9, 0, 1, 2, 3], [4, 5, 6, 7, 8]])
report("roll axis=1 and tuple shifts ((1, 1), axis=(1, 0)) and ((2, -1), (0, 1))",
       eq(np.roll(x2, -1, axis=1), [[r[(j + 1) % 5] for j in range(5)] for r in X2])
       and eq(np.roll(x2, (1, 1), axis=(1, 0)), [[X2[(i - 1) % 2][(j - 1) % 5] for j in range(5)] for i in range(2)])
       and eq(np.roll(x2, (2, -1), axis=(0, 1)), [[X2[(i - 2) % 2][(j + 1) % 5] for j in range(5)] for i in range(2)]))
report("roll with the same axis repeated adds the shifts (roll(x, (1, 2), axis=(0, 0)) == roll(x, 3))", np.roll(x, (1, 2), axis=(0, 0)).tolist() == np.roll(x, 3).tolist())
report("roll of an empty array; shift tuple with axis=None sums the shifts on the flattened array", np.roll(np.zeros(0), 3).shape == (0,) and np.roll(x2, (1, 1)).tolist() == np.roll(x2, 2).tolist())
report("roll: shift tuple / axis tuple length mismatch raises ValueError", raises(lambda: np.roll(x2, (1, 2, 3), axis=(0, 1)), ValueError))
m = np.arange(6).reshape(2, 3); Mm = m.tolist()
def rot1(l):  # counter-clockwise, first axis toward second: r[i][j] = m[j][ncols-1-i]
    nr, nc = len(l), len(l[0]); return [[l[j][nc - 1 - i] for j in range(nr)] for i in range(nc)]
refs = [Mm]
for _ in range(3): refs.append(rot1(refs[-1]))
report("rot90 k = 0..7 and negative k (k mod 4) = repeated counter-clockwise rotation", all(eq(np.rot90(m, k), refs[k % 4]) for k in range(-5, 8)))
report("rot90(m, k, axes=(1,0)) is the reverse of rot90(m, k, axes=(0,1)) ('rot90(m, k=1, axes=(1,0)) is the reverse')",
       all(eq(np.rot90(m, k, axes=(1, 0)), refs[(-k) % 4]) for k in range(4)))
report("rot90 on 3-D with axes=(1,2) rotates each 2-D slab", eq(np.rot90(A234, 1, axes=(1, 2)), [rot1(s) for s in L234]))
report("rot90: axes of equal values or wrong length raise ValueError", raises(lambda: np.rot90(m, 1, axes=(0, 0)), ValueError) and raises(lambda: np.rot90(m, 1, axes=(0,)), ValueError))
report("flip axis=None reverses every axis; flip axis tuple; fliplr / flipud",
       eq(np.flip(A234), [[r[::-1] for r in s[::-1]] for s in L234[::-1]]) and eq(np.flip(A234, (0, 2)), [[r[::-1] for r in s] for s in L234[::-1]])
       and eq(np.fliplr(m), [r[::-1] for r in Mm]) and eq(np.flipud(m), Mm[::-1]) and eq(np.flipud(np.arange(3)), [2, 1, 0]))
report("flip returns a view (O(1))", np.shares_memory(np.flip(m), m))
report("fliplr of a 1-D array raises ValueError ('must be >= 2-d')", raises(lambda: np.fliplr(np.arange(3)), ValueError))
def ref_tile(l, shape, reps):
    reps = tuple(reps); d = max(len(shape), len(reps)); shape = (1,) * (d - len(shape)) + tuple(shape); reps = (1,) * (d - len(reps)) + reps
    flat = dict(zip(cidx(tuple(shape[k] for k in range(d) if True)), [None] * 0))
    lst = l
    for _ in range(d - len(np.shape(l))): lst = [lst]
    out_shape = tuple(s * r for s, r in zip(shape, reps))
    return build(out_shape, lambda t: get(lst, [t[k] % shape[k] for k in range(d)]))
okt = True; bad = []
for arr, reps in [([0, 1, 2], 2), ([0, 1, 2], (2, 2)), ([0, 1, 2], (2, 1, 2)), ([[1, 2], [3, 4]], 2), ([[1, 2], [3, 4]], (2, 1)), ([1, 2, 3, 4], (4, 1)),
                  (A234.tolist(), (2, 1)), ([[1, 2]], (3, 1, 2, 1)), ([5], 0)]:
    got = np.tile(np.array(arr), reps); exp = ref_tile(arr, np.shape(arr), reps if isinstance(reps, tuple) else (reps,))
    if not (got.shape == np.shape(exp) and got.tolist() == exp): okt = False; bad.append((arr, reps, got.shape))
report("tile: reps promoted / array promoted by prepending 1s, output = periodic extension (9 cases incl. docstring)", okt, str(bad))
report("repeat: scalar repeats, per-element repeats, axis=None flattens",
       np.repeat(3, 4).tolist() == [3] * 4 and np.repeat([[1, 2], [3, 4]], 2).tolist() == [1, 1, 2, 2, 3, 3, 4, 4]
       and np.repeat([[1, 2], [3, 4]], [1, 2], axis=0).tolist() == [[1, 2], [3, 4], [3, 4]] and np.repeat([[1, 2], [3, 4]], 3, axis=1).tolist() == [[1, 1, 1, 2, 2, 2], [3, 3, 3, 4, 4, 4]])
report("repeat with zero repeats drops elements; negative repeats and wrong-length repeats raise ValueError",
       np.repeat([1, 2, 3], [0, 2, 0]).tolist() == [2, 2] and raises(lambda: np.repeat([1, 2], -1), ValueError) and raises(lambda: np.repeat([1, 2, 3], [1, 2]), ValueError))

# ====================================================================================
print("---- meshgrid / mgrid / ogrid / indices / ix_")
# ====================================================================================
xs, ys, zs = [0, 1, 2], [10, 20], [7, 8, 9, 6]
X, Y = np.meshgrid(xs, ys)
report("meshgrid 'xy' (default): outputs of shape (N, M) = (len(y), len(x)); X[j][i] = x[i], Y[j][i] = y[j]",
       X.shape == (2, 3) and eq(X, [[x_ for x_ in xs] for _ in ys]) and eq(Y, [[y_ for _ in xs] for y_ in ys]))
X, Y = np.meshgrid(xs, ys, indexing="ij")
report("meshgrid 'ij': shape (M, N); X[i][j] = x[i]", X.shape == (3, 2) and eq(X, [[x_ for _ in ys] for x_ in xs]) and eq(Y, [[y_ for y_ in ys] for _ in xs]))
X, Y, Z = np.meshgrid(xs, ys, zs)
report("meshgrid 3-D 'xy': shape (N, M, P) per the Notes", X.shape == (2, 3, 4) and Z[1, 2, 3] == 6 and X[1, 2, 3] == 2 and Y[1, 2, 3] == 20)
Xs, Ys = np.meshgrid(xs, ys, sparse=True)
report("meshgrid sparse=True: shapes (1, M) and (N, 1) for 'xy', broadcast to the dense grid", Xs.shape == (1, 3) and Ys.shape == (2, 1) and eq(Xs + Ys, (np.meshgrid(xs, ys)[0] + np.meshgrid(xs, ys)[1]).tolist()))
Xs, Ys = np.meshgrid(xs, ys, sparse=True, indexing="ij")
report("meshgrid sparse 'ij': shapes (M, 1) and (1, N)", Xs.shape == (3, 1) and Ys.shape == (1, 2))
xv = np.array(xs); Xc, _ = np.meshgrid(xv, ys, copy=False)
report("meshgrid copy=False returns views of the inputs (shares memory, zero stride)", np.shares_memory(Xc, xv) and 0 in Xc.strides)
report("meshgrid of one / zero inputs: 1-D -> (array,), none -> ()", len(np.meshgrid(xs)) == 1 and np.meshgrid(xs)[0].tolist() == xs and len(np.meshgrid()) == 0)
report("meshgrid bad indexing string raises ValueError", raises(lambda: np.meshgrid(xs, ys, indexing="yx"), ValueError))
mg = np.mgrid[0:5, 0:3]
report("mgrid[0:5, 0:3]: shape (2, 5, 3), dense index grids", mg.shape == (2, 5, 3) and eq(mg[0], [[i] * 3 for i in range(5)]) and eq(mg[1], [[0, 1, 2]] * 5))
g = np.mgrid[-1:1:5j]
report("mgrid complex step 5j: 'the integer part of its magnitude is interpreted as the number of points', stop INCLUSIVE", g.tolist() == [-1.0, -0.5, 0.0, 0.5, 1.0])
g2 = np.mgrid[0:1:0.25]
report("mgrid real step: stop EXCLUSIVE (like arange)", g2.tolist() == [0.0, 0.25, 0.5, 0.75])
g3 = np.mgrid[0:3:4j, 0:1:3j]
report("mgrid mixed complex steps (4j, 3j): shape (2, 4, 3), values linspace", g3.shape == (2, 4, 3) and g3[0][:, 0].tolist() == [0.0, 1.0, 2.0, 3.0] and g3[1][0].tolist() == [0.0, 0.5, 1.0])
g4 = np.mgrid[0:1:3.5j]
info(f"mgrid[0:1:3.5j] (non-integer magnitude) -> {g4.tolist()} (docstring: integer part of the magnitude)")
report("mgrid[0:1:3.5j] uses int(3.5) = 3 points", len(g4) == 3)
report("mgrid[0:1:3.5j]: 'the stop value **is inclusive**' also for a non-integer magnitude -> [0, 0.5, 1]", g4.tolist() == [0.0, 0.5, 1.0], str(g4.tolist()))
og4 = np.ogrid[0:1:3.5j]
report("ogrid[0:1:3.5j] likewise [0, 0.5, 1] (same docstring sentence)", og4.tolist() == [0.0, 0.5, 1.0], str(og4.tolist()))
og = np.ogrid[-1:1:5j]
report("ogrid 1-D complex step = mgrid", og.tolist() == g.tolist())
og2 = np.ogrid[0:5, 0:3]
report("ogrid[0:5, 0:3]: open grids of shapes (5, 1) and (1, 3)", og2[0].shape == (5, 1) and og2[1].shape == (1, 3) and og2[0].ravel().tolist() == list(range(5)))
ind = np.indices((2, 3))
report("indices((2,3)): grid[k][i][j] = (i, j)[k]", ind.shape == (2, 2, 3) and eq(ind[0], [[0, 0, 0], [1, 1, 1]]) and eq(ind[1], [[0, 1, 2]] * 2))
isp = np.indices((2, 3), sparse=True)
report("indices sparse=True returns a tuple of shapes (2,1), (1,3)", isinstance(isp, tuple) and isp[0].shape == (2, 1) and isp[1].shape == (1, 3))
report("indices dtype=", np.indices((2, 2), dtype=np.int8).dtype == np.int8)
aa = np.arange(10).reshape(2, 5)
ixg = np.ix_([0, 1], [2, 4])
report("ix_: open mesh shapes (2,1)/(1,2), a[ix_] = cross product selection", ixg[0].shape == (2, 1) and ixg[1].shape == (1, 2) and aa[ixg].tolist() == [[2, 4], [7, 9]])
report("ix_ with a boolean sequence converts it to the nonzero indices", aa[np.ix_([True, True], [2, 4])].tolist() == [[2, 4], [7, 9]] and np.ix_([False, True, True])[0].tolist() == [1, 2])
report("ix_ with a 2-D argument raises ValueError ('Cross index must be 1 dimensional')", raises(lambda: np.ix_([[0, 1]]), ValueError))

# ====================================================================================
print("---- linspace / arange / logspace / geomspace")
# ====================================================================================
report("linspace docstring examples (2..3 num=5, endpoint=False, retstep)", np.linspace(2.0, 3.0, 5).tolist() == [2.0, 2.25, 2.5, 2.75, 3.0]
       and np.allclose(np.linspace(2.0, 3.0, num=5, endpoint=False), [2.0, 2.2, 2.4, 2.6, 2.8], rtol=0, atol=1e-15)
       and np.linspace(2.0, 3.0, num=5, retstep=True)[1] == 0.25)
worst = 0.0; last_exact = True
for (s, e, nn) in [(0, 1, 7), (0.1, 0.7, 11), (-3.3, 1e5 / 3, 97), (1e-300, 1e-299, 13), (5, -5, 12), (0.1, 0.3, 3), (1.0, 1.0 + 2 ** -40, 9)]:
    got = np.linspace(s, e, nn); fs, fe = F(s), F(e)
    for i, gv in enumerate(got.tolist()):
        tr = fs + (fe - fs) * i / (nn - 1)
        worst = max(worst, abs(F(gv) - tr) / max(abs(fs), abs(fe)))
    last_exact &= got[-1] == e and got[0] == s
report("linspace: 'stop is the last sample' EXACTLY (y[-1] = stop) and first = start", last_exact)
report("linspace values within 4 ulp of max(|start|, |stop|) of the exact start + i*(stop-start)/(num-1) (Fraction; no bound is documented)", worst < 4 * 2 ** -52, f"worst {float(worst):.2e}")
info(f"linspace worst |error| / max(|start|,|stop|) vs Fraction truth: {float(worst):.2e} (= {float(worst) / 2 ** -52:.2f} ulp)")
ls, st = np.linspace(0, 1, 5, endpoint=False, retstep=True)
report("linspace endpoint=False: all but the last of num+1 samples; step = (stop-start)/num", np.allclose(ls, [0, 0.2, 0.4, 0.6, 0.8], rtol=0, atol=1.2e-16) and st == 0.2)
l1, s1 = np.linspace(2, 3, 1, retstep=True)
report("linspace num=1: [start]; retstep step is NaN when endpoint=True (undefined step)", l1.tolist() == [2.0] and math.isnan(s1))
l1b, s1b = np.linspace(2, 3, 1, endpoint=False, retstep=True)
report("linspace num=1 endpoint=False: [start], step = stop - start", l1b.tolist() == [2.0] and s1b == 1.0)
report("linspace num=0 -> empty; negative num raises ValueError", np.linspace(0, 1, 0).shape == (0,) and raises(lambda: np.linspace(0, 1, -1), ValueError))
report("linspace dtype is never integer by inference ('float is chosen even if the arguments would produce an array of integers')", np.linspace(0, 10, 11).dtype == np.float64)
li = np.linspace(-2.5, 2.5, 6, dtype=int)
report("linspace integer dtype: 'rounded towards -inf' (1.20+)", li.tolist() == [math.floor(float(F(-5, 2) + i)) for i in range(6)], str(li.tolist()))
li2 = np.linspace(0, 1, 4, dtype=int)
report("linspace(0,1,4,dtype=int) -> [0,0,0,1] (floor of 0, 1/3, 2/3, 1)", li2.tolist() == [0, 0, 0, 1])
la = np.linspace([0, 10], [1, 20], 3, axis=1)
report("linspace array start/stop: axis=1 places samples on the last axis", la.shape == (2, 3) and la.tolist() == [[0.0, 0.5, 1.0], [10.0, 15.0, 20.0]])
info(f"linspace(inf, inf, 3) = {quiet(lambda: np.linspace(np.inf, np.inf, 3)).tolist()}")
l32 = np.linspace(0, 1, 7, dtype=np.float32)
report("linspace dtype=float32: output float32, stop exact, values = float32 of the float64 samples", l32.dtype == np.float32 and l32[-1] == np.float32(1) and l32.tolist() == np.float32(np.linspace(0, 1, 7)).tolist())
a32 = np.arange(0, 1, 0.1, dtype=np.float32)
report("arange dtype=float32 length ceil((1-0)/0.1) = 10", len(a32) == 10 and a32.dtype == np.float32)
lc = np.linspace(0, 1 + 1j, 3)
report("linspace complex endpoints", lc.dtype.kind == "c" and lc.tolist() == [0j, 0.5 + 0.5j, 1 + 1j])
# arange
ar = np.arange(1, 1.3, 0.1)
Ln = math.ceil((1.3 - 1) / 0.1)
report("arange float length = ceil((stop - start)/step) evaluated in float (documented)", len(ar) == Ln, f"len={len(ar)} ceil={Ln}")
info(f"arange(1, 1.3, 0.1) = {ar.tolist()} length {len(ar)}; (1.3-1)/0.1 = {(1.3 - 1) / 0.1!r}; last > stop: {ar[-1] > 1.3}")
report("arange(1, 1.3, 0.1): the documented hazard occurs ('may result in the last element of out being greater than stop')", ar[-1] > 1.3)
okar = True
for (s, e, stp) in [(0, 1, 0.1), (0.5, 7.25, 0.25), (-1, 1, 0.3), (10, 0, -0.7), (0, 2, 1 / 3), (0, 1e3, 0.1)]:
    r = np.arange(s, e, stp)
    if len(r) != math.ceil((e - s) / stp): okar = False
    delta = F(float(s + stp)) - F(s)
    if not all(abs(F(v_) - (F(s) + i * delta)) <= abs(F(s) + i * delta) * F(2, 2 ** 52) + F(1, 2 ** 60) for i, v_ in enumerate(r.tolist())): okar = False
report("arange float: length ceil((stop-start)/step) and out[i] = start + i*(dtype(start+step) - dtype(start)) (Warnings section) within 2 ulp", okar)
report("arange docstring integer examples and step sign", np.arange(3).tolist() == [0, 1, 2] and np.arange(3, 7, 2).tolist() == [3, 5] and np.arange(5, 1, -2).tolist() == [5, 3] and np.arange(3, 1).tolist() == [])
report("arange(0, 5, 0.5, dtype=int) -> ten zeros; arange(-3, 3, 0.5, dtype=int) -> [-3..8] (Warnings section)",
       np.arange(0, 5, 0.5, dtype=np.int_).tolist() == [0] * 10 and np.arange(-3, 3, 0.5, dtype=np.int_).tolist() == list(range(-3, 9)))
report("arange step 0 raises ZeroDivisionError / ValueError", raises(lambda: np.arange(0, 1, 0)))
info("arange step=0 raises " + str(exc_name(lambda: np.arange(0, 1, 0))))
report("arange integer dtype default int64 / float for float args", np.arange(3).dtype == np.int_ and np.arange(3.0).dtype == np.float64)
bigs = np.arange(2 ** 53 - 2, 2 ** 53 + 2, dtype=np.int64)
report("arange large int64 near 2**53 exact", bigs.tolist() == list(range(2 ** 53 - 2, 2 ** 53 + 2)))
# logspace / geomspace
lg = np.logspace(0, 3, 4)
report("logspace(0,3,4) = [1,10,100,1000] exactly (10.0**k)", lg.tolist() == [1.0, 10.0, 100.0, 1000.0])
lg2 = np.logspace(2.0, 3.0, num=4, base=2.0)
report("logspace base=2 docstring = [4, 5.0397, 6.3496, 8] (2**linspace) within 1e-15", close_list(lg2, [2.0 ** (2 + i / 3) for i in range(4)], rel=4.5e-16))
report("logspace endpoint=False", close_list(np.logspace(2.0, 3.0, num=4, endpoint=False), [10 ** (2 + i / 4) for i in range(4)], rel=1e-15))
if V >= (1, 25):
    lb = np.logspace(0, 2, 3, base=[2, 10])
    report("1.25+: array base: result shape (num, len(base)) with column j = base[j]**linspace", lb.shape == (3, 2) and lb[:, 0].tolist() == [1.0, 2.0, 4.0] and lb[:, 1].tolist() == [1.0, 10.0, 100.0])
    lb2 = np.logspace(0, 2, 3, base=[2, 10], axis=-1)
    report("1.25+: array base with axis=-1 puts samples last", lb2.shape == (2, 3) and lb2[1].tolist() == [1.0, 10.0, 100.0])
else:
    report("pre-1.25: array base unsupported (versionchanged 1.25.0 'Non-scalar base is now supported')", raises(lambda: np.logspace(0, 2, 3, base=[2, 10])))
gs = np.geomspace(1, 1000, num=4)
report("geomspace(1, 1000, 4) = [1, 10, 100, 1000] (docstring)", np.allclose(gs, [1, 10, 100, 1000], rtol=1e-15, atol=0) and gs[0] == 1 and gs[-1] == 1000)
worst = 0.0; ends = True
for s, e, nn in [(1, 256, 9), (3.7, 1e10, 33), (1e-5, 7.25, 5), (1000, 1, 4), (-1000, -1, 4), (-2.5, -1e-3, 17), (0.1, 0.3, 11)]:
    gg = np.geomspace(s, e, nn); ends &= gg[0] == s and gg[-1] == e
    r_ = (e / s) ** (1 / (nn - 1))
    for i, v_ in enumerate(gg.tolist()):
        tr = s * math.exp(math.log(e / s) * i / (nn - 1)); worst = max(worst, abs(v_ - tr) / abs(tr))
report("geomspace endpoints exact (result[0] = start, result[-1] = stop) incl. decreasing and negative ranges", ends)
report("geomspace interior values within 1e-14 relative of s*(e/s)**(i/(n-1))", worst < 1e-14, f"worst {worst:.2e}")
info(f"geomspace worst rel error {worst:.2e}")
report("geomspace(1, 256, 9, dtype=int_) truncates (docstring: [1,2,4,7,16,32,63,127,256] 'may not produce exact integers')",
       np.geomspace(1, 256, num=9, dtype=np.int_).tolist() in ([1, 2, 4, 7, 16, 32, 63, 127, 256], [1, 2, 4, 8, 16, 32, 64, 128, 256]))
info(f"geomspace(1,256,9,dtype=int_) = {np.geomspace(1, 256, num=9, dtype=np.int_).tolist()}")
report("geomspace(-1000, -1, 4) = [-1000, -100, -10, -1]", np.allclose(np.geomspace(-1000, -1, num=4), [-1000, -100, -10, -1], rtol=1e-15, atol=0))
gj = np.geomspace(1j, 1000j, num=4)
report("geomspace(1j, 1000j, 4) is a straight line [1j, 10j, 100j, 1000j] (docstring)", close_list(gj, [1j, 10j, 100j, 1000j], rel=1e-14, abs_=1e-12))
gc = np.geomspace(-1 + 0j, 1 + 0j, num=5)
report("geomspace(-1, 1, 5) complex: half circle exp(i*pi*(1 - k/4)) (docstring 'Circle')", close_list(gc, [complex(math.cos(math.pi * (1 - k / 4)), math.sin(math.pi * (1 - k / 4))) for k in range(5)], rel=0, abs_=1e-15))
report("geomspace with zero raises ValueError ('Geometric sequence cannot include zero')", raises(lambda: np.geomspace(0, 10, 3), ValueError))
info(f"geomspace(-1, 1, 3) real (sign change) -> {quiet(lambda: np.geomspace(-1, 1, 3)).tolist()} (no documented error)")

# ====================================================================================
print("---- insert / delete / append")
# ====================================================================================
a = np.array([[1, 1], [2, 2], [3, 3]])
report("insert docstring: insert(a, 1, 5) flattens -> [1,5,1,2,2,3,3]", np.insert(a, 1, 5).tolist() == [1, 5, 1, 2, 2, 3, 3])
report("insert axis=1 scalar index vs [1] sequence ('obj=0 behaves very different from obj=[0]')",
       np.insert(a, 1, [1, 2, 3], axis=1).tolist() == [[1, 1, 1], [2, 2, 2], [3, 3, 3]] and np.insert(a, [1], [[1], [2], [3]], axis=1).tolist() == [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
       and np.insert(a, 1, [[1], [2], [3]], axis=1).shape == (3, 5))
b = a.flatten()
report("insert multiple indices refer to positions in the ORIGINAL array: insert(b, [2, 2], [5, 6]) and slice(2,4)",
       np.insert(b, [2, 2], [5, 6]).tolist() == [1, 1, 5, 6, 2, 2, 3, 3] and np.insert(b, slice(2, 4), [5, 6]).tolist() == [1, 1, 5, 2, 6, 2, 3, 3])
report("insert unsorted index list: values placed before each original position (stable)", np.insert(b, [4, 1, 4], [7, 8, 9]).tolist() == [1, 8, 1, 2, 2, 7, 9, 3, 3])
report("insert float values into int array are cast ([2.5, 3] -> [2, 3])", np.insert(b, [2, 2], [7.13, False]).tolist() == [1, 1, 7, 0, 2, 2, 3, 3])
report("insert index == len appends; negative index counts from the end (before the last)", np.insert(np.arange(3), 3, 9).tolist() == [0, 1, 2, 9] and np.insert(np.arange(3), -1, 9).tolist() == [0, 1, 9, 2])
report("insert out-of-range index raises IndexError (both signs)", raises(lambda: np.insert(np.arange(3), 5, 9), IndexError) and raises(lambda: np.insert(np.arange(3), -5, 9), IndexError))
bins = quiet(lambda: np.insert(np.arange(3), np.array([True, False, True]), 9).tolist()) if not raises(lambda: np.insert(np.arange(3), np.array([True, False, True]), 9)) else exc_name(lambda: np.insert(np.arange(3), np.array([True, False, True]), 9))
if V >= (2, 2) or np.__version__ >= "2.1.2":
    report("2.1.2+: insert with a boolean obj: 'treated as a mask of elements to insert' -> before positions 0 and 2", bins == [9, 0, 1, 9, 2], str(bins))
    info(f"insert boolean obj of other lengths (no documented rule): len 2 -> {np.insert(np.arange(3), np.array([True, False]), 9).tolist()}, len 4 -> {np.insert(np.arange(3), np.array([True, False, True, True]), 9).tolist()} (mask of length n+1 can address the append position)")
else:
    report("pre-2.1.2: insert with a boolean obj casts it 'to the integers 0 and 1' (versionchanged 2.1.2) -> before positions 1, 0, 1", bins == [9, 0, 9, 9, 1, 2], str(bins))
arr = np.arange(12).reshape(3, 4)
report("delete docstring: delete(arr, 1, 0), delete(arr, np.s_[::2], 1), delete(arr, [1,3,5], None)",
       np.delete(arr, 1, 0).tolist() == [[0, 1, 2, 3], [8, 9, 10, 11]] and np.delete(arr, np.s_[::2], 1).tolist() == [[1, 3], [5, 7], [9, 11]]
       and np.delete(arr, [1, 3, 5], None).tolist() == [0, 2, 4, 6, 7, 8, 9, 10, 11])
report("delete negative indices and repeated indices (deleted once)", np.delete(np.arange(6), [-1, 0, 0]).tolist() == [1, 2, 3, 4])
mk = np.array([True, False, True, False, False, True])
report("delete with a boolean mask of the axis length removes the True positions", np.delete(np.arange(6), mk).tolist() == [1, 3, 4])
report("delete boolean mask of the wrong length raises ValueError", raises(lambda: np.delete(np.arange(6), [True, False]), ValueError))
report("delete out-of-range index raises IndexError (scalar and sequence)", raises(lambda: np.delete(np.arange(3), 3), IndexError) and raises(lambda: np.delete(np.arange(3), [0, 3]), IndexError) and raises(lambda: np.delete(np.arange(3), -4), IndexError))
report("delete empty index list returns a copy", (lambda r: r.tolist() == [0, 1, 2] and not np.shares_memory(r, x))(np.delete(x[:3], [])))
report("append flattens without axis; with axis needs matching ndim (ValueError)",
       np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]]).tolist() == list(range(1, 10)) and np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0).shape == (3, 3)
       and raises(lambda: np.append([[1, 2, 3], [4, 5, 6]], [7, 8, 9], axis=0), ValueError))

# ====================================================================================
print("---- split family")
# ====================================================================================
def ref_array_split(lst, k):
    n = len(lst); q, r = divmod(n, k); out = []; pos = 0
    for i in range(k):
        sz = q + 1 if i < r else q; out.append(lst[pos:pos + sz]); pos += sz
    return out
ok_s = True
for n_ in range(0, 14):
    for k in range(1, 7):
        got = [p.tolist() for p in np.array_split(np.arange(n_), k)]
        if got != ref_array_split(list(range(n_)), k): ok_s = False
report("array_split: 'l % n sub-arrays of size l//n + 1 and the rest of size l//n' (n = 0..13, k = 1..6)", ok_s)
report("array_split docstring: 8 into 3 -> [0,1,2],[3,4,5],[6,7]", [p.tolist() for p in np.array_split(np.arange(8.0), 3)] == [[0, 1, 2], [3, 4, 5], [6, 7]])
report("split: equal division required else ValueError ('array split does not result in an equal division')", raises(lambda: np.split(np.arange(8), 3), ValueError) and len(np.split(np.arange(9), 3)) == 3)
sp = np.split(np.arange(8.0), [3, 5, 6, 10])
report("split at indices incl. one beyond the end -> empty last piece (docstring)", [p.tolist() for p in sp] == [[0, 1, 2], [3, 4], [5], [6, 7], []])
report("split with decreasing indices gives empty pieces", [p.tolist() for p in np.split(np.arange(6), [4, 2])] == [[0, 1, 2, 3], [], [2, 3, 4, 5]])
report("split sections=0 raises (ZeroDivisionError/ValueError)", raises(lambda: np.split(np.arange(4), 0)))
report("array_split sections <= 0 raises ValueError ('number sections must be larger than 0')", raises(lambda: np.array_split(np.arange(4), 0), ValueError))
x44 = np.arange(16.0).reshape(4, 4)
report("hsplit splits axis 1 of 2-D, axis 0 of 1-D; vsplit axis 0; dsplit axis 2",
       [p.shape for p in np.hsplit(x44, 2)] == [(4, 2), (4, 2)] and [p.tolist() for p in np.hsplit(np.arange(6), 3)] == [[0, 1], [2, 3], [4, 5]]
       and [p.shape for p in np.vsplit(x44, [3])] == [(3, 4), (1, 4)] and [p.shape for p in np.dsplit(np.zeros((2, 2, 4)), 2)] == [(2, 2, 2)] * 2)
report("vsplit of 1-D and dsplit of 2-D raise ValueError ('only works on arrays of 2/3 or more dimensions')", raises(lambda: np.vsplit(np.arange(4), 2), ValueError) and raises(lambda: np.dsplit(x44, 2), ValueError))
report("split pieces are views of the input", np.shares_memory(np.split(x44, 2)[1], x44))

# ====================================================================================
print("---- stack family / concatenate / block / atleast_*d")
# ====================================================================================
p, q = np.array([1, 2, 3]), np.array([4, 5, 6])
report("stack axis 0 / 1 / -1 of 1-D arrays", np.stack([p, q]).tolist() == [[1, 2, 3], [4, 5, 6]] and np.stack([p, q], axis=1).tolist() == [[1, 4], [2, 5], [3, 6]] and np.stack([p, q], -1).shape == (3, 2))
report("stack: shape mismatch raises ValueError; empty list raises ValueError", raises(lambda: np.stack([p, np.arange(4)]), ValueError) and raises(lambda: np.stack([]), ValueError))
report("stack axis out of range raises AxisError", raises(lambda: np.stack([p, q], axis=3), AxisError))
report("hstack 1-D concatenates, 2-D along axis 1; vstack promotes 1-D to rows",
       np.hstack([p, q]).tolist() == [1, 2, 3, 4, 5, 6] and np.hstack([[[1], [2]], [[3], [4]]]).tolist() == [[1, 3], [2, 4]] and np.vstack([p, q]).tolist() == [[1, 2, 3], [4, 5, 6]])
report("dstack of 1-D -> (1, N, k); of 2-D -> (M, N, k)", np.dstack([p, q]).shape == (1, 3, 2) and np.dstack([p, q]).tolist() == [[[1, 4], [2, 5], [3, 6]]] and np.dstack([[[1], [2]], [[3], [4]]]).shape == (2, 1, 2))
report("column_stack: 1-D arrays become columns; 2-D stacked as-is", np.column_stack([p, q]).tolist() == [[1, 4], [2, 5], [3, 6]] and np.column_stack([np.ones((3, 2)), p]).shape == (3, 3))
if hasattr(np, "row_stack"):
    w, rsv = warns(lambda: np.row_stack([p, q]), DeprecationWarning)
    report(f"row_stack = vstack; {'2.0+: emits DeprecationWarning (row_stack alias deprecated in 2.0)' if NP2 else '1.x: no warning'}", rsv.tolist() == [[1, 2, 3], [4, 5, 6]] and w == NP2)
else:
    report("row_stack removed", V >= (2, 5))
report("concatenate axis=None flattens all inputs first", np.concatenate([np.array([[1, 2], [3, 4]]), np.array([[5, 6]])], axis=None).tolist() == [1, 2, 3, 4, 5, 6])
report("concatenate: ndim mismatch / shape mismatch off-axis raise ValueError", raises(lambda: np.concatenate([np.zeros((2, 2)), np.zeros(2)]), ValueError) and raises(lambda: np.concatenate([np.zeros((2, 2)), np.zeros((2, 3))]), ValueError))
report("concatenate: zero-length inputs allowed", np.concatenate([np.zeros((0, 3)), np.ones((2, 3))]).shape == (2, 3))
if V >= (1, 20):
    report("concatenate dtype=float from ints", np.concatenate([p, q], dtype=float).dtype == np.float64)
    report("concatenate dtype=int from floats raises TypeError under default casting='same_kind'", raises(lambda: np.concatenate([np.array([1.5]), np.array([2])], dtype=int), TypeError))
    report("concatenate dtype=int casting='unsafe' truncates ([1.7, -1.7] -> [1, -1])", np.concatenate([np.array([1.7, -1.7]), np.array([2])], dtype=int, casting="unsafe").tolist() == [1, -1, 2])
    report("concatenate casting='no' with differing dtypes raises TypeError", raises(lambda: np.concatenate([np.zeros(2, np.float32), np.zeros(2)], casting="no"), TypeError))
    report("concatenate out= and dtype= together raise TypeError", raises(lambda: np.concatenate([p, q], out=np.zeros(6), dtype=float), TypeError))
report("concatenate out= receives the result", (lambda o: (np.concatenate([p, q], out=o), o.tolist())[1])(np.zeros(6)) == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
A_ = np.eye(2) * 2; B_ = np.eye(3) * 3
blk = np.block([[A_, np.zeros((2, 3))], [np.ones((3, 2)), B_]])
report("block docstring (2x2 / 3x3 blocks) -> 5x5 with the blocks in place", blk.shape == (5, 5) and blk[:2, :2].tolist() == A_.tolist() and blk[2:, 2:].tolist() == B_.tolist() and blk[2:, :2].tolist() == [[1, 1]] * 3)
report("block 1-D = hstack; [[a],[b]] = vstack; scalars are 0-d blocks", np.block([p, q]).tolist() == [1, 2, 3, 4, 5, 6] and np.block([[p], [q]]).tolist() == [[1, 2, 3], [4, 5, 6]] and np.block([1, 2]).tolist() == [1, 2])
report("block: mismatched list depths raise ValueError; empty list raises ValueError", raises(lambda: np.block([[1, 2], 3]), ValueError) and raises(lambda: np.block([]), ValueError))
report("block: incompatible shapes raise ValueError", raises(lambda: np.block([[np.zeros((2, 2)), np.zeros((3, 3))]]), ValueError))
report("atleast_1d: scalar -> (1,), 1-D unchanged (same object)", np.atleast_1d(1.0).shape == (1,) and np.atleast_1d(p) is p)
report("atleast_2d: (N,) -> (1, N); scalar -> (1, 1)", np.atleast_2d(p).shape == (1, 3) and np.atleast_2d(3).shape == (1, 1))
report("atleast_3d: (N,) -> (1, N, 1); (M, N) -> (M, N, 1); scalar -> (1,1,1); 3-D unchanged",
       np.atleast_3d(p).shape == (1, 3, 1) and np.atleast_3d(np.zeros((2, 5))).shape == (2, 5, 1) and np.atleast_3d(1).shape == (1, 1, 1) and np.atleast_3d(A234).shape == (2, 3, 4))
mult = np.atleast_1d(1, [3, 4])
report(f"atleast_1d of several inputs returns a {'tuple (2.0+)' if NP2 else 'list (1.x)'}", isinstance(mult, tuple if NP2 else list) and [m_.shape for m_ in mult] == [(1,), (2,)])
if V >= (2, 0) and "ndim" in str(inspect.signature(np.atleast_1d)): pass

# ====================================================================================
print("---- expand_dims / squeeze / moveaxis / swapaxes / rollaxis / transpose")
# ====================================================================================
x3 = np.zeros((2, 3))
report("expand_dims axis 0 / 1 / -1 / tuple (0, 3) / (0, -1)", np.expand_dims(x3, 0).shape == (1, 2, 3) and np.expand_dims(x3, 1).shape == (2, 1, 3)
       and np.expand_dims(x3, -1).shape == (2, 3, 1) and np.expand_dims(x3, (0, 3)).shape == (1, 2, 3, 1) and np.expand_dims(x3, (0, -1)).shape == (1, 2, 3, 1)
       and np.expand_dims(np.zeros(2), (2, 0)).shape == (1, 2, 1))
report("expand_dims out-of-range axis raises AxisError; repeated axis raises ValueError", raises(lambda: np.expand_dims(x3, 4), AxisError) and raises(lambda: np.expand_dims(x3, (0, 0)), ValueError))
report("squeeze removes all length-1 axes; axis selects; tuple axis", np.squeeze(np.zeros((1, 3, 1))).shape == (3,) and np.squeeze(np.zeros((1, 3, 1)), axis=0).shape == (3, 1) and np.squeeze(np.zeros((1, 3, 1)), axis=(0, 2)).shape == (3,))
report("squeeze axis with length != 1 raises ValueError", raises(lambda: np.squeeze(np.zeros((1, 3, 1)), axis=1), ValueError))
report("squeeze of (1,1) returns 0-d; squeeze axis out of range raises AxisError", np.squeeze(np.zeros((1, 1))).shape == () and raises(lambda: np.squeeze(np.zeros((1, 3)), axis=2), AxisError))
xm = np.zeros((3, 4, 5))
report("moveaxis docstring shapes: (0,-1)->(4,5,3); (-1,0)->(5,3,4); ([0,1],[-1,-2])->(5,4,3)",
       np.moveaxis(xm, 0, -1).shape == (4, 5, 3) and np.moveaxis(xm, -1, 0).shape == (5, 3, 4) and np.moveaxis(xm, [0, 1], [-1, -2]).shape == (5, 4, 3))
mv = np.moveaxis(A234, 0, 2)
report("moveaxis values: out[j,k,i] = a[i,j,k]", eq(mv, build((3, 4, 2), lambda t: L234[t[2]][t[0]][t[1]])))
report("moveaxis repeated source raises ValueError; source/destination length mismatch raises ValueError",
       raises(lambda: np.moveaxis(xm, [0, 0], [1, 2]), ValueError) and raises(lambda: np.moveaxis(xm, [0, 1], [1]), ValueError))
report("swapaxes values and view", eq(np.swapaxes(A234, 0, 2), build((4, 3, 2), lambda t: L234[t[2]][t[1]][t[0]])) and np.shares_memory(np.swapaxes(A234, 0, 2), A234))
xr = np.ones((3, 4, 5, 6))
report("rollaxis docstring shapes: (3,1)->(3,6,4,5); (2)->(5,3,4,6); (1,4)->(3,5,6,4)",
       np.rollaxis(xr, 3, 1).shape == (3, 6, 4, 5) and np.rollaxis(xr, 2).shape == (5, 3, 4, 6) and np.rollaxis(xr, 1, 4).shape == (3, 5, 6, 4))
report("rollaxis start > ndim raises AxisError", raises(lambda: np.rollaxis(xr, 1, 5), AxisError))
tp = np.transpose(A234, (1, -1, 0))
report("transpose with axes incl. negative: out[j,k,i] = a[i,j,k] for axes (1,-1,0)", eq(tp, build((3, 4, 2), lambda t: L234[t[2]][t[0]][t[1]])))
report("transpose default reverses axes; repeated axes raise ValueError; wrong length raises ValueError",
       np.transpose(A234).shape == (4, 3, 2) and raises(lambda: np.transpose(A234, (0, 0, 1)), ValueError) and raises(lambda: np.transpose(A234, (0, 1)), ValueError))
report("1-D transpose is a no-op", np.transpose(p).tolist() == [1, 2, 3])

# ====================================================================================
print("---- triu / tril / tri / diag / diagflat / diagonal / fill_diagonal")
# ====================================================================================
M34 = np.arange(1, 13).reshape(3, 4); L34 = M34.tolist()
ok_t = all(eq(np.triu(M34, k), [[v if j - i >= k else 0 for j, v in enumerate(r)] for i, r in enumerate(L34)])
           and eq(np.tril(M34, k), [[v if j - i <= k else 0 for j, v in enumerate(r)] for i, r in enumerate(L34)]) for k in range(-4, 6))
report("triu / tril for k = -4..5: keep j - i >= k / <= k", ok_t)
report("triu/tril on 3-D apply to the final two axes", eq(np.tril(A234, -1), [[[v if j - i <= -1 else 0 for j, v in enumerate(r)] for i, r in enumerate(s)] for s in L234]))
report("tri(N, M, k) = ones where j <= i + k; dtype", all(eq(np.tri(3, 5, k), [[1.0 if j <= i + k else 0.0 for j in range(5)] for i in range(3)]) for k in (-3, -1, 0, 2, 5)) and np.tri(2, dtype=int).dtype == int)
report("triu of a 1-D array: treated as a row repeated (documented 'k-th diagonal zeroed' of the broadcast (N,N))", np.triu([1, 2, 3]).tolist() == [[1, 2, 3], [0, 2, 3], [0, 0, 3]])
x9 = np.arange(9).reshape(3, 3)
report("diag of 2-D extracts the k-th diagonal for k = -3..3 (empty beyond)", all(np.diag(x9, k).tolist() == [x9.tolist()[i][i + k] for i in range(3) if 0 <= i + k < 3] for k in range(-3, 4)))
report("diag of 1-D builds a 2-D array with v on the k-th diagonal (size len(v)+|k|)", all(eq(np.diag([1, 2], k), [[([1, 2][i] if j - i == k and i < 2 else ([1, 2][j] if k < 0 and i - j == -k and j < 2 else 0)) for j in range(2 + abs(k))] for i in range(2 + abs(k))]) for k in (-2, 0, 1)))
report("diag of 3-D raises ValueError ('Input must be 1- or 2-d')", raises(lambda: np.diag(np.zeros((2, 2, 2))), ValueError))
report("diagflat flattens the input first; k offset", np.diagflat([[1, 2], [3, 4]]).tolist() == [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]] and np.diagflat([1, 2], 1).tolist() == [[0, 1, 0], [0, 0, 2], [0, 0, 0]])
dg = x9.diagonal()
report("diagonal returns a read-only view ('Starting in NumPy 1.9 it returns a read-only view'): write raises ValueError", not dg.flags.writeable and np.shares_memory(dg, x9) and raises(lambda: dg.__setitem__(0, 5), ValueError))
report("np.diag of 2-D also returns the read-only diagonal view", not np.diag(x9).flags.writeable)
report("diagonal offsets and axis1/axis2 on 3-D: result's last axis is the diagonal",
       eq(A234.diagonal(1, 1, 2), [[s[i][i + 1] for i in range(3)] for s in L234]) and eq(A234.diagonal(0, 0, 2), [[L234[i][j][i] for i in range(2)] for j in range(3)]))
report("diagonal axis1 == axis2 raises ValueError", raises(lambda: A234.diagonal(0, 1, 1), ValueError))
fd = np.zeros((7, 3), int); np.fill_diagonal(fd, 5)
report("fill_diagonal tall wrap=False: only the first N rows ([5,0,0],[0,5,0],[0,0,5], rest 0)", eq(fd, [[5 if (i == j and i < 3) else 0 for j in range(3)] for i in range(7)]))
fd = np.zeros((7, 3), int); np.fill_diagonal(fd, 4, wrap=True)
exp_fd = [[0] * 3 for _ in range(7)]
for pos in range(0, 21, 4): exp_fd[pos // 3][pos % 3] = 4
report("fill_diagonal wrap=True: flat step ncols+1 continues after the square block (docstring 7x3: rows 0,1,2,4,5,6)", eq(fd, exp_fd), str(fd.tolist()))
fw = np.zeros((3, 5), int); np.fill_diagonal(fw, [1, 2, 3, 4])
report("fill_diagonal wide array and val sequence (repeated/truncated to the diagonal)", eq(fw, [[([1, 2, 3][i] if i == j else 0) for j in range(5)] for i in range(3)]))
fv = np.zeros((4, 4), int); np.fill_diagonal(fv, [7, 8])
report("fill_diagonal with shorter val repeats it cyclically", np.diag(fv).tolist() == [7, 8, 7, 8])
f3 = np.zeros((3, 3, 3), int); np.fill_diagonal(f3, 2)
report("fill_diagonal 3-D: a[i,i,i] only", all(f3[i, j, k] == (2 if i == j == k else 0) for i in range(3) for j in range(3) for k in range(3)))
report("fill_diagonal on a non-hypercube N-D (N>2) raises ValueError ('All dimensions of input must be of equal length')", raises(lambda: np.fill_diagonal(np.zeros((2, 3, 3)), 1), ValueError))

# ====================================================================================
print("---- ravel_multi_index / unravel_index")
# ====================================================================================
dims = (7, 6); arrm = [[3, 6, 6], [4, 5, 1]]
report("ravel_multi_index docstring: [22, 41, 37] (C), [31, 41, 13] (F)", np.ravel_multi_index(arrm, dims).tolist() == [22, 41, 37] and np.ravel_multi_index(arrm, dims, order="F").tolist() == [31, 41, 13])
report("ravel_multi_index mode='clip' / 'wrap' docstring: [22, 23, 19] and (4,2) with modes ('clip','wrap') -> 12",
       np.ravel_multi_index(arrm, (4, 6), mode="clip").tolist() == [22, 23, 19] and np.ravel_multi_index(arrm, (4, 4), mode=("clip", "wrap")).tolist() == [12, 13, 13])
report("ravel_multi_index scalar docstring: (3,1,4,1) in (6,7,8,9) -> 1621", int(np.ravel_multi_index((3, 1, 4, 1), (6, 7, 8, 9))) == 1621)
ok_r = True
shp = (3, 4, 5)
for mi in [(0, 0, 0), (2, 3, 4), (1, 2, 3), (-1, 5, 7), (4, -2, 12)]:
    for mode in ("wrap", "clip"):
        m2 = [(i % s) if mode == "wrap" else min(max(i, 0), s - 1) for i, s in zip(mi, shp)]
        if int(np.ravel_multi_index(mi, shp, mode=mode)) != (m2[0] * 4 + m2[1]) * 5 + m2[2]: ok_r = False
        if int(np.ravel_multi_index(mi, shp, mode=mode, order="F")) != m2[0] + 3 * (m2[1] + 4 * m2[2]): ok_r = False
report("ravel_multi_index wrap/clip x C/F against the closed-form strides (incl. negative / oversized)", ok_r)
report("ravel_multi_index mode='raise' out of range raises ValueError", raises(lambda: np.ravel_multi_index((3, 0, 0), shp), ValueError) and raises(lambda: np.ravel_multi_index((-1, 0, 0), shp), ValueError))
report("unravel_index docstring: [22,41,37] in (7,6) -> ([3,6,6],[4,5,1]); F -> ([3,6,6],[4,5,1]) for [31,41,13]; 1621 -> (3,1,4,1)",
       [t.tolist() for t in np.unravel_index([22, 41, 37], (7, 6))] == [[3, 6, 6], [4, 5, 1]] and [t.tolist() for t in np.unravel_index([31, 41, 13], (7, 6), order="F")] == [[3, 6, 6], [4, 5, 1]]
       and tuple(int(t) for t in np.unravel_index(1621, (6, 7, 8, 9))) == (3, 1, 4, 1))
report("unravel_index round-trips every flat index of (3,4,5) in C and F", all(int(np.ravel_multi_index(np.unravel_index(i, shp, order=o), shp, order=o)) == i for i in range(60) for o in "CF"))
report("unravel_index out-of-range / negative raises ValueError", raises(lambda: np.unravel_index(60, shp), ValueError) and raises(lambda: np.unravel_index(-1, shp), ValueError))
report("unravel_index with shape () and index 0 -> ()", np.unravel_index(0, ()) == ())
if NP2:
    report("2.0: unravel_index 'dims' keyword removed (TypeError)", raises(lambda: np.unravel_index(1, dims=(2, 2)), TypeError))

# ====================================================================================
print("---- advanced indexing semantics")
# ====================================================================================
a3 = np.arange(3 * 4 * 5).reshape(3, 4, 5); L3 = a3.tolist()
i0, i2 = [0, 2], [1, 3]
r1 = a3[i0, :, i2]
report("a[arr1, :, arr2]: advanced indices separated by a slice -> broadcast dims FIRST: shape (2, 4), r[k, j] = a[i0[k], j, i2[k]]",
       r1.shape == (2, 4) and eq(r1, [[L3[i0[k]][j][i2[k]] for j in range(4)] for k in range(2)]))
r2 = a3[:, [0, 2], [1, 3]]
report("a[:, arr1, arr2]: adjacent advanced indices -> dims in place: shape (3, 2)", r2.shape == (3, 2) and eq(r2, [[L3[i][[0, 2][k]][[1, 3][k]] for k in range(2)] for i in range(3)]))
r3 = a3[[[0], [2]], :, [1, 3]]
report("a[(2,1) idx, :, (2,) idx]: broadcast (2,2) index dims first -> (2, 2, 4)", r3.shape == (2, 2, 4) and eq(r3, [[[L3[[0, 2][p_]][j][[1, 3][q_]] for j in range(4)] for q_ in range(2)] for p_ in range(2)]))
r4 = a3[[0, 2], :, 1]
report("an integer counts as an advanced index: a[arr, :, 1] -> dims first (2, 4) (docstring 'not x[arr1, :, 1]')", r4.shape == (2, 4) and eq(r4, [[L3[[0, 2][k]][j][1] for j in range(4)] for k in range(2)]))
r5 = a3[1, :, [0, 4]]
report("a[1, :, arr] also puts the advanced dim first: shape (2, 4)", r5.shape == (2, 4) and eq(r5, [[L3[1][j][[0, 4][k]] for j in range(4)] for k in range(2)]))
r6 = a3[..., [0, 1]]
report("a[..., arr] = take(arr, axis=-1)", r6.shape == (3, 4, 2) and eq(r6, [[[r[0], r[1]] for r in s] for s in L3]))
x5 = np.zeros((10, 20, 30, 40, 50), dtype=np.int8)
ind1 = np.zeros((2, 3, 4), dtype=np.intp); ind2 = np.zeros((1, 3, 1), dtype=np.intp)
report("doc shapes: x[:, ind_1, ind_2] -> (10,2,3,4,40,50); x[:, ind_1, :, ind_2] -> (2,3,4,10,30,50)", x5[:, ind1, ind2].shape == (10, 2, 3, 4, 40, 50) and x5[:, ind1, :, ind2].shape == (2, 3, 4, 10, 30, 50))
report("doc: x[..., ind, :] shape (10, 2, 5, 2, 30) for x (10,20,30), ind (2,5,2)", np.zeros((10, 20, 30))[..., np.zeros((2, 5, 2), int), :].shape == (10, 2, 5, 2, 30))
mask2 = rs.rand(3, 4) > 0.5
rb = a3[mask2]
report("boolean mask with fewer dims (3,4) on (3,4,5): result (count, 5), rows in C order of True positions",
       rb.shape == (int(mask2.sum()), 5) and eq(rb, [L3[i][j] for i, j in cidx((3, 4)) if mask2[i, j]]))
mask1 = np.array([True, False, True])
report("1-D boolean on axis 0 = nonzero index; combined with a slice and an int array", eq(a3[mask1], [L3[0], L3[2]]) and eq(a3[mask1, :, [0, 4]], [[L3[0][j][0] for j in range(4)], [L3[2][j][4] for j in range(4)]]))
report("boolean mask of wrong length raises IndexError", raises(lambda: a3[np.array([True, False])], IndexError))
rep = np.zeros(5); rep[[1, 1, 3, 1]] = [10, 20, 30, 40]
report("repeated indices in assignment: final value is one of the assigned values ('no guarantee for the iteration order')", rep[1] in (10, 20, 40) and rep[3] == 30)
info(f"x[[1,1,3,1]] = [10,20,30,40] -> x[1] = {rep[1]} (last-wins observed: {rep[1] == 40}; the docs promise no order)")
xa = np.arange(0, 50, 10); xa[np.array([1, 1, 3, 1])] += 1
report("x[[1,1,3,1]] += 1 increments only once (docstring [0, 11, 20, 31, 40])", xa.tolist() == [0, 11, 20, 31, 40])
xb = np.arange(0, 50, 10); np.add.at(xb, [1, 1, 3, 1], 1)
report("np.add.at accumulates repeated indices ([0, 13, 20, 31, 40])", xb.tolist() == [0, 13, 20, 31, 40])
xc = np.zeros((3, 3)); np.add.at(xc, ([0, 0, 2], [1, 1, 0]), [1.0, 2.0, 5.0])
report("np.add.at with a tuple of index arrays and values", xc.tolist() == [[0, 3, 0], [0, 0, 0], [5, 0, 0]])
xd = np.ones(4); np.multiply.at(xd, [0, 0, 2], 3.0); np.negative.at(xd, [1, 1])
report("np.multiply.at accumulates; unary ufunc.at (negative twice = identity)", xd.tolist() == [9.0, 1.0, 3.0, 1.0])
report("negative indices count from the end; out-of-bounds raise IndexError (int and array)",
       a3[-1, -1, -1] == 59 and a3[[-3]].tolist() == [L3[0]] and raises(lambda: a3[3], IndexError) and raises(lambda: a3[[0, 3]], IndexError) and raises(lambda: a3[0, 0, -6], IndexError))
report("empty index array: a[[]] shape (0, 4, 5); a[:, []] shape (3, 0, 5); on an int array dtype preserved",
       a3[[]].shape == (0, 4, 5) and a3[:, []].shape == (3, 0, 5) and a3[np.array([], dtype=int)].dtype == a3.dtype)
report("float index arrays raise IndexError", raises(lambda: a3[np.array([0.0])], IndexError))
report("advanced indexing returns a copy, basic slicing a view", not np.shares_memory(a3[[0, 1]], a3) and np.shares_memory(a3[0:2], a3))
report("x[()] of a 0-d array returns a scalar; x[...] a 0-d view", np.isscalar(np.array(3)[()]) and np.array(3)[...].shape == ())

# ====================================================================================
print("---- nonzero / argwhere / where")
# ====================================================================================
nz = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
report("nonzero: row-major (C) order indices per dimension (docstring)", [t.tolist() for t in np.nonzero(nz)] == [[0, 1, 2, 2], [0, 1, 0, 1]])
if V >= (2, 1):
    report("2.1+: nonzero on a 0-d array raises ValueError (deprecated since 1.17)", raises(lambda: np.nonzero(np.array(1)), ValueError) and raises(lambda: np.array(0).nonzero(), ValueError))
else:
    w1, r1_ = warns(lambda: np.nonzero(np.array(1)), DeprecationWarning)
    report("1.17-2.0: nonzero on a 0-d array warns DeprecationWarning and behaves as atleast_1d", w1 and r1_[0].tolist() == [0] and quiet(lambda: np.nonzero(np.array(0)))[0].tolist() == [])
aw = np.argwhere(np.arange(6).reshape(2, 3) > 1)
report("argwhere: (N, ndim) grouped by element (docstring [[0,2],[1,0],[1,1],[1,2]])", aw.tolist() == [[0, 2], [1, 0], [1, 1], [1, 2]])
report("argwhere on 0-d: 'produces a result of the correct shape for a 0D array' -> (1, 0) / (0, 0)", np.argwhere(np.array(1)).shape == (1, 0) and np.argwhere(np.array(0)).shape == (0, 0))
report("argwhere on an empty array -> (0, ndim)", np.argwhere(np.zeros((0, 3))).shape == (0, 2))
c_ = np.array([True, False, True])
report("where 3-arg: result dtype = result_type(x, y) (int8 array, float32 array -> float32)", np.where(c_, np.array([1, 2, 3], np.int8), np.array([1, 2, 3], np.float32)).dtype == np.float32)
report("where 3-arg: int64 array and float python scalar -> float64; values chosen elementwise", (lambda r: r.dtype == np.float64 and r.tolist() == [1.0, 0.5, 3.0])(np.where(c_, np.array([1, 2, 3]), 0.5)))
wu = np.where(c_, np.array([1, 2, 3], np.uint8), 7)
report("where(uint8 array, python int 7) stays uint8 (both value-based 1.x and NEP 50 2.x)", wu.dtype == np.uint8)
if NP2:
    def wval(f):
        try: r_ = f(); return f"{r_.dtype}:{r_.tolist()}"
        except Exception as e_: return type(e_).__name__
    w300 = wval(lambda: np.where(c_, np.array([1, 2, 3], np.uint8), 300)); wm129 = wval(lambda: np.where(c_, np.array([1, 2, 3], np.int8), -129))
    info(f"2.x where(c, uint8 array, 300) -> {w300}; where(c, int8 array, -129) -> {wm129}; uint8 array + 300 -> {exc_name(lambda: np.array([1], np.uint8) + 300)}")
    report("2.x NEP 50 (weak Python int): where(c, uint8 array, 300) / (int8 array, -129) raise OverflowError (NEP 50 [T5] '300 cannot be converted to uint8')",
           w300 == "OverflowError" and wm129 == "OverflowError", f"got {w300} / {wm129}")
else:
    report("1.x value-based casting: where(uint8 array, 300) -> uint16 with the exact value", (lambda r: r.dtype == np.uint16 and r.tolist() == [1, 300, 3])(np.where(c_, np.array([1, 2, 3], np.uint8), 300)))
report("where with only x raises ValueError ('either both or neither of x and y should be given')", raises(lambda: np.where(c_, 1), ValueError))
report("where 1-arg = nonzero", [t.tolist() for t in np.where(nz)] == [t.tolist() for t in np.nonzero(nz)])
report("where broadcasting (3,1) cond with (4,) x", np.where(np.array([[True], [False], [True]]), np.arange(4), -1).tolist() == [[0, 1, 2, 3], [-1] * 4, [0, 1, 2, 3]])

# ====================================================================================
print("---- apply_along_axis / vectorize / frompyfunc")
# ====================================================================================
b_ = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
report("apply_along_axis scalar result: axis removed (docstring my_func -> [4., 5., 6.])", np.apply_along_axis(lambda a: (a[0] + a[-1]) * 0.5, 0, b_).tolist() == [4.0, 5.0, 6.0])
report("apply_along_axis 1-D result replaces the axis (sorted rows)", np.apply_along_axis(sorted, 1, np.array([[8, 1, 7], [4, 3, 9], [5, 2, 6]])).tolist() == [[1, 7, 8], [3, 4, 9], [2, 5, 6]])
dd = np.apply_along_axis(np.diag, -1, b_)
report("apply_along_axis 2-D result: the axis is replaced by the result's dims (docstring (3,3,3))", dd.shape == (3, 3, 3) and dd[1].tolist() == [[4, 0, 0], [0, 5, 0], [0, 0, 6]])
rr = np.apply_along_axis(lambda r: r[0] if r[0] == 0 else r[0] + 0.5, 1, np.arange(6).reshape(3, 2))
info(f"apply_along_axis where the first call returns int 0 and later calls floats -> {rr.tolist()} dtype {rr.dtype} (output buffer is allocated from the first result's dtype; not documented)")
report("apply_along_axis pitfall recorded: output dtype follows the FIRST call (later floats truncated)", rr.dtype.kind in "iu" and rr.tolist() == [0, 2, 4])
report("apply_along_axis on an axis of length 0 raises ValueError ('Cannot apply_along_axis when any iteration dimensions are 0')", raises(lambda: np.apply_along_axis(np.sum, 0, np.zeros((2, 0))), ValueError))
aa3 = np.apply_along_axis(np.cumsum, 1, A234)
report("apply_along_axis 3-D axis=1 = per-fibre cumsum", eq(aa3, [[[sum(L234[i][k][j] for k in range(r + 1)) for j in range(4)] for r in range(3)] for i in range(2)]))
calls = []
def f_calls(x):
    calls.append(x); return x * 2
vf = np.vectorize(f_calls); outv = vf([1, 2, 3])
report("vectorize without otypes calls the function on the first element one extra time (documented: cache=True prevents 'calling the function twice')", len(calls) == 4 and outv.tolist() == [2, 4, 6], str(calls))
calls.clear(); np.vectorize(f_calls, cache=True)([1, 2, 3])
report("vectorize cache=True calls the function exactly once per element", len(calls) == 3)
calls.clear(); np.vectorize(f_calls, otypes=[int])([1, 2, 3])
report("vectorize with otypes calls once per element", len(calls) == 3)
vp = np.vectorize(lambda x: 0 if x == 0 else x + 0.5)
r_ = vp([0, 1, 2])
report("vectorize first-call inference pitfall: 'output type determined by calling the function with the first element' -> int, fractions lost", r_.dtype.kind in "iu" and r_.tolist() == [0, 1, 2], str(r_.tolist()))
report("vectorize otypes=[float] fixes it ([0.0, 1.5, 2.5])", np.vectorize(lambda x: 0 if x == 0 else x + 0.5, otypes=[float])([0, 1, 2]).tolist() == [0.0, 1.5, 2.5])
report("vectorize otypes as a typecode string 'd' and multiple outputs", (lambda o: o[0].dtype == np.float64 and o[1].dtype == np.int_ and o[1].tolist() == [1, 4])(np.vectorize(lambda x: (x / 2, x * x), otypes="dl")([1, 2])))
def mypoly(p_, x_):
    _p = list(p_); res = 0
    for c__ in _p: res = res * x_ + c__
    return res
vpoly = np.vectorize(mypoly, excluded=["p_"])
report("vectorize excluded by keyword name: p not vectorized (docstring polyval: [3, 4, 1 ... ])", vpoly(p_=[1, 2, 3], x_=[0, 1]).tolist() == [3, 6])
vpoly2 = np.vectorize(mypoly); vpoly2.excluded.add(0)
report("vectorize excluded by position (excluded.add(0))", vpoly2([1, 2, 3], x_=[0, 1]).tolist() == [3, 6])
pearson = np.vectorize(lambda a_, b_: float(np.corrcoef(a_, b_)[0, 1]), signature="(n),(n)->()")
report("vectorize signature '(n),(n)->()' loops over the leading dims (docstring pearsonr)", pearson([[0, 1, 2, 3]], [[1, 2, 3, 4], [4, 3, 2, 1]]).shape == (2,) and np.allclose(pearson([[0, 1, 2, 3]], [[1, 2, 3, 4], [4, 3, 2, 1]]), [1.0, -1.0], atol=1e-14))
conv = np.vectorize(np.convolve, signature="(n),(m)->(k)")
report("vectorize signature '(n),(m)->(k)' output core dim from the result (docstring convolve shape (3, 5))", conv(np.eye(4), [1, 2, 1]).shape == (4, 6))
report("vectorize signature: mismatched core dims raise ValueError", raises(lambda: pearson([1, 2, 3], [1, 2]), ValueError))
report("vectorize of an empty input without otypes raises ValueError ('cannot call vectorize on size 0 inputs unless otypes is set')", raises(lambda: np.vectorize(lambda x: x)([]), ValueError) and np.vectorize(lambda x: x, otypes=[float])([]).shape == (0,))
ofp = np.frompyfunc(lambda x, y: x + y, 2, 1)
fr = ofp(np.array([1, 2]), np.array([3, 4]))
report("frompyfunc returns an object-dtype array (docstring 'always returns PyObject arrays')", fr.dtype == object and fr.tolist() == [4, 6])
report("frompyfunc ufunc attributes nin / nout / identity kw", ofp.nin == 2 and ofp.nout == 1 and np.frompyfunc(operator.add, 2, 1, identity=0).reduce(np.array([], dtype=object)) == 0)
report("frompyfunc with Fractions keeps exact Python objects", np.frompyfunc(lambda x: x / 3, 1, 1)(np.array([F(1), F(2)], dtype=object)).tolist() == [F(1, 3), F(2, 3)])

# ====================================================================================
print("---- copyto / shares_memory / trim_zeros / sliding_window_view / as_strided / array_equal")
# ====================================================================================
dst = np.zeros(4, dtype=np.int64)
report("copyto default casting='same_kind' rejects float -> int (TypeError)", raises(lambda: np.copyto(dst, np.array([1.5, 2.5, 3.5, 4.5])), TypeError))
np.copyto(dst, np.array([1.7, -2.7, 3.2, 4.9]), casting="unsafe")
report("copyto casting='unsafe' truncates toward zero", dst.tolist() == [1, -2, 3, 4])
dst = np.zeros(4); np.copyto(dst, np.array([1.0, 2.0, 3.0, 4.0]), where=[True, False, True, False])
report("copyto where= copies only where True", dst.tolist() == [1.0, 0.0, 3.0, 0.0])
dst = np.zeros((2, 3)); np.copyto(dst, np.arange(3.0))
report("copyto broadcasts src to dst", dst.tolist() == [[0, 1, 2], [0, 1, 2]])
report("copyto casting='no' with float32 -> float64 raises TypeError; 'safe' allows it", raises(lambda: np.copyto(np.zeros(2), np.zeros(2, np.float32), casting="no"), TypeError) and np.copyto(np.zeros(2), np.zeros(2, np.float32), casting="safe") is None)
info("copyto(uint8, 300) -> " + str(exc_name(lambda: np.copyto(np.zeros(2, np.uint8), 300)) or (lambda d: (np.copyto(d, 300), d.tolist())[1])(np.zeros(2, np.uint8))))
xs_ = np.arange(10)
report("shares_memory exact: x[::2] and x[1::2] do not share; may_share_memory (bounds) says they may",
       not np.shares_memory(xs_[::2], xs_[1::2]) and np.may_share_memory(xs_[::2], xs_[1::2]))
report("shares_memory overlapping slices True; disjoint halves False for both", np.shares_memory(xs_[:6], xs_[4:]) and not np.shares_memory(xs_[:5], xs_[5:]) and not np.may_share_memory(xs_[:5], xs_[5:]))
def sm0(a_, b_):
    try: return np.shares_memory(a_, b_, max_work=0)
    except Exception as e_: return type(e_).__name__
m0 = [sm0(xs_[::2], xs_[1::2]), sm0(xs_[:6], xs_[4:]), sm0(xs_[:5], xs_[5:])]
report("shares_memory max_work=0: 'Only the memory bounds of a and b are checked." + (" This is equivalent to using may_share_memory()' (2.x docstring)" if NP2 else "' (1.x docstring, max_work=MAY_SHARE_BOUNDS = 0)"),
       m0 == [np.may_share_memory(xs_[::2], xs_[1::2]), np.may_share_memory(xs_[:6], xs_[4:]), np.may_share_memory(xs_[:5], xs_[5:])], f"got {m0}, may_share_memory gives [True, True, False]")
report("shares_memory max_work=1 (finite effort) solves the interleaved case exactly: False", np.shares_memory(xs_[::2], xs_[1::2], max_work=1) is False or np.shares_memory(xs_[::2], xs_[1::2], max_work=1) == False)
report("shares_memory of an array with a copy is False", not np.shares_memory(xs_, xs_.copy()))
tz = np.array((0, 0, 0, 1, 2, 3, 0, 2, 1, 0))
report("trim_zeros docstring: default 'fb' -> [1,2,3,0,2,1]; 'b' -> [0,0,0,1,2,3,0,2,1]", np.trim_zeros(tz).tolist() == [1, 2, 3, 0, 2, 1] and np.trim_zeros(tz, "b").tolist() == [0, 0, 0, 1, 2, 3, 0, 2, 1])
report("trim_zeros 'f'; all-zeros -> empty; list input returns a list", np.trim_zeros(tz, "f").tolist() == [1, 2, 3, 0, 2, 1, 0] and np.trim_zeros(np.zeros(4)).shape == (0,) and np.trim_zeros([0, 1, 2, 0]) == [1, 2])
report("trim_zeros treats -0.0 and False as zero, NaN as non-zero", np.trim_zeros(np.array([-0.0, 1.0, 0.0])).tolist() == [1.0] and np.trim_zeros(np.array([np.nan, 0.0])).shape == (1,))
if V >= (2, 2):
    t2 = np.array([[0, 0, 2, 3, 0, 0], [0, 1, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0]])
    report("2.2+: trim_zeros on N-D trims the bounding box (docstring [[0,2,3],[1,0,3]]) and axis=-1", np.trim_zeros(t2).tolist() == [[0, 2, 3], [1, 0, 3]] and np.trim_zeros(t2, axis=-1).tolist() == [[0, 2, 3], [1, 0, 3], [0, 0, 0]])
from numpy.lib.stride_tricks import sliding_window_view, as_strided
sw = sliding_window_view(np.arange(6), 3)
report("sliding_window_view 1-D: shape (n-w+1, w), row i = x[i:i+w]", sw.shape == (4, 3) and sw.tolist() == [list(range(i, i + 3)) for i in range(4)])
x2d = np.arange(12).reshape(3, 4); X2d = x2d.tolist()
sw2 = sliding_window_view(x2d, (2, 2))
report("sliding_window_view 2-D (2,2): shape (2,3,2,2), windows = sub-blocks", sw2.shape == (2, 3, 2, 2) and eq(sw2, build((2, 3, 2, 2), lambda t: X2d[t[0] + t[2]][t[1] + t[3]])))
sw3 = sliding_window_view(x2d, 3, axis=1)
report("sliding_window_view axis=1: window dim appended last (3, 2, 3)", sw3.shape == (3, 2, 3) and eq(sw3, build((3, 2, 3), lambda t: X2d[t[0]][t[1] + t[2]])))
sw4 = sliding_window_view(x2d, (2, 3), axis=(0, 1))
report("sliding_window_view axis tuple; repeated axis windows along the same axis twice (docstring (2,2) on axis (0,0) -> shape (2,4,2,2))",
       sw4.shape == (2, 2, 2, 3) and sliding_window_view(x2d, (2, 2), axis=(0, 0)).shape == (1, 4, 2, 2))
report("sliding_window_view default writeable=False (write raises ValueError); a view (shares memory)", not sw.flags.writeable and raises(lambda: sw.__setitem__((0, 0), 9), ValueError) and np.shares_memory(sw, sw.base if sw.base is not None else sw))
src_w = np.arange(5); sww = sliding_window_view(src_w, 3, writeable=True); sww[0, 2] = 99
report("sliding_window_view writeable=True writes through to the original (shared locations)", src_w[2] == 99 and sww[1, 1] == 99 and sww[2, 0] == 99)
report("sliding_window_view window larger than the axis raises ValueError; negative window raises ValueError",
       raises(lambda: sliding_window_view(np.arange(3), 4), ValueError) and raises(lambda: sliding_window_view(np.arange(3), -1), ValueError))
report("sliding_window_view window_shape length != axis count raises ValueError", raises(lambda: sliding_window_view(x2d, (2, 2, 2)), ValueError))
it = np.arange(10, dtype=np.int64)
ast = as_strided(it, shape=(4, 3), strides=(16, 8))
report("as_strided: shape (4,3) strides (16,8) on int64 -> rows [2i, 2i+1, 2i+2]", ast.tolist() == [[2 * i, 2 * i + 1, 2 * i + 2] for i in range(4)])
ast0 = as_strided(it[:1], shape=(3, 2), strides=(0, 0))
report("as_strided zero strides broadcast one element", ast0.tolist() == [[0, 0]] * 3)
report("as_strided writeable=False returns a read-only view", not as_strided(it, shape=(2,), strides=(8,), writeable=False).flags.writeable)
report("array_equal: shape and values; equal_nan=True treats NaN == NaN; default False",
       np.array_equal([1, 2], [1, 2]) and not np.array_equal([1, 2], [1, 2, 3]) and not np.array_equal([1, 2], [[1, 2]])
       and np.array_equal([1, np.nan], [1, np.nan], equal_nan=True) and not np.array_equal([1, np.nan], [1, np.nan]))
info(f"array_equal([nan+1j],[1+nanj], equal_nan=True) = {np.array_equal(np.array([complex(np.nan, 1)]), np.array([complex(1, np.nan)]), equal_nan=True)} (docs: NaN considered equal; complex rule not stated)")
report("array_equal with equal_nan on int arrays works (no isnan TypeError)", np.array_equal(np.array([1, 2]), np.array([1, 2]), equal_nan=True))
report("array_equiv: broadcastable and equal -> True (docstring [1,2] vs [[1,2],[1,2]]); [1,2] vs [[1,2,1,2],...] False",
       np.array_equiv([1, 2], [[1, 2], [1, 2]]) and not np.array_equiv([1, 2], [[1, 2, 1, 2], [1, 2, 1, 2]]) and not np.array_equiv([1, 2], [[1, 2], [1, 3]]))
report("array_equiv of non-broadcastable shapes returns False (no exception)", np.array_equiv([1, 2, 3], [1, 2]) is False or np.array_equiv([1, 2, 3], [1, 2]) == False)

print(f"#### elapsed {time.time() - T0:.1f} s")
