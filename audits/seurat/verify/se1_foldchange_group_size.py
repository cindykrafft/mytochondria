#!/usr/bin/env python3
"""SE1: Seurat v5 avg_log2FC depends on group size (pseudocount 1/n per group).

Faithful ports of the three FoldChange mean functions Seurat has shipped,
applied to LogNormalize'd data (x = log1p(counts / libsize * 1e4)):

  v3  (<= 3.2.3) : ln  ( mean(expm1(x)) + 1 )            avg_logFC,  threshold 0.25
  v4  (4.0-4.4)  : log2( mean(expm1(x)) + 1 )            avg_log2FC, threshold 0.25
  v5  (>= 5.0.0) : log2( (sum(expm1(x)) + 1) / n_group ) avg_log2FC, threshold 0.1
                   R/differential_expression.R (main @ 084d9e4) lines 810-820,
                   1073-1080, 1112-1130; commit 69b054b7 (2023-10-18).

v5's pseudocount is therefore 1/n_1 for group 1 and 1/n_2 for group 2, so for a
gene with the SAME mean mu in both groups the reported fold change is

      bias(mu, n1, n2) = log2( (mu + 1/n1) / (mu + 1/n2) )   (exact, part A)

which is positive whenever n1 < n2 -- i.e. in FindAllMarkers, where ident.1 is one
cluster and ident.2 is every other cell.  Parts B-C measure what that does to a
FindMarkers-style marker table on simulated data with known truth, using the same
filters as FindMarkers.default (min.pct >= 0.01 on rounded pct, |logFC| >=
threshold, Wilcoxon asymptotic with continuity + tie correction, Bonferroni over
all genes).

No claim is made about p-values: the test statistic never sees the fold change.
The finding is about the avg_log2FC column, which papers threshold, rank and plot.
"""
import numpy as np
from scipy import stats

rng = np.random.default_rng(20260902)

def lognorm(counts):
    lib = counts.sum(axis=0, keepdims=True)
    return np.log1p(counts / lib * 1e4)

def fc_v3(x1, x2):
    return np.log(np.expm1(x1).mean(1) + 1) - np.log(np.expm1(x2).mean(1) + 1)

def fc_v4(x1, x2):
    return np.log2(np.expm1(x1).mean(1) + 1) - np.log2(np.expm1(x2).mean(1) + 1)

def fc_v5(x1, x2, pc=1.0):
    return (np.log2((np.expm1(x1).sum(1) + pc) / x1.shape[1])
            - np.log2((np.expm1(x2).sum(1) + pc) / x2.shape[1]))

def fc_ideal(x1, x2, eps=1e-9):
    """Reference: ratio of group means of expm1(x) with a symmetric, negligible pseudocount."""
    return np.log2(np.expm1(x1).mean(1) + eps) - np.log2(np.expm1(x2).mean(1) + eps)

def pct(x):
    return np.round((x > 0).mean(1), 3)          # FoldChange.default rounds to 3 digits

def wilcox_p(x1, x2):
    p = np.ones(x1.shape[0])
    for g in range(x1.shape[0]):
        a, b = x1[g], x2[g]
        if a.max() == b.max() == 0:              # all-zero: presto reports 1
            continue
        p[g] = stats.mannwhitneyu(a, b, alternative="two-sided",
                                  method="asymptotic", use_continuity=True).pvalue
    return p

# ---------------------------------------------------------------- Part A: closed form
print("PART A  exact bias for a gene with identical mean mu in both groups, v5 formula")
print("        bias = log2((mu + 1/n1)/(mu + 1/n2)); v3/v4 bias is 0 by construction")
print("%8s %8s | %s" % ("n1", "n2", "  ".join("mu=%-5g" % m for m in (0.01, 0.03, 0.1, 0.3, 1.0, 3.0))))
for n1, n2 in ((50, 5000), (200, 5000), (200, 20000), (1000, 20000), (5000, 5000)):
    row = [np.log2((m + 1/n1) / (m + 1/n2)) for m in (0.01, 0.03, 0.1, 0.3, 1.0, 3.0)]
    print("%8d %8d | %s" % (n1, n2, "  ".join("%7.3f" % v for v in row)))
