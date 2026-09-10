#!/usr/bin/env python3
"""Held-up checks: paired-end bookkeeping, the summary line and -summary file,
-trimlog, keepBothReads / minAdapterLength, thread-count invariance, and inputs
of unequal length.

Usage: python3 heldup_pe_bookkeeping.py <trimmomatic.jar | build dir>

The pipeline ILLUMINACLIP:TruSeq3-PE-2.fa:2:30:10[:m:keep] LEADING:3 TRAILING:3
SLIDINGWINDOW:4:15 MINLEN:36 is applied to 3,000 synthetic pairs by the port and
by the jar; the four output files, the four counters and every trimlog line are
compared.
"""
import os, random, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trimmomatic_ref as R

target = sys.argv[1]
rng = random.Random(5)
P1 = "TACACTCTTTCCCTACACGACGCTCTTCCGATCT"; P2 = "GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT"
FA = [(">PrefixPE/1", P1), (">PrefixPE/2", P2), (">PE1", P1), (">PE1_rc", R.rc(P1)), (">PE2", P2), (">PE2_rc", R.rc(P2))]
tmp = os.path.join(os.environ.get("TMPDIR", "/tmp"), "trimmo_pe_%d" % os.getpid())
os.makedirs(tmp, exist_ok=True)
fa = os.path.join(tmp, "TruSeq3-PE-2.fa")
with open(fa, "w") as fh:
    for n, s in FA:
        fh.write("%s\n%s\n" % (n, s))

NP = 3000
pairs = []
for i in range(NP):
    L = rng.randint(0, 200)
    n1 = rng.choice([100, 100, 150, 75]); n2 = rng.choice([100, 100, 150, 75])
    F = R.rand_seq(rng, L)
    r1 = (F + R.rc(P2) + R.rand_seq(rng, n1))[:n1]
    r2 = (R.rc(F) + R.rc(P1) + R.rand_seq(rng, n2))[:n2]
    q1 = R.rand_quals(rng, n1, rng.choice(["mixed", "uniform", "high"]))
    q2 = R.rand_quals(rng, n2, rng.choice(["mixed", "uniform", "high"]))
    r1 = R.mutate(rng, r1, rng.choice([0, 0.01, 0.05]), allow_n=0.01)
    r2 = R.mutate(rng, r2, rng.choice([0, 0.01, 0.05]), allow_n=0.01)
    pairs.append(("pair%d/1 extra comment" % i, r1, q1, "pair%d/2 extra comment" % i, r2, q2))
recs1 = [(a, b, c) for a, b, c, d, e, f in pairs]
recs2 = [(d, e, f) for a, b, c, d, e, f in pairs]


def single_chain(seq, q):
    """LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 on one read; returns (start, end) or None."""
    a = R.leading(seq, q, 3)
    if a is None: return None
    s1, q1 = seq[a[0]:], q[a[0]:]
    b = R.trailing_coded(s1, q1, 3)
    if b is None: return None
    s2, q2 = s1[:b[1]], q1[:b[1]]
    c = R.sliding_window_coded(s2, q2, 4, 15)
    if c is None: return None
    if c[1] < 36: return None
    return (a[0], a[0] + c[1])


def port_pipeline(clip):
    res = []
    for n1, s1, q1, n2, s2, q2 in pairs:
        k1, k2 = clip.process((s1, q1), (s2, q2))
        o1 = single_chain(s1[:k1], q1[:k1]) if k1 else None
        o2 = single_chain(s2[:k2], q2[:k2]) if k2 else None
        res.append((o1, o2))
    return res


