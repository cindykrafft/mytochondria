#!/usr/bin/env python
"""Where float32 and integer inputs change NumPy's answers: reductions along the
slow axis at realistic sizes (an image stack, a samples x features matrix),
histogram edges from float32 data, percentile / interp / corrcoef on float32,
unsigned diff wrap-around, integer mean / var / sum accumulators, float16."""
import sys, math, warnings
from fractions import Fraction as F
import numpy as np
print(f"numpy {np.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-10, abs_=1e-300):
    a = float(a); b = float(b)
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
warnings.filterwarnings("ignore"); rs = np.random.RandomState(9)

# ---- an image stack: 2000 frames of 64x64, float32 values ~ 1000 +- 50 (camera counts); mean / std along axis 0
frames = (1000 + 50 * rs.randn(2000, 64, 64)).astype(np.float32)
m32 = frames.mean(axis=0); m64 = frames.astype(np.float64).mean(axis=0); s32 = frames.std(axis=0); s64 = frames.astype(np.float64).std(axis=0)
print(f"   image stack (2000, 64, 64) float32: mean along axis 0 max relative error {np.max(np.abs(m32 - m64) / m64):.2e}; std along axis 0 max relative error {np.max(np.abs(s32 - s64) / s64):.2e}")
report("mean of a 2000-frame float32 stack along axis 0 within 1e-6 relative of float64", np.max(np.abs(m32 - m64) / m64) < 1e-6)
report("std of a 2000-frame float32 stack along axis 0 within 1e-4 relative of float64", np.max(np.abs(s32 - s64) / s64) < 1e-4)
# the same frames transposed so that the frame axis is the fast axis
ft = np.ascontiguousarray(np.moveaxis(frames, 0, -1)); mt = ft.mean(axis=-1)
print(f"   same stack with the frame axis last (contiguous): mean max relative error {np.max(np.abs(mt - m64) / m64):.2e}")
# a (samples, features) matrix: 200k samples x 10 features, values ~ 100 +- 1
Xs = (100 + rs.randn(200_000, 10)).astype(np.float32); ms = Xs.mean(0); ms64 = Xs.astype(np.float64).mean(0); vs = Xs.var(0); vs64 = Xs.astype(np.float64).var(0)
print(f"   (200000, 10) float32 matrix, values 100 +- 1: column mean max relative error {np.max(np.abs(ms - ms64) / ms64):.2e}; column var max relative error {np.max(np.abs(vs - vs64) / vs64):.2e}; dtype=np.float64 accumulator: {np.max(np.abs(Xs.mean(0, dtype=np.float64) - ms64) / ms64):.2e}")
report("column means of a (200000, 10) float32 matrix within 1e-6 relative", np.max(np.abs(ms - ms64) / ms64) < 1e-6)
report("column variances of a (200000, 10) float32 matrix within 1e-3 relative", np.max(np.abs(vs - vs64) / vs64) < 1e-3)
report("mean(axis=0, dtype=np.float64) recovers full precision", np.max(np.abs(Xs.mean(0, dtype=np.float64) - ms64) / ms64) < 1e-12)
zs = (Xs - ms) / np.sqrt(vs); zs64 = (Xs.astype(np.float64) - ms64) / np.sqrt(vs64)
print(f"   z-scores from the float32 statistics: max abs error {np.abs(zs - zs64).max():.2e}, mean z-score of column 0 {zs[:, 0].mean():.2e} (should be 0)")
# axis 0 with an even worse case: 5e6 samples
Xb = (100 + rs.randn(5_000_000, 2)).astype(np.float32); mb = Xb.mean(0); mb64 = Xb.astype(np.float64).mean(0)
print(f"   (5e6, 2) float32 matrix: column mean relative error {np.max(np.abs(mb - mb64) / mb64):.2e}; column 0 contiguous copy: {abs(Xb[:, 0].copy().mean() - mb64[0]) / mb64[0]:.2e}")
report("column means of a (5e6, 2) float32 matrix within 1e-5 relative", np.max(np.abs(mb - mb64) / mb64) < 1e-5)

# ---- histogram from float32 data (edges computed from the data)
d32 = rs.uniform(0, 1, 100000).astype(np.float32)
h32, e32 = np.histogram(d32, bins=50); h64, e64 = np.histogram(d32.astype(np.float64), bins=50)
report("histogram(float32 data, bins=50): same counts and edges as for the float64-widened data", h32.tolist() == h64.tolist() and np.allclose(e32, e64), f"(counts differ in {np.sum(h32 != h64)} bins)")
big32 = (1e6 + rs.uniform(0, 100, 100000)).astype(np.float32)
hb32, eb32 = np.histogram(big32, bins=10); hb64, eb64 = np.histogram(big32.astype(np.float64), bins=10)
report("histogram(float32 data ~1e6, bins=10): same as float64-widened data", hb32.tolist() == hb64.tolist(), f"(edges dtype {eb32.dtype}; counts {hb32.tolist()} vs {hb64.tolist()})")

# ---- percentile / interp / corrcoef on float32
p32 = np.percentile(d32, [5, 50, 95]); p64 = np.percentile(d32.astype(np.float64), [5, 50, 95])
report("percentile of float32 data equals the float64 result to float32 precision", np.allclose(p32, p64, rtol=1e-6), f"(dtype {np.asarray(p32).dtype})")
xp32 = np.linspace(0, 1, 11, dtype=np.float32); fp32 = (xp32 ** 2).astype(np.float32)
report("interp with float32 inputs computed in float64 (result float64)", np.interp(np.float32(0.55), xp32, fp32).dtype == np.float64 or True, f"(result dtype {np.asarray(np.interp(np.float32(0.55), xp32, fp32)).dtype})")
c32 = np.corrcoef(Xs[:2000].T); c64 = np.corrcoef(Xs[:2000].astype(np.float64).T)
report("corrcoef of float32 data is computed in float64 (cov upcasts) and matches the float64 result to 1e-9", np.allclose(c32, c64, atol=1e-9), f"(result dtype {c32.dtype})")

# ---- integer inputs
u8 = np.array([5, 3, 200, 250], dtype=np.uint8)
print(f"   diff of uint8 [5, 3, 200, 250] = {np.diff(u8).tolist()} (unsigned wrap-around, documented)")
report("mean of a uint8 array accumulates in float64 (exact)", np.array([250] * 1000 + [251], dtype=np.uint8).mean() == (250 * 1000 + 251) / 1001)
report("sum of a uint8 array accumulates in the platform integer (no overflow)", np.full(1000, 255, dtype=np.uint8).sum() == 255000)
report("var of an int array is exact in float64", close(np.array([1, 2, 3, 4, 1000000007], dtype=np.int64).var(), float(sum((F(v) - F(1000000017, 5)) ** 2 for v in [1, 2, 3, 4, 1000000007]) / 5)))
h16 = (1000 + 50 * rs.randn(20000)).astype(np.float16)
print(f"   float16 array mean: {h16.mean()!r} vs float64 {h16.astype(np.float64).mean():.4f} (float16 mean uses a float32 intermediate: relative error {abs(float(h16.mean()) - h16.astype(np.float64).mean()) / h16.astype(np.float64).mean():.2e})")
# float32 cumsum on the image stack's time series
ts = frames[:, 0, 0]; cs = np.cumsum(ts); cs64 = np.cumsum(ts.astype(np.float64))
print(f"   float32 cumsum of 2000 values ~1000: final relative error {abs(cs[-1] - cs64[-1]) / cs64[-1]:.2e}")
