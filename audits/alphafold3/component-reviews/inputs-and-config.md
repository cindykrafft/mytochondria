# Input handling, configuration and parameter loading

Scope: `common/folding_input.py`, `common/base_config.py`, `common/safe_pickle.py`,
`run_alphafold.py`, `model/params.py`, `model/model_config.py`, `docs/input.md`.
Tree: `main` @ `c0f97eda`.

The compiled extension is not needed for most of this scope, so the real
`folding_input.py` was loaded with the heavy imports stubbed and exercised directly.

---

## I1 — `to_json` reorders chains, so a two-stage run sees a different token layout [verified]

`common/folding_input.py:1487-1496`:

```python
    deduped_chains = {}
    deduped_chain_ids = {}
    for chain in self.chains:
      deduped_chains[chain.hash_without_id()] = chain
      deduped_chain_ids.setdefault(chain.hash_without_id(), []).append(chain.id)

    sequences = []
    for chain_content_hash, ids in deduped_chain_ids.items():
      chain = deduped_chains[chain_content_hash]
      sequences.append(chain.to_dict(seq_id=ids if len(ids) > 1 else ids[0]))
```

Chains are grouped by content across the whole input and emitted one entry per group, at
the position where the group first appeared. Two identical chains separated by a
different chain are therefore emitted together, and the chain between them moves after
them. `from_json` rebuilds `Input.chains` in the emitted order, so the round trip
reorders the input.

That matters because chain order is load-bearing. `to_structure` (`:1430-1465`) lays out
tokens in chain order, and `model/features.py:146-159` assigns `asym_id`, `entity_id` and
`sym_id` by first appearance in that layout. For a homodimer with a ligand between the
two copies:

```
single-stage chain order : ['A', 'B', 'C']
two-stage (reload) order : ['A', 'C', 'B']
single-stage asym_id: {'A': 1, 'B': 2, 'C': 3}
two-stage   asym_id: {'A': 1, 'C': 2, 'B': 3}
```

`run_alphafold.py:649-658` always writes `<name>_data.json = fold_input.to_json()`, so in
the documented split workflow — data pipeline with `--norun_inference`, then inference
from that JSON, which is what the performance docs recommend for large runs — the model
receives a different token order and different asym ids than a single end-to-end run of
the same input with the same seed. A single-stage run is unaffected, because the
in-memory object keeps its order.

The fix merges only *consecutive* content-identical chains, which keeps the emitted order
faithful; interleaved copies are written as separate entries. The upstream
`folding_input_test.py` suite gives an identical pass/fail set before and after (20
failures either way, all from the CCD pickle and test data absent in this environment).

## I2 — The parameter-file pattern for uncompressed shards has a stray `]` [verified]

`model/params.py:207`. Covered under
[`network-and-diffusion.md` N5](network-and-diffusion.md), where the second independent
rediscovery is recorded.

---

## Considered and not filed

`ccdCodes: []` is accepted as a zero-length ligand and `to_structure` then builds the
sequence `"()"`. A validation gap rather than a demonstrated wrong prediction; rejecting
an empty `ccd_ids` in `Ligand.__post_init__` would close it.

`data/pipeline.py:552,585` rebuild chains from `chain.sequence`, the modified
single-letter property — the same class of mistake that `97d2023` fixed for RNA in
`fill_missing_fields`. Traced through `to_ccd_sequence`: the modifications are re-applied,
so the model's CCD sequence is unchanged and only the stored single-letter string in
`_data.json` differs. Benign.

`model/params.py:82` slices `payload[-0:]`, which is the whole buffer rather than an
empty one, but it is reachable only for a zero-element parameter that never occurs and
that would fail at `reshape` anyway.

---

## Exonerated

Eleven areas checked and cleared: `Template.from_dict`'s `templateIndices or []` with a
`strict=True` zip (the failing combination cannot be produced by the old serializer, and
empty against empty returns `{}`); `to_json`'s deduplication *content* correctness and
the multi-copy round trip, which matches the upstream
`test_to_json_sequence_deduplication` — only the ordering is affected, as I1 records; the
1-based modification index convention across protein, RNA and DNA and through
`from_mmcif`; `CCD_` prefix handling, stripped for the server dialect, deliberately kept
for ions, and rejected in the AlphaFold 3 dialect; the empty-string versus `None` MSA
semantics, where `""` means a deliberately empty custom MSA and `None` means unset,
including the path-guard truthiness; bonded-atom-pair parsing and validation (type, chain
membership, the 1-based residue range, rejection for SMILES ligands, uniqueness, and the
conversion to 0-based in `to_structure`); RNG seed handling, including the uint32
validation added by `a84d263`, the at-least-one-seed rule and the contiguous
`with_multiple_seeds` range; `base_config.py`'s `_Autocreate` and dict-to-Config
coercion, with no mutable shared state; `safe_pickle`'s allowlist; `GlobalConfig`'s
immutable tuple defaults; and `data_constants.MSA_PAD_VALUES` with `msa_mask: 1`, which
is the correct gap-row semantics for the block-diagonal MSA merge, together with
`_validate_user_ccd_keys` against `docs/input.md`.
