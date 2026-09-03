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

Because the loader is memoised, every `Ccd` built from the same pickle path receives *the
same dict object*, and `update` mutates it in place. The class docstring states the
opposite intent — "Wraps the dict to prevent accidental mutation" — and `__hash__` returns
`id(self)` with the comment "Ok since this is immutable."

### Why it matters

`run_alphafold.py:1067` loops over every fold input in one process, and `predict_structure`
(`run_alphafold.py:585`) builds a fresh `Ccd(user_ccd=fold_input.user_ccd)` per input. So
with `--input_dir`:

- a `userCCD` supplied by one input stays visible to every later input in the run, and
- an entry that deliberately overrides a standard CCD code — a documented use of `userCCD`
  — keeps overriding it for later inputs that supply no `userCCD` at all.

`scoring/chirality.py:129` and `structure/mmcif.py:177`, which construct a default `Ccd()`,
see the injected entries too.

The failure is silent and order-dependent. A changed CCD entry changes which atoms exist
for that component, and therefore `make_flat_atom_layout`, the token count for the residue,
the tokenizer's per-token atom slots and canonical order, `get_reference`
(`ref_pos` / `ref_element` / `ref_charge` / `ref_atom_name_chars`) and the intra-ligand bond
graph. The second job simply models a different molecule, with no warning, and the result
depends on the order the inputs happen to be processed in.

### Where it came from

This looks like an unintended consequence of the fix for #509 (RAM OOM with per-input
`userCCD`s). PR #514 proposed solving it with a `collections.ChainMap` overlay onto a
shared cached base; that was closed in favour of a8ecdb2 ("Cache the underlying CCD
dictionary instead of the whole CCD object"), which caches the dict but keeps the in-place
`update`. Before a8ecdb2 each `__init__` unpickled its own copy, so `update` was
per-instance and correct. A `ChainMap` never writes to its base, which is why the #514
shape would not have had this effect.

### Reproduction

The constructor reproduced verbatim, stubbing only the pickle loader and the CIF parser —
neither takes part in the aliasing. Job 2 is constructed with **no** `user_ccd`:

```
--- shipped (main @ c0f97eda) ---
job1  len=3  LIG=['USER LIG']  ALA=['USER ALA']
job2  len=3  LIG in job2: True
job2  ALA=['USER ALA']   (should be ['real ALA'])
job3  len=4  sees job1 LIG: True
LEAK ACROSS INPUTS: True
job1/job2 share one dict object: True

--- patched (fix/ccd-user-ccd-copy) ---
job1  len=3  LIG=['USER LIG']  ALA=['USER ALA']
job2  len=2  LIG in job2: False
job2  ALA=['real ALA']   (should be ['real ALA'])
job3  len=3  sees job1 LIG: False
LEAK ACROSS INPUTS: False
job1/job2 share one dict object: False

shipped leaks: True   patched leaks: False
```

Script: `verify/c1_ccd_shared_mutation.py` in the linked audit repository; it runs both
forms in one pass and asserts the leak exists before the change and not after.

### The change

Overlay onto a copy instead of mutating the shared object. Only the top-level dict is
duplicated — the component values are still shared by reference — so the memory win of
a8ecdb2 is preserved and the OOM in #509 does not come back.

If you would rather have zero copying at all, `ChainMap(user_ccd_cifs, shared_dict)` gives
the same correctness with no duplicate top-level dict, which is what #514 proposed. It
needs a little care because `Ccd` implements `Mapping` by delegating to `self._dict`, and
`len()` over a `ChainMap` de-duplicates keys across the maps rather than summing them. I am
happy to send that version instead if you prefer it.

### Testing

The reproduction above, run against both the shipped and the patched constructor in a
single script, with the assertion shown. I have **not** run a full prediction: the model
parameters are not publicly redistributable, so I cannot fold an input end to end. The
change is confined to how the CCD dictionary is assembled, and no existing behaviour
changes for a single input or for an input with no `userCCD`. If you would like a specific
input folded to confirm, say which and I will arrange it.

---

_This patch and description were written with AI assistance (Claude Code), disclosed per
CONTRIBUTING.md. I reviewed the diff and executed the reproduction above; every line of
output quoted here is real program output, not hallucinated._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