print("        Seurat v5 default logfc.threshold = 0.1; common paper cutoffs 0.25, 0.5, 1.")
print()

# ---------------------------------------------------------------- simulation helpers
def simulate(n1, n2, G=5000, de_frac=0.10, seed=1):
    """NB counts (theta = 2), 10x-like: library sizes lognormal around 5,000 UMIs, gene
    proportions lognormal so that the median normalized mean (x 1e4 scale) is ~0.05 and
    the 16-84% range is ~0.007-0.4. Cluster of n1 cells vs rest of n2 cells. de_frac of
    genes get a true log2 fold change in {-2,-1,-0.5,0.5,1,2} in the cluster."""
    r = np.random.default_rng(seed)
    base = np.exp(r.normal(-5.0, 2.0, G))
    prop = base / base.sum()
    lib1 = np.exp(r.normal(0, 0.35, n1)) * 5000
    lib2 = np.exp(r.normal(0, 0.35, n2)) * 5000
    true = np.zeros(G)
    de = r.choice(G, int(G * de_frac), replace=False)
    true[de] = r.choice([-2, -1, -0.5, 0.5, 1, 2], de.size)
    theta = 2.0
    mu1 = np.outer(prop * 2.0 ** true, lib1)
    mu2 = np.outer(prop, lib2)
    c1 = r.negative_binomial(theta, theta / (theta + mu1))
    c2 = r.negative_binomial(theta, theta / (theta + mu2))
    return c1, c2, true

def findmarkers_table(x1, x2, fc, thresh, min_pct=0.01, G=None):
    p1, p2 = pct(x1), pct(x2)
    keep = (np.maximum(p1, p2) >= min_pct) & (np.abs(fc) >= thresh)
    return keep, p1, p2

# ---------------------------------------------------------------- Part B: null genes
print("PART B  simulated cluster (n1) vs rest (n2), NB counts, 5000 genes, 10% truly DE.")
print("        B1: NULL genes passing FindMarkers' prefilter (min.pct >= 0.01 and |logFC| >= threshold)")
print("%6s %6s | %-4s %8s %8s %8s %8s %8s %8s" % ("n1", "n2", "ver", "n_pass", "frac>0", "mean_FC", "FC>0.25", "FC<-.25", "FC>0.5"))
sims = {}
for n1, n2 in ((50, 4950), (100, 4900), (300, 4700), (1000, 4000), (2500, 2500)):
    c1, c2, true = simulate(n1, n2, seed=n1)
    X = lognorm(np.hstack([c1, c2])); x1, x2 = X[:, :n1], X[:, n1:]
    sims[(n1, n2)] = (x1, x2, true)
    null = true == 0
    for ver, f, th in (("v4", fc_v4, 0.25), ("v5", fc_v5, 0.1)):
        fc = f(x1, x2)
        keep, p1, p2 = findmarkers_table(x1, x2, fc, th)
        k = keep & null
        fcn = fc[k]
        nan = float("nan")
        print("%6d %6d | %-4s %8d %8.3f %8.3f %8.3f %8.3f %8.3f" % (
            n1, n2, ver, k.sum(), (fcn > 0).mean() if k.sum() else nan,
            fcn.mean() if k.sum() else nan, (fcn > 0.25).mean() if k.sum() else nan,
            (fcn < -0.25).mean() if k.sum() else nan, (fcn > 0.5).mean() if k.sum() else nan))
