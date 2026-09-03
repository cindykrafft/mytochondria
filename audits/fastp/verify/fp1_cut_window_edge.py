#!/usr/bin/env python3
"""FP1: --cut_front / --cut_tail discard (window_size - 1) extra bases when
combined with --trim_front1 / --trim_tail1, even when no window fails.

`Filter::trimAndCut` (src/filter.cpp) advances the 5' cut position to the END of
the first window whose mean quality passes -- which is how the "drop the bases of
the failing window" rule is implemented, since consecutive windows overlap. The
guard that suppresses that advance when the very first window already passes is
written against the read start (`if(s > 0)`, filter.cpp:121) instead of the
globally trimmed start (`front`), and its 3' mirror against `l-1`
(`if(t < l-1)`, filter.cpp:189) instead of `l-tail-1`. So whenever
--trim_front1/--trim_tail1 > 0 the extra advance also fires on reads whose first
window is fine, and window_size-1 good bases are dropped for every read.

Part A  constant Q40 reads: no window can fail, so any loss beyond -f/-t is spurious
Part B  20,000 random reads vs the two independent ports in fastp_ref.py
Part C  what it costs: bases lost and reads pushed under --length_required

Usage: python3 fp1_cut_window_edge.py [path-to-fastp]      (default ./fastp)
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastp_ref import CutOpts, run_fastp, trim_and_cut  # noqa: E402

EXE = sys.argv[1] if len(sys.argv) > 1 else "./fastp"
random.seed(2026)
print("fastp:", os.popen(f"{EXE} --version 2>&1").read().strip())

NOFILT = ["-Q", "-L", "-A", "-G", "-w", "1"]


def rnd_seq(n):
    return "".join(random.choice("ACGT") for _ in range(n))


# ------------------------------------------------------------------- Part A
print("\n== Part A: 100 reads of 60 nt, every base Q40 ('I'): no sliding window can fail")
recs = [(f"r{i}", rnd_seq(60), "I" * 60) for i in range(100)]
rows = [
    ("-f 5", ["-f", "5"], 55),
    ("--cut_front", ["--cut_front"], 60),
    ("--cut_front -f 5", ["--cut_front", "-f", "5"], 55),
    ("--cut_front -f 5 -W 10", ["--cut_front", "-f", "5", "-W", "10"], 55),
    ("--cut_front -f 1", ["--cut_front", "-f", "1"], 59),
    ("-t 5", ["-t", "5"], 55),
    ("--cut_tail", ["--cut_tail"], 60),
    ("--cut_tail -t 5", ["--cut_tail", "-t", "5"], 55),
    ("--cut_tail -t 5 -W 10", ["--cut_tail", "-t", "5", "-W", "10"], 55),
    ("--cut_right -f 5", ["--cut_right", "-f", "5"], 55),
    ("--cut_right -t 5", ["--cut_right", "-t", "5"], 55),
    ("--cut_front --cut_tail -f 5 -t 5", ["--cut_front", "--cut_tail", "-f", "5", "-t", "5"], 50),
]
print(f"  {'options':<34} {'expected len':>12} {'observed lens':>18}   verdict")
for label, args, expected in rows:
    reads, _, _ = run_fastp(EXE, args + NOFILT, records=recs)
    lens = sorted({len(s) for s, _ in reads.values()})
    ok = lens == [expected]
    print(f"  {label:<34} {expected:>12} {str(lens):>18}   {'ok' if ok else 'LOSES ' + str(expected - lens[0]) + ' EXTRA BASES'}")

# ------------------------------------------------------------------- Part B
print("\n== Part B: 20,000 random reads (len 40-150, phred 2-40) vs independent ports")
recs = []
for i in range(20000):
    n = random.randint(40, 150)
    recs.append((f"r{i}", rnd_seq(n),
                 "".join(chr(random.randint(2, 40) + 33) for _ in range(n))))

cases = [
    ("--cut_front", ["--cut_front"], 0, 0, CutOpts(front=True)),
    ("--cut_front -f 5", ["--cut_front", "-f", "5"], 5, 0, CutOpts(front=True)),
    ("--cut_front -f 5 -W 8 -M 25", ["--cut_front", "-f", "5", "-W", "8", "-M", "25"], 5, 0,
     CutOpts(front=True, w=8, q=25)),
    ("--cut_tail", ["--cut_tail"], 0, 0, CutOpts(tail=True)),
    ("--cut_tail -t 5", ["--cut_tail", "-t", "5"], 0, 5, CutOpts(tail=True)),
    ("--cut_tail -t 3 -W 6 -M 15", ["--cut_tail", "-t", "3", "-W", "6", "-M", "15"], 0, 3,
     CutOpts(tail=True, w=6, q=15)),
    ("--cut_front --cut_tail -f 4 -t 4", ["--cut_front", "--cut_tail", "-f", "4", "-t", "4"], 4, 4,
     CutOpts(front=True, tail=True)),
    ("--cut_right -f 5 -t 5", ["--cut_right", "-f", "5", "-t", "5"], 5, 5, CutOpts(right=True)),
]
print(f"  {'options':<32} {'== shipped port':>16} {'== fixed port':>14} {'reads differing':>16} {'bases lost':>11}")
for label, args, f, t, opts in cases:
    reads, _, _ = run_fastp(EXE, args + NOFILT, records=recs)
    same_ship = same_fix = 0
    differ = 0
    lost = 0
    for name, seq, qual in recs:
        got = reads.get(name)
        ship = trim_and_cut(seq, qual, f, t, opts, "shipped")
        fix = trim_and_cut(seq, qual, f, t, opts, "fixed")
        same_ship += (got == ship) if got or ship else 1
        same_fix += (got == fix) if got or fix else 1
        if ship != fix:
            differ += 1
            lost += (len(fix[0]) if fix else 0) - (len(ship[0]) if ship else 0)
    print(f"  {label:<32} {same_ship:>10}/20000 {same_fix:>9}/20000 {differ:>16} {lost:>11}")

# ------------------------------------------------------------------- Part C
print("\n== Part C: cost on a realistic run (20,000 reads, default filters, -l 15)")
for label, args, f, t, opts in [
    ("--cut_front -f 5", ["--cut_front", "-f", "5"], 5, 0, CutOpts(front=True)),
    ("--cut_tail -t 5", ["--cut_tail", "-t", "5"], 0, 5, CutOpts(tail=True)),
    ("--cut_front -f 5 -W 10", ["--cut_front", "-f", "5", "-W", "10"], 5, 0, CutOpts(front=True, w=10)),
]:
    reads, _, _ = run_fastp(EXE, args + ["-A", "-G", "-w", "1"], records=recs)
    ship_bases = sum(len(s) for s, _ in reads.values())
    fix_bases = kept_fix = 0
    for name, seq, qual in recs:
        fix = trim_and_cut(seq, qual, f, t, opts, "fixed")
        if fix and len(fix[0]) >= 15:
            kept_fix += 1
            fix_bases += len(fix[0])
    print(f"  {label:<24} shipped: {len(reads):>6} reads {ship_bases:>8} bases | "
          f"with the fix: {kept_fix:>6} reads {fix_bases:>8} bases | "
          f"lost {kept_fix - len(reads):>5} reads {fix_bases - ship_bases:>7} bases "
          f"({100.0 * (fix_bases - ship_bases) / fix_bases:.2f} %)")
