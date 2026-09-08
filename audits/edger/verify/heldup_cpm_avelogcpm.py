#!/usr/bin/env python3
"""Held-up check: cpm(log=TRUE), rpkm(), aveLogCPM() and addPriorCount() against ports of
their documented definitions (cpm.Rd, aveLogCPM.Rd, addPriorCount.Rd):

  prior count per library:  p_j = prior.count * L_j / mean_j(L_j)
  log-CPM:                  log2((y_gj + p_j) / (L_j + 2 p_j) * 1e6)
  RPKM:                     CPM / (length/1000);  log2-RPKM = log2-CPM - log2(length/1000)
  aveLogCPM:                one-group NB GLM fitted to y_g + p_j with offsets log(L_j + 2 p_j)
                            and dispersion 0.05 (default): the MLE beta solves
                            sum_j (y_j - mu_j)/(1 + phi mu_j) = 0, mu_j = exp(beta + o_j);
                            AveLogCPM = (beta + log 1e6)/log 2.

Run: python heldup_cpm_avelogcpm.py [--lib=<version>]
"""
import numpy as np
from scipy.optimize import brentq
from rrun import run_r, version_arg, edger_version

V = version_arg()
print("edgeR/limma:", edger_version(V))
rng = np.random.default_rng(5)
G, n = 3000, 7
L = rng.uniform(3e5, 4e7, n)
nf = np.exp(rng.normal(0, 0.2, n)); nf /= np.exp(np.mean(np.log(nf)))
mu = np.exp(rng.normal(2, 2.5, G))
y = rng.negative_binomial(4, 4/(4+mu[:, None]*L[None, :]/1e6)).astype(float)
y[rng.random((G, n)) < 0.15] = 0
length = rng.integers(200, 20000, G).astype(float)
outs, _ = run_r("""
L <- as.numeric(L); nf <- as.numeric(nf); len <- as.numeric(len)
d <- DGEList(y, lib.size=L, norm.factors=nf, genes=data.frame(Length=len))
write.csv(cpm(d, log=TRUE), file.path(OUT,"lcpm.csv"), row.names=FALSE)
write.csv(cpm(d, log=TRUE, prior.count=0.5), file.path(OUT,"lcpm05.csv"), row.names=FALSE)
write.csv(cpm(d, normalized.lib.sizes=FALSE), file.path(OUT,"cpm_raw.csv"), row.names=FALSE)
write.csv(rpkm(d, log=TRUE), file.path(OUT,"lrpkm.csv"), row.names=FALSE)
write.csv(rpkm(d), file.path(OUT,"rpkm.csv"), row.names=FALSE)
write.csv(cbind(aveLogCPM(d)), file.path(OUT,"ave.csv"), row.names=FALSE)
write.csv(cbind(aveLogCPM(d, dispersion=0.3, prior.count=1)), file.path(OUT,"ave2.csv"), row.names=FALSE)
write.csv(cbind(aveLogCPM(d, dispersion=0)), file.path(OUT,"ave0.csv"), row.names=FALSE)
""", V, {"y": y, "L": L.reshape(1, -1), "nf": nf.reshape(1, -1), "len": length.reshape(1, -1)})
Ln = L*nf
def logcpm(y, Ln, pc):
    p = pc*Ln/Ln.mean()
    return np.log2((y + p)/(Ln + 2*p)*1e6)
print(f"log2-CPM (prior 2)   max |edgeR - formula| = {np.max(np.abs(outs['lcpm'] - logcpm(y, Ln, 2))):.2e}")
print(f"log2-CPM (prior 0.5) max |edgeR - formula| = {np.max(np.abs(outs['lcpm05'] - logcpm(y, Ln, 0.5))):.2e}")
print(f"CPM, normalized.lib.sizes=FALSE: max rel err vs y/L*1e6 = {np.max(np.abs(outs['cpm_raw']/(y/L*1e6) - 1)[y > 0]):.2e}")
print(f"RPKM      max rel err vs CPM/(len/1000)       = {np.max(np.abs(outs['rpkm']/(y/Ln*1e6/(length[:, None]/1000)) - 1)[y > 0]):.2e}")
print(f"log2-RPKM max |edgeR - (log2CPM - log2(len/1000))| = {np.max(np.abs(outs['lrpkm'] - (logcpm(y, Ln, 2) - np.log2(length[:, None]/1000)))):.2e}")

def ave_port(y, Ln, pc, phi):
    p = pc*Ln/Ln.mean()
    o = np.log(Ln + 2*p)
    out = np.empty(len(y))
    for g in range(len(y)):
        yy = y[g] + p
        f = lambda b: np.sum((yy - np.exp(b+o))/(1 + phi*np.exp(b+o)))
        out[g] = brentq(f, -60, 30, xtol=1e-13)
    return (out + np.log(1e6))/np.log(2)
for name, pc, phi in [("ave", 2, 0.05), ("ave2", 1, 0.3), ("ave0", 2, 0.0)]:
    ref = ave_port(y, Ln, pc, phi)
    print(f"aveLogCPM(prior.count={pc}, dispersion={phi}): max |edgeR - one-group NB MLE port| = {np.max(np.abs(outs[name] - ref)):.2e}   (range {ref.min():.2f}..{ref.max():.2f})")
