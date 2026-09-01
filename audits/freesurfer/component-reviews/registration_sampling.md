# Component: mri_vol2surf / bbregister-mri_segreg / mri_surf2surf
Agent verdict (code traced dev+v6.0.0+v7.1.1; F1 reproduced in a COMPILED test):

F1 CONFIRMED (all versions): --projfrac-avg/--projdist-avg float accumulation drops the
   max-depth sample for common (min,max,delta) triplets. `for(ProjFrac=min; ProjFrac<=max;
   ProjFrac+=delta)` with float: 0..1 by 0.1 -> samples 0..0.9 (mean depth 0.45 not 0.5);
   0.2..0.8 by 0.1 -> 0.2..0.7. Systematic white-ward shift ~0.05*thickness (~0.12-0.15mm)
   of fMRI sampling profile at every vertex; also --projfrac-max and mri_surf2vol
   --fill-projfrac (F4). mri_vol2surf.cpp:596-598,635; v6 .c:510-512,540.

F2 CONFIRMED mechanism / PLAUSIBLE exposure: register.dat lacking the trailing float2int line
   silently activates FLT2INT_TKREG floor/ceil/floor -> anisotropic ~half-voxel shifts
   (~1.5mm/axis at 3mm EPI) with default nearest interp. Only third-party-written .dat files;
   FreeSurfer writers append "round". registerio.cpp:140-145; resample.cpp:794-797.

F3 CONFIRMED (all versions): out-of-FOV projection samples contribute ZEROS to projfrac-avg
   (divides by full nproj) -> graded silent attenuation band at functional FOV edges, survives
   into group maps as artifactual deactivation/reduced effect. resample.cpp:806-809;
   mri_vol2surf.cpp:623-635.

F4 CONFIRMED minor: same endpoint-exclusion loop in mri_surf2vol --fill-projfrac (pial shell
   left unfilled). mri_surf2vol.cpp:352.

VERIFIED CORRECT: tkreg CRS2XYZ convention closes end-to-end (no half-voxel mismatch);
bbregister boundary offsets + cost sign chain for T1/T2*/BOLD; surf2surf barycentric/nnfr
weights and --reshape indexing. (--trghits crash noted, not a bias.)

MAPS TO: registration_sampling group (36 papers; 6 explicit mri_vol2surf, 11 bbregister).
F1/F3 bias every surface-sampled fMRI statistic slightly; direction consistent across subjects.
