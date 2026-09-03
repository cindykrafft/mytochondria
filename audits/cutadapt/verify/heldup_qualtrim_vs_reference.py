#!/usr/bin/env python3
"""Held-up checks for the quality-based paths, against independent Python ports.

1. quality_trim_index vs a port of BWA's bwa_trim_read (3' end) and its mirror
   (5' end), random quality strings, phred+33 and phred+64, cutoffs 0..40.
2. nextseq_trim_index vs the documented variant (G bases count as cutoff-1).
3. poly_a_trim_index vs the algorithm as described in doc/algorithms.rst
   (suffix with <= 20 % non-A, score +1/-2, max score, shorter wins ties,
   tails < 3 ignored) and the poly-T mirror.
4. expected_errors vs sum(10^(-q/10)), both offsets, and the SCORE_TO_ERROR_RATE table.
5. The predicates' boundary comparisons (>, not >=).
"""
import random
from fractions import Fraction

import cutadapt
from dnaio import SequenceRecord
from cutadapt.qualtrim import quality_trim_index, nextseq_trim_index, poly_a_trim_index, expected_errors
from cutadapt.predicates import TooShort, TooLong, TooManyExpectedErrors, TooManyN

print("cutadapt", cutadapt.__version__)
random.seed(3)


def bwa_back(q, cutoff):
    s, best, stop = 0, 0, len(q)
    for i in reversed(range(len(q))):
        s += cutoff - q[i]
        if s < 0:
            break
        if s > best:
            best, stop = s, i
    return stop


def bwa_front(q, cutoff):
    s, best, start = 0, 0, 0
    for i in range(len(q)):
        s += cutoff - q[i]
        if s < 0:
            break
        if s > best:
            best, start = s, i + 1
    return start


def ref_quality_trim(q, cf, cb):
    start, stop = bwa_front(q, cf), bwa_back(q, cb)
    if start >= stop:
        return 0, 0
    return start, stop


def ref_nextseq(seq, q, cutoff):
    s, best, stop = 0, 0, len(q)
    for i in reversed(range(len(q))):
        qi = cutoff - 1 if seq[i] == "G" else q[i]
        s += cutoff - qi
        if s < 0:
            break
        if s > best:
            best, stop = s, i
    return stop


def ref_poly_a(s):
    n = len(s)
    best_index, best_score = n, 0
    for i in range(n - 1, -1, -1):  # suffix s[i:]
        suf = s[i:]
        non_a = sum(1 for c in suf if c != "A")
        if Fraction(non_a, len(suf)) > Fraction(1, 5):
            continue
        score = (len(suf) - non_a) - 2 * non_a
        if score > best_score:  # strictly greater: shorter suffix wins ties
            best_score, best_index = score, i
    if n - best_index < 3:
        return n
    return best_index


def ref_poly_t(s):
    r = s[::-1].replace("A", "x").replace("T", "A").replace("x", "T")
    return len(s) - ref_poly_a(r)


# 1
bad = 0
n_tests = 0
for base in (33, 64):
    for _ in range(20000):
        n = random.randint(0, 80)
        q = [random.randint(0, 41 if base == 33 else 40) for _ in range(n)]
        qs = "".join(chr(x + base) for x in q)
        cf, cb = random.choice([0, 0, 5, 10, 15, 20, 30, 40]), random.choice([0, 10, 15, 20, 25, 30, 40])
        n_tests += 1
        if quality_trim_index(qs, cf, cb, base) != ref_quality_trim(q, cf, cb):
            bad += 1
print(f"1. quality_trim_index vs BWA port: {n_tests} random cases, mismatches {bad}")

# 2
bad = n_tests = 0
for base in (33, 64):
    for _ in range(20000):
        n = random.randint(0, 80)
        seq = "".join(random.choice("ACGTGGG") for _ in range(n))
        q = [random.randint(0, 40) for _ in range(n)]
        rec = SequenceRecord("r", seq, "".join(chr(x + base) for x in q))
        cutoff = random.choice([10, 15, 20, 25, 30])
        n_tests += 1
        if nextseq_trim_index(rec, cutoff, base) != ref_nextseq(seq, q, cutoff):
            bad += 1
print(f"2. nextseq_trim_index vs port: {n_tests} random cases, mismatches {bad}")

# 3
bad = bad_t = n_tests = 0
for _ in range(30000):
    n = random.randint(0, 40)
    s = "".join(random.choice("ACGT") for _ in range(random.randint(0, 20)))
    tail = "".join(random.choice("AAAAAAAACGT") for _ in range(n))
    s = s + tail
    n_tests += 1
    if poly_a_trim_index(s) != ref_poly_a(s):
        bad += 1
    t = s[::-1].translate(str.maketrans("ACGT", "TGCA"))
    if poly_a_trim_index(t, revcomp=True) != ref_poly_t(t):
        bad_t += 1
print(f"3. poly_a_trim_index vs documented algorithm: {n_tests} cases, poly-A mismatches {bad}, poly-T mismatches {bad_t}")

# 4
worst = 0.0
for base in (33, 64):
    for _ in range(5000):
        n = random.randint(0, 200)
        q = [random.randint(0, 93 if base == 33 else 62) for _ in range(n)]
        got = expected_errors("".join(chr(x + base) for x in q), base)
        exp = sum(10 ** (-x / 10) for x in q)
        if exp:
            worst = max(worst, abs(got - exp) / exp)
        elif got != 0.0:
            worst = max(worst, abs(got))
print(f"4. expected_errors vs sum 10^(-q/10): 10000 random strings, both offsets, worst relative error {worst:.2e}")
tab_worst = max(abs(expected_errors(chr(q + 33)) - 10 ** (-q / 10)) / 10 ** (-q / 10) for q in range(94))
print(f"   SCORE_TO_ERROR_RATE table, phred 0..93: worst relative deviation from 10^(-q/10): {tab_worst:.2e}")
try:
    expected_errors(chr(94 + 33))
    print("   phred 94 accepted (unexpected)")
except ValueError as e:
    print(f"   phred 94: ValueError ({e})")

# 5
r = SequenceRecord("r", "ACGTACGTAC", "IIIIIIIIII")  # length 10, EE = 10 * 1e-4
print(f"5. read of length 10: TooShort(10)={TooShort(10).test(r, None)} TooShort(11)={TooShort(11).test(r, None)} "
      f"TooLong(10)={TooLong(10).test(r, None)} TooLong(9)={TooLong(9).test(r, None)}")
ee = expected_errors(r.qualities)
print(f"   EE={ee!r}: TooManyExpectedErrors(EE)={TooManyExpectedErrors(ee).test(r, None)} "
      f"TooManyExpectedErrors(EE*0.999)={TooManyExpectedErrors(ee * 0.999).test(r, None)}")
rn = SequenceRecord("r", "ACGTNNACGT", "IIIIIIIIII")
print(f"   2 N of 10: TooManyN(2)={TooManyN(2).test(rn, None)} TooManyN(1)={TooManyN(1).test(rn, None)} "
      f"TooManyN(0.2)={TooManyN(0.2).test(rn, None)} TooManyN(0.19)={TooManyN(0.19).test(rn, None)} TooManyN(0)={TooManyN(0).test(rn, None)}")
