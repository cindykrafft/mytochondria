#!/usr/bin/env python3
"""Held-up checks (and small notes) for the quality/length steps: SLIDINGWINDOW, LEADING,
TRAILING, MINLEN, MAXLEN, CROP, HEADCROP, TAILCROP, AVGQUAL, BASECOUNT, TOPHRED33/64, and the
automatic Phred-offset detection. Shipped build vs the references in tm_ref.py on random
reads with an Illumina-like quality profile (including N bases).

Usage: python3 heldup_quality_trimmers.py <trimmomatic.jar | build-dir>
"""
import os, random, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_ref as T

build = T.build_from_arg(sys.argv[1]); print("build:", " ".join(build))

def real_read(rng, R, n_rate=0.01):
    seq, quals = [], []
    for i in range(R):
        qq = rng.choice([40, 40, 37, 37, 32, 27, 20]) if i < R * 0.5 else rng.choice([37, 32, 27, 22, 14, 11, 6, 2])
        b = rng.choice("ACGT")
        if rng.random() < n_rate: b, qq = "N", rng.choice([2, 40])   # an N sometimes carries a high quality char
        seq.append(b); quals.append(qq)
    return "".join(seq), quals

def compare(reads, res, ref_fn, label):
    eq = neq = 0; ex = []
    for name, sq, qs in reads:
        ref = ref_fn(sq, qs)
        got = res.get(name)
        got_t = (got[0], got[1]) if got else None
        ref_t = (ref[0], ref[1]) if ref else None
        if got_t == ref_t: eq += 1
        else:
            neq += 1
            if len(ex) < 2: ex.append((name, len(sq), got_t and len(got_t[0]), ref_t and len(ref_t[0])))
    print("   %-40s shipped == reference %d/%d%s" % (label, eq, len(reads), ("  e.g. " + str(ex)) if ex else ""))
    return neq

rng = random.Random(11)
reads = [("r%d" % k, *real_read(rng, rng.choice([50, 75, 100, 150, 150, 250]))) for k in range(20000)]

print("\nA. SLIDINGWINDOW on 20,000 reads (50-250 nt, ~1% N):")
for step in ("SLIDINGWINDOW:4:15", "SLIDINGWINDOW:4:20", "SLIDINGWINDOW:5:20", "SLIDINGWINDOW:4:30", "SLIDINGWINDOW:3:20", "SLIDINGWINDOW:4:5", "SLIDINGWINDOW:10:25"):
    w, q = int(step.split(":")[1]), float(step.split(":")[2])
    res, log, d = T.run_se(build, reads, [step])
    compare(reads, res, lambda s, qs: T.sliding_window_code(s, qs, w, q), step + " vs as-coded port")
    compare(reads, res, lambda s, qs: T.sliding_window_doc(s, qs, w, q), step + " vs documented reading")
print("   note: both references score an N base as quality 0 (the code's getQualityAsInteger(true)); without that the ports differ.")
short = [("s%d" % n, "ACGT"[:n] if n <= 4 else T.rand_seq(random.Random(n), n), [40] * n) for n in (1, 2, 3, 4, 5, 8)]
res, log, d = T.run_se(build, short, ["SLIDINGWINDOW:4:15"])
print("   all-Q40 reads of length 1,2,3,4,5,8 through SLIDINGWINDOW:4:15 -> surviving:", {n: len(v[0]) for n, v in sorted(res.items())}, "|", T.summary_line(log))
res, log, d = T.run_se(build, short, ["SLIDINGWINDOW:8:15"])
print("   same reads through SLIDINGWINDOW:8:15 -> surviving:", {n: len(v[0]) for n, v in sorted(res.items())}, "(reads shorter than the window are dropped whatever their quality)")
first = [("f", "ACGTACGTACGT" + "ACGT" * 20, [2] * 4 + [40] * 88)]
res, log, d = T.run_se(build, first, ["SLIDINGWINDOW:4:15"])
print("   read whose first 4 bases are Q2 then 88 x Q40, SLIDINGWINDOW:4:15 -> surviving:", {n: len(v[0]) for n, v in res.items()}, "(first window fails: whole read dropped, as the documented 'clip at the first failing window' implies)")

print("\nB. LEADING / TRAILING on the same 20,000 reads:")
for thr in (3, 20, 30):
    res, log, d = T.run_se(build, reads, ["LEADING:%d" % thr])
    compare(reads, res, lambda s, qs: T.leading(s, qs, thr), "LEADING:%d" % thr)
    res, log, d = T.run_se(build, reads, ["TRAILING:%d" % thr])
    n1 = compare(reads, res, lambda s, qs: T.trailing_doc(s, qs, thr), "TRAILING:%d vs documented" % thr)
    compare(reads, res, lambda s, qs: T.trailing_code(s, qs, thr), "TRAILING:%d vs as-coded (loop stops at 1)" % thr)
edge = [("only_first", "ACGT" * 10, [30] + [10] * 39), ("only_last", "ACGT" * 10, [10] * 39 + [30]), ("first_two", "ACGT" * 10, [30, 30] + [10] * 38)]
res, log, d = T.run_se(build, edge, ["TRAILING:20"])
print("   TRAILING:20 on reads whose only Q30 base is the first / the last / the first two:", {n: (len(v[0]) if v else 0) for n, v in res.items()}, "-> dropped:", [n for n, _, _ in edge if n not in res])
res, log, d = T.run_se(build, edge, ["LEADING:20"])
print("   LEADING:20 on the same reads:", {n: len(v[0]) for n, v in res.items()}, "-> dropped:", [n for n, _, _ in edge if n not in res])

