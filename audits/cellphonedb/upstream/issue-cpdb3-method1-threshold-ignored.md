Title: `threshold` has no effect on any output of `cpdb_analysis_method` (METHOD 1)

<!-- ventolab/CellphoneDB has no issue template; this follows the structure of a minimal
     complete verifiable example. -->

**Version:** 5.0.1 (PyPI wheel and `master` @ `dc8abd15`, byte-identical). The same applies to
v4.0.0; v3.1.0 still returned `significant_means` to the caller.

### What the documentation says

`docs/RESULTS-DOCUMENTATION.md:59` (METHOD 1): "Note that CellphoneDB will report the means **only
if** all the gene members of the interactions are expressed by at least a fraction of cells in a
cell type (`threshold`). If the condition `threshold` is not met, the interaction will be ignored
in the corresponding cell type pairs." Line 78 repeats it: "Only interactions involving receptors
and ligands expressed by more than a fraction of the cells (`threshold` default is 0.1, which is
10%) in the specific cluster are included."

### What the code does

`cpdb_analysis_method.call` does compute the percent analysis (lines 134-138) and does pass it to
`build_results`, which uses it to build `significant_means` (lines 240-242) — the only table in
this method that the threshold touches. But the returned dict is then assembled from three other
keys (lines 175-177):

```python
analysis_result['means_result'] = means_result
analysis_result['deconvoluted'] = deconvoluted_result
analysis_result['deconvoluted_percents'] = deconvoluted_percents
```

`significant_means` is used only for a rank sort (lines 171-173) and dropped.
`file_utils.save_dfs_as_tsv` (line 184) writes exactly the keys of that dict, so no thresholded
table is returned or written, and `threshold` becomes inert.

### Minimal reproduction

Runs METHOD 1 twice on the same data, changing only `threshold`, and compares every file written.

```python
import filecmp, glob, os, tempfile
import pandas as pd
from cellphonedb.utils import db_utils
from cellphonedb.src.core.methods import cpdb_analysis_method

d = tempfile.mkdtemp()
TABLES = {
 "gene_input.csv":
   "gene_name,uniprot,hgnc_symbol,ensembl\nLIG1,P00001,LIG1,ENSG00000000001\n"
   "REC1,P00002,REC1,ENSG00000000002\nSUB1,P00003,SUB1,ENSG00000000003\n"
   "SUB2,P00004,SUB2,ENSG00000000004\nLIG2,P00005,LIG2,ENSG00000000005\n",
 "protein_input.csv":
   "uniprot,protein_name,transmembrane,peripheral,secreted,secreted_desc,secreted_highlight,"
   "receptor,receptor_desc,integrin,other,other_desc,tags,tags_reason,tags_description\n"
   "P00001,LIG1_HUMAN,False,False,True,,True,False,,False,False,,,,\n"
   "P00002,REC1_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
   "P00003,SUB1_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
   "P00004,SUB2_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
   "P00005,LIG2_HUMAN,False,False,True,,True,False,,False,False,,,,\n",
 "complex_input.csv":
   "complex_name,uniprot_1,uniprot_2,uniprot_3,uniprot_4,transmembrane,peripheral,secreted,"
   "secreted_desc,secreted_highlight,receptor,receptor_desc,integrin,other,other_desc,pdb_id,"
   "pdb_structure,stoichiometry,comments_complex\n"
   "RECCPLX,P00003,P00004,,,True,False,False,,False,True,,False,False,,,,,\n"
   "BIGCPLX,P00002,P00003,P00004,P00005,True,False,False,,False,True,,False,False,,,,,\n",
 "interaction_input.csv":
   "partner_a,partner_b,protein_name_a,protein_name_b,annotation_strategy,source\n"
   "P00001,P00002,LIG1_HUMAN,REC1_HUMAN,curated,test\n"
   "P00001,RECCPLX,LIG1_HUMAN,,curated,test\n",
}
for name, text in TABLES.items():
    open(os.path.join(d, name), "w").write(text)
db_utils.create_db(d)
db = glob.glob(d + "/cellphonedb_*.zip")[0]

cells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
pd.DataFrame([[2., 3., 4., 0., 0., 1., 0., 0., 0.],      # LIG1: 100% / 33% / 0% of cells
              [0., 0., 1., 2., 2., 2., 1., 0., 0.],      # REC1
              [1., 1., 1., 3., 3., 3., 0., 0., 2.],      # SUB1
              [2., 2., 2., 1., 1., 1., 3., 3., 0.],      # SUB2
              [0., 0., 0., 1., 2., 3., 4., 4., 4.]],     # LIG2
             index=["ENSG0000000000%d" % i for i in (1, 2, 3, 4, 5)],
             columns=cells).rename_axis("Gene").to_csv(d + "/counts.txt", sep="\t")
pd.DataFrame({"Cell": cells, "cell_type": ["CTA"] * 3 + ["CTB"] * 3 + ["CTC"] * 3}).to_csv(
    d + "/meta.txt", sep="\t", index=False)

out = {}
for thr in (0.1, 0.99):
    out[thr] = os.path.join(d, "out_%s" % thr)
    r = cpdb_analysis_method.call(cpdb_file_path=db, meta_file_path=d + "/meta.txt",
                                  counts_file_path=d + "/counts.txt", counts_data="ensembl",
                                  output_path=out[thr], threshold=thr, result_precision=3,
                                  output_suffix="run", threads=1)
    print("threshold=%-5s keys returned: %s" % (thr, sorted(r.keys())))
files = sorted(os.listdir(out[0.1]))
for f in files:
    print("   %-46s identical between threshold 0.1 and 0.99: %s"
          % (f, filecmp.cmp(os.path.join(out[0.1], f), os.path.join(out[0.99], f), shallow=False)))
assert not all(filecmp.cmp(os.path.join(out[0.1], f), os.path.join(out[0.99], f), shallow=False)
               for f in files), "threshold=0.99 should drop interactions, but every file is identical"
```

