# afni/afni #73 — `3dvolreg` exits 0 after "NBL does not match nim" and leaves an empty file

_Issue-fix kit, 2026-09-03, against `afni/afni` master @ `c3fde703`
(Merge pull request #971). This PR answers a **user-reported issue** that has been
open since 2018; it is not an item from the project's own backlog (the ten open
`cindykrafft` issues/PRs on the repository are the project's, and this kit does not add to
them)._

## The issue

**[#73](https://github.com/afni/afni/issues/73)** — *3dvolreg incorrect exit code and
"ERROR: nifti_image_write_hdr_img: NBL does not match nim"* — reported 2018-02-22 by
`chrisgorgo` (MRIQC), 3 comments (not readable from this session), **no assignee**
(the `assignee`/`assignees` fields of the search result are null).

Reporter's claim, from the body: running `3dvolreg -prefix …_volreg.nii.gz` on an EPI
that MRIQC's `reorient_and_discard` step had produced, AFNI printed
`** WARNING: NIfTI file … dimensions altered since AFNI extension was added`, then
`** ERROR: nifti_image_write_hdr_img: NBL does not match nim`, exited with status **0**,
and left a **0-byte** `_volreg.nii.gz`. The reporter's own `3dinfo` on the input shows
`Number of time steps = 204` next to `For info on all 203 sub-bricks`.

## Diagnosis (file:line on `c3fde703`)

The input file had been sliced by nibabel, which carries NIfTI header extensions over
unchanged. Its AFNI extension therefore still describes the original 204 volumes while
the NIfTI header says 203.

1. `src/thd_niftiread.c:850-871` (`THD_nifti_process_afni_ext`): compares the header
   dims with the extension's `NIfTI_nums`, prints the "dimensions altered" warning
   when they differ — and then applies the stale attributes anyway
   (`THD_dblkatr_from_niml` + `THD_datablock_apply_atr`).
2. `src/thd_initdblk.c:1123-1173` (`THD_datablock_apply_atr`): builds `dset->taxis`
   from the extension's `TAXIS_NUMS`, so `taxis->ntt = 204`, while `dblk->nvals`
   stays at the header's 203 (`thd_niftiread.c:614-616`). From here on
   `DSET_NUM_TIMES(dset) != DSET_NVALS(dset)` — exactly the `3dinfo` pair the reporter
   quoted (`3dinfo -ntimes` vs `-nv` shows it directly).
3. `src/thd_niftiwrite.c:104-105, 460, 474`: on output, `nbl.nbricks = DSET_NVALS`
   (203) but `nim->nt = DSET_NUM_TIMES` (204); `nifti1_io.c:5761`
   `nifti_NBL_matches_nim` rejects the pair with "NBL does not match nim". The file has
   already been opened, hence the 0-byte output.
4. `src/3dvolreg.c:1305` (and 1314, 1319, 1324): `DSET_write(new_dset)` is called
   without looking at its return value, so the failure is silent and the program exits 0.

HEAD/BRIK datasets cannot get into this state (the reader in `thd_dsetdblk.c` sets
`ntt` and `nvals` from the same attributes); only NIfTI files with a stale extension can.

## The fix (branch `fix/issue-73-nifti-stale-taxis`, `0001-*.patch`)

- `src/thd_initdblk.c`: after the time axis is built from `TAXIS_NUMS`, if `ntt` differs
  from the number of sub-bricks actually present, warn and set
  `taxis->ntt = dblk->nvals`. The NIfTI header is authoritative for how many volumes
  exist; the extension's other attributes (labels, history, …) are applied as before.
- `src/3dvolreg.c`: check the return value of `DSET_write` for the output dataset and
  the three `-savedisp` datasets, `ERROR_exit` on failure (the idiom used in
  `3dExchange.c:273`), so a failed write is never a silent success.
- `tests/scripts/test_3dvolreg.py` (new; the suite had no 3dvolreg test): synthesises a
  12×12×6×8 int16 NIfTI with nibabel, has `3dcalc` rewrite it so it carries an AFNI
  extension, drops the last volume with nibabel (extension kept), then asserts
  `3dinfo -ntimes == -nv == 7`, that `3dvolreg` succeeds (`tools.run_cmd` raises on
  non-zero exit) and that the NIfTI output has 7 volumes. `data_paths = {}`, so it needs
  no `afni_ci_test_data` download.

Diff: 3 files, +105/−4 (`3dvolreg.c` +11/−4, `thd_initdblk.c` +16, test +78).

## Reproduction (`repro.py`, numpy only, no nibabel needed)

Builds the same file by hand (NIfTI-1 header via `struct`; the last volume is removed
while the byte range 348..`vox_offset` — the extension — is left untouched) and runs
`3dinfo` and `3dvolreg`.

**Before** (`repro.before.out`, master binaries):

```
$ 3dinfo -ntimes -nv dropped.nii
** WARNING: NIfTI file …/dropped.nii dimensions altered since AFNI extension was added
8	7
$ 3dvolreg -prefix vr.nii.gz -1Dfile vr.1D -base 0 dropped.nii
…
** ERROR: nifti_image_write_engine: NBL does not match nim
[exit status 0]
vr.nii.gz size: 0 bytes
RESULT: exit=0 output_bytes=0
```

**After** (`repro.after.out`, fixed binaries):

```
$ 3dinfo -ntimes -nv dropped.nii
** WARNING: NIfTI file …/dropped.nii dimensions altered since AFNI extension was added
*+ WARNING: AFNI extension of …/dropped.nii claims 8 time points, but the dataset has 7 sub-bricks; using 7
7	7
$ 3dvolreg -prefix vr.nii.gz -1Dfile vr.1D -base 0 dropped.nii
…
[exit status 0]
vr.nii.gz size: 10553 bytes
RESULT: exit=0 output_bytes=10553
```

**Regression check** (`regress_check.out`): on a healthy NIfTI (extension consistent)
and on a HEAD/BRIK copy of it, `3dvolreg` from master and from the branch produce
byte-identical motion parameters and byte-identical output bricks.

## Tests and linters

| | master binaries | fixed binaries |
|---|---|---|
| `pytest tests/scripts/test_3dvolreg.py` (Python 3.10) | **1 failed** — `assert 8 == 7` at the `3dinfo` check (`pytest.before.out`) | **1 passed** in 0.23 s (`pytest.after.out`) |

Run from `tests/` with the branch's `3dvolreg`, `3dinfo`, `3dcalc`, `libmri.so` on
`PATH`/`LD_LIBRARY_PATH`. Notes on running the suite here:

- The suite's `run_cmd` uses `asyncio.wait` on raw coroutines, which Python ≥ 3.11
  rejects (`TypeError: Passing coroutines is forbidden`); under Python 3.12 the test
  therefore errors *inside the harness* after the fix. The project's `environment.yml`
  pins Python 3.11, where this was already an error — worth a look by the maintainers
  but out of scope here. Python 3.10 (`uv venv --python /usr/bin/python3.10`; pytest
  9.1, numpy 2.x, nibabel 5.4, datalad 0.19.6, filelock, attrs, xvfbwrapper) runs the
  suite's default path.
- `conftest.py`'s session hook `datalad.install`s `afni_ci_test_data`; that call passes
  two positional arguments and fails with both datalad 1.6 and 0.19. A plain
  `git clone --depth 1 https://github.com/afni/afni_ci_test_data.git tests/afni_ci_test_data`
  with the remote renamed to `afni_ci_test_data` satisfies the hook. The new test needs
  none of that data.
- The suite's existing data-backed tests for the touched area (`test_3dinfo.py`,
  `test_3dcalc.py`) were **not** run: they need `afnipy` installed and git-annex for
  `datalad get`, neither of which is in this container. The regression check above
  stands in for them.
