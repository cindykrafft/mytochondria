#!/usr/bin/env python3
"""BF1 (unit level): the exact trigger and the direction of the error in
bcftools' Mann-Whitney bias Z-score, by calling the SHIPPED function.

`calc_mwu_biasZ()` (bam2bcf.c) is linked straight out of the audited build's
`bam2bcf.o` into a tiny C driver, so the arithmetic executed here is byte for
byte the arithmetic that `bcftools mpileup` runs when it writes INFO/MQBZ,
BQBZ, RPBZ, SCBZ, MQSBZ and NMBZ.  The end-to-end evidence is in
bf1_mwu_tie_overflow.py; this harness answers three questions the end-to-end
run cannot answer cheaply:

  1. exactly which pileups trigger it (the boundary in the tie-bin count p),
  2. whether the reported |Z| is ever too LARGE (a false filter) or only ever
     too SMALL (a real bias that escapes the filter),
  3. whether it can collapse to exactly 0 ("no bias") or to nan/inf.

Truth is the same Mann-Whitney normal approximation with tie correction that
the C code intends, evaluated in Python integers (unbounded), cross-checked
against scipy.stats.mannwhitneyu on the expanded samples.

usage: python bf1b_mwu_unit_surface.py <bcftools-src-dir> <htslib-dir> [workdir]
"""
import math, os, subprocess, sys, tempfile

DRIVER_C = r'''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
double calc_mwu_biasZ(int *a, int *b, int n, int left_only, int do_Z);
int main(void){
    static char line[1<<20];
    while (fgets(line,sizeof line,stdin)){
        char name[256]; int n, i;
        char *tok=strtok(line," \t\n"); if(!tok) continue;
        strcpy(name,tok); n=atoi(strtok(NULL," \t\n"));
        int *a=calloc(n,sizeof(int)), *b=calloc(n,sizeof(int));
        char *as=strtok(NULL," \t\n"), *bs=strtok(NULL," \t\n");
        i=0; for(char*q=strtok(as,",");q&&i<n;q=strtok(NULL,","))a[i++]=atoi(q);
        i=0; for(char*q=strtok(bs,",");q&&i<n;q=strtok(NULL,","))b[i++]=atoi(q);
        printf("%s\t%.6f\n",name,calc_mwu_biasZ(a,b,n,0,1));
        free(a); free(b);
    }
    return 0;
}
'''

INT32_MAX = 2147483647


def truth(a, b):
    """The tie-corrected normal-approximation Z the C code is written to compute,
    in exact Python integers."""
    n = len(a); e = l = na = nb = t = 0
    for i in range(n - 1, -1, -1):
        e += a[i] * b[i]
        l += a[i] * nb
        na += a[i]; nb += b[i]
        p = a[i] + b[i]
        t += (p * p - 1) * p
    if not na or not nb:
        return None
    U = l + e * 0.5
    m = na * nb / 2.0
    var2 = (na * nb) / 12.0 * ((na + nb + 1) - t / float((na + nb) * (na + nb - 1)))
    if var2 <= 0:
        return 0.0
    return (U - m) / math.sqrt(var2)


def scipy_truth(a, b):
    """Independent check of `truth` for small cases: expand the histograms into
    samples and use scipy's tie-corrected normal approximation."""
    try:
        from scipy.stats import mannwhitneyu
    except ImportError:
        return None
    import numpy as np
    xa = np.repeat(np.arange(len(a)), a)
    xb = np.repeat(np.arange(len(b)), b)
    if not len(xa) or not len(xb):
        return None
    r = mannwhitneyu(xa, xb, alternative='two-sided', method='asymptotic',
                     use_continuity=False)
    # recover the signed Z from U and the tie-corrected sd
    na, nb = len(xa), len(xb)
    U = r.statistic
    m = na * nb / 2.0
    import collections
    cnt = collections.Counter(np.concatenate([xa, xb]).tolist())
    tie = sum(c ** 3 - c for c in cnt.values())
    var = na * nb / 12.0 * ((na + nb + 1) - tie / float((na + nb) * (na + nb - 1)))
    return (U - m) / math.sqrt(var)


def wrap32(x):
    x &= 0xFFFFFFFF
    return x - (1 << 32) if x >= (1 << 31) else x


def replica(a, b):
    """Byte-for-byte replica of bam2bcf.c calc_mwu_biasZ, keeping every
    accumulator in the C declared width: e, l, na, nb, p are `int`, t is
    `int64_t` but is fed the `int`-typed product (p*p-1)*p."""
    n = len(a); e = l = na = nb = 0; t = 0
    for i in range(n - 1, -1, -1):
        e = wrap32(e + wrap32(a[i] * b[i]))
        l = wrap32(l + wrap32(a[i] * nb))
        na = wrap32(na + a[i]); nb = wrap32(nb + b[i])
        p = wrap32(a[i] + b[i])
        t += wrap32(wrap32(wrap32(p * p) - 1) * p)
    if not na or not nb:
        return None
    U = l + e * 0.5
    m = wrap32(na * nb) / 2.0
    var2 = wrap32(na * nb) / 12.0 * ((na + nb + 1) - t / float(wrap32((na + nb) * (na + nb - 1))))
    if var2 <= 0:
        return 0.0
    return (U - m) / math.sqrt(var2)


