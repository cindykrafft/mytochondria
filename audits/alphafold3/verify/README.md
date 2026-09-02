# Verification scripts

Each script reproduces one finding against the code under test and prints the numbers
quoted in the component reviews. They are independent of the subagent harnesses used
during the review: these are the second, confirming implementation.

Run them with a Python 3.11+ environment holding `numpy`, `rdkit`, `jax`, `dm-haiku` and
(for C3's cross-check) `gemmi`. Most take the clone under test as `AF3`, so the same
script can be pointed at the shipped tree and at a patched one:

```bash
python -m venv af3venv && ./af3venv/bin/pip install numpy rdkit jax dm-haiku gemmi
git clone https://github.com/google-deepmind/alphafold3   # main @ c0f97eda
AF3=$PWD/alphafold3 ./af3venv/bin/python c2_chain_ids_length.py
```

| script | finding | needs |
|---|---|---|
| `c1_ccd_shared_mutation.py` | a user CCD mutates the process-global cached CCD dict | stdlib |
| `c2_chain_ids_length.py` | `summary_confidences` `chain_ids` is per token, not per chain | `AF3`, numpy |
| `c3_selenocysteine_mapping.py` | `SEC` maps to alanine rather than cysteine | `AF3`, gemmi optional |
| `c4_hydrogen_name_bond_filter.py` | ligand bonds to mercury dropped as if hydrogen | rdkit |
| `c5_msa_pairing_unstable_sort.py` | unstable species sort breaks the documented pairing order | numpy |
| `c6_rna_zvalue_units.py` | RNA Z-value documented in bases, nhmmer wants megabases | HMMER on PATH |
| `c7_template_hit_keep_alignment_error.py` | `AlignmentError` escapes `Hit.keep` | `AF3` (see note) |
| `c8_cross_attention_key_mask.py` | the cross-attention key mask is a no-op | numpy |
| `c9_cross_attention_patch_check.py` | the same, against the real module, shipped vs patched | jax, haiku, stub tree |
| `c10_nucleic_backbone_frame_idx.py` | DNA backbone frames select the base nitrogen | `AF3`, numpy |

Notes.

`c1` reproduces the `Ccd` constructor verbatim, stubbing only the pickle loader and the
CIF parser, neither of which takes part in the aliasing under test. Running the real
class needs the CCD pickle, which is built by `build_data` from a download.

`c7` needs `alphafold3.cpp.fasta_iterator`, reached through `data/parsers.py`, so it runs
only where the compiled extension is available. The mechanism is visible without it: the
`is_valid` call at `templates.py:357` sits outside the `try` that catches
`AlignmentError` at `:361`.

`c9` reuses the stub package from the network review (a `tokamax` stub implementing the
documented kernel semantics) and takes `TREE=shipped|patched` rather than `AF3`.

Findings verified with tooling that is impractical to ship here are described in the
component reviews with their measured output: the mmCIF work ran against a full local
build of the C++ extension, and the MSA tool-level claims against HMMER 3.4 binaries.
