#!/usr/bin/env python3
"""Pearson correlation of two AFNI datasets within a mask (via 3dmaskdump)."""
import subprocess, sys, numpy as np
mask, a, b = sys.argv[1:4]
def dump(ds):
    out = subprocess.run(['3dmaskdump', '-mask', mask, '-noijk', '-quiet', ds], capture_output=True, text=True).stdout
    return np.array(out.split(), float)
x, y = dump(a), dump(b)
print("%.4f" % np.corrcoef(x, y)[0, 1])
