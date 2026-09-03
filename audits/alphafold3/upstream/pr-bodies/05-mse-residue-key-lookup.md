**Branch:** `fix/mse-residue-key-lookup` ·
[open this PR](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/mse-residue-key-lookup?expand=1)

**Title:** Look up MSE residues by key, not by position

---

### What is wrong

`src/alphafold3/structure/parsing.py:1631`:

```python
    met_residues_mask = (residues.name == 'MET')[atom_res_key]
```

`atom_res_key` holds residue **keys** (from
`string_array.remap_multiple(..., mapping=chain_res_builder.key_for_res)`), while
`(residues.name == 'MET')` is a boolean array indexed **positionally**. The two agree only
while every key equals its row index. `make_residues_table` sorts the residues table, so
when the `_atom_site` chain order differs from the order of the scheme tables the keys stop
matching positions and the mask lands on the wrong residues.

### Why it matters

A selenomethionine's selenium then keeps the name `SE` and element `SE` inside a residue
that has already been renamed `MET`. `SE` is not an ATOM37 atom name, so the residue
silently loses its `SD` downstream. `fix_mse_residues=True` is set for user-provided
template mmCIFs (`model/features.py:785`) and for `Input.from_mmcif`, and selenomethionine
is common in the crystal structures people supply as templates.

### Reproduction

The same mmCIF twice, differing only in the order of the two chains in `_atom_site`:

```
--- _atom_site chain order AB: residues.key=[0, 1, 2, 3, 4, 5] names=['ALA','MET','GLY','GLY','ALA','ALA']
   chain A res 2 -> atom names: ['N','CA','C','O','CB','CG','SD','CE']  elements: [...,'S',...]
   MET residue still containing an SE atom? False
--- _atom_site chain order BA: residues.key=[3, 4, 5, 0, 1, 2] names=['GLY','ALA','ALA','ALA','MET','GLY']
   chain A res 2 -> atom names: ['N','CA','C','O','CB','CG','SE','CE']  elements: [...,'SE',...]
   MET residue still containing an SE atom? True
```

This was run against a local build of the C++ extension with unmodified HEAD Python on
top, so it is the real parser, not a reimplementation.

### The change

Use `residues.apply_array_to_column('name', atom_res_key)`, which maps keys to values.

### Testing

With the patch applied, both chain orders give `SD`/`S` and no `MET` residue retains an
`SE` atom. I also re-ran a `to_mmcif` → `from_mmcif` round trip on the four wwPDB files in
`src/alphafold3/test_data` (5y2e, 6s61, 6ydw, 7rye) plus the bundled test template, all
atom-, residue-, bond- and chain-identical before and after the change:

```
5y2e.cif Structure(5Y2E: 1 chains, 45 residues, 353 atoms) bonds 0 | atoms same: True residues same: True bonds same: True
6s61.cif Structure(6S61: 2 chains, 173 residues, 2760 atoms) bonds 3 | atoms same: True residues same: True bonds same: True
6ydw.cif Structure(6YDW: 1 chains, 217 residues, 1775 atoms) bonds 0 | atoms same: True residues same: True bonds same: True
7rye.cif Structure(7RYE: 1 chains, 78 residues, 612 atoms) bonds 0 | atoms same: True residues same: True bonds same: True
```

I have not run a full prediction with released weights.

---

_This patch and description were written with AI assistance (Claude Code), disclosed per
CONTRIBUTING.md. The code and the reproductions above were reviewed and executed by me; no
test output here is hallucinated._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
