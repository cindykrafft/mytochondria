#!/usr/bin/env python3
"""AF1: faithful port of AFNI's CalcRanksForReHo / ReHoIt, buggy vs fixed.

Ports src/ptaylor/rsfc.c exactly, INCLUDING the trailing tie-run that the C loop
never closes (AF1b) -- that detail is not cosmetic, it is what makes the error
curve non-monotonic and what exonerates L2-normalised input.

    python3 reho_tie_sim.py          # all three tables
    python3 reho_tie_sim.py --json   # machine-readable

Needs numpy only. Results are checked in as reho_tie_results.json.
"""
import json, sys
import numpy as np

rng = np.random.default_rng(0)


CLOSE_TAIL = False   # True models commit 29384a2 (merged 2026-08-27), which closes a tie run at the end


def ranks_and_ties(ts, truncate, close_tail=None):
    """rsfc.c:79-118. Returns (ranks, T) with T = sum len*(len^2-1)."""
    if close_tail is None:
        close_tail = CLOSE_TAIL
    N = len(ts)
    P = np.argsort(ts, kind="stable")          # gsl_sort_vector_index
    IND = np.empty(N)
    IND[P] = np.arange(1, N + 1)
    # THE BUG: `int *sorted` receives a float from THD_get_voxel()
    s = np.trunc(ts[P]).astype(np.int64) if truncate else ts[P]
    T = 0
    istie, lentie = -1, 0
    for m in range(1, N):
        if s[m] == s[m - 1] and lentie == 0:
            istie, lentie = m - 1, 2
        elif s[m] == s[m - 1] and lentie > 0:
            lentie += 1
        elif s[m] != s[m - 1] and lentie > 0:
            tr = istie + 0.5 * (lentie - 1)
            T += lentie * (lentie * lentie - 1)
            for mm in range(lentie):
                IND[P[istie + mm]] = tr + 1
            istie, lentie = -1, 0
    # AF1b: in the code shipped in every AFNI release through 26.2.03 a run reaching
    # the end of the array is never finalized. Commit 29384a2 (authored 2023-09-27,
    # merged to master only on 2026-08-27, one day before the float fix) closes it;
    # with integer truncation still in place that makes every series lying inside one
    # integer bin a single full-length tie, the denominator becomes exactly zero and
    # ReHo is NaN. close_tail=True models that one-day state.
    if close_tail and lentie > 0:
        tr = istie + 0.5 * (lentie - 1)
        T += lentie * (lentie * lentie - 1)
        for mm in range(lentie):
            IND[P[istie + mm]] = tr + 1
    return IND, T


def reho(block, truncate, close_tail=None):
    """rsfc.c:164-199 (ReHoIt). block is M voxels x N time points."""
    M, N = block.shape
    R = np.empty((M, N))
    Tfac = 0
    for i in range(M):
        r, T = ranks_and_ties(block[i], truncate, close_tail)
        R[i] = r
        Tfac += T
    bigR = ((R.sum(axis=0)) ** 2).sum()
    num = 12.0 * bigR - M * M * N * 3 * (N + 1) ** 2
    den = M * M * N * (N * N - 1) - M * Tfac
    return num / den if den != 0 else float("nan")


def make(M, N, rho=0.6):
    """A neighbourhood with a shared signal, giving a realistic true W."""
    c = rng.standard_normal(N)
    return np.sqrt(rho) * c + np.sqrt(1 - rho) * rng.standard_normal((M, N))


M, N, NSIM = 27, 200, 40
out = {"config": {"neighbourhood": M, "timepoints": N, "sims_per_point": NSIM,
                  "true_W_target": 0.60}}

