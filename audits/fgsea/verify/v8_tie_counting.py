"""Exact (integer) ES for every k-subset vs fgsea's floating ES; how many exact ties fgsea's
comparison misses, and the resulting p-values (v8_tie_counting.R output)."""
import sys, json, itertools
from fractions import Fraction
import numpy as np

def exact_es(w, pos, N):
    k = len(pos); NR = sum(w[p] for p in pos); best_p = Fraction(0); best_n = Fraction(0); c = 0
    for j, p in enumerate(pos):
        m = p - j                                        # misses before this hit
        bottom = Fraction(c, NR) - Fraction(m, N - k)
        c += w[p]
        top = Fraction(c, NR) - Fraction(m, N - k)
        best_p = max(best_p, top); best_n = min(best_n, bottom)
    return best_p if best_p > -best_n else (best_n if best_p < -best_n else Fraction(0))

for lab in sys.argv[2:]:
    J = json.load(open(f"{sys.argv[1]}/v8_{lab}.json"))
    print(f"\n=== fgsea {J['version']} ({lab}) ===")
    for dn, D in J["designs"].items():
        N, k, w = D["N"], D["k"], [int(x) for x in D["w"]]
        subsets = list(itertools.combinations(range(N), k))
        ex = [exact_es(w, s, N) for s in subsets]
        fl = np.array([float(x) for x in D["es"]])
        n_ge0 = sum(1 for e in ex if e >= 0); n_le0 = sum(1 for e in ex if e <= 0)
        for key, o in D["obs"].items():
            pos = tuple(x - 1 for x in o["members"]); i = subsets.index(pos)
            e0 = ex[i]; f0 = fl[i]
            if e0 < 0:
                n_exact = sum(1 for e in ex if e <= e0); n_float = int(np.sum(fl <= f0)); den = n_le0
            else:
                n_exact = sum(1 for e in ex if e >= e0); n_float = int(np.sum(fl >= f0)); den = n_ge0
            ties = sum(1 for e in ex if e == e0)
            ties_float_equal = int(np.sum(fl == f0))
            print(f"{dn} set {key:>12}: ES = {float(e0):+.6f} (exact {e0}); {ties} subsets tie exactly, fgsea's doubles equal for {ties_float_equal}; "
                  f"subsets counted as at least as extreme: exact {n_exact}, by fgsea's comparison {n_float}")
            print(f"{'':>22} p exact (same sign) = {n_exact/den:.5g}; fgsea's own ES values give {n_float/den:.5g} (x{n_float/n_exact:.3f}); "
                  f"fgseaSimple 1e6 perms: alone (R path) {o['simple_R_p']:.5g}, with a second set (C++ path) {o['simple_Cpp_p']:.5g}; fgseaMultilevel {o['multilevel_p']:.5g}")
