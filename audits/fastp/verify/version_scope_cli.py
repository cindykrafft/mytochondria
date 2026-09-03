#!/usr/bin/env python3
"""Version scope by execution: the three confirmed findings through the command
line only, so the same script runs on every release that builds here.

FP1  --cut_front -f 5 on reads whose every base is Q40: no window can fail, so
     the output should be 55 nt of the 60; anything shorter is FP1.
FP2  single-end auto-detection of a built-in adapter longer than 60 nt
     (TruSeq Small RNA RPI1, 63 nt) on 20,000 reads that all carry it.
FP3  200 reads carrying the adapter with one inserted base at read position 40,
     with an explicit --adapter_sequence.

Usage: python3 version_scope_cli.py <path-to-fastp>
"""
import os
import random
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastp_ref import read_fastq, write_fastq  # noqa: E402

EXE = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else "./fastp"
random.seed(2026)
ver = subprocess.run([EXE, "--version"], capture_output=True, text=True)
print((ver.stdout + ver.stderr).strip().splitlines()[-1], "(", EXE, ")")

AD33 = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"
RPI1 = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"
TMP = tempfile.mkdtemp()


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def run(records, args, want_out=True):
    p1 = os.path.join(TMP, "in.fq")
    write_fastq(p1, records)
    o1 = os.path.join(TMP, "out.fq")
    cmd = [EXE, "-i", p1, "-j", os.path.join(TMP, "o.json"), "-h", os.path.join(TMP, "o.html")]
    if want_out:
        cmd += ["-o", o1]
    cmd += list(args)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    reads = read_fastq(o1) if want_out and os.path.exists(o1) else {}
    return reads, proc.stderr


# FP1
recs = [(f"r{i}", rnd(60), "I" * 60) for i in range(200)]
for label, args in [("--cut_front -f 5", ["--cut_front", "-f", "5"]),
                    ("--cut_tail  -t 5", ["--cut_tail", "-t", "5"]),
                    ("control -f 5    ", ["-f", "5"])]:
    reads, _ = run(recs, args + ["-Q", "-L", "-A", "-G", "-w", "1"])
    lens = sorted({len(s) for s, _ in reads.values()})
    print(f"FP1  {label}: output lengths {lens} (expected [55])")

# FP2
recs = []
for i in range(20000):
    # read-through: the read ends inside the adapter, no random tail, so that the
    # pre-1.0 nucleotide-tree detection has a fair chance as well
    ins = rnd(random.randint(20, 37))
    seq = (ins + RPI1)[:100]
    recs.append((f"r{i}", seq, "I" * len(seq)))
reads, err = run(recs, ["-w", "1"])
printed = re.findall(r"^[ACGT]{20,}$", err, re.M)
trimmed = re.search(r"reads with adapter trimmed: (\d+)", err)
print(f"FP2  auto-detect a 63 nt built-in adapter: printed "
      f"{(str(len(printed[0])) + ' nt') if printed else 'nothing'}, "
      f"'No adapter detected' {'yes' if 'No adapter detected' in err else 'no'}, "
      f"reads trimmed {trimmed.group(1) if trimmed else '?'} of 20000")
reads, err = run(recs, ["-a", RPI1, "-w", "1"])
trimmed = re.search(r"reads with adapter trimmed: (\d+)", err)
print(f"     control, the same adapter given with -a: reads trimmed "
      f"{trimmed.group(1) if trimmed else '?'} of 20000")

# FP3
def insert_base(ad, p):
    return ad[:p] + ("G" if ad[p] != "G" else "T") + ad[p:]


for label, mk in [("exact adapter    ", lambda: AD33),
                  ("one inserted base", lambda: insert_base(AD33, 8)),
                  ("one deleted base ", lambda: AD33[:8] + AD33[9:])]:
    recs = [(f"r{i}", (rnd(40) + mk() + rnd(60))[:100], "I" * 100) for i in range(200)]
    reads, _ = run(recs, ["-a", AD33, "-Q", "-L", "-G", "-w", "1"])
    n40 = sum(1 for s, _ in reads.values() if len(s) == 40)
    print(f"FP3  {label}: trimmed to 40 nt {n40:>4}/200")
