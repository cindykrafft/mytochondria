# FieldTrip upstream filing kit

FieldTrip takes contributions as GitHub pull requests against `master` from a
fork (https://www.fieldtriptoolbox.org/development/git/); an issue first is
suggested for changes that need discussion, and branches may be named after
the issue. Recommended order:

1. **FT1 — permutation p-value ties** (`issue-ft1-pvalue-ties.md`, then
   `pr-ft1-pvalue-ties.md`). This changes reported p-values, so file the issue
   first and reference it from the PR. Patch:
   `0001-Count-ties-when-computing-Monte-Carlo-p-values-inste.patch`.
2. **FT11 — PSI edge bins** (`issue-ft11-psi-edge.md`, then
   `pr-ft11-psi-edge.md`). Patch: `0001-ft_connectivity_psi-exclude-...patch`.
3. **FT7 — correlationT df** (`pr-ft7-correlationT-df.md`, PR only).
4. **FTR — depsamplesregrT typo** (`pr-ftr-depsamplesregrT.md`, PR only).
5. **FT2 — two-sided warning** (`pr-ft2-twosided-warning.md`, PR only).

## Live branches on the fork (cindykrafft/fieldtrip, each one commit on master @ 2e14f72)

| finding | branch | head | compare page |
|---|---|---|---|
| FT1 | `fix/permutation-pvalue-ties` | 3713810 | https://github.com/fieldtrip/fieldtrip/compare/master...cindykrafft:fieldtrip:fix/permutation-pvalue-ties?expand=1 |
| FT11 | `fix/psi-edge-bin` | cf99d1d | https://github.com/fieldtrip/fieldtrip/compare/master...cindykrafft:fieldtrip:fix/psi-edge-bin?expand=1 |
| FT7 | `fix/correlationT-df` | a65f5a6 | https://github.com/fieldtrip/fieldtrip/compare/master...cindykrafft:fieldtrip:fix/correlationT-df?expand=1 |
| FTR | `fix/depsamplesregrT-cvar` | 684f26c | https://github.com/fieldtrip/fieldtrip/compare/master...cindykrafft:fieldtrip:fix/depsamplesregrT-cvar?expand=1 |
| FT2 | `fix/twosided-warning` | 656e974 | https://github.com/fieldtrip/fieldtrip/compare/master...cindykrafft:fieldtrip:fix/twosided-warning?expand=1 |

To push the branches from a fork of `fieldtrip/fieldtrip`:

```bash
git clone --depth 1 https://github.com/<you>/fieldtrip && cd fieldtrip
for p in ../0001-*.patch; do
  b=$(basename "$p" .patch | sed 's/^0001-//'); git checkout -b "fix/$b" master && git am "$p" && git checkout master
done
git push -u origin --all
```

(Each patch applies to master @ 2e14f72 independently.) The maintainers may
ask for a `test_issueNNNN.m`; the `../verify/` scripts contain the material.

Verification behind every filing is in `../verify/` and quoted in
`../component-reviews/statistics-core.md`; each patch was re-validated by
running the corresponding script against the patched tree.
