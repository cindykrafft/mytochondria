#!/usr/bin/env python3
"""Reproduction for afni/afni issue #73.

3dvolreg exits 0 after "nifti_image_write_hdr_img: NBL does not match nim"
and leaves an empty output file, when its input NIfTI carries an AFNI
extension whose TAXIS_NUMS no longer matches the NIfTI header (the header
says N-1 volumes, the stale extension says N).  Such files are produced by
any tool that drops volumes with nibabel/nilearn while preserving header
extensions (MRIQC's reorient_and_discard step in the report).

Needs numpy and the AFNI programs 3dcalc, 3dinfo, 3dvolreg on PATH
(or in $AFNI_BIN).  No external data.
"""
import os
import struct
import subprocess
import sys

import numpy as np

NX, NY, NZ, NT = 12, 12, 6, 8


def write_nifti1(path, data, dx=3.0):
    """Minimal NIfTI-1 writer (int16, no extension) for a 4D array x,y,z,t."""
    nx, ny, nz, nt = data.shape
    hdr = bytearray(352)                       # 348-byte header + 4-byte ext flag
    struct.pack_into("<i", hdr, 0, 348)
    struct.pack_into("<8h", hdr, 40, 4, nx, ny, nz, nt, 1, 1, 1)
    struct.pack_into("<h", hdr, 70, 4)         # datatype = INT16
    struct.pack_into("<h", hdr, 72, 16)        # bitpix
    struct.pack_into("<8f", hdr, 76, 1.0, dx, dx, dx, 2.0, 1, 1, 1)
    struct.pack_into("<f", hdr, 108, 352.0)    # vox_offset
    struct.pack_into("<f", hdr, 112, 1.0)      # scl_slope
    struct.pack_into("<B", hdr, 123, 10)       # xyzt_units: mm | sec
    struct.pack_into("<h", hdr, 252, 1)        # qform_code = SCANNER_ANAT
    struct.pack_into("<h", hdr, 254, 1)        # sform_code
    struct.pack_into("<6f", hdr, 256, 0, 0, 0, 0, 0, 0)  # quatern b,c,d, qoffsets
    struct.pack_into("<4f", hdr, 280, dx, 0, 0, 0)
    struct.pack_into("<4f", hdr, 296, 0, dx, 0, 0)
    struct.pack_into("<4f", hdr, 312, 0, 0, dx, 0)
    hdr[344:348] = b"n+1\0"
    with open(path, "wb") as f:
        f.write(hdr)
        f.write(np.asfortranarray(data.astype("<i2")).tobytes(order="F"))


def drop_last_volume_keep_extensions(src, dst):
    """Rewrite src as dst with dim[4] -= 1 and the last volume's data removed,
    leaving the header extension block (348..vox_offset) untouched -- exactly
    what nibabel does when a script slices a 4D image and saves it."""
    raw = bytearray(open(src, "rb").read())
    dim = list(struct.unpack_from("<8h", raw, 40))
    bitpix = struct.unpack_from("<h", raw, 72)[0]
    vox_offset = int(struct.unpack_from("<f", raw, 108)[0])
    volbytes = dim[1] * dim[2] * dim[3] * bitpix // 8
    nt = dim[4]
    assert nt > 1
    dim[4] = nt - 1
    struct.pack_into("<8h", raw, 40, *dim)
    out = raw[:vox_offset] + raw[vox_offset:vox_offset + volbytes * (nt - 1)]
    open(dst, "wb").write(bytes(out))


def run(cmd, **kw):
    print("$ " + " ".join(cmd))
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True, **kw)
    print(p.stdout.rstrip())
    print("[exit status %d]" % p.returncode)
    return p


def main():
    abin = os.environ.get("AFNI_BIN")
    if abin:
        os.environ["PATH"] = abin + os.pathsep + os.environ["PATH"]
    work = sys.argv[1] if len(sys.argv) > 1 else "repro_work"
    os.makedirs(work, exist_ok=True)
    os.chdir(work)
    for f in ("synth.nii", "withext.nii", "dropped.nii", "vr.nii.gz",
              "vr.1D", "withext_vr.nii.gz"):
        if os.path.exists(f):
            os.remove(f)

    rng = np.random.default_rng(0)
    data = (1000 + 100 * rng.standard_normal((NX, NY, NZ, NT))).round()
    write_nifti1("synth.nii", data)

    # 1. let AFNI write the file, so it carries an AFNI extension
    run(["3dcalc", "-a", "synth.nii", "-expr", "a", "-prefix", "withext.nii"])

    # 2. drop the last volume, keeping the (now stale) AFNI extension
    drop_last_volume_keep_extensions("withext.nii", "dropped.nii")

    # 3. what does AFNI think the file is?
    p = run(["3dinfo", "-ntimes", "-nv", "dropped.nii"])
    print("(-ntimes is the length of the time axis, -nv the number of"
          " sub-bricks; both should be %d)" % (NT - 1))

    # 4. 3dvolreg on the file, NIfTI output
    p = run(["3dvolreg", "-prefix", "vr.nii.gz", "-1Dfile", "vr.1D",
             "-base", "0", "dropped.nii"])
    size = os.path.getsize("vr.nii.gz") if os.path.exists("vr.nii.gz") else -1
    print("vr.nii.gz size: %d bytes (-1 = missing)" % size)
    print("RESULT: exit=%d output_bytes=%d" % (p.returncode, size))


if __name__ == "__main__":
    main()
