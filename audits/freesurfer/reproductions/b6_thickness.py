#!/usr/bin/env python3
"""Numerical reproduction of B6 on FreeSurfer's own test subject (bert).

mris_anatomical_stats accumulates per-ROI thickness over every vertex whose
aparc annotation maps to the ROI (mris_anatomical_stats.cpp:839-848, filter is
only `marked >= 0`), never consulting ?h.cortex.label — while the same
program's global MeanThickness and the ROI GrayVol are cortex-masked.

Step 1 validates this reimplementation against the reference aparc table that
ships with the FreeSurfer test data (produced by the real binary with
`-cortex lh.cortex.label -a lh.aparc.annot`).
Step 2 recomputes ThickAvg restricted to cortex.label and reports the delta.
"""
import numpy as np, nibabel as nib
import nibabel.freesurfer.io as fsio

sub = "testdata/bert"
thick = fsio.read_morph_data(f"{sub}/surf/lh.thickness")
labels, ctab, names = fsio.read_annot(f"{sub}/label/lh.aparc.annot")
names = [n.decode() for n in names]
cortex = set(fsio.read_label(f"{sub}/label/lh.cortex.label").tolist())
nv = len(thick)
in_cortex = np.zeros(nv, bool); in_cortex[list(cortex)] = True

# reference table (real binary output)
ref = {}
for line in open("testdata/aparc.stats.ref.table"):
    if line.startswith("#") or not line.strip(): continue
    p = line.split()
    ref[p[0]] = dict(nvert=int(p[1]), thickavg=float(p[4]), thickstd=float(p[5]))

rows = []
for idx, name in enumerate(names):
    if name in ("unknown", "corpuscallosum"): continue   # skipped by name in the C code
    m = labels == idx
    n_all = int(m.sum())
    if n_all == 0: continue
    t_all = thick[m]
    # as-shipped: every annot-labeled vertex
    avg_all = t_all.mean()
    std_all = t_all.std(ddof=0)
    # cortex-masked alternative
    mc = m & in_cortex
    avg_masked = thick[mc].mean() if mc.sum() else np.nan
    n_out = int((m & ~in_cortex).sum())
    n_zero = int((t_all < 1e-6).sum())
    r = ref.get(name, {})
    rows.append((name, n_all, r.get("nvert"), avg_all, r.get("thickavg"),
                 std_all, r.get("thickstd"), n_out, n_zero,
                 avg_masked, avg_masked - avg_all))

print("STEP 1 - validation against the real binary's reference output:")
nv_ok = sum(1 for r in rows if r[2] is not None and r[1] == r[2])
ta_ok = sum(1 for r in rows if r[4] is not None and abs(r[3] - r[4]) <= 0.0005)
ts_ok = sum(1 for r in rows if r[6] is not None and abs(r[5] - r[6]) <= 0.0005)
print(f"  ROIs: {len(rows)} | NumVert exact: {nv_ok} | ThickAvg within 0.0005: {ta_ok} | ThickStd within 0.0005: {ts_ok}")
worst = max((abs(r[3]-r[4]), r[0]) for r in rows if r[4] is not None)
print(f"  worst ThickAvg deviation: {worst[0]:.4f} mm ({worst[1]})")

print("\nSTEP 2 - as-shipped vs cortex-masked ThickAvg (deltas > 0.005 mm):")
print(f"{'ROI':32s} {'nvert':>6s} {'outside':>7s} {'zeros':>5s} {'shipped':>8s} {'masked':>8s} {'delta_mm':>9s}")
tot_out = 0
for r in sorted(rows, key=lambda r: -abs(r[10] if r[10]==r[10] else 0)):
    name, n_all, _, avg_all, _, _, _, n_out, n_zero, avg_m, d = r
    tot_out += n_out
    if abs(d) > 0.005:
        print(f"{name:32s} {n_all:6d} {n_out:7d} {n_zero:5d} {avg_all:8.3f} {avg_m:8.3f} {d:+9.3f}")
print(f"\ntotal annot-labeled vertices outside cortex.label: {tot_out}")
