# Component: R-based group programs
`3dMEMA`, `3dMVM`, `3dLME`, `3dLMEr`

AF3 CONFIRMED (two degrees-of-freedom bugs). `src/R_scripts/3dMEMA.R:2516-2517, 2547`.
   (a) A double negative in the two-group homoskedastic path computes
   `nTotal + nMiss1 - nMiss2 - ...`, inflating voxelwise DF by twice the group-1
   missing count. (b) Under `-unequal_variance`, group-2 t-statistics are
   CDF-converted using group-1's DF.
   Impact: anticonservative p-values at missing-data voxels, and wrong group-2
   statistics wherever the two groups' missing-data patterns differ. Requires
   `-missing_data` and more than one group.

AF4 CONFIRMED. `src/R_scripts/3dLMEr.R:1401-1402`. The GLF stat-type index omits a
   factor of 2 on `num_glt`, so the chi-square declaration lands on GLT Z-bricks --
   a Z of 3 then displays p ~= 0.22 instead of 0.0027 -- and GLF bricks lose their
   statistical type entirely (no p-values, wrong FDR handling).
   Impact: stored values are correct, but every p-value read off those bricks (GUI
   thresholding, `3dClusterize`, FDR) is wrong whenever a run mixes GLTs and GLFs.

AF4b CONFIRMED mis-specification. `src/R_scripts/3dLME.R:2002-2003`: `par` receives
   the whole DF vector, so multiple `-glfCode` tests are all stamped with GLF #1's
   chi-square DF -- wrong p-values for GLF bricks 2..n whenever their DFs differ.

AF5 CONFIRMED. `src/R_scripts/3dMVM.R:1253`: `-robust` GLT z-conversion uses
   `qnorm(p)` instead of `qnorm(p/2)` on a two-sided chi-square p. The same author's
   correct formula appears elsewhere in the same codebase (`3dMVM.R:2056`,
   `3dLMEr.R:901`).
   Impact: robust-regression GLT t/z magnitudes understated, displayed p roughly 2x
   too large. Conservative -- reported findings stand; real effects may have been
   missed.

LIKELY: GLTs that omit a covariate evaluate it at the sample mean rather than the
   user's `-qVarCenters` (`3dMVM.R:1243-1246` and equivalents in 3dLMEr/3dLME) --
   with factor x covariate interactions the GLT estimates then differ from their
   documented meaning and are inconsistent with the omnibus F-tests.

MINOR: 3dMEMA's I^2 uses n-p-1 instead of n-p (slight upward bias); the I^2 sub-brick
   is left all-zero in `-residual_Z` mode; `tConvert` can write +/-Inf for |t| >~ 38
   (`3dMEMA.R:1734, 2121-2131`). `3dMVM -wsE2` aborts via a dangling `else` on a NULL
   old-afex field (`3dMVM.R:1205-1208`) -- a crash, not wrong numbers.

VERIFIED CORRECT: the R programs' I/O scale-factor handling and contrast coding.
