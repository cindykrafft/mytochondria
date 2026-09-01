# Component review: image & file I/O

Scope: `@nifti`, `@file_array`, `@gifti` (main methods); `spm_vol*`,
`spm_read_vols`, `spm_write_vol`/`spm_create_vol`/`spm_write_plane`,
`spm_type`, `spm_file_merge`/`spm_file_split`, format converters (DICOM,
ECAT, MINC, PAR/REC, NetCDF), `spm_jsonwrite`, `spm_load`/`spm_save`,
`spm_BIDS`, `spm_check_filename`.
Method: full read against the NIfTI-1/2 and DICOM standards; quaternion
round-trips and scaling paths verified numerically.

## Confirmed

1. **`spm_file_merge.m:105`** — `sf = max(mx/dmx,-mn/dmn)`: `dmn` is the
   datatype *minimum* (negative), so the second term is negative for data with
   mn < 0 and the max always picks `mx/dmx`. Merging 3D→4D into int16 with a
   negative-dominant range underflows and clamps at −32768 (reproduced:
   −1000 reads back −100.003). The correct form is in `spm_write_vol.m:66`.
   **High** (SP7).
2. **`spm_read_vols.m:44`** — `Y(Y(:,:,:,im)==0) = NaN`: the partial logical
   mask is applied linearly to the *first* numel(mask) elements, so with
   NaN-capable and integer volumes interleaved the wrong volumes are masked
   (and the integer one never is). Silent, both volumes wrong. **High** (needs
   the two-argument masking form).
3. **`@gifti/private/gifti_read.m:160`** — `strncpm` typo (for `strncmp`),
   swallowed by the surrounding try/catch: byte-swapping is disabled for
   `Endian="BigEndian"` files on little-endian hosts — vertices/cdata read as
   garbage with no warning. The ExternalFileBinary branch never applies
   endianness at all. **High** for BE files (rare but standard-legal).
4. **`spm_mnc2nifti.m:165`** — `dcoff(:,:,1,i5,i5,i6)` should be `(…,i4,i5,i6)`:
   every frame of a dynamic MINC volume is written with frame 1's intercept
   whenever `image-min` varies across frames (typical for PET). **High.**
5. **`spm_dicom_convert.m:572, 162-172, 1626`** — PixelSpacing components
   paired with the wrong direction cosines (DICOM PS3.3 C.7.6.2: IOP(1:3) is
   the row direction; PixelSpacing = [between-rows, between-columns]); the
   spectroscopy path swaps them back with a "for some reason, pixel spacing
   needs to be swapped" comment. Wrong in-plane voxel sizes for non-square
   pixels → wrong geometry downstream. **High when triggered** (SP6).
6. **`spm_parrec2nifti.m:100-101`** — the slice-reorder permutation is applied
   on the wrong side (`dato(:,:,:,i) = dati(:,:,slice_order,i)`); wrong for any
   non-self-inverse (interleaved) stored order — the very case it exists for.
   **High when triggered.**
7. **`@file_array/private/file2mat.c` (~417-440)** — `map->dtype` (and
   `map.addr`) never initialised on the stack; an unrecognised dtype code
   (RGB24=128, FLOAT128, corrupted header) tests uninitialised memory and can
   call a garbage function pointer instead of erroring. **Moderate.**
8. **`spm_dicom_convert.m:141,200`** — mosaic datatype/descrip taken from
   `Headers{1}` inside the per-file loop; mixed-type batches written with the
   wrong datatype (integer clamping). **Moderate.**
9. **`@nifti/subsasgn.m:221`** — `obj.hdr.end_slice` typo (for `slice_end`):
   stale value written to disk plus a junk field. **Low.**
10. **`spm_check_filename.m:72-73`** — `fname` used before assignment (should
    be `V(i).fname`); the try swallows it, so the filename-recovery fallback
    is a silent no-op. **Low.**
11. **`@nifti/private/read_hdr_raw.m:127-146`** — only the first header
    extension is read; trailing-zero stripping corrupts binary extensions;
    `write_hdr_raw` never writes extensions (silently dropped). **Low.**
12. **`spm_save.m` (csv/tsv)** — quotes are doubled but the field is only
    wrapped when it contains the delimiter: values with `"` (or newlines)
    round-trip corrupted through `spm_load`. **Low.**

## Plausible

13. `spm_dicom_convert.m:1792-1798` — the multiframe variable-scaling path
    forces int16 with the DICOM slope, clamping unsigned values > 32767.
14. `@nifti/nifti.m:61` — `scl_slope==0` with `scl_inter≠0` not neutralised
    (NIfTI-1 says ignore both): constant image; `scl_slope=NaN` fails to load.
15. `spm_dicom_convert.m:536-541` — multi-frame-as-slices spacing built from
    SliceThickness, ignoring SpacingBetweenSlices (gap compression).
16. `spm_parrec2nifti.m` — signed int types for unsigned REC data (wrap
    above 32767) and a half-voxel origin offset (−dim/2 vs (dim+1)/2).
17. `@file_array/subsasgn.m:63-65` — int32 subscripts on the write path
    (read path is int64): >2³¹-element writes silently misplace data.
18. `spm_load.m` (dsvread) — collapses blank lines; a headerless file whose
    first row holds `n/a` is misread as a header; `str2double` turns tokens
    like `5i`/`Inf` into numbers.
19. `@nifti/private/decode_qform0.m:48` — `Z(Z<0)=1` discards the magnitude
    of out-of-spec negative pixdims.

## Verified correct

`M2Q`/`Q2M` quaternions exactly per NIfTI-1 (round-trip < 3e-12 over 20,000
rotations; qfac and Q(4)<0 handling per spec); the 0-based↔1-based voxel
conventions everywhere traced (decode/encode_qform0, sform read/write,
mayo2nifti1, mosaic and standard AnalyzeToDicom, diminfo slice bounds);
`@file_array` write scaling/NaN/clamp-then-round order and complex interleave;
`mat2file` contiguity logic; `file2mat` bounds and 1-bit plane padding;
`spm_vol_nifti` 4D/5D offsets; `spm_create_vol` minoff; `spm_write_vol`
scalefactor; `spm_file_split` round-trip; ECAT subheader/record offsets;
DICOM signed-pixel decoding, CSA1 item lengths, TM/DA/DS parsing.
