#!/usr/bin/env python3
"""Held-up checks for the read modifiers and filters through the CLI, on random
paired-end FASTQ (600 pairs, lengths 0..70, ~35 % with a planted 3' adapter, N runs at
the ends, phred 2..40), against Python references:

  -m / -M boundaries (a read of exactly --minimum-length is kept)
  -m LEN1:LEN2 with --pair-filter any | both | first
  --max-n as count and as fraction
  --discard-untrimmed pair-filter default ('any' with -a and -A; 'both' with -a only)
  -l / -u / --trim-n / --strip-suffix
  two-file input == --interleaved input == --interleaved output == -j 3
"""
import os
import random
import subprocess
import sys
import tempfile

import cutadapt

print("cutadapt", cutadapt.__version__)
random.seed(42)
AD1 = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"
AD2 = "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def make_read(adapter):
    n = random.randint(0, 70)
    s = rnd(n)
    if random.random() < 0.35 and n > 5:
        cut = random.randint(3, n)
        s = s[:cut] + adapter[: n - cut]
    if random.random() < 0.2:
        s = "N" * random.randint(1, 3) + s[3:] if len(s) > 3 else s
    if random.random() < 0.2:
        s = s[:-2] + "NN" if len(s) > 2 else s
    q = "".join(chr(random.randint(2, 40) + 33) for _ in s)
    return s, q


pairs = []
for i in range(600):
    s1, q1 = make_read(AD1)
    s2, q2 = make_read(AD2)
    pairs.append((f"pair{i}_suffix/1", s1, q1, f"pair{i}_suffix/2", s2, q2))


def write(path, idx):
    with open(path, "w") as f:
        for p in pairs:
            f.write(f"@{p[idx]}\n{p[idx + 1]}\n+\n{p[idx + 2]}\n")


