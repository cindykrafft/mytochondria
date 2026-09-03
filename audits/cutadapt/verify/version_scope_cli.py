#!/usr/bin/env python3
"""Version scope by execution: the four confirmed findings reproduced through the
command line only (no Python API, so it runs on old releases too). Run it with the
`cutadapt` executable of the venv under test on PATH / next to sys.executable.

  CA1  -e 1 with a 49-nt 3' adapter: reads carrying the adapter with exactly one
       substitution are not trimmed (300 reads; expected 300 trimmed)
  CA2  --max-ee 1 --quality-base 64 on phred+64 data with ~7 expected errors per
       read: nothing is discarded (expected: all 300 discarded)
  CA3  two anchored 5' adapters (12 nt / 11 nt) and a read that is the 11-mer
       exactly and the 12-mer with one insertion: default index assigns the
       12-mer, --no-index the 11-mer
  CA4  -g ^ADAPTER with one inserted base in the adapter occurrence and exactly one
       allowed error (-e 1 on the 34-nt Illumina adapter; -e 0.1 on the 19-nt
       Nextera adapter): fewer reads trimmed than with -g ADAPTER on the same file
       (expected: equal). The prefilter dates from 4.3, so 4.1 is a negative control.
"""
import os
import random
import subprocess
import sys
import tempfile

random.seed(2026)
EXE = os.path.join(os.path.dirname(sys.executable), "cutadapt")
print(subprocess.run([EXE, "--version"], capture_output=True, text=True).stdout.strip().splitlines()[-1], "(", EXE, ")")


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def run(args, inp, out):
    r = subprocess.run([EXE, *args, "-o", out, inp], capture_output=True, text=True)
    if r.returncode != 0:
        return None, (r.stderr.strip().splitlines() or ["?"])[-1]
    with open(out) as f:
        lines = f.read().splitlines()
    return [(lines[i][1:].split()[0], lines[i + 1]) for i in range(0, len(lines), 4)], None


def write_fastq(path, reads, base=33, quals=None):
    with open(path, "w") as f:
        for i, s in enumerate(reads):
            q = quals[i] if quals else "I" * len(s)
            f.write(f"@r{i}\n{s}\n+\n{q}\n")


with tempfile.TemporaryDirectory() as tmp:
    inp, out = os.path.join(tmp, "in.fastq"), os.path.join(tmp, "out.fastq")

    # CA1
    ad = rnd(49)
    reads = []
    for _ in range(300):
        p = random.randrange(49)
        reads.append(rnd(20) + ad[:p] + random.choice([c for c in "ACGT" if c != ad[p]]) + ad[p + 1 :] + rnd(30))
    write_fastq(inp, reads)
    res, err = run(["-e", "1", "-a", ad], inp, out)
    print("CA1  -e 1, 49-nt adapter, 300 one-substitution reads: trimmed to 20 nt:",
          sum(1 for _, s in res if len(s) == 20) if res else err)
    res, err = run(["-e", "1.0000001", "-a", ad], inp, out)
    print("     control -e 1.0000001:", sum(1 for _, s in res if len(s) == 20) if res else err)

    # CA2
    reads, quals = [], []
    for _ in range(300):
        n = random.randint(80, 120)
        reads.append(rnd(n))
        quals.append("".join(chr(random.randint(2, 20) + 64) for _ in range(n)))
    write_fastq(inp, reads, quals=quals)
    ee = [sum(10 ** (-(ord(c) - 64) / 10) for c in q) for q in quals]
    res, err = run(["--max-ee", "1", "--quality-base", "64"], inp, out)
    print(f"CA2  --max-ee 1 --quality-base 64, 300 phred+64 reads with EE {min(ee):.1f}..{max(ee):.1f}: kept",
          len(res) if res else err, "(expected 0)")

    # CA3
    reads = ["ACGTACGTAC" + "A" + "GT" + rnd(20) for _ in range(50)]
    write_fastq(inp, reads)
    for label, extra in (("default", []), ("--no-index", ["--no-index"])):
        d = os.path.join(tmp, label.strip("-"))
        os.makedirs(d, exist_ok=True)
        r = subprocess.run([EXE, "-e", "0.1", "-g", "A=^ACGTACGTACGT", "-g", "B=^ACGTACGTACA", *extra,
                            "-o", os.path.join(d, "{name}.fastq"), inp], capture_output=True, text=True)
        if r.returncode != 0:
            print(f"CA3  {label}:", (r.stderr.strip().splitlines() or ['?'])[-1])
            continue
        counts = {}
        for name in ("A", "B", "unknown"):
            p = os.path.join(d, f"{name}.fastq")
            counts[name] = sum(1 for _ in open(p)) // 4 if os.path.exists(p) else 0
        print(f"CA3  {label:10s}: {counts}")

    # CA4
    for ad, e in (("AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC", "1"), ("CTGTCTCTTATACACATCT", "0.1")):
        reads = []
        for p in range(len(ad) + 1):
            for _ in range(10):
                reads.append(ad[:p] + random.choice("ACGT") + ad[p:] + rnd(30))
        write_fastq(inp, reads)
        for label, args in (("-g ^AD", ["-g", "^" + ad]), ("-g AD ", ["-g", ad]), ("-g XAD", ["-g", "X" + ad])):
            res, err = run(["-e", e, *args], inp, out)
            print(f"CA4  {len(ad)}-nt adapter -e {e} {label}: trimmed",
                  sum(1 for _, s in res if len(s) < len(ad) + 31) if res else err, f"of {len(reads)}")
