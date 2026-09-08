#!/usr/bin/env python3
"""Held-up check: exactTest()/exactTestDoubleTail() against a scipy enumeration of the
conditional test of Robinson & Smyth (2008, Biostatistics 9:321), and the accuracy of the
beta approximation that replaces the enumeration above big.count=900.

Reference (written from the paper): with n1, n2 libraries of equal size, group sums
S1 ~ NB(mean n1 mu, size n1/phi), S2 ~ NB(mean n2 mu, size n2/phi) are independent and
S = S1+S2 ~ NB(mean (n1+n2) mu, size (n1+n2)/phi); the conditional probability
P(S1 = x | S = s) = f1(x) f2(s-x) / f(s) does not depend on mu.
"doubletail" p-value = 2 * min(P(S1 <= s1 | s), P(S1 >= s1 | s)), capped at 1.
For phi = 0 the conditional law is Binomial(s, n1/(n1+n2)) and edgeR uses binomTest.

Run: python heldup_exact_test.py [--lib=<version>]
"""
import numpy as np
from scipy.stats import nbinom, binom, beta as beta_dist
from rrun import run_r, version_arg, edger_version

V = version_arg()
print("edgeR/limma:", edger_version(V))

def cond_p_doubletail(s1, s2, n1, n2, phi):
    s = s1 + s2
    if s == 0:
        return 1.0
    if phi <= 0:
        p = n1/(n1+n2)
        lo = binom.cdf(s1, s, p); hi = binom.sf(s1-1, s, p)
        return min(1.0, 2*min(lo, hi))
    x = np.arange(0, s+1)
    mu = s/(n1+n2)
    def nbpmf(k, n, mu_):
        size = n/phi; p = size/(size+mu_)
        return nbinom.pmf(k, size, p)
    top = nbpmf(x, n1, n1*mu)*nbpmf(s-x, n2, n2*mu)
    cond = top/top.sum()                        # exact normalisation of the conditional law
    lo = cond[:s1+1].sum(); hi = cond[s1:].sum()
    return min(1.0, 2*min(lo, hi))

rng = np.random.default_rng(3)
# --- part 1: exactTestDoubleTail on small/medium counts vs enumeration --------------
n1, n2 = 3, 2
G = 400
phi = rng.choice([0.05, 0.2, 0.8], G)
mu = np.exp(rng.uniform(np.log(1), np.log(300), G))
y1 = rng.negative_binomial(1/phi[:, None], 1/(1+phi[:, None]*mu[:, None]), (G, n1)).astype(float)
y2 = rng.negative_binomial(1/phi[:, None], 1/(1+phi[:, None]*mu[:, None]*rng.choice([1, 3], (G, 1))), (G, n2)).astype(float)
outs, _ = run_r("""
p <- exactTestDoubleTail(y1, y2, dispersion=as.numeric(phi))
write.csv(cbind(p), file.path(OUT,"p.csv"), row.names=FALSE)
p0 <- exactTestDoubleTail(y1, y2, dispersion=0)
write.csv(cbind(p0), file.path(OUT,"p0.csv"), row.names=FALSE)
""", V, {"y1": y1, "y2": y2, "phi": phi.reshape(1, -1)})
ref = np.array([cond_p_doubletail(int(y1[g].sum()), int(y2[g].sum()), n1, n2, phi[g]) for g in range(G)])
ref0 = np.array([cond_p_doubletail(int(y1[g].sum()), int(y2[g].sum()), n1, n2, 0.0) for g in range(G)])
small = (y1.sum(1) <= 900) | (y2.sum(1) <= 900)
print(f"part 1: {G} genes, n1={n1}, n2={n2}, group sums up to {int(max(y1.sum(1).max(), y2.sum(1).max()))}")
d = np.abs(outs['p'][small]-ref[small])
print(f"  NB doubletail p: max |edgeR - enumeration| over {small.sum()} genes below big.count = {d.max():.2e}")
print(f"  max relative |diff| on p < 0.05 genes = {np.max(np.abs(outs['p'][small]/ref[small]-1)[ref[small]<0.05]):.2e}")
s1 = y1.sum(1); s2 = y2.sum(1); mu1 = n1*(s1+s2)/(n1+n2)
atmean = (s1 == mu1)[small]
print(f"  genes with s1 exactly equal to its null expectation n1*s/(n1+n2): {atmean.sum()}; edgeR returns p=1 for them, "
      f"2*min(tails) gives min {ref[small][atmean].min() if atmean.any() else float('nan'):.3f}")
