**Branch:** `fix/cross-attention-key-mask` ·
[open this PR](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/cross-attention-key-mask?expand=1)

**Title:** Add the query and key masks in cross_attention instead of multiplying them

---

### What is wrong

`cross_attention` builds its attention bias by **multiplying** the two mask terms
(`src/alphafold3/model/network/diffusion_transformer.py:287-292`):

```python
  # bias: ... x heads (1) x query x key
  bias = (
      1e9
      * (mask_q - 1.0)[..., None, :, None]
      * (mask_k - 1.0)[..., None, None, :]
  )
```

`(m - 1)` is `0` for a valid position and `-1` for a padded one, so the product is zero
whenever either side is valid:

| mask_q | mask_k | bias as written | intended |
|---|---|---|---|
| 1 | 1 | 0 | 0 (attend) |
| 1 | 0 | **0** | **-1e9 (mask)** |
| 0 | 1 | 0 | 0 (row zeroed later) |
| 0 | 0 | **+1e9** | -1e9 (mask) |

No key is ever masked for a valid query, and a fully padded pair receives a *positive*
1e9. `self_attention` in the same file (`:141`) builds its bias correctly, by adding:
`bias = (1e9 * (mask - 1.0))[..., None, None, :]`.

### Why it matters

Padded key slots carry zeroed keys and values, so they contribute no content — but they
still take softmax mass away from the real keys, and `pair_logits` on those slots is not
zero, so it steers that mass.

The window packing in `features.AtomCrossAtt.compute_features` shifts a key window back
inside the real-atom range only when there are at least 128 real heavy atoms; below that
the window runs off the end and carries padding. So this is latent for ordinary proteins
and **active for small inputs**: short peptides, a single small ligand, small nucleic-acid
fragments. The atom transformer runs in the diffusion encoder and decoder at every
denoising step, so it moves predicted coordinates.

This also departs from SI Algorithms 5, 6 and 24, where the softmax runs over the valid
keys of the subset.

### Reproduction

Softmax mass landing on padded keys, for a 5-residue peptide window (30 real atoms of 128
key slots):

```
shipped: softmax mass on PADDED keys, over valid queries:
        mean 0.755  min 0.643  max 0.850
fixed  : softmax mass on PADDED keys, over valid queries:
        mean 0.000  min 0.000  max 0.000

98 of 128 key slots in this window are padding, and none of them is masked.
```

Running the real module and comparing against physically deleting the padded keys — if the
mask worked, the two must be identical:

```
--- shipped (main @ c0f97ed) ---
|out| mean     : 0.007221
max |diff| vs dropping the padded keys entirely: 1.883e-02
padded keys are masked: False
--- patched ---
|out| mean     : 0.01029
max |diff| vs dropping the padded keys entirely: 0.000e+00
padded keys are masked: True
```

Scripts: `verify/c8_cross_attention_key_mask.py` and
`verify/c9_cross_attention_patch_check.py` in the linked audit repository. The module was
run verbatim with random parameters under a `tokamax` stub implementing the documented
kernel semantics, since the released weights are not publicly redistributable.

### The change

Add the two terms rather than multiplying them. The query term is redundant — padded query
rows are zeroed by `queries_act *= queries_mask[..., None]` afterwards — but keeping it
makes the intent explicit and matches the shape comment above the line.

### A caveat you should weigh

The released checkpoint was trained with this code. If the same masking was in place
during training, the weights are self-consistent with the current behaviour and this fix
will shift predictions for inputs under 128 heavy atoms. I have no way to check that from
outside, so please validate against the released weights before taking it. Either way the
computed attention is not the one the supplementary algorithms describe, so if the
behaviour is intended it is worth a comment on the line.

### Testing

Both reproductions above, on the shipped and patched trees. I have not run a full
prediction with released weights, for the reason given above.

---

_This patch and description were written with AI assistance (Claude Code), disclosed per
CONTRIBUTING.md. The code and the reproductions above were reviewed and executed by me; no
test output here is hallucinated._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
