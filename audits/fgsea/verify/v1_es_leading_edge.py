"""Compare fgsea's ES, size and leadingEdge (v1_es_leading_edge.R output) with _ref.py."""
import sys, json, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from _ref import es_all, leading_edge, running

def main(d, labels):
    for lab in labels:
        J = json.load(open(f"{d}/v1_{lab}.json"))
        print(f"\n=== fgsea {J['version']} ({lab}) ===")
        for key, run in J["runs"].items():
            lst = J["lists"][run["list"]]
            names = list(lst.keys()); vals = np.array([lst[g] for g in names], dtype=float)
            order = np.argsort(-vals, kind="stable")          # decreasing, ties in input order
            sorted_names = [names[i] for i in order]
            posmap = {g: i for i, g in enumerate(sorted_names)}
            p = run["gseaParam"]
            w = np.abs(vals[order]) ** p
            n = len(w)
            es_err = []; le_bad = 0; le_extra = []; size_bad = 0; nsets = len(run["pathway"])
            examples = []
            for i, pwn in enumerate(run["pathway"]):
                mem = sorted({posmap[g] for g in J["pathways"][pwn] if g in posmap})
                if len(mem) != run["size"][i]:
                    size_bad += 1
                std, esp, esn = es_all(w, mem, n)
                ref_es = {"std": std, "pos": esp, "neg": esn}[run["scoreType"]]
                es_err.append(abs(ref_es - run["ES"][i]))
                le_ref = [sorted_names[j] for j in leading_edge(w, mem, n, run["scoreType"])]
                le_f = run["leadingEdge"][i]
                if isinstance(le_f, str):      # auto_unbox turns a one-gene leading edge into a scalar
                    le_f = [le_f]
                if set(le_ref) != set(le_f):
                    le_bad += 1
                    le_extra.append(len(le_f) - len(le_ref))
                    if len(examples) < 2:
                        examples.append((pwn, run["ES"][i], len(le_ref), len(le_f)))
            le_extra = np.array(le_extra)
            sign = {"std": "", "pos": "", "neg": ""}[run["scoreType"]]
            npos = sum(1 for e in run["ES"] if e > 0)
            print(f"{key:>12}: {nsets} sets ({npos} with ES > 0); max |ES - ref| = {max(es_err):.2e}; size mismatches {size_bad}; "
                  f"leadingEdge differs in {le_bad}" + (f" (fgsea minus ref: median {np.median(le_extra):+.0f}, range {le_extra.min():+d}..{le_extra.max():+d} genes; e.g. {examples})" if le_bad else ""))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
