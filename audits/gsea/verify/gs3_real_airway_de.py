import pandas as pd, numpy as np, sys
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
D = "/tmp/gs3real/data"
cnt = pd.read_csv(f"{D}/airway_counts.csv", index_col=0)
meta = pd.read_csv(f"{D}/airway_meta.csv", index_col=0)
print("counts", cnt.shape, "all-zero genes", int((cnt.sum(axis=1) == 0).sum()))
dds = DeseqDataSet(counts=cnt.T, metadata=meta, design="~cell + dex", quiet=True)
dds.deseq2()
st = DeseqStats(dds, contrast=["dex", "trt", "untrt"], quiet=True)
st.summary()
res = st.results_df
res.to_csv(f"{D}/airway_deseq2_results.csv")
z = cnt.index[cnt.sum(axis=1) == 0]
print("rows in results:", len(res), " all-zero genes present in results:", res.index.isin(z).sum())
print("all-zero rows look like:"); print(res.loc[res.index.isin(z)].head(3))
print("NaN counts per column:"); print(res.isna().sum())
print("exact-zero stat:", int((res['stat'] == 0).sum()), " exact-zero LFC:", int((res['log2FoldChange'] == 0).sum()))
print("padj non-NA (tested):", int(res['padj'].notna().sum()))
