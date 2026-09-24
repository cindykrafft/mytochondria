"""V3: the site and genotype filters the cohort applies before every statistic
(--maf, --max-maf, --mac, --max-missing, --max-missing-count, --minQ, --minDP,
--minGQ, --min-alleles/--max-alleles, --remove-indels, --keep-only-indels,
--thin, --remove-filtered-all) against the set of sites a direct reading of
the manual keeps, using --kept-sites and --missing-site.
"""
import random, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(11)
print(f"vcftools {version()}")
d = tmpdir()
N = 30; samples = [f"s{i:02d}" for i in range(N)]
sites = []
for pos in sorted(rng.sample(range(1, 100000), 1200)):
    u = rng.random()
    if u < 0.08: alts = ["CT"]; freqs = [0.7, 0.3]            # insertion
    elif u < 0.14: ref = "AT"; alts = ["A"]; freqs = [0.8, 0.2]  # deletion
    elif u < 0.24: alts = ["C", "G"]; freqs = [0.6, 0.3, 0.1]   # triallelic (third allele rare)
    else: p = rng.uniform(0.0, 1.0); alts = ["C"]; freqs = [p, 1 - p]
    ref = "AT" if (0.08 <= u < 0.14) else "A"
    miss = rng.choice([0.0, 0.05, 0.15, 0.3, 0.5])
    gts = [(None, None, False) if rng.random() < miss else (rng.choices(range(len(freqs)), freqs)[0], rng.choices(range(len(freqs)), freqs)[0], False) for _ in range(N)]
    dps = [rng.choice([2, 5, 8, 12, 25]) for _ in range(N)]; gqs = [rng.choice([5, 15, 25, 40, 90]) for _ in range(N)]
    sites.append(Site("chr1", pos, ref, alts, round(rng.uniform(5, 100), 1), rng.choice(["PASS", "PASS", "PASS", "LowQual"]), gts, dps, gqs))
vcf = os.path.join(d, "f.vcf"); write_vcf(vcf, samples, sites, with_dp=True, with_gq=True)
by_pos = {s.pos: s for s in sites}

def kept(args):
    outs, log = run(vcf, args + ["--kept-sites"])
    return {int(r[1]) for r in outs["kept.sites"][1:]}

def alleles_of(s, gt_filter=None):
    out = []
    for i, (a, b, _) in enumerate(s.gts):
        if a is None: continue
        if gt_filter and not gt_filter(s, i): continue
        out += [a, b]
    return out

def check(label, args, keep_fn):
    got = kept(args); exp = {s.pos for s in sites if keep_fn(s)}
    only_got = got - exp; only_exp = exp - got
    return report(f"{label}: kept {len(got)} sites (expected {len(exp)})", got == exp, "" if got == exp else f"(kept but not expected {len(only_got)}, expected but dropped {len(only_exp)})")

def maf(s):
    al = alleles_of(s); n = len(al); c = collections.Counter(al)
    return min(min(c.get(k, 0) / n, 1 - c.get(k, 0) / n) for k in range(1 + len(s.alts)))
def mac(s):
    al = alleles_of(s); c = collections.Counter(al)
    return min(min(c.get(k, 0), len(al) - c.get(k, 0)) for k in range(1 + len(s.alts)))
def call_rate(s): return sum(1 for a, b, _ in s.gts if a is not None) / N
def is_indel(s): return len(s.ref) != 1 or any(len(a) != 1 for a in s.alts)

check("--maf 0.05 (manual: minor allele frequency over non-missing alleles; the code takes the least frequent allele of the site)", ["--maf", "0.05"], lambda s: maf(s) >= 0.05)
check("--max-maf 0.1", ["--max-maf", "0.1"], lambda s: maf(s) <= 0.1)
check("--mac 3", ["--mac", "3"], lambda s: mac(s) >= 3)
check("--max-missing 0.9 (call rate >= 0.9)", ["--max-missing", "0.9"], lambda s: call_rate(s) >= 0.9)
check("--max-missing 1", ["--max-missing", "1"], lambda s: call_rate(s) >= 1)
check("--max-missing-count 3 (manual: sites with 'more than this number of missing genotypes' are excluded)", ["--max-missing-count", "3"], lambda s: sum(1 for a, b, _ in s.gts if a is None) <= 3)
got = kept(["--max-missing-count", "3"])
print(f"   --max-missing-count 3: vcftools keeps {len(got)}; sites with <= 3 missing genotypes {sum(1 for s in sites if sum(1 for a, b, _ in s.gts if a is None) <= 3)}; sites with <= 3 missing chromosomes (<= 1 genotype) {sum(1 for s in sites if 2 * sum(1 for a, b, _ in s.gts if a is None) <= 3)}")
check("--minQ 30", ["--minQ", "30"], lambda s: s.qual >= 30)
check("--remove-filtered-all (FILTER = PASS)", ["--remove-filtered-all"], lambda s: s.filt == "PASS")
check("--remove-indels", ["--remove-indels"], lambda s: not is_indel(s))
check("--keep-only-indels", ["--keep-only-indels"], lambda s: is_indel(s))
check("--min-alleles 2 --max-alleles 2", ["--min-alleles", "2", "--max-alleles", "2"], lambda s: len(s.alts) == 1)
# genotype-level filters set genotypes to missing; then --max-missing applies to the surviving calls
gf_dp = lambda s, i: s.dp[i] >= 10
gf_gq = lambda s, i: s.gq[i] >= 20
check("--minDP 10 --max-missing 0.8 (genotypes with DP < 10 become missing first)", ["--minDP", "10", "--max-missing", "0.8"],
      lambda s: sum(1 for i, (a, b, _) in enumerate(s.gts) if a is not None and gf_dp(s, i)) / N >= 0.8)
