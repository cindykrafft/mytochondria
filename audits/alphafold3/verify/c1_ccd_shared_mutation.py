"""C1: Ccd(user_ccd=...) mutates the process-global cached CCD dict.

Reproduces src/alphafold3/constants/chemical_components.py:29-82 verbatim,
stubbing only the pickle loader and the CIF parser (both come from the compiled
extension, and neither participates in the aliasing under test).
"""
import functools, os

REAL_CCD = {'ALA': {'_chem_comp.id': ['ALA'], 'note': ['real ALA']},
            'CYS': {'_chem_comp.id': ['CYS'], 'note': ['real CYS']}}


def _load_pickle(path):          # stands in for safe_pickle.load(open(path,'rb'))
    return dict(REAL_CCD)


def parse_multi_data_cif(user_ccd):   # stands in for cif_dict.parse_multi_data_cif
    return {k: {'note': ['USER ' + k]} for k in user_ccd.split(',')}


@functools.cache                      # chemical_components.py:36
def _load_ccd_pickle_cached(path):
    return _load_pickle(path)


PATCHED = False   # flipped by main() to exercise both forms


class Ccd:
    __slots__ = ('_dict', '_ccd_pickle_path')

    def __init__(self, ccd_pickle_path=None, user_ccd=None):
        self._ccd_pickle_path = ccd_pickle_path or 'ccd.pickle'
        shared = _load_ccd_pickle_cached(self._ccd_pickle_path)       # line 73
        if PATCHED:
            # fix/ccd-user-ccd-copy: overlay onto a copy
            if user_ccd is not None:
                if not user_ccd:
                    raise ValueError('User CCD cannot be an empty string.')
                user_ccd_cifs = {k: v for k, v in parse_multi_data_cif(user_ccd).items()}
                self._dict = {**shared, **user_ccd_cifs}
            else:
                self._dict = shared
            return
        self._dict = shared
        if user_ccd is not None:
            if not user_ccd:
                raise ValueError('User CCD cannot be an empty string.')
            user_ccd_cifs = {k: v for k, v in parse_multi_data_cif(user_ccd).items()}
            self._dict.update(user_ccd_cifs)                          # line 82
    def __getitem__(self, k):
        return self._dict[k]
    def __contains__(self, k):
        return k in self._dict
    def __len__(self):
        return len(self._dict)


def scenario(label):
    _load_ccd_pickle_cached.cache_clear()
    print('--- %s ---' % label)
    job1 = Ccd(user_ccd='LIG,ALA')        # input 1 supplies a user CCD, overriding ALA
    print('job1  len=%d  LIG=%s  ALA=%s'
          % (len(job1), job1['LIG']['note'], job1['ALA']['note']))

    job2 = Ccd()                          # input 2 supplies NO user CCD at all
    print('job2  len=%d  LIG in job2: %s' % (len(job2), 'LIG' in job2))
    print('job2  ALA=%s   (should be %s)'
          % (job2['ALA']['note'], REAL_CCD['ALA']['note']))

    job3 = Ccd(user_ccd='OTH')            # input 3 supplies a different user CCD
    print('job3  len=%d  sees job1 LIG: %s' % (len(job3), 'LIG' in job3))

    leaked = ('LIG' in job2) or job2['ALA']['note'] != REAL_CCD['ALA']['note']
    print('LEAK ACROSS INPUTS:', leaked)
    print('job1/job2 share one dict object:', job1._dict is job2._dict)
    print()
    return leaked


shipped_leaks = scenario('shipped (main @ c0f97eda)')
PATCHED = True
patched_leaks = scenario('patched (fix/ccd-user-ccd-copy)')

print('shipped leaks: %s   patched leaks: %s' % (shipped_leaks, patched_leaks))
assert shipped_leaks and not patched_leaks, 'expected the leak only before the fix'
print('OK: the fix removes the leak and nothing else changes.')
