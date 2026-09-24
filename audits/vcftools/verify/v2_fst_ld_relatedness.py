"""V2: --weir-fst-pop (per site, the log's mean and weighted estimates, and
--fst-window-size/--fst-window-step) against a port of Weir & Cockerham 1984;
--hap-r2 / --geno-r2 against exact r2, D, D'; --relatedness2 against the
KING-robust estimator with complete data and with missing genotypes.

Two populations of 20 diploids drawn from different allele frequencies
(Fst about 0.1), 1,500 biallelic + 5 % triallelic sites, phased genotypes.
"""
import random, sys, os, collections, math, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(7)
print(f"vcftools {version()}")
d = tmpdir()
N1 = N2 = 20; N = N1 + N2
samples = [f"a{i:02d}" for i in range(N1)] + [f"b{i:02d}" for i in range(N2)]
pop1 = samples[:N1]; pop2 = samples[N1:]

def make_sites(missing_rate, n_sites=1500, span=300000, tri=0.05):
    positions = sorted(rng.sample(range(1, span), n_sites)); sites = []
    for pos in positions:
        if rng.random() < tri:
            f1 = [0.5, 0.3, 0.2]; f2 = [0.6, 0.1, 0.3]; alts = ["C", "G"]
        else:
            p = rng.uniform(0.05, 0.95); dev = rng.gauss(0, math.sqrt(0.1 * p * (1 - p)))
            p1 = min(0.98, max(0.02, p + dev)); p2 = min(0.98, max(0.02, p - dev))
            f1 = [p1, 1 - p1]; f2 = [p2, 1 - p2]; alts = ["C"]
        gts = []
        for i in range(N):
            f = f1 if i < N1 else f2
            if rng.random() < missing_rate: gts.append((None, None, True))
            else: gts.append((rng.choices(range(len(f)), f)[0], rng.choices(range(len(f)), f)[0], True))
        sites.append(Site("chr1", pos, "A", alts, 100.0, "PASS", gts, [20] * N, [60] * N))
    return sites

for label, miss in (("complete genotypes", 0.0), ("8 % missing genotypes", 0.08)):
    sites = make_sites(miss); by_pos = {s.pos: s for s in sites}
    vcf = os.path.join(d, f"f{int(miss * 100)}.vcf"); write_vcf(vcf, samples, sites)
    p1 = pop_file(d, "pop1.txt", pop1); p2 = pop_file(d, "pop2.txt", pop2)
    # ---- per-site Fst
    outs, log = run(vcf, ["--weir-fst-pop", p1, "--weir-fst-pop", p2])
    rows = outs["weir.fst"][1:]
    bad = 0; sum1 = sum2 = sum3 = 0.0; cnt = 0
    for r in rows:
        s = by_pos[int(r[1])]
        pg = [[(a, b) for a, b, _ in s.gts[:N1]], [(a, b) for a, b, _ in s.gts[N1:]]]
        sa, sall, fst = wc_fst(pg)
        got = float(r[2]) if r[2] not in ("-nan", "nan") else float("nan")
        if not close(got, fst): bad += 1
        if not math.isnan(fst): sum1 += sa; sum2 += sall; sum3 += fst; cnt += 1
    report(f"--weir-fst-pop per site ({label}): {len(rows)} sites; WEIR_AND_COCKERHAM_FST = sum_a / sum(a+b+c) over alleles equals the port on {len(rows) - bad}/{len(rows)}", bad == 0)
    import re
    m_mean = re.search(r"mean Fst estimate: ([-\d.e]+)", log); m_w = re.search(r"weighted Fst estimate: ([-\d.e]+)", log)
    report(f"  log: mean Fst {m_mean.group(1)} (port {sum3 / cnt:.5f}), weighted Fst {m_w.group(1)} (port {sum1 / sum2:.5f})",
           abs(float(m_mean.group(1)) - sum3 / cnt) < 6e-6 and abs(float(m_w.group(1)) - sum1 / sum2) < 6e-6)
    # ---- windowed Fst
    W, step = 50000, 25000
    outs, log = run(vcf, ["--weir-fst-pop", p1, "--weir-fst-pop", p2, "--fst-window-size", W, "--fst-window-step", step])
    rows = outs["windowed.weir.fst"][1:]
    bins = collections.defaultdict(lambda: [0.0, 0.0, 0.0, 0])
    for s in sites:
        pg = [[(a, b) for a, b, _ in s.gts[:N1]], [(a, b) for a, b, _ in s.gts[N1:]]]
        sa, sall, fst = wc_fst(pg)
        if math.isnan(fst): continue
        first = max(0, math.ceil((s.pos - W) / step)); last = math.ceil(s.pos / step)
        for idx in range(first, last):
            b = bins[idx]; b[0] += sa; b[1] += sall; b[2] += fst; b[3] += 1
    bad = 0
    for r in rows:
        idx = (int(r[1]) - 1) // step; b = bins[idx]
        if int(r[3]) != b[3] or not close(float(r[4]), b[0] / b[1]) or not close(float(r[5]), b[2] / b[3]): bad += 1
    report(f"--fst-window-size {W} --fst-window-step {step} ({label}): {len(rows)} windows; N_VARIANTS, WEIGHTED_FST = sum a / sum (a+b+c), MEAN_FST = mean of per-site Fst on {len(rows) - bad}/{len(rows)}", bad == 0 and len(rows) == len(bins))

