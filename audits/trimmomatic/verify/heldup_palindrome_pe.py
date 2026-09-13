#!/usr/bin/env python3
"""Held-up checks and notes for ILLUMINACLIP palindrome mode and the paired-end machinery:
insert-length sweep with read-through (both reads clipped to the insert / reverse dropped),
keepBothReads, minAdapterLength, the four PE outputs and the summary counts against a
per-read expectation, the -summary file, the -trimlog fields, -threads invariance, and what
happens with input files of unequal length.

Usage: python3 heldup_palindrome_pe.py <trimmomatic.jar | build-dir> [adapters-dir]
"""
import os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_ref as T

build = T.build_from_arg(sys.argv[1])
adir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(sys.argv[1].rstrip("/")), "adapters")
print("build:", " ".join(build))

def make_pair(rng, R, L, A1, A2, q=37):
    """Insert of length L read through into the adapter: read 1 continues into A1 (the
    reverse complement of the read-2 side adapter), read 2 into A2, then random bases."""
    frag = T.rand_seq(rng, L)
    r1 = (frag + A1 + T.rand_seq(rng, R))[:R]
    r2 = (T.revcomp(frag) + A2 + T.rand_seq(rng, R))[:R]
    return r1, [q] * R, r2, [q] * R

def outcome(res, name, R):
    if name in res["1P"]: return ("both", len(res["1P"][name][0]), len(res["2P"][name][0]))
    if name in res["1U"]: return ("fwd", len(res["1U"][name][0]), 0)
    if name in res["2U"]: return ("rev", 0, len(res["2U"][name][0]))
    return ("dropped", 0, 0)

# ---------------------------------------------------------------- A. insert sweep
# Read-through sequences per adapter file: what follows the insert in read 1 / read 2. For
# TruSeq3 the prefix pair is the complete adapter, for Nextera the 19-nt mosaic end is
# followed by the rest of the transposase adapter (Trans2_rc / Trans1_rc in the file).
print("A. palindrome + simple mode on error-free 2x100 / 2x150 pairs, one pair per insert length; expectation = the documented palindrome rule")
print("   (smallest insert scoring >= 30, forward clipped to it, reverse dropped unless keepBothReads, at least minAdapterLength adapter bases)")
print("   combined with the simple-mode sequences of the file scored by the best-sub-range port (tm_ref.simple_clip mode='code'):")
for fa in ("TruSeq3-PE.fa", "TruSeq3-PE-2.fa", "NexteraPE-PE.fa"):
    AD = os.path.join(adir, fa); recs = dict(T.load_fasta(AD))
    P1 = [v for k, v in recs.items() if k.startswith("Prefix") and k.endswith("/1")][0]
    P2 = [v for k, v in recs.items() if k.startswith("Prefix") and k.endswith("/2")][0]
    P = min(len(P1), len(P2)); P1, P2 = P1[len(P1) - P:], P2[len(P2) - P:]
    simple_fwd = [v for k, v in recs.items() if not k.startswith("Prefix") and not k.endswith("/2")]
    simple_rev = [v for k, v in recs.items() if not k.startswith("Prefix") and not k.endswith("/1")]
    A1 = recs.get("Trans2_rc", T.revcomp(P2)); A2 = recs.get("Trans1_rc", T.revcomp(P1))
    for R in (100, 150):
        for spec, minad, keep in (("2:30:10", 8, False), ("2:30:10:1:true", 1, True), ("2:30:10:20:false", 20, False)):
            rng = random.Random(R)
            reads1, reads2, meta = [], [], []
            for L in range(0, R + 20):
                r1, q1, r2, q2 = make_pair(rng, R, L, A1, A2)
                name = "L%d" % L
                reads1.append((name, r1, q1)); reads2.append((name, r2, q2)); meta.append((name, L, r1, q1, r2, q2))
            res, log, d = T.run_pe(build, reads1, reads2, ["ILLUMINACLIP:%s:%s" % (AD, spec)])
            ok = bad = 0; ex = []
            for name, L, r1, q1, r2, q2 in meta:
                pal = T.palindrome_clip(r1, q1, r2, q2, P1, P2, 2, 30, min_adapter=minad)
                k1 = R if pal is None else pal
                k2 = R if pal is None else (pal if keep else 0)
                for a in simple_fwd:
                    if k1 > 0:
                        c = T.simple_clip(r1, q1, a, 2, 10, mode="code", min_overlap=T.code_min_overlap(10))
                        if c is not None: k1 = min(k1, c)
                for a in simple_rev:
                    if k2 > 0:
                        c = T.simple_clip(r2, q2, a, 2, 10, mode="code", min_overlap=T.code_min_overlap(10))
                        if c is not None: k2 = min(k2, c)
                exp = ("both", k1, k2) if (k1 > 0 and k2 > 0) else (("fwd", k1, 0) if k1 > 0 else (("rev", 0, k2) if k2 > 0 else ("dropped", 0, 0)))
                got = outcome(res, name, R)
                if got == exp: ok += 1
                else:
                    bad += 1
                    if len(ex) < 3: ex.append((L, got, exp))
            print("   %-18s 2x%-4d %-18s inserts 0..%d: shipped == reference %d/%d%s" % (fa, R, spec, R + 19, ok, len(meta), ("  e.g. (insert, shipped, expected): " + str(ex)) if ex else ""))

