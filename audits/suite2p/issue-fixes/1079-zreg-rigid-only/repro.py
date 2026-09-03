"""Reproduction for MouseLand/suite2p#1079 (part 1): registering against a list of
reference images (z-registration, ops["zpos_registration"]) crashes when
nonrigid=False.  Synthetic data, CPU, numpy arrays.

Run with PYTHONPATH pointing at the suite2p tree under test.
"""
import sys, traceback
import numpy as np
import torch
import suite2p
from suite2p.registration import register

rng = np.random.default_rng(0)
n_frames, Ly, Lx = 6, 64, 64
mov = rng.normal(1000, 50, (n_frames, Ly, Lx)).astype(np.int16)
mov[:, 10:20, 10:20] += 2000
refs = [mov[0].copy(), np.roll(mov[0], 5, axis=0).copy()]   # two "z-planes"

print("suite2p", suite2p.version)
for nonrigid in (True, False):
    frames = mov.copy()
    try:
        out = register.register_frames(frames, refs, nonrigid=nonrigid, block_size=[32, 32],
                                       batch_size=3, device=torch.device("cpu"))
        ymax, xmax, cmax, ymax1, xmax1, cmax1, zest, cmax_all = out[3]
        print(f"nonrigid={nonrigid}: OK, zest={zest.tolist()}, cmax_all shape={cmax_all.shape}, "
              f"nonrigid offsets={'present' if ymax1 is not None else 'None'}")
    except Exception as e:
        tb = traceback.extract_tb(sys.exc_info()[2])[-1]
        print(f"nonrigid={nonrigid}: {type(e).__name__}: {e}  [{tb.filename.split('/')[-1]}:{tb.lineno}: {tb.line}]")
