"""C4: the "remove bonds to Hydrogen" filter deletes bonds to mercury.

model/features.py:1295-1300 filters ligand-ligand bonds by ATOM NAME prefix:

    # Remove any bonds to Hydrogen atoms.
    bond_layout = bond_layout[
        ~np.char.startswith(bond_layout.atom_name.astype(str), 'H').any(axis=1)
    ]

Atom names in AlphaFold 3 are the uppercased element symbol plus a counter
(data/tools/rdkit_utils.py:520-525, "'Cl' becomes 'CL'"), so mercury is named
HG1, hafnium HF1, holmium HO1. Their bonds start with 'H' and are dropped.

The filter is also redundant for its stated purpose: the preceding keep_mask
(features.py:1271-1294) keeps only bonds whose two endpoints appear in the flat
atom layout, and that layout drops hydrogens BY ELEMENT
(atom_layout.py:845-848: `e != 'H' and e != 'D'`), so no hydrogen bond can still
be present at this point.

Needs rdkit only. Usage: python c4_hydrogen_name_bond_filter.py
"""
import collections
import numpy as np
from rdkit import Chem

SMILES = 'C[Hg]Cl'   # methylmercury chloride motif


def af3_atom_names(mol):
    """The naming rule from rdkit_utils.assign_atom_names_from_graph."""
    counts = collections.Counter()
    names = []
    for atom in mol.GetAtoms():
        element = atom.GetSymbol().upper()      # 'Hg' -> 'HG', as in the CCD
        counts[element] += 1
        names.append(f'{element}{counts[element]}')
    return names


mol = Chem.AddHs(Chem.MolFromSmiles(SMILES))
names = af3_atom_names(mol)
elements = [a.GetSymbol() for a in mol.GetAtoms()]

print('ligand %s' % SMILES)
print('atoms          :', list(zip(names, elements)))

bonds = [(names[b.GetBeginAtomIdx()], names[b.GetEndAtomIdx()]) for b in mol.GetBonds()]
print('bonds from CCD :', bonds)

# 1. The flat atom layout drops hydrogens by element (atom_layout.py:845-848).
heavy = {n for n, e in zip(names, elements) if e not in ('H', 'D')}
print('\nflat layout atoms (hydrogens dropped by element):', sorted(heavy))

# 2. keep_mask: both endpoints must exist in the layout (features.py:1271-1294).
kept = [b for b in bonds if b[0] in heavy and b[1] in heavy]
print('after keep_mask:', kept, ' <- already contains no hydrogen bond')

# 3. The name-prefix filter, verbatim.
arr = np.array(kept)
survivors = arr[~np.char.startswith(arr.astype(str), 'H').any(axis=1)] if len(arr) else arr
print('after the startswith("H") filter:', [tuple(r) for r in survivors])

dropped = [b for b in kept if tuple(b) not in {tuple(r) for r in survivors}]
print('\ndropped by the H filter:', dropped)
print('the ligand reaches token_bonds with %d of its %d covalent bonds'
      % (len(survivors), len(kept)))
print('every bond dropped here joins a heavy atom, not a hydrogen:',
      all(all(e != 'H' for e in (elements[names.index(a)], elements[names.index(b)]))
          for a, b in dropped))
