#!/usr/bin/env python3
"""The NOTE-level behaviours, each executed on the shipped binary.

N1  --overlap_diff_limit / --overlap_diff_percent_limit are enforced over the
    first 50 bases of the overlap only (overlapanalysis.cpp:28-41)
N2  --overlap_len_require N accepts an overlap only when it is longer than N
N3  the insert-size histogram is filled by worker thread 0 only, so it scales
    with 1/--thread (peprocessor.cpp:449, :497)
N4  --poly_g_min_len N already trims a tail of N-1 G
N5  -m/--merge silently switches on base correction (options.cpp:120-121)
N6  the adapter search needs 5 matching bases at the read end, not 4

Usage: python3 notes_overlap_polyg_threads.py [path-to-fastp]
"""
import json
import os
import random
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastp_ref import read_fastq, run_fastp, write_fastq  # noqa: E402

EXE = sys.argv[1] if len(sys.argv) > 1 else "./fastp"
random.seed(31337)
print("fastp:", os.popen(f"{EXE} --version 2>&1").read().strip())
COMP = str.maketrans("ACGTN", "TGCAN")


def rc(s):
    return s.translate(COMP)[::-1]


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def mutate(s, i):
    return s[:i] + ("A" if s[i] != "A" else "C") + s[i + 1:]


def run_pe(r1, r2, args, merged=False):
    tmp = tempfile.mkdtemp()
    p1, p2 = os.path.join(tmp, "1.fq"), os.path.join(tmp, "2.fq")
    write_fastq(p1, r1)
    write_fastq(p2, r2)
    o1, o2 = os.path.join(tmp, "o1.fq"), os.path.join(tmp, "o2.fq")
    jp = os.path.join(tmp, "o.json")
    cmd = [EXE, "-i", p1, "-I", p2, "-j", jp, "-h", os.path.join(tmp, "h"),
           "-A", "-G", "-Q", "-L", "-w", "1", "--dont_eval_duplication"]
    mp = os.path.join(tmp, "m.fq")
    if merged:
        cmd += ["-m", "--merged_out", mp, "-o", o1, "-O", o2]
    else:
        cmd += ["-o", o1, "-O", o2]
    cmd += list(args)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    js = json.load(open(jp))
    nmerged = len(read_fastq(mp)) if merged and os.path.exists(mp) else 0
    return js, nmerged, proc.stderr


# ------------------------------------------------------------------------ N1
print("\n== N1: where the mismatches sit inside an 80 nt overlap "
      "(200 pairs each, default --overlap_diff_limit 5, --overlap_diff_percent_limit 20)")
print(f"  {'mismatches':>10} {'in overlap positions':>22} {'pairs merged':>13} {'corrected_bases':>16}")
for k in (0, 1, 3, 5, 6, 10, 20, 30):
    for where in ("0-49", "50-79"):
        r1, r2 = [], []
        for i in range(200):
            insert = rnd(120)
            a = insert[:100]
            b = insert[20:120]
            positions = random.sample(range(0, 50) if where == "0-49" else range(50, 80),
                                      min(k, 30))
            for p in positions:
                b = mutate(b, p)
            r1.append((f"p{i}", a, "I" * 100))
            r2.append((f"p{i}", rc(b), "I" * 100))
        js, nm, _ = run_pe(r1, r2, ["-c"], merged=True)
        cb = js["filtering_result"].get("corrected_bases", 0)
        print(f"  {k:>10} {where:>22} {nm:>13} {cb:>16}")

# ------------------------------------------------------------------------ N2
print("\n== N2: --overlap_len_require 30, exact overlap lengths (200 pairs each)")
for ov in (28, 29, 30, 31, 32, 35):
    T = 200 - ov
    r1, r2 = [], []
    for i in range(200):
        insert = rnd(T)
        r1.append((f"p{i}", insert[:100], "I" * 100))
        r2.append((f"p{i}", rc(insert[T - 100:]), "I" * 100))
    js, nm, _ = run_pe(r1, r2, ["--overlap_len_require", "30"], merged=True)
    print(f"  overlap {ov:>3} nt: pairs merged {nm:>4}/200   "
          f"{'accepted' if nm > 100 else 'rejected'}")