- Linters: `codespell` (the project's only CI workflow) is clean on the three changed
  files; the test module is `black`-formatted (`tests/scripts/test_python_style.py`
  runs `black --check` on every test module). No C formatter is configured upstream.

## Build notes

`cp Makefile.linux_ubuntu_24_64 Makefile; make AFNI_version.h; make libf2c.so;
make -j libmri.so; make 3dvolreg 3dinfo 3dcalc` (gcc 13.3, Ubuntu 24.04, after
`apt-get install libxt-dev libmotif-dev libxpm-dev libxi-dev libxmu-dev libgsl-dev
libglw1-mesa-dev`). Two things to know: `libmri.a` is not the target on this
platform (`MRI_SHARED=Linux` selects `libmri.so`), and the `f2c/` and `coxplot/`
sub-makes are not `-j`-safe (their `ar`/`ld` run before the objects exist), so build
`libf2c.so` and `libcoxplot.a` sequentially first. The project container's root
filesystem filled up during this session (shared with other sessions); the build was
done on `/dev/shm` (16 GB tmpfs) with `TMPDIR` pointed there.

## Other candidates considered

All 63 open issues were listed (`repo:afni/afni is:open`, one call), 53 of them by
users or maintainers. Read in full where it mattered:

- **#556** *Commit 23d5855 broke 3dRetinoPhase "delay" based estimation* — already
  fixed by the reporter's own PR #627 (merged 2026-02-24, `058f4bce` in
  `plug_delay_V2.h`); the issue was simply never closed. Nothing to do but close it.