def check(label, steps, clip, threads=1, opts=()):
    d = os.path.join(tmp, re.sub(r"\W", "_", label)); os.makedirs(d, exist_ok=True)
    opts = list(opts) + ["-summary", os.path.join(d, "summary.txt"), "-trimlog", os.path.join(d, "trimlog.txt")]
    out, log = R.run_pe(target, recs1, recs2, steps, opts=opts, threads=threads, tmpdir=d)
    exp = port_pipeline(clip)
    both = fwd = rev = drop = 0
    e1P, e1U, e2P, e2U = [], [], [], []
    tl = []
    for (n1, s1, q1, n2, s2, q2), (o1, o2) in zip(pairs, exp):
        r1 = (n1, s1[o1[0]:o1[1]], q1[o1[0]:o1[1]]) if o1 else None
        r2 = (n2, s2[o2[0]:o2[1]], q2[o2[0]:o2[1]]) if o2 else None
        if r1 and r2: both += 1; e1P.append(r1); e2P.append(r2)
        elif r1: fwd += 1; e1U.append(r1)
        elif r2: rev += 1; e2U.append(r2)
        else: drop += 1
        for nm, sq, o in ((n1, s1, o1), (n2, s2, o2)):
            if o: tl.append("%s %d %d %d %d" % (nm, o[1] - o[0], o[0], o[1], len(sq) - o[1]))
            else: tl.append("%s 0 0 0 0" % nm)
    ok_files = all(out[k] == e for k, e in (("1P", e1P), ("1U", e1U), ("2P", e2P), ("2U", e2U)))
    m = re.search(r"Input Read Pairs: (\d+) Both Surviving: (\d+) \(([\d.]+)%\) Forward Only Surviving: (\d+) \(([\d.]+)%\) Reverse Only Surviving: (\d+) \(([\d.]+)%\) Dropped: (\d+) \(([\d.]+)%\)", log)
    got = tuple(int(m.group(i)) for i in (1, 2, 4, 6, 8)) if m else None
    pct = tuple(m.group(i) for i in (3, 5, 7, 9)) if m else None
    exp_pct = tuple("%.2f" % (100.0 * x / NP) for x in (both, fwd, rev, drop))
    summ = open(os.path.join(d, "summary.txt")).read().split("\n")
    sv = {l.split(": ")[0]: l.split(": ")[1] for l in summ if ": " in l}
    summ_ok = (sv.get("Input Read Pairs") == str(NP) and sv.get("Both Surviving Reads") == str(both)
               and sv.get("Forward Only Surviving Reads") == str(fwd) and sv.get("Reverse Only Surviving Reads") == str(rev)
               and sv.get("Dropped Reads") == str(drop) and sv.get("Both Surviving Read Percent") == exp_pct[0]
               and sv.get("Dropped Read Percent") == exp_pct[3])
    tlog = [l for l in open(os.path.join(d, "trimlog.txt")).read().split("\n") if l]
    tl_ok = tlog == tl
    print("%-46s outputs %s | counts jar=%s port=(%d, %d, %d, %d, %d) %s, sum=%s | percents %s | -summary %s | trimlog %d lines %s"
          % (label, "1P/1U/2P/2U identical" if ok_files else "DIFFER",
             got, NP, both, fwd, rev, drop, "match" if got == (NP, both, fwd, rev, drop) else "MISMATCH",
             "ok" if got and got[1] + got[2] + got[3] + got[4] == got[0] else "BAD",
             "match" if pct == exp_pct else "MISMATCH %s vs %s" % (pct, exp_pct),
             "match" if summ_ok else "MISMATCH", len(tlog), "match" if tl_ok else "MISMATCH"))
    if not tl_ok:
        for a, b in list(zip(tlog, tl))[:3]:
            if a != b: print("     trimlog jar: %r  port: %r" % (a, b))
    if not ok_files:
        for k, e in (("1P", e1P), ("1U", e1U), ("2P", e2P), ("2U", e2U)):
            if out[k] != e:
                print("     %s: jar %d records, port %d" % (k, len(out[k]), len(e)))
    return out, log


