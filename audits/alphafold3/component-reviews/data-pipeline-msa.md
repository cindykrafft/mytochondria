# Data pipeline: MSA search, parsing and pairing

Scope: `data/pipeline.py`, `data/msa*.py`, `data/parsers.py`, `data/tools/`,
`model/msa_pairing.py`, and the sharded-search documentation. Tree: `main` @ `c0f97eda`.
HMMER 3.4 was installed in the audit environment, so the tool-level claims below were
checked against the real `jackhmmer` and `nhmmer` binaries.

---

## M1 — An unstable sort scrambles the documented within-species pairing order [verified]

`model/msa_pairing.py:137`:

```python
    sort_idxs = species_ids.argsort()
```

numpy's default sort kind is quicksort, which is not stable, so rows within one species
emerge in an arbitrary order. `_align_species` documents exactly the opposite
(`msa_pairing.py:47-49`):

> Within a species, MSAs are aligned based on their original order (the first sequence
> for a species in the first chain's MSA is aligned to the first sequence for the same
> species in the second chain's MSA).

and then crops each species to the smallest per-chain hit count (`:79`):

```python
        row_indices = species_to_rows[species][:min_msa_size]
```

a3m rows arrive in ascending E-value order — confirmed by running real jackhmmer, 0
inversions over a 259-hit MSA — so "original order" means "best hit first". With an
unstable sort the crop keeps arbitrary homologs rather than the best-ranked ones, and
pairs rows the docstring says should not be paired.

[`../verify/c5_msa_pairing_unstable_sort.py`](../verify/c5_msa_pairing_unstable_sort.py),
on a two-chain heteromer with 8000- and 3000-row uniprot MSAs over 400 species:

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

The crop happens *before* the rank metric sorts the paired rows, so rows lost here cannot
be recovered later. It bites whenever two chains have different hit counts for a species,
which is the normal case for a heteromer.

The result is deterministic for a given input and numpy version — this is not run-to-run
noise — but it is arbitrary with respect to MSA rank, and a numpy change could shift it.
The fix is one keyword, `argsort(kind='stable')`.

Whether better-ranked pairing improves accuracy is a question for the maintainers, who
know what the model was trained against. What is not in question is that the code does
not do what its own docstring says.

## M2 — The docs give the RNA Z-value in bases; nhmmer wants megabases [verified]

`docs/performance.md:118-120`:

> Save the total number of sequences in the protein databases, and the total number of
> nucleic bases in the RNA databases – these will be needed later as a flag to
> Jackhmmer/Nhmmer to correctly scale e-values across all shards.

Correct for Jackhmmer, wrong for Nhmmer. From the installed binaries:

```
nhmmer    -Z <x>             : set database size (Megabases) to <x> for E-value calculations  (x>0)
jackhmmer -Z <x>        : set # of comparisons done, for E-value calculation
```

The example values further down the same page are already megabase-scale
(`--rna_central_z_value=13271.415730` for a database of about 13.3 Gb), and
`data/msa_config.py:88` documents the parameter correctly as megabases. So the prose and
the example disagree by a factor of a million, and a user who follows the prose passes a
Z that is a million times too large. E-values scale linearly with Z, so hits drop below
the inclusion threshold and the RNA MSA is silently shallower.

[`../verify/c6_rna_zvalue_units.py`](../verify/c6_rna_zvalue_units.py), with real nhmmer:

```
-Z given in megabases (the doc example):       best E-value 4.6e-36, 2 hit(s) kept at -E 1e-3
-Z given in bases (the doc prose):             best E-value 4.6e-30, 2 hit(s) kept at -E 1e-3

E-values inflated by a factor of 1e+06 purely from the unit.
  at -E 1e-3    megabases keeps 2, bases keeps 2
  at -E 1e-9    megabases keeps 2, bases keeps 1
  at -E 1e-15   megabases keeps 1, bases keeps 1
```

## M3 — The sharded example command is split by a missing backslash [verified]

`docs/performance.md:143`. The `--rna_central_z_value=13271.415730` line carries no
trailing `\`, so the four flags after it — `--jackhmmer_n_cpu`,
`--jackhmmer_max_parallel_shards`, `--nhmmer_n_cpu`, `--nhmmer_max_parallel_shards` —
are parsed as a separate command and silently dropped. Since the surrounding prose is
about tuning exactly those, a user copying the block gets none of the tuning. The same
class of defect was fixed in `docs/installation.md` by `8a84535`; this occurrence
remains.

---

## Excluded as already reported

The paired-row rank metric at `msa_pairing.py:180` computes
`np.abs(np.prod(rows.astype(np.float32), axis=1))`, which overflows to `+inf` in float32
for complexes with roughly a dozen or more distinct chains and deep MSAs, collapsing the
ranking into ties. This review reproduced it and then found it is **open pull request
#719**, "Avoid float32 overflow when ranking paired MSA rows", and the source of **open
issue #236**, "RuntimeWarning: overflow encountered in reduce". Not claimed here.

---

## Exonerated

Disproved by execution rather than argument: the protein, RNA and DNA integer alphabets
match `residue_names` exactly across all 27-plus entries; the species regex matches
1000 of 1000 real UniProt headers; nhmmer's `-A` output is bounded by
`min(-E, --incE)`, so the missing `--incE` is not a tenfold leak (tested at four
thresholds); `jackhmmer -h --seq_limit 1` exits 1 on stock HMMER 3.4, so the capability
probe is correct; sharded and unsharded jackhmmer produce identical hit sets with the
same ordering, cap and query placement, and featurise identically; and the full
nhmmer → hmmbuild → hmmalign → featurise RNA chain emits no `.` characters and maps
database `T` to `U` correctly (25, not UNK 30).

Two things deliberately not filed. Every monomer and homomer receives a duplicate query
row — confirmed in the shipped `featurised_example.pkl`, where `num_alignments=2` with
both rows identical — which is almost certainly training-consistent behaviour rather
than a defect. And `data/msa_identifiers.py` is unreachable dead code, so its regex,
which diverges from the one actually used, cannot misbehave.

The MSA-depth difference against the AlphaFold Server is documented in
`docs/known_issues.md` (the Server runs sharded Jackhmmer without `--domZ`) and was
treated as out of bounds throughout.
