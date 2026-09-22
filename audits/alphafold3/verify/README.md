# Reproducers (2026-09-22, main a66cc52)

No C++ build or GPU here: `run_stubbed*.py <tree>/src` import the pure-Python modules from a
`git archive` of the tree with the compiled modules stubbed (see `../README.md`); the `.out`
files are their output on `main` and on the fix branch.

- `mcve_to_json_chain_order.py` → `mcve_to_json_chain_order.out` (AF1)
- `mcve_summary_confidences_chain_ids.py` → `mcve_summary_confidences_chain_ids.out` (AF2, constructor driven)
- `mcve_summary_confidences_shipped_output.py` → `mcve_summary_confidences_shipped_output.out` (AF2 on `test_data/alphafold_run_outputs/run_alphafold_test_output_bucket_default.pkl`: 150 entries vs 2 chains)
- `run_tests_stubbed.py` runs `folding_input_test.py`; `test-runs.txt` has the new test failing on `main` and the whole file on both trees (91 pass, the same 19 mmCIF/CCD-dependent errors on each)
- `0001-*.patch`, `0002-*.patch`: branch `fix/to-json-preserves-chain-order` (fix, test); `0003-*.patch`: `fix/summary-confidences-chain-ids`
