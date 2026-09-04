#!/usr/bin/env python3
"""PL1: PLINK 1.9 --hwe removes variants whose exact HWE p-value is ABOVE the
threshold when the variant has 2 or 3 heterozygotes (and in a few other shapes).

Mechanism (1.9/plink_stats.c, SNPHWE_t and SNPHWE_midp_t): after the centre of
the het-count distribution is summed, the tail containing the observed count is
extended by one element (P(hets-2), or P(hets+2) in the upper-tail branch) but the
loop that compares the running tail sum against the pass threshold is only entered
for obs_hets >= 4 (lower branch) / obs_homr > 1 (upper branch).  For the skipped
cases the only remaining comparison sits inside the *other* tail's loop, which
executes zero times whenever that tail has at most one element -- always the case
for 2 heterozygotes -- so the function falls through to `return 1` (fail) without
ever counting the second element.  The filter therefore acts on
p - P(hets-2) instead of p.

Part A (function level): the shipped SNPHWE_t / SNPHWE_midp_t, linked from the
checked build's objects into stats_driver19, is queried for every genotype table
with n <= NMAX and hets <= HMAX; the threshold at which the verdict flips is found
by bisection and compared with the exact p (fractions.Fraction reference).  A
correct filter flips exactly at p (offset 0); a negative offset means the variant
is removed at thresholds below its p.  The same for plink2's HweThreshLn through
stats_driver2 (control: expected 0 wrong).
Part B (command line): --hardy prints the p, --hwe with a threshold just below it
removes the variant in plink 1.9 and keeps it in plink2.

Usage: pl1_hwe_threshold_boundary.py [NMAX] [HMAX]; env STATS_DRIVER19, STATS_DRIVER2,
PLINK19, PLINK2.
"""
import os, sys, subprocess, tempfile
from collections import defaultdict
from fractions import Fraction
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import write_pedmap, run, read_table, PLINK19, PLINK2, version, SCRATCH
from exact_ref import hwe_p, hwe_dist

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
HMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 6
print(version(PLINK19)); print(version(PLINK2))

def bisect_flip(drv, label):
    def q(qs):
        return subprocess.run([drv], input="\n".join(qs) + "\n", capture_output=True, text=True).stdout.splitlines()
    tables = [(h, a, n - h - a) for n in range(2, NMAX + 1) for h in range(min(n, HMAX) + 1) for a in range(n - h + 1) if a <= n - h - a]
    print(f"\n== {label}: bisection of the flip threshold, n <= {NMAX}, hets <= {HMAX} exhaustive ({len(tables)} tables)")
    for mid in (0, 1):
        live = [(h, a, b, float(hwe_p(h, a, b, bool(mid)))) for h, a, b in tables]
        live = [t for t in live if 0 < t[3] < (0.5 if mid else 1)]      # midp function assumes thresh < 0.5
        lo, hi = [0.5] * len(live), [1.5] * len(live)
        for _ in range(42):
            mids = [(l + u) / 2 for l, u in zip(lo, hi)]
            out = q([f"T {h} {a} {b} {mid} {p*f!r}" for (h, a, b, p), f in zip(live, mids)])
            for i, o in enumerate(out):
                if int(o.split()[6]) == 1: hi[i] = mids[i]
                else: lo[i] = mids[i]
        byh = defaultdict(list); worst = (0, None)
        for (h, a, b, p), f in zip(live, hi):
            byh[h].append(f - 1)
            if f - 1 < worst[0]: worst = (f - 1, (h, a, b, p))
        print(f"  midp={mid}: flip threshold / exact p - 1 by heterozygote count (0 = correct; < 0 = removed although p > threshold)")
        tot_bad = 0
        for h in sorted(byh):
            v = byh[h]; bad = [x for x in v if abs(x) > 1e-9]; tot_bad += len(bad)
            print(f"    hets={h}: {len(v):6d} tables, wrong boundary: {len(bad):6d}; offset range [{min(v):+.2e}, {max(v):+.2e}]; median wrong offset {sorted(bad)[len(bad)//2] if bad else 0:+.2e}")
        if worst[1] is None:
            print(f"    total wrong: {tot_bad} of {len(live)}; no negative offset")
        else:
            print(f"    total wrong: {tot_bad} of {len(live)}; largest offset {worst[0]:+.3e} at (hets, hom1, hom2) = {worst[1][:3]} with p = {worst[1][3]:.4g}")
        # for hets = 2 the offset should equal -P(0)/(tail sum) = -(P(0)/P(2)) / (p / P(2)) : check on the hets=2 tables
        if not mid:
            worst_chk = 0.0
            for (h, a, b, p), f in zip(live, hi):
                if h == 2:
                    n = h + a + b; rare = 2 * min(a, b) + h; homr, homc = min(a, b), max(a, b)
                    d = hwe_dist(n, rare)
                    predicted = -float(d[0] / (p if p else 1)) if 0 in d else 0.0
                    worst_chk = max(worst_chk, abs((f - 1) - predicted))
            print(f"    hets=2 tables: max |offset - (-P(hets=0)/p)| = {worst_chk:.1e}  (the omitted tail element explains the offset)")

