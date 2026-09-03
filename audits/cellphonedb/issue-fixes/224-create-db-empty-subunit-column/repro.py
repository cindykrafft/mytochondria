#!/usr/bin/env python3
"""Issue #224: db_utils.create_db fails on a complex_input.csv whose widest uniprot_N column is unused.

Builds a minimal, self-consistent set of the four *_input.csv files (no download) in which the
only complex is a dimer, while complex_input.csv keeps the standard uniprot_1..uniprot_4 header.
pandas reads the two unused subunit columns as all-NaN float64, and the sanity test in
db_utils.sanity_test_report_unknown_proteins merges them against the string 'uniprot' column.
Expected: the database is created. Got (master @ dc8abd15): ValueError from pandas.merge.
"""
import os
import sys
import glob
import tempfile
import traceback
from importlib.metadata import version

import pandas as pd
from cellphonedb.utils import db_utils

GENE = ("gene_name,uniprot,hgnc_symbol,ensembl\n"
        "LIG1,P00001,LIG1,ENSG00000000001\n"
        "SUB1,P00003,SUB1,ENSG00000000003\n"
        "SUB2,P00004,SUB2,ENSG00000000004\n")
PROTEIN = ("uniprot,protein_name,transmembrane,peripheral,secreted,secreted_desc,secreted_highlight,"
           "receptor,receptor_desc,integrin,other,other_desc,tags,tags_reason,tags_description\n"
           "P00001,LIG1_HUMAN,False,False,True,,True,False,,False,False,,,,\n"
           "P00003,SUB1_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
           "P00004,SUB2_HUMAN,True,False,False,,False,True,,False,False,,,,\n")
# The released complex_input.csv header (uniprot_1..4; v5 adds uniprot_5), with a single dimer.
COMPLEX = ("complex_name,uniprot_1,uniprot_2,uniprot_3,uniprot_4,transmembrane,peripheral,secreted,"
           "secreted_desc,secreted_highlight,receptor,receptor_desc,integrin,other,other_desc,"
           "pdb_id,pdb_structure,stoichiometry,comments_complex\n"
           "RECCPLX,P00003,P00004,,,True,False,False,,False,True,,False,False,,,,,\n")
INTERACTION = ("partner_a,partner_b,protein_name_a,protein_name_b,annotation_strategy,source\n"
               "P00001,RECCPLX,LIG1_HUMAN,,curated,test\n")

d = tempfile.mkdtemp(prefix="cpdb224_")
for name, text in [("gene_input.csv", GENE), ("protein_input.csv", PROTEIN),
                   ("complex_input.csv", COMPLEX), ("interaction_input.csv", INTERACTION)]:
    with open(os.path.join(d, name), "w") as fh:
        fh.write(text)

print("cellphonedb %s, pandas %s" % (version("cellphonedb"), pd.__version__))
complex_df = pd.read_csv(os.path.join(d, "complex_input.csv"))
print("complex_input.csv as read by pandas:",
      {c: str(complex_df[c].dtype) for c in complex_df.columns if c.startswith("uniprot_")})
try:
    db_utils.create_db(d)
except Exception:
    print("RESULT: create_db raised")
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)
zips = glob.glob(os.path.join(d, "cellphonedb_*.zip"))
print("RESULT: created", [os.path.basename(z) for z in zips])
sys.exit(0 if zips else 1)
