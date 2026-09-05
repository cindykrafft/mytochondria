**Comment posted on #106 on 2026-09-03** (assigned issue: diagnosis and branch link, no PR).

# spm/spm #106 — `spm_MDP_VB_prune` returns NaN priors when a column is left with no prior mass

_Issue-fix kit, 2026-09-03. Not filed; PR not opened. Base: `spm/spm@4e20e07`
(main, 2026-09-02). Branch in the scratch clone: `fix/issue-106-mdp-prune-zero-column`._

## The issue

- **#106 — "spm_MDP_VB_prune: division by zero when all column entries are pruned in
  SIMPLE mode"** — https://github.com/spm/spm/issues/106 (opened 2026-02-08, 0 comments,
  no label, no PR).
- **Reporter's claim.** Running `spm_RDP_update` on the Lorenz-attractor part of
  `DEM_demo_MDP_video.m` with `BMR = 'SIMPLE'`, after a few training iterations some
  columns of the likelihood tensor are completely pruned; the mass-preserving rescale
  `rA = times(rA,sum(pA)./sum(rA))` (lines 89-92) divides by zero, `0*Inf = NaN` flows
  into `spm_MDP_log_evidence`, and `spm_betaln` errors with "Input must be nonnegative".
  Suggested fix: retain the prior for fully-pruned columns before rescaling.
- Comments could not be read from this session (there are none anyway); the body
  contains the traceback, root cause and a proposed patch, which was enough.

> **Assigned issue (2026-09-04).** #106 is assigned to the DEM toolbox author (Friston, 2026-05-11, with #104 and #105). Under the project's rule no PR is opened on an assigned issue: the diagnosis and the branch link go on the thread as a comment (`comment.md`); `pr-body.md` is kept only in case the assignee asks for a PR.

## Diagnosis (on `4e20e07`)

`toolbox/DEM/spm_MDP_VB_prune.m`:

- `:89-92` (`SIMPLE`): `rA = spm_psi(qA)` is normalised per column and thresholded at
  `-log(32)`; the surviving mask is multiplied by the prior `pA` and then rescaled by
  `sum(pA)./sum(rA)`.
- `:82-83` (`MI`, the default): `rA = pA.*exp(pA.*dEdA)` and the same rescale.

