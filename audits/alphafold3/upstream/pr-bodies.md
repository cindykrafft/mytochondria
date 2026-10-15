# PR bodies (google-deepmind/alphafold3 has no pull-request template; free text)

CONTRIBUTING.md asks three things of AI-assisted work, and each PR body below states them: the
AI generation is declared, the diff has been manually reviewed, and the change has been manually
tested. Those statements are the submitter's, so before opening either PR: read the diff on the
fork branch, and run the commands under "Testing" once yourself (the `verify/` directory has the
stub runners for a machine without the C++ build). The Google CLA must be on file first
(https://cla.developers.google.com/): PR #734 got the CLA-bot failure and the maintainer applied
the fix himself instead of merging. The base branch is `main`.

---

### PR 1 — `fix/to-json-preserves-chain-order` — "Keep chain order stable across a to_json / from_json round trip"

Fixes #NNN.

`Input.to_json()` grouped content-identical chains across the whole input, so two identical chains separated by a different chain were written together and the chain between them moved after them; `from_json` rebuilds `Input.chains` in the written order, so a round trip reordered the input. `run_alphafold.py` writes every job's `<name>_data.json` with `to_json()`, and the two-stage workflow in `docs/performance.md` feeds it back in, so the second stage ran on a different chain order (hence a different token layout and `asym_id`/`entity_id`/`sym_id` assignment) than an end-to-end run of the same JSON, although users are told that the order follows the `sequences` field (#476, #150). For a homodimer with a ligand between the copies, `A, B, C` came back as `A, C, B`.

This merges only *consecutive* content-identical chains, which keeps the written order faithful; the usual `"id": ["A", "B"]` layout is still collapsed, and interleaved copies are written as separate entries.

**Testing.** New test `test_to_json_keeps_chain_order_of_interleaved_duplicates` in `folding_input_test.py`: on `main` it fails with `['A', 'C', 'B'] != ['A', 'B', 'C']`, with the fix it passes. The existing `to_json` tests (`test_to_json` ×2, `test_to_json_sequence_deduplication`, `test_to_json_sequence_deduplication_round_trip`) pass on the branch, so adjacent duplicates are still merged. Run with

```
python src/alphafold3/common/folding_input_test.py -k to_json
```

The change does not touch inference; no model run was made for it.

**AI generation.** The analysis, the patch, the test and this description were produced with Claude Code. I have reviewed the diff and run the tests above myself before opening this PR.

---

### PR 2 — `fix/summary-confidences-chain-ids` — "Make summary_confidences chain_ids one entry per chain"

Fixes #NNN.

`StructureConfidenceSummary.from_inference_result` built `chain_ids` directly from `token_chain_ids`, so it carried one entry per token, each chain repeated once per token it owns. `docs/output.md` and the dataclass docstring describe it as a `[num_chains]` array "in the same order as all of the other chain-level arrays", and `chain_ptm`, `chain_iptm`, `chain_pair_pae_min` and `chain_pair_iptm` are per chain, so zipping `chain_ids` against them mislabelled the chains silently. On the run output shipped in `test_data` the field held 150 entries against 2 for `chain_ptm`.

This de-duplicates `token_chain_ids` keeping first-appearance order, which is the asym order the chain-level fields are built in, using the expression from #678, where this field was agreed as "the deduplicated unique chain ID list ... in the same order as the positional arrays". On the shipped test output the field becomes `['P', 'LL']`.

**Testing.** No unit test covers `confidence_types.py`; two scripts drive `from_inference_result` directly and check `len(chain_ids) == len(chain_ptm)`: a constructor-driven one (chains A with 3 tokens and B with 2: `['A', 'A', 'A', 'B', 'B']` before, `['A', 'B']` after) and one on `test_data/alphafold_run_outputs/run_alphafold_test_output_bucket_default.pkl` (150 entries before, `['P', 'LL']` after). Both are in the issue. The field is written by `write_outputs` only and nothing in the repository reads it back, so no other output changes. No model run was made for it.

**AI generation.** The analysis, the patch and this description were produced with Claude Code. I have reviewed the diff and run the two scripts above myself before opening this PR.

---

### PR 3 — `docs/performance-rna-z-value-and-continuation` — "Document the RNA Z-value in megabases and fix the example's line continuation"

Two fixes to the sharded-databases section of `docs/performance.md`:

1. The text asks users to save "the total number of nucleic bases in the RNA databases" for the RNA Z-value. Jackhmmer's `-Z` is a number of sequences, but Nhmmer's `-Z` is a database size in megabases ("set database size (Megabases) to <x> for E-value calculations"). The example values on the same page are already in megabases (`--rna_central_z_value=13271.415730` for about 13.3 Gb). #557 shows the same confusion: the answer there says "megabases" and also "the total length of all sequences". Following the prose gives a Z-value a million times too large, which inflates every RNA E-value by that factor, so hits are dropped from the RNA MSA without any warning. The text now asks for megabases and says why the units differ.
2. The `--rna_central_z_value=13271.415730` line of the example command has no trailing backslash. `run_alphafold.py` therefore starts without the four flags after it (`--jackhmmer_n_cpu`, `--jackhmmer_max_parallel_shards`, `--nhmmer_n_cpu`, `--nhmmer_max_parallel_shards`), and the shell then tries to run those lines as a separate command.

Documentation only; no code or test changes.

**AI generation.** The analysis, the patch and this description were produced with Claude Code. I have reviewed the diff myself before opening this PR.

