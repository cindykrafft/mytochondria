"""Held-up checks: the shipped scrublet package against the independent port
in reference.py on synthetic data with labelled doublets.

  A  helpers: sparse_var / sparse_zscore / sparse_multiply / tot_counts_norm
     vs dense numpy
  B  get_vscores + filter_genes vs the reference v-score fit and gating
  C  full pipeline (use_approx_neighbors=False): doublet-neighbour counts,
     scores, standard errors vs the reference; sparse vs dense input; int vs
     float32 input; random_state reproducibility; user-supplied total_counts
  D  closed forms: score formula == odds/(1+odds) form; SE == first-order
     error propagation by finite differences; se_q == Beta(nd+1, N-nd+1) sd;
     k and k_adj; detected/detectable/overall rates; threshold == skimage
  E  annoy (default use_approx_neighbors=True) vs exact neighbours

Run inside the venv with scrublet installed:  python heldup_reference_port.py
"""

from __future__ import annotations

import importlib.metadata as md
import io
import sys
import warnings
from contextlib import redirect_stdout

import numpy as np
import scipy.sparse as sp

warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import reference as R  # noqa: E402
from synth import make_counts, recall_precision  # noqa: E402

import scrublet as scr  # noqa: E402
from scrublet import helper_functions as H  # noqa: E402

print("scrublet", md.version("scrublet"), "file", scr.__file__)
for p in ("numpy", "scipy", "scikit-learn", "scikit-image", "annoy"):
    print(" ", p, md.version(p))

X, is_doublet, cell_type = make_counts()
n_obs, n_genes = X.shape
print(f"\nsynthetic data: {n_obs} cells x {n_genes} genes, {is_doublet.sum()} true heterotypic doublets, mean UMI {X.sum(1).mean():.0f}")


def quiet(fn, *a, **k):
    with redirect_stdout(io.StringIO()):
        return fn(*a, **k)


# ------------------------------------------------------------------ A helpers
print("\n[A] sparse helpers vs dense numpy")
Xd = X.toarray().astype(float)
Xn_ref = R.total_count_normalise(Xd, Xd.sum(1), Xd.sum(1).mean())
Xn = H.tot_counts_norm(X, total_counts=X.sum(1).A.ravel(), target_total=Xd.sum(1).mean())
print(f"  tot_counts_norm vs dense:            max|diff| = {np.abs(Xn.toarray() - Xn_ref).max():.3g}")
print(f"  sparse_var vs np.var(ddof=0):        max|diff| = {np.abs(H.sparse_var(Xn) - Xn_ref.var(0)).max():.3g}  (relative {np.abs(H.sparse_var(Xn) - Xn_ref.var(0)).max()/Xn_ref.var(0).max():.3g})")
sub = Xn[:, :200]
z_ref = (sub.toarray() - sub.toarray().mean(0)) / sub.toarray().std(0)
z = np.asarray(H.sparse_zscore(sub))
print(f"  sparse_zscore vs dense z-score:      max|diff| = {np.abs(z - z_ref).max():.3g}")
a = np.arange(1, sub.shape[0] + 1, dtype=float)
print(f"  sparse_multiply vs row scaling:      max|diff| = {np.abs(H.sparse_multiply(sub, a).toarray() - sub.toarray() * a[:, None]).max():.3g}")
E1 = sp.csc_matrix(X[:10]).copy()
E2, tot = H.subsample_counts(E1.copy(), 1.0, X[:10].sum(1).A.ravel())
print(f"  subsample_counts(rate=1) passthrough: counts unchanged {np.array_equal(E2.toarray(), E1.toarray())}, totals unchanged {np.array_equal(tot, X[:10].sum(1).A.ravel())}")

# ------------------------------------------------------------------ B v-scores
print("\n[B] get_vscores / filter_genes vs reference")
v_s, CVe, CVi, gix_s, mu_s, ff_s, a_s, b_s = H.get_vscores(Xn)
v_r, gix_r, mu_r, ff_r, a_r, b_r = R.vscores(Xn_ref)
print(f"  genes with mean>0: shipped {len(gix_s)}, reference {len(gix_r)}, identical index {np.array_equal(gix_s, gix_r)}")
print(f"  fitted b: shipped {float(np.ravel(b_s)[0]):.6g}  reference {float(np.ravel(b_r)[0]):.6g};  a: {float(np.ravel(a_s)[0]):.6g} vs {float(np.ravel(a_r)[0]):.6g}")
print(f"  v-scores: max|rel diff| = {np.abs(v_s - v_r).max() / v_r.max():.3g}")
g_s = H.filter_genes(Xn, min_vscore_pctl=85, min_counts=3, min_cells=3)
g_r = R.gene_filter(Xn_ref, 3, 3, 85)
print(f"  filter_genes: shipped keeps {len(g_s)}, reference keeps {len(g_r)}, identical {np.array_equal(g_s, g_r)}")
# the running quantile: p=0.1 is the 0.1th percentile (numpy convention), i.e. the bin minimum for bins with < 1000 genes
xq, yq = H.runningquantile(np.log(mu_s), np.log(ff_s / mu_s), 0.1, 50)
o = np.argsort(np.log(mu_s)); xs = np.log(mu_s)[o]; ys = np.log(ff_s / mu_s)[o]
dx = (xs[-1] - xs[0]) / 50
mins = [ys[(xs >= c - dx / 2) & (xs < c + dx / 2)].min() for c in xq if ((xs >= c - dx / 2) & (xs < c + dx / 2)).any()]
yq_nonempty = [y for y, c in zip(yq, xq) if ((xs >= c - dx / 2) & (xs < c + dx / 2)).any()]
print(f"  runningquantile(p=0.1) equals the per-bin minimum in {np.sum(np.isclose(mins, yq_nonempty))} of {len(mins)} non-empty bins (it is np.percentile(., 0.1), the 0.1th percentile)")

