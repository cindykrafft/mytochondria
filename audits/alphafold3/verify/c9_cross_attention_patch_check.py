"""C9: does cross_attention actually mask padded keys?

Runs the real diffusion_transformer.cross_attention from the tree under test and
compares its output against the same call with the padded key slots physically
removed. Equal output means the mask works.

    shipped  max |diff| 1.883e-02 against |out| mean 7.2e-03  -> not masked
    patched  max |diff| 0.000e+00                             -> masked

Needs jax, haiku and the stub tree from agents/network/ (the compiled extension
is not required). Usage:

    TREE=shipped python c9_cross_attention_patch_check.py
    TREE=patched python c9_cross_attention_patch_check.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if os.environ.get('TREE') == 'patched':
    import harness_common_patched  # noqa: F401
else:
    import harness_common  # noqa: F401

import numpy as np, jax, jax.numpy as jnp, haiku as hk
from alphafold3.model import model_config
from alphafold3.model.network import diffusion_transformer as dt

gc = model_config.GlobalConfig(bfloat16='none', final_init='linear',
                               flash_attention_implementation='xla')
cfg = dt.CrossAttentionConfig(num_head=4, key_dim=128, value_dim=128)
S, Q, K, C, NM = 2, 8, 12, 32, 4
ks = jax.random.split(jax.random.PRNGKey(0), 8)
x_q = jax.random.normal(ks[0], (S, Q, C)); x_k = jax.random.normal(ks[1], (S, K, C))
cq = jax.random.normal(ks[2], (S, Q, C)); ck = jax.random.normal(ks[3], (S, K, C))
pair_logits = jax.random.normal(ks[4], (S, cfg.num_head, Q, K))
mask_q = jnp.ones((S, Q))
mask_k = jnp.array(np.r_[np.ones(K - NM), np.zeros(NM)])[None].repeat(S, 0)
# Padded key slots carry zeroed content, as atom_layout.convert produces.
x_k = x_k * mask_k[..., None]; ck = ck * mask_k[..., None]


def run(xk, ck_, mk, pl):
    def f():
        return dt.cross_attention(x_q, xk, mask_q, mk, cfg, gc,
                                  pair_logits=pl, single_cond_q=cq,
                                  single_cond_k=ck_)
    t = hk.transform(f)
    p = t.init(ks[5])
    return t.apply(p, ks[6])


full = run(x_k, ck, mask_k, pair_logits)
kept = slice(0, K - NM)
dropped = run(x_k[:, kept], ck[:, kept], mask_k[:, kept], pair_logits[..., kept])
d = float(jnp.abs(full - dropped).max())
print('tree           :', os.environ.get('TREE', 'shipped'))
print('|out| mean     : %.4g' % float(jnp.abs(full).mean()))
print('max |diff| vs dropping the padded keys entirely: %.3e' % d)
print('padded keys are masked:', d < 1e-6)
