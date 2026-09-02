"""C10: DNA rows of RESTYPE_RIGIDGROUP_DENSE_ATOM_IDX select the base N, not C1'.

model/protein_data_processing.py resolves the backbone-frame atoms C1'/C3'/C4'
once against RNA adenosine and writes those indices for all eight nucleic
residue types. DNA rows of DENSE_ATOM carry no O2', so every atom from C1'
onwards sits one slot earlier and the DNA rows select the base nitrogen:

    DA, DG -> N9, C3', C4'      DC, DT -> N1, C3', C4'

The sibling _make_restype_pseudobeta_idx already resolves per residue type.
Latent today: the table's only consumer is indexed by template aatype, and
template features currently carry protein aatypes only.

Usage:
  AF3=/path/to/alphafold3 python c10_nucleic_backbone_frame_idx.py
"""
import os, sys

AF3 = os.environ.get('AF3', '')
if not AF3:
    sys.exit('set AF3=/path/to/alphafold3 clone')
sys.path.insert(0, os.path.join(AF3, 'src'))
from alphafold3.constants import atom_types, residue_names

path = os.path.join(AF3, 'src/alphafold3/model/protein_data_processing.py')
ns = {}
exec(compile(open(path).read(), path, 'exec'), ns)   # noqa: S102
table = ns['RESTYPE_RIGIDGROUP_DENSE_ATOM_IDX']
offset = ns['NUM_AA_WITH_UNK_AND_GAP']

wrong = 0
for i, resname in enumerate(residue_names.NUCLEIC_TYPES):
    idx = [int(j) for j in table[i + offset, 0, :]]
    names = [atom_types.DENSE_ATOM[resname][j] for j in idx]
    ok = names == ["C1'", "C3'", "C4'"]
    wrong += not ok
    print('  %-3s idx=%-12s -> %-22s %s'
          % (resname, idx, names, 'ok' if ok else '<-- selects the base nitrogen'))
print('\nnucleic residue types with a wrong backbone frame: %d of %d'
      % (wrong, len(residue_names.NUCLEIC_TYPES)))