def read_fastq(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return [(lines[i][1:], lines[i + 1], lines[i + 3]) for i in range(0, len(lines), 4)]


def run(args, tmp, inputs, out=("o.fq", "p.fq")):
    outs = [os.path.join(tmp, o) for o in out]
    flags = ["-o", outs[0]] + (["-p", outs[1]] if len(outs) > 1 else [])
    subprocess.run([sys.executable, "-m", "cutadapt", "--quiet", *args, *flags, *inputs], check=True)
    return [read_fastq(o) for o in outs]


def bwa_back(q, cutoff):
    s, best, stop = 0, 0, len(q)
    for i in reversed(range(len(q))):
        s += cutoff - q[i]
        if s < 0:
            break
        if s > best:
            best, stop = s, i
    return stop


ok = lambda cond: "ok" if cond else "MISMATCH"

with tempfile.TemporaryDirectory() as tmp:
    r1, r2 = os.path.join(tmp, "r1.fq"), os.path.join(tmp, "r2.fq")
    write(r1, 0)
    write(r2, 3)
    il = os.path.join(tmp, "il.fq")
    with open(il, "w") as f:
        for p in pairs:
            f.write(f"@{p[0]}\n{p[1]}\n+\n{p[2]}\n@{p[3]}\n{p[4]}\n+\n{p[5]}\n")

    # single-end -m / -M boundary
    got = run(["-m", "30"], tmp, [r1], out=("o.fq",))[0]
    ref = [(n, s, q) for n, s, q, *_ in pairs if len(s) >= 30]
    print(f"-m 30 single-end: kept {len(got)}, reference (len >= 30) {len(ref)}: {ok(got == ref)}; "
          f"reads of exactly 30 nt kept: {sum(1 for _, s, _ in got if len(s) == 30)} of {sum(1 for _, s, *_ in pairs if len(s) == 30)}")
    got = run(["-M", "40"], tmp, [r1], out=("o.fq",))[0]
    ref = [(n, s, q) for n, s, q, *_ in pairs if len(s) <= 40]
    print(f"-M 40 single-end: kept {len(got)}, reference (len <= 40) {len(ref)}: {ok(got == ref)}")

    # paired -m with pair filter modes
    for mode, rule in [("any", lambda a, b: a or b), ("both", lambda a, b: a and b), ("first", lambda a, b: a)]:
        g1, g2 = run(["-m", "30:20", "--pair-filter", mode], tmp, [r1, r2])
        ref = [p for p in pairs if not rule(len(p[1]) < 30, len(p[4]) < 20)]
        same = [(a[0], a[1], a[2]) for a in g1] == [(p[0], p[1], p[2]) for p in ref] and [(b[0], b[1], b[2]) for b in g2] == [(p[3], p[4], p[5]) for p in ref]
        print(f"-m 30:20 --pair-filter {mode:5s}: kept {len(g1)} pairs, reference {len(ref)}: {ok(same)}")
    g1, g2 = run(["-m", "30"], tmp, [r1, r2])
    ref = [p for p in pairs if not (len(p[1]) < 30 or len(p[4]) < 30)]
    print(f"-m 30 paired (default any): kept {len(g1)}, reference {len(ref)}: {ok(len(g1) == len(ref) and [a[0] for a in g1] == [p[0] for p in ref])}")

    # --max-n
    for arg, rule in [("2", lambda s: s.count("N") > 2), ("0.1", lambda s: len(s) > 0 and s.count("N") / len(s) > 0.1), ("0", lambda s: s.count("N") > 0)]:
        got = run(["--max-n", arg], tmp, [r1], out=("o.fq",))[0]
        ref = [(n, s, q) for n, s, q, *_ in pairs if not rule(s)]
        print(f"--max-n {arg:3s}: kept {len(got)}, reference {len(ref)}: {ok(got == ref)}")

    # --discard-untrimmed pair-filter default
    from cutadapt.adapters import BackAdapter
    a1, a2 = BackAdapter(AD1), BackAdapter(AD2)
    t1 = [a1.match_to(p[1]) is not None for p in pairs]
    t2 = [a2.match_to(p[4]) is not None for p in pairs]
    g1, _ = run(["-a", AD1, "-A", AD2, "--discard-untrimmed"], tmp, [r1, r2])
    ref = sum(1 for x, y in zip(t1, t2) if x and y)
    print(f"-a -A --discard-untrimmed: kept {len(g1)} pairs; reference 'both mates trimmed' {ref}: {ok(len(g1) == ref)}")
    g1, _ = run(["-a", AD1, "--discard-untrimmed"], tmp, [r1, r2])
    print(f"-a only --discard-untrimmed: kept {len(g1)} pairs; reference 'R1 trimmed' {sum(t1)}: {ok(len(g1) == sum(t1))}")

    # modifiers
    got = run(["-l", "25"], tmp, [r1], out=("o.fq",))[0]
    print(f"-l 25: all lengths == min(len, 25): {ok(all(len(s) == min(len(p[1]), 25) for (_, s, _), p in zip(got, pairs)))}")
    got = run(["-l", "-25"], tmp, [r1], out=("o.fq",))[0]
    print(f"-l -25: sequence == original[-25:]: {ok(all(s == p[1][-25:] for (_, s, _), p in zip(got, pairs)))}")
    got = run(["-u", "5", "-u", "-3"], tmp, [r1], out=("o.fq",))[0]
    print(f"-u 5 -u -3: sequence == original[5:-3]: {ok(all(s == p[1][5:len(p[1]) - 3] for (_, s, _), p in zip(got, pairs)))}")
    got = run(["--trim-n"], tmp, [r1], out=("o.fq",))[0]
    print(f"--trim-n: sequence == original.strip('N'): {ok(all(s == p[1].strip('N') for (_, s, _), p in zip(got, pairs)))}")
    got = run(["--strip-suffix", "_suffix/1"], tmp, [r1], out=("o.fq",))[0]
    print(f"--strip-suffix: names stripped: {ok(all(n == p[0][:-len('_suffix/1')] for (n, _, _), p in zip(got, pairs)))}")
    got = run(["-q", "20"], tmp, [r1], out=("o.fq",))[0]
    print(f"-q 20: == BWA port: {ok(all(s == p[1][: bwa_back([ord(c) - 33 for c in p[2]], 20)] for (_, s, _), p in zip(got, pairs)))}")

    # interleaved / cores equivalence
    common = ["-a", AD1, "-A", AD2, "-q", "20", "-m", "20", "--trim-n", "--max-n", "0.2", "-e", "0.1", "-O", "3"]
    base = run(common, tmp, [r1, r2])
    inter_in = run(common + ["--interleaved"], tmp, [il])
    inter_out = run(common + ["--interleaved"], tmp, [r1, r2], out=("io.fq",))[0]
    inter_out = [(inter_out[i], inter_out[i + 1]) for i in range(0, len(inter_out), 2)]
    j3 = run(common + ["-j", "3"], tmp, [r1, r2])
    print(f"pipeline {' '.join(common[:8])}...: kept {len(base[0])} pairs")
    print(f"   --interleaved input == two files: {ok(inter_in == base)}")
    print(f"   --interleaved output == two files: {ok([a for a, _ in inter_out] == base[0] and [b for _, b in inter_out] == base[1])}")
    print(f"   -j 3 == -j 1: {ok(j3 == base)}")
