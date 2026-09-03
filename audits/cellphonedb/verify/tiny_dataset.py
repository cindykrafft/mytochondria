"""Shared fixture for the CellphoneDB harnesses: a hand-made database and a 9-cell dataset.

Everything here is written from scratch by this module -- no downloaded data. The official
CellphoneDB database download (`db_utils.download_database`, which fetches
github.com/ventolab/cellphonedb-data archives) returns HTTP 403 from this environment, so the
harnesses build their own database with the package's own `db_utils.create_db` from four
hand-written *_input.csv tables. The tables are deliberately minimal:

  proteins   LIG1 P00001, REC1 P00002, SUB1 P00003, SUB2 P00004, LIG2 P00005
  genes      one ensembl id each, plus a SECOND ensembl id for LIG1 (ENSG...011) used only by
             the duplicate-gene-row harness; it is absent from the counts matrix otherwise
  complexes  RECCPLX = SUB1 + SUB2                (2 subunits)
             BIGCPLX = REC1 + SUB1 + SUB2 + LIG2  (4 subunits)
  interactions  LIG1-REC1, LIG2-RECCPLX, LIG1-RECCPLX, LIG1-BIGCPLX

The counts matrix is 5 genes x 9 cells, three cell types of three cells each, with values
chosen by hand so that every branch of the method is exercised and every quantity can be
written down exactly:

              CTA (A1 A2 A3)   CTB (B1 B2 B3)   CTC (C1 C2 C3)     cluster means      cluster pcts
  LIG1          2  3  4          0  0  1          0  0  0          3,    1/3,  0      1,   1/3, 0
  REC1          0  0  1          2  2  2          1  0  0          1/3,  2,    1/3    1/3, 1,   1/3
  SUB1          1  1  1          3  3  3          0  0  2          1,    3,    2/3    1,   1,   1/3
  SUB2          2  2  2          1  1  1          3  3  0          2,    1,    2      1,   1,   2/3
  LIG2          0  0  0          1  2  3          4  4  4          0,    2,    4      0,   1,   1

  RECCPLX (min over subunits, taken on the cluster means)  1,  1,  2/3    pcts 1, 1, 1/3
  BIGCPLX (min over subunits)                              0,  1,  1/3    pcts 0, 1, 1/3

9 cells in three groups of three gives 9!/(3!)^3 = 1680 distinct label assignments, so the
exact permutation null can be enumerated exhaustively (see cpdb2_pvalue_ties_and_zero.py).
"""
import os
import glob
import numpy as np
import pandas as pd

GENES = ["ENSG00000000001", "ENSG00000000002", "ENSG00000000003",
         "ENSG00000000004", "ENSG00000000005"]
GENE_LABEL = {"ENSG00000000001": "LIG1", "ENSG00000000002": "REC1",
              "ENSG00000000003": "SUB1", "ENSG00000000004": "SUB2",
              "ENSG00000000005": "LIG2"}
CELLS = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
CELL_TYPES = ["CTA"] * 3 + ["CTB"] * 3 + ["CTC"] * 3
COUNTS = np.array([
    [2., 3., 4.,   0., 0., 1.,   0., 0., 0.],   # LIG1
    [0., 0., 1.,   2., 2., 2.,   1., 0., 0.],   # REC1
    [1., 1., 1.,   3., 3., 3.,   0., 0., 2.],   # SUB1
    [2., 2., 2.,   1., 1., 1.,   3., 3., 0.],   # SUB2
    [0., 0., 0.,   1., 2., 3.,   4., 4., 4.],   # LIG2
])

GENE_INPUT = """gene_name,uniprot,hgnc_symbol,ensembl
LIG1,P00001,LIG1,ENSG00000000001
LIG1,P00001,LIG1,ENSG00000000011
REC1,P00002,REC1,ENSG00000000002
SUB1,P00003,SUB1,ENSG00000000003
SUB2,P00004,SUB2,ENSG00000000004
LIG2,P00005,LIG2,ENSG00000000005
"""
PROTEIN_INPUT = """uniprot,protein_name,transmembrane,peripheral,secreted,secreted_desc,secreted_highlight,receptor,receptor_desc,integrin,other,other_desc,tags,tags_reason,tags_description
P00001,LIG1_HUMAN,False,False,True,,True,False,,False,False,,,,
P00002,REC1_HUMAN,True,False,False,,False,True,,False,False,,,,
P00003,SUB1_HUMAN,True,False,False,,False,True,,False,False,,,,
P00004,SUB2_HUMAN,True,False,False,,False,True,,False,False,,,,
P00005,LIG2_HUMAN,False,False,True,,True,False,,False,False,,,,
"""
COMPLEX_INPUT = """complex_name,uniprot_1,uniprot_2,uniprot_3,uniprot_4,transmembrane,peripheral,secreted,secreted_desc,secreted_highlight,receptor,receptor_desc,integrin,other,other_desc,pdb_id,pdb_structure,stoichiometry,comments_complex
RECCPLX,P00003,P00004,,,True,False,False,,False,True,,False,False,,,,,
BIGCPLX,P00002,P00003,P00004,P00005,True,False,False,,False,True,,False,False,,,,,
"""
INTERACTION_INPUT = """partner_a,partner_b,protein_name_a,protein_name_b,annotation_strategy,source
P00001,P00002,LIG1_HUMAN,REC1_HUMAN,curated,test
P00005,RECCPLX,LIG2_HUMAN,,curated,test
P00001,RECCPLX,LIG1_HUMAN,,curated,test
P00001,BIGCPLX,LIG1_HUMAN,,curated,test
"""


