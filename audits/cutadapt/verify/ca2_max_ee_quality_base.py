#!/usr/bin/env python3
"""CA2: `--max-expected-errors` / `--max-average-error-rate` ignore `--quality-base`.

`TooManyExpectedErrors.test` and `TooHighAverageErrorRate.test` call
`expected_errors(read.qualities)` with the default base 33, so on phred+64 data
declared with `--quality-base 64` every quality is read 31 too high and the
expected-error sum is ~1259x too small: nothing is filtered. `-q` (quality
trimming) does receive the base and is correct -- shown here as the control.

Synthetic FASTQ: 2000 reads, length 50-150, phred 2..40 uniform per base.
Reference: sum of 10^(-q/10) computed in Python with the true offset.
"""
import os
import random
import subprocess
import sys
import tempfile

import cutadapt

print("cutadapt", cutadapt.__version__)
random.seed(7)

reads = []
for i in range(2000):
    n = random.randint(50, 150)
    seq = "".join(random.choice("ACGT") for _ in range(n))
    quals = [random.randint(2, 40) for _ in range(n)]
    reads.append((f"r{i}", seq, quals))


def ee(quals):
    return sum(10 ** (-q / 10) for q in quals)


def write_fastq(path, base):
    with open(path, "w") as f:
        for name, seq, quals in reads:
            f.write(f"@{name}\n{seq}\n+\n{''.join(chr(q + base) for q in quals)}\n")


def run(args, inp, tmp):
    out = os.path.join(tmp, "out.fastq")
    subprocess.run([sys.executable, "-m", "cutadapt", *args, "-o", out, inp, "--quiet"], check=True)
    with open(out) as f:
        lines = f.read().splitlines()
    return [(lines[i][1:], lines[i + 1]) for i in range(0, len(lines), 4)]


def bwa_trim_back(quals, cutoff):
    s, best, stop = 0, 0, len(quals)
    for i in reversed(range(len(quals))):
        s += cutoff - quals[i]
        if s < 0:
            break
        if s > best:
            best, stop = s, i
    return stop


with tempfile.TemporaryDirectory() as tmp:
    fq33 = os.path.join(tmp, "in33.fastq")
    fq64 = os.path.join(tmp, "in64.fastq")
    write_fastq(fq33, 33)
    write_fastq(fq64, 64)

    for thr in (0.5, 1.0, 2.0):
        ref_kept = {name for name, _, q in reads if not ee(q) > thr}
        k33 = {n for n, _ in run(["--max-ee", str(thr)], fq33, tmp)}
        k64 = {n for n, _ in run(["--max-ee", str(thr), "--quality-base", "64"], fq64, tmp)}
        print(
            f"--max-ee {thr}: reference keeps {len(ref_kept)}/2000 | "
            f"phred+33 file, default base: keeps {len(k33)} (== reference: {k33 == ref_kept}) | "
            f"phred+64 file, --quality-base 64: keeps {len(k64)} (== reference: {k64 == ref_kept})"
        )

    for thr in (0.01, 0.02):
        ref_kept = {name for name, _, q in reads if not ee(q) / len(q) > thr}
        k33 = {n for n, _ in run(["--max-aer", str(thr)], fq33, tmp)}
        k64 = {n for n, _ in run(["--max-aer", str(thr), "--quality-base", "64"], fq64, tmp)}
        print(
            f"--max-aer {thr}: reference keeps {len(ref_kept)}/2000 | phred+33: keeps {len(k33)} "
            f"(== ref: {k33 == ref_kept}) | phred+64 + --quality-base 64: keeps {len(k64)} (== ref: {k64 == ref_kept})"
        )

    # Control: -q honours --quality-base
    ref = {name: seq[: bwa_trim_back(q, 20)] for name, seq, q in reads}
    got33 = dict(run(["-q", "20"], fq33, tmp))
    got64 = dict(run(["-q", "20", "--quality-base", "64"], fq64, tmp))
    print(
        f"control -q 20: phred+33 == BWA port: {got33 == ref}; phred+64 with --quality-base 64 == BWA port: {got64 == ref}"
    )

    # What the phred+64 run actually computed: the +33 interpretation
    from cutadapt.qualtrim import expected_errors

    name, seq, q = reads[0]
    q64 = "".join(chr(x + 64) for x in q)
    print(
        f"read {name}: true EE (base 64) = {ee(q):.4f}; shipped expected_errors(q, base=64) = {expected_errors(q64, 64):.4f}; "
        f"shipped default expected_errors(q) = {expected_errors(q64):.6f} (this is what the predicate uses)"
    )
