Title: deconvoluted.txt reports the complex's minimum on every subunit row instead of the subunit's own mean

<!-- ventolab/CellphoneDB has no issue template; this follows the structure of a minimal
     complete verifiable example. -->

**Version:** 5.0.1 (PyPI wheel and `master` @ `dc8abd15`, byte-identical); the same two lines are
present in v3.1.0, v4.0.0 and v5.0.0. `deconvoluted_percents.txt` (new in v5) is affected the same
way.

### What the documentation says

`docs/RESULTS-DOCUMENTATION.md:287` describes the per-cluster columns of `deconvoluted.txt` as
"mean: **Mean expression of the corresponding gene** in each cluster", with `gene_name` being
"Gene identifier for **one of the subunits** that are participating in the interaction", and
line 255 describes the percentages file as denoting "the percentage of cells expressing a given
gene". Line 254 gives the file's purpose: "This is important as some of the interacting partners
are heteromers. In other words, multiple molecules have to be expressed in the same cluster in
order for the interacting partner to be functional."

### What the code does

`deconvolute_complex_interaction_component`
(`cpdb_statistical_analysis_complex_method.py:366-371`) labels the row with the **subunit** but
fills `multidata_id` from the **complex**:

```python
deconvoluted_result[
    ['multidata_id', 'protein_name', 'gene_name', 'name', 'is_complex', 'id_cp_interaction',
     'receptor', 'complex_name']] = \
    deconvolution_complex[
        ['complex_multidata_id', 'protein_name_simple', 'gene_name_simple', 'name_simple', ...]]
```

and `deconvoluted_complex_result_build` (lines 292-304) joins the per-cluster tables on that id:

```python
deconvoluted_result.set_index('multidata_id', inplace=True, drop=True)
deconvoluted_result = pd.concat([deconvoluted_result,
                                 clusters_means.reindex(deconvoluted_result.index)], axis=1, ...)
```

`clusters_means` holds one row per complex containing the **minimum over its subunits**
(`cpdb_statistical_analysis_helper.py:154-159`), so each subunit row receives the complex minimum,
and all subunits of a complex show identical numbers. Simple (non-complex) rows are unaffected.

### Minimal reproduction

`RECCPLX = SUB1 + SUB2`, and in cell type CTB the cells express SUB1 at 3, 3, 3 and SUB2 at
1, 1, 1 — so SUB1's mean in CTB is 3.0 and the complex minimum is 1.0.

```python
import glob, os, tempfile
import pandas as pd
from cellphonedb.utils import db_utils
from cellphonedb.src.core.methods import cpdb_statistical_analysis_method

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
pd.DataFrame([[2., 3., 4., 0., 0., 1., 0., 0., 0.],      # LIG1
              [0., 0., 1., 2., 2., 2., 1., 0., 0.],      # REC1
              [1., 1., 1., 3., 3., 3., 0., 0., 2.],      # SUB1 -> mean 3.0 in CTB
              [2., 2., 2., 1., 1., 1., 3., 3., 0.],      # SUB2 -> mean 1.0 in CTB
              [0., 0., 0., 1., 2., 3., 4., 4., 4.]],     # LIG2
             index=["ENSG0000000000%d" % i for i in (1, 2, 3, 4, 5)],
             columns=cells).rename_axis("Gene").to_csv(d + "/counts.txt", sep="\t")
pd.DataFrame({"Cell": cells, "cell_type": ["CTA"] * 3 + ["CTB"] * 3 + ["CTC"] * 3}).to_csv(
    d + "/meta.txt", sep="\t", index=False)

r = cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=d + "/meta.txt", counts_file_path=d + "/counts.txt",
    counts_data="ensembl", output_path=d + "/out", iterations=100, threshold=0.1, threads=1,
    debug_seed=0, result_precision=3, pvalue=0.05, separator="|", output_suffix="run")
dec = r["deconvoluted"]
print(dec[["gene_name", "complex_name", "CTA", "CTB", "CTC"]].to_string(index=False))
sub1 = dec[(dec.gene_name == "SUB1") & (dec.complex_name == "RECCPLX")].iloc[0]
assert float(sub1["CTB"]) == 3.0, \
    "deconvoluted.txt reports %.3f for SUB1 in CTB; its own mean is 3.0" % float(sub1["CTB"])
```

**Output**

```
gene_name complex_name   CTA   CTB   CTC
     LIG1          NaN 3.000 0.333 0.000
     LIG1          NaN 3.000 0.333 0.000
     SUB1      RECCPLX 1.000 1.000 0.667
     SUB2      RECCPLX 1.000 1.000 0.667
     REC1          NaN 0.333 2.000 0.333
Traceback (most recent call last):
  File "repro_cpdb4.py", line 13, in <module>
    assert float(sub1["CTB"]) == 3.0, \
           ^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: deconvoluted.txt reports 1.000 for SUB1 in CTB; its own mean is 3.0
```

**Expected:** the SUB1 row shows SUB1's mean (1.0, 3.0, 0.667) and the SUB2 row shows SUB2's
(2.0, 1.0, 2.0). **Got:** both rows show 1.0, 1.0, 0.667 — the complex's minimum. A reader asking
"is SUB1 expressed in CTB?" is shown SUB2's value.

*What shrinking the example revealed:* the simple rows (LIG1, REC1) are correct, which localised
the problem to `deconvolute_complex_interaction_component`; and the two subunit rows of a complex
are always identical to each other, which identified the join key as the complex id rather than
any averaging mistake. On a four-subunit complex all four rows collapse to the same numbers.

### Why it matters

This is the file the documentation points users at to confirm that every subunit of a heteromer is
expressed in a cluster, and it cannot answer that question in its current form — a complex whose
minimum is driven by one weakly expressed subunit looks as though *all* its subunits are weak.
`deconvoluted_percents.txt` has the same problem, so the percentage columns cannot be used to
check the `threshold` condition per subunit either.

### Suggested fix

Keep the subunit's `protein_multidata_id` in a separate column and join the per-gene tables on
that for complex rows, keeping `complex_name` for grouping. This changes the numbers in a
published output file, so I have not sent a patch — happy to prepare one if you would like it in
that shape.

Found in a source-level correctness audit of research software (methods and harnesses:
https://github.com/cindykrafft/research-software-audit/tree/main/audits/cellphonedb)

---
_Generated by [Claude Code](https://claude.ai/code)_
