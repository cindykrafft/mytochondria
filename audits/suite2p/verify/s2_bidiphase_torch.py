#!/usr/bin/env python3
"""S2: bidiphase.shift corrupts odd scan lines when given a torch tensor.

suite2p/registration/bidiphase.py::shift moves the odd scan lines by
`bidiphase` pixels with an in-place assignment whose source and destination
slices overlap:

    frames[:, 1::2, bidiphase:] = frames[:, 1::2, :-bidiphase]

numpy makes a temporary copy for overlapping assignments; torch.Tensor.copy_
does not, so the assignment reads pixels it has already overwritten. Since
v1.0.0.1 (Feb 2026) register_frames and shift_frames_and_write pass torch
tensors to bidi.shift, so with bidirectional-phase correction enabled every
frame's odd lines are corrupted instead of shifted, while the reference image
(still shifted through the numpy path in registration_wrapper) is correct.

Run inside a venv with suite2p >= 1.0 (verified on 1.1.0, torch 2.13 CPU):

    python s2_bidiphase_torch.py

Expected output (suite2p 1.1.0):

    unit: numpy odd row after shift 3: [8, 9, 10, 8, 9, 10, 11, 12]
    unit: torch odd row after shift 3: [8, 9, 10, 8, 9, 10, 8, 9]  | matches numpy: False
    end-to-end register_frames(bidiphase=3, CPU): odd lines correct? False
      fraction of odd-line pixels wrong: 34.4%
"""
import logging
import numpy as np
import torch
logging.disable(logging.CRITICAL)
import suite2p
from suite2p.registration import register, bidiphase as bidi

print("suite2p", suite2p.version, "| torch", torch.__version__)
fr = np.arange(2 * 4 * 8, dtype=np.int16).reshape(2, 4, 8)
ref = bidi.shift(fr.copy(), 3)
out = bidi.shift(torch.from_numpy(fr.copy()), 3)
print("unit: numpy odd row after shift 3:", ref[0, 1].tolist())
print("unit: torch odd row after shift 3:", out[0, 1].tolist(),
      " | matches numpy:", np.array_equal(out.numpy(), ref))

rng = np.random.default_rng(0)
Ly, Lx, nfr, b = 64, 96, 6, 3
refimg = (rng.random((Ly, Lx)) * 1000).astype(np.int16)
mov = np.tile(refimg, (nfr, 1, 1)).copy()          # identical frames -> zero motion
expected = bidi.shift(mov.copy(), b)               # numpy semantics = intended result
got = mov.copy()
register.register_frames(got, refimg, batch_size=3, bidiphase=b, norm_frames=False,
                         nonrigid=False, maxregshift=0.1, device=torch.device("cpu"))
ok = np.array_equal(got[:, 1::2, b:], expected[:, 1::2, b:])
print("end-to-end register_frames(bidiphase=3, CPU): odd lines correct?", ok)
print("  fraction of odd-line pixels wrong: %.1f%%"
      % (100 * (got[:, 1::2, b:] != expected[:, 1::2, b:]).mean()))
