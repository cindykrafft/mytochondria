#!/usr/bin/env python3
"""Held-up check: --hardy and --hwe through the command line of the built PLINK 1.9
and PLINK 2.0 binaries against exact rational arithmetic (exact_ref.py), on
synthetic autosomal genotypes with missing calls and with the mid-p variant.

For each variant the harness computes the exact Wigginton p from the genotype
counts of the samples PLINK uses (founders; all samples with --nonfounders) and
compares with the P column of plink.hwe / plink2.hardy; then checks that
--hwe <t> removes exactly the variants with exact p < t.
"""
import os, sys, tempfile, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import simulate, write_pedmap, run, read_table, fnum, PLINK19, PLINK2, version
from exact_ref import hwe_p

rng = np.random.default_rng(20260903)
n, m = 300, 400
maf = np.r_[rng.uniform(0.01, 0.5, m - 40), np.full(20, 0.5), np.full(20, 0.02)]
g = simulate(n, m, rng, maf=maf, missing_rate=0.03)
# push 60 variants out of HWE (excess / deficit of hets)
for j in range(60):
    het = g[:, j] == 1
    if j % 2:
        g[het, j] = 2 * (rng.random(het.sum()) < 0.5)          # deficit
    else:
        hom = g[:, j] != 1
        g[hom & (rng.random(n) < 0.4), j] = 1                    # excess
counts = {}
for j in range(m):
    col = g[:, j]
    counts[j] = (int((col == 1).sum()), int((col == 0).sum()), int((col == 2).sum()))
exact = {mid: {j: hwe_p(*counts[j], midp=mid) for j in range(m)} for mid in (False, True)}

print(version(PLINK19)); print(version(PLINK2))
with tempfile.TemporaryDirectory() as tmp:
    pre = write_pedmap(os.path.join(tmp, "d"), g)
    for label, exe, args, pcol, idcol, extra in (
        ("plink 1.9 --hardy", PLINK19, ["--file", pre, "--hardy", "--out", os.path.join(tmp, "o19")], "P", "SNP", []),
        ("plink 1.9 --hardy midp", PLINK19, ["--file", pre, "--hardy", "midp", "--out", os.path.join(tmp, "o19m")], "P", "SNP", []),
        ("plink2 --hardy", PLINK2, ["--pedmap", pre, "--hardy", "--out", os.path.join(tmp, "o2")], "P", "ID", []),
        ("plink2 --hardy midp", PLINK2, ["--pedmap", pre, "--hardy", "midp", "--out", os.path.join(tmp, "o2m")], "MIDP", "ID", []),
    ):
        run(exe, args)
        out = args[-1] + (".hwe" if "1.9" in label else ".hardy")
        t = read_table(out)
        midp = "midp" in label
        rows = [(sid, p) for sid, p, test in zip(t[idcol], t[pcol], t.get("TEST", ["ALL"] * len(t[idcol]))) if test in ("ALL", "ALL(NP)")]
        worst = 0.0
        for sid, p in rows:
            j = int(sid[3:]) - 1
            ex = float(exact[midp][j])
            got = fnum(p)
            if pcol == "LOG10_P":
                got = 10 ** got
            rel = abs(got - ex) / ex
            worst = max(worst, rel)
        print(f"{label:24s}: {len(rows)} variants, max |P - exact|/exact = {worst:.2e}  (6 significant digits printed)")
    # --hwe threshold filtering
    for thr in (0.05, 1e-3, 1e-6):
        for label, exe, args, keep_file in (
            ("plink 1.9", PLINK19, ["--file", pre, "--hwe", str(thr), "--write-snplist", "--out", os.path.join(tmp, "h19")], os.path.join(tmp, "h19.snplist")),
            ("plink 1.9 midp", PLINK19, ["--file", pre, "--hwe", str(thr), "midp", "--write-snplist", "--out", os.path.join(tmp, "h19m")], os.path.join(tmp, "h19m.snplist")),
            ("plink2", PLINK2, ["--pedmap", pre, "--hwe", str(thr), "--write-snplist", "--out", os.path.join(tmp, "h2")], os.path.join(tmp, "h2.snplist")),
            ("plink2 midp", PLINK2, ["--pedmap", pre, "--hwe", str(thr), "midp", "--write-snplist", "--out", os.path.join(tmp, "h2m")], os.path.join(tmp, "h2m.snplist")),
        ):
            run(exe, args)
            kept = {l.strip() for l in open(keep_file) if l.strip()}
            midp = "midp" in label
            expected = {f"snp{j+1}" for j in range(m) if not (exact[midp][j] < thr)}
            print(f"--hwe {thr:g} {label:16s}: kept {len(kept)}, expected {len(expected)}, symmetric difference {len(kept ^ expected)}")
