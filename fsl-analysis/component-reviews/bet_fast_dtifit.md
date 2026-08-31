# Component: bet2 / fast4 / fdt (dtifit, bedpostx CPU)
Verified end-to-end from input parsing to saved outputs; meshclass fetched for BET mesh.

F1 CONFIRMED defect, currently INACTIVE: DTI::angles2rot writes rot(1,3)/rot(2,3) into
   transposed cells then overwrites them — two cells never assigned; corrupts the
   Levenberg-Marquardt tensor fit's cost/Jacobian/eigenvectors. No caller in the fdt
   tree today (dtifit uses tensorfit(), xfibres uses linfit) — a landmine, not an
   active bias. diffmodels.cc:155-163.

F2 CONFIRMED systematic: dtifit clamps signal below 1% of S0 (dtifit.cc:295;
   diffmodels.cc:41) -> per-direction ADC capped at 4.6/b. At b=3000, CSF (D~3.0e-3)
   fits as D~1.53e-3: MD/L1 underestimated ~2x in high-diffusivity voxels. b=1000
   single-shell in-brain unaffected. Always downward; silent.

F3 CONFIRMED: no negative-eigenvalue handling — FA>1 and negative L3/MD reach output
   files (tensorfit sorts but never clamps; calc_FA guards only fsquared<0).
   ROI-mean FA inflated / MD deflated wherever low-SNR voxels enter the ROI;
   interacts with F2 on the same voxels.

F4 CONFIRMED: BET2 mask = interior + every surface-touching voxel (one-sided
   voxelization) -> brain volume overestimated by a partial one-voxel shell (~1-2% at
   1mm, grows with voxel size). Plus the self-intersection fallback applies 10^(pass+1)
   extra smoothing only to triggering subjects -> heteroscedastic positive volume bias.
   Consistent across subjects (group contrasts mostly survive); absolute volumes and
   cross-resolution comparisons biased up.

F5 CONFIRMED negligible: BET2 median-intensity tm off by one rank (bet2.cpp:379-381).

F6 CONFIRMED inconsistency: FAST4 bias-field smoothing — single-channel sigma =
   0.51*lowpass (docs say FWHM mm; actual FWHM ~24mm at -l 20, ~20% smoother than
   documented; kernalsize argument ignored); multi-channel uses sqrt(lowpass/xdim),
   a dimensionally different rule. Single- vs multi-channel tissue volumes not
   comparable at the same -l; under-correction of strong coil inhomogeneity.

F7 PLAUSIBLE minor: --wls SSE map is unweighted (weighted line commented out);
   xfibres proposal adaptation continues after burn-in (breaks detailed balance
   formally; affects spread more than means); FAST PV delta-grid float endpoint miss
   (sub-1e-4).

VERIFIED CORRECT: dtifit linear-fit chain (b-matrix, bvec normalization, eigen
selection all orderings, FA/MO formulas hand-verified, multiple b0s, DKI scaling,
gradient-nonlinearity correction); bedpostx MCMC model math (stick/gamma/zeppelin
signals, Rician logIo, priors, accept/reject incl. self-healing staleness); BET2
evolution vs Smith 2002 (incl. the deliberate f^0.275 remap of -f — not a bug).

MAPS TO: 16 BET papers (absolute volumes), 9 dtifit/bedpostx papers (F2 for b>=1500
multi-shell; F3 for ROI stats near CSF/edges), 4 FAST papers (F6).
