Title: (comment on #2610) on reading the +1 as a bandwidth term: the ratio of sums is bandwidth-free; the +1 then only halves it

<!-- Reply to schoffelen's comment of 2026-09-07 on PR #2610 ("almost ready to merge ... whether the original intention was a 'bandwidth'-parameter normalisation ... the sum should be taken for the denominator and numerator separately"). Numbers from audits/fieldtrip/verify/ft11d_psi_normalize_bandwidth.py. -->

I think the reading holds together, and it does make a difference which way the sums go. With the denominator summed separately, the `+1` per product adds up to the number of products in the window, so the option becomes

    Ψ_norm(f) = Im Σ_W conj(C)·C' / ( |W| + Σ_W |C||C'| )

which is bandwidth-free, whereas the per-term ratio still grows with `nbin` like the raw PSI. Measured on two channels with a 10-sample delay (`ft11d_psi_normalize_bandwidth.py` in the Mytochondria repository), value at the centre bin, ratio of `nbin=8` to `nbin=2`:

| definition | high coherence (|C| ≈ 0.98) | moderate (|C| ≈ 0.5) |
|---|---|---|
| raw sum (normalize='no') | 4.0 | 2.0 |
| per-term ratio (current branch) | 4.0 | 2.1 |
| ratio of sums with the +1 (your reading) | 1.0 | 0.5 |
| ratio of sums without the +1 | 1.0 | 0.6 |
| raw sum / number of products | 1.0 | 0.5 |

So separate sums are the right move if the option is meant to remove the bandwidth dependence. What the `+1` then contributes is only a change of scale: at full coherence the denominator is `2|W|` instead of `|W|`, so the result is half of the magnitude-weighted mean sine of the phase step; at low coherence `Σ|C||C'|` is small and the result is close to the raw sum divided by the number of products. Two cleaner forms give the same invariance with an interpretation attached:

- without the `+1`: `Im Σ conj(C)C' / Σ |C||C'|`, the magnitude-weighted mean sine of the phase step, bounded in [−1, 1];
- raw sum divided by the number of products: the mean imaginary product, i.e. the PSI per bin.

I have no evidence for what the 2010 author meant, so this is a design choice rather than a bug report. Happy to implement whichever you pick on this branch, or leave the option as it is on the branch and do it as a follow-up so this PR can merge.