# ------------------------------------------------------------------ C pipeline
print("\n[C] full pipeline, exact neighbours, vs reference")
ref = R.run(X, seed=0)
s = scr.Scrublet(X, random_state=0)
scores, pred = quiet(s.scrub_doublets, use_approx_neighbors=False, verbose=False)
print(f"  gene filter: shipped {len(s._gene_filter)} genes, reference {len(ref['genes'])}, identical {np.array_equal(s._gene_filter, ref['genes'])}")
print(f"  doublet parents identical: {np.array_equal(s.doublet_parents_, ref['pairs'])}  (n_sim = {len(ref['pairs'])}, self-pairs i==j: {(ref['pairs'][:,0]==ref['pairs'][:,1]).sum()}, repeated ordered pairs: {len(ref['pairs']) - len({tuple(p) for p in ref['pairs']})})")
print(f"  k = {s.n_neighbors} (reference {ref['k']}), k_adj = {ref['k_adj']}")
nd_ship = np.r_[s.doublet_scores_obs_, s.doublet_scores_sim_]
d_obs = np.abs(s.doublet_scores_obs_ - ref["scores_obs"])
d_sim = np.abs(s.doublet_scores_sim_ - ref["scores_sim"])
print(f"  observed scores: max|diff| = {d_obs.max():.3g}, cells differing > 1e-9: {(d_obs > 1e-9).sum()} of {n_obs}")
print(f"  simulated scores: max|diff| = {d_sim.max():.3g}, differing > 1e-9: {(d_sim > 1e-9).sum()} of {len(d_sim)}")
print(f"  standard errors (obs): max|diff| = {np.abs(s.doublet_errors_obs_ - ref['se_obs']).max():.3g}")
# manifold agreement up to component sign
sgn = np.sign((s.manifold_obs_ * ref["manifold_obs"]).sum(0))
print(f"  PCA manifold (arpack vs full SVD, sign-aligned): max|diff| = {np.abs(s.manifold_obs_ - ref['manifold_obs'] * sgn).max():.3g}")
print(f"  threshold {s.threshold_:.4f}; detected {s.detected_doublet_rate_:.4f}; detectable {s.detectable_doublet_fraction_:.4f}; overall {s.overall_doublet_rate_:.4f}")
rec, prec, npred = recall_precision(pred, is_doublet)
print(f"  vs truth: {npred} called, recall {rec:.3f}, precision {prec:.3f}")

s2 = scr.Scrublet(X.toarray(), random_state=0)
scores2, pred2 = quiet(s2.scrub_doublets, use_approx_neighbors=False, verbose=False)
print(f"  dense input: scores identical {np.array_equal(scores, scores2)}, calls identical {np.array_equal(pred, pred2)}")
s3 = scr.Scrublet(sp.csr_matrix(X).astype(np.float32), random_state=0)
scores3, pred3 = quiet(s3.scrub_doublets, use_approx_neighbors=False, verbose=False)
print(f"  CSR float32 input: max|score diff| = {np.abs(scores - scores3).max():.3g}, calls identical {np.array_equal(pred, pred3)}")
s4 = scr.Scrublet(X, random_state=0)
scores4, pred4 = quiet(s4.scrub_doublets, use_approx_neighbors=False, verbose=False)
print(f"  rerun same random_state: scores identical {np.array_equal(scores, scores4)}")
s5 = scr.Scrublet(X, random_state=1)
scores5, pred5 = quiet(s5.scrub_doublets, use_approx_neighbors=False, verbose=False)
print(f"  random_state=1: parents identical to seed 0: {np.array_equal(s5.doublet_parents_, s.doublet_parents_)}; max|score diff| = {np.abs(scores - scores5).max():.3g}; calls agree on {(pred == pred5).mean():.3f} of cells")
s6 = scr.Scrublet(X, total_counts=X.sum(1).A.ravel().astype(float), random_state=0)
scores6, _ = quiet(s6.scrub_doublets, use_approx_neighbors=False, verbose=False)
print(f"  user total_counts == row sums: scores identical {np.array_equal(scores, scores6)}")
print(f"  simulate_doublets reseeds the *global* numpy RNG: np.random.rand() after a run with random_state=0 is {np.random.rand():.6f} both times: ", end="")
quiet(scr.Scrublet(X[:200], random_state=0).simulate_doublets); r1 = np.random.rand()
quiet(scr.Scrublet(X[:200], random_state=0).simulate_doublets); r2 = np.random.rand()
print(r1 == r2)

