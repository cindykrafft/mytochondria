#!/usr/bin/env python3
"""Synthetic volumes for checking the 3dReHo builds against each other and against the
Python port in ../reproductions/reho_tie_sim.py. Writes white/band-passed Gaussian 4D
NIfTIs (12x12x12 voxels, 148 TRs at TR 2 s, shared signal giving true W ~ 0.62) at
several SDs, plus variants with 12 zero-filled 'censored' volumes."""
import numpy as np, nibabel as nib, sys
out = sys.argv[1] if len(sys.argv) > 1 else '.'
rng = np.random.default_rng(3); N = 148; TR = 2.0; nx = ny = nz = 12
def bp(x):
    f = np.fft.rfftfreq(N, TR); X = np.fft.rfft(x, axis=-1); X[..., (f < 0.01) | (f > 0.1)] = 0
    y = np.fft.irfft(X, n=N, axis=-1); return y / y.std(axis=-1, keepdims=True)
c = rng.standard_normal(N)
base = np.sqrt(0.6) * c + np.sqrt(0.4) * rng.standard_normal((nx, ny, nz, N))
aff = np.diag([3, 3, 3, 1.])
for lab, x in [('white', base / base.std(-1, keepdims=True)), ('bp', bp(base))]:
    for sd in [0.2, 0.35, 0.5, 1.0]:
        d = (sd * x).astype(np.float32); nib.save(nib.Nifti1Image(d, aff), f'{out}/{lab}_sd{sd:.2f}.nii.gz')
        dc = d.copy(); dc[..., rng.choice(N, 12, replace=False)] = 0
        nib.save(nib.Nifti1Image(dc, aff), f'{out}/{lab}_sd{sd:.2f}_cen.nii.gz')
nib.save(nib.Nifti1Image(np.ones((nx, ny, nz), np.uint8), aff), f'{out}/mask.nii.gz')
