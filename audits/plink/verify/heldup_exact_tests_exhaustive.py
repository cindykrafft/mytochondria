"""Held-up check: the shipped exact-test functions of both versions against exact
rational arithmetic (exact_ref.py), for every genotype table with n <= NMAX and
every 2x2 table with N <= FMAX, with and without mid-p:
  plink 1.9  SNPHWE2 (p), fisher22 (p)                       via stats_driver19
  plink 2.0  HweLnP (ln p), Fisher22TwoSidedP (p and ln p)    via stats_driver2
plus the threshold functions on a grid of thresholds (plink 1.9's shows the PL1
boundary defect on tables whose p sits just above a grid value; see pl1_*).
Usage: heldup_exact_tests_exhaustive.py <driver> [NMAX] [FMAX]"""
import subprocess, sys, math, itertools
from fractions import Fraction
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_ref import hwe_p, fisher_p
DRV = sys.argv[1] if len(sys.argv) > 1 else "./stats_driver2"
LNP = "driver2" in os.path.basename(DRV)
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 60
FMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 40

queries, truth = [], []
for n in range(1, NMAX + 1):
    for hets in range(n + 1):
        for hom1 in range(n - hets + 1):
            hom2 = n - hets - hom1
            if hom1 > hom2:   # symmetric; driver normalizes
                continue
            for midp in (0, 1):
                queries.append(f"H {hets} {hom1} {hom2} {midp}")
                truth.append(("H", hets, hom1, hom2, midp, hwe_p(hets, hom1, hom2, bool(midp))))
for N in range(1, FMAX + 1):
    for m11 in range(N + 1):
        for m12 in range(N - m11 + 1):
            for m21 in range(N - m11 - m12 + 1):
                m22 = N - m11 - m12 - m21
                for midp in (0, 1):
                    queries.append(f"F {m11} {m12} {m21} {m22} {midp}")
                    truth.append(("F", m11, m12, m21, m22, midp, fisher_p(m11, m12, m21, m22, bool(midp))))
out = subprocess.run([DRV], input="\n".join(queries) + "\n", capture_output=True, text=True).stdout.splitlines()
assert len(out) == len(queries), (len(out), len(queries))
worst = {"H": (0, None), "F": (0, None), "Flog": (0, None)}
bad = []
nH = nF = 0
for q, t, o in zip(queries, truth, out):
    f = o.split()
    if t[0] == "H":
        nH += 1
        p19 = float(f[5]); exact = t[5]
        got = math.exp(p19) if LNP else p19     # driver2 prints ln p
        rel = abs(got - float(exact)) / float(exact)
        if rel > worst["H"][0]: worst["H"] = (rel, q)
        if rel > 1e-9: bad.append((q, got, float(exact), rel))
    else:
        nF += 1
        p, lnp = float(f[6]), math.log(float(f[6])); exact = t[6]
        rel = abs(p - float(exact)) / float(exact)
        rel2 = abs(math.exp(lnp) - float(exact)) / float(exact)
        if rel > worst["F"][0]: worst["F"] = (rel, q)
        if rel2 > worst["Flog"][0]: worst["Flog"] = (rel2, q)
        if rel > 1e-9 or rel2 > 1e-9: bad.append((q, p, float(exact), max(rel, rel2)))
print(f"HWE tables n<=  {NMAX}: {nH} queries (x2 for midp), worst relative error {worst['H'][0]:.3e} at '{worst['H'][1]}'")
print(f"Fisher tables N<={FMAX}: {nF} queries, worst relative error p {worst['F'][0]:.3e} at '{worst['F'][1]}', ln p {worst['Flog'][0]:.3e} at '{worst['Flog'][1]}'")
print(f"mismatches (rel > 1e-9): {len(bad)}")
for b in bad[:30]:
    print("  ", b)
# threshold function: for a grid of thresholds, HweThreshLn == (p < thresh)?
tq, tt = [], []
thresholds = [1e-2, 1e-3, 1e-4, 1e-6, 1e-8, 1e-10, 1e-15, 1e-20, 1e-50]
for n in range(1, min(NMAX, 40) + 1):
    for hets in range(n + 1):
        for hom1 in range(n - hets + 1):
            hom2 = n - hets - hom1
            if hom1 > hom2: continue
            for midp in (0, 1):
                p = hwe_p(hets, hom1, hom2, bool(midp))
                for th in thresholds:
                    tq.append(f"T {hets} {hom1} {hom2} {midp} {th!r}")
                    tt.append(p < Fraction(th))
out = subprocess.run([DRV], input="\n".join(tq) + "\n", capture_output=True, text=True).stdout.splitlines()
assert len(out) == len(tq)
tbad = [(q, o) for q, e, o in zip(tq, tt, out) if int(o.split()[6]) != int(e)]
print(f"threshold function on {len(tq)} (table, threshold) pairs, thresholds {thresholds}: {len(tbad)} disagreements with (exact p < threshold)")
for b in tbad[:20]: print("  ", b)
# exact-threshold cases: p exactly equal to a threshold must pass (not fail), per the 1+eps tolerance
eq = []
for n in range(1, 30):
    for hets in range(n + 1):
        for hom1 in range(n - hets + 1):
            hom2 = n - hets - hom1
            if hom1 > hom2: continue
            p = hwe_p(hets, hom1, hom2, False)
            if 0 < p < 1:
                eq.append((hets, hom1, hom2, p))
eqq = [f"T {h} {a} {b} 0 {float(p)!r}" for h, a, b, p in eq]
out = subprocess.run([DRV], input="\n".join(eqq) + "\n", capture_output=True, text=True).stdout.splitlines()
fails = sum(int(o.split()[6]) for o in out)
print(f"p == threshold (float of exact p) on {len(eqq)} tables: {fails} reported as failing (expected 0: tolerance keeps p == thresh)")
