# Featurisation, atom layout and chemical components

Scope: `model/features.py`, `model/atom_layout/atom_layout.py`, `model/pipeline/`,
`constants/`, `structure/chemical_components.py`, `data/tools/rdkit_utils.py`.
Tree: `main` @ `c0f97eda` (post-v3.0.4). Verification scripts in [`../verify/`](../verify/).

Legend: **[verified]** executed against the shipped code; **[code-read]** mechanism
unambiguous from the source; **[latent]** wrong but not reachable today.

---

## A1 — A user CCD permanently overwrites the process-global CCD cache [verified]

`constants/chemical_components.py:73,82`:

```python
    self._dict = _load_ccd_pickle_cached(self._ccd_pickle_path)
    ...
      self._dict.update(user_ccd_cifs)
```

`_load_ccd_pickle_cached` is `@functools.cache`d on the pickle path, so every `Ccd`
built from the default path receives *the same dict object*, and `update` mutates it
in place. The class docstring says the opposite: "Wraps the dict to prevent accidental
mutation", and `__hash__` returns `id(self)` with the comment "Ok since this is
immutable."

`run_alphafold.py:1067` loops over every fold input in one process, and
`predict_structure` (`:585`) builds a fresh `Ccd(user_ccd=fold_input.user_ccd)` per
input. A `userCCD` from one job therefore stays visible to every later job, and an
entry that deliberately overrides a standard CCD code — a documented use of `userCCD`
— keeps overriding it for inputs that supply no `userCCD` at all. The internal
default-CCD consumers (`scoring/chirality.py:129`, `structure/mmcif.py:177`) see it too.

Reproduced in [`../verify/c1_ccd_shared_mutation.py`](../verify/c1_ccd_shared_mutation.py):

```
job1  len=3  LIG=['USER LIG']  ALA=['USER ALA']
job2  len=3  LIG in job2: True
job2  ALA=['USER ALA']   (should be ['real ALA'])
job3  len=4  sees job1 LIG: True

LEAK ACROSS INPUTS: True
all three share one dict object: True
```

Everything downstream of a corrupted entry is affected: `make_flat_atom_layout` (which
atoms exist, hence the token count for that residue), the tokenizer's per-token atom
slots and canonical order, `get_reference` (`ref_pos`, `ref_element`, `ref_charge`,
`ref_atom_name_chars`) and the intra-ligand bond graph. The failure is silent and
order-dependent: the second job simply models a different molecule.

**Origin.** Introduced by `a8ecdb2` "Cache the underlying CCD dictionary instead of the
whole CCD object", which is the memory fix for the closed issue #509 (~3 GB per user
CCD). Before it, each `__init__` unpickled its own copy and `update` was per-instance
and correct. Worth noting for the upstream report: PR #514 proposed fixing #509 with a
`collections.ChainMap` overlay onto a shared base, and a `ChainMap` never writes to its
base — that shape would not have had this effect. It was closed in favour of `a8ecdb2`,
which caches the dict but keeps the in-place `update`. The fix here keeps the memory win:
overlay onto a shallow copy (`{**shared, **user_ccd_cifs}`), so only the top-level dict is
duplicated and the component values stay shared.

Two independent agents found this one from different directions (the chemical-component
review and the featurisation review), which is why it heads the list.

## A2 — Bonds to mercury are deleted as if they were hydrogens [verified]

`model/features.py:1295-1300`, in `LigandLigandBondInfo.compute_features`:

```python
      # Remove any bonds to Hydrogen atoms.
      bond_layout = bond_layout[
          ~np.char.startswith(bond_layout.atom_name.astype(str), 'H').any(
              axis=1
          )
      ]
```

The test is on the atom *name*, not the element. AlphaFold 3 names ligand atoms as the
uppercased element symbol plus a counter (`rdkit_utils.py:520-525`, whose own comment
notes "'Cl' becomes 'CL'"), so mercury is `HG1`, hafnium `HF1`, holmium `HO1`. Every
bond row touching one of them is dropped.

The filter also cannot do the job its comment describes. The `keep_mask` immediately
above it (`:1271-1294`) keeps only bonds whose two endpoints appear in `all_tokens`, and
that flat layout already drops hydrogens **by element** (`atom_layout.py:845-848`,
`e != 'H' and e != 'D'`). By this point no hydrogen bond can remain, so the name test
can only produce false positives on heavy atoms.