# 1. error vs data scale
scale_rows = []
for sd in [0.05, 0.1, 0.25, 0.5, 0.75, 1, 1.5, 2, 3, 5, 10, 50, 1000]:
    t, b = [], []
    for _ in range(NSIM):
        blk = sd * make(M, N)
        t.append(reho(blk, False)); b.append(reho(blk, True))
    t, b = np.array(t), np.array(b)
    scale_rows.append({"sd": sd, "true_W": round(float(np.nanmean(t)), 4),
                       "buggy_W": round(float(np.nanmean(b)), 4),
                       "rel_err_pct": round(float(np.nanmean(np.abs(b - t) / t) * 100), 1)})
out["error_vs_scale"] = scale_rows

# 2. realistic pipeline configurations
cases = [
 ("raw EPI, mean 1000, 1% fluctuation",        lambda z: 1000 + 10 * z),
 ("grand-mean scaled to 10,000 (CCS/PhiPipe/HALFpipe/FSL)", lambda z: 10000 + 100 * z),
 ("afni_proc.py scale block: mean 100, SD 1",  lambda z: 100 + z),
 ("afni_proc.py errts residuals: mean 0, SD 1", lambda z: z),
 ("z-scored time series (SD 1)",               lambda z: z),
 ("L2-normalised, 3dTproject -norm",
  lambda z: z / np.sqrt((z ** 2).sum(axis=-1, keepdims=True))),
]
cfg_rows = []
for lab, f in cases:
    t, b = [], []
    for _ in range(NSIM):
        blk = f(make(M, N))
        t.append(reho(blk, False)); b.append(reho(blk, True))
    t, b = np.array(t), np.array(b)
    cfg_rows.append({"config": lab, "true_W": round(float(np.nanmean(t)), 4),
                     "buggy_W": round(float(np.nanmean(b)), 4),
                     "abs_err": round(float(np.nanmean(np.abs(b - t))), 4)})
out["configurations"] = cfg_rows

# 3. AF1c: the bug makes ReHo a partial function of BOLD amplitude
amp_rows = []
for sd in [0.3, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0]:
    t, b = [], []
    for _ in range(60):
        blk = sd * make(M, N, 0.6)
        t.append(reho(blk, False)); b.append(reho(blk, True))
    amp_rows.append({"sd": sd, "true_W": round(float(np.nanmean(t)), 4),
                     "buggy_W": round(float(np.nanmean(b)), 4)})
out["amplitude_confound"] = amp_rows

a = np.array([reho(1.00 * make(M, N, 0.6), True) for _ in range(120)])
c = np.array([reho(0.75 * make(M, N, 0.6), True) for _ in range(120)])
d = (a.mean() - c.mean()) / np.sqrt((a.var() + c.var()) / 2)
out["spurious_group_difference"] = {
    "note": "identical true ReHo, 25% difference in BOLD amplitude",
    "group_A_sd": 1.0, "group_B_sd": 0.75,
    "buggy_W_A": round(float(a.mean()), 4), "buggy_W_B": round(float(c.mean()), 4),
    "cohens_d": round(float(d), 2), "true_cohens_d": 0.0}

if "--json" in sys.argv:
    print(json.dumps(out, indent=1)); sys.exit()

print("AF1  error vs data scale (mean-0 data)")
print(f"{'SD':>8} {'true W':>9} {'buggy W':>9} {'rel err':>9}")
for r in out["error_vs_scale"]:
    print(f"{r['sd']:8} {r['true_W']:9.4f} {r['buggy_W']:9.4f} {r['rel_err_pct']:8.1f}%")
print("\nAF1  realistic pipeline configurations")
for r in out["configurations"]:
    print(f"  {r['config']:56s} true={r['true_W']:.4f} buggy={r['buggy_W']:.4f} err={r['abs_err']:.4f}")
print("\nAF1c amplitude confound (true W held at ~0.60)")
for r in out["amplitude_confound"]:
    print(f"  SD={r['sd']:<5} true={r['true_W']:.4f} buggy={r['buggy_W']:.4f}")
g = out["spurious_group_difference"]
print(f"\n  {g['note']}: buggy d = {g['cohens_d']} (true d = 0)")
