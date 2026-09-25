#!/usr/bin/env python
"""Preprocessing (PolynomialFeatures, SplineTransformer, Binarizer, LabelBinarizer,
MultiLabelBinarizer, OrdinalEncoder, OneHotEncoder deeper options, TargetEncoder,
MaxAbsScaler, Normalizer, KernelCenterer, FunctionTransformer, PowerTransformer
yeo-johnson, QuantileTransformer normal, add_dummy_feature, the function forms,
RobustScaler options, StandardScaler on sparse), feature_extraction (text, hashing,
dict, image), impute (KNN, Iterative, MissingIndicator, SimpleImputer options) and
compose / pipeline -- every check against an independent recomputation (Fraction,
mpmath, a plain-Python reference implementation such as a Cox-de Boor B-spline
evaluator, or a documented invariant / docstring example)."""
import sys, math, warnings, itertools, inspect, re, unicodedata, collections, tempfile, shutil, os
sys.path.insert(0, ".")
from _synth import *
import mpmath
from mpmath import mp, mpf
mp.dps = 30
import scipy.sparse as sp
from sklearn.preprocessing import (PolynomialFeatures, SplineTransformer, Binarizer, binarize, LabelBinarizer,
                                   label_binarize, MultiLabelBinarizer, OrdinalEncoder, OneHotEncoder, MaxAbsScaler,
                                   maxabs_scale, Normalizer, normalize, KernelCenterer, FunctionTransformer,
                                   PowerTransformer, power_transform, QuantileTransformer, quantile_transform,
                                   add_dummy_feature, scale, minmax_scale, robust_scale, StandardScaler, MinMaxScaler,
                                   RobustScaler)
from sklearn.feature_extraction.text import (CountVectorizer, TfidfTransformer, TfidfVectorizer, HashingVectorizer,
                                             ENGLISH_STOP_WORDS)
from sklearn.feature_extraction import DictVectorizer, FeatureHasher
from sklearn.feature_extraction.image import (extract_patches_2d, reconstruct_from_patches_2d, grid_to_graph,
                                              img_to_graph, PatchExtractor)
from sklearn.utils import murmurhash3_32
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import KNNImputer, IterativeImputer, MissingIndicator, SimpleImputer
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor, make_column_transformer
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline, make_union
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, BayesianRidge
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold, StratifiedKFold
banner(); warnings.filterwarnings("ignore")
V = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
rs = np.random.RandomState(13)

def allclose(a, b, rel=1e-9, abs_=1e-12):
    a = np.asarray(a, float); b = np.asarray(b, float)
    if a.shape != b.shape: return False
    both_nan = np.isnan(a) & np.isnan(b)
    d = np.abs(a - b) <= abs_ + rel * np.maximum(np.abs(a), np.abs(b))
    return bool(np.all(d | both_nan))

def dense(M):
    return M.toarray() if sp.issparse(M) else np.asarray(M)

def has_param(cls, name):
    return name in inspect.signature(cls.__init__).parameters

def caught(fn, cat=Warning):
    """Run fn, return (result, [warnings of category cat])."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        out = fn()
    return out, [x for x in w if issubclass(x.category, cat)]

def ppf(p):
    """Standard normal quantile, independent of scipy (mpmath erfinv)."""
    return float(mpmath.sqrt(2) * mpmath.erfinv(2 * mpf(p) - 1))

def fr_solve(A, b):
    """Exact Gaussian elimination on Fractions."""
    n = len(A); M = [list(map(F, A[i])) + [F(b[i])] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0); M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]; M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]

def ols_exact(X, y):
    """Exact least squares with intercept: returns (intercept, coef) as Fractions."""
    A = [[F(1)] + [F(v) for v in row] for row in X]; p = len(A[0])
    AtA = [[sum(A[k][i] * A[k][j] for k in range(len(A))) for j in range(p)] for i in range(p)]
    Aty = [sum(A[k][i] * F(y[k]) for k in range(len(A))) for i in range(p)]
    beta = fr_solve(AtA, Aty); return beta[0], beta[1:]

# =============================================================================
print("== preprocessing: PolynomialFeatures")
XP = np.array([[2, 3, 5], [-1, 4, 0], [7, -2, 1], [0, 0, 0], [0.5, -1.5, 2.25]], float)
def poly_truth(X, degree, interaction_only=False, include_bias=True):
    """Column order as documented: bias, then all combinations of increasing degree
    (combinations_with_replacement order: [1, a, b, a^2, ab, b^2] for [a, b])."""
    dmin, dmax = degree if isinstance(degree, tuple) else (0, degree)
    n = X.shape[1]; comb = itertools.combinations if interaction_only else itertools.combinations_with_replacement
    combos = [()] if include_bias else []
    for d in range(max(1, dmin), dmax + 1): combos.extend(comb(range(n), d))
    powers = [[c.count(j) for j in range(n)] for c in combos]
    out = [[math.prod(F(x[j]) ** p[j] for j in range(n)) for p in powers] for x in X]
    return np.array(powers), np.array([[float(v) for v in row] for row in out])
pf = PolynomialFeatures(degree=2).fit(XP); pw, Zt = poly_truth(XP, 2)
print(f"   degree=2 powers_ rows: {pf.powers_.tolist()}")
report("PolynomialFeatures(degree=2) powers_ = documented order [1, a, b, c, a^2, ab, ac, b^2, bc, c^2]", np.array_equal(pf.powers_, pw))
report("PolynomialFeatures(degree=2) transform = exact products (Fraction)", allclose(pf.transform(XP), Zt, 1e-13))
report("PolynomialFeatures(degree=2) n_output_features_ = C(n+d, d) = 10", pf.n_output_features_ == 10, f"({pf.n_output_features_})")
report("PolynomialFeatures get_feature_names_out(['a','b','c']) = ['1','a','b','c','a^2','a b','a c','b^2','b c','c^2']",
       pf.get_feature_names_out(["a", "b", "c"]).tolist() == ["1", "a", "b", "c", "a^2", "a b", "a c", "b^2", "b c", "c^2"], f"({pf.get_feature_names_out(['a', 'b', 'c']).tolist()})")
p3 = PolynomialFeatures(degree=3, interaction_only=True).fit(XP); pw3, Z3 = poly_truth(XP, 3, True)
report("PolynomialFeatures(degree=3, interaction_only=True): 'products of at most degree distinct features' -> [1, a, b, c, ab, ac, bc, abc] (powers_ and values exact)",
       np.array_equal(p3.powers_, pw3) and allclose(p3.transform(XP), Z3, 1e-13) and p3.n_output_features_ == 8, f"(powers_ {p3.powers_.tolist()})")
pnb = PolynomialFeatures(degree=2, include_bias=False).fit(XP); pwn, Zn = poly_truth(XP, 2, False, False)
report("PolynomialFeatures(include_bias=False) drops only the all-zero-power column", np.array_equal(pnb.powers_, pwn) and allclose(pnb.transform(XP), Zn, 1e-13))
pt = PolynomialFeatures(degree=(2, 3)).fit(XP); pwt, Ztt = poly_truth(XP, (2, 3))
report("PolynomialFeatures(degree=(2,3)): only degree-2 and degree-3 terms (plus bias) in documented order", np.array_equal(pt.powers_, pwt) and allclose(pt.transform(XP), Ztt, 1e-13) and pt.n_output_features_ == 1 + 6 + 10, f"(n_out {pt.n_output_features_})")
p01 = PolynomialFeatures(degree=(0, 2)).fit(XP); p11 = PolynomialFeatures(degree=(1, 2)).fit(XP)
report("PolynomialFeatures: 'min_degree=0 and min_degree=1 are equivalent' (documented)", np.array_equal(p01.powers_, p11.powers_) and allclose(p01.transform(XP), p11.transform(XP)))
pti = PolynomialFeatures(degree=(2, 3), interaction_only=True, include_bias=False).fit(XP); pwti, Zti = poly_truth(XP, (2, 3), True, False)
report("PolynomialFeatures(degree=(2,3), interaction_only, no bias) = [ab, ac, bc, abc]", np.array_equal(pti.powers_, pwti) and allclose(pti.transform(XP), Zti, 1e-13))
for fmt in ("csr", "csc"):
    Xs = sp.csr_matrix(XP) if fmt == "csr" else sp.csc_matrix(XP)
    Zs = PolynomialFeatures(degree=3).fit_transform(Xs); _, Z3f = poly_truth(XP, 3)
    report(f"PolynomialFeatures(degree=3) on {fmt} sparse input: sparse output with the same values as the dense expansion", sp.issparse(Zs) and allclose(dense(Zs), Z3f, 1e-13), f"(format {Zs.format})")
    Zs2 = PolynomialFeatures(degree=2, interaction_only=True).fit_transform(Xs); _, Z2i = poly_truth(XP, 2, True)
    report(f"PolynomialFeatures(interaction_only) on {fmt} input equals exact values", allclose(dense(Zs2), Z2i, 1e-13))
Z32 = PolynomialFeatures(degree=2).fit_transform(XP.astype(np.float32))
report("PolynomialFeatures on float32 input: output dtype float32 and values within 1e-6 relative of exact", Z32.dtype == np.float32 and allclose(Z32, Zt, 1e-6))
p0 = PolynomialFeatures(degree=0).fit(XP)
report("PolynomialFeatures(degree=0, include_bias=True) = a single column of ones", p0.transform(XP).shape == (5, 1) and np.all(p0.transform(XP) == 1))
try:
    PolynomialFeatures(degree=0, include_bias=False).fit(XP); report("PolynomialFeatures(degree=0, include_bias=False) raises ValueError (empty output)", False)
except ValueError: report("PolynomialFeatures(degree=0, include_bias=False) raises ValueError (empty output)", True)
pF = PolynomialFeatures(degree=2, order="F").fit_transform(XP)
report("PolynomialFeatures(order='F') gives the same values, Fortran-contiguous", allclose(pF, Zt, 1e-13) and pF.flags.f_contiguous)
XP1 = XP[:, :1]; p1 = PolynomialFeatures(degree=4).fit(XP1); _, Z1 = poly_truth(XP1, 4)
report("PolynomialFeatures single feature degree=4 = [1, x, x^2, x^3, x^4]", allclose(p1.transform(XP1), Z1, 1e-13) and p1.get_feature_names_out().tolist() == ["1", "x0", "x0^2", "x0^3", "x0^4"])

# =============================================================================
print("== preprocessing: SplineTransformer (Cox-de Boor reference in Fractions)")
def bspline_basis(t, k, x, right_closed_at=None):
    """All B_{i,k}(x) on the knot vector t (Cox-de Boor recursion, exact Fractions).
    Half-open intervals [t_i, t_{i+1}); at x == right_closed_at the last base interval is closed."""
    t = [F(v) for v in t]; x = F(x); m = len(t) - 1
    if right_closed_at is not None and x == right_closed_at:
        B = [1 if t[i] < x <= t[i + 1] else 0 for i in range(m)]
    else:
        B = [1 if t[i] <= x < t[i + 1] else 0 for i in range(m)]
    B = [F(v) for v in B]
    for d in range(1, k + 1):
        B = [((x - t[i]) / (t[i + d] - t[i]) * B[i] if t[i + d] != t[i] else 0)
             + ((t[i + d + 1] - x) / (t[i + d + 1] - t[i + 1]) * B[i + 1] if t[i + d + 1] != t[i + 1] else 0)
             for i in range(m - d)]
    return B
def bspline_deriv(t, k, x, right_closed_at=None):
    """B'_{i,k}(x) = k (B_{i,k-1}/(t_{i+k}-t_i) - B_{i+1,k-1}/(t_{i+k+1}-t_{i+1}))."""
    if k == 0: return [F(0)] * (len(t) - 1)
    tt = [F(v) for v in t]; Bl = bspline_basis(t, k - 1, x, right_closed_at); n = len(t) - k - 1
    return [k * ((Bl[i] / (tt[i + k] - tt[i]) if tt[i + k] != tt[i] else 0) - (Bl[i + 1] / (tt[i + k + 1] - tt[i + 1]) if tt[i + k + 1] != tt[i + 1] else 0)) for i in range(n)]
def lagrange(nodes, vals, x):
    s = F(0)
    for i, (xi, yi) in enumerate(zip(nodes, vals)):
        term = F(yi)
        for j, xj in enumerate(nodes):
            if j != i: term *= (F(x) - xj) / (xi - xj)
        s += term
    return s
def spline_truth(X1, base, degree, extrapolation, include_bias=True):
    """Spline basis values for a 1-D feature from base knots (Fractions).  Exterior knots as
    documented ('degree number of knots are added before the first knot, the same after the last
    knot'), spaced like the first / last knot interval (source comment); periodic knots wrap."""
    base = [F(b) for b in base]; nk = len(base); xmin, xmax = base[0], base[-1]
    if extrapolation == "periodic":
        period = xmax - xmin
        t = [b - period for b in base[-(degree + 1):-1]] + base + [b + period for b in base[1:degree + 1]]; ns = nk - 1
    else:
        dmin = base[1] - base[0]; dmax = base[-1] - base[-2]
        t = [base[0] - (degree - i) * dmin for i in range(degree)] + base + [base[-1] + (i + 1) * dmax for i in range(degree)]; ns = nk + degree - 1
    rows = []
    for xv in X1:
        x = F(xv)
        if extrapolation == "periodic":
            xm = xmin + (x - xmin) % period
            full = bspline_basis(t, degree, xm)
            row = [full[j] + (full[ns + j] if j < degree else 0) for j in range(ns)]
        else:
            xc = min(max(x, xmin), xmax); B = bspline_basis(t, degree, xc, right_closed_at=xmax)
            if extrapolation == "constant" or xmin <= x <= xmax: row = B
            elif extrapolation == "linear":
                dB = bspline_deriv(t, degree, xc, right_closed_at=xmax); row = [B[j] + (x - xc) * dB[j] for j in range(ns)]
            elif extrapolation == "continue":
                a, b = (base[0], base[1]) if x < xmin else (base[-2], base[-1])
                nodes = [a + (b - a) * F(i + 1, degree + 2) for i in range(degree + 1)]
                vals = [bspline_basis(t, degree, nd, right_closed_at=xmax) for nd in nodes]
                row = [lagrange(nodes, [v[j] for v in vals], x) for j in range(ns)]
        rows.append(row)
    if not include_bias: rows = [r[:-1] for r in rows]
    return np.array([[float(v) for v in r] for r in rows])
def pct_exact(vals, p):
    """numpy 'linear' percentile in Fractions."""
    s = sorted(F(v) for v in vals); pos = F(p) * (len(s) - 1); lo = int(math.floor(pos)); hi = min(lo + 1, len(s) - 1)
    return s[lo] + (pos - lo) * (s[hi] - s[lo])

Xsp = np.array([0.0, 1, 2, 3, 4.5, 6, 7.25, 9, 10, 12, 11.5, 2.75, 8])
Xout = np.array([-3.0, -0.5, 0.0, 2.5, 4.0, 8.0, 12.0, 13.0, 20.0])
base_u = [F(0), F(4), F(8), F(12)]
ex = SplineTransformer(degree=2, n_knots=3).fit_transform(np.arange(6).reshape(6, 1))
doc_ex = np.array([[0.5, 0.5, 0, 0], [0.18, 0.74, 0.08, 0], [0.02, 0.66, 0.32, 0], [0, 0.32, 0.66, 0.02], [0, 0.08, 0.74, 0.18], [0, 0, 0.5, 0.5]])
report("SplineTransformer docstring example (arange(6), degree=2, n_knots=3) reproduced to 2 decimals", allclose(np.round(ex, 2), doc_ex, 0, 1e-12) and allclose(ex, spline_truth(np.arange(6), [0, F(5, 2), 5], 2, "constant"), 1e-12))
for degree in (0, 1, 2, 3):
    for extr in ("constant", "linear", "continue", "periodic"):
        st = SplineTransformer(n_knots=4, degree=degree, knots="uniform", extrapolation=extr).fit(Xsp[:, None])
        Zin = st.transform(Xsp[:, None]); Tin = spline_truth(Xsp, base_u, degree, extr)
        To = spline_truth(Xout, base_u, degree, extr); err = ""
        try: Zo = st.transform(Xout[:, None])
        except Exception as e: Zo = np.full_like(To, np.nan); err = f"transform raised {type(e).__name__}: {e}"
        okin = allclose(Zin, Tin, 1e-12, 1e-12); oko = allclose(Zo, To, 1e-12, 1e-12) and not err
        nspl = 3 if extr == "periodic" else 3 + degree
        if degree == 1 and extr == "constant": print(f"   degree=1 constant: outside rows {Zo[[0, -1]].tolist()} truth {To[[0, -1]].tolist()}")
        report(f"SplineTransformer(degree={degree}, knots='uniform', extrapolation='{extr}'): basis values inside the knot range = Cox-de Boor (exact, 1e-12) and n_features_out_ = n_knots{'-1' if extr == 'periodic' else '+degree-1'} = {nspl}",
               okin and st.n_features_out_ == nspl, f"(max diff {np.max(np.abs(Zin - Tin)):.1e}, n_out {st.n_features_out_})")
        report(f"SplineTransformer(degree={degree}, extrapolation='{extr}'): values outside [min, max] follow the documented rule ('{ {'constant': 'value of the splines at min/max', 'linear': 'linear extrapolation', 'continue': 'splines extrapolated as is', 'periodic': 'periodicity = distance first-last knot'}[extr] }')",
               oko, err or f"(max diff {np.max(np.abs(Zo - To)):.1e})")
        if degree >= 1 and extr != "periodic":
            report(f"SplineTransformer(degree={degree}, '{extr}'): partition of unity inside the range (rows sum to 1)", allclose(Zin.sum(1), np.ones(len(Xsp)), 1e-12))
# quantile knots
stq = SplineTransformer(n_knots=4, degree=3, knots="quantile").fit(Xsp[:, None])
base_q = [pct_exact(Xsp, F(i, 3)) for i in range(4)]
print(f"   quantile base knots (library) {stq.bsplines_[0].t[3:7].tolist()}  exact percentiles {[float(b) for b in base_q]}")
report("SplineTransformer(knots='quantile'): base knots = percentiles at linspace(0,100,n_knots) (linear) and basis = Cox-de Boor on those knots (1e-9)",
       allclose(stq.bsplines_[0].t[3:7], [float(b) for b in base_q], 1e-12) and allclose(stq.transform(Xsp[:, None]), spline_truth(Xsp, base_q, 3, "constant"), 1e-9, 1e-12))
# array knots
kn = np.array([[0.0], [3.0], [5.0], [12.0]])
sta = SplineTransformer(degree=3, knots=kn, extrapolation="linear").fit(Xsp[:, None])
report("SplineTransformer(knots=array): given knots used as base knots ('directly specifies the sorted knot positions including the boundary knots'), n_knots ignored; values and linear extrapolation exact",
       allclose(sta.transform(Xsp[:, None]), spline_truth(Xsp, [0, 3, 5, 12], 3, "linear"), 1e-12) and allclose(sta.transform(Xout[:, None]), spline_truth(Xout, [0, 3, 5, 12], 3, "linear"), 1e-11) and sta.n_features_out_ == 6)
sta2 = SplineTransformer(degree=2, knots=kn, extrapolation="periodic").fit(Xsp[:, None])
report("SplineTransformer(knots=array non-uniform, periodic, degree=2): periodic wrap with period = last - first knot (exact)",
       allclose(sta2.transform(Xout[:, None]), spline_truth(Xout, [0, 3, 5, 12], 2, "periodic"), 1e-12) and sta2.n_features_out_ == 3)
try:
    SplineTransformer(knots=np.array([[0.0], [5.0], [3.0]])).fit(Xsp[:, None]); report("SplineTransformer(knots unsorted) raises ValueError", False)
except ValueError: report("SplineTransformer(knots unsorted) raises ValueError", True)
# include_bias=False
stb = SplineTransformer(n_knots=4, degree=3, include_bias=False).fit(Xsp[:, None]); stf = SplineTransformer(n_knots=4, degree=3).fit(Xsp[:, None])
report("SplineTransformer(include_bias=False): 'the last spline element inside the data range of a feature is dropped' -> columns = full[:, :-1], n_features_out_ = n_splines-1",
       allclose(stb.transform(Xsp[:, None]), stf.transform(Xsp[:, None])[:, :-1]) and stb.n_features_out_ == 5)
# two features: blocks per feature
X2 = np.column_stack([Xsp, 3 * Xsp - 7])
st2 = SplineTransformer(n_knots=4, degree=3, include_bias=False).fit(X2)
T2 = np.hstack([spline_truth(Xsp, base_u, 3, "constant", False), spline_truth(3 * Xsp - 7, [-7, 5, 17, 29], 3, "constant", False)])
report("SplineTransformer on 2 features: output = [splines of x0 | splines of x1], feature names x0_sp_0..x0_sp_4, x1_sp_0..", allclose(st2.transform(X2), T2, 1e-12) and st2.get_feature_names_out().tolist() == [f"x{i}_sp_{j}" for i in range(2) for j in range(5)], f"({st2.get_feature_names_out().tolist()[:3]}...)")
if has_param(SplineTransformer, "sparse_output"):
    for extr in ("constant", "linear", "continue", "periodic"):
        sts = SplineTransformer(n_knots=4, degree=3, extrapolation=extr, sparse_output=True).fit(Xsp[:, None])
        Zs = sts.transform(Xout[:, None])
        report(f"SplineTransformer(sparse_output=True, '{extr}'): CSR output equal to the dense output (incl. extrapolated rows)", sp.issparse(Zs) and Zs.format == "csr" and allclose(dense(Zs), spline_truth(Xout, base_u, 3, extr), 1e-11), f"(format {Zs.format if sp.issparse(Zs) else 'dense'})")
