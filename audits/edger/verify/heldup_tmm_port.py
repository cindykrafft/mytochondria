#!/usr/bin/env python3
"""Held-up check: normLibSizes()/calcNormFactors() against independent numpy ports of
TMM (Robinson & Oshlack 2010, Genome Biology 11:R25), RLE (Anders & Huber 2010) and
upper-quartile (Bullard et al. 2010) normalisation, written from the papers:

TMM for library k against reference r, over genes with positive counts in both:
    M_g = log2((y_gk/N_k)/(y_gr/N_r)),  A_g = 0.5 log2((y_gk/N_k)(y_gr/N_r))
    trim the 30 % most extreme M (both tails) and the 5 % most extreme A,
    TMM = sum(w_g M_g)/sum(w_g), w_g = 1/v_g,
    v_g = (N_k - y_gk)/(N_k y_gk) + (N_r - y_gr)/(N_r y_gr)   (delta-method variance)
    factor = 2^TMM;   reference = library whose upper quartile (of counts / N) is
    closest to the mean upper quartile;   factors scaled to geometric mean 1.
The trimming in edgeR is by rank with ties.method="average" and keeps ranks in
[floor(n*trim)+1, n-floor(n*trim)]; the port does the same on sorted order and the
tie question is checked separately (no ties in the continuous M/A of random NB data).

Run: python heldup_tmm_port.py [--lib=<version>]
"""
import numpy as np
from scipy.stats import rankdata
from rrun import run_r, version_arg, edger_version

V = version_arg()
print("edgeR/limma:", edger_version(V))
TIES = "average"

def uq_factors(y, N, p=0.75):
    return np.array([np.quantile(y[:, j], p) for j in range(y.shape[1])]) / N   # R type 7 == numpy default

def tmm_pair(obs, ref, No, Nr, logratioTrim=0.3, sumTrim=0.05, weighting=True):
    fin = (obs > 0) & (ref > 0)
    obs, ref = obs[fin], ref[fin]
    M = np.log2((obs/No)/(ref/Nr))
    # same floating-point order as the paper's definition and edgeR: last-bit ties in A decide
    # tie blocks at the 5 % trim boundary, so 0.5*log2(product) would not reproduce them
    A = (np.log2(obs/No) + np.log2(ref/Nr))/2
    v = (No-obs)/No/obs + (Nr-ref)/Nr/ref
    if np.max(np.abs(M)) < 1e-6:
        return 1.0
    n = len(M)
    loM = int(np.floor(n*logratioTrim)); loA = int(np.floor(n*sumTrim))
    if TIES == "average":
        # R's rank(ties.method="average"): a tie block straddling the trim boundary is kept or
        # dropped as a whole, so the trimmed fraction is not exactly 30 % / 5 % when there are ties
        rM = rankdata(M) - 1; rA = rankdata(A) - 1
    else:
        rM = np.argsort(np.argsort(M, kind="stable"), kind="stable")      # 0-based ranks, ties in order
        rA = np.argsort(np.argsort(A, kind="stable"), kind="stable")
    keep = (rM >= loM) & (rM <= n-1-loM) & (rA >= loA) & (rA <= n-1-loA)
    if weighting:
        f = np.sum(M[keep]/v[keep]) / np.sum(1/v[keep])
    else:
        f = np.mean(M[keep])
    return 2.0**f

def tmm_factors(y, N, refColumn=None, **kw):
    y = y[(y > 0).any(1)]
    if refColumn is None:
        f75 = uq_factors(y, N)
        refColumn = int(np.argmin(np.abs(f75 - f75.mean())))
    f = np.array([tmm_pair(y[:, i], y[:, refColumn], N[i], N[refColumn], **kw) for i in range(y.shape[1])])
    return f/np.exp(np.mean(np.log(f))), refColumn

def rle_factors(y, N):
    y = y[(y > 0).any(1)]
    with np.errstate(divide="ignore"):
        gm = np.exp(np.mean(np.log(y), axis=1))
    ok = gm > 0
    f = np.array([np.median(y[ok, j]/gm[ok]) for j in range(y.shape[1])])/N
    return f/np.exp(np.mean(np.log(f)))

def uq_norm(y, N, p=0.75):
    y = y[(y > 0).any(1)]
    f = uq_factors(y, N, p)
    return f/np.exp(np.mean(np.log(f)))

