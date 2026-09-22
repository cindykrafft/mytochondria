"""AlphaFold 3: Input.to_json() reorders chains when identical chains are separated by a different chain.

Run inside an AlphaFold 3 install:  python mcve_to_json_chain_order.py
Prints the chain order before and after one to_json/from_json round trip.
"""
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
