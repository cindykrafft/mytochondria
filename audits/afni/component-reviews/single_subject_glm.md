# Component: single-subject GLM
`3dDeconvolve`, `3dREMLfit`, `remla.c`, `1dgenARMA11`

AF15 CONFIRMED, numerically reproduced. `src/armacor.c:147, 343`: `abs(cnew)` applies
   integer `abs()` to a double, so it is 0 for every |c| < 1 and the generated
   correlation sequence always stops at lag 5/7 regardless of the true decay (the
   intended sequence runs to lag 59 in the verified example). Simulation-validation
   studies built on `-arma31`/`-arma51` noise generated far weaker long-range
   autocorrelation than they requested. The default `-arma11` path is unaffected.

LATENT: `remla.c:1807, 1916` -- the ARMA(3,1)/(5,1) root-to-coefficient formulas use
   the *sum* instead of the *product* of roots (should be p3 = a*r1^2,
   p5 = a*r1^2*r2^2; the 2020 `armacor.c` is correct). Compiled into `3dREMLfit`
   but never called. Should not be resurrected as-is.

CONVENTION: legacy `-stim_file` lagged regressors bleed across `-concat` run
   boundaries; the modern `-stim_times` path correctly clamps each event's response
   to its own run.

VERIFIED CORRECT, and this is the single most-used code path in the package:
`3dDeconvolve` design-matrix construction, Legendre baselines, censoring and DF
bookkeeping, GLT t/F statistics, and the BLOCK/SPM/TENT/CSPLIN basis functions
against closed forms. `3dREMLfit`'s live ARMA(1,1) path: the (a,b)->(rho,lambda) map
validated by direct simulation, plus banded Choleski, the REML objective, GLS
estimates and whitened GLT algebra.
