#!/usr/bin/env python3
"""Version scope of TC1 through the command line only, on any Trimmomatic build.

Usage: python3 version_scope_cli.py <trimmomatic.jar | build dir> [label]

Runs the Part A pair of tc1_palindrome_int_division.py (50 nt reads, 40 nt
insert, six mismatches in read 2 at positions 0,2,37,39,42,45) three times:
  Q9  mismatches: README score 27.1 (< 30: nothing to clip); coded 32.5 -> clipped
  Q10 mismatches: both 26.5 -> nothing to clip (sanity: the geometry is right)
  no mismatches : 36.1 -> clipped to 40 nt / read 2 dropped (positive control)
A version is AFFECTED when the Q9 case is clipped while the Q10 case is not.
Also runs one SLIDINGWINDOW / TRAILING sentinel so the old builds are seen to
behave like master on the held-up paths.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trimmomatic_ref as R

target = sys.argv[1]
label = sys.argv[2] if len(sys.argv) > 2 else target
tmp = os.path.join(os.environ.get("TMPDIR", "/tmp"), "trimmo_vs_%d" % os.getpid())
os.makedirs(tmp, exist_ok=True)
P1 = "TACACTCTTTCCCTACACGACGCTCTTCCGATCT"; P2 = "GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT"
fa = os.path.join(tmp, "TruSeq3-PE-2.fa")
with open(fa, "w") as fh:
    for n, s in ((">PrefixPE/1", P1), (">PrefixPE/2", P2), (">PE1", P1), (">PE1_rc", R.rc(P1)), (">PE2", P2), (">PE2_rc", R.rc(P2))):
        fh.write("%s\n%s\n" % (n, s))
STEP = "ILLUMINACLIP:%s:2:30:10" % fa

R1 = "CCGTAATGCCTTTCCCTAACAGAGTTTTTCGAACTCGTGTAGATCGGAAG"
R2 = "CCCCGAGTTCGAAAAACTCTGTTAGGGAAAGGCATTAGGTAGCTCTGAAG"   # six mismatches vs the perfect read-through mate
MM = [0, 2, 37, 39, 42, 45]
R2_PERFECT = list(R2)
for p in MM:
    R2_PERFECT[p] = {"A": "T", "C": "A", "G": "C", "T": "G"}[R2_PERFECT[p]]
R2_PERFECT = "".join(R2_PERFECT)

print("== %s" % label)
res = {}
for case, r2, qmm in (("Q9", R2, 9), ("Q10", R2, 10), ("perfect", R2_PERFECT, 35)):
    q1 = [35] * 50; q2 = [35] * 50
    for p in MM:
        q2[p] = qmm
    out, log = R.run_pe(target, [("p", R1, q1)], [("p", r2, q2)], [STEP])
    l1 = {n: len(s) for n, s, _ in out["1P"] + out["1U"]}.get("p")
    l2 = {n: len(s) for n, s, _ in out["2P"] + out["2U"]}.get("p")
    res[case] = (l1, l2)
    print("  %-8s read1 %-8s read2 %s" % (case + ":", "%d nt" % l1 if l1 else "dropped", "%d nt" % l2 if l2 else "dropped"))
affected = res["Q9"] == (40, None) and res["Q10"] == (50, 50) and res["perfect"] == (40, None)
print("  TC1 (integer Q/10 penalty in palindrome mode): %s" % ("AFFECTED" if affected else ("not affected" if res["Q9"] == (50, 50) and res["perfect"] == (40, None) else "INCONCLUSIVE %s" % res)))

# sentinels on the held-up paths
q = [30, 30, 30, 30, 30, 30, 10, 10, 10, 10, 30, 30]
out, _ = R.run_se(target, [("s", "A" * 12, q)], ["SLIDINGWINDOW:4:20"])
sw = len(out[0][1]) if out else None
out, _ = R.run_se(target, [("t", "A" * 21, [30] + [10] * 20)], ["TRAILING:20"])
tr = len(out[0][1]) if out else None
out, _ = R.run_se(target, [("m", "ACGT" * 25, [35] * 60 + [8] * 40)], ["MAXINFO:40:0.8"])
mi = len(out[0][1]) if out else None
print("  sentinels: SLIDINGWINDOW:4:20 keeps %s nt (master 6); TRAILING:20 first-base-only read -> %s (master dropped); MAXINFO:40:0.8 keeps %s nt"
      % (sw, "%d nt" % tr if tr else "dropped", mi))
