#!/usr/bin/env python3
"""Held-up check: --freq, --missing and --het / --ibc on synthetic data with
missing calls, both binaries, against numpy closed forms.

--freq:    ALT/A1 frequency = ALT allele count / non-missing allele count (founders).
--missing: per-variant F_MISS = missing / n; per-sample F_MISS = missing / m.
--het:     O(HOM), E(HOM) = sum over polymorphic variants of 1 - 2pq * 2n/(2n-1)
           (allele counts from founders, the "unbiased" form both versions use
           when frequencies are estimated from the data), N(NM), F = (O-E)/(N-E).
"""
import os, sys, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import simulate, write_pedmap, run, read_table, fnum, PLINK19, PLINK2, version

rng = np.random.default_rng(7)
n, m = 200, 300
g = simulate(n, m, rng, missing_rate=0.05)
g[:, 0] = 0                       # monomorphic
g[:, 1] = np.where(g[:, 1] < 0, -1, 2)
g[:, 2] = -1                      # all missing
g[:, 3] = 1                       # all het
obs = g >= 0
alt_ct = np.where(obs, g, 0).sum(0)
nm2 = 2 * obs.sum(0)
with np.errstate(invalid="ignore", divide="ignore"):
    p_alt = alt_ct / nm2
fmiss_var = 1 - obs.mean(0)
fmiss_sample = 1 - obs.mean(1)
# --het expectation
poly = (alt_ct > 0) & (alt_ct < nm2) & (nm2 > 0)
p = p_alt[poly]; N2 = nm2[poly]
e_hom_per_var = 1 - 2 * p * (1 - p) * N2 / (N2 - 1)
het = (g == 1)
o_hom = ((g[:, poly] >= 0) & ~het[:, poly]).sum(1)
e_hom = (np.where(g[:, poly] >= 0, 1, 0) * e_hom_per_var).sum(1)
n_nm = (g[:, poly] >= 0).sum(1)
F = (o_hom - e_hom) / (n_nm - e_hom)

