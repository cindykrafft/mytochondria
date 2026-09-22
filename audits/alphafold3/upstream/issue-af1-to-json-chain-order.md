Title: `Input.to_json()` reorders chains when identical chains are separated by a different chain, so `<name>_data.json` does not describe the run that produced it

<!-- google-deepmind/alphafold3 has no issue template. Prior-report search 2026-09-22 (to_json / chain order / data.json reordered / from_json order): no match; the nearest threads are questions about the "id" list (#356) and about the chain order of the chain-level confidence arrays (#150), neither reports this. Verified on main a66cc52 by running the round trip in pure Python (audits/alphafold3/verify/mcve_to_json_chain_order.out); no model run was made. -->

`Input.to_json()` (`src/alphafold3/common/folding_input.py`) merges chains with identical content into one `sequences` entry carrying a list of ids. It groups by content across the *whole* input, so two identical chains that are separated by a different chain are written together, at the position of the first one, and the chain that sat between them is written after them. `Input.from_json()` rebuilds `Input.chains` in the order the entries are written, so one round trip through `to_json` changes the chain order.

`run_alphafold.py` writes `<name>_data.json` with `to_json()` for every job, and the documented two-stage workflow (`--run_inference=false`, then inference from that JSON; `docs/performance.md`, "Data Pipeline Only") feeds that file back in. For an input like the one below the second stage therefore runs on a different chain order than a single end-to-end run of the same JSON: `Input.to_structure` lays the tokens out in chain order and `_compute_asym_entity_and_sym_id` assigns `asym_id`, `entity_id` and `sym_id` by first appearance in that layout, so the model input differs, and the output structure lists the chains in the new order. Nothing warns: the `_data.json` simply records a different complex than the one that was submitted.

Minimal example, pure Python (no model run):

```python
import json
from alphafold3.common import folding_input

INPUT = {
    "name": "homodimer_with_ligand_between",
    "modelSeeds": [1],
    "sequences": [
        {"protein": {"id": "A", "sequence": "MKTAYIAKQRQISFVKSHFSRQ"}},
        {"ligand": {"id": "B", "smiles": "CC(=O)O"}},
        {"protein": {"id": "C", "sequence": "MKTAYIAKQRQISFVKSHFSRQ"}},
    ],
    "dialect": "alphafold3",
    "version": 1,
}

fold_input = folding_input.Input.from_json(json.dumps(INPUT))
before = [c.id for c in fold_input.chains]
round_tripped = folding_input.Input.from_json(fold_input.to_json())
after = [c.id for c in round_tripped.chains]
print("chain order before round trip:", before)
print("chain order after  round trip:", after)
print("sequences emitted by to_json: ", [list(s.values())[0]["id"] for s in json.loads(fold_input.to_json())["sequences"]])
assert after == before, "to_json/from_json changed the chain order"
```

On `main` (a66cc52) the output is

```
chain order before round trip: ['A', 'B', 'C']
chain order after  round trip: ['A', 'C', 'B']
sequences emitted by to_json:  [['A', 'C'], 'B']
AssertionError: to_json/from_json changed the chain order
```

Expected: `['A', 'B', 'C']` after the round trip, i.e. `sequences` written in the input order. The grouping code is the same in v3.0.1 through v3.0.4 (v3.0.0 wrote one entry per chain and did not have this).

Inputs with non-adjacent identical chains are ordinary: a homodimer with the ligand or cofactor listed between the two copies, or an antibody heavy/light pair followed by a second copy of the same antigen.

Proposed fix: merge only *consecutive* content-identical chains. That keeps the written order faithful and still collapses the usual `"id": ["A", "B"]` layout; interleaved copies are written as separate entries, which `from_json` accepts. The change with a regression test (fails on `main` with `['A', 'C', 'B'] != ['A', 'B', 'C']`, passes with the fix; the four existing `to_json` tests, including `test_to_json_sequence_deduplication`, still pass) is on https://github.com/cindykrafft/alphafold3/compare/main...fix/to-json-preserves-chain-order and I can open it as a pull request.
