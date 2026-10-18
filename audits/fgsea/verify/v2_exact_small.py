"""Exact p and NES (all C(n,k) sets) vs fgsea (v2_exact_small.R output), scoreType std/pos/neg."""
import sys, json, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from _ref import exact_null, es_all, pvals_from_null

def main(d, labels):
    for lab in labels:
        J = json.load(open(f"{d}/v2_{lab}.json"))
        print(f"\n=== fgsea {J['version'][0]} ({lab}): multilevel = geometric mean of 20 runs (eps = 0); simple = 2e5 permutations ===")
        print(f"{'design':>7} {'set':>14} {'type':>4} {'ES':>8} {'ES ref':>8} {'p exact':>10} {'ML p':>10} {'ML/ex':>6} {'simple p':>10} {'S/ex':>6} {'NES exact':>9} {'NES ML':>8} {'NES S':>8}")
        ratios = {"ml": [], "simple": []}
        for dn, rec in J["designs"].items():
            st = rec["stats"]; names = list(st); vals = np.array([st[g][0] for g in names])
            w = np.abs(vals); n = len(w)
            first = next(iter(rec["sets"].values()))
            k = len(first["members"])
            null = exact_null(w, n, k)
            for key, r in rec["sets"].items():
                mem = r["members"]
                std, esp, esn = es_all(w, mem, n)
                for typ, es_ref in (("std", std), ("pos", esp), ("neg", esn)):
                    x = r[typ]
                    pe, nese = pvals_from_null(es_ref, *null, score_type=typ)
                    mlp = np.array(x["ml_p"]); gm = float(np.exp(np.mean(np.log(mlp))))
                    sp = x["simple_p"][0]; nml = float(np.median(x["ml_nes"])); ns = x["simple_nes"][0]
                    ratios["ml"].append(gm / pe); ratios["simple"].append(sp / pe)
                    print(f"{dn:>7} {key:>14} {typ:>4} {x['ES'][0]:8.4f} {es_ref:8.4f} {pe:10.4g} {gm:10.4g} {gm/pe:6.3f} {sp:10.4g} {sp/pe:6.3f} {nese:9.4f} {nml:8.4f} {ns:8.4f}")
        for kx, v in ratios.items():
            v = np.array(v)
            print(f"ratio {kx:>6}/exact: median {np.median(v):.3f}  min {v.min():.3f}  max {v.max():.3f}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
