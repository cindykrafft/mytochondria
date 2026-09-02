# Structure parsing, mmCIF and the C++ core

Scope: `structure/parsing.py`, `structure/structure.py`, the table machinery, and the 14
C++ sources under `structure/cpp/` and `parsers/cpp/`. Tree: `main` @ `c0f97eda`.

This part of the review ran against a **real build of the C++ extension** (abseil,
pybind11 and pybind11_abseil fetched and compiled, then all 14 `.cc` files built
verbatim), with unmodified HEAD Python on top, so the results below are actual program
output rather than a reimplementation. The proposed fixes for S1 and S2 were applied to
patched copies and re-tested.

---

## S1 — `fix_mse_residues` indexes residues by key as if by position [verified]

`structure/parsing.py:1631`:

```python
    met_residues_mask = (residues.name == 'MET')[atom_res_key]
```

`atom_res_key` holds residue **keys**, produced by
`string_array.remap_multiple(..., mapping=chain_res_builder.key_for_res)`, while
`(residues.name == 'MET')` is a boolean array indexed **positionally**. The two agree
only while every key equals its row index. `make_residues_table` sorts the residues
table, so when the `_atom_site` chain order differs from the order of the scheme tables
the keys stop matching positions and the mask lands on the wrong residues.

The consequence is that a selenomethionine's selenium keeps the name `SE` and element
`SE` inside a residue that has already been renamed `MET`. Running the identical mmCIF
twice, differing only in the order of the two chains in `_atom_site`:

```
--- _atom_site chain order AB: residues.key=[0, 1, 2, 3, 4, 5] names=['ALA','MET','GLY','GLY','ALA','ALA']
   chain A res 2 -> atom names: ['N','CA','C','O','CB','CG','SD','CE']  elements: [...,'S',...]
   MET residue still containing an SE atom? False
--- _atom_site chain order BA: residues.key=[3, 4, 5, 0, 1, 2] names=['GLY','ALA','ALA','ALA','MET','GLY']
   chain A res 2 -> atom names: ['N','CA','C','O','CB','CG','SE','CE']  elements: [...,'SE',...]
   MET residue still containing an SE atom? True
```

`SE` is not an ATOM37 atom name, so the affected residue silently loses its `SD` atom
downstream. `fix_mse_residues` is hard-wired on for user template mmCIFs
(`model/features.py:785`) and for `Input.from_mmcif`, and selenomethionine is ubiquitous
in crystal structures used as templates.

The fix is `residues.apply_array_to_column('name', atom_res_key) == 'MET'`, which maps
keys to values. With it applied, both chain orders give `SD`/`S`, and the round-trip
tests on the four shipped wwPDB files still pass unchanged.

## S2 — `FixArginine` renames a lone HH22 to HH21 [verified]

`structure/cpp/mmcif_utils_pybind.cc:339-342`. The routine swaps the two guanidinium
branches and, where only one of a pair is present, renames it to its partner:
`HH11 <-> HH21`, `HH12 <-> HH22`. The last branch renames a lone `HH22` to `HH21`, which
belongs to the other pair:

```cpp
    } else if (hh22_index >= 0) {
      Py_DECREF(atom_ids[hh22_index]);
      Py_INCREF(hh21_.get());          // should be hh12_
      atom_ids[hh22_index] = hh21_.get();
    }
```

The residue comes out with the wrong atom name and, when an `HH21` is also present, with
two atoms called `HH21`. Fix verified on a patched build.

## S3 — Alt-loc resolution groups by consecutive runs [verified]

`structure/cpp/mmcif_altlocs.cc:105-174, 184-206` groups by consecutive runs of atom name
and comp id rather than by identity. Two consequences, both measured:

- Non-interleaved altlocs (all of conformer A, then all of conformer B) keep **both**
  conformers: 12 atoms where 6 are expected.
- Atom-interleaved microheterogeneity collapses a residue to a single atom.

Files in the wild are usually interleaved per atom, which is the case the run-grouping
was written for, so this is a robustness gap rather than an everyday defect.

## S4 — The `_entity_poly_seq` fallback mis-keys residues [verified]

`structure/parsing.py:1168-1185`, used when `_pdbx_poly_seq_scheme` is absent. Three
problems compound: the keys are per entity, so two chains sharing an entity with
different author numbering collide; `np.char.add` concatenates without a separator, so
`"1" + "12"` and `"11" + "2"` are the same key; and the insertion-code map is keyed by
`label_seq_id` alone. Valid files fail with a `ValueError` rather than parsing wrongly,
so this is loud. Post-`142e4bc` code.

## S5 — The CIF tokenizer discards quoting [verified]

`parsers/cpp/cif_dict_lib.cc:56-114, 412, 429, 728`. A quoted `"_x"` appearing in a
loop's first column is consumed as a loop key, shifting every subsequent column; a quoted
`"loop_"` ends the loop; and `parse_multi_data_cif` splits on `data_` occurring inside a
quoted value. The writer's own quoted output is therefore not always re-readable by the
reader. Reaching this needs a deliberately awkward file, hence the low severity.

---

## Exonerated

Thirteen areas were checked against a concrete failure mode and cleared: tokenizer
handling of semicolon text fields and `\r\n`; the writer's delimiter choice and multiline
emission; duplicate tags and loop counts; `.` and `?` normalisation across tables;
multi-model selection (first, all, and explicit) including bonds; `struct_conn`
symmetric matching and its symmetry, altloc and missing-atom dropping; bioassembly
operator composition, checked numerically so that `(1)(2)` really gives `R(x + t)`, and
the chain renaming that follows it; the layout `Filter` and offset arithmetic together
with `index_by_key`, `concat_databases` and the stable sorts; OpenMM-style table
inference; `fix_unknown_dna` and chem-comp handling; C++ bounds, refcount and lifetime
hygiene; and a full `to_mmcif` → `from_mmcif` round trip on the four shipped wwPDB files
with bonds, which is atom-, residue-, bond- and chain-identical.

Three items were examined and judged not worth filing: a bond with `alt_id='?'` against
altloc atoms raises loudly rather than silently mis-parsing; the chain label in one
`remap_res_id` error message is cosmetic; and per-model altloc differences in multi-model
files are a documented quirk of the 2grz test case.
