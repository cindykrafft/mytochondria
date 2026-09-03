#!/usr/bin/env python3
"""N6: `db_utils.create_db` raises an opaque pandas ValueError when a `uniprot_N` column of
complex_input.csv is entirely empty.

`sanity_test_report_unknown_proteins` (db_utils.py:597-608) merges the complex table against the
protein table once per subunit column:

    for col in protein_column_names:                       # uniprot_1 .. uniprot_4 (or _5)
        aux_df = pd.merge(complex_db_df, protein_db_df, left_on=col, right_on='uniprot',
                          how='outer')

If no complex in the file uses, say, `uniprot_4`, pandas reads that column as all-NaN float64 and
refuses to merge it against the string `uniprot` column:

    ValueError: You are trying to merge on float64 and str columns for key 'uniprot_4'.

So building a custom database (the documented `T0_BuildDBfromFiles` workflow) fails whenever every
complex has fewer subunits than the widest `uniprot_N` column present in the header -- e.g. a file
whose complexes are all dimers, but which keeps the standard four/five-column header. The user has
to either add a wide complex they do not want or trim the header.

The message names a column of their input, so it is diagnosable, but it comes from a *sanity test*
whose purpose is to warn about unknown proteins, and no unknown protein is involved.
"""
import os
import sys
import tempfile
import traceback
from importlib.metadata import version

import pandas as pd
from cellphonedb.utils import db_utils

GENE = ("gene_name,uniprot,hgnc_symbol,ensembl\n"
        "LIG1,P00001,LIG1,ENSG00000000001\nREC1,P00002,REC1,ENSG00000000002\n"
        "SUB1,P00003,SUB1,ENSG00000000003\nSUB2,P00004,SUB2,ENSG00000000004\n")
PROT = ("uniprot,protein_name,transmembrane,peripheral,secreted,secreted_desc,secreted_highlight,"
        "receptor,receptor_desc,integrin,other,other_desc,tags,tags_reason,tags_description\n"
        "P00001,LIG1_HUMAN,False,False,True,,True,False,,False,False,,,,\n"
        "P00002,REC1_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
        "P00003,SUB1_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
        "P00004,SUB2_HUMAN,True,False,False,,False,True,,False,False,,,,\n")
CPLX_HDR = ("complex_name,uniprot_1,uniprot_2,uniprot_3,uniprot_4,transmembrane,peripheral,"
            "secreted,secreted_desc,secreted_highlight,receptor,receptor_desc,integrin,other,"
            "other_desc,pdb_id,pdb_structure,stoichiometry,comments_complex\n")
DIMER_ONLY = CPLX_HDR + "RECCPLX,P00003,P00004,,,True,False,False,,False,True,,False,False,,,,,\n"
WITH_A_WIDE_COMPLEX = DIMER_ONLY + \
    "BIGCPLX,P00001,P00002,P00003,P00004,True,False,False,,False,True,,False,False,,,,,\n"
INT = ("partner_a,partner_b,protein_name_a,protein_name_b,annotation_strategy,source\n"
       "P00001,P00002,LIG1_HUMAN,REC1_HUMAN,curated,test\n"
       "P00001,RECCPLX,LIG1_HUMAN,,curated,test\n")


def try_build(label, complex_csv):
    d = tempfile.mkdtemp()
    for name, text in [("gene_input.csv", GENE), ("protein_input.csv", PROT),
                       ("complex_input.csv", complex_csv), ("interaction_input.csv", INT)]:
        open(os.path.join(d, name), "w").write(text)
    cols = pd.read_csv(os.path.join(d, "complex_input.csv"))
    empty = [c for c in cols.columns if c.startswith("uniprot_") and cols[c].isna().all()]
    print("\n=== %s" % label)
    print("    complexes: %d, entirely empty subunit columns: %s" % (len(cols), empty or "none"))
    try:
        db_utils.create_db(d)
        print("    RESULT: created successfully")
    except Exception:
        print("    RESULT: raised ->")
        traceback.print_exc(file=sys.stdout)


print("cellphonedb %s   pandas %s" % (version("cellphonedb"), pd.__version__))
try_build("complex_input.csv with only a dimer (uniprot_3 and uniprot_4 empty)", DIMER_ONLY)
try_build("the same file plus one four-subunit complex", WITH_A_WIDE_COMPLEX)
print("\nThe only difference between the two runs is whether some complex happens to fill the")
print("widest subunit column. The fix is a dtype-safe merge (e.g. skip all-NaN columns, or")
print("compare as strings) in sanity_test_report_unknown_proteins.")
