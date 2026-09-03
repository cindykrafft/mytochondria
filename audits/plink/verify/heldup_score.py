#!/usr/bin/env python3
"""Held-up check: --score on both binaries against numpy, covering mean imputation
of missing genotypes (default), no-mean-imputation, center, and sum vs average
output, with a score file whose effect allele is sometimes REF and sometimes ALT.

Reference (per sample i): with effect-allele dosage d_ij in {0,1,2} (or missing),
  mean imputation:  missing d_ij := 2 * f_j (f_j = effect-allele frequency, founders)
  center:           d_ij := d_ij - 2 f_j
  score_sum_i = sum_j w_j d_ij ;  average = score_sum_i / (number of alleles counted)
  where the allele count is 2 * (#variants) with mean imputation and
  2 * (#non-missing variants) without.
"""
import os, sys, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import simulate, write_pedmap, run, read_table, fnum, PLINK19, PLINK2, version

rng = np.random.default_rng(5)
n, m = 150, 60
g = simulate(n, m, rng, missing_rate=0.08)
obs = g >= 0
w = rng.normal(0, 1, m)
eff_is_alt = rng.random(m) < 0.6
d = np.where(eff_is_alt[None, :], g, 2 - g).astype(float)
d[~obs] = np.nan
alt_ct = np.where(obs, g, 0).sum(0); nm2 = 2 * obs.sum(0)
f_alt = alt_ct / nm2
f_eff = np.where(eff_is_alt, f_alt, 1 - f_alt)

def ref(mean_impute, center, average):
    x = d.copy()
    if mean_impute:
        x = np.where(np.isnan(x), 2 * f_eff[None, :], x)
    if center:
        x = x - 2 * f_eff[None, :]
    s = np.nansum(x * w[None, :], 1)
    cnt = np.where(mean_impute, 2 * m, 2 * obs.sum(1))
    return s / cnt if average else s, cnt

print(version(PLINK19)); print(version(PLINK2))
with tempfile.TemporaryDirectory() as tmp:
    pre = write_pedmap(os.path.join(tmp, "d"), g)
    sf = os.path.join(tmp, "score.txt")
    with open(sf, "w") as f:
        for j in range(m):
            f.write(f"snp{j+1} {'T' if eff_is_alt[j] else 'A'} {w[j]:.10g}\n")
    cases = [
        ("default (mean-impute, average)", [], True, False, True),
        ("sum", ["sum"], True, False, False),
        ("no-mean-imputation", ["no-mean-imputation"], False, False, True),
        ("no-mean-imputation sum", ["no-mean-imputation", "sum"], False, False, False),
        ("center", ["center"], True, True, True),
        ("center no-mean-imputation", ["center", "no-mean-imputation"], False, True, True),
    ]
    for label, mods, mi, ce, av in cases:
        r, cnt = ref(mi, ce, av)
        run(PLINK19, ["--file", pre, "--score", sf, "1", "2", "3", *mods, "--out", os.path.join(tmp, "s19")])
        t = read_table(os.path.join(tmp, "s19.profile"))
        idx = [int(s[1:]) - 1 for s in t["IID"]]
        d19 = max(abs(fnum(x) - r[i]) for i, x in zip(idx, t["SCORE"]))
        c19 = max(abs(fnum(x) - cnt[i]) for i, x in zip(idx, t["CNT"]))
        # plink2: request sums and averages explicitly
        cols = "maybefid,nallele,denom,dosagesum,scoreavgs,scoresums"
        mods2 = [x for x in mods if x != "sum"]
        run(PLINK2, ["--pedmap", pre, "--score", sf, "1", "2", "3", "cols=" + cols, *mods2, "--out", os.path.join(tmp, "s2")])
        t2 = read_table(os.path.join(tmp, "s2.sscore"))
        idx2 = [int(s[1:]) - 1 for s in t2["IID"]]
        col = "SCORE1_AVG" if av else "SCORE1_SUM"
        d2 = max(abs(fnum(x) - r[i]) for i, x in zip(idx2, t2[col]))
        c2 = max(abs(fnum(x) - cnt[i]) for i, x in zip(idx2, t2["DENOM"]))
        print(f"{label:30s}: plink1.9 max|SCORE-ref| {d19:.2e} |CNT-ref| {c19:g};  plink2 max|{col}-ref| {d2:.2e} |DENOM-ref| {c2:g}")
    # dosage-sum column and NALLELE semantics in plink2
    print("plink2 NALLELE (first 3 samples):", t2["NAMED_ALLELE_DOSAGE_SUM"][:3] if "NAMED_ALLELE_DOSAGE_SUM" in t2 else t2.get("ALLELE_CT", ["?"])[:3])
