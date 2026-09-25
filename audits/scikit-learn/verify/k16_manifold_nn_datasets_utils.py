#!/usr/bin/env python
"""manifold (MDS / smacof, Isomap, LocallyLinearEmbedding, SpectralEmbedding, TSNE, trustworthiness),
neural_network (MLPClassifier / MLPRegressor, BernoulliRBM), datasets (every make_* generator and the
bundled load_* datasets) and utils (extmath, class_weight, resample / shuffle, sparsefuncs, check_array,
type_of_target, graph shortest paths, murmurhash3_32, gen_even_slices / gen_batches, Bunch).

Every check is against an independent truth: plain-Python reference implementations written from the
documented algorithm (Dijkstra, brute-force kNN, SMACOF Guttman transform with a hand-written PAV isotonic
fit, classical MDS by numpy eigh, LLE barycentre weights from the documented regularised system, LTSA
alignment matrix, normalised graph Laplacian, t-SNE perplexity binary search / KL / gradient, MLP forward
pass and loss from the user-guide formulas, finite differences, RBM free energy by enumerating the hidden
states in mpmath, MurmurHash3_x86_32 in pure Python), closed forms (Fractions, mpmath chi2 quantiles and
truncated-Poisson means), and the documented examples of the docstrings."""
import sys, math, warnings, inspect, collections, zlib, heapq, itertools, pickle
sys.path.insert(0, ".")
from _synth import *
import mpmath
from mpmath import mp, mpf
mp.dps = 30
import scipy.sparse as sp
import sklearn
from sklearn import manifold
from sklearn.manifold import MDS, Isomap, LocallyLinearEmbedding, SpectralEmbedding, TSNE, smacof, trustworthiness
from sklearn.manifold import spectral_embedding
from sklearn.neural_network import MLPClassifier, MLPRegressor, BernoulliRBM
from sklearn import datasets
from sklearn.utils import extmath
from sklearn.utils.extmath import randomized_svd, weighted_mode, safe_sparse_dot, row_norms, density, cartesian, fast_logdet, softmax
from sklearn.utils.class_weight import compute_class_weight, compute_sample_weight
from sklearn.utils import resample, shuffle, gen_even_slices, gen_batches, Bunch, murmurhash3_32
from sklearn.utils.sparsefuncs import mean_variance_axis, incr_mean_variance_axis
from sklearn.utils.validation import check_array
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.graph import single_source_shortest_path_length
banner(); warnings.filterwarnings("ignore")
V = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
rs = np.random.RandomState(16)


def section(t):
    global rs
    print("== " + t); rs = np.random.RandomState(zlib.crc32(t.encode()) % 2 ** 31)


def has_param(obj, name):
    return name in inspect.signature(obj).parameters


def raises(fn, exc=Exception):
    try:
        fn()
    except exc as e:
        return type(e).__name__
    return None


def caught(fn, cat=Warning):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        out = fn()
    return out, [x for x in w if issubclass(x.category, cat)]


