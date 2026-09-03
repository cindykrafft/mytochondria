#!/usr/bin/env python3
"""CA1: `-e N` (absolute number of errors) is converted to a rate k/n and the
acceptance test is `errors <= length * rate` in floating point. For some (k, n)
the product `n * (k/n)` rounds *below* k (e.g. 49 * (1/49) = 0.9999999999999999),
so the adapter is only found with k-1 errors: `-e 1` on a 49-nt adapter allows
no errors at all, `-e 2` on a 98-nt adapter allows one.

Part A: closed form -- which (k, n) and which partial lengths L are affected.
Part B: shipped Aligner / PrefixComparer / adapter classes on synthetic reads.
Part C: the CLI on a synthetic FASTQ.
"""
import os
import random
import subprocess
import sys
import tempfile
from fractions import Fraction

import cutadapt
from cutadapt.adapters import (
    BackAdapter,
    FrontAdapter,
    PrefixAdapter,
    SuffixAdapter,
    IndexedPrefixAdapters,
)

print("cutadapt", cutadapt.__version__, "python", sys.version.split()[0])
random.seed(20260903)


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def mutate(s, k):
    """Return s with exactly k substitutions at distinct positions."""
    s = list(s)
    for i in random.sample(range(len(s)), k):
        s[i] = random.choice([c for c in "ACGT" if c != s[i]])
    return "".join(s)


# ---------------------------------------------------------------- Part A
print("\n== A. closed form: int(n * (k / n)) < k, i.e. a full-length match with k errors is rejected")
affected = {}
for k in range(1, 6):
    ns = [n for n in range(1, 301) if int(n * (k / n)) < k]
    affected[k] = ns
    print(f"  k={k}: n in {ns}")

print("\n   partial-length boundaries L <= n where int(L * (k/n)) < floor(L*k/n) (exact rational), n <= 300:")
for k in range(1, 6):
    hits = []
    for n in range(1, 301):
        rate = k / n
        for L in range(1, n + 1):
            exact = (L * k) // n
            if int(L * rate) < exact:
                hits.append((n, L))
    print(f"  k={k}: {len(hits)} (n, L) pairs; first 12: {hits[:12]}")

print("\n   decimal rates as typed on the command line (-e 0.1 etc.), L <= 300:")
for r in ("0.05", "0.1", "0.12", "0.15", "0.2", "0.25", "0.3", "0.29"):
    rate = float(r)
    fr = Fraction(r)
    hits = [L for L in range(1, 301) if int(L * rate) < (fr * L).numerator // (fr * L).denominator]
    print(f"  -e {r}: {len(hits)} affected lengths; first 10: {hits[:10]}")

# ---------------------------------------------------------------- Part B
print("\n== B. shipped adapter classes: adapter of length n, read carries it with exactly k substitutions")
rows = []
for k, n in [(1, 49), (1, 98), (2, 98), (3, 47), (2, 49), (1, 50), (1, 48), (2, 50), (3, 30)]:
    ad = rnd(n)
    found = {}
    for label, cls, mk in [
        ("BackAdapter(-a)", BackAdapter, lambda a, m: rnd(20) + m + rnd(15)),
        ("FrontAdapter(-g)", FrontAdapter, lambda a, m: rnd(15) + m + rnd(20)),
        ("PrefixAdapter(^,indels)", PrefixAdapter, lambda a, m: m + rnd(20)),
        ("SuffixAdapter($,indels)", SuffixAdapter, lambda a, m: rnd(20) + m),
    ]:
        adapter = cls(ad, max_errors=k, min_overlap=3)
        m_k = adapter.match_to(mk(ad, mutate(ad, k)))
        m_k1 = adapter.match_to(mk(ad, mutate(ad, k - 1)))
        found[label] = (m_k is not None, m_k1 is not None)
    p = PrefixAdapter(ad, max_errors=k, indels=False)
    found["PrefixAdapter(^,--no-indels)"] = (
        p.match_to(mutate(ad, k) + rnd(20)) is not None,
        p.match_to(mutate(ad, k - 1) + rnd(20)) is not None,
    )
    rate = BackAdapter(ad, max_errors=k).max_error_rate
    print(f"  k={k} n={n}: rate={rate!r} n*rate={n*rate!r} expected(affected)={n in affected[k]}")
    for label, (fk, fk1) in found.items():
        print(f"      {label:28s} found with k errors: {str(fk):5s}  with k-1 errors: {fk1}")

print("\n   wildcard adapter: 50 nt with one N (49 non-N), -e 1, full-length match with 1 substitution outside the N")
ad = rnd(25) + "N" + rnd(24)
a = BackAdapter(ad, max_errors=1, min_overlap=3)
occ = list(ad)
occ[25] = "A"
occ[3] = "C" if occ[3] != "C" else "G"
read = rnd(10) + "".join(occ) + rnd(10)
print(f"   effective_length={a.effective_length} rate={a.max_error_rate!r} -> match: {a.match_to(read)}")

print("\n   AdapterIndex (demultiplexing path): two 49-nt anchored barcodes, -e 1")
b1, b2 = rnd(49), rnd(49)
idx = IndexedPrefixAdapters([PrefixAdapter(b1, max_errors=1, indels=False), PrefixAdapter(b2, max_errors=1, indels=False)])
print("   index max_k per adapter:", [int(len(x.sequence) * x.max_error_rate) for x in idx._index._adapters])
print("   read = barcode1 with 1 substitution -> ", idx.match_to(mutate(b1, 1) + rnd(30)))
print("   read = barcode1 exact              -> ", idx.match_to(b1 + rnd(30)))

# ---------------------------------------------------------------- Part C
print("\n== C. CLI: 300 reads = 20 nt + 49-nt adapter with exactly 1 substitution + 30 nt; `-e 1` vs `-e 1.0000001` vs `-e 2`")
ad = rnd(49)
with tempfile.TemporaryDirectory() as tmp:
    fq = os.path.join(tmp, "in.fastq")
    with open(fq, "w") as f:
        for i in range(300):
            s = rnd(20) + mutate(ad, 1) + rnd(30)
            f.write(f"@r{i}\n{s}\n+\n{'I' * len(s)}\n")
    for e in ("1", "1.0000001", "2", "0.0204081632653062"):
        out = os.path.join(tmp, f"out{e}.fastq")
        subprocess.run(
            [sys.executable, "-m", "cutadapt", "-e", e, "-a", ad, "-o", out, fq, "--quiet"],
            check=True,
        )
        with open(out) as f:
            lens = [len(line.strip()) for i, line in enumerate(f) if i % 4 == 1]
        trimmed = sum(1 for L in lens if L < 99)
        print(f"   -e {e:20s}: reads trimmed {trimmed}/300 (a trimmed read is 20 nt long: {sum(1 for L in lens if L == 20)})")
