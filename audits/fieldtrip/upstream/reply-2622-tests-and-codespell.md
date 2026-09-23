Title: (comment on PR #2622) suggested tests run under Octave; test/private copy added; the codespell failure is a variable name on master

<!-- Reply to the github-actions bot's comment of 2026-09-23 16:11 on PR #2622 ("please consider testing: test_bug2269, test_ft_fetch_data, test_issue1292" outside the DCCN; test_bug3379, test_pull810, test_bug1667 inside), and to the red "Check for spelling errors" check. Thread read in full 2026-09-23 (helper transcript "Mytochondria threads ft 2614 2621 2622"). The fourth commit 99b4c3c is already on the branch; the four tests were run on it under Octave 8.4 (audits/fieldtrip/verify/octave_survey/octave_survey_fixed4_raw.tsv). Codespell was run locally with the repository's .codespellrc on the branch and on master 9a10401: the only hit is plotting/private/outline_shape.m:21 "eary" in both, i.e. red on master too; the .codespellrc change is proposed, not included. MATLAB is not available in the session, so the DCCN tests and a MATLAB run are the maintainers' or the owner's. -->

The three suggested tests that need no data, run on this branch under GNU Octave 8.4 (no MATLAB here):

| test | master | this branch |
|---|---|---|
| `test_bug2269` | fails in `compat/octave/startsWith.m` (cell pattern) | passes |
| `test_ft_fetch_data` | fails, `NaN: dimensions must be scalars` in `test/private/ft_fetch_data.m` | passes |
| `test_issue1292` | same | passes |

The last two failed for the reason the PR fixes: `test/private/ft_fetch_data.m` is a third copy of `ft_fetch_data` with the same `addOptional` declarations, so the header struct landed in `begsample` and `nan()` got a struct as a dimension. I pushed 99b4c3c, which applies the `addParameter` change to that copy as well; the three copies are identical again. The DCCN tests (`test_bug3379`, `test_pull810`, `test_bug1667`) need private data, so I could not run them.

The failing "Check for spelling errors" check is not from this PR: with the repository's `.codespellrc`, the only hit on `plotting utilities` is `plotting/private/outline_shape.m:21`, the variable `eary` (the y-coordinates of the ear outline next to `earx`), and it is the same on current master. If you want the check green, one line in `.codespellrc` does it; I have left it out of this PR since it is unrelated:

```
ignore-words-list = indx,...,datas,earx,eary
```