[`../verify/c4_hydrogen_name_bond_filter.py`](../verify/c4_hydrogen_name_bond_filter.py),
for the methylmercury motif `C[Hg]Cl`:

```
atoms          : [('C1', 'C'), ('HG1', 'Hg'), ('CL1', 'Cl'), ('H1', 'H'), ('H2', 'H'), ('H3', 'H')]
flat layout atoms (hydrogens dropped by element): ['C1', 'CL1', 'HG1']
after keep_mask: [('C1', 'HG1'), ('HG1', 'CL1')]  <- already contains no hydrogen bond
after the startswith("H") filter: []

the ligand reaches token_bonds with 0 of its 2 covalent bonds
```

Organomercurials are not exotic in the PDB: heavy-atom derivatives for phasing,
thimerosal, methylmercury adducts. Larger ones lose exactly the bonds that anchor the
metal. The same applies to a user `bondedAtomPairs` entry touching such an atom, and to
any CCD ligand with an atom named `HG`. Present since the initial release `4f52a3b`.

## A3 — Template features are cached per sequence, so per-chain templates are discarded [verified]

`model/features.py:771-782, 814-818`. Template features are computed once per
`entity_id` (derived only from the three-letter sequence) and cached;
`templates_by_chain_id[chain_id]` is read **only** in the cache-miss branch. A second
chain with the same sequence reuses the first chain's features and its own templates are
never opened.

