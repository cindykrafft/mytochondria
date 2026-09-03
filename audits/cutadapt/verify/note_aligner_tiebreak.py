#!/usr/bin/env python3
"""NOTE: the Aligner docstring (_align.pyx:146-154) says that among alignments
with equal score the one with fewer errors is chosen, then the leftmost. The
implementation (_align.pyx:548-552, 590-594) only replaces the current best on
a strictly higher score, i.e. ties go to the leftmost occurrence regardless of
errors. Same criterion as doc/algorithms.rst ("leftmost ... even if a later
match has fewer errors"), so the docstring is what is out of date.
"""
import cutadapt
from cutadapt.adapters import BackAdapter, FrontAdapter

print("cutadapt", cutadapt.__version__)
ad = "ACGTACGTAC"  # 10 nt
# internal full-length occurrence with 1 mismatch (score 9-1 = 8, errors 1),
# then a partial exact occurrence of 8 nt at the read end (score 8, errors 0)
read = "TTTTT" + "ACGTACGTAG" + "TTTTTTTTTT" + "ACGTACGT"
m = BackAdapter(ad, max_errors=0.2, min_overlap=3).match_to(read)
print(f"3' adapter {ad}, read {read}")
print(f"   candidates: internal 1-mismatch (rstart 5, score 8, errors 1) vs terminal exact 8-mer (rstart 25, score 8, errors 0)")
print(f"   chosen: rstart={m.rstart} rstop={m.rstop} score={m.score} errors={m.errors} -> "
      f"{'leftmost (more errors)' if m.rstart == 5 else 'fewest errors'}")
# mirror for 5' adapters: an adapter SUFFIX of 8 nt at the read start (score 8, errors 0),
# then an internal full-length occurrence with 1 mismatch (score 8, errors 1)
read = ad[2:] + "TTTTTTTTTT" + "TCGTACGTAC" + "TTTTT"
m = FrontAdapter(ad, max_errors=0.2, min_overlap=3).match_to(read)
print(f"5' adapter, read {read}: chosen rstart={m.rstart} rstop={m.rstop} score={m.score} errors={m.errors} -> "
      f"{'leftmost (partial exact 8-mer, fewer errors)' if m.rstart == 0 else 'internal 1-mismatch occurrence'}")
