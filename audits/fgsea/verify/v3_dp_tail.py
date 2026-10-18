"""fgseaMultilevel p-values against an EXACT tail probability on realistic-length lists.

Truth: the ranked list has small positive integer weights (|stat| in 1..4, n = 1000), so fgsea's
integer scaling is exact and P(ES+* >= ES+) over all C(n, k) gene sets is computed exactly by
dynamic programming (_ref.dp_tail_pos, checked against brute force in dp_selftest.py).
For scoreType = "pos" fgsea's p is that unconditional tail.  For "std" and ES > 0.5,
ES+ >= ES implies |ES-| <= 1 - ES < ES, so P(ES* >= ES) = P(ES+* >= ES) and the documented p is
that divided by P(ES* >= 0) (estimated here from 4e6 random sets; SE ~ 0.05 %).

Usage:  python3 v3_dp_tail.py make <dir>     -> <dir>/v3_spec.json (stats, sets, truth)
        python3 v3_dp_tail.py compare <dir> <label> [<label> ...]   (reads <dir>/v3_<label>.json)
"""
import sys, json, math, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from _ref import dp_tail_pos, es_all, batch_es

N = 1000

def make(d):
    rng = np.random.default_rng(20261018)
    z = np.sort(rng.standard_normal(N))[::-1]
    mag = np.clip(np.ceil(np.abs(z) * 1.5), 1, 4).astype(int)
    stats = (np.sign(z) * mag).astype(int)
    stats[stats == 0] = 1
    w = np.abs(stats)
    sets = []
    for k in (15, 40):
        # members spread evenly over the top L positions; L controls the p-value
        for L in ([k, 2 * k, 40, 60, 100, 160, 250, 400] if k == 15 else [k, 60, 100, 160, 250, 400]):
            if L < k:
                continue
            pos = sorted(set(np.linspace(0, L - 1, k).round().astype(int).tolist()))
            if len(pos) != k:
                continue
            sets.append({"name": f"k{k}_top{L}", "k": k, "pos": pos})
        # and a mirrored negative set for the std path
        L = 100
        pos = sorted(set((N - 1 - np.linspace(0, L - 1, k).round().astype(int)).tolist()))
        sets.append({"name": f"k{k}_bottom{L}", "k": k, "pos": pos})
    # P(ES* >= 0) and P(ES* <= 0) per k (Monte Carlo, 4e6 sets)
    denom = {}
    for k in (15, 40):
        cnt_ge = cnt_le = tot = 0
        for _ in range(40):
            P = np.sort(np.argsort(rng.random((100000, N)), axis=1)[:, :k], axis=1) if False else \
                np.sort(np.array([rng.choice(N, k, replace=False) for _ in range(1)]), axis=1)
            break
        # faster sampler: random keys, take k smallest
        B = 100000
        for _ in range(40):
            keys = rng.random((B, N))
            P = np.sort(np.argpartition(keys, k, axis=1)[:, :k], axis=1)
            s, p, m = batch_es(w, P, N)
            cnt_ge += int((s >= 0).sum()); cnt_le += int((s <= 0).sum()); tot += B
        denom[k] = {"ge0": cnt_ge / tot, "le0": cnt_le / tot, "n": tot}
        print("k", k, denom[k], flush=True)
    for st in sets:
        k = st["k"]
        std, esp, esn = es_all(w, st["pos"], N)
        st["ES_ref"] = std
        if std > 0:
            tail = dp_tail_pos(w, N, k, st["pos"])
            st["p_pos_exact"] = tail
            st["p_std_exact"] = tail / denom[k]["ge0"] if std > 0.5 else None
        else:
            # mirror: reversed list, ES+ of the reversed positions = |ES-| here
            wr = w[::-1].copy(); posr = sorted(N - 1 - np.array(st["pos"]))
            tail = dp_tail_pos(wr, N, k, posr)
            st["p_neg_exact"] = tail
            st["p_std_exact"] = tail / denom[k]["le0"] if -std > 0.5 else None
        print(st["name"], "ES", round(std, 6), "exact", {kk: v for kk, v in st.items() if kk.startswith("p_")}, flush=True)
    names = [f"g{i:04d}" for i in range(N)]
    json.dump({"stats": stats.tolist(), "names": names, "sets": sets, "denom": denom}, open(f"{d}/v3_spec.json", "w"))

def compare(d, labels):
    spec = json.load(open(f"{d}/v3_spec.json"))
    for lab in labels:
        res = json.load(open(f"{d}/v3_{lab}.json"))
        print(f"\n=== fgsea {res['version']} ({lab}); {res['reps']} runs per set, eps = 0, sampleSize = 101 ===")
        print(f"{'set':>14} {'ES':>8} {'type':>4} {'p exact':>10} {'median p':>10} {'gmean p':>10} {'gm/exact':>8} {'min':>9} {'max':>9} {'med log2err':>11} {'|dlog2|<=2err':>13}")
        for st in spec["sets"]:
            r = res["sets"][st["name"]]
            for typ, key in (("pos", "p_pos_exact"), ("std", "p_std_exact")):
                if typ not in r or st.get(key) is None:
                    continue
                pv = np.array(r[typ]["pval"], dtype=float); le = np.array([np.nan if x is None else x for x in r[typ]["log2err"]], dtype=float)
                ex = st[key]
                gm = float(np.exp(np.mean(np.log(pv))))
                dl = np.abs(np.log2(pv) - math.log2(ex))
                cover = np.mean(dl <= 2 * le) if np.isfinite(le).any() else float('nan')
                print(f"{st['name']:>14} {r['ES']:8.5f} {typ:>4} {ex:10.3e} {np.median(pv):10.3e} {gm:10.3e} {gm/ex:8.3f} {pv.min():9.2e} {pv.max():9.2e} {np.nanmedian(le) if np.isfinite(le).any() else float('nan'):11.3f} {cover:13.2f}")
            if abs(r["ES"] - st["ES_ref"]) > 1e-6:
                print("   ES MISMATCH", r["ES"], st["ES_ref"])
        if "pos" in r and st.get("p_pos_exact") is not None:
            pass

if __name__ == "__main__":
    if sys.argv[1] == "make":
        make(sys.argv[2])
    else:
        compare(sys.argv[2], sys.argv[3:])