print(version(PLINK19)); print(version(PLINK2))
with tempfile.TemporaryDirectory() as tmp:
    pre = write_pedmap(os.path.join(tmp, "d"), g)
    # --- freq
    run(PLINK19, ["--file", pre, "--freq", "--out", os.path.join(tmp, "f19")])
    t = read_table(os.path.join(tmp, "f19.frq"))
    # 1.9 A1 is the minor allele; compare MAF = min(p, 1-p) with NCHROBS
    maf = np.minimum(p_alt, 1 - p_alt)
    d = max(abs(fnum(x) - maf[int(s[3:]) - 1]) for s, x in zip(t["SNP"], t["MAF"]) if not np.isnan(maf[int(s[3:]) - 1]))
    dn = max(abs(fnum(x) - nm2[int(s[3:]) - 1]) for s, x in zip(t["SNP"], t["NCHROBS"]))
    print(f"plink 1.9 --freq: max |MAF - min(p,1-p)| = {d:.2e}, max |NCHROBS - 2*nonmissing| = {dn:g}; all-missing variant MAF printed as {t['MAF'][2]!r}")
    run(PLINK2, ["--pedmap", pre, "--freq", "--out", os.path.join(tmp, "f2")])
    t = read_table(os.path.join(tmp, "f2.afreq"))
    d = max(abs(fnum(x) - p_alt[int(s[3:]) - 1]) for s, x in zip(t["ID"], t["ALT_FREQS"]) if not np.isnan(p_alt[int(s[3:]) - 1]))
    dn = max(abs(fnum(x) - nm2[int(s[3:]) - 1]) for s, x in zip(t["ID"], t["OBS_CT"]))
    print(f"plink2    --freq: max |ALT_FREQS - p| = {d:.2e}, max |OBS_CT - 2*nonmissing| = {dn:g}; all-missing variant ALT_FREQS printed as {t['ALT_FREQS'][2]!r}")
    # --- missing
    run(PLINK19, ["--file", pre, "--missing", "--out", os.path.join(tmp, "m19")])
    tv = read_table(os.path.join(tmp, "m19.lmiss")); ts = read_table(os.path.join(tmp, "m19.imiss"))
    dv = max(abs(fnum(x) - fmiss_var[int(s[3:]) - 1]) for s, x in zip(tv["SNP"], tv["F_MISS"]))
    ds = max(abs(fnum(x) - fmiss_sample[int(s[1:]) - 1]) for s, x in zip(ts["IID"], ts["F_MISS"]))
    print(f"plink 1.9 --missing: max |F_MISS - truth| per variant {dv:.2e}, per sample {ds:.2e}")
    run(PLINK2, ["--pedmap", pre, "--missing", "--out", os.path.join(tmp, "m2")])
    tv = read_table(os.path.join(tmp, "m2.vmiss")); ts = read_table(os.path.join(tmp, "m2.smiss"))
    dv = max(abs(fnum(x) - fmiss_var[int(s[3:]) - 1]) for s, x in zip(tv["ID"], tv["F_MISS"]))
    ds = max(abs(fnum(x) - fmiss_sample[int(s[1:]) - 1]) for s, x in zip(ts["IID"], ts["F_MISS"]))
    print(f"plink2    --missing: max |F_MISS - truth| per variant {dv:.2e}, per sample {ds:.2e}")
    # --- het
    run(PLINK19, ["--file", pre, "--het", "--out", os.path.join(tmp, "h19")])
    t = read_table(os.path.join(tmp, "h19.het"))
    idx = [int(s[1:]) - 1 for s in t["IID"]]
    do = max(abs(fnum(x) - o_hom[i]) for i, x in zip(idx, t["O(HOM)"]))
    de = max(abs(fnum(x) - e_hom[i]) for i, x in zip(idx, t["E(HOM)"]))
    dn = max(abs(fnum(x) - n_nm[i]) for i, x in zip(idx, t["N(NM)"]))
    df = max(abs(fnum(x) - F[i]) for i, x in zip(idx, t["F"]))
    print(f"plink 1.9 --het: max |O(HOM) diff| {do:g}, |E(HOM) diff| {de:.2e}, |N(NM) diff| {dn:g}, |F diff| {df:.2e} (E(HOM) printed to 6 s.f.)")
    run(PLINK2, ["--pedmap", pre, "--het", "--out", os.path.join(tmp, "h2")])
    t = read_table(os.path.join(tmp, "h2.het"))
    idx = [int(s[1:]) - 1 for s in t["IID"]]
    do = max(abs(fnum(x) - o_hom[i]) for i, x in zip(idx, t["O(HOM)"]))
    de = max(abs(fnum(x) - e_hom[i]) for i, x in zip(idx, t["E(HOM)"]))
    dn = max(abs(fnum(x) - n_nm[i]) for i, x in zip(idx, t["OBS_CT"]))
    df = max(abs(fnum(x) - F[i]) for i, x in zip(idx, t["F"]))
    print(f"plink2    --het: max |O(HOM) diff| {do:g}, |E(HOM) diff| {de:.2e}, |OBS_CT diff| {dn:g}, |F diff| {df:.2e}")
    # plink2 --het small-sample: the same 2n/(2n-1) correction is opt-in there; default is 2pq
    e_hom_plain = (np.where(g[:, poly] >= 0, 1, 0) * (1 - 2 * p * (1 - p))).sum(1)
    F_plain = (o_hom - e_hom_plain) / (n_nm - e_hom_plain)
    de2 = max(abs(fnum(x) - e_hom_plain[i]) for i, x in zip(idx, t["E(HOM)"]))
    df2 = max(abs(fnum(x) - F_plain[i]) for i, x in zip(idx, t["F"]))
    print(f"plink2    --het vs uncorrected 1-2pq: |E(HOM) diff| {de2:.2e}, |F diff| {df2:.2e}")
    run(PLINK2, ["--pedmap", pre, "--het", "small-sample", "--out", os.path.join(tmp, "h2s")])
    t = read_table(os.path.join(tmp, "h2s.het"))
    idx = [int(s[1:]) - 1 for s in t["IID"]]
    de3 = max(abs(fnum(x) - e_hom[i]) for i, x in zip(idx, t["E(HOM)"]))
    df3 = max(abs(fnum(x) - F[i]) for i, x in zip(idx, t["F"]))
    print(f"plink2    --het small-sample vs 2n/(2n-1)-corrected: |E(HOM) diff| {de3:.2e}, |F diff| {df3:.2e}")
