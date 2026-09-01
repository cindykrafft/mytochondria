#!/usr/bin/env python3
"""MACS p-value convention: p = P(X > t) [all versions since 1.4] vs the
textbook discrete p-value P(X >= t). Quantify the gap where peak calls
are decided, and the achieved size of a Poisson test at the -log10 p = 5
default cutoff under both conventions."""
import numpy as np
from scipy.stats import poisson

print("counts near the calling margin (default -log10 p cutoff = 5):")
print(f"{'lambda':>7} {'t*':>4} | {'P(X>=t*)':>10} {'P(X>t*)':>10} {'ratio':>6} | -log10: {'>=':>6} {'>':>6}")
for lam in [0.5, 1, 2, 5, 10, 25]:
    # t* = smallest t whose MACS pscore (>) exceeds 5
    t = 1
    while -np.log10(poisson.sf(t, lam)) < 5: t += 1
    p_ge = poisson.sf(t-1, lam)   # P(X >= t)
    p_gt = poisson.sf(t, lam)     # P(X > t)  == MACS
    print(f"{lam:>7} {t:>4} | {p_ge:>10.3e} {p_gt:>10.3e} {p_ge/p_gt:>6.2f} | {-np.log10(p_ge):>6.2f} {-np.log10(p_gt):>6.2f}")

print("\nachieved per-position size at nominal p<=1e-5 (Poisson null, exact):")
print(f"{'lambda':>7} | {'size with >= (proper)':>21} {'size with > (MACS)':>19} {'inflation':>9}")
for lam in [0.5, 1, 2, 5, 10, 25]:
    # rejection region under each convention
    t_ge = 0
    while poisson.sf(t_ge-1, lam) > 1e-5: t_ge += 1   # smallest t with P(X>=t)<=1e-5
    t_gt = 0
    while poisson.sf(t_gt, lam) > 1e-5: t_gt += 1     # smallest t with P(X>t)<=1e-5
    size_ge = poisson.sf(t_ge-1, lam)                  # P(reject) = P(X>=t_ge)
    size_gt = poisson.sf(t_gt-1, lam)                  # MACS rejects when T=t and P(X>t)<=1e-5 -> region X>=t_gt
    print(f"{lam:>7} | {size_ge:>21.3e} {size_gt:>19.3e} {size_gt/size_ge:>8.1f}x")
