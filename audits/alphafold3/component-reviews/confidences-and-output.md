# Confidence metrics, ranking and output writing

Scope: `model/confidences.py`, `model/confidence_types.py`, `model/scoring/`,
`model/network/confidence_head.py`, `model/post_processing.py`,
`model/mmcif_metadata.py`, and `docs/output.md`. Tree: `main` @ `c0f97eda`.

These are the numbers papers quote, so every metric was compared against an independent
float64 implementation of the published formula on small hand-built inputs, and against
the confidence quantities stored in the run output shipped in `test_data`. The harness
records 30 checks passing and 3 failing, the failures being the findings below.

---

## C1 — `chain_ids` in `summary_confidences.json` is per token, not per chain [verified]

`model/confidence_types.py:194`:

```python
    chain_ids = [str(c) for c in inference_result.metadata['token_chain_ids']]
```

`token_chain_ids` is a `[num_tokens]` array (`docs/output.md:209`), but `chain_ids` is
documented at `docs/output.md:195` as

> A \[num_chains\] array with chain IDs in the same order as all the other chain-based
> fields

and the neighbouring fields really are per chain. Anything that zips `chain_ids` against
`chain_ptm`, `chain_iptm`, `chain_pair_pae_min` or `chain_pair_iptm` — which is the
stated purpose of the field — misaligns silently.

Measured on the shapes of the run output shipped in `test_data`
([`../verify/c2_chain_ids_length.py`](../verify/c2_chain_ids_length.py)):

```
len(chain_ids)      = 150  <- docs/output.md:195 declares [num_chains]
len(chain_ptm)      = 2
len(chain_iptm)     = 2
chain_pair_iptm     = (2, 2)
chain_ids[:8]       = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']

chain_ids aligns with the chain-based fields: False
de-duplicated chain_ids would be: ['P', 'L']
```

Introduced by `e68269f` "Add chain IDs in the summary confidence JSON for easier use", so
it is newer than v3.0.4 and affects the field's only purpose. De-duplicating with
`dict.fromkeys` preserves first-appearance order, which is the asym order the chain-based
fields are built in.

## C2 — Per-residue pLDDT rows merge for multi-residue ligand chains [verified]

`model/mmcif_metadata.py:200-206` groups `_ma_qa_metric_local` rows by
`(label_asym_id, label_seq_id, label_comp_id)`. Non-polymer chains carry
`label_seq_id = '.'`, so two residues of a branched or glycan chain that share a
component id collapse into a single averaged row:

```
NAG(90) + NAG(10) -> single row ('B', '.', 'NAG', '50.00')
```

The written mmCIF then reports one pLDDT for what were two sugar residues. Adding
`auth_seq_id` (and the insertion code) to the key separates them.

## C3 — The documented pTM floor for short chains is too low [verified]

`docs/output.md` states that pTM is below 0.05 for chains shorter than 20 tokens. The
implemented formula clips `d0` at `N = 19`, giving `d0 = 0.168 Å`, so the TM term for the
lowest PAE bin is 0.312 and a confident short peptide can reach pTM of roughly 0.15 to
0.31. Documentation defect only; the computation matches the paper.

---

## Exonerated

Twenty items were checked against ground truth and cleared: PAE, PDE and pLDDT bin
centres; the `d0` formula and its clipping; the choice of `N` (global versus per pair);
the expectation over PAE bins; pTM, ipTM and chain-pair ipTM against a brute-force
implementation of the published formula; the cross-chain aggregations including their
handling of ion chains that produce NaNs; `chain_pair_pae` and `chain_pair_pde`; the
ranking formula and both its NaN and clash paths; PAE asymmetry; padding masks; chain
ordering; RASA parsing, its window and its short-chain handling; the `has_clash`
thresholds; the Kabsch alignment, which matches scipy to 1e-14; and JSON rounding. Seven
stored metadata quantities were reproduced exactly from the shipped run output, including
`ranking_score` 0.705825683153766.

Five items were measured and deliberately not filed, all because they do not reach an
exported number or are clearly intended: the `1e-8` epsilon in `weighted_mean` biases
one-token chains in unexported PDE and PAE aggregates by -4.7e-4 at N=13; the RASA
maximum-ASA fallback to alanine for DSSP `X` and lowercase-cysteine letters is latent,
since AlphaFold 3 writes only `covale` bonds and DSSP 4.4.7 reads disulfides from
`_struct_conn`; `contact_probs` integrates to 7.9375 Å rather than the documented 8 Å,
which is the bin edge; `has_clash` is serialised as `0.0`/`1.0`; and `average_pde` uses a
bfloat16 denominator but is not exported.

The known issue that CUDA capability 7.x GPUs produce clashing output with a ranking
score at or below -99 is a hardware and XLA numerics matter, documented upstream, and was
treated as out of bounds.
