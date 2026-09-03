**Title:** Ending-node triangle attention uses the transposed pair bias relative to SI Algorithm 15

---

`src/alphafold3/model/network/modules.py:222-249`:

```python
    pair_mask = jnp.swapaxes(pair_mask, -1, -2)
    act = hm.LayerNorm(name='act_norm')(act)

    nonbatched_bias = hm.Linear(
        self.config.num_head, use_bias=False, name='pair_bias_projection'
    )(act)                                   # <- projected from the UN-swapped act
    nonbatched_bias = jnp.transpose(nonbatched_bias, [2, 0, 1])
    ...
    if self.transpose:
      act = jnp.swapaxes(act, -2, -3)        # <- act swapped only afterwards
```

For `transpose=True`, q/k/v come from `act^T` while the bias is projected from the
un-swapped `act`, giving `b_ik`. SI Algorithm 15 (TriangleAttentionEndingNode) specifies
`a_ijk = softmax_k(q_ij·k_kj/√c + b_ki)`, and AlphaFold 2's public `TriangleAttention`
performs the `per_column` swap **before** the LayerNorm and the `feat_2d_weights`
projection, which yields `b_ki`. The refactor that merged both orientations into a
`transpose` flag appears to have moved the projection above the swap.

Checked against two NumPy references sharing the module's parameters (N=9 real of 13
padded tokens, 4 heads, output magnitude ~0.21):

```
transpose=False (starting node, Alg.14): |code-paper_bias|=2.98e-07  |code-transposed_bias|=7.84e-01
transpose=True  (ending node,   Alg.15): |code-paper_bias|=8.43e-01  |code-transposed_bias|=2.38e-07
```

The starting node matches the published algorithm to float32 round-off. The ending node
matches the transposed variant exactly and differs from Algorithm 15 by roughly four times
the output magnitude.

**This is not a bug in released-weight predictions.** The checkpoint was trained with this
code, so its `pair_bias_projection` weights are consistent with the transposed convention
and predictions are unaffected. I am raising it because it silently breaks equivalence with
the published algorithm and with AlphaFold 2, which costs time for anyone
re-implementing, porting, or retraining from the supplementary information.

The resolution may well be a note in the SI rather than a code change — changing the code
would alter what the released weights expect. Happy to send either.

---

_Investigated with AI assistance (Claude Code), disclosed per CONTRIBUTING.md. The numbers
above are real program output from running the module verbatim with random parameters; the
released weights are not publicly redistributable, so no weighted comparison was possible._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
