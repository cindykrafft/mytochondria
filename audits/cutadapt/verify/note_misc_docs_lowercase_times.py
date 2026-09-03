#!/usr/bin/env python3
"""Small executed checks behind the remaining notes and one withdrawn suspicion.

N3  doc/algorithms.rst:209-222 gives a Python implementation of the poly-A
    algorithm; it iterates `enumerate(range(n))`, so `nuc` is an int and never
    equals "A". Run verbatim, it never trims. The shipped Cython code is right.
N7  --trim-n (NEndTrimmer, modifiers.py:906-907) and --nextseq-trim
    (qualtrim.pyx:107) look for uppercase N / G only; adapter matching upper-cases
    reads, these two do not.
W3  remainder() (adapters.py:1588-1602) composes the untrimmed interval over
    several matches (--times 2 with --action mask/lowercase): executed on a
    5'+3' read, both orders. (The insert must not begin/end with the adapter
    base: a trailing T would join the poly-T adapter under the leftmost rule.)
"""
import cutadapt
from dnaio import SequenceRecord
from cutadapt.qualtrim import poly_a_trim_index, nextseq_trim_index
from cutadapt.modifiers import NEndTrimmer, AdapterCutter, ModificationInfo
from cutadapt.adapters import FrontAdapter, BackAdapter

print("cutadapt", cutadapt.__version__)


def doc_poly_a(s):  # verbatim from doc/algorithms.rst
    n = len(s)
    best_index = n
    best_score = score = errors = 0
    for i, nuc in reversed(list(enumerate(range(n)))):
        if nuc == "A":
            score += 1
        else:
            score -= 2
            errors += 1
        if score > best_score and errors <= 0.2 * (n - i):
            best_index = i
            best_score = score
    return s[:best_index]


s = "CGTACGTACG" + "A" * 12
print(f"N3 doc snippet on {s}: returns {doc_poly_a(s)!r}; shipped poly_a_trim_index -> {s[:poly_a_trim_index(s)]!r}")

r = SequenceRecord("r", "nnACGTACGTNN", "I" * 12)
print(f"N7 --trim-n on {r.sequence}: -> {NEndTrimmer()(r, ModificationInfo(r)).sequence!r} (lowercase n kept)")
rg = SequenceRecord("r", "ACGTACGT" + "g" * 10, "I" * 8 + "#" * 10)
rG = SequenceRecord("r", "ACGTACGT" + "G" * 10, "I" * 8 + "#" * 10)
print(f"N7 --nextseq-trim=20 on ...GGGGGGGGGG (Q2) -> stop {nextseq_trim_index(rG, 20)}; on ...gggggggggg -> stop {nextseq_trim_index(rg, 20)}")

front, back = FrontAdapter("GGGGGGGG", max_errors=0), BackAdapter("TTTTTTTT", max_errors=0)
seq = "GGGGGGGG" + "ACGTACGTACGA" + "TTTTTTTT"
for adapters in ([front, back], [back, front]):
    rec = SequenceRecord("r", seq, "I" * len(seq))
    out = AdapterCutter(adapters, times=2, action="mask")(rec, ModificationInfo(rec))
    print(f"W3 --times 2 --action mask, order {[a.sequence[0] for a in adapters]}: {out.sequence} "
          f"({'ok' if out.sequence == 'N' * 8 + 'ACGTACGTACGA' + 'N' * 8 else 'MISMATCH'})")
    rec = SequenceRecord("r", seq, "I" * len(seq))
    out = AdapterCutter(adapters, times=2, action="lowercase")(rec, ModificationInfo(rec))
    print(f"W3 --times 2 --action lowercase: {out.sequence} ({'ok' if out.sequence == 'g' * 8 + 'ACGTACGTACGA' + 't' * 8 else 'MISMATCH'})")
