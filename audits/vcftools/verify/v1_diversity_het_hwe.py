"""V1: --site-pi, --window-pi (with and without --window-pi-step), --TajimaD,
--het, --hardy, --freq/--counts, --missing-indv, --missing-site, --depth,
--site-mean-depth and --012, recomputed exactly from a generated VCF of 40
diploid individuals, 2,000 sites on one chromosome (5 % triallelic, 4 %
monomorphic, 8 % missing genotypes), plus a complete-data copy for Tajima's D.
"""
import random, sys, os, collections, math, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(1)
print(f"vcftools {version()}")
d = tmpdir()
N = 40; samples = [f"s{i:02d}" for i in range(N)]

def make_sites(missing_rate, n_sites=2000, chrom="chr1", span=200000):
    positions = sorted(rng.sample(range(1, span), n_sites))
    sites = []
    for pos in positions:
        u = rng.random()
        if u < 0.05:
            freqs = [0.6, 0.3, 0.1]; alts = ["C", "G"]
        elif u < 0.09:
            freqs = [1.0, 0.0]; alts = ["C"]
        else:
            p = rng.uniform(0.02, 0.98); freqs = [p, 1 - p]; alts = ["C"]
        gts = []; dps = []; gqs = []
        for i in range(N):
            if rng.random() < missing_rate:
                gts.append((None, None, False))
            else:
                a = rng.choices(range(len(freqs)), freqs)[0]; b = rng.choices(range(len(freqs)), freqs)[0]
                gts.append((a, b, False))
            dps.append(rng.randint(3, 40)); gqs.append(rng.randint(5, 99))
        sites.append(Site(chrom, pos, "A", alts, round(rng.uniform(10, 500), 1), "PASS", gts, dps, gqs))
    return sites

sites = make_sites(0.08)
vcf = os.path.join(d, "a.vcf"); write_vcf(vcf, samples, sites, with_dp=True, with_gq=True)
by_pos = {s.pos: s for s in sites}

# ---- --site-pi
outs, log = run(vcf, ["--site-pi"])
rows = outs["sites.pi"][1:]
bad = sum(1 for r in rows if not close(float(r[2]), site_pi(by_pos[int(r[1])].gts)))
report(f"--site-pi: {len(rows)} sites; pi = mismatching pairs / ordered pairs of non-missing alleles on {len(rows) - bad}/{len(rows)}", bad == 0 and len(rows) == len(sites))

# ---- --window-pi
def window_pi_truth(W, step):
    Nchr = 2 * N; mono_pairs = Nchr * (Nchr - 1)
    bins = collections.defaultdict(lambda: [0, 0, 0])   # n_poly, pairs, mismatches
    for s in sites:
        alleles = [x for a, b, _ in s.gts if a is not None for x in (a, b)]
        n = len(alleles); c = collections.Counter(alleles)
        mism = sum(k * (n - k) for k in c.values())
        if mism == 0: continue
        first = max(0, math.ceil((s.pos - W) / step)); last = math.ceil(s.pos / step)
        for idx in range(first, last):
            bins[idx][0] += 1; bins[idx][1] += n * (n - 1); bins[idx][2] += mism
    out = {}
    for idx, (npoly, pairs, mism) in bins.items():
        mono = W - npoly
        out[idx * step + 1] = (npoly, mono, mism / (pairs + mono * mono_pairs))
    return out
for W, step in ((10000, 10000), (10000, 2500)):
    outs, log = run(vcf, ["--window-pi", W, "--window-pi-step", step])
    rows = outs["windowed.pi"][1:]
    truth = window_pi_truth(W, step)
    bad = 0
    has_mono = len(rows[0]) == 6            # master prints N_MONOMORPHIC; 0.1.16 and earlier do not
    for r in rows:
        t = truth.get(int(r[1])); pi_col = 5 if has_mono else 4
        if t is None or int(r[3]) != t[0] or (has_mono and int(r[4]) != t[1]) or not close(float(r[pi_col]), t[2]): bad += 1
    report(f"--window-pi {W} --window-pi-step {step}: {len(rows)} windows; N_VARIANTS{', N_MONOMORPHIC = W - N_VARIANTS' if has_mono else ''}, and PI = mismatches / (pairs at variant sites + (W - N_VARIANTS) x 2N(2N-1)) on {len(rows) - bad}/{len(rows)}",
           bad == 0 and len(rows) == len(truth))

# ---- --TajimaD on complete data, then with missing genotypes
sites_full = make_sites(0.0)
vcf_full = os.path.join(d, "full.vcf"); write_vcf(vcf_full, samples, sites_full)
def tajima_truth(sites, W, n):
    bins = collections.defaultdict(lambda: [0, 0.0])
    for s in sites:
        if len(s.alts) != 1: continue
        alleles = [x for a, b, _ in s.gts if a is not None for x in (a, b)]
        p = alleles.count(0) / len(alleles)
        if 0 < p < 1:
            b = s.pos // W; bins[b][0] += 1; bins[b][1] += p * (1 - p)
    return {b * W: (S, tajima_d(sp, S, n)) for b, (S, sp) in bins.items()}
