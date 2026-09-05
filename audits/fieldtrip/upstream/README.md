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

## Filed PRs and their test scripts

- FT1 → [fieldtrip/fieldtrip#2608](https://github.com/fieldtrip/fieldtrip/pull/2608) (fixes #2607); branch now carries `test/test_pull2608.m` (commit 1df1958)
- FT11 → [fieldtrip/fieldtrip#2610](https://github.com/fieldtrip/fieldtrip/pull/2610) (fixes #2609); branch now carries `test/test_pull2610.m` (commit b260b08) and an updated `test/test_ft_connectivity_psi.m` (commit 2f59b90: the existing test used `rpt_chan_chan` input, i.e. a single frequency bin, whose only nonzero output was the very contamination the fix removes; it now uses a 10-bin frequency axis and passes on both master and the branch)
  - 2026-09-04: the maintainer (schoffelen) pushed two commits onto the PR branch (6a03c27 "reorganised code, added comments", 5e7e454 "added tests"): the `normalize='yes'` denominator is now built from the raw coherency magnitudes (`|C(f)||C(f+1)| + 1`, the `+1` kept with a FIXME), `nansum` became `sum(..., 'omitnan')`, and `test_ft_connectivity_psi` gained a two-channel time-shifted simulation with 501 bins plus a `rpt_chancmb_freq` case, both with and without `normalize`. He asked for `test_pull2610` to be removed (its reference reproduced the old denominator, so it is circular and fails with his change) and for a dpss issue.
  - 2026-09-05: `test_pull2610` removed from the branch (9af1fc4). On head 5e7e454 under Octave 8.4 (`verify/pull2610-octave/head5e7e454.results`, `sum.m` shim for `'omitnan'`): `test_ft_connectivity_psi` PASS, `test_ft_connectivityanalysis` (hanning) PASS, `test_pull2610` fails on the normalized reference as expected. Replies drafted: `issue-ft13-reply-2610-tests.md` (PR #2610), `issue-ft14-reply-2609-edge-bins.md` (his NaN-or-data question on #2609); the dpss issue is `issue-ft12-dpss-hack-two-outputs.md` (reproduction `verify/ft12_dpss_hack_two_outputs.m`). The kit copy of `test_pull2610.m` in `tests/` is kept as the record.
- FT2 → [#2613](https://github.com/fieldtrip/fieldtrip/pull/2613) **merged 2026-09-04** by schoffelen ("Looks good to me. Thanks."). #2608, #2611, #2612 open without comments.

- FT7 → [fieldtrip/fieldtrip#2611](https://github.com/fieldtrip/fieldtrip/pull/2611); FTR → [#2612](https://github.com/fieldtrip/fieldtrip/pull/2612) (filed 2026-09-02, open)

Copies of both test scripts are in `tests/`. Each passes on its PR branch and
fails on unpatched master (FieldTrip's `test_pullNNNN.m` convention: `DATA no`,
runnable outside the DCCN).

## Live branches on the fork (cindykrafft/fieldtrip, each one commit on master @ 2e14f72)

| finding | branch | head | compare page |
|---|---|---|---|
| FT1 | `fix/permutation-pvalue-ties` | 3713810 | https://github.com/fieldtrip/fieldtrip/compare/master...cindykrafft:fieldtrip:fix/permutation-pvalue-ties?expand=1 |
| FT11 | `fix/psi-edge-bin` | 9af1fc4 (7 commits: ours + 2 by the maintainer) | https://github.com/fieldtrip/fieldtrip/compare/master...cindykrafft:fieldtrip:fix/psi-edge-bin?expand=1 |
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
