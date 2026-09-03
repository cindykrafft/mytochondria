**Branch:** `fix/ligand-bond-hydrogen-filter` ·
[open this PR](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/ligand-bond-hydrogen-filter?expand=1)

**Title:** Stop dropping ligand bonds to atoms whose name starts with H

---

### What is wrong

`LigandLigandBondInfo.compute_features` filters ligand-ligand bonds by atom **name**
(`src/alphafold3/model/features.py:1295-1300`):

```python
      # Remove any bonds to Hydrogen atoms.
      bond_layout = bond_layout[
          ~np.char.startswith(bond_layout.atom_name.astype(str), 'H').any(
              axis=1
          )
      ]
```

AlphaFold 3 names ligand atoms as the uppercased element symbol plus a counter
(`data/tools/rdkit_utils.py:520-525`, whose comment notes "'Cl' becomes 'CL'"), so mercury
is `HG1`, hafnium `HF1`, holmium `HO1`. Every bond row touching one of those is dropped as
if it were a bond to hydrogen.

The filter also cannot do the job its comment describes. The `keep_mask` immediately above
it (`:1271-1294`) already keeps only bonds whose two endpoints appear in `all_tokens`, and
that flat layout drops hydrogens **by element** (`atom_layout.py:845-848`,
`e != 'H' and e != 'D'`). By the time this line runs there is no hydrogen bond left to
remove, so the name test can only produce false positives on heavy atoms.

### Why it matters

For the methylmercury motif `C[Hg]Cl` the ligand reaches `token_bonds` with none of its
covalent bonds, leaving three unconnected tokens. Larger organomercurials lose exactly the
bonds that anchor the metal. Organomercury is not exotic in the PDB — heavy-atom
derivatives for phasing, thimerosal, methylmercury adducts. The same applies to any CCD
ligand with an atom named `HG`, and to a user `bondedAtomPairs` entry touching such an atom.

### Reproduction

Real RDKit naming plus the filter verbatim:

```
ligand C[Hg]Cl
atoms          : [('C1', 'C'), ('HG1', 'Hg'), ('CL1', 'Cl'), ('H1', 'H'), ('H2', 'H'), ('H3', 'H')]
bonds from CCD : [('C1', 'HG1'), ('HG1', 'CL1'), ('C1', 'H1'), ('C1', 'H2'), ('C1', 'H3')]

flat layout atoms (hydrogens dropped by element): ['C1', 'CL1', 'HG1']
after keep_mask: [('C1', 'HG1'), ('HG1', 'CL1')]  <- already contains no hydrogen bond
after the startswith("H") filter: []

dropped by the H filter: [('C1', 'HG1'), ('HG1', 'CL1')]
the ligand reaches token_bonds with 0 of its 2 covalent bonds
every bond dropped here joins a heavy atom, not a hydrogen: True
```

Script: `verify/c4_hydrogen_name_bond_filter.py` in the linked audit repository.

### The change

Remove the filter. It is dead weight for its stated purpose, as shown above, and actively
harmful for heavy atoms whose names begin with H.

If you would rather keep a belt-and-braces guard, it should key on the element rather than
the name. That needs `atom_element` carried through the synthetic rows built at
`features.py:1746-1766`, which currently construct the merged `AtomLayout` with only
`atom_name`, `chain_id` and `res_id`; the elements are available from
`ccd_cif['_chem_comp_atom.type_symbol']` at that point. I am happy to send that version
instead if you prefer it.

### Testing

Ran the reproduction above; with the filter removed both bonds survive. The preceding
`keep_mask` was checked to confirm no hydrogen bond can reach this point, so removing the
filter does not reintroduce hydrogen bonds. I have not run a full prediction — the model
parameters are not publicly redistributable.

---

_This patch and description were written with AI assistance (Claude Code), disclosed per
CONTRIBUTING.md. The code and the reproduction above were reviewed and executed by me; no
test output here is hallucinated._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
