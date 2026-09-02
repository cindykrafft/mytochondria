"""C7: AlignmentError escapes Hit.keep() instead of dropping the hit.

data/templates.py wraps the align_ratio check in try/except AlignmentError so a
hit that cannot be realigned is skipped with a warning. The is_valid check one
statement ABOVE it sits outside that try, and is_valid is what actually triggers
the realignment (it reads query_to_hit_mapping, whose cached property calls
template_realign.realign_hit_to_structure). So for a realign failure the handler
can never fire: the exception escapes keep(), propagates through _filter_hits,
and aborts template featurisation for the whole input.

Loads the REAL templates.py from the tree under test, stubbing the modules it
imports that need the compiled extension.

Usage:
  AF3=/path/to/alphafold3 python c7_template_hit_keep_alignment_error.py
"""
import os, sys, types

AF3 = os.environ.get('AF3', '')
if not AF3:
    sys.exit('set AF3=/path/to/alphafold3 clone')
SRC = os.path.join(AF3, 'src')
sys.path.insert(0, SRC)


def stub(name, **attrs):
    m = types.ModuleType(name)
    m.__path__ = []
    for k, v in attrs.items():
        setattr(m, k, v)
    sys.modules[name] = m
    return m


stub('alphafold3.cpp')
stub('alphafold3.structure', Structure=object, from_mmcif=lambda *a, **k: None)
stub('alphafold3.data.structure_stores', StructureStore=object,
     NotFoundError=type('NotFoundError', (Exception,), {}))
stub('alphafold3.data.tools.hmmsearch', Hmmsearch=object)
import alphafold3  # noqa: F401

from alphafold3.data import templates  # the real module, from the tree under test

# A hit whose mmCIF structure sequence is LONGER than the seqres length, which
# is what makes realign_hit_to_structure raise.
hit = templates.Hit(
    pdb_id='xxxx',
    auth_chain_id='A',
    hmmsearch_sequence='DEFG',
    structure_sequence='XDEFGY',
    query_sequence='DEFG',
    start_index=0,
    end_index=4,
    full_length=4,
    release_date=None,
    chain_poly_type='polypeptide(L)',
    unresolved_res_indices=None,
)

print('hit: seqres length %d, structure sequence %r (length %d)'
      % (hit.full_length, hit.structure_sequence, len(hit.structure_sequence)))
try:
    kept = hit.keep(release_date_cutoff=None, max_subsequence_ratio=None,
                    min_align_ratio=0.1, min_hit_length=None)
    print('keep() returned %r  -> the hit is dropped gracefully, as intended' % kept)
except Exception as e:  # noqa: BLE001
    print('keep() raised %s: %s' % (type(e).__name__, str(e).splitlines()[0]))
    print('-> the exception escapes keep(), so _filter_hits aborts the whole input')
