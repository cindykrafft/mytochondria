#!/usr/bin/env python3
"""What held up: poly-G/poly-X trimming, base correction, UMI handling,
--reads_to_process, --split, and the duplication-rate estimator.

H1  --trim_poly_g / --trim_poly_x against the ports in fastp_ref.py
H2  base correction (-c) rules on constructed pairs with known quality patterns
H3  UMI extraction (read1 / per_read / index1, --umi_skip, --umi_prefix)
H4  --reads_to_process
H5  --split: no read lost, no read duplicated
H6  duplication rate and --dedup against a known duplication level

Usage: python3 heldup_pipeline_and_dup.py [path-to-fastp]
"""
import json
import os
import random
import subprocess
import sys
import tempfile
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastp_ref import read_fastq, run_fastp, trim_poly_g, trim_poly_x, write_fastq  # noqa: E402

EXE = sys.argv[1] if len(sys.argv) > 1 else "./fastp"
random.seed(99)
print("fastp:", os.popen(f"{EXE} --version 2>&1").read().strip())
BASE = ["-A", "-G", "-Q", "-L", "-w", "1", "--dont_eval_duplication"]
COMP = str.maketrans("ACGTN", "TGCAN")


def rc(s):
    return s.translate(COMP)[::-1]


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


# ------------------------------------------------------------------------ H1
print("\n== H1: poly-G / poly-X trimming vs the ports (20,000 constructed tails)")
recs = []
for i in range(20000):
    body = rnd(random.randint(20, 60))
    kind = i % 4
    if kind == 0:
        tail = "G" * random.randint(0, 20)
    elif kind == 1:
        tail = "A" * random.randint(0, 20)
    elif kind == 2:  # poly-G with sequencing errors sprinkled in
        tail = "".join(random.choice("GGGGGGGGGT") for _ in range(random.randint(0, 25)))
    else:
        tail = "".join(random.choice("AAAAAAAAAC") for _ in range(random.randint(0, 25)))
    recs.append((f"r{i}", body + tail, "I" * (len(body) + len(tail))))

for label, args, fn in [
    ("-g (poly_g_min_len 10)", ["-g"], lambda s: trim_poly_g(s, 10)),
    ("-g --poly_g_min_len 5", ["-g", "--poly_g_min_len", "5"], lambda s: trim_poly_g(s, 5)),
    ("-g --poly_g_min_len 20", ["-g", "--poly_g_min_len", "20"], lambda s: trim_poly_g(s, 20)),
    ("-x (poly_x_min_len 10)", ["-x"], lambda s: trim_poly_x(s, 10)),
    ("-x --poly_x_min_len 15", ["-x", "--poly_x_min_len", "15"], lambda s: trim_poly_x(s, 15)),
]:
    reads, _, _ = run_fastp(EXE, args + ["-A", "-Q", "-L", "-w", "1", "--dont_eval_duplication"],
                            records=recs)
    ok = 0
    for n, s, q in recs:
        want = fn(s)
        got = reads.get(n)
        got_seq = got[0] if got else ""
        ok += got_seq == want
    print(f"  {label:<28} reads equal to the port: {ok}/20000")

# ------------------------------------------------------------------------ H2
print("\n== H2: base correction (-c): GOOD_QUAL = Q30, BAD_QUAL = Q14 "
      "(basecorrector.cpp:20-21)")
