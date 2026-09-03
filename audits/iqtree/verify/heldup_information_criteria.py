#!/usr/bin/env python3
"""Held-up check: parameter counts and AIC/AICc/BIC arithmetic in the .iqtree report and
in ModelFinder's model table, single-alignment and partitioned.

Design: a 6-taxon alignment (600 sites) simulated under GTR+G4 in this script.
  A. `-m GTR+F+I+G4`: the reported "Number of free parameters" must be
     branches (2n-3=9) + 5 GTR rates + 3 frequencies + alpha + p_inv = 19, and
     AIC = -2L + 2k, AICc = AIC + 2k(k+1)/(n-k-1), BIC = -2L + k ln n with n = sites.
  B. `-m MF` (ModelFinder only): every row of "List of models sorted by BIC scores"
     must satisfy the same arithmetic with an integer k that equals the count implied
     by the model name (rate-matrix parameters + 3 for +F + 1 for +G + 1 for +I
     + 2c-2 for +Rc + 9 branches); the reported best model must be the BIC argmin.
  C. Partitioned (two charsets): the total under -p (edge-linked proportional) must be
     9 + (2-1) + 2*(5+3+1) = 28 for GTR+F+G4 in both partitions; -q (equal) 27; -Q
     (unlinked) 36. And for `-m MFP -p`, the total must equal 9 + 1 + the sum over
     partitions of the selected models' parameters.
"""
import os, sys, re, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iqt

print("binary:", iqt.IQTREE2); print(iqt.version())
D = os.path.join(iqt.RUNDIR, "ic"); os.makedirs(D, exist_ok=True)
rng = np.random.default_rng(7)
tree = "(((A:0.08,B:0.12):0.07,C:0.15):0.05,(D:0.1,E:0.2):0.06,F:0.18);"
root = iqt.parse_newick(tree)
fq = [0.3, 0.2, 0.2, 0.3]; Q = iqt.gtr_Q([1.5, 4.0, 0.8, 1.2, 5.0, 1.0], fq)
names, seqs = iqt.simulate(root, 600, Q, fq, rng, gamma=(0.8, 4))
iqt.write_fasta(os.path.join(D, "aln.fa"), names, seqs)
n = len(seqs[0]); ntax = len(names); nbr = 2 * ntax - 3
print("alignment: %d taxa, %d sites" % (ntax, n))

def ic(L, k, n):
    AIC = -2 * L + 2 * k
    return AIC, AIC + 2.0 * k * (k + 1) / max(n - k - 1, 1), -2 * L + k * math.log(n)

RATE_PARAMS = {"JC": 0, "F81": 0, "K80": 1, "HKY": 1, "TNe": 2, "TN": 2, "K81": 2, "K81u": 2,
               "TPM2": 2, "TPM2u": 2, "TPM3": 2, "TPM3u": 2, "K3P": 2, "K3Pu": 2, "K2P": 1, "TIMe": 3, "TIM": 3, "TIM2e": 3, "TIM2": 3,
               "TIM3e": 3, "TIM3": 3, "TVMe": 4, "TVM": 4, "SYM": 5, "GTR": 5}
def expected_k(model, branches):
    parts = model.split("+"); k = RATE_PARAMS[parts[0]] + branches
    for p in parts[1:]:
        if p == "F": k += 3
        elif p == "FQ": k += 0
        elif p.startswith("G"): k += 1
        elif p == "I": k += 1
        elif p.startswith("R"): k += 2 * int(p[1:]) - 2
        else: raise ValueError(p)
    return k

# ---- A
out, rep = iqt.run(["-s", "aln.fa", "-m", "GTR+F+I+G4", "-T", "1", "-seed", "1"], "ic_gtr", cwd=D)
L = iqt.report_value(rep, "Log-likelihood of the tree")
k = int(iqt.report_value(rep, "Number of free parameters (#branches + #model parameters)"))
AIC, AICc, BIC = (iqt.report_value(rep, s) for s in ("Akaike information criterion (AIC) score",
                  "Corrected Akaike information criterion (AICc) score", "Bayesian information criterion (BIC) score"))
eA, eAc, eB = ic(L, k, n)
print("A. GTR+F+I+G4: logL %.4f  k=%d (expected %d)  AIC %.4f (%.4f)  AICc %.4f (%.4f)  BIC %.4f (%.4f)"
      % (L, k, nbr + 5 + 3 + 1 + 1, AIC, eA, AICc, eAc, BIC, eB))