def maxrel(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    return float(np.max(np.abs(a - b)) / max(np.max(np.abs(b)), 1e-300))


def sign_align(A, B):
    """Flip the columns of A to match the sign of B (largest-|B| entry); returns the aligned copy."""
    A = np.array(A, float, copy=True)
    for j in range(A.shape[1]):
        k = int(np.argmax(np.abs(B[:, j])))
        if A[k, j] * B[k, j] < 0: A[:, j] = -A[:, j]
    return A


def pdist_py(X):
    n = len(X); return [[math.dist(X[i], X[j]) for j in range(n)] for i in range(n)]


def knn_py(D, k, include_self=False):
    """indices of the k nearest by distance matrix D (list of lists), ties broken by index."""
    out = []
    for i in range(len(D)):
        c = sorted((D[i][j], j) for j in range(len(D)) if include_self or j != i)
        out.append([j for _, j in c[:k]])
    return out


def dijkstra_py(adj, s):
    n = len(adj); dist = [math.inf] * n; dist[s] = 0.0; h = [(0.0, s)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist[u]: continue
        for v, w in adj[u].items():
            if d + w < dist[v]: dist[v] = d + w; heapq.heappush(h, (dist[v], v))
    return dist


def classical_mds(D, k):
    D = np.asarray(D, float); n = len(D); H = np.eye(n) - np.ones((n, n)) / n
    K = -0.5 * H @ (D ** 2) @ H; w, U = np.linalg.eigh(K); o = np.argsort(w)[::-1][:k]
    return U[:, o] * np.sqrt(w[o]), K, w


def pav(y):
    """Pool-adjacent-violators, non-decreasing least-squares fit (plain Python)."""
    blocks = []
    for v in y:
        blocks.append([v, 1])
        while len(blocks) > 1 and blocks[-2][0] > blocks[-1][0]:
            v2, n2 = blocks.pop(); v1, n1 = blocks.pop(); blocks.append([(v1 * n1 + v2 * n2) / (n1 + n2), n1 + n2])
    out = []
    for v, n in blocks: out += [v] * n
    return out


def guttman(X, Dhat):
    X = np.asarray(X, float); n = len(X); d = np.sqrt(((X[:, None] - X[None]) ** 2).sum(-1))
    d[d == 0] = 1e-5
    R = Dhat / d; np.fill_diagonal(R, 0.0); B = -R; B[np.diag_indices(n)] = R.sum(1)
    return B @ X / n


def edist(X):
    X = np.asarray(X, float); return np.sqrt(np.maximum(((X[:, None] - X[None]) ** 2).sum(-1), 0))


def upper(M):
    n = len(M); return np.array([M[i][j] for i in range(n) for j in range(i + 1, n)])


# =====================================================================================================
section("manifold: smacof / MDS")
n = 7
Z = rs.randn(n, 3)
Dm = edist(Z) + np.abs(rs.randn(n, n)) * 0.3; Dm = (Dm + Dm.T) / 2; np.fill_diagonal(Dm, 0)   # non-Euclidean, distinct values
X0 = rs.randn(n, 2)
sm_kw = dict(metric=True, n_components=2, n_init=1)
if has_param(smacof, "normalized_stress"): sm_kw["normalized_stress"] = False
# one Guttman step from a given init
X1, st1, it1 = smacof(Dm, init=X0.copy(), max_iter=1, return_n_iter=True, **sm_kw)
X1_ref = guttman(X0, Dm)
report("smacof(metric, max_iter=1): X = Guttman transform (1/n) B(X0) X0 of the init (documented step 3)", np.allclose(X1, X1_ref, rtol=1e-12, atol=1e-12), f"(max|diff| {np.max(np.abs(X1 - X1_ref)):.2e}, n_iter {it1})")
s_new = float(np.sum((upper(edist(X1)) - upper(Dm)) ** 2)); s_old = float(np.sum((upper(edist(X0)) - upper(Dm)) ** 2))
print(f"   raw stress of returned X {s_new:.10g}; of the init X0 {s_old:.10g}; returned stress {float(st1):.10g}")
report("smacof(metric, max_iter=1): returned stress = sum_{i<j} (d_ij(X) - delta_ij)^2 of the RETURNED X ('final value of the stress')", close(st1, s_new, rel=1e-10), f"(stress {float(st1):.10g} vs of returned X {s_new:.10g}; of the init {s_old:.10g})")
# converged metric run
Xc, stc, itc = smacof(Dm, init=X0.copy(), max_iter=300, eps=1e-9, return_n_iter=True, **sm_kw)
s_c = float(np.sum((upper(edist(Xc)) - upper(Dm)) ** 2))
report("smacof(metric, eps=1e-9): stress_ = raw stress of the returned embedding (converged run)", close(stc, s_c, rel=1e-6), f"(stress {float(stc):.10g} vs recomputed {s_c:.10g}, n_iter {itc})")
Xd, std_ = smacof(Dm, random_state=0, **{k: v for k, v in sm_kw.items()})
report("smacof(metric, default eps, random init): stress = raw stress of the returned X", close(std_, float(np.sum((upper(edist(Xd)) - upper(Dm)) ** 2)), rel=1e-6), f"(stress {float(std_):.8g} vs {float(np.sum((upper(edist(Xd)) - upper(Dm)) ** 2)):.8g})")
# Euclidean data -> near zero stress
Zp = rs.randn(8, 2); Dz = edist(Zp)
Xz, stz = smacof(Dz, init=Zp + 0.05 * rs.randn(8, 2), max_iter=3000, eps=1e-12, **sm_kw)
report("smacof on exactly 2-D-embeddable dissimilarities from a nearby init: stress -> 0 (distances reproduced)", float(stz) < 1e-8 * float(np.sum(upper(Dz) ** 2)) and np.allclose(edist(Xz), Dz, atol=1e-4), f"(stress {float(stz):.2e}, max|d-delta| {np.max(np.abs(edist(Xz) - Dz)):.2e})")
# normalized stress (Stress-1) with metric MDS
if V >= (1, 7):
    Xn, stn = smacof(Dm, init=X0.copy(), max_iter=300, eps=1e-9, metric=True, n_components=2, n_init=1, normalized_stress=True)
    dd = upper(edist(Xn)); s1 = math.sqrt(float(np.sum((dd - upper(Dm)) ** 2)) / float(np.sum(dd ** 2)))
    report("smacof(metric, normalized_stress=True) [1.7+: 'supported for metric MDS']: Stress-1 = sqrt(sum (d-delta)^2 / sum d^2)", close(stn, s1, rel=1e-6), f"({float(stn):.10g} vs {s1:.10g})")
elif V >= (1, 2):
    e = raises(lambda: smacof(Dm, metric=True, normalized_stress=True, n_init=1))
    report("smacof(metric=True, normalized_stress=True) [1.2-1.6: 'Only supported in non-metric MDS'] raises ValueError", e == "ValueError", f"({e})")
if V >= (1, 2):
    import sklearn.manifold._mds as _m
    dflt = inspect.signature(smacof).parameters["normalized_stress"].default
    print(f"   smacof normalized_stress default {dflt!r}")
    report("smacof normalized_stress default: 'auto' from 1.4 ('The default value changed from False to \"auto\" in version 1.4'), False-equivalent before", (dflt == "auto") if V >= (1, 4) else (dflt in (False, "warn")), f"({dflt!r})")

# non-metric: the monotone-regression step, replicated with a hand-written PAV
def nm_ref(D, X0, iters, first_raw):
    n = len(D); iu = np.triu_indices(n, 1); order = np.argsort(D[iu], kind="stable"); X = np.asarray(X0, float)
    for it in range(iters):
        d = edist(X)[iu]
        if first_raw and it == 0:
            dh = D[iu].astype(float)
        else:
            fit = pav(list(d[order])); dh = np.empty_like(d); dh[order] = fit
        dh = dh * math.sqrt((n * (n - 1) / 2) / float(np.sum(dh ** 2)))
        Dh = np.zeros((n, n)); Dh[iu] = dh; Dh = Dh + Dh.T
        X = guttman(X, Dh)
    dnew = edist(X)[iu]; raw = float(np.sum((dnew - dh) ** 2))
    return X, raw, math.sqrt(raw / float(np.sum(dnew ** 2)))

first_raw = V >= (1, 7)
k_it = 2 if first_raw else 1
nm_kw = dict(metric=False, n_components=2, n_init=1)
Xnm, stnm = smacof(Dm, init=X0.copy(), max_iter=k_it, **nm_kw)
Xr, rawr, s1r = nm_ref(Dm, X0, k_it, first_raw)
report(f"smacof(metric=False, max_iter={k_it}): X = Guttman transform against disparities = isotonic (PAV) fit of d(X) on the delta order, symmetric, normalised to sum_(i<j) dhat^2 = n(n-1)/2" + (" (1.7+: first iteration uses the scaled deltas)" if first_raw else ""),
       np.allclose(Xnm, Xr, rtol=1e-9, atol=1e-10), f"(max|diff| {np.max(np.abs(Xnm - Xr)):.3e})")
if V >= (1, 7):
    report(f"smacof(metric=False, max_iter={k_it}) default normalized_stress='auto' -> Stress-1 = sqrt(sum (d - dhat)^2 / sum d^2) of the returned X against its disparities (user-guide formula)", close(stnm, s1r, rel=1e-8), f"({float(stnm):.10g} vs {s1r:.10g}; raw {rawr:.6g})")
if V >= (1, 2):
    _, st_one = smacof(Dm, init=X0.copy(), max_iter=1, metric=False, n_components=2, n_init=1, normalized_stress=True)
    report("smacof(metric=False, normalized_stress=True, max_iter=1): Stress-1 lies in [0, 1] ('0 perfect ... 0.2 poor'; Kruskal's ratio cannot exceed 1)", 0 <= float(st_one) <= 1, f"({float(st_one):.6g})")
# converged non-metric: Stress-1 vs Kruskal's definition (optimal monotone disparities of the returned configuration)
nmk = dict(nm_kw);
if V >= (1, 2): nmk["normalized_stress"] = True
Xnc, stnc = smacof(Dm, init=X0.copy(), max_iter=3000, eps=1e-12, **nmk)
iu = np.triu_indices(n, 1); order = np.argsort(Dm[iu]); dnc = edist(Xnc)[iu]
fit = np.empty_like(dnc); fit[order] = pav(list(dnc[order]))
kr = math.sqrt(float(np.sum((dnc - fit) ** 2)) / float(np.sum(dnc ** 2)))
print(f"   converged non-metric: stress_ {float(stnc):.6g}; Kruskal Stress-1 of the returned X (optimal PAV disparities) {kr:.6g}")
if V >= (1, 2):
    report("smacof(metric=False, normalized_stress=True, converged): value = Kruskal Stress-1 of the returned configuration (to 1e-3 abs)", abs(float(stnc) - kr) < 1e-3, f"({float(stnc):.6g} vs {kr:.6g})")
# rank invariance of non-metric MDS (converged, same init)
Xm3, st3 = smacof(Dm ** 3, init=X0.copy(), max_iter=3000, eps=1e-12, **nmk)
def procrustes_err(A, B):
    A = A - A.mean(0); B = B - B.mean(0); A = A / np.linalg.norm(A); B = B / np.linalg.norm(B)
    U, s, Vt = np.linalg.svd(A.T @ B); return 1 - s.sum() ** 2
pe = procrustes_err(Xnc, Xm3)
d3 = edist(Xm3)[iu]; f3 = np.empty_like(d3); f3[order] = pav(list(d3[order]))
kr3 = math.sqrt(float(np.sum((d3 - f3) ** 2)) / float(np.sum(d3 ** 2)))
print(f"   Kruskal Stress-1 (w.r.t. the delta order) of the delta run {kr:.6g}, of the delta^3 run {kr3:.6g}")
report("non-metric smacof depends only on the rank order of the dissimilarities: delta and delta^3 give the same configuration up to similarity (converged, same init)", pe < 1e-6, f"(Procrustes residual {pe:.2e}; stresses {float(stnc):.6g} / {float(st3):.6g}; Kruskal Stress-1 of both configurations for the same ordering {kr:.4g} / {kr3:.4g})")

# MDS estimator
def mds_est(metric_mds=True, precomputed=False, **kw):
    if V >= (1, 8):
        return MDS(metric_mds=metric_mds, metric="precomputed" if precomputed else "euclidean", init="random", **kw)
    return MDS(metric=metric_mds, dissimilarity="precomputed" if precomputed else "euclidean", **kw)

nsk = {"normalized_stress": False} if V >= (1, 2) else {}
m = mds_est(True, True, n_init=1, max_iter=300, eps=1e-9, **nsk).fit(Dm, init=X0.copy())
Xs2, sts2 = smacof(Dm, init=X0.copy(), max_iter=300, eps=1e-9, **sm_kw)
report("MDS(precomputed).fit(D, init=...) = smacof(D, init=...) (documented: MDS runs SMACOF): same embedding_ and stress_", np.allclose(m.embedding_, Xs2) and close(m.stress_, sts2), f"(max|diff| {np.max(np.abs(m.embedding_ - Xs2)):.1e})")
report("MDS(precomputed): dissimilarity_matrix_ is the input matrix", np.array_equal(m.dissimilarity_matrix_, Dm))
report("MDS(metric).stress_ = sum_{i<j} (d_ij(embedding_) - delta_ij)^2", close(m.stress_, float(np.sum((upper(edist(m.embedding_)) - upper(Dm)) ** 2)), rel=1e-6))
Xe = rs.randn(9, 4)
me = mds_est(True, False, n_init=1, random_state=0, **nsk).fit(Xe)
report("MDS(euclidean): dissimilarity_matrix_ = pairwise Euclidean distances of X (plain Python)", np.allclose(me.dissimilarity_matrix_, pdist_py(Xe.tolist()), rtol=1e-12, atol=1e-12))
report("MDS: embedding_ shape (n_samples, n_components); fit_transform returns embedding_", me.embedding_.shape == (9, 2) and np.allclose(mds_est(True, False, n_init=1, random_state=0, **nsk).fit_transform(Xe), me.embedding_))
e = raises(lambda: mds_est(True, True, n_init=1).fit(Dm + np.triu(np.ones((n, n)), 1)))
report("MDS(precomputed) with a non-symmetric matrix raises ValueError ('Must be symmetric')", e == "ValueError", f"({e})")
if V >= (1, 4):
    mn = mds_est(False, True, n_init=1, max_iter=300).fit(Dm, init=X0.copy())
    mnT = mds_est(False, True, n_init=1, max_iter=300, normalized_stress=True).fit(Dm, init=X0.copy())
    report("MDS(non-metric), default normalized_stress='auto' [1.4+] = normalized_stress=True ('non-metric MDS returns normalized stress')", close(mn.stress_, mnT.stress_, rel=1e-12), f"({mn.stress_:.8g} vs {mnT.stress_:.8g})")
    mm = mds_est(True, True, n_init=1, max_iter=300).fit(Dm, init=X0.copy())
    mmF = mds_est(True, True, n_init=1, max_iter=300, normalized_stress=False).fit(Dm, init=X0.copy())
    report("MDS(metric), default normalized_stress='auto' [1.4+] = normalized_stress=False ('metric MDS returns raw stress')", close(mm.stress_, mmF.stress_, rel=1e-12), f"({mm.stress_:.8g} vs {mmF.stress_:.8g})")
mni = mds_est(True, True, n_init=3, random_state=1, max_iter=50, **nsk)
mni.fit(Dm)
ss = []
rsx = np.random.RandomState(1)
print(f"   MDS(n_init=3) stress_ {mni.stress_:.6g}, n_iter_ {mni.n_iter_}")
report("MDS: n_iter_ is a positive int <= max_iter", 1 <= mni.n_iter_ <= 50)
if hasattr(manifold, "ClassicalMDS"):
    cm = manifold.ClassicalMDS(n_components=2, metric="precomputed").fit(Dm)
    Ycl, _, _ = classical_mds(Dm, 2)
    report("ClassicalMDS [1.8+] (precomputed) = top eigenvectors of -1/2 H D^2 H scaled by sqrt(eigenvalue), up to sign", np.allclose(sign_align(cm.embedding_, Ycl), Ycl, rtol=1e-8, atol=1e-10), f"(max rel {maxrel(sign_align(cm.embedding_, Ycl), Ycl):.1e})")

# =====================================================================================================
section("manifold: Isomap")
t = np.sort(rs.uniform(0, 3 * np.pi, 45)); h = rs.uniform(0, 3, 45)
Xi = np.c_[t * np.cos(t) / 3, h, t * np.sin(t) / 3] + 0.01 * rs.randn(45, 3)
Dx = pdist_py(Xi.tolist()); k = 7
nb = knn_py(Dx, k)
adj = [dict() for _ in range(45)]
for i in range(45):
    for j in nb[i]: adj[i][j] = Dx[i][j]; adj[j][i] = Dx[i][j]
G = np.array([dijkstra_py(adj, s) for s in range(45)])
print(f"   graph connected: {np.isfinite(G).all()}")
iso = Isomap(n_neighbors=k, n_components=2, eigen_solver="dense").fit(Xi)
report("Isomap.dist_matrix_ = geodesic distances: Dijkstra (plain Python) on the symmetrised kNN graph with Euclidean edge weights", np.allclose(iso.dist_matrix_, G, rtol=1e-10, atol=1e-10), f"(max|diff| {np.max(np.abs(iso.dist_matrix_ - G)):.1e})")
Ycm, Kc, wK = classical_mds(G, 2)
report("Isomap.embedding_ = classical MDS of the geodesic distances (top eigvecs of -1/2 H D^2 H scaled by sqrt(eigenvalue)), up to column sign", np.allclose(sign_align(iso.embedding_, Ycm), Ycm, rtol=1e-7, atol=1e-8), f"(max rel {maxrel(sign_align(iso.embedding_, Ycm), Ycm):.1e})")
Yf = iso.embedding_
re_doc = np.linalg.norm(Kc - Yf @ Yf.T) / 45
report("Isomap.reconstruction_error() = ||K(D) - K(D_fit)||_F / n_samples with K(D) = -1/2 (I-1/n) D^2 (I-1/n) (docstring Notes)", close(iso.reconstruction_error(), re_doc, rel=1e-7), f"({iso.reconstruction_error():.10g} vs {re_doc:.10g})")
Kfit = -0.5 * (np.eye(45) - 1 / 45) @ edist(Yf) ** 2 @ (np.eye(45) - 1 / 45)
report("   ... with K(D_fit) computed literally from the embedding's own distance matrix", close(iso.reconstruction_error(), np.linalg.norm(Kc - Kfit) / 45, rel=1e-7))
report("Isomap.transform(training X) reproduces embedding_ (geodesic rows through the point itself)", np.allclose(iso.transform(Xi), iso.embedding_, rtol=1e-7, atol=1e-8), f"(max|diff| {np.max(np.abs(iso.transform(Xi) - iso.embedding_)):.1e})")
xq = Xi[:3] + 0.02
dq = [[math.dist(xq[a], Xi[b]) for b in range(45)] for a in range(3)]
Gq = []
for a in range(3):
    nn = sorted(range(45), key=lambda b: dq[a][b])[:k]
    Gq.append([min(dq[a][b] + G[b][j] for b in nn) for j in range(45)])
Gq = np.array(Gq); H = np.eye(45) - 1 / 45
Kq = -0.5 * Gq ** 2; Kq_c = Kq - Kq.mean(1, keepdims=True) - (-0.5 * G ** 2).mean(0) + (-0.5 * G ** 2).mean()
w_, U_ = np.linalg.eigh(Kc); o = np.argsort(w_)[::-1][:2]
Yq = Kq_c @ U_[:, o] / np.sqrt(w_[o])
report("Isomap.transform(new X): geodesic = min over the k nearest training points of (edge + dist_matrix_ row), then the kernel-PCA projection of -1/2 G^2", np.allclose(sign_align(iso.transform(xq), Yq), Yq, rtol=1e-6, atol=1e-8), f"(max rel {maxrel(sign_align(iso.transform(xq), Yq), Yq):.1e})")
isoFW = Isomap(n_neighbors=k, n_components=2, path_method="FW", eigen_solver="dense").fit(Xi)
isoD = Isomap(n_neighbors=k, n_components=2, path_method="D", eigen_solver="dense").fit(Xi)
report("Isomap path_method 'FW' and 'D' give the same geodesic matrix (both exact shortest paths)", np.allclose(isoFW.dist_matrix_, isoD.dist_matrix_, rtol=1e-12, atol=1e-12))
rad = 1.2
adjr = [dict() for _ in range(45)]
for i in range(45):
    for j in range(45):
        if i != j and Dx[i][j] <= rad: adjr[i][j] = Dx[i][j]
Gr = np.array([dijkstra_py(adjr, s) for s in range(45)])
if np.isfinite(Gr).all():
    isor = Isomap(n_neighbors=None, radius=rad, n_components=2, eigen_solver="dense").fit(Xi)
    report("Isomap(radius=r, n_neighbors=None): geodesics on the radius graph (edges with d <= r) = plain-Python Dijkstra", np.allclose(isor.dist_matrix_, Gr, rtol=1e-10, atol=1e-10), f"(max|diff| {np.max(np.abs(isor.dist_matrix_ - Gr)):.1e})")
else:
    print("   radius graph not connected; radius check skipped")
e = raises(lambda: Isomap(n_neighbors=5, radius=1.0).fit(Xi))
report("Isomap(n_neighbors=5, radius=1.0): both set raises ValueError ('Both n_neighbors and radius are provided')", e == "ValueError", f"({e})")
report("Isomap: embedding_ shape (n, n_components); kernel_pca_ eigenvalues descending", iso.embedding_.shape == (45, 2) and iso.kernel_pca_.eigenvalues_[0] >= iso.kernel_pca_.eigenvalues_[1])

# =====================================================================================================
section("manifold: LocallyLinearEmbedding")
tt = rs.uniform(0, 2.5 * np.pi, 40); hh = rs.uniform(0, 2, 40)
Xl = np.c_[np.cos(tt), hh, np.sin(tt)] + 0.02 * rs.randn(40, 3)
kL = 6; reg = 1e-3
Dl = pdist_py(Xl.tolist()); nbl = knn_py(Dl, kL)
W = np.zeros((40, 40))
for i in range(40):
    Cz = Xl[nbl[i]] - Xl[i]; Cg = Cz @ Cz.T; tr = np.trace(Cg)
    Cg = Cg + (reg * tr if tr > 0 else reg) * np.eye(kL)
    w = np.linalg.solve(Cg, np.ones(kL)); W[i, nbl[i]] = w / w.sum()
M = (np.eye(40) - W).T @ (np.eye(40) - W)
wM, UM = np.linalg.eigh(M)
Yl_ref = UM[:, 1:3]
lle = LocallyLinearEmbedding(n_neighbors=kL, n_components=2, reg=reg, eigen_solver="dense").fit(Xl)
from sklearn.manifold import _locally_linear as _ll
Wsk = _ll.barycenter_kneighbors_graph(Xl, kL, reg=reg)
Wsk = Wsk.toarray() if hasattr(Wsk, "toarray") else np.asarray(Wsk)
report("LLE(standard) reconstruction weights = solution of the documented regularised local system (C + reg*trace(C) I) w = 1, w/sum(w) ('reg multiplies the trace of the local covariance')", np.allclose(Wsk, W, rtol=1e-9, atol=1e-12), f"(max|diff| {np.max(np.abs(Wsk - W)):.1e})")
report("LLE(standard) weights: each row sums to 1 and is supported on the k nearest neighbours only", np.allclose(Wsk.sum(1), 1) and all(set(np.nonzero(Wsk[i])[0]) <= set(nbl[i]) for i in range(40)))
report("LLE(standard).embedding_ = eigenvectors 2..n_components+1 of (I-W)^T(I-W) (bottom, constant one skipped), up to sign", np.allclose(sign_align(lle.embedding_, Yl_ref), Yl_ref, rtol=1e-6, atol=1e-8), f"(max rel {maxrel(sign_align(lle.embedding_, Yl_ref), Yl_ref):.1e})")
report("LLE(standard).reconstruction_error_ = sum of those two eigenvalues", close(lle.reconstruction_error_, wM[1] + wM[2], rel=1e-6, abs_=1e-14), f"({lle.reconstruction_error_:.6e} vs {wM[1] + wM[2]:.6e}; smallest eigenvalue {wM[0]:.1e})")
Ea = LocallyLinearEmbedding(n_neighbors=kL, n_components=2, eigen_solver="arpack", random_state=0).fit(Xl)
sub = np.linalg.norm(Ea.embedding_ @ np.linalg.pinv(Ea.embedding_) - Yl_ref @ Yl_ref.T)
print(f"   arpack: reconstruction_error_ {Ea.reconstruction_error_:.6e} (dense {lle.reconstruction_error_:.6e}); column sums {np.round(Ea.embedding_.sum(0), 4).tolist()}")
report("LLE(standard, eigen_solver='arpack') spans the same 2-D subspace as the dense solution (projector distance < 0.05)", sub < 0.05, f"(||P_arpack - P_dense|| {sub:.3g})")
report("LLE(standard, eigen_solver='arpack'): the trivial constant eigenvector is excluded (columns orthogonal to 1)", np.allclose(Ea.embedding_.sum(0), 0, atol=1e-6), f"(column sums {np.round(Ea.embedding_.sum(0), 4).tolist()})")
# LTSA reference
M2 = np.zeros((40, 40))
for i in range(40):
    Xn = Xl[nbl[i]] - Xl[nbl[i]].mean(0)
    Uu = np.linalg.svd(Xn, full_matrices=True)[0][:, :2]
    Gi = np.c_[np.ones(kL) / math.sqrt(kL), Uu]
    idx = np.ix_(nbl[i], nbl[i]); M2[idx] += np.eye(kL) - Gi @ Gi.T
w2, U2 = np.linalg.eigh(M2)
ltsa = LocallyLinearEmbedding(n_neighbors=kL, n_components=2, method="ltsa", eigen_solver="dense").fit(Xl)
report("LLE(method='ltsa'): embedding = eigenvectors 2..3 of the LTSA alignment matrix sum_i S_i (I - G_i G_i^T) S_i^T (G_i = [1/sqrt(k), top local PCs]), up to sign", np.allclose(sign_align(ltsa.embedding_, U2[:, 1:3]), U2[:, 1:3], rtol=1e-6, atol=1e-7), f"(max rel {maxrel(sign_align(ltsa.embedding_, U2[:, 1:3]), U2[:, 1:3]):.1e})")
report("LLE(method='ltsa').reconstruction_error_ = sum of those eigenvalues", close(ltsa.reconstruction_error_, w2[1] + w2[2], rel=1e-6, abs_=1e-14))
for meth, kk in [("hessian", 6), ("modified", 6)]:
    em = LocallyLinearEmbedding(n_neighbors=kk, n_components=2, method=meth, eigen_solver="dense").fit(Xl).embedding_
    ok = em.shape == (40, 2) and np.isfinite(em).all() and np.allclose(em.T @ em, np.eye(2), atol=1e-8) and np.allclose(em.sum(0), 0, atol=1e-7)
    report(f"LLE(method='{meth}', n_neighbors={kk}): runs; columns orthonormal and orthogonal to the constant vector (null-space eigenvectors)", ok, f"(E^T E {np.round(em.T @ em, 8).tolist()}, col sums {np.round(em.sum(0), 9).tolist()})")
for nc in (1, 2, 3):
    bound = nc * (1 + (nc + 1) / 2)      # docstring: n_neighbors > n_components * (1 + (n_components + 1) / 2
    kbad = int(math.floor(bound)) if bound == int(bound) else int(math.floor(bound))
    kgood = kbad + 1
    Xh = np.c_[Xl, rs.randn(40, 1) * 0.1]
    e_bad = raises(lambda: LocallyLinearEmbedding(n_neighbors=kbad, n_components=nc, method="hessian", eigen_solver="dense").fit(Xh))
    e_good = raises(lambda: LocallyLinearEmbedding(n_neighbors=kgood, n_components=nc, method="hessian", eigen_solver="dense").fit(Xh))
    report(f"LLE(hessian, n_components={nc}): documented 'n_neighbors > n_components*(1+(n_components+1)/2)' = {bound:g}: n_neighbors={kbad} raises, {kgood} runs", e_bad == "ValueError" and e_good is None, f"({e_bad}, {e_good})")
e = raises(lambda: LocallyLinearEmbedding(n_neighbors=1, n_components=2, method="modified", eigen_solver="dense").fit(Xl))
report("LLE(modified) with n_neighbors < n_components raises ValueError", e == "ValueError", f"({e})")
e = raises(lambda: LocallyLinearEmbedding(n_neighbors=40, n_components=2).fit(Xl))
report("LLE with n_neighbors >= n_samples raises ValueError", e == "ValueError", f"({e})")
e = raises(lambda: LocallyLinearEmbedding(n_neighbors=5, n_components=4).fit(Xl))
report("LLE with n_components > n_features raises ValueError ('output dimension must be less than or equal to input dimension')", e == "ValueError", f"({e})")
xq = Xl[:4] + 0.03
dq = [[math.dist(xq[a], Xl[b]) for b in range(40)] for a in range(4)]
Tq = []
for a in range(4):
    nn = sorted(range(40), key=lambda b: dq[a][b])[:kL]
    Cz = Xl[nn] - xq[a]; Cg = Cz @ Cz.T; Cg += reg * np.trace(Cg) * np.eye(kL); w = np.linalg.solve(Cg, np.ones(kL)); w /= w.sum()
    Tq.append(w @ lle.embedding_[nn])
report("LLE.transform(new X) = barycentre weights on the k training neighbours (same regularised system) applied to embedding_", np.allclose(lle.transform(xq), np.array(Tq), rtol=1e-8, atol=1e-10), f"(max|diff| {np.max(np.abs(lle.transform(xq) - np.array(Tq))):.1e})")

# =====================================================================================================
section("manifold: SpectralEmbedding / spectral_embedding")
Xs = np.r_[rs.randn(15, 3), rs.randn(15, 3) + 2.5]
nfe = Xs.shape[1]
A = np.exp(-(1.0 / nfe) * edist(Xs) ** 2)
def lap_embed(A, k, drop_first=True):
    A0 = A.copy(); np.fill_diagonal(A0, 0); d = A0.sum(1); Dh = 1 / np.sqrt(d)
    L = np.eye(len(A)) - Dh[:, None] * A0 * Dh[None]
    w, U = np.linalg.eigh(L); E = U / np.sqrt(d)[:, None]
    return (E[:, 1:k + 1] if drop_first else E[:, :k]), w
Eref, wL = lap_embed(A, 2)
se = SpectralEmbedding(n_components=2, affinity="rbf", random_state=0).fit(Xs)
report("SpectralEmbedding(affinity='rbf', gamma=None): affinity_matrix_ = exp(-gamma ||x-y||^2) with gamma = 1/n_features", np.allclose(se.affinity_matrix_, A, rtol=1e-12, atol=1e-14))
if hasattr(se, "gamma_"):
    report("SpectralEmbedding: gamma_ = 1/n_features when gamma=None", close(se.gamma_, 1 / nfe))
report("SpectralEmbedding.embedding_ = eigenvectors 2..k+1 of the normalised Laplacian I - D^-1/2 A D^-1/2 (self-loops ignored) divided by sqrt(degree), up to sign", np.allclose(sign_align(se.embedding_, Eref), Eref, rtol=1e-6, atol=1e-8), f"(max rel {maxrel(sign_align(se.embedding_, Eref), Eref):.1e}; eigenvalues {np.round(wL[:3], 6).tolist()})")
sep = SpectralEmbedding(n_components=2, affinity="precomputed", random_state=0).fit(A)
report("SpectralEmbedding(affinity='precomputed') on the same rbf matrix gives the same embedding", np.allclose(np.abs(sep.embedding_), np.abs(se.embedding_), rtol=1e-7, atol=1e-9))
full = spectral_embedding(A, n_components=3, drop_first=False, random_state=0)
report("spectral_embedding(drop_first=False): first column is the constant vector (trivial eigenvector / sqrt(degree))", np.allclose(full[:, 0], full[0, 0], rtol=1e-7) and abs(full[0, 0]) > 0, f"(spread {np.ptp(full[:, 0]):.1e})")
report("spectral_embedding(drop_first=True) = drop_first=False without its first column", np.allclose(np.abs(spectral_embedding(A, n_components=2, drop_first=True, random_state=0)), np.abs(full[:, 1:3]), rtol=1e-7, atol=1e-9))
Eu, _ = lap_embed(A, 2, drop_first=True)
A0 = A.copy(); np.fill_diagonal(A0, 0); Lu = np.diag(A0.sum(1)) - A0
wu, Uu = np.linalg.eigh(Lu)
seu = spectral_embedding(A, n_components=2, norm_laplacian=False, random_state=0)
report("spectral_embedding(norm_laplacian=False): eigenvectors 2..k+1 of the unnormalised Laplacian D - A, up to sign", np.allclose(sign_align(seu, Uu[:, 1:3]), Uu[:, 1:3], rtol=1e-6, atol=1e-8))
kk = max(int(30 / 10), 1)
Dsp = pdist_py(Xs.tolist()); nbs = knn_py(Dsp, kk, include_self=True)
Ann = np.zeros((30, 30))
for i in range(30):
    for j in nbs[i]: Ann[i, j] = 1
Ann = 0.5 * (Ann + Ann.T)
senn = SpectralEmbedding(n_components=2, random_state=0).fit(Xs)
Amat = senn.affinity_matrix_.toarray() if hasattr(senn.affinity_matrix_, "toarray") else senn.affinity_matrix_
report("SpectralEmbedding(affinity='nearest_neighbors', n_neighbors=None): n_neighbors = max(n_samples/10, 1), connectivity graph incl. self, symmetrised 0.5(A + A^T)", np.array_equal(Amat, Ann) and getattr(senn, "n_neighbors_", kk) == kk, f"(n_neighbors_ {getattr(senn, 'n_neighbors_', None)})")
report("SpectralEmbedding: embedding_ shape (n_samples, n_components); fit_transform = embedding_", senn.embedding_.shape == (30, 2) and np.allclose(np.abs(SpectralEmbedding(n_components=2, random_state=0).fit_transform(Xs)), np.abs(senn.embedding_)))

# =====================================================================================================
section("manifold: TSNE")
from sklearn.manifold import _t_sne, _utils as _tu
Xt = np.r_[rs.randn(14, 4), rs.randn(13, 4) + 3.0, rs.randn(13, 4) - 3.0]
nT = len(Xt); perp = 8.0
D2 = edist(Xt) ** 2


def cond_row_py(d2, perp, tol=1e-5, steps=100):
    """p_{j|i} = exp(-beta d_ij^2)/sum; binary search on beta until entropy = log(perplexity) (nats)."""
    target = math.log(perp); beta = 1.0; lo, hi = -math.inf, math.inf
    for _ in range(steps):
        w = [math.exp(-x * beta) for x in d2]; s = sum(w); p = [x / s for x in w]
        Hh = -sum(q * math.log(q) for q in p if q > 0)
        if abs(Hh - target) <= tol: break
        if Hh > target:
            lo = beta; beta = beta * 2 if hi == math.inf else (beta + hi) / 2
        else:
            hi = beta; beta = beta / 2 if lo == -math.inf else (beta + lo) / 2
    return p


Pc_ref = np.zeros((nT, nT))
for i in range(nT):
    idx = [j for j in range(nT) if j != i]; p = cond_row_py([D2[i, j] for j in idx], perp)
    Pc_ref[i, idx] = p
Pc = _tu._binary_search_perplexity(D2.astype(np.float32), perp, 0)
Hrows = [-sum(q * math.log(q) for q in Pc[i] if q > 0) for i in range(nT)]
report("TSNE perplexity calibration: every conditional row p_{.|i} reaches entropy log(perplexity) within the binary-search tol 1e-5", max(abs(h_ - math.log(perp)) for h_ in Hrows) <= 1e-5 + 1e-9, f"(max |H - log perp| {max(abs(h_ - math.log(perp)) for h_ in Hrows):.2e})")
report("TSNE conditional P rows = plain-Python binary search (rel 1e-3; both within tol)", np.allclose(Pc, Pc_ref, rtol=1e-3, atol=1e-7), f"(max|diff| {np.max(np.abs(Pc - Pc_ref)):.1e})")
Pj_ref = (Pc_ref + Pc_ref.T) / (2 * nT)
Pj = _t_sne._joint_probabilities(D2, perp, 0)
from scipy.spatial.distance import squareform
report("TSNE exact joint P = (p_{j|i} + p_{i|j}) / 2n (symmetrised, sums to 1)", np.allclose(squareform(Pj), Pj_ref, rtol=1e-3, atol=1e-9) and close(Pj.sum() * 2, 1.0, rel=1e-9), f"(sum over i!=j {2 * Pj.sum():.12f})")
kn = min(nT - 1, int(3 * perp + 1))
nbT = [sorted(range(nT), key=lambda j: (D2[i, j], j))[1:kn + 1] for i in range(nT)]
Pcn = np.zeros((nT, nT))
for i in range(nT):
    Pcn[i, nbT[i]] = cond_row_py([D2[i, j] for j in nbT[i]], perp)
Pbh_ref = Pcn + Pcn.T; Pbh_ref /= Pbh_ref.sum()
rows_ = np.repeat(np.arange(nT), kn); cols_ = np.array([j for i in range(nT) for j in nbT[i]])
Dnn = sp.csr_matrix((np.array([D2[i, j] for i in range(nT) for j in nbT[i]]), (rows_, cols_)), shape=(nT, nT))
Pbh = _t_sne._joint_probabilities_nn(Dnn, perp, 0).toarray()
report(f"TSNE barnes_hut P: calibration over the k = min(n-1, 3*perplexity+1) = {kn} nearest neighbours only, then P + P^T normalised to 1", np.allclose(Pbh, Pbh_ref, rtol=1e-3, atol=1e-9), f"(max|diff| {np.max(np.abs(Pbh - Pbh_ref)):.1e})")


def kl_py(P, Y, dof=1.0):
    n = len(Y); num = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j: num[i, j] = (1 + float(np.sum((Y[i] - Y[j]) ** 2)) / dof) ** (-(dof + 1) / 2)
    Q = num / num.sum(); kl = 0.0; grad = np.zeros_like(Y, dtype=float)
    for i in range(n):
        for j in range(n):
            if i != j and P[i, j] > 0: kl += P[i, j] * math.log(P[i, j] / Q[i, j])
    c = 2 * (dof + 1) / dof
    for i in range(n):
        for j in range(n):
            if i != j: grad[i] += c * (P[i, j] - Q[i, j]) * (Y[i] - Y[j]) * (1 + float(np.sum((Y[i] - Y[j]) ** 2)) / dof) ** -1
    return kl, grad


Yr = rs.randn(nT, 2)
kl_r, g_r = kl_py(Pj_ref, Yr)
kl_e, g_e = _t_sne._kl_divergence(Yr.ravel(), Pj, 1.0, nT, 2)
report("TSNE exact objective: KL(P||Q) with Student-t Q and gradient 4 sum_j (p_ij - q_ij)(y_i - y_j)(1+|y_i-y_j|^2)^-1 match the plain-Python formulas", close(kl_e, kl_r, rel=1e-3) and np.allclose(g_e.reshape(nT, 2), g_r, rtol=1e-3, atol=1e-7), f"(KL {kl_e:.8f} vs {kl_r:.8f})")
Pfull = sp.csr_matrix(squareform(Pj))
kl_b, g_b = _t_sne._kl_divergence_bh(Yr.ravel().astype(np.float32), Pfull, 1.0, nT, 2, angle=0.0)
report("TSNE barnes_hut with angle=0 and full P reproduces the exact gradient and KL (float32 tolerance): exact vs barnes_hut agree", np.allclose(g_b.reshape(nT, 2), g_e.reshape(nT, 2), rtol=1e-3, atol=1e-6) and close(kl_b, kl_e, rel=1e-3), f"(max|dgrad| {np.max(np.abs(g_b.reshape(nT, 2) - g_e.reshape(nT, 2))):.1e}; KL {kl_b:.6f} vs {kl_e:.6f})")
kl_b5, g_b5 = _t_sne._kl_divergence_bh(Yr.ravel().astype(np.float32), Pfull, 1.0, nT, 2, angle=0.5)
print(f"   angle=0.5: rel grad error {np.linalg.norm(g_b5 - g_e) / np.linalg.norm(g_e):.2e}")
itkw = {"max_iter": 1000} if V >= (1, 5) else {"n_iter": 1000}
lrk = {"learning_rate": "auto"} if V < (1, 2) else {}
tsE = TSNE(perplexity=perp, method="exact", init="random", random_state=0, **itkw, **lrk).fit(Xt)
Yt = tsE.embedding_.astype(float)
kl_fin, _ = kl_py(Pj_ref, Yt)
report("TSNE(method='exact').kl_divergence_ = KL(P||Q) of the returned embedding recomputed (rel 1e-3)", close(tsE.kl_divergence_, kl_fin, rel=1e-3), f"({tsE.kl_divergence_:.8f} vs {kl_fin:.8f}; n_iter_ {tsE.n_iter_})")
tsB = TSNE(perplexity=perp, method="barnes_hut", init="random", random_state=0, **itkw, **lrk).fit(Xt)
kl_finB, _ = kl_py(Pbh_ref, tsB.embedding_.astype(float))
print(f"   barnes_hut: kl_divergence_ {tsB.kl_divergence_:.6f}; exact KL of its sparse P at the embedding {kl_finB:.6f}; exact-method KL {tsE.kl_divergence_:.6f}")
report("TSNE(method='barnes_hut').kl_divergence_ within 5% of the exact KL(P_bh||Q) of the returned embedding", close(tsB.kl_divergence_, kl_finB, rel=0.05), f"({tsB.kl_divergence_:.6f} vs {kl_finB:.6f})")
report("TSNE exact vs barnes_hut on the same small data: final KL within 25% and both trustworthiness(k=5) > 0.9", close(tsB.kl_divergence_, tsE.kl_divergence_, rel=0.25) and trustworthiness(Xt, tsE.embedding_) > 0.9 and trustworthiness(Xt, tsB.embedding_) > 0.9,
       f"(KL {tsE.kl_divergence_:.4f} / {tsB.kl_divergence_:.4f}; T {trustworthiness(Xt, tsE.embedding_):.4f} / {trustworthiness(Xt, tsB.embedding_):.4f})")
# init='pca' scaling: freeze the optimisation with a negligible learning rate
itkw250 = {"max_iter": 250} if V >= (1, 5) else {"n_iter": 250}
tsP = TSNE(perplexity=perp, init="pca", learning_rate=1e-30, method="exact", random_state=0, **itkw250).fit(Xt)
Xc_ = Xt - Xt.mean(0); Uu, s_, Vt_ = np.linalg.svd(Xc_, full_matrices=False); pcs = Uu[:, :2] * s_[:2]
E0 = tsP.embedding_.astype(float)
if V >= (1, 2):
    pref = pcs / np.std(pcs[:, 0]) * 1e-4
    report("TSNE(init='pca') [1.2+]: initial embedding = PCA scores rescaled so PC1 has std 1e-4 (optimisation frozen by learning_rate=1e-30)", np.allclose(sign_align(E0, pref), pref, rtol=1e-4, atol=1e-10), f"(std col0 {np.std(E0[:, 0]):.4e}, max rel {maxrel(sign_align(E0, pref), pref):.1e})")
else:
    report("TSNE(init='pca') [1.1: 'will change ... in 1.2']: initial embedding = unscaled PCA scores", np.allclose(sign_align(E0, pcs), pcs, rtol=1e-4, atol=1e-5), f"(std col0 {np.std(E0[:, 0]):.4e})")
if V >= (1, 2):
    for n_, ee in [(40, 12.0), (300, 1.0)]:
        Xn_ = rs.randn(n_, 3)
        tl = TSNE(perplexity=5, early_exaggeration=ee, method="exact" if n_ < 100 else "barnes_hut", init="random", random_state=0, **itkw250).fit(Xn_)
        exp_lr = max(n_ / ee / 4, 50)
        report(f"TSNE(learning_rate='auto') n={n_}, early_exaggeration={ee}: learning_rate_ = max(N / early_exaggeration / 4, 50) = {exp_lr:g}", close(tl.learning_rate_, exp_lr))
else:
    print("   learning_rate_ attribute not exposed before 1.2 (skipped)")
e = raises(lambda: TSNE(perplexity=30).fit(rs.randn(20, 3)))
report("TSNE(perplexity >= n_samples) raises ValueError", e == "ValueError", f"({e})")
report("TSNE: embedding_ shape (n, 2), n_iter_ <= max_iter, n_features_in_", tsE.embedding_.shape == (nT, 2) and tsE.n_iter_ <= 1000 and tsE.n_features_in_ == 4)
Dpre_t = edist(Xt); Dpre_t0 = Dpre_t.copy()
tsPre = TSNE(perplexity=perp, method="exact", metric="precomputed", init="random", random_state=0, **itkw, **lrk).fit(Dpre_t)
report("TSNE(metric='precomputed', method='exact') with the Euclidean distance matrix = the default euclidean run ('X is assumed to be a distance matrix'; squared internally)", np.allclose(tsPre.embedding_, tsE.embedding_, rtol=1e-4, atol=1e-4), f"(max|diff| {np.max(np.abs(tsPre.embedding_ - tsE.embedding_)):.1e})")
report("TSNE(metric='precomputed', method='exact').fit(D) leaves the caller's D unchanged (estimators must not mutate X)", np.array_equal(Dpre_t, Dpre_t0), f"(max|D_after - D_before| {np.max(np.abs(Dpre_t - Dpre_t0)):.3g}; D_after == D_before**2: {np.allclose(Dpre_t, Dpre_t0 ** 2)})")
Dbh = Dpre_t0.copy(); TSNE(perplexity=perp, method="barnes_hut", metric="precomputed", init="random", random_state=0, **itkw250, **lrk).fit(Dbh)
report("TSNE(metric='precomputed', method='barnes_hut').fit(D) leaves D unchanged", np.array_equal(Dbh, Dpre_t0))
Dro = Dpre_t0.copy(); Dro.setflags(write=False)
e = raises(lambda: TSNE(perplexity=perp, method="exact", metric="precomputed", init="random", random_state=0, **itkw250, **lrk).fit(Dro))
report("TSNE(metric='precomputed', method='exact') accepts a read-only distance matrix", e is None, f"({e})")


# =====================================================================================================
section("manifold: trustworthiness")
def trust_py(X, Y, k):
    n = len(X); DX = pdist_py(X); DY = pdist_py(Y); s = 0
    for i in range(n):
        orderX = sorted((j for j in range(n) if j != i), key=lambda j: (DX[i][j], j))
        rank = {j: r + 1 for r, j in enumerate(orderX)}
        nnY = sorted((j for j in range(n) if j != i), key=lambda j: (DY[i][j], j))[:k]
        s += sum(max(0, rank[j] - k) for j in nnY)
    return 1 - 2.0 / (n * k * (2 * n - 3 * k - 1)) * s
Xw = rs.randn(30, 5); Yw = Xw[:, :2] + 0.5 * rs.randn(30, 2)
for kw_ in (1, 5, 10):
    report(f"trustworthiness(n_neighbors={kw_}) = 1 - 2/(nk(2n-3k-1)) sum_i sum_(j in U_i^k) max(0, r(i,j) - k) (plain Python)", close(trustworthiness(Xw, Yw, n_neighbors=kw_), trust_py(Xw.tolist(), Yw.tolist(), kw_), rel=1e-12), f"({trustworthiness(Xw, Yw, n_neighbors=kw_):.10f} vs {trust_py(Xw.tolist(), Yw.tolist(), kw_):.10f})")
report("trustworthiness(X, X) = 1", close(trustworthiness(Xw, Xw, n_neighbors=5), 1.0))
e = raises(lambda: trustworthiness(Xw, Yw, n_neighbors=15))
report("trustworthiness(n_neighbors >= n_samples/2) raises ValueError ('should be less than n_samples / 2')", e == "ValueError", f"({e})")
Dpre = edist(Xw)
report("trustworthiness(metric='precomputed') with the distance matrix = euclidean", close(trustworthiness(Dpre, Yw, n_neighbors=5, metric="precomputed"), trustworthiness(Xw, Yw, n_neighbors=5)))


# =====================================================================================================
section("neural_network: MLP forward pass, loss_, gradients")
def act_f(name, z):
    if name == "identity": return z
    if name == "logistic": return 1 / (1 + np.exp(-z))
    if name == "tanh": return np.tanh(z)
    if name == "relu": return np.maximum(z, 0)


def forward(X, coefs, inter, hid, out):
    a = np.asarray(X, float)
    for i, (W, b) in enumerate(zip(coefs, inter)):
        z = a @ W + b
        if i < len(coefs) - 1: a = act_f(hid, z)
        else:
            if out == "softmax":
                z = z - z.max(1, keepdims=True); e = np.exp(z); a = e / e.sum(1, keepdims=True)
            else: a = act_f(out, z)
    return a


def l2(coefs): return sum(float(np.sum(W ** 2)) for W in coefs)


def doc_loss(kind, Y, Yhat, coefs, alpha, n):
    """User-guide formulas: (1/2n) sum_i ||yhat_i - y_i||^2 + alpha/(2n)||W||^2 ;
    -(1/n) sum (y ln yhat + (1-y) ln(1-yhat)) + alpha/(2n)||W||^2 ; multiclass: -(1/n) sum_i ln yhat_i[y_i]."""
    if kind == "squared": data = float(np.sum((Yhat - Y) ** 2)) / (2 * n)
    elif kind == "binary": data = -float(np.sum(Y * np.log(Yhat) + (1 - Y) * np.log(1 - Yhat))) / n
    else: data = -float(np.sum(Y * np.log(Yhat))) / n
    return data + alpha / (2 * n) * l2(coefs)


Xn = rs.randn(40, 3); nN = 40
yb = (Xn[:, 0] + 0.5 * Xn[:, 1] + 0.3 * rs.randn(40) > 0).astype(int)
cb = MLPClassifier(hidden_layer_sizes=(4,), activation="tanh", solver="lbfgs", alpha=0.3, max_iter=500, random_state=0).fit(Xn, yb)
pb = forward(Xn, cb.coefs_, cb.intercepts_, "tanh", "logistic")[:, 0]
report("MLPClassifier binary: out_activation_ 'logistic'; predict_proba = [1-s, s] with s = logistic of the recomputed forward pass", cb.out_activation_ == "logistic" and np.allclose(cb.predict_proba(Xn), np.c_[1 - pb, pb], rtol=1e-12, atol=1e-14))
Lb = doc_loss("binary", yb, pb, cb.coefs_, 0.3, nN)
report("MLPClassifier binary (lbfgs): loss_ = -(1/n) sum [y ln p + (1-y) ln(1-p)] + alpha/(2n) ||W||^2 at the returned weights", close(cb.loss_, Lb, rel=1e-10), f"({cb.loss_:.12g} vs {Lb:.12g})")
report("MLPClassifier.predict = classes_[proba >= 0.5] (binary threshold)", np.array_equal(cb.predict(Xn), cb.classes_[(pb > 0.5).astype(int)]))
ym = np.digitize(Xn[:, 0] + 0.3 * rs.randn(40), [-0.5, 0.5])
cm_ = MLPClassifier(hidden_layer_sizes=(5, 3), activation="relu", solver="lbfgs", alpha=0.1, max_iter=500, random_state=1).fit(Xn, ym)
pm = forward(Xn, cm_.coefs_, cm_.intercepts_, "relu", "softmax")
Ym = (ym[:, None] == cm_.classes_[None]).astype(float)
report("MLPClassifier multiclass: out_activation_ 'softmax'; predict_proba = softmax of the recomputed forward pass (2 hidden layers)", cm_.out_activation_ == "softmax" and np.allclose(cm_.predict_proba(Xn), pm, rtol=1e-10, atol=1e-14))
report("MLPClassifier multiclass (lbfgs): loss_ = -(1/n) sum_i ln p_i[y_i] + alpha/(2n)||W||^2", close(cm_.loss_, doc_loss("multi", Ym, pm, cm_.coefs_, 0.1, nN), rel=1e-9), f"({cm_.loss_:.12g} vs {doc_loss('multi', Ym, pm, cm_.coefs_, 0.1, nN):.12g})")
Yml = np.c_[yb, (Xn[:, 2] > 0).astype(int), (Xn[:, 1] > 0.3).astype(int)]
cml = MLPClassifier(hidden_layer_sizes=(4,), activation="logistic", solver="lbfgs", alpha=0.2, max_iter=500, random_state=0).fit(Xn, Yml)
pml = forward(Xn, cml.coefs_, cml.intercepts_, "logistic", "logistic")
report("MLPClassifier multilabel: independent logistic outputs; predict_proba recomputed", cml.out_activation_ == "logistic" and np.allclose(cml.predict_proba(Xn), pml, rtol=1e-10, atol=1e-14))
report("MLPClassifier multilabel (lbfgs): loss_ = binary cross-entropy summed over labels / n + alpha/(2n)||W||^2", close(cml.loss_, doc_loss("binary", Yml, pml, cml.coefs_, 0.2, nN), rel=1e-9), f"({cml.loss_:.12g} vs {doc_loss('binary', Yml, pml, cml.coefs_, 0.2, nN):.12g})")
yr = Xn @ np.array([1.0, -2.0, 0.5]) + 0.1 * rs.randn(40)
for actn in ("identity", "logistic", "tanh", "relu"):
    rg = MLPRegressor(hidden_layer_sizes=(6,), activation=actn, solver="lbfgs", alpha=0.05, max_iter=300, random_state=0).fit(Xn, yr)
    pr = forward(Xn, rg.coefs_, rg.intercepts_, actn, "identity")[:, 0]
    report(f"MLPRegressor(activation='{actn}'): predict = identity output of the recomputed forward pass", np.allclose(rg.predict(Xn), pr, rtol=1e-12, atol=1e-12))
    report(f"MLPRegressor(activation='{actn}', lbfgs): loss_ = (1/2n) sum (yhat - y)^2 + alpha/(2n)||W||^2 at the returned weights", close(rg.loss_, doc_loss("squared", yr, pr, rg.coefs_, 0.05, nN), rel=1e-9), f"({rg.loss_:.12g} vs {doc_loss('squared', yr, pr, rg.coefs_, 0.05, nN):.12g})")
Yr2 = np.c_[yr, 2 * Xn[:, 1] ** 2]
rg2 = MLPRegressor(hidden_layer_sizes=(6,), activation="tanh", solver="lbfgs", alpha=0.05, max_iter=300, random_state=0).fit(Xn, Yr2)
pr2 = forward(Xn, rg2.coefs_, rg2.intercepts_, "tanh", "identity")
ug = doc_loss("squared", Yr2, pr2, rg2.coefs_, 0.05, nN)
per_out = float(np.sum((pr2 - Yr2) ** 2)) / (2 * nN * 2) + 0.05 / (2 * nN) * l2(rg2.coefs_)
print(f"   2-output regressor: loss_ {rg2.loss_:.10g}; user-guide (1/2n) sum_i ||yhat_i - y_i||^2 + reg {ug:.10g}; mean over outputs too {per_out:.10g}")
report("MLPRegressor 2 outputs (lbfgs): loss_ = user-guide Loss = 1/(2n) sum_i ||yhat_i - y_i||_2^2 + alpha/(2n)||W||^2", close(rg2.loss_, ug, rel=1e-9), f"({rg2.loss_:.10g} vs {ug:.10g}; = {per_out:.10g} with the squared error also averaged over the 2 outputs)")

# gradient check through _backprop
def backprop(est, X, Y):
    nl = est.n_layers_
    acts = [X] + [None] * (nl - 1); deltas = [None] * (nl - 1)
    cg = [np.empty_like(W) for W in est.coefs_]; ig = [np.empty_like(b) for b in est.intercepts_]
    if "sample_weight" in inspect.signature(est._backprop).parameters:
        return est._backprop(X, Y, None, acts, deltas, cg, ig)
    return est._backprop(X, Y, acts, deltas, cg, ig)


def fd_check(est, X, Y, kind, hid, out, alpha):
    loss, cg, ig = backprop(est, X, Y)
    n_ = len(X)
    def f():
        return doc_loss(kind, Y, forward(X, est.coefs_, est.intercepts_, hid, out), est.coefs_, alpha, n_)
    worst = 0.0
    for arrs, grads in ((est.coefs_, cg), (est.intercepts_, ig)):
        for A_, G_ in zip(arrs, grads):
            for idx in np.ndindex(A_.shape):
                old = A_[idx]; h_ = 1e-6
                A_[idx] = old + h_; fp = f(); A_[idx] = old - h_; fm = f(); A_[idx] = old
                num = (fp - fm) / (2 * h_); worst = max(worst, abs(num - G_[idx]) / max(1e-6, abs(num)))
    return loss, f(), worst


Xs3 = rs.randn(7, 3)
er = MLPRegressor(hidden_layer_sizes=(4, 3), activation="tanh", alpha=0.7, max_iter=1, solver="sgd", random_state=0).fit(Xs3, rs.randn(7))
yy = rs.randn(7, 1)
lo_, lf, wr = fd_check(er, Xs3, yy, "squared", "tanh", "identity", 0.7)
report("MLPRegressor._backprop: loss = documented squared loss (recomputed) and gradients = central finite differences of it (2 hidden tanh layers)", close(lo_, lf, rel=1e-12) and wr < 1e-5, f"(loss {lo_:.10g} vs {lf:.10g}; worst rel grad err {wr:.1e})")
ec = MLPClassifier(hidden_layer_sizes=(4,), activation="logistic", alpha=0.4, max_iter=1, solver="sgd", random_state=0).fit(Xs3, [0, 1, 2, 0, 1, 2, 0])
Yc = np.eye(3)[[2, 0, 1, 1, 0, 2, 2]]
lo_, lf, wc = fd_check(ec, Xs3, Yc, "multi", "logistic", "softmax", 0.4)
report("MLPClassifier._backprop (softmax + cross-entropy): loss recomputed and gradients = finite differences", close(lo_, lf, rel=1e-12) and wc < 1e-5, f"(loss {lo_:.10g} vs {lf:.10g}; worst rel grad err {wc:.1e})")
ecb = MLPClassifier(hidden_layer_sizes=(3,), activation="relu", alpha=0.4, max_iter=1, solver="sgd", random_state=2).fit(Xs3, [0, 1, 1, 0, 1, 0, 0])
lo_, lf, wb = fd_check(ecb, Xs3, np.array([[1], [0], [1], [1], [0], [0], [1.0]]), "binary", "relu", "logistic", 0.4)
report("MLPClassifier._backprop (logistic output + binary cross-entropy, relu hidden): loss and gradients = finite differences", close(lo_, lf, rel=1e-12) and wb < 1e-4, f"(worst rel grad err {wb:.1e})")

section("neural_network: MLP training bookkeeping (n_iter_, t_, partial_fit, early stopping, loss_ per epoch)")
Xe_ = rs.randn(53, 3); ye_ = (Xe_[:, 0] > 0).astype(int)
ce = MLPClassifier(hidden_layer_sizes=(5,), solver="adam", learning_rate_init=0.05, max_iter=15, early_stopping=True, validation_fraction=0.2, n_iter_no_change=100, random_state=0).fit(Xe_, ye_)
nval = math.ceil(0.2 * 53); ntr = 53 - nval
vs = np.array(ce.validation_scores_)
print(f"   validation_scores_ * {nval}: {np.round(vs * nval, 6).tolist()[:6]} ...; n_iter_ {ce.n_iter_}, t_ {ce.t_}")
report(f"MLPClassifier(early_stopping, validation_fraction=0.2) on 53 samples: validation set of ceil(0.2*53) = {nval} samples (every validation accuracy a multiple of 1/{nval})", np.allclose(vs * nval, np.round(vs * nval), atol=1e-9) and len(vs) == ce.n_iter_)
report(f"MLPClassifier(early_stopping): t_ = n_iter_ * n_training_samples ({ntr}) ('number of training samples seen by the solver')", ce.t_ == ce.n_iter_ * ntr, f"(t_ {ce.t_}, n_iter_ {ce.n_iter_})")
if "set to `None`" in (MLPClassifier.__doc__ or "") or "set to None" in (MLPClassifier.__doc__ or ""):
    report("MLPClassifier(early_stopping=True): best_loss_ is None (documented)", ce.best_loss_ is None, f"({ce.best_loss_})")
cn = MLPClassifier(hidden_layer_sizes=(5,), solver="sgd", max_iter=7, tol=0.0, n_iter_no_change=1000, random_state=0).fit(Xe_, ye_)
report("MLPClassifier(sgd, max_iter=7, no early stop): n_iter_ = 7, t_ = 7 * n_samples, len(loss_curve_) = 7", cn.n_iter_ == 7 and cn.t_ == 7 * 53 and len(cn.loss_curve_) == 7, f"(n_iter_ {cn.n_iter_}, t_ {cn.t_})")
n0, t0 = cn.n_iter_, cn.t_
cn.partial_fit(Xe_, ye_)
exp_n = 1 if V >= (1, 3) else n0 + 1
report("MLPClassifier.partial_fit after fit: t_ + n_samples; n_iter_ = iterations of this call (1) from 1.3 ('n_iter_ ... on the current call', 1.3 changelog), cumulative before", cn.n_iter_ == exp_n and cn.t_ == t0 + 53, f"(n_iter_ {cn.n_iter_}, t_ {cn.t_})")
rq = MLPRegressor(hidden_layer_sizes=(3,), solver="sgd", max_iter=5, tol=0.0, n_iter_no_change=1000, random_state=0).fit(Xe_, Xe_[:, 0])
rq.partial_fit(Xe_, Xe_[:, 0])
report("MLPRegressor fit(max_iter=5) + partial_fit: t_ 'Mathematically equals n_iters * X.shape[0]' (docstring) with n_iters = n_iter_", rq.t_ == rq.n_iter_ * 53, f"(t_ {rq.t_}, n_iter_ {rq.n_iter_}, n_iter_ * n = {rq.n_iter_ * 53})")
e = raises(lambda: MLPClassifier(solver="sgd").partial_fit(Xe_, ye_))
report("MLPClassifier.partial_fit first call without classes raises ValueError", e == "ValueError", f"({e})")
# loss_ of an epoch with a full batch = loss at the weights the epoch started from
pr_ = MLPRegressor(hidden_layer_sizes=(4,), activation="tanh", solver="sgd", alpha=0.5, batch_size=53, learning_rate_init=0.01, momentum=0.0, shuffle=False, max_iter=1, random_state=0)
yr_ = Xe_ @ np.array([1.0, 0.5, -1.0])
pr_.partial_fit(Xe_, yr_)
W0 = [W.copy() for W in pr_.coefs_]; b0 = [b.copy() for b in pr_.intercepts_]
pr_.partial_fit(Xe_, yr_)
L0 = doc_loss("squared", yr_, forward(Xe_, W0, b0, "tanh", "identity")[:, 0], W0, 0.5, 53)
report("MLPRegressor(sgd, full batch).partial_fit: loss_ = documented loss at the weights the epoch started from", close(pr_.loss_, L0, rel=1e-10), f"({pr_.loss_:.12g} vs {L0:.12g})")
# mini-batches with (practically) frozen weights: the reported epoch loss vs the documented loss
fr = MLPRegressor(hidden_layer_sizes=(4,), activation="tanh", solver="sgd", alpha=5.0, batch_size=13, learning_rate_init=1e-14, momentum=0.0, shuffle=False, max_iter=1, random_state=0)
fr.partial_fit(Xe_[:52], yr_[:52])
Wf = [W.copy() for W in fr.coefs_]; bf = [b.copy() for b in fr.intercepts_]
fr.partial_fit(Xe_[:52], yr_[:52])
Lf = doc_loss("squared", yr_[:52], forward(Xe_[:52], Wf, bf, "tanh", "identity")[:, 0], Wf, 5.0, 52)
Lf4 = Lf + 3 * 5.0 / (2 * 52) * l2(Wf)
print(f"   4 mini-batches of 13, weights frozen: loss_ {fr.loss_:.10g}; documented loss {Lf:.10g}; with the L2 term counted once per batch {Lf4:.10g}")
report("MLPRegressor(sgd, batch_size=13 -> 4 batches per epoch, weights frozen): loss_ = documented loss (data term + alpha/(2n)||W||^2)", close(fr.loss_, Lf, rel=1e-8), f"({fr.loss_:.10g} vs {Lf:.10g}; = {Lf4:.10g} with alpha/(2n)||W||^2 counted per batch)")
cmp_ = MLPRegressor(hidden_layer_sizes=(3,), solver="lbfgs", alpha=0.1, max_iter=200, random_state=0)
if has_param(MLPRegressor.fit, "sample_weight"):
    swt = np.array([2, 1, 3, 1, 1, 2, 1] * 3)[:20]
    Xw_ = rs.randn(20, 2); yw_ = Xw_[:, 0] - Xw_[:, 1] ** 2
    a1 = MLPRegressor(hidden_layer_sizes=(3,), solver="lbfgs", alpha=0.1, max_iter=200, random_state=0).fit(Xw_, yw_, sample_weight=swt)
    a2 = MLPRegressor(hidden_layer_sizes=(3,), solver="lbfgs", alpha=0.1, max_iter=200, random_state=0).fit(np.repeat(Xw_, swt, 0), np.repeat(yw_, swt))
    report("MLPRegressor.fit(sample_weight=integers) [1.7+] = fit on rows repeated that many times (lbfgs, same init): same loss_ and coefs_", close(a1.loss_, a2.loss_, rel=1e-6) and all(np.allclose(p, q, rtol=1e-5, atol=1e-7) for p, q in zip(a1.coefs_, a2.coefs_)), f"(loss {a1.loss_:.10g} vs {a2.loss_:.10g})")

section("neural_network: BernoulliRBM")
Xb = (rs.rand(12, 5) > 0.5).astype(float)
rbm = BernoulliRBM(n_components=3, learning_rate=0.1, n_iter=20, random_state=7).fit(Xb)
W_, bh, bv = rbm.components_, rbm.intercept_hidden_, rbm.intercept_visible_
report("BernoulliRBM.transform = P(h=1|v) = logistic(v W^T + b_hidden)", np.allclose(rbm.transform(Xb), 1 / (1 + np.exp(-(Xb @ W_.T + bh))), rtol=1e-12))


def free_energy_mp(v):
    """F(v) = -log sum_h exp(-E(v,h)), E(v,h) = -b_v.v - b_h.h - v^T W^T h, by enumerating the 2^3 hidden states."""
    tot = mpf(0)
    for hs in itertools.product([0, 1], repeat=len(bh)):
        E = -sum(mpf(bv[i]) * v[i] for i in range(len(v))) - sum(mpf(bh[j]) * hs[j] for j in range(len(bh))) - sum(mpf(W_[j, i]) * v[i] * hs[j] for i in range(len(v)) for j in range(len(bh)))
        tot += mpmath.exp(-E)
    return -mpmath.log(tot)


flip = np.random.RandomState(7).randint(0, 5, 12)
ss_ = rbm.score_samples(Xb)
ref = []
for i in range(12):
    v = list(Xb[i]); v2 = list(v); v2[flip[i]] = 1 - v2[flip[i]]
    F1, F2 = free_energy_mp(v), free_energy_mp(v2)
    ref.append(float(5 * mpmath.log(1 / (1 + mpmath.exp(-(F2 - F1))))))
report("BernoulliRBM.score_samples = n_features * log sigmoid(F(v_flipped) - F(v)) with one random bit flipped per sample (free energy by enumerating hidden states in mpmath)", np.allclose(ss_, ref, rtol=1e-10), f"(max|diff| {np.max(np.abs(ss_ - np.array(ref))):.1e})")
pl_exact = []; pl_sd = []
for i in range(12):
    v = list(Xb[i]); F1 = free_energy_mp(v); terms = []
    for kf in range(5):
        v2 = list(v); v2[kf] = 1 - v2[kf]; terms.append(float(5 * mpmath.log(1 / (1 + mpmath.exp(-(free_energy_mp(v2) - F1))))))
    pl_exact.append(sum(terms) / 5); pl_sd.append(float(np.std(terms)))
acc = np.zeros(12)
rb2 = BernoulliRBM(n_components=3); rb2.__dict__.update(rbm.__dict__)
NS = 400
for s_ in range(NS):
    rb2.random_state = s_; acc += rb2.score_samples(Xb)
acc /= NS
zs = np.abs(acc - np.array(pl_exact)) / (np.array(pl_sd) / math.sqrt(NS))
report(f"BernoulliRBM.score_samples averaged over {NS} random flips -> the pseudo-likelihood sum_i log P(v_i | v_-i) (every sample within 4.5 standard errors)", np.all(zs < 4.5), f"(max z {zs.max():.2f})")
report("BernoulliRBM: components_ shape (n_components, n_features), intercepts shapes", W_.shape == (3, 5) and bh.shape == (3,) and bv.shape == (5,))
rb32 = BernoulliRBM(n_components=3, n_iter=2, random_state=0).fit(Xb.astype(np.float32))
report("BernoulliRBM float32 input: components_ and transform stay float32", rb32.components_.dtype == np.float32 and rb32.transform(Xb.astype(np.float32)).dtype == np.float32, f"({rb32.components_.dtype}, {rb32.transform(Xb.astype(np.float32)).dtype})")
report("BernoulliRBM sparse input: transform equals dense", np.allclose(rbm.transform(sp.csr_matrix(Xb)), rbm.transform(Xb)))


# =====================================================================================================
section("datasets: make_classification")
Xc, yc = datasets.make_classification(n_samples=400, n_features=12, n_informative=3, n_redundant=2, n_repeated=3, n_classes=3, n_clusters_per_class=2, flip_y=0.0, shuffle=False, random_state=3)
inf_ = Xc[:, :3]
res_red = np.linalg.lstsq(inf_, Xc[:, 3:5], rcond=None)[1]
report("make_classification(shuffle=False): columns n_inf..n_inf+n_red are exact linear combinations of the informative columns (no intercept)", np.all(res_red < 1e-18 * len(Xc) + 1e-20) or np.allclose(inf_ @ np.linalg.lstsq(inf_, Xc[:, 3:5], rcond=None)[0], Xc[:, 3:5], atol=1e-12), f"(residual SS {res_red})")
rep_ok = all(any(np.array_equal(Xc[:, 5 + r], Xc[:, c]) for c in range(5)) for r in range(3))
report("make_classification(shuffle=False): the next n_repeated columns duplicate informative/redundant columns exactly", rep_ok)
C_noise = np.corrcoef(Xc[:, 8:].T, Xc[:, :5].T)[:4, 4:]
report("make_classification: remaining n_features - 8 columns are independent noise (|corr| with useful columns < 0.2)", np.max(np.abs(C_noise)) < 0.2, f"(max |r| {np.max(np.abs(C_noise)):.3f})")
report("make_classification(weights=None, flip_y=0, shuffle=False): balanced classes (counts differ by <= 1) laid out cluster by cluster", max(np.bincount(yc)) - min(np.bincount(yc)) <= 1 and list(yc[:67]) == [0] * 67, f"(counts {np.bincount(yc).tolist()})")
for cs in (1.0, 2.5):
    Xh, yh = datasets.make_classification(n_samples=8000, n_features=2, n_informative=2, n_redundant=0, n_classes=4, n_clusters_per_class=1, flip_y=0.0, class_sep=cs, shuffle=False, random_state=0)
    cents = np.array([Xh[yh == c].mean(0) for c in range(4)])
    report(f"make_classification(class_sep={cs}): cluster means sit on hypercube vertices (+-class_sep)^n_informative (sample means, within 0.1)", np.allclose(np.abs(cents), cs, atol=0.1) and len({tuple(np.sign(c)) for c in cents}) == 4, f"(means {np.round(cents, 3).tolist()})")
Xw1, yw1 = datasets.make_classification(n_samples=1000, weights=[0.1, 0.3], n_classes=3, n_informative=3, flip_y=0.0, random_state=0)
cnt = np.bincount(yw1, minlength=3)
report("make_classification(weights=[0.1,0.3], 3 classes, flip_y=0): class counts = n*w with the last weight inferred as 0.6 (+- n_clusters_per_class)", all(abs(cnt[i] - 1000 * w) <= 2 for i, w in enumerate([0.1, 0.3, 0.6])), f"(counts {cnt.tolist()})")
Xw2, yw2 = datasets.make_classification(n_samples=100, weights=[0.7, 0.7], flip_y=0.0, random_state=0)
print(f"   weights=[0.7, 0.7] (sum 1.4): returned {len(yw2)} samples, class counts {np.bincount(yw2).tolist()}")
report("make_classification(weights summing to 1.4, n_samples=100): 'More than n_samples samples may be returned if the sum of weights exceeds 1'", len(yw2) > 100, f"(returned {len(yw2)} samples; counts {np.bincount(yw2).tolist()} vs n*w = 70/70)")
Xa, ya = datasets.make_classification(n_samples=20000, n_classes=2, flip_y=0.0, shuffle=False, random_state=5)
Xb_, yb_ = datasets.make_classification(n_samples=20000, n_classes=2, flip_y=0.3, shuffle=False, random_state=5)
frac = float(np.mean(ya != yb_))
report("make_classification(flip_y=0.3, 2 classes): fraction of labels changed ~ flip_y*(1-1/n_classes) = 0.15 ('fraction of samples whose class is assigned randomly')", abs(frac - 0.15) < 4.5 * math.sqrt(0.15 * 0.85 / 20000), f"({frac:.4f})")
X0c, _ = datasets.make_classification(n_samples=50, n_features=6, shift=0.0, scale=1.0, random_state=9, shuffle=False)
X1c, _ = datasets.make_classification(n_samples=50, n_features=6, shift=2.0, scale=3.0, random_state=9, shuffle=False)
report("make_classification(shift=2, scale=3): X = (X_0 + shift) * scale ('scaling happens after shifting')", np.allclose(X1c, (X0c + 2.0) * 3.0, rtol=1e-14))
Xsh, ysh = datasets.make_classification(n_samples=200, n_features=5, n_informative=2, n_redundant=1, n_repeated=1, shift=None, scale=None, random_state=4)
report("make_classification(shift=None, scale=None): random per-feature shift in [-class_sep, class_sep] and scale in [1, 101] (column std range)", np.all(Xsh.std(0) > 0.5), f"(col std {np.round(Xsh.std(0), 2).tolist()})")
e = raises(lambda: datasets.make_classification(n_features=4, n_informative=3, n_redundant=2))
report("make_classification: n_informative + n_redundant + n_repeated > n_features raises ValueError", e == "ValueError", f"({e})")
e = raises(lambda: datasets.make_classification(n_informative=2, n_classes=3, n_clusters_per_class=2, n_redundant=0))
report("make_classification: n_classes * n_clusters_per_class > 2**n_informative raises ValueError", e == "ValueError", f"({e})")
Xrr, _ = datasets.make_classification(n_samples=3, n_features=2004, n_informative=2, n_redundant=2, n_repeated=2000, flip_y=0, shuffle=False, random_state=0)
srcs = collections.Counter(next(c for c in range(4) if np.array_equal(Xrr[:, 4 + r], Xrr[:, c])) for r in range(2000))
print(f"   n_repeated=2000 source columns among the 4 informative+redundant: {dict(sorted(srcs.items()))} (informational: the end columns are drawn half as often)")

section("datasets: make_regression / make_sparse_uncorrelated / friedman")
Xr1, yr1, cf = datasets.make_regression(n_samples=60, n_features=8, n_informative=3, bias=4.5, noise=0.0, coef=True, random_state=0)
report("make_regression(noise=0, coef=True): y = X @ coef + bias exactly", np.allclose(yr1, Xr1 @ cf + 4.5, rtol=1e-12, atol=1e-10))
report("make_regression: exactly n_informative nonzero coefficients, drawn from 100*U(0,1)", np.count_nonzero(cf) == 3 and np.all((cf[cf != 0] > 0) & (cf[cf != 0] < 100)), f"(coef {np.round(cf, 3).tolist()})")
Xr2, yr2, cf2 = datasets.make_regression(n_samples=20000, n_features=5, n_informative=5, noise=2.5, coef=True, random_state=1)
resid = yr2 - Xr2 @ cf2
report("make_regression(noise=2.5): residual y - X coef has std 2.5 ('standard deviation of the gaussian noise')", abs(resid.std() - 2.5) < 4.5 * 2.5 / math.sqrt(2 * 20000) and abs(resid.mean()) < 4.5 * 2.5 / math.sqrt(20000), f"(std {resid.std():.4f}, mean {resid.mean():.4f})")
report("make_regression(effective_rank=None): X is standard normal (mean 0, variance 1)", abs(Xr2.mean()) < 0.02 and abs(Xr2.var() - 1) < 0.03, f"(mean {Xr2.mean():.4f}, var {Xr2.var():.4f})")
Xr3, yr3, cf3 = datasets.make_regression(n_samples=30, n_features=4, n_targets=3, coef=True, random_state=2)
report("make_regression(n_targets=3): y shape (n, 3) and coef shape (n_features, 3), y = X coef", yr3.shape == (30, 3) and cf3.shape == (4, 3) and np.allclose(yr3, Xr3 @ cf3))
Xr4, yr4 = datasets.make_regression(n_samples=50, n_features=40, effective_rank=5, tail_strength=0.2, random_state=3)
sv = np.linalg.svd(Xr4, compute_uv=False); ii = np.arange(40)
prof = (1 - 0.2) * np.exp(-(ii / 5) ** 2) + 0.2 * np.exp(-0.1 * ii / 5)
report("make_regression(effective_rank=5, tail_strength=0.2): X has the make_low_rank_matrix singular profile", np.allclose(sv, prof, rtol=1e-10, atol=1e-12), f"(max|diff| {np.max(np.abs(sv - prof)):.1e})")
Xsu, ysu = datasets.make_sparse_uncorrelated(n_samples=20000, n_features=6, random_state=0)
rsu = ysu - (Xsu[:, 0] + 2 * Xsu[:, 1] - 2 * Xsu[:, 2] - 1.5 * Xsu[:, 3])
report("make_sparse_uncorrelated: y(X) = X0 + 2 X1 - 2 X2 - 1.5 X3 (docstring formula, no noise term)", np.allclose(rsu, 0, atol=1e-12), f"(residual std {rsu.std():.4f}, mean {rsu.mean():.4f})")
report("make_sparse_uncorrelated: X ~ N(0,1)", abs(Xsu.mean()) < 0.02 and abs(Xsu.var() - 1) < 0.03)
Xf1, yf1 = datasets.make_friedman1(n_samples=200, n_features=7, random_state=0)
report("make_friedman1: y = 10 sin(pi x0 x1) + 20 (x2-0.5)^2 + 10 x3 + 5 x4 (noise=0), X ~ U[0,1]^7", np.allclose(yf1, [10 * math.sin(math.pi * a[0] * a[1]) + 20 * (a[2] - 0.5) ** 2 + 10 * a[3] + 5 * a[4] for a in Xf1.tolist()], rtol=1e-13) and Xf1.min() >= 0 and Xf1.max() <= 1 and Xf1.shape == (200, 7))
e = raises(lambda: datasets.make_friedman1(n_features=4))
report("make_friedman1(n_features=4) raises ValueError (needs >= 5)", e is not None, f"({e})")
Xf2, yf2 = datasets.make_friedman2(n_samples=500, random_state=0)
rng_ok = (Xf2[:, 0].min() >= 0 and Xf2[:, 0].max() <= 100 and Xf2[:, 1].min() >= 40 * math.pi and Xf2[:, 1].max() <= 560 * math.pi and Xf2[:, 2].min() >= 0 and Xf2[:, 2].max() <= 1 and Xf2[:, 3].min() >= 1 and Xf2[:, 3].max() <= 11)
report("make_friedman2: documented input ranges and y = sqrt(x0^2 + (x1 x2 - 1/(x1 x3))^2)", rng_ok and np.allclose(yf2, [math.sqrt(a[0] ** 2 + (a[1] * a[2] - 1 / (a[1] * a[3])) ** 2) for a in Xf2.tolist()], rtol=1e-13))
Xf3, yf3 = datasets.make_friedman3(n_samples=500, random_state=0)
report("make_friedman3: y = arctan((x1 x2 - 1/(x1 x3)) / x0)", np.allclose(yf3, [math.atan((a[1] * a[2] - 1 / (a[1] * a[3])) / a[0]) for a in Xf3.tolist()], rtol=1e-13))
_, yfn = datasets.make_friedman3(n_samples=20000, noise=0.3, random_state=0); Xfn, _ = datasets.make_friedman3(n_samples=20000, noise=0.0, random_state=0)
rf = yfn - np.array([math.atan((a[1] * a[2] - 1 / (a[1] * a[3])) / a[0]) for a in Xfn.tolist()])
report("make_friedman3(noise=0.3): y - formula ~ 0.3 N(0,1) (same X for the same seed)", abs(rf.std() - 0.3) < 0.01, f"(std {rf.std():.4f})")

section("datasets: blobs / moons / circles / s_curve / swiss_roll / hastie / gaussian_quantiles")
cen = np.array([[0.0, 0.0], [10.0, -5.0], [-8.0, 6.0]]); stds = [0.5, 1.0, 2.0]
Xbl, ybl = datasets.make_blobs(n_samples=30001, centers=cen, cluster_std=stds, random_state=0)
cnt = np.bincount(ybl)
report("make_blobs(n_samples=30001, 3 centers): 'equally divided among clusters' (remainder to the first)", cnt.tolist() == [10001, 10000, 10000], f"({cnt.tolist()})")
ok = all(np.allclose(Xbl[ybl == c].mean(0), cen[c], atol=4.5 * stds[c] / math.sqrt(10000)) and np.allclose(Xbl[ybl == c].std(0), stds[c], rtol=0.03) for c in range(3))
report("make_blobs(centers=array, cluster_std=list): per-cluster mean = center, per-coordinate std = cluster_std", ok)
Xbl2, ybl2, cen2 = datasets.make_blobs(n_samples=[5, 7, 9], n_features=3, center_box=(2.0, 3.0), return_centers=True, random_state=1)
report("make_blobs(n_samples=[5,7,9], return_centers=True): per-cluster counts as given, centers drawn inside center_box", np.bincount(ybl2).tolist() == [5, 7, 9] and cen2.shape == (3, 3) and cen2.min() >= 2 and cen2.max() <= 3)
Xm, ym_ = datasets.make_moons(n_samples=101, shuffle=False, noise=None)
o = Xm[ym_ == 0]; i_ = Xm[ym_ == 1]
report("make_moons(101, noise=None): 50 outer / 51 inner; outer on the unit upper half circle, inner on the unit circle centred (1, 0.5) lower half", len(o) == 50 and len(i_) == 51 and np.allclose(np.hypot(o[:, 0], o[:, 1]), 1) and np.all(o[:, 1] >= -1e-12) and np.allclose(np.hypot(i_[:, 0] - 1, i_[:, 1] - 0.5), 1) and np.all(i_[:, 1] <= 0.5 + 1e-12))
Xm2, ym2 = datasets.make_moons(n_samples=(3, 8), random_state=0)
report("make_moons(n_samples=(3, 8)) tuple: 3 outer, 8 inner", np.bincount(ym2).tolist() == [3, 8])
Xci, yci = datasets.make_circles(n_samples=101, factor=0.3, shuffle=False)
r_ = np.hypot(Xci[:, 0], Xci[:, 1])
report("make_circles(101, factor=0.3): outer radius 1 (50 points), inner radius factor (51 points), angles evenly spaced without duplicates", np.allclose(r_[yci == 0], 1) and np.allclose(r_[yci == 1], 0.3) and np.bincount(yci).tolist() == [50, 51] and len(np.unique(np.round(Xci, 12), axis=0)) == 101)
e = raises(lambda: datasets.make_circles(factor=1.0))
report("make_circles(factor=1.0) raises ValueError (factor must be < 1)", e is not None, f"({e})")
Xsc, tsc = datasets.make_s_curve(n_samples=300, random_state=0)
report("make_s_curve: x = sin t, z = sign(t)(cos t - 1), y in [0,2], t in [-3pi/2, 3pi/2]", np.allclose(Xsc[:, 0], np.sin(tsc)) and np.allclose(Xsc[:, 2], np.sign(tsc) * (np.cos(tsc) - 1)) and Xsc[:, 1].min() >= 0 and Xsc[:, 1].max() <= 2 and np.abs(tsc).max() <= 1.5 * math.pi)
Xsw, tsw = datasets.make_swiss_roll(n_samples=300, random_state=0)
report("make_swiss_roll: x = t cos t, z = t sin t, y in [0,21], t in [1.5pi, 4.5pi]", np.allclose(Xsw[:, 0], tsw * np.cos(tsw)) and np.allclose(Xsw[:, 2], tsw * np.sin(tsw)) and Xsw[:, 1].min() >= 0 and Xsw[:, 1].max() <= 21 and tsw.min() >= 1.5 * math.pi and tsw.max() <= 4.5 * math.pi)
if has_param(datasets.make_swiss_roll, "hole"):
    Xh_, th_ = datasets.make_swiss_roll(n_samples=3000, hole=True, random_state=0)
    inhole = (th_ > 2.5 * math.pi) & (th_ < 3.5 * math.pi) & (Xh_[:, 1] > 7) & (Xh_[:, 1] < 14)
    report("make_swiss_roll(hole=True): no point in the central (t, y) rectangle", not inhole.any() and np.allclose(Xh_[:, 0], th_ * np.cos(th_)), f"({inhole.sum()} in hole)")
Xha, yha = datasets.make_hastie_10_2(n_samples=5000, random_state=0)
report("make_hastie_10_2: y = 1 if sum(x^2) > 9.34 else -1; X standard normal, shape (n, 10)", Xha.shape == (5000, 10) and np.array_equal(yha, np.where((Xha ** 2).sum(1) > 9.34, 1.0, -1.0)))
p934 = float(mpmath.gammainc(5, 0, 9.34 / 2, regularized=True))
report("make_hastie_10_2: 9.34 is the chi2(10) median -> class balance ~ 1/2", abs(p934 - 0.5) < 1e-3 and abs(np.mean(yha > 0) - (1 - p934)) < 4.5 * 0.5 / math.sqrt(5000), f"(P(chi2_10 <= 9.34) = {p934:.5f}; frac +1 {np.mean(yha > 0):.4f})")
Xgq, ygq = datasets.make_gaussian_quantiles(n_samples=3000, n_features=3, n_classes=3, cov=2.0, mean=[1.0, -1.0, 0.5], shuffle=False, random_state=0)
r2 = ((Xgq - np.array([1.0, -1.0, 0.5])) ** 2).sum(1)
nested = all(r2[ygq == c].max() <= r2[ygq == c + 1].min() for c in range(2))
q = [float(2.0 * mpmath.findroot(lambda x: mpmath.gammainc(1.5, 0, x / 2, regularized=True) - mpf(k) / 3, 3.0)) for k in (1, 2)]
bnd = [r2[ygq == 0].max(), r2[ygq == 1].max()]
report("make_gaussian_quantiles(mean, cov=2): classes are nested shells in squared distance from the mean", nested)
def chi2pdf(x, k): return float(mpmath.power(x, k / 2 - 1) * mpmath.exp(-x / 2) / (mpmath.power(2, k / 2) * mpmath.gamma(k / 2)))
se_q = [math.sqrt(qq * (1 - qq) / 3000) / (chi2pdf(x / 2.0, 3) / 2.0) for qq, x in zip((1 / 3, 2 / 3), q)]
report("make_gaussian_quantiles: shell boundaries at cov * chi2(n_features) quantiles 1/3, 2/3 (within 4.5 standard errors of a sample quantile)", all(abs(b - qq) < 4.5 * se for b, qq, se in zip(bnd, q, se_q)), f"(boundaries {np.round(bnd, 4).tolist()} vs {np.round(q, 4).tolist()}, SE {np.round(se_q, 3).tolist()})")
report("make_gaussian_quantiles(n_samples=3000, n_classes=3): 'equally divided among classes' (1000 each)", np.bincount(ygq).tolist() == [1000, 1000, 1000])
_, yq2 = datasets.make_gaussian_quantiles(n_samples=11, n_classes=4, random_state=0)
report("make_gaussian_quantiles(n_samples=11, n_classes=4): 'equally divided among classes' -> counts differ by at most 1", max(np.bincount(yq2)) - min(np.bincount(yq2)) <= 1, f"(counts {np.bincount(yq2).tolist()})")

section("datasets: low-rank / spd / sparse spd / multilabel / biclusters / checkerboard")
for (ns, nf, er, ts) in [(30, 50, 4, 0.5), (60, 20, 10, 0.0), (40, 40, 2, 1.0)]:
    Lr = datasets.make_low_rank_matrix(n_samples=ns, n_features=nf, effective_rank=er, tail_strength=ts, random_state=0)
    ii = np.arange(min(ns, nf)); prof = (1 - ts) * np.exp(-(ii / er) ** 2) + ts * np.exp(-0.1 * ii / er)
    sv = np.linalg.svd(Lr, compute_uv=False)
    report(f"make_low_rank_matrix({ns}x{nf}, effective_rank={er}, tail_strength={ts}): singular values = (1-ts) exp(-(i/r)^2) + ts exp(-0.1 i/r)", np.allclose(sv, np.sort(prof)[::-1], rtol=1e-9, atol=1e-13), f"(max|diff| {np.max(np.abs(sv - np.sort(prof)[::-1])):.1e})")
S_ = datasets.make_spd_matrix(6, random_state=0)
asym = np.max(np.abs(S_ - S_.T))
report("make_spd_matrix(6): symmetric (to 1e-12) and positive definite", asym < 1e-12 and np.linalg.eigvalsh((S_ + S_.T) / 2).min() > 0, f"(max|S - S^T| {asym:.1e}; min eig {np.linalg.eigvalsh((S_ + S_.T) / 2).min():.3f})")
print(f"   make_spd_matrix exact symmetry: {np.array_equal(S_, S_.T)} (max asymmetry {asym:.1e})")
kd = "n_dim" if has_param(datasets.make_sparse_spd_matrix, "n_dim") else "dim"
Ssp = datasets.make_sparse_spd_matrix(**{kd: 30}, alpha=0.9, random_state=0)
report("make_sparse_spd_matrix(30, alpha=0.9): exactly symmetric, positive definite, sparse", np.array_equal(Ssp, Ssp.T) and np.linalg.eigvalsh(Ssp).min() > 0 and np.mean(Ssp == 0) > 0.5, f"(zeros {np.mean(Ssp == 0):.2f}, min eig {np.linalg.eigvalsh(Ssp).min():.3f})")
Ssn = datasets.make_sparse_spd_matrix(**{kd: 30}, alpha=0.9, norm_diag=True, random_state=0)
report("make_sparse_spd_matrix(norm_diag=True): unit diagonal, still PD", np.allclose(np.diag(Ssn), 1) and np.linalg.eigvalsh(Ssn).min() > 0)
if has_param(datasets.make_sparse_spd_matrix, "sparse_format"):
    Sf = datasets.make_sparse_spd_matrix(n_dim=30, alpha=0.9, sparse_format="csr", random_state=0)
    report("make_sparse_spd_matrix(sparse_format='csr') [1.4+]: sparse CSR equal to the dense output", sp.issparse(Sf) and Sf.format == "csr" and np.allclose(Sf.toarray(), Ssp))
for allow in (True, False):
    Xml, Yml_, pc, pwc = datasets.make_multilabel_classification(n_samples=4000, n_features=15, n_classes=4, n_labels=2, length=30, allow_unlabeled=allow, return_distributions=True, random_state=0)
    lo = 0 if allow else 1
    ks = range(lo, 5); wts = [mpmath.poisson(2) if False else mpf(2) ** k * mpmath.exp(-2) / mpmath.factorial(k) for k in ks]
    mean_t = float(sum(k * w for k, w in zip(ks, wts)) / sum(wts)); var_t = float(sum(k * k * w for k, w in zip(ks, wts)) / sum(wts)) - mean_t ** 2
    nl = Yml_.sum(1)
    report(f"make_multilabel_classification(allow_unlabeled={allow}): labels per sample ~ Poisson(2) truncated to [{lo}, n_classes] (mean {mean_t:.4f})", nl.min() >= lo and nl.max() <= 4 and abs(nl.mean() - mean_t) < 4.5 * math.sqrt(var_t / 4000), f"(mean {nl.mean():.4f}; min {nl.min()} max {nl.max()})")
    rsum = Xml.sum(1)
    Lt = [mpf(30) ** k * mpmath.exp(-30) / mpmath.factorial(k) for k in range(0, 200)]
    mean_L = float(sum(k * w for k, w in enumerate(Lt)) / (1 - Lt[0]))
    report(f"make_multilabel_classification(length=30): row sums (document lengths) ~ Poisson(30) conditioned >= 1", rsum.min() >= 1 and abs(rsum.mean() - mean_L) < 4.5 * math.sqrt(30 / 4000), f"(mean {rsum.mean():.3f})")
    report("make_multilabel_classification(return_distributions=True): p_c sums to 1, p_w_c columns sum to 1", close(pc.sum(), 1) and np.allclose(pwc.sum(0), 1))
Xs_, Ys_ = datasets.make_multilabel_classification(n_samples=20, sparse=True, return_indicator="sparse", random_state=1)
Xd_, Yd_ = datasets.make_multilabel_classification(n_samples=20, sparse=False, return_indicator="dense", random_state=1)
report("make_multilabel_classification(sparse=True, return_indicator='sparse') = dense variant (same seed)", sp.issparse(Xs_) and sp.issparse(Ys_) and np.array_equal(Xs_.toarray(), Xd_) and np.array_equal(Ys_.toarray(), Yd_))
_, Yl_ = datasets.make_multilabel_classification(n_samples=20, return_indicator=False, random_state=1)
report("make_multilabel_classification(return_indicator=False): list of label lists matching the indicator", [sorted(r) for r in Yl_] == [sorted(np.nonzero(r)[0].tolist()) for r in Yd_])
Bx, Brow, Bcol = datasets.make_biclusters((30, 20), 3, noise=0.0, minval=10, maxval=100, shuffle=True, random_state=0)
okb = Brow.shape == (3, 30) and Bcol.shape == (3, 20) and np.all(Brow.sum(0) == 1) and np.all(Bcol.sum(0) == 1)
inside = np.zeros_like(Bx, dtype=bool)
for c in range(3):
    blk = Bx[np.ix_(Brow[c], Bcol[c])]; inside |= np.outer(Brow[c], Bcol[c])
    okb &= (blk.size == 0) or (np.ptp(blk) == 0 and 10 <= blk.flat[0] <= 100)
okb &= np.all(Bx[~inside] == 0)
report("make_biclusters((30,20), 3, noise=0): every row/column in exactly one bicluster; each bicluster block constant in [minval, maxval]; zeros elsewhere", bool(okb))
Cx, Crow, Ccol = datasets.make_checkerboard((24, 18), (3, 2), noise=0.0, shuffle=True, random_state=0)
okc = Crow.shape == (6, 24) and Ccol.shape == (6, 18)
for b in range(6):
    blk = Cx[np.ix_(Crow[b], Ccol[b])]; okc &= (blk.size == 0) or (np.ptp(blk) == 0 and 10 <= blk.flat[0] <= 100)
okc &= np.all(np.logical_or.reduce([np.outer(Crow[b], Ccol[b]) for b in range(6)]))
report("make_checkerboard((24,18), (3,2)): 6 biclusters tile the matrix; each block constant in [minval, maxval]", bool(okc))
Bn, Brn, Bcn = datasets.make_biclusters((30, 20), 3, noise=2.0, shuffle=False, random_state=0)
B0, _, _ = datasets.make_biclusters((30, 20), 3, noise=0.0, shuffle=False, random_state=0)
report("make_biclusters(noise=2.0): X - noiseless X has std ~ 2 (same seed, shuffle=False)", abs((Bn - B0).std() - 2.0) < 0.2, f"(std {(Bn - B0).std():.3f})")

dt = {"data_transposed": False} if has_param(datasets.make_sparse_coded_signal, "data_transposed") else {}
Ysc, Dsc, Csc = datasets.make_sparse_coded_signal(n_samples=12, n_components=9, n_features=6, n_nonzero_coefs=3, random_state=0, **dt)
report("make_sparse_coded_signal (data_transposed=False layout): Y = X D, D rows (atoms) unit norm, each code row has exactly n_nonzero_coefs nonzeros", Ysc.shape == (12, 6) and Dsc.shape == (9, 6) and Csc.shape == (12, 9) and np.allclose(Ysc, Csc @ Dsc) and np.allclose(np.linalg.norm(Dsc, axis=1), 1) and np.all((Csc != 0).sum(1) == 3))

section("datasets: bundled load_*")
ir = datasets.load_iris()
report("load_iris: data (150, 4), 50 per class, target_names setosa/versicolor/virginica, 4 feature_names", ir.data.shape == (150, 4) and np.bincount(ir.target).tolist() == [50, 50, 50] and list(ir.target_names) == ["setosa", "versicolor", "virginica"] and len(ir.feature_names) == 4)
report("load_iris: documented summary statistics (sepal length min 4.3 max 7.9 mean 5.84; petal width mean 1.20)", ir.data[:, 0].min() == 4.3 and ir.data[:, 0].max() == 7.9 and round(ir.data[:, 0].mean(), 2) == 5.84 and round(ir.data[:, 3].mean(), 2) == 1.20, f"(mean sl {ir.data[:, 0].mean():.4f}, pw {ir.data[:, 3].mean():.4f})")
Xi_, yi_ = datasets.load_iris(return_X_y=True)
report("load_iris(return_X_y=True) returns (data, target)", np.array_equal(Xi_, ir.data) and np.array_equal(yi_, ir.target))
dg = datasets.load_digits()
report("load_digits: (1797, 64), images (1797, 8, 8) = data reshaped, integer values 0..16, class counts from DESCR", dg.data.shape == (1797, 64) and dg.images.shape == (1797, 8, 8) and np.array_equal(dg.images.reshape(1797, 64), dg.data) and dg.data.min() == 0 and dg.data.max() == 16 and np.all(dg.data == np.round(dg.data)) and np.bincount(dg.target).tolist() == [178, 182, 177, 183, 181, 182, 181, 179, 174, 180], f"({np.bincount(dg.target).tolist()})")
d5 = datasets.load_digits(n_class=5)
report("load_digits(n_class=5): only digits 0..4 (the matching rows of the full set)", set(d5.target) == set(range(5)) and len(d5.target) == sum([178, 182, 177, 183, 181]) and np.array_equal(d5.data, dg.data[dg.target < 5]))
wn = datasets.load_wine()
report("load_wine: (178, 13), class counts 59/71/48", wn.data.shape == (178, 13) and np.bincount(wn.target).tolist() == [59, 71, 48], f"({np.bincount(wn.target).tolist()})")
bc = datasets.load_breast_cancer()
report("load_breast_cancer: (569, 30), 212 malignant (target 0) / 357 benign (target 1)", bc.data.shape == (569, 30) and np.bincount(bc.target).tolist() == [212, 357] and list(bc.target_names) == ["malignant", "benign"])
db = datasets.load_diabetes()
report("load_diabetes: (442, 10), integer target in [25, 346]", db.data.shape == (442, 10) and db.target.min() == 25 and db.target.max() == 346 and np.all(db.target == np.round(db.target)))
dbr = datasets.load_diabetes(scaled=False)
raw = dbr.data
sc_ref = (raw - raw.mean(0)) / (raw.std(0) * math.sqrt(442))
print(f"   diabetes: max|scaled - (raw-mean)/(std*sqrt(n))| {np.max(np.abs(db.data - sc_ref)):.2e}; column sums of squares {np.round((db.data ** 2).sum(0), 8).tolist()}; |mean| max {np.abs(db.data.mean(0)).max():.1e}")
report("load_diabetes(scaled=True): each feature mean-centred and scaled by std * sqrt(n_samples) (recomputed from scaled=False, to 1e-6 abs)", np.allclose(db.data, sc_ref, atol=1e-6), f"(max|diff| {np.max(np.abs(db.data - sc_ref)):.1e})")
report("load_diabetes(scaled=True): 'the sum of squares of each column totals 1' (to 1e-4)", np.allclose((db.data ** 2).sum(0), 1, atol=1e-4))
report("load_diabetes(scaled=False): raw age 19..79 and sex coded 1/2", raw[:, 0].min() == 19 and raw[:, 0].max() == 79 and set(np.unique(raw[:, 1])) == {1.0, 2.0})
ln = datasets.load_linnerud()
report("load_linnerud: data (20, 3) exercise [Chins, Situps, Jumps], target (20, 3) physiological [Weight, Waist, Pulse]", ln.data.shape == (20, 3) and ln.target.shape == (20, 3) and list(ln.feature_names) == ["Chins", "Situps", "Jumps"] and list(ln.target_names) == ["Weight", "Waist", "Pulse"])
report("load_* return Bunch objects with DESCR text and frame=None without as_frame", all(isinstance(b, Bunch) and isinstance(b.DESCR, str) and len(b.DESCR) > 100 and b.get("frame", None) is None for b in (ir, dg, wn, bc, db, ln)))


# =====================================================================================================
section("utils.extmath")
for shp in [(60, 40), (30, 70)]:
    Mlr = rs.randn(shp[0], 5) @ rs.randn(5, shp[1])
    U_, s_, Vt_ = randomized_svd(Mlr, 5, random_state=0)
    s_ex = np.linalg.svd(Mlr, compute_uv=False)[:5]
    report(f"randomized_svd on an exactly rank-5 {shp[0]}x{shp[1]} matrix: singular values = exact SVD (rel 1e-10), U S Vt reconstructs M", np.allclose(s_, s_ex, rtol=1e-10) and np.allclose(U_ * s_ @ Vt_, Mlr, atol=1e-9 * np.abs(Mlr).max()), f"(max rel {maxrel(s_, s_ex):.1e})")
    big = np.argmax(np.abs(U_), axis=0)
    report(f"randomized_svd(flip_sign=True) {shp}: the largest-|.| loading of each left singular vector is positive", np.all(U_[big, np.arange(5)] > 0))
Mfull = rs.randn(80, 50)
s_r = randomized_svd(Mfull, 10, n_iter=10, n_oversamples=30, random_state=0)[1]; s_x = np.linalg.svd(Mfull, compute_uv=False)[:10]
report("randomized_svd on a full-rank Gaussian matrix, n_iter=10: top-10 singular values within 2% of exact", np.allclose(s_r, s_x, rtol=0.02), f"(max rel {maxrel(s_r, s_x):.1e})")
report("weighted_mode docstring example 1: ([4,1,4,2,4,2], ones) -> (array([4.]), array([3.]))", [x.tolist() for x in weighted_mode([4, 1, 4, 2, 4, 2], [1] * 6)] == [[4.0], [3.0]])
report("weighted_mode docstring example 2: weights [1,3,0.5,1.5,1,2] -> (array([2.]), array([3.5]))", [x.tolist() for x in weighted_mode([4, 1, 4, 2, 4, 2], [1, 3, 0.5, 1.5, 1, 2])] == [[2.0], [3.5]])
report("weighted_mode tie ('more than one such value, only the first is returned'): smallest tied value", [x.tolist() for x in weighted_mode([3, 1, 3, 1, 5], [1, 1, 1, 1, 1.5])] == [[1.0], [2.0]])
A2 = rs.randint(0, 3, (4, 6)); W2 = rs.rand(4, 6)
ref_m = []; ref_c = []
for r in range(4):
    tot = collections.defaultdict(float)
    for a, w in zip(A2[r], W2[r]): tot[a] += w
    best = max(sorted(tot), key=lambda a: tot[a]); ref_m.append(best); ref_c.append(tot[best])
mo, co = weighted_mode(A2, W2, axis=1)
report("weighted_mode(axis=1) on a 2-D array = per-row weighted mode (plain Python)", np.allclose(mo.ravel(), ref_m) and np.allclose(co.ravel(), ref_c))
Sd = sp.random(20, 15, density=0.3, random_state=0, format="csr"); Dd = rs.randn(15, 4)
r1 = safe_sparse_dot(Sd, Dd)
report("safe_sparse_dot(sparse, dense) = dense product (returned dense)", np.allclose(np.asarray(r1), Sd.toarray() @ Dd) and not sp.issparse(r1))
r2_ = safe_sparse_dot(Sd, Sd.T)
report("safe_sparse_dot(sparse, sparse) is sparse unless dense_output=True", sp.issparse(r2_) and not sp.issparse(safe_sparse_dot(Sd, Sd.T, dense_output=True)) and np.allclose(r2_.toarray(), Sd.toarray() @ Sd.toarray().T))
report("safe_sparse_dot(dense 1-D, dense 1-D) = inner product", close(safe_sparse_dot(np.arange(3.0), np.arange(3.0)), 5.0))
Xn_ = rs.randn(7, 4)
report("row_norms = sqrt(sum x^2) per row; squared=True the squares; sparse same", np.allclose(row_norms(Xn_), [math.sqrt(sum(v * v for v in r)) for r in Xn_.tolist()]) and np.allclose(row_norms(Xn_, squared=True), (Xn_ ** 2).sum(1)) and np.allclose(row_norms(sp.csr_matrix(Xn_)), row_norms(Xn_)))
if hasattr(extmath, "stable_cumsum"):
    arr = rs.rand(1000).astype(np.float32)
    sc, wsc = caught(lambda: extmath.stable_cumsum(arr))
    ref = list(itertools.accumulate(float(F(float(v))) for v in arr))
    report("stable_cumsum: float64 cumulative sum of the float32 input", sc.dtype == np.float64 and np.allclose(sc, ref, rtol=1e-12))
Xsm = rs.randn(5, 4) * 30
sm = softmax(Xsm)
refsm = np.array([[float(mpmath.exp(v) / mpmath.fsum(mpmath.exp(w) for w in row)) for v in row] for row in Xsm.tolist()])
report("softmax = exp(x) / sum exp(x) per row (mpmath), rows sum to 1, no overflow for |x| ~ 100", np.allclose(sm, refsm, rtol=1e-12, atol=1e-300) and np.allclose(sm.sum(1), 1))
report("softmax(1000 + x) = softmax(x) (max subtracted before exp)", np.allclose(softmax(Xsm + 1000), refsm, rtol=1e-12))
cp = Xsm.copy(); softmax(cp, copy=False)
report("softmax(copy=False) works in place", np.allclose(cp, refsm, rtol=1e-12))
Sden = sp.random(10, 10, density=0.25, random_state=0, format="csr")
report("density(sparse) = nnz / (rows * cols) (docstring example: 0.25)", close(density(Sden), 0.25) and close(density(np.array([[0, 1.0], [2.0, 0]])), 0.5))
report("cartesian docstring example (([1,2,3],[4,5],[6,7])) -> 12 rows in lexicographic order", cartesian(([1, 2, 3], [4, 5], [6, 7])).tolist() == [list(t) for t in itertools.product([1, 2, 3], [4, 5], [6, 7])])
if V >= (1, 2):
    cm2 = cartesian(([1, 2], [0.5, 1.5]))
    report("cartesian of int and float arrays [1.2+]: dtype = most permissive (float64)", cm2.dtype == np.float64 and cm2.tolist() == [[1, 0.5], [1, 1.5], [2, 0.5], [2, 1.5]])
report("fast_logdet docstring example [[5,1],[2,8]] -> log(38)", close(fast_logdet(np.array([[5.0, 1.0], [2.0, 8.0]])), math.log(38), rel=1e-14))
A5 = rs.randn(5, 5); A5 = A5 @ A5.T + np.eye(5)
report("fast_logdet(SPD) = log det (mpmath)", close(fast_logdet(A5), float(mpmath.log(mpmath.det(mpmath.matrix(A5.tolist())))), rel=1e-12))
report("fast_logdet: negative determinant -> -inf; singular -> -inf", fast_logdet(np.array([[0.0, 1.0], [1.0, 0.0]])) == -np.inf and fast_logdet(np.array([[1.0, 2.0], [2.0, 4.0]])) == -np.inf)

section("utils.class_weight")
yw = np.array([1, 1, 1, 1, 0, 0])
report("compute_class_weight('balanced') docstring example [1,1,1,1,0,0] -> [1.5, 0.75]", np.allclose(compute_class_weight("balanced", classes=np.array([0, 1]), y=yw), [1.5, 0.75]))
y3 = np.array(["a"] * 5 + ["b"] * 2 + ["c"] * 13)
cw = compute_class_weight("balanced", classes=np.array(["a", "b", "c"]), y=y3)
report("compute_class_weight('balanced') = n_samples / (n_classes * bincount(y)) (Fractions)", np.allclose(cw, [float(F(20, 3 * 5)), float(F(20, 3 * 2)), float(F(20, 3 * 13))], rtol=1e-15))
report("compute_class_weight(None) = ones; dict -> given weights, missing classes 1", np.allclose(compute_class_weight(None, classes=np.array([0, 1, 2]), y=[0, 1, 2]), 1) and np.allclose(compute_class_weight({0: 2.0, 2: 0.5}, classes=np.array([0, 1, 2]), y=[0, 1, 2]), [2.0, 1.0, 0.5]))
e = raises(lambda: compute_class_weight("balanced", classes=np.array([0, 1]), y=[0, 1, 2]))
report("compute_class_weight: labels in y missing from classes raise ValueError", e == "ValueError", f"({e})")
e = raises(lambda: compute_class_weight("balanced", classes=np.array([0, 1, 5]), y=[0, 1, 1]))
report("compute_class_weight('balanced'): a class absent from y raises ValueError ('classes should have valid labels that are in y')", e == "ValueError", f"({e})")
if has_param(compute_class_weight, "sample_weight"):
    swc = np.array([1.0, 2.0, 1.0, 3.0, 0.5, 4.0])
    tot = swc.sum(); w0 = swc[yw == 0].sum(); w1 = swc[yw == 1].sum()
    report("compute_class_weight('balanced', sample_weight) = sum(w) / (n_classes * weighted class count) ('weighted equivalent')", np.allclose(compute_class_weight("balanced", classes=np.array([0, 1]), y=yw, sample_weight=swc), [tot / (2 * w0), tot / (2 * w1)]))
report("compute_sample_weight('balanced') docstring example -> [0.75]*4 + [1.5]*2", np.allclose(compute_sample_weight("balanced", yw), [0.75] * 4 + [1.5] * 2))
Ymo = np.c_[[0, 0, 1, 1, 1, 2], [5, 6, 6, 6, 6, 6]]
w_a = {0: 6 / (3 * 2), 1: 6 / (3 * 3), 2: 6 / (3 * 1)}; w_b = {5: 6 / (2 * 1), 6: 6 / (2 * 5)}
refw = [w_a[a] * w_b[b] for a, b in Ymo.tolist()]
report("compute_sample_weight('balanced', 2-output y): 'the weights of each column of y will be multiplied'", np.allclose(compute_sample_weight("balanced", Ymo), refw))
report("compute_sample_weight([dict, dict], multi-output) = product of the per-output dict weights", np.allclose(compute_sample_weight([{0: 1, 1: 2, 2: 3}, {5: 10, 6: 1}], Ymo), [{0: 1, 1: 2, 2: 3}[a] * {5: 10, 6: 1}[b] for a, b in Ymo.tolist()]))
yi = np.array([0, 0, 0, 1, 1, 2, 2, 2, 2, 2]); ind = np.array([0, 0, 1, 3, 3, 3, 5, 6])
sub = yi[ind]; cnts = collections.Counter(sub.tolist()); kc = len(cnts)
refi = [len(sub) / (kc * cnts[c]) if c in cnts else None for c in yi.tolist()]
got = compute_sample_weight("balanced", yi, indices=ind)
report("compute_sample_weight('balanced', indices=bootstrap): class weights from y[indices] (repeats counted), applied to all samples", np.allclose(got, [r if r is not None else 0.0 for r in refi]), f"({np.round(got, 4).tolist()})")
e = raises(lambda: compute_sample_weight({0: 1}, yi, indices=ind))
report("compute_sample_weight(dict, indices=...) raises ValueError ('Only balanced is supported ... if this is provided')", e == "ValueError", f"({e})")

section("utils: resample / shuffle / chunking / Bunch")
Xr_ = np.arange(40).reshape(20, 2); yr_ = np.arange(20) % 4
a1, b1 = resample(Xr_, yr_, random_state=0)
report("resample default: bootstrap of n rows with replacement, arrays resampled consistently", len(a1) == 20 and np.array_equal(a1[:, 0] // 2 % 4, b1) and len(set(a1[:, 0].tolist())) < 20)
a2, b2 = resample(Xr_, yr_, replace=False, n_samples=7, random_state=0)
report("resample(replace=False, n_samples=7): 7 distinct rows, consistent", len(a2) == 7 and len(set(a2[:, 0].tolist())) == 7 and np.array_equal(a2[:, 0] // 2 % 4, b2))
e = raises(lambda: resample(Xr_, replace=False, n_samples=21))
report("resample(replace=False, n_samples > n) raises ValueError", e == "ValueError", f"({e})")
ys = np.array([0] * 30 + [1] * 10)
_, ys2 = resample(np.arange(40), ys, replace=False, n_samples=20, stratify=ys, random_state=0)
report("resample(stratify=y, n_samples=20, replace=False): class proportions preserved (15 / 5)", np.bincount(ys2).tolist() == [15, 5], f"({np.bincount(ys2).tolist()})")
_, ys3 = resample(np.arange(40), ys, replace=True, n_samples=12, stratify=ys, random_state=1)
report("resample(stratify=y, replace=True, n_samples=12): 9 / 3", np.bincount(ys3).tolist() == [9, 3], f"({np.bincount(ys3).tolist()})")
if has_param(resample, "sample_weight"):
    swr = np.zeros(20); swr[[2, 5]] = [1.0, 3.0]
    r_ = resample(np.arange(20), sample_weight=swr, n_samples=4000, random_state=0)
    report("resample(sample_weight) [1.7+]: zero-weight rows never drawn; frequencies proportional to weights (1:3)", set(r_.tolist()) <= {2, 5} and abs(np.mean(r_ == 5) - 0.75) < 4.5 * math.sqrt(0.75 * 0.25 / 4000), f"(frac of 5: {np.mean(r_ == 5):.4f})")
Ssp_ = sp.csr_matrix(Xr_)
s1, s2, s3 = shuffle(Xr_, yr_, Ssp_, random_state=3)
report("shuffle: a permutation of the rows, applied consistently to arrays and sparse matrices", sorted(s1[:, 0].tolist()) == Xr_[:, 0].tolist() and np.array_equal(s1[:, 0] // 2 % 4, s2) and np.array_equal(s3.toarray(), s1))
s4 = shuffle(Xr_, n_samples=5, random_state=3)
report("shuffle(n_samples=5): first 5 rows of the permutation", len(s4) == 5 and np.array_equal(s4, s1[:5]))
report("gen_batches docstring examples: (7,3), (6,3), (2,3), (7,3,min_batch_size=0), (7,3,min_batch_size=2)",
       list(gen_batches(7, 3)) == [slice(0, 3), slice(3, 6), slice(6, 7)] and list(gen_batches(6, 3)) == [slice(0, 3), slice(3, 6)] and list(gen_batches(2, 3)) == [slice(0, 2)] and list(gen_batches(7, 3, min_batch_size=0)) == [slice(0, 3), slice(3, 6), slice(6, 7)] and list(gen_batches(7, 3, min_batch_size=2)) == [slice(0, 3), slice(3, 7)])
report("gen_even_slices docstring examples: (10,1), (10,10), (10,5), (10,3)",
       list(gen_even_slices(10, 1)) == [slice(0, 10, None)] and list(gen_even_slices(10, 10)) == [slice(i, i + 1, None) for i in range(10)] and list(gen_even_slices(10, 5)) == [slice(i, i + 2, None) for i in range(0, 10, 2)] and list(gen_even_slices(10, 3)) == [slice(0, 4, None), slice(4, 7, None), slice(7, 10, None)])
ok = True
for nn_ in range(1, 23):
    for pk in range(1, 8):
        sl = list(gen_even_slices(nn_, pk)); sizes = [s.stop - s.start for s in sl]
        ok &= (sum(sizes) == nn_ and (max(sizes) - min(sizes) <= 1 if sizes else True) and all(sl[i].stop == sl[i + 1].start for i in range(len(sl) - 1)) and sizes == sorted(sizes, reverse=True))
report("gen_even_slices(n, n_packs) for 1 <= n < 23, packs < 8: contiguous, cover 0..n, sizes differ by <= 1, larger first", ok)
report("gen_even_slices(10, 3, n_samples=8): slices clipped at n_samples", list(gen_even_slices(10, 3, n_samples=8)) == [slice(0, 4, None), slice(4, 7, None), slice(7, 8, None)], f"({list(gen_even_slices(10, 3, n_samples=8))})")
b = Bunch(a=1, b=2)
b.a = 3; b.c = 6; b["d"] = 7
report("Bunch docstring: b['b'] == b.b == 2; b.a = 3 -> b['a'] == 3; b.c = 6 -> b['c'] == 6; keys readable as attributes", b["b"] == b.b == 2 and b["a"] == 3 and b["c"] == 6 and b.d == 7)
bp = pickle.loads(pickle.dumps(b))
report("Bunch survives pickling (keys and attribute access)", bp.a == 3 and bp["d"] == 7 and isinstance(bp, Bunch))
report("Bunch: missing attribute raises AttributeError", raises(lambda: b.zzz) == "AttributeError")

section("utils.sparsefuncs")
Dm_ = rs.randn(12, 5); Dm_[rs.rand(12, 5) < 0.5] = 0
for fmt in ("csr", "csc"):
    Sm = sp.csr_matrix(Dm_) if fmt == "csr" else sp.csc_matrix(Dm_)
    for ax in (0, 1):
        mu, va = mean_variance_axis(Sm, axis=ax)
        report(f"mean_variance_axis({fmt}, axis={ax}) = dense mean and population variance", np.allclose(mu, Dm_.mean(ax), rtol=1e-12, atol=1e-15) and np.allclose(va, Dm_.var(ax), rtol=1e-10, atol=1e-14))
wts = rs.rand(12) + 0.1
mu, va, sw = mean_variance_axis(sp.csr_matrix(Dm_), axis=0, weights=wts, return_sum_weights=True)
mw = (wts[:, None] * Dm_).sum(0) / wts.sum(); vw = (wts[:, None] * (Dm_ - mw) ** 2).sum(0) / wts.sum()
report("mean_variance_axis(weights, return_sum_weights=True): weighted mean / variance, sum of weights per feature", np.allclose(mu, mw) and np.allclose(va, vw) and np.allclose(sw, wts.sum()))
ex = sp.csr_matrix((np.array([8, 1, 2, 5]), np.array([0, 1, 2, 2]), np.array([0, 3, 4, 4, 4])))
mu, va = mean_variance_axis(ex.astype(float), axis=0)
report("mean_variance_axis docstring example -> ([2, 0.25, 1.75], [12, 0.1875, 4.1875])", np.allclose(mu, [2, 0.25, 1.75]) and np.allclose(va, [12, 0.1875, 4.1875]))
m2, v2, n2 = incr_mean_variance_axis(ex.astype(float), axis=0, last_mean=np.zeros(3), last_var=np.zeros(3), last_n=2)
col = [[F(0), F(0), F(8), F(0), F(0), F(0)], [F(0), F(0), F(1), F(0), F(0), F(0)], [F(0), F(0), F(2), F(5), F(0), F(0)]]
mref = [sum(c) / 6 for c in col]; vref = [sum((x - m_) ** 2 for x in c) / 6 for c, m_ in zip(col, mref)]
report("incr_mean_variance_axis docstring example (last_n=2, zero stats): = mean/var of the 6 combined rows (Fractions)", np.allclose(m2, [float(x) for x in mref]) and np.allclose(v2, [float(x) for x in vref]) and np.allclose(n2, 6), f"({np.round(m2, 4).tolist()}, {np.round(v2, 4).tolist()}, {n2.tolist()})")
Da, Db = Dm_[:5], Dm_[5:]
mu_a, va_a = mean_variance_axis(sp.csr_matrix(Da), axis=0)
m3, v3, n3 = incr_mean_variance_axis(sp.csr_matrix(Db), axis=0, last_mean=mu_a, last_var=va_a, last_n=np.full(5, 5.0))
report("incr_mean_variance_axis: stats of batch A updated with batch B = stats of A u B", np.allclose(m3, Dm_.mean(0)) and np.allclose(v3, Dm_.var(0)) and np.allclose(n3, 12))
Dn = Dm_.copy(); Dn[1, 2] = np.nan; Dn[4, 2] = np.nan; Dn[7, 0] = np.nan
m4, v4, n4 = incr_mean_variance_axis(sp.csr_matrix(Dn), axis=0, last_mean=np.zeros(5), last_var=np.zeros(5), last_n=np.zeros(5))
report("incr_mean_variance_axis: 'NaNs are ignored' -> nanmean / nanvar per feature and per-feature counts", np.allclose(m4, np.nanmean(Dn, 0)) and np.allclose(v4, np.nanvar(Dn, 0)) and n4.tolist() == [11, 12, 10, 12, 12], f"(n {n4.tolist()})")
m5, v5, n5 = incr_mean_variance_axis(sp.csc_matrix(Db), axis=1, last_mean=np.zeros(7), last_var=np.zeros(7), last_n=np.zeros(7))
report("incr_mean_variance_axis(axis=1) from zero stats = per-row mean / variance", np.allclose(m5, Db.mean(1)) and np.allclose(v5, Db.var(1)))

section("utils.validation.check_array")
fin = "ensure_all_finite" if has_param(check_array, "ensure_all_finite") else "force_all_finite"
report("check_array(float32, dtype='numeric') preserves float32; int64 preserved", check_array(np.ones((2, 2), np.float32)).dtype == np.float32 and check_array(np.ones((2, 2), np.int64)).dtype == np.int64)
report("check_array(object array of numbers, dtype='numeric') -> float64 ('dtype is preserved unless array.dtype is object')", check_array(np.array([[1, 2.5], [3, 4]], dtype=object)).dtype == np.float64)
report("check_array(int, dtype=[float64, float32]) -> first listed type; float32 kept", check_array(np.ones((2, 2), int), dtype=[np.float64, np.float32]).dtype == np.float64 and check_array(np.ones((2, 2), np.float32), dtype=[np.float64, np.float32]).dtype == np.float32)
Xnan = np.array([[1.0, np.nan], [2.0, 3.0]]); Xinf = np.array([[1.0, np.inf], [2.0, 3.0]])
report(f"check_array: NaN / inf raise ValueError by default ({fin}=True)", raises(lambda: check_array(Xnan)) == "ValueError" and raises(lambda: check_array(Xinf)) == "ValueError")
report(f"check_array({fin}='allow-nan'): NaN passes, inf still raises", raises(lambda: check_array(Xnan, **{fin: "allow-nan"})) is None and raises(lambda: check_array(Xinf, **{fin: "allow-nan"})) == "ValueError")
report(f"check_array({fin}=False): NaN and inf pass", raises(lambda: check_array(Xinf, **{fin: False})) is None and raises(lambda: check_array(Xnan, **{fin: False})) is None)
if has_param(check_array, "force_writeable"):
    ro = np.arange(6.0).reshape(2, 3); ro.setflags(write=False)
    out = check_array(ro, force_writeable=True)
    report("check_array(read-only, force_writeable=True): writeable result, input left read-only and unchanged", out.flags.writeable and not ro.flags.writeable and np.array_equal(out, ro))
    report("check_array(read-only) default keeps the read-only view (no copy forced)", not check_array(ro).flags.writeable)
report("check_array(1-D) raises ValueError ('Expected 2D array'); ensure_2d=False passes", raises(lambda: check_array(np.arange(3.0))) == "ValueError" and check_array(np.arange(3.0), ensure_2d=False).shape == (3,))
report("check_array(3-D) raises unless allow_nd=True", raises(lambda: check_array(np.ones((2, 2, 2)))) == "ValueError" and check_array(np.ones((2, 2, 2)), allow_nd=True).shape == (2, 2, 2))
report("check_array(0 samples) raises ValueError (ensure_min_samples=1); 0 features raises (ensure_min_features=1)", raises(lambda: check_array(np.empty((0, 3)))) == "ValueError" and raises(lambda: check_array(np.empty((3, 0)))) == "ValueError")
report("check_array(complex) raises ValueError ('Complex data not supported')", raises(lambda: check_array(np.array([[1 + 1j, 2]]))) == "ValueError")
report("check_array(sparse, accept_sparse=False) raises TypeError; accept_sparse='csr' converts csc -> csr", raises(lambda: check_array(sp.csc_matrix(np.eye(3)))) == "TypeError" and check_array(sp.csc_matrix(np.eye(3)), accept_sparse="csr").format == "csr")
report("check_array(order='F') returns Fortran-contiguous; copy=True returns a new buffer", check_array(np.ones((3, 3)), order="F").flags.f_contiguous and not np.shares_memory(check_array(Xn_, copy=True), Xn_))
if has_param(check_array, "ensure_non_negative"):
    report("check_array(ensure_non_negative=True) [1.6+] raises on a negative entry", raises(lambda: check_array(np.array([[1.0, -1.0]]), ensure_non_negative=True)) == "ValueError")
report("check_array(list of lists) -> float64 ndarray", check_array([[1, 2], [3, 4.5]]).dtype == np.float64)

section("utils.multiclass.type_of_target")
doc_ex = [([0.1, 0.6], "continuous"), ([1, -1, -1, 1], "binary"), (["a", "b", "a"], "binary"), ([1.0, 2.0], "binary"), ([1, 0, 2], "multiclass"),
          ([1.0, 0.0, 3.0], "multiclass"), (["a", "b", "c"], "multiclass"), (np.array([[1, 2], [3, 1]]), "multiclass-multioutput"), ([[1, 2]], "multilabel-indicator"),
          (np.array([[1.5, 2.0], [3.0, 1.6]]), "continuous-multioutput"), (np.array([[0, 1], [1, 1]]), "multilabel-indicator")]
for yv, exp in doc_ex:
    got = type_of_target(yv)
    report(f"type_of_target({yv if not isinstance(yv, np.ndarray) else yv.tolist()}) = '{exp}' (docstring example)", got == exp, f"(got {got!r})")
more = [([3, 3, 3], "binary", "<= 2 discrete values"), (np.array([[1], [2], [3]]), "multiclass", "column vector"), (np.array([[0.5], [1.5]]), "continuous", "column vector of floats"),
        (np.ones((2, 2, 2)), "unknown", "3d array"), (sp.csr_matrix(np.array([[0, 1], [1, 0]])), "multilabel-indicator", "sparse indicator"),
        (np.array([[0, 2], [2, 0]]), "multilabel-indicator", "2 unique values, >= 2 columns"),
        (np.array([[1.5, 2.5]]), "unknown", "1 x 2 floats: 'continuous-multioutput' needs both dimensions > 1, 'continuous' needs 1d/column"),
        (np.array([[1, 2, 3]]), "unknown", "1 x 3 ints: 'multiclass-multioutput' needs both dimensions > 1")]
for yv, exp, why in more:
    try: got = type_of_target(yv)
    except Exception as e_: got = type(e_).__name__
    report(f"type_of_target: {why} -> '{exp}'", got == exp, f"(got {got!r})")
try: got = type_of_target([[1, 2], [3]])
except Exception as e_: got = type(e_).__name__
report("type_of_target(sequence of sequences [[1,2],[3]]) -> 'unknown' (Returns: \"'unknown': ... such as a 3d array, sequence of sequences\")", got == "unknown", f"(got {got!r})")
try: got = type_of_target(np.array([object(), object()], dtype=object))
except Exception as e_: got = type(e_).__name__
report("type_of_target(array of non-sequence objects) -> 'unknown'", got == "unknown", f"(got {got!r})")

section("utils: graph / murmurhash3_32")
g1 = np.array([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
report("single_source_shortest_path_length docstring example 1 -> {0: 0, 1: 1, 2: 2}", single_source_shortest_path_length(g1, 0) == {0: 0, 1: 1, 2: 2})
report("single_source_shortest_path_length docstring example 2 (ones 6x6, source 2)", sorted(single_source_shortest_path_length(np.ones((6, 6)), 2).items()) == [(0, 1), (1, 1), (2, 0), (3, 1), (4, 1), (5, 1)])
Ag = (rs.rand(25, 25) < 0.09).astype(int); Ag = np.maximum(Ag, Ag.T); np.fill_diagonal(Ag, 0)
def bfs(A, s, cutoff=None):
    dist = {s: 0}; fr = [s]
    while fr:
        nxt = []
        for u in fr:
            for v in np.nonzero(A[u])[0].tolist():
                if v not in dist and (cutoff is None or dist[u] + 1 <= cutoff): dist[v] = dist[u] + 1; nxt.append(v)
        fr = nxt
    return dist
ok = all(single_source_shortest_path_length(sp.csr_matrix(Ag), s) == bfs(Ag, s) for s in range(25))
okc = all(single_source_shortest_path_length(Ag, s, cutoff=2) == bfs(Ag, s, 2) for s in range(25))
report("single_source_shortest_path_length on a random graph = plain-Python BFS hop counts (all sources)", ok)
report("single_source_shortest_path_length(cutoff=2): only paths of length <= cutoff", okc)
M32 = 0xFFFFFFFF
def rotl(x, r): return ((x << r) | (x >> (32 - r))) & M32
def mmh3_py(data, seed=0):
    c1, c2 = 0xcc9e2d51, 0x1b873593; h = seed & M32; n = len(data); nb = n // 4
    for i in range(nb):
        k = int.from_bytes(data[4 * i:4 * i + 4], "little"); k = (k * c1) & M32; k = rotl(k, 15); k = (k * c2) & M32
        h ^= k; h = rotl(h, 13); h = (h * 5 + 0xe6546b64) & M32
    tail = data[4 * nb:]; k = 0
    if len(tail) >= 3: k ^= tail[2] << 16
    if len(tail) >= 2: k ^= tail[1] << 8
    if len(tail) >= 1:
        k ^= tail[0]; k = (k * c1) & M32; k = rotl(k, 15); k = (k * c2) & M32; h ^= k
    h ^= n; h ^= h >> 16; h = (h * 0x85ebca6b) & M32; h ^= h >> 13; h = (h * 0xc2b2ae35) & M32; h ^= h >> 16
    return h
def signed(u): return u - (1 << 32) if u >= 1 << 31 else u
report("pure-Python MurmurHash3_x86_32 reproduces the published test vectors ('' seed 0 -> 0, '' seed 1 -> 0x514E28B7, 'hello' seed 0 -> 0x248BFA47)", mmh3_py(b"", 0) == 0 and mmh3_py(b"", 1) == 0x514E28B7 and mmh3_py(b"hello", 0) == 0x248BFA47)
keys = ["", "a", "ab", "abc", "abcd", "abcde", "hello", "The quick brown fox jumps over the lazy dog", "héllo wörld", "漢字"]
ok_s = all(murmurhash3_32(k_, seed=sd) == signed(mmh3_py(k_.encode("utf-8"), sd)) and murmurhash3_32(k_, seed=sd, positive=True) == mmh3_py(k_.encode("utf-8"), sd) for k_ in keys for sd in (0, 1, 42, 2 ** 31 - 1))
report("murmurhash3_32(str) = MurmurHash3_x86_32 of the UTF-8 bytes; positive=False -> signed int32, positive=True -> unsigned (seeds 0, 1, 42, 2^31-1)", ok_s)
ok_b = all(murmurhash3_32(k_.encode("utf-8"), seed=3) == signed(mmh3_py(k_.encode("utf-8"), 3)) for k_ in keys)
report("murmurhash3_32(bytes) = MurmurHash3_x86_32 of the bytes", ok_b)
ints = [0, 1, -1, 42, 2 ** 31 - 1, -2 ** 31]
ok_i = all(murmurhash3_32(np.int32(v), seed=5) == signed(mmh3_py(int(v & M32).to_bytes(4, "little"), 5)) for v in ints)
report("murmurhash3_32(np.int32 key) = hash of its 4 little-endian bytes", ok_i)
arr = np.array(ints, dtype=np.int32)
report("murmurhash3_32(int32 array, positive=True) = element-wise unsigned hashes", np.array_equal(murmurhash3_32(arr, seed=5, positive=True), [mmh3_py(int(v & M32).to_bytes(4, "little"), 5) for v in ints]))