overlap = rnd(80)
cases = [
    ("r1 Q40, r2 Q2   -> r2 takes r1's base", 40, 2, "r2"),
    ("r1 Q2,  r2 Q40  -> r1 takes r2's base", 2, 40, "r1"),
    ("r1 Q30, r2 Q14  -> boundary, corrected", 30, 14, "r2"),
    ("r1 Q29, r2 Q14  -> not corrected", 29, 14, "none"),
    ("r1 Q30, r2 Q15  -> not corrected", 30, 15, "none"),
    ("r1 Q40, r2 Q20  -> not corrected", 40, 20, "none"),
]
print(f"  {'case':<44} {'corrected_bases':>16} {'expected':>10}  {'r1 out':>8} {'r2 out':>8}")
for label, q1, q2, who in cases:
    r1s = overlap
    r2s = rc(overlap)
    # single mismatch at overlap position 40
    bad = "A" if overlap[40] != "A" else "C"
    r1s = overlap[:40] + bad + overlap[41:]
    q1s = "".join(chr(q1 + 33) if i == 40 else "I" for i in range(80))
    q2s = "".join(chr(q2 + 33) if i == 39 else "I" for i in range(80))  # mirrored position
    tmp = tempfile.mkdtemp()
    p1, p2 = os.path.join(tmp, "1.fq"), os.path.join(tmp, "2.fq")
    write_fastq(p1, [("p", r1s, q1s)])
    write_fastq(p2, [("p", r2s, q2s)])
    o1, o2 = os.path.join(tmp, "o1.fq"), os.path.join(tmp, "o2.fq")
    jp = os.path.join(tmp, "o.json")
    subprocess.run([EXE, "-i", p1, "-I", p2, "-o", o1, "-O", o2, "-c", "-j", jp,
                    "-h", os.path.join(tmp, "o.html"), "-A", "-G", "-Q", "-L", "-w", "1",
                    "--dont_eval_duplication"], capture_output=True, text=True)
    js = json.load(open(jp))
    cb = js["filtering_result"].get("corrected_bases", 0)
    a1 = read_fastq(o1)["p"][0]
    a2 = read_fastq(o2)["p"][0]
    fixed1 = "kept" if a1[40] == bad else "changed"
    fixed2 = "kept" if a2[39] == rc(overlap)[39] else "changed"
    exp = 0 if who == "none" else 1
    print(f"  {label:<44} {cb:>16} {exp:>10}  {fixed1:>8} {fixed2:>8}")

# ------------------------------------------------------------------------ H3
print("\n== H3: UMI extraction")
name = "NS500713:64:HFKJJBGXY:1:11101:1675:1101 1:N:0:TATAGCCT+GACCCCCA"
seq = "AAAAAAAA" + "GCTACTTGGAGTACCAATAATAAAGTGAGCCCACC"
qual = "I" * len(seq)
for label, args, want_name, want_seq in [
    ("--umi_loc read1 --umi_len 8", ["-U", "--umi_loc", "read1", "--umi_len", "8"],
     "NS500713:64:HFKJJBGXY:1:11101:1675:1101:AAAAAAAA", seq[8:]),
    ("... --umi_skip 3", ["-U", "--umi_loc", "read1", "--umi_len", "8", "--umi_skip", "3"],
     "NS500713:64:HFKJJBGXY:1:11101:1675:1101:AAAAAAAA", seq[11:]),
    ("... --umi_prefix UMI", ["-U", "--umi_loc", "read1", "--umi_len", "8",
                             "--umi_prefix", "UMI"],
     "NS500713:64:HFKJJBGXY:1:11101:1675:1101:UMI_AAAAAAAA", seq[8:]),
    ("--umi_loc index1 (from the read name)", ["-U", "--umi_loc", "index1"],
     "NS500713:64:HFKJJBGXY:1:11101:1675:1101:TATAGCCT", seq),
]:
    tmp = tempfile.mkdtemp()
    p1 = os.path.join(tmp, "1.fq")
    write_fastq(p1, [(name, seq, qual)])
    o1 = os.path.join(tmp, "o1.fq")
    subprocess.run([EXE, "-i", p1, "-o", o1, "-j", os.path.join(tmp, "j"),
                    "-h", os.path.join(tmp, "h")] + args + BASE, capture_output=True)
    lines = open(o1).read().splitlines()
    got_name, got_seq = lines[0][1:].split()[0], lines[1]
    print(f"  {label:<40} name {'ok' if got_name == want_name else 'DIFFERS: ' + got_name}"
          f"   seq {'ok' if got_seq == want_seq else 'DIFFERS'}")

