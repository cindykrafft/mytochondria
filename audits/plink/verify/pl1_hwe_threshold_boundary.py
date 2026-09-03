#!/usr/bin/env python3
"""PL1: PLINK 1.9 --hwe removes variants whose exact HWE p-value is above the
threshold when the variant has 2 or 3 heterozygotes (occasionally more).

Part A (function level, shipped SNPHWE_t / SNPHWE_midp_t compiled from the
audited tree and driven through stats_driver19): for every genotype table with
n <= 300 and <= 8 heterozygotes, bisect the threshold at which the filter flips
and compare with the exact p.  Correct: fail iff p < threshold.
Part B (command line): a dataset containing the table (hets 2, hom 2, hom 2),
whose exact p is 185/385 = 0.48052; `--hardy` prints that p and `--hwe 0.48`
removes the variant; `--hwe 0.4805` and `--hwe 0.4806` shown for contrast.
plink2 on the same data keeps it.
"""
import os, sys, subprocess, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import write_pedmap, run, read_table, fnum, PLINK19, PLINK2, version
from exact_ref import hwe_p
from fractions import Fraction

print(version(PLINK19)); print(version(PLINK2))
DRV = os.environ.get("STATS_DRIVER19")
if DRV and os.path.exists(DRV):
    print("\n== A. bisection of the SNPHWE_t / SNPHWE_midp_t flip point (n <= 300, hets <= 8 exhaustive)")
    from collections import defaultdict
    def drv(qs):
        return subprocess.run([DRV], input="\n".join(qs) + "\n", capture_output=True, text=True).stdout.splitlines()
    tables = [(h, a, n - h - a) for n in range(2, 301) for h in range(min(n, 8) + 1) for a in range(n - h + 1) if a <= n - h - a]
    for mid in (0, 1):
        live = [(h, a, b, float(hwe_p(h, a, b, bool(mid)))) for h, a, b in tables]
        live = [t for t in live if 0 < t[3] < (0.5 if mid else 1)]
        lo, hi = [0.5] * len(live), [1.5] * len(live)
        for _ in range(40):
            mids = [(l + u) / 2 for l, u in zip(lo, hi)]
            out = drv([f"T {h} {a} {b} {mid} {p*f!r}" for (h, a, b, p), f in zip(live, mids)])
            for i, o in enumerate(out):
                if int(o.split()[6]) == 1: hi[i] = mids[i]
                else: lo[i] = mids[i]
        byh = defaultdict(list)
        for (h, a, b, p), f in zip(live, hi): byh[h].append(f - 1)
        print(f"  midp={mid}: flip threshold / exact p - 1, by heterozygote count (0 = correct; negative = removed although p > threshold)")
        for h in sorted(byh):
            v = byh[h]; bad = [x for x in v if abs(x) > 1e-9]
            print(f"    hets={h}: {len(v):5d} tables, wrong boundary: {len(bad):5d}; offset range [{min(v):+.2e}, {max(v):+.2e}]; median wrong offset {sorted(bad)[len(bad)//2] if bad else 0:+.2e}")
else:
    print("(set STATS_DRIVER19 to the driver binary for part A)")

print("\n== B. command line")
rng = np.random.default_rng(0)
n = 6
# variant 1: counts hets=2, hom(A)=2, hom(T)=2 ; variants 2-5: filler in HWE
g = np.array([[0, 0, 1, 1, 2, 2]]).T.astype(np.int8)
filler = (rng.random((n, 4)) < 0.5).astype(np.int8) + (rng.random((n, 4)) < 0.5).astype(np.int8)
g = np.hstack([g, filler])
p_exact = hwe_p(2, 2, 2)
print(f"variant snp1 genotype counts: hets 2, hom 2, hom 2; exact HWE p = {p_exact} = {float(p_exact):.6f}")
with tempfile.TemporaryDirectory() as tmp:
    pre = write_pedmap(os.path.join(tmp, "d"), g)
    run(PLINK19, ["--file", pre, "--hardy", "--out", os.path.join(tmp, "h")])
    t = read_table(os.path.join(tmp, "h.hwe"))
    print(f"plink 1.9 --hardy: snp1 P = {t['P'][0]}  (GENO {t['GENO'][0]})")
    for thr in ("0.48", "0.4805", "0.48052", "0.4806", "0.5"):
        run(PLINK19, ["--file", pre, "--hwe", thr, "--write-snplist", "--out", os.path.join(tmp, "w")])
        kept = [l.strip() for l in open(os.path.join(tmp, "w.snplist"))]
        run(PLINK2, ["--pedmap", pre, "--hwe", thr, "--write-snplist", "--out", os.path.join(tmp, "w2")])
        kept2 = [l.strip() for l in open(os.path.join(tmp, "w2.snplist"))]
        verdict = lambda k: "removed" if "snp1" not in k else "kept"
        expect = "removed" if p_exact < Fraction(thr) else "kept"
        print(f"  --hwe {thr:8s}: plink 1.9 {verdict(kept):8s} plink2 {verdict(kept2):8s} expected {expect}")
    # a larger, realistic table: hets 2, rare hom 5, common hom 1000
    g2 = np.zeros((1007, 3), np.int8); g2[:2, 0] = 1; g2[2:7, 0] = 2
    g2[:, 1:] = (rng.random((1007, 2)) < 0.3).astype(np.int8) + (rng.random((1007, 2)) < 0.3).astype(np.int8)
    p2 = hwe_p(2, 5, 1000)
    pre = write_pedmap(os.path.join(tmp, "e"), g2)
    run(PLINK19, ["--file", pre, "--hardy", "--out", os.path.join(tmp, "h2")])
    t = read_table(os.path.join(tmp, "h2.hwe"))
    print(f"\nvariant with hets 2, hom 5, hom 1000 (n = 1007): exact p = {float(p2):.10g}; plink 1.9 --hardy P = {t['P'][0]}")
    for f in (1 - 3e-5, 1 - 6e-5, 1 - 1e-4, 1 - 2e-4):
        thr = f"{float(p2) * f:.12g}"
        run(PLINK19, ["--file", pre, "--hwe", thr, "--write-snplist", "--out", os.path.join(tmp, "w")])
        kept = [l.strip() for l in open(os.path.join(tmp, "w.snplist"))]
        run(PLINK2, ["--pedmap", pre, "--hwe", thr, "--write-snplist", "--out", os.path.join(tmp, "w2")])
        kept2 = [l.strip() for l in open(os.path.join(tmp, "w2.snplist"))]
        print(f"  --hwe {thr} (= p * {f:.5f}): plink 1.9 {'removed' if 'snp1' not in kept else 'kept':8s} plink2 {'removed' if 'snp1' not in kept2 else 'kept':8s} expected kept")
