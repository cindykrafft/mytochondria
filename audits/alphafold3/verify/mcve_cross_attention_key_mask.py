"""AF3: diffusion_transformer.cross_attention never masks padded keys.

Usage: python mcve_cross_attention_key_mask.py <alphafold3 checkout>/src

Calls the real cross_attention() from the given checkout (Haiku, random
parameters; the released weights are not used) on one atom-attention window: 32 queries, 128 key slots of
which only the first 30 are real atoms, as for a 5-residue peptide (30 heavy atoms;
AtomCrossAtt.compute_features can shift a 128-key window back inside the real atoms
only when there are at least 128 of them). AlphaFold 3's compiled modules are
stubbed: nothing in them is called.
"""
import sys
import types


class Stub(types.ModuleType):
  __path__ = []

  def __getattr__(self, name):
    if name.startswith('__'):
      raise AttributeError(name)
    return type(name, (), {})


for _m in ['alphafold3.cpp', 'alphafold3.cpp.cif_dict', 'alphafold3.structure',
           'alphafold3.structure.mmcif', 'alphafold3.constants.chemical_components',
           'alphafold3.constants.chemical_component_sets',
           'alphafold3.model.atom_layout', 'alphafold3.model.atom_layout.atom_layout']:
  sys.modules[_m] = Stub(_m)
sys.modules['alphafold3.structure'].mmcif = sys.modules['alphafold3.structure.mmcif']
sys.modules['alphafold3.model.atom_layout'].atom_layout = sys.modules['alphafold3.model.atom_layout.atom_layout']
sys.path.insert(0, sys.argv[1])

import haiku as hk  # noqa: E402
import jax  # noqa: E402
import jax.numpy as jnp  # noqa: E402
import numpy as np  # noqa: E402
from alphafold3.model import model_config  # noqa: E402
from alphafold3.model.network import diffusion_transformer as dt  # noqa: E402

Q, K, REAL, C = 32, 128, 30, 128
captured = []
_softmax = jax.nn.softmax


def recording_softmax(x, axis=-1):
  w = _softmax(x, axis=axis)
  captured.append(w)
  return w


dt.jax.nn.softmax = recording_softmax  # dt calls jax.nn.softmax


def f(x_q, x_k, mask_q, mask_k, pair_logits):
  return dt.cross_attention(
      x_q, x_k, mask_q, mask_k,
      config=dt.CrossAttentionConfig(),
      global_config=model_config.GlobalConfig(),
      pair_logits=pair_logits,
      name='x')


fn = hk.transform(f)
rng = np.random.default_rng(0)
x_q = jnp.asarray(rng.normal(size=(1, Q, C)), jnp.float32)
x_k = jnp.asarray(rng.normal(size=(1, K, C)), jnp.float32)
# Padded key slots carry zeros, as gathered padding does.
x_k = x_k.at[:, REAL:].set(0.0)
mask_q = jnp.ones((1, Q), jnp.float32)
mask_k = jnp.asarray(np.r_[np.ones(REAL), np.zeros(K - REAL)][None], jnp.float32)
num_head = dt.CrossAttentionConfig().num_head
pair = jnp.asarray(rng.normal(size=(1, num_head, Q, K)), jnp.float32)
pair = pair.at[..., REAL:].set(0.0)
params = fn.init(jax.random.PRNGKey(0), x_q, x_k, mask_q, mask_k, pair)
# The output projections are zero-initialised, which would make every output 0;
# draw all parameters at random instead (scale 0.05), so the output check is live.
leaves, tree = jax.tree_util.tree_flatten(params)
params = jax.tree_util.tree_unflatten(tree, [
    jnp.asarray(rng.normal(scale=0.05, size=l.shape), l.dtype) for l in leaves])

captured.clear()
out1 = fn.apply(params, None, x_q, x_k, mask_q, mask_k, pair)
w = np.asarray(captured[-1])  # (1, heads, Q, K)
mass = w[..., REAL:].sum(-1)
print(f'{K - REAL} of {K} key slots padded (zero features, zero pair logits); softmax mass on padded keys per valid '
      f'query: mean {mass.mean():.3f}, max {mass.max():.3f}')

# Change only what sits in the padded key slots: features and pair logits.
x_k2 = x_k.at[:, REAL:].set(jnp.asarray(rng.normal(size=(1, K - REAL, C)), jnp.float32))
pair2 = pair.at[..., REAL:].set(jnp.asarray(rng.normal(size=(1, num_head, Q, K - REAL)), jnp.float32))
out2 = fn.apply(params, None, x_q, x_k2, mask_q, mask_k, pair2)
print(f'max change in the valid queries\' output when only padded keys change: '
      f'{float(jnp.abs(out2 - out1).max()):.3g}')
