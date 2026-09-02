# Network, diffusion sampler and geometry

Scope: `model/network/` (Evoformer, Pairformer, diffusion head and transformer, atom
cross-attention), `model/components/`, `model/jax/geometry/`, `model/model.py`,
`model/params.py`. Tree: `main` @ `c0f97eda`.

Model weights are not publicly redistributable and the compiled extension was not built
for this part of the review, so every number below comes from running the repository's
own modules verbatim with random parameters, under a `tokamax` stub implementing the
documented kernel semantics, and comparing against an independent transcription of the
published algorithm (Abramson et al. 2024, supplementary information).

---

## N1 — The cross-attention key mask is a no-op [verified]

`model/network/diffusion_transformer.py:287-292`:

```python
  # bias: ... x heads (1) x query x key
  bias = (
      1e9
      * (mask_q - 1.0)[..., None, :, None]
      * (mask_k - 1.0)[..., None, None, :]
  )
```

The two mask terms are **multiplied** where they should be added. `(m - 1)` is `0` for a
valid position and `-1` for a padded one, so the product is zero whenever either side is
valid:

```
truth table for one query/key pair (bias that reaches the softmax):
                       shipped        correct
mask_q=1 mask_k=1      0              0 (attend)
mask_q=1 mask_k=0      -0             -1e9 (mask)
mask_q=0 mask_k=1      -0             0 (row zeroed later)
mask_q=0 mask_k=0      1e+09          -1e9 (mask)
```

No key is ever masked for a valid query, and a fully padded pair gets a *positive* +1e9.
`self_attention` in the same file (`:141`) builds its bias correctly, by adding.

Padded key slots carry zeroed keys and values, so they contribute no content, but they
still take softmax mass away from the real keys, and `pair_logits` on those slots is not
zero, so it steers that mass. Measured on a 5-residue peptide window
([`../verify/c8_cross_attention_key_mask.py`](../verify/c8_cross_attention_key_mask.py)):

```
shipped: softmax mass on PADDED keys, over valid queries:
        mean 0.755  min 0.643  max 0.850
fixed  : softmax mass on PADDED keys, over valid queries:
        mean 0.000  min 0.000  max 0.000

98 of 128 key slots in this window are padding, and none of them is masked.
```

Running the real module and comparing against physically deleting the padded keys
([`../verify/c9_cross_attention_patch_check.py`](../verify/c9_cross_attention_patch_check.py)):

```
--- shipped (main @ c0f97ed) ---
|out| mean     : 0.007221
max |diff| vs dropping the padded keys entirely: 1.883e-02
padded keys are masked: False
--- patched ---
max |diff| vs dropping the padded keys entirely: 0.000e+00
padded keys are masked: True
```

**When it fires.** `features.AtomCrossAtt.compute_features` shifts a key window back
inside the real-atom range only when there are at least 128 real heavy atoms; below that
the window runs off the end and carries padding. So the defect is latent for ordinary
proteins and active for small inputs — short peptides, a single small ligand, small
nucleic-acid fragments. The atom transformer runs in the diffusion encoder *and* decoder
at every one of the denoising steps, so this moves predicted coordinates directly.

Violates SI Algorithms 5, 6 and 24, where the softmax runs over the valid keys of the
subset. Unchanged since the initial release.

## N2 — Ending-node triangle attention uses the transposed pair bias [verified]

`model/network/modules.py:222-249`. For `transpose=True`, q/k/v are taken from `act^T`
while `nonbatched_bias` is projected from the **un-swapped** `act`, because the swap
happens after the projection. AlphaFold 2's public `TriangleAttention` performs the
`per_column` swap before the LayerNorm and the bias projection.

Against two NumPy references sharing the module's parameters:

```
transpose=False (starting node, Alg.14): |code-paper_bias|=2.98e-07  |code-transposed_bias|=7.84e-01
transpose=True  (ending node,   Alg.15): |code-paper_bias|=8.43e-01  |code-transposed_bias|=2.38e-07
```

The starting node matches SI Algorithm 14 to float32 round-off; the ending node matches
the transposed variant exactly and differs from SI Algorithm 15 by roughly four times
the output magnitude.

**This is not a released-weights regression.** The checkpoint was trained with this code,
so its `pair_bias_projection` weights are consistent with the transposed convention and
predictions from the released weights are unaffected. It is reported because it silently
breaks equivalence with the published algorithm and with AlphaFold 2, which misleads
re-implementations, ports and any retraining. The right resolution may well be a note in
the supplementary information rather than a code change.

## N3 — `_MultiFileIO.seek(..., SEEK_END)` has the wrong sign [verified, latent]

`model/params.py:135-168` computes `pos = self._length - pos` where `io.RawIOBase`
requires `length + offset`. The common `seek(0, SEEK_END)` is accidentally correct, which
is why the class works today.

```
seek(0,SEEK_END): tell()= 20  correct=20
seek(-5,SEEK_END): tell()= 25  correct=15
seek(3,SEEK_END):  tell()= 17  correct=23
```

If such a seek lands past `_length`, the sub-file read returns zero bytes, `count` stays
0, `_abspos` never reaches `_length`, and `while mem:` never terminates — a hang rather
than an exception (a subsequent `read(5)` was killed at a 25 s timeout). Filed as latent
because the current load path could not be shown to issue a non-zero `SEEK_END` seek.

## N4 — `bias_init=1.0` is silently ignored on every gating projection [code-read]

`modules.py:125, 193, 310` and `diffusion_transformer.py:175, 326` all pass
`bias_init=1.0` to `hm.Linear`, whose `use_bias` defaults to `False` and which reads
`bias_init` only when it is `True`. No bias parameter is created. AlphaFold 2 created
exactly such a gating bias initialised to 1.0, so this reads as carried-over intent that
was dropped in the port.

