"""Alternate candidate (not fixed here): issues #190 / #225, KeyError in score_interactions.

Uses the project fixture (../../verify/tiny_dataset.py) and makes one subunit (SUB1) of the complex RECCPLX
negative in one cell type, as scaled/z-scored input would be. The cluster-mean product of the subunits is
then negative, scoring_utils._geometric_mean takes a fractional power of it -> NaN, MinMaxScaler keeps the
NaN, and DataFrame.stack() in _get_lr_scores drops NaN cells (pandas < 3), so the pair is missing from
interacting_pair2score and score_product raises KeyError on the complex-containing pair.
"""
import os, sys, tempfile, traceback
import numpy as np, pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "verify"))
import tiny_dataset as T
from cellphonedb.src.core.methods import cpdb_analysis_method
tmp = tempfile.mkdtemp(prefix='probe_')
db = T.build_db(os.path.join(tmp, 'db'))
counts = T.COUNTS.copy()
# make SUB1 negative in CTA (as scaled / z-scored data would be): mean(SUB1|CTA) < 0, mean(SUB2|CTA) > 0
counts[2, 0:3] = [-1., -1., -1.]
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, 'in'), counts=counts)
try:
    res = cpdb_analysis_method.call(cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp,
        counts_data='ensembl', output_path=os.path.join(tmp, 'out'), threshold=0.1, result_precision=3,
        separator='|', output_suffix='x', score_interactions=True, threads=1)
    print(res['interaction_scores'])
except Exception:
    traceback.print_exc(file=sys.stdout)
