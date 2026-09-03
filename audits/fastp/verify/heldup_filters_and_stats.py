#!/usr/bin/env python3
"""What held up: the read-level filters and the reported statistics.

Every check runs the shipped binary on synthetic reads with known truth and
compares against an independent Python reference (fastp_ref.pass_filter and
plain counting), never against fastp's own arithmetic.

H1  --qualified_quality_phred / --unqualified_percent_limit / --n_base_limit /
    --average_qual / --length_required / --length_limit / --low_complexity_filter
H2  the JSON summary: total_reads, total_bases, q20/q30 bases and rates,
    gc_content, read1_mean_length
H3  the JSON kmer_count table (1,024 5-mers)
H4  --trim_front1 / --trim_tail1 / --max_len1 on their own
H5  --phred64
H6  boundary behaviour of every threshold

Usage: python3 heldup_filters_and_stats.py [path-to-fastp]
"""
import json
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastp_ref import pass_filter, run_fastp  # noqa: E402

EXE = sys.argv[1] if len(sys.argv) > 1 else "./fastp"
random.seed(4242)
print("fastp:", os.popen(f"{EXE} --version 2>&1").read().strip())

BASE = ["-A", "-G", "-w", "1", "--dont_eval_duplication"]

# 20,000 reads with a wide spread of lengths, qualities, N content and complexity
recs = []
for i in range(20000):
    n = random.randint(5, 150)
    mode = i % 4
    if mode == 0:
        seq = "".join(random.choice("ACGT") for _ in range(n))
    elif mode == 1:
        seq = "".join(random.choice("ACGTN") for _ in range(n))
    elif mode == 2:  # low complexity
        seq = "".join(random.choice("AC") for _ in range(n // 3 + 1)) * 3
        seq = seq[:n]
    else:
        seq = random.choice("ACGT") * n
    lo, hi = random.choice([(2, 40), (2, 15), (25, 40), (10, 30)])
    qual = "".join(chr(random.randint(lo, hi) + 33) for _ in range(len(seq)))
    recs.append((f"r{i}", seq, qual))

# ------------------------------------------------------------------------ H1
print("\n== H1: filters, 20,000 reads, output compared read by read")
cases = [
    ("defaults (-q 15 -u 40 -n 5 -l 15)", [], dict()),
    ("-q 30 -u 20", ["-q", "30", "-u", "20"], dict(qualified_q=30, unqualified_pct=20)),
    ("-q 20 -u 0", ["-q", "20", "-u", "0"], dict(qualified_q=20, unqualified_pct=0)),
    ("-n 0", ["-n", "0"], dict(n_limit=0)),
    ("-n 3", ["-n", "3"], dict(n_limit=3)),
    ("-e 25", ["-e", "25"], dict(avg_qual=25)),
    ("-e 30 -q 25 -u 30", ["-e", "30", "-q", "25", "-u", "30"],
     dict(avg_qual=30, qualified_q=25, unqualified_pct=30)),
    ("-l 50", ["-l", "50"], dict(min_len=50)),
    ("-l 50 --length_limit 100", ["-l", "50", "--length_limit", "100"],
     dict(min_len=50, max_len=100)),
    ("-y (-Y 30)", ["-y"], dict(complexity=0.30)),
    ("-y -Y 50", ["-y", "-Y", "50"], dict(complexity=0.50)),
    ("-Q (quality filter off)", ["-Q"], dict(qual_filter=False)),
    ("-L (length filter off)", ["-L"], dict(len_filter=False)),
]
print(f"  {'options':<36} {'kept (fastp)':>12} {'kept (reference)':>17} {'identical sets':>15}")
for label, args, kw in cases:
    reads, _, jpath = run_fastp(EXE, args + BASE, records=recs)
    ref = {n for n, s, q in recs if pass_filter(s, q, **kw) == "pass"}
    print(f"  {label:<36} {len(reads):>12} {len(ref):>17} {str(set(reads) == ref):>15}")

# reason codes
print("\n  filtering_result counts vs the reference reasons (-q 25 -u 30 -n 2 -e 20 -l 40 --length_limit 120 -y)")
args = ["-q", "25", "-u", "30", "-n", "2", "-e", "20", "-l", "40", "--length_limit", "120", "-y"]
kw = dict(qualified_q=25, unqualified_pct=30, n_limit=2, avg_qual=20, min_len=40,
          max_len=120, complexity=0.30)
reads, _, jpath = run_fastp(EXE, args + BASE, records=recs)
js = json.load(open(jpath))
ref = Counter(pass_filter(s, q, **kw) for n, s, q in recs)
fr = js["filtering_result"]
for key, jkey in [("pass", "passed_filter_reads"), ("low_quality", "low_quality_reads"),
                  ("too_many_N", "too_many_N_reads"), ("too_short", "too_short_reads"),
                  ("too_long", "too_long_reads"), ("low_complexity", "low_complexity_reads")]:
    print(f"    {jkey:<26} fastp {fr[jkey]:>7}   reference {ref[key]:>7}   "
          f"{'ok' if fr[jkey] == ref[key] else 'DIFFERS'}")

# ------------------------------------------------------------------------ H2
print("\n== H2: JSON summary before filtering vs direct counting")
js_pre = js["summary"]["before_filtering"]
tot_reads = len(recs)
tot_bases = sum(len(s) for _, s, _ in recs)
q20 = sum(1 for _, _, q in recs for c in q if ord(c) >= 33 + 20)
q30 = sum(1 for _, _, q in recs for c in q if ord(c) >= 33 + 30)
gc = sum(s.count("G") + s.count("C") for _, s, _ in recs)
mean_len = tot_bases // tot_reads
for label, got, ref in [
    ("total_reads", js_pre["total_reads"], tot_reads),
    ("total_bases", js_pre["total_bases"], tot_bases),
    ("q20_bases", js_pre["q20_bases"], q20),
    ("q30_bases", js_pre["q30_bases"], q30),
    ("read1_mean_length", js_pre["read1_mean_length"], mean_len),
]:
    print(f"  {label:<20} fastp {got:>12}   reference {ref:>12}   {'ok' if got == ref else 'DIFFERS'}")
for label, got, ref in [
    ("q20_rate", js_pre["q20_rate"], q20 / tot_bases),
    ("q30_rate", js_pre["q30_rate"], q30 / tot_bases),
    ("gc_content", js_pre["gc_content"], gc / tot_bases),
]:
    print(f"  {label:<20} fastp {got:>12.6f}   reference {ref:>12.6f}   "
          f"{'ok' if abs(got - ref) < 1e-6 else 'DIFFERS'}")

# ------------------------------------------------------------------------ H3
print("\n== H3: JSON kmer_count (1,024 5-mers) vs direct counting")
ref_k = Counter()
for _, s, _ in recs:
    for i in range(4, len(s)):
        k = s[i - 4:i + 1]
        if all(c in "ACGT" for c in k):
            ref_k[k] += 1
got_k = js["read1_before_filtering"]["kmer_count"]
bad = [k for k in got_k if got_k[k] != ref_k.get(k, 0)]
print(f"  entries: {len(got_k)}   total counted: fastp {sum(got_k.values())} "
      f"reference {sum(ref_k.values())}   mismatching entries: {len(bad)}")

# ------------------------------------------------------------------------ H4
print("\n== H4: global trimming on its own (no sliding window)")
for label, args, fn in [
    ("-f 7", ["-f", "7"], lambda s: s[7:]),
    ("-t 7", ["-t", "7"], lambda s: s[:-7] if len(s) > 7 else ""),
    ("-f 5 -t 5", ["-f", "5", "-t", "5"], lambda s: s[5:-5] if len(s) > 10 else ""),
    ("-b 40 (--max_len1)", ["-b", "40"], lambda s: s[:40]),
    ("-f 10 -b 40", ["-f", "10", "-b", "40"], lambda s: s[10:][:40]),
]:
    reads, _, _ = run_fastp(EXE, args + ["-Q", "-L"] + BASE, records=recs)
    ok = miss = 0
    for n, s, q in recs:
        want = fn(s)
        got = reads.get(n)
        if len(want) == 0:
            miss += got is not None
        elif got is None:
            miss += 1
        else:
            ok += got[0] == want
    print(f"  {label:<20} reads matching the reference: {ok:>6}/{sum(1 for _, s, _ in recs if fn(s))}"
          f"   unexpected: {miss}")

# ------------------------------------------------------------------------ H5
print("\n== H5: --phred64")
p64 = [(n, s, "".join(chr(ord(c) - 33 + 64) for c in q)) for n, s, q in recs[:5000]]
reads64, _, j64 = run_fastp(EXE, ["-6", "-q", "25", "-u", "30", "-e", "20"] + BASE, records=p64)
reads33, _, j33 = run_fastp(EXE, ["-q", "25", "-u", "30", "-e", "20"] + BASE, records=recs[:5000])
print(f"  phred+64 input with -6 gives the same surviving reads as phred+33: "
      f"{set(reads64) == set(reads33)}")
print(f"  qualities converted to phred+33 in the output: "
      f"{all(reads64[n][1] == reads33[n][1] for n in reads33)}")
j64d, j33d = json.load(open(j64)), json.load(open(j33))
print(f"  q30_bases: phred64 {j64d['summary']['before_filtering']['q30_bases']}, "
      f"phred33 {j33d['summary']['before_filtering']['q30_bases']}")

# ------------------------------------------------------------------------ H6
print("\n== H6: threshold boundaries (one read each, 100 nt)")
seq = "ACGT" * 25
tests = [
    ("-l 100 on a 100 nt read (kept: < is strict)", ["-l", "100"], "I" * 100, seq, True),
    ("-l 101 on a 100 nt read", ["-l", "101"], "I" * 100, seq, False),
    ("--length_limit 100 on a 100 nt read", ["--length_limit", "100"], "I" * 100, seq, True),
    ("--length_limit 99 on a 100 nt read", ["--length_limit", "99"], "I" * 100, seq, False),
    ("-e 20 with mean quality exactly 20", ["-e", "20"], chr(20 + 33) * 100, seq, True),
    ("-e 21 with mean quality exactly 20", ["-e", "21"], chr(20 + 33) * 100, seq, False),
    ("-n 5 with exactly 5 N", ["-n", "5"], "I" * 100, "N" * 5 + seq[5:], True),
    ("-n 4 with exactly 5 N", ["-n", "4"], "I" * 100, "N" * 5 + seq[5:], False),
    ("-q 20 -u 40 with exactly 40 % below Q20", ["-q", "20", "-u", "40"],
     chr(19 + 33) * 40 + chr(20 + 33) * 60, seq, True),
    ("-q 20 -u 39 with exactly 40 % below Q20", ["-q", "20", "-u", "39"],
     chr(19 + 33) * 40 + chr(20 + 33) * 60, seq, False),
    # 101 nt with exactly 50 of the 100 adjacent pairs different -> complexity 0.5
    ("-y -Y 50 on a sequence with complexity exactly 50 %", ["-y", "-Y", "50"], "I" * 101,
     "A" * 51 + "CA" * 25, True),
    ("-y -Y 51 on the same sequence", ["-y", "-Y", "51"], "I" * 101,
     "A" * 51 + "CA" * 25, False),
]
for label, args, qual, s, expect_kept in tests:
    reads, _, _ = run_fastp(EXE, args + BASE, records=[("t", s, qual)])
    kept = "t" in reads
    print(f"  {label:<46} kept={str(kept):<5} expected={str(expect_kept):<5} "
          f"{'ok' if kept == expect_kept else 'DIFFERS'}")
