"""T1: TPM and effective length.

(a) abundance.tsv TPM recomputed from est_counts and eff_length with the
    documented formula (exact port of the arithmetic).
(b) --single -l/-s: eff_length of every target vs L - mu_L + 1 with mu_L the
    mean of the Gaussian(l, s) truncated to [0, L] (lengths 40..3000 bp,
    including targets shorter than -l), for several (l, s) incl. the survey's
    "-l 55 -s 1e-08" and "-l 50 -s 20".
(c) paired-end: the reported "estimated average fragment length" and the
    effective lengths implied mu_L = L + 1 - eff_length against the truth
    FLD the reads were simulated from (Gaussian 250/40 and 180/30).
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *

rng = random.Random(1)
d = tmpdir()
print("kallisto", kversion())

# transcriptome: random genes plus targets of fixed lengths 40..3000
lens = [40, 60, 80, 100, 120, 150, 180, 200, 220, 250, 300, 400, 600, 999, 1000, 1001, 1500, 3000]
extra = [("len%04d" % L, rand_seq(rng, L)) for L in lens]
tx = make_transcriptome(rng, n_genes=40, extra=extra)
idx = build_index(tx, d)
names = list(tx)
rho = {n: rng.lognormvariate(0, 1) for n in names}

fails = 0

def check_tpm(ab, label):
    global fails
    c = [ab[n]["est_counts"] for n in names]
    el = [ab[n]["eff_length"] for n in names]
    t = tpm_from(c, el)
    worst = max(abs(a - ab[n]["tpm"]) / max(ab[n]["tpm"], 1e-9) for a, n in zip(t, names) if ab[n]["tpm"] > 1e-3)
    ok = worst < 1e-4
    fails += not ok
    print("%s %s: TPM from est_counts/eff_length matches the formula, worst rel. diff %.2e"
          % ("ok  " if ok else "FAIL", label, worst))

# (b) single-end eff lens
for (l, s) in [(200, 20), (180, 30), (50, 20), (55, 1e-8), (300, 80)]:
    p = gauss_fld(l, s, minlen=0)
    frags, _ = simulate(rng, tx, rho, gauss_fld(l, s if s > 1 else 1, minlen=1), 4000, read_len=50, paired=False)
    out, err = run_quant(idx, d, frags, paired=False, single_l=l, single_s=s, name="se_%g_%g" % (l, s), extra=["--plaintext"])
    ab = read_abundance(os.path.join(out, "abundance.tsv"))
    worst = 0.0; worst_n = None
    rows = []
    for n in names:
        L = len(tx[n])
        # kallisto's truncation: FLD on 0..999; targets >= 1000 use the full mean
        Lc = min(L, 999)
        exp = L - trunc_mean(p, Lc) + 1
        if trunc_mean(p, Lc) == 0.0:
            exp = L + 1
        got = ab[n]["eff_length"]
        diff = abs(got - exp) / exp
        if diff > worst:
            worst, worst_n = diff, n
        if n.startswith("len"):
            rows.append((n, L, "%.3f" % exp, "%.3f" % got))
    ok = worst < 1e-4
    fails += not ok
    print("%s --single -l %g -s %g: eff_length vs L - mu_L + 1 (truncated Gaussian), worst rel. diff %.2e (%s)"
          % ("ok  " if ok else "FAIL", l, s, worst, worst_n))
    for r in rows:
        print("       %-8s L=%5d  port=%10s  kallisto=%10s" % r)
    check_tpm(ab, "--single -l %g -s %g" % (l, s))

# (c) paired-end FLD estimate
for (m, s) in [(250, 40), (180, 30)]:
    p = gauss_fld(m, s, minlen=1)
    frags, _ = simulate(rng, tx, rho, p, 30000, read_len=75, paired=True)
    true_mean = sum(x[2] for x in frags) / len(frags)
    out, err = run_quant(idx, d, frags, paired=True, name="pe_%d" % m, extra=["--plaintext"])
    ab = read_abundance(os.path.join(out, "abundance.tsv"))
    est = stderr_mean_fl(err)
    print("     paired-end FLD N(%d,%d): simulated fragments mean %.2f (all), kallisto 'estimated average fragment length' %.2f"
          % (m, s, true_mean, est))
    # implied truncated means for the fixed-length targets
    for n in names:
        if not n.startswith("len"):
            continue
        L = len(tx[n])
        mu_impl = L + 1 - ab[n]["eff_length"]
        print("       %-8s L=%5d  eff_length=%9.3f  implied mu_L=%8.3f  truth mu_L=%8.3f"
              % (n, L, ab[n]["eff_length"], mu_impl, trunc_mean(p, min(L, 999))))
    check_tpm(ab, "paired-end N(%d,%d)" % (m, s))

print("FAILURES:", fails)
