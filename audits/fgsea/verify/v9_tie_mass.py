"""How much of a permutation tail is an exact tie, for gene sets whose ES sits at the first hit
(ES = -(S1 - 1)/(N - k)), on lists of realistic length?  fgseaSimple and the simple stage of
fgseaMultilevel drop most of these ties (v8_tie_counting); this measures what is at stake.
Monte Carlo over uniformly random gene sets; bottoms are computed from the previous cumulative
sum so that ES at the first hit is the same double for every set (exact ties preserved)."""
import numpy as np
rng = np.random.default_rng(99)

def es_batch(w, P, n):
    k = P.shape[1]; rw = w[P]; NR = rw.sum(1, keepdims=True)
    cum = np.cumsum(rw, 1); prev = cum - rw; prev[:, 0] = 0.0
    mis = P - np.arange(k)[None, :]
    tops = cum / NR - mis / (n - k); bots = prev / NR - mis / (n - k)
    mx = tops.max(1); mn = np.minimum(bots.min(1), 0)
    return np.where(mx > -mn, mx, np.where(mx < -mn, mn, 0.0)), (bots.argmin(1) == 0)

def sample(n, k, B):
    out = []
    while sum(len(x) for x in out) < B:
        P = np.sort(rng.integers(0, n, size=(200000, k)), 1)
        ok = (np.diff(P, axis=1) > 0).all(1); out.append(P[ok])
    return np.concatenate(out)[:B]

print(f"{'N':>6} {'k':>3} {'S1':>6} {'ES':>8} {'P(ES*<=ES | ES*<=0)':>20} {'tied share of tail':>18} {'p if 2/3 of ties dropped':>24}")
for n, k, fracs in [(500, 15, [0.35, 0.45, 0.55]), (2000, 15, [0.35, 0.45, 0.55]), (10000, 15, [0.35, 0.45]), (20000, 50, [0.25, 0.3])]:
    z = np.sort(rng.standard_normal(n))[::-1]; w = np.abs(z)
    B = 2_000_000 if n <= 2000 else 600_000
    es, at1 = es_batch(w, sample(n, k, B), n)
    for f in fracs:
        s1 = int(n * f); es0 = -(s1) / (n - k)            # first member at 0-based position s1
        neg = es <= 0
        tail = np.sum(es <= es0 + 1e-15); tie = np.sum(np.abs(es - es0) < 1e-15)
        p = tail / neg.sum(); share = tie / max(tail, 1)
        print(f"{n:>6} {k:>3} {s1+1:>6} {es0:8.4f} {p:20.4g} {share:18.3%} {p*(1-2/3*share):24.4g}")