def build_db(target_dir):
    """Write the four *_input.csv tables and run db_utils.create_db; return the .zip path."""
    from cellphonedb.utils import db_utils
    os.makedirs(target_dir, exist_ok=True)
    for name, text in [("gene_input.csv", GENE_INPUT), ("protein_input.csv", PROTEIN_INPUT),
                       ("complex_input.csv", COMPLEX_INPUT),
                       ("interaction_input.csv", INTERACTION_INPUT)]:
        with open(os.path.join(target_dir, name), "w") as fh:
            fh.write(text)
    for stale in glob.glob(os.path.join(target_dir, "cellphonedb_*.zip")):
        os.remove(stale)
    db_utils.create_db(target_dir)
    return glob.glob(os.path.join(target_dir, "cellphonedb_*.zip"))[0]


def write_inputs(target_dir, counts=None, genes=None, cells=None, cell_types=None):
    """Write counts/meta/microenvironment files; return (counts_fp, meta_fp, microenvs_fp)."""
    os.makedirs(target_dir, exist_ok=True)
    counts = COUNTS if counts is None else counts
    genes = GENES if genes is None else genes
    cells = CELLS if cells is None else cells
    cell_types = CELL_TYPES if cell_types is None else cell_types
    counts_fp = os.path.join(target_dir, "counts.txt")
    df = pd.DataFrame(counts, index=genes, columns=cells)
    df.index.name = "Gene"
    df.to_csv(counts_fp, sep="\t")
    meta_fp = os.path.join(target_dir, "meta.txt")
    pd.DataFrame({"Cell": cells, "cell_type": cell_types}).to_csv(meta_fp, sep="\t", index=False)
    me_fp = os.path.join(target_dir, "microenvs.txt")
    pd.DataFrame({"cell_type": sorted(set(cell_types)),
                  "microenvironment": ["env1"] * len(set(cell_types))}).to_csv(
        me_fp, sep="\t", index=False)
    return counts_fp, meta_fp, me_fp


# ---------------------------------------------------------------------------
# Independent reference implementation of the method as CellphoneDB documents it
# (README "METHOD 1"/"METHOD 2" and docs/RESULTS-DOCUMENTATION.md). Plain numpy;
# no CellphoneDB code is used below this line.
# ---------------------------------------------------------------------------

# interactions as (partner_a, partner_b) where a partner is either a gene row or a complex
INTERACTIONS = [("LIG1", "REC1"), ("LIG2", "RECCPLX"), ("LIG1", "RECCPLX"), ("LIG1", "BIGCPLX")]
COMPLEXES = {"RECCPLX": ["SUB1", "SUB2"], "BIGCPLX": ["REC1", "SUB1", "SUB2", "LIG2"]}


def cluster_means_pcts(counts, labels, gene_labels=None):
    """Per-cluster mean expression (zeros included) and fraction of cells with value > 0.

    Complexes are summarised by the MINIMUM over subunits, taken after the per-subunit
    cluster means have been computed (this is what the docs describe: "we use the member of
    the complex with the minimum expression").
    """
    gene_labels = [GENE_LABEL[g] for g in GENES] if gene_labels is None else gene_labels
    labels = np.asarray(labels)
    names = sorted(set(labels))
    means, pcts = {}, {}
    for ct in names:
        sel = labels == ct
        means[ct] = counts[:, sel].mean(axis=1)
        pcts[ct] = (counts[:, sel] > 0).mean(axis=1)
    means = pd.DataFrame(means, index=gene_labels)[names]
    pcts = pd.DataFrame(pcts, index=gene_labels)[names]
    for cname, subunits in COMPLEXES.items():
        means.loc[cname] = means.loc[subunits].min(axis=0)
        pcts.loc[cname] = pcts.loc[subunits].min(axis=0)
    return means, pcts


def interaction_means(means, cluster_pairs):
    """(mean_a + mean_b)/2, set to 0 when either side's cluster mean is 0."""
    out = {}
    for ca, cb in cluster_pairs:
        col = []
        for pa, pb in INTERACTIONS:
            x, y = means.at[pa, ca], means.at[pb, cb]
            col.append(0.0 if (x <= 0 or y <= 0) else (x + y) / 2.0)
        out["{}|{}".format(ca, cb)] = col
    return pd.DataFrame(out, index=["{}_{}".format(a, b) for a, b in INTERACTIONS])


def interaction_pcts(pcts, cluster_pairs, threshold):
    """1 when BOTH partners are expressed in more than `threshold` of their cluster's cells."""
    out = {}
    for ca, cb in cluster_pairs:
        col = []
        for pa, pb in INTERACTIONS:
            col.append(int((pcts.at[pa, ca] > threshold) and (pcts.at[pb, cb] > threshold)))
        out["{}|{}".format(ca, cb)] = col
    return pd.DataFrame(out, index=["{}_{}".format(a, b) for a, b in INTERACTIONS])


def cluster_pairs_of(labels):
    names = sorted(set(np.asarray(labels)))
    return [(a, b) for a in names for b in names]
