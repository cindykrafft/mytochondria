#!/usr/bin/env python3
"""Held-up check: IQ-TREE 2's log-likelihood, discrete-gamma category rates, +I, +I+G,
fixed-parameter GTR+F and the Lewis +ASC correction against an independent numpy
implementation (Felsenstein pruning; gamma quantiles/means via scipy).

Design: a 5-taxon tree with fixed branch lengths, a 300-site alignment simulated under
JC in this script, and `-te tree -blfix` so the binary evaluates the likelihood at the
given branch lengths with the model parameters fixed in the model string. The
reference is computed here from the same tree/alignment. The +ASC case uses only
the variable columns of the alignment (the binary refuses constant sites under +ASC,
which is also checked).
"""
import os, sys, math, re
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iqt

print("binary:", iqt.IQTREE2)
print(iqt.version())
D = os.path.join(iqt.RUNDIR, "closed_form"); os.makedirs(D, exist_ok=True)
rng = np.random.default_rng(20260903)

tree = "((A:0.05,B:0.12):0.08,(C:0.2,D:0.03):0.06,E:0.15);"
root = iqt.parse_newick(tree)
open(os.path.join(D, "tree.nwk"), "w").write(tree + "\n")
freqs_jc = np.full(4, 0.25); Q_jc = iqt.gtr_Q([1] * 6, freqs_jc)
names, seqs = iqt.simulate(root, 300, Q_jc, freqs_jc, rng)
iqt.write_fasta(os.path.join(D, "aln.fa"), names, seqs)
pats, w = iqt.patterns_from_seqs(seqs)
print("alignment: %d taxa, %d sites, %d patterns" % (len(names), len(seqs[0]), len(w)))

def check(label, model, ref, extra=(), asc=False, aln="aln.fa"):
    args = ["-s", aln, "-te", "tree.nwk", "-blfix", "-m", model, "-T", "1", "-seed", "1", "-wsl"] + list(extra)
    out, rep = iqt.run(args, "cf_" + label, cwd=D)
    lnL = iqt.report_value(rep, "Log-likelihood of the tree")
    print("%-28s %-22s iqtree %14.4f  reference %14.4f  diff %9.2e" % (label, model, lnL, ref, lnL - ref))
    assert abs(lnL - ref) < 2e-3, (label, lnL, ref)
    return rep

# 1. JC, no rate heterogeneity
check("JC", "JC", iqt.loglik(root, pats, w, Q_jc, freqs_jc))
# 2. JC+G4 with alpha fixed (mean-rate categories, the default)
alpha = 0.6
rep = check("JC+G4{0.6} mean", "JC+G4{0.6}", iqt.loglik(root, pats, w, Q_jc, freqs_jc, gamma=(alpha, 4, "mean")))
tab = iqt.report_gamma_table(rep)
ref = iqt.gamma_rates_mean(alpha, 4)
print("  +G4 category rates (mean):   iqtree", [r for r, p in tab], " scipy", np.round(ref, 4).tolist())
assert np.allclose([r for r, p in tab], ref, rtol=1e-3)
# 3. JC+G4 with the median variant (-gmedian)
rep = check("JC+G4{0.6} median", "JC+G4{0.6}", iqt.loglik(root, pats, w, Q_jc, freqs_jc, gamma=(alpha, 4, "median")), extra=["-gmedian"])
tab = iqt.report_gamma_table(rep)
ref = iqt.gamma_rates_median(alpha, 4)
print("  +G4 category rates (median): iqtree", [r for r, p in tab], " scipy", np.round(ref, 4).tolist())
assert np.allclose([r for r, p in tab], ref, rtol=1e-3)
# 4. JC+I with p_inv fixed
check("JC+I{0.3}", "JC+I{0.3}", iqt.loglik(root, pats, w, Q_jc, freqs_jc, pinv=0.3))
# 5. JC+I+G4 both fixed: gamma rates scaled by 1/(1-pinv), proportions (1-pinv)/k
rep = check("JC+I{0.3}+G4{0.6}", "JC+I{0.3}+G4{0.6}", iqt.loglik(root, pats, w, Q_jc, freqs_jc, gamma=(alpha, 4, "mean"), pinv=0.3))
tab = iqt.report_gamma_table(rep)
ref = iqt.gamma_rates_mean(alpha, 4) / 0.7
print("  +I+G4 category rates: iqtree", [r for r, p in tab], " scipy/(1-pinv)", np.round(ref, 4).tolist(),
      " props", [p for r, p in tab])
assert np.allclose([r for r, p in tab], ref, rtol=1e-3) and np.allclose([p for r, p in tab], 0.7 / 4, atol=1e-4)
# 6. GTR with fixed rates and +F fixed frequencies
rates = [1.5, 4.0, 0.8, 1.2, 5.0, 1.0]; fq = [0.3, 0.2, 0.2, 0.3]
Q = iqt.gtr_Q(rates, fq)
check("GTR{..}+F{..}", "GTR{1.5,4.0,0.8,1.2,5.0}+F{0.3,0.2,0.2,0.3}", iqt.loglik(root, pats, w, Q, fq))
check("GTR{..}+F{..}+G4{0.6}", "GTR{1.5,4.0,0.8,1.2,5.0}+F{0.3,0.2,0.2,0.3}+G4{0.6}", iqt.loglik(root, pats, w, Q, fq, gamma=(alpha, 4, "mean")))
# 7. +ASC (Lewis 2001) on the variable columns only
var_cols = [i for i in range(len(seqs[0])) if len(set(s[i] for s in seqs)) > 1]
vseqs = ["".join(s[i] for i in var_cols) for s in seqs]
iqt.write_fasta(os.path.join(D, "var.fa"), names, vseqs)
vp, vw = iqt.patterns_from_seqs(vseqs)
print("variable-site alignment: %d sites" % len(var_cols))
check("JC+ASC", "JC+ASC", iqt.loglik(root, vp, vw, Q_jc, freqs_jc, asc=True), aln="var.fa")
check("GTR+F+ASC+G4", "GTR{1.5,4.0,0.8,1.2,5.0}+F{0.3,0.2,0.2,0.3}+ASC+G4{0.6}", iqt.loglik(root, vp, vw, Q, fq, gamma=(alpha, 4, "mean"), asc=True), aln="var.fa")
# 8. +ASC on an alignment with constant sites must be refused
try:
    iqt.run(["-s", "aln.fa", "-te", "tree.nwk", "-m", "JC+ASC", "-T", "1"], "cf_asc_refused", cwd=D)
    print("+ASC with constant sites: NOT refused (unexpected)")
except RuntimeError as e:
    m = re.search(r"Invalid use of \+ASC[^\n]*", str(e))
    print("+ASC with constant sites refused:", m.group(0) if m else "(error, message not matched)")
print("ALL CLOSED-FORM CHECKS PASSED")