assert k == nbr + 10 and abs(AIC - eA) < 2e-3 and abs(AICc - eAc) < 2e-3 and abs(BIC - eB) < 2e-3

# ---- B
out, rep = iqt.run(["-s", "aln.fa", "-m", "MF", "-T", "1", "-seed", "1"], "ic_mf", cwd=D)
m = re.search(r"List of models sorted by BIC scores:\s*\n\s*\nModel\s+LogL\s+AIC\s+w-AIC\s+AICc\s+w-AICc\s+BIC\s+w-BIC\n((?:\S.*\n)+)", rep)
rows = []
for line in m.group(1).splitlines():
    f = line.split()
    if len(f) < 11: continue          # Model LogL AIC +/- w-AIC AICc +/- w-AICc BIC +/- w-BIC
    rows.append((f[0], float(f[1]), float(f[2]), float(f[5]), float(f[8])))
best_line = re.search(r"Best-fit model according to BIC:\s*(\S+)", rep).group(1)
print("B. ModelFinder table: %d models; best by BIC: %s" % (len(rows), best_line))
maxdev = 0.0; bad = []
for name, L, AIC, AICc, BIC in rows:
    kf = (AIC + 2 * L) / 2
    k = int(round(kf))
    ek = expected_k(name, nbr)
    eA, eAc, eB = ic(L, k, n)
    dev = max(abs(kf - k), abs(AICc - eAc), abs(BIC - eB))
    maxdev = max(maxdev, dev)
    if k != ek or dev > 5e-3: bad.append((name, k, ek, dev))
print("   k from AIC is an integer and AICc/BIC follow from (L, k, n=%d) for every row: max deviation %.2e" % (n, maxdev))
print("   k matches the count implied by the model name for all %d rows: %s" % (len(rows), "yes" if not bad else bad))
for name, L, AIC, AICc, BIC in rows[:6]:
    print("   %-14s logL %11.4f  k=%2d  AICc %10.3f  BIC %10.3f" % (name, L, int(round((AIC + 2 * L) / 2)), AICc, BIC))
argmin = min(rows, key=lambda r: r[4])[0]
print("   BIC argmin of the table: %s  (reported best: %s)" % (argmin, best_line))
assert not bad and argmin == best_line
# weights: w-BIC should be exp(-(BIC-min)/2) normalised
# ---- C
open(os.path.join(D, "part.nex"), "w").write("#nexus\nbegin sets;\n  charset p1 = 1-300;\n  charset p2 = 301-600;\nend;\n")
for flag, expect, label in (("-p", nbr + 1 + 2 * 9, "edge-linked proportional (-p)"),
                            ("-q", nbr + 2 * 9, "edge-linked equal (-q)"),
                            ("-Q", 2 * nbr + 2 * 9, "edge-unlinked (-Q)")):
    out, rep = iqt.run(["-s", "aln.fa", flag, "part.nex", "-m", "GTR+F+G4", "-T", "1", "-seed", "1"], "ic_part" + flag, cwd=D)
    k = int(iqt.report_value(rep, "Number of free parameters (#branches + #model parameters)"))
    L = iqt.report_value(rep, "Log-likelihood of the tree")
    BIC = iqt.report_value(rep, "Bayesian information criterion (BIC) score")
    nrep = int(re.search(r"Sample size \(n, alignment length\):\s*(\d+)", rep).group(1)) if "Sample size (n, alignment length)" in rep else n
    print("C. %-32s GTR+F+G4 x2: k=%d (expected %d)  BIC %.4f (recomputed with n=%d: %.4f)" % (label, k, expect, BIC, n, ic(L, k, n)[2]))
    assert k == expect and abs(BIC - ic(L, k, n)[2]) < 2e-3
out, rep = iqt.run(["-s", "aln.fa", "-p", "part.nex", "-m", "MFP", "-T", "1", "-seed", "1"], "ic_mfp_p", cwd=D)
k = int(iqt.report_value(rep, "Number of free parameters (#branches + #model parameters)"))
models = re.findall(r"charpartition mymodels =\s*\n((?:.*\n)+?)end;", open(os.path.join(D, "ic_mfp_p.best_scheme.nex")).read())[0]
sel = re.findall(r"^\s*([^:\s]+):", models, re.M)
esum = nbr + (len(sel) - 1) + sum(expected_k(s, 0) for s in sel)
print("C. -m MFP -p: selected %s -> k=%d (expected %d)" % (sel, k, esum))
assert k == esum
print("ALL INFORMATION-CRITERION CHECKS PASSED")
