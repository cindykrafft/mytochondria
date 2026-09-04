# suite2p #1079 — z-registration (list of reference images) crashes with `nonrigid=False`

Issue: [MouseLand/suite2p#1079](https://github.com/MouseLand/suite2p/issues/1079),
"Two bugs related to zcorr processing", opened 2024-01-18 by liadJB against v0.14.2,
labelled `bug`, 0 comments, **assigned to carsen-stringer** (see `assigned.txt`).
The reporter registers with `register.registration_wrapper(..., refImg=refImgs)` where
`refImgs` is a list (one image per z-plane) to obtain `ops["zpos_registration"]`, and
reports (1) a crash whenever `nonrigid=False` and (2) a crash on a two-channel recording
with `nonrigid=True`.

Tree used: `main` @ 90be895 (= v1.1.0), cloned fresh at depth 1.

## Diagnosis

Part 1 reproduces on `main`, with a different traceback than the one reported for
v0.14.2 (the registration code was rewritten for v1.0):

```
suite2p/registration/register.py:459, in shift_frames
    fr_torch = nonrigid.transform_data(fr_torch, blocks[2], blocks[1], blocks[0], ...
IndexError: list index out of range
```

- `register_frames` (`register.py:581-586`) calls `compute_filters_and_norm` with
  `block_size=None` when `nonrigid=False`; each reference then gets `maskMulNR = None`
  and `blocks = []`.
- For a single reference, `compute_shifts` (`register.py:383-412`) returns
  `ymax1, xmax1, cmax1 = None, None, None` in that case, and `shift_frames`
  (`register.py:445-459`) skips the nonrigid warp because `yoff1 is None`.
- For `nZ > 1` (`register.py:357-381`) `compute_shifts` unconditionally allocates six
  offset tensors, `shapes = [(n,), (n,), (n,), (n, nb), (n, nb), (n, nb)]` with `nb = 0`,
  and returns zero-width tensors for the nonrigid entries. `shift_frames` sees
  `yoff1 is not None`, calls `nonrigid.transform_data(fr_torch, blocks[2], ...)` on the
  empty block list, and raises.

Part 2 (two channels, `nonrigid=True`) runs on `main`: `shift_frames_and_write` receives
`blocks = refAndMasks[0][-3]` and the per-block offsets have the right shape
(`repro_wrapper.after.out`, and the same script on unmodified `main` passes the two
`nonrigid=True` cases).

## Fix (`0001-compute_shifts-return-None-nonrigid-offsets-for-rigi.patch`, branch `fix/issue-1079-zreg-rigid-only`)

In the `nZ > 1` branch of `compute_shifts`, build only the three rigid offset tensors
when the reference carries no nonrigid masks and return `None` for the nonrigid
entries, exactly as the `nZ == 1` branch does. Six changed lines in
`suite2p/registration/register.py`; no change when `nonrigid=True` or for
single-reference registration.

## Reproduction

`repro.py` registers a 6-frame 64x64 synthetic movie (`register.register_frames`, CPU)
against two reference images, with `nonrigid=True` and `nonrigid=False`.

Before (`repro.before.out`):
```
suite2p 1.1.0
nonrigid=True: OK, zest=[0, 0, 0, 0, 0, 0], cmax_all shape=(6, 2), nonrigid offsets=present
nonrigid=False: IndexError: list index out of range  [register.py:459: fr_torch = nonrigid.transform_data(fr_torch, blocks[2], blocks[1], blocks[0],]
```

After (`repro.after.out`):
```
suite2p 1.1.0
nonrigid=True: OK, zest=[0, 0, 0, 0, 0, 0], cmax_all shape=(6, 2), nonrigid offsets=present
nonrigid=False: OK, zest=[0, 0, 0, 0, 0, 0], cmax_all shape=(6, 2), nonrigid offsets=None
```

`repro_wrapper.py` is the reporter's call, `registration_wrapper` on `BinaryFile`
inputs with a two-image reference list, for one and two channels and `nonrigid` off/on.
Before the fix the two `nonrigid=False` rows fail with the same `IndexError`; after
(`repro_wrapper.after.out`) all four complete and return `zpos_registration`.

## Tests

New test `tests/test_registration.py::test_register_frames_with_reference_list_rigid_only`
(parametrised over `nonrigid`), in the style of the existing data-free unit tests in that
file. `pytest tests/test_registration.py`:

| | result |
|---|---|
| `main` + new test | 3 passed, 1 skipped (MPS), **1 failed** (`[False]`, `IndexError` at `register.py:459`) |
| branch | 4 passed, 1 skipped |

The regression/smoke tests under `tests/regression` and `tests/smoke` download data
from OSF and were not run (no egress from this session). Suite2p has no linter
configuration; `ruff check` (default rules) on the two touched files reports 20
findings on `main` and 20 on the branch, none in the changed lines.

The patch applies to `main` @ 90be895 with `git am`.

## Filing conventions read

`docs/developer_doc.md` (run `pytest tests/`; test data from OSF), `tests/instructions.md`,
`.github/ISSUE_TEMPLATE/bug_report.yml`. No CONTRIBUTING.md, no PR template, no changelog
file (releases are described on GitHub). Test added next to the existing unit tests in
`tests/test_registration.py`.

## Status: issue is assigned

The issue is assigned to the maintainer (carsen-stringer). Per the project rule, no PR is
opened for an assigned issue: `comment.md` is a diagnosis plus an offer of the branch,
`pr-body.md` is ready should the maintainer want the PR. Nothing has been filed or pushed.

## Other candidates considered

Of 40 open issues (all read; 3 are this account's), the ones that are user-reported bugs:

| issue | why not |
|---|---|
| #1208 reg_tif_chan2 tiffs written into `reg_tif/` (chan2 overwrites chan1) | reproduced on `main` (`register.py:974` passes `tif_root_align` instead of `tif_root_alt`; harness `repro_1208.py` + `repro_1208.before.out` here), but open PR #1261 (2026-08-05) already fixes it |
| #1211 nonrigid registration fails with one block along a dimension | open PR #1260 already addresses it (same author as #1261); #1251 is the same crash on v0.99rc0 |
| #1250 `force_sktiff` ignored in `tiff.ome_to_binary` | one-line cause confirmed (`tiff.py:323`), but open PR #1262 already addresses it |
| #1239 crash with computed bidiphase = -1 | fixed on `main`: v1.0.0.1 shifted the reference frames by `int(settings["bidiphase"])` (0, since the offset was being estimated) and its `bidiphase.shift` had no `< 0` guard, so any estimated nonzero offset raised the broadcast error; v1.1.0 uses the estimated value and guards both signs. A comment pointing to v1.1.0 would close it |
| #1252 "Array must not contain infs or NaNs" in detection | reporter feeds an old-style `default_ops()` dict to the v1.1 `run_s2p`; `diameter` reaches `roi_stats` as 0. Needs their data and an API-migration decision |
| #1109 `sbx_to_binary` frame count wrong with two channels | needs `.sbx` data; open PR #1242 refactors the sbx reader |
| #248 `look_one_level_down` ignores `bad_frames.npy` (2019) | where to look for the file across subfolders is a design decision |

The issue comments cannot be read from this session (only the body and the comment
count); #1079 has none.

## Caveats

- Environment: PyTorch could only be installed as the CUDA wheel (the CPU index is not
  reachable from this session) and was run on CPU with stub CUDA libraries; the changed
  code is device-independent tensor bookkeeping and the tests run on `device="cpu"`.
- Part 2 of the issue could not be reproduced on `main` with synthetic data; the
  reporter's v0.14.2 traceback (`upsample_block_shifts` reshape) points at code that no
  longer exists.
- Alternative the maintainers might prefer: make `shift_frames` treat a zero-width
  `yoff1` as "no nonrigid shifts" instead of changing `compute_shifts`. The patch keeps
  the two `compute_shifts` branches consistent, which seemed the smaller change.
