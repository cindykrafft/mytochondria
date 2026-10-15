Title: `cross_attention` multiplies the query and key mask terms, so padded keys are never masked (inputs with fewer than 128 atoms)

<!-- AF3. Re-verified 2026-10-15 on main 045ffa4 by execution: ../verify/mcve_cross_attention_key_mask.py, output in
     ../verify/mcve_cross_attention_key_mask.out. Duplicate check 2026-10-15: no issue or PR on the attention mask; the open
     atom cross-attention PRs #733/#740 are about the ref_space_uid layout conversion. Issue only: the fix branch
     fix/cross-attention-key-mask (a1544f5, applies on main) is offered, not opened, because it changes model behaviour. -->

In `src/alphafold3/model/network/diffusion_transformer.py`, `cross_attention` builds its mask bias as a product:

```python
bias = (
    1e9
    * (mask_q - 1.0)[..., None, :, None]
    * (mask_k - 1.0)[..., None, None, :]
)
```

`mask - 1` is 0 for a valid position and -1 for a padded one, so the product is 0 whenever either side is valid. A valid query therefore gets bias 0 on every key, padded keys included, and only fully padded (query, key) pairs get a non-zero entry (+1e9). `self_attention` in the same file adds its mask term (`1e9 * (mask - 1.0)` over the keys), which is what the shape comment `# bias: ... x heads (1) x query x key` suggests was intended here too.

**When it matters.** `AtomCrossAtt.compute_features` gives each block of 32 queries a 128-atom key window and shifts the windows back inside the real atoms. A window only fits when the input has at least 128 atoms in total, so for larger inputs every key is real and the bias makes no difference. For inputs with fewer than 128 atoms some key slots are padding, and the atom transformer attends to them in the diffusion encoder and decoder at every denoising step. Examples are a short peptide, a small ligand or a short nucleic-acid fragment on its own. A 5-residue peptide has 30 atoms, so 98 of its 128 key slots are padding.

**Reproduction.** The script calls the real `cross_attention` from `main` (045ffa4) under Haiku with random parameters. The released weights are not used, and AlphaFold 3's compiled modules are stubbed since nothing in them is called. The window has 32 valid queries and 128 key slots, of which the first 30 are real and the padded slots hold zero features and zero pair logits:

```
main 045ffa4:
98 of 128 key slots padded (zero features, zero pair logits); softmax mass on padded keys per valid query: mean 0.666, max 0.777
max change in the valid queries' output when only padded keys change: 0.00366
main 045ffa4 with the two mask terms added instead of multiplied:
98 of 128 key slots padded (zero features, zero pair logits); softmax mass on padded keys per valid query: mean 0.000, max 0.000
max change in the valid queries' output when only padded keys change: 0
```

So on `main` the padded slots take most of the attention of every valid query in such a window, and what is stored in them reaches the output. With trained weights the share depends on the learned logits, which I have not measured.

**Fix.** Add the two terms:

```python
bias = (1e9 * (mask_q - 1.0))[..., None, :, None] + (
    1e9 * (mask_k - 1.0)
)[..., None, None, :]
```

Only the key term matters for the result. The query term adds the same constant to every logit in a padded query's row, which leaves its softmax unchanged; it is kept to match the shape comment.

I am filing this as an issue rather than a PR because the released weights were trained with the current code path, so a fix may move predictions for small inputs in either direction. Whether to change it, or only to document it, is your call. A branch with the change is at https://github.com/cindykrafft/alphafold3/tree/fix/cross-attention-key-mask and I can open it as a PR if you want it. The reproduction script is at https://github.com/cindykrafft/mytochondria/blob/main/audits/alphafold3/verify/mcve_cross_attention_key_mask.py.

**AI generation.** The analysis, the script and this text were produced with Claude Code; I have read the code path and run the script myself.
