# Component review: spatial toolboxes

Scope: `toolbox/FieldMap`, `toolbox/DARTEL` (*.m), `toolbox/Shoot` (*.m),
`toolbox/Longitudinal`, `toolbox/OldNorm`, `toolbox/OldSeg`,
`toolbox/Spatial`, `spm_dartel_integrate`.
Method: full read of Longitudinal/OldNorm/OldSeg/Spatial; FieldMap covered
by the first reviewer up to interruption; DARTEL/Shoot spot-checked for major
errors. Suspicious transforms ported to NumPy and round-tripped.

**Coverage caveat, stated plainly:** this is the one subsystem the project
calls thoroughly-but-not-exhaustively covered. The original reviewer was
interrupted mid-FieldMap (after confirming the finding below and clearing
the phase-unwrap region merging examined to that point); a second reviewer
completed the remaining toolboxes. No confirmed FieldMap defect was recorded,
but its coverage is partial.

## Confirmed

1. **`toolbox/Spatial/spm_smooth_extrap.m:57-59`** (`spm_smooth_fft`) — the
   centred coordinate grid `(1:dims) - dims/2 - 1` used to build the k-space
   Gaussian lands on an integer centre only for even dimensions; odd
   dimensions get a grid off-centre by half a voxel, an asymmetric kernel,
   and a smoothed volume shifted ~0.5 voxel along every odd axis (reproduced:
   a 7-voxel impulse's centre of mass moves +0.45 voxels; an 8-voxel axis
   moves −0.02). Used for VDM smoothing/extrapolation
   (`spm_est_vdm_from_phase:85`, `spm_scope`), so fieldmap-less distortion
   correction inherits a systematic geometric shift on odd-sized volumes.
   **Medium-high** (SP16); independently confirmed by both reviewers.

## Verified correct

Longitudinal: `spm_groupwise_ls` (Jacobian cofactor gradient transport),
`spm_dexpm` (recursive derivative-of-expm, verified algebraically),
`spm_meanm` (Karcher mean), `spm_compute_avg_mat`, `spm_pairwise`,
`spm_series_align`, `spm_noise_estimate`, `spm_rice_mixture`.
OldNorm: `spm_write_sn` (incl. its det<0 sign fix — the reference the root
`spm_deformations` lacks), `spm_normalise`, `spm_get_orig_coord`.
OldSeg: `spm_prep2sn`, `spm_preproc_write` (one harmless no-op line in
`clean_gwc`).
Spatial: `spm_dctdst` (DCT-II/DST-I/DST-II pairs round-tripped for even and
odd N), `spm_scope` (topup-style Jacobian-modulated cost/gradient/Hessian),
`spm_slice2vol_estimate`/`_reslice` (chain rule and push/pull conventions),
`spm_est_vdm_from_phase` (phase→Hz→voxel-shift dimensionally consistent; its
docstring's "mm" is a documentation nit).
DARTEL/Shoot spot-check: integration directions `[1 0]`/`[0 1]` used
consistently and documented; `spm_shoot_update` multinomial gradient/Hessian
standard.