else: print("   (SplineTransformer sparse_output not available in this build: skipped)")
try:
    SplineTransformer(n_knots=4, extrapolation="error").fit(Xsp[:, None]).transform(np.array([[13.0]])); report("SplineTransformer(extrapolation='error') raises ValueError for a value beyond the knots", False)
except ValueError: report("SplineTransformer(extrapolation='error') raises ValueError for a value beyond the knots", True)
ste = SplineTransformer(n_knots=4, extrapolation="error").fit(Xsp[:, None])
report("SplineTransformer(extrapolation='error') accepts the boundary values themselves", allclose(ste.transform(np.array([[0.0], [12.0]])), spline_truth([0, 12], base_u, 3, "constant"), 1e-12))
try:
    SplineTransformer(n_knots=3, degree=3, extrapolation="periodic").fit(Xsp[:, None]); report("SplineTransformer(periodic) with degree >= n_knots raises ValueError ('Periodic splines require degree < n_knots')", False)
except ValueError: report("SplineTransformer(periodic) with degree >= n_knots raises ValueError ('Periodic splines require degree < n_knots')", True)
st32 = SplineTransformer(n_knots=4, degree=3).fit(Xsp[:, None].astype(np.float32))
report("SplineTransformer on float32 input: values within 1e-6 of exact", allclose(st32.transform(Xsp[:, None].astype(np.float32)), spline_truth(Xsp, base_u, 3, "constant"), 1e-6, 1e-7))
if has_param(SplineTransformer, "sparse_output"):
    err = ""
    try:
        Z0s = SplineTransformer(n_knots=4, degree=0, extrapolation="constant", sparse_output=True).fit(Xsp[:, None]).transform(Xout[:, None])
        ok0 = allclose(dense(Z0s), spline_truth(Xout, base_u, 0, "constant"), 1e-12)
    except Exception as e: ok0 = False; err = f"raised {type(e).__name__}: {e}"
    report("SplineTransformer(degree=0, extrapolation='constant', sparse_output=True): rows beyond the knots = 'value of the splines at minimum and maximum' (bin indicator at min / max)", ok0, err or f"(rows for x=-3, 20: {dense(Z0s)[[0, -1]].tolist()} expected {spline_truth(Xout, base_u, 0, 'constant')[[0, -1]].tolist()})")

# =============================================================================
print("== preprocessing: Binarizer / binarize")
XB = np.array([[-1.0, 0.0, 0.5], [1.0, 2.0, -0.5], [0.0, 0.0, 0.0]])
for thr in (0.0, 0.5, -0.5, 2.0):
    Zb = Binarizer(threshold=thr).fit_transform(XB); Tb = (XB > thr).astype(float)
    report(f"Binarizer(threshold={thr}): 'values greater than the threshold map to 1, ... less than or equal to the threshold map to 0' (value == threshold -> 0)", np.array_equal(Zb, Tb) and np.array_equal(binarize(XB, threshold=thr), Tb))
Zbs = Binarizer(threshold=0.5).fit_transform(sp.csr_matrix(XB))
report("Binarizer on CSR input: sparse output with the same 0/1 values", sp.issparse(Zbs) and np.array_equal(dense(Zbs), (XB > 0.5).astype(float)))
try:
    Binarizer(threshold=-0.5).fit_transform(sp.csr_matrix(XB)); report("Binarizer(threshold<0) on sparse raises ValueError ('Threshold may not be less than 0 for operations on sparse matrices')", False)
except ValueError: report("Binarizer(threshold<0) on sparse raises ValueError ('Threshold may not be less than 0 for operations on sparse matrices')", True)
report("Binarizer keeps the input dtype (float32 in -> float32 out; int in -> int out)", Binarizer().fit_transform(XB.astype(np.float32)).dtype == np.float32 and Binarizer().fit_transform(np.array([[1, -2], [0, 3]])).dtype.kind == "i")

# =============================================================================
print("== preprocessing: LabelBinarizer / label_binarize / MultiLabelBinarizer")
lb = LabelBinarizer().fit([1, 2, 6, 4, 2])
report("LabelBinarizer docstring example: classes_ = [1, 2, 4, 6], transform([1, 6]) = [[1,0,0,0],[0,0,0,1]]", lb.classes_.tolist() == [1, 2, 4, 6] and lb.transform([1, 6]).tolist() == [[1, 0, 0, 0], [0, 0, 0, 1]])
ylb = ["c", "a", "b", "a", "d", "c"]; classes = sorted(set(ylb))
lb4 = LabelBinarizer(neg_label=-3, pos_label=5).fit(ylb); Ylb = lb4.transform(ylb)
Tlb = np.array([[5 if c == v else -3 for c in classes] for v in ylb])
report("LabelBinarizer(neg_label=-3, pos_label=5) multiclass: one column per sorted class, pos/neg values as given", lb4.classes_.tolist() == classes and np.array_equal(Ylb, Tlb) and Ylb.dtype.kind == "i", f"(dtype {Ylb.dtype})")
report("LabelBinarizer multiclass inverse_transform(transform(y)) = y", lb4.inverse_transform(Ylb).tolist() == ylb)
scores = np.array([[0.1, 0.9, 0.3, 0.2], [0.5, 0.4, 0.45, 0.1], [0.0, 0.0, 0.0, 1.0]])
report("LabelBinarizer multiclass inverse_transform on scores = argmax class ('Multiclass uses the maximal score instead of a threshold')", LabelBinarizer().fit(ylb).inverse_transform(scores).tolist() == ["b", "a", "d"])
lbb = LabelBinarizer().fit(["yes", "no", "no", "yes"]); Yb = lbb.transform(["yes", "no", "no", "yes"])
report("LabelBinarizer binary target: 'Binary targets transform to a column vector' [[1],[0],[0],[1]], classes_ = ['no','yes']", Yb.shape == (4, 1) and Yb.ravel().tolist() == [1, 0, 0, 1] and lbb.classes_.tolist() == ["no", "yes"])
lbb2 = LabelBinarizer(neg_label=-1, pos_label=1).fit(["yes", "no"])
report("LabelBinarizer(neg_label=-1, pos_label=1) binary: column of -1/1", lbb2.transform(["yes", "no", "no"]).ravel().tolist() == [1, -1, -1])
inv = lbb2.inverse_transform(np.array([[0.0], [0.1], [-0.1], [1.0], [-5.0]]))
report("LabelBinarizer binary inverse_transform: default threshold = (pos_label + neg_label)/2 = 0; 'value > threshold' -> positive class, value == threshold -> negative", inv.tolist() == ["no", "yes", "no", "yes", "no"], f"({inv.tolist()})")
inv2 = lbb2.inverse_transform(np.array([[0.5], [0.4], [0.6]]), threshold=0.5)
report("LabelBinarizer binary inverse_transform(threshold=0.5): strictly greater than the threshold is positive", inv2.tolist() == ["no", "no", "yes"], f"({inv2.tolist()})")
lbs = LabelBinarizer(sparse_output=True).fit(ylb); Ys = lbs.transform(ylb)
report("LabelBinarizer(sparse_output=True): CSR matrix with the same one-hot values", sp.issparse(Ys) and Ys.format == "csr" and np.array_equal(dense(Ys), np.array([[1 if c == v else 0 for c in classes] for v in ylb])))
report("LabelBinarizer(sparse_output=True) inverse_transform round trip", lbs.inverse_transform(Ys).tolist() == ylb)
try:
    LabelBinarizer(sparse_output=True, neg_label=-1).fit(ylb); report("LabelBinarizer(sparse_output=True, neg_label != 0) raises ValueError (documented in the error message: sparse output requires neg_label=0, pos_label != 0)", False)
except ValueError: report("LabelBinarizer(sparse_output=True, neg_label != 0) raises ValueError (documented in the error message: sparse output requires neg_label=0, pos_label != 0)", True)
try:
    LabelBinarizer(neg_label=1, pos_label=1).fit(ylb); report("LabelBinarizer(neg_label >= pos_label) raises ValueError", False)
except ValueError: report("LabelBinarizer(neg_label >= pos_label) raises ValueError", True)
Yml = np.array([[0, 1, 1], [1, 0, 0]]); lbm = LabelBinarizer().fit(Yml)
report("LabelBinarizer on a multilabel indicator: classes_ = column indices [0,1,2] and transform of labels is one-hot (docstring example)", lbm.classes_.tolist() == [0, 1, 2] and lbm.transform([0, 1, 2, 1]).tolist() == [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0]] and lbm.y_type_ == "multilabel-indicator")
report("label_binarize(y, classes=[...]) equals LabelBinarizer with the given class order (unsorted classes kept in the given order)",
       label_binarize(["b", "a", "c"], classes=["c", "a", "b"]).tolist() == [[0, 0, 1], [0, 1, 0], [1, 0, 0]] and label_binarize([1, 0], classes=[0, 1]).tolist() == [[1], [0]])
report("label_binarize(pos_label=0, neg_label=-1) 'To account for pos_label == 0': one column with 0 for the positive and -1 for the negative", label_binarize([1, 0, 1], classes=[0, 1], pos_label=0, neg_label=-1).ravel().tolist() == [0, -1, 0], f"({label_binarize([1, 0, 1], classes=[0, 1], pos_label=0, neg_label=-1).ravel().tolist()})")
# MultiLabelBinarizer
mlb = MultiLabelBinarizer().fit([(1, 2), (3,), (2, 5)])
report("MultiLabelBinarizer classes_ sorted when classes=None: [1, 2, 3, 5]; transform gives the indicator matrix", mlb.classes_.tolist() == [1, 2, 3, 5] and mlb.transform([(1, 2), (3,), (2, 5)]).tolist() == [[1, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 1]])
mlb2 = MultiLabelBinarizer(classes=["sci-fi", "comedy", "thriller"]).fit([["comedy"], ["sci-fi", "thriller"]])
report("MultiLabelBinarizer(classes=[...]) keeps the given order ('sci-fi','comedy','thriller') and fit_transform follows it", mlb2.classes_.tolist() == ["sci-fi", "comedy", "thriller"] and mlb2.transform([["comedy"], ["sci-fi", "thriller"]]).tolist() == [[0, 1, 0], [1, 0, 1]])
res, ws = caught(lambda: mlb.transform([(1, 7), (9,)]), UserWarning)
report("MultiLabelBinarizer.transform with unknown classes: ignored (rows [1,0,0,0],[0,0,0,0]) and a UserWarning 'unknown class(es) ... will be ignored' is raised", res.tolist() == [[1, 0, 0, 0], [0, 0, 0, 0]] and any("unknown class" in str(w.message) for w in ws), f"(warnings: {[str(w.message)[:60] for w in ws]})")
Yms = MultiLabelBinarizer(sparse_output=True).fit_transform([(1, 2), (3,), (2, 5)])
report("MultiLabelBinarizer(sparse_output=True): CSR indicator with the same values", sp.issparse(Yms) and Yms.format == "csr" and np.array_equal(dense(Yms), [[1, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 1]]))
report("MultiLabelBinarizer inverse_transform gives tuples of the classes in classes_ order", mlb.inverse_transform(np.array([[1, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1]])) == [(1, 2), (), (2, 5)])
report("MultiLabelBinarizer with a duplicate label in one sample still yields a 0/1 indicator", MultiLabelBinarizer().fit_transform([(1, 1, 2), (2,)]).tolist() == [[1, 1], [0, 1]])
try:
    MultiLabelBinarizer(classes=[1, 1, 2]).fit([(1,)]); report("MultiLabelBinarizer(classes with duplicates) raises ValueError", False)
except ValueError: report("MultiLabelBinarizer(classes with duplicates) raises ValueError", True)

# =============================================================================
print("== preprocessing: OrdinalEncoder")
Xo = np.array([["b", "x"], ["a", "y"], ["c", "x"], ["a", "z"], ["b", "x"]], dtype=object)
oe = OrdinalEncoder().fit(Xo)
report("OrdinalEncoder categories_ sorted per feature (['a','b','c'], ['x','y','z']) and codes = index in categories_, dtype float64", [c.tolist() for c in oe.categories_] == [["a", "b", "c"], ["x", "y", "z"]] and oe.transform(Xo).tolist() == [[1, 0], [0, 1], [2, 0], [0, 2], [1, 0]] and oe.transform(Xo).dtype == np.float64)
oe2 = OrdinalEncoder(categories=[["c", "b", "a"], ["z", "y", "x"]], dtype=np.int32).fit(Xo)
report("OrdinalEncoder(categories=given order, dtype=int32): codes follow the given order, output dtype int32", oe2.transform(Xo).tolist() == [[1, 2], [2, 1], [0, 2], [2, 0], [1, 2]] and oe2.transform(Xo).dtype == np.int32)
report("OrdinalEncoder inverse_transform(transform(X)) = X", np.array_equal(oe.inverse_transform(oe.transform(Xo)), Xo))
try:
    oe.transform(np.array([["d", "x"]], dtype=object)); report("OrdinalEncoder default handle_unknown='error' raises ValueError on an unknown category", False)
except ValueError: report("OrdinalEncoder default handle_unknown='error' raises ValueError on an unknown category", True)
oeu = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1).fit(Xo)
Zu = oeu.transform(np.array([["d", "x"], ["a", "q"]], dtype=object))
report("OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1): unknown categories encoded as -1, known ones unchanged", Zu.tolist() == [[-1, 0], [0, -1]])
report("OrdinalEncoder(use_encoded_value) inverse_transform maps unknown_value back to None", oeu.inverse_transform(Zu).tolist() == [[None, "x"], ["a", None]], f"({oeu.inverse_transform(Zu).tolist()})")
oen = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan).fit(Xo)
report("OrdinalEncoder(unknown_value=np.nan): unknown -> NaN (float output)", np.isnan(oen.transform(np.array([["d", "x"]], dtype=object))[0, 0]))
try:
    OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=1).fit(Xo); report("OrdinalEncoder(unknown_value colliding with a code 0..n_cat-1) raises ValueError", False)
except ValueError: report("OrdinalEncoder(unknown_value colliding with a code 0..n_cat-1) raises ValueError", True)
Xm = np.array([["b"], ["a"], [np.nan], ["a"], [None]], dtype=object)
oem = OrdinalEncoder().fit(Xm)
print(f"   categories_ with missing: {oem.categories_[0].tolist()}; transform {oem.transform(Xm).ravel().tolist()}")
zm = oem.transform(Xm).ravel()
report("OrdinalEncoder with np.nan and None: 'will also passthrough missing values that are indicated by np.nan' (-> NaN) while None 'will be considered separate categories' (code 2; categories_ = ['a','b',None,nan])",
       np.isnan(zm[2]) and zm[[0, 1, 3, 4]].tolist() == [1, 0, 0, 2] and oem.categories_[0].tolist()[:3] == ["a", "b", None] and (isinstance(oem.categories_[0][3], float) and np.isnan(oem.categories_[0][3])))
oem2 = OrdinalEncoder(encoded_missing_value=-2).fit(Xm); zm2 = oem2.transform(Xm).ravel(); inv_m = oem2.inverse_transform(oem2.transform(Xm))[2, 0]
report("OrdinalEncoder(encoded_missing_value=-2): np.nan encoded as -2 (user guide example with -1) and inverse_transform gives back NaN", zm2[2] == -2 and zm2[[0, 1, 3, 4]].tolist() == [1, 0, 0, 2] and isinstance(inv_m, float) and np.isnan(inv_m), f"(inverse of missing: {inv_m!r})")
ug = OrdinalEncoder(encoded_missing_value=-1).fit_transform([["male"], ["female"], [np.nan], ["female"]])
report("OrdinalEncoder(encoded_missing_value=-1) user-guide example -> [[1],[0],[-1],[0]]", ug.ravel().tolist() == [1, 0, -1, 0])
if has_param(OrdinalEncoder, "min_frequency"):
    Xinf = np.array([["dog"] * 5 + ["cat"] * 20 + ["rabbit"] * 10 + ["snake"] * 3], dtype=object).T
    oi = OrdinalEncoder(min_frequency=6).fit(Xinf)
    report("OrdinalEncoder(min_frequency=6) user-guide example: infrequent_categories_ = ['dog','snake'], transform dog/cat/rabbit/snake = [2, 0, 1, 2] (infrequent = last code)",
           oi.infrequent_categories_[0].tolist() == ["dog", "snake"] and oi.transform(np.array([["dog"], ["cat"], ["rabbit"], ["snake"]])).ravel().tolist() == [2, 0, 1, 2])
    Xtr = np.array([["a"] * 5 + ["b"] * 20 + ["c"] * 10 + ["d"] * 3 + [np.nan]], dtype=object).T
    oi2 = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=3, max_categories=3, encoded_missing_value=4).fit(Xtr)
    Zi2 = oi2.transform(np.array([["a"], ["b"], ["c"], ["d"], ["e"], [np.nan]], dtype=object)).ravel().tolist()
    report("OrdinalEncoder(max_categories=3, unknown_value=3, encoded_missing_value=4) user-guide example: a/b/c/d/e/nan -> [2, 0, 1, 2, 3, 4] ('max_categories does not take into account missing or unknown categories')", Zi2 == [2, 0, 1, 2, 3, 4], f"({Zi2})")
    report("OrdinalEncoder infrequent inverse_transform gives 'infrequent_sklearn' for the grouped code", oi.inverse_transform(np.array([[2.0], [0.0]])).ravel().tolist() == ["infrequent_sklearn", "cat"], f"({oi.inverse_transform(np.array([[2.0], [0.0]])).ravel().tolist()})")
    oi3 = OrdinalEncoder(min_frequency=0.25).fit(Xinf)   # 0.25 * 38 = 9.5 -> counts < 9.5 infrequent: dog(5), snake(3)
    report("OrdinalEncoder(min_frequency=0.25 float): 'cardinality smaller than min_frequency * n_samples' (9.5) -> dog, snake infrequent; rabbit (10) frequent", oi3.infrequent_categories_[0].tolist() == ["dog", "snake"])
else: print("   (OrdinalEncoder min_frequency/max_categories need 1.3+: skipped)")

# =============================================================================
print("== preprocessing: OneHotEncoder (drop / infrequent / handle_unknown / names / dtype)")
def OHE(**kw):
    if V < (1, 2) and "sparse_output" in kw: kw["sparse"] = kw.pop("sparse_output")
    return OneHotEncoder(**kw)
Xh = np.array([["Male", 1], ["Female", 3], ["Female", 2]], dtype=object)
oh = OHE(handle_unknown="ignore").fit(Xh)
report("OneHotEncoder docstring example: categories_, transform([['Female',1],['Male',4]]) with an unknown -> all-zero block, inverse_transform gives None for the unknown",
       [c.tolist() for c in oh.categories_] == [["Female", "Male"], [1, 2, 3]] and dense(oh.transform([["Female", 1], ["Male", 4]])).tolist() == [[1, 0, 1, 0, 0], [0, 1, 0, 0, 0]]
       and oh.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]]).tolist() == [["Male", 1], [None, 2]] and oh.get_feature_names_out(["gender", "group"]).tolist() == ["gender_Female", "gender_Male", "group_1", "group_2", "group_3"])
ohb = OHE(drop="if_binary").fit(Xh)
report("OneHotEncoder(drop='if_binary'): 'drop the first category in each feature with two categories. Features with 1 or more than 2 categories are left intact' -> 4 columns, drop_idx_ = [0, None]",
       dense(ohb.transform([["Female", 1], ["Male", 2]])).tolist() == [[0, 1, 0, 0], [1, 0, 1, 0]] and ohb.drop_idx_.tolist() == [0, None] and ohb.get_feature_names_out().tolist() == ["x0_Male", "x1_1", "x1_2", "x1_3"], f"(drop_idx_ {ohb.drop_idx_.tolist()})")
oha = OHE(drop=["Male", 2]).fit(Xh)
report("OneHotEncoder(drop=array): 'drop[i] is the category in feature X[:, i] that should be dropped' -> drop_idx_ = [1, 1], names ['x0_Female','x1_1','x1_3']",
       oha.drop_idx_.tolist() == [1, 1] and oha.get_feature_names_out().tolist() == ["x0_Female", "x1_1", "x1_3"] and dense(oha.transform([["Male", 2], ["Female", 3]])).tolist() == [[0, 0, 0], [1, 0, 1]])
oh1 = OHE(drop="first").fit(np.array([["only"], ["only"]], dtype=object))
report("OneHotEncoder(drop='first') with a single category: 'the feature will be dropped entirely' (0 output columns)", dense(oh1.transform([["only"]])).shape == (1, 0))
report("OneHotEncoder(drop='if_binary') with a single category leaves the feature intact (1 column)", dense(OHE(drop="if_binary").fit_transform(np.array([["only"], ["only"]], dtype=object))).shape == (2, 1))
try:
    OHE(drop=["Nope", 2]).fit(Xh); report("OneHotEncoder(drop=array with a non-existing category) raises ValueError", False)
except ValueError: report("OneHotEncoder(drop=array with a non-existing category) raises ValueError", True)
# infrequent categories
Xinf = np.array([["a"] * 5 + ["b"] * 20 + ["c"] * 10 + ["d"] * 3], dtype=object).T
ohi = OHE(max_categories=3, sparse_output=False).fit(Xinf)
report("OneHotEncoder(max_categories=3) docstring example: infrequent_categories_ = ['a','d'], transform a/b -> [[0,0,1],[1,0,0]] (infrequent column last)",
       ohi.infrequent_categories_[0].tolist() == ["a", "d"] and ohi.transform([["a"], ["b"]]).tolist() == [[0, 0, 1], [1, 0, 0]] and ohi.get_feature_names_out().tolist() == ["x0_b", "x0_c", "x0_infrequent_sklearn"])