# ---------------------------------------------------------------- B. PE bookkeeping
print("\nB. 3,000 pairs (2x100, Illumina-like qualities) through LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 (no adapters):")
def real_read(rng, R):
    quals = [rng.choice([40, 37, 32, 27, 20]) if i < R * 0.5 else rng.choice([37, 32, 27, 22, 14, 11, 6, 2]) for i in range(R)]
    seq = "".join(rng.choice("ACGT") if rng.random() > 0.01 else "N" for _ in range(R))
    return seq, quals
def pipe(s, q):
    r = T.leading(s, q, 3)
    if r is None: return None
    r = T.trailing_code(r[0], r[1], 3)
    if r is None: return None
    r = T.sliding_window_code(r[0], r[1], 4, 15)
    if r is None: return None
    return T.minlen(r[0], r[1], 36)
rng = random.Random(21)
reads1 = [("p%d" % k, *real_read(rng, 100)) for k in range(3000)]
reads2 = [("p%d" % k, *real_read(rng, 100)) for k in range(3000)]
d = None
import tempfile
d = tempfile.mkdtemp(prefix="tm_pe_book_")
STEPS = ["LEADING:3", "TRAILING:3", "SLIDINGWINDOW:4:15", "MINLEN:36"]
res, log, d = T.run_pe(build, reads1, reads2, STEPS, extra=["-summary", os.path.join(d, "summary.txt"), "-trimlog", os.path.join(d, "trimlog.txt")], workdir=d)
exp_counts = {"both": 0, "fwd": 0, "rev": 0, "dropped": 0}; ok = 0; bad = []
exp_by = {}
for (n, s1, q1), (_, s2, q2) in zip(reads1, reads2):
    e1, e2 = pipe(s1, q1), pipe(s2, q2)
    cls = "both" if (e1 and e2) else ("fwd" if e1 else ("rev" if e2 else "dropped"))
    exp_counts[cls] += 1
    exp_by[n] = (cls, e1, e2)
    got = outcome(res, n, 100)
    exp = (cls, len(e1[0]) if e1 else 0, len(e2[0]) if e2 else 0)
    if got == exp:
        # sequences too
        if cls == "both" and (res["1P"][n] != e1 or res["2P"][n] != e2): bad.append(n)
        elif cls == "fwd" and res["1U"][n] != e1: bad.append(n)
        elif cls == "rev" and res["2U"][n] != e2: bad.append(n)
        else: ok += 1
    else: bad.append((n, got, exp))
print("   per-pair outputs (file, sequence, quality) equal the expectation for %d/3000; mismatches: %s" % (ok, bad[:3]))
print("   expected counts:", exp_counts)
print("   log line:      ", T.summary_line(log, True))
with open(os.path.join(d, "summary.txt")) as fh: summ = fh.read().strip().splitlines()
print("   -summary file: ", " | ".join(summ))
n = 3000
pct = lambda x: "%.2f" % (100.0 * x / n)
exp_summary = ["Input Read Pairs: %d" % n, "Both Surviving Reads: %d" % exp_counts["both"], "Both Surviving Read Percent: " + pct(exp_counts["both"]),
               "Forward Only Surviving Reads: %d" % exp_counts["fwd"], "Forward Only Surviving Read Percent: " + pct(exp_counts["fwd"]),
               "Reverse Only Surviving Reads: %d" % exp_counts["rev"], "Reverse Only Surviving Read Percent: " + pct(exp_counts["rev"]),
               "Dropped Reads: %d" % exp_counts["dropped"], "Dropped Read Percent: " + pct(exp_counts["dropped"])]