DRV19 = os.environ.get("STATS_DRIVER19", os.path.join(SCRATCH, "drivers/stats_driver19_new"))
DRV2 = os.environ.get("STATS_DRIVER2", os.path.join(SCRATCH, "drivers/stats_driver2_new"))
if os.path.exists(DRV19): bisect_flip(DRV19, "plink 1.9 SNPHWE_t / SNPHWE_midp_t (stats_driver19, shipped objects)")
else: print("(no STATS_DRIVER19; part A skipped)")
if os.path.exists(DRV2): bisect_flip(DRV2, "plink2 HweThreshLn (stats_driver2, shipped objects) -- control")
else: print("(no STATS_DRIVER2; plink2 control skipped)")

print("\n== B. command line")
rng = np.random.default_rng(0)
def cli(g, tag, thr_list, expect_kept_fn):
    with tempfile.TemporaryDirectory() as tmp:
        pre = write_pedmap(os.path.join(tmp, "d"), g)
        run(PLINK19, ["--file", pre, "--hardy", "--out", os.path.join(tmp, "h")])
        t = read_table(os.path.join(tmp, "h.hwe"))
        run(PLINK19, ["--file", pre, "--hardy", "midp", "--out", os.path.join(tmp, "hm")])
        tm = read_table(os.path.join(tmp, "hm.hwe"))
        print(f"{tag}: plink 1.9 --hardy P = {t['P'][0]}, --hardy midp P = {tm['P'][0]} (GENO {t['GENO'][0]})")
        for thr, mid in thr_list:
            mods = ["midp"] if mid else []
            run(PLINK19, ["--file", pre, "--hwe", thr, *mods, "--write-snplist", "--out", os.path.join(tmp, "w")])
            kept = [l.strip() for l in open(os.path.join(tmp, "w.snplist"))]
            run(PLINK2, ["--pedmap", pre, "--hwe", thr, *mods, "--write-snplist", "--out", os.path.join(tmp, "w2")])
            kept2 = [l.strip() for l in open(os.path.join(tmp, "w2.snplist"))]
            v = lambda k: "removed" if "snp1" not in k else "kept"
            print(f"  --hwe {thr:<22s}{'midp ' if mid else '     '}: plink 1.9 {v(kept):8s} plink2 {v(kept2):8s} expected {expect_kept_fn(thr, mid)}")

# table 1: hets 2, hom 2, hom 2 (n = 6); exact p = 185/385
g = np.array([[0, 0, 1, 1, 2, 2]]).T.astype(np.int8)
g = np.hstack([g, (rng.random((6, 4)) < 0.5).astype(np.int8) + (rng.random((6, 4)) < 0.5).astype(np.int8)])
p, pm = hwe_p(2, 2, 2), hwe_p(2, 2, 2, True)
d6 = hwe_dist(6, 6)
print(f"table (hets 2, hom 2, hom 2): exact p = {p} = {float(p):.6f}; mid-p = {pm} = {float(pm):.6f}; het-count distribution {{h: str(v) for h, v in d6.items()}}")
print(f"  omitted tail element P(hets=0) = {d6[0]} = {float(d6[0]):.5f}; p - P(0) = {float(p - d6[0]):.5f}, so thresholds in ({float(p - d6[0]):.4f}, {float(p):.4f}) remove the variant")
cli(g, "n = 6", [("0.48", 0), ("0.46", 0), ("0.45", 0), ("0.4805", 0), ("0.4806", 0), ("0.3", 1), ("0.29", 1), ("0.28", 1)],
    lambda thr, mid: "removed" if (pm if mid else p) < Fraction(thr) else "kept")
# table 2: hets 2, hom 5, hom 1000 (n = 1007), a realistic rare-variant shape
g2 = np.zeros((1007, 3), np.int8); g2[:2, 0] = 1; g2[2:7, 0] = 2
g2[:, 1:] = (rng.random((1007, 2)) < 0.3).astype(np.int8) + (rng.random((1007, 2)) < 0.3).astype(np.int8)
p2, p2m = hwe_p(2, 5, 1000), hwe_p(2, 5, 1000, True)
omitted = Fraction(2, 4 * 6 * 1001)   # P(0)/P(2)
print(f"\ntable (hets 2, hom 5, hom 1000): exact p = {float(p2):.10g}; mid-p = {float(p2m):.10g}; P(0)/P(2) = {float(omitted):.3e}")
thr = [(f"{float(p2) * (1 - f):.12g}", 0) for f in (1e-5, 3e-5, 6e-5, 1e-4, 2e-4)] + [(f"{float(p2m) * (1 - f):.12g}", 1) for f in (3e-5, 1e-4)]
cli(g2, "n = 1007", thr, lambda t, m: "kept")
# table 3: hets 3, hom 4, hom 300
g3 = np.zeros((307, 3), np.int8); g3[:3, 0] = 1; g3[3:7, 0] = 2
g3[:, 1:] = (rng.random((307, 2)) < 0.3).astype(np.int8) + (rng.random((307, 2)) < 0.3).astype(np.int8)
p3 = hwe_p(3, 4, 300)
print(f"\ntable (hets 3, hom 4, hom 300): exact p = {float(p3):.10g}; P(1)/P(3) = {float(Fraction(6, 4*5*301)):.3e}")
cli(g3, "n = 307", [(f"{float(p3) * (1 - f):.12g}", 0) for f in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2)], lambda t, m: "kept")
