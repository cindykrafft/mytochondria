**Branch:** `fix/ccd-user-ccd-copy` ·
[open this PR](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/ccd-user-ccd-copy?expand=1)

**Title:** Do not let a user CCD mutate the shared cached CCD dictionary

---

### What is wrong

`Ccd.__init__` overlays the user CCD onto the dictionary returned by
`_load_ccd_pickle_cached`, which is `@functools.cache`d on the pickle path
(`src/alphafold3/constants/chemical_components.py:73,82`):

```python
    self._dict = _load_ccd_pickle_cached(self._ccd_pickle_path)
    ...
      self._dict.update(user_ccd_cifs)
```

Every `Ccd` built from the default path therefore receives *the same dict object*, and
`update` mutates it in place. The class docstring states the opposite intent — "Wraps the
dict to prevent accidental mutation" — and `__hash__` returns `id(self)` with the comment
"Ok since this is immutable."

### Why it matters

`run_alphafold.py:1067` loops over every fold input in one process, and
`predict_structure` (`run_alphafold.py:585`) builds a fresh
`Ccd(user_ccd=fold_input.user_ccd)` per input. So with `--input_dir`, a `userCCD` from one
input stays visible to every later input, and an entry that deliberately overrides a
standard CCD code — a documented use of `userCCD` — keeps overriding it for inputs that
supply no `userCCD` at all. `scoring/chirality.py:129` and `structure/mmcif.py:177`, which
construct a default `Ccd`, see the injected entries too.

The consequence is silent and order-dependent. A corrupted CCD entry changes which atoms
exist for that component, hence `make_flat_atom_layout`, the token count for the residue,
the tokenizer's per-token atom slots and canonical order, `get_reference`
(`ref_pos`/`ref_element`/`ref_charge`/`ref_atom_name_chars`) and the intra-ligand bond
graph. The second job simply models a different molecule, with no warning.

This looks like an unintended consequence of `a8ecdb2` ("Cache the underlying CCD
dictionary instead of the whole CCD object"), which is the memory fix for #509. Before
that commit each `__init__` unpickled its own copy, so `update` was per-instance and
correct.

### Reproduction

Reproducing the constructor verbatim, stubbing only the pickle loader and the CIF parser
(neither takes part in the aliasing). Job 2 is constructed with **no** `user_ccd`:

```
job1  len=3  LIG=['USER LIG']  ALA=['USER ALA']
job2  len=3  LIG in job2: True
job2  ALA=['USER ALA']   (should be ['real ALA'])
job3  len=4  sees job1 LIG: True

LEAK ACROSS INPUTS: True
all three share one dict object: True
```

Script: `verify/c1_ccd_shared_mutation.py` in the linked audit repository.

### The change

Overlay onto a shallow copy instead of mutating the shared object. Only the top-level dict
is duplicated — the values are still shared by reference — so the memory win of `a8ecdb2`
is preserved.

### Testing

Ran the reproduction above against the patched constructor: `job2` sees neither `LIG` nor
the `ALA` override, and the instances no longer share a dict object. I have not run a full
prediction, since the model parameters are not publicly redistributable; the change is
confined to the CCD dictionary's construction.

---

_This patch and description were written with AI assistance (Claude Code), disclosed per
CONTRIBUTING.md. The code and the reproduction above were reviewed and executed by me; no
test output here is hallucinated._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