print("   -summary file equals the expectation:", summ == exp_summary)
# trimlog: name length startPos endPos trimTail, one line per input read (forward then reverse)
tl = {}
with open(os.path.join(d, "trimlog.txt")) as fh:
    lines = [l.split() for l in fh if l.strip()]
tl_ok = 0; tl_bad = []
for i, (nm, s1, q1) in enumerate(reads1):
    for which, (s, q) in enumerate(((s1, q1), reads2[i][1:])):
        e = exp_by[nm][1 + which]
        if e:
            start = T.leading(s, q, 3)  # bases removed at the start = len(s) - len(after LEADING)
            start = len(s) - len(start[0])
            exp_line = [nm, str(len(e[0])), str(start), str(start + len(e[0])), str(len(s) - start - len(e[0]))]
        else:
            exp_line = [nm, "0", "0", "0", "0"]
        got = lines[2 * i + which]
        if got == exp_line: tl_ok += 1
        elif len(tl_bad) < 3: tl_bad.append((got, exp_line))
print("   -trimlog: %d lines for %d input reads; lines equal to (name, surviving length, first surviving base, end, bases trimmed from the end): %d/%d; mismatches: %s" % (len(lines), 2 * n, tl_ok, 2 * n, tl_bad))

# ---------------------------------------------------------------- C. threads
print("\nC. -threads invariance (same 3,000 pairs, ILLUMINACLIP:TruSeq3-PE-2.fa:2:30:10 + the steps above, uncompressed output):")
AD = os.path.join(adir, "TruSeq3-PE-2.fa")
outs = {}
for th in (1, 2, 4, 8):
    dd = tempfile.mkdtemp(prefix="tm_thr_")
    in1, in2 = os.path.join(dd, "in1.fq"), os.path.join(dd, "in2.fq")
    T.write_fastq(in1, reads1); T.write_fastq(in2, reads2)
    files = [os.path.join(dd, "o_%s.fq" % k) for k in ("1P", "1U", "2P", "2U")]
    cmd = list(build) + ["PE", "-threads", str(th), "-phred33", "-summary", os.path.join(dd, "s.txt"), "-trimlog", os.path.join(dd, "t.txt"), in1, in2] + files + ["ILLUMINACLIP:%s:2:30:10" % AD] + STEPS
    p = subprocess.run(cmd, capture_output=True, text=True, env=T.ENV)
    outs[th] = tuple(open(f).read() for f in files) + (open(os.path.join(dd, "s.txt")).read(), open(os.path.join(dd, "t.txt")).read())
    print("   -threads %d: %s" % (th, T.summary_line(p.stdout + p.stderr, True)))
print("   four outputs + summary + trimlog byte-identical across -threads 1/2/4/8:", all(outs[t] == outs[1] for t in outs))
print("   SE, -threads 1 vs 4 vs 8 with ILLUMINACLIP:TruSeq3-SE.fa:2:30:10 + steps:")
se_out = {}
for th in (1, 4, 8):
    dd = tempfile.mkdtemp(prefix="tm_thrse_")
    T.write_fastq(os.path.join(dd, "in.fq"), reads1 + [(n + "b", s, q) for n, s, q in reads2])
    cmd = list(build) + ["SE", "-threads", str(th), "-phred33", os.path.join(dd, "in.fq"), os.path.join(dd, "o.fq"), "ILLUMINACLIP:%s:2:30:10" % os.path.join(adir, "TruSeq3-SE.fa")] + STEPS
    p = subprocess.run(cmd, capture_output=True, text=True, env=T.ENV)
    se_out[th] = open(os.path.join(dd, "o.fq")).read()
print("   SE output byte-identical across -threads 1/4/8:", all(v == se_out[1] for v in se_out.values()))

# ---------------------------------------------------------------- D. unequal input files
print("\nD. input files of unequal length (forward 100 reads, reverse 90; MINLEN:1):")
r1 = [("u%d" % k, "ACGT" * 25, [37] * 100) for k in range(100)]
r2 = [("u%d" % k, "TTGA" * 25, [37] * 100) for k in range(90)]
res, log, d = T.run_pe(build, r1, r2, ["MINLEN:1"])
print("   ", T.summary_line(log, True), "| reads in 1P/1U/2P/2U:", {k: len(v) for k, v in res.items()})
res, log, d = T.run_pe(build, r1, r2, ["MINLEN:1"], extra=["-validatePairs"])
warn = [l for l in log.splitlines() if "WARNING" in l or "validation" in l.lower()]
print("    with -validatePairs:", warn[:2] if warn else "(no warning)", "|", T.summary_line(log, True))
