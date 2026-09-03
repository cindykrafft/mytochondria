#!/usr/bin/env python3
"""Reproduction for freesurfer/freesurfer#1358: mri_convert --out_orientation
shifts the output grid by one voxel on every flipped axis.

Usage: repro.py <dir-with-mri_convert-and-mri_info> [workdir]
Builds the reporter's 256^3 volume of ones with an identity affine (nibabel),
reorients it RAS->LIA with --out_orientation and with --reorder, converts the
first back to RAS, and reports c_ras and the number of zero voxels in each.
Also runs the test.sh scenario on a synthetic conformed (LIA) volume.
"""
import os, subprocess, sys
import numpy as np
import nibabel as nib

bindir = os.path.abspath(sys.argv[1])
work = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else "repro_work")
os.makedirs(work, exist_ok=True)
os.chdir(work)
env = dict(os.environ, PATH=bindir + os.pathsep + os.environ["PATH"])

def run(*args):
    r = subprocess.run(args, env=env, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout, r.stderr)
        raise SystemExit("command failed: " + " ".join(args))
    return r.stdout

def cras(fn):
    img = nib.load(fn)
    return tuple(np.round(img.header["c_ras"] if "c_ras" in img.header else
                          img.header.get_zooms(), 4))

def report(fn):
    img = nib.load(fn)
    data = np.asarray(img.dataobj)
    hdr = img.header
    c = hdr.get_vox2ras() @ np.array([hdr["dims"][0] / 2.0, hdr["dims"][1] / 2.0, hdr["dims"][2] / 2.0, 1.0])
    nz = int((data == 0).sum())
    print("%-18s c_ras=(%g, %g, %g)  zeros=%d (%.2f%%)" %
          (fn, c[0], c[1], c[2], nz, 100.0 * nz / data.size))
    return nz

print("== reporter's scenario: ones.mgz (256^3, identity affine) ==")
nib.save(nib.MGHImage(np.ones((256,) * 3, dtype=np.uint8), np.eye(4)), "ones.mgz")
run("mri_convert", "--in_orientation", "RAS", "--out_orientation", "LIA", "ones.mgz", "ones_LIA.mgz")
run("mri_convert", "--reorder", "-1", "3", "-2", "ones.mgz", "ones_reorder.mgz")
run("mri_convert", "--in_orientation", "LIA", "--out_orientation", "RAS", "ones_LIA.mgz", "ones_RAS.mgz")
z = [report(f) for f in ("ones.mgz", "ones_reorder.mgz", "ones_LIA.mgz", "ones_RAS.mgz")]
print("mri_diff ones_LIA.mgz ones_reorder.mgz:",
      subprocess.run(["mri_diff", "ones_LIA.mgz", "ones_reorder.mgz"], env=env, capture_output=True, text=True).stdout.strip().replace("\n", " | ") or "identical")
print("mri_diff ones.mgz ones_RAS.mgz:",
      subprocess.run(["mri_diff", "ones.mgz", "ones_RAS.mgz"], env=env, capture_output=True, text=True).stdout.strip().replace("\n", " | ") or "identical")

print("\n== test.sh scenario on a synthetic conformed LIA volume (random uchar) ==")
rng = np.random.default_rng(1358)
data = rng.integers(1, 255, size=(256,) * 3, dtype=np.uint8)
aff = np.array([[-1, 0, 0, 127.3], [0, 0, 1, -128.7], [0, -1, 0, 129.1], [0, 0, 0, 1.0]])
nib.save(nib.MGHImage(data, aff), "conf.mgz")
run("mri_convert", "conf.mgz", "reorient-ras.mgz", "--out_orientation", "RAS", "-rt", "nearest")
run("mri_convert", "conf.mgz", "reorder-ras.mgz", "--reorder", "-1", "-3", "2")
run("mri_convert", "reorient-ras.mgz", "roundtrip-lia.mgz", "--out_orientation", "LIA", "-rt", "nearest")
for a, b in (("reorient-ras.mgz", "reorder-ras.mgz"), ("roundtrip-lia.mgz", "conf.mgz")):
    r = subprocess.run(["mri_diff", a, b], env=env, capture_output=True, text=True)
    print("mri_diff %s %s -> exit %d: %s" % (a, b, r.returncode, r.stdout.strip().replace("\n", " | ") or "identical"))
print("RESULT:", "BUG (zeros introduced / volumes differ)" if (z[2] or z[3]) else "OK")
