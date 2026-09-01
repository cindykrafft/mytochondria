#!/usr/bin/env python3
"""KL1: the refractory-CCG split veto in Kilosort 4.1.5+ is dead code.

`kilosort/swarmsplitter.py::check_CCG` contains

    if len(st1) == 0 or len(st2 == 0) or T == 0:
        return False, False

`st2 == 0` is a boolean *array*; `len(st2 == 0)` equals `len(st2)`, which is
truthy for every non-empty spike train.  The guard therefore fires on every
real input and `check_CCG` always returns (False, False).  Downstream,
`refractoriness()` (the "never split a refractory pair" veto used by
`swarmsplitter.split` via the `meta` spike-time channel) can then never
return 1, so Kilosort 4.1.5-4.1.7 decides splits purely on modularity and
bimodality.  Versions 4.0-4.1.4 applied the veto.

A second defect in the same line: the guard sits *after* the
`compute_CCG(st1, st2)` call, so the empty-array case it checks for has
already crashed inside `compute_CCG` (numba ValueError on `st.max()` of an
empty array) before the guard is reached.  Only the `T == 0` clause can ever
usefully trigger.

Run inside a venv with kilosort >= 4.1.5:

    python kl1_swarmsplitter_gate.py

Expected output (kilosort 4.1.7, torch CPU):

    n1,n2: 5948 5791
    swarmsplitter.check_CCG -> (False, False)
    swarmsplitter.refractoriness -> 0   (0 = "allow split")
    CCG_metrics: R12=0.0000 Q12=0.0000 Q00=31.1000
    pre-4.1.5 verdict: cross_refractory = True   ("never split")
    guard truthiness: len(st2==0) = 5791
    empty st2 -> ValueError inside compute_CCG (guard never reached)
"""
import numpy as np
from kilosort import swarmsplitter as sw
from kilosort import CCG

rng = np.random.default_rng(0)

# A single refractory neuron (3 ms refractory period, ~10 Hz, 20 min),
# artificially split in half: the classic oversplit scenario the veto
# was designed to catch.
T = 1200.0
isi = rng.exponential(0.1, 20000) + 0.003
st = np.cumsum(isi)
st = st[st < T]
mask = rng.random(st.size) < 0.5
st1, st2 = np.sort(st[mask]), np.sort(st[~mask])
print("n1,n2:", st1.size, st2.size)

print("swarmsplitter.check_CCG ->", sw.check_CCG(st1, st2))
print("swarmsplitter.refractoriness ->", sw.refractoriness(st1, st2),
      '  (0 = "allow split")')

K, Tt = CCG.compute_CCG(st1, st2)
R12, Q12, Q00 = CCG.CCG_metrics(st1, st2, K, Tt, nbins=500, tbin=1 / 1000)
print("CCG_metrics: R12=%.4f Q12=%.4f Q00=%.4f" % (R12, Q12, Q00))
print("pre-4.1.5 verdict: cross_refractory =",
      R12 < .25 and (Q12 < .05 or Q00 < .25), '  ("never split")')

print("guard truthiness: len(st2==0) =", len(st2 == 0))

try:
    sw.check_CCG(np.array([1.0, 2.0]), np.array([]))
    print("empty st2 -> no crash (unexpected)")
except ValueError as e:
    print("empty st2 -> ValueError inside compute_CCG (guard never reached):",
          str(e)[:60])
