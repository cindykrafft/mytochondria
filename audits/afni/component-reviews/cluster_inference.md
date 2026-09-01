# Component: cluster-extent inference
`3dClustSim`, `3dFWHMx`, ACF machinery, `3dXClustSim`/ETAC, `3dClusterize`

AF9 CONFIRMED, numerically reproduced. `src/mri_fwhm.c:1211-1218`,
   `src/3dBlurToFWHM.c:738`. The widely quoted 4th output of `3dFWHMx` measures the
   half-maximum width of the ACF *curve*, which for Gaussian-smoothed data is exactly
   sqrt(2) x the smoothing-kernel FWHM (verified: an 8 mm kernel reports 11.31).
   The help attributes the gap to "long tails", conflating a real tail effect with a
   hard-wired change of definition.
   Impact: published ACF smoothness values are not comparable with classic /
   SPM / FSL kernel-FWHM numbers, and `3dBlurToFWHM -acf -FWHM G` stops at ACF-width
   G, delivering only about G/sqrt(2) of kernel-equivalent smoothing -- so papers
   describing their smoothing that way describe it incorrectly.
   Crucially `3dClustSim -acf` cluster p-values are NOT affected: only the (a,b,c)
   parameters are passed and the simulation reproduces the ACF itself.

AF16b CONFIRMED. `src/3dXClustSim.c:1685-1686, 2493-2494`: an ETAC realloc
   copy-paste bug reallocs `tfs` and assigns the result to `fps` -- aliasing,
   use-after-free UB, corrupted warm starts. Reachable in `-muchoFPR`-style runs
   exceeding 128 calibration steps. Final thresholds are closed-loop calibrated, so
   typical runs land correctly.

LATENT: `3dClustSim -tdof` thresholds t-distributed values at Gaussian quantiles
   (`3dClustSim.c:1622-1633`) -- conservative direction, hidden option, no shipped
   pipeline uses it. Dead-code cluster finders in `mri_clusterize.c:415-492`
   (inside `#if 0`) test `jp < nx` where `ny` is required; the `USE_SHAVE` block at
   `3dClustSim.c:2385` would not compile.

VERIFIED CORRECT (the reassuring half, and the highest-stakes machinery in the
package): the entire post-2015 ACF cluster-inference pipeline -- 3dFWHMx ACF
fitting, the ACF random-field generator (Monte-Carlo validated), 3dClustSim
sidedness and alpha tables with no off-by-one, identical NN cluster definitions in
simulation and in data, and the GUI table-lookup path end to end.