print()
print("        B2: ALL null genes passing min.pct, binned by true normalized mean mu; v5 formula.")
print("            mean reported FC vs the exact pseudocount bias log2((mu+1/n1)/(mu+1/n2)) at the bin's")
print("            mean mu; and the share of null genes reported beyond +0.25 / -0.25 (v4 in brackets)")
print("%6s %6s | %-14s %6s %9s %9s %14s %14s" % ("n1", "n2", "mu bin", "n", "mean_v5", "exact", ">+0.25 v5[v4]", "<-0.25 v5[v4]"))
for (n1, n2), (x1, x2, true) in sims.items():
    if n1 > 1000: continue
    null = true == 0
    mu = np.expm1(x2).mean(1)                       # rest-group mean = null gene's true mu (x1e4 scale)
    p1, p2 = pct(x1), pct(x2)
    ok = null & (np.maximum(p1, p2) >= 0.01)
    fc5 = fc_v5(x1, x2); fc4 = fc_v4(x1, x2)
    for lo, hi in ((0.005, 0.02), (0.02, 0.05), (0.05, 0.15), (0.15, 0.5), (0.5, 2), (2, 1e9)):
        b = ok & (mu >= lo) & (mu < hi)
        if b.sum() < 20: continue
        m = mu[b].mean()
        print("%6d %6d | [%6.3f,%6.3f) %6d %9.3f %9.3f %7.3f[%5.3f] %7.3f[%5.3f]" % (
            n1, n2, lo, min(hi, 99), b.sum(), fc5[b].mean(), np.log2((m + 1/n1) / (m + 1/n2)),
            (fc5[b] > 0.25).mean(), (fc4[b] > 0.25).mean(), (fc5[b] < -0.25).mean(), (fc4[b] < -0.25).mean()))
print("        The difference mean_v5 - exact is sampling noise plus Jensen's inequality (log of a")
print("        small-count mean), which is symmetric-to-negative; the exact term is the systematic part.")
print()

# ---------------------------------------------------------------- Part C: DE genes, sign and magnitude
print("PART C  same simulations: truly DE genes reaching Bonferroni p_val_adj < 0.05 (Wilcoxon, log-normalized data):")
print("        sign of reported avg_log2FC vs truth, and error vs the ideal log2 ratio of means")
print("%6s %6s | %-4s %6s %9s %10s %10s %10s" % ("n1", "n2", "ver", "n_sig", "signflip", "medAbsErr", "down:med", "up:med"))
for (n1, n2), (x1, x2, true) in sims.items():
    p = wilcox_p(x1, x2)
    padj = np.minimum(p * x1.shape[0], 1)
    ideal = fc_ideal(x1, x2)
    for ver, f, th in (("v4", fc_v4, 0.25), ("v5", fc_v5, 0.1)):
        fc = f(x1, x2)
        keep, _, _ = findmarkers_table(x1, x2, fc, th)
        sig = keep & (padj < 0.05) & (true != 0)
        flip = np.sign(fc[sig]) != np.sign(true[sig])
        err = np.abs(fc[sig] - ideal[sig])
        down = sig & (true < 0); up = sig & (true > 0)
        print("%6d %6d | %-4s %6d %9.4f %10.3f %10.3f %10.3f" % (
            n1, n2, ver, sig.sum(), flip.mean() if sig.sum() else float("nan"),
            np.median(err) if sig.sum() else float("nan"),
            np.median(fc[down] / true[down]) if down.sum() else float("nan"),
            np.median(fc[up] / true[up]) if up.sum() else float("nan")))
print("        down:med / up:med = median of reported/true log2FC for truly down- / up-regulated")
print("        genes (1.0 = unbiased). v4 compresses both symmetrically (pseudocount 1 on means << 1);")
print("        v5 compresses down-regulated and stretches up-regulated genes when n1 < n2.")
print()

# ---------------------------------------------------------------- Part D: worked example
print("PART D  worked example, one gene, equal true expression, n1 = 200 cluster vs n2 = 19,800 rest")
for mu in (0.02, 0.05, 0.1):
    r = np.random.default_rng(7)
    c1 = r.poisson(mu, 200); c2 = r.poisson(mu, 19800)
    # emulate normalized values directly (libsize = 1e4 so log1p(count) == LogNormalize value)
    x1 = np.log1p(c1)[None, :]; x2 = np.log1p(c2)[None, :]
    print("  mu=%.2f  pct.1=%.3f pct.2=%.3f  v4 FC=%+.3f  v5 FC=%+.3f  exact v5 bias=%+.3f  ideal=%+.3f" % (
        mu, pct(x1)[0], pct(x2)[0], fc_v4(x1, x2)[0], fc_v5(x1, x2)[0],
        np.log2((mu + 1/200) / (mu + 1/19800)), fc_ideal(x1, x2)[0]))
