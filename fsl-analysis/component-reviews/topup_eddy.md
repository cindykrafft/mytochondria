# Component: topup / eddy (susceptibility + eddy-current/motion correction)
Reviewed end-to-end: bvec rotation, field->displacement units, Jacobian modulation,
resampling contracts, --repol.

F1 CONFIRMED (narrow): applytopup --method=jac, plain-fieldmap branch, uses xdim for the
   y-scale (applytopup.cpp:1140-1146: ycomp *= ... * ovol.xdim()) -> Jacobian dy/dy term
   scaled by xdim/ydim. Only bites with a NON-topup field + anisotropic in-plane voxels +
   PE in y; isotropic in-plane (the common case) unaffected — why it survives.

F2 PLAUSIBLE (file-convention dependent): eddy_rotated_bvecs ignore the FSL x-flip
   convention for positive-determinant (neurological-stored) NIfTIs — eddy applies R^T
   where F.R^T.F is needed; direction error ~2x subject rotation about y/z for such data.
   Radiological (det<0) data exact. No neuro/radio handling anywhere in eddy (verified
   by grep); within the code the rotation is provably self-consistent (see V1).

F3 minor: --resamp=lsr bvecs averaged without renormalization, positional pairing
   (chord vector, |b|<1). Rare output path.

F4 PLAUSIBLE minor: --repol "replaced" slices keep original corrupted intensities where
   the transformed prediction mask is invalid (FOV edges) -> mosaic slices in final data.

F5 observation: outlier DETECTION predictions include the tested volume (conservative,
   under-flags moderate dropout, worst on sparse shells); REPLACEMENT is correctly
   leave-one-out.

VERIFIED CORRECT (prime suspects exonerated): bvec rotation direction exactly matches the
applied resampling (raw_general_transform contract traced; PEAS folded in before writing);
field units/sign/readout-time scaling consistent topup->eddy->applytopup for AP and PA;
Jacobian modulation applied exactly once from the same field used to resample, in both
directions, incl. the tricky s2v combined EC+susceptibility field.

MAPS TO: 24 topup/eddy papers — standard pipelines NOT invalidated; check any paper using
applytopup jac with dual-echo fieldmaps + anisotropic voxels, or neurological-stored data.
