#!/usr/bin/env python3
"""CA3: the adapter index (default for >= 2 anchored adapters, i.e. demultiplexing)
picks the best adapter by *number of matches* (adapters.py `_match_to_multiple_lengths`),
while the non-indexed path (`MultipleAdapters.match_to`, used with `--no-index`
and for all non-anchored adapters) picks by alignment *score*
(match +1, mismatch -1, indel -2 -- the criterion documented in
doc/algorithms.rst "changes in Cutadapt 4"). The index also stores the match
count in the Match's `score` field. Same input, different assignment.

Part A: minimal example (two 5' anchored barcodes of length 12 and 11).
Part B: random barcode sets, reads with one planted edit: how often the two
        paths disagree, split by kind of disagreement.
Part C: mixed adapter lists (indexed barcodes + a regular 3' adapter): the
        `score` stored by the index is compared with real alignment scores.
Part D: the CLI (`-g ^name=SEQ ... -o {name}.fastq`) with and without --no-index.
"""
import os
import random
import subprocess
import sys
import tempfile
from collections import Counter

import cutadapt
from cutadapt.adapters import PrefixAdapter, BackAdapter, IndexedPrefixAdapters, MultipleAdapters
from cutadapt.modifiers import AdapterCutter

print("cutadapt", cutadapt.__version__)
random.seed(11)


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def one_edit(s):
    kind = random.choice(["sub", "ins", "del"])
    i = random.randrange(len(s))
    if kind == "sub":
        return s[:i] + random.choice([c for c in "ACGT" if c != s[i]]) + s[i + 1 :], kind
    if kind == "ins":
        return s[:i] + random.choice("ACGT") + s[i:], kind
    return s[:i] + s[i + 1 :], kind


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


# ---------------------------------------------------------------- Part A
print("\n== A. minimal example: A=ACGTACGTACGT (12 nt), B=ACGTACGTACA (11 nt), -e 0.1 (1 error each)")
print("   read = ACGTACGTAC A GT...  = B exactly (11 matches, 0 errors, score 11)")
print("                             = A with one inserted base (12 matches, 1 indel, score 12-2=10)")
A = PrefixAdapter("ACGTACGTACGT", max_errors=0.1, name="A")
B = PrefixAdapter("ACGTACGTACA", max_errors=0.1, name="B")
read = "ACGTACGTAC" + "A" + "GT" + rnd(20)
for order in ([A, B], [B, A]):
    mi = IndexedPrefixAdapters(order).match_to(read)
    mn = MultipleAdapters(order).match_to(read)
    print(f"   order {[a.name for a in order]}: index -> {mi.adapter.name} {mi}")
    print(f"                    --no-index -> {mn.adapter.name} {mn}")

# ---------------------------------------------------------------- Part B
print("\n== B. random barcode sets, reads = barcode + one random edit (sub/ins/del) + 40 nt; -e 1, indels allowed")
print("   three-way: index | --no-index via adapter.match_to (k-mer prefilter + aligner) | --no-index via the bare aligner")
print("   (the prefilter has its own false negatives for anchored adapters -- see CA4 -- so the criterion is judged on the bare aligner)")


def make_set(lengths, n=6, min_dist=3):
    while True:
        bcs = [rnd(random.choice(lengths)) for _ in range(n)]
        if all(lev(x, y) >= min_dist for i, x in enumerate(bcs) for y in bcs[i + 1 :]):
            return bcs


def best_by_aligner(adapters, seq):
    """MultipleAdapters.match_to without the k-mer prefilter: same score/errors/order rule."""
    best = None
    for a in adapters:
        r = a.aligner.locate(seq)
        if r is None:
            continue
        score, errors = r[4], r[5]
        if best is None or score > best[0] or (score == best[0] and errors < best[1]):
            best = (score, errors, a.name)
    return best[2] if best else None


