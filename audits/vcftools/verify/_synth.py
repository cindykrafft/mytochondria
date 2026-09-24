"""Shared helpers for the VCFtools harnesses: a VCF writer for diploid
genotypes with optional missing calls, per-genotype DP/GQ, site QUAL and
FILTER, multi-allelic sites and phasing; a runner that calls `vcftools` with
`--out` in a temp dir and returns the output tables parsed by suffix; and the
statistics recomputed exactly in Python (per-site pi, Tajima's D constants,
Weir & Cockerham 1984 Fst, the Wigginton HWE exact test, KING-robust
relatedness, r2/D/D').

Every harness takes the directory holding the `vcftools` binary as argv[1]
(default $VCFTOOLS_BIN_DIR, else PATH).
"""
import collections, glob, itertools, math, os, random, subprocess, sys, tempfile

def bin_dir():
    return sys.argv[1] if len(sys.argv) > 1 else os.environ.get("VCFTOOLS_BIN_DIR", "")

def vcftools_exe():
    return os.path.join(bin_dir(), "vcftools") if bin_dir() else "vcftools"

def version():
    p = subprocess.run([vcftools_exe(), "--version"], capture_output=True, text=True)
    return (p.stdout + p.stderr).strip().split("\n")[0].replace("VCFtools (", "").rstrip(")")

def tmpdir():
    return tempfile.mkdtemp(prefix="vcft_")

Site = collections.namedtuple("Site", "chrom pos ref alts qual filt gts dp gq")
# gts: list of (a, b, phased) with a/b allele indices or None for missing

def write_vcf(path, samples, sites, with_dp=False, with_gq=False):
    with open(path, "w") as f:
        f.write("##fileformat=VCFv4.2\n")
        chroms = []
        for s in sites:
            if s.chrom not in chroms: chroms.append(s.chrom)
        for c in chroms:
            f.write(f"##contig=<ID={c},length=100000000>\n")
        f.write('##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">\n')
        f.write('##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read depth">\n')
        f.write('##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype quality">\n')
        f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t" + "\t".join(samples) + "\n")
        fmt = "GT" + (":DP" if with_dp else "") + (":GQ" if with_gq else "")
        for s in sites:
            cols = [s.chrom, str(s.pos), ".", s.ref, ",".join(s.alts), str(s.qual), s.filt, ".", fmt]
            for i, (a, b, ph) in enumerate(s.gts):
                g = "./." if a is None else f"{a}{'|' if ph else '/'}{b}"
                if with_dp: g += f":{s.dp[i]}"
                if with_gq: g += f":{s.gq[i]}"
                cols.append(g)
            f.write("\t".join(cols) + "\n")

def run(vcf, args, keep=None):
    """Run vcftools; returns (outputs: {suffix: rows (list of lists)}, log text)."""
    d = tmpdir()
    cmd = [vcftools_exe(), "--vcf", vcf, "--out", os.path.join(d, "o")] + [str(a) for a in args]
    if keep:
        kp = os.path.join(d, "keep.txt"); open(kp, "w").write("\n".join(keep) + "\n"); cmd += ["--keep", kp]
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=d)
    outs = {}
    for f in glob.glob(os.path.join(d, "o.*")):
        suf = os.path.basename(f)[2:]
        if suf == "log": continue
        rows = [l.rstrip("\n").split("\t") for l in open(f) if l.strip()]
        outs[suf] = rows
    log = open(os.path.join(d, "o.log")).read() if os.path.exists(os.path.join(d, "o.log")) else p.stderr
    if p.returncode != 0:
        log += f"\n[vcftools exited with status {p.returncode}: {p.stderr.strip()[-200:]}]"
        outs["_crash"] = p.returncode
    return outs, log + p.stderr

def close(a, b, rel=6e-6, abs_=1e-12):
    """vcftools prints doubles with 6 significant digits."""
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= abs_ + rel * max(abs(a), abs(b))

def report(label, ok, detail=""):
    print(f"{'ok  ' if ok else 'FAIL'} {label}{('  ' + detail) if detail else ''}")
    return ok

def pop_file(d, name, samples):
    p = os.path.join(d, name); open(p, "w").write("\n".join(samples) + "\n"); return p

# ------------------------------------------------------------- exact statistics
def site_pi(gts):
    """Nei's per-site pi over non-missing alleles: mismatching pairs / all ordered pairs."""
    alleles = [x for a, b, _ in gts if a is not None for x in (a, b)]
    n = len(alleles); c = collections.Counter(alleles)
    if n < 2: return float("nan")
    return sum(k * (n - k) for k in c.values()) / (n * (n - 1))

def tajima_constants(n):
    a1 = sum(1.0 / i for i in range(1, n)); a2 = sum(1.0 / (i * i) for i in range(1, n))
    b1 = (n + 1) / (3.0 * (n - 1)); b2 = 2.0 * (n * n + n + 3) / (9.0 * n * (n - 1))
    c1 = b1 - 1 / a1; c2 = b2 - (n + 2) / (a1 * n) + a2 / (a1 * a1)
    return a1, a2, c1 / a1, c2 / (a1 * a1 + a2)

def tajima_d(pis_sum_p1p, S, n):
    """VCFtools' form: pi = 2 * sum p(1-p) * n/(n-1), theta_w = S/a1."""
    a1, a2, e1, e2 = tajima_constants(n)
    pi = 2.0 * pis_sum_p1p * n / (n - 1); tw = S / a1
    return (pi - tw) / math.sqrt(e1 * S + e2 * S * (S - 1))