rng = np.random.default_rng(7)
worst = {"TMM": 0, "TMM-unweighted": 0, "TMM-refColumn": 0, "RLE": 0, "upperquartile": 0, "TMMwsp==TMM(no zeros, same ref)": 0}
worst_ordered = 0
refs_agree = 0
for rep in range(8):
    G, n = 4000, rng.integers(3, 9)
    N = rng.uniform(0.5e6, 5e6, n)
    base = np.exp(rng.normal(3, 1.5, G))
    fc = np.ones((G, n))
    de = rng.random(G) < 0.15                       # 15 % DE genes, mostly up in half the samples -> composition bias
    fc[de, : n//2] = np.exp(rng.normal(1.0, 0.5, (de.sum(), n//2)))
    mu = base[:, None]*fc*N[None, :]/1e6
    y = rng.negative_binomial(5, 5/(5+mu)).astype(float)
    y[rng.random((G, n)) < 0.05] = 0                # some exact zeros
    if rep >= 4:
        y = np.round(y*rng.uniform(1, 1.5, (G, n)))  # break ties: no two genes share (obs, ref) pairs
    inputs = {"y": y, "N": N.reshape(1, -1)}
    outs, _ = run_r("""
    N <- as.numeric(N)
    f <- normLibSizes(y, lib.size=N, method="TMM")
    write.csv(cbind(f), file.path(OUT,"tmm.csv"), row.names=FALSE)
    write.csv(cbind(normLibSizes(y, lib.size=N, method="TMM", doWeighting=FALSE)), file.path(OUT,"tmmu.csv"), row.names=FALSE)
    write.csv(cbind(normLibSizes(y, lib.size=N, method="TMM", refColumn=2)), file.path(OUT,"tmm2.csv"), row.names=FALSE)
    write.csv(cbind(normLibSizes(y, lib.size=N, method="RLE")), file.path(OUT,"rle.csv"), row.names=FALSE)
    write.csv(cbind(normLibSizes(y, lib.size=N, method="upperquartile")), file.path(OUT,"uq.csv"), row.names=FALSE)
    ypos <- y[rowSums(y==0)==0,]
    write.csv(cbind(normLibSizes(ypos, lib.size=N, method="TMM", refColumn=1), normLibSizes(ypos, lib.size=N, method="TMMwsp", refColumn=1)), file.path(OUT,"wsp.csv"), row.names=FALSE)
    """ if V != "3.36.0" else """
    N <- as.numeric(N)
    f <- calcNormFactors(y, lib.size=N, method="TMM")
    write.csv(cbind(f), file.path(OUT,"tmm.csv"), row.names=FALSE)
    write.csv(cbind(calcNormFactors(y, lib.size=N, method="TMM", doWeighting=FALSE)), file.path(OUT,"tmmu.csv"), row.names=FALSE)
    write.csv(cbind(calcNormFactors(y, lib.size=N, method="TMM", refColumn=2)), file.path(OUT,"tmm2.csv"), row.names=FALSE)
    write.csv(cbind(calcNormFactors(y, lib.size=N, method="RLE")), file.path(OUT,"rle.csv"), row.names=FALSE)
    write.csv(cbind(calcNormFactors(y, lib.size=N, method="upperquartile")), file.path(OUT,"uq.csv"), row.names=FALSE)
    ypos <- y[rowSums(y==0)==0,]
    write.csv(cbind(calcNormFactors(ypos, lib.size=N, method="TMM", refColumn=1), calcNormFactors(ypos, lib.size=N, method="TMMwsp", refColumn=1)), file.path(OUT,"wsp.csv"), row.names=FALSE)
    """, V, inputs)
    p_tmm, ref = tmm_factors(y, N)
    p_tmmu, _ = tmm_factors(y, N, weighting=False)
    p_tmm2, _ = tmm_factors(y, N, refColumn=1)
    TIES = "ordered"; p_ord, _ = tmm_factors(y, N); TIES = "average"
    worst_ordered = max(worst_ordered, np.max(np.abs(outs["tmm"]/p_ord - 1)))
    nties = G - len(np.unique(np.round(np.log2((y[:, 0]+0.5)/(y[:, ref]+0.5)), 12)))
    print(f"rep {rep}: n={n}, tie blocks in M (column 1 vs ref): {nties:5d}   edgeR vs port(average ranks) {np.max(np.abs(outs['tmm']/p_tmm-1)):.1e}   vs port(ordered ranks) {np.max(np.abs(outs['tmm']/p_ord-1)):.1e}")
    worst["TMM"] = max(worst["TMM"], np.max(np.abs(outs["tmm"]/p_tmm - 1)))
    worst["TMM-unweighted"] = max(worst["TMM-unweighted"], np.max(np.abs(outs["tmmu"]/p_tmmu - 1)))
    worst["TMM-refColumn"] = max(worst["TMM-refColumn"], np.max(np.abs(outs["tmm2"]/p_tmm2 - 1)))
    worst["RLE"] = max(worst["RLE"], np.max(np.abs(outs["rle"]/rle_factors(y, N) - 1)))
    worst["upperquartile"] = max(worst["upperquartile"], np.max(np.abs(outs["uq"]/uq_norm(y, N) - 1)))
    w = outs["wsp"]
    worst["TMMwsp==TMM(no zeros, same ref)"] = max(worst["TMMwsp==TMM(no zeros, same ref)"], np.max(np.abs(w[:, 1]/w[:, 0] - 1)))
    if rep == 0:
        print(f"rep 0: TMM factors edgeR {np.round(outs['tmm'],5)} port {np.round(p_tmm,5)} (port reference column {ref+1})")
print("\nmax relative difference edgeR vs port over 8 random datasets (3-8 samples, 4000 genes, 15 % DE, 5 % zeros; reps 4-7 tie-free):")
for k, v in worst.items():
    print(f"  {k:36s} {v:.2e}")
print(f"  {'TMM vs port with ordered ranks':36s} {worst_ordered:.2e}   (the tie-block effect of rank(ties='average') at the trim boundary)")
