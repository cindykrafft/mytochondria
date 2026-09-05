# PR #2610 tests under Octave 8.4 (2026-09-03)

Run on the fork branch `fix/psi-edge-bin` at `9d99bac` and, for comparison, on `master` at `2e14f72`:

| test | branch | master |
|---|---|---|
| `test_pull2610` | PASS | (fails by design: max abs diff 0.69 at the edge bins) |
| `test_ft_connectivity_psi` | PASS | PASS (with the branch's 10-bin input) |
| `test_ft_connectivityanalysis` with `cfgf.taper = 'hanning'` in place of `cfgf.tapsmofrq = 2` (the maintainer's suggestion; Octave has no `dpss`) | PASS (`int_branch.result`) | PASS (`int_master.result`) |

Octave needed shims for functions it lacks (`convertStringsToChars`, `convertCharsToStrings`, `istable`, `isstring`,
all pass-through or `false`), kept in this directory; they are Octave-only and not part of the PR.
The hanning copy of the integration test was made with `sed` on the four `cfgf.tapsmofrq` lines and is not committed to the branch.

## Re-run on the maintainer's head `5e7e454` (2026-09-05)

`head5e7e454.results`. Octave 8.4 has no `sum(..., 'omitnan')` (the maintainer replaced `nansum` with it), so `sum.m` here is a
pass-through shim that zeroes NaNs first; Octave-only, not part of the PR. The runner scripts now add this directory and
`../shims` to the path explicitly (FieldTrip's `ft_defaults` had shadowed the cwd copies).

| test | head 5e7e454 |
|---|---|
| `test_ft_connectivity_psi` (maintainer's extended version) | PASS |
| `test_ft_connectivityanalysis` (hanning) | PASS |
| `test_pull2610` | FAIL on the normalized reference (max abs diff 0.19): its reference encoded the old denominator; removed from the branch in 9af1fc4 as the maintainer asked |
