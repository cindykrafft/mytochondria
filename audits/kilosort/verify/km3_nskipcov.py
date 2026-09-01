#!/usr/bin/env python3
"""KM3: Kilosort 2/2.5/3 whitening-covariance normalizer off-by-one.

preProcess/get_whitening_matrix.m accumulates the channel covariance over
batches 1, 1+nSkipCov, 1+2*nSkipCov, ... <= Nbatch:

    while ibatch<=Nbatch
        ...
        CC = CC + (datr' * datr)/NT;
        ibatch = ibatch + ops.nSkipCov;
    end
    CC = CC / ceil((Nbatch-1)/ops.nSkipCov);

The loop visits floor((Nbatch-1)/nSkipCov) + 1 batches, but the normalizer is
ceil((Nbatch-1)/nSkipCov).  Whenever nSkipCov divides (Nbatch-1) exactly, the
two differ by one and the covariance is inflated by (m+1)/m, where
m = (Nbatch-1)/nSkipCov.  Because Wrot ~ C^(-1/2), the whitened data are then
uniformly scaled by sqrt(m/(m+1)), and every threshold expressed in whitened
units (ops.Th, ops.spkTh) becomes effectively sqrt((m+1)/m) harder.

With the default nSkipCov = 25 this hits 1 in 25 possible batch counts, and
the size of the effect depends on recording length:

    Nbatch =   26 (~57 s @30 kHz):  covariance x2.00 -> thresholds x1.414
    Nbatch =   51 (~1.9 min):       covariance x1.50 -> thresholds x1.225
    Nbatch =  251 (~9.5 min):       covariance x1.10 -> thresholds x1.049
    Nbatch = 1651 (~62 min):        covariance x1.02 -> thresholds x1.008

Same code in KS2 (v2.0.2), KS2.5 (v2.5.2), KS3 (v3.0.2), all at
preProcess/get_whitening_matrix.m line 48.  Kilosort 4 fixed it by counting
iterations (kilosort/preprocessing.py::get_whitening_matrix, `k`).

This script reproduces the arithmetic and demonstrates the scale effect on a
synthetic covariance.
"""
import math

import numpy as np


def matlab_count(nbatch, nskip):
    """Number of batches the MATLAB while-loop actually accumulates."""
    count, ibatch = 0, 1
    while ibatch <= nbatch:
        count += 1
        ibatch += nskip
    return count


nskip = 25
print(" Nbatch  accumulated  normalizer  covariance-inflation  threshold-factor")
for nbatch in (26, 51, 251, 1651, 1650, 1652):
    acc = matlab_count(nbatch, nskip)
    norm = math.ceil((nbatch - 1) / nskip)
    infl = acc / norm
    print("%7d  %11d  %10d  %19.3f  %16.3f"
          % (nbatch, acc, norm, infl, infl ** 0.5))

# Scale effect on the whitening transform: W ~ C^{-1/2}
rng = np.random.default_rng(0)
A = rng.standard_normal((32, 32))
C = A @ A.T + 32 * np.eye(32)          # a valid covariance
for infl in (2.0, 1.5, 1.1):
    E, D, _ = np.linalg.svd(C)
    W_true = (E / np.sqrt(D)) @ E.T
    E, D, _ = np.linalg.svd(infl * C)
    W_bad = (E / np.sqrt(D)) @ E.T
    ratio = np.linalg.norm(W_true) / np.linalg.norm(W_bad)
    print("covariance x%.1f -> whitened amplitudes shrink by x%.4f "
          "(expected %.4f)" % (infl, ratio, infl ** 0.5))
