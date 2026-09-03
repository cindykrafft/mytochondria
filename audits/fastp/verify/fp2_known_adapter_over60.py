#!/usr/bin/env python3
"""FP2: a built-in adapter longer than 60 nt is auto-detected, printed, and then
thrown away, so adapter trimming is silently disabled.

`Evaluator::evalAdapterAndReadNum` first calls `checkKnownAdapters`
(src/evaluator.cpp:257-343, added in v0.26.0/v1.0.0), which can return any entry of
`src/knownadapters.h`, including the 139 entries longer than 60 nt. `main.cpp:458`
and `:474` then do

    if(adapt.length() > 60 ) adapt.resize(0, 60);

`std::string::resize(size_type n, char c)` resizes to n and pads with c, so this
sets the adapter to the EMPTY string instead of truncating it to 60 characters.
The next line, `if(adapt.length() > 0)`, is therefore false: fastp prints
"No adapter detected for read1", sets the adapter to "", and (for SE data)
performs no adapter trimming at all -- after having printed the correct adapter
one line earlier. The JSON report loses its whole "adapter_cutting" section.

Part A  census of the built-in adapter table by length
Part B  SE runs: auto-detection vs explicit --adapter_sequence, per adapter length
Part C  PE runs with --detect_adapter_for_pe
Part D  what the read1 output looks like (bases of adapter left in the reads)

Usage: python3 fp2_known_adapter_over60.py [path-to-fastp] [path-to-knownadapters.h]
"""
import json
import os
import random
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastp_ref import write_fastq  # noqa: E402

EXE = sys.argv[1] if len(sys.argv) > 1 else "./fastp"
HDR = sys.argv[2] if len(sys.argv) > 2 else None
random.seed(11)
print("fastp:", os.popen(f"{EXE} --version 2>&1").read().strip())

COMP = str.maketrans("ACGTN", "TGCAN")


def rc(s):
    return s.translate(COMP)[::-1]


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


# ------------------------------------------------------------------- Part A
print("\n== Part A: census of src/knownadapters.h")
if HDR and os.path.exists(HDR):
    text = open(HDR).read()
    ads = re.findall(r'knownAdapters\["([ACGT]+)"\]\s*=\s*"([^"]*)"', text)
    seqs = [a for a, _ in ads]
    over = [a for a, _ in ads if len(a) > 60]
    # checkKnownAdapters keeps the entry with the strictly largest hit count and
    # scans the table in std::map (lexicographic) order, so a shorter adapter that
    # is a prefix of a long one always wins the tie and shields it from the bug.
    naked = [a for a in over if not any(b != a and a.startswith(b) for b in seqs)]
    print(f"  built-in adapters: {len(ads)}; longer than 60 nt: {len(over)} "
          f"({100.0 * len(over) / len(ads):.0f} %); of those, without a shorter "
          f"built-in prefix: {len(naked)}")
    fam = {}
    for a, d in ads:
        if a in naked:
            key = d.split("|")[0].strip().lstrip(">").rstrip("0123456789_ (")
            fam[key] = fam.get(key, 0) + 1
    print("  families that can be selected and then discarded:")
    for k in sorted(fam, key=lambda k: -fam[k])[:8]:
        print(f"    {fam[k]:>4}  {k}")
else:
    print("  (knownadapters.h not given; skipping census)")

# ------------------------------------------------------------------- Part B
ADAPTERS = [
    ("TruSeq Universal Adapter (58 nt)",
     "AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT"),
    ("TruSeq Adapter Read 1 (33 nt)",
     "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"),
    ("TruSeq Small RNA RPI1 (63 nt)",
     "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"),
    ("TruSeq Adapter Index 5 (63 nt)",
     "GATCGGAAGAGCACACGTCTGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"),
    ("Reverse_adapter (64 nt)",
     "AGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"),
    ("RNA PCR Primer Index 35 (63 nt)",
     "CAAGCAGAAGACGGCATACGAGATAAAATGGTGACTGGAGTTCCTTGGCACCCGAGAATTCCA"),
    ("pcr_dimer (119 nt)",
     "AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCTAGATCGG"
     "AAGAGCGGTTCAGCAGGAATGCCGAGACCGATCTCGTATGCCGTCTTCTGCTTG"),
]
NREADS, RLEN = 20000, 100


