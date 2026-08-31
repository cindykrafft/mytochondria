# Component: flirt / mcflirt / newimage / warpfns / applywarp / fnirt
Reviewed end-to-end incl. interpolation kernels and coordinate conventions.

F1 CONFIRMED (env-dependent, silent): sinc interpolation uses shared mutable scratch
   buffers (kernel.h:45-47 storex/y/z, process-global kernel dedup) written by a const
   method (newimage.cc:594-602), while raw_general_transform spawns threads over y-rows
   (warpfns.h:826-882; thread count = FSL_NUM_THREADS). applywarp --interp sinc with
   FSL_NUM_THREADS>1: threads mix each other's kernel weights -> plausible-looking but
   wrong voxel values, nondeterministic run to run, up to full local contrast at edges.
   Trilinear safe; spline path mutex-guarded; only sinc/userkernel races.

F2 CONFIRMED: flirt -usesqform applies the basescale conversion twice (qsform_init_mat
   scales at flirt.cc:1263-1275, set_initmat scales again :1278-1292; correct count is
   zero for this path) -> init translation multiplied by 1/basescale^2. basescale != 1
   is AUTO-enabled for voxels < 0.75mm (7T/HCP structurals: translations inflated
   x2-2.8) or > 12mm. Converged output stays self-consistent, but the wrong starting
   point (tens of mm) can push the search out of its basin -> gross misregistration on
   exactly the high-res data -usesqform targets.

F3 CONFIRMED: BBR fieldmap extrapolation direction is a transformed homogeneous POINT,
   not a direction (costfns.cc:2767-2770): affine translation contaminates the "PE
   direction", normalization includes the homogeneous term, and the PE axis is
   hard-coded to y. Vertices near/outside the fieldmap mask get B0 shifts extrapolated
   from an arbitrary direction -> biased BBR transforms (epi_reg --fmap), fraction of a
   voxel up to a few voxels at steep-gradient mask edges. Non-fieldmap BBR unaffected.

F4 PLAUSIBLE minor: applywarp --usesqform --super half-voxel correction folded to the
   wrong side of the sform affine in the no-warp branch -> sub-voxel residual shift.

F5 PLAUSIBLE input-dependent: silent abs-vs-rel warp auto-detection (is_abs_convention,
   SD heuristic) can misclassify third-party warp files -> gross silent misregistration
   (FNIRT files immune via intent codes).

NOT-BUGS verified: grad_calc divisor "discrepancy" is an exact similarity (Jacobian
det invariant); commented-out neurological swaps are dead safety code (radiological
order enforced on read).

VERIFIED CORRECT: premat/warp/postmat composition incl. FNIRT affine add/remove and
supersampling compensation; MI/NMI/CR fuzzy binning (exact partition of unity, exact
overlap renormalization); spline interpolation (textbook Unser poles); MCFLIRT applies
motion exactly once, middle-volume reference, exact Jenkinson RMS.

MAPS TO: 19 FLIRT / 9 MCFLIRT / 7 FNIRT papers; F1 depends on cluster env
(FSL_NUM_THREADS); F2 on sub-0.75mm + -usesqform; F3 on epi_reg fieldmap BBR.
