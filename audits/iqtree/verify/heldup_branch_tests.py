#!/usr/bin/env python3
"""Branch supports on a 4-taxon JC alignment, where everything is hand-computable:
the two NNI alternatives of the single internal branch are the other two topologies,
and under JC (no free model parameters) their fully optimised log-likelihoods come
from `-te` runs of the binary itself. Checks:
  * aBayes = 1/(1 + e^{l1-l0} + e^{l2-l0})                     (Anisimova et al. 2011)
  * parametric aLRT (`-alrt 0`): a port of tree/phylotree.cpp:Statistics_To_Probabilities
    (PhyML's table) evaluated at 2*(l0 - max(l1,l2)), compared with the reported
    value, and with scipy's chi2_1 cdf and the 1/2 chi2_0 + 1/2 chi2_1 mixture.
  * SH-aLRT: an independent RELL port (multinomial site resampling of the three
    site-log-likelihood vectors, Guindon et al. 2010 rule as in testOneBranch)
    compared with the reported percentage within Monte-Carlo error.
Two alignments: one simulated with a short internal branch (moderate support) and
one with a long one (high support).
"""
import os, sys, re, math
import numpy as np
from scipy.stats import chi2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iqt

print("binary:", iqt.IQTREE2); print(iqt.version())
D = os.path.join(iqt.RUNDIR, "branch"); os.makedirs(D, exist_ok=True)

def statistics_to_probabilities(x):
    """Port of tree/phylotree.cpp Statistics_To_Probabilities (master a00094e0)."""
    table = [(0.000000393, 0.00000157, 0.0005, 0.001), (0.00000157, 0.0000393, 0.001, 0.005),
             (0.0000393, 0.000157, 0.005, 0.01), (0.000157, 0.000982, 0.01, 0.025),
             (0.000982, 0.00393, 0.025, 0.05), (0.00393, 0.0158, 0.05, 0.1), (0.0158, 0.0642, 0.1, 0.2),
             (0.0642, 0.148, 0.2, 0.3), (0.148, 0.275, 0.3, 0.4), (0.275, 0.455, 0.4, 0.5),
             (0.455, 0.708, 0.5, 0.6), (0.708, 1.074, 0.6, 0.7), (1.074, 1.642, 0.7, 0.8),
             (1.642, 2.706, 0.8, 0.9), (2.706, 3.841, 0.9, 0.95), (3.841, 5.024, 0.95, 0.975),
             (5.024, 6.635, 0.975, 0.99), (6.635, 7.879, 0.99, 0.995), (7.879, 10.828, 0.995, 0.999),
             (10.828, 12.116, 0.999, 0.9995)]
    if x >= 12.116: r = 0.9999
    elif x < 0.000000393: r = 0.0001
    else:
        for a, b, fa, fb in table:
            if a <= x < b:
                r = (b - x) / (b - a) * fa + (x - a) / (b - a) * fb; break
    r = r + (1.0 - r) / 2.0          # mixture 1/2 chi2_0 + 1/2 chi2_1
    return r * r * r                 # cubed (inherited from PhyML's alrt.c)

topos = {"t0": "((A,B),(C,D));", "t1": "((A,C),(B,D));", "t2": "((A,D),(B,C));"}
for k, v in topos.items(): open(os.path.join(D, k + ".nwk"), "w").write(v + "\n")
freqs = np.full(4, 0.25); Q = iqt.gtr_Q([1] * 6, freqs)

def site_lh(prefix):
    txt = open(os.path.join(D, prefix + ".sitelh")).read().split("\n")[1]
    return np.array([float(x) for x in txt.split()[1:]])