def mq_hist(nref_hi, nalt_hi, nalt_lo, lo=29, hi=59, nbins=60):
    """A realistic MQ histogram: reference reads and some alt reads at MQ>=59
    (the BWA/bowtie2 maximum, capped to bin 59 by bam2bcf.c:493), the rest of
    the alt reads at MQ 30."""
    a = [0] * nbins; b = [0] * nbins
    a[hi] = nref_hi; b[hi] = nalt_hi; b[lo] = nalt_lo
    return a, b


def build_driver(srcdir, htsdir, workdir):
    c = os.path.join(workdir, "mwu_drv.c")
    exe = os.path.join(workdir, "mwu_drv")
    open(c, "w").write(DRIVER_C)
    objs = [os.path.join(srcdir, o) for o in
            ("bam2bcf.o", "bam2bcf_iaux.o", "bam2bcf_indel.o",
             "read_consensus.o", "str_finder.o")]
    missing = [o for o in objs if not os.path.exists(o)]
    if missing:
        sys.exit("missing object files (run `make` in %s first): %s" % (srcdir, missing))
    hts = os.path.join(htsdir, "libhts.a")
    cmd = ["gcc", "-O2", "-o", exe, c] + objs + [hts,
           "-lz", "-lm", "-lbz2", "-llzma", "-lcurl", "-lcrypto",
           "-ldeflate", "-lpthread", "-ldl"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("link failed:\n" + r.stderr[-2000:])
    return exe


def run(exe, cases):
    inp = "".join("%s %d %s %s\n" % (nm, len(a), ",".join(map(str, a)), ",".join(map(str, b)))
                  for nm, a, b in cases)
    out = subprocess.run([exe], input=inp, capture_output=True, text=True).stdout
    return {ln.split("\t")[0]: float(ln.split("\t")[1]) for ln in out.strip().split("\n")}


def main():
    srcdir, htsdir = sys.argv[1], sys.argv[2]
    workdir = sys.argv[3] if len(sys.argv) > 3 else tempfile.mkdtemp()
    exe = build_driver(srcdir, htsdir, workdir)
    ver = subprocess.run([os.path.join(srcdir, "bcftools"), "--version"],
                         capture_output=True, text=True).stdout.split("\n")
    print("binary: %s / %s" % (ver[0].strip(), ver[1].strip()))
    print("shipped function: calc_mwu_biasZ() linked out of %s/bam2bcf.o" % srcdir)
    # the version string alone cannot tell a patched tree from an unpatched one,
    # so echo the declaration that decides the arithmetic
    for ln in open(os.path.join(srcdir, "bam2bcf.c")):
        if "l = 0, na = 0, nb = 0" in ln:
            print("accumulator declaration in bam2bcf.c: %s" % ln.strip())
            break
    print("INT32_MAX = %d ; cube root = %.2f\n" % (INT32_MAX, INT32_MAX ** (1 / 3.)))

    fails = 0          # real problems: scipy cross-check, unexpected boundary
    rep_ne = 0         # cases where the build disagrees with the int32 replica

    # ---- 1. `truth` agrees with scipy on a case small enough to expand -------
    a, b = mq_hist(400, 30, 20)
    st = scipy_truth(a, b)
    tz = truth(a, b)
    print("[cross-check] truth() vs scipy.stats.mannwhitneyu (tie-corrected, no "
          "continuity correction) on 400 ref / 50 alt reads: |Z| %.6f vs %s"
          % (abs(tz), "%.6f" % abs(st) if st is not None else "scipy unavailable"))
    print("  (scipy's U is taken over the first sample, so only |Z| is comparable;"
          " bcftools' sign convention is U(ref<alt) - mean.)")
    if st is not None and abs(abs(st) - abs(tz)) > 1e-6:
        fails += 1; print("  MISMATCH -> the Python truth is not trustworthy\n")
    else:
        print("  agree\n")

    # ---- 2. the boundary ----------------------------------------------------
    print("[boundary] one tie bin of p reads, 40 alt reads in a second bin.")
    print("%6s %14s %6s %12s %12s %12s  %s"
          % ("p", "p^3", "int32", "truth Z", "bcftools Z", "replica Z", ""))
    cases = []
    for p in range(1286, 1296):
        a = [0] * 60; b = [0] * 60
        a[59] = p - 1; b[59] = 1; b[29] = 40
        cases.append(("p%d" % p, a, b))
    got = run(exe, cases)
    first_bad = None
    for nm, a, b in cases:
        p = int(nm[1:]); tz = truth(a, b); gz = got[nm]; rz = replica(a, b)
        bad = abs(gz - tz) > 1e-3
        if bad and first_bad is None:
            first_bad = p
        if abs(gz - rz) > 1e-3:
            rep_ne += 1
        print("%6d %14d %6s %12.4f %12.4f %12.4f  %s"
              % (p, p ** 3, "OVF" if p ** 3 > INT32_MAX else "fits", tz, gz, rz,
                 "WRONG" if bad else "ok"))
    expect_p = int(INT32_MAX ** (1 / 3.)) + 1
    print("  first p that is wrong: %s (smallest p with p^3 > INT32_MAX: %d)"
          % (first_bad, expect_p))
    if first_bad is None:
        print("  no divergence anywhere in this range -- this is a build in which "
              "the accumulators are wide enough (i.e. patched)\n")
    elif first_bad != expect_p:
        fails += 1; print("  UNEXPECTED boundary\n")
    else:
        print()

    # ---- 3. direction, over a wide sweep ------------------------------------
    print("[direction] 5% alt fraction, half the alt reads at MQ30; total reads "
          "at the site swept.")
    cases = []
    for tot in list(range(1300, 60001, 137)) + [100000, 200000]:
        nalt = max(2, tot // 20)
        a, b = mq_hist(tot - nalt, nalt // 2, nalt - nalt // 2)
        cases.append(("t%d" % tot, a, b))
    got = run(exe, cases)
    n_wrong = n_infl = n_zero = n_nan = 0
    worst = None
    for nm, a, b in cases:
        tz = truth(a, b); gz = got[nm]; rz = replica(a, b)
        if abs(gz - rz) > 1e-3:
            rep_ne += 1
        if abs(gz - tz) > 1e-3:
            n_wrong += 1
            if abs(gz) > abs(tz) + 1e-9:
                n_infl += 1
            if abs(gz) < 1e-9:
                n_zero += 1
            if math.isnan(gz) or math.isinf(gz):
                n_nan += 1
            if worst is None or abs(tz) - abs(gz) > worst[1]:
                worst = (nm, abs(tz) - abs(gz), tz, gz)
    print("  %d cases, %d wrong; |Z| too LARGE in %d, exactly 0 in %d, nan/inf in %d"
          % (len(cases), n_wrong, n_infl, n_zero, n_nan))
    if worst is None:
        print("  no case diverges from the truth: nothing to report a direction for.\n")
    else:
        print("  worst under-report: %s truth %.4f -> bcftools %.4f (|Z| lost %.4f)"
              % (worst[0], worst[2], worst[3], worst[1]))
        print("  => the tie term is only ever wrapped DOWNWARD, so var2 is too "
              "large and the reported |Z| is always too small: a biased site is "
              "reported as less biased than it is, never more.\n")

    # ---- 4. does it change a filtering verdict? ----------------------------
    print("[filter impact] `MQBZ < -3` is the mapping-quality-bias cut in the "
          "bcftools/samtools \"calling SNPs/INDELs\" workflow and in the filter "
          "recipes built on it.  Sweep of pileups: total reads at the site x alt "
          "fraction x fraction of the alt reads carrying the lower MQ.")
    cases = []
    for tot in (1200, 1500, 2000, 3000, 5000, 8000, 12000, 20000):
        for altfrac in (0.02, 0.05, 0.10, 0.20):
            for lofrac in (0.05, 0.10, 0.25, 0.50, 1.0):
                nalt = max(4, int(tot * altfrac))
                nlo = max(1, int(nalt * lofrac))
                a, b = mq_hist(tot - nalt, nalt - nlo, nlo)
                cases.append(("f%d_%d_%d" % (tot, altfrac * 100, lofrac * 100), a, b))
    got = run(exe, cases)
    flips = []
    n_bad = 0
    for nm, a, b in cases:
        tz = truth(a, b); gz = got[nm]
        if abs(gz - tz) > 1e-3:
            n_bad += 1
        if tz < -3 and gz >= -3:
            flips.append((nm, max(a[i] + b[i] for i in range(60)), tz, gz))
    print("  %d pileups swept, %d get a wrong Z; in %d of them the MQBZ < -3 "
          "verdict FLIPS from drop to keep." % (len(cases), n_bad, len(flips)))
    print("  %-22s %8s %12s %12s" % ("total_altpct_lopct", "tie p", "truth Z", "bcftools Z"))
    for nm, p, tz, gz in flips[:12]:
        print("  %-22s %8d %12.4f %12.4f" % (nm, p, tz, gz))
    if len(flips) > 12:
        print("  ... and %d more" % (len(flips) - 12))
    print()

    print("harness self-check failures (scipy cross-check + boundary): %d" % fails)
    print("cases where this build disagrees with the int32-wrapping replica: %d "
          "(0 on an unpatched build -- the replica is exact; all of them on a "
          "build whose accumulators have been widened)" % rep_ne)


if __name__ == "__main__":
    main()
