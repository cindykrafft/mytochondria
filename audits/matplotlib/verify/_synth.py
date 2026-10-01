"""Shared helpers for the Matplotlib harnesses. Every harness runs under whichever
interpreter is given:
    <venv>/bin/python m1_....py
and prints the installed versions first. Matplotlib is forced onto the Agg backend
(no display). Truths are independent: fractions.Fraction, closed forms, plain-Python
ports written from the documentation, or SciPy where installed (informational on the
older builds, which carry no SciPy)."""
import sys, math
import matplotlib
matplotlib.use("Agg")
import numpy as np

try:
    import scipy
    HAVE_SCIPY = True
except Exception:
    HAVE_SCIPY = False

def banner():
    extra = f"  scipy {scipy.__version__}" if HAVE_SCIPY else "  (no scipy)"
    print(f"matplotlib {matplotlib.__version__}  numpy {np.__version__}{extra}  python {sys.version.split()[0]}")

def mpl_version():
    return tuple(int(x) for x in matplotlib.__version__.split(".")[:2])

def report(label, ok, detail=""):
    print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))

def close(a, b, rel=1e-9, abs_=1e-12):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))

def allclose(a, b, rel=1e-9, abs_=1e-12):
    a = np.asarray(a, dtype=float); b = np.asarray(b, dtype=float)
    if a.shape != b.shape: return False
    return bool(np.all([close(x, y, rel, abs_) for x, y in zip(a.ravel(), b.ravel())]))

def maxdiff(a, b):
    a = np.asarray(a, dtype=float); b = np.asarray(b, dtype=float)
    return float(np.nanmax(np.abs(a - b))) if a.size else 0.0
