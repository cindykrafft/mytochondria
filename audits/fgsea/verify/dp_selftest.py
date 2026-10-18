"""Check the DP tail probability against brute-force enumeration on small lists."""
import sys, itertools, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from _ref import dp_tail_pos, exact_null, es_all
rng = np.random.default_rng(3)
for n, k in [(18, 3), (22, 4), (26, 5)]:
    w = np.sort(rng.integers(1, 5, n))[::-1].copy()
    null_std, null_pos, null_neg = exact_null(w, n, k)
    for obs in [list(range(k)), [0, 1, 5, 9, 12][:k], list(range(n - k, n)), [2, 7, 11, 15, 17][:k]]:
        e = es_all(w, obs, n)[1]
        if e <= 0:
            continue
        brute = np.mean(null_pos >= e - 1e-12)
        dp = dp_tail_pos(w, n, k, obs)
        print(f"n={n} k={k} obs={obs} ES+={e:.6f} brute={brute:.10g} dp={dp:.10g} rel.diff={abs(dp-brute)/brute:.2e}")
