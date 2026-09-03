# Submitting these upstream

All 14 branches are pushed to **[cindykrafft/alphafold3](https://github.com/cindykrafft/alphafold3)**,
each one commit on `c0f97eda`, each independent of the others. Ready-to-paste PR
descriptions are in [`pr-bodies/`](pr-bodies/) and issue bodies in
[`issue-bodies/`](issue-bodies/).

## Before you open anything

Three things `CONTRIBUTING.md` asks for, two of which only you can do:

1. **Sign the Google CLA** at <https://cla.developers.google.com/>. Contributions cannot be
   merged without it, and you only need to do it once across all Google projects.
2. **Manually review each diff.** The guidelines are explicit that AI-assisted PRs must be
   reviewed by the submitter. Each diff is between 1 and 20 lines; the PR bodies quote the
   exact code being changed.
3. **AI assistance is disclosed** in every prepared body, as the guidelines require. Note
   also the line *"Please do not submit AI generated PRs where test results have been
   hallucinated"* — every number in these bodies is real output from a script in
   [`../verify/`](../verify/), and each body states plainly what was **not** tested: no
   prediction was run against released weights, because they are not publicly
   redistributable. If a maintainer asks you to fold a specific input to check a change,
   that is the gap they will be probing.

## Suggested pacing

Fourteen pull requests in one day from one contributor is a lot of review load, and the
first three are the ones that would change someone's results. I would send them in waves
and let the response to the first shape the rest.

**Wave 1 — the ones that matter.** One at a time, or all three together.

| | branch | body |
|---|---|---|
| 1 | `fix/ccd-user-ccd-copy` | [`pr-bodies/01`](pr-bodies/01-ccd-user-ccd-copy.md) |
| 2 | `fix/ligand-bond-hydrogen-filter` | [`pr-bodies/02`](pr-bodies/02-ligand-bond-hydrogen-filter.md) |
| 3 | `fix/cross-attention-key-mask` | [`pr-bodies/03`](pr-bodies/03-cross-attention-key-mask.md) |

Wave 1 note: #1 is a regression from the fix for issue #509, so it is worth linking that
issue in the PR. #3 carries a genuine caveat about released weights that the body states
up front — expect that to be the discussion.

**Wave 2 — solid, lower blast radius.**
`fix/msa-pairing-stable-sort` ([04](pr-bodies/04-msa-pairing-stable-sort.md)),
`fix/mse-residue-key-lookup` ([05](pr-bodies/05-mse-residue-key-lookup.md)),
`fix/summary-confidences-chain-ids` ([06](pr-bodies/06-summary-confidences-chain-ids.md)),
`fix/per-chain-template-cache-key`, `fix/to-json-preserves-chain-order`,
`fix/template-hit-keep-alignment-error`
(bodies 07-09 in [`pr-bodies/07-14-remaining.md`](pr-bodies/07-14-remaining.md)).

**Wave 3 — small and uncontroversial.** The docs fix, `ref-max-modified-date-none`,
`arginine-hh22-rename`, `nucleic-rigidgroup-dense-atom-idx`, `params-bin-shard-regex`
(bodies 10-14, same file). The docs one is the easiest possible first merge if you would
rather open with something trivial.

**Issues, after the PRs.** [`issue-bodies/A`](issue-bodies/A-selenocysteine-maps-to-alanine.md)
(selenocysteine) and [`B`](issue-bodies/B-triangle-attention-transposed-bias.md)
(triangle-attention bias) are the two worth their own threads;
[`C`](issue-bodies/C-smaller-findings.md) collects six smaller ones.

## Opening a PR

Each body starts with a compare link that opens GitHub's PR form with the branch
pre-selected, for example:

```
https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/ccd-user-ccd-copy?expand=1
```

Paste the title and body from the corresponding file. Base is `main`.

## Do not claim these two

Both were reproduced during the audit and both are already reported upstream. Filing them
again would be noise:

- `ref_space_uid` converted through the wrong atom layout in atom cross-attention —
  **open issue #730**. If you want to add value there, the useful new detail is that the
  shape guard in `atom_layout.convert` (`:955-961`) which would have caught it is disabled
  under `jit`, because its `isinstance(gather_info.input_shape, np.ndarray)` clause is
  False once `run_alphafold.py:495-500` has mapped the example through `jnp.asarray`.
  Called eagerly the same conversion raises
  `ValueError: Input array layout axes are incompatible`.
- float32 overflow in the paired-MSA rank metric — **open PR #719**, **open issue #236**.