**Output**

```
threshold=0.1   keys returned: ['deconvoluted', 'deconvoluted_percents', 'means_result']
threshold=0.99  keys returned: ['deconvoluted', 'deconvoluted_percents', 'means_result']
   simple_analysis_deconvoluted_percents_run.txt  identical between threshold 0.1 and 0.99: True
   simple_analysis_deconvoluted_run.txt           identical between threshold 0.1 and 0.99: True
   simple_analysis_means_result_run.txt           identical between threshold 0.1 and 0.99: True
Traceback (most recent call last):
  File "repro_cpdb3.py", line 17, in <module>
    assert not all(filecmp.cmp(os.path.join(out[0.1], f), os.path.join(out[0.99], f), shallow=False)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: threshold=0.99 should drop interactions, but every file is identical
```

**Expected:** at `threshold=0.99` almost every interaction should be dropped (no gene is expressed
in 99 % of the cells of every cluster). **Got:** all three files byte-identical to the
`threshold=0.1` run. On this fixture, 14 of the 36 cells of the means table carry a non-zero mean
that the documented threshold rule excludes.

*What shrinking the example revealed:* the two runs differ in no byte at all, which ruled out "the
threshold is applied but weakly" and pointed straight at the returned dict — `significant_means`
is built correctly, it is simply never returned or saved. Running the same comparison through
`cpdb_statistical_analysis_method` (METHOD 2) on the same data keeps 9 significant entries at
`threshold=0.1` and 6 at `threshold=0.99`, so the machinery works; only METHOD 1 discards it.

### Suggested fix

Either add `significant_means` to `analysis_result` in `cpdb_analysis_method.call` (restoring the
documented behaviour, and giving METHOD 1 the `significant_means` file that the METHOD 1 section
of the documentation implies), or state in the docstring and in the METHOD 1 documentation that
`threshold` does not affect this method's output. The first adds a file to METHOD 1's output,
which is a behaviour change, so I have not sent a patch.

Found in a source-level correctness audit of research software (methods and harnesses:
https://github.com/cindykrafft/research-software-audit/tree/main/audits/cellphonedb)

---
_Generated by [Claude Code](https://claude.ai/code)_
