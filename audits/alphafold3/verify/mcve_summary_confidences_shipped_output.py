"""AlphaFold 3: chain_ids per token, shown on the run output shipped in the repository.

Loads src/alphafold3/test_data/alphafold_run_outputs/run_alphafold_test_output_bucket_default.pkl
(the pickled inference results used by run_alphafold_test.py), passes the first InferenceResult to
StructureConfidenceSummary.from_inference_result and compares len(chain_ids) with len(chain_ptm).

Run inside an AlphaFold 3 install:  python mcve_summary_confidences_shipped_output.py
"""
import json, pickle, types
import numpy as np
from alphafold3.common import resources
from alphafold3.model import confidence_types

# Unpickle without importing the model package: unknown classes become plain state holders.
class _Holder:
    def __init__(self, *a, **k): pass
    def __setstate__(self, s): self.__dict__.update(s if isinstance(s, dict) else {'state': s})
class _Unpickler(pickle.Unpickler):
    def find_class(self, mod, name):
        try:
            return super().find_class(mod, name)
        except Exception:
            return type(name, (_Holder,), {})

path = resources.ROOT / 'test_data/alphafold_run_outputs/run_alphafold_test_output_bucket_default.pkl'
outputs = _Unpickler(open(path, 'rb')).load()
metadata = outputs[0]['inference_results'][0].__dict__['metadata']
result = types.SimpleNamespace(metadata=metadata)
summary = json.loads(confidence_types.StructureConfidenceSummary.from_inference_result(result).to_json())
print('token_chain_ids:', len(metadata['token_chain_ids']), 'tokens; distinct chains',
      list(dict.fromkeys(str(c) for c in metadata['token_chain_ids'])))
print('chain_ptm :', summary['chain_ptm'], '(', len(summary['chain_ptm']), 'chains )')
print('chain_ids :', summary['chain_ids'][:8], '...' if len(summary['chain_ids']) > 8 else '', '(', len(summary['chain_ids']), 'entries )')
assert len(summary['chain_ids']) == len(summary['chain_ptm']), 'chain_ids is per token, not per chain'
