# Issue fix: `mri_convert --out_orientation` shifts the grid by one voxel on flipped axes (freesurfer/freesurfer#1358)

This kit answers a user-reported issue, not an audit finding: **[#1358 "`mri_convert` loses
information on image image reorientation"](https://github.com/freesurfer/freesurfer/issues/1358)**,
opened 2025-08-26 by dkuegler (FastSurfer developer), open, 2 comments (comment text is not
readable from this session; the body alone contains a complete synthetic reproduction), no
assignee and no labels (checked 2026-09-03 via the search API's `assignee`/`labels` fields, which
came back empty for all 18 open issues).

**Reporter's claim.** Reorienting a 256³ volume of ones with `--in_orientation RAS
--out_orientation LIA` gives a volume whose `c_ras` is (128,128,128) while `--reorder -1 3 -2`
gives (127,128,127); the reoriented volume contains 130,816 zeros (a full plane at index 0 on
each flipped axis), and converting it back to RAS does not restore the input. The reporter
attributes it to `c_ras` referring to voxel N/2 rather than the image center.

## Diagnosis (on `dev` at f1fa3c6, 2026-09-03)

Confirmed; the reporter's mechanism is exactly right.

- `mri_convert/mri_convert.cpp:2899` — the default output template is a copy of the input header
  (`MRIcopyHeader(mri, mri_template)`), including `c_ras`.
- `mri_convert/mri_convert.cpp:3053` — `--out_orientation` then calls
  `MRIorientationStringToDircos(mri_template, ...)`, which rewrites only the nine direction
  cosines; `--out_{i,j,k}_direction` (`:3033-3049`) does the same by hand. `c_ras` is left as is.
- `utils/mri.cpp:640-642` (`MRIxfmCRS2XYZ`) — `c_ras` is defined as the RAS coordinate of voxel
  `(W/2, H/2, D/2)`. For even dimensions that is half a voxel away from the geometric center of
  the field of view, which lies at `((W-1)/2, (H-1)/2, (D-1)/2)`.
- Consequence: keeping `c_ras` while flipping an axis moves the output grid by
  `2 × ½ voxel = 1 voxel` along that axis. On the reporter's volume the RAS output covers
  x ∈ [1, 256] instead of [0, 255]; voxel index 0 samples outside the input and `MRIresample`
  (`:3426`) fills it with 0. Converting back repeats the shift in the other direction, so the
  round trip loses one slice per flipped axis rather than restoring the input.
- `utils/mriio.cpp:11587-11600` (`MRIreorderVox2RAS`, used by `--reorder`) does it right: it maps
  a reversed axis through `width - 1`, i.e. it keeps the field of view fixed in RAS. That is why the
  reporter's `--reorder` image has `c_ras = 127` and no zeros.

## Fix (`0001-bf-mri_convert-out_orientation-keeps-the-field-of-vi.patch`, 42 + 11 lines)

In `mri_convert.cpp`, when `--out_orientation` or any `--out_{i,j,k}_direction` is given:
before the cosines are changed, compute the RAS position of the template's FOV center
`vox2ras · ((W-1)/2, (H-1)/2, (D-1)/2)`; after they are changed, set
`c_ras = FOVcenter + Mdc · D · (½, ½, ½)` with the new cosines. That is the same invariant
`MRIreorderVox2RAS` maintains. Nothing runs on any other path, and `--out_center` still overrides
afterwards. The change intentionally alters the output of the affected invocations by the
one-voxel shift being removed.

`mri_convert/test.sh` gains a check on the existing `indata/ref/rawavg-conform.ref.mgz`
(conformed, LIA): `--out_orientation RAS -rt nearest` must `compare_vol`-equal
`--reorder -1 -3 2`, and reorienting that result back to LIA must equal the reference.

## Reproduction (`repro.py`, `repro.before.out`, `repro.after.out`)

Built `utils`, `mri_convert`, `mri_info`, `mri_diff` from a fresh depth-1 clone of `dev`
(f1fa3c6) on Ubuntu 24.04, gcc 13.3, cmake 3.28, system ITK 5.3 (`libinsighttoolkit5-dev`),
`-DMINIMAL=ON -DBUILD_GUIS=OFF -DBUILD_FORTRAN=OFF -DWARNING_AS_ERROR=OFF`, plus
`build-x11shim.cmake` passed as `CMAKE_PROJECT_freesurfer_INCLUDE` (the in-tree
`cmake/FindX11.cmake` does not create the `X11::X11` target the system VTK 9.1 config references;
build-environment only, not part of the patch). The locally built binaries were run with the
in-tree developer license side door (`SURFER_SIDEDOOR`, `utils/chklc.cpp:125-130`) since no
license file is obtainable here. `repro.py` reproduces the reporter's scenario with nibabel and
then the `test.sh` scenario on a synthetic conformed LIA volume with random uchar data.

| check | before (f1fa3c6) | after (d555eea) |
|---|---|---|
| `c_ras` of `ones_LIA.mgz` (`--out_orientation LIA`) vs `ones_reorder.mgz` (`--reorder -1 3 -2`) | (128,128,128) vs (127,128,127) | (127,128,127) both |
| zeros in `ones_LIA.mgz` | 130,816 (0.78 %) | 0 |
| zeros in `ones_RAS.mgz` (LIA → RAS again) | 130,816 | 0 |
| `mri_diff ones_LIA.mgz ones_reorder.mgz` | geometry differs, row 1 col 4 by 1.0 | `diffcount 0` |
| `mri_diff ones.mgz ones_RAS.mgz` | 130,816 voxels differ | `diffcount 0` |
| test.sh scenario: `--out_orientation RAS -rt nearest` vs `--reorder -1 -3 2` | geometry differs by 1.0 | `diffcount 0` |
| test.sh scenario: round trip vs input | 130,816 voxels differ (max 254) | `diffcount 0` |

Unaffected invocations are unchanged (`regression.out`, `mri_diff` before vs after on the same
input): plain copy, `--conform`, `-vs 2 2 2`, `--out_center`, and `--out_orientation` combined
with `--out_center` all give `diffcount 0` with identical geometry. The two direction-changing
invocations differ by exactly the shift being fixed (`--out_orientation RAS -vs 2 2 2`: 2.0 mm =
one 2 mm voxel; `--out_i_direction 1 0 0` on an LIA volume: 1.0 mm).

## Tests and linter

- Project test for the touched program: `mri_convert/test.sh` cannot be executed here because
  `mri_convert/testdata.tar.gz` is a git-annex object (not in the clone). The two new
  `compare_vol` checks were run verbatim on a synthetic conformed volume instead: both fail
  before (`mri_diff` exit 104 and 106) and pass after (exit 0). The 12 pre-existing checks in the
  script are untouched and, per the regression table, `--conform` output is byte-for-byte the same
  in data and geometry.
- Build: `mri_convert.cpp` compiles with no new warnings (gcc 13.3, `-O2`).
- Formatter: the repo ships a Google-based `.clang-format`, but `mri_convert.cpp` has never been
  formatted with it (Allman braces throughout). `git clang-format --diff` on the hunk proposes only
  brace-style and line-wrap changes that would make the new block the one Google-style island in
  the file, so the patch follows the surrounding file's style instead; the two alignment
  double-spaces it flagged were removed.
- Commit message uses the `bf:` prefix required by `CONTRIBUTING.md`; there is no changelog file
  or PR template in the repository.

## Other candidates considered

Only 18 issues are open on the repository (9 of them this account's audit filings); the full
listing was read. Of the other nine:

- **#1452** `mri_normalize`: unbounded `HISTOalloc` after an unguarded division in
  `MRIapplyBiasCorrectionSameGeometry` (jrussell9000, 2026-08-15). Genuine crash with a crisp
  fix (bound `nbins` in `MRIhistogram`, guard the divisor), but the reporter only reproduced it
  on real data he cannot share and says his synthetic phantom may not reach the failing call;
  a fix without an executed reproduction would violate the brief. Good next target.
- **#1446** Python tools use `os.cpu_count()` instead of `len(os.sched_getaffinity(0))`
  (EricDeveaud, 2026-07-21). Real on SLURM, but it is a behavior/design change across ~15
  scripts (several vendored from nnUNet), not a wrong result; left to the maintainers.
- **#1394** `segmentHA_T2.sh` writes empty stats when `USE_T1=0` (dmartindeblas, 2025-11-12,
  3 comments, tentative fix in the body). Plausible shell bug, but it needs the MATLAB runtime
  hippocampal-subfield pipeline output to reproduce; not feasible here.
- #1458, #1456, #1450 are container/packaging environment problems; #1435 is a question;
  #1333 is a feature request.

Search notes: the semantic `search_issues` backend returns ~20 loosely matched items per query
with states mixed; the listing that worked was `repo:freesurfer/freesurfer is:open` (all 18 in
one page). All 16 open PRs were listed (`search_pull_requests`, `repo:freesurfer/freesurfer is:open`):
none references #1358 or `--out_orientation`; the only one touching `mri_convert` is #1413
(vector-field rotation, a feature), which this 42-line hunk should not conflict with.

## Caveats

- The maintainers may prefer to make `--out_orientation` a pure axis reordering (no
  interpolation) when the requested orientation is a permutation/flip of the input, which would
  also remove the trilinear blur on the reporter's path; this patch keeps the resampling design
  and only fixes the geometry, so `-rt nearest` is needed for bit-exactness in the test.
- The same half-voxel convention also means `-vs`/`--out_i_size` resampling keeps `c_ras` rather
  than the FOV center (a half-voxel shift of the field of view when the voxel size changes). That
  is a separate, long-standing behavior with its own downstream expectations and is deliberately
  not touched here; it is mentioned in the PR body as out of scope.
- Comments on #1358 could not be read; if a maintainer has already proposed a different
  convention there, the PR text should be adjusted before filing.