print("pairs: %d (insert 0-200, read lengths 75/100/150, errors 0-5%%, 1%% N)" % NP)
CHAIN = ["LEADING:3", "TRAILING:3", "SLIDINGWINDOW:4:15", "MINLEN:36"]
print("\n== ILLUMINACLIP variants, -threads 1")
base = check("ILLUMINACLIP:...:2:30:10 (default 8, keep=false)", ["ILLUMINACLIP:%s:2:30:10" % fa] + CHAIN, R.IlluminaClip(fa, 2, 30, 10))
check("ILLUMINACLIP:...:2:30:10:8:true (keepBothReads)", ["ILLUMINACLIP:%s:2:30:10:8:true" % fa] + CHAIN, R.IlluminaClip(fa, 2, 30, 10, 8, True))
check("ILLUMINACLIP:...:2:30:10:1:true (minAdapterLength 1)", ["ILLUMINACLIP:%s:2:30:10:1:true" % fa] + CHAIN, R.IlluminaClip(fa, 2, 30, 10, 1, True))
check("ILLUMINACLIP:...:2:30:10:12 (minAdapterLength 12)", ["ILLUMINACLIP:%s:2:30:10:12" % fa] + CHAIN, R.IlluminaClip(fa, 2, 30, 10, 12, False))
check("ILLUMINACLIP:...:1:20:7", ["ILLUMINACLIP:%s:1:20:7" % fa] + CHAIN, R.IlluminaClip(fa, 1, 20, 7))

print("\n== thread-count invariance (same pipeline, -threads 2/4/8)")
for t in (2, 4, 8):
    out, log = check("ILLUMINACLIP:...:2:30:10 -threads %d" % t, ["ILLUMINACLIP:%s:2:30:10" % fa] + CHAIN, R.IlluminaClip(fa, 2, 30, 10), threads=t)
    same = all(out[k] == base[0][k] for k in ("1P", "1U", "2P", "2U"))
    print("     -threads %d: four outputs byte-identical to -threads 1: %s" % (t, same))

print("\n== inputs of unequal length (file 1 has 7 extra reads at the end)")
extra = [("extra%d/1" % i, R.rand_seq(rng, 100), [35] * 100) for i in range(7)]
d = os.path.join(tmp, "unequal"); os.makedirs(d, exist_ok=True)
out, log = R.run_pe(target, recs1 + extra, recs2, ["MINLEN:1"], opts=["-summary", os.path.join(d, "s.txt")], tmpdir=d)
m = re.search(r"Input Read Pairs: (\d+) Both Surviving: (\d+)", log)
n_extra_written = sum(1 for n, s, q in out["1P"] + out["1U"] if n.startswith("extra"))
print("  summary: Input Read Pairs %s, Both Surviving %s (pairs in common: %d); extra reads written to any output: %d" % (m.group(1), m.group(2), NP, n_extra_written))

print("\n== SE summary and trimlog on the same reads (read 1 only)")
d = os.path.join(tmp, "se"); os.makedirs(d, exist_ok=True)
out, log = R.run_se(target, recs1, CHAIN, opts=["-summary", os.path.join(d, "s.txt"), "-trimlog", os.path.join(d, "t.txt")], tmpdir=d)
exp = {}
for n1, s1, q1 in recs1:
    o = single_chain(s1, q1)
    exp[n1] = o
kept = sum(1 for v in exp.values() if v)
m = re.search(r"Input Reads: (\d+) Surviving: (\d+) \(([\d.]+)%\) Dropped: (\d+) \(([\d.]+)%\)", log)
tl = [l for l in open(os.path.join(d, "t.txt")).read().split("\n") if l]
etl = ["%s %d %d %d %d" % (n1, o[1] - o[0], o[0], o[1], len(s1) - o[1]) if (o := exp[n1]) else "%s 0 0 0 0" % n1 for n1, s1, q1 in recs1]
ok = [(n, s, q) for n, s, q in out] == [(n1, s1[o[0]:o[1]], q1[o[0]:o[1]]) for n1, s1, q1 in recs1 if (o := exp[n1])]
print("  output %s; summary line Input %s Surviving %s (%s%%) Dropped %s (%s%%) vs port %d/%d/%.2f%%/%d; trimlog %s"
      % ("identical" if ok else "DIFFERS", m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), NP, kept, 100.0 * kept / NP, NP - kept,
         "match (%d lines)" % len(tl) if tl == etl else "MISMATCH"))