def make_reads(adapter, n=NREADS, rlen=RLEN):
    """Every read carries the adapter after an insert of 20-37 nt (read-through).

    The read ends inside or just after the adapter, as a real read-through does;
    anything after the adapter is drawn at random."""
    out = []
    for i in range(n):
        ins = rnd(random.randint(20, 37))
        seq = (ins + adapter + rnd(rlen))[:rlen]
        out.append((f"r{i}", seq, "I" * len(seq), len(ins)))
    return out


def run(args, records, r2=None):
    tmp = tempfile.mkdtemp()
    p1 = os.path.join(tmp, "in1.fq")
    write_fastq(p1, [(n, s, q) for n, s, q, _ in records])
    cmd = [EXE, "-i", p1, "-o", os.path.join(tmp, "o1.fq"),
           "-j", os.path.join(tmp, "o.json"), "-h", os.path.join(tmp, "o.html"), "-w", "1"]
    if r2 is not None:
        p2 = os.path.join(tmp, "in2.fq")
        write_fastq(p2, [(n, s, q) for n, s, q, _ in r2])
        cmd += ["-I", p2, "-O", os.path.join(tmp, "o2.fq")]
    cmd += list(args)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    with open(os.path.join(tmp, "o.json")) as fh:
        js = json.load(fh)
    return js, proc.stderr, os.path.join(tmp, "o1.fq")


print(f"\n== Part B: single-end, {NREADS} reads of {RLEN} nt, every read carries the adapter")
print(f"  {'built-in adapter':<34} {'len':>4} {'printed by fastp':>18} {'auto: trimmed':>14} {'explicit -a: trimmed':>21}")
for label, ad in ADAPTERS:
    recs = make_reads(ad)
    js, err, _ = run([], recs)
    hits = re.findall(r"^[ACGT]{20,}$", err, re.M)
    printed = f"{len(hits[0])} nt" if hits else "nothing"
    no_ad = "No adapter detected" in err
    auto = js.get("adapter_cutting", {}).get("adapter_trimmed_reads", "no section")
    js2, _, _ = run(["-a", ad], recs)
    expl = js2.get("adapter_cutting", {}).get("adapter_trimmed_reads", "no section")
    verdict = "-> DISCARDED" if no_ad else ""
    print(f"  {label:<34} {len(ad):>4} {printed:>18} {str(auto):>14} {str(expl):>21}  {verdict}")

# ------------------------------------------------------------------- Part C
print("\n== Part C: paired-end with --detect_adapter_for_pe (adapter trimming by overlap still runs)")
print(f"  {'built-in adapter':<34} {'len':>4} {'read1_adapter_sequence':>24} {'trimmed reads':>14}")
for label, ad in ADAPTERS[:1] + ADAPTERS[2:4]:
    r1 = make_reads(ad, n=20000)
    r2 = [(n, (rc(s[:ins]) + rc(ad) + rnd(RLEN))[:RLEN], "I" * RLEN, ins) for n, s, q, ins in r1]
    js, err, _ = run(["-2", "--disable_adapter_trimming"], r1, r2=r2)  # detection only
    seq = js.get("adapter_cutting", {}).get("read1_adapter_sequence", "no section")
    js2, err2, _ = run(["-2"], r1, r2=r2)
    tr = js2.get("adapter_cutting", {}).get("adapter_trimmed_reads", "no section")
    seq2 = js2.get("adapter_cutting", {}).get("read1_adapter_sequence", "no section")
    print(f"  {label:<34} {len(ad):>4} {str(seq2)[:24]:>24} {str(tr):>14}")

# ------------------------------------------------------------------- Part D
print("\n== Part D: what stays in the reads (SE, TruSeq Small RNA RPI1, 63 nt)")
ad = ADAPTERS[2][1]
recs = make_reads(ad, n=2000)
js, err, out1 = run([], recs)
lines = open(out1).read().splitlines()
got = {lines[i][1:]: lines[i + 1] for i in range(0, len(lines), 4)}
correct = {n: s[:ins] for n, s, q, ins in recs}
untrimmed = sum(1 for n in correct if got.get(n) != correct[n])
adapter_bases = sum(len(got[n]) - len(correct[n]) for n in correct if n in got)
print(f"  reads whose adapter was not removed: {untrimmed}/2000")
print(f"  adapter bases left in the output:    {adapter_bases}")
print(f"  stderr said: " + " | ".join(l for l in err.splitlines()
                                      if "detect" in l.lower() or "adapter" in l.lower())[:400])