At inference it is a no-op *provided* the checkpoint contains no
`.../gating_query/bias` entries; Haiku silently ignores extra parameters, so any that do
exist are being dropped. That could not be checked without the weights. For retraining,
gates initialise at `sigmoid(0) = 0.5` rather than `sigmoid(1) ≈ 0.73`.

## N5 — The parameter-file pattern for uncompressed shards has a stray `]` [verified]

`model/params.py:207`:

```python
      (r'(?P<model_name>.*)\.bin]\.[0-9]+$', False),
```

It is meant to be the uncompressed counterpart of `\.bin\.zst\.[0-9]+$`. The stray `]`
requires a literal `]` after `bin`:

```
['af3.bin']                       -> OK   compressed=False
['af3.bin.zst.0','af3.bin.zst.1'] -> OK   compressed=True
['af3.0.bin','af3.1.bin']         -> OK   compressed=False
['af3.bin.0','af3.bin.1']         -> FileNotFoundError: No models matched
['af3.bin].0','af3.bin].1']       -> OK   compressed=False   <- the typo's actual effect
```

Low severity: the shipped parameters are a single `.bin.zst`, and the alternative
`.N.bin` layout works. Found independently by two reviews. Present since `4f52a3b`.

---

## Excluded as already reported

The atom cross-attention encoder converts `batch.ref_structure.ref_space_uid` through
`queries_to_keys` although that array is in the token-atoms layout rather than the
queries layout, so `offsets_valid` compares a query atom's reference-space id against an
unrelated atom's, and the same-reference-space prior is largely destroyed (measured: for
a 60-residue chain, 16 of 3732 genuinely intra-residue atom pairs recovered). This
review reproduced it, and then found it is **open issue #730**, "Incorrect layout
conversion of `ref_space_uid` in atom cross-attention", which reports the same line and
proposes the same fix. It is therefore not claimed as a finding here. Worth adding to
that issue if the maintainers want it: the shape guard in `atom_layout.convert`
(`:955-961`) that would have caught the mismatch is disabled under `jit`, because its
`isinstance(gather_info.input_shape, np.ndarray)` clause is False once
`run_alphafold.py:495-500` has mapped the example through `jnp.asarray`. Called eagerly
the same conversion raises `ValueError: Input array layout axes are incompatible`.

---

## Exonerated

**Diffusion sampler.** `sample()` matches an independent transcription of SI Algorithm 18
to 1.55e-6 / 3.73e-7 / 2.29e-5 across three configurations, while two deliberately
introduced off-by-one variants are rejected by the same test (9.8e-2 and 5.9e+2). The
noise schedule has 201 levels for 200 steps, endpoints `2560.0` and `0.0064`, strictly
decreasing, and the scan consumes `noise_levels[1:]`, so there is no endpoint
off-by-one. EDM preconditioning satisfies `c_skip² + (c_out/σ_data)² = 1` and `c_noise`
matches the embedding. `random_rotation` is proper and Haar-isotropic over 400 draws.
`random_augmentation` preserves pairwise distances to 3.8e-6 and is invariant to a 100 Å
input shift. Per-sample RNG keys are split into the vmapped carry, giving samples that
are mutually distinct and reproducible per key.

**Trunk.** `TriangleMultiplication` matches SI Algorithms 12 and 13 to 7.2e-7 / 4.8e-7
once the interleaved channel pairing is accounted for. `GridSelfAttention(transpose=False)`
matches SI Algorithm 14 to 3.0e-7. Padding invariance holds bit-exactly (0.0) for
TriangleMultiplication both directions, GridSelfAttention both orientations, the full
PairFormer iteration, `OuterProductMean` and `MSAAttention`. The fused
`OuterProductMean` einsum from `7b4c2a5` equals the explicit masked mean to 1.3e-6 and
is chunk-size independent.

**Sharding.** `mapping.sharded_apply` equals the unsharded function with max-abs error
exactly 0 over 126 combinations of sequence length and shard size, including every
partial-remainder case. `inference_subbatch` is chunk-size invariant to 1.1e-5,
`sharded_map` agrees with `jax.vmap` to 9.5e-7.

**Geometry** (N=500 each). `Rot3Array` composition, inverse, `apply_to_point` and
`apply_inverse` all correct, with the reversed-order variant differing by 1.97;
`from_two_vectors` has the documented axis order and signs; `from_quaternion` matches the
Hamilton active-rotation convention to 6.0e-7; `from_svd` equals the Kabsch projection
with `det=+1`; `Rigid3Array` round-trips and composes correctly; `dihedral_angle` matches
the IUPAC reference.

**Heads and plumbing.** `DiffusionHead._conditioning` matches SI Algorithm 21, including
the asymmetry of passing raw `embeddings['single']` with conditioned `trunk_pair_cond`,
which SI Algorithm 20 line 3 specifies. Relative encoding matches SI Algorithm 3.
Recycling carries only `prev['pair']` and `prev['single']` and uses the final embeddings.
`hm.LayerNorm` upcasts before parameter creation. Both `use_glu_kernel` paths are
algebraically identical. No dropout anywhere in the inference path.

Examined and not filed: `Evoformer._embed_bonds` sets only one direction of the contact
matrix, which needs a featurisation-side check of whether `bond_layout` already carries
both orientations; a `(num_tokens, 24, 24, 16)` pair tensor in `_per_atom_conditioning`
that both call sites discard (dead, eliminated by XLA); an ignored `broadcast_dim`
parameter; `qkv_dim = max(num_channels // num_head, 16)`, which never triggers with
shipped configs; and the `+1e9` bias on fully padded pairs from N1, which produces no
NaN because the softmax subtracts the row max.
