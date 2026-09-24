Title: (comment on PR #1043) regression tests added as suggested

<!-- Reply to kvnloo's comment of 2026-09-24 07:18 on PR #1043 (author association NONE, not a maintainer: an independent tester who exercised the fix in 12 cases and asked for a two-level regression test). Thread read in full 2026-09-24 (helper transcript "Mytochondria threads kilosort 1043"); nothing from the maintainers on any of the five Kilosort filings yet. The tests are pushed as eabed49 on the PR branch; run under kilosort at the branch with CPU torch: 4 passed; with main's swarmsplitter.py: 2 failed (ValueError in compute_CCG on the empty input; cross_refractory False and refractoriness 0 on the refractory halves). -->

Thanks for checking it independently, and for the test sketch. I pushed eabed49 with `tests/test_swarmsplitter.py`, which covers both levels you describe:

- `test_check_ccg_empty_inputs`: an empty first, second or only train returns `(False, False)` instead of reaching `compute_CCG`;
- `test_check_ccg_zero_duration`: the `T == 0` path;
- `test_refractoriness_blocks_refractory_split`: two random halves of one simulated refractory unit (3 ms refractory period, ~10 Hz, 20 min) are reported `cross_refractory` and `refractoriness()` returns 1;
- `test_refractoriness_allows_independent_units`: two independent units are not vetoed, so the fix does not simply block every split.

With this branch all four pass (CPU torch); with the `swarmsplitter.py` of v4.1.5 through v4.1.7 the empty-input test raises `ValueError` inside `compute_CCG` and the veto test fails with `refractoriness() == 0`, so the tests catch both halves of the original problem. Like your run, this is CPU-only and does not include a full sorting pass.