outs, log = run(vcf_full, ["--TajimaD", 10000])
rows = outs["Tajima.D"][1:]; truth = tajima_truth(sites_full, 10000, 2 * N)
bad = sum(1 for r in rows if int(r[2]) != truth.get(int(r[1]), (None,))[0] or not close(float(r[3]), truth[int(r[1])][1]))
report(f"--TajimaD 10000, complete genotypes: {len(rows)} bins; N_SNPS and D (pi = 2 sum p(1-p) n/(n-1), theta_w = S/a1, n = 2 x individuals) on {len(rows) - bad}/{len(rows)}", bad == 0)
outs, log = run(vcf, ["--TajimaD", 10000])
rows = outs["Tajima.D"][1:]; truth = tajima_truth(sites, 10000, 2 * N)
bad = sum(1 for r in rows if not close(float(r[3]), truth[int(r[1])][1]))
print(f"   --TajimaD with 8 % missing genotypes: D reproduced with n fixed at 2 x individuals (80) and per-site p over the non-missing alleles on {len(rows) - bad}/{len(rows)} bins (the sample size per site is 65-80; the statistic assumes a constant n)")

# ---- --het
outs, log = run(vcf, ["--het"])
rows = outs["het"][1:]
bad = 0
for r in rows:
    i = samples.index(r[0]); obs = 0; exp = 0.0; nsites = 0
    for s in sites:
        if len(s.alts) != 1: continue
        alleles = [x for a, b, _ in s.gts if a is not None for x in (a, b)]
        n = len(alleles); freq = alleles.count(1) / n
        if freq <= 1e-15 or 1 - freq <= 1e-15: continue
        a, b, _ = s.gts[i]
        if a is None: continue
        nsites += 1; obs += (a == b); exp += 1 - 2 * freq * (1 - freq) * n / (n - 1)
    F = (obs - exp) / (nsites - exp)
    if int(r[1]) != obs or abs(float(r[2]) - exp) > 0.051 or int(r[3]) != nsites or abs(float(r[4]) - F) > 1e-4: bad += 1
report(f"--het: O(HOM), E(HOM) = sum 1 - 2p(1-p) n/(n-1) over biallelic polymorphic sites where the individual is called, N_SITES and F on {len(rows) - bad}/{len(rows)} individuals (E(HOM) printed to 1 decimal, F to 5)", bad == 0)

# ---- --hardy
outs, log = run(vcf, ["--hardy"])
rows = outs["hwe"][1:]
bad = 0; checked = 0
for r in rows:
    s = by_pos[int(r[1])]
    if len(s.alts) != 1: continue
    checked += 1
    g = [(a, b) for a, b, _ in s.gts if a is not None]
    b11 = sum(1 for a, b in g if a == 0 and b == 0); b12 = sum(1 for a, b in g if a != b); b22 = sum(1 for a, b in g if a == 1 and b == 1)
    tot = len(g); freq = (2 * b11 + b12) / (2 * tot)
    e11, e12, e22 = freq * freq * tot, 2 * freq * (1 - freq) * tot, (1 - freq) ** 2 * tot
    chisq = (b11 - e11) ** 2 / e11 + (b12 - e12) ** 2 / e12 + (b22 - e22) ** 2 / e22 if e11 > 0 and e12 > 0 and e22 > 0 else float("nan")
    p_hwe, p_lo, p_hi = hwe_exact(b12, b11, b22)
    obs = r[2].split("/"); exp = r[3].split("/")
    ok = [int(obs[0]), int(obs[1]), int(obs[2])] == [b11, b12, b22] and all(abs(float(exp[k]) - v) < 0.0051 for k, v in enumerate((e11, e12, e22)))
    ok = ok and (math.isnan(chisq) or close(float(r[4]), chisq)) and close(float(r[5]), p_hwe) and close(float(r[6]), p_lo) and close(float(r[7]), p_hi)
    if not ok: bad += 1
report(f"--hardy: observed and expected genotype counts, chi-square, and the exact-test P_HWE / P_HET_DEFICIT / P_HET_EXCESS (Wigginton 2005 port) on {checked - bad}/{checked} biallelic sites", bad == 0)

# ---- --freq and --counts
outs, log = run(vcf, ["--freq"]); rows = outs["frq"][1:]
bad = 0
for r in rows:
    s = by_pos[int(r[1])]; alleles = [x for a, b, _ in s.gts if a is not None for x in (a, b)]
    n = len(alleles); nal = 1 + len(s.alts)
    fr = [float(x.split(":")[1]) for x in r[4:]]
    exp = [alleles.count(k) / n for k in range(nal)]
    if int(r[2]) != nal or int(r[3]) != n or any(not close(a, b) for a, b in zip(fr, exp)): bad += 1
