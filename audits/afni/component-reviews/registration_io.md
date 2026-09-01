# Component: registration, motion, interpolation, NIfTI I/O
`3dvolreg`, `3dTshift`, `3dAllineate`/`3dQwarp`, `thd_niftiread.c`, interpolation kernels

AF6 CONFIRMED. `src/thd_niftiread.c:653`. The `NIFTI_SLICE_SEQ_DEC` loop condition
   compares `kk >= slice_end` instead of `slice_start`, so it executes exactly once
   and every slice offset stays zero. `3dTshift` then sees a uniform pattern and
   performs no correction while appearing to succeed.
   Impact: up to about one TR of uncorrected temporal misalignment for
   sequential-descending acquisitions whose NIfTI files carry slice codes --
   including files AFNI itself writes for seq-z datasets. The trigger is a header
   field papers never report, so a code-side warning would find affected datasets far
   better than the literature can.

AF12b CONFIRMED. `src/3dTshift.c:630-633`: under `-no_detrend` a copy-paste error
   demeans `far` twice and `gar` never, so every second voxel is shifted with its
   full DC offset against zero-fill/wraparound edges -- systematic even/odd voxel
   striping at run edges.

LATENT: `wsinc5` interpolation with `AFNI_WSINC5_RADIUS=20` sums 41 taps where only
   40 are initialized (`mri_genalign_util.c:777-783`) -- a garbage-weighted
   uninitialized read. The default radius 5 is unaffected.
   `AFNI_dicomm_to_xyz` applies the forward instead of the inverse axis permutation
   (`thd_coords.c:419-432`) -- zero callers in the tree.

VERIFIED CORRECT: `3dvolreg` motion conventions and shear decomposition (300,000
random cases, maximum reconstruction error ~1e-8); NIfTI qform/sform L-R handling,
with no flip risk; all interpolation kernels (partition of unity confirmed);
datum-conversion rounding uses proper `rint`, not truncation; blur-kernel
normalization and the FWHM<->sigma constant.
