# Component review: C/MEX sources (`src/`)

Scope: everything in `src/` except `src/external` — B-splines, joint
histogram, GMM, the shoot/dartel/diffeo family, volume sampling/slicing,
connected components, local maxima, resels, MRF, render/project, utilities.
Method: full read; boundary index arithmetic traced on small concrete
volumes; the byte-swap defect reproduced with a compiled harness.

## Confirmed

1. **`spm_getdata.c:64-84`** — `getuint64`/`getint64` byte-swappers use a
   `double y` temporary: `return(y)` performs a *numeric* conversion of the
   byte-swapped double rather than a bit reinterpretation (every other
   swapper uses a same-type temporary). Reproduced compiled: input
   `0x0102030405060708` returns 0 vs the correct 578437695752307201. Reached
   via `spm_vol_utils`' `GET()` for byte-swapped INT64/UINT64 NIfTI: silently
   garbage voxel values. **Medium** (rare datatype+endianness combination).
2. **`spm_get_lm.c:61-92`** — all 26 neighbour tests use
   `(i=get_index(...))>0` where `>=0` is required: `get_index` returns exactly
   0 for voxel (1,1,1), so a neighbour at linear index 0 can never disqualify
   a candidate. A voxel adjacent to the volume's first voxel is reported as a
   local maximum even when (1,1,1) is larger. The centre-voxel guards
   correctly use `<0`. **Low-medium.**
3. **`spm_unlink.c:30`** — trailing-space trim loop uses an unsigned
   `mwIndex` with `k>=0` (always true): empty or all-space filenames
   underflow to SIZE_MAX and read out of bounds. **Low.**

## Plausible

4. `spm_slice_vol.c:38` and `spm_render_vol.c:224` — matrix size check uses
   `&&` for `||`: a 4×3 matrix passes and 16 doubles are read from a
   12-element array (malformed caller input only).
5. `spm_bwlabel.c:294-296`, `spm_global.c:14,47` — element counts in plain
   `int`: volumes above ~2.1e9 voxels overflow into undersized allocations /
   wrong loop bounds.

## Verified correct

`shoot_boundary` circulant/Neumann wrapping; difference-operator neighbour
offsets in `shoot_regularisers`/`shoot_optimN`/`shoot_diffeo3d`; the OpenMP
`reduction`/`collapse` regions (per-row offsets recomputed, scratch private)
and the `pushpull` atomic scatter; `spm_project`'s MNI bounds checks; the
B-spline weight/pole tables in `bsplines.c` (Unser); `spm_brainwarp`'s
misnamed `MYMAX` (deliberately computes min(ratio,1) — intended df scaling).
