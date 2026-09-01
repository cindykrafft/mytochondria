# Component: cluster / smoothest / infer (GRF cluster correction)
Traced at fsl/cluster master (ead7b49); numeric claims verified by compiling verbatim
copies of the code under test and a line-faithful Python transcription of Infer.

F1 CONFIRMED SEVERE (2D analyses only): cluster.cc:534-538 calls infer.setD(2) for
   single-slice images, but Infer's constructor (infer.cc:36-57) has already frozen
   Em_ and B_ with the 3D EC density and 3D exponent; setD only changes the exponent
   used at evaluation (pow(k,2/D)). Constructor comment even says the caller should
   set D=2 "to be done by calling program" — impossible. Verified numerically:
   t=2.3,k=30: p_code=1.2e-5 vs true 1.3e-3 (~100x anticonservative); t=3.1,k=30:
   ~12,000x. FEAT supports single-slice (featlib.tcl:5956). 3D whole-brain unaffected.

F2 CONFIRMED (conservative, small-n): smoothest.cc:67-77 LUT interpolation anchors the
   slope at the lower node but adds it to the UPPER node's value — off by a full
   inter-node step; plus v<6 returns 1.1 without the sqrt applied to every other path
   (should be 1.242). dLh multiplier ratio code/correct: dof5 0.886, dof10 0.988.
   A cluster at true p=0.05 reported as p=0.077 at dof 5. Hits small-n FLAME higher
   levels (stats/dof 5-11); negligible at first-level dof.

F3 CONFIRMED (formula error, practical impact nil): infer.cc:54 uses (2pi)^(-1/2) where
   the Mills-ratio expansion requires (2pi)^(+1/2) — B_ low by exactly (2pi)^(2/3)=3.405
   in the |t|>=8 branch; p discontinuity at t=8 (B_ 1.681 -> 0.492). Conservative, only
   for CDT>=8. Also unguarded Em_=0 -> log(0) at |t|>=13, and CDT<1 would go negative.

F4 CONFIRMED design/assumption (the Eklund-relevant one): FEAT hard-codes 26-connectivity
   (featlib.tcl:5104-5119, pixdim-dependent choice commented out) while Infer's extent
   distribution is connectivity-free continuum theory + squared-exponential ACF.
   Anticonservative at low CDT (z=2.3); an assumption mismatch faithfully implemented,
   not a transcription slip.

F5 PLAUSIBLE minor: dof correction applied to DLH but not RESELS/FWHM (smoothest.cc:329
   vs 333-338); FEAT's voxel-wise GRF path uses RESELS (featlib.tcl:6018-6022) ->
   mildly anticonservative voxel FWE at low dof (~0.01-0.05 z-units).

F6 NOTE: the (v-2)/(v-1) residual-standardization correction is computed and never
   applied (commented out) — provably a no-op anyway (only the ratio SSminus/S2 is used).

F7 NOTE: fallback paths (no res4d; easythresh) estimate smoothness from the z-map itself
   -> conservative when real activation present.

VERIFIED CORRECT: 3D GRF formulas exactly implement Friston-1994/Worsley (matched an
independent Python implementation to all digits, t=2.3/3.1, k=50-400) — Eklund-type
z=2.3 anticonservativeness in 3D is the theory's assumptions, NOT a coding slip;
smoothest core algebra (sigmasq, dLh, FWHM, fail-safe clamps, edge handling);
connected_components + FEAT wiring (incl. zeropad safety). Trap for reproducers:
infertest.cc prints ln(p) labeled as p.

MAPS TO: GRF cluster papers (7) + every FEAT z>2.3 cluster result (25 FEAT papers);
F2 discriminator: small-n group analyses; F1: single-slice studies.
