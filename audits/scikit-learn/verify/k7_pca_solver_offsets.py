#!/usr/bin/env python
"""PCA solvers on float64 data whose features carry a large common offset
(timestamps, genomic coordinates, raw instrument values): explained variance,
ratios and the projection of every solver against the exact centred
eigendecomposition, for a small (400 x 2) and a tall (20000 x 5) matrix (the
latter selects the covariance_eigh solver under svd_solver='auto' in 1.5+)."""
import sys, math, warnings
sys.path.insert(0, ".")
from _synth import *
from sklearn.decomposition import PCA
banner(); warnings.filterwarnings("ignore"); rs = np.random.RandomState(6)
solvers = ["auto", "full", "arpack", "randomized"] + (["covariance_eigh"] if sklearn.__version__ >= "1.5" else [])
for n, d in ((400, 2), (20000, 5)):
    L = rs.randn(d, d); base = rs.randn(n, d) @ L
    Xc = base - base.mean(0); ev = np.linalg.eigvalsh(Xc.T @ Xc / (n - 1))[::-1]
    Pfull = PCA(n_components=d - 1, svd_solver="full").fit(base); Tfull = Pfull.transform(base)
    for off in (0.0, 1e4, 1e6, 1e7, 1e8):
        X = base + off
        for sv in solvers:
            try:
                p = PCA(n_components=d - 1, svd_solver=sv, random_state=0).fit(X)
            except Exception as e:
                print(f"   n={n} d={d} offset {off:.0e} solver {sv}: {type(e).__name__}: {str(e)[:80]}"); continue
            chosen = getattr(p, "_fit_svd_solver", sv)
            dev = np.max(np.abs(p.explained_variance_ / ev[:d - 1] - 1)); rdev = np.max(np.abs(p.explained_variance_ratio_ / (ev[:d - 1] / ev.sum()) - 1))
            T = p.transform(X); tdev = min(np.abs(T[:, 0] * s - Tfull[:, 0]).max() for s in (1, -1)) / np.abs(Tfull[:, 0]).max()
            flag = "" if dev < 1e-6 else "   <-- "
            print(f"   n={n} d={d} offset {off:.0e} solver {sv:15s} (-> {chosen:15s}): explained_variance_ rel dev {dev:.1e}, ratio rel dev {rdev:.1e}, PC1 scores rel dev {tdev:.1e}{flag}")
            report(f"PCA n={n} d={d} offset {off:.0e} solver='{sv}': explained_variance_ within 1e-6 relative of exact", dev < 1e-6)
