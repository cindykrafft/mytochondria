"""AlphaFold 3: summary_confidences chain_ids has one entry per token, not one per chain.

StructureConfidenceSummary.from_inference_result copies metadata['token_chain_ids'] verbatim
into chain_ids, which the dataclass documents as [num_chains] "in the same order as the
chain-level arrays". This drives the constructor with a two-chain result (chain A of three
tokens, chain B of two) and compares the lengths.

Run inside an AlphaFold 3 install:  python mcve_summary_confidences_chain_ids.py
(Any real run shows the same thing: compare len(chain_ids) with len(chain_ptm) in
<name>_summary_confidences.json.)
"""
import json, types
import numpy as np
from alphafold3.model import confidence_types

metadata = {
    'token_chain_ids': np.array(['A', 'A', 'A', 'B', 'B']),   # five tokens, two chains
    'ptm': 0.9, 'iptm': 0.8, 'ranking_score': 0.85, 'fraction_disordered': 0.0, 'has_clash': 0.0,
    'chain_pair_pae_min': np.zeros((2, 2)), 'chain_pair_iptm': np.zeros((2, 2)),
    'iptm_ichain': np.array([0.9, 0.8]), 'iptm_xchain': np.array([0.7, 0.6]),
}
result = types.SimpleNamespace(metadata=metadata)
summary = confidence_types.StructureConfidenceSummary.from_inference_result(result)
out = json.loads(summary.to_json())
print("chain_ptm :", out['chain_ptm'], "  (", len(out['chain_ptm']), "chains )")
print("chain_ids :", out['chain_ids'], "  (", len(out['chain_ids']), "entries )")
print("zip(chain_ids, chain_ptm):", list(zip(out['chain_ids'], out['chain_ptm'])))
assert len(out['chain_ids']) == len(out['chain_ptm']), "chain_ids is per token, not per chain"
