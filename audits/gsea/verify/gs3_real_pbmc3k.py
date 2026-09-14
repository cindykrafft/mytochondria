#!/usr/bin/env python3
"""GS3 precondition on a real single-cell dataset: 10x PBMC 3k (2,638 cells, 13,714 genes after
the scanpy tutorial's min_cells=3 filter, eight Louvain cell types), as shipped in
chanzuckerberg/cellxgene `example-dataset/pbmc3k.h5ad`.

For every cell type versus the rest and for every pair of cell types, a Seurat-style
avg_log2FC ranking over all 13,714 genes (log2(mean(expm1)+1) difference, which is exactly 0
for a gene absent from both groups, as FindMarkers reports with logfc.threshold = 0 and
min.pct = 0), then for every MSigDB 7.5.1 collection the number of sets with 15..500 members
present whose members are all at 0 (the GS3 condition), and how close the nearest sets come.
Needs the h5ad and the msigdb_*.gmt files under /tmp/gs3real/data (see gs3_real_airway.py).
"""
import glob, os, itertools, warnings
import numpy as np, pandas as pd, scipy.sparse as sp, scanpy as sc
warnings.filterwarnings("ignore")
D = "/tmp/gs3real/data"
a = sc.read_h5ad(f"{D}/pbmc3k.h5ad"); r = a.raw.to_adata()
X = r.X.toarray() if sp.issparse(r.X) else r.X
genes = np.array(r.var_names); lab = a.obs["louvain"].astype(str).values; E = np.expm1(X)
present = set(genes)
colls = sorted(os.path.basename(f)[7:-4] for f in glob.glob(f"{D}/msigdb_*.gmt"))
memb = {}
for coll in colls:
    d = {l.split("\t")[0]: [g for g in l.rstrip("\n").split("\t")[2:] if g in present] for l in open(f"{D}/msigdb_{coll}.gmt")}
    memb[coll] = {n: g for n, g in d.items() if 15 <= len(g) <= 500}
print(f"PBMC3k: {len(genes)} genes, {len(set(lab))} cell types; MSigDB sets with 15..500 present members: {sum(len(d) for d in memb.values())}")
show = ["H", "C2_CP_KEGG", "C2_CP_REACTOME", "C5_GO_BP", "C5_GO_CC", "C5_GO_MF", "C8", "C7_IMMUNESIGDB"]
def rank(m1, m2):
    return pd.Series(np.log2(E[m1].mean(0) + 1) - np.log2(E[m2].mean(0) + 1), index=genes).sort_values(ascending=False)
def report(label, s):
    zero = set(s.index[s == 0])
    counts = {coll: sum(all(x in zero for x in g) for g in d.values()) for coll, d in memb.items()}
    fr = max((sum(x in zero for x in g) / len(g), n) for d in memb.values() for n, g in d.items())
    print(f"{label:42s} {len(zero):6d} zeros ({100*len(zero)/len(s):4.1f} %)  all-zero sets: {sum(counts.values()):3d} "
          f"[{' '.join(f'{c[:8]}={counts[c]}' for c in show)}]  nearest {fr[0]:.2f} ({fr[1][:40]})")
print("\ncell type vs rest:")
for ct in sorted(set(lab)):
    report(ct, rank(lab == ct, lab != ct))
print("\npairwise:")
for c1, c2 in itertools.combinations(sorted(set(lab)), 2):
    report(f"{c1} vs {c2}", rank(lab == c1, lab == c2))
