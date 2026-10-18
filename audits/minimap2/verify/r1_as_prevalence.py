"""R1: how often AS:i disagrees with its own CIGAR on realistic -x sr data, and
what the fix changes.

Sample genome = random 2 Mb reference with a SNP every ~1 kb and a 1-3 bp indel
every ~10 kb; 20,000 2 x 150 bp pairs, fragments N(350, 50), Illumina-like
substitution errors rising from 0.1 % at the 5' end to 1.5 % at the 3' end.
Every primary record's AS is recomputed from its CIGAR with the manual's
scoring (-x sr: A=2, B=8, O=12,24, E=2,1, N -1). Run on $MM2 and, if given,
$MM2_FIX; for the pair, every SAM field except AS is compared record by record.
"""
import os, sys, random, collections, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

FIX = os.environ.get("MM2_FIX")
rng = random.Random(2026)
G = 2000000
ref = rand_seq(rng, G)
sample = list(ref)
for p in range(500, G - 500, 1000):
    q = p + rng.randint(-300, 300)
    sample[q] = other_base(rng, sample[q])
edits = []
for p in range(5000, G - 5000, 10000):
    q = p + rng.randint(-2000, 2000)
    if rng.random() < .5:
        edits.append((q, "D", rng.randint(1, 3)))
    else:
        edits.append((q, "I", rand_seq(rng, rng.randint(1, 3))))
for q, k, x in sorted(edits, reverse=True):
    if k == "D": del sample[q:q + x]
    else: sample[q:q] = list(x)
sample = "".join(sample)
d = tmpdir(); fa = os.path.join(d, "ref.fa"); write_fasta(fa, [("chr1", ref)])


def illumina(s):
    out = list(s)
    for i in range(len(out)):
        if rng.random() < 0.001 + 0.014 * (i / (len(out) - 1)) ** 2:
            out[i] = other_base(rng, out[i])
    return "".join(out)


r1, r2 = [], []
for i in range(20000):
    flen = max(160, int(rng.gauss(350, 50)))
    st = rng.randint(0, len(sample) - flen)
    f = sample[st:st + flen]
    if rng.random() < .5:
        f = revcomp(f)
    r1.append((f"p{i}", illumina(f[:150]))); r2.append((f"p{i}", illumina(revcomp(f)[:150])))
fq1 = os.path.join(d, "r1.fq"); fq2 = os.path.join(d, "r2.fq")
write_fastq(fq1, r1); write_fastq(fq2, r2)


def go(binpath):
    out = subprocess.run([binpath, "-ax", "sr", "-t1", fa, fq1, fq2], capture_output=True, text=True).stdout
    recs = {}
    for r in parse_sam(out):
        if r["flag"] & 0x904: continue
        recs[(r["qname"], r["flag"] & 0xc0)] = r
    return recs, out


def summarise(label, recs):
    diff = collections.Counter(); n = 0; reads_bad = 0
    for r in recs.values():
        n += 1
        pa = port_as(aligned_pairs(r, ref), 2, 8, 12, 2, 24, 1)
        dd = r["tags"]["AS"] - pa
        diff[dd] += 1
    bad = n - diff[0]
    print(f"[{label}] {n} primary mapped records; AS == AS recomputed from the CIGAR on {diff[0]} "
          f"({100.0 * diff[0] / n:.2f} %); AS above it on {bad} ({100.0 * bad / n:.2f} %), by: {dict(sorted((k, v) for k, v in diff.items() if k))}")
    return diff


print(version(), " 2 Mb reference; 20,000 pairs 2 x 150 bp; -x sr")
rt, _ = go(MM2)
summarise("tested build", rt)
if FIX:
    rf, _ = go(FIX)
    summarise("fixed build", rf)
    other = 0; as_changed = 0
    for k, a in rt.items():
        b = rf.get(k)
        if b is None: other += 1; continue
        fa_ = {x: a[x] for x in a if x != "tags"}; fb = {x: b[x] for x in b if x != "tags"}
        ta = dict(a["tags"]); tb = dict(b["tags"])
        if ta.pop("AS") != tb.pop("AS"): as_changed += 1
        if fa_ != fb or ta != tb: other += 1
    print(f"[tested vs fixed] AS changed on {as_changed} records; any other field (FLAG, POS, MAPQ, CIGAR, TLEN, tags) "
          f"changed on {other} of {len(rt)}")