print("\nC. length and average-quality steps on 5,000 reads of length 1-200:")
rng = random.Random(5)
reads2 = [("r%d" % k, *real_read(rng, rng.randint(1, 200))) for k in range(5000)]
checks = [("MINLEN:36", lambda s, q: T.minlen(s, q, 36)), ("MINLEN:100", lambda s, q: T.minlen(s, q, 100)),
          ("MAXLEN:100", lambda s, q: T.maxlen(s, q, 100)), ("CROP:75", lambda s, q: T.crop(s, q, 75)),
          ("HEADCROP:10", lambda s, q: T.headcrop(s, q, 10)), ("TAILCROP:10", lambda s, q: T.tailcrop(s, q, 10)),
          ("AVGQUAL:20", lambda s, q: T.avgqual(s, q, 20)), ("AVGQUAL:30", lambda s, q: T.avgqual(s, q, 30)),
          ("BASECOUNT:N:0:2", lambda s, q: T.basecount(s, q, "N", 0, 2)), ("BASECOUNT:GC:40:120", lambda s, q: T.basecount(s, q, "GC", 40, 120))]
for step, fn in checks:
    res, log, d = T.run_se(build, reads2, [step])
    compare(reads2, res, fn, step)
res, log, d = T.run_se(build, [("ten", "ACGTACGTAC", [40] * 10), ("eleven", "ACGTACGTACG", [40] * 11)], ["HEADCROP:10"])
print("   HEADCROP:10 on reads of 10 and 11 nt -> surviving:", {n: len(v[0]) for n, v in res.items()}, "|", T.summary_line(log))
res, log, d = T.run_se(build, [("ten", "ACGTACGTAC", [40] * 10)], ["CROP:0"])
print("   CROP:0 on a 10-nt read -> surviving:", {n: len(v[0]) for n, v in res.items()}, "|", T.summary_line(log), "(a zero-length record is written)")
res, log, d = T.run_se(build, reads2, ["LEADING:3", "TRAILING:3", "SLIDINGWINDOW:4:15", "MINLEN:36"])
def pipe(s, q):
    r = T.leading(s, q, 3)
    if r is None: return None
    r = T.trailing_code(r[0], r[1], 3)
    if r is None: return None
    r = T.sliding_window_code(r[0], r[1], 4, 15)
    if r is None: return None
    return T.minlen(r[0], r[1], 36)
compare(reads2, res, pipe, "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 (chained)")

print("\nD. TOPHRED33 / TOPHRED64 conversion:")
rd = [("c%d" % k, *real_read(random.Random(k), 60, 0)) for k in range(200)]
res, log, d = T.run_se(build, rd, ["TOPHRED64"], off=33)
raw = T.read_fastq(os.path.join(d, "out.fq"), 64)
print("   -phred33 input, TOPHRED64: output qualities read back with offset 64 equal the input integers for %d/200 reads" % sum(1 for n, s, q in rd if raw.get(n) == (s, q)))
res, log, d = T.run_se(build, rd, ["TOPHRED33"], off=64)
raw = T.read_fastq(os.path.join(d, "out.fq"), 33)
print("   -phred64 input, TOPHRED33: output read back with offset 33 equals the input for %d/200 reads" % sum(1 for n, s, q in rd if raw.get(n) == (s, q)))
res, log, d = T.run_se(build, rd, ["TOPHRED33"], off=33)
raw = T.read_fastq(os.path.join(d, "out.fq"), 33)
print("   -phred33 input, TOPHRED33: unchanged for %d/200 reads" % sum(1 for n, s, q in rd if raw.get(n) == (s, q)))

print("\nE. automatic Phred-offset detection (no -phred flag; the parser histograms the first 10,000 reads):")
def detect(reads, off):
    d = tempfile.mkdtemp(prefix="tm_det_")
    T.write_fastq(os.path.join(d, "in.fq"), reads, off)
    cmd = list(build) + ["SE", "-threads", "1", os.path.join(d, "in.fq"), os.path.join(d, "out.fq"), "MINLEN:1"]
    p = subprocess.run(cmd, capture_output=True, text=True, env=T.ENV)
    log = p.stdout + p.stderr
    det = [l for l in log.splitlines() if "encoding" in l.lower()]
    return (det[0] if det else "(no detection line)"), p.returncode, len(T.read_fastq(os.path.join(d, "out.fq"), off))
typical = [("t%d" % k, *real_read(random.Random(k), 100, 0)) for k in range(500)]
print("   typical qualities (2-40) written Phred+33 ->", detect(typical, 33))
print("   typical qualities (2-40) written Phred+64 ->", detect(typical, 64))
hi = [("h%d" % k, T.rand_seq(random.Random(k), 100), [random.Random(k * 7 + i).choice([27, 30, 33, 37, 40]) for i in range(100)]) for k in range(500)]
print("   all qualities 27-40 (a strictly pre-filtered library) written Phred+33 ->", detect(hi, 33))
print("   all qualities 27-40 written Phred+64 ->", detect(hi, 64))
lo = [("l%d" % k, T.rand_seq(random.Random(k), 100), [random.Random(k * 7 + i).choice([2, 5, 8, 10, 15]) for i in range(100)]) for k in range(500)]
print("   all qualities 2-15 written Phred+64 (chars 66-79, counted by neither window) ->", detect(lo, 64))
pb = [("p%d" % k, T.rand_seq(random.Random(k), 100), [random.Random(k * 7 + i).choice([30, 40, 50, 60, 70, 93]) for i in range(100)]) for k in range(500)]
print("   qualities 30-93 as in PacBio HiFi FASTQ, written Phred+33 ->", detect(pb, 33))
