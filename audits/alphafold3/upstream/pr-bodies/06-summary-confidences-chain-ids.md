**Branch:** `fix/summary-confidences-chain-ids` ·
[open this PR](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/summary-confidences-chain-ids?expand=1)

**Title:** Make summary_confidences chain_ids one entry per chain

---

### What is wrong

`src/alphafold3/model/confidence_types.py:194` builds the field straight from the
per-token array:

```python
    chain_ids = [str(c) for c in inference_result.metadata['token_chain_ids']]
```

`token_chain_ids` is `[num_tokens]` (`docs/output.md:209`), but `chain_ids` is documented
at `docs/output.md:195` as

> A \[num_chains\] array with chain IDs in the same order as all the other chain-based
> fields

and `chain_ptm`, `chain_iptm`, `chain_pair_pae_min` and `chain_pair_iptm` really are per
chain. So anything zipping `chain_ids` against them — the field's stated purpose — silently
misaligns.

### Reproduction

Using the shapes of the run output shipped in
`src/alphafold3/test_data/alphafold_run_outputs/` (150 tokens, 2 chains), with the real
`confidence_types.py` loaded:

```
len(chain_ids)      = 150  <- docs/output.md:195 declares [num_chains]
len(chain_ptm)      = 2
len(chain_iptm)     = 2
chain_pair_iptm     = (2, 2)
chain_ids[:8]       = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']

chain_ids aligns with the chain-based fields: False
de-duplicated chain_ids would be: ['P', 'L']
```

Script: `verify/c2_chain_ids_length.py` in the linked audit repository.

This came in with `e68269f` ("Add chain IDs in the summary confidence JSON for easier
use"), so it is newer than v3.0.4.

### The change

De-duplicate with `dict.fromkeys`, which preserves first-appearance order — the asym order
the chain-based fields are built in.

### Testing

Same script against the patched tree: `len(chain_ids) = 2`, `['P', 'L']`, aligned with
`chain_ptm`.

---

_This patch and description were written with AI assistance (Claude Code), disclosed per
CONTRIBUTING.md. The code and the reproduction above were reviewed and executed by me; no
test output here is hallucinated._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
