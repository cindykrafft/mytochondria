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
  - 2026-09-05 18:11-18:13Z: all three posted by the owner: dpss issue **#2614**, the reply on #2610 (comment 13, citing #2614), the reply on #2609 (comment 2). Confirmed by a full re-read of the eight threads at 19:59Z; no maintainer reply since his 2026-09-04 comment.
  - 2026-09-07 (read 15:38Z via a helper session): on #2610 schoffelen says "we're almost ready to merge this one" and asks whether the `+1` was meant as a bandwidth normalisation, in which case numerator and denominator should be summed separately. Measured in `verify/ft11d_psi_normalize_bandwidth.py` (`.out`): the ratio of sums is bandwidth-free (nbin 8 vs 2: 1.0 at |C| 0.98) where the per-term ratio scales like the raw PSI (4.0); the `+1` then only halves the magnitude-normalised value at full coherence. Reply drafted: `issue-ft15-reply-2610-bandwidth.md`. On #2614 he calls the hack route "clearly not recommended", the issue very minor (Octave not on the developers' radar), and proposes instead: a specest consistency look (why only mtmfft has `weightopt`), an Octave survey for the FAQ page, and a website FAQ on the missing-dpss problem seen at courses. Reply drafted: `issue-ft16-reply-2614-scope.md` (posted 2026-09-07 17:06Z); FAQ text drafted: `faq-dpss-without-signal-toolbox.md`.
  - 2026-09-16 (read 2026-09-22 via a helper session): schoffelen on #2614: FAQ yes, as a PR for a new page in fieldtrip/website; on the adaptive weighting, the eigenvalue-weighted variant could fit mtmconvol but the derivative-based one cannot, and the benefit is minor; on the Octave survey, "the proof of the pudding is in the eating". Done on 2026-09-22: the page in website format, `website-faq-dpss_without_toolbox.md`, committed as `faq/spectral/dpss_without_toolbox.md` on branch `faq/dpss-without-toolbox`, opened 2026-09-22 as fieldtrip/website#958, **merged 2026-09-23 06:26 UTC by robertoostenveld**, who first pushed one commit of his own (f16105e: new title "How to deal with dpss errors when you don't have the Signal Processing Toolbox?", links to the MathWorks dpss page, the matlab_replacements FAQ and the Riedel & Sidorenko DOI, one wording change); his only comment is "thanks!". Thread read in full 2026-09-23 (helper transcript "Mytochondria thread website 958"): nothing asked, nothing to answer there; the survey runner `verify/octave_survey.py` (471 `DATA no` tests, one Octave process each, WALLTIME-based limits, resumable); reply drafted `reply-2614-faq-octave.md` (post after the website PR exists and the survey is running).
  - 2026-09-22/23: the Octave survey ran (471 `DATA no` tests, Octave 8.4, master cfdad9b): 191 pass. The two biggest causes are FieldTrip's own: `external/stats` never added to the path since 55ee593 (2026-09-15; `ft_platform_supports('stats')` errors on a removed variable inside `ft_defaults`' try; hits MATLAB without the Statistics Toolbox too; `test_external_stats` fails on master), and the `compat/octave` `startsWith`/`endsWith`/`contains` shims with cell-array patterns; behind them `ft_fetch_data`'s `addOptional`. Fixed on branch `fix/octave-compat-survey` of the fork (three commits, pushed), re-run: 286 pass. Write-up `verify/octave_survey/README.md`; issue `issue-ft17-external-stats-not-added.md` (the regression, FT17; **filed 2026-09-23 as #2621**) and PR body `pr-ft17-octave-compat.md` (**PR #2622**, four commits after 99b4c3c on 2026-09-23, merges clean into master 9a10401); the #2614 comment with the table `reply-2614-survey-results.md` (**posted 2026-09-23 16:12**, supersedes `reply-2614-faq-octave.md`); Octave FAQ page edit `website-faq-octave-edit.md`, only if he wants it there.
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
  - 2026-09-23 (read 18:51Z via a helper session): #2614's fifth comment is the owner's survey comment (posted 16:12Z, as drafted); #2621 has no comments; PR #2622 has the github-actions bot's suggested-tests comment (test_bug2269, test_ft_fetch_data, test_issue1292 outside the DCCN; test_bug3379, test_pull810, test_bug1667 inside) and a red "Check for spelling errors" check. The two failing suggested tests stopped in test/private/ft_fetch_data.m, a third copy with the same addOptional declarations: fixed as 99b4c3c on the branch, all three suggested tests pass under Octave (verify/octave_survey/octave_survey_fixed4_raw.tsv). Codespell run locally with .codespellrc: the only hit is the variable `eary` in plotting/private/outline_shape.m:21, on master too (since 9c4a3af), so the check is red on the base branch; a .codespellrc line is proposed in the reply, not pushed. Reply drafted: `reply-2622-tests-and-codespell.md`.