check("--minGQ 20 --max-missing 0.8", ["--minGQ", "20", "--max-missing", "0.8"],
      lambda s: sum(1 for i, (a, b, _) in enumerate(s.gts) if a is not None and gf_gq(s, i)) / N >= 0.8)
check("--minDP 10 --maf 0.05 (MAF over the genotypes that survive the DP filter; a site with no surviving call passes, its MAF being NaN)", ["--minDP", "10", "--maf", "0.05"],
      lambda s: (lambda al: min(min(collections.Counter(al).get(k, 0) / len(al), 1 - collections.Counter(al).get(k, 0) / len(al)) for k in range(1 + len(s.alts))) >= 0.05 if al else True)(alleles_of(s, gf_dp)))
# --thin
got = kept(["--thin", "500"])
exp = set(); last = -10**9
for s in sites:
    if s.pos - last >= 500: exp.add(s.pos); last = s.pos
report(f"--thin 500: keeps a site when it is at least 500 bp after the last kept site ({len(got)} vs {len(exp)})", got == exp)
got = kept(["--thin", "500"]); # also check strictly-greater interpretation
exp2 = set(); last = -10**9
for s in sites:
    if s.pos - last > 500: exp2.add(s.pos); last = s.pos
print(f"   --thin: 'at least 500 bp' set size {len(exp)}, 'more than 500 bp' set size {len(exp2)}, vcftools {len(got)}")
# --missing-site after --minDP: N_GENOTYPES_FILTERED column
outs, log = run(vcf, ["--minDP", "10", "--missing-site"]); rows = outs["lmiss"][1:]
bad = 0
for r in rows:
    s = by_pos[int(r[1])]
    # vcf_entry::filter_genotypes_by_depth marks every genotype with DP outside the range, missing calls included, so a ./. with DP < 10 is "filtered", not "missing"
    nfilt = sum(1 for i in range(N) if not gf_dp(s, i))
    nmiss = sum(1 for i, (a, b, _) in enumerate(s.gts) if a is None and gf_dp(s, i))
    # layout: N_DATA = chromosomes of unfiltered genotypes (2N - 2 x filtered), N_GENOTYPES_FILTERED = filtered genotypes, N_MISS = missing chromosomes among them, F_MISS = N_MISS / N_DATA
    ok = int(r[2]) == 2 * (N - nfilt) and int(r[3]) == nfilt and int(r[4]) == 2 * nmiss and close(float(r[5]), 2 * nmiss / (2 * (N - nfilt)) if N > nfilt else float("nan"))
    if not ok: bad += 1
print(f"   --minDP 10 --missing-site: first row {rows[0]}")
report(f"--missing-site after --minDP: N_DATA = chromosomes of unfiltered genotypes, N_GENOTYPES_FILTERED, N_MISS = missing chromosomes, F_MISS = N_MISS / N_DATA on {len(rows) - bad}/{len(rows)} sites", bad == 0)
# the same sites under --max-missing: the call rate counts filtered genotypes as missing
outs2, log2 = run(vcf, ["--minDP", "10", "--max-missing", "0.9", "--kept-sites"]); kept09 = {int(r[1]) for r in outs2["kept.sites"][1:]}
f_miss = {int(r[1]): float(r[5]) for r in rows}
low_fmiss_dropped = sum(1 for p, f in f_miss.items() if f <= 0.1 and p not in kept09)
print(f"   after --minDP 10: {sum(1 for f in f_miss.values() if f <= 0.1)} sites report F_MISS <= 0.1 in --missing-site, of which {low_fmiss_dropped} are dropped by --max-missing 0.9 (the call rate there counts the filtered genotypes as missing)")
report("--missing-site's F_MISS and --max-missing's call rate treat depth-filtered genotypes the same way (F_MISS leaves them out of N_DATA; the call rate N_non_missing_chr / N_chr counts them as missing)", low_fmiss_dropped == 0)