# ------------------------------------------------------------------------ N3
print("\n== N3: insert-size histogram vs --thread (4,000 pairs, insert size 120)")
r1, r2 = [], []
for i in range(4000):
    insert = rnd(120)
    r1.append((f"p{i}", insert[:100], "I" * 100))
    r2.append((f"p{i}", rc(insert[20:120]), "I" * 100))
for w in (1, 2, 3, 4, 8):
    tmp = tempfile.mkdtemp()
    p1, p2 = os.path.join(tmp, "1.fq"), os.path.join(tmp, "2.fq")
    write_fastq(p1, r1)
    write_fastq(p2, r2)
    jp = os.path.join(tmp, "o.json")
    subprocess.run([EXE, "-i", p1, "-I", p2, "-o", os.path.join(tmp, "o1.fq"),
                    "-O", os.path.join(tmp, "o2.fq"), "-j", jp, "-h", os.path.join(tmp, "h"),
                    "-A", "-G", "-Q", "-L", "-w", str(w), "--dont_eval_duplication"],
                   capture_output=True)
    js = json.load(open(jp))
    hist = js["insert_size"]["histogram"]
    print(f"  -w {w}: peak {js['insert_size']['peak']:>4}  counted pairs "
          f"{sum(hist) + js['insert_size']['unknown']:>6} of 4000  "
          f"(bin 120 = {hist[120]})")

# ------------------------------------------------------------------------ N4
print("\n== N4: --poly_g_min_len 10, reads ending in exactly k G (preceded by a non-G)")
for k in range(6, 13):
    recs = [(f"r{i}", rnd(50) + "T" + "G" * k, "I" * (51 + k)) for i in range(200)]
    reads, _, _ = run_fastp(EXE, ["-g", "--poly_g_min_len", "10", "-A", "-Q", "-L", "-w", "1",
                                  "--dont_eval_duplication"], records=recs)
    trimmed = sum(1 for n, s, q in recs if reads.get(n, (s,))[0] != s)
    print(f"  tail of {k:>2} G: reads trimmed {trimmed:>4}/200   "
          f"{'trimmed' if trimmed > 100 else 'kept'}")

# ------------------------------------------------------------------------ N5
print("\n== N5: -m/--merge and base correction")
r1, r2 = [], []
for i in range(200):
    insert = rnd(120)
    b = mutate(insert[20:120], 60)          # one mismatch, correctable by quality
    r1.append((f"p{i}", insert[:100], "I" * 100))
    q2 = "".join("#" if j == 39 else "I" for j in range(100))   # Q2 at the mismatch
    r2.append((f"p{i}", rc(b), q2))
for label, args, merged in [("plain PE (no -c)", [], False),
                            ("PE with -c", ["-c"], False),
                            ("PE with -m", [], True),
                            ("PE with -m -c", ["-c"], True)]:
    js, nm, _ = run_pe(r1, r2, args, merged=merged)
    cb = js["filtering_result"].get("corrected_bases", "absent")
    print(f"  {label:<18} corrected_bases in the JSON: {str(cb):>7}   merged reads {nm}")

# ------------------------------------------------------------------------ N6
print("\n== N6: how many adapter bases at the 3' end are enough (-a, 33 nt adapter)")
AD = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"
for k in range(2, 9):
    recs = [(f"r{i}", rnd(60) + AD[:k], "I" * (60 + k)) for i in range(200)]
    reads, _, _ = run_fastp(EXE, ["-a", AD, "-A" if False else "-Q", "-L", "-G", "-w", "1",
                                  "--dont_eval_duplication"], records=recs)
    trimmed = sum(1 for n, s, q in recs if len(reads.get(n, (s,))[0]) == 60)
    print(f"  {k} adapter bases at the read end: trimmed {trimmed:>4}/200")
