# Component: Python pipeline, DTI and PCA tools
`afni_proc.py`/`afnipy`, `timing_tool.py`, `3dDWItoDT`, `3dTrackID`, `3dpc`

AF14 CONFIRMED. `src/3dDWItoDT.c:2618-2641`: the b=0 guard present in the linear
   path (`Form_R_Matrix`) was never copied into `Computebmatrix`, so a `0 0 0`
   gradient row makes the entire default nonlinear tensor fit NaN.

AF14b LIKELY, numerically demonstrated. `src/3dDWItoDT.c:2975-3008`: only the
   diagonal of H- is negated, collapsing the Cayley descent step to the diagonal of
   FD, with a symmetric-only inverse applied to a non-symmetric matrix. Still a
   descent direction, so it converges -- but it can stop at a non-stationary point,
   and was shown to stall above both the corrected scheme and the true least-squares
   minimum (FA error in the 3rd-4th decimal in the test case; data-dependent).

AF16 CONFIRMED, label only. `src/3dpc.c:689`: an integer-rounding `+0.499` left in a
   `%f` format overstates the variance in sub-brick labels by ~0.5 percentage points.
   The `_eig.1D` values are correct; only readers of the brick labels are affected.

AF22 LIKELY. `src/ptaylor/3dTrackID.c:3492-3495`: no negative-rounding guard before
   `sqrt` for per-bundle standard deviations, so float accumulation of
   sum(x^2) - N*mean^2 can go negative and write NaN FA/MD/RD/L1 stdevs into `.grid`
   files. The identical bug was fixed for bundle length directly below in 2016.

AF23 LIKELY (timing_tool.py). `afnipy/lib_timing.py:706-717` `-timing_to_1D`: two
   events touching the same TR overwrite rather than accumulate their fractions
   (0.3 instead of 0.6), which can flip `min_frac` threshold decisions; plus an
   IndexError for events ending exactly at run end. `:197-198` `-global_to_local`:
   an `nrows < 2` early return leaves a lone event in run 1 at its global time -- a
   misplaced or dropped regressor for single-event-per-class timing files.

LATENT (`afni_util.py`): `proj_onto_vec` with `unit_v2=0` crashes (two-arg call to a
   one-arg function) and divides by the norm instead of the squared norm -- the only
   in-tree caller passes unit vectors; `argmax`/`argmin` ignore their `absval` flag;
   `write_as_timing` opens its output file in read mode (unreachable).
   `3dcalc gran()`: half the draws come from a sum-of-12-uniforms with zero mass
   beyond +/-6 sigma and wrong tails beyond ~+/-3 sigma -- matters only for
   tail-sensitive null simulations.
   `AFNIio.R`'s pure-R I/O fallback (`-Rio` only) reads bytes as signed and truncates
   floats to 2-byte ints on write; near-dead, since `R_io.so` is mandatory in modern
   installs.

VERIFIED CORRECT, and directly relevant to AF1: `afni_proc.py` numerics --
percent-signal-change scaling, motion enorm (per-run derivative, no run-break
contamination), censor bookkeeping, outlier logic, TSNR, and the timing conversions
apart from the two flagged above. Also FA/MD formulas and eigen handling in
`3dDWItoDT`.
