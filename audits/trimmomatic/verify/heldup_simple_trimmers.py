#!/usr/bin/env python3
"""Held-up checks: the single-read trimmers of Trimmomatic against independent
Python references, record by record, on synthetic reads with known qualities.

Usage: python3 heldup_simple_trimmers.py <trimmomatic.jar | build dir>

Steps covered: SLIDINGWINDOW, LEADING, TRAILING, MAXINFO, MINLEN, MAXLEN, CROP,
HEADCROP, TAILCROP, AVGQUAL, BASECOUNT, TOPHRED33/TOPHRED64, -phred64 input,
automatic Phred detection, and a multi-step pipeline. Every read carries a
unique name so the output can be matched to the input; output order is checked.
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trimmomatic_ref as R

target = sys.argv[1]
rng = random.Random(20260909)

N = 4000
reads = []
for i in range(N):
    n = rng.randint(1, 160)
    seq = R.mutate(rng, R.rand_seq(rng, n), 0.0, allow_n=0.03)
    prof = rng.choice(["mixed", "mixed", "uniform", "high"])
    reads.append(("r%d" % i, seq, R.rand_quals(rng, n, prof)))
print("reads: %d, lengths %d-%d" % (N, min(len(s) for _, s, _ in reads), max(len(s) for _, s, _ in reads)))


def compare(label, steps, ref_fn, offset=33, opts=(), out_offset=None):
    out, log = R.run_se(target, reads, steps, opts=opts, offset=offset)
    got = {name: (seq, q) for name, seq, q in out}
    names_out = [name for name, _, _ in out]
    # expected
    exp = {}
    for name, seq, quals in reads:
        r = ref_fn(seq, quals)
        if r is not None:
            s, e = r
            exp[name] = (seq[s:e], quals[s:e])
    order_ok = names_out == [n for n, _, _ in reads if n in exp]
    mism = [n for n in exp if n not in got or got[n][0] != exp[n][0] or got[n][1] != exp[n][1]]
    extra = [n for n in got if n not in exp]
    n_drop = N - len(exp)
    print("%-52s kept %4d dropped %4d | jar==ref on %d/%d reads, %d unexpected in output, order %s"
          % (label, len(exp), n_drop, N - len(mism) - len(extra), N, len(extra), "kept" if order_ok else "CHANGED"))
    for n in (mism + extra)[:3]:
        print("    e.g. %s: jar=%s ref=%s" % (n, got.get(n, ("<dropped>",))[0], exp.get(n, ("<dropped>",))[0]))
    return len(mism) + len(extra)


bad = 0
print("\n== SLIDINGWINDOW (as-coded reference: keep to the end of the last passing window, then strip trailing bases < quality)")
for w, q in ((4, 20), (4, 15), (5, 20), (10, 25), (1, 20), (4, 30), (3, 3)):
    bad += compare("SLIDINGWINDOW:%d:%d" % (w, q), ["SLIDINGWINDOW:%d:%d" % (w, q)],
                   lambda s, ql, w=w, q=q: R.sliding_window_coded(s, ql, w, q))
print("  -- the README's wording read literally (cut at the start of the first failing window) differs from the jar on:")
for w, q in ((4, 20), (4, 15)):
    diff = 0
    for name, seq, quals in reads:
        if R.sliding_window_coded(seq, quals, w, q) != R.sliding_window_doc(seq, quals, w, q):
            diff += 1
    print("     SLIDINGWINDOW:%d:%d  %d/%d reads (design choice, see review N-notes)" % (w, q, diff, N))
short = sum(1 for _, s, _ in reads if len(s) < 4)
print("  -- reads shorter than the window (%d of %d here for w=4) are dropped by the jar (as-coded reference agrees above)" % (short, N))

print("\n== LEADING / TRAILING")
for t in (3, 10, 20, 30):
    bad += compare("LEADING:%d" % t, ["LEADING:%d" % t], lambda s, ql, t=t: R.leading(s, ql, t))
    bad += compare("TRAILING:%d (as coded, base 0 never checked)" % t, ["TRAILING:%d" % t],
                   lambda s, ql, t=t: R.trailing_coded(s, ql, t))
    d = sum(1 for _, s, ql in reads if R.trailing_coded(s, ql, t) != R.trailing_doc(s, ql, t))
    print("     TRAILING:%d: reads whose only base >= %d is base 0 (dropped by the jar, 1 nt by the README): %d/%d" % (t, t, d, N))

print("\n== MAXINFO (float reference of the coded formula; ties may differ in the last ulp)")
for tl, st in ((40, 0.8), (50, 0.5), (36, 0.9), (100, 0.2), (75, 0.5)):
    bad += compare("MAXINFO:%d:%s" % (tl, st), ["MAXINFO:%d:%s" % (tl, st)],
                   lambda s, ql, tl=tl, st=st: R.maxinfo(s, ql, tl, st))

print("\n== MINLEN / MAXLEN / CROP / HEADCROP / TAILCROP / AVGQUAL / BASECOUNT")
for n in (36, 50, 1, 160):
    bad += compare("MINLEN:%d" % n, ["MINLEN:%d" % n], lambda s, ql, n=n: R.minlen(s, ql, n))
for n in (100, 20):
    bad += compare("MAXLEN:%d" % n, ["MAXLEN:%d" % n], lambda s, ql, n=n: R.maxlen(s, ql, n))
for n in (100, 36, 1):
    bad += compare("CROP:%d" % n, ["CROP:%d" % n], lambda s, ql, n=n: R.crop(s, ql, n))
for n in (10, 1, 50):
    bad += compare("HEADCROP:%d (read of <= n bases dropped)" % n, ["HEADCROP:%d" % n], lambda s, ql, n=n: R.headcrop(s, ql, n))
    bad += compare("TAILCROP:%d" % n, ["TAILCROP:%d" % n], lambda s, ql, n=n: R.tailcrop(s, ql, n))
for t in (20, 25, 30):
    bad += compare("AVGQUAL:%d" % t, ["AVGQUAL:%d" % t], lambda s, ql, t=t: R.avgqual(s, ql, t))
bad += compare("BASECOUNT:N:0:2", ["BASECOUNT:N:0:2"], lambda s, ql: R.basecount(s, ql, "N", 0, 2))
bad += compare("BASECOUNT:GC:20", ["BASECOUNT:GC:20"], lambda s, ql: R.basecount(s, ql, "GC", 20))

print("\n== TOPHRED64 / TOPHRED33 and -phred64 input")
out, _ = R.run_se(target, reads, ["TOPHRED64"], opts=["-phred33"])
ok = sum(1 for (n1, s1, q1), (n2, s2, q2) in zip(reads, out) if n1 == n2 and s1 == s2 and q1 == q2)
print("%-52s %d/%d records identical after re-decoding with offset 64" % ("TOPHRED64 on phred33 input", ok, N))
bad += N - ok
out, _ = R.run_se(target, reads, ["TOPHRED33"], opts=["-phred64"], offset=64)
ok = sum(1 for (n1, s1, q1), (n2, s2, q2) in zip(reads, out) if n1 == n2 and s1 == s2 and q1 == q2)
print("%-52s %d/%d records identical after re-decoding with offset 33" % ("TOPHRED33 on phred64 input", ok, N))
bad += N - ok
# a quality trimmer on phred64 input must use the phred64 values
out, _ = R.run_se(target, reads, ["LEADING:20", "TRAILING:20"], opts=["-phred64"], offset=64)
got = {n: s for n, s, _ in out}
ok = 0; kept = 0
for n, s, q in reads:
    a = R.leading(s, q, 20)
    e = None
    if a is not None:
        b = R.trailing_coded(s[a[0]:], q[a[0]:], 20)
        if b is not None:
            e = s[a[0]:a[0] + b[1]]
    if e is not None:
        kept += 1
    if (n in got) == (e is not None) and (e is None or got[n] == e):
        ok += 1
print("%-52s %d/%d reads agree with the reference (%d kept)" % ("LEADING:20 TRAILING:20 with -phred64", ok, N, kept))
bad += N - ok

print("\n== automatic Phred detection (no -phred flag)")
for off, prof, label in ((33, "mixed", "phred33 data, mixed qualities"), (64, "mixed", "phred64 data, mixed qualities"),
                         (33, "high", "phred33 data, all Q30-41")):
    sub = [(n, s, R.rand_quals(rng, len(s), prof)) for n, s, _ in reads[:2000]]
    try:
        out, log = R.run_se(target, sub, ["MINLEN:1"], offset=off, autodetect=True)
        det = [l for l in log.splitlines() if "detected" in l or "Unable" in l]
        ok = sum(1 for (n1, s1, q1), (n2, s2, q2) in zip(sub, out) if n1 == n2 and s1 == s2 and q1 == q2)
        print("%-52s %s; %d/%d records round-trip" % (label, det[0].strip() if det else "(no detection message)", ok, len(sub)))
    except RuntimeError as e:
        msg = [l for l in str(e).splitlines() if "Unable" in l or "Error" in l]
        print("%-52s FAILED: %s" % (label, msg[:1]))

print("\n== pipeline: ILLUMINACLIP-free multi-step order (LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36)")
def pipe(s, ql):
    a = R.leading(s, ql, 3)
    if a is None: return None
    s1, q1 = s[a[0]:], ql[a[0]:]
    b = R.trailing_coded(s1, q1, 3)
    if b is None: return None
    s2, q2 = s1[:b[1]], q1[:b[1]]
    c = R.sliding_window_coded(s2, q2, 4, 15)
    if c is None: return None
    s3 = s2[:c[1]]
    if len(s3) < 36: return None
    return (a[0], a[0] + c[1])
bad += compare("LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36", ["LEADING:3", "TRAILING:3", "SLIDINGWINDOW:4:15", "MINLEN:36"], pipe)

print("\nTOTAL record mismatches across all checks: %d" % bad)