# ---- LD on the complete, phased library
sites = make_sites(0.0, n_sites=300, span=60000, tri=0.0); by_pos = {s.pos: s for s in sites}
vcf = os.path.join(d, "ld.vcf"); write_vcf(vcf, samples, sites)
outs, log = run(vcf, ["--hap-r2", "--ld-window-bp", 5000, "--min-r2", 0.0])
rows = outs["hap.ld"][1:]
bad = 0
for r in rows:
    s1, s2 = by_pos[int(r[1])], by_pos[int(r[2])]
    h1 = [x for a, b, _ in s1.gts for x in (a, b)]; h2 = [x for a, b, _ in s2.gts for x in (a, b)]
    r2, D, Dp = ld_stats([1 - x for x in h1], [1 - x for x in h2])     # vcftools indexes on the reference allele
    if int(r[3]) != 2 * N or not close(float(r[4]), r2) or not close(float(r[5]), D) or not close(float(r[6]), Dp): bad += 1
n_pairs = sum(1 for i in range(len(sites)) for j in range(i + 1, len(sites)) if sites[j].pos - sites[i].pos <= 5000)
report(f"--hap-r2 --ld-window-bp 5000: {len(rows)} pairs (expected {n_pairs}); N_CHR, R^2, D and Dprime on {len(rows) - bad}/{len(rows)}", bad == 0 and len(rows) == n_pairs)
outs, log = run(vcf, ["--geno-r2", "--ld-window-bp", 5000, "--min-r2", 0.0])
rows = outs["geno.ld"][1:]
bad = 0
for r in rows:
    s1, s2 = by_pos[int(r[1])], by_pos[int(r[2])]
    g1 = [(a == 0) + (b == 0) for a, b, _ in s1.gts]; g2 = [(a == 0) + (b == 0) for a, b, _ in s2.gts]
    mx, my = statistics.mean(g1), statistics.mean(g2)
    cov = sum((x - mx) * (y - my) for x, y in zip(g1, g2)); vx = sum((x - mx) ** 2 for x in g1); vy = sum((y - my) ** 2 for y in g2)
    r2 = cov * cov / (vx * vy)
    if int(r[3]) != N or not close(float(r[4]), r2): bad += 1
report(f"--geno-r2 --ld-window-bp 5000: {len(rows)} pairs (expected {n_pairs}); N_INDV and R^2 = squared Pearson correlation of dosages on {len(rows) - bad}/{len(rows)}", bad == 0 and len(rows) == n_pairs)

# ---- relatedness2: complete data vs the same genotypes with 20 % missing calls
base = make_sites(0.0, n_sites=3000, span=600000, tri=0.0)
# make individuals b00..b04 clones of a00..a04 (kinship 0.5 with self, 0.5 duplicates) and b05 a child of a05 x a06
sites_full = []
for s in base:
    g = list(s.gts)
    for k in range(5): g[N1 + k] = g[k]
    ga, gb = g[5], g[6]; g[N1 + 5] = (rng.choice(ga[:2]), rng.choice(gb[:2]), True)
    sites_full.append(s._replace(gts=g))
sites_miss = [s._replace(gts=[(None, None, True) if rng.random() < 0.2 else g for g in s.gts]) for s in sites_full]
def king(s_list, i, j):
    n_aa_bb = n_AAaa = n_Ai = n_Aj = 0
    for s in s_list:
        a, b = s.gts[i][:2], s.gts[j][:2]
        if a[0] is None or b[0] is None: continue
        ha = a[0] != a[1]; hb = b[0] != b[1]
        n_aa_bb += ha and hb; n_AAaa += (not ha) and (not hb) and a[0] != b[0]; n_Ai += ha; n_Aj += hb
    return (n_aa_bb - 2 * n_AAaa) / (n_Ai + n_Aj)
def vcftools_style(s_list, i, j):
    n_aa_bb = n_AAaa = n_Ai = n_Aj = 0
    for s in s_list:
        a, b = s.gts[i][:2], s.gts[j][:2]
        if a[0] is not None and a[0] != a[1]: n_Ai += 1
        if b[0] is not None and b[0] != b[1]: n_Aj += 1
        if a[0] is None or b[0] is None: continue
        ha = a[0] != a[1]; hb = b[0] != b[1]
        n_aa_bb += ha and hb; n_AAaa += (not ha) and (not hb) and a[0] != b[0]
    return (n_aa_bb - 2 * n_AAaa) / (n_Ai + n_Aj)
pairs = [(0, N1), (1, N1 + 1), (5, N1 + 5), (6, N1 + 5), (0, 1), (7, N1 + 7)]
for label, sl in (("complete", sites_full), ("20 % missing", sites_miss)):
    vcf = os.path.join(d, f"rel_{label[:3]}.vcf"); write_vcf(vcf, samples, sl)
    outs, log = run(vcf, ["--relatedness2"])
    tab = {(r[0], r[1]): float(r[6]) for r in outs["relatedness2"][1:]}
    print(f"   --relatedness2, {label}:")
    ok_v = ok_k = True
    for i, j in pairs:
        got = tab[(samples[i], samples[j])]; kk = king(sl, i, j); vv = vcftools_style(sl, i, j)
        ok_v &= close(got, vv); ok_k &= close(got, kk)
        print(f"      {samples[i]}-{samples[j]:5s} RELATEDNESS_PHI {got:8.4f}   KING-robust over shared called sites {kk:8.4f}   het counts over each individual's own called sites {vv:8.4f}")
    print(f"   --relatedness2 ({label}): equals the estimator with per-individual heterozygote counts over that individual's own called sites (master's arithmetic): {'yes' if ok_v else 'no'}")
    report(f"--relatedness2 ({label}): equals KING-robust with all counts over the sites called in both individuals", ok_k,
           "" if ok_k else "(with missing calls the denominator counts heterozygous sites the partner is not called at, so kinship is underestimated)")
