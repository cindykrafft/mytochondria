Title: `chain_ids` in `summary_confidences.json` has one entry per token, not one per chain as documented

<!-- google-deepmind/alphafold3 has no issue template. Prior-report search 2026-09-22: no report of this. PR #678 and #150 read in full 2026-09-22 (helper transcripts): in #678 (ntnn19, closed 2026-07-09) Augustin-Zidek declined dict-keyed scores for backward compatibility and agreed to "the deduplicated unique chain ID list ... in the same order as the positional arrays" ("Yes, correct."); the PR's own diff had exactly that de-duplication, and his commit e68269f "inspired by your PR" dropped it. #150 (2024): he told a user the chain-level arrays follow the input JSON order and can be inferred from token_chain_ids. Verified on main a66cc52 with the constructor-driven script below and on the run output shipped in the repository (audits/alphafold3/verify/mcve_summary_confidences_*.out); no model run was made. -->

`docs/output.md` describes `chain_ids` in `<name>_summary_confidences.json` as "A [num_chains] array with chain IDs in the same order as all of the other chain-level arrays to make the JSON more self-contained", and the `StructureConfidenceSummary` docstring in `src/alphafold3/model/confidence_types.py` says the same. `from_inference_result` builds it as

```python
chain_ids = [str(c) for c in inference_result.metadata['token_chain_ids']]
```

which is one entry per *token*, each chain repeated once per token it owns. The fields next to it (`chain_ptm`, `chain_iptm`, `chain_pair_pae_min`, `chain_pair_iptm`) really are per chain, so the obvious use, `dict(zip(chain_ids, chain_ptm))`, labels the chain pTMs wrong without any error: with chains A (3 tokens) and B (2 tokens) it yields `('A', ptm_A), ('A', ptm_B)`, and the dict keeps only one of them.

On the run output shipped in the repository (`src/alphafold3/test_data/alphafold_run_outputs/run_alphafold_test_output_bucket_default.pkl`, chains `P` and `LL`), `from_inference_result` returns `chain_ids` with 150 entries (`['P', 'P', 'P', ...]`) next to `chain_ptm` with 2.

Minimal example driving the constructor directly (no model run):

```python
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
```

On `main` (a66cc52):

```
chain_ptm : [0.9, 0.8]   ( 2 chains )
chain_ids : ['A', 'A', 'A', 'B', 'B']   ( 5 entries )
zip(chain_ids, chain_ptm): [('A', 0.9), ('A', 0.8)]
AssertionError: chain_ids is per token, not per chain
```

Expected: `chain_ids == ['A', 'B']`. Affected: v3.0.4 (where the field was added, e68269f) and `main`. The per-token list is already available as `token_chain_ids` in `<name>_confidences.json`, so nothing is lost by making this field what the docs say.

This also seems to be what was intended: the field came out of #678, where the agreed design was "the deduplicated unique chain ID list to summary_confidences.json, in the same order as the positional arrays", and that PR's diff de-duplicated with `list(dict.fromkeys(...))`; e68269f kept the docstring and the field but not the de-duplication.

Proposed fix: de-duplicate `token_chain_ids` keeping first-appearance order, which is the order the chain-level arrays are built in (the expression from #678). One-line change on https://github.com/cindykrafft/alphafold3/compare/main...fix/summary-confidences-chain-ids (on the shipped test output it gives `['P', 'LL']`); I can open it as a pull request.
