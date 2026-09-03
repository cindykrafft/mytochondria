"""Exact references for the HWE exact test (Wigginton 2005) and the 2x2 Fisher
test, in rational arithmetic (fractions.Fraction) so that the tail definition
"sum of P(table) over tables with P <= P(observed)" is decided exactly, ties
included.  mid-p: P(table) < P(obs) tables plus half of the tied mass."""
from fractions import Fraction
from math import comb, log
import functools

@functools.lru_cache(maxsize=None)
def hwe_dist(n, rare):
    """Probability of each heterozygote count given n genotypes and `rare`
    copies of the rarer allele. Returns dict hets -> Fraction."""
    out = {}
    for h in range(rare % 2, rare + 1, 2):
        homr = (rare - h) // 2
        homc = n - h - homr
        if homr < 0 or homc < 0:
            continue
        # 2^h n! rare! (2n-rare)! / (homr! h! homc! (2n)!)
        # use combinatorial form: n!/(homr! h! homc!) * 2^h / C(2n, rare)
        num = Fraction(comb(n, h) * comb(n - h, homr) * 2 ** h, comb(2 * n, rare))
        out[h] = num
    return out

def hwe_p(hets, hom1, hom2, midp=False):
    n = hets + hom1 + hom2
    rare = 2 * min(hom1, hom2) + hets
    if n == 0:
        return Fraction(1, 2) if midp else Fraction(1)
    d = hwe_dist(n, rare)
    p_obs = d[hets]
    less = sum(p for p in d.values() if p < p_obs)
    tie = sum(p for p in d.values() if p == p_obs)
    return less + (tie / 2 if midp else tie)

def fisher_dist(m11, m12, m21, m22):
    r1, r2 = m11 + m12, m21 + m22
    c1 = m11 + m21
    n = r1 + r2
    out = {}
    lo, hi = max(0, c1 - r2), min(r1, c1)
    for a in range(lo, hi + 1):
        out[a] = Fraction(comb(r1, a) * comb(r2, c1 - a), comb(n, c1))
    return out

def fisher_p(m11, m12, m21, m22, midp=False):
    d = fisher_dist(m11, m12, m21, m22)
    p_obs = d[m11]
    less = sum(p for p in d.values() if p < p_obs)
    tie = sum(p for p in d.values() if p == p_obs)
    return less + (tie / 2 if midp else tie)
