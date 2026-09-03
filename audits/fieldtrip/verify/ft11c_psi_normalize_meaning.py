"""What ft_connectivity_psi's normalize='yes' computes, line-for-line port of phaseslope (master 2e14f72)."""
import numpy as np
rng = np.random.default_rng(3)
m, nbin = 20, 3
# synthetic coherency with a phase that increases with frequency (channel 1 leads) and magnitude in (0.2, 0.95)
mag = rng.uniform(0.2, 0.95, m); phase = np.cumsum(rng.uniform(0.05, 0.3, m))
C = mag * np.exp(1j * phase)

def phaseslope_ft(C, n, norm, fix_edge=False):
    x = C.astype(complex).copy(); m = len(x); y = np.zeros(m)
    x[:-1] = np.conj(x[:-1]) * x[1:]                      # products; x[-1] stays raw C(fmax)
    if fix_edge: x[-1] = 0
    if norm:
        coh = np.zeros(m)
        coh[:-1] = np.abs(x[:-1]) * np.abs(x[1:]) + 1      # computed AFTER x holds products
        if fix_edge: coh[-1] = 1
        for k in range(m):
            a, b = max(0, k - n), min(m, k + n + 1)
            with np.errstate(divide="ignore", invalid="ignore"):
                y[k] = np.imag(np.nansum(x[a:b] / coh[a:b]))
    else:
        for k in range(m):
            a, b = max(0, k - n), min(m, k + n + 1); y[k] = np.imag(np.nansum(x[a:b]))
    return y

def window_sum(v, n):
    m = len(v); return np.array([np.sum(v[max(0, k - n):min(m, k + n + 1)]) for k in range(m)])

prod = np.conj(C[:-1]) * C[1:]                             # the m-1 adjacent products
psi = window_sum(np.r_[np.imag(prod), 0], nbin)            # Nolte PSI: window sum of imag products
# candidate meanings of "normalize"
den_intended = np.abs(C[:-1]) * np.abs(C[1:])              # |C(f)||C(f+1)|  (what the FIXME says: "get the coherence")
phase_only = window_sum(np.r_[np.imag(prod / den_intended), 0], nbin)            # = sum sin(dphi): amplitude removed
intended_plus1 = window_sum(np.r_[np.imag(prod / (den_intended + 1)), 0], nbin)  # same with the +1
den_actual = np.r_[np.abs(prod[:-1]) * np.abs(prod[1:]), 0] + 1                  # what the code builds: |prod(f)||prod(f+1)| + 1
actual_port = window_sum(np.r_[np.imag(prod / den_actual), 0], nbin)

ft_yes = phaseslope_ft(C, nbin, True, fix_edge=True)       # shipped normalize='yes' with only the edge fix from PR 2610
ft_no = phaseslope_ft(C, nbin, False, fix_edge=True)
print("bins 1..%d (edge-fixed), nbin=%d" % (m, nbin))
print("max|ft normalize=no  - Nolte PSI|                       = %.2e" % np.max(np.abs(ft_no - psi)))
print("max|ft normalize=yes - port of what the code builds|   = %.2e" % np.max(np.abs(ft_yes - actual_port)))
print("max|ft normalize=yes - intended |C(f)||C(f+1)|+1|      = %.2e" % np.max(np.abs(ft_yes - intended_plus1)))
print("max|ft normalize=yes - phase-only sum sin(dphi)|       = %.2e" % np.max(np.abs(ft_yes - phase_only)))
print()
print("per-bin, bins 4..8: den_actual = |prod(f)||prod(f+1)|+1  vs  den_intended+1 = |C(f)||C(f+1)|+1")
for f in range(3, 8):
    print("  f=%2d |C|=%.2f |C(f+1)|=%.2f  den_actual=%.3f  den_intended+1=%.3f  den_intended=%.3f" % (f+1, mag[f], mag[f+1], den_actual[f], den_intended[f]+1, den_intended[f]))
# how much does the +1 and the wrong denominator matter: ratio of normalized to unnormalized PSI
print()
print("ratio normalize=yes / normalize=no, bins 4..17: min %.3f max %.3f (phase-only reference would give %.3f .. %.3f)" % (
    np.min(ft_yes[3:17] / ft_no[3:17]), np.max(ft_yes[3:17] / ft_no[3:17]), np.min(phase_only[3:17] / ft_no[3:17]), np.max(phase_only[3:17] / ft_no[3:17])))
# limiting behaviour
for s in (0.05, 0.5, 0.95):
    Cs = s * np.exp(1j * phase); a = phaseslope_ft(Cs, nbin, True, True); b = phaseslope_ft(Cs, nbin, False, True)
    print("constant |C|=%.2f: normalize=yes / no = %.4f  (1/(|C|^4+1) = %.4f; the intended 1/(|C|^2+1) = %.4f; pure phase would be 1/|C|^2 = %.4f)" % (s, a[8] / b[8], 1 / (s**4 + 1), 1 / (s**2 + 1), 1 / s**2))