for case, internal, nsites in (("short", 0.02, 400), ("long", 0.15, 400)):
    rng = np.random.default_rng(1 if case == "short" else 2)
    root = iqt.parse_newick("((A:0.1,B:0.1):%g,C:0.1,D:0.1);" % internal)
    names, seqs = iqt.simulate(root, nsites, Q, freqs, rng)
    aln = "aln_%s.fa" % case; iqt.write_fasta(os.path.join(D, aln), names, seqs)
    # log-likelihoods of the three topologies, all five branches optimised
    lh = {}; slh = {}
    for t in topos:
        out, rep = iqt.run(["-s", aln, "-te", t + ".nwk", "-m", "JC", "-T", "1", "-wsl"], "bt_%s_%s" % (case, t), cwd=D)
        lh[t] = iqt.report_value(rep, "Log-likelihood of the tree"); slh[t] = site_lh("bt_%s_%s" % (case, t))
    best = max(lh, key=lh.get); alts = [t for t in topos if t != best]
    l0, l1, l2 = lh[best], lh[alts[0]], lh[alts[1]]
    print("\n== %s internal branch (%g), %d sites: logL %s" % (case, internal, nsites, {t: round(v, 4) for t, v in lh.items()}))
    # reported supports: SH-aLRT and aBayes in one run, parametric aLRT in another
    R = 20000
    out, rep = iqt.run(["-s", aln, "-m", "JC", "-alrt", str(R), "-abayes", "-T", "1", "-seed", "5"], "bt_%s_sh" % case, cwd=D)
    tf = open(os.path.join(D, "bt_%s_sh.treefile" % case)).read()
    sh_rep, ab_rep = map(float, re.search(r"\)([0-9.]+)/([0-9.]+):", tf).groups())
    out, rep = iqt.run(["-s", aln, "-m", "JC", "-alrt", "0", "-T", "1", "-seed", "5"], "bt_%s_par" % case, cwd=D)
    tf2 = open(os.path.join(D, "bt_%s_par.treefile" % case)).read()
    par_rep = float(re.search(r"\)/([0-9.]+):", tf2).group(1))   # label is "/<aLRT>" (empty SH slot), 3 significant digits
    ml_topo = re.sub(r":[0-9.e-]+|\)[0-9./]+", "", tf2).strip()
    print("   ML tree in the -alrt run: %s   (best -te topology: %s)" % (ml_topo, best))
    # references
    ab_ref = 1.0 / (1.0 + math.exp(l1 - l0) + math.exp(l2 - l0))
    stat = 2 * (l0 - max(l1, l2))
    par_ref = statistics_to_probabilities(stat)
    print("   aBayes:          reported %.4f   reference %.4f   diff %.1e" % (ab_rep, ab_ref, ab_rep - ab_ref))
    print("   parametric aLRT: reported %.4f   port of Statistics_To_Probabilities(%.4f) = %.4f   diff %.1e" % (par_rep, stat, par_ref, par_rep - par_ref))
    c1 = chi2.cdf(stat, 1); mix = 1 - 0.5 * (1 - c1)
    print("     for comparison: chi2_1 cdf %.4f; mixture 1/2chi2_0+1/2chi2_1 cdf %.4f; mixture^3 %.4f" % (c1, mix, mix ** 3))
    assert abs(ab_rep - ab_ref) < 2e-3 and abs(par_rep - par_ref) < 6e-3
    # SH-aLRT RELL port
    rng2 = np.random.default_rng(99)
    S = np.vstack([slh[best], slh[alts[0]], slh[alts[1]]]); L = np.array([l0, l1, l2])
    alrt = l0 - max(l1, l2)
    cnt = 0
    W = rng2.multinomial(nsites, np.full(nsites, 1.0 / nsites), size=R)
    lh_new = W @ S.T                     # (R, 3)
    cs = lh_new - L[None, :]
    srt = np.sort(cs, axis=1)
    cnt = int(np.sum(alrt > (srt[:, 2] - srt[:, 1]) + 0.05))
    sh_ref = 100.0 * cnt / R
    se = 100 * math.sqrt(max(sh_ref / 100 * (1 - sh_ref / 100), 1e-6) / R) * math.sqrt(2)
    print("   SH-aLRT:         reported %.1f%%   RELL port %.2f%% (R=%d; MC s.e. of the difference ~%.2f)" % (sh_rep, sh_ref, R, se))
    assert abs(sh_rep - sh_ref) < max(4 * se, 1.0)
print("\nALL BRANCH-TEST CHECKS PASSED")