# ------------------------------------------------------------------------ H4
print("\n== H4: --reads_to_process")
recs = [(f"r{i}", rnd(60), "I" * 60) for i in range(5000)]
for n in (1, 999, 1000, 1001, 4999, 5000, 6000):
    reads, _, jp = run_fastp(EXE, ["--reads_to_process", str(n)] + BASE, records=recs)
    js = json.load(open(jp))
    got = js["summary"]["before_filtering"]["total_reads"]
    exp = min(n, 5000)
    print(f"  --reads_to_process {n:>5}: total_reads {got:>5} (expected {exp:>5})  "
          f"first read kept is {sorted(reads, key=lambda k: int(k[1:]))[0]}  "
          f"{'ok' if got == exp else 'DIFFERS'}")

# ------------------------------------------------------------------------ H5
print("\n== H5: --split / --split_by_lines: reads conserved")
tmp = tempfile.mkdtemp()
p1 = os.path.join(tmp, "in.fq")
write_fastq(p1, recs)
for label, args, expect_files in [("--split 4", ["-s", "4"], 4),
                                  ("--split 7", ["-s", "7"], 7),
                                  ("--split_by_lines 4000", ["-S", "4000"], None)]:
    d = tempfile.mkdtemp()
    subprocess.run([EXE, "-i", p1, "-o", os.path.join(d, "out.fq"),
                    "-j", os.path.join(d, "j"), "-h", os.path.join(d, "h")] + args + BASE,
                   capture_output=True)
    files = sorted(f for f in os.listdir(d) if f.endswith("out.fq"))
    seen = Counter()
    for f in files:
        for k in read_fastq(os.path.join(d, f)):
            seen[k] += 1
    print(f"  {label:<22} files {len(files):>3} "
          f"(expected {expect_files if expect_files else 'n/a'})   reads {sum(seen.values()):>5}/5000"
          f"   duplicated {sum(1 for v in seen.values() if v > 1)}   missing {5000 - len(seen)}")

# ------------------------------------------------------------------------ H6
print("\n== H6: duplication rate against a known duplication level (SE and PE)")
for dup_frac in (0.0, 0.2, 0.5):
    uniq = int(20000 * (1 - dup_frac))
    pool = [rnd(100) for _ in range(uniq)]
    seqs = pool + [random.choice(pool) for _ in range(20000 - uniq)]
    random.shuffle(seqs)
    truth = 1.0 - len(set(seqs)) / len(seqs)
    r1 = [(f"r{i}", s, "I" * 100) for i, s in enumerate(seqs)]
    tmp = tempfile.mkdtemp()
    p1 = os.path.join(tmp, "1.fq")
    write_fastq(p1, r1)
    p2 = os.path.join(tmp, "2.fq")
    write_fastq(p2, [(n, rc(s), q) for n, s, q in r1])
    out = {}
    for mode, extra in (("SE", []), ("PE", ["-I", p2, "-O", os.path.join(tmp, "o2.fq")])):
        jp = os.path.join(tmp, f"j{mode}")
        subprocess.run([EXE, "-i", p1, "-o", os.path.join(tmp, f"o1{mode}.fq"),
                        "-j", jp, "-h", os.path.join(tmp, "h"), "-A", "-G", "-Q", "-L",
                        "-w", "1"] + extra, capture_output=True)
        out[mode] = json.load(open(jp))["duplication"]["rate"]
    jp = os.path.join(tmp, "jd")
    subprocess.run([EXE, "-i", p1, "-o", os.path.join(tmp, "od.fq"), "-j", jp,
                    "-h", os.path.join(tmp, "h"), "-D", "-A", "-G", "-Q", "-L", "-w", "1"],
                   capture_output=True)
    kept = len(read_fastq(os.path.join(tmp, "od.fq")))
    print(f"  true duplication {truth:.4f}: fastp SE {out['SE']:.4f}  PE {out['PE']:.4f}  "
          f"| --dedup keeps {kept} reads (distinct = {len(set(seqs))})")
