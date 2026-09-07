"""What the candidate 'normalize' definitions of ft_connectivity_psi do, as a function of the
integration bandwidth (nbin) and of the coherence level.

Two channels, y2 = a delayed copy of the common signal (10 samples at 1000 Hz) plus noise;
coherency from ntrial FFTs. For the products p(f) = conj(C(f)) C(f+1), over a window W of
2*nbin+1 bins (fewer at the edges):

  A  raw          sum_W imag(p)                                   (normalize='no')
  B  per-term     sum_W imag(p / (|C(f)||C(f+1)| + 1))            (branch head 5e7e454)
  C  separate+1   imag(sum_W p) / sum_W (|C(f)||C(f+1)| + 1)      (maintainer's reading of the +1 as a bandwidth term)
  D  separate     imag(sum_W p) / sum_W |C(f)||C(f+1)|            (magnitude-weighted mean sine of the phase step)
  E  mean         sum_W imag(p) / |W|                             (raw divided by the number of products)

Printed: the value at the centre bin (250 Hz) for nbin = 2, 4, 8 at three noise levels, and the
ratio nbin=8 / nbin=2, which is 1 for a bandwidth-free quantity.
"""
import numpy as np
rng = np.random.default_rng(7)
fs, n, ntrial, lag = 1000, 1000, 200, 10

def coherency(noise):
    C = np.zeros(n // 2 + 1, complex); P1 = np.zeros(n // 2 + 1); P2 = np.zeros(n // 2 + 1)
    for _ in range(ntrial):
        x = rng.standard_normal(n + lag)
        y1 = x[:n] + noise * rng.standard_normal(n)
        y2 = x[lag:lag + n] + noise * rng.standard_normal(n)
        f1, f2 = np.fft.rfft(y1), np.fft.rfft(y2)
        C += f1 * np.conj(f2); P1 += abs(f1) ** 2; P2 += abs(f2) ** 2
    return C / np.sqrt(P1 * P2)

def psis(C, nbin, k):
    m = len(C); p = np.conj(C[:-1]) * C[1:]                      # products f -> f+1, m-1 of them
    lo, hi = max(0, k - nbin), min(m - 1, k + nbin)               # products indexed by f (window reaches bin hi)
    w = p[lo:hi]; mag = (abs(C[lo:hi]) * abs(C[lo + 1:hi + 1]))
    return dict(A=np.imag(w).sum(), B=np.imag(w / (mag + 1)).sum(), C=np.imag(w.sum()) / (mag + 1).sum(),
                D=np.imag(w.sum()) / mag.sum(), E=np.imag(w).sum() / len(w))

k = 250
for noise in (0.1, 1.0, 3.0):
    C = coherency(noise); s = abs(C[k - 8:k + 9]).mean()
    print(f"noise {noise}: mean |C| around bin {k} = {s:.3f}")
    rows = {nb: psis(C, nb, k) for nb in (2, 4, 8)}
    print("  nbin " + " ".join(f"{key:>9}" for key in "ABCDE"))
    for nb, r in rows.items(): print(f"  {nb:4d} " + " ".join(f"{r[key]:9.4f}" for key in "ABCDE"))
    print("  8/2  " + " ".join(f"{rows[8][key] / rows[2][key]:9.3f}" for key in "ABCDE"))
