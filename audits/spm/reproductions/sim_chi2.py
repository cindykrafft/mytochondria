import numpy as np
from scipy import ndimage, stats
from numpy import log, pi, sqrt, exp
from ec_check import spm_ECdensity
from impact_check import spm_ECdensity_Xfixed

rng = np.random.default_rng(42)

# 2D smooth Gaussian component fields via FFT smoothing, periodic (torus -> only R2 term matters, no boundary)
n = 256
FWHM = 8.0
sigma = FWHM/sqrt(8*log(2))

# Build Gaussian smoothing kernel in Fourier space (periodic => torus, EC has no boundary terms)
kx = np.fft.fftfreq(n)*n
KX, KY = np.meshgrid(kx, kx, indexing='ij')
H = exp(-2*(pi**2)*(sigma**2)*((KX/n)**2 + (KY/n)**2))
# variance normalization computed empirically below

def smooth_field():
    w = rng.standard_normal((n, n))
    f = np.fft.ifft2(np.fft.fft2(w)*H).real
    return f

# normalize to unit variance
tmp = np.stack([smooth_field() for _ in range(20)])
sd = tmp.std()

def euler_char(B):
    """EC of union of closed pixels (2D), torus topology (wrap)."""
    P = B.sum()
    E = (B & np.roll(B, -1, 0)).sum() + (B & np.roll(B, -1, 1)).sum()
    F = (B & np.roll(B, -1, 0) & np.roll(B, -1, 1) & np.roll(np.roll(B, -1, 0), -1, 1)).sum()
    return P - E + F

v = 4
ts = [12.0, 16.0, 20.0]
nsim = 300
ECs = np.zeros((nsim, len(ts)))
for s in range(nsim):
    X = sum(smooth_field()**2 for _ in range(v))/sd**2
    for j, t in enumerate(ts):
        ECs[s, j] = euler_char(X >= t)

emp = ECs.mean(0)
se = ECs.std(0)/sqrt(nsim)

# Predictions: torus, resels R2 = (n/FWHM)^2, R1=0, R0=0 (no boundary on torus; R0 for torus is 0)
R2 = (n/FWHM)**2
for j, t in enumerate(ts):
    rho_buggy = spm_ECdensity('X', t, [1, v])[2, 0]
    rho_fixed = spm_ECdensity_Xfixed(t, v)[2, 0]
    print(f"t={t}: empirical E[EC]={emp[j]:.3f} +/- {se[j]:.3f} | "
          f"SPM(buggy)={R2*rho_buggy:.3f} | corrected={R2*rho_fixed:.3f}")
