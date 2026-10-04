# Facts for a comment on matplotlib PR #32428 (MPL2)

_Owner's decision 2026-10-04: Matplotlib gets one comment only, on the open documentation PR #32428, and no new
issue or PR. These are facts, not comment text. Matplotlib does not accept AI-written comments, so write it in
your own words. Keep it short. Their policy also asks you to say how AI was used, so a one-line disclosure
belongs in it._

**Not to post yet.** First read PR #32428 in full (helper session "Read-only: matplotlib PR #32428
transcript"). Post only if it is still open and still says masked values are ignored.

## The point

- The PR keeps (or adds) the sentence "Non-finite and masked values are ignored." in the `violin_stats` /
  `violinplot` docstrings. To be confirmed against the PR head by the helper read.
- For masked values that is not what the code does on main or in any 3.11 release. NaN and ±inf are dropped as
  documented. Masked entries are kept.
- Cause: `lib/matplotlib/cbook.py:1591`, `x = np.asarray(x)`, removes the mask before
  `delete_masked_points(x)` on the next line. So only non-finite values are removed.
- Both the line and the claim came from PR #31707 (merged 2026-05-28, backported in #31774). That release
  note is in 3.11.0.

## Evidence (3.11.2 release and main, identical)

- `repro.py` in `MPL2-violin-stats-masked/`: 20 lines, numpy and matplotlib only. Paste it into the comment
  rather than linking it.
- The data are 40 normal values plus 50, −50 and 3.3, all three masked.
  - `violin_stats`: min −50.0 and max 50.0, where the unmasked data give −2.325 and 1.493.
  - Mean 0.0205 instead of −0.0604.
  - `violinplot` draws its max line at 50.0.

## The two ways it can go (for them to choose; you can just name both)

- Make the code match the docs: `np.asanyarray(x)` at `cbook.py:1591`. One line. With a test, it passed
  test_cbook and test_axes on the 3.11.2 + main overlay (`MPL2-violin-stats-masked/tests.txt`).
- Or make the docs match the code: drop "and masked" from the sentence, and fix the 3.11.0 API note
  `api_changes_3.11.0/behavior.rst:108–112`. The same note is still duplicated in
  `doc/api/next_api_changes/behavior/violinplot_empty.rst`.

## Disclosure facts

- An automated audit (AI-assisted) found the mismatch and wrote the reproducer and the candidate one-line
  change.
- You checked the reproducer output yourself before posting. Run `repro.py` once on your own machine first.

## After posting

- Tell the session: the comment URL and time. It goes into `site/filed-fixes.txt`, `seen.json` and the
  console as MPL2 (comment on a maintainer's PR).
- Only you reply to anything on that thread. The session can explain a question and re-run tests, but it
  drafts nothing for this repository.