for mf, exp in ((5, ["d"]), (6, ["a", "d"]), (3, []), (4, ["d"])):
    o = OHE(min_frequency=mf, sparse_output=False).fit(Xinf); got = [] if o.infrequent_categories_[0] is None else o.infrequent_categories_[0].tolist()
    report(f"OneHotEncoder(min_frequency={mf} int): 'categories with a smaller cardinality will be considered infrequent' (count == min_frequency stays frequent) -> {exp}", got == exp, f"(got {got})")
for mf, exp in ((0.1, ["d"]), (0.2, ["a", "d"]), (5 / 38, ["d"]), (10 / 38, ["a", "d"]), (10.0001 / 38, ["a", "c", "d"])):
    o = OHE(min_frequency=mf, sparse_output=False).fit(Xinf); got = [] if o.infrequent_categories_[0] is None else o.infrequent_categories_[0].tolist()
    report(f"OneHotEncoder(min_frequency={mf:.4f} float): 'cardinality smaller than min_frequency * n_samples' ({mf * 38:.4f}) -> {exp}", got == exp, f"(got {got})")
o = OHE(min_frequency=4, max_categories=3, sparse_output=False).fit(Xinf)
report("OneHotEncoder(min_frequency=4, max_categories=3): 'selected based on min_frequency first and max_categories categories are kept' -> infrequent ['a','d'] (user guide: snake then dog)", o.infrequent_categories_[0].tolist() == ["a", "d"] and o.transform([["a"], ["b"], ["c"], ["d"]]).tolist() == [[0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
Xtie = np.array([["a"] * 20 + ["b"] * 10 + ["c"] * 10 + ["d"] * 10], dtype=object).T
ot = OHE(max_categories=3).fit(Xtie)
print(f"   max_categories=3 with b, c, d tied at 10: infrequent_categories_ = {ot.infrequent_categories_[0].tolist()}, kept = {ot.get_feature_names_out().tolist()}")
report("OneHotEncoder(max_categories=3) ties at the cutoff: user guide example says infrequent = ['b','c'] (so 'd', the highest in lexicon order, is kept)", ot.infrequent_categories_[0].tolist() == ["b", "c"])
report("OneHotEncoder(max_categories=3) ties: user guide sentence 'the first max_categories are taken based on lexicon ordering' would keep a, b (infrequent c, d)", ot.infrequent_categories_[0].tolist() == ["c", "d"], f"(infrequent {ot.infrequent_categories_[0].tolist()})")
o1 = OHE(max_categories=1, sparse_output=False).fit(Xinf)
print(f"   max_categories=1: infrequent_categories_ {o1.infrequent_categories_}, names {o1.get_feature_names_out().tolist()}")
if V >= (1, 3):
    report("OneHotEncoder(max_categories=1): all categories infrequent -> a single column of ones (1.3+ accepts 1; user guide says 'any integer greater than 1')", o1.transform([["a"], ["b"]]).tolist() == [[1], [1]] and o1.infrequent_categories_[0].tolist() == ["a", "b", "c", "d"])
else:
    report("OneHotEncoder(max_categories=1) on <1.3: outside the documented domain ('any integer greater than 1'); measured: no grouping at all (infrequent_categories_ [None]) -- informational", o1.infrequent_categories_[0] is None, f"({o1.get_feature_names_out().tolist()})")
ohu = OHE(handle_unknown="infrequent_if_exist", sparse_output=False, min_frequency=6).fit(Xinf)
report("OneHotEncoder(handle_unknown='infrequent_if_exist', min_frequency=6): unknown 'dragon' -> the infrequent column [0,0,1]; inverse_transform of it = 'infrequent_sklearn'",
       ohu.transform([["dragon"]]).tolist() == [[0, 0, 1]] and ohu.inverse_transform([[0, 0, 1]]).tolist() == [["infrequent_sklearn"]], f"({ohu.inverse_transform([[0, 0, 1]]).tolist()})")
ohu2 = OHE(handle_unknown="infrequent_if_exist", sparse_output=False).fit(Xinf)
report("OneHotEncoder(handle_unknown='infrequent_if_exist') without infrequent categories: unknown -> all zeros and inverse_transform None (documented 'handle as with ignore')",
       ohu2.transform([["dragon"]]).tolist() == [[0, 0, 0, 0]] and ohu2.inverse_transform([[0, 0, 0, 0]]).tolist() == [[None]])
if V >= (1, 6):
    res, ws = caught(lambda: OHE(handle_unknown="warn", sparse_output=False, min_frequency=6).fit(Xinf).transform([["dragon"]]), UserWarning)
    report("OneHotEncoder(handle_unknown='warn'): UserWarning issued and the encoding proceeds as 'infrequent_if_exist'", res.tolist() == [[0, 0, 1]] and len(ws) >= 1, f"({[str(w.message)[:50] for w in ws]})")
ohd = OHE(min_frequency=6, drop="first", sparse_output=False).fit(Xinf)
print(f"   min_frequency=6 + drop='first': categories_ {ohd.categories_[0].tolist()}, infrequent {ohd.infrequent_categories_[0].tolist()}, drop_idx_ {ohd.drop_idx_.tolist()}, names {ohd.get_feature_names_out().tolist()}")
report("OneHotEncoder(min_frequency=6, drop='first'): 'dropping behavior is handled after the grouping' -> drops the first remaining column ('b'), keeps c and infrequent", ohd.get_feature_names_out().tolist() == ["x0_c", "x0_infrequent_sklearn"] and ohd.transform([["b"], ["a"], ["c"]]).tolist() == [[0, 0], [0, 1], [1, 0]])
try:
    ohda = OHE(min_frequency=6, drop=["a"], sparse_output=False).fit(Xinf); exc = None
    okd = ohda.get_feature_names_out().tolist() == ["x0_b", "x0_c"] and ohda.transform([["a"], ["d"], ["b"]]).tolist() == [[0, 0], [0, 0], [1, 0]]; det = f"({ohda.get_feature_names_out().tolist()})"
except Exception as e: exc = e; okd = False; det = f"raised {type(e).__name__}: {e}"
report("OneHotEncoder(min_frequency=6, drop=['a']) with 'a' infrequent: drop_idx_ docstring 'if drop_idx[i] corresponds to an infrequent category, then the entire infrequent category is dropped'", okd, det)
report("OneHotEncoder(min_frequency=6, drop=['a']) with 'a' infrequent: the source intends a ValueError ('Unable to drop category ... because it is infrequent'), not another exception type", isinstance(exc, ValueError), f"(got {type(exc).__name__})")
try:
    ohdn = OHE(min_frequency=2, drop=[1], sparse_output=False).fit(np.array([[1], [1], [2], [2], [3]]))
    okn = False; detn = f"(fitted; names {ohdn.get_feature_names_out().tolist()})"
except ValueError as e: okn = True; detn = ""
except Exception as e: okn = False; detn = f"raised {type(e).__name__}: {e}"
report("OneHotEncoder(min_frequency=2, drop=[1]) numeric categories (counts 2,2,1 -> 3 infrequent), dropping the frequent category 1: fits with names ['x0_2','x0_infrequent_sklearn']", not okn and "['x0_2', 'x0_infrequent_sklearn']" in detn, detn)
try:
    OHE(min_frequency=2, drop=[3], sparse_output=False).fit(np.array([[1], [1], [2], [2], [3]])); okn = False; detn = "(no error)"
except ValueError: okn = True; detn = ""
except Exception as e: okn = False; detn = f"raised {type(e).__name__}: {e}"
report("OneHotEncoder(min_frequency=2, drop=[3]) with numeric infrequent category 3: raises ValueError (numpy scalar .item() works for numeric dtypes)", okn, detn)
if has_param(OneHotEncoder, "feature_name_combiner"):
    def custom_combiner(feature, category): return str(feature) + "_" + type(category).__name__ + "_" + str(category)
    oc = OHE(feature_name_combiner=custom_combiner).fit(Xh)
    report("OneHotEncoder(feature_name_combiner=callable) docstring example: ['x0_str_Female','x0_str_Male','x1_int_1','x1_int_2','x1_int_3']", oc.get_feature_names_out().tolist() == ["x0_str_Female", "x0_str_Male", "x1_int_1", "x1_int_2", "x1_int_3"], f"({oc.get_feature_names_out().tolist()})")
    report("OneHotEncoder(feature_name_combiner='concat') = feature + '_' + str(category)", OHE(feature_name_combiner="concat").fit(Xh).get_feature_names_out(["g", "n"]).tolist() == ["g_Female", "g_Male", "n_1", "n_2", "n_3"])
Zsp = OHE().fit_transform(Xh); Zd = OHE(sparse_output=False).fit_transform(Xh)
report("OneHotEncoder default sparse_output=True gives CSR; sparse_output=False the same values dense; dtype float64", sp.issparse(Zsp) and Zsp.format == "csr" and np.array_equal(dense(Zsp), Zd) and Zsp.dtype == np.float64 and Zd.dtype == np.float64)
Zi = OHE(dtype=np.int8, sparse_output=False).fit_transform(Xh)
report("OneHotEncoder(dtype=np.int8): output dtype int8 with the same 0/1 values", Zi.dtype == np.int8 and np.array_equal(Zi, Zd))
ohc = OHE(categories=[["Male", "Female", "Other"], [3, 2, 1]], sparse_output=False).fit(Xh)
report("OneHotEncoder(categories=given): columns follow the given category order incl. unseen 'Other'", ohc.categories_[0].tolist() == ["Male", "Female", "Other"] and ohc.transform([["Female", 1]]).tolist() == [[0, 1, 0, 0, 0, 1]])
ohn = OHE(sparse_output=False).fit([["male", "Safari"], ["female", None], [np.nan, "Firefox"]])
report("OneHotEncoder user-guide example with missing values: nan and None become categories (['female','male',nan], ['Firefox','Safari',None])",
       ohn.categories_[0].tolist()[:2] == ["female", "male"] and ohn.categories_[1].tolist() == ["Firefox", "Safari", None] and ohn.transform([["male", "Safari"], ["female", None], [np.nan, "Firefox"]]).tolist() == [[0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0]])

# =============================================================================
print("== preprocessing: TargetEncoder (1.3+)")
try:
    from sklearn.preprocessing import TargetEncoder
except ImportError:
    TargetEncoder = None; print("   (TargetEncoder not available before 1.3: skipped)")
def te_truth(cats, xcol, y, smooth):
    """Documented shrinkage: S_i = lambda_i * mean_i + (1 - lambda_i) * global mean, lambda_i = n_i/(m + n_i);
    smooth='auto': m = sigma_i^2 / tau^2 (variance of y within category i / global variance of y). Exact Fractions."""
    y = [F(v) for v in y]; n = len(y); ymean = sum(y) / n; out = []
    tau2 = sum((v - ymean) ** 2 for v in y) / n
    for c in cats:
        ys = [y[i] for i in range(n) if xcol[i] == c]; ni = len(ys)
        if ni == 0: out.append(ymean); continue
        mi = sum(ys) / ni
        if smooth == "auto":
            s2 = sum((v - mi) ** 2 for v in ys) / ni; den = tau2 * ni + s2
            out.append(ymean if den == 0 else (tau2 * ni / den) * mi + (1 - tau2 * ni / den) * ymean)
        else:
            m = F(smooth); lam = F(ni) / (m + ni); out.append(lam * mi + (1 - lam) * ymean)
    return [float(v) for v in out]
if TargetEncoder is not None:
    xt = np.array(list("abcabcaabbdcabcaabcd"), dtype=object)[:, None]; cats_t = ["a", "b", "c", "d"]
    yb = np.array([1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0])
    yc = np.array([2.5, -1.0, 3.0, 1.5, 0.5, 2.0, 4.0, 3.5, -2.0, 1.0, 7.0, 2.5, 3.0, -1.5, 1.0, 2.0, 5.0, -0.5, 2.5, 6.0])
    for smooth in (1.0, 5.0, 0.0, "auto"):
        for name, y, ttype in (("binary", yb, "binary"), ("continuous", yc, "continuous")):
            te = TargetEncoder(smooth=smooth, target_type=ttype).fit(xt, y)
            T = te_truth(cats_t, xt[:, 0], y, smooth)
            report(f"TargetEncoder(smooth={smooth!r}, {name}).fit: encodings_ = documented shrinkage S_i = lambda_i n_iY/n_i + (1-lambda_i) n_Y/n{' with the empirical-Bayes m = sigma_i^2/tau^2' if smooth == 'auto' else ''} (exact, rel 1e-12); target_mean_ = mean(y); categories_ sorted",
                   te.categories_[0].tolist() == cats_t and allclose(te.encodings_[0], T, 1e-12) and close(te.target_mean_, float(np.mean(y)), 1e-14), f"(encodings_ {np.round(te.encodings_[0], 6).tolist()})")
    te1 = TargetEncoder(smooth=2.0, target_type="continuous").fit(xt, yc)
    Zt = te1.transform(np.array([["a"], ["d"], ["zzz"], [np.nan]], dtype=object))
    T1 = te_truth(cats_t, xt[:, 0], yc, 2.0)
    report("TargetEncoder.transform: known category -> its encoding; unseen category and nan (not seen in fit) -> target_mean_ ('Categories that are not seen during fit are encoded with the target mean')",
           allclose(Zt.ravel(), [T1[0], T1[3], np.mean(yc), np.mean(yc)], 1e-12))
    report("TargetEncoder fit(X, y).transform(X) on the training data = plain (non cross-fitted) encoding lookup", allclose(te1.transform(xt).ravel(), [T1[cats_t.index(c)] for c in xt[:, 0]], 1e-12))
    # cross fitting in fit_transform: continuous target -> KFold(5) without shuffle -> contiguous folds
    kw_cv = {"cv": KFold(5)} if V >= (1, 9) else {"cv": 5, "shuffle": False}
    te_cv = TargetEncoder(smooth=2.0, target_type="continuous", **kw_cv)
    Zcv = te_cv.fit_transform(xt, yc)
    def cross_fit_truth(xcol, y, smooth, folds):
        out = np.empty(len(y))
        for test in folds:
            train = [i for i in range(len(y)) if i not in test]
            enc = te_truth(cats_t, [xcol[i] for i in train], [y[i] for i in train], smooth)
            ymean_tr = float(np.mean([y[i] for i in train]))
            for i in test:
                c = xcol[i]; present = any(xcol[j] == c for j in train)
                out[i] = enc[cats_t.index(c)] if present else ymean_tr
        return out
    folds5 = [list(range(4 * k, 4 * k + 4)) for k in range(5)]
    Tcv = cross_fit_truth(xt[:, 0], yc, 2.0, folds5)
    print(f"   fit_transform (cross-fitted) first 6: {np.round(Zcv.ravel()[:6], 6).tolist()}\n   truth                              {np.round(Tcv[:6], 6).tolist()}")
    report("TargetEncoder.fit_transform (continuous, 5 contiguous KFold folds): 'each fold is encoded using the encodings learnt using the other k-1 folds' (recomputed fold by fold, incl. a category absent from the training folds -> training-fold target mean)",
           allclose(Zcv.ravel(), Tcv, 1e-12))
    report("TargetEncoder.fit_transform also stores the full-data encodings_ ('learns category encodings from the full training data and stores them in encodings_')", allclose(te_cv.encodings_[0], te_truth(cats_t, xt[:, 0], yc, 2.0), 1e-12))
    report("TargetEncoder: fit_transform(X, y) != fit(X, y).transform(X) (documented note)", not allclose(Zcv, te1.transform(xt)))
    # binary: StratifiedKFold(5) without shuffle (library splitter used only to obtain the fold indices)
    kw_cvb = {"cv": StratifiedKFold(5)} if V >= (1, 9) else {"cv": 5, "shuffle": False}
    te_cvb = TargetEncoder(smooth="auto", target_type="binary", **kw_cvb); Zcvb = te_cvb.fit_transform(xt, yb)
    foldsb = [list(te) for _, te in StratifiedKFold(5).split(xt, yb)]
    report("TargetEncoder.fit_transform (binary, smooth='auto', StratifiedKFold(5) unshuffled folds): cross-fitted values recomputed fold by fold with the empirical-Bayes shrinkage", allclose(Zcvb.ravel(), cross_fit_truth(xt[:, 0], yb, "auto", foldsb), 1e-12))
    # shuffle / random_state determinism (deprecated in 1.9 -> use a KFold with random_state)
    if V >= (1, 9):
        Za = TargetEncoder(smooth=2.0, target_type="continuous", cv=KFold(5, shuffle=True, random_state=3)).fit_transform(xt, yc)
        Zb_ = TargetEncoder(smooth=2.0, target_type="continuous", cv=KFold(5, shuffle=True, random_state=3)).fit_transform(xt, yc)
        Zc_ = TargetEncoder(smooth=2.0, target_type="continuous", cv=KFold(5, shuffle=True, random_state=4)).fit_transform(xt, yc)
        folds_r = [list(te) for _, te in KFold(5, shuffle=True, random_state=3).split(xt)]
        report("TargetEncoder(cv=KFold(shuffle=True, random_state=3)): deterministic for the same seed, cross-fitted values recomputed on those folds; different seed -> different values", allclose(Za, Zb_) and allclose(Za.ravel(), cross_fit_truth(xt[:, 0], yc, 2.0, folds_r), 1e-12) and not allclose(Za, Zc_))
        _, ws = caught(lambda: TargetEncoder(target_type="continuous", shuffle=True, random_state=0).fit_transform(xt, yc), FutureWarning)
        report("TargetEncoder(shuffle=..., random_state=...) on 1.9: FutureWarning ('deprecated in version 1.9')", len(ws) >= 1 and "deprecated" in str(ws[0].message))
    else:
        Za = TargetEncoder(smooth=2.0, target_type="continuous", cv=5, shuffle=True, random_state=3).fit_transform(xt, yc)
        Zb_ = TargetEncoder(smooth=2.0, target_type="continuous", cv=5, shuffle=True, random_state=3).fit_transform(xt, yc)
        Zc_ = TargetEncoder(smooth=2.0, target_type="continuous", cv=5, shuffle=True, random_state=4).fit_transform(xt, yc)
        folds_r = [list(te) for _, te in KFold(5, shuffle=True, random_state=3).split(xt)]
        report("TargetEncoder(shuffle=True, random_state=3): deterministic for the same seed, cross-fitted values = KFold(5, shuffle=True, random_state=3) folds; different seed -> different values", allclose(Za, Zb_) and allclose(Za.ravel(), cross_fit_truth(xt[:, 0], yc, 2.0, folds_r), 1e-12) and not allclose(Za, Zc_))
    if V >= (1, 4):
        ym = np.array([0, 1, 2, 0, 1, 2, 0, 0, 1, 1, 2, 2, 0, 1, 2, 0, 0, 1, 2, 2])
        xt2 = np.column_stack([xt, np.array(list("xyxyxyxyxyxxyyxyxyxy"), dtype=object)])
        tem = TargetEncoder(smooth=3.0, target_type="multiclass").fit(xt2, ym)
        exp = []
        for f, cats in ((0, cats_t), (1, ["x", "y"])):
            for k in (0, 1, 2): exp.append(te_truth(cats, xt2[:, f], (ym == k).astype(int), 3.0))
        okm = all(allclose(tem.encodings_[i], exp[i], 1e-12) for i in range(6))
        report("TargetEncoder(target_type='multiclass'): encodings_ ordered f0_c0, f0_c1, f0_c2, f1_c0, ... each = the binary one-vs-all encoding of that class (exact); classes_ = [0,1,2]; target_mean_ = class frequencies",
               okm and tem.classes_.tolist() == [0, 1, 2] and allclose(tem.target_mean_, [np.mean(ym == k) for k in range(3)], 1e-14), f"(n encodings {len(tem.encodings_)})")
        Zm = tem.transform(xt2[:3])
        report("TargetEncoder multiclass transform: n_features * n_classes columns in the documented order", Zm.shape == (3, 6) and allclose(Zm[0], [exp[k][cats_t.index(xt2[0, 0])] for k in range(3)] + [exp[3 + k][["x", "y"].index(xt2[0, 1])] for k in range(3)], 1e-12) and tem.get_feature_names_out().tolist() == ["x0_0", "x0_1", "x0_2", "x1_0", "x1_1", "x1_2"], f"({tem.get_feature_names_out().tolist()})")
    tea = TargetEncoder(target_type="auto").fit(xt, yb); tec = TargetEncoder(target_type="auto").fit(xt, yc)
    report("TargetEncoder(target_type='auto') infers 'binary' for 0/1 and 'continuous' for floats (target_type_)", tea.target_type_ == "binary" and tec.target_type_ == "continuous")
    ten = TargetEncoder(smooth=1.0, target_type="continuous").fit(np.array([["a"], [np.nan], ["a"], [None]], dtype=object), [1.0, 2.0, 3.0, 4.0])
    print(f"   TargetEncoder categories with nan/None: {ten.categories_[0].tolist()}  encodings_ {ten.encodings_[0].tolist()}")
    report("TargetEncoder 'considers missing values, such as np.nan or None, as another category': nan and None each get an encoding (documented as one 'missing' category: they are two categories here, as for OneHotEncoder)", len(ten.categories_[0]) == 3)

# =============================================================================
print("== preprocessing: MaxAbsScaler / Normalizer / KernelCenterer / FunctionTransformer")
Xa = np.array([[1.0, -2.0, 0.0], [-4.0, 0.5, 0.0], [2.0, 3.0, 0.0], [0.5, -0.25, 0.0]])
ma = MaxAbsScaler().fit(Xa)
report("MaxAbsScaler max_abs_ = max |x| per feature, scale_ = max_abs_ with a zero column -> scale 1 ('constant' feature), transform = X / scale_ (exact)",
       ma.max_abs_.tolist() == [4, 3, 0] and ma.scale_.tolist() == [4, 3, 1] and np.array_equal(ma.transform(Xa), Xa / np.array([4, 3, 1])))
map_ = MaxAbsScaler().partial_fit(Xa[:2]).partial_fit(Xa[2:3]).partial_fit(Xa[3:])
report("MaxAbsScaler partial_fit over 3 chunks = fit (max_abs_, scale_, n_samples_seen_)", np.array_equal(map_.max_abs_, ma.max_abs_) and np.array_equal(map_.scale_, ma.scale_) and map_.n_samples_seen_ == 4)
for fmt in (sp.csr_matrix, sp.csc_matrix):
    ms = MaxAbsScaler().fit(fmt(Xa)); Zms = ms.transform(fmt(Xa))
    report(f"MaxAbsScaler on {fmt.__name__}: same max_abs_/scale_ as dense, sparse output equal to the dense transform, inverse_transform round trip", np.array_equal(ms.max_abs_, ma.max_abs_) and sp.issparse(Zms) and np.array_equal(dense(Zms), ma.transform(Xa)) and np.array_equal(dense(ms.inverse_transform(Zms)), Xa))
report("maxabs_scale(X) = MaxAbsScaler().fit_transform(X) (documented 'Equivalent function without the estimator API')", np.array_equal(maxabs_scale(Xa), ma.transform(Xa)))
report("MaxAbsScaler on float32 keeps float32 and exact values", MaxAbsScaler().fit_transform(Xa.astype(np.float32)).dtype == np.float32 and np.array_equal(MaxAbsScaler().fit_transform(Xa.astype(np.float32)), (Xa / np.array([4, 3, 1])).astype(np.float32)))
if has_param(MaxAbsScaler, "clip"):
    report("MaxAbsScaler(clip=True): held-out values clipped to [-1, 1]", MaxAbsScaler(clip=True).fit(Xa).transform(np.array([[8.0, -9.0, 5.0]])).tolist() == [[1.0, -1.0, 1.0]])
report("MaxAbsScaler with NaN: 'NaNs are treated as missing values: disregarded in fit, and maintained in transform'", MaxAbsScaler().fit(np.array([[1.0], [np.nan], [-3.0]])).max_abs_.tolist() == [3.0] and np.isnan(MaxAbsScaler().fit_transform(np.array([[1.0], [np.nan], [-3.0]]))[1, 0]))
# Normalizer
Xn = np.array([[3.0, -4.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 1.0], [-2.0, 0.5, 2.5]])
def norm_truth(X, kind):
    out = []
    for row in X:
        r = [F(v) for v in row]
        if kind == "l1": nv = sum(abs(v) for v in r)
        elif kind == "max": nv = max(abs(v) for v in r)
        else: nv = None
        if kind == "l2": s2 = float(sum(v * v for v in r)); out.append([float(v) / math.sqrt(s2) if s2 else 0.0 for v in r])
        else: out.append([float(v / nv) if nv else 0.0 for v in r])
    return np.array(out)
for kind in ("l1", "l2", "max"):
    Zn = Normalizer(norm=kind).fit_transform(Xn)
    report(f"Normalizer(norm='{kind}'): rows scaled by their {kind} norm (exact; all-zero row stays zero), equals normalize(X, norm='{kind}') and the sparse-input result", allclose(Zn, norm_truth(Xn, kind), 1e-15) and allclose(normalize(Xn, norm=kind), Zn) and allclose(dense(Normalizer(norm=kind).fit_transform(sp.csr_matrix(Xn))), Zn))
Zn2, norms = normalize(Xn, norm="l2", return_norm=True)
print(f"   normalize(return_norm=True) norms {norms.tolist()}")
report("normalize(return_norm=True): 'the computed norms' = l2 row norms 5, 0, sqrt3, sqrt(10.5) (an all-zero row has norm 0)", allclose(norms, [5, 0, math.sqrt(3), math.sqrt(10.5)], 1e-15), f"(norm of the zero row reported as {norms[1]})")
report("normalize(return_norm=True): the returned norms are the divisors actually used (X = Z * norms, zero row -> 1)", allclose(Zn2 * norms[:, None], Xn, 1e-15) and allclose(norms[[0, 2, 3]], [5, math.sqrt(3), math.sqrt(10.5)], 1e-15))
Zc = normalize(Xn, norm="l1", axis=0)
report("normalize(axis=0) normalizes columns", allclose(Zc, norm_truth(Xn.T, "l1").T, 1e-15))
report("Normalizer(norm='max') uses max |x| ('max: max absolute value'): row [-2, 0.5, 2.5] -> divided by 2.5", allclose(Normalizer(norm="max").fit_transform(Xn)[3], [-0.8, 0.2, 1.0], 1e-15))
# KernelCenterer: linear kernel -> centred kernel = (X - mean)(X - mean)^T exactly
Xk = np.array([[1.0, -2.0, 2.0], [2.0, 0.0, 0.0], [0.0, 1.0, -1.0], [3.0, 1.0, 0.5]]); Xk_new = np.array([[1.0, 1.0, 1.0], [-2.0, 0.5, 3.0]])
Kf = Xk @ Xk.T; Kn = Xk_new @ Xk.T
kc = KernelCenterer().fit(Kf)
Xkf = [[F(v) for v in row] for row in Xk]; mu = [sum(r[j] for r in Xkf) / len(Xkf) for j in range(3)]
Cf = np.array([[float(sum((a[j] - mu[j]) * (b[j] - mu[j]) for j in range(3))) for b in Xkf] for a in Xkf])
Xnf = [[F(v) for v in row] for row in Xk_new]
Cn = np.array([[float(sum((a[j] - mu[j]) * (b[j] - mu[j]) for j in range(3))) for b in Xkf] for a in Xnf])
n = 4; one = np.full((n, n), 1 / n)
report("KernelCenterer.fit: K_fit_rows_ = column means of K, K_fit_all_ = overall mean (exact)", allclose(kc.K_fit_rows_, Kf.mean(0), 1e-15) and close(kc.K_fit_all_, Kf.mean(), 1e-15))
report("KernelCenterer.transform(K_fit) = K - 1K - K1 + 1K1 = phi-centred kernel (X - mean)(X - mean)^T (exact, 1e-13)", allclose(kc.transform(Kf), Cf, 1e-13) and allclose(kc.transform(Kf), Kf - one @ Kf - Kf @ one + one @ Kf @ one, 1e-13))
one_m = np.full((2, n), 1 / n)
report("KernelCenterer.transform(K_new) for new data = K_new - 1'_m K - K_new 1_n + 1'_m K 1_n = (X_new - mean)(X - mean)^T (exact, 1e-13)", allclose(kc.transform(Kn), Cn, 1e-13) and allclose(kc.transform(Kn), Kn - one_m @ Kf - Kn @ one + one_m @ Kf @ one, 1e-13))
report("KernelCenterer: the centred training kernel has zero row/column sums", allclose(kc.transform(Kf).sum(0), np.zeros(4), 0, 1e-12))
# FunctionTransformer
Xf = np.array([[1.0, 4.0], [9.0, 16.0]])
ft = FunctionTransformer(func=np.sqrt, inverse_func=np.square).fit(Xf)
report("FunctionTransformer(func=sqrt, inverse_func=square): transform = sqrt, inverse_transform = square (exact)", np.array_equal(ft.transform(Xf), np.sqrt(Xf)) and np.array_equal(ft.inverse_transform(np.sqrt(Xf)), Xf))
_, ws = caught(lambda: FunctionTransformer(func=np.sqrt, inverse_func=np.exp, check_inverse=True).fit(Xf), UserWarning)
report("FunctionTransformer(check_inverse=True, non-inverse pair): UserWarning 'The provided functions are not strictly inverse of each other'", any("not strictly inverse" in str(w.message) for w in ws), f"({[str(w.message)[:50] for w in ws]})")
_, ws = caught(lambda: FunctionTransformer(func=np.sqrt, inverse_func=np.exp, check_inverse=False).fit(Xf), UserWarning)
report("FunctionTransformer(check_inverse=False): no warning", len(ws) == 0)
report("FunctionTransformer default (func=None) is the identity, and passes a list through untouched with validate=False", FunctionTransformer().fit_transform([[1, 2]]) == [[1, 2]])
report("FunctionTransformer(validate=True) converts the input to an ndarray", isinstance(FunctionTransformer(validate=True).fit_transform([[1, 2]]), np.ndarray))
fk = FunctionTransformer(func=lambda X, p: X ** p, inverse_func=lambda X, p: X ** (1 / p), kw_args={"p": 3}, inv_kw_args={"p": 3})
report("FunctionTransformer(kw_args / inv_kw_args) forwarded to func / inverse_func", np.array_equal(fk.fit_transform(Xf), Xf ** 3) and allclose(fk.inverse_transform(Xf ** 3), Xf, 1e-14))
f1 = FunctionTransformer(feature_names_out="one-to-one", validate=True).fit(Xf)
report("FunctionTransformer(feature_names_out='one-to-one'): get_feature_names_out = input names (x0, x1 / given)", f1.get_feature_names_out().tolist() == ["x0", "x1"] and f1.get_feature_names_out(["a", "b"]).tolist() == ["a", "b"])
f2 = FunctionTransformer(func=lambda X: np.hstack([X, X.sum(1, keepdims=True)]), feature_names_out=lambda est, names: list(names) + ["sum"]).fit(Xf)
report("FunctionTransformer(feature_names_out=callable(transformer, input_features)) used verbatim", f2.get_feature_names_out(["a", "b"]).tolist() == ["a", "b", "sum"])
try:
    FunctionTransformer(func=np.sqrt).fit(Xf).get_feature_names_out(); report("FunctionTransformer(feature_names_out=None).get_feature_names_out raises AttributeError", False)
except AttributeError: report("FunctionTransformer(feature_names_out=None).get_feature_names_out raises AttributeError", True)
fs = FunctionTransformer(func=lambda X: X * 2, accept_sparse=True, validate=True)
report("FunctionTransformer(accept_sparse=True, validate=True) passes a CSR matrix to func", sp.issparse(fs.fit_transform(sp.csr_matrix(Xf))) and np.array_equal(dense(fs.fit_transform(sp.csr_matrix(Xf))), 2 * Xf))

# =============================================================================
print("== preprocessing: PowerTransformer (yeo-johnson MLE recomputed) / QuantileTransformer normal")
def yj(x, lam):
    x = mpf(x); lam = mpf(lam)
    if x >= 0: return ((x + 1) ** lam - 1) / lam if lam != 0 else mpmath.log(x + 1)
    return -(((-x + 1) ** (2 - lam) - 1) / (2 - lam)) if lam != 2 else -mpmath.log(-x + 1)
def yj_llf(xs, lam):
    """Yeo-Johnson profile log-likelihood: -n/2 log var(psi) + (lam-1) sum sign(x) log(|x|+1)."""
    ps = [yj(v, lam) for v in xs]; n = len(ps); m = sum(ps) / n; var = sum((p - m) ** 2 for p in ps) / n
    return -mpf(n) / 2 * mpmath.log(var) + (mpf(lam) - 1) * sum(mpmath.sign(mpf(v)) * mpmath.log(abs(mpf(v)) + 1) for v in xs)
def yj_mle(xs, lo=-6, hi=8):
    grid = [lo + i * mpf(hi - lo) / 400 for i in range(401)]; vals = [yj_llf(xs, g) for g in grid]
    k = max(range(len(grid)), key=lambda i: vals[i]); a, b = grid[max(k - 1, 0)], grid[min(k + 1, len(grid) - 1)]
    gr = (mpmath.sqrt(5) - 1) / 2
    c, d = b - gr * (b - a), a + gr * (b - a); fc, fd = yj_llf(xs, c), yj_llf(xs, d)
    for _ in range(120):
        if fc > fd: b, d, fd = d, c, fc; c = b - gr * (b - a); fc = yj_llf(xs, c)
        else: a, c, fc = c, d, fd; d = a + gr * (b - a); fd = yj_llf(xs, d)
    return (a + b) / 2
Xpt = np.array([[0.5, -3.0], [2.0, 1.5], [7.0, -0.5], [1.0, 4.0], [0.1, 2.0], [3.5, -1.0], [12.0, 0.0], [0.8, 6.0]])
ptj = PowerTransformer(method="yeo-johnson", standardize=False).fit(Xpt)
lam_ref = [yj_mle(Xpt[:, j]) for j in range(2)]
print(f"   lambdas_ {ptj.lambdas_.tolist()}  golden-section MLE {[float(l) for l in lam_ref]}")
report("PowerTransformer(yeo-johnson) lambdas_ = maximiser of the Yeo-Johnson profile log-likelihood (own mpmath golden-section MLE, |diff| < 1e-5)", all(abs(float(lam_ref[j]) - ptj.lambdas_[j]) < 1e-5 for j in range(2)))
Zpt = ptj.transform(Xpt); Tpt = np.array([[float(yj(Xpt[i, j], ptj.lambdas_[j])) for j in range(2)] for i in range(Xpt.shape[0])])
report("PowerTransformer(yeo-johnson, standardize=False) transform = psi(x, lambda) with the documented piecewise formula (rel 1e-12)", allclose(Zpt, Tpt, 1e-12))
pts = PowerTransformer(method="yeo-johnson", standardize=True).fit(Xpt)
report("PowerTransformer(standardize=True) = (psi - mean)/std (population std) of the unstandardised output ('zero-mean, unit-variance normalization')", allclose(pts.transform(Xpt), (Tpt - Tpt.mean(0)) / Tpt.std(0), 1e-12) and allclose(pts.lambdas_, ptj.lambdas_))
report("PowerTransformer(yeo-johnson) inverse_transform(transform(X)) = X (rel 1e-9)", allclose(pts.inverse_transform(pts.transform(Xpt)), Xpt, 1e-9) and allclose(ptj.inverse_transform(Zpt), Xpt, 1e-9))
report("power_transform(X, method='yeo-johnson') = PowerTransformer().fit_transform(X) (documented equivalence)", allclose(power_transform(Xpt, method="yeo-johnson"), pts.transform(Xpt)))
Xnan = Xpt.copy(); Xnan[2, 0] = np.nan
ptn = PowerTransformer(standardize=False).fit(Xnan)
report("PowerTransformer with NaN: 'disregarded in fit, and maintained in transform' (lambda from the non-NaN values, NaN stays NaN)", abs(float(yj_mle(Xnan[~np.isnan(Xnan[:, 0]), 0])) - ptn.lambdas_[0]) < 1e-5 and np.isnan(ptn.transform(Xnan)[2, 0]))
Zf32 = PowerTransformer(standardize=False).fit_transform(Xpt.astype(np.float32))
pt32 = PowerTransformer(standardize=False).fit(Xpt.astype(np.float32))
print(f"   float32 lambdas_ {pt32.lambdas_.tolist()} vs float64 {ptj.lambdas_.tolist()}; max rel diff of the transform {np.max(np.abs(Zf32 - Zpt) / np.maximum(np.abs(Zpt), 1e-12)):.1e}")
report("PowerTransformer on float32 input: lambdas_ within 1e-5 of the float64 MLE and output within 1e-4 relative of the float64 transform", allclose(Zf32, Zpt, 1e-4, 1e-5) and allclose(pt32.lambdas_, ptj.lambdas_, 1e-5), f"(lambda diff {np.max(np.abs(pt32.lambdas_ - ptj.lambdas_)):.1e})")
X0 = np.array([[1.0], [1.0], [1.0]])
try:
    Z0 = PowerTransformer().fit_transform(X0); print(f"   constant column: lambdas_ {PowerTransformer().fit(X0).lambdas_.tolist()}  transform {Z0.ravel().tolist()}"); ok0 = bool(np.all(Z0 == 0)); det0 = ""
except Exception as e: ok0 = False; det0 = f"raised {type(e).__name__}: {str(e)[:80]}"
report("PowerTransformer(yeo-johnson) on a constant column: fits and the transform is all zeros (no NaN, no exception)", ok0, det0)
# QuantileTransformer normal
xq = np.array([-3.0, 0.2, 1.0, 1.5, 2.25, 4.0, 5.5, 7.0, 9.0, 12.5, 20.0])[:, None]; nq = len(xq)
qt = QuantileTransformer(n_quantiles=nq, output_distribution="normal").fit(xq)
Zq = qt.transform(xq).ravel()
clip_min = ppf(1e-7 - np.spacing(1)); clip_max = ppf(1 - (1e-7 - np.spacing(1)))
Tq = np.array([ppf(F(i, nq - 1)) if 0 < i < nq - 1 else (clip_min if i == 0 else clip_max) for i in range(nq)])
print(f"   normal output {np.round(Zq, 6).tolist()}\n   truth         {np.round(Tq, 6).tolist()}")
report("QuantileTransformer(output_distribution='normal', n_quantiles=n): interior = Phi^-1(i/(n-1)) (mpmath erfinv, rel 1e-9); min/max mapped to the clipped bounds Phi^-1(1e-7 - eps), Phi^-1(1 - 1e-7 + eps) = -/+5.1993",
       allclose(Zq, Tq, 1e-9, 1e-12), f"(bounds {Zq.min():.6f} {Zq.max():.6f} vs {clip_min:.6f} {clip_max:.6f})")
Zout = qt.transform(np.array([[-100.0], [1000.0]])).ravel()
report("QuantileTransformer normal: 'values ... below or above the fitted range will be mapped to the bounds of the output distribution' (the same clipped bounds)", allclose(Zout, [clip_min, clip_max], 1e-12))
qtu = QuantileTransformer(n_quantiles=nq).fit(xq)
report("QuantileTransformer uniform: values outside the fitted range map to 0 and 1", qtu.transform(np.array([[-100.0], [1000.0]])).ravel().tolist() == [0.0, 1.0])
xmid = np.array([[0.6], [10.75]])  # between data points
u_ref = [F(1, 10) + (F(6, 10) - F(2, 10)) / (F(1) - F(2, 10)) * F(1, 10), F(8, 10) + (F(1075, 100) - F(9)) / (F(125, 10) - F(9)) * F(1, 10)]  # 0.15 and 0.85
report("QuantileTransformer normal on new in-range values = Phi^-1 of the linearly interpolated empirical CDF (recomputed)", allclose(qt.transform(xmid).ravel(), [ppf(u) for u in u_ref], 1e-9))
report("QuantileTransformer normal inverse_transform(transform(x)) = x for interior points (rel 1e-9)", allclose(qt.inverse_transform(qt.transform(xq))[1:-1], xq[1:-1], 1e-9) and allclose(qt.inverse_transform(qt.transform(xq)), xq, 1e-6))
xa = rs.normal(size=(300, 2)); xa[:, 1] += 5
qa = QuantileTransformer(n_quantiles=50, subsample=100, random_state=0).fit(xa); qb = QuantileTransformer(n_quantiles=50, subsample=100, random_state=0).fit(xa)
qc = QuantileTransformer(n_quantiles=50, subsample=100, random_state=1).fit(xa)
report("QuantileTransformer(subsample=100 < n, random_state=0): quantiles_ deterministic for the same seed and different for another seed", np.array_equal(qa.quantiles_, qb.quantiles_) and not np.array_equal(qa.quantiles_, qc.quantiles_))
qn = QuantileTransformer(n_quantiles=50, subsample=None).fit(xa) if V >= (1, 5) else QuantileTransformer(n_quantiles=50, subsample=10 ** 9).fit(xa)
report("QuantileTransformer without subsampling: quantiles_ = np.percentile-equivalent linear quantiles of all data (recomputed in Fractions)", allclose(qn.quantiles_[:, 0], [float(pct_exact(xa[:, 0], F(i, 49))) for i in range(50)], 1e-12))
report("quantile_transform(X, ...) = QuantileTransformer(...).fit_transform(X) (documented equivalence)", allclose(quantile_transform(xq, n_quantiles=nq, output_distribution="normal"), qt.transform(xq)))
report("QuantileTransformer(n_quantiles > n_samples) warns and uses n_samples quantiles", (lambda r: r[0].n_quantiles_ == nq and len(r[1]) >= 1)(caught(lambda: QuantileTransformer(n_quantiles=1000).fit(xq), UserWarning)))

# =============================================================================
print("== preprocessing: add_dummy_feature / function forms / RobustScaler options / StandardScaler sparse")
Xd = np.array([[1.0, 2.0], [3.0, 4.0]])
report("add_dummy_feature(X) prepends a column of ones; value=5 -> column of 5 (dense)", add_dummy_feature(Xd).tolist() == [[1, 1, 2], [1, 3, 4]] and add_dummy_feature(Xd, value=5).tolist() == [[5, 1, 2], [5, 3, 4]])
for fmt in (sp.csr_matrix, sp.csc_matrix, sp.coo_matrix):
    Zdd = add_dummy_feature(fmt(Xd), value=2.0)
    report(f"add_dummy_feature on {fmt.__name__}: sparse result with the dummy as first column", sp.issparse(Zdd) and dense(Zdd).tolist() == [[2, 1, 2], [2, 3, 4]])
Xs = rs.normal(size=(30, 4)) * np.array([1, 10, 100, 0.01]) + np.array([5, -50, 1000, 0])
report("scale(X) = StandardScaler().fit_transform(X)", allclose(scale(Xs), StandardScaler().fit_transform(Xs), 1e-13))
report("scale(X, with_mean=False, with_std=True) = X / population std", allclose(scale(Xs, with_mean=False), Xs / Xs.std(0), 1e-12))
report("minmax_scale(X, feature_range=(-1, 2)) = MinMaxScaler((-1, 2)).fit_transform(X)", allclose(minmax_scale(Xs, feature_range=(-1, 2)), MinMaxScaler((-1, 2)).fit_transform(Xs), 1e-13))
report("minmax_scale(X, axis=1) scales rows", allclose(minmax_scale(Xs, axis=1), MinMaxScaler().fit_transform(Xs.T).T, 1e-13))
report("robust_scale(X, quantile_range=(10, 90), unit_variance=True) = RobustScaler(...).fit_transform(X)", allclose(robust_scale(Xs, quantile_range=(10, 90), unit_variance=True), RobustScaler(quantile_range=(10, 90), unit_variance=True).fit_transform(Xs), 1e-13))
rb = RobustScaler(quantile_range=(10.0, 90.0)).fit(Xs)
q10 = [float(pct_exact(Xs[:, j], F(1, 10))) for j in range(4)]; q90 = [float(pct_exact(Xs[:, j], F(9, 10))) for j in range(4)]
report("RobustScaler(quantile_range=(10, 90)): center_ = median, scale_ = q90 - q10 (linear percentiles, exact)", allclose(rb.center_, np.median(Xs, 0), 1e-13) and allclose(rb.scale_, np.array(q90) - np.array(q10), 1e-12))
rbu = RobustScaler(quantile_range=(10.0, 90.0), unit_variance=True).fit(Xs)
report("RobustScaler(unit_variance=True): scale_ divided by Phi^-1(0.9) - Phi^-1(0.1) ('so that normally distributed features have a variance of 1', mpmath erfinv)", allclose(rbu.scale_, (np.array(q90) - np.array(q10)) / (ppf(0.9) - ppf(0.1)), 1e-12))
rbc = RobustScaler(with_centering=False, with_scaling=True).fit(Xs)
report("RobustScaler(with_centering=False): center_ is None and transform = X / scale_", rbc.center_ is None and allclose(rbc.transform(Xs), Xs / rbc.scale_))
rbz = RobustScaler().fit(np.array([[1.0], [1.0], [1.0], [1.0]]))
report("RobustScaler on a constant feature: scale_ = 1 (zeros in scale handled), transform = 0", rbz.scale_.tolist() == [1.0] and np.all(rbz.transform(np.array([[1.0]])) == 0))
Xsp_ = sp.csr_matrix(np.abs(Xs))
ss = StandardScaler(with_mean=False).fit(Xsp_); Zss = ss.transform(Xsp_)
var_exact = [float(sum((F(v) - sum(F(u) for u in np.abs(Xs)[:, j]) / 30) ** 2 for v in np.abs(Xs)[:, j]) / 30) for j in range(4)]
report("StandardScaler(with_mean=False) on CSR: mean_ and var_ computed on the sparse data (population variance, exact), transform = X / sqrt(var_) still sparse",
       allclose(ss.var_, var_exact, 1e-9) and allclose(ss.mean_, np.abs(Xs).mean(0), 1e-12) and sp.issparse(Zss) and allclose(dense(Zss), np.abs(Xs) / np.sqrt(var_exact), 1e-9))
try:
    StandardScaler(with_mean=True).fit(Xsp_); report("StandardScaler(with_mean=True) on sparse raises ValueError ('This does not work (and will raise an exception) when attempted on sparse matrices')", False)
except ValueError: report("StandardScaler(with_mean=True) on sparse raises ValueError ('This does not work (and will raise an exception) when attempted on sparse matrices')", True)
report("StandardScaler(with_mean=False) dense equals the sparse result", allclose(StandardScaler(with_mean=False).fit_transform(np.abs(Xs)), dense(Zss), 1e-12))
ssp = StandardScaler(with_mean=False).partial_fit(Xsp_[:10]).partial_fit(Xsp_[10:])
report("StandardScaler(with_mean=False) partial_fit on sparse chunks = fit (var_ rel 1e-8)", allclose(ssp.var_, ss.var_, 1e-8) and allclose(ssp.mean_, ss.mean_, 1e-10))

# =============================================================================
print("== feature_extraction.text: CountVectorizer")
TOK = re.compile(r"(?u)\b\w\w+\b")
def ref_word_tokens(doc, lower=True, stop=None, ngram=(1, 1), token_re=TOK):
    """Documented default: lowercase, tokens = r'(?u)\\b\\w\\w+\\b', stop words removed, word n-grams for min_n <= n <= max_n."""
    if lower: doc = doc.lower()
    toks = token_re.findall(doc)
    if stop: toks = [t for t in toks if t not in stop]
    return [" ".join(toks[i:i + n]) for n in range(ngram[0], ngram[1] + 1) for i in range(len(toks) - n + 1)]
def ref_char_ngrams(doc, ngram, lower=True):
    if lower: doc = doc.lower()
    doc = re.sub(r"\s\s+", " ", doc)
    return [doc[i:i + n] for n in range(ngram[0], ngram[1] + 1) for i in range(len(doc) - n + 1)]
def ref_char_wb_ngrams(doc, ngram, lower=True):
    """'creates character n-grams only from text inside word boundaries; n-grams at the edges of words are padded with space'."""
    if lower: doc = doc.lower()
    out = []
    for w in re.sub(r"\s\s+", " ", doc).split():
        w = " " + w + " "
        for n in range(ngram[0], ngram[1] + 1):
            if len(w) <= n: out.append(w); break     # a short word is counted once (source rule; documented? no)
            out.extend(w[i:i + n] for i in range(len(w) - n + 1))
    return out
def ref_matrix(docs, analyzer, vocab=None):
    toks = [analyzer(d) for d in docs]
    if vocab is None: vocab = sorted(set(t for ts in toks for t in ts))
    M = np.zeros((len(docs), len(vocab)), int); idx = {v: i for i, v in enumerate(vocab)}
    for i, ts in enumerate(toks):
        for t in ts:
            if t in idx: M[i, idx[t]] += 1
    return vocab, M
corpus = ["This is the first document.", "This document is the second document.", "And this is the third one.", "Is this the first document?"]
cv = CountVectorizer(); Xc = cv.fit_transform(corpus)
report("CountVectorizer docstring example: feature names ['and','document','first','is','one','second','the','third','this'] and the count matrix",
       cv.get_feature_names_out().tolist() == ["and", "document", "first", "is", "one", "second", "the", "third", "this"] and dense(Xc).tolist() == [[0, 1, 1, 1, 0, 0, 1, 0, 1], [0, 2, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 0, 1]])
vocab_ref, M_ref = ref_matrix(corpus, ref_word_tokens)
report("CountVectorizer default = lowercase + tokens r'(?u)\\b\\w\\w+\\b' (regex reference), vocabulary sorted alphabetically, CSR int64 counts", cv.get_feature_names_out().tolist() == vocab_ref and np.array_equal(dense(Xc), M_ref) and Xc.format == "csr" and Xc.dtype == np.int64)
cv2 = CountVectorizer(analyzer="word", ngram_range=(2, 2)); X2 = cv2.fit_transform(corpus)
report("CountVectorizer(ngram_range=(2,2)) docstring example: 13 bigram features starting ['and this','document is','first document',...] and the bigram counts (reference n-grams)",
       cv2.get_feature_names_out().tolist()[:3] == ["and this", "document is", "first document"] and X2.shape == (4, 13) and (lambda v, M: cv2.get_feature_names_out().tolist() == v and np.array_equal(dense(X2), M))(*ref_matrix(corpus, lambda d: ref_word_tokens(d, ngram=(2, 2)))))
docs2 = ["The Quick brown fox, the QUICK fox!! Jumps over 42 lazy-dogs; a fox é ça", "Über-cool naïve café: résumé, résumé 3x xyz_abc"]
for lower in (True, False):
    cvl = CountVectorizer(lowercase=lower); Xl = cvl.fit_transform(docs2); v, M = ref_matrix(docs2, lambda d: ref_word_tokens(d, lower=lower))
    report(f"CountVectorizer(lowercase={lower}) on punctuation / digits / accents / underscore: tokens = regex reference (single-character tokens 'a','3x'? '3x' kept, 'a' dropped)", cvl.get_feature_names_out().tolist() == v and np.array_equal(dense(Xl), M), f"(vocab {v})")
cvs = CountVectorizer(stop_words="english"); Xst = cvs.fit_transform(corpus)
v, M = ref_matrix(corpus, lambda d: ref_word_tokens(d, stop=ENGLISH_STOP_WORDS))
report("CountVectorizer(stop_words='english') removes the ENGLISH_STOP_WORDS frozenset ('a built-in stop word list for English'); the list is a frozenset of 318 words containing 'the','is','and','this','one'",
       isinstance(ENGLISH_STOP_WORDS, frozenset) and len(ENGLISH_STOP_WORDS) == 318 and all(w in ENGLISH_STOP_WORDS for w in ("the", "is", "and", "this", "one")) and cvs.get_feature_names_out().tolist() == v and np.array_equal(dense(Xst), M), f"(len {len(ENGLISH_STOP_WORDS)}, vocab {v})")
report("CountVectorizer(stop_words='english').get_stop_words() is ENGLISH_STOP_WORDS", cvs.get_stop_words() == ENGLISH_STOP_WORDS)
cvsb = CountVectorizer(stop_words=["document", "is"], ngram_range=(1, 2)); Xsb = cvsb.fit_transform(corpus)
v, M = ref_matrix(corpus, lambda d: ref_word_tokens(d, stop={"document", "is"}, ngram=(1, 2)))
report("CountVectorizer(stop_words=list, ngram_range=(1,2)): stop words removed before n-grams are formed ('this the' bigram appears)", cvsb.get_feature_names_out().tolist() == v and np.array_equal(dense(Xsb), M) and "this the" in v)
for ngr in ((1, 1), (2, 3), (3, 3)):
    cvc = CountVectorizer(analyzer="char", ngram_range=ngr); Xcc = cvc.fit_transform(docs2); v, M = ref_matrix(docs2, lambda d: ref_char_ngrams(d, ngr))
    report(f"CountVectorizer(analyzer='char', ngram_range={ngr}): n-grams of the whitespace-normalised lowercased document incl. spaces (reference)", cvc.get_feature_names_out().tolist() == v and np.array_equal(dense(Xcc), M), f"({len(v)} features)")
docs_wb = ["quick brown foxes jumped", "brown  quick   quickly"]
for ngr in ((2, 2), (2, 4), (3, 5)):
    cvw = CountVectorizer(analyzer="char_wb", ngram_range=ngr); Xw = cvw.fit_transform(docs_wb); v, M = ref_matrix(docs_wb, lambda d: ref_char_wb_ngrams(d, ngr))
    report(f"CountVectorizer(analyzer='char_wb', ngram_range={ngr}) on words longer than max_n: each word padded ' w ' and all its n-grams counted (reference)", cvw.get_feature_names_out().tolist() == v and np.array_equal(dense(Xw), M), f"({len(v)} features, e.g. {v[:4]})")
cvw = CountVectorizer(analyzer="char_wb", ngram_range=(3, 5)); Xw = cvw.fit_transform(["ab cd ab"])
print(f"   char_wb (3,5) on short words 'ab cd ab': features {cvw.get_feature_names_out().tolist()} counts {dense(Xw).ravel().tolist()}")
report("CountVectorizer(char_wb, (3,5)) on a word shorter than min_n: ' ab ' (4 chars) yields ' ab', 'ab ' (3-grams) and ' ab ' once (the padded word counted once, source rule)", cvw.get_feature_names_out().tolist() == [" ab", " ab ", " cd", " cd ", "ab ", "cd "] and dense(Xw).ravel().tolist() == [2, 2, 1, 1, 2, 1])
# min_df / max_df exactness (df of and:1 document:3 first:2 is:4 one:1 second:1 the:4 third:1 this:4)
dfs = {"and": 1, "document": 3, "first": 2, "is": 4, "one": 1, "second": 1, "the": 4, "third": 1, "this": 4}
for kw, keep in (({"min_df": 2}, lambda d: d >= 2), ({"min_df": 3}, lambda d: d >= 3), ({"max_df": 3}, lambda d: d <= 3), ({"max_df": 1}, lambda d: d <= 1),
                 ({"min_df": 0.5}, lambda d: d >= 2.0), ({"min_df": 0.75}, lambda d: d >= 3.0), ({"max_df": 0.75}, lambda d: d <= 3.0), ({"max_df": 0.25}, lambda d: d <= 1.0), ({"min_df": 0.5, "max_df": 0.75}, lambda d: 2.0 <= d <= 3.0)):
    got = CountVectorizer(**kw).fit(corpus).get_feature_names_out().tolist(); exp = sorted(t for t, d in dfs.items() if keep(d))
    report(f"CountVectorizer({kw}): terms with df 'strictly lower' than min_df / 'strictly higher' than max_df ignored; float = proportion of the 4 documents (boundary df kept) -> {exp}", got == exp, f"(got {got})")
try:
    CountVectorizer(min_df=0.75, max_df=0.5).fit(corpus); report("CountVectorizer(max_df < min_df) raises ValueError", False)
except ValueError: report("CountVectorizer(max_df < min_df) raises ValueError", True)
try:
    CountVectorizer(min_df=5).fit(corpus); report("CountVectorizer pruning every term raises ValueError ('After pruning, no terms remain')", False)
except ValueError: report("CountVectorizer pruning every term raises ValueError ('After pruning, no terms remain')", True)
tfs = collections.Counter(t for d in corpus for t in ref_word_tokens(d))
print(f"   term frequencies across the corpus: {dict(sorted(tfs.items()))}")
cvm = CountVectorizer(max_features=3).fit(corpus); kept = cvm.get_feature_names_out().tolist()
report("CountVectorizer(max_features=3): 'top max_features ordered by term frequency across the corpus' -> the 3 terms with tf 5 (document), 4, 4 (is/the/this tie at 4: two of them)", len(kept) == 3 and "document" in kept and all(tfs[t] == 4 for t in kept if t != "document"), f"(kept {kept})")
cvm2 = CountVectorizer(max_features=2).fit(corpus); kept2 = cvm2.get_feature_names_out().tolist()
print(f"   max_features=2 kept {kept2}; max_features=3 kept {kept}; ties at tf=4: is, the, this")
report("CountVectorizer(max_features): the kept vocabulary is sorted alphabetically and indices 0..k-1", kept == sorted(kept) and sorted(cvm.vocabulary_.values()) == [0, 1, 2])
cvb = CountVectorizer(binary=True); Xb = cvb.fit_transform(corpus)
report("CountVectorizer(binary=True): 'all non zero counts are set to 1' ('document' twice in doc 2 -> 1)", np.array_equal(dense(Xb), (M_ref > 0).astype(int)))
cvv = CountVectorizer(vocabulary=["document", "this", "zebra"]); Xv = cvv.fit_transform(corpus)
report("CountVectorizer(vocabulary=list): columns in the given order (not sorted), unseen term gives a zero column, other tokens ignored", cvv.get_feature_names_out().tolist() == ["document", "this", "zebra"] and dense(Xv).tolist() == [[1, 1, 0], [2, 1, 0], [0, 1, 0], [1, 1, 0]] and cvv.fixed_vocabulary_)
cvd = CountVectorizer(vocabulary={"this": 1, "document": 0}); Xvd = cvd.fit_transform(corpus)
report("CountVectorizer(vocabulary=dict term->index): columns placed at the given indices", cvd.get_feature_names_out().tolist() == ["document", "this"] and dense(Xvd).tolist() == [[1, 1], [2, 1], [0, 1], [1, 1]])
try:
    CountVectorizer(vocabulary={"a": 0, "b": 2}).fit(corpus); report("CountVectorizer(vocabulary with a gap in indices) raises ValueError ('should not have any gap')", False)
except ValueError: report("CountVectorizer(vocabulary with a gap in indices) raises ValueError ('should not have any gap')", True)
report("CountVectorizer(vocabulary given, min_df/max_df/max_features ignored)", CountVectorizer(vocabulary=["and", "the"], min_df=3, max_features=1).fit(corpus).get_feature_names_out().tolist() == ["and", "the"])
cva = CountVectorizer(analyzer=lambda d: d.split("|")); Xa_ = cva.fit_transform(["a|b b|c", "b b|a"])
report("CountVectorizer(analyzer=callable): 'used to extract the sequence of features out of the raw, unprocessed input' (no lowercasing / tokenising)", cva.get_feature_names_out().tolist() == ["a", "b b", "c"] and dense(Xa_).tolist() == [[1, 1, 1], [1, 1, 0]])
acc = ["Résumé naïve Ça façade Über"]
def strip_ascii(s): return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
def strip_uni(s): return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
for mode, fn in (("ascii", strip_ascii), ("unicode", strip_uni)):
    cvacc = CountVectorizer(strip_accents=mode).fit(acc); v, _ = ref_matrix(acc, lambda d: ref_word_tokens(fn(d)))
    report(f"CountVectorizer(strip_accents='{mode}'): accents removed before tokenising (reference: NFKD + {'ascii encode/ignore' if mode == 'ascii' else 'drop combining marks'}) -> {v}", cvacc.get_feature_names_out().tolist() == v, f"(got {cvacc.get_feature_names_out().tolist()})")
cvg = CountVectorizer(token_pattern=r"\b(\w)\w*\b"); Xg = cvg.fit_transform(["alpha beta apple"])
report("CountVectorizer(token_pattern with one capturing group): 'the captured group content, not the entire match, becomes the token'", cvg.get_feature_names_out().tolist() == ["a", "b"] and dense(Xg).tolist() == [[2, 1]])
try:
    CountVectorizer(token_pattern=r"(\w)(\w+)").fit(["ab cd"]); report("CountVectorizer(token_pattern with two capturing groups) raises ValueError ('At most one capturing group')", False)
except ValueError: report("CountVectorizer(token_pattern with two capturing groups) raises ValueError ('At most one capturing group')", True)
report("CountVectorizer(dtype=np.float32) returns that dtype", CountVectorizer(dtype=np.float32).fit_transform(corpus).dtype == np.float32)
report("CountVectorizer.transform on new documents ignores unseen tokens and keeps the fitted columns", dense(cv.transform(["the zebra document document"])).tolist() == [[0, 2, 0, 0, 0, 0, 1, 0, 0]])
report("CountVectorizer.inverse_transform returns the terms with nonzero counts per document", sorted(cv.inverse_transform(Xc[0])[0].tolist()) == ["document", "first", "is", "the", "this"])
try:
    CountVectorizer().fit("a single string"); report("CountVectorizer.fit on a single string raises ValueError ('Iterable over raw text documents expected')", False)
except ValueError: report("CountVectorizer.fit on a single string raises ValueError ('Iterable over raw text documents expected')", True)
try:
    CountVectorizer().fit(["a", "b c"]); report("CountVectorizer with an empty vocabulary (only 1-character tokens) raises ValueError ('empty vocabulary')", False)
except ValueError: report("CountVectorizer with an empty vocabulary (only 1-character tokens) raises ValueError ('empty vocabulary')", True)

# =============================================================================
print("== feature_extraction.text: TfidfTransformer / TfidfVectorizer / HashingVectorizer")
C = dense(Xc).astype(float); ndoc, nterm = C.shape; df = (C > 0).sum(0)
def tfidf_truth(C, smooth, sublinear, norm, use_idf=True):
    n, m = C.shape; out = []
    df = [sum(1 for i in range(n) if C[i, j] > 0) for j in range(m)]
    idf = [mpmath.log(mpf(1 + n) / (1 + df[j])) + 1 if smooth else mpmath.log(mpf(n) / df[j]) + 1 for j in range(m)] if use_idf else [mpf(1)] * m
    for i in range(n):
        row = [(1 + mpmath.log(mpf(C[i, j])) if C[i, j] > 0 else mpf(0)) if sublinear else mpf(C[i, j]) for j in range(m)]
        row = [row[j] * idf[j] for j in range(m)]
        if norm == "l2": nv = mpmath.sqrt(sum(v * v for v in row)); row = [v / nv for v in row] if nv else row
        elif norm == "l1": nv = sum(abs(v) for v in row); row = [v / nv for v in row] if nv else row
        out.append([float(v) for v in row])
    return np.array(out), [float(v) for v in idf]
for smooth in (True, False):
    for sub in (False, True):
        for norm in ("l2", "l1", None):
            tt = TfidfTransformer(smooth_idf=smooth, sublinear_tf=sub, norm=norm).fit(Xc); Zt = dense(tt.transform(Xc)); T, idf_ref = tfidf_truth(C, smooth, sub, norm)
            report(f"TfidfTransformer(smooth_idf={smooth}, sublinear_tf={sub}, norm={norm}): idf = {'ln((1+n)/(1+df))+1' if smooth else 'ln(n/df)+1'}, tf = {'1+ln(tf)' if sub else 'tf'}, {norm or 'no'} row normalisation (mpmath, rel 1e-12)", allclose(tt.idf_, idf_ref, 1e-12) and allclose(Zt, T, 1e-12))
tn = TfidfTransformer(use_idf=False, norm=None).fit(Xc)
report("TfidfTransformer(use_idf=False, norm=None) returns the raw counts as float ('If False, idf(t) = 1')", np.array_equal(dense(tn.transform(Xc)), C) and dense(tn.transform(Xc)).dtype == np.float64)
Xc32 = TfidfTransformer().fit_transform(Xc.astype(np.float32))
report("TfidfTransformer on float32 counts keeps float32 and values within 1e-6", Xc32.dtype == np.float32 and allclose(dense(Xc32), tfidf_truth(C, True, False, "l2")[0], 1e-6))
tv = TfidfVectorizer(); Ztv = tv.fit_transform(corpus)
report("TfidfVectorizer = CountVectorizer followed by TfidfTransformer ('Equivalent to CountVectorizer followed by TfidfTransformer'): same vocabulary, idf_ and values (exact)", tv.get_feature_names_out().tolist() == cv.get_feature_names_out().tolist() and np.array_equal(dense(Ztv), dense(TfidfTransformer().fit_transform(Xc))) and np.array_equal(tv.idf_, TfidfTransformer().fit(Xc).idf_))
tv2 = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, norm="l1", smooth_idf=False, min_df=2); Z2 = tv2.fit_transform(corpus)
cv_2 = CountVectorizer(ngram_range=(1, 2), min_df=2); Xc2 = cv_2.fit_transform(corpus)
report("TfidfVectorizer(ngram (1,2), sublinear, l1, smooth_idf=False, min_df=2) = CountVectorizer(same) + TfidfTransformer(same) and equals the mpmath recomputation", allclose(dense(Z2), dense(TfidfTransformer(sublinear_tf=True, norm="l1", smooth_idf=False).fit_transform(Xc2)), 1e-14) and allclose(dense(Z2), tfidf_truth(dense(Xc2).astype(float), False, True, "l1")[0], 1e-12))
report("TfidfVectorizer.transform on new docs = counts * fitted idf_, l2-normalised", allclose(dense(tv.transform(["the document"])).ravel(), (lambda r: r / np.linalg.norm(r))(np.array([0, 1, 0, 0, 0, 0, 1, 0, 0]) * tv.idf_), 1e-12))
def hash_ref(tokens_list, n_features, alternate_sign, binary=False):
    """Column = |murmurhash3_32(token, seed=0, signed)| mod n_features; sign of the hash flips the value when alternate_sign."""
    M = np.zeros((len(tokens_list), n_features))
    for i, toks in enumerate(tokens_list):
        for t in toks:
            h = int(murmurhash3_32(t, seed=0, positive=False)); M[i, abs(h) % n_features] += (1 if h >= 0 else -1) if alternate_sign else 1
    if binary: M = np.sign(M) * (M != 0)  # not used
    return M
for alt in (True, False):
    hv = HashingVectorizer(n_features=16, alternate_sign=alt, norm=None); Zh = dense(hv.transform(corpus)); Th = hash_ref([ref_word_tokens(d) for d in corpus], 16, alt)
    report(f"HashingVectorizer(n_features=16, alternate_sign={alt}, norm=None): column = |murmurhash3_32(token, seed=0)| mod 16 ('signed 32-bit version of Murmurhash3'), value {'signed by the hash sign' if alt else '+1 per occurrence'} (recomputed with sklearn.utils.murmurhash3_32; collisions summed)", np.array_equal(Zh, Th), f"(nnz {np.count_nonzero(Th)} of {Th.size}; collisions {sum(len(set(abs(int(murmurhash3_32(t, seed=0, positive=False))) % 16 for t in ref_word_tokens(d))) != len(set(ref_word_tokens(d))) for d in corpus)} docs)")
hv2 = HashingVectorizer(n_features=16, norm="l2"); Zh2 = dense(hv2.transform(corpus)); Th2 = hash_ref([ref_word_tokens(d) for d in corpus], 16, True)
report("HashingVectorizer(norm='l2') = the signed hashed counts l2-normalised per row", allclose(Zh2, Th2 / np.linalg.norm(Th2, axis=1, keepdims=True), 1e-12))
hv3 = HashingVectorizer(n_features=16, norm=None, binary=True, alternate_sign=False); Zh3 = dense(hv3.transform(corpus))
report("HashingVectorizer(binary=True, alternate_sign=False): non-zero entries set to 1", np.array_equal(Zh3, (hash_ref([ref_word_tokens(d) for d in corpus], 16, False) > 0).astype(float)))
hv4 = HashingVectorizer(n_features=2 ** 20, norm=None, alternate_sign=False, analyzer="char_wb", ngram_range=(2, 3)); Zh4 = hv4.transform(docs_wb)
Th4 = hash_ref([ref_char_wb_ngrams(d, (2, 3)) for d in docs_wb], 2 ** 20, False)
report("HashingVectorizer(analyzer='char_wb', n_features=2**20) = FeatureHasher applied to the char_wb reference n-grams", np.array_equal(dense(Zh4), Th4) and Zh4.shape == (2, 2 ** 20))
report("HashingVectorizer is stateless: transform without fit works and fit_transform gives the same", np.array_equal(dense(HashingVectorizer(n_features=16, norm=None).fit_transform(corpus)), dense(HashingVectorizer(n_features=16, norm=None).transform(corpus))))
# FeatureHasher
fh = FeatureHasher(n_features=10, alternate_sign=False)
D = [{"dog": 1, "cat": 2, "elephant": 4}, {"dog": 2, "run": 5, "color": "red", "zero": 0}]
def fh_ref(rows, n_features, alt):
    M = np.zeros((len(rows), n_features))
    for i, feats in enumerate(rows):
        for f, v in feats:
            if isinstance(v, str): f, v = f"{f}={v}", 1
            if v == 0: continue
            h = int(murmurhash3_32(f, seed=0, positive=False)); M[i, abs(h) % n_features] += v * ((1 if h >= 0 else -1) if alt else 1)
    return M
report("FeatureHasher(input_type='dict', alternate_sign=False): value summed at |murmurhash3_32(name)| mod n_features; string values hashed as 'name=value' with value 1; zero values dropped", np.array_equal(dense(fh.transform(D)), fh_ref([list(d.items()) for d in D], 10, False)) and fh.transform(D).nnz <= 7)
fhs = FeatureHasher(n_features=10, alternate_sign=True)
report("FeatureHasher(alternate_sign=True): 'an alternating sign is added to the features' -> sign of the hash", np.array_equal(dense(fhs.transform(D)), fh_ref([list(d.items()) for d in D], 10, True)))
report("FeatureHasher docstring example: n_features=10, [{'dog':1,'cat':2,'elephant':4},{'dog':2,'run':5}] -> the printed matrix", dense(FeatureHasher(n_features=10).transform([{"dog": 1, "cat": 2, "elephant": 4}, {"dog": 2, "run": 5}])).tolist() == [[0, 0, -4, -1, 0, 0, 0, 0, 0, 2], [0, 0, 0, -2, -5, 0, 0, 0, 0, 0]])
fp = FeatureHasher(n_features=10, input_type="pair", alternate_sign=False)
report("FeatureHasher(input_type='pair') accepts (name, value) pairs with the same hashing", np.array_equal(dense(fp.transform([[("dog", 1), ("cat", 2)], [("dog", 2)]])), fh_ref([[("dog", 1), ("cat", 2)], [("dog", 2)]], 10, False)))
fst = FeatureHasher(n_features=10, input_type="string", alternate_sign=False)
report("FeatureHasher(input_type='string'): 'a value of 1 is implied' per string (repeats add up)", np.array_equal(dense(fst.transform([["dog", "cat", "dog"], ["run"]])), fh_ref([[("dog", 1), ("cat", 1), ("dog", 1)], [("run", 1)]], 10, False)))
report("FeatureHasher output is CSR float64 by default; dtype=np.float32 honoured", fh.transform(D).format == "csr" and fh.transform(D).dtype == np.float64 and FeatureHasher(n_features=10, dtype=np.float32).transform(D).dtype == np.float32)
report("FeatureHasher: unicode and its utf-8 bytes hash to the same column ('Unicode strings are converted to UTF-8 first')", np.array_equal(dense(fst.transform([["café"]])), dense(fst.transform([["café".encode("utf-8")]]))) if V >= (1, 3) else True)

# =============================================================================
print("== feature_extraction: DictVectorizer")
Dd = [{"foo": 1, "bar": 2}, {"foo": 3, "baz": 1}]
dv = DictVectorizer(sparse=False); Xdv = dv.fit_transform(Dd)
report("DictVectorizer docstring example: feature_names_ ['bar','baz','foo'] (sorted), dense [[2,0,1],[0,1,3]]", dv.get_feature_names_out().tolist() == ["bar", "baz", "foo"] and Xdv.tolist() == [[2, 0, 1], [0, 1, 3]] and dv.transform({"foo": 4, "unseen_feature": 3}).tolist() == [[0, 0, 4]])
Dstr = [{"city": "Dubai", "temperature": 33.0}, {"city": "London", "temperature": 12.0}, {"city": "San Francisco", "temperature": 18.0}]
dvs = DictVectorizer(); Xds = dvs.fit_transform(Dstr)
report("DictVectorizer: string values one-hot as 'city=Dubai' etc. ('one boolean-valued feature ... for each of the possible string values'), numeric passthrough, sorted names, sparse CSR by default",
       dvs.get_feature_names_out().tolist() == ["city=Dubai", "city=London", "city=San Francisco", "temperature"] and dense(Xds).tolist() == [[1, 0, 0, 33], [0, 1, 0, 12], [0, 0, 1, 18]] and sp.issparse(Xds) and Xds.format == "csr")
dvu = DictVectorizer(sort=False).fit([{"zeta": 1, "alpha": 2}, {"beta": "x"}])
report("DictVectorizer(sort=False): feature_names_ in order of first appearance ['zeta','alpha','beta=x']", dvu.get_feature_names_out().tolist() == ["zeta", "alpha", "beta=x"])
report("DictVectorizer(separator='|') builds 'city|Dubai'", DictVectorizer(separator="|").fit(Dstr).get_feature_names_out().tolist()[0] == "city|Dubai")
report("DictVectorizer.inverse_transform recovers the dicts (numeric values and one-hot as 'city=Dubai': 1)", dvs.inverse_transform(Xds) == [{"city=Dubai": 1.0, "temperature": 33.0}, {"city=London": 1.0, "temperature": 12.0}, {"city=San Francisco": 1.0, "temperature": 18.0}], f"({dvs.inverse_transform(Xds)[0]})")
report("DictVectorizer.transform: 'Features that do not occur in a sample will have a zero value'; unseen features are ignored (documented in the example)", dense(dvs.transform([{"city": "Paris", "temperature": 5.0}])).tolist() == [[0, 0, 0, 5]])
report("DictVectorizer(dtype=np.int32) honoured", DictVectorizer(dtype=np.int32).fit_transform(Dd).dtype == np.int32)
if V >= (1, 1):
    dvi = DictVectorizer(sparse=False).fit([{"tags": ["a", "b", "a"]}, {"tags": ["b"]}])
    report("DictVectorizer with a sequence of strings as value: 'will iterate over the values and will count the occurrences of each string value' -> tags=a: 2, tags=b: 1", dvi.get_feature_names_out().tolist() == ["tags=a", "tags=b"] and dvi.transform([{"tags": ["a", "b", "a"]}, {"tags": ["b"]}]).tolist() == [[2, 1], [0, 1]], f"({dvi.get_feature_names_out().tolist()}, {dvi.transform([{'tags': ['a', 'b', 'a']}]).tolist()})")
report("DictVectorizer.restrict(support) keeps only the selected features", DictVectorizer(sparse=False).fit(Dstr).restrict(np.array([True, False, False, True])).get_feature_names_out().tolist() == ["city=Dubai", "temperature"])

# =============================================================================
print("== feature_extraction.image: patches / graphs")
img = np.arange(30, dtype=float).reshape(5, 6) * 1.5 - 7
def patches_ref(im, ph, pw):
    H, W = im.shape[:2]; return np.array([im[i:i + ph, j:j + pw] for i in range(H - ph + 1) for j in range(W - pw + 1)])
P = extract_patches_2d(img, (2, 3)); Pr = patches_ref(img, 2, 3)
report("extract_patches_2d(5x6, (2,3)): (5-2+1)*(6-3+1) = 16 patches, row-major order (top-left to bottom-right), values exact", P.shape == (16, 2, 3) and np.array_equal(P, Pr))
img3 = np.stack([img, img * 2, img - 1], -1); P3 = extract_patches_2d(img3, (2, 3))
report("extract_patches_2d on a (5,6,3) colour image: patches (16, 2, 3, 3) with channels last, exact", P3.shape == (16, 2, 3, 3) and np.array_equal(P3, patches_ref(img3, 2, 3)))
P5 = extract_patches_2d(img, (2, 3), max_patches=5, random_state=0); P5b = extract_patches_2d(img, (2, 3), max_patches=5, random_state=0)
report("extract_patches_2d(max_patches=5, random_state=0): exactly 5 patches, deterministic, each a genuine patch of the image", P5.shape == (5, 2, 3) and np.array_equal(P5, P5b) and all(any(np.array_equal(p, q) for q in Pr) for p in P5))
P25 = extract_patches_2d(img, (2, 3), max_patches=0.25, random_state=1)
report("extract_patches_2d(max_patches=0.25 float): 'a proportion of the total number of patches' -> int(0.25 * 16) = 4 patches", P25.shape == (4, 2, 3))
P100 = extract_patches_2d(img, (2, 3), max_patches=100, random_state=0); nuniq = len({p.tobytes() for p in P100})
print(f"   max_patches=100 (> 16 total): {P100.shape[0]} patches returned, {nuniq} distinct")
report("extract_patches_2d(max_patches=100 > total): docstring 'n_patches is either max_patches or the total number of patches that can be extracted' -> the 16 patches (all distinct)", P100.shape[0] == 16 and nuniq == 16, f"({P100.shape[0]} returned, {nuniq} distinct: sampled with replacement)")
P12 = extract_patches_2d(img, (2, 3), max_patches=12, random_state=0); n12 = len({p.tobytes() for p in P12})
report("extract_patches_2d(max_patches=12 of 16): 12 distinct patches ('The maximum number of patches to extract')", P12.shape[0] == 12 and n12 == 12, f"({n12} distinct of 12: sampled with replacement)")
try:
    extract_patches_2d(img, (6, 3)); report("extract_patches_2d with patch height > image height raises ValueError", False)
except ValueError: report("extract_patches_2d with patch height > image height raises ValueError", True)
R = reconstruct_from_patches_2d(P, (5, 6))
report("reconstruct_from_patches_2d(all patches) recovers the image exactly", np.array_equal(R, img))
Pm = P.copy(); Pm[3] += 10.0; Pm[10] -= 4.0
def reconstruct_ref(patches, H, W):
    ph, pw = patches.shape[1:3]; acc = [[F(0)] * W for _ in range(H)]; cnt = [[0] * W for _ in range(H)]; k = 0
    for i in range(H - ph + 1):
        for j in range(W - pw + 1):
            for a in range(ph):
                for b in range(pw): acc[i + a][j + b] += F(patches[k, a, b]); cnt[i + a][j + b] += 1
            k += 1
    return np.array([[float(acc[i][j] / cnt[i][j]) for j in range(W)] for i in range(H)])
report("reconstruct_from_patches_2d with perturbed patches: each pixel = mean of the overlapping patch values ('averaging the overlapping regions', exact Fractions)", allclose(reconstruct_from_patches_2d(Pm, (5, 6)), reconstruct_ref(Pm, 5, 6), 1e-14))
R3 = reconstruct_from_patches_2d(P3, (5, 6, 3))
report("reconstruct_from_patches_2d for colour patches recovers the (5,6,3) image", np.array_equal(R3, img3))
pe = PatchExtractor(patch_size=(2, 3)).fit(np.stack([img, img + 1]))
Ppe = pe.transform(np.stack([img, img + 1]))
report("PatchExtractor(patch_size=(2,3)).transform on 2 images = the concatenated extract_patches_2d results (32 patches)", Ppe.shape == (32, 2, 3) and np.array_equal(Ppe[:16], Pr) and np.array_equal(Ppe[16:], Pr + 1))
pe2 = PatchExtractor(patch_size=(2, 3), max_patches=3, random_state=0)
report("PatchExtractor(max_patches=3) gives 3 patches per image", pe2.transform(np.stack([img, img + 1])).shape == (6, 2, 3))
pe3 = PatchExtractor().fit(np.zeros((1, 40, 60)))
report("PatchExtractor(patch_size=None): patch size = (img_height // 10, img_width // 10) = (4, 6)", pe3.transform(np.zeros((1, 40, 60))).shape[1:] == (4, 6))
G = grid_to_graph(3, 4); Gd = dense(G)
def grid_edges(nx, ny):
    idx = lambda x, y: x * ny + y; E = set()
    for x in range(nx):
        for y in range(ny):
            if y + 1 < ny: E.add((idx(x, y), idx(x, y + 1)))
            if x + 1 < nx: E.add((idx(x, y), idx(x + 1, y)))
    return E
E = grid_edges(3, 4); Ad = np.zeros((12, 12), int)
for a, b in E: Ad[a, b] = Ad[b, a] = 1
print(f"   grid_to_graph(3,4): nnz {G.nnz}, diagonal {np.diag(Gd).tolist()}")
report("grid_to_graph(3, 4): symmetric 4-connectivity adjacency (17 undirected edges, 'Edges exist if 2 voxels are connected') plus a unit diagonal (self-loops, measured), int dtype", np.array_equal(Gd - np.diag(np.diag(Gd)), Ad) and np.all(np.diag(Gd) == 1) and G.nnz == 2 * 17 + 12 and Gd.dtype.kind == "i")
mask = np.ones((3, 4), bool); mask[0, 0] = False; mask[2, 3] = False
Gm = dense(grid_to_graph(3, 4, mask=mask))
report("grid_to_graph(mask): only the masked-in voxels (10) are nodes and edges between them kept", Gm.shape == (10, 10) and (Gm - np.eye(10, dtype=int)).sum() // 2 == sum(1 for a, b in E if mask.ravel()[a] and mask.ravel()[b]))
img_g = np.array([[1.0, 2.0, 4.0, 8.0], [0.5, 3.0, 2.5, 1.0], [9.0, 0.0, 1.0, 1.0]])
IG = dense(img_to_graph(img_g))
Wref = np.zeros((12, 12))
for a, b in grid_edges(3, 4): Wref[a, b] = Wref[b, a] = abs(img_g.ravel()[a] - img_g.ravel()[b])
report("img_to_graph: 'Edges are weighted with the gradient values' = |pixel_i - pixel_j| for 4-neighbours (exact); diagonal = pixel values (measured); dtype = img dtype",
       np.array_equal(IG - np.diag(np.diag(IG)), Wref) and np.array_equal(np.diag(IG), img_g.ravel()) and IG.dtype == img_g.dtype)
report("img_to_graph(return_as=np.ndarray) gives the dense array; dtype=np.float32 honoured", isinstance(img_to_graph(img_g, return_as=np.ndarray), np.ndarray) and img_to_graph(img_g, dtype=np.float32).dtype == np.float32)
Gz = dense(grid_to_graph(2, 2, 2))
report("grid_to_graph(2,2,2) 3-D: 12 undirected edges (6-connectivity) + 8 self-loops", (Gz.sum() - 8) // 2 == 12 and Gz.shape == (8, 8))

# =============================================================================
print("== impute: KNNImputer (nan_euclidean recomputed) / MissingIndicator / SimpleImputer options")
NA = np.nan
Xk = np.array([[1.0, 2.0, NA, 4.0], [2.0, NA, 3.0, 5.0], [NA, 3.0, 1.0, 7.0], [3.0, 4.0, 3.5, NA], [4.5, 1.0, 2.0, 6.0], [0.5, 2.5, 4.0, 3.0], [6.0, 5.0, NA, 2.0]])
def nan_euclid(a, b):
    """Documented: sqrt(weight * sq. distance over present coordinates), weight = n_coords / n_present; NaN if none present."""
    pres = [j for j in range(len(a)) if not math.isnan(a[j]) and not math.isnan(b[j])]
    if not pres: return None
    return mpmath.sqrt(mpf(len(a)) / len(pres) * sum((mpf(a[j]) - mpf(b[j])) ** 2 for j in pres))
def knn_ref(Xfit, X, k, weights):
    """Documented: 'Each sample's missing values are imputed using the mean value from n_neighbors nearest neighbors found
    in the training set' and 'nearest neighbors that have a value for the feature' (user guide)."""
    out = X.copy()
    for i in range(X.shape[0]):
        for c in range(X.shape[1]):
            if not math.isnan(X[i, c]): continue
            donors = [(nan_euclid(X[i], Xfit[d]), d) for d in range(Xfit.shape[0]) if not math.isnan(Xfit[d, c])]
            donors = [(dist, d) for dist, d in donors if dist is not None]
            if not donors: out[i, c] = float(np.nanmean(Xfit[:, c])); continue
            donors.sort(key=lambda t: t[0]); sel = donors[:k]
            if weights == "uniform": out[i, c] = float(sum(mpf(Xfit[d, c]) for _, d in sel) / len(sel))
            else:
                w = [1 / dist for dist, _ in sel]; out[i, c] = float(sum(wi * mpf(Xfit[d, c]) for wi, (_, d) in zip(w, sel)) / sum(w))
    return out
d01 = nan_euclid(Xk[0], Xk[1]); print(f"   nan_euclidean(row0,row1) = sqrt(4/2 * ((1-2)^2 + (4-5)^2)) = {float(d01):.6f} (=2)")
for k in (1, 2, 3):
    for w in ("uniform", "distance"):
        ki = KNNImputer(n_neighbors=k, weights=w).fit(Xk); Zk = ki.transform(Xk); Tk = knn_ref(Xk, Xk, k, w)
        report(f"KNNImputer(n_neighbors={k}, weights='{w}') on the training data: nan_euclidean donors with a value for the feature, {'mean' if w == 'uniform' else '1/distance-weighted mean'} of the {k} nearest (recomputed, rel 1e-12)", allclose(Zk, Tk, 1e-12), f"(max diff {np.nanmax(np.abs(Zk - Tk)):.1e})")
Xnew = np.array([[NA, 2.0, 3.0, NA], [1.0, NA, NA, 4.0], [NA, NA, NA, NA]])
ki = KNNImputer(n_neighbors=2).fit(Xk); Zn = ki.transform(Xnew); Tn = knn_ref(Xk, Xnew, 2, "uniform")
report("KNNImputer.transform on new rows (donors from the training set); an all-NaN row (no common coordinates) gets the training column means", allclose(Zn, Tn, 1e-12) and allclose(Zn[2], np.nanmean(Xk, 0), 1e-12))
report("KNNImputer(n_neighbors=10 > number of donors) uses all available donors", allclose(KNNImputer(n_neighbors=10).fit_transform(Xk), knn_ref(Xk, Xk, 10, "uniform"), 1e-12))
ki_ind = KNNImputer(n_neighbors=2, add_indicator=True).fit(Xk); Zi = ki_ind.transform(Xk)
report("KNNImputer(add_indicator=True): imputed columns followed by the MissingIndicator columns (one per feature with missing values at fit: all 4 here)", Zi.shape == (7, 8) and allclose(Zi[:, :4], knn_ref(Xk, Xk, 2, "uniform"), 1e-12) and np.array_equal(Zi[:, 4:], np.isnan(Xk).astype(float)))
Xe = Xk.copy(); Xe[:, 1] = NA
if has_param(KNNImputer, "keep_empty_features"):
    Zke = KNNImputer(n_neighbors=2, keep_empty_features=True).fit_transform(Xe); Zkd = KNNImputer(n_neighbors=2).fit_transform(Xe)
    report("KNNImputer: an all-missing feature is dropped by default; keep_empty_features=True keeps it 'imputed value is always 0'", Zkd.shape == (7, 3) and Zke.shape == (7, 4) and np.all(Zke[:, 1] == 0) and allclose(Zke[:, [0, 2, 3]], Zkd, 1e-12))
    report("KNNImputer with an all-missing feature: other columns imputed with the 3 remaining coordinates (weight 3/n_present)", allclose(Zkd, knn_ref(Xe[:, [0, 2, 3]], Xe[:, [0, 2, 3]], 2, "uniform"), 1e-12))
Zk32 = KNNImputer(n_neighbors=2).fit_transform(Xk.astype(np.float32))
report("KNNImputer on float32 input: float32 output within 1e-6 of the exact imputation", Zk32.dtype == np.float32 and allclose(Zk32, knn_ref(Xk, Xk, 2, "uniform"), 1e-6, 1e-6))
report("KNNImputer(missing_values=-1) treats -1 as missing", allclose(KNNImputer(n_neighbors=2, missing_values=-1).fit_transform(np.where(np.isnan(Xk), -1, Xk)), knn_ref(Xk, Xk, 2, "uniform"), 1e-12))
report("KNNImputer with no missing values returns the input unchanged", np.array_equal(KNNImputer().fit_transform(np.nan_to_num(Xk)), np.nan_to_num(Xk)))
report("KNNImputer.get_feature_names_out drops the empty feature and appends 'missingindicator_x..' with add_indicator", KNNImputer(add_indicator=True).fit(Xk).get_feature_names_out().tolist() == ["x0", "x1", "x2", "x3", "missingindicator_x0", "missingindicator_x1", "missingindicator_x2", "missingindicator_x3"])
# MissingIndicator
Xmi = np.array([[1.0, NA, 3.0, 4.0], [NA, 2.0, 3.0, 5.0], [1.0, 2.0, 3.0, NA]])
mi = MissingIndicator().fit(Xmi)
report("MissingIndicator(features='missing-only'): features_ = columns with missing values at fit [0, 1, 3]; transform = boolean mask of those columns", mi.features_.tolist() == [0, 1, 3] and np.array_equal(mi.transform(Xmi), np.isnan(Xmi)[:, [0, 1, 3]]) and mi.transform(Xmi).dtype == bool)
mia = MissingIndicator(features="all").fit(Xmi)
report("MissingIndicator(features='all'): all 4 columns, mask = isnan(X)", mia.features_.tolist() == [0, 1, 2, 3] and np.array_equal(mia.transform(Xmi), np.isnan(Xmi)))
try:
    mi.transform(np.array([[1.0, 2.0, NA, 4.0]])); report("MissingIndicator(error_on_new=True) raises ValueError when a feature without missing values at fit has missing values at transform", False)
except ValueError: report("MissingIndicator(error_on_new=True) raises ValueError when a feature without missing values at fit has missing values at transform", True)
mie = MissingIndicator(error_on_new=False).fit(Xmi)
report("MissingIndicator(error_on_new=False) ignores missing values in new columns (only features_ reported)", np.array_equal(mie.transform(np.array([[1.0, 2.0, NA, 4.0]])), [[False, False, False]]))
report("MissingIndicator(sparse=True) returns a CSC/CSR sparse mask; sparse='auto' on dense input gives dense", sp.issparse(MissingIndicator(sparse=True).fit_transform(Xmi)) and not sp.issparse(MissingIndicator().fit_transform(Xmi)) and np.array_equal(dense(MissingIndicator(sparse=True).fit_transform(Xmi)), np.isnan(Xmi)[:, [0, 1, 3]]))
Xms = sp.csr_matrix(np.where(np.isnan(Xmi), -1.0, Xmi))
report("MissingIndicator(missing_values=-1) on a CSR matrix: sparse='auto' -> sparse output with the same mask", sp.issparse(MissingIndicator(missing_values=-1).fit_transform(Xms)) and np.array_equal(dense(MissingIndicator(missing_values=-1).fit_transform(Xms)), np.isnan(Xmi)[:, [0, 1, 3]]))
report("MissingIndicator.get_feature_names_out = 'missingindicator_<name>' for features_", mi.get_feature_names_out(["a", "b", "c", "d"]).tolist() == ["missingindicator_a", "missingindicator_b", "missingindicator_d"])
# SimpleImputer most_frequent / constant / strings / keep_empty_features
Xmf = np.array([[3.0, 1.0], [1.0, 1.0], [NA, 2.0], [3.0, 2.0], [1.0, NA], [5.0, 3.0]])
smf = SimpleImputer(strategy="most_frequent").fit(Xmf)
report("SimpleImputer(most_frequent) numeric tie (1 and 3 twice each, 1 and 2 twice each): 'only the smallest is returned' -> statistics_ [1, 1]", smf.statistics_.tolist() == [1.0, 1.0] and smf.transform(Xmf)[2, 0] == 1.0 and smf.transform(Xmf)[4, 1] == 1.0, f"({smf.statistics_.tolist()})")
Xstr = np.array([["b", "x"], ["a", NA], ["b", "y"], ["a", "y"], [NA, "x"]], dtype=object)
sms = SimpleImputer(strategy="most_frequent").fit(Xstr)
report("SimpleImputer(most_frequent) on strings: tie a/b -> smallest 'a'; x/y tie -> 'x'; NaN replaced", sms.statistics_.tolist() == ["a", "x"] and sms.transform(Xstr)[4, 0] == "a" and sms.transform(Xstr)[1, 1] == "x", f"({sms.statistics_.tolist()})")
smc = SimpleImputer(strategy="constant").fit(Xstr)
report("SimpleImputer(strategy='constant') on strings: default fill_value 'missing_value'", smc.transform(Xstr)[4, 0] == "missing_value" and smc.statistics_.tolist() == ["missing_value", "missing_value"])
smn = SimpleImputer(strategy="constant", fill_value=-9).fit(Xmf)
report("SimpleImputer(strategy='constant', fill_value=-9) numeric; default fill_value for numeric data is 0", smn.transform(Xmf)[2, 0] == -9 and SimpleImputer(strategy="constant").fit_transform(Xmf)[2, 0] == 0)
report("SimpleImputer(most_frequent) with the missing placeholder more frequent than any value: statistics_ ignores the placeholder", SimpleImputer(strategy="most_frequent").fit(np.array([[NA], [NA], [NA], [2.0], [7.0]])).statistics_.tolist() == [2.0])
try:
    SimpleImputer(strategy="mean").fit(Xstr); report("SimpleImputer(strategy='mean') on strings raises ValueError ('Can only be used with numeric data')", False)
except ValueError: report("SimpleImputer(strategy='mean') on strings raises ValueError ('Can only be used with numeric data')", True)
Xemp = np.array([[1.0, NA], [2.0, NA], [NA, NA]])
if has_param(SimpleImputer, "keep_empty_features"):
    report("SimpleImputer(mean): an all-missing feature is dropped by default (output 1 column); keep_empty_features=True keeps it as 0; with strategy='constant' as fill_value",
           SimpleImputer().fit_transform(Xemp).shape == (3, 1) and SimpleImputer(keep_empty_features=True).fit_transform(Xemp)[:, 1].tolist() == [0, 0, 0]
           and SimpleImputer(strategy="constant", fill_value=7, keep_empty_features=True).fit_transform(Xemp)[:, 1].tolist() == [7, 7, 7])
    report("SimpleImputer(most_frequent, keep_empty_features=True): empty feature imputed with 0", SimpleImputer(strategy="most_frequent", keep_empty_features=True).fit_transform(Xemp)[:, 1].tolist() == [0, 0, 0])
if V >= (1, 5):
    scb = SimpleImputer(strategy=lambda col: float(np.max(col))).fit(Xmf)
    report("SimpleImputer(strategy=callable): 'scalar statistic returned by running the callable over a dense 1d array containing non-missing values of each column' -> max = [5, 3]", scb.statistics_.tolist() == [5.0, 3.0])
smi = SimpleImputer(strategy="median", add_indicator=True).fit(Xmf)
report("SimpleImputer(add_indicator=True): indicator columns appended for the features with missing values", smi.transform(Xmf).shape == (6, 4) and np.array_equal(smi.transform(Xmf)[:, 2:], np.isnan(Xmf).astype(float)))
Xsi = sp.csc_matrix(np.array([[1.0, 0.0], [0.0, 3.0], [-1.0, -1.0]]))
report("SimpleImputer(missing_values=-1, strategy='mean') on CSC: explicit zeros count in the mean ([[1,0],[0,3],[-1,-1]] -> means 0.5, 1.5)", dense(SimpleImputer(missing_values=-1, strategy="mean").fit_transform(Xsi)).tolist() == [[1, 0], [0, 3], [0.5, 1.5]])

# =============================================================================
print("== impute: IterativeImputer (one round recomputed with exact OLS)")
Xit = np.array([[1.0, 2.0, 3.0], [2.0, NA, 5.5], [NA, 3.0, 2.0], [4.0, 5.0, NA], [5.0, 4.5, 8.0], [NA, 1.0, 1.5], [3.0, 3.5, 4.0], [6.0, NA, 9.5], [2.5, 2.0, 2.5]])
mean0 = np.nanmean(Xit, 0)
ii0 = IterativeImputer(max_iter=0).fit(Xit)
report("IterativeImputer(max_iter=0): result = the initial (mean) imputation, n_iter_ = 0", allclose(ii0.transform(Xit), np.where(np.isnan(Xit), mean0, Xit), 1e-14) and ii0.n_iter_ == 0 and allclose(ii0.transform(Xit), SimpleImputer().fit_transform(Xit), 1e-14))
ii0m = IterativeImputer(max_iter=0, initial_strategy="median").fit(Xit)
report("IterativeImputer(max_iter=0, initial_strategy='median') = SimpleImputer(median)", allclose(ii0m.transform(Xit), SimpleImputer(strategy="median").fit_transform(Xit), 1e-14))
def iterative_round_ref(X, order, n_rounds=1, lo=None, hi=None):
    """One (or more) rounds of chained-equation imputation with an exact OLS (intercept) estimator on the
    current filled matrix: for each feature in `order`, fit on rows where it is observed using all other
    columns as predictors, predict its missing rows, update in place."""
    mask = np.isnan(X); Xt = np.where(mask, np.nanmean(X, 0), X).astype(object)
    Xt = [[F(v) for v in row] for row in Xt]
    for _ in range(n_rounds):
        for j in order:
            miss = [i for i in range(len(Xt)) if mask[i, j]]
            if not miss: continue
            obs = [i for i in range(len(Xt)) if not mask[i, j]]; others = [c for c in range(X.shape[1]) if c != j]
            b0, coef = ols_exact([[Xt[i][c] for c in others] for i in obs], [Xt[i][j] for i in obs])
            for i in miss:
                v = b0 + sum(coef[k] * Xt[i][c] for k, c in enumerate(others))
                if lo is not None and np.isfinite(lo[j]): v = max(v, F(lo[j]))
                if hi is not None and np.isfinite(hi[j]): v = min(v, F(hi[j]))
                Xt[i][j] = v
    return np.array([[float(v) for v in row] for row in Xt])
print(f"   missing counts per column: {np.isnan(Xit).sum(0).tolist()}")
for order, idx in (("roman", [0, 1, 2]), ("arabic", [2, 1, 0]), ("ascending", [2, 0, 1]), ("descending", [1, 0, 2])):
    ii1 = IterativeImputer(estimator=LinearRegression(), max_iter=1, imputation_order=order, tol=0).fit(Xit)
    seq = [t.feat_idx for t in ii1.imputation_sequence_]
    T1 = iterative_round_ref(Xit, idx)
    exp_seq = idx
    report(f"IterativeImputer(LinearRegression, max_iter=1, imputation_order='{order}'): visiting order {exp_seq} ({ {'roman': 'left to right', 'arabic': 'right to left', 'ascending': 'fewest missing first (counts 2,2,1; tie in stable order)', 'descending': 'most missing first (reverse of ascending)'}[order] }) and one round = exact OLS chained imputation (rel 1e-8)",
           seq == exp_seq and allclose(ii1.transform(Xit), T1, 1e-8), f"(sequence {seq}, max diff {np.max(np.abs(ii1.transform(Xit) - T1)):.1e})")
Xit2 = Xit.copy(); Xit2[0, 2] = NA; Xit2[1, 0] = NA  # missing counts: col0 3, col1 2, col2 2
iia = IterativeImputer(estimator=LinearRegression(), max_iter=1, imputation_order="ascending", tol=0).fit(Xit2); iid = IterativeImputer(estimator=LinearRegression(), max_iter=1, imputation_order="descending", tol=0).fit(Xit2)
report("IterativeImputer imputation_order 'ascending' = 'From features with fewest missing values to most' [1, 2, 0]; 'descending' = [0, 2, 1] (ties keep / reverse the stable order)", [t.feat_idx for t in iia.imputation_sequence_] == [1, 2, 0] and [t.feat_idx for t in iid.imputation_sequence_] == [0, 2, 1], f"({[t.feat_idx for t in iia.imputation_sequence_]}, {[t.feat_idx for t in iid.imputation_sequence_]})")
report("IterativeImputer(descending) one round = OLS chained imputation in the order [0, 2, 1] (rel 1e-8)", allclose(iid.transform(Xit2), iterative_round_ref(Xit2, [0, 2, 1]), 1e-8))
iir = IterativeImputer(estimator=LinearRegression(), max_iter=3, imputation_order="random", random_state=0, tol=0).fit(Xit)
seqr = [t.feat_idx for t in iir.imputation_sequence_]
report("IterativeImputer(imputation_order='random'): 'A random order for each round' -> each round is a permutation of the features; deterministic with random_state", all(sorted(seqr[3 * r:3 * r + 3]) == [0, 1, 2] for r in range(3)) and seqr == [t.feat_idx for t in IterativeImputer(estimator=LinearRegression(), max_iter=3, imputation_order="random", random_state=0, tol=0).fit(Xit).imputation_sequence_], f"({seqr})")
Xsk = Xit.copy(); Xsk[:, 1] = np.nan_to_num(Xsk[:, 1], nan=3.0)  # column 1 complete
iisk = IterativeImputer(estimator=LinearRegression(), max_iter=1, skip_complete=True, tol=0, imputation_order="roman").fit(Xsk); iins = IterativeImputer(estimator=LinearRegression(), max_iter=1, skip_complete=False, tol=0, imputation_order="roman").fit(Xsk)
report("IterativeImputer(skip_complete=True): complete feature 1 not in imputation_sequence_ (n_features_with_missing_ = 2); skip_complete=False fits it anyway; identical imputations", [t.feat_idx for t in iisk.imputation_sequence_] == [0, 2] and iisk.n_features_with_missing_ == 2 and [t.feat_idx for t in iins.imputation_sequence_] == [0, 1, 2] and allclose(iisk.transform(Xsk), iins.transform(Xsk), 1e-10))
Zsk_new = iisk.transform(np.array([[NA, NA, 4.0]]))
report("IterativeImputer(skip_complete=True).transform: a feature complete at fit but missing at transform 'will be imputed with the initial imputation method only' (mean of column 1)", close(Zsk_new[0, 1], np.mean(Xsk[:, 1]), 1e-12), f"({Zsk_new[0, 1]} vs mean {np.mean(Xsk[:, 1])})")
ii2 = IterativeImputer(estimator=LinearRegression(), max_iter=2, imputation_order="roman", tol=0).fit(Xit)
report("IterativeImputer(max_iter=2, tol=0): two rounds = two passes of the exact chained OLS (rel 1e-8), n_iter_ = 2", allclose(ii2.transform(Xit), iterative_round_ref(Xit, [0, 1, 2], 2), 1e-8) and ii2.n_iter_ == 2)
iic = IterativeImputer(estimator=LinearRegression(), max_iter=1, imputation_order="roman", tol=0, min_value=2.0, max_value=[np.inf, 4.0, 6.0]).fit(Xit)
Tc = iterative_round_ref(Xit, [0, 1, 2], 1, lo=[2.0, 2.0, 2.0], hi=[np.inf, 4.0, 6.0]); Tu = iterative_round_ref(Xit, [0, 1, 2], 1)
print(f"   clipping: unclipped imputed values {np.round(Tu[np.isnan(Xit)], 4).tolist()} -> clipped {np.round(Tc[np.isnan(Xit)], 4).tolist()}")
report("IterativeImputer(min_value=2, max_value=[inf, 4, 6]): imputed values clipped per feature inside the chain (exact chained OLS with clipping, rel 1e-8); clipping changes at least one value here", allclose(iic.transform(Xit), Tc, 1e-8) and not allclose(Tc, Tu))
# convergence: max|X_t - X_{t-1}| / max|X_known| < tol, checked against the per-round results
rounds = [IterativeImputer(estimator=LinearRegression(), max_iter=k, imputation_order="roman", tol=0).fit_transform(Xit) for k in range(1, 9)]
changes = [np.max(np.abs(rounds[k] - rounds[k - 1])) for k in range(1, len(rounds))]
scale_known = np.max(np.abs(Xit[~np.isnan(Xit)]))
for tol in (1e-1, 1e-2, 1e-3, 1e-4):
    iit = IterativeImputer(estimator=LinearRegression(), max_iter=8, imputation_order="roman", tol=tol).fit(Xit)
    exp_iter = next((k + 2 for k, c in enumerate(changes) if c / scale_known < tol), 8)
    report(f"IterativeImputer(tol={tol}): stops at the first round t with max|X_t - X_(t-1)|/max|X[known]| < tol (documented criterion) -> n_iter_ = {exp_iter}", iit.n_iter_ == exp_iter and allclose(iit.transform(Xit), rounds[exp_iter - 1], 1e-10), f"(n_iter_ {iit.n_iter_}; changes/scale {[f'{c / scale_known:.1e}' for c in changes[:exp_iter]]})")
_, ws = caught(lambda: IterativeImputer(estimator=LinearRegression(), max_iter=2, tol=1e-12).fit(Xit))
report("IterativeImputer that does not converge within max_iter warns (ConvergenceWarning)", any("ConvergenceWarning" in w.category.__name__ for w in ws))
iip1 = IterativeImputer(estimator=BayesianRidge(), sample_posterior=True, max_iter=3, random_state=0).fit(Xit); iip2 = IterativeImputer(estimator=BayesianRidge(), sample_posterior=True, max_iter=3, random_state=0).fit(Xit); iip3 = IterativeImputer(estimator=BayesianRidge(), sample_posterior=True, max_iter=3, random_state=1).fit(Xit)
report("IterativeImputer(sample_posterior=True): deterministic given random_state, different seeds differ, 'early stopping is only applied if sample_posterior=False' -> n_iter_ = max_iter", allclose(iip1.transform(Xit), iip2.transform(Xit)) and not allclose(iip1.transform(Xit), iip3.transform(Xit)) and iip1.n_iter_ == 3)
Xit1 = Xit[:, :1]
report("IterativeImputer with a single feature: initial imputation returned, n_iter_ = 0", allclose(IterativeImputer().fit_transform(Xit1), np.where(np.isnan(Xit1), np.nanmean(Xit1), Xit1)) and IterativeImputer().fit(Xit1).n_iter_ == 0)
iii = IterativeImputer(estimator=LinearRegression(), max_iter=1, tol=0, add_indicator=True).fit(Xit)
report("IterativeImputer(add_indicator=True): imputed columns then indicator columns", iii.transform(Xit).shape == (9, 6) and np.array_equal(iii.transform(Xit)[:, 3:], np.isnan(Xit).astype(float)))
if has_param(IterativeImputer, "keep_empty_features"):
    Xie = Xit.copy(); Xie[:, 1] = NA
    report("IterativeImputer with an all-missing feature: dropped by default, kept as 0 with keep_empty_features=True", IterativeImputer(max_iter=1).fit_transform(Xie).shape == (9, 2) and np.all(IterativeImputer(max_iter=1, keep_empty_features=True).fit_transform(Xie)[:, 1] == 0))
if has_param(IterativeImputer, "fill_value"):
    report("IterativeImputer(initial_strategy='constant', fill_value=-1, max_iter=0) fills with -1", np.all(IterativeImputer(initial_strategy="constant", fill_value=-1, max_iter=0).fit_transform(Xit)[np.isnan(Xit)] == -1))

# =============================================================================
print("== compose: ColumnTransformer / TransformedTargetRegressor")
Xct = np.array([[1.0, 10.0, 0.5, 100.0, 3.0], [2.0, 20.0, 1.5, 200.0, 1.0], [3.0, 30.0, 2.5, 300.0, 2.0], [4.0, 40.0, 3.5, 400.0, 5.0]])
ct = ColumnTransformer([("sc", StandardScaler(), [0, 1]), ("mm", MinMaxScaler(), [3])], remainder="drop").fit(Xct)
Tct = np.hstack([StandardScaler().fit_transform(Xct[:, [0, 1]]), MinMaxScaler().fit_transform(Xct[:, [3]])])
report("ColumnTransformer(remainder='drop'): output = [transformer 1 output | transformer 2 output] in transformers order ('The order of the columns ... follows the order of how the columns are specified'), unspecified columns dropped", allclose(ct.transform(Xct), Tct) and ct.transform(Xct).shape == (4, 3))
ctp = ColumnTransformer([("mm", MinMaxScaler(), [3]), ("sc", StandardScaler(), [0, 1])], remainder="passthrough").fit(Xct)
Tp = np.hstack([MinMaxScaler().fit_transform(Xct[:, [3]]), StandardScaler().fit_transform(Xct[:, [0, 1]]), Xct[:, [2, 4]]])
report("ColumnTransformer(remainder='passthrough'): remaining columns (2, 4) appended after the transformers, in their original order ('This subset of columns is concatenated with the output of the transformers')", allclose(ctp.transform(Xct), Tp))
cte = ColumnTransformer([("sc", StandardScaler(), [0])], remainder=MaxAbsScaler()).fit(Xct)
report("ColumnTransformer(remainder=estimator): remaining columns transformed by the remainder estimator, appended last", allclose(cte.transform(Xct), np.hstack([StandardScaler().fit_transform(Xct[:, [0]]), MaxAbsScaler().fit_transform(Xct[:, [1, 2, 3, 4]])])))
cts = ColumnTransformer([("sc", StandardScaler(), slice(0, 2)), ("mm", MinMaxScaler(), np.array([False, False, False, True, False])), ("f", FunctionTransformer(), lambda X: [4])]).fit(Xct)
report("ColumnTransformer column selection by slice / boolean mask / callable(X) -> same as index lists", allclose(cts.transform(Xct), np.hstack([Tct, Xct[:, [4]]])))
ctw = ColumnTransformer([("sc", StandardScaler(), [0, 1]), ("mm", MinMaxScaler(), [3])], transformer_weights={"sc": 2.0, "mm": 0.5}).fit(Xct)
report("ColumnTransformer(transformer_weights): 'The output of the transformer is multiplied by these weights'", allclose(ctw.transform(Xct), np.hstack([2.0 * Tct[:, :2], 0.5 * Tct[:, 2:]])))
report("ColumnTransformer.fit_transform = fit then transform", allclose(ColumnTransformer([("sc", StandardScaler(), [0, 1]), ("mm", MinMaxScaler(), [3])]).fit_transform(Xct), Tct))
report("ColumnTransformer.named_transformers_ holds the fitted transformers (StandardScaler mean_ of columns 0, 1)", allclose(ct.named_transformers_["sc"].mean_, Xct[:, [0, 1]].mean(0)))
names = ct.get_feature_names_out(["a", "b", "c", "d", "e"])
report("ColumnTransformer.get_feature_names_out(verbose_feature_names_out=True): 'sc__a', 'sc__b', 'mm__d'; passthrough remainder -> 'remainder__c', 'remainder__e'", names.tolist() == ["sc__a", "sc__b", "mm__d"] and ctp.get_feature_names_out(["a", "b", "c", "d", "e"]).tolist() == ["mm__d", "sc__a", "sc__b", "remainder__c", "remainder__e"], f"({ctp.get_feature_names_out(['a', 'b', 'c', 'd', 'e']).tolist()})")
ctn = ColumnTransformer([("sc", StandardScaler(), [0, 1]), ("mm", MinMaxScaler(), [3])], verbose_feature_names_out=False).fit(Xct)
report("ColumnTransformer(verbose_feature_names_out=False): plain input names", ctn.get_feature_names_out(["a", "b", "c", "d", "e"]).tolist() == ["a", "b", "d"])
try:
    ColumnTransformer([("s1", StandardScaler(), [0]), ("s2", MinMaxScaler(), [0])], verbose_feature_names_out=False).fit(Xct).get_feature_names_out(); report("ColumnTransformer(verbose_feature_names_out=False) with duplicate output names raises ValueError ('will error if feature names are not unique')", False)
except ValueError: report("ColumnTransformer(verbose_feature_names_out=False) with duplicate output names raises ValueError ('will error if feature names are not unique')", True)
if V >= (1, 6):
    ctf = ColumnTransformer([("sc", StandardScaler(), [0, 1])], verbose_feature_names_out="{feature_name}@{transformer_name}").fit(Xct)
    ctc = ColumnTransformer([("sc", StandardScaler(), [0, 1])], verbose_feature_names_out=lambda t, f: f"{f}-{t}".upper()).fit(Xct)
    report("ColumnTransformer(verbose_feature_names_out=str template / callable) formats names as documented", ctf.get_feature_names_out(["a", "b", "c", "d", "e"]).tolist() == ["a@sc", "b@sc"] and ctc.get_feature_names_out(["a", "b", "c", "d", "e"]).tolist() == ["A-SC", "B-SC"])
Xcat = np.array([["a", 1.0], ["b", 2.0], ["c", 3.0], ["a", 4.0], ["b", 5.0], ["c", 6.0], ["a", 7.0], ["d", 8.0]], dtype=object)
for thr, expect_sparse in ((0.3, False), (0.5, True), (0.0, False), (1.0, True)):
    ct_sp = ColumnTransformer([("oh", OHE(), [0]), ("id", FunctionTransformer(validate=True), [1])], sparse_threshold=thr).fit(Xcat)
    Z = ct_sp.transform(Xcat); density = (8 + 8) / (8 * 5)   # one-hot 8 nnz + identity 8 nnz of 8 x 5 -> 0.4
    report(f"ColumnTransformer(sparse_threshold={thr}): overall density 0.4 (nnz 16 / 40) {'<' if density < thr else '>='} threshold -> {'sparse' if expect_sparse else 'dense'} ('stacked as a sparse matrix if the overall density is lower than this value'; 0 -> always dense)", sp.issparse(Z) == expect_sparse and allclose(dense(Z)[:, :4], dense(OHE().fit_transform(Xcat[:, [0]]))), f"(sparse={sp.issparse(Z)})")
ct_all_dense = ColumnTransformer([("id", FunctionTransformer(validate=True), [1])], sparse_threshold=1.0).fit(Xcat)
report("ColumnTransformer with all-dense outputs stays dense whatever the threshold ('this keyword will be ignored')", not sp.issparse(ct_all_dense.transform(Xcat)))
mct = make_column_transformer((StandardScaler(), [0, 1]), (MinMaxScaler(), [3]))
report("make_column_transformer names transformers by lowercased class name ('standardscaler', 'minmaxscaler')", [n for n, _, _ in mct.transformers] == ["standardscaler", "minmaxscaler"] and allclose(mct.fit_transform(Xct), Tct))
try:
    ColumnTransformer([("sc", StandardScaler(), ["a"])]).fit(Xct); report("ColumnTransformer with string column names on a numpy array raises ValueError ('Specifying the columns using strings is only supported for dataframes')", False)
except ValueError: report("ColumnTransformer with string column names on a numpy array raises ValueError ('Specifying the columns using strings is only supported for dataframes')", True)
print("   (column selection by name / make_column_selector(dtype_include) / set_output('pandas') need pandas, not installed: skipped)")
ctd = ColumnTransformer([("sc", StandardScaler(), [0]), ("drop", "drop", [1]), ("pt", "passthrough", [4])]).fit(Xct)
report("ColumnTransformer with 'drop' and 'passthrough' as transformers: dropped column absent, passthrough column verbatim", allclose(ctd.transform(Xct), np.hstack([StandardScaler().fit_transform(Xct[:, [0]]), Xct[:, [4]]])))
# TransformedTargetRegressor
Xr = np.array([[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]]); yr = np.exp(0.5 * Xr.ravel() + 1.0) * np.array([1.0, 1.1, 0.9, 1.05, 0.95, 1.0])
ttr = TransformedTargetRegressor(regressor=LinearRegression(), func=np.log, inverse_func=np.exp).fit(Xr, yr)
b0, coef = ols_exact(Xr, np.log(yr))
report("TransformedTargetRegressor(func=log, inverse_func=exp): regressor_ fitted on func(y) (exact OLS on log y, rel 1e-12)", close(ttr.regressor_.intercept_, float(b0), 1e-12) and close(ttr.regressor_.coef_[0], float(coef[0]), 1e-12))
Xq_ = np.array([[1.5], [7.0], [-2.0]])
report("TransformedTargetRegressor.predict = inverse_func(regressor_.predict(X)) exactly (exp of the linear prediction), 1-d output", allclose(ttr.predict(Xq_), np.exp(ttr.regressor_.predict(Xq_)), 1e-15) and ttr.predict(Xq_).shape == (3,) and allclose(ttr.predict(Xq_), [math.exp(float(b0 + coef[0] * F(v))) for v in Xq_.ravel()], 1e-12))
ttr_t = TransformedTargetRegressor(regressor=LinearRegression(), transformer=StandardScaler()).fit(Xr, yr)
sc_y = StandardScaler().fit(yr[:, None]); b0s, coefs = ols_exact(Xr, sc_y.transform(yr[:, None]).ravel())
report("TransformedTargetRegressor(transformer=StandardScaler): regressor_ fitted on transformer.transform(y) (2-d internally), predict = transformer_.inverse_transform(regressor_.predict(X)) (rel 1e-12)",
       close(ttr_t.regressor_.coef_[0], float(coefs[0]), 1e-12) and allclose(ttr_t.predict(Xq_), sc_y.inverse_transform(ttr_t.regressor_.predict(Xq_)[:, None]).ravel(), 1e-12) and allclose(ttr_t.transformer_.mean_, [yr.mean()]))
report("TransformedTargetRegressor with a linear regressor and StandardScaler on y predicts exactly like plain LinearRegression (affine invariance)", allclose(ttr_t.predict(Xq_), LinearRegression().fit(Xr, yr).predict(Xq_), 1e-10))
_, ws = caught(lambda: TransformedTargetRegressor(regressor=LinearRegression(), func=np.log, inverse_func=np.sqrt).fit(Xr, yr), UserWarning)
report("TransformedTargetRegressor(check_inverse=True) with non-inverse func pair: UserWarning 'The provided functions or transformer are not strictly inverse of each other'", any("not strictly inverse" in str(w.message) for w in ws))
_, ws = caught(lambda: TransformedTargetRegressor(regressor=LinearRegression(), func=np.log, inverse_func=np.sqrt, check_inverse=False).fit(Xr, yr), UserWarning)
report("TransformedTargetRegressor(check_inverse=False): no warning", len(ws) == 0)
report("TransformedTargetRegressor default (no func/transformer): identity -> predictions equal LinearRegression", allclose(TransformedTargetRegressor().fit(Xr, yr).predict(Xq_), LinearRegression().fit(Xr, yr).predict(Xq_), 1e-12))
try:
    TransformedTargetRegressor(regressor=LinearRegression(), func=np.log).fit(Xr, yr); report("TransformedTargetRegressor(func without inverse_func) raises ValueError", False)
except ValueError: report("TransformedTargetRegressor(func without inverse_func) raises ValueError", True)
try:
    TransformedTargetRegressor(regressor=LinearRegression(), transformer=StandardScaler(), func=np.log, inverse_func=np.exp).fit(Xr, yr); report("TransformedTargetRegressor(transformer and func both set) raises ValueError", False)
except ValueError: report("TransformedTargetRegressor(transformer and func both set) raises ValueError", True)
report("TransformedTargetRegressor.score = r2 of the back-transformed predictions (r2_exact)", close(ttr.score(Xr, yr), float(r2_exact(yr, ttr.predict(Xr))), 1e-12))

# =============================================================================
print("== pipeline: Pipeline / FeatureUnion / make_pipeline / make_union")
Xpl = rs.normal(size=(40, 4)) * np.array([1, 5, 0.2, 10]); ypl = (Xpl[:, 0] + 0.3 * Xpl[:, 1] - Xpl[:, 2] > 0).astype(int); wpl = rs.uniform(0.5, 2, 40)
pipe = Pipeline([("sc", StandardScaler()), ("pca", PCA(n_components=2, svd_solver="full")), ("clf", LogisticRegression(C=0.7))]).fit(Xpl, ypl)
sc_m = StandardScaler().fit(Xpl); Z1 = sc_m.transform(Xpl); pca_m = PCA(n_components=2, svd_solver="full").fit(Z1); Z2 = pca_m.transform(Z1); clf_m = LogisticRegression(C=0.7).fit(Z2, ypl)
report("Pipeline.fit chains fit_transform: intermediate steps equal manual chaining (scaler mean_, PCA components_ up to sign, classifier coef_)", allclose(pipe["sc"].mean_, sc_m.mean_) and allclose(np.abs(pipe["pca"].components_), np.abs(pca_m.components_), 1e-9) and allclose(np.abs(pipe["clf"].coef_), np.abs(clf_m.coef_), 1e-8))
report("Pipeline[:-1].transform(X) = manual chained transform (PCA sign fixed by comparing |.|); pipe[:-1] is a Pipeline of the first steps", isinstance(pipe[:-1], Pipeline) and len(pipe[:-1].steps) == 2 and allclose(np.abs(pipe[:-1].transform(Xpl)), np.abs(Z2), 1e-9))
report("Pipeline.predict_proba / decision_function / predict = the final estimator applied to the transformed X (passthrough)", allclose(pipe.predict_proba(Xpl), pipe["clf"].predict_proba(pipe[:-1].transform(Xpl))) and allclose(pipe.decision_function(Xpl), pipe["clf"].decision_function(pipe[:-1].transform(Xpl))) and np.array_equal(pipe.predict(Xpl), pipe["clf"].predict(pipe[:-1].transform(Xpl))))
report("Pipeline steps slicing: pipe[0] is the StandardScaler, pipe[-1] the classifier, pipe['pca'] by name, pipe[1:] a Pipeline of pca+clf", isinstance(pipe[0], StandardScaler) and isinstance(pipe[-1], LogisticRegression) and isinstance(pipe["pca"], PCA) and [n for n, _ in pipe[1:].steps] == ["pca", "clf"])
report("Pipeline.score(X, y, sample_weight) = final_estimator.score(Xt, y, sample_weight) (weighted accuracy, exact)", close(pipe.score(Xpl, ypl, sample_weight=wpl), pipe["clf"].score(pipe[:-1].transform(Xpl), ypl, sample_weight=wpl), 1e-15) and close(pipe.score(Xpl, ypl, sample_weight=wpl), float(sum(F(w) for w, a, b in zip(wpl, ypl, pipe.predict(Xpl)) if a == b) / sum(F(w) for w in wpl)), 1e-12))
pp = Pipeline([("sc", "passthrough"), ("none", None), ("clf", LogisticRegression(C=0.7))]).fit(Xpl, ypl)
report("Pipeline with 'passthrough' and None steps: they are skipped (classifier fitted on the raw X)", allclose(pp["clf"].coef_, LogisticRegression(C=0.7).fit(Xpl, ypl).coef_) and allclose(pp.predict_proba(Xpl), LogisticRegression(C=0.7).fit(Xpl, ypl).predict_proba(Xpl)))
pipe2 = Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(C=0.7))]); pipe2.set_params(sc__with_mean=False, clf__C=3.0)
report("Pipeline.set_params with nested 'step__param' names reaches the step parameters", pipe2["sc"].with_mean is False and pipe2["clf"].C == 3.0 and pipe2.get_params()["clf__C"] == 3.0)
pipe2.set_params(sc=MinMaxScaler())
report("Pipeline.set_params(step=new_estimator) replaces the step", isinstance(pipe2["sc"], MinMaxScaler))
tmpdir = tempfile.mkdtemp(prefix="k13_cache_")
try:
    from joblib import Memory
    class CountingScaler(StandardScaler):
        calls = []
        def fit(self, X, y=None, sample_weight=None):
            CountingScaler.calls.append(1); return super().fit(X, y, sample_weight=sample_weight)
    mem = Memory(location=tmpdir, verbose=0)
    pm1 = Pipeline([("sc", CountingScaler()), ("clf", LogisticRegression(C=0.7))], memory=mem).fit(Xpl, ypl)
    n1 = len(CountingScaler.calls)
    pm2 = Pipeline([("sc", CountingScaler()), ("clf", LogisticRegression(C=0.7))], memory=mem).fit(Xpl, ypl)
    n2 = len(CountingScaler.calls)
    pnc = Pipeline([("sc", CountingScaler()), ("clf", LogisticRegression(C=0.7))]).fit(Xpl, ypl)
    report("Pipeline(memory=joblib.Memory): the second fit with identical data and params reuses the cached transformer (fit not called again) and gives identical results to the uncached pipeline", n1 == 1 and n2 == 1 and allclose(pm1.predict_proba(Xpl), pnc.predict_proba(Xpl), 1e-12) and allclose(pm2["sc"].mean_, pnc["sc"].mean_) and allclose(pm2["clf"].coef_, pnc["clf"].coef_, 1e-12), f"(fit calls after 1st/2nd cached fit: {n1}, {n2})")
    report("Pipeline(memory) with a string path also works", allclose(Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(C=0.7))], memory=tmpdir).fit(Xpl, ypl).predict_proba(Xpl), pnc.predict_proba(Xpl), 1e-12))