- **#708** *afni_proc.py doesn't work without volreg* (20 comments) — addressed
  upstream in Oct 2024 (`-volreg_no_volreg`, `b4d3c483`; and `db_mod.py:8515` now
  falls back to "assuming on final grid" instead of the fatal error); open for
  discussion, not a bug to fix.
- **#875** *3dttest++ -Clustsim issue with .nii inputs* (5 unreadable comments) — some
  of the parallel `-randomsign` jobs failed to write their temp files; looks
  environmental (memory/disk under `-Clustsim`), needs real group data and long
  `3dClustSim` runs, and the comments probably already hold the answer.
- **#48** *Return error code when to3d quits due to -quit_on_err flag* (2016, no
  comments, unassigned) — a plausible small alternate of the same "wrong exit status"
  kind; not verified.
- **#105** *3dskullstrip testing writes a file to the wrong directory* — empty body;
  the fixed-name debug write it most likely refers to (`eyenodes.1D.dset`,
  `SUMA_3dSkullStrip.c:1432`) is compiled out (`#if 0`).
- **#763** *Bug with "-Allineate_opts" in align_epi_anat.py?* — no comments, not read
  in full; would need alignment data.

## Caveats

- The three comments on #73 could not be read from this session; the diagnosis rests on
  the body, which was sufficient (the reporter's `3dinfo` lines are the mismatch).
- An alternative the maintainers might prefer: skip `THD_datablock_apply_atr` entirely
  when `NIfTI_nums` disagrees with the header (`thd_niftiread.c:861`), discarding every
  attribute of a stale extension rather than only correcting the time axis. The chosen
  fix is narrower and keeps labels/history; either resolves #73.
- `3dvolreg` was the reported program, and the only one changed to check `DSET_write`;
  most AFNI programs share the ignore-the-status pattern. With the reader fix, the write
  no longer fails for this input in any program, so the exit-status change is a
  belt-and-braces addition rather than the fix.
- A single-volume slice of an AFNI-written 4D file (`nvals = 1`) now gets a time axis of
  length 1 instead of the stale length; AFNI already handles `ntt = 1` datasets (e.g.
  `3dTcat` of one volume).
- The reporter also asked about the exit code of `3dvolreg` generally; other error
  paths that `exit(0)` were not checked.
