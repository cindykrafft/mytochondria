# Component: flameo (FLAME group mixed effects) + shared f2z/t2z
Suspect routines ported faithfully to Python and tested against scipy / grid-search truth.

F1 CONFIRMED (independent confirmation of the f2z.cc:48 parenthesis bug found by the
   FILM review): re-derived the integration-by-parts series; fix reproduces scipy exact
   F tail to <1e-3 z. Emitted errors with branch gating: d1=4,d2=100: true 6.84 ->
   reported 5.61; d1=6,d2=30: 7.84 -> 5.62. NON-MONOTONIC in F (d1=4,d2=100: z drops
   6.25 -> 4.94 as F increases past 16.75). Reached from every flameo run mode (OLS, FE,
   FLAME1, FLAME1+2). d1=2 coincidentally exact. Conservative + rank distortion.

F2 CONFIRMED MAJOR (FLAME1+2 F-tests, >=2 EVs): multitfit uses the UNIVARIATE t
   moment-matching formula v=2/(1-phi/cosi) for a P-dimensional fit (needs cosi/P).
   gsmanager.cc:471. Verified: P=1 recovers true dof; P=2/3/5 yields dof ~2.9/2.5/2.3
   REGARDLESS of true dof (Gaussian samples -> 3.0). F=10,d1=2: z=3.04 at dof 18 vs
   z=1.67 at dof 3. Massively deflates flame12 F statistics. t contrasts (P=1) correct.

F3 CONFIRMED edge: FLAME1 dof fallback — if every in-contrast variance group has
   ntpts<=nevs, tdof silently stays INT_MAX/10 (~2.1e8) -> t converted with no
   small-sample penalty; inflates z. gsmanager.cc:2594-2611 (outlier variant
   inconsistently uses 1000 at :2652).

F4 CONFIRMED (burn-in dependent): FLAME2 MCMC initializes random-effects variance beta
   in NORMALIZED units but runs the chain on RAW cope/varcope (factor var(Y_raw),
   commonly 1e2-1e6), fixed proposal width 4 -> insufficient burn-in biases beta low ->
   z inflated at high-variance voxels. The in-code |z2-z1|>3 tripwire confirms the mode.

F5 PLAUSIBLE: solveforbeta golden-section can lock onto boundary plateau (beta=1e-10)
   when marginal posterior bimodal (~1/300 simulated voxels) -> z inflated there. The
   Brent bookkeeping typo at :391 verified to change NO results (300 trials).

F6 minor confirmed: d1=1 F -> +inf z via fdtr/ndtri; MCMC `return` vs `continue` on
   out-of-support proposals (costs mixing, not correctness); adaptation never stops;
   int() truncation of fractional BIDET dof (<=1 dof conservative); stage-1 vs stage-2
   outlier variance models disagree under --infer.

DOF bookkeeping: lower-level dofs ignored by FLAME1 (used only in FE mode and as the
FLAME2 phi prior); FLAME1 z = t at min in-contrast group (N_g - p_g).

VERIFIED CORRECT: all t-statistic z conversions (scipy-checked, dof 3-1000, t 2-50,
max err ~4e-5); OLS path (n-p variance, contrast variance, dofs); FLAME1 marginal
energy formula + exact un-doing of per-voxel normalization on output; design/grp
parsing with hard errors instead of silent misgrouping.

PRACTICAL READ: t-contrast results from OLS/FE/FLAME1 (the overwhelmingly common FEAT
higher-level configs) rest on code the review could not fault. Distortions concentrate
in F-tests (F1 all modes; F2 flame12) and flame12 edge paths (F3-F5, inflation).

MAPS TO: 9 FLAME papers + every FEAT higher-level analysis in the 25 FEAT papers;
F-test users are the exposed subset.
