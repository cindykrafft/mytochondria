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
