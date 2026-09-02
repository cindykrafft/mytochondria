"""C2: SummaryConfidences.chain_ids is per-token, not per-chain.

Loads the real src/alphafold3/model/confidence_types.py verbatim, stubbing only
the compiled extension and the modules it imports for typing, then builds an
inference result whose metadata has the same shapes as the run output shipped in
the repository (150 tokens over 2 chains) and prints the field lengths.

Usage:
  AF3=/path/to/alphafold3 python c2_chain_ids_length.py
"""
import os, sys, types
import numpy as np

AF3 = os.environ.get('AF3', '')
if not AF3:
    sys.exit('set AF3=/path/to/alphafold3 clone')
SRC = os.path.join(AF3, 'src')
sys.path.insert(0, SRC)


def stub(name, **attrs):
    m = types.ModuleType(name)
    for k, v in attrs.items():
        setattr(m, k, v)
    sys.modules[name] = m
    return m


stub('alphafold3.cpp')
stub('alphafold3.cpp.json_serialize', structure_confidence_full_to_json=lambda **k: '{}')
stub('alphafold3.structure', Structure=object)
stub('alphafold3.model.model', InferenceResult=object)
import alphafold3  # noqa: F401  (namespace package under src)

path = os.path.join(SRC, 'alphafold3/model/confidence_types.py')
mod = types.ModuleType('af3_confidence_types')
mod.__file__ = path
sys.modules['af3_confidence_types'] = mod
exec(compile(open(path).read(), path, 'exec'), mod.__dict__)

# Shapes as in test_data/alphafold_run_outputs/run_alphafold_test_output_bucket_default.pkl:
# 150 tokens, 2 chains ('P' then 'L').
n_tokens, chains = 150, ['P'] * 100 + ['L'] * 50


class R:  # stands in for model.InferenceResult
    metadata = {
        'token_chain_ids': np.array(chains),
        'ptm': 0.81073031, 'iptm': 0.67959953,
        'ranking_score': 0.70582568, 'fraction_disordered': 0.0, 'has_clash': 0.0,
        'chain_pair_pae_min': np.zeros((2, 2)), 'chain_pair_iptm': np.zeros((2, 2)),
        'iptm_ichain': np.array([0.83866367, 0.74195246]),
        'iptm_xchain': np.array([0.67959953, 0.67959953]),
    }


sc = mod.StructureConfidenceSummary.from_inference_result(R())
print('num_tokens in this example :', n_tokens)
print('num_chains in this example :', len(dict.fromkeys(chains)))
print()
print('len(chain_ids)      =', len(sc.chain_ids), ' <- docs/output.md:195 declares [num_chains]')
print('len(chain_ptm)      =', len(sc.chain_ptm))
print('len(chain_iptm)     =', len(sc.chain_iptm))
print('chain_pair_iptm     =', sc.chain_pair_iptm.shape)
print('chain_ids[:8]       =', list(sc.chain_ids[:8]))
print()
print('chain_ids aligns with the chain-based fields:',
      len(sc.chain_ids) == len(sc.chain_ptm))
print('de-duplicated chain_ids would be:', list(dict.fromkeys(sc.chain_ids)))
