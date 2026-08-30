# Component: mri_glmfit / fsglm / cluster correction
Agent verdict (dev + v6.0.0 + v7.1.1 + v7.4.1 traced):

F1 CONFIRMED ANTICONSERVATIVE (v5.3-7.4, fixed only on dev): VOLUME cluster correction
   connectivity mismatch — null CSD built with 6-connectivity (clustGetClusters hardcodes
   allowdiag=0; mri_glmfit.cpp:1893) while observed clusters use --allowdiag 26-connectivity
   (mri_glmfit-sim script v6:~600, v7.1.1:640, v7.4.1:674). Observed clusters can only be >= null
   -> cluster p-values biased DOWNWARD in every volume-based --sim mc-full/--perm result.
   Dev fixes it and comments "must match mri_volcluster". SURFACE analyses unaffected.

F2 CONFIRMED small anticonservative (all versions): CSD p-value convention nover/nreps with
   strict >; exact (b+1)/(m+1) convention only behind env var FS_CSDPVALCLUSTSIZE_GTE (7.2+).
   In-code comment: "Using just > is too liberal". Also CSDpvalMaxSig has no floor -> p=0 ->
   +/-inf written into sig.voxel.mgh.

F3 CONFIRMED strongly anticonservative, narrow scope (all versions): GLMtestFFx multi-row (F)
   contrasts not divided by J — Wald stat handed to F(J,dof) without /J. J=2 Wald=6: true
   p~0.05 reported as ~0.0025 (~20x). Only fixed-effects (--yffxvar/--ffxdof) with J>1;
   random-effects GLM correct. fsglm.cpp:703-711 (v6 identical).

F4 CONFIRMED (7.2..dev): pcc output dead code — inverted NULL guard after 2022 refactor;
   pcc.mgh never written/zero. Effect sizes only, not p-values. fsglm.cpp:425-427.

F5 CONFIRMED code property (all versions): permutation shuffle is biased swap (not
   Fisher-Yates) -> null not uniform over permutations; small, direction unclear.
   evschutils.cpp:505-520. DEV-ONLY hard bug: sign-flip branch reseeds with fixed seed each
   draw -> degenerate 2-state null (not in any release yet).

F6 CONFIRMED dev-only: --fdr cluster-forming threshold computed differently on sim vs data side
   (BH at 2q vs 2x BH-at-q cutoff). Not in 7.x scripts.

F7 PLAUSIBLE small: mc-z cache FWHM rounded to nearest integer table (no interpolation);
   searchspace vs data-mask mismatch unchecked outside CSDmerge.

Eklund-era context (grounded in repo): mc-z machinery unchanged v6->dev; v6 help already warns
against CDT 1.3 without permutation; v7 switched --perm to ter Braak residual permutation.

VERIFIED CORRECT: core GLM (beta/rvar/F/p/WLS dof); one/two-tail bookkeeping end-to-end
(-log10(2) adjustments consistent across glmfit/mcsim/surfcluster); surface cluster area fix
applied once on both paths; BH step-up correct.

MAPS TO: group_glm (12 papers). Key discriminator: volume-based vs surface-based correction;
FFx F-tests; nsim size for borderline p.
