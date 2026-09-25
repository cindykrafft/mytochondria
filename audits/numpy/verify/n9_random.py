#!/usr/bin/env python
"""NumPy random, deeper pass (n3 covered the basic streams and one setting each of
choice / permutation / shuffle / multivariate_normal / binomial / normal /
exponential / gamma).  Every distribution method of Generator (default_rng) and of
the legacy RandomState, 400,000 draws at 2-5 parameter settings including the
edge regimes (tiny shapes, poisson(1e6), binomial(1e9, 0.3), p near 0 and 1,
non-integer negative_binomial n, hypergeometric extremes, zipf a near 1, vonmises
kappa 1e-9 / 0.01 / 1000 / 1e7, noncentral df < 1, logseries p near 1, weibull /
power a < 1, standard_t df 1 and 2 via quantiles, lognormal sigma 3), compared
with exact moments (mean z-test with the exact variance; variance z-test with the
exact fourth central moment, only where the 8th moment is finite) and with the
empirical CDF at exact quantiles (continuous) or exact CDF values (discrete);
support / integrality checks; dirichlet, multinomial, multivariate_hypergeometric
row constraints and exact marginals; documented boundary values and parameter
validation; Generator.integers (every dtype, full ranges, endpoint, errors,
broadcasting, chi-square uniformity with exact p-values) and the legacy randint /
random_integers / tomaxint; random(dtype, out) and the raw-to-double mapping;
choice (p tolerance, replace=False with p = successive weighted sampling with the
exact ordered-pair law, axis, shuffle=False, zero-p entries); shuffle /
permutation / permuted axis semantics and uniformity over all 24 permutations;
bytes; SeedSequence (C++ reference vectors, a pure-Python reimplementation,
spawn); the five bit generators against pure-Python reference implementations
(PCG64 XSL-RR, PCG64 DXSM, MT19937 (also CPython's own MT19937), Philox4x64-10,
SFC64), the reference CSV vectors shipped in numpy/random/tests/data, the
seeding chain SeedSequence -> state, advance / jumped (LCG jump-ahead in pure
Python; MT19937 2**128 jump through Berlekamp-Massey + x**(2**128) mod the
characteristic polynomial over GF(2)), state round trips, pickling, spawn, legacy
seeding (init_genrand / init_by_array, CPython random.seed cross-check), legacy
random_sample / gauss against CPython's res53 + the documented polar method, seed
type handling, stream identity across builds (RandomState frozen; Generator
compared with values recorded from numpy 2.4.6 and differences matched against
the release notes), hang checks in subprocesses, and the docstring examples.
Truths: mpmath at 30 digits, fractions.Fraction, closed forms, pure-Python
reference implementations, CPython's random module.  No scipy anywhere."""
import sys, os, math, warnings, itertools, time, json, hashlib, pickle, random as pyrandom, subprocess, csv, glob
from fractions import Fraction as F
import numpy as np
import mpmath as mp
mp.mp.dps = 30
V = tuple(int(x) for x in np.__version__.split('.')[:2])
NP2 = V >= (2, 0)
V3 = tuple(int(''.join(c for c in x if c.isdigit()) or 0) for x in (np.__version__.split('.') + ['0'])[:3])
def banner(): print(f"numpy {np.__version__}  mpmath {mp.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-10, abs_=1e-300):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
def mpclose(a, b, rel):
    a = mp.mpf(a); b = mp.mpf(b); return abs(a - b) <= rel * max(abs(a), abs(b), mp.mpf(10)**-300)
def raises(fn, exc):
    try: fn(); return False
    except exc: return True
    except Exception: return False
def exc_name(fn):
    try: fn(); return "no exception"
    except Exception as e: return f"{type(e).__name__}: {str(e)[:70]}"
ZMAX = 5.0
PMIN = 5.733e-7          # two-sided 5-sigma tail probability
N = 400_000
warnings.filterwarnings("ignore")
M32 = 0xFFFFFFFF; M64 = (1 << 64) - 1; M128 = (1 << 128) - 1

# ======================================================================
# stream digests (cross-build identity).  Recorded with numpy 2.4.6.
# ======================================================================
SEEDD = 20260925
def _dig(v):
    if isinstance(v, (bytes, bytearray)): b = bytes(v)
    else:
        a = np.asarray(v)
        if a.dtype.kind == 'f': b = a.astype(np.float64).tobytes()
        elif a.dtype.kind in 'iub': b = a.astype(np.int64).tobytes() if a.dtype != np.uint64 else a.tobytes()
        else: b = repr(a.tolist()).encode()
    return hashlib.sha1(b).hexdigest()[:16]
def _shuf(rng, x):
    x = np.array(x); rng.shuffle(x); return x
GEN_STREAMS = [
    ("random", lambda g: g.random(40)), ("random_f32", lambda g: g.random(40, dtype=np.float32)),
    ("standard_normal", lambda g: g.standard_normal(40)), ("standard_normal_f32", lambda g: g.standard_normal(40, dtype=np.float32)),
    ("standard_exponential", lambda g: g.standard_exponential(40)), ("standard_exponential_inv", lambda g: g.standard_exponential(40, method='inv')),
    ("standard_exponential_f32", lambda g: g.standard_exponential(40, dtype=np.float32)),
    ("standard_gamma_0.3", lambda g: g.standard_gamma(0.3, 40)), ("standard_gamma_3", lambda g: g.standard_gamma(3.0, 40)),
    ("standard_gamma_f32", lambda g: g.standard_gamma(3.0, 40, dtype=np.float32)),
    ("beta_small", lambda g: g.beta(0.3, 0.4, 40)), ("beta_big", lambda g: g.beta(3.0, 4.0, 40)),
    ("binomial_inv", lambda g: g.binomial(20, 0.2, 40)), ("binomial_btpe", lambda g: g.binomial(1000, 0.4, 40)), ("binomial_p_gt_half", lambda g: g.binomial(1000, 0.9, 40)),
    ("chisquare", lambda g: g.chisquare(3.5, 40)), ("dirichlet", lambda g: g.dirichlet([1.0, 2.0, 3.0], 10)),
    ("dirichlet_small", lambda g: g.dirichlet([0.05, 0.05, 0.05], 10)), ("exponential", lambda g: g.exponential(2.0, 40)),
    ("f", lambda g: g.f(3.0, 7.0, 40)), ("gamma", lambda g: g.gamma(2.5, 2.0, 40)),
    ("geometric_search", lambda g: g.geometric(0.5, 40)), ("geometric_inv", lambda g: g.geometric(0.1, 40)),
    ("gumbel", lambda g: g.gumbel(1.0, 2.0, 40)), ("hypergeometric_small", lambda g: g.hypergeometric(10, 20, 5, 40)),
    ("hypergeometric_hrua", lambda g: g.hypergeometric(500, 600, 400, 40)), ("laplace", lambda g: g.laplace(1.0, 2.0, 40)),
    ("logistic", lambda g: g.logistic(1.0, 2.0, 40)), ("lognormal", lambda g: g.lognormal(1.0, 0.5, 40)),
    ("logseries", lambda g: g.logseries(0.9, 40)), ("multinomial", lambda g: g.multinomial(20, [0.2, 0.3, 0.5], 10)),
    ("mvhg_marginals", lambda g: g.multivariate_hypergeometric([5, 10, 15], 12, 10)),
    ("mvhg_count", lambda g: g.multivariate_hypergeometric([5, 10, 15], 12, 10, method='count')),
    ("mvnormal_svd", lambda g: g.multivariate_normal([0, 1], [[2, 0.5], [0.5, 1]], 10)),
    ("mvnormal_cholesky", lambda g: g.multivariate_normal([0, 1], [[2, 0.5], [0.5, 1]], 10, method='cholesky')),
    ("negative_binomial", lambda g: g.negative_binomial(2.5, 0.3, 40)), ("noncentral_chisquare", lambda g: g.noncentral_chisquare(3.0, 2.0, 40)),
    ("noncentral_chisquare_df_lt_1", lambda g: g.noncentral_chisquare(0.5, 2.0, 40)), ("noncentral_f", lambda g: g.noncentral_f(3.0, 7.0, 2.0, 40)),
    ("normal", lambda g: g.normal(1.0, 2.0, 40)), ("pareto", lambda g: g.pareto(3.0, 40)),
    ("poisson_small", lambda g: g.poisson(3.0, 40)), ("poisson_ptrs", lambda g: g.poisson(300.0, 40)),
    ("power", lambda g: g.power(3.0, 40)), ("rayleigh", lambda g: g.rayleigh(2.0, 40)),
    ("standard_cauchy", lambda g: g.standard_cauchy(40)), ("standard_t", lambda g: g.standard_t(5.0, 40)),
    ("triangular", lambda g: g.triangular(0.0, 1.0, 3.0, 40)), ("uniform", lambda g: g.uniform(1.0, 3.0, 40)),
    ("vonmises", lambda g: g.vonmises(1.0, 4.0, 40)), ("vonmises_big_kappa", lambda g: g.vonmises(1.0, 1e7, 40)),
    ("wald", lambda g: g.wald(3.0, 2.0, 40)), ("wald_extreme", lambda g: g.wald(1e9, 2.25, 40)), ("weibull", lambda g: g.weibull(2.0, 40)),
    ("zipf", lambda g: g.zipf(2.5, 40)), ("zipf_near_1", lambda g: g.zipf(1.1, 40)),
    ("integers_int64", lambda g: g.integers(0, 1000, 40)), ("integers_int64_full", lambda g: g.integers(-2**63, 2**63, 40, dtype=np.int64)),
    ("integers_uint64_full", lambda g: g.integers(0, 2**64, 40, dtype=np.uint64)), ("integers_int32", lambda g: g.integers(-7, 1000, 40, dtype=np.int32)),
    ("integers_int16", lambda g: g.integers(0, 300, 40, dtype=np.int16)), ("integers_uint8", lambda g: g.integers(0, 200, 40, dtype=np.uint8)),
    ("integers_bool", lambda g: g.integers(0, 2, 40, dtype=bool)), ("integers_endpoint", lambda g: g.integers(0, 10, 40, endpoint=True)),
    ("integers_broadcast", lambda g: g.integers([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)),
    ("choice", lambda g: g.choice(100, 20)), ("choice_p", lambda g: g.choice(5, 20, p=[0.1, 0.2, 0.3, 0.2, 0.2])),
    ("choice_noreplace", lambda g: g.choice(100, 20, replace=False)), ("choice_noreplace_big", lambda g: g.choice(10**6, 20, replace=False)),
    ("choice_noreplace_p", lambda g: g.choice(10, 5, replace=False, p=np.arange(1, 11) / 55)),
    ("choice_noshuffle", lambda g: g.choice(100, 20, replace=False, shuffle=False)),
    ("shuffle", lambda g: _shuf(g, np.arange(30))), ("permutation", lambda g: g.permutation(30)),
    ("permuted", lambda g: g.permuted(np.arange(24).reshape(4, 6), axis=1)), ("bytes", lambda g: g.bytes(37)),
]
RS_STREAMS = [
    ("random_sample", lambda r: r.random_sample(40)), ("rand", lambda r: r.rand(40)), ("randn", lambda r: r.randn(41)),
    ("standard_normal", lambda r: r.standard_normal(40)), ("standard_exponential", lambda r: r.standard_exponential(40)),
    ("standard_gamma_0.3", lambda r: r.standard_gamma(0.3, 40)), ("standard_gamma_3", lambda r: r.standard_gamma(3.0, 40)),
    ("beta_small", lambda r: r.beta(0.3, 0.4, 40)), ("beta_big", lambda r: r.beta(3.0, 4.0, 40)),
    ("binomial_inv", lambda r: r.binomial(20, 0.2, 40)), ("binomial_btpe", lambda r: r.binomial(1000, 0.4, 40)),
    ("chisquare", lambda r: r.chisquare(3.5, 40)), ("dirichlet", lambda r: r.dirichlet([1.0, 2.0, 3.0], 10)),
    ("exponential", lambda r: r.exponential(2.0, 40)), ("f", lambda r: r.f(3.0, 7.0, 40)), ("gamma", lambda r: r.gamma(2.5, 2.0, 40)),
    ("geometric", lambda r: r.geometric(0.5, 40)), ("geometric_inv", lambda r: r.geometric(0.1, 40)),
    ("gumbel", lambda r: r.gumbel(1.0, 2.0, 40)), ("hypergeometric_small", lambda r: r.hypergeometric(10, 20, 5, 40)),
    ("hypergeometric_hrua", lambda r: r.hypergeometric(500, 600, 400, 40)), ("laplace", lambda r: r.laplace(1.0, 2.0, 40)),
    ("logistic", lambda r: r.logistic(1.0, 2.0, 40)), ("lognormal", lambda r: r.lognormal(1.0, 0.5, 40)),
    ("logseries", lambda r: r.logseries(0.9, 40)), ("multinomial", lambda r: r.multinomial(20, [0.2, 0.3, 0.5], 10)),
    ("multivariate_normal", lambda r: r.multivariate_normal([0, 1], [[2, 0.5], [0.5, 1]], 10)),
    ("negative_binomial", lambda r: r.negative_binomial(2.5, 0.3, 40)), ("noncentral_chisquare", lambda r: r.noncentral_chisquare(3.0, 2.0, 40)),
    ("noncentral_chisquare_df_lt_1", lambda r: r.noncentral_chisquare(0.5, 2.0, 40)), ("noncentral_f", lambda r: r.noncentral_f(3.0, 7.0, 2.0, 40)),
    ("normal", lambda r: r.normal(1.0, 2.0, 40)), ("pareto", lambda r: r.pareto(3.0, 40)),
    ("poisson_small", lambda r: r.poisson(3.0, 40)), ("poisson_ptrs", lambda r: r.poisson(300.0, 40)),
    ("power", lambda r: r.power(3.0, 40)), ("rayleigh", lambda r: r.rayleigh(2.0, 40)),
    ("standard_cauchy", lambda r: r.standard_cauchy(40)), ("standard_t", lambda r: r.standard_t(5.0, 40)),
    ("triangular", lambda r: r.triangular(0.0, 1.0, 3.0, 40)), ("uniform", lambda r: r.uniform(1.0, 3.0, 40)),
    ("vonmises", lambda r: r.vonmises(1.0, 4.0, 40)), ("wald", lambda r: r.wald(3.0, 2.0, 40)), ("weibull", lambda r: r.weibull(2.0, 40)),
    ("zipf", lambda r: r.zipf(2.5, 40)),
    ("randint", lambda r: r.randint(0, 1000, 40)), ("randint_int64_full", lambda r: r.randint(-2**63, 2**63, 40, dtype=np.int64)),
    ("randint_uint64_full", lambda r: r.randint(0, 2**64, 40, dtype=np.uint64)), ("randint_int32", lambda r: r.randint(-7, 1000, 40, dtype=np.int32)),
    ("randint_int16", lambda r: r.randint(0, 300, 40, dtype=np.int16)), ("randint_uint8", lambda r: r.randint(0, 200, 40, dtype=np.uint8)),
    ("randint_bool", lambda r: r.randint(0, 2, 40, dtype=bool)), ("random_integers", lambda r: r.random_integers(1, 6, 40)),
    ("tomaxint", lambda r: r.tomaxint(40)), ("choice", lambda r: r.choice(100, 20)), ("choice_p", lambda r: r.choice(5, 20, p=[0.1, 0.2, 0.3, 0.2, 0.2])),
    ("choice_noreplace", lambda r: r.choice(100, 20, replace=False)), ("choice_noreplace_p", lambda r: r.choice(10, 5, replace=False, p=np.arange(1, 11) / 55)),
    ("shuffle", lambda r: _shuf(r, np.arange(30))), ("permutation", lambda r: r.permutation(30)), ("bytes", lambda r: r.bytes(37)),
]
def stream_digests():
    out = {}
    for name, fn in GEN_STREAMS:
        try: out["G." + name] = _dig(fn(np.random.default_rng(SEEDD)))
        except Exception as e: out["G." + name] = f"raised {type(e).__name__}"
    for name, fn in RS_STREAMS:
        try: out["R." + name] = _dig(fn(np.random.RandomState(SEEDD)))
        except Exception as e: out["R." + name] = f"raised {type(e).__name__}"
    return out
if os.environ.get("N9_RECORD"):
    print(json.dumps(stream_digests(), indent=0, sort_keys=True)); sys.exit(0)

banner()
_seed = [1000]
def seed():
    _seed[0] += 1; return _seed[0]
def G(): return np.random.default_rng(seed())
def R(): return np.random.RandomState(seed() % 2**32)
def pval_two_sided_z(z): return float(mp.erfc(abs(mp.mpf(z)) / mp.sqrt(2)))
def chi2_sf(x, k): return float(mp.gammainc(mp.mpf(k) / 2, mp.mpf(x) / 2, mp.inf, regularized=True))
def poisson_tail_p(count, lam):
    """two-sided exact Poisson tail probability of an event count (used for rare events)"""
    lam = mp.mpf(lam)
    if lam == 0: return 1.0 if count == 0 else 0.0
    lo = mp.gammainc(count + 1, lam, mp.inf, regularized=True)            # P(C <= count)
    hi = 1 - (mp.gammainc(count, lam, mp.inf, regularized=True) if count > 0 else 0)   # P(C >= count)
    return float(min(1, 2 * min(lo, hi)))

# ======================================================================
# exact-moment machinery
# ======================================================================
def raw_to_central(m):
    m1, m2, m3, m4 = [mp.mpf(x) for x in m]
    return m1, m2 - m1**2, m4 - 4*m1*m3 + 6*m1**2*m2 - 3*m1**4
def chi2_raw(nu, r):
    """E[(chi^2_nu)^r] = 2^r Gamma(nu/2 + r) / Gamma(nu/2); r may be negative if nu/2 + r > 0"""
    nu = mp.mpf(nu); return mp.mpf(2)**r * mp.gamma(nu/2 + r) / mp.gamma(nu/2)
def poisson_weights(lam):
    """Poisson(lam) weights j = 0, 1, ... until negligible (1e-40) past the mode"""
    lam = mp.mpf(lam); w = [mp.exp(-lam)]; j = 0
    while True:
        j += 1; w.append(w[-1] * lam / j)
        if j > lam and w[-1] < mp.mpf(10)**-40: break
    return w
def ncchi2_raw(k, lam, r):
    w = poisson_weights(mp.mpf(lam) / 2)
    return sum(w[j] * chi2_raw(mp.mpf(k) + 2*j, r) for j in range(len(w)))
def ncchi2_cdf(k, lam, x):
    w = poisson_weights(mp.mpf(lam) / 2)
    return sum(w[j] * mp.gammainc((mp.mpf(k) + 2*j) / 2, 0, mp.mpf(x) / 2, regularized=True) for j in range(len(w)))
def ncf_cdf(d1, d2, lam, x):
    w = poisson_weights(mp.mpf(lam) / 2); d1 = mp.mpf(d1); d2 = mp.mpf(d2); x = mp.mpf(x)
    return sum(w[j] * mp.betainc(d1/2 + j, d2/2, 0, d1*x / (d1*x + d2), regularized=True) for j in range(len(w)))
def disc_moments(logpmf, lo, hi):
    """raw moments 1..4 and total mass over the integer support [lo, hi] (plain Python floats)"""
    s = [0.0] * 5
    for k in range(lo, hi + 1):
        p = math.exp(logpmf(k))
        s[0] += p; s[1] += p * k; s[2] += p * k**2; s[3] += p * k**3; s[4] += p * k**4
    return s

class Spec:
    def __init__(self, label, gen, rs, lo, hi, integer=False, mean=None, var=None, mu4=None, cdf=None, disc=False, lo_incl=True, hi_incl=True,
                 transform=None, note="", pts=None, rs_note=None):
        self.label = label; self.gen = gen; self.rs = rs; self.lo = lo; self.hi = hi; self.integer = integer
        self.mean = mean; self.var = var; self.mu4 = mu4; self.cdf = cdf; self.disc = disc
        self.lo_incl = lo_incl; self.hi_incl = hi_incl; self.transform = transform; self.note = note; self.pts = pts

def run_spec(sp):
    for api, fn in (("Generator", sp.gen), ("RandomState", sp.rs)):
        if fn is None: continue
        rng = G() if api == "Generator" else R()
        try:
            x = np.asarray(fn(rng, N))
        except Exception as e:
            report(f"{api}.{sp.label}", False, f"raised {type(e).__name__}: {e}"); continue
        x = x.astype(np.float64) if x.dtype != np.float64 else x
        det = []; ok = True
        flo = float(sp.lo); fhi = float(sp.hi)          # plain floats: comparing an array with an mpf is element-wise mpmath
        lo_ok = (x >= flo).all() if sp.lo_incl else (x > flo).all()
        hi_ok = (x <= fhi).all() if sp.hi_incl else (x < fhi).all()
        fin = bool(np.isfinite(x).all())
        sup = bool(lo_ok and hi_ok and fin)
        if sp.integer: sup = sup and bool((x == np.round(x)).all())
        if not sup:
            ok = False; det.append(f"SUPPORT VIOLATED min={np.nanmin(x)} max={np.nanmax(x)} finite={fin} n_below={int((x < flo).sum())} n_nan={int(np.isnan(x).sum())}")
        y = sp.transform(x) if sp.transform is not None else x
        y = y[np.isfinite(y)]
        n = len(y)
        if sp.mean is not None and sp.var is not None:
            mean = mp.mpf(sp.mean); var = mp.mpf(sp.var)
            xbar = mp.mpf(float(np.mean(y)))
            if var == 0:
                if not (y == float(mean)).all(): ok = False
                det.append(f"degenerate: all == {float(mean)}: {bool((y == float(mean)).all())}")
            else:
                zm = float((xbar - mean) / mp.sqrt(var / n))
                extra = ""
                if abs(zm) > ZMAX and sp.integer and n * float(var) < 2000:
                    # rare-event regime: exact Poisson tail of the count of non-modal draws
                    mode = float(np.round(float(mean)))
                    cnt = int((y != mode).sum()); lam = float(n * (1 - float(sp.cdf(mode) - (sp.cdf(mode - 1) if mode - 1 >= sp.lo else 0))))
                    pv = poisson_tail_p(cnt, lam); extra = f" [rare events: {cnt} non-modal draws vs Poisson({lam:.3g}), exact two-sided p={pv:.2e}]"
                    if pv >= PMIN: zm_ok = True
                    else: zm_ok = False
                else: zm_ok = abs(zm) <= ZMAX
                det.append(f"mean {float(xbar):.6g} vs {float(mean):.6g} z={zm:+.2f}{extra}")
                if not zm_ok: ok = False
                if sp.mu4 is not None:
                    mu4 = mp.mpf(sp.mu4)
                    s2 = mp.mpf(float(np.var(y)))
                    se = mp.sqrt((mu4 - var**2) / n)
                    zv = float((s2 - var) / se) if se > 0 else 0.0
                    det.append(f"var {float(s2):.6g} vs {float(var):.6g} z={zv:+.2f}")
                    if abs(zv) > ZMAX and not extra: ok = False
        if sp.cdf is not None:
            zs = []
            if sp.disc:
                if sp.pts is not None: pts = sp.pts
                else:
                    m = float(sp.mean) if sp.mean is not None else float(np.median(x))
                    sd = math.sqrt(float(sp.var)) if sp.var is not None else max(1.0, float(np.std(x)))
                    pts = sorted({int(math.floor(v)) for v in (m - sd, m, m + sd)})
                pts = [k for k in pts if sp.lo <= k < sp.hi]
                for k in pts:
                    p = mp.mpf(sp.cdf(k))
                    if p <= 0 or p >= 1: continue
                    cnt = int((x <= k).sum()); frac = mp.mpf(cnt) / len(x)
                    z = float((frac - p) / mp.sqrt(p * (1 - p) / len(x)))
                    tail = float(min(p, 1 - p)) * len(x)
                    if tail < 50:
                        # few expected events on one side: exact Poisson tail instead of the normal z
                        c_small = cnt if p < 0.5 else len(x) - cnt
                        pv = poisson_tail_p(c_small, tail); zs.append(f"P(X<={k})={float(p):.6g} count-tail p={pv:.2e}")
                        if pv < PMIN: ok = False
                    else:
                        zs.append(f"P(X<={k})={float(p):.6g} z={z:+.2f}")
                        if abs(z) > ZMAX: ok = False
            else:
                # exact CDF at the sample quantiles: F(X_(nq)) is a uniform order statistic, mean q, sd sqrt(q(1-q)/n)
                xs = np.sort(x)
                for q in (0.1, 0.5, 0.9):
                    xq = float(xs[int(math.ceil(q * len(xs))) - 1])
                    Fq = mp.mpf(sp.cdf(xq))
                    z = float((Fq - q) / mp.sqrt(mp.mpf(q) * (1 - q) / len(x)))
                    zs.append(f"F(sample q{q}={xq:.5g})={float(Fq):.6f} z={z:+.2f}")
                    if abs(z) > ZMAX: ok = False
            det.append("CDF " + ", ".join(zs))
        what = []
        if sp.mean is not None and sp.var is not None: what.append("mean" + ("/variance" if sp.mu4 is not None else "") + " z-tests vs exact moments")
        if sp.cdf is not None: what.append("empirical CDF vs exact CDF values" if sp.disc else "exact CDF at the sample 10/50/90% quantiles")
        report(f"{api}.{sp.label} n={len(x)}: support{' int' if sp.integer else ''} [{sp.lo},{sp.hi}], " + ", ".join(what) + (f" [{sp.note}]" if sp.note else ""), ok, "; ".join(det))

def pdf_check(label, pdf, lo, hi, mean, var, pts=None):
    """the docstring pdf integrates to 1 and reproduces the closed-form mean / variance (mpmath quad)"""
    pts = pts or [lo, hi]
    with mp.workdps(20):
        tot = mp.quad(pdf, pts); m1 = mp.quad(lambda x: x * pdf(x), pts)
        v = mp.quad(lambda x: (x - mp.mpf(mean))**2 * pdf(x), pts)
    ok = close(tot, 1, 1e-8) and close(m1, mean, 1e-7, 1e-12) and close(v, var, 1e-6, 1e-12)
    report(f"docstring pdf of {label}: integrates to 1, mean = {float(mean):.6g}, variance = {float(var):.6g} (mpmath quad vs closed form)", ok, f"int={float(tot):.12g} mean={float(m1):.10g} var={float(v):.10g}")

T_START = time.time()
# ======================================================================
# continuous distributions
# ======================================================================
print("---- continuous distributions (moment SE: variance z-test only where the 8th moment is finite)")
specs = []
def beta_spec(a, b):
    a = mp.mpf(a); b = mp.mpf(b)
    raw = [mp.fprod((a + r) / (a + b + r) for r in range(k)) for k in (1, 2, 3, 4)]
    m, v, m4 = raw_to_central(raw)
    return Spec(f"beta({float(a)}, {float(b)})", lambda g, n: g.beta(float(a), float(b), n), lambda r, n: r.beta(float(a), float(b), n), 0, 1,
                mean=m, var=v, mu4=m4, cdf=lambda x: mp.betainc(a, b, 0, x, regularized=True))
for a, b in [(0.05, 0.05), (2, 7), (1, 1), (30, 0.3), (0.5, 0.5)]: specs.append(beta_spec(a, b))
pdf_check("beta(2, 7)  B(a,b)^-1 x^(a-1)(1-x)^(b-1)", lambda x: x**1 * (1 - x)**6 / mp.beta(2, 7), 0, 1, mp.mpf(2)/9, mp.mpf(2*7)/(81*10))
def gamma_raw(k, th): k = mp.mpf(k); th = mp.mpf(th); return [th**r * mp.gamma(k + r) / mp.gamma(k) for r in (1, 2, 3, 4)]
def gamma_spec(k, th, label=None, gen=None, rs="same", note=""):
    m, v, m4 = raw_to_central(gamma_raw(k, th)); kk = mp.mpf(k); tt = mp.mpf(th)
    if rs == "same": rs = (lambda r, n: r.gamma(k, th, n))
    return Spec(label or f"gamma({k}, {th})", gen or (lambda g, n: g.gamma(k, th, n)), rs, 0, mp.inf,
                mean=m, var=v, mu4=m4, cdf=lambda x: mp.gammainc(kk, 0, mp.mpf(x) / tt, regularized=True), note=note)
for k, th in [(0.01, 1.0), (0.5, 3.0), (1000.0, 0.5), (1.0, 2.5)]: specs.append(gamma_spec(k, th))
specs.append(gamma_spec(0.01, 1.0, "standard_gamma(0.01)", lambda g, n: g.standard_gamma(0.01, n), lambda r, n: r.standard_gamma(0.01, n)))
specs.append(gamma_spec(2.5, 1.0, "standard_gamma(2.5)", lambda g, n: g.standard_gamma(2.5, n), lambda r, n: r.standard_gamma(2.5, n)))
specs.append(gamma_spec(2.5, 1.0, "standard_gamma(2.5, dtype=float32)", lambda g, n: g.standard_gamma(2.5, n, dtype=np.float32), None))
specs.append(gamma_spec(0.3, 1.0, "standard_gamma(0.3, dtype=float32)", lambda g, n: g.standard_gamma(0.3, n, dtype=np.float32), None))
for df in [0.5, 3.0, 100.0]:
    specs.append(gamma_spec(df / 2, 2.0, f"chisquare({df})", lambda g, n, df=df: g.chisquare(df, n), lambda r, n, df=df: r.chisquare(df, n)))
for sc in [0.001, 7.5]:
    specs.append(gamma_spec(1.0, sc, f"exponential(scale={sc})", lambda g, n, sc=sc: g.exponential(sc, n), lambda r, n, sc=sc: r.exponential(sc, n)))
specs.append(gamma_spec(1.0, 1.0, "standard_exponential(method='zig')", lambda g, n: g.standard_exponential(n, method='zig'), lambda r, n: r.standard_exponential(n)))
specs.append(gamma_spec(1.0, 1.0, "standard_exponential(method='inv')", lambda g, n: g.standard_exponential(n, method='inv'), None))
specs.append(gamma_spec(1.0, 1.0, "standard_exponential(dtype=float32, method='zig')", lambda g, n: g.standard_exponential(n, dtype=np.float32), None))
specs.append(gamma_spec(1.0, 1.0, "standard_exponential(dtype=float32, method='inv')", lambda g, n: g.standard_exponential(n, dtype=np.float32, method='inv'), None))
pdf_check("gamma(0.5, 3)  x^(k-1) e^(-x/theta) / (theta^k Gamma(k))", lambda x: x**mp.mpf(-0.5) * mp.exp(-x / 3) / (mp.sqrt(3) * mp.gamma(0.5)), 0, mp.inf, 1.5, 4.5, [0, 1, 10, mp.inf])
pdf_check("chisquare(3)  x^(k/2-1) e^(-x/2) / (2^(k/2) Gamma(k/2))", lambda x: x**0.5 * mp.exp(-x / 2) / (2**1.5 * mp.gamma(1.5)), 0, mp.inf, 3, 6, [0, 3, 30, mp.inf])
# f / noncentral_f  (E[F^r] needs dfden > 2r; variance z-test needs the 8th moment: dfden > 16)
def f_raw(d1, d2, r): return (mp.mpf(d2) / d1)**r * chi2_raw(d1, r) * chi2_raw(d2, -r)
def f_spec(d1, d2):
    d1m = mp.mpf(d1); d2m = mp.mpf(d2)
    cdf = lambda x: mp.betainc(d1m/2, d2m/2, 0, d1m*x / (d1m*x + d2m), regularized=True)
    if d2 > 16: m, v, m4 = raw_to_central([f_raw(d1, d2, r) for r in (1, 2, 3, 4)])
    elif d2 > 4: m, v, m4 = f_raw(d1, d2, 1), f_raw(d1, d2, 2) - f_raw(d1, d2, 1)**2, None
    else: m = v = m4 = None
    return Spec(f"f({d1}, {d2})", lambda g, n: g.f(d1, d2, n), lambda r, n: r.f(d1, d2, n), 0, mp.inf, mean=m, var=v, mu4=m4, cdf=cdf,
                note="dfden<=4: infinite variance, CDF only" if d2 <= 4 else "")
for d1, d2 in [(1, 48), (20, 20), (0.5, 3), (5, 100)]: specs.append(f_spec(d1, d2))
def ncf_spec(d1, d2, lam):
    raw = [(mp.mpf(d2) / d1)**r * ncchi2_raw(d1, lam, r) * chi2_raw(d2, -r) for r in (1, 2, 3, 4)]
    m, v, m4 = raw_to_central(raw)
    docmean = mp.mpf(d2) * (d1 + lam) / (d1 * (mp.mpf(d2) - 2))
    assert mpclose(m, docmean, 1e-20), (m, docmean)
    return Spec(f"noncentral_f({d1}, {d2}, {lam})", lambda g, n: g.noncentral_f(d1, d2, lam, n), lambda r, n: r.noncentral_f(d1, d2, lam, n), 0, mp.inf,
                mean=m, var=v, mu4=m4 if d2 > 16 else None, cdf=lambda x: ncf_cdf(d1, d2, lam, x),
                note=("dfnum < 1" if d1 < 1 else "") + ("; nonc = 0" if lam == 0 else ""))
for d1, d2, lam in [(3, 20, 3.0), (0.5, 10, 1.0), (5, 50, 0.0)]: specs.append(ncf_spec(d1, d2, lam))
def ncchi_spec(k, lam):
    m, v, m4 = raw_to_central([ncchi2_raw(k, lam, r) for r in (1, 2, 3, 4)])
    k_ = mp.mpf(k); l_ = mp.mpf(lam)
    assert mpclose(m, k_ + l_, 1e-20) and mpclose(v, 2 * (k_ + 2*l_), 1e-20) and mpclose(m4, 12 * (k_ + 2*l_)**2 + 48 * (k_ + 4*l_), 1e-18), (m, v, m4)
    return Spec(f"noncentral_chisquare({k}, {lam})", lambda g, n: g.noncentral_chisquare(k, lam, n), lambda r, n: r.noncentral_chisquare(k, lam, n), 0, mp.inf,
                mean=m, var=v, mu4=m4, cdf=lambda x: ncchi2_cdf(k, lam, x), note="df < 1 (Poisson-mixture branch)" if k < 1 else ("df == 1" if k == 1 else ""))
for k, lam in [(3, 20.0), (0.5, 2.0), (5, 0.0), (1.0, 0.5), (0.1, 30.0)]: specs.append(ncchi_spec(k, lam))
report("noncentral_chisquare closed forms (mean df+nonc, var 2(df+2nonc), mu4 12(df+2nonc)^2+48(df+4nonc)) agree with the Poisson mixture of chi-squares (mpmath, 30 digits)", True)
eg = mp.euler
for mu, b in [(0.0, 0.1), (5.0, 3.0)]:
    b_ = mp.mpf(b); mu_ = mp.mpf(mu)
    specs.append(Spec(f"gumbel({mu}, {b})", lambda g, n, mu=mu, b=b: g.gumbel(mu, b, n), lambda r, n, mu=mu, b=b: r.gumbel(mu, b, n), -mp.inf, mp.inf,
                      mean=mu_ + eg * b_, var=mp.pi**2 * b_**2 / 6, mu4=3 * mp.pi**4 * b_**4 / 20, cdf=lambda x, mu_=mu_, b_=b_: mp.exp(-mp.exp(-(mp.mpf(x) - mu_) / b_)),
                      note="docstring: 'mean of mu + 0.57721 beta and a variance of pi^2/6 beta^2'"))
pdf_check("gumbel(5, 3)  exp(-(x-mu)/beta - exp(-(x-mu)/beta)) / beta", lambda x: mp.exp(-(x - 5) / 3 - mp.exp(-(x - 5) / 3)) / 3, -mp.inf, mp.inf, 5 + eg * 3, mp.pi**2 * 9 / 6, [-40, 0, 5, 20, 250])   # finite limits: density < 1e-60 outside, and exp(-exp(1e20)) stalls mpmath
for mu, b in [(0.0, 1.0), (-2.0, 0.5)]:
    b_ = mp.mpf(b); mu_ = mp.mpf(mu)
    specs.append(Spec(f"laplace({mu}, {b})", lambda g, n, mu=mu, b=b: g.laplace(mu, b, n), lambda r, n, mu=mu, b=b: r.laplace(mu, b, n), -mp.inf, mp.inf,
                      mean=mu_, var=2 * b_**2, mu4=24 * b_**4, cdf=lambda x, mu_=mu_, b_=b_: mp.exp((mp.mpf(x) - mu_) / b_) / 2 if x < mu_ else 1 - mp.exp(-(mp.mpf(x) - mu_) / b_) / 2,
                      note="docstring: loc is 'location (or mean)'"))
pdf_check("laplace(-2, 0.5)  exp(-|x-mu|/lambda) / (2 lambda)", lambda x: mp.exp(-abs(x + 2) / mp.mpf(0.5)) / 1, -mp.inf, mp.inf, -2, 0.5, [-mp.inf, -2, mp.inf])
for mu, s in [(10.0, 1.0), (0.0, 0.01)]:
    s_ = mp.mpf(s); mu_ = mp.mpf(mu)
    specs.append(Spec(f"logistic({mu}, {s})", lambda g, n, mu=mu, s=s: g.logistic(mu, s, n), lambda r, n, mu=mu, s=s: r.logistic(mu, s, n), -mp.inf, mp.inf,
                      mean=mu_, var=s_**2 * mp.pi**2 / 3, mu4=mp.mpf(21) / 5 * (s_**2 * mp.pi**2 / 3)**2, cdf=lambda x, mu_=mu_, s_=s_: 1 / (1 + mp.exp(-(mp.mpf(x) - mu_) / s_)),
                      note="docstring: loc is 'location or mean, also median'"))
pdf_check("logistic(10, 1)  e^{-(x-mu)/s} / (s (1 + e^{-(x-mu)/s})^2)", lambda x: mp.exp(-(x - 10)) / (1 + mp.exp(-(x - 10)))**2, -mp.inf, mp.inf, 10, mp.pi**2 / 3, [-mp.inf, 10, mp.inf])
for mu, sg in [(3.0, 1.0), (0.0, 0.1), (0.0, 3.0)]:
    mu_ = mp.mpf(mu); sg_ = mp.mpf(sg)
    specs.append(Spec(f"lognormal({mu}, {sg}) -> log(x)", lambda g, n, mu=mu, sg=sg: g.lognormal(mu, sg, n), lambda r, n, mu=mu, sg=sg: r.lognormal(mu, sg, n), 0, mp.inf, lo_incl=(sg > 1),
                      mean=mu_, var=sg_**2, mu4=3 * sg_**4, transform=np.log, cdf=None, note="docstring: 'log(x) is normally distributed' with the given mean and sigma"))
    cdfl = lambda x, mu_=mu_, sg_=sg_: mp.ncdf((mp.log(x) - mu_) / sg_) if x > 0 else mp.mpf(0)
    if sg <= 1:
        raw = [mp.exp(r * mu_ + r**2 * sg_**2 / 2) for r in (1, 2, 3, 4)]
        m, v, m4 = raw_to_central(raw)
        specs.append(Spec(f"lognormal({mu}, {sg})", lambda g, n, mu=mu, sg=sg: g.lognormal(mu, sg, n), lambda r, n, mu=mu, sg=sg: r.lognormal(mu, sg, n), 0, mp.inf, lo_incl=False,
                          mean=m, var=v, mu4=m4 if sg < 0.5 else None, cdf=cdfl, note="sigma=1: variance test skipped (kurtosis of x^2 ~ e^16 makes the CLT for s^2 invalid at n=4e5)" if sg == 1 else ""))
    else:
        specs.append(Spec(f"lognormal({mu}, {sg})", lambda g, n, mu=mu, sg=sg: g.lognormal(mu, sg, n), lambda r, n, mu=mu, sg=sg: r.lognormal(mu, sg, n), 0, mp.inf, lo_incl=True,
                          cdf=cdfl, note="sigma=3: variance e^18 (e^9 - 1), moments not testable at n=4e5, CDF only; exp(3 z) may underflow only below z=-248: support (0, inf)"))
for mu, sg in [(0.0, 0.1), (3.0, 2.5), (1e6, 1e-3)]:
    mu_ = mp.mpf(mu); sg_ = mp.mpf(sg)
    specs.append(Spec(f"normal({mu}, {sg})", lambda g, n, mu=mu, sg=sg: g.normal(mu, sg, n), lambda r, n, mu=mu, sg=sg: r.normal(mu, sg, n), -mp.inf, mp.inf,
                      mean=mu_, var=sg_**2, mu4=3 * sg_**4, cdf=lambda x, mu_=mu_, sg_=sg_: mp.ncdf((mp.mpf(x) - mu_) / sg_)))
specs.append(Spec("standard_normal()", lambda g, n: g.standard_normal(n), lambda r, n: r.standard_normal(n), -mp.inf, mp.inf, mean=0, var=1, mu4=3, cdf=mp.ncdf))
specs.append(Spec("standard_normal(dtype=float32)", lambda g, n: g.standard_normal(n, dtype=np.float32), None, -mp.inf, mp.inf, mean=0, var=1, mu4=3, cdf=mp.ncdf))
specs.append(Spec("randn()", None, lambda r, n: r.randn(n), -mp.inf, mp.inf, mean=0, var=1, mu4=3, cdf=mp.ncdf))
pdf_check("normal(3, 2.5)  exp(-(x-mu)^2/(2 sigma^2)) / sqrt(2 pi sigma^2)", lambda x: mp.exp(-(x - 3)**2 / (2 * mp.mpf(2.5)**2)) / mp.sqrt(2 * mp.pi * mp.mpf(2.5)**2), -mp.inf, mp.inf, 3, 6.25, [-mp.inf, 3, mp.inf])
for a in [0.5, 3.0, 10.0]:
    a_ = mp.mpf(a)
    if a > 8: m, v, m4 = raw_to_central([mp.gamma(a_ - r) * mp.gamma(r + 1) / mp.gamma(a_) for r in (1, 2, 3, 4)])
    elif a > 2: m, v, m4 = mp.mpf(1) / (a_ - 1), a_ / ((a_ - 1)**2 * (a_ - 2)), None
    else: m = v = m4 = None
    specs.append(Spec(f"pareto({a})", lambda g, n, a=a: g.pareto(a, n), lambda r, n, a=a: r.pareto(a, n), 0, mp.inf, mean=m, var=v, mu4=m4,
                      cdf=lambda x, a_=a_: 1 - (1 + mp.mpf(x))**(-a_), note="Lomax: pdf a/(1+x)^(a+1) on [0, inf)" + ("; a=0.5 has no mean: CDF only" if a < 1 else "")))
pdf_check("pareto(3)  a / (1+x)^(a+1)  (Lomax, docstring: 'Pareto II or Lomax distribution with specified shape')", lambda x: 3 / (1 + x)**4, 0, mp.inf, mp.mpf(1)/2, mp.mpf(3)/(4*1), [0, 1, 10, mp.inf])
for a in [0.3, 5.0, 1.0]:
    a_ = mp.mpf(a); m, v, m4 = raw_to_central([a_ / (a_ + r) for r in (1, 2, 3, 4)])
    specs.append(Spec(f"power({a})", lambda g, n, a=a: g.power(a, n), lambda r, n, a=a: r.power(a, n), 0, 1, mean=m, var=v, mu4=m4, cdf=lambda x, a_=a_: mp.mpf(x)**a_,
                      note="a=1 is uniform" if a == 1 else ""))
pdf_check("power(5)  a x^(a-1) on [0,1]", lambda x: 5 * x**4, 0, 1, mp.mpf(5)/6, mp.mpf(5)/7 - (mp.mpf(5)/6)**2)
for sc in [3.0, 0.01]:
    s_ = mp.mpf(sc); m, v, m4 = raw_to_central([s_**r * mp.mpf(2)**(mp.mpf(r)/2) * mp.gamma(1 + mp.mpf(r)/2) for r in (1, 2, 3, 4)])
    specs.append(Spec(f"rayleigh({sc})", lambda g, n, sc=sc: g.rayleigh(sc, n), lambda r, n, sc=sc: r.rayleigh(sc, n), 0, mp.inf, mean=m, var=v, mu4=m4,
                      cdf=lambda x, s_=s_: 1 - mp.exp(-mp.mpf(x)**2 / (2 * s_**2)), note="docstring: 'scale, also equals the mode'"))
pdf_check("rayleigh(3)  x/sigma^2 exp(-x^2/(2 sigma^2))", lambda x: x / 9 * mp.exp(-x**2 / 18), 0, mp.inf, 3 * mp.sqrt(mp.pi / 2), (4 - mp.pi) / 2 * 9, [0, 3, 30, mp.inf])
specs.append(Spec("standard_cauchy()", lambda g, n: g.standard_cauchy(n), lambda r, n: r.standard_cauchy(n), -mp.inf, mp.inf, cdf=lambda x: mp.mpf(1)/2 + mp.atan(x) / mp.pi, note="no moments: quantiles only"))
def t_cdf(df):
    df = mp.mpf(df)
    def cdf(x):
        x = mp.mpf(x); tail = mp.betainc(df / 2, mp.mpf(1)/2, 0, df / (df + x**2), regularized=True) / 2
        return 1 - tail if x >= 0 else tail
    return cdf
for df in [1.0, 2.0, 5.0, 30.0]:
    d_ = mp.mpf(df)
    if df > 8: m, v, m4 = 0, d_ / (d_ - 2), 3 * d_**2 / ((d_ - 2) * (d_ - 4))
    elif df > 2: m, v, m4 = 0, d_ / (d_ - 2), None
    else: m = v = m4 = None
    specs.append(Spec(f"standard_t({df})", lambda g, n, df=df: g.standard_t(df, n), lambda r, n, df=df: r.standard_t(df, n), -mp.inf, mp.inf, mean=m, var=v, mu4=m4, cdf=t_cdf(df),
                      note="df=1 is Cauchy: quantiles only" if df == 1 else ("df=2: infinite variance, quantiles only" if df == 2 else ("df=5: 8th moment infinite, mean test only" if df == 5 else ""))))
pdf_check("standard_t(5)  Gamma((df+1)/2)/(sqrt(pi df) Gamma(df/2)) (1+x^2/df)^(-(df+1)/2)", lambda x: mp.gamma(3) / (mp.sqrt(5 * mp.pi) * mp.gamma(2.5)) * (1 + x**2 / 5)**(-3), -mp.inf, mp.inf, 0, mp.mpf(5)/3, [-mp.inf, -5, 0, 5, mp.inf])
def tri_spec(l, m_, r):
    l_ = mp.mpf(l); m__ = mp.mpf(m_); r_ = mp.mpf(r)
    def pdf(x):
        if x < l_ or x > r_: return mp.mpf(0)
        if x <= m__: return 2 * (x - l_) / ((r_ - l_) * (m__ - l_)) if m__ > l_ else mp.mpf(0)
        return 2 * (r_ - x) / ((r_ - l_) * (r_ - m__)) if r_ > m__ else mp.mpf(0)
    pts = sorted({l_, m__, r_})
    with mp.workdps(20):
        raw = [mp.quad(lambda x, k=k: x**k * pdf(x), pts) for k in (1, 2, 3, 4)]
    mean, var, mu4 = raw_to_central(raw)
    assert close(mean, (l_ + m__ + r_) / 3, 1e-12)
    assert close(var, (l_**2 + m__**2 + r_**2 - l_*m__ - l_*r_ - m__*r_) / 18, 1e-10)
    def cdf(x):
        x = mp.mpf(x)
        if x <= l_: return mp.mpf(0)
        if x >= r_: return mp.mpf(1)
        if x <= m__: return (x - l_)**2 / ((r_ - l_) * (m__ - l_))
        return 1 - (r_ - x)**2 / ((r_ - l_) * (r_ - m__))
    return Spec(f"triangular({l}, {m_}, {r})", lambda g, n: g.triangular(l, m_, r, n), lambda rr, n: rr.triangular(l, m_, r, n), l, r, mean=mean, var=var, mu4=mu4, cdf=cdf,
                note="left == mode" if l == m_ else ("mode == right" if m_ == r else ""))
for l, m_, r in [(-3.0, 0.0, 8.0), (0.0, 0.0, 1.0), (0.0, 1.0, 1.0), (10.0, 10.5, 11.0)]: specs.append(tri_spec(l, m_, r))
for a, b in [(-1.0, 0.0), (1e9, 1e9 + 1)]:
    a_ = mp.mpf(a); b_ = mp.mpf(b)
    specs.append(Spec(f"uniform({a}, {b})", lambda g, n, a=a, b=b: g.uniform(a, b, n), lambda r, n, a=a, b=b: r.uniform(a, b, n), a, b, hi_incl=True,
                      mean=(a_ + b_) / 2, var=(b_ - a_)**2 / 12, mu4=(b_ - a_)**4 / 80, cdf=lambda x, a_=a_, b_=b_: (mp.mpf(x) - a_) / (b_ - a_),
                      note="docstring: 'The high limit may be included ... due to floating-point rounding'"))
specs.append(Spec("uniform(0.0, 1e-300) scaled by 1e300", lambda g, n: g.uniform(0.0, 1e-300, n), lambda r, n: r.uniform(0.0, 1e-300, n), 0, 1e-300, hi_incl=True,
                  mean=mp.mpf(1)/2, var=mp.mpf(1)/12, mu4=mp.mpf(1)/80, transform=lambda x: x * 1e300, note="tiny width: moments of x*1e300 (float squares of 1e-300 underflow)"))
specs.append(Spec("random()", lambda g, n: g.random(n), lambda r, n: r.random_sample(n), 0, 1, hi_incl=False, mean=mp.mpf(1)/2, var=mp.mpf(1)/12, mu4=mp.mpf(1)/80, cdf=lambda x: mp.mpf(x),
                  note="docstring: 'half-open interval [0.0, 1.0)'"))
specs.append(Spec("random(dtype=float32)", lambda g, n: g.random(n, dtype=np.float32), None, 0, 1, hi_incl=False, mean=mp.mpf(1)/2, var=mp.mpf(1)/12, mu4=mp.mpf(1)/80, cdf=lambda x: mp.mpf(x)))
specs.append(Spec("rand()", None, lambda r, n: r.rand(n), 0, 1, hi_incl=False, mean=mp.mpf(1)/2, var=mp.mpf(1)/12, mu4=mp.mpf(1)/80, cdf=lambda x: mp.mpf(x)))
def vm_spec(kappa):
    k_ = mp.mpf(kappa); I0e = mp.besseli(0, k_) * mp.exp(-k_)
    pdf = lambda x: mp.exp(k_ * (mp.cos(x) - 1)) / (2 * mp.pi * I0e)
    s = min(1.0, 1 / math.sqrt(kappa))
    pts = sorted({-mp.pi, mp.pi, mp.mpf(0)} | {mp.mpf(c * s) for c in (-30, -10, -3, -1, 1, 3, 10, 30) if abs(c * s) < math.pi})
    with mp.workdps(20):
        raw = [mp.quad(lambda x, k=k: x**k * pdf(x), pts) for k in (1, 2, 3, 4)]
        tot = mp.quad(pdf, pts)
    assert close(tot, 1, 1e-10), tot
    mean, var, mu4 = raw_to_central(raw)
    cdf = lambda x: mp.quad(pdf, [p for p in pts if p < x] + [mp.mpf(x)]) if x > -mp.pi else mp.mpf(0)
    return Spec(f"vonmises(0, {kappa})", lambda g, n: g.vonmises(0.0, kappa, n), lambda r, n: r.vonmises(0.0, kappa, n), -mp.pi, mp.pi, mean=0, var=var, mu4=mu4, cdf=cdf,
                note="moments of theta on [-pi, pi] by mpmath quad of exp(kappa cos)/(2 pi I0)" + ("; kappa > 1e6: Generator uses a wrapped normal" if kappa > 1e6 else "") + ("; kappa < 1e-8 uniform branch" if kappa < 1e-8 else ""))
for kappa in [0.01, 4.0, 1000.0, 1e-9, 1e7]: specs.append(vm_spec(kappa))
for mu, lam in [(3.0, 2.0), (1.0, 100.0), (0.1, 0.01)]:
    mu_ = mp.mpf(mu); l_ = mp.mpf(lam); var = mu_**3 / l_
    cdf = lambda x, mu_=mu_, l_=l_: mp.ncdf(mp.sqrt(l_ / x) * (x / mu_ - 1)) + mp.exp(2 * l_ / mu_) * mp.ncdf(-mp.sqrt(l_ / x) * (x / mu_ + 1)) if x > 0 else mp.mpf(0)
    specs.append(Spec(f"wald({mu}, {lam})", lambda g, n, mu=mu, lam=lam: g.wald(mu, lam, n), lambda r, n, mu=mu, lam=lam: r.wald(mu, lam, n), 0, mp.inf, lo_incl=False,
                      mean=mu_, var=var, mu4=var**2 * (3 + 15 * mu_ / l_), cdf=cdf, note="docstring: 'mean : Distribution mean'"))
pdf_check("wald(3, 2)  sqrt(scale/(2 pi x^3)) exp(-scale (x-mean)^2 / (2 mean^2 x))", lambda x: mp.sqrt(2 / (2 * mp.pi * x**3)) * mp.exp(-2 * (x - 3)**2 / (18 * x)), 0, mp.inf, 3, mp.mpf(27)/2, [0, 1, 3, 10, 100, mp.inf])
for a in [0.5, 1.0, 5.0]:
    a_ = mp.mpf(a); m, v, m4 = raw_to_central([mp.gamma(1 + mp.mpf(r) / a_) for r in (1, 2, 3, 4)])
    specs.append(Spec(f"weibull({a})", lambda g, n, a=a: g.weibull(a, n), lambda r, n, a=a: r.weibull(a, n), 0, mp.inf, mean=m, var=v, mu4=m4, cdf=lambda x, a_=a_: 1 - mp.exp(-mp.mpf(x)**a_),
                      note="a=1 reduces to the exponential (docstring)" if a == 1 else ""))
pdf_check("weibull(5)  a x^(a-1) exp(-x^a)", lambda x: 5 * x**4 * mp.exp(-x**5), 0, mp.inf, mp.gamma(1.2), mp.gamma(1.4) - mp.gamma(1.2)**2, [0, 1, 3, mp.inf])
t0 = time.time()
for sp in specs:
    _t = time.time(); run_spec(sp)
    if os.environ.get('N9_PROFILE'): print(f'   [{time.time() - _t:.2f} s] {sp.label}', flush=True)
print(f"   continuous block {time.time() - t0:.1f} s")

# vonmises with mu away from 0: wrap-around keeps [-pi, pi]; circular moments E cos(X-mu) = I1/I0, E sin(X-mu) = 0
for mu, kappa in [(3.0, 4.0), (-3.1, 0.5), (3.14, 1e7)]:
    k_ = mp.mpf(kappa); r1 = mp.besseli(1, k_) / mp.besseli(0, k_); r2 = mp.besseli(2, k_) / mp.besseli(0, k_)
    vc = (1 + r2) / 2 - r1**2; vs = (1 - r2) / 2
    for api, x in (("Generator", G().vonmises(mu, kappa, N)), ("RandomState", R().vonmises(mu, kappa, N))):
        c = np.cos(x - mu); s = np.sin(x - mu)
        zc = float((mp.mpf(float(c.mean())) - r1) / mp.sqrt(vc / N)) if vc > 0 else 0.0
        zs = float(mp.mpf(float(s.mean())) / mp.sqrt(vs / N))
        ok = bool((x >= -np.pi).all() and (x <= np.pi).all()) and abs(zc) <= ZMAX and abs(zs) <= ZMAX
        report(f"{api}.vonmises({mu}, {kappa}): all in [-pi, pi] (docstring 'on the interval [-pi, pi]'), E cos(X-mu) = I1/I0 = {float(r1):.6g}, E sin(X-mu) = 0", ok,
               f"min {x.min():.6f} max {x.max():.6f}; cos z={zc:+.2f} sin z={zs:+.2f}")

print("---- discrete distributions")
specs = []
def binom_cdf_factory(n_, p):
    if n_ <= 10000:
        n_m = mp.mpf(n_); q_ = 1 - mp.mpf(p)
        return lambda k: mp.betainc(n_m - k, k + 1, 0, q_, regularized=True) if 0 <= k < n_ else (mp.mpf(1) if k >= n_ else mp.mpf(0))
    # huge n: pmf by the exact ratio recurrence outward from the mode (mpmath start value), summed in floats
    mode = int((n_ + 1) * p); sd = math.sqrt(n_ * p * (1 - p)); W = int(45 * sd) + 10
    Wl = min(W, mode); Wr = min(W, n_ - mode)
    with mp.workdps(40):
        lp0 = mp.loggamma(n_ + 1) - mp.loggamma(mode + 1) - mp.loggamma(n_ - mode + 1) + mode * mp.log(p) + (n_ - mode) * mp.log1p(-p)
    p0 = float(mp.exp(lp0)); rat = p / (1 - p)
    left = [p0]                                           # left[i] = pmf(mode - i)
    for i in range(1, Wl + 1):
        k = mode - i + 1                                  # pmf(k-1) = pmf(k) * k / ((n-k+1) rat)
        left.append(left[-1] * k / ((n_ - k + 1) * rat))
    suf = [0.0] * (Wl + 2)                                # suf[i] = P(X <= mode - i)
    for i in range(Wl, -1, -1): suf[i] = suf[i + 1] + left[i]
    right = [p0]                                          # right[i] = pmf(mode + i)
    for i in range(1, Wr + 1):
        k = mode + i - 1; right.append(right[-1] * (n_ - k) * rat / (k + 1))
    total = suf[0] + sum(right[1:])
    report(f"binomial({n_}, {p}) exact pmf table by ratio recurrence from the mode (start value mpmath loggamma): total mass 1", abs(total - 1) < 1e-9, f"mass {total!r}")
    def cdf(k):
        k = int(k)
        if k >= mode: return mp.mpf(suf[0] + sum(right[1:k - mode + 1]))
        return mp.mpf(suf[mode - k]) if mode - k <= Wl else mp.mpf(0)
    return cdf
def binom_spec(n_, p):
    n_m = mp.mpf(n_); p_ = mp.mpf(p); q_ = 1 - p_
    var = n_m * p_ * q_
    return Spec(f"binomial({n_}, {p})", lambda g, n: g.binomial(n_, p, n), lambda r, n: r.binomial(n_, p, n), 0, n_, integer=True, disc=True,
                mean=n_m * p_, var=var, mu4=var * (1 + 3 * (n_m - 2) * p_ * q_), cdf=binom_cdf_factory(n_, p))
for n_, p in [(10**9, 0.3), (10, 1e-6), (10, 0.999999), (1, 0.5), (50, 0.5), (1000, 0.01), (10**6, 1e-7)]: specs.append(binom_spec(n_, p))
for p in [1e-4, 0.35, 0.4, 0.2, 0.999, 1e-15]:
    p_ = mp.mpf(p); var = (1 - p_) / p_**2
    specs.append(Spec(f"geometric({p})", lambda g, n, p=p: g.geometric(p, n), lambda r, n, p=p: r.geometric(p, n), 1, mp.inf, integer=True, disc=True,
                      mean=1 / p_, var=var, mu4=var**2 * (9 + p_**2 / (1 - p_)), cdf=lambda k, p_=p_: 1 - (1 - p_)**k, note="support k = 1, 2, ... (docstring f(k) = (1-p)^(k-1) p)"))
def hyper_spec(good, bad, ns):
    lo = max(0, ns - bad); hi = min(ns, good)
    with mp.workdps(40):
        lc = lambda n, k: mp.loggamma(n + 1) - mp.loggamma(k + 1) - mp.loggamma(n - k + 1)
        pm = {k: mp.exp(lc(good, k) + lc(bad, ns - k) - lc(good + bad, ns)) for k in range(lo, hi + 1)}
        tot = sum(pm.values())
    assert abs(tot - 1) < 1e-25, tot
    raw = [sum(pm[k] * k**r for k in pm) for r in (1, 2, 3, 4)]
    m, v, m4 = raw_to_central(raw)
    assert mpclose(m, mp.mpf(ns) * good / (good + bad), 1e-20)
    tab = {}; acc = mp.mpf(0)
    for k in range(lo, hi + 1): acc += pm[k]; tab[k] = acc
    return Spec(f"hypergeometric({good}, {bad}, {ns})", lambda g, n: g.hypergeometric(good, bad, ns, n), lambda r, n: r.hypergeometric(good, bad, ns, n), lo, hi, integer=True, disc=True,
                mean=m, var=v, mu4=m4, cdf=lambda k: tab.get(int(k), mp.mpf(1) if k >= hi else mp.mpf(0)))
for good, bad, ns in [(100, 2, 10), (15, 15, 15), (10**9 - 1, 10**9 - 1, 1000), (1000, 1000, 1990), (5, 95, 100), (10**9 - 1, 10, 5), (7, 3, 9), (20, 30, 50), (500, 600, 400)]:
    specs.append(hyper_spec(good, bad, ns))
def logser_spec(p):
    """raw moments E[X^r] = Li_{1-r}(p) / (-ln(1-p)) with the closed forms of Li_0, Li_-1, Li_-2, Li_-3; CDF via the Lerch transcendent"""
    p_ = mp.mpf(p); L = -mp.log1p(-p_); q = 1 - p_
    li = [p_ / q, p_ / q**2, p_ * (1 + p_) / q**3, p_ * (1 + 4*p_ + p_**2) / q**4]
    m, v, m4 = raw_to_central([x / L for x in li])
    def cdf(k):
        k = int(k)
        if k < 1: return mp.mpf(0)
        return 1 - p_**(k + 1) * mp.lerchphi(p_, 1, k + 1) / L
    assert mpclose(cdf(3), sum(p_**j / j for j in (1, 2, 3)) / L, 1e-20)
    return Spec(f"logseries({p})", lambda g, n: g.logseries(p, n), lambda r, n: r.logseries(p, n), 1, mp.inf, integer=True, disc=True, mean=m, var=v, mu4=m4,
                cdf=cdf, note="pmf -p^k/(k ln(1-p)) (docstring)")
for p in [0.6, 0.999, 1e-6, 1 - 1e-7]: specs.append(logser_spec(p))
for n_, p in [(1.0, 0.1), (2.5, 0.3), (100.0, 0.999), (0.5, 0.01), (1e-3, 0.5)]:
    n_m = mp.mpf(n_); p_ = mp.mpf(p); var = n_m * (1 - p_) / p_**2
    specs.append(Spec(f"negative_binomial({n_}, {p})", lambda g, n, n_=n_, p=p: g.negative_binomial(n_, p, n), lambda r, n, n_=n_, p=p: r.negative_binomial(n_, p, n), 0, mp.inf, integer=True, disc=True,
                      mean=n_m * (1 - p_) / p_, var=var, mu4=var**2 * (3 + 6 / n_m + p_**2 / (n_m * (1 - p_))), cdf=lambda k, n_m=n_m, p_=p_: mp.betainc(n_m, k + 1, 0, p_, regularized=True),
                      note="number of failures before n successes, pmf Gamma(N+n)/(N! Gamma(n)) p^n (1-p)^N (docstring)" + ("; non-integer n" if n_ != int(n_) else "")))
for lam in [5.0, 1e6, 0.01, 1000.0, 9.99]:
    l_ = mp.mpf(lam)
    specs.append(Spec(f"poisson({lam})", lambda g, n, lam=lam: g.poisson(lam, n), lambda r, n, lam=lam: r.poisson(lam, n), 0, mp.inf, integer=True, disc=True,
                      mean=l_, var=l_, mu4=l_ + 3 * l_**2, cdf=lambda k, l_=l_: mp.gammainc(k + 1, l_, mp.inf, regularized=True), note="docstring: 'mean and variance, which should be approximately lam'"))
ZIPF_M = 2**63      # proposals X > (double)RAND_INT_MAX = 2^63 are rejected (random_zipf comment: 'a Zipf distribution truncated to sys.maxint')
def zipf_spec(a, pts):
    a_ = mp.mpf(a); z = mp.zeta(a_); zt = z - mp.zeta(a_, ZIPF_M + 1)
    cdf = lambda k: (z - mp.zeta(a_, int(k) + 1)) / zt if k >= 1 else mp.mpf(0)
    if a > 9: m, v, m4 = raw_to_central([mp.zeta(a_ - r) / z for r in (1, 2, 3, 4)])
    elif a > 3: m, v, m4 = mp.zeta(a_ - 1) / z, mp.zeta(a_ - 2) / z - (mp.zeta(a_ - 1) / z)**2, None
    else: m = v = m4 = None
    trunc = float(1 - zt / z)
    return Spec(f"zipf({a})", lambda g, n: g.zipf(a, n), lambda r, n: r.zipf(a, n), 1, float(ZIPF_M), integer=True, disc=True, mean=m, var=v, mu4=m4, cdf=cdf, pts=pts,
                note=f"pmf k^-a / zeta(a) conditioned on k <= 2^63 (untruncated mass beyond 2^63: {trunc:.3g}); moments zeta(a-r)/zeta(a) where finite")
for a, pts in [(1.001, [1, 2, 10, 10**6, 10**15]), (1.1, [1, 2, 3, 10, 100, 10**4]), (2.5, [1, 2, 3, 10]), (4.0, [1, 2, 5]), (10.0, [1, 2])]: specs.append(zipf_spec(a, pts))
t0 = time.time()
for sp in specs:
    _t = time.time(); run_spec(sp)
    if os.environ.get('N9_PROFILE'): print(f'   [{time.time() - _t:.2f} s] {sp.label}', flush=True)
print(f"   discrete block {time.time() - t0:.1f} s")
# zipf(1.1): compare with the untruncated law too (informational: the truncation is what the code states)
xz = G().zipf(1.1, N); z11 = mp.zeta(1.1)
print(f"   zipf(1.1): P(X=1) empirical {np.mean(xz == 1):.5f}; untruncated 1/zeta(1.1) = {float(1 / z11):.5f}; truncated at 2^63 = {float(1 / (z11 - mp.zeta(1.1, ZIPF_M + 1))):.5f}")

# zipf near 1: cause of the CDF deviation -- the rejection step of random_zipf with T = pow(1 + 1/X, a - 1) in float64
# (T == 1 for X > 2**53, so every huge proposal is accepted) vs the same step with T - 1 = expm1((a-1) log1p(1/X))
for a in (1.1, 1.001):
    rr = np.random.default_rng(99); am1 = a - 1; b = 2.0**am1; Mz = 2.0**63; n = 4_000_000
    U01 = rr.random(n); U = U01 * Mz**(-am1) + (1 - U01); Vv = rr.random(n)
    Xp = np.floor(U**(-1.0 / am1)); kp = (Xp <= Mz) & (Xp >= 1); Xp = Xp[kp]; Vv = Vv[kp]
    Tf = (1.0 + 1.0 / Xp)**am1; accf = Vv * Xp * (Tf - 1.0) / (b - 1.0) <= Tf / b
    Tm1 = np.expm1(am1 * np.log1p(1.0 / Xp)); acce = Vv * Xp * Tm1 / (b - 1.0) <= (1 + Tm1) / b
    zt_ = mp.zeta(a) - mp.zeta(a, ZIPF_M + 1); pt = float((mp.zeta(a, 2**53 + 1) - mp.zeta(a, ZIPF_M + 1)) / zt_)
    xg = G().zipf(a, 1_000_000)
    print(f"   zipf({a}): P(X > 2^53): exact truncated law {pt:.5f}; numpy Generator {np.mean(xg > 2.0**53):.5f}; rejection step re-run with float64 T {np.mean(Xp[accf] > 2.0**53):.5f}; with T-1 = expm1((a-1) log1p(1/X)) {np.mean(Xp[acce] > 2.0**53):.5f}")
# ---- multivariate: dirichlet, multinomial, multivariate_hypergeometric, multivariate_normal
print("---- multivariate distributions")
def marginal_tests(label, X, means, varss, mu4s, extra=""):
    n = X.shape[0]; zs = []; ok = True
    for j in range(X.shape[1]):
        m = mp.mpf(means[j]); v = mp.mpf(varss[j]); m4 = mp.mpf(mu4s[j])
        col = X[:, j][np.isfinite(X[:, j])]
        if v == 0:
            zs.append(f"[{j}] degenerate all=={float(m)}: {bool((col == float(m)).all())}"); ok = ok and bool((col == float(m)).all()); continue
        zm = float((mp.mpf(float(col.mean())) - m) / mp.sqrt(v / n))
        se = mp.sqrt((m4 - v**2) / n)
        zv = float((mp.mpf(float(col.var())) - v) / se) if se > 0 else 0.0
        zs.append(f"[{j}] mean z={zm:+.2f} var z={zv:+.2f}")
        if abs(zm) > ZMAX or abs(zv) > ZMAX: ok = False
    report(label + extra, ok, "; ".join(zs))
g_doc = np.random.Generator.dirichlet.__doc__
dir_zero_ok = "less than zero" in g_doc and "less than or equal to zero" not in g_doc
for alpha in [(10.0, 5.0, 3.0), (0.05, 0.05, 0.05), (1.0, 1.0), (0.02, 0.5, 3.0), (1e-3, 1e-3)]:
    a0 = sum(alpha)
    for api, X in (("Generator", G().dirichlet(alpha, N)), ("RandomState", R().dirichlet(alpha, N))):
        nanrows = int(np.isnan(X).any(axis=1).sum())
        rows = np.abs(X.sum(axis=1) - 1); rmax = float(np.nanmax(rows)) if rows.size else 0.0
        okr = nanrows == 0 and rmax < 1e-12 and bool((X >= 0).all() and (X <= 1).all())
        report(f"{api}.dirichlet({alpha}) rows are points of the simplex: no NaN, sum to 1 (docstring 'sum_i x_i = 1'), entries in [0, 1]", okr,
               f"NaN rows {nanrows}, max |sum-1| {rmax:.2e}, rows with sum > 1+1e-12: {int((X.sum(axis=1) > 1 + 1e-12).sum())}")
        means, varss, mu4s = [], [], []
        for ai in alpha:
            m, v, m4 = raw_to_central([mp.fprod((mp.mpf(ai) + r) / (mp.mpf(a0) + r) for r in range(k)) for k in (1, 2, 3, 4)])
            means.append(m); varss.append(v); mu4s.append(m4)
        marginal_tests(f"{api}.dirichlet({alpha}) marginals are beta(alpha_i, alpha0 - alpha_i): mean / variance z-tests per component (finite rows)", X, means, varss, mu4s,
                       " [small alpha: Generator stick-breaking path when alpha.max() < 0.1]" if max(alpha) < 0.1 else "")
def trinomial_cross(n_, p0, p1):
    """exact E[(X0-m0)^2 (X1-m1)^2] for the (X0, X1, rest) trinomial by enumeration"""
    m0 = n_ * p0; m1 = n_ * p1; s = 0.0; p2 = 1 - p0 - p1
    for i in range(n_ + 1):
        for j in range(n_ + 1 - i):
            k = n_ - i - j
            if (p0 == 0 and i) or (p1 == 0 and j) or (p2 <= 0 and k): continue
            lp = math.lgamma(n_ + 1) - math.lgamma(i + 1) - math.lgamma(j + 1) - math.lgamma(k + 1)
            lp += (i * math.log(p0) if i else 0) + (j * math.log(p1) if j else 0) + (k * math.log(p2) if k else 0)
            s += math.exp(lp) * (i - m0)**2 * (j - m1)**2
    return s
for n_, pv in [(20, [1/6.] * 6), (100, [0.1, 0.2, 0.7]), (7, [0.5, 0.0, 0.5]), (1, [0.3, 0.7])]:
    for api, X in (("Generator", G().multinomial(n_, pv, N)), ("RandomState", R().multinomial(n_, pv, N))):
        report(f"{api}.multinomial({n_}, {np.round(pv, 3).tolist()}) rows sum to n, integer, within [0, n]", bool((X.sum(axis=1) == n_).all() and X.dtype.kind in "iu" and (X >= 0).all() and (X <= n_).all()))
        means = [n_ * p for p in pv]; varss = [n_ * p * (1 - p) for p in pv]; mu4s = [n_ * p * (1 - p) * (1 + 3 * (n_ - 2) * p * (1 - p)) for p in pv]
        marginal_tests(f"{api}.multinomial({n_}, p) marginals binomial(n, p_i): mean / variance z-tests", X, means, varss, mu4s, " [zero probability never drawn]" if 0.0 in pv else "")
        if 0.0 in pv: report(f"{api}.multinomial: category with p=0 has count 0 always", bool((X[:, pv.index(0.0)] == 0).all()))
        c = float(np.cov(X[:, 0], X[:, 1])[0, 1]); ct = -n_ * pv[0] * pv[1]
        e4 = trinomial_cross(n_, pv[0], pv[1]); se = math.sqrt(max(e4 - ct**2, 0.0) / N)
        z = (c - ct) / se if se > 0 else 0.0
        report(f"{api}.multinomial({n_}, p) cov(X0, X1) = -n p0 p1 = {ct:.4g} (SE from the exact trinomial E[(X0-m0)^2 (X1-m1)^2])", abs(z) <= ZMAX if se > 0 else abs(c - ct) < 1e-12, f"sample cov {c:.5g} z={z:+.2f}")
for colors, ns in [([16, 8, 4], 6), ([5, 3, 2, 1], 11), ([1000, 1, 1], 500), ([3, 3, 3], 0), ([16, 8, 4], 28)]:
    tot = sum(colors)
    for method in ("marginals", "count"):
        X = G().multivariate_hypergeometric(colors, ns, N, method=method)
        report(f"Generator.multivariate_hypergeometric({colors}, {ns}, method='{method}') rows sum to nsample, 0 <= x_i <= colors_i, integer", bool((X.sum(axis=1) == ns).all() and (X >= 0).all() and (X <= np.array(colors)).all() and X.dtype.kind in "iu"))
        means, varss, mu4s = [], [], []
        for ci in colors:
            lo = max(0, ns - (tot - ci)); hi = min(ns, ci)
            lc = lambda n, k: math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            s = disc_moments(lambda k: lc(ci, k) + lc(tot - ci, ns - k) - lc(tot, ns), lo, hi)
            m, v, m4 = raw_to_central(s[1:]); means.append(m); varss.append(v if abs(v) > 1e-9 else 0); mu4s.append(m4)
        marginal_tests(f"Generator.multivariate_hypergeometric({colors}, {ns}, '{method}') marginals hypergeometric(c_i, N-c_i, nsample): mean / variance z-tests", X, means, varss, mu4s,
                       " [nsample = sum(colors): variate equals colors]" if ns == tot else (" [nsample=0]" if ns == 0 else ""))
report("Generator.multivariate_hypergeometric(colors, nsample > sum(colors)) raises ValueError (docstring 'nsample must not be greater than sum(colors)')", raises(lambda: G().multivariate_hypergeometric([16, 8, 4], 29), ValueError))
report("Generator.multivariate_hypergeometric method='bogus' raises ValueError ('Must be count or marginals')", raises(lambda: G().multivariate_hypergeometric([16, 8, 4], 6, method='bogus'), ValueError))
report("Generator.multivariate_hypergeometric negative color raises ValueError ('must be nonnegative')", raises(lambda: G().multivariate_hypergeometric([16, -1, 4], 6), ValueError))
report("Generator.multivariate_hypergeometric sum(colors) >= 10**9 with method='marginals' raises ValueError ('must be less than 10**9')", raises(lambda: G().multivariate_hypergeometric([10**9 - 5, 10], 6), ValueError))
mean3 = np.array([1.0, -2.0, 0.5]); cov3 = np.array([[4.0, 1.0, 0.5], [1.0, 2.0, -0.3], [0.5, -0.3, 1.0]])
def mvn_check(label, X, mean, cov):
    n = X.shape[0]; ok = True; det = []
    for j in range(3):
        zm = (X[:, j].mean() - mean[j]) / math.sqrt(cov[j, j] / n)
        if abs(zm) > ZMAX: ok = False
        det.append(f"m{j} z={zm:+.2f}")
    C = np.cov(X.T, bias=True)
    for i in range(3):
        for j in range(i, 3):
            se = math.sqrt((cov[i, i] * cov[j, j] + cov[i, j]**2) / n)   # Var of the sample covariance for a Gaussian
            z = (C[i, j] - cov[i, j]) / se
            if abs(z) > ZMAX: ok = False
            det.append(f"c{i}{j} z={z:+.2f}")
    report(label, ok, " ".join(det))
for method in ("svd", "cholesky", "eigh"):
    mvn_check(f"Generator.multivariate_normal 3-D method='{method}': means and all covariance entries within z (SE (s_ii s_jj + s_ij^2)/n)", G().multivariate_normal(mean3, cov3, N, method=method), mean3, cov3)
mvn_check("RandomState.multivariate_normal 3-D: means and covariance entries within z", R().multivariate_normal(mean3, cov3, N), mean3, cov3)
sing = np.array([[1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 2.0]])
for api, mk in (("Generator", lambda: G().multivariate_normal([0, 0, 0], sing, N)), ("RandomState", lambda: R().multivariate_normal([0, 0, 0], sing, N))):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always"); Xs = mk()
    d = float(np.abs(Xs[:, 0] - Xs[:, 1]).max()); zv = (Xs[:, 2].var() - 2) / math.sqrt(2 * 4 / N); z0 = (Xs[:, 0].var() - 1) / math.sqrt(2 / N)
    report(f"{api}.multivariate_normal with a singular PSD covariance (rank 2): no warning ('positive-semidefinite for proper sampling'), x0 == x1 to 1e-6, var x0 = 1, var x2 = 2",
           len(w) == 0 and d < 1e-6 and abs(zv) <= ZMAX and abs(z0) <= ZMAX, f"warnings {[str(x.message)[:40] for x in w]} max|x0-x1| {d:.2e} var z {z0:+.2f} {zv:+.2f}")
bad = np.array([[1.0, 2.0], [2.0, 1.0]])
for api, mk in (("Generator", G), ("RandomState", R)):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always"); mk().multivariate_normal([0, 0], bad, 10)
    report(f"{api}.multivariate_normal(check_valid='warn' default) on a non-PSD cov warns RuntimeWarning", any(issubclass(x.category, RuntimeWarning) for x in w), str([str(x.message) for x in w]))
    report(f"{api}.multivariate_normal(check_valid='raise') on a non-PSD cov raises ValueError", raises(lambda: mk().multivariate_normal([0, 0], bad, 10, check_valid='raise'), ValueError))
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always"); mk().multivariate_normal([0, 0], bad, 10, check_valid='ignore')
    report(f"{api}.multivariate_normal(check_valid='ignore') on a non-PSD cov is silent", len(w) == 0)
    report(f"{api}.multivariate_normal(check_valid='bogus') raises ValueError", raises(lambda: mk().multivariate_normal([0, 0], np.eye(2), 10, check_valid='bogus'), ValueError))
    report(f"{api}.multivariate_normal output shape: size=(3, 3) with N=2 -> (3, 3, 2); size=None -> (2,)", mk().multivariate_normal([1, 2], np.eye(2), (3, 3)).shape == (3, 3, 2) and mk().multivariate_normal([1, 2], np.eye(2)).shape == (2,))
    report(f"{api}.multivariate_normal: mean length != cov size raises ValueError; non-square cov raises ValueError", raises(lambda: mk().multivariate_normal([0, 0, 0], np.eye(2)), ValueError) and raises(lambda: mk().multivariate_normal([0, 0], np.ones((2, 3))), ValueError))
report("Generator.multivariate_normal(method='bogus') raises ValueError", raises(lambda: G().multivariate_normal([0, 0], np.eye(2), 10, method='bogus'), ValueError))
print(f"   distributions total {time.time() - T_START:.1f} s")

# ======================================================================
# documented boundary values and parameter validation
# ======================================================================
print("---- boundary values and parameter validation (docstring ranges)")
def allv(fn, val, n=200):
    try: x = np.asarray(fn(n)); return bool((x == val).all()), x[:3].tolist()
    except Exception as e: return False, f"raised {type(e).__name__}: {e}"
BOUND = [   # (label, generator-call, rs-call, expected value)   both APIs unless None
    ("binomial(n, p=0) == 0 ('p ... >= 0 and <= 1')", lambda o, n: o.binomial(10, 0.0, n), 0),
    ("binomial(n, p=1) == n", lambda o, n: o.binomial(10, 1.0, n), 10),
    ("binomial(n=0, p) == 0 ('n ... >= 0')", lambda o, n: o.binomial(0, 0.5, n), 0),
    ("poisson(lam=0) == 0 ('must be >= 0')", lambda o, n: o.poisson(0.0, n), 0),
    ("geometric(p=1) == 1 (first trial succeeds)", lambda o, n: o.geometric(1.0, n), 1),
    ("negative_binomial(n, p=1) == 0 (no failures)", lambda o, n: o.negative_binomial(3.5, 1.0, n), 0),
    ("hypergeometric(ngood=0, nbad, nsample) == 0", lambda o, n: o.hypergeometric(0, 5, 3, n), 0),
    ("hypergeometric(ngood, nbad=0, nsample) == nsample", lambda o, n: o.hypergeometric(5, 0, 3, n), 3),
    ("hypergeometric(ngood, nbad, nsample=ngood+nbad) == ngood ('less than or equal to the sum')", lambda o, n: o.hypergeometric(10, 5, 15, n), 10),
    ("logseries(p=0) == 1 ('Must be in the range [0, 1)')", lambda o, n: o.logseries(0.0, n), 1),
    ("gamma(shape=0) == 0 ('Must be non-negative')", lambda o, n: o.gamma(0.0, 1.0, n), 0.0),
    ("standard_gamma(shape=0) == 0", lambda o, n: o.standard_gamma(0.0, n), 0.0),
    ("gamma(shape, scale=0) == 0", lambda o, n: o.gamma(2.0, 0.0, n), 0.0),
    ("exponential(scale=0) == 0 ('Must be non-negative')", lambda o, n: o.exponential(0.0, n), 0.0),
    ("normal(loc, scale=0) == loc ('Must be non-negative')", lambda o, n: o.normal(3.0, 0.0, n), 3.0),
    ("lognormal(mean, sigma=0) == exp(mean)", lambda o, n: o.lognormal(0.0, 0.0, n), 1.0),
    ("laplace(loc, scale=0) == loc", lambda o, n: o.laplace(1.5, 0.0, n), 1.5),
    ("gumbel(loc, scale=0) == loc", lambda o, n: o.gumbel(1.5, 0.0, n), 1.5),
    ("logistic(loc, scale=0) == loc", lambda o, n: o.logistic(1.5, 0.0, n), 1.5),
    ("rayleigh(scale=0) == 0", lambda o, n: o.rayleigh(0.0, n), 0.0),
    ("uniform(low, high=low) == low ('When high == low, values of low will be returned')", lambda o, n: o.uniform(2.0, 2.0, n), 2.0),
    ("triangular(l, m, r) with a width-1e-300 interval stays in [l, r]", None, None),
]
for label, fn, val in BOUND:
    if fn is None: continue
    for api, mk in (("Generator", G), ("RandomState", R)):
        if api == "RandomState" and "hypergeometric" in label and False: pass
        ok, first = allv(lambda n: fn(mk(), n), val)
        report(f"{api}.{label}", ok, f"first {first}")
x = G().triangular(1.0, 1.0, 1.0 + 1e-15, 1000)
report("Generator.triangular(1, 1, 1+1e-15) stays in [left, right]", bool((x >= 1.0).all() and (x <= 1.0 + 1e-15).all()))
# errors (documented ranges)
ERR = [
    ("binomial(n=-1) raises ValueError ('>= 0')", lambda o: o.binomial(-1, 0.5), ValueError, "both"),
    ("binomial(p=1.5) raises ValueError", lambda o: o.binomial(10, 1.5), ValueError, "both"),
    ("binomial(p=nan) raises ValueError", lambda o: o.binomial(10, np.nan), ValueError, "both"),
    ("poisson(lam=-1) raises ValueError", lambda o: o.poisson(-1.0), ValueError, "both"),
    ("poisson(lam=1e19) raises ValueError ('lam is within 10 sigma of the maximum representable value')", lambda o: o.poisson(1e19), ValueError, "both"),
    ("geometric(p=0) raises ValueError", lambda o: o.geometric(0.0), ValueError, "both"),
    ("geometric(p=1.5) raises ValueError", lambda o: o.geometric(1.5), ValueError, "both"),
    ("negative_binomial(n=0) raises ValueError ('> 0')", lambda o: o.negative_binomial(0, 0.5), ValueError, "both"),
    ("negative_binomial(p=0) raises ValueError ('Must satisfy 0 < p <= 1')", lambda o: o.negative_binomial(1, 0.0), ValueError, "G"),
    ("hypergeometric(nsample > ngood + nbad) raises ValueError", lambda o: o.hypergeometric(10, 5, 16), ValueError, "both"),
    ("hypergeometric(ngood=10**9) raises ValueError ('Must be nonnegative and less than 10**9')", lambda o: o.hypergeometric(10**9, 1, 5), ValueError, "G"),
    ("hypergeometric(ngood=-1) raises ValueError", lambda o: o.hypergeometric(-1, 5, 2), ValueError, "both"),
    ("hypergeometric(nsample=0) raises ValueError (legacy: 'Must be at least 1')", lambda o: o.hypergeometric(10, 5, 0), ValueError, "R"),
    ("logseries(p=1) raises ValueError ('[0, 1)')", lambda o: o.logseries(1.0), ValueError, "both"),
    ("logseries(p=-0.1) raises ValueError", lambda o: o.logseries(-0.1), ValueError, "both"),
    ("logseries(p=nan) raises ValueError", lambda o: o.logseries(np.nan), ValueError, "both"),
    ("zipf(a=1) raises ValueError ('Must be greater than 1')", lambda o: o.zipf(1.0), ValueError, "both"),
    ("vonmises(kappa=-1) raises ValueError ('has to be >=0')", lambda o: o.vonmises(0.0, -1.0), ValueError, "both"),
    ("power(a=0) raises ValueError ('Raises ValueError If a <= 0')", lambda o: o.power(0.0), ValueError, "both"),
    ("pareto(a=0) raises ValueError ('Must be positive')", lambda o: o.pareto(0.0), ValueError, "both"),
    ("beta(a=0) raises ValueError ('positive (>0)')", lambda o: o.beta(0.0, 1.0), ValueError, "both"),
    ("gamma(shape=-1) raises ValueError", lambda o: o.gamma(-1.0), ValueError, "both"),
    ("normal(scale=-1) raises ValueError", lambda o: o.normal(0.0, -1.0), ValueError, "both"),
    ("uniform(low=3, high=2) raises ValueError ('high - low must be non-negative')", lambda o: o.uniform(3.0, 2.0), ValueError, "G"),
    ("triangular(left == right) raises ValueError ('must be larger than left')", lambda o: o.triangular(0, 0, 0), ValueError, "both"),
    ("triangular(mode > right) raises ValueError ('left <= mode <= right')", lambda o: o.triangular(0, 2, 1), ValueError, "both"),
    ("chisquare(df=0) raises ValueError ('must be > 0')", lambda o: o.chisquare(0.0), ValueError, "both"),
    ("noncentral_chisquare(df=0) raises ValueError", lambda o: o.noncentral_chisquare(0.0, 1.0), ValueError, "both"),
    ("noncentral_chisquare(nonc=-1) raises ValueError ('non-negative')", lambda o: o.noncentral_chisquare(1.0, -1.0), ValueError, "both"),
    ("f(dfden=0) raises ValueError", lambda o: o.f(1.0, 0.0), ValueError, "both"),
    ("noncentral_f(nonc=-1) raises ValueError ('>= 0')", lambda o: o.noncentral_f(1.0, 1.0, -1.0), ValueError, "both"),
    ("wald(scale=0) raises ValueError ('must be > 0')", lambda o: o.wald(1.0, 0.0), ValueError, "both"),
    ("wald(mean=0) raises ValueError ('must be > 0')", lambda o: o.wald(0.0, 1.0), ValueError, "both"),
    ("standard_t(df=0) raises ValueError ('must be > 0')", lambda o: o.standard_t(0.0), ValueError, "both"),
    ("weibull(a=-1) raises ValueError ('Must be nonnegative')", lambda o: o.weibull(-1.0), ValueError, "both"),
    ("rayleigh(scale=-1) raises ValueError", lambda o: o.rayleigh(-1.0), ValueError, "both"),
    ("dirichlet(alpha with a negative entry) raises ValueError", lambda o: o.dirichlet([-1.0, 1.0]), ValueError, "both"),
    ("multinomial(n=-1) raises ValueError", lambda o: o.multinomial(-1, [0.5, 0.5]), ValueError, "both"),
    ("multinomial(pvals containing NaN) raises ValueError ('pvals contains NaNs')", lambda o: o.multinomial(5, [0.5, np.nan]), ValueError, "both"),
    ("multinomial(sum(pvals[:-1]) > 1) raises ValueError", lambda o: o.multinomial(5, [0.7, 0.7, 0.1]), ValueError, "both"),
    ("multinomial(pvals < 0) raises ValueError", lambda o: o.multinomial(5, [-0.1, 1.1]), ValueError, "both"),
]
for label, fn, exc, which in ERR:
    for api, mk in (("Generator", G), ("RandomState", R)):
        if which == "G" and api != "Generator": continue
        if which == "R" and api != "RandomState": continue
        report(f"{api}.{label}", raises(lambda: fn(mk()), exc), exc_name(lambda: fn(mk())))
# version / API differences read from the installed docstrings
for api, cls, mk in (("Generator", np.random.Generator, G), ("RandomState", np.random.RandomState, R)):
    d = cls.dirichlet.__doc__
    if "less than or equal to zero" in d:
        report(f"{api}.dirichlet([0, 1]) raises ValueError (this build's docstring: 'less than or equal to zero')", raises(lambda: mk().dirichlet([0.0, 1.0]), ValueError), exc_name(lambda: mk().dirichlet([0.0, 1.0])))
    else:
        x = mk().dirichlet([0.0, 1.0], 100)
        report(f"{api}.dirichlet([0, 1]) allowed (this build's docstring: 'less than zero' raises): component with alpha=0 is always 0, the other is 1 (to 1 ulp)", bool((x[:, 0] == 0).all() and (np.abs(x[:, 1] - 1) <= 2.3e-16).all()), f"values of x1: {np.unique(x[:, 1]).tolist()}")
report("Generator.hypergeometric(nsample=0) == 0 (docstring 'nsample ... Must be nonnegative')", allv(lambda n: G().hypergeometric(10, 5, 0, n), 0)[0])
report("Generator.binomial(n=10.7) truncates n to 10 (docstring 'Floats are also accepted, but they will be truncated to integers'): same stream as n=10",
       np.array_equal(np.random.default_rng(5).binomial(10.7, 0.5, 1000), np.random.default_rng(5).binomial(10, 0.5, 1000)))
report("RandomState.binomial(n=10.7) truncates n to 10: same stream as n=10", np.array_equal(np.random.RandomState(5).binomial(10.7, 0.5, 1000), np.random.RandomState(5).binomial(10, 0.5, 1000)))
for api, mk in (("Generator", lambda s: np.random.default_rng(s)), ("RandomState", lambda s: np.random.RandomState(s))):
    report(f"{api}.multinomial: the last pvals entry is ignored (docstring 'the last element is always assumed to account for the remaining probability'): [0.6, 0.6] == [0.6, 0.4] stream",
           np.array_equal(mk(9).multinomial(5, [0.6, 0.6], 500), mk(9).multinomial(5, [0.6, 0.4], 500)))
x = R().uniform(3.0, 2.0, 1000)
print(f"   RandomState.uniform(3, 2) (docstring: 'If high < low, the results are officially undefined'): returns values in [{x.min():.4f}, {x.max():.4f}]")
for api, mk in (("Generator", G), ("RandomState", R)):
    x = mk().weibull(0.0, 100)
    print(f"   {api}.weibull(a=0) ('Must be nonnegative'): returns {np.unique(x).tolist()} (the code's convention; the a -> 0 limit of (-ln U)^(1/a) is not a distribution)")
# negative_binomial p = 0 on the legacy API: the legacy docstring allows p in [0, 1]
d = np.random.RandomState.negative_binomial.__doc__
x = R().negative_binomial(1, 0.0, 20)
report("RandomState.negative_binomial(1, p=0) (legacy docstring: 'p is in the interval [0, 1]') returns non-negative counts or raises",
       bool((x >= 0).all()), f"returned {np.unique(x).tolist()[:3]}; docstring mentions [0, 1]: {'interval [0, 1]' in d}")
# wald: support (0, inf) at an extreme mean/scale ratio (2.3.4 release note: 'fix negative samples generated by Wald distribution (#29609)')
for api, mk in (("Generator", G), ("RandomState", R)):
    x = mk().wald(1e9, 2.25, 100000)
    ok = bool((x > 0).all())
    fixed_note = "fixed in 2.3.4 for Generator (gh-29926)" if api == "Generator" else "legacy_wald keeps the old formula"
    report(f"{api}.wald(mean=1e9, scale=2.25): all samples > 0 (inverse Gaussian support) [{fixed_note}]", ok, f"n_negative {int((x < 0).sum())}, n_zero {int((x == 0).sum())}, min {x.min():.4g}")
for p in [1e-17, 1e-300]:
    for api, mk in (("Generator", G), ("RandomState", R)):
        x = mk().geometric(p, 20000)
        report(f"{api}.geometric(p={p}): no negative counts (support k >= 1; Generator clamps at int64 max since 1.25, changelog gh-23691 'Don't return negative values from Generator.geometric')",
               bool((x >= 1).all()), f"min {x.min()}, n_negative {int((x < 0).sum())}")
x = R().negative_binomial(1e10, 1e-10, 20)
report("RandomState.negative_binomial(1e10, 1e-10) (mean 1e20 > int64 max): returns non-negative counts or raises (Generator raises the documented ValueError)", bool((x >= 0).all()), f"returned {np.unique(x).tolist()[:3]}")
report("Generator.negative_binomial(1e10, 1e-10) raises ValueError (docstring constraint n(1-p)/p + 10 n sqrt(n) (1-p)/p < 2**63 - 1 - 10 sqrt(2**63 - 1))", raises(lambda: G().negative_binomial(1e10, 1e-10), ValueError))
for api, mk in (("Generator", G), ("RandomState", R)):
    x = mk().beta(1e-3, 1e-3, 100000)
    report(f"{api}.beta(1e-3, 1e-3): no NaN, all in [0, 1] (2.0 changelog gh-24267 'Fix generation of nan by beta')", bool(np.isfinite(x).all() and (x >= 0).all() and (x <= 1).all()), f"NaN {int(np.isnan(x).sum())}")
    ro = np.arange(10); ro.flags.writeable = False
    report(f"{api}.shuffle(read-only array) raises ValueError (1.23 changelog gh-20621 'Check writeable flag in shuffle')", raises(lambda: mk().shuffle(ro), ValueError))
    x = mk().multinomial(3 * 10**9, [0.3, 0.7], 50)
    report(f"{api}.multinomial(n=3e9) rows sum to n (n beyond int32; changelog gh-25119 'Make n a long int')", bool((x.sum(axis=1) == 3 * 10**9).all()) and abs(x[:, 0].mean() - 9e8) < 5 * math.sqrt(3e9 * 0.21 / 50))
ro = np.arange(10); ro.flags.writeable = False
report("Generator.permuted(x, out=read-only) raises ValueError", raises(lambda: G().permuted(np.arange(10), out=ro), ValueError))
a2 = np.arange(6).reshape(3, 2)
report("Generator.choice(2-D a, size=()) returns one row of shape (2,) ('output ndim = a.ndim - 1 + len(size)'; 2.0 changelog gh-26544)", (lambda: (lambda c: c.shape == (2,) and any((c == r).all() for r in a2))(G().choice(a2, size=())))() if not raises(lambda: G().choice(a2, size=()), Exception) else False,
       exc_name(lambda: G().choice(a2, size=())))
# hangs: legacy zipf with large a and old Generator.zipf (no a >= 1025 short-cut) -- run in a subprocess with a timeout
def hang_check(code, timeout=10):
    """run code in a subprocess: (hung, output-with-return-code)"""
    try:
        r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=timeout)
        return False, f"rc={r.returncode} " + r.stdout.strip()[:80] + r.stderr.strip()[-80:]
    except subprocess.TimeoutExpired:
        return True, f"no result within {timeout} s"
for api, code in (("Generator", "import numpy as np; print(np.random.default_rng(1).zipf(2000.0, 3))"), ("RandomState", "import numpy as np; print(np.random.RandomState(1).zipf(2000.0, 3))")):
    hung, out = hang_check(code)
    report(f"{api}.zipf(a=2000) returns (a > 1 is the only documented constraint; P(X > 1) < 3e-309) instead of hanging", not hung, out)
hung, out = hang_check("import numpy as np; print(np.random.RandomState(1).zipf(1024.0, 3))")
report("RandomState.zipf(a=1024) returns", not hung, out)

# ======================================================================
# Generator.integers and the legacy randint / random_integers / tomaxint
# ======================================================================
print("---- integers / randint")
def chi2_uniform(label, x, lo, hi):
    """chi-square goodness of fit of integer draws to uniform on [lo, hi] (exact p-value from mpmath gammainc)"""
    k = hi - lo + 1; cnt = np.bincount((np.asarray(x).astype(np.int64) - lo), minlength=k)
    e = len(x) / k; stat = float(((cnt - e)**2).sum() / e); pv = chi2_sf(stat, k - 1)
    report(f"{label}: chi-square uniformity over {k} cells (exact p-value)", pv >= PMIN and cnt.size == k, f"chi2={stat:.1f} df={k-1} p={pv:.3g}")
DT = [np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64]
for dt in DT:
    ii = np.iinfo(dt); g = G()
    x = g.integers(int(ii.min), int(ii.max) + 1, 2_000_000 if ii.bits <= 16 else N, dtype=dt)
    x2 = g.integers(int(ii.min), int(ii.max), N, dtype=dt, endpoint=True)
    ok = x.dtype == dt and x2.dtype == dt
    if ii.bits <= 16:
        ok = ok and int(x.min()) == ii.min and int(x.max()) == ii.max
        det = f"min {x.min()} max {x.max()}"
    else:
        half = (int(ii.min) + int(ii.max) + 1) // 2
        f_hi = float(np.mean(x >= half)) if ii.bits < 64 or dt == np.int64 else float(np.mean(x >= np.uint64(2**63)))
        lsb = float(np.mean((x.astype(np.uint64) & np.uint64(1)) == 1))
        z1 = (f_hi - 0.5) / math.sqrt(0.25 / N); z2 = (lsb - 0.5) / math.sqrt(0.25 / N); ok = ok and abs(z1) <= ZMAX and abs(z2) <= ZMAX
        det = f"top-half fraction z={z1:+.2f}, odd fraction z={z2:+.2f}"
    report(f"Generator.integers full range of {np.dtype(dt).name} (endpoint False with high = max+1, and endpoint=True with high = max): dtype kept, extremes / top bit / low bit uniform", ok, det)
    if ii.bits == 8: chi2_uniform(f"Generator.integers(full {np.dtype(dt).name})", x, int(ii.min), int(ii.max))
    report(f"Generator.integers(dtype={np.dtype(dt).name}): high = max+2 raises ValueError; low = min-1 raises ValueError",
           raises(lambda: G().integers(0, int(ii.max) + 2, dtype=dt), ValueError) and raises(lambda: G().integers(int(ii.min) - 1, 1, dtype=dt), ValueError))
    report(f"Generator.integers(dtype={np.dtype(dt).name}, endpoint=True): high = max+1 raises ValueError", raises(lambda: G().integers(0, int(ii.max) + 1, dtype=dt, endpoint=True), ValueError))
    r = R()
    y = r.randint(int(ii.min), int(ii.max) + 1, 2_000_000 if ii.bits <= 16 else N, dtype=dt)
    ok = y.dtype == dt
    if ii.bits <= 16: ok = ok and int(y.min()) == ii.min and int(y.max()) == ii.max
    else:
        half = (int(ii.min) + int(ii.max) + 1) // 2
        f_hi = float(np.mean(y >= half)) if dt != np.uint64 else float(np.mean(y >= np.uint64(2**63)))
        ok = ok and abs((f_hi - 0.5) / math.sqrt(0.25 / N)) <= ZMAX
    report(f"RandomState.randint full range of {np.dtype(dt).name}: dtype kept, extremes reached / top half 1/2", ok)
    report(f"RandomState.randint(dtype={np.dtype(dt).name}): high = max+2 raises ValueError", raises(lambda: R().randint(0, int(ii.max) + 2, dtype=dt), ValueError))
xb = G().integers(0, 2, N, dtype=bool); xb2 = G().integers(False, True, N, dtype=bool, endpoint=True)
zb = (xb.mean() - 0.5) / math.sqrt(0.25 / N); zb2 = (xb2.mean() - 0.5) / math.sqrt(0.25 / N)
report("Generator.integers(0, 2, dtype=bool) and (False, True, endpoint=True): dtype bool, P(True) = 1/2", xb.dtype == np.bool_ and xb2.dtype == np.bool_ and abs(zb) <= ZMAX and abs(zb2) <= ZMAX, f"z={zb:+.2f} {zb2:+.2f}")
report("Generator.integers(0, 3, dtype=bool) raises ValueError", raises(lambda: G().integers(0, 3, dtype=bool), ValueError))
yb = R().randint(0, 2, N, dtype=bool)
report("RandomState.randint(0, 2, dtype=bool): dtype bool, P(True) = 1/2", yb.dtype == np.bool_ and abs((yb.mean() - 0.5) / math.sqrt(0.25 / N)) <= ZMAX)
report("Generator.integers(5, 5) raises ValueError (empty [low, high))", raises(lambda: G().integers(5, 5), ValueError))
report("Generator.integers(5, 5, endpoint=True) == 5", allv(lambda n: G().integers(5, 5, n, endpoint=True), 5)[0])
report("Generator.integers(6, 5, endpoint=True) raises ValueError", raises(lambda: G().integers(6, 5, endpoint=True), ValueError))
report("Generator.integers(0, 10, dtype=float) raises TypeError (integer dtypes only)", raises(lambda: G().integers(0, 10, dtype=np.float64), TypeError), exc_name(lambda: G().integers(0, 10, dtype=np.float64)))
report("Generator.integers(0, 10, dtype='>i8') (non-native byteorder) raises ValueError ('Byteorder must be native')", raises(lambda: G().integers(0, 10, dtype='>i8'), (ValueError, TypeError)), exc_name(lambda: G().integers(0, 10, dtype='>i8')))
report("Generator.integers(0, 2**64, dtype=uint64) accepted; 2**64 + 1 raises ValueError", G().integers(0, 2**64, 5, dtype=np.uint64).dtype == np.uint64 and raises(lambda: G().integers(0, 2**64 + 1, dtype=np.uint64), ValueError))
x = G().integers(7, size=N)
report("Generator.integers(7) (high=None): 'results are from 0 to low' exclusive -> [0, 6], default dtype int64", x.dtype == np.int64 and int(x.min()) == 0 and int(x.max()) == 6)
x = G().integers(7, size=N, endpoint=True)
report("Generator.integers(7, endpoint=True) (high=None): [0, 7]", int(x.min()) == 0 and int(x.max()) == 7)
v = G().integers(0, 10)
report("Generator.integers(0, 10) with size=None returns a numpy int64 scalar (docstring 'single value is returned')", isinstance(v, np.int64) and 0 <= v < 10, type(v).__name__)
report("Generator.integers(0, 10, size=0) returns an empty int64 array; size=(2, 0) keeps the shape", G().integers(0, 10, 0).shape == (0,) and G().integers(0, 10, (2, 0)).shape == (2, 0))
lo_b = np.array([1, 3, 5, 7]); hi_b = np.array([[10], [20]])
Xb = np.stack([G().integers(lo_b, hi_b, dtype=np.uint8) for _ in range(3000)])
okb = Xb.shape[1:] == (2, 4) and Xb.dtype == np.uint8 and bool((Xb >= lo_b).all() and (Xb < hi_b).all()) and bool((Xb.min(axis=0) == np.broadcast_to(lo_b, (2, 4))).all() and (Xb.max(axis=0) == np.broadcast_to(hi_b - 1, (2, 4))).all())
report("Generator.integers([1, 3, 5, 7], [[10], [20]], dtype=uint8) (docstring example): shape (2, 4), each cell covers exactly [low_j, high_i - 1]", okb)
Xb = np.stack([G().integers(lo_b, hi_b, endpoint=True) for _ in range(3000)])
report("Generator.integers(broadcast, endpoint=True): each cell covers exactly [low_j, high_i]", bool((Xb.min(axis=0) == np.broadcast_to(lo_b, (2, 4))).all() and (Xb.max(axis=0) == np.broadcast_to(hi_b, (2, 4))).all()))
report("Generator.integers(broadcast) with a low > high cell raises ValueError", raises(lambda: G().integers([0, 10], [5, 5]), ValueError))
Yb = np.stack([R().randint(lo_b, hi_b, dtype=np.uint8) for _ in range(3000)])
report("RandomState.randint([1, 3, 5, 7], [[10], [20]]) broadcasting: each cell covers exactly [low_j, high_i - 1]", Yb.shape[1:] == (2, 4) and bool((Yb.min(axis=0) == np.broadcast_to(lo_b, (2, 4))).all() and (Yb.max(axis=0) == np.broadcast_to(hi_b - 1, (2, 4))).all()))
chi2_uniform("Generator.integers(0, 10)", G().integers(0, 10, N), 0, 9)
chi2_uniform("Generator.integers(-3, 3, endpoint=True, dtype=int16)", G().integers(-3, 3, N, endpoint=True, dtype=np.int16), -3, 3)
chi2_uniform("Generator.integers(0, 7, dtype=int8)", G().integers(0, 7, N, dtype=np.int8), 0, 6)
chi2_uniform("Generator.integers(0, 1000)", G().integers(0, 1000, N), 0, 999)
chi2_uniform("Generator.integers(0, 3*2**61) // 2**61 (non-power-of-two range near 2**63)", G().integers(0, 3 * 2**61, N) // 2**61, 0, 2)
chi2_uniform("Generator.integers(0, 3*2**62, dtype=uint64) // 2**62", (G().integers(0, 3 * 2**62, N, dtype=np.uint64) // np.uint64(2**62)).astype(np.int64), 0, 2)
chi2_uniform("Generator.integers(0, 10**12 + 7) // (10**11 + 1)", G().integers(0, 10**12 + 7, N) // (10**11 + 1), 0, 9)
chi2_uniform("Generator.integers(0, 2**31 + 5, dtype=uint32) mod 7 [approximately uniform: 2**31+5 cells]", (G().integers(0, 2**31 + 5, N, dtype=np.uint32) % 7).astype(np.int64), 0, 6)
chi2_uniform("RandomState.randint(0, 10)", R().randint(0, 10, N), 0, 9)
chi2_uniform("RandomState.randint(0, 3*2**61) // 2**61", R().randint(0, 3 * 2**61, N) // 2**61, 0, 2)
chi2_uniform("RandomState.randint(-3, 4, dtype=int8)", R().randint(-3, 4, N, dtype=np.int8), -3, 3)
x = R().randint(7, size=N)
report("RandomState.randint(7) (high=None): [0, 6], default dtype np.int_ ('int')", x.dtype == np.dtype(int) and int(x.min()) == 0 and int(x.max()) == 6)
report("RandomState.randint(5, 5) raises ValueError", raises(lambda: R().randint(5, 5), ValueError))
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always"); x = R().random_integers(1, 6, N); x1 = R().random_integers(6, size=N)
report("RandomState.random_integers(1, 6): closed interval [1, 6] ('inclusive'); random_integers(6) -> [1, 6]; DeprecationWarning ('This function has been deprecated')",
       int(x.min()) == 1 and int(x.max()) == 6 and int(x1.min()) == 1 and int(x1.max()) == 6 and any(issubclass(q.category, DeprecationWarning) for q in w))
chi2_uniform("RandomState.random_integers(1, 6)", x, 1, 6)
x = R().tomaxint(N)
lim = np.iinfo(np.dtype("long")).max
report(f"RandomState.tomaxint(): 'uniformly distributed random integers in the interval [0, np.iinfo(long).max]' = [0, {lim}]; top half fraction 1/2",
       int(x.min()) >= 0 and int(x.max()) <= lim and abs((np.mean(x > lim // 2) - 0.5) / math.sqrt(0.25 / N)) <= ZMAX, f"dtype {x.dtype}")

# ======================================================================
# random(dtype, out), the uint64 -> double mapping, legacy random_sample / gauss vs CPython
# ======================================================================
print("---- random(dtype, out) and the raw-to-float mappings")
g = G(); out = np.empty(1000)
r_ = g.random(out=out)
report("Generator.random(out=a) fills a in place and returns a itself", r_ is out and bool((out >= 0).all() and (out < 1).all()) and len(np.unique(out)) == 1000)
out32 = np.empty((10, 10), dtype=np.float32)
report("Generator.random(size, dtype=float32, out=float32 array) accepted and returned", G().random((10, 10), dtype=np.float32, out=out32) is out32)
report("Generator.random(dtype=float32, out=float64 array) raises TypeError ('must match the type')", raises(lambda: G().random(dtype=np.float32, out=np.empty(5)), TypeError), exc_name(lambda: G().random(dtype=np.float32, out=np.empty(5))))
report("Generator.random(size=(3,), out=array of shape (4,)) raises ValueError ('same shape as the provided size')", raises(lambda: G().random(3, out=np.empty(4)), ValueError))
report("Generator.random(out=non-contiguous) raises ValueError", raises(lambda: G().random(out=np.empty(10)[::2]), ValueError), exc_name(lambda: G().random(out=np.empty(10)[::2])))
report("Generator.random(dtype=int32) raises TypeError ('only float64 and float32 are supported')", raises(lambda: G().random(5, dtype=np.int32), TypeError), exc_name(lambda: G().random(5, dtype=np.int32)))
report("Generator.random() with size=None returns a Python float (docstring example 'type(rfloat) -> float')", isinstance(G().random(), float))
for meth, call in [("standard_normal", lambda g, o: g.standard_normal(out=o)), ("standard_exponential", lambda g, o: g.standard_exponential(out=o)), ("standard_gamma(2.0)", lambda g, o: g.standard_gamma(2.0, out=o))]:
    o = np.empty(50); o32 = np.empty(50, dtype=np.float32)
    ok = call(G(), o) is o and np.isfinite(o).all()
    ok32 = {"standard_normal": lambda: G().standard_normal(dtype=np.float32, out=o32), "standard_exponential": lambda: G().standard_exponential(dtype=np.float32, out=o32), "standard_gamma(2.0)": lambda: G().standard_gamma(2.0, dtype=np.float32, out=o32)}[meth]() is o32
    report(f"Generator.{meth}(out=) returns out (float64 and float32)", ok and ok32)
    s1 = seed(); a = np.empty(20); call(np.random.default_rng(s1), a)
    b = {"standard_normal": lambda g: g.standard_normal(20), "standard_exponential": lambda g: g.standard_exponential(20), "standard_gamma(2.0)": lambda g: g.standard_gamma(2.0, 20)}[meth](np.random.default_rng(s1))
    report(f"Generator.{meth}(out=a) writes the same values as the size= call", np.array_equal(a, b))
report("Generator.standard_normal(dtype=int64) raises TypeError", raises(lambda: G().standard_normal(3, dtype=np.int64), TypeError))
sb = seed(); xb = np.random.default_rng(sb).standard_exponential(5, method='bogus') if not raises(lambda: G().standard_exponential(3, method='bogus'), Exception) else None
print(f"   Generator.standard_exponential(method='bogus') (docstring: \"Either 'inv' or 'zig'\"): " + ("raises" if xb is None else f"accepted silently; equals the 'inv' stream: {np.array_equal(xb, np.random.default_rng(sb).standard_exponential(5, method='inv'))}"))
s1 = seed()
raw = np.random.PCG64(s1).random_raw(64)
d = np.random.Generator(np.random.PCG64(s1)).random(64)
ref = np.array([(int(v) >> 11) * 2.0**-53 for v in raw])
report("Generator(PCG64).random() == (raw >> 11) * 2**-53 (next_double of the bit generator; 53-bit resolution)", np.array_equal(d, ref))
f32 = np.random.Generator(np.random.PCG64(s1)).random(64, dtype=np.float32)
w32 = []
for v in raw[:32]: v = int(v); w32 += [v & M32, v >> 32]          # pcg64_next32: low word first, high word buffered
ref32 = np.array([(u >> 8) * 2.0**-24 for u in w32], dtype=np.float32)
report("Generator(PCG64).random(dtype=float32) == (next_uint32 >> 8) * 2**-24 with next_uint32 = low then high half of each raw word", np.array_equal(f32, ref32))
# legacy RandomState: MT19937 + res53 doubles + polar Gaussian, against CPython's random module (same MT19937 and res53)
for s in [0, 12345, 2**32 - 1]:
    rs = np.random.RandomState(s); st = rs.get_state()
    py = pyrandom.Random(); py.setstate((3, tuple(int(k) for k in st[1]) + (int(st[2]),), None))
    a = rs.random_sample(500); b = np.array([py.random() for _ in range(500)])
    report(f"RandomState({s}).random_sample == CPython random.random() from the same MT19937 state (res53: (a>>5)*2**26 + (b>>6)) / 2**53", np.array_equal(a, b))
    rs = np.random.RandomState(s); st = rs.get_state()
    py = pyrandom.Random(); py.setstate((3, tuple(int(k) for k in st[1]) + (int(st[2]),), None))
    gs = rs.standard_normal(301); out = []; cache = None
    while len(out) < 301:
        if cache is not None: out.append(cache); cache = None; continue
        while True:
            x1 = 2.0 * py.random() - 1.0; x2 = 2.0 * py.random() - 1.0; r2 = x1 * x1 + x2 * x2
            if r2 < 1.0 and r2 != 0.0: break
        f = math.sqrt(-2.0 * math.log(r2) / r2); cache = f * x1; out.append(f * x2)
    report(f"RandomState({s}).standard_normal == Marsaglia polar method on CPython's MT19937 doubles (returns f*x2, caches f*x1)", np.array_equal(gs, np.array(out)), f"max diff {np.max(np.abs(gs - np.array(out))):.2e}")
rs = np.random.RandomState(3)
report("RandomState: random / random_sample / rand are the same stream (documented aliases)",
       all(np.array_equal(getattr(np.random.RandomState(3), m)(*a), np.random.RandomState(3).random_sample(20)) for m, a in [("random", (20,)), ("rand", (20,))]))
al = []
for m in ("ranf", "sample", "random", "random_sample", "rand"):
    if hasattr(np.random, m):
        np.random.seed(3); al.append(np.array_equal(getattr(np.random, m)(20), np.random.RandomState(3).random_sample(20)))
report("module-level np.random.ranf / sample / random / random_sample / rand (legacy aliases) after np.random.seed(3) == RandomState(3).random_sample", all(al) and len(al) >= 3, f"{len(al)} aliases present")
report("RandomState: randn(20) == standard_normal(20) (documented equivalence)", np.array_equal(np.random.RandomState(4).randn(20), np.random.RandomState(4).standard_normal(20)))
np.random.seed(77); a = np.random.random_sample(10); b = np.random.RandomState(77).random_sample(10)
report("np.random.seed(s) + np.random.random_sample == RandomState(s).random_sample (module-level singleton)", np.array_equal(a, b))
if V >= (1, 24):
    orig = np.random.get_bit_generator(); np.random.set_bit_generator(np.random.PCG64(123))
    a = np.random.random_sample(20); np.random.set_bit_generator(orig)
    b = np.random.Generator(np.random.PCG64(123)).random(20)
    report("np.random.set_bit_generator(PCG64(123)) (1.24 release note): module random_sample equals Generator(PCG64(123)).random (same next_double)", np.array_equal(a, b))
else:
    report("np.random.set_bit_generator absent before 1.24 (added in 1.24.0, release-noted)", not hasattr(np.random, "set_bit_generator"))

# ======================================================================
# choice
# ======================================================================
print("---- choice")
for api, mk in (("Generator", G), ("RandomState", R)):
    ok_tol = True
    try: mk().choice(3, 5, p=[0.2, 0.3, 0.5 + 1e-9])
    except Exception: ok_tol = False
    report(f"{api}.choice: p summing to 1 + 1e-9 is accepted (tolerance sqrt(eps) = 1.5e-8)", ok_tol)
    report(f"{api}.choice: p summing to 1 + 1e-7 raises ValueError ('probabilities do not sum to 1')", raises(lambda: mk().choice(3, 5, p=[0.2, 0.3, 0.5 + 1e-7]), ValueError))
    report(f"{api}.choice: negative p raises ValueError; NaN p raises ValueError; 2-D p raises ValueError; len(p) != len(a) raises ValueError",
           raises(lambda: mk().choice(3, 5, p=[0.7, -0.2, 0.5]), ValueError) and raises(lambda: mk().choice(3, 5, p=[0.5, np.nan, 0.5]), ValueError)
           and raises(lambda: mk().choice(3, 2, p=[[0.5, 0.5, 0]]), ValueError) and raises(lambda: mk().choice(3, 2, p=[0.5, 0.5]), ValueError))
    report(f"{api}.choice: empty a with size > 0 raises ValueError; choice([], 0) and choice(0, 0) return empty; choice(-1) raises ValueError",
           raises(lambda: mk().choice([], 3), ValueError) and mk().choice([], 0).size == 0 and mk().choice(0, 0).size == 0 and raises(lambda: mk().choice(-1, 1), ValueError))
    report(f"{api}.choice(3, 4, replace=False) raises ValueError (sample larger than population)", raises(lambda: mk().choice(3, 4, replace=False), ValueError))
    x = mk().choice(5, N, p=[0.5, 0.0, 0.5, 0.0, 0.0])
    report(f"{api}.choice: zero-probability entries are never chosen (400k draws); fractions of the two p=0.5 entries 1/2",
           bool(np.isin(x, [0, 2]).all()) and abs((np.mean(x == 0) - 0.5) / math.sqrt(0.25 / N)) <= ZMAX)
    xs = [tuple(sorted(mk().choice(5, 2, replace=False, p=[0.5, 0, 0.5, 0, 0]))) for _ in range(200)]
    report(f"{api}.choice(5, 2, replace=False, p with two non-zero entries) always returns exactly those two", set(xs) == {(0, 2)})
    report(f"{api}.choice(5, 3, replace=False, p with two non-zero entries) raises ValueError ('Fewer non-zero entries in p than size')", raises(lambda: mk().choice(5, 3, replace=False, p=[0.5, 0, 0.5, 0, 0]), ValueError))
    v = mk().choice(5)
    report(f"{api}.choice(5) with size=None returns a scalar integer", np.ndim(v) == 0 and 0 <= v < 5, type(v).__name__)
    # p frequencies
    pv = [0.1, 0.05, 0.25, 0.6]; x = mk().choice(4, N, p=pv); cnt = np.bincount(x, minlength=4)
    stat = float(sum((cnt[i] - N * pv[i])**2 / (N * pv[i]) for i in range(4))); pval = chi2_sf(stat, 3)
    report(f"{api}.choice(4, p={pv}) frequencies: chi-square vs p (exact p-value)", pval >= PMIN, f"chi2={stat:.2f} p={pval:.3g}")
    # replace=False with p: successive weighted sampling; exact law of the ordered pair (i, j): p_i p_j / (1 - p_i)
    pv = [0.1, 0.2, 0.3, 0.4]; M = 60000
    pairs = np.array([mk().choice(4, 2, replace=False, p=pv) for _ in range(M)])
    cnt = {}
    for a_, b_ in pairs.tolist(): cnt[(a_, b_)] = cnt.get((a_, b_), 0) + 1
    exp_ = {(i, j): M * pv[i] * pv[j] / (1 - pv[i]) for i in range(4) for j in range(4) if i != j}
    stat = sum((cnt.get(k, 0) - e)**2 / e for k, e in exp_.items()); pval = chi2_sf(stat, 11)
    report(f"{api}.choice(4, 2, replace=False, p) ordered pairs follow successive weighted sampling P(i, j) = p_i p_j / (1 - p_i) ({M} calls, chi-square 11 df)",
           pval >= PMIN and set(cnt) <= set(exp_), f"chi2={stat:.2f} p={pval:.3g}")
    # replace=False uniform: every 3-subset in order equally likely
    M = 60000; tri = [tuple(mk().choice(5, 3, replace=False)) for _ in range(M)]
    cnt = {}
    for t in tri: cnt[t] = cnt.get(t, 0) + 1
    e = M / 60; stat = sum((c - e)**2 / e for c in cnt.values()) + (60 - len(cnt)) * e; pval = chi2_sf(stat, 59)
    report(f"{api}.choice(5, 3, replace=False): all 60 ordered triples equally likely ({M} calls, chi-square 59 df)", pval >= PMIN and len(cnt) == 60, f"chi2={stat:.1f} p={pval:.3g}")
    A = np.arange(12).reshape(4, 3)
    if api == "RandomState":
        report("RandomState.choice(2-D array) raises ValueError (legacy docstring: 'a : 1-D array-like or int')", raises(lambda: mk().choice(A, 2), ValueError)); continue
    c = mk().choice(A, 2, replace=False)
    report(f"{api}.choice(2-D array, 2, replace=False) selects whole rows (axis 0)", c.shape == (2, 3) and all(any((row == r).all() for r in A) for row in c) and not (c[0] == c[1]).all())
a2 = np.arange(12).reshape(4, 3)
c = G().choice(a2, 5, axis=1)
report("Generator.choice(a, 5, axis=1): shape (4, 5), every output column is a column of a ('size shape will be inserted into the axis dimension')", c.shape == (4, 5) and all(any((c[:, k] == a2[:, j]).all() for j in range(3)) for k in range(5)))
c = G().choice(a2, (2, 2), axis=1)
report("Generator.choice(a, (2, 2), axis=1): output ndim = a.ndim - 1 + len(size) -> shape (4, 2, 2)", c.shape == (4, 2, 2))
c = G().choice(a2, 2, replace=False, axis=1)
report("Generator.choice(a, 2, replace=False, axis=1): two distinct columns", c.shape == (4, 2) and not (c[:, 0] == c[:, 1]).all())
report("Generator.choice(axis=2) on a 2-D array raises AxisError (ValueError / IndexError subclass)", raises(lambda: G().choice(a2, 2, axis=2), (ValueError, IndexError)))
# shuffle=False: still a uniform sample without replacement (inclusion probability k/n)
for n_, k_, M in [(20, 5, 40000), (100000, 10, 20000)]:
    samples = np.array([G().choice(n_, k_, replace=False, shuffle=False) for _ in range(M)])
    uniq = all(len(set(r)) == k_ for r in samples[:2000].tolist())
    bins = np.bincount((samples.ravel() * 10) // n_, minlength=10); e = M * k_ / 10
    stat = float(((bins - e)**2 / e).sum()); pval = chi2_sf(stat, 9)
    report(f"Generator.choice({n_}, {k_}, replace=False, shuffle=False) ({'Floyd' if n_ > 10000 else 'partial Fisher-Yates'} path): distinct entries, inclusion probability k/n (decile chi-square)", uniq and pval >= PMIN, f"chi2={stat:.1f} p={pval:.3g}")
    samples2 = np.array([G().choice(n_, k_, replace=False) for _ in range(M)])
    pos0 = np.bincount((samples2[:, 0] * 10) // n_, minlength=10); e0 = M / 10
    stat = float(((pos0 - e0)**2 / e0).sum()); pval = chi2_sf(stat, 9)
    report(f"Generator.choice({n_}, {k_}, replace=False) (shuffle=True): the first element is uniform over the population (decile chi-square)", pval >= PMIN, f"chi2={stat:.1f} p={pval:.3g}")

# ======================================================================
# shuffle / permutation / permuted
# ======================================================================
print("---- shuffle / permutation / permuted")
perms = list(itertools.permutations(range(4))); pidx = {p: i for i, p in enumerate(perms)}
def perm_chi2(label, rows):
    cnt = np.zeros(24)
    for r in rows: cnt[pidx[tuple(r)]] += 1
    e = len(rows) / 24; stat = float(((cnt - e)**2 / e).sum()); pval = chi2_sf(stat, 23)
    report(f"{label}: all 24 permutations of 4 equally likely ({len(rows)} draws, chi-square 23 df)", pval >= PMIN, f"chi2={stat:.1f} p={pval:.3g}")
X = G().permuted(np.tile(np.arange(4), (N, 1)), axis=1)
perm_chi2("Generator.permuted(tile(arange(4)), axis=1): each row shuffled independently", X.tolist())
for api, mk in (("Generator", G), ("RandomState", R)):
    rows = []
    rng = mk()
    for _ in range(48000):
        a = np.arange(4); rng.shuffle(a); rows.append(a.tolist())
    perm_chi2(f"{api}.shuffle(arange(4))", rows)
    rng = mk(); rows = [rng.permutation(4).tolist() for _ in range(48000)]
    perm_chi2(f"{api}.permutation(4)", rows)
    A = np.arange(20).reshape(5, 4); B = A.copy(); mk().shuffle(B)
    report(f"{api}.shuffle(2-D) shuffles rows only: rows intact, same multiset of rows", sorted(map(tuple, B.tolist())) == sorted(map(tuple, A.tolist())))
    L = list(range(10)); r_ = mk().shuffle(L)
    report(f"{api}.shuffle(list) works in place and returns None", r_ is None and sorted(L) == list(range(10)))
    x = np.arange(10); p_ = mk().permutation(x)
    report(f"{api}.permutation(array) returns a shuffled copy and leaves the input unchanged", (x == np.arange(10)).all() and sorted(p_.tolist()) == list(range(10)) and p_ is not x)
    report(f"{api}.permutation(2-D) permutes rows only", sorted(map(tuple, mk().permutation(A).tolist())) == sorted(map(tuple, A.tolist())))
    report(f"{api}.shuffle of a 0-d array raises TypeError", raises(lambda: mk().shuffle(np.array(5)), TypeError), exc_name(lambda: mk().shuffle(np.array(5))))
    o = np.array([{"a": 1}, [2], "3", 4.0], dtype=object); o2 = o.copy(); mk().shuffle(o2)
    report(f"{api}.shuffle(object array) permutes the object references", sorted(map(repr, o2.tolist())) == sorted(map(repr, o.tolist())))
    v = np.arange(20)[::2].copy(); base = np.arange(20); view = base[::2]; mk().shuffle(view)
    report(f"{api}.shuffle(non-contiguous view) shuffles the viewed elements in the base array and leaves the others", sorted(base[::2].tolist()) == list(range(0, 20, 2)) and (base[1::2] == np.arange(1, 20, 2)).all())
    m = np.arange(24).reshape(4, 6); m2 = m.copy(); mk().shuffle(m2[:, 0])
    report(f"{api}.shuffle(column view) shuffles only that column", sorted(m2[:, 0].tolist()) == [0, 6, 12, 18] and (m2[:, 1:] == m[:, 1:]).all())
A = np.arange(24).reshape(4, 6)
B = A.copy(); G().shuffle(B, axis=1)
report("Generator.shuffle(x, axis=1): columns permuted as whole columns (same permutation for every row)", all(sorted(B[:, j].tolist()) in [sorted(A[:, k].tolist()) for k in range(6)] for j in range(6)) and len({tuple((B[i] - A[i, 0]).tolist()) for i in range(4)}) == 1)
C = G().permutation(A, axis=1)
report("Generator.permutation(x, axis=1): columns permuted as a whole, input unchanged", (A == np.arange(24).reshape(4, 6)).all() and len({tuple((C[i] - A[i, 0]).tolist()) for i in range(4)}) == 1)
P = G().permuted(A, axis=1)
report("Generator.permuted(x, axis=1): 'each slice along the given axis is shuffled independently': rows keep their elements; x unchanged",
       all(sorted(P[i].tolist()) == A[i].tolist() for i in range(4)) and (A == np.arange(24).reshape(4, 6)).all())
P0 = G().permuted(A, axis=0)
report("Generator.permuted(x, axis=0): each column keeps its elements", all(sorted(P0[:, j].tolist()) == A[:, j].tolist() for j in range(6)))
Pn = G().permuted(A)
report("Generator.permuted(x) (axis=None): 'the flattened array is shuffled' -> same shape, all 24 values, elements move across rows", Pn.shape == A.shape and sorted(Pn.ravel().tolist()) == list(range(24)) and any(sorted(Pn[i].tolist()) != A[i].tolist() for i in range(4)))
Xo = A.copy(); r_ = G().permuted(Xo, axis=1, out=Xo)
report("Generator.permuted(x, axis=1, out=x): shuffles in place and returns out", r_ is Xo and all(sorted(Xo[i].tolist()) == A[i].tolist() for i in range(4)))
report("Generator.permuted(out= of the wrong shape) raises ValueError", raises(lambda: G().permuted(A, out=np.empty((6, 4), dtype=A.dtype)), ValueError))
report("Generator.permutation(5, axis=1) / permutation(scalar array) raise (AxisError for 0-d: docstring example)", raises(lambda: G().permutation(np.array(5)), (ValueError, IndexError, TypeError)))
report("Generator.permutation(int) = shuffled arange", sorted(G().permutation(50).tolist()) == list(range(50)))

# ======================================================================
# bytes
# ======================================================================
print("---- bytes")
for api, mk in (("Generator", G), ("RandomState", R)):
    b = mk().bytes(N)
    cnt = np.bincount(np.frombuffer(b, dtype=np.uint8), minlength=256); e = N / 256
    stat = float(((cnt - e)**2 / e).sum()); pval = chi2_sf(stat, 255)
    report(f"{api}.bytes(400000): type bytes, length exact, byte values uniform (chi-square 255 df)", isinstance(b, bytes) and len(b) == N and pval >= PMIN, f"chi2={stat:.1f} p={pval:.3g}")
    report(f"{api}.bytes(0) == b'' and bytes(1), bytes(7) have exact lengths", mk().bytes(0) == b"" and len(mk().bytes(1)) == 1 and len(mk().bytes(7)) == 7)

# ======================================================================
# SeedSequence: C++ reference vectors, pure-Python reimplementation, spawn
# ======================================================================
print("---- SeedSequence")
def ss_words(x):
    if isinstance(x, (int, np.integer)):
        x = int(x)
        if x < 0: raise ValueError("negative")
        if x == 0: return [0]
        w = []
        while x > 0: w.append(x & M32); x >>= 32
        return w
    out = []
    for v in x: out += ss_words(v)
    return out
class PySeedSeq:
    """pure-Python port of O'Neill's seed_seq hash as described in numpy.random.bit_generator.SeedSequence"""
    INIT_A = 0x43b0d7e5; MULT_A = 0x931e8875; INIT_B = 0x8b51f9dd; MULT_B = 0x58f38ded; MIX_L = 0xca01f9dd; MIX_R = 0x4973f715
    def __init__(self, entropy, spawn_key=(), pool_size=4):
        run = ss_words(entropy); sp = ss_words(list(spawn_key)) if len(spawn_key) else []
        if sp and len(run) < pool_size: run = run + [0] * (pool_size - len(run))
        ent = run + sp; hc = [self.INIT_A]
        def hashmix(v):
            v = (v ^ hc[0]) & M32; hc[0] = (hc[0] * self.MULT_A) & M32; v = (v * hc[0]) & M32; return v ^ (v >> 16)
        def mix(x, y):
            r = (self.MIX_L * x - self.MIX_R * y) & M32; return r ^ (r >> 16)
        pool = [hashmix(ent[i] if i < len(ent) else 0) for i in range(pool_size)]
        for i_src in range(pool_size):
            for i_dst in range(pool_size):
                if i_src != i_dst: pool[i_dst] = mix(pool[i_dst], hashmix(pool[i_src]))
        for i_src in range(pool_size, len(ent)):
            for i_dst in range(pool_size): pool[i_dst] = mix(pool[i_dst], hashmix(ent[i_src]))
        self.pool = pool
    def generate_state(self, n, u64=False):
        nw = 2 * n if u64 else n; hc = self.INIT_B; out = []
        for i in range(nw):
            d = self.pool[i % len(self.pool)] ^ hc; hc = (hc * self.MULT_B) & M32; d = (d * hc) & M32; out.append(d ^ (d >> 16))
        return [out[2*i] | (out[2*i + 1] << 32) for i in range(n)] if u64 else out
CPP_IN = [[3735928559, 195939070, 229505742, 305419896], [3668361503, 4165561550, 1661411377, 3634257570], [164546577, 4166754639, 1765190214, 1303880213],
          [446610472, 3941463886, 522937693, 1882353782], [1864922766, 1719732118, 3882010307, 1776744564], [4141682960, 3310988675, 553637289, 902896340],
          [1134851934, 2352871630, 3699409824, 2648159817], [1240956131, 3107113773, 1283198141, 1924506131], [2669565031, 579818610, 3042504477, 2774880435],
          [2766103236, 2883057919, 4029656435, 862374500]]
CPP_OUT = [[3914649087, 576849849, 3593928901, 2229911004], [2240804226, 3691353228, 1365957195, 2654016646], [3562296087, 3191708229, 1147942216, 3726991905],
           [1403443605, 3591372999, 1291086759, 441919183], [1086200464, 2191331643, 560336446, 3658716651], [3249937430, 2346751812, 847844327, 2996632307],
           [2584285912, 4034195531, 3523502488, 169742686], [959045797, 3875435559, 1886309314, 359682705], [3978441347, 432478529, 3223635119, 138903045],
           [296367413, 4262059219, 13109864, 3283683422]]
CPP_OUT64 = [[2477551240072187391, 9577394838764454085], [15854241394484835714, 11398914698975566411], [13708282465491374871, 16007308345579681096],
             [15424829579845884309, 1898028439751125927], [9411697742461147792, 15714068361935982142], [10079222287618677782, 12870437757549876199],
             [17326737873898640088, 729039288628699544], [16644868984619524261, 1544825456798124994], [1857481142255628931, 596584038813451439],
             [18305404959516669237, 14103312907920476776]]
ok_np = all(np.random.SeedSequence(i).generate_state(4).tolist() == o and np.random.SeedSequence(i).generate_state(2, np.uint64).tolist() == o64 for i, o, o64 in zip(CPP_IN, CPP_OUT, CPP_OUT64))
ok_py = all(PySeedSeq(i).generate_state(4) == o and PySeedSeq(i).generate_state(2, True) == o64 for i, o, o64 in zip(CPP_IN, CPP_OUT, CPP_OUT64))
report("SeedSequence(entropy).generate_state(4) and (2, uint64) reproduce the 10 C++ reference vectors of O'Neill's seed_seq (gist 540829265469e673d045)", ok_np, f"pure-Python port also matches: {ok_py}")
cases = [(0, (), 4), (12345, (), 4), (2**200 + 17, (), 4), ([1, 2, 3], (), 4), ([2**40, 5], (), 4), (12345, (1, 2), 4), (98765, (0,), 8), (list(range(20)), (3,), 4)]
bad = []
for ent, sk, ps in cases:
    a = np.random.SeedSequence(ent, spawn_key=sk, pool_size=ps).generate_state(16).tolist(); b = PySeedSeq(ent, sk, ps).generate_state(16)
    a64 = np.random.SeedSequence(ent, spawn_key=sk, pool_size=ps).generate_state(8, np.uint64).tolist(); b64 = PySeedSeq(ent, sk, ps).generate_state(8, True)
    if a != b or a64 != b64: bad.append((ent if not isinstance(ent, list) else ent[:3], sk, ps))
report("SeedSequence(entropy, spawn_key, pool_size).generate_state(16) / (8, uint64) == pure-Python seed_seq hash for 8 entropy / spawn_key / pool_size cases (words little-endian, spawn_key appended after zero-padding the run entropy to pool_size)", not bad, f"mismatch {bad}")
ss = np.random.SeedSequence(4242)
kids = ss.spawn(3); kids2 = ss.spawn(2)
ok = [k.spawn_key for k in kids] == [(0,), (1,), (2,)] and [k.spawn_key for k in kids2] == [(3,), (4,)] and all(k.entropy == 4242 for k in kids + kids2) and ss.n_children_spawned == 5
ok = ok and all(np.array_equal(k.generate_state(4), np.random.SeedSequence(4242, spawn_key=k.spawn_key).generate_state(4)) for k in kids)
gk = kids[1].spawn(2)
ok = ok and [k.spawn_key for k in gk] == [(1, 0), (1, 1)]
report("SeedSequence.spawn: children get spawn_key parent+(i,) with i continuing across calls (n_children_spawned), same entropy; grandchildren extend the key", ok)
report("SeedSequence(-1) raises ValueError ('All integer values must be non-negative'); SeedSequence(1.5) raises TypeError; pool_size=3 raises ValueError",
       raises(lambda: np.random.SeedSequence(-1), ValueError) and raises(lambda: np.random.SeedSequence(1.5), TypeError) and raises(lambda: np.random.SeedSequence(1, pool_size=3), ValueError))
e = np.random.SeedSequence().entropy
report("SeedSequence() (entropy None) draws a 128-bit OS integer (pool_size * 32 bits); two instances differ", isinstance(e, int) and 0 <= e < 2**128 and e != np.random.SeedSequence().entropy, f"entropy bits {e.bit_length()}")
report("SeedSequence(sq1.entropy) regenerates the same state (docstring example)", np.array_equal(np.random.SeedSequence(e).generate_state(10), np.random.SeedSequence(e).generate_state(10)))
report("SeedSequence.generate_state(dtype=float) raises ValueError ('only support uint32 or uint64')", raises(lambda: np.random.SeedSequence(1).generate_state(3, np.float64), ValueError))

# ======================================================================
# bit generators: pure-Python references, CSV vectors, seeding chains
# ======================================================================
print("---- bit generators vs pure-Python references")
PCG_MULT = (2549297995355413924 << 64) | 4865540595714422341
CHEAP = 0xda942042e4dd58b5
def rotr64(x, r): return ((x >> r) | (x << ((-r) & 63))) & M64
class PyPCG64:
    def __init__(self, state, inc): self.s = state; self.inc = inc
    def next(self):
        self.s = (self.s * PCG_MULT + self.inc) & M128
        hi = self.s >> 64; lo = self.s & M64; return rotr64(hi ^ lo, hi >> 58)
class PyDXSM:
    def __init__(self, state, inc): self.s = state; self.inc = inc
    def next(self):
        hi = self.s >> 64; lo = (self.s & M64) | 1
        hi ^= hi >> 32; hi = (hi * CHEAP) & M64; hi ^= hi >> 48; hi = (hi * lo) & M64
        self.s = (self.s * CHEAP + self.inc) & M128; return hi
def pcg_srandom(initstate, initseq, mult):
    inc = ((initseq << 1) | 1) & M128; s = (0 * mult + inc) & M128; s = (s + initstate) & M128; s = (s * mult + inc) & M128
    return s, inc
def lcg_advance(state, delta, mult, plus):
    """Brown (1994) arbitrary-stride LCG jump, all arithmetic mod 2**128"""
    acc_m, acc_p = 1, 0; delta &= M128
    while delta > 0:
        if delta & 1: acc_m = (acc_m * mult) & M128; acc_p = (acc_p * mult + plus) & M128
        plus = ((mult + 1) * plus) & M128; mult = (mult * mult) & M128; delta >>= 1
    return (acc_m * state + acc_p) & M128
def philox_block(ctr, key):
    c = list(ctr); k = list(key)
    for r in range(10):
        if r: k = [(k[0] + 0x9E3779B97F4A7C15) & M64, (k[1] + 0xBB67AE8584CAA73B) & M64]
        p0 = 0xD2E7470EE14C6C93 * c[0]; p1 = 0xCA5A826395121157 * c[2]
        c = [(p1 >> 64) ^ c[1] ^ k[0], p1 & M64, (p0 >> 64) ^ c[3] ^ k[1], p0 & M64]
    return c
class PyPhilox:
    def __init__(self, ctr, key, buf=None, pos=4): self.ctr = sum(int(v) << (64 * i) for i, v in enumerate(ctr)); self.key = [int(k) for k in key]; self.buf = list(buf) if buf is not None else [0] * 4; self.pos = pos
    def next(self):
        if self.pos < 4: v = self.buf[self.pos]; self.pos += 1; return v
        self.ctr = (self.ctr + 1) & ((1 << 256) - 1)
        self.buf = philox_block([(self.ctr >> (64 * i)) & M64 for i in range(4)], self.key); self.pos = 1; return self.buf[0]
class PySFC64:
    def __init__(self, s): self.s = [int(v) for v in s]
    def next(self):
        a, b, c, w = self.s; tmp = (a + b + w) & M64
        self.s = [b ^ (b >> 11), (c + (c << 3)) & M64, (((c << 24) | (c >> 40)) & M64) + tmp & M64, (w + 1) & M64]
        return tmp
class PyMT:
    def __init__(self, key, pos): self.mt = [int(k) for k in key]; self.pos = int(pos)
    def gen(self):
        mt = self.mt
        for kk in range(624):
            y = (mt[kk] & 0x80000000) | (mt[(kk + 1) % 624] & 0x7fffffff)
            mt[kk] = mt[(kk + 397) % 624] ^ (y >> 1) ^ (0x9908b0df if y & 1 else 0)
        self.pos = 0
    def next(self):
        if self.pos >= 624: self.gen()
        y = self.mt[self.pos]; self.pos += 1
        y ^= y >> 11; y ^= (y << 7) & 0x9d2c5680; y ^= (y << 15) & 0xefc60000; return y ^ (y >> 18)
def mt_init_genrand(s):
    mt = [s & M32]
    for i in range(1, 624): mt.append((1812433253 * (mt[i - 1] ^ (mt[i - 1] >> 30)) + i) & M32)
    return mt
def mt_init_by_array(key):
    mt = mt_init_genrand(19650218); i, j, n = 1, 0, 624
    for _ in range(max(n, len(key))):
        mt[i] = ((mt[i] ^ ((mt[i - 1] ^ (mt[i - 1] >> 30)) * 1664525)) + key[j] + j) & M32
        i += 1; j += 1
        if i >= n: mt[0] = mt[n - 1]; i = 1
        if j >= len(key): j = 0
    for _ in range(n - 1):
        mt[i] = ((mt[i] ^ ((mt[i - 1] ^ (mt[i - 1] >> 30)) * 1566083941)) - i) & M32
        i += 1
        if i >= n: mt[0] = mt[n - 1]; i = 1
    mt[0] = 0x80000000
    return mt
def py_from_state(bg):
    st = bg.state; name = st['bit_generator']
    if name == 'PCG64': return PyPCG64(int(st['state']['state']), int(st['state']['inc']))
    if name == 'PCG64DXSM': return PyDXSM(int(st['state']['state']), int(st['state']['inc']))
    if name == 'Philox': return PyPhilox(st['state']['counter'], st['state']['key'], st['buffer'], int(st['buffer_pos']))
    if name == 'SFC64': return PySFC64(st['state']['state'])
    if name == 'MT19937': return PyMT(st['state']['key'], st['state']['pos'])
BGS = [("PCG64", np.random.PCG64), ("PCG64DXSM", np.random.PCG64DXSM), ("MT19937", np.random.MT19937), ("Philox", np.random.Philox), ("SFC64", np.random.SFC64)]
for name, C in BGS:
    for s in [0, 12345, 2**100 + 3]:
        bg = C(s); ref = py_from_state(bg)
        raw = bg.random_raw(2000).tolist(); pyv = [ref.next() for _ in range(2000)]
        report(f"{name}({s}).random_raw(2000) == pure-Python {name} started from the published state dict", raw == pyv, f"first {raw[:2]}")
    # mid-stream: after a Generator consumed an odd number of 32-bit halves the state dict still describes the stream
    bg = C(7); g = np.random.Generator(bg); g.random(3); g.integers(0, 2**32, 3, dtype=np.uint32)
    ref = py_from_state(bg); report(f"{name}: state dict after mixed 64/32-bit consumption reproduces the remaining raw stream", bg.random_raw(100).tolist() == [ref.next() for _ in range(100)])
# CPython's MT19937 as a second reference
bg = np.random.MT19937(99); st = bg.state['state']
py = pyrandom.Random(); py.setstate((3, tuple(int(k) for k in st['key']) + (int(st['pos']),), None))
report("MT19937(99).random_raw(3000) == CPython random.getrandbits(32) from the same (key, pos) (independent C implementation)", bg.random_raw(3000).tolist() == [py.getrandbits(32) for _ in range(3000)])
# reference CSV vectors shipped with numpy
ddir = os.path.join(os.path.dirname(np.random.__file__), "tests", "data")
for name, C in BGS:
    fn = name.lower()
    for i in (1, 2):
        path = os.path.join(ddir, f"{fn}-testset-{i}.csv")
        if not os.path.exists(path): report(f"{name} testset-{i}.csv present", False, path); continue
        with open(path) as fh:
            rows = [l.strip().split(",") for l in fh if l.strip()]
        sd = int(rows[0][1].strip(), 0); vals = [int(r[1].strip(), 0) for r in rows[1:]]
        raw = C(sd).random_raw(len(vals)).tolist()
        pyv = py_from_state(C(sd)); pyl = [pyv.next() for _ in range(len(vals))]
        report(f"{name}(seed={hex(sd)}).random_raw({len(vals)}) == numpy/random/tests/data/{fn}-testset-{i}.csv (pure-Python reference agrees: {pyl == vals})", raw == vals)
# seeding chain SeedSequence -> state
bad = []
for s in [0, 1, 12345, 2**64 + 5, [3, 1, 4, 1, 5]]:
    ss = PySeedSeq(s)
    v = ss.generate_state(4, True); st, inc = pcg_srandom((v[0] << 64) | v[1], (v[2] << 64) | v[3], PCG_MULT)
    d = np.random.PCG64(s).state['state']
    if (int(d['state']), int(d['inc'])) != (st, inc): bad.append(("PCG64", s))
    d = np.random.PCG64DXSM(s).state['state']
    if (int(d['state']), int(d['inc'])) != (st, inc): bad.append(("PCG64DXSM", s))
    k = ss.generate_state(2, True); d = np.random.Philox(s).state
    if [int(x) for x in d['state']['key']] != k or [int(x) for x in d['state']['counter']] != [0, 0, 0, 0] or int(d['buffer_pos']) != 4: bad.append(("Philox", s))
    v3 = ss.generate_state(3, True); ref = PySFC64(v3 + [1])
    for _ in range(12): ref.next()
    if [int(x) for x in np.random.SFC64(s).state['state']['state']] != ref.s: bad.append(("SFC64", s))
    v = ss.generate_state(624); d = np.random.MT19937(s).state['state']
    if [int(x) for x in d['key']] != [0x80000000] + v[1:] or int(d['pos']) != 623: bad.append(("MT19937", s, int(d['pos'])))
report("Seeding chain: PCG64 / PCG64DXSM state = srandom(seed words 0-1, inc words 2-3 of generate_state(4, uint64)); Philox key = generate_state(2, uint64), counter 0; SFC64 = generate_state(3, uint64) + counter 1, 12 discarded outputs; MT19937 key = [0x80000000] + generate_state(624)[1:] (pure-Python SeedSequence)", not bad, f"mismatch {bad}")
print(f"   MT19937(SeedSequence) starts with pos = {np.random.MT19937(1).state['state']['pos']} (the Cython loop variable after range(1, 624)); the first output is tempered key[623] = a SeedSequence word, not an MT19937 recurrence output")

# ======================================================================
# advance / jumped
# ======================================================================
print("---- advance / jumped")
JUMP = 210306068529402873165736369884012333109
from decimal import Decimal, getcontext
getcontext().prec = 80
phi = (1 + Decimal(5).sqrt()) / 2; jp = (phi - 1) * (Decimal(2)**128)
report("PCG64 jump step 210306068529402873165736369884012333109 (docstring) is the odd integer nearest (phi-1) 2**128 ('The step size is phi-1 when multiplied by 2**128')", JUMP % 2 == 1 and abs(Decimal(JUMP) - jp) < 1, f"(phi-1) 2^128 = {jp:.3f}")
for name, C, mult in (("PCG64", np.random.PCG64, PCG_MULT), ("PCG64DXSM", np.random.PCG64DXSM, CHEAP)):
    ok = True; det = []
    for d_ in [1, 1000, 2**100 + 12345, 2**128 - 1]:
        bg = C(31); s0 = int(bg.state['state']['state']); inc = int(bg.state['state']['inc'])
        bg.advance(d_)
        if int(bg.state['state']['state']) != lcg_advance(s0, d_, mult, inc): ok = False; det.append(d_)
    report(f"{name}.advance(delta) state == pure-Python LCG jump-ahead (Brown 1994) for delta = 1, 1000, 2**100+12345, 2**128-1", ok, f"bad {det}")
    raw = C(31).random_raw(1010).tolist(); bg = C(31); bg.advance(1000)
    report(f"{name}.advance(1000) then random_raw(10) == draws 1000..1009 of the fresh stream ('as-if delta draws have occurred')", bg.random_raw(10).tolist() == raw[1000:])
    bg = C(31); g = np.random.Generator(bg); g.random(1, dtype=np.float32); h1 = bg.state['has_uint32']; bg.advance(5)
    report(f"{name}.advance resets the buffered 32-bit half ('resets any pre-computed random numbers')", h1 == 1 and bg.state['has_uint32'] == 0)
    bg = C(31); s0 = int(bg.state['state']['state']); inc = int(bg.state['state']['inc']); j1 = bg.jumped(); j3 = bg.jumped(3)
    report(f"{name}.jumped() / jumped(3) state == advance by jumps * 210306068529402873165736369884012333109; the original is unchanged",
           int(j1.state['state']['state']) == lcg_advance(s0, JUMP, mult, inc) and int(j3.state['state']['state']) == lcg_advance(s0, 3 * JUMP, mult, inc) and int(bg.state['state']['state']) == s0)
    report(f"{name}.jumped() returns a new {name} instance (type preserved)", type(j1) is C)
# Philox: advance / jumped vs the documented 'draws'
raw = np.random.Philox(5).random_raw(40).tolist()
p = np.random.Philox(5); p.advance(1); a1 = p.random_raw(4).tolist()
rp = PyPhilox([0, 0, 0, 0], np.random.Philox(5).state['state']['key']); rp.ctr += 1; ref_ctr = [rp.next() for _ in range(4)]
report("Philox.advance(1) then random_raw(4) == raw draws 1..4 of the fresh stream (docstring: 'Advance the underlying RNG as-if delta draws have occurred')", a1 == raw[1:5],
       f"observed == draws 4..7 (one 4-word counter block skipped): {a1 == raw[4:8]}; == pure-Python counter+1 block: {a1 == ref_ctr}")
p = np.random.Philox(5); j = p.jumped(); key = [int(k) for k in p.state['state']['key']]
rp = PyPhilox([0, 0, 0, 0], key); rp.ctr = 2**128
report("Philox.jumped() == counter + 2**128 (implementation: advance(2**128)), i.e. 2**130 raw draws; docstring 'as-if (2**128) * jumps random numbers have been generated'",
       j.random_raw(8).tolist() == [rp.next() for _ in range(8)])
print("   Philox: advance(delta) adds delta to the 256-bit counter; each counter value yields 4 raw 64-bit draws (class docstring: 'advance can be used to advance the counter')")
p = np.random.Philox(counter=5, key=77); rp = PyPhilox([5, 0, 0, 0], [77, 0])
report("Philox(counter=5, key=77) (explicit key/counter): raw stream == pure-Python Philox4x64-10 from counter 5+1", p.random_raw(12).tolist() == [rp.next() for _ in range(12)])
report("Philox(seed, key=...) raises ValueError (seed and key are mutually exclusive)", raises(lambda: np.random.Philox(1, key=2), ValueError))
# MT19937.jumped: x**(2**128) mod the characteristic polynomial over GF(2)
def berlekamp_massey(bits):
    C = 1; B = 1; L = 0; m = 1; Sx = 0
    for n, b in enumerate(bits):
        Sx = (Sx << 1) | b
        d = (C & Sx).bit_count() & 1
        if d == 0: m += 1
        elif 2 * L <= n:
            T = C; C ^= B << m; L = n + 1 - L; B = T; m = 1
        else:
            C ^= B << m; m += 1
    return C, L
SP = [int(''.join(c + '0' for c in format(b, '08b'))[:-1] or '0', 2) for b in range(256)]
SP2 = [v.to_bytes(2, 'little') for v in SP]
def gf2_sq(a):
    b = a.to_bytes((a.bit_length() + 7) // 8 or 1, 'little')
    return int.from_bytes(b''.join(SP2[x] for x in b), 'little')
def make_reducer(P, L):
    top = {}
    for q in range(256):                                  # q(x) * P(x), q of degree < 8
        prod = 0
        for i in range(8):
            if q >> i & 1: prod ^= P << i
        top[prod >> L] = prod
    def red(a):
        while a.bit_length() > L + 7:
            sh = a.bit_length() - (L + 8); t = a >> (L + sh)
            a ^= top[t] << sh
        while a.bit_length() > L:
            a ^= P << (a.bit_length() - 1 - L)
        return a
    return red
t0 = time.time()
mtb = np.random.MT19937(2024); outs = mtb.random_raw(40000).astype(np.uint64)
C_, L_ = berlekamp_massey([int(v) & 1 for v in outs[:2 * 19937 + 50]])
Pm = int(format(C_, 'b').zfill(L_ + 1)[::-1], 2)     # characteristic polynomial (reverse of the connection polynomial)
red = make_reducer(Pm, L_)
J16 = 2
for _ in range(16): J16 = red(gf2_sq(J16))
Jp = J16
for _ in range(112): Jp = red(gf2_sq(Jp))
J2 = Jp
for _ in range(128): J2 = red(gf2_sq(J2))
def predict_from(o, Jpoly, k):
    idx = np.array([i for i in range(Jpoly.bit_length()) if Jpoly >> i & 1], dtype=np.int64)
    return np.array([int(np.bitwise_xor.reduce(o[idx + t])) for t in range(k)], dtype=np.uint64)
report(f"MT19937: Berlekamp-Massey on the output LSBs gives the degree-19937 characteristic polynomial, and x**(2**16) mod P predicts outputs 2**16 + t exactly (method check, {time.time() - t0:.1f} s)",
       L_ == 19937 and np.array_equal(predict_from(outs, J16, 20), np.random.MT19937(2024).random_raw(2**16 + 20)[2**16:].astype(np.uint64)), f"L={L_}")
def mt_case(label, mk, Jpoly, jumps, k=624 * 4):
    base = mk(); st = base.state
    o = base.random_raw(Jpoly.bit_length() + k + 10).astype(np.uint64)
    b2 = np.random.MT19937(); b2.state = st; jo = b2.jumped(jumps).random_raw(k).astype(np.uint64)
    pr = predict_from(o, Jpoly, k); agree = (pr == jo)
    blocks = [int(agree[i:i + 624].sum()) for i in range(0, k, 624)]
    report(f"MT19937 {label}: jumped({jumps}) raw outputs == outputs 2**{128 * jumps} + t of the original stream (docstring 'as-if 2**(128 * jumps) random numbers have been generated')",
           bool(agree.all()), f"start pos {st['state']['pos']}, jumped pos {b2.jumped(jumps).state['state']['pos']}; agreeing outputs per 624-block: {blocks}")
mt_case("seeded by SeedSequence (pos 623)", lambda: np.random.MT19937(2024), Jp, 1)
mt_case("after 700 draws (pos 75)", lambda: (lambda m: (m.random_raw(700), m)[1])(np.random.MT19937(2024)), Jp, 1)
mt_case("legacy-seeded, 1248 draws (pos 624, a block boundary)", lambda: (lambda m: (m._legacy_seeding(2024), m.random_raw(1248), m)[2])(np.random.MT19937()), Jp, 1)
mt_case("seeded by SeedSequence (pos 623)", lambda: np.random.MT19937(2024), J2, 2)
print("   numpy's own test (test_generator_mt19937.test_jumped) compares only the jumped key hash and pos with Matsumoto's C jump code; the jump code treats key/pos as a circular buffer (gen_next), numpy's generator regenerates whole blocks from key[0]")
b = np.random.MT19937(2024); j_ = b.jumped().jumped()
report("MT19937: jumped().jumped() == jumped(2) (jumps compose)", j_.random_raw(20).tolist() == np.random.MT19937(2024).jumped(2).random_raw(20).tolist())
report("SFC64 has no jumped / advance (documented bit generators with jump support: PCG64, PCG64DXSM, Philox, MT19937)", not hasattr(np.random.SFC64(1), "jumped") and not hasattr(np.random.SFC64(1), "advance"))

# ======================================================================
# state round trips, pickling, spawn
# ======================================================================
print("---- state round trips, pickling, spawn")
for name, C in BGS:
    bg = C(11); g = np.random.Generator(bg); g.random(3); g.random(1, dtype=np.float32)
    st = bg.state; a = g.random(20, dtype=np.float32).tolist() + g.integers(0, 100, 5).tolist()
    bg2 = C(); bg2.state = st; g2 = np.random.Generator(bg2)
    b = g2.random(20, dtype=np.float32).tolist() + g2.integers(0, 100, 5).tolist()
    report(f"{name}: state dict round trip (with a buffered 32-bit half) continues the stream exactly", a == b)
    wrong = dict(st); wrong['bit_generator'] = 'Other'
    report(f"{name}: setting a state dict with the wrong bit_generator name raises ValueError", raises(lambda: setattr(C(), 'state', wrong), ValueError))
    g = np.random.Generator(C(12)); g.standard_normal(3); g2 = pickle.loads(pickle.dumps(g))
    report(f"pickle round trip of Generator({name}) continues the stream", np.array_equal(g.standard_normal(50), g2.standard_normal(50)))
    bg = C(13); bg.random_raw(5); bg2 = pickle.loads(pickle.dumps(bg))
    report(f"pickle round trip of {name} continues the raw stream", bg.random_raw(20).tolist() == bg2.random_raw(20).tolist())
rs = np.random.RandomState(21); rs.randn(3)                  # odd number of normals: a cached gaussian is pending
st = rs.get_state()
report("RandomState.get_state(): ('MT19937', 624 uint32 key, pos, has_gauss, cached_gaussian) with has_gauss = 1 after an odd number of normals",
       st[0] == 'MT19937' and st[1].shape == (624,) and st[1].dtype == np.uint32 and st[3] == 1 and isinstance(st[4], float))
a = rs.randn(10); rs2 = np.random.RandomState(); rs2.set_state(st)
report("RandomState.set_state(5-tuple) restores the cached gaussian: next normals identical", np.array_equal(a, rs2.randn(10)))
rs3 = np.random.RandomState(); rs3.set_state(st[:3]); first = rs3.randn(1)[0]
report("RandomState.set_state(3-tuple) (documented backwards-compatible form) is accepted and drops the cached gaussian (next normal is fresh, not the cached value)", first != st[4])
sd = rs.get_state(legacy=False)
report("RandomState.get_state(legacy=False) returns the dict form (with has_gauss / gauss); set_state(dict) round trips",
       isinstance(sd, dict) and 'has_gauss' in sd and (lambda r: (r.set_state(sd), np.array_equal(r.randn(5), (lambda q: (q.set_state(sd), q.randn(5))[1])(np.random.RandomState())))[1])(np.random.RandomState()))
rs = np.random.RandomState(5); rs.random_sample(3); r2 = pickle.loads(pickle.dumps(rs))
report("pickle round trip of RandomState continues the stream", np.array_equal(rs.random_sample(20), r2.random_sample(20)))
report("RandomState.set_state(('MT19937', 623 words, 0)) is rejected (ValueError or IndexError)", raises(lambda: np.random.RandomState().set_state(('MT19937', np.zeros(623, np.uint32), 0)), (ValueError, IndexError)), exc_name(lambda: np.random.RandomState().set_state(('MT19937', np.zeros(623, np.uint32), 0))))
report("RandomState.set_state(('PCG64', ...)) raises ValueError (state must match the bit generator)", raises(lambda: np.random.RandomState().set_state(('PCG64', np.zeros(624, np.uint32), 0)), ValueError))
for label, code in (("RandomState.set_state(('MT19937', key, pos=10**7))", "import numpy as np\nrs = np.random.RandomState(1)\ntry:\n    rs.set_state(('MT19937', np.arange(624, dtype=np.uint32), 10**7)); print('accepted'); print(rs.random_sample())\nexcept Exception as e: print('raised', type(e).__name__)"),
                    ("MT19937.state = {'key': ..., 'pos': 700}", "import numpy as np\nb = np.random.MT19937(1)\ntry:\n    b.state = {'bit_generator': 'MT19937', 'state': {'key': np.arange(624, dtype=np.uint32), 'pos': 700}}; print('accepted'); print(b.random_raw(10**6)[-1])\nexcept Exception as e: print('raised', type(e).__name__)")):
    hung, out = hang_check(code, 30)
    ok = (not hung) and ("raised" in out)
    report(f"{label} then drawing: the out-of-range pos (key has 624 words) is rejected with an exception instead of reading past the key array (docstring: 'an integer pos'; 1.26.3 release note gh-25466 'avoid seg fault from OOB access in RandomState.set_state()')", ok, out[:90])
if V >= (1, 25):
    g = np.random.default_rng(777); kids = g.spawn(2); kids2 = g.spawn(1)
    ok = all(np.array_equal(k.random(10), np.random.default_rng(np.random.SeedSequence(777, spawn_key=(i,))).random(10)) for i, k in enumerate(kids))
    ok = ok and np.array_equal(kids2[0].random(10), np.random.default_rng(np.random.SeedSequence(777, spawn_key=(2,))).random(10))
    report("Generator.spawn(n) (1.25 release note): children == default_rng(SeedSequence(entropy, spawn_key=(i,))), index continues across calls", ok)
    bg = np.random.PCG64(778); kb = bg.spawn(2)
    report("BitGenerator.spawn(n): same class, streams from spawn_key (i,); seed_seq exposes the SeedSequence", all(type(k) is np.random.PCG64 for k in kb)
           and kb[1].random_raw(5).tolist() == np.random.PCG64(np.random.SeedSequence(778, spawn_key=(1,))).random_raw(5).tolist() and bg.seed_seq.entropy == 778)
    report("Generator.spawn on Philox(key=...) (no SeedSequence) raises TypeError ('When the underlying SeedSequence does not implement spawning')",
           raises(lambda: np.random.Generator(np.random.Philox(key=5)).spawn(1), TypeError))
else:
    report("Generator.spawn / BitGenerator.spawn / seed_seq absent before 1.25 (added in 1.25.0, release-noted)", not hasattr(np.random.Generator, "spawn") and not hasattr(np.random.PCG64(1), "spawn"))

# ======================================================================
# legacy seeding, seed-type handling, default_rng
# ======================================================================
print("---- legacy seeding and seed types")
ok = True
for s in [0, 1, 12345, 2**32 - 1]:
    st = np.random.RandomState(s).get_state()
    ok = ok and st[1].tolist() == mt_init_genrand(s) and st[2] == 624 and st[3] == 0
report("RandomState(int s) state == init_genrand(s) (Knuth 1812433253 recurrence), pos 624, no cached gaussian, for s = 0, 1, 12345, 2**32-1", ok)
ok = True
for key in [[1, 2, 3], [0], [2**32 - 1, 5, 7, 9, 11], list(range(700))]:
    ok = ok and np.random.RandomState(key).get_state()[1].tolist() == mt_init_by_array(key)
report("RandomState(sequence) state == init_by_array(sequence) (MT19937 reference, incl. a 700-word key)", ok)
ok = True
for s in [0, 7, 12345, 2**32 - 1]:
    py = pyrandom.Random(s); pyk = list(py.getstate()[1][:624])
    ok = ok and np.random.RandomState([s]).get_state()[1].tolist() == pyk
report("RandomState([s]) state == CPython random.Random(s) state (CPython seeds MT19937 with init_by_array of the 32-bit words)", ok)
a7 = np.random.RandomState(np.array([7])).get_state()[1].tolist(); l7 = np.random.RandomState([7]).get_state()[1].tolist(); i7 = np.random.RandomState(7).get_state()[1].tolist()
print(f"   RandomState(np.array([7])) == RandomState(7) (init_genrand, via .squeeze()): {a7 == i7}; == RandomState([7]) (init_by_array): {a7 == l7}  (docstring: 'an array (or other sequence) of such integers')")
report("RandomState(np.uint32(7)) == RandomState(7); RandomState(np.int64(7)) == RandomState(7)",
       np.random.RandomState(np.uint32(7)).get_state()[1].tolist() == i7 and np.random.RandomState(np.int64(7)).get_state()[1].tolist() == i7)
report("RandomState(2**32) and RandomState(-1) raise ValueError ('any integer between 0 and 2**32 - 1 inclusive')", raises(lambda: np.random.RandomState(2**32), ValueError) and raises(lambda: np.random.RandomState(-1), ValueError))
report("RandomState([2**32]) and RandomState([-1, 3]) raise ValueError", raises(lambda: np.random.RandomState([2**32]), ValueError) and raises(lambda: np.random.RandomState([-1, 3]), ValueError))
report("RandomState(1.5) raises TypeError; RandomState([]) raises ValueError; RandomState([[1, 2], [3, 4]]) raises ValueError",
       raises(lambda: np.random.RandomState(1.5), TypeError) and raises(lambda: np.random.RandomState([]), ValueError) and raises(lambda: np.random.RandomState([[1, 2], [3, 4]]), ValueError),
       f"{exc_name(lambda: np.random.RandomState(1.5))}; {exc_name(lambda: np.random.RandomState([]))}")
rs = np.random.RandomState(1); rs.random_sample(5); rs.seed(99)
report("RandomState.seed(s) re-seeds == RandomState(s)", np.array_equal(rs.random_sample(10), np.random.RandomState(99).random_sample(10)))
report("RandomState(None) and np.random.seed() use OS entropy: two instances differ", not np.array_equal(np.random.RandomState().random_sample(4), np.random.RandomState().random_sample(4)))
bg = np.random.MT19937(); bg._legacy_seeding(4321)
report("MT19937()._legacy_seeding(s) state == RandomState(s) state", bg.state['state']['key'].tolist() == np.random.RandomState(4321).get_state()[1].tolist())
rs = np.random.RandomState(np.random.PCG64(55))
report("RandomState(PCG64(55)).random_sample == Generator(PCG64(55)).random (legacy_double = next_double of the bit generator)", np.array_equal(rs.random_sample(20), np.random.Generator(np.random.PCG64(55)).random(20)))
report("RandomState(PCG64).seed() raises TypeError ('can only re-seed a MT19937 BitGenerator')", raises(lambda: np.random.RandomState(np.random.PCG64(1)).seed(3), TypeError))
rs = np.random.RandomState(np.random.MT19937(np.random.SeedSequence(123456789)))
ref = py_from_state(rs._bit_generator)
report("RandomState(MT19937(SeedSequence(123456789))) (docstring example): random_sample == res53 of the pure-Python MT stream", rs.random_sample(10).tolist() == [((ref.next() >> 5) * 67108864 + (ref.next() >> 6)) / 9007199254740992.0 for _ in range(10)])
a = np.random.default_rng(424242).random(20)
report("default_rng(s) == Generator(PCG64(s)) == Generator(PCG64(SeedSequence(s))) (documented: int passed to SeedSequence)",
       np.array_equal(a, np.random.Generator(np.random.PCG64(424242)).random(20)) and np.array_equal(a, np.random.Generator(np.random.PCG64(np.random.SeedSequence(424242))).random(20)))
g = np.random.default_rng(3)
report("default_rng(Generator) returns it unaltered ('If passed a Generator, it will be returned unaltered')", np.random.default_rng(g) is g)
bg = np.random.Philox(4); gg = np.random.default_rng(bg)
report("default_rng(BitGenerator) wraps it ('it will be wrapped by Generator'): .bit_generator is the same object", gg.bit_generator is bg)
report("default_rng(-1) raises ValueError ('all values must be non-negative'); default_rng([1, -2]) raises ValueError", raises(lambda: np.random.default_rng(-1), ValueError) and raises(lambda: np.random.default_rng([1, -2]), ValueError))
report("default_rng(1.5) raises TypeError; default_rng('abc') raises TypeError", raises(lambda: np.random.default_rng(1.5), TypeError) and raises(lambda: np.random.default_rng('abc'), TypeError), f"{exc_name(lambda: np.random.default_rng(1.5))}; {exc_name(lambda: np.random.default_rng('abc'))}")
report("default_rng(np.int64(5)) == default_rng(5); default_rng(np.array([1, 2], dtype=uint64)) == default_rng([1, 2]) (element-wise uint32 coercion)",
       np.array_equal(np.random.default_rng(np.int64(5)).random(5), np.random.default_rng(5).random(5)) and np.array_equal(np.random.default_rng(np.array([1, 2], dtype=np.uint64)).random(5), np.random.default_rng([1, 2]).random(5)))
report("default_rng([2**40, 7]) == pure-Python SeedSequence chain -> PCG64 srandom -> XSL-RR", (lambda v: np.random.default_rng([2**40, 7]).bit_generator.random_raw(5).tolist() == (lambda r: [r.next() for _ in range(5)])(PyPCG64(*pcg_srandom((v[0] << 64) | v[1], (v[2] << 64) | v[3], PCG_MULT))))(PySeedSeq([2**40, 7]).generate_state(4, True)))
report("default_rng() twice (OS entropy) gives different streams", not np.array_equal(np.random.default_rng().random(4), np.random.default_rng().random(4)))
if "RandomState" in (np.random.default_rng.__doc__ or ""):
    rs = np.random.RandomState(8); gg = np.random.default_rng(rs)
    report("default_rng(RandomState) ('When passed a legacy RandomState instance it will be coerced to a Generator'): Generator over the same bit generator", isinstance(gg, np.random.Generator) and gg.bit_generator is rs._bit_generator)
else:
    report("default_rng(RandomState) not documented in this build: raises TypeError", raises(lambda: np.random.default_rng(np.random.RandomState(8)), TypeError), exc_name(lambda: np.random.default_rng(np.random.RandomState(8))))

# ======================================================================
# docstring examples
# ======================================================================
print("---- docstring examples")
rng = np.random.default_rng(12345); rf = rng.random()
report("default_rng docstring: default_rng(12345).random() -> 0.22733602246716966 (a Python float)", rf == 0.22733602246716966 and isinstance(rf, float), repr(rf))
ri = np.random.default_rng(12345).integers(low=0, high=10, size=3)
report("default_rng docstring: default_rng(12345).integers(low=0, high=10, size=3) -> array([6, 2, 7]), elements numpy.int64", ri.tolist() == [6, 2, 7] and type(ri[0]) is np.int64, str(ri.tolist()))
a = np.random.default_rng(seed=42).random((3, 3))
docv = np.array([[0.77395605, 0.43887844, 0.85859792], [0.69736803, 0.09417735, 0.97562235], [0.7611397, 0.78606431, 0.12811363]])
report("default_rng docstring: default_rng(seed=42).random((3, 3)) matches the printed 8-digit array", bool(np.all(np.abs(a - docv) <= 5e-9)), f"max diff {np.abs(a - docv).max():.1e}")
v = np.random.default_rng(122807528840384100672342137672332424406).random()
report("random/index.rst: default_rng(122807528840384100672342137672332424406).random() -> 0.5363922081269535", v == 0.5363922081269535, repr(v))
report("default_rng docstring: print(rng) -> 'Generator(PCG64)'", str(np.random.default_rng(1)) == "Generator(PCG64)", str(np.random.default_rng(1)))
sg = np.random.SeedSequence(1234); rg = [np.random.Generator(np.random.PCG64(s)) for s in sg.spawn(10)]
report("PCG64 docstring parallel example: [Generator(PCG64(s)) for s in SeedSequence(1234).spawn(10)] gives 10 distinct streams", len({tuple(g.integers(0, 2**62, 4).tolist()) for g in rg}) == 10)
bitg = np.random.MT19937(np.random.SeedSequence(1234)); rgs = []
for _ in range(10):
    rgs.append(np.random.Generator(bitg)); bitg = bitg.jumped()
report("MT19937 docstring example: chained jumped() generators give 10 distinct streams", len({tuple(g.integers(0, 2**62, 4).tolist()) for g in rgs}) == 10)
x = np.random.default_rng(6).permuted(np.arange(24).reshape(3, 8), axis=1)
report("Generator.permuted docstring example shape: rows of arange(24).reshape(3, 8) keep their 8 values", all(sorted(x[i].tolist()) == list(range(8 * i, 8 * i + 8)) for i in range(3)))
x = np.random.default_rng(7).choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
report("Generator.choice docstring example choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0]) only returns 0, 2, 3", bool(np.isin(x, [0, 2, 3]).all()))
x = np.random.default_rng(8).integers(5, size=(2, 4))
report("Generator.integers docstring example integers(5, size=(2, 4)): shape (2, 4), values 0..4", x.shape == (2, 4) and x.min() >= 0 and x.max() <= 4)
x = np.random.default_rng(9).integers(1, [3, 5, 10]); y = np.random.default_rng(9).integers([1, 5, 7], 10)
report("Generator.integers docstring examples with 3 different upper / lower bounds: each element in its own range", bool(((x >= 1) & (x < [3, 5, 10])).all() and ((y >= [1, 5, 7]) & (y < 10)).all()))

# ======================================================================
# stream identity across builds
# ======================================================================
print("---- stream identity across builds (digests of the first draws from seed 20260925; expected values recorded with numpy 2.4.6)")
EXPECTED = {
    'G.beta_big': '3c667f5f8699c5d6', 'G.beta_small': '5e0dd54203f92364', 'G.binomial_btpe': '057e7d6da2d6be6b', 'G.binomial_inv': '125ec362aba2f255',
    'G.binomial_p_gt_half': '5364e3f5269b016e', 'G.bytes': '15724a94d441b9e8', 'G.chisquare': '86d882941a3b9252', 'G.choice': '7408b9d7a8a910cf',
    'G.choice_noreplace': '51be57300cbcaf9b', 'G.choice_noreplace_big': '29df9cf2599960b9', 'G.choice_noreplace_p': 'b312f40a150f764b', 'G.choice_noshuffle': '986d6f45abc2da9c',
    'G.choice_p': '7a680c3d9bc6b732', 'G.dirichlet': 'a9a847b4bc931adb', 'G.dirichlet_small': '46fedc30040e9e2e', 'G.exponential': 'a2a835351d25b475',
    'G.f': '76d28b640631e9f2', 'G.gamma': '26e4b03e1261f7d3', 'G.geometric_inv': 'fd5f4a505506ae61', 'G.geometric_search': '43e61a1a79aad4af',
    'G.gumbel': 'ee83d87fa11f04c5', 'G.hypergeometric_hrua': 'b41278b66a2ec9c4', 'G.hypergeometric_small': '2998deed37510481', 'G.integers_bool': '43ae3e5407a9e1e6',
    'G.integers_broadcast': 'a2d17fd37aeb205c', 'G.integers_endpoint': '7cc4530a6a395410', 'G.integers_int16': '47ee82067660719f', 'G.integers_int32': '293f46c2d8af24ba',
    'G.integers_int64': 'd815059062eba310', 'G.integers_int64_full': 'b763254e4d0f17aa', 'G.integers_uint64_full': 'b5d31244107653df', 'G.integers_uint8': '99e70c70e381fce4',
    'G.laplace': '1b26d84f47074bca', 'G.logistic': '71f2a33553f0fe2e', 'G.lognormal': 'ca490393dc720987', 'G.logseries': 'e4e5c4c8fb900401',
    'G.multinomial': '269afbfdae1a037f', 'G.mvhg_count': 'f02d8c9f0ad2abe1', 'G.mvhg_marginals': '96f22a5b09a97150', 'G.mvnormal_cholesky': '3acfb144a5a5af78',
    'G.mvnormal_svd': '0ec1bbe84013a20a', 'G.negative_binomial': '153dad21198aecd3', 'G.noncentral_chisquare': '8bc384ba6d569eae', 'G.noncentral_chisquare_df_lt_1': '505da4dd3494fd9f',
    'G.noncentral_f': 'a76cea09570136a6', 'G.normal': '1b87efbddf05aa43', 'G.pareto': '50ea1eb4601cde98', 'G.permutation': '9ed65210748b4622',
    'G.permuted': 'd4053e62e313b0fd', 'G.poisson_ptrs': '7c909ffaea81b9bc', 'G.poisson_small': '070a4172d55ffa25', 'G.power': '014d0520242e9aa5',
    'G.random': '799d1614690cf395', 'G.random_f32': '5728495dc7c71c51', 'G.rayleigh': '28fff57e0db89e13', 'G.shuffle': '9ed65210748b4622',
    'G.standard_cauchy': 'b348b3fa855cca2f', 'G.standard_exponential': 'cffea265f8667af7', 'G.standard_exponential_f32': 'f82979258cdd83ec', 'G.standard_exponential_inv': '29432857a68434e1',
    'G.standard_gamma_0.3': '7e35c33a355adf51', 'G.standard_gamma_3': '833e0f1b5847b858', 'G.standard_gamma_f32': '1971163f6d931833', 'G.standard_normal': '3f9340c452260c10',
    'G.standard_normal_f32': 'e06d0df02cb4cbb6', 'G.standard_t': 'fa084ffb121ac526', 'G.triangular': '4e8c1cd8b140bc85', 'G.uniform': '31ab09484cca8542',
    'G.vonmises': '8f4b27a0f560203c', 'G.vonmises_big_kappa': '22aad3768821c516', 'G.wald': '0985c036f9692908', 'G.wald_extreme': '710d4bdc80097504',
    'G.weibull': 'ec3efe2faab8993a', 'G.zipf': '576ee44438986ae7', 'G.zipf_near_1': '04cda9f5f2496f00', 'R.beta_big': '460e8598a1288c4c',
    'R.beta_small': 'b117a07b68d314b8', 'R.binomial_btpe': '4e112f7bf7a59a80', 'R.binomial_inv': 'a8a0cb6387ecfefc', 'R.bytes': '3102614821cc2053',
    'R.chisquare': 'ed1b89f02373b0d4', 'R.choice': '4e83046d1049d152', 'R.choice_noreplace': '228244bf04c8a6fd', 'R.choice_noreplace_p': '8c3e4f4b7507910c',
    'R.choice_p': '08a1b7db1b657821', 'R.dirichlet': '8202f6e05dba4dc3', 'R.exponential': '49729129a0e30962', 'R.f': '5453a688e88aed01',
    'R.gamma': 'f2d26b1801947130', 'R.geometric': '2320d10548c73093', 'R.geometric_inv': 'd73f30fed31c928b', 'R.gumbel': '350750bab3f3cdf7',
    'R.hypergeometric_hrua': '1d41d16d675211d8', 'R.hypergeometric_small': '668e6e94505c6c24', 'R.laplace': 'b87f1372cc542588', 'R.logistic': '94222f1bd426e92c',
    'R.lognormal': 'ebb3115734449a54', 'R.logseries': '4ce5b8d18512535d', 'R.multinomial': 'ef63d62993af881e', 'R.multivariate_normal': '8e74ccb22ae36ba0',
    'R.negative_binomial': '8a051a0c8b6aabed', 'R.noncentral_chisquare': '8e40282b940dc8c8', 'R.noncentral_chisquare_df_lt_1': '4b364158e011cddb', 'R.noncentral_f': '46c56ce38bf6d30b',
    'R.normal': '5aec99f85d8aa794', 'R.pareto': 'afe0c77daefc1940', 'R.permutation': '85933990cd8d5ebb', 'R.poisson_ptrs': 'de2c7d158a95b7af',
    'R.poisson_small': '6ef711c397ff1cad', 'R.power': '2538bb7d824fcf89', 'R.rand': 'a79508f81d664cfd', 'R.randint': '07ffd25f90a36bdd',
    'R.randint_bool': 'f54c59c1bc07941a', 'R.randint_int16': 'b662be6f68edddd6', 'R.randint_int32': 'e77e71682dc27dac', 'R.randint_int64_full': 'f2aaec8207bfd758',
    'R.randint_uint64_full': '205e0e61636f6cb4', 'R.randint_uint8': '9737652babf1823b', 'R.randn': '2561cbba12492103', 'R.random_integers': '868d1f8741056894',
    'R.random_sample': 'a79508f81d664cfd', 'R.rayleigh': '303774e898f939ad', 'R.shuffle': '85933990cd8d5ebb', 'R.standard_cauchy': 'feef311a9674b6b5',
    'R.standard_exponential': '8ec2bbead313a8a4', 'R.standard_gamma_0.3': 'bd1ae63117c382c7', 'R.standard_gamma_3': '2387943b33a43efd', 'R.standard_normal': '36e9e1a4d8dd4c90',
    'R.standard_t': '24d720d3ef90cef5', 'R.tomaxint': '8a4fa950def113a8', 'R.triangular': 'afac5b94dd2ffa8c', 'R.uniform': '3254e70479ce4ccf',
    'R.vonmises': 'a333d8e2778ab079', 'R.wald': '48c09951367ccd96', 'R.weibull': '5075b269b6f91ff9', 'R.zipf': '6a95617fde7f04d6',
}
# Generator stream changes documented in the release notes between the tested builds and 2.4.6: key -> (first version with the 2.4.6 stream, note)
KNOWN_GEN_CHANGES = {
    "G.wald": ((2, 3, 4), "2.3.4 release notes gh-29926 / 2.4.0 changelog gh-29609 'fix negative samples generated by Wald distribution' (new closed form for every draw)"),
    "G.wald_extreme": ((2, 3, 4), "2.3.4 release notes gh-29926 'fix negative samples generated by Wald distribution'"),
    "G.zipf_near_1": ((2, 1, 0), "2.1.0 changelog gh-27048 'Fix long delays/hangs with zipf(a) when a near 1' (proposals restricted to U > Umin)"),
}
got = stream_digests()
if not EXPECTED:
    print("   EXPECTED digests not recorded; run with N9_RECORD=1 under numpy 2.4.6")
else:
    for key in sorted(got):
        exp = EXPECTED.get(key)
        if exp is None: continue
        same = got[key] == exp
        if key.startswith("R."):
            report(f"RandomState stream {key[2:]} identical to numpy 2.4.6 (legacy streams frozen: 'no more modifications to RandomState')", same, f"{got[key]} vs {exp}")
        else:
            kc = KNOWN_GEN_CHANGES.get(key)
            if same: report(f"Generator stream {key[2:]} identical to numpy 2.4.6", True)
            elif kc is not None and V3 < kc[0]: report(f"Generator stream {key[2:]} differs from numpy 2.4.6 [release-noted: {kc[1]}]", True, f"{got[key]} vs {exp}")
            else: report(f"Generator stream {key[2:]} identical to numpy 2.4.6 (no stream change release-noted for this method)", False, f"{got[key]} vs {exp}")

# coverage self-check: every public distribution / sampling method was exercised above
used_src = open(__file__).read()
for cls, name in ((np.random.Generator, "Generator"), (np.random.RandomState, "RandomState")):
    meths = [m for m in dir(cls) if not m.startswith("_") and callable(getattr(cls, m))]
    missing = [m for m in meths if f".{m}(" not in used_src]
    report(f"coverage: every public {name} method is called somewhere in this harness", not missing, f"missing {missing}")
print(f"   total {time.time() - T_START:.1f} s")