report(f"--freq: N_ALLELES, N_CHR (non-missing alleles) and each allele's frequency on {len(rows) - bad}/{len(rows)} sites", bad == 0)
outs, log = run(vcf, ["--counts"]); rows = outs["frq.count"][1:]
bad = sum(1 for r in rows if [int(x.split(":")[1]) for x in r[4:]] != [[x for a, b, _ in by_pos[int(r[1])].gts if a is not None for x in (a, b)].count(k) for k in range(1 + len(by_pos[int(r[1])].alts))])
report(f"--counts: allele counts on {len(rows) - bad}/{len(rows)} sites", bad == 0)

# ---- missingness
outs, log = run(vcf, ["--missing-indv"]); rows = outs["imiss"][1:]
bad = 0
for r in rows:
    i = samples.index(r[0]); nmiss = sum(1 for s in sites if s.gts[i][0] is None)
    if int(r[1]) != len(sites) or int(r[3]) != nmiss or abs(float(r[4]) - nmiss / len(sites)) > 1e-9: bad += 1
report(f"--missing-indv: N_DATA, N_MISS and F_MISS on {len(rows) - bad}/{len(rows)} individuals", bad == 0)
outs, log = run(vcf, ["--missing-site"]); rows = outs["lmiss"][1:]
bad = 0
for r in rows:
    s = by_pos[int(r[1])]; nmiss = 2 * sum(1 for a, b, _ in s.gts if a is None)
    if int(r[2]) != 2 * N or int(r[4]) != nmiss or abs(float(r[5]) - nmiss / (2 * N)) > 1e-9: bad += 1
report(f"--missing-site: N_DATA (= 2 x individuals), N_MISS (missing chromosomes) and F_MISS on {len(rows) - bad}/{len(rows)} sites", bad == 0)

# ---- depth
outs, log = run(vcf, ["--depth"]); rows = outs["idepth"][1:]
bad = 0
for r in rows:
    i = samples.index(r[0])
    dps = [s.dp[i] for s in sites]                       # every genotype carries a DP, missing calls included
    dps_called = [s.dp[i] for s in sites if s.gts[i][0] is not None]
    m_all = statistics.mean(dps); m_called = statistics.mean(dps_called)
    got = float(r[2]); nsites = int(r[1])
    if not ((nsites == len(dps) and abs(got - m_all) < 1e-6) or (nsites == len(dps_called) and abs(got - m_called) < 1e-6)): bad += 1
print(f"   --depth: N_SITES {rows[0][1]} of {len(sites)} for the first individual ({sum(1 for s in sites if s.gts[0][0] is not None)} called); MEAN_DEPTH {rows[0][2]}")
report(f"--depth: MEAN_DEPTH equals the mean DP over the sites counted in N_SITES on {len(rows) - bad}/{len(rows)} individuals", bad == 0)
outs, log = run(vcf, ["--site-mean-depth"]); rows = outs["ldepth.mean"][1:]
bad = 0; var_kind = collections.Counter()
for r in rows:
    s = by_pos[int(r[1])]; dps = [s.dp[i] for i in range(N)]; dps_called = [s.dp[i] for i in range(N) if s.gts[i][0] is not None]
    got_m, got_v = float(r[2]), float(r[3])
    ok = False
    for dd in (dps, dps_called):
        m = statistics.mean(dd)
        if close(got_m, m):
            for kind, v in (("sample", statistics.variance(dd)), ("population", statistics.pvariance(dd))):
                if close(got_v, v): ok = True; var_kind[(len(dd) == N, kind)] += 1
    if not ok: bad += 1
print(f"   --site-mean-depth: variance definition found: {dict(var_kind)} (key: (all genotypes incl. missing calls?, variance kind))")
report(f"--site-mean-depth: MEAN_DEPTH and VAR_DEPTH consistent with one definition on {len(rows) - bad}/{len(rows)} sites", bad == 0)

# ---- --012
outs, log = run(vcf, ["--012"])
if "012" not in outs:
    report("--012: the matrix is written", False, "(" + log.strip().splitlines()[-1][:160] + ")")
    sys.exit(0)
mat = outs["012"]; pos_rows = outs["012.pos"]; ind = outs["012.indv"]
bi = [s for s in sites if len(s.alts) == 1]     # the writer skips multi-allelic sites with a one-off log warning ("012: Only outputting biallelic loci.")
bad = 0
for r in mat:
    i = int(r[0]); vals = [int(x) for x in r[1:]]
    exp = [(-1 if s.gts[i][0] is None else (s.gts[i][0] != 0) + (s.gts[i][1] != 0)) for s in bi]
    if vals != exp: bad += 1
print(f"   --012: {len(pos_rows)} positions listed of {len(sites)} sites ({len(sites) - len(bi)} multi-allelic sites skipped); log: {[l for l in log.splitlines() if '012' in l][-1].strip()[:80]}")
report(f"--012: dosage of non-reference alleles (-1 for missing) over the biallelic sites on {len(mat) - bad}/{len(mat)} individuals", bad == 0 and len(pos_rows) == len(bi))
