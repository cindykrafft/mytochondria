"""C3: selenocysteine (SEC) is remapped to alanine, not cysteine.

Imports the real, pure-Python src/alphafold3/constants/residue_names.py and
follows the same two hops that structure.fix_non_standard_polymer_residues and
mmcif_names.py:207 take: CCD code -> one letter (CCD_NAME_TO_ONE_LETTER) ->
standard three-letter (PROTEIN_COMMON_ONE_TO_THREE). Also cross-checks against
gemmi's CCD-derived residue table when gemmi is installed.

Usage:
  AF3=/path/to/alphafold3 python c3_selenocysteine_mapping.py
"""
import os, sys
from collections import Counter

AF3 = os.environ.get('AF3', '')
if not AF3:
    sys.exit('set AF3=/path/to/alphafold3 clone')
sys.path.insert(0, os.path.join(AF3, 'src'))
from alphafold3.constants import residue_names as rn

one = rn.CCD_NAME_TO_ONE_LETTER
three = rn.PROTEIN_COMMON_ONE_TO_THREE

print('CCD_NAME_TO_ONE_LETTER entries:', len(one))
print()
print('%-5s %-8s %-8s %s' % ('code', 'letter', 'becomes', 'name'))
for code, name in [('SEC', 'selenocysteine'), ('CYS', 'cysteine'),
                   ('MSE', 'selenomethionine'), ('MET', 'methionine'),
                   ('CSO', 's-hydroxycysteine'), ('SEP', 'phosphoserine')]:
    letter = one.get(code)
    print('%-5s %-8s %-8s %s' % (code, letter, three.get(letter, 'UNK'), name))

fam = {k: v for k, v in one.items() if k.startswith(('CS', 'CY', 'SC'))}
print('\ncysteine-family codes (CS*/CY*/SC*): %d, mapping to %s'
      % (len(fam), dict(Counter(fam.values()).most_common())))
print('SE* codes:', {k: one[k] for k in sorted(one) if k.startswith('SE')})

print('\nselenomethionine is the precedent in the same table:'
      '  MSE -> %s -> %s' % (one['MSE'], three[one['MSE']]))
print('selenocysteine instead loses its chalcogen:      '
      '  SEC -> %s -> %s   (expected C -> CYS)' % (one['SEC'], three[one['SEC']]))

try:
    import gemmi
    print('\ngemmi %s CCD-derived table:' % gemmi.__version__)
    for code in ('SEC', 'CYS', 'MSE'):
        r = gemmi.find_tabulated_residue(code)
        print('  %-4s one_letter=%r is_standard=%s kind=%s'
              % (code, r.one_letter_code, r.is_standard(), r.kind))
except ImportError:
    print('\n(gemmi not installed; skipping the external cross-check)')
