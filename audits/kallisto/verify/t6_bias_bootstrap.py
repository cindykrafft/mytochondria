"""T6: --bias and bootstraps.

(a) Bootstraps without --bias: the mean of B bootstrap est_counts against
    the point estimate (a bootstrap of a multinomial resample should centre on
    it), and each bs_abundance_*.tsv's TPM against its own est_counts and
    eff_length (port of the formula).
(b) Bootstraps with --bias: Bootstrap::run_em (Bootstrap.cpp:4-13) builds a
    new EMAlgorithm from the fragment-length means, i.e. with the plain
    effective lengths L - mu_L + 1, and runs it with recomputeEffLen = false,
    while the point estimate's EM replaces them with bias-corrected lengths
    at round 50 (EMAlgorithm.h, update_eff_lens).  The plaintext/HDF5
    writers then report every bootstrap with the point estimate's
    bias-corrected eff_length.  Measured: bootstrap mean vs point estimate
    under --bias, on a library simulated with a start-site sequence bias so
    that the bias-corrected lengths differ from the plain ones.
(c) --bias on an unbiased library: reported eff_length vs L - mu_L + 1 for
    long targets (update_eff_lens sums L - mu - 6 forward and L - mu reverse
    start positions, half each).
"""
import os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *

rng = random.Random(6)
d = tmpdir()
ver = kversion()
print("kallisto", ver)


def biased_frags(tx, rho, p, n, strength):
    """Rejection-sample fragments under kallisto's model with an extra
    acceptance weight that depends on the GC content of the 6-mer at read 1's
    5' end (2 bases upstream, 4 into the read, read-1 strand)."""
    out = []
    while len(out) < n:
        fr, _ = simulate(rng, tx, rho, p, n, read_len=75, paired=True)
        for x in fr:
            name, st, f, a, b, flip = x
            s = tx[name]
            if not flip:
                ctx = s[max(0, st - 2):st + 4]
            else:
                e = st + f
                ctx = revcomp(s[e - 4:e + 2])
            gc = sum(1 for c in ctx if c in "GC")
            w = (1 + strength * gc) / (1 + strength * 6)
            if rng.random() < w:
                out.append(x)
            if len(out) >= n:
                break
    return out


def bs_tables(out, B):
    tabs = []
    for b in range(B):
        pth = os.path.join(out, "bs_abundance_%d.tsv" % b)
        if os.path.exists(pth):
            tabs.append(read_abundance(pth))
    return tabs


tx = make_transcriptome(rng, n_genes=60, max_iso=5, exon_len=(80, 400), n_exons=(3, 8))
names = list(tx)
idx = build_index(tx, d)
rho = {n: rng.lognormvariate(1.5, 1.2) for n in names}
p = gauss_fld(250, 40)
B = 60

