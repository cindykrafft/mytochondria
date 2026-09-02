"""C8: the cross_attention key mask is a no-op; padded keys keep softmax mass.

model/network/diffusion_transformer.py:287-292 builds the attention bias by
MULTIPLYING the two mask terms:

    bias = (
        1e9
        * (mask_q - 1.0)[..., None, :, None]
        * (mask_k - 1.0)[..., None, None, :]
    )

(m - 1) is 0 for a valid position and -1 for a padded one, so the product is 0
whenever either side is valid. A valid query therefore gets bias 0 on every key,
padded ones included, and a fully padded pair gets +1e9 rather than -1e9. The
sibling self_attention in the same file (line 141) does it correctly, by adding:

    bias = (1e9 * (mask - 1.0))[..., None, None, :]

Padded key slots carry zeroed keys and values, but they still take softmax mass
away from the real keys, and the pair bias on those slots is not zero, so it
steers that mass. This fires wherever a 128-key window contains padded slots,
which happens when an input has fewer than 128 real heavy atoms (small peptides,
single small ligands, nucleic-acid fragments).

Needs numpy only. Usage: python c8_cross_attention_key_mask.py
"""
import numpy as np

rng = np.random.default_rng(0)


def bias_shipped(mask_q, mask_k):
    return (1e9
            * (mask_q - 1.0)[..., None, :, None]
            * (mask_k - 1.0)[..., None, None, :])


def bias_fixed(mask_q, mask_k):
    return (1e9 * (mask_k - 1.0))[..., None, None, :]


print('truth table for one query/key pair (bias that reaches the softmax):')
print('%-22s %-14s %s' % ('', 'shipped', 'correct'))
for q, k, want in ((1., 1., '0 (attend)'), (1., 0., '-1e9 (mask)'),
                   (0., 1., "0 (row zeroed later)"), (0., 0., '-1e9 (mask)')):
    mq, mk = np.array([q]), np.array([k])
    print('mask_q=%.0f mask_k=%.0f      %-14.3g %s'
          % (q, k, bias_shipped(mq, mk)[0, 0, 0], want))

# A 5-residue peptide: one 128-key window, 30 real atoms.
n_q, n_k, n_real = 32, 128, 30
mask_q = np.zeros(n_q); mask_q[:n_real] = 1.0
mask_k = np.zeros(n_k); mask_k[:n_real] = 1.0
logits = rng.normal(size=(1, n_q, n_k)).astype(np.float64)

for name, bias in (('shipped', bias_shipped(mask_q, mask_k)),
                   ('fixed  ', bias_fixed(mask_q, mask_k))):
    z = logits + bias
    z = z - z.max(axis=-1, keepdims=True)
    p = np.exp(z)
    p /= p.sum(axis=-1, keepdims=True)
    leaked = p[0, mask_q == 1][:, mask_k == 0].sum(axis=-1)
    print('\n%s: softmax mass on PADDED keys, over valid queries:' % name)
    print('        mean %.3f  min %.3f  max %.3f'
          % (leaked.mean(), leaked.min(), leaked.max()))

print('\n%d of %d key slots in this window are padding, and none of them is masked.'
      % (n_k - n_real, n_k))