The mask can never remove *every* entry of a column (its maximum is always 0 > -log 32;
`spm_psi.m:6` clips at -32 so even an all-zero count column survives), so the reporter's
"all entries pruned" is not literally what happens. What does happen is that the
surviving entries can all carry **zero prior mass**: either the prior column is all zeros
(a state the prior has never visited while the posterior `qA` accumulated counts — the
usual situation in the recursive `spm_RDP_update` loop, where `pp{g}` is the previous
epoch's prior and pruned entries were already zeroed), or pruning removes exactly the
entries where `pA > 0`. Then `sum(rA) = 0`, the factor is `Inf` or `0/0`, and the whole
column of `rA` becomes `NaN`. `spm_MDP_log_evidence.m` adds `1/32`, so `sA` and `F` are
`NaN` too; `spm_betaln.m:27` (`max(z,exp(-32))`, since a546bf3, 2023-06) silently maps
the `NaN` to `exp(-32)` in Octave (and in MATLAB, where `max` also ignores NaN), `F<-T`
is false, but line 116 (`MI`) or 108 (`SIMPLE`) writes the `NaN` column of `rA` back
into the returned prior `pA`, and in `SIMPLE` mode the posterior column is replaced by
`max(NaN-p,0) = 0`, destroying the accumulated counts. The corrupted prior is what the
next epoch of `spm_RDP_update` / `spm_MDP_VB_update` starts from. The `MI` branch has
the same `0/0` for an all-zero prior column.

The reporter's error message ("Input must be nonnegative" from `spm_betaln`) could not be
reproduced here: with the clamp in the current `spm_betaln` the failure is a silent
`NaN` under Octave 8.4; whether MATLAB's `gammaln` raises on the intermediate values in
the reporter's version was not verifiable without MATLAB. The root `0/0` is the same
in either case.

## Reproduction (`repro.m`, Octave 8.4, real SPM code)

```matlab
qA = [64; 1];  pA = [0; 1];                    % prior zero at the surviving entry
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
qA = [64 64; 1 1];  pA = [0 1; 0 1];           % zero prior column next to a healthy one
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0);         % default MI mode
[sA2,rA2] = spm_MDP_VB_prune(sA + 1, rA, 0, 0, [], 'SIMPLE');   % next epoch
```

`repro.before.out` (pre-fix file shadowed in via `PREFIX`):

```
[1] SIMPLE: prior is zero at every entry that survives pruning
reduced posterior sA =   0   0
reduced prior rA     = NaN NaN
[2] SIMPLE: prior column of zeros, second column healthy
sA = [0 65; 0 0]      rA = [NaN 2; NaN 0]
[3] MI (default) mode, same input
sA = [64 64; 1 1]     rA = [NaN 1; NaN 1]
[4] next call with the returned prior
sA = [0 66; 0 1]      rA = [NaN 2; NaN 0]
any NaN in outputs: 1
```

`repro.after.out`:

```
[1] sA = 64 1        rA = 0 1          (column left unchanged)
[2] sA = [64 65; 1 0]   rA = [0 2; 0 0]   (healthy column reduced exactly as before)
[3] sA = [64 64; 1 1]   rA = [0 1; 0 1]
[4] sA = [65 66; 2 1]   rA = [0 2; 0 0]
any NaN in outputs: 0
```

Run: `SPMSRC=<spm checkout> [PREFIX=<dir with pre-fix spm_MDP_VB_prune.m>] octave-cli repro.m`.
`octshim/sum.m` supplies `sum(x,'all')`, which Octave 8.4 lacks and `spm_MDP_MI` uses.

## The fix (`0001-Guard-spm_MDP_VB_prune-against-columns-left-with-no-.patch`)

`toolbox/DEM/spm_MDP_VB_prune.m`: the rescale is moved out of the `MI`/`SIMPLE`
switch; columns with `~any(rA,1)` are set back to `pA` (so `spm_MDP_log_evidence`
returns `F = 0` and both the Occam's-window and the model-averaging branches leave
`qA`/`pA` unchanged there) and get rescale factor 1; all other columns are rescaled by
`sum(pA)./sum(rA)` exactly as before. 12 lines added, 2 removed. This is the reporter's
guard, extended so an all-zero prior column (where `sum(pA)` is itself 0) does not hit a
second `0/0`, and applied to both modes.

## Tests

- New `tests/test_spm_MDP_VB_prune.m` (matlab.unittest classdef, after
  `test_spm_Ncdf.m`): reference reduction of a healthy column, the two zero-mass cases in
  `SIMPLE`, default `MI` with a zero prior column, a 3-D tensor. `driver106.m` runs the
  same 23 assertions in Octave:

  | | assertions failed |
  |---|---|
  | `main` (`4e20e07`) | **11 / 23** (every NaN check and every "column unchanged" check) |
  | fixed branch | **0 / 23** |

- Existing tests for the module: there are none for `toolbox/DEM` besides `ROBOT_DEM.m`
  (runs the demos, MATLAB + figures), which could not be run here.
- Linter: SPM's `tests/test_checkcode.m` wraps MATLAB `checkcode` (unavailable in
  Octave). Both touched files parse and execute in Octave 8.4; no tabs, trailing
  whitespace, CRLF or non-ASCII introduced (the one trailing-whitespace line in the
  file, 135, predates the patch).
- The unittest class itself was not executed (no MATLAB).

## Other candidates considered

- **#104 `spm_VBX_update`: uniform posteriors from a row/column mismatch** — the most
  consequential claim (MNIST accuracy 9.7 % vs 87 %), but the diagnosis is against a
  2025-02 checkout; `spm_dot` was rewritten on top of `tensorprod` on 2026-01-13
  (`69d5b75`) and returns a column for the case described, so it needs re-diagnosis on
  current `main`, a `tensorprod` shim for Octave and the MNIST demo to confirm. Not chosen.
- **#105 `spm_MDP_VB_XXX`: outer product in the path posterior (T > 1)** — same reporter,
  same stale `spm_dot` premise, needs the compression demos to reproduce. Not chosen.
- **#126 DAiSS `bf_output_image_mv` undefined `contrast`** — already fixed on `main` by
  `2c81812` (2026-05-12, "GRB mod 12/5/26"); the issue was simply not closed. Nothing to
  fix; worth a note to the maintainers.
- **#86 `spm_BIDS` `parse_filename` `orderfields` crash for `dir-AP_dwi`** — genuine
  crash (an empty struct is concatenated into `subject.dwi`), but the fix is a choice of
  which entities the dwi template admits, and open PR #17 touches the same lines. Design
  call for the maintainers.
- **#144 `cfg_getfile` breaks matlabbatch** — a maintainer already applied a workaround
  (`a5c4c10`) and says neither problem can be replicated; no reproduction in the body.

## Caveats

- Not run on the reporter's actual scenario (`DEM_demo_MDP_video`, Part 2, `spm_RDP_update`)
  — the demo needs MATLAB graphics and long runs; the 2×2 inputs hit the same line.
- Alternative the maintainers might prefer: dropping the guard into the `SIMPLE` branch
  only (leaving `MI` as is), or excluding zero-mass columns from the reduction rather
  than retaining them. The retained-column choice follows the reporter's suggestion and
  keeps `F = 0` for those columns, so it is a no-op there in both branches.
- `f ~= 0` (contraction over a factor) was not exercised by the tests; the guard sits
  after the contraction and before the fold, so it is dimension-agnostic.