for label, lengths in [("mixed lengths 10-12", [10, 11, 12]), ("all length 10", [10])]:
    tally = Counter()
    kinds = Counter()
    n_reads = 0
    for trial in range(25):
        bcs = make_set(lengths)
        adapters_i = [PrefixAdapter(s, max_errors=1, name=f"bc{i}") for i, s in enumerate(bcs)]
        adapters_n = [PrefixAdapter(s, max_errors=1, name=f"bc{i}") for i, s in enumerate(bcs)]
        ci = AdapterCutter(adapters_i, index=True)
        cn = AdapterCutter(adapters_n, index=False)
        for _ in range(400):
            i = random.randrange(len(bcs))
            edited, kind = one_edit(bcs[i])
            seq = edited + rnd(40)
            mi = ci.adapters.match_to(seq)
            mn = cn.adapters.match_to(seq)
            ni = mi.adapter.name if mi else None
            nn = mn.adapter.name if mn else None
            na = best_by_aligner(adapters_n, seq)
            n_reads += 1
            if ni == na:
                tally["index == bare aligner (score rule)"] += 1
            elif ni is None:
                tally["index unassigned, bare aligner assigns"] += 1
            elif na is None:
                tally["index assigns, bare aligner unassigned"] += 1
            else:
                tally["index and bare aligner assign DIFFERENT adapters"] += 1
                kinds[("criterion", kind)] += 1
                ra = {a.name: a.aligner.locate(seq) for a in adapters_n if a.aligner.locate(seq)}
                print(f"      differing read {seq[:16]}... planted {bcs[i]} ({kind}); index -> {ni} {mi}; "
                      f"bare aligner (score, errors, order) -> {na}; all aligner hits: {ra}")
            if nn != na:
                tally["--no-index match_to != bare aligner (prefilter false negative, CA4)"] += 1
                kinds[("prefilter", kind)] += 1
    print(f"   {label}: {n_reads} reads -> {dict(tally)}")
    print(f"      by planted edit: {dict(kinds)}")

# ---------------------------------------------------------------- Part C
print("\n== C. index Match.score is the number of matches, not the alignment score")
bc1, bc2 = "ACGTTGCAAC", "GGATCCTTGA"
ad3 = "TTCAGACGTGTGC"
idx = IndexedPrefixAdapters([PrefixAdapter(bc1, max_errors=1, name="bc1"), PrefixAdapter(bc2, max_errors=1, name="bc2")])
non = MultipleAdapters([PrefixAdapter(bc1, max_errors=1, name="bc1"), PrefixAdapter(bc2, max_errors=1, name="bc2")])
seq = bc1[:5] + "T" + bc1[5:] + rnd(20)  # bc1 with an inserted T
print(f"   read = bc1 with one insertion: index score={idx.match_to(seq).score} errors={idx.match_to(seq).errors}; "
      f"--no-index score={non.match_to(seq).score} errors={non.match_to(seq).errors}")
print("   mixed list [^bc1, ^bc2, 3'-adapter], read = bc1-with-insertion + 15 nt + first 9 nt of the 3' adapter:")
seq = bc1[:5] + "T" + bc1[5:] + rnd(15) + ad3[:9]
for index in (True, False):
    cutter = AdapterCutter(
        [PrefixAdapter(bc1, max_errors=1, name="bc1"), PrefixAdapter(bc2, max_errors=1, name="bc2"),
         BackAdapter(ad3, max_errors=0.1, name="ad3")],
        index=index,
    )
    m = cutter.adapters.match_to(seq)
    print(f"      index={index}: chosen {m.adapter.name} (score field {m.score}, errors {m.errors})")

# ---------------------------------------------------------------- Part D
print("\n== D. CLI demultiplexing (-g A=^... -g B=^... -o {name}.fastq), the Part A read repeated 100x, default vs --no-index")
with tempfile.TemporaryDirectory() as tmp:
    fq = os.path.join(tmp, "in.fastq")
    with open(fq, "w") as f:
        for i in range(100):
            s = "ACGTACGTAC" + "A" + "GT" + rnd(20)
            f.write(f"@r{i}\n{s}\n+\n{'I' * len(s)}\n")
    for extra in ([], ["--no-index"]):
        outdir = os.path.join(tmp, "noindex" if extra else "index")
        os.makedirs(outdir)
        subprocess.run(
            [sys.executable, "-m", "cutadapt", "-e", "0.1", "-g", "A=^ACGTACGTACGT", "-g", "B=^ACGTACGTACA",
             "-o", os.path.join(outdir, "{name}.fastq"), fq, "--quiet", *extra],
            check=True,
        )
        counts = {}
        for name in ("A", "B", "unknown"):
            p = os.path.join(outdir, f"{name}.fastq")
            counts[name] = sum(1 for _ in open(p)) // 4 if os.path.exists(p) else 0
        print(f"   {'--no-index' if extra else 'default   '}: {counts}")
