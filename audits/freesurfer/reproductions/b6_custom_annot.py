#!/usr/bin/env python3
"""B6, the exposed path: a custom parcellation (Schaefer2018-200, as published
for fsaverage) mapped to an individual subject (bert) by nearest-neighbor on
the registration sphere -- the same mapping mri_surf2surf --sval-annot performs
-- then fed to the mris_anatomical_stats accumulation (validated exactly
against the real binary in b6_thickness.py).

Custom annots carry no cortex.label constraint (that relabeling lives inside
mris_ca_label -l, which never runs for atlas transfers), so parcels can and do
overhang the medial wall, where thickness is exactly 0.
"""
import numpy as np
import nibabel.freesurfer.io as fsio
from scipy.spatial import cKDTree

sub = "testdata/bert"
# fsaverage -> bert nearest-neighbor via spherical registration
fs_sph, _ = fsio.read_geometry("fsaverage/surf/lh.sphere.reg")
be_sph, _ = fsio.read_geometry(f"{sub}/surf/lh.sphere.reg")
fs_sph /= np.linalg.norm(fs_sph, axis=1, keepdims=True)
be_sph /= np.linalg.norm(be_sph, axis=1, keepdims=True)
lab_fs, ctab, names = fsio.read_annot("lh.Schaefer200.annot")
names = [n.decode() for n in names]
idx = cKDTree(fs_sph).query(be_sph, k=1)[1]
lab = lab_fs[idx]                      # bert-vertex parcel ids

thick = fsio.read_morph_data(f"{sub}/surf/lh.thickness")
cortex = fsio.read_label(f"{sub}/label/lh.cortex.label")
in_cortex = np.zeros(len(thick), bool); in_cortex[cortex] = True

rows = []
for i, name in enumerate(names):
    if i == 0:  # background/medial wall entry
        continue
    m = lab == i
    n = int(m.sum())
    if n == 0: continue
    t = thick[m]
    avg_shipped = t.mean()                       # the mris_anatomical_stats way
    mc = m & in_cortex
    avg_masked = thick[mc].mean() if mc.sum() else np.nan
    n_out = int((m & ~in_cortex).sum())
    n_zero = int((t < 1e-6).sum())
    rows.append((name.replace("7Networks_",""), n, n_out, n_zero,
                 avg_shipped, avg_masked, avg_masked - avg_shipped))

tot = len(rows)
affected = [r for r in rows if r[6] == r[6] and abs(r[6]) > 0.001]
print(f"parcels on lh: {tot} | parcels with any vertex outside cortex.label: "
      f"{sum(1 for r in rows if r[2] > 0)} | parcels with |bias| > 0.001 mm: {len(affected)}")
print(f"labeled vertices outside cortex.label: {sum(r[2] for r in rows)} "
      f"(of {sum(r[1] for r in rows)}); zero-thickness among labeled: {sum(r[3] for r in rows)}")
print()
print(f"{'parcel':34s} {'nvert':>6s} {'outside':>7s} {'zeros':>5s} {'shipped':>8s} {'masked':>8s} {'bias_mm':>8s}")
for r in sorted(rows, key=lambda r: r[6] if r[6] == r[6] else 0)[:15]:
    print(f"{r[0]:34s} {r[1]:6d} {r[2]:7d} {r[3]:5d} {r[4]:8.3f} {r[5]:8.3f} {r[6]:+8.3f}")
bias = [abs(r[6]) for r in affected]
if bias:
    print(f"\namong affected parcels: median |bias| = {np.median(bias):.3f} mm, "
          f"max = {max(bias):.3f} mm")
