#!/usr/bin/env python3
"""Held-up checks for the aligner and the k-mer prefilter, on random data.

For every adapter type (3', 5', anywhere, non-internal, anchored) and random
adapters/reads:
  P1  reported errors == Levenshtein distance of the two aligned substrings
      (independent DP), and == Hamming distance with --no-indels
  P2  errors / (aligned adapter length minus N) <= max error rate (exact rational)
  P3  aligned adapter length >= min_overlap; anchored types align the full adapter
  P4  a planted exact full-length occurrence is either returned (0 errors, full
      score) or an acceptable occurrence further LEFT is returned instead
      (the documented leftmost-occurrence rule, doc/algorithms.rst "changes in
      Cutadapt 4": an earlier occurrence within the error tolerance wins even if
      a later one has fewer errors). Counted separately: how often the earlier,
      worse occurrence won.
  P6  never both a reference prefix and a query prefix skipped (docstring:
      "at least one of query_start and reference_start is zero")
  P5  the k-mer prefilter never suppresses a match the aligner would return:
      adapter.match_to(read) == RemoveXMatch(*adapter.aligner.locate(read))
      (this is the only place a false negative could enter silently)
Randomness: seed 5; ~100k alignments.
"""
import random
from fractions import Fraction

import cutadapt
from cutadapt.adapters import (
    BackAdapter, FrontAdapter, AnywhereAdapter, NonInternalBackAdapter, NonInternalFrontAdapter,
    PrefixAdapter, SuffixAdapter,
)

print("cutadapt", cutadapt.__version__)
random.seed(5)
ILLUMINA = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"
SMALLRNA = "TGGAATTCTCGGGTGCCAAGG"


def rnd(n, alphabet="ACGT"):
    return "".join(random.choice(alphabet) for _ in range(n))


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def edits(s, k, indels=True):
    for _ in range(k):
        i = random.randrange(len(s))
        kind = random.choice(["sub", "ins", "del"] if indels and len(s) > 4 else ["sub"])
        if kind == "sub":
            s = s[:i] + random.choice([c for c in "ACGT" if c != s[i]]) + s[i + 1 :]
        elif kind == "ins":
            s = s[:i] + random.choice("ACGT") + s[i:]
        else:
            s = s[:i] + s[i + 1 :]
    return s


TYPES = [
    ("3' (-a)", BackAdapter, lambda ad, occ: (rnd(random.randint(0, 40)), occ, rnd(random.randint(0, 30)))),
    ("5' (-g)", FrontAdapter, lambda ad, occ: (rnd(random.randint(0, 30)), occ, rnd(random.randint(0, 40)))),
    ("anywhere (-b)", AnywhereAdapter, lambda ad, occ: (rnd(random.randint(0, 30)), occ, rnd(random.randint(0, 30)))),
    ("non-internal 3' (ADAPTERX)", NonInternalBackAdapter, lambda ad, occ: (rnd(random.randint(0, 40)), occ, "")),
    ("non-internal 5' (XADAPTER)", NonInternalFrontAdapter, lambda ad, occ: ("", occ, rnd(random.randint(0, 40)))),
    ("anchored 5' (^ADAPTER)", PrefixAdapter, lambda ad, occ: ("", occ, rnd(random.randint(0, 40)))),
    ("anchored 3' (ADAPTER$)", SuffixAdapter, lambda ad, occ: (rnd(random.randint(0, 40)), occ, "")),
]

for indels in (True, False):
    print(f"\n== indels={indels}")
    for label, cls, build in TYPES:
        p1 = p2 = p3 = p4 = p5 = p6 = earlier = 0
        n_match = n_total = n_planted = 0
        for trial in range(2500):
            ad = random.choice([ILLUMINA, SMALLRNA, rnd(random.randint(5, 25)), rnd(random.randint(8, 20), "ACGTN")])
            if ad.count("N") == len(ad):
                continue
            rate = random.choice([0.1, 0.1, 0.2, 0.25, 1, 2])
            kwargs = dict(max_errors=rate, min_overlap=random.choice([1, 3, 5]), indels=indels)
            if cls in (PrefixAdapter, SuffixAdapter):
                kwargs.pop("min_overlap")
            adapter = cls(ad, **kwargs)
            eff = adapter.effective_length
            max_k = int(eff * adapter.max_error_rate)
            planted = random.random() < 0.6
            if planted:
                k = random.randint(0, max_k)
                occ = edits(ad.replace("N", random.choice("ACGT")), k, indels)
                pre, occ, post = build(ad, occ)
                read = pre + occ + post
            else:
                read = rnd(random.randint(0, 80))
                k = None
            n_total += 1
            m = adapter.match_to(read)
            # P5: prefilter equivalence
            raw = adapter.aligner.locate(read.upper())
            if (m is None) != (raw is None) or (m is not None and (m.astart, m.astop, m.rstart, m.rstop, m.score, m.errors) != tuple(raw)):
                p5 += 1
            if m is None:
                continue
            n_match += 1
            a_sub = ad[m.astart : m.astop]
            r_sub = read[m.rstart : m.rstop]
            if "N" in a_sub:
                d = None  # wildcard columns: distance not defined by plain Levenshtein
            elif indels:
                d = lev(a_sub, r_sub)
            else:
                d = None if len(a_sub) != len(r_sub) else sum(x != y for x, y in zip(a_sub, r_sub))
                if len(a_sub) != len(r_sub):
                    p1 += 1
            if d is not None and d != m.errors:
                p1 += 1
            eff_len = m.length - a_sub.count("N")
            if eff_len and Fraction(m.errors, eff_len) > Fraction(adapter.max_error_rate).limit_denominator(10**6):
                p2 += 1
            if m.length < adapter.min_overlap or (cls in (PrefixAdapter, SuffixAdapter) and m.length != len(ad)):
                p3 += 1
            if m.astart != 0 and m.rstart != 0:
                p6 += 1
            if planted and k == 0:
                n_planted += 1
                if m.rstart < len(pre) and not (m.errors == 0 and m.score == len(ad)):
                    earlier += 1
                elif not (m.errors == 0 and m.score == len(ad) and m.rstart <= len(pre)):
                    p4 += 1
        print(f"  {label:28s} n={n_total:5d} matches={n_match:5d} exact-planted={n_planted:4d} | "
              f"P1 errors!=edit-dist: {p1}  P2 rate exceeded: {p2}  P3 overlap/anchor: {p3}  "
              f"P4 planted exact lost: {p4} (earlier worse occurrence won: {earlier})  "
              f"P5 prefilter != aligner: {p5}  P6 both prefixes skipped: {p6}")