finally:
    shutil.rmtree(tmpdir, ignore_errors=True)
report("Pipeline.get_feature_names_out chains the steps' feature names (scaler one-to-one -> pca0, pca1)", pipe[:-1].get_feature_names_out(["a", "b", "c", "d"]).tolist() == ["pca0", "pca1"])
report("Pipeline.fit_transform on a transformer-only pipeline = chained fit_transform (exact)", allclose(np.abs(Pipeline([("sc", StandardScaler()), ("pca", PCA(2, svd_solver="full"))]).fit_transform(Xpl)), np.abs(Z2), 1e-9))
report("Pipeline.inverse_transform applies the steps' inverse_transform in reverse", allclose(Pipeline([("sc", StandardScaler()), ("mm", MinMaxScaler())]).fit(Xpl).inverse_transform(Pipeline([("sc", StandardScaler()), ("mm", MinMaxScaler())]).fit_transform(Xpl)), Xpl, 1e-10))
try:
    Pipeline([("clf", LogisticRegression()), ("sc", StandardScaler())]).fit(Xpl, ypl); report("Pipeline with a non-transformer intermediate step raises TypeError", False)
except TypeError: report("Pipeline with a non-transformer intermediate step raises TypeError", True)
mp = make_pipeline(StandardScaler(), StandardScaler(), PCA(2), LogisticRegression())
report("make_pipeline names steps by lowercased class name, duplicates suffixed -1, -2: ['standardscaler-1','standardscaler-2','pca','logisticregression']", [n for n, _ in mp.steps] == ["standardscaler-1", "standardscaler-2", "pca", "logisticregression"], f"({[n for n, _ in mp.steps]})")
# FeatureUnion
fu = FeatureUnion([("pca", PCA(n_components=2, svd_solver="full")), ("sc", StandardScaler()), ("poly", PolynomialFeatures(2, include_bias=False))]).fit(Xpl)
Zfu = fu.transform(Xpl)
Tfu = np.hstack([PCA(2, svd_solver="full").fit_transform(Xpl), StandardScaler().fit_transform(Xpl), PolynomialFeatures(2, include_bias=False).fit_transform(Xpl)])
report("FeatureUnion: outputs concatenated horizontally in transformer order (2 + 4 + 14 columns; PCA compared up to sign)", Zfu.shape == (40, 20) and allclose(np.abs(Zfu[:, :2]), np.abs(Tfu[:, :2]), 1e-9) and allclose(Zfu[:, 2:], Tfu[:, 2:], 1e-12))
fuw = FeatureUnion([("sc", StandardScaler()), ("mm", MinMaxScaler())], transformer_weights={"sc": 3.0, "mm": 0.25}).fit(Xpl)
report("FeatureUnion(transformer_weights): 'Multiplicative weights for features per transformer'", allclose(fuw.transform(Xpl), np.hstack([3.0 * StandardScaler().fit_transform(Xpl), 0.25 * MinMaxScaler().fit_transform(Xpl)]), 1e-12))
report("FeatureUnion.get_feature_names_out prefixes with the transformer name ('sc__x0', ...)", fu.get_feature_names_out().tolist()[:3] == ["pca__pca0", "pca__pca1", "sc__x0"], f"({fu.get_feature_names_out().tolist()[:3]})")
fud = FeatureUnion([("sc", StandardScaler()), ("drop", "drop"), ("pt", "passthrough")]).fit(Xpl)
report("FeatureUnion with 'drop' and 'passthrough' transformers: dropped one contributes nothing, passthrough gives X verbatim", allclose(fud.transform(Xpl), np.hstack([StandardScaler().fit_transform(Xpl), Xpl]), 1e-12))
mu = make_union(StandardScaler(), MinMaxScaler(), StandardScaler())
report("make_union names transformers by lowercased class name with -1/-2 suffixes for duplicates", [n for n, _ in mu.transformer_list] == ["standardscaler-1", "minmaxscaler", "standardscaler-2"], f"({[n for n, _ in mu.transformer_list]})")
fsp = FeatureUnion([("oh", OHE()), ("sc", FunctionTransformer(validate=True))]).fit(np.array([[1.0], [2.0], [1.0]]))
report("FeatureUnion with one sparse output returns a sparse matrix with dense blocks stacked", sp.issparse(fsp.transform(np.array([[1.0], [2.0]]))) and dense(fsp.transform(np.array([[1.0], [2.0]]))).tolist() == [[1, 0, 1], [0, 1, 2]])
report("FeatureUnion.fit_transform = fit + transform", allclose(FeatureUnion([("sc", StandardScaler()), ("mm", MinMaxScaler())]).fit_transform(Xpl), FeatureUnion([("sc", StandardScaler()), ("mm", MinMaxScaler())]).fit(Xpl).transform(Xpl)))
print("== done")
