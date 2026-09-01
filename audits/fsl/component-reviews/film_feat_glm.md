# Component: FILM / feat5 / miscmaths f2z / cprob (first-level GLM)
Findings verified by compiling routines verbatim and comparing against 400-digit mpmath
and scipy; taper bug verified by a 9000-rep simulation of the full FILM pipeline.

F1 CONFIRMED MAJOR (all versions, FSL origins -> current master): misplaced parenthesis in
   F->z tail conversion. miscmaths/f2z.cc:48:
     loggam = (d1/2.0)*(log(d1/d2) - logbeta(d2/2,d1/2));   // logbeta wrongly inside *
   Correct: (d1/2)*log(d1/d2) - logbeta(d2/2,d1/2). Error exactly zero for d1=2 (why it
   survived 25 years), grows with d1 and d2. Verified: d1=6,d2=500,F=20: FSL z=4.97 vs
   true 9.33; d1=4,d2=200,F=20: 6.05 vs 7.39. Engages above z~4.8. Direction:
   CONSERVATIVE (understated), but also non-monotone: buggy logp can defer to fdtr which
   returns 1.0 -> ndtri -> +inf voxels in zfstat maps (d1=6,d2=200,F=20: true z=8.64,
   output +inf). Affects every published FEAT/FLAME/randomise F-test with >=3 rows and
   reported zf >= ~4.8 (glimGls.cc:120; gsmanager.cc:2494,2756,2863). One-parenthesis fix
   reproduces true log-sf to 4 decimals in all cases tested.

F2 CONFIRMED: d1=1 F-tests never use the asymptotic (f2z.cc:83 requires d1>1) -> saturate
   via double-precision fdtr at z~8.2, then +inf for p < ~1.1e-16. Capped/inf peaks in
   one-row F maps; t-path unaffected (accurate to t=50+).

F3 CONFIRMED (every default FILM analysis): Tukey taper off-by-one — lag k receives
   w(k+1); lag 0 shrunk, window hits zero at M-1. AutoCorrEstimator.cc:524-534.
   Simulation (AR1 phi=.35, N=180, M=13 default): variance understated 2.6% from taper
   shift alone (with ACF estimation bias: 10.8% total vs 8.7% with correct taper) ->
   t/z inflated ~1-1.5%, deterministic, not reduced by spatial ACF smoothing.

F4 CONFIRMED minor: sigma^2 divisor N-p (glimGls.cc:80 R.Trace()) inconsistent with the
   dof N-p-1 used for t/F (grand-mean removal + DC-killed filter) -> varcopes biased low
   by (N-p-1)/(N-p), ~0.5-3%. Anticonservative, small.

F5 PLAUSIBLE conditional: design-column means exempted from whitening (mean added back
   after filtering; data DC removed entirely) -> no-op for FEAT designs (feat_model
   remmeans), but film_gls on non-demeaned/voxelwise EVs (--vxf/--vef): copes and t
   roughly HALVED in simulation with EV mean ~0.4*range. Perfusion/PPI-variant subset.

VERIFIED CORRECT: t->z conversion exact to |dz|~2e-4 over dof 5-400, t to 50 (published
t-based zstat images numerically sound arbitrarily far into the tail); prewhitening
symmetry (same per-voxel filter on data and design) and GLS variance forms; feat5
smoothest/cluster wiring (dof, DLH, RESELS, VOLUME all passed correctly).

MAPS TO: all 25 FEAT/FILM papers (F3 universal small inflation; F1/F2 wherever F-tests
reported); FLAME/randomise F maps inherit F1 through the shared f2z.