for label, strength, extra in [("unbiased library, no --bias", 0.0, []),
                               ("GC-biased library, no --bias", 3.0, []),
                               ("GC-biased library, --bias", 3.0, ["--bias"])]:
    frags = biased_frags(tx, rho, p, 40000, strength) if strength > 0 else simulate(rng, tx, rho, p, 40000, read_len=75)[0]
    out, err = run_quant(idx, d, frags, paired=True, name="bs_%s" % label.replace(" ", "_").replace(",", "").replace("-", ""),
                         extra=["--plaintext", "-b", str(B)] + extra)
    ab = read_abundance(os.path.join(out, "abundance.tsv"))
    tabs = bs_tables(out, B)
    print("\n%s: %d fragments, %d bootstraps" % (label, len(frags), len(tabs)))
    # TPM formula inside each bootstrap table
    worst = 0.0
    for t in tabs:
        c = [t[n]["est_counts"] for n in names]; el = [t[n]["eff_length"] for n in names]
        tp = tpm_from(c, el)
        worst = max(worst, max(abs(a - t[n]["tpm"]) / t[n]["tpm"] for a, n in zip(tp, names) if t[n]["tpm"] > 1))
    print("   bootstrap TPM vs est_counts/eff_length formula: worst rel. diff %.1e" % worst)
    same_el = all(t[n]["eff_length"] == ab[n]["eff_length"] for t in tabs for n in names)
    print("   bootstrap tables carry the point estimate's eff_length: %s" % same_el)
    # centring: z = (mean_bs - point) / (sd_bs / sqrt(B))
    zs = []
    rows = []
    for n in names:
        v = [t[n]["est_counts"] for t in tabs]
        m = statistics.mean(v); sd = statistics.pstdev(v)
        pt = ab[n]["est_counts"]
        if pt < 50 or sd == 0:
            continue
        z = (m - pt) / (sd / math.sqrt(len(v)))
        zs.append(z)
        rows.append((abs(z), n, pt, m, sd, (m - pt) / pt))
    rows.sort(reverse=True)
    big = sum(1 for z in zs if abs(z) > 4)
    print("   targets with >= 50 reads: %d; |mean_bs - point| / (sd_bs/sqrt(B)) > 4 for %d; median |z| %.2f"
          % (len(zs), big, statistics.median([abs(z) for z in zs])))
    for az, n, pt, m, sd, rel in rows[:6]:
        print("     %-9s point %9.1f  bootstrap mean %9.1f  (%+.1f %%)  sd %7.1f  z %+.1f"
              % (n, pt, m, 100 * rel, sd, (m - pt) / (sd / math.sqrt(len(tabs)))))
    # how far bias-corrected lengths moved
    if "--bias" in extra:
        plain = [eff_len_model(p, min(len(tx[n]), 999)) + max(0, len(tx[n]) - 999) for n in names]
        r = sorted(ab[n]["eff_length"] / pl for n, pl in zip(names, plain))
        print("   bias-corrected / plain eff_length: min %.3f median %.3f max %.3f" % (r[0], r[len(r) // 2], r[-1]))
        # EM with the plain lengths on the point estimate's classes: compare to the bootstrap mean
        comp = Compat(tx)
        ec = collections.Counter(comp.fragment_ec(x[3], x[4]) for x in frags)
        ec.pop(frozenset(), None)
        a_plain, _ = em(ec, plain, len(names), tol=1e-10)
        a_bias, _ = em(ec, [ab[n]["eff_length"] for n in names], len(names), tol=1e-10)
        dd = []
        for i, n in enumerate(names):
            v = [t[n]["est_counts"] for t in tabs]
            if ab[n]["est_counts"] >= 50:
                dd.append((abs(statistics.mean(v) - a_plain[i]), abs(statistics.mean(v) - a_bias[i])))
        print("   bootstrap means: mean |bs_mean - EM(plain eff_length)| %.2f vs mean |bs_mean - EM(bias eff_length)| %.2f reads"
              % (statistics.mean(x[0] for x in dd), statistics.mean(x[1] for x in dd)))

# (c) --bias on an unbiased library, long single-isoform targets
tx2 = collections.OrderedDict(("u%02d" % i, rand_seq(rng, rng.randint(1500, 3000))) for i in range(40))
idx2 = build_index(tx2, d)
rho2 = {n: 1.0 for n in tx2}
fr2, _ = simulate(rng, tx2, rho2, p, 200000, read_len=75)
out, err = run_quant(idx2, d, fr2, paired=True, name="unbiased_bias", extra=["--plaintext", "--bias"])
ab2 = read_abundance(os.path.join(out, "abundance.tsv"))
est_mu = stderr_mean_fl(err)
diffs = [ab2[n]["eff_length"] - (len(tx2[n]) - est_mu + 1) for n in tx2]
print("\n--bias on an unbiased library (40 single-isoform targets 1.5-3 kb, 200,000 pairs):")
print("   eff_length - (L - mu + 1), mu = kallisto's FLD mean %.2f: mean %+.2f, median %+.2f, sd %.2f"
      % (est_mu, statistics.mean(diffs), statistics.median(diffs), statistics.pstdev(diffs)))
