#!/usr/bin/env python3
"""CA4: the k-mer prefilter (kmer_heuristic.py, added in 4.3 to skip the aligner
when no adapter k-mer is present) searches anchored and non-internal adapters in a
window exactly as long as the adapter (`create_back_overlap_searchsets`: window
`(-length, None)` for 3' types, `(0, length)` for 5' types). An adapter occurrence
that carries an inserted base spans length+1 read positions, so the k-mer chunk
on the far side of the insertion falls outside the window: `kmers_present` is
False and `match_to` returns None although the aligner accepts the occurrence
(1 error, within `-e`). Regular 3'/5' adapters are covered by their internal
search set; with `--no-indels` the prefilter is not used for anchored adapters.
The loss needs exactly ONE allowed error (two k-mer chunks; with more chunks a
chunk on the near side of the insertion is still inside the window): adapters of
10-19 nt at the default -e 0.1, 5-9 nt at -e 0.2, or any length with -e 1.

Part A: API. For each adapter type, reads = adapter with ONE inserted base at
        position p (every p), + random flanks. Compare match_to (prefilter +
        aligner) with the bare aligner.
Part B: CLI. The same reads through `cutadapt -g ^ADAPTER` vs `-g ADAPTER`
        (regular 5', same alignment, prefilter works) and `-a ADAPTER$` vs `-a ADAPTER`.
Part C: 'anywhere' adapters: reads shorter than the adapter that lie entirely
        inside it (min_overlap 3) -- the other prefilter blind spot.
"""
import os
import random
import subprocess
import sys
import tempfile

import cutadapt
from cutadapt.adapters import (
    BackAdapter, FrontAdapter, AnywhereAdapter, NonInternalBackAdapter, NonInternalFrontAdapter,
    PrefixAdapter, SuffixAdapter,
)

print("cutadapt", cutadapt.__version__)
random.seed(4)
ILLUMINA = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"  # 34 nt, -e 0.1 -> 3 errors
SMALLRNA = "TGGAATTCTCGGGTGCCAAGG"  # 21 nt, -e 0.1 -> 2 errors
NEXTERA = "CTGTCTCTTATACACATCT"  # 19 nt -> 1 error


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def with_insertion(s, p):
    return s[:p] + random.choice("ACGT") + s[p:]


print("\n== A. one inserted base at each position p of the adapter occurrence, 200 random flank draws per p")
for label, cls, front in [
    ("anchored 5' (^ADAPTER)", PrefixAdapter, True),
    ("anchored 3' (ADAPTER$)", SuffixAdapter, False),
    ("non-internal 5' (XADAPTER)", NonInternalFrontAdapter, True),
    ("non-internal 3' (ADAPTERX)", NonInternalBackAdapter, False),
    ("regular 5' (-g)", FrontAdapter, True),
    ("regular 3' (-a)", BackAdapter, False),
]:
    for ad, e in ((ILLUMINA, 0.1), (SMALLRNA, 0.1), (NEXTERA, 0.1), (ILLUMINA, 1), (SMALLRNA, 1)):
        kwargs = dict(max_errors=e)
        if cls not in (PrefixAdapter, SuffixAdapter):
            kwargs["min_overlap"] = 3
        adapter = cls(ad, **kwargs)
        aligner_found = prefilter_found = 0
        lost_positions = []
        for p in range(len(ad) + 1):
            lost = 0
            for _ in range(200):
                occ = with_insertion(ad, p)
                read = occ + rnd(random.randint(0, 40)) if front else rnd(random.randint(0, 40)) + occ
                raw = adapter.aligner.locate(read)
                m = adapter.match_to(read)
                aligner_found += raw is not None
                prefilter_found += m is not None
                if raw is not None and m is None:
                    lost += 1
            if lost:
                lost_positions.append((p, lost))
        n = 200 * (len(ad) + 1)
        print(f"  {label:27s} {len(ad)} nt -e {e}: aligner accepts {aligner_found}/{n}, match_to returns {prefilter_found}/{n} "
              f"-> lost {aligner_found - prefilter_found} ({100 * (aligner_found - prefilter_found) / max(aligner_found, 1):.0f}% of accepted); "
              f"insertion positions with losses: {[p for p, _ in lost_positions]}")

print("\n== B. CLI: (n+1) x 20 reads = adapter with one inserted base at p=0..n, plus 30 random nt")
with tempfile.TemporaryDirectory() as tmp:
    for AD, e in ((ILLUMINA, "0.1"), (ILLUMINA, "1"), (NEXTERA, "0.1")):
        print(f"   adapter {AD} ({len(AD)} nt), -e {e}:")
        for label, args, front in [
            ("-g ^AD (anchored 5')", ["-g", "^" + AD], True),
            ("-g AD  (regular 5')", ["-g", AD], True),
            ("-g XAD (non-internal 5')", ["-g", "X" + AD], True),
            ("-a AD$ (anchored 3')", ["-a", AD + "$"], False),
            ("-a AD  (regular 3')", ["-a", AD], False),
        ]:
            fq = os.path.join(tmp, "in.fastq")
            with open(fq, "w") as f:
                i = 0
                for p in range(len(AD) + 1):
                    for _ in range(20):
                        occ = with_insertion(AD, p)
                        s = occ + rnd(30) if front else rnd(30) + occ
                        f.write(f"@r{i}\n{s}\n+\n{'I' * len(s)}\n")
                        i += 1
            out = os.path.join(tmp, "out.fastq")
            subprocess.run([sys.executable, "-m", "cutadapt", "-e", e, *args, "-o", out, fq, "--quiet"], check=True)
            with open(out) as f:
                lens = [len(line.strip()) for j, line in enumerate(f) if j % 4 == 1]
            trimmed = sum(1 for L in lens if L < len(AD) + 31)
            print(f"      {label:26s}: {trimmed}/{i} reads trimmed")

print("\n== C. anywhere (-b) adapter, reads that lie entirely inside the adapter (min_overlap 3)")
adapter = AnywhereAdapter(ILLUMINA, max_errors=0.1, min_overlap=3)
lost = total = 0
for start in range(1, len(ILLUMINA) - 3):
    for length in range(3, min(12, len(ILLUMINA) - start)):
        read = ILLUMINA[start : start + length]
        total += 1
        if adapter.aligner.locate(read) is not None and adapter.match_to(read) is None:
            lost += 1
print(f"   internal substrings of the adapter as whole reads: {total}; aligner matches but match_to returns None: {lost}")