The MSA path deliberately does not do this: `Msa.compute_features`
(`features.py:451-540`) uses `seen_entities` only to *label* `entity_id` and reads
`unpaired_msa_by_chain_id[b_chain_id]` per chain. The two paths disagree about whether
per-chain inputs are honoured, and the comment at `:819-821` ("each chains templates
can't see each other") assumes the per-chain reading.

Such an input is representable and is built per chain by the pipeline
(`model/pipeline/pipeline.py:459`); `folding_input.hash_without_id` includes `_templates`
(`folding_input.py:308-317`), so the two chains stay distinct objects. Executed with a
tracer on the template read:

```
templates_by_chain_id actually read for chains: ['A']
  chain A -> templates ['tmplA_1', 'tmplA_2']
  chain B -> templates ['tmplA_1', 'tmplA_2']
RESULT: chain B's own templates ['tmplB_1'] were silently discarded.
```

Symmetric homomers, where both chains carry the same templates, are unaffected — so this
bites precisely the users who deliberately supply asymmetric template evidence.

## A4 — `TypeError` on the library entry point's own default [verified]

`model/features.py:1530`:

```python
    max_modified_date = max(modified_dates)
    if max_modified_date < ref_max_modified_date:
```

The parameter is annotated `datetime.date` (`:1507`) but is `None` all the way down the
public path: `data/featurisation.py:51` and
`model/pipeline/pipeline.py:145` (`WholePdbPipeline.Config.ref_max_modified_date`) both
default it to `None`. The branch is entered whenever a component's CCD ideal coordinates
contain `?` — which is what sends `get_reference` into this fallback in the first place.

```
explicit date (run_alphafold.py path) -> [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]]
None (featurise_input default)        -> TypeError: '<' not supported between
                                         instances of 'datetime.date' and 'NoneType'
```

`run_alphafold.py` always passes `max_template_date`, so the CLI is safe. Library users
of the documented `alphafold3.data.featurisation.featurise_input`, or of
`WholePdbPipeline` with a default `Config`, are not.

## A5 — DNA backbone frames select the base nitrogen [verified, latent]

`model/protein_data_processing.py:69-77` resolves `C1'`/`C3'`/`C4'` once against RNA
adenosine and writes those indices for all eight nucleic residue types. DNA rows of
`DENSE_ATOM` have no `O2'`, so every atom from `C1'` onwards sits one slot earlier:

```
  DA  idx=[12, 8, 6]   -> ['N9', "C3'", "C4'"]   <-- selects the base nitrogen
  DC  idx=[12, 8, 6]   -> ['N1', "C3'", "C4'"]   <-- selects the base nitrogen
nucleic residue types with a wrong backbone frame: 4 of 8
```

The sibling `_make_restype_pseudobeta_idx` (`:100-108`) already resolves per residue
type, which is what marks this as an oversight rather than a convention. Latent in
v3.0.4: the table's only consumer (`template_modules.py:299-306`) is indexed by template
aatype, and `Templates.compute_features` produces protein aatypes only. The table is
shipped wrong regardless. Script:
[`../verify/c10_nucleic_backbone_frame_idx.py`](../verify/c10_nucleic_backbone_frame_idx.py).

## A6 — `seen_entities` is never populated in `MSA.compute_features` [code-read, latent]

`model/features.py:439, 485-488`. The dict is initialised and read but written only in
`Templates.compute_features` (`:814`), so the lookup never hits and every chain gets
`entity_id = 1`. Latent: `feats['entity_id']` is not copied into `cropped_chain`
(`:585-590`) and `msa_pairing` never reads it; the token-level `entity_id` the network
sees comes from the independent and correct `_compute_asym_entity_and_sym_id`
(`:128-168`). Dead-but-wrong code sitting beside correct code that does the same job.

## A7 — Selenocysteine is remapped to alanine [verified]

`constants/residue_names.py:199`:

```python
    'SEB': 'S', 'SEC': 'A', 'SEG': 'A', 'SEL': 'S', 'SEM': 'S', 'SEN': 'S',
```

`CCD_NAME_TO_ONE_LETTER` feeds `structure.fix_non_standard_polymer_residues`
(`structure.py:200`) and `mmcif_names.py:207`, which map the one-letter code back through
`PROTEIN_COMMON_ONE_TO_THREE`. Selenocysteine therefore becomes `ALA`:

```
code  letter   becomes  name
SEC   A        ALA      selenocysteine
MSE   M        MET      selenomethionine
CSO   C        CYS      s-hydroxycysteine

cysteine-family codes (CS*/CY*/SC*): 38, mapping to {'C': 35, 'N': 1, 'G': 1, 'X': 1}
gemmi 0.7.5 CCD-derived table: SEC one_letter='U' is_standard=True kind=ResidueKind.AA
```

Selenocysteine is the selenium analogue of cysteine, exactly as selenomethionine is of
methionine, and `MSE -> M` is the precedent in the same table. Mapping it to alanine
deletes the side-chain chalcogen entirely. Script:
[`../verify/c3_selenocysteine_mapping.py`](../verify/c3_selenocysteine_mapping.py).

**Caveat.** RCSB, EBI and PDBj are all blocked by this environment's egress proxy, so the
CCD's own `mon_nstd_parent_comp_id` field could not be fetched directly. The argument
rests on the table's internal convention, gemmi's CCD-derived table, and the chemistry.
Filed as a question rather than a patch for that reason.

---

## Exonerated

Checked against a concrete failure mode and cleared. From the featurisation review:
`data3.fix_template_features` gathering atom37 index 0 into unused dense slots (never
read); the padding-atom UID collision in `compute_gather_idxs` (neutralised by
`queries_mask` before any activation); `AtomCrossAtt` negative key-window indices (always
land on padding); SMILES atom naming agreeing between the layout and the reference
conformer (verified with real rdkit — `AddHs` appends hydrogens after all heavy atoms);
`get_random_conformer` on embedding failure (`ETKDGv3.clearConfs` defaults True, so the
`except` path is taken as intended); `ref_mask == 1` with all-zero `ref_pos` (by design;
`Frames.compute_features` handles the collapsed case explicitly); `structure_cleaning`
leaving-atom order versus the bond filters (the earlier filter is strictly tighter);
the `clean_structure` fast versus slow path for glycan O1 (divergence unreachable from
`to_structure`); the `inter_chain_bonds` axis-1 reduction (single-model only);
`PolymerLigandBondInfo` renaming endpoints to CA/C1' (deliberate coarsening, the
atom-level consumer sees the true atoms); `AtomLayout.to_array` docstring field order
(documentation only, the round trip is consistent); `residues_from_structure`
start-terminus rule; `MSA_GAP_IDX` alphabet (`'-'` is 21 in both alphabets); one-hot
depths (32, 31, 128, 64); `side_chains.CHI_ANGLES_MASK` row ordering;
`_remove_multi_bonds`'s over-aggressive greedy pass (not reached by the pipeline).

From the chemical-component review: periodic-table values against RDKit; the atom
tables; one-hot orderings; the value range of the 1248-entry residue table;
`safe_pickle`'s allowlist; `mmcif_metadata` terms-of-use handling; `structure/bonds.py`;
`structure/chemical_components.py`; `mmcif_names.py`; the build and pickle generators;
`fetch_databases.sh` and the Dockerfile; the installation docs.

One cosmetic item not filed: `constants/periodic_table.py:127` spells niobium `'Niobiu'`.
The `name` field is never used in any computation.