print(f"  max |diff| on the other genes: {d[~atmean].max():.2e}")
# edgeR doubles the tail on the side of s1 relative to its null mean (s1 < mu1: left tail); the
# port doubles the smaller tail. They differ only when the mean and the median of the skewed
# conditional law fall on different sides of s1, i.e. when both tails exceed 0.5 and p is ~1.
def tails(s1, s2, phi):
    s = s1 + s2; x = np.arange(0, s+1); mu_ = s/(n1+n2)
    size1, size2 = n1/phi, n2/phi
    top = nbinom.pmf(x, size1, size1/(size1+n1*mu_))*nbinom.pmf(s-x, size2, size2/(size2+n2*mu_))
    c = top/top.sum(); return c[:s1+1].sum(), c[s1:].sum()
tl = np.array([tails(int(y1[g].sum()), int(y2[g].sum()), phi[g]) for g in range(G)])[small]
edger_side_big = np.where((s1 < mu1)[small], tl[:, 0], tl[:, 1]) >= 0.5      # the tail edgeR doubles is >= 0.5 -> p = 1
print(f"  genes where the tail on s1's side of the null mean is >= 0.5 (edgeR doubles that tail and returns p = 1): {edger_side_big.sum()};"
      f" edgeR p on them: min {outs['p'][small][edger_side_big].min():.3f}; port (2 x smaller tail) min {ref[small][edger_side_big].min():.3f}")
rest = ~edger_side_big & ~atmean
print(f"  max |diff| on the remaining {rest.sum()} genes: {d[rest].max():.2e}")
print(f"  Poisson (dispersion=0) via binomTest vs binomial doubletail: max |diff| = {np.max(np.abs(outs['p0']-ref0)):.2e}"
      f"  (binomTest uses the small-probability rejection region, not doubled tails; see below)")
print(f"  ... of which {np.sum(np.abs(outs['p0']-ref0) > 1e-9)} genes differ by more than 1e-9")

# --- part 2: beta approximation above big.count vs enumeration ---------------------
print("\npart 2: beta approximation (used when both group sums > big.count=900) vs enumeration")
rows = []
for s1, s2, phi_ in [(1000, 1000, 0.05), (1000, 1300, 0.05), (1000, 1300, 0.2), (2000, 3000, 0.1), (5000, 5600, 0.02), (901, 1500, 0.5)]:
    o, _ = run_r(f"""
    p_big <- exactTestDoubleTail(matrix({s1}/3,1,3), matrix({s2}/2,1,2), dispersion={phi_}, big.count=900)
    p_enum <- exactTestDoubleTail(matrix({s1}/3,1,3), matrix({s2}/2,1,2), dispersion={phi_}, big.count=1e9)
    write.csv(cbind(p_big, p_enum), file.path(OUT,"pp.csv"), row.names=FALSE)
    """, V)
    ex = cond_p_doubletail(s1, s2, 3, 2, phi_)
    rows.append((s1, s2, phi_, o["pp"][0], o["pp"][1], ex))
print("  %6s %6s %5s | %12s %12s %12s" % ("s1", "s2", "phi", "beta approx", "edgeR enum", "scipy enum"))
for r in rows:
    print("  %6d %6d %5.2f | %12.4e %12.4e %12.4e" % r)

# --- part 3: exactTest() end to end with equal library sizes (no pseudo-counts) ------
print("\npart 3: exactTest(DGEList) with equal library sizes, dispersion given: p vs enumeration, logFC vs formula")
n1, n2 = 3, 3
G = 300
phi2 = 0.1
mu = np.exp(rng.uniform(np.log(2), np.log(200), G))
y = np.hstack([rng.negative_binomial(1/phi2, 1/(1+phi2*mu[:, None]), (G, n1)),
               rng.negative_binomial(1/phi2, 1/(1+phi2*mu[:, None]*2), (G, n2))]).astype(float)
L = 1e6
outs, _ = run_r(f"""
d <- DGEList(y, group=factor(c(rep("A",{n1}),rep("B",{n2}))), lib.size=rep({L},{n1+n2}))
et <- exactTest(d, dispersion={phi2})
write.csv(et$table[,c("logFC","PValue")], file.path(OUT,"tab.csv"), row.names=FALSE)
""", V, {"y": y})
ref = np.array([cond_p_doubletail(int(y[g, :n1].sum()), int(y[g, n1:].sum()), n1, n2, phi2) for g in range(G)])
tab = outs["tab"]
print(f"  p-values: max |edgeR - enumeration| = {np.max(np.abs(tab[:,1]-ref)):.2e}  (library sizes equal, so q2qnbinom is the identity)")
# logFC: one-group NB fits of y + prior.count (0.125 per library, scaled by lib size) with
# offset log(L + 2*prior); with equal library sizes the MLE of the mean is the plain mean.
pc = 0.125
lfc = np.log2((y[:, n1:].mean(1)+pc)/(L+2*pc)) - np.log2((y[:, :n1].mean(1)+pc)/(L+2*pc))
print(f"  logFC: max |edgeR - log2 of prior-augmented group means| = {np.max(np.abs(tab[:,0]-lfc)):.2e}")
