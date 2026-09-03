**Branch:** `fix/msa-pairing-stable-sort` ·
[open this PR](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/msa-pairing-stable-sort?expand=1)

**Title:** Group MSA rows by species with a stable sort

---

### What is wrong

`create_paired_features` groups MSA rows by species with
`src/alphafold3/model/msa_pairing.py:137`:

```python
    sort_idxs = species_ids.argsort()
```

numpy's default sort kind is quicksort, which is not stable, so rows within one species
come out in an arbitrary order.

`_align_species` documents the opposite (`msa_pairing.py:47-49`):

> Within a species, MSAs are aligned based on their original order (the first sequence for
> a species in the first chain's MSA is aligned to the first sequence for the same species
> in the second chain's MSA).

and then crops each species to the smallest per-chain hit count (`:79`):

```python
        row_indices = species_to_rows[species][:min_msa_size]
```

Both the pairing and the crop depend on the grouping preserving MSA order.

### Why it matters

a3m rows arrive best-hit-first — I confirmed with a real jackhmmer run that the row order
is ascending E-value order (0 inversions over a 259-hit MSA). So the crop is meant to keep
the best-ranked homologs for a species; with an unstable sort it keeps arbitrary ones, and
pairs rows the docstring says should not be paired. The crop happens before the rank
metric sorts the paired rows, so rows dropped here cannot be recovered later.

It bites whenever two chains have different hit counts for a species, which is the normal
case for a heteromer.

### Reproduction

Two-chain heteromer, 8000- and 3000-row uniprot MSAs over 400 species, grouping code
verbatim:

```
chain A: 401 species, 400 of them come out NOT in original MSA order
chain B: 401 species, 388 of them come out NOT in original MSA order

paired rows kept for chain A: 2995
median MSA rank kept, shipped (unstable) : 4003
median MSA rank kept, stable sort        : 1626
rows in common between the two           : 1332 of 2995
rows from the MSA top 100, shipped 30 vs stable 99
chain-A rows paired against a different chain-B row than documented: 2853
```

Script: `verify/c5_msa_pairing_unstable_sort.py` in the linked audit repository.

To be precise about the failure mode: the result is deterministic for a given input and
numpy version, so this is not run-to-run nondeterminism. It is arbitrary with respect to
MSA rank, and a numpy change could shift it.

### The change

`argsort(kind='stable')`, plus a comment saying why the stability is load-bearing.

### A question for you

This changes which sequences reach the model for every multimer with paired MSAs, so
whether it is an improvement depends on what the model was trained against — which you
know and I do not. If the training pipeline used an unstable sort too, then reproducing it
is the correct behaviour and the docstring is what should change instead. Happy to close
this in favour of a comment if that is the case.

### Testing

The reproduction above, on the shipped and patched grouping. I have not run a full
prediction with released weights.

---

_This patch and description were written with AI assistance (Claude Code), disclosed per
CONTRIBUTING.md. The code and the reproduction above were reviewed and executed by me; no
test output here is hallucinated._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
