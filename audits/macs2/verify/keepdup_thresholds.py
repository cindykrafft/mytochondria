#!/usr/bin/env python3
"""M1: with --keep-dup auto, MACS computes a control-specific binomial
threshold, logs it, then filters the CONTROL with the TREATMENT's
threshold (callpeak_cmd.py, all versions 2.1.x - current MACS3).
Table: what the thresholds actually are at realistic depths."""
from scipy.stats import binom

def macs_binom_inv(p_cum, n, p):
    # MACS binomial_cdf_inv(1-1e-5, N, 1/gsize): smallest k with CDF >= p_cum
    k = 0
    while binom.cdf(k, n, p) < p_cum: k += 1
    return k

gs = 2.7e9
depths = [5e6, 10e6, 20e6, 50e6, 100e6, 200e6, 500e6]
print("gsize=2.7e9 (hs), p=1e-5 binomial threshold (max allowed dups/position/strand):")
print(f"{'depth':>8} {'threshold':>9}")
th = {}
for n in depths:
    t = macs_binom_inv(1-1e-5, int(n), 1/gs)
    th[n] = t
    print(f"{n/1e6:>6.0f}M {t:>9}")
print("\nscenario: treatment 20M, control 100M, --keep-dup auto:")
print(f"  control filtered at treatment threshold {th[20e6]} instead of its own {th[100e6]}")
print("  -> positions in control with duplication between the two thresholds lose real reads")
print("  -> local lambda underestimated at high-coverage control loci -> anticonservative there")