# ------------------------------------------------------------------ D closed forms
print("\n[D] closed forms")
nd = np.arange(0, ref["k_adj"] + 1, dtype=float)
N, rho, r = float(ref["k_adj"]), 0.1, 2.0
print(f"  score == odds/(1+odds) with odds = q*rho/(r*(1-rho)*(1-q)): max|diff| = {np.abs(R.score(nd, N, rho, r) - R.score_odds_form(nd, N, rho, r)).max():.3g}")
q_pure = r / (rho + r)  # fraction simulated in a pure doublet state (f_S = 0)
print(f"  score at q = r/(rho+r) (pure doublet state, no singlets nearby): {rho * q_pure / r / (1 - rho - q_pure * (1 - rho - rho / r)):.4f} = 1/(2-rho) = {1/(2-rho):.4f}; score reaches 1 only at q = 1")
# finite-difference error propagation
def ld(q, rho_):
    return q * rho_ / r / (1 - rho_ - q * (1 - rho_ - rho_ / r))
q = (nd + 1) / (N + 2); h = 1e-6
dq = (ld(q + h, rho) - ld(q - h, rho)) / (2 * h); drho = (ld(q, rho + h) - ld(q, rho - h)) / (2 * h)
se_fd = np.sqrt((dq * np.sqrt(q * (1 - q) / (N + 3))) ** 2 + (drho * 0.02) ** 2)
print(f"  SE == sqrt((dL/dq se_q)^2 + (dL/drho se_rho)^2) by finite differences: max|rel diff| = {(np.abs(R.standard_error(nd, N, rho, r, 0.02) - se_fd) / se_fd).max():.3g}")
from scipy.stats import beta
sd_beta = beta(nd + 1, N - nd + 1).std()
print(f"  se_q == sd of Beta(nd+1, N-nd+1): max|diff| = {np.abs(np.sqrt(q * (1 - q) / (N + 3)) - sd_beta).max():.3g}")
print(f"  k = round(0.5*sqrt(n_obs)) = {R.k_default(n_obs)} (shipped {s.n_neighbors}); k_adj = round(k*(1+r)) = {R.k_adjusted(R.k_default(n_obs), n_obs, len(ref['pairs']))}")
from skimage.filters import threshold_minimum
c = R.call(s.doublet_scores_obs_, s.doublet_scores_sim_, s.threshold_)
print(f"  threshold == skimage.threshold_minimum(sim scores): {s.threshold_ == threshold_minimum(s.doublet_scores_sim_)}")
print(f"  rates: detected {c['detected_doublet_rate']:.6f} vs {s.detected_doublet_rate_:.6f}; detectable {c['detectable_doublet_fraction']:.6f} vs {s.detectable_doublet_fraction_:.6f}; overall {c['overall_doublet_rate']:.6f} vs {s.overall_doublet_rate_:.6f}")
print(f"  z_scores == (score - threshold)/se: {np.allclose(s.z_scores_, (s.doublet_scores_obs_ - s.threshold_) / s.doublet_errors_obs_)}")
# fallback when no minimum exists
s_uni = scr.Scrublet(X[:200], random_state=0)
s_uni.doublet_scores_obs_ = np.full(200, 0.05); s_uni.doublet_errors_obs_ = np.full(200, 0.01)
s_uni.doublet_scores_sim_ = np.full(400, 0.05)
out = quiet(s_uni.call_doublets, verbose=True)
print(f"  call_doublets with unimodal (constant) simulated scores: returns {out}, predicted_doublets_ = {s_uni.predicted_doublets_}, threshold_ set: {hasattr(s_uni, 'threshold_')}")

# ------------------------------------------------------------------ E annoy
print("\n[E] approximate (annoy, default) vs exact neighbours")
s7 = scr.Scrublet(X, random_state=0)
scores7, pred7 = quiet(s7.scrub_doublets, use_approx_neighbors=True, verbose=False)
print(f"  max|score diff| = {np.abs(scores7 - scores).max():.3g}; median |diff| = {np.median(np.abs(scores7 - scores)):.3g}; calls agree on {(pred7 == pred).mean():.4f} of cells; threshold {s7.threshold_:.4f} vs {s.threshold_:.4f}")
rec7, prec7, n7 = recall_precision(pred7, is_doublet)
print(f"  annoy vs truth: {n7} called, recall {rec7:.3f}, precision {prec7:.3f}   (exact: {npred}, {rec:.3f}, {prec:.3f})")
s8 = scr.Scrublet(X, random_state=0)
scores8, _ = quiet(s8.scrub_doublets, use_approx_neighbors=True, verbose=False)
print(f"  annoy rerun with the same random_state: identical scores {np.array_equal(scores7, scores8)}")