def wc_fst(pop_gts):
    """Weir & Cockerham 1984 per-site: pop_gts = list over populations of lists of (a, b) with None for missing.
    Returns (sum_a, sum_all, fst) summing the per-allele a, b, c over all alleles present."""
    r = len(pop_gts)
    alleles = sorted({x for pg in pop_gts for a, b in pg if a is not None for x in (a, b)})
    n = [sum(1 for a, b in pg if a is not None) for pg in pop_gts]
    n_sum = sum(n); nbar = n_sum / r
    nc = (n_sum - sum(x * x for x in n) / n_sum) / (r - 1)
    sum_a = sum_all = 0.0
    for j in alleles:
        p = [sum((a == j) + (b == j) for a, b in pg if a is not None) / (2.0 * n[i]) for i, pg in enumerate(pop_gts)]
        pbar = sum(n[i] * p[i] for i in range(r)) / n_sum
        hbar = sum(sum(1 for a, b in pg if a is not None and a != b and (a == j or b == j)) for pg in pop_gts) / n_sum
        ssqr = sum(n[i] * (p[i] - pbar) ** 2 for i in range(r)) / ((r - 1) * nbar)
        a = nbar / nc * (ssqr - (pbar * (1 - pbar) - (r - 1) / r * ssqr - hbar / 4) / (nbar - 1))
        b = nbar / (nbar - 1) * (pbar * (1 - pbar) - (r - 1) / r * ssqr - (2 * nbar - 1) / (4 * nbar) * hbar)
        c = hbar / 2
        sum_a += a; sum_all += a + b + c
    return sum_a, sum_all, (sum_a / sum_all if sum_all != 0 else float("nan"))

def hwe_exact(obs_hets, obs_hom1, obs_hom2):
    """Wigginton, Cutler & Abecasis 2005 exact test; returns (p_hwe, p_het_deficit, p_het_excess)."""
    obs_homc = max(obs_hom1, obs_hom2); obs_homr = min(obs_hom1, obs_hom2)
    rare = 2 * obs_homr + obs_hets; genotypes = obs_hets + obs_homc + obs_homr
    probs = [0.0] * (rare + 1)
    mid = rare * (2 * genotypes - rare) // (2 * genotypes)
    if (rare & 1) != (mid & 1): mid += 1
    curr_homr = (rare - mid) // 2; curr_homc = genotypes - mid - curr_homr
    probs[mid] = 1.0; total = 1.0
    curr_hets = mid
    while curr_hets > 1:
        probs[curr_hets - 2] = probs[curr_hets] * curr_hets * (curr_hets - 1.0) / (4.0 * (curr_homr + 1.0) * (curr_homc + 1.0))
        total += probs[curr_hets - 2]; curr_hets -= 2; curr_homr += 1; curr_homc += 1
    curr_hets = mid; curr_homr = (rare - mid) // 2; curr_homc = genotypes - mid - curr_homr
    while curr_hets <= rare - 2:
        probs[curr_hets + 2] = probs[curr_hets] * 4.0 * curr_homr * curr_homc / ((curr_hets + 2.0) * (curr_hets + 1.0))
        total += probs[curr_hets + 2]; curr_hets += 2; curr_homr -= 1; curr_homc -= 1
    probs = [x / total for x in probs]
    p_hi = sum(probs[i] for i in range(obs_hets, rare + 1))      # het excess: P(hets >= observed)
    p_lo = sum(probs[i] for i in range(0, obs_hets + 1))         # het deficit: P(hets <= observed)
    p_hwe = min(1.0, sum(x for x in probs if x <= probs[obs_hets]))
    return p_hwe, p_lo, p_hi

def king_robust(g1, g2):
    """Manichaikul 2010 KING-robust kinship from 0/1/2 dosages (None = missing):
    (N_Aa,Bb - 2 N_AA,bb) / (N_Aa + N_Bb) ... the estimator VCFtools implements is checked in the harness."""
    pairs = [(a, b) for a, b in zip(g1, g2) if a is not None and b is not None]
    n_aa_bb = sum(1 for a, b in pairs if a == 1 and b == 1)
    n_AA_bb = sum(1 for a, b in pairs if (a == 0 and b == 2) or (a == 2 and b == 0))
    n_Aa = sum(1 for a, b in pairs if a == 1); n_Bb = sum(1 for a, b in pairs if b == 1)
    return (n_aa_bb - 2 * n_AA_bb) / (n_Aa + n_Bb) if (n_Aa + n_Bb) else float("nan")

def ld_stats(h1, h2):
    """r2, D, D' from two lists of haplotype alleles (0/1) of equal length (phased, no missing)."""
    n = len(h1); pA = sum(h1) / n; pB = sum(h2) / n
    pAB = sum(1 for a, b in zip(h1, h2) if a == 1 and b == 1) / n
    D = pAB - pA * pB
    denom = pA * (1 - pA) * pB * (1 - pB)
    r2 = D * D / denom if denom else float("nan")
    dmax = min(pA * (1 - pB), (1 - pA) * pB) if D > 0 else min(pA * pB, (1 - pA) * (1 - pB))
    return r2, D, (D / dmax if dmax else float("nan"))
