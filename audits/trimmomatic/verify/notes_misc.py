#!/usr/bin/env python3
"""Notes N1-N7 executed on the shipped jar (design choices and limits, not wrong
numbers):

N1  MAXINFO on a read longer than 1,000 nt: the length-score table has 1,000
    entries (LONGEST_READ), so the step throws ArrayIndexOutOfBoundsException.
N2  N bases are scored as quality 0 by every quality step regardless of the
    stored quality character (getQualityAsInteger(true)).
N3  automatic Phred detection needs at least one quality character in 33-58 or
    80-104; data whose qualities are all Q26-Q46 (phred33) abort with
    "Unable to detect quality encoding" even though only phred33 can explain them.
N4  TRAILING never examines base 0: a read whose only base above the threshold is
    its first base is dropped instead of trimmed to 1 nt (the project's own test
    documents this).
N5  HEADCROP:n / TAILCROP:n drop a read of exactly n bases (nothing left) - fine -
    and SLIDINGWINDOW drops any read shorter than the window outright.
N6  SLIDINGWINDOW keeps the read to the end of the last passing window, then strips
    trailing bases below the per-base threshold; a literal reading of the README
    ("cut once the average falls below") would cut at the start of the failing
    window. Executed on the held-up harness; here one example.
N7  ILLUMINACLIP simple mode scores an alignment by a run-merging 'maximum range'
    heuristic rather than the plain sum the README describes; one example each way.

Usage: python3 notes_misc.py <trimmomatic.jar | build dir>
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trimmomatic_ref as R

target = sys.argv[1]
tmp = os.path.join(os.environ.get("TMPDIR", "/tmp"), "trimmo_notes_%d" % os.getpid())
os.makedirs(tmp, exist_ok=True)

print("N1: MAXINFO:40:0.8 on reads of 999, 1000 and 1001 nt")
for n in (999, 1000, 1001):
    recs = [("r", "ACGT" * (n // 4) + "A" * (n % 4), [35] * n)]
    try:
        out, log = R.run_se(target, recs, ["MAXINFO:40:0.8"])
        print("  %4d nt: kept %d nt" % (n, len(out[0][1])))
    except RuntimeError as e:
        msg = [l for l in str(e).splitlines() if "Exception" in l]
        print("  %4d nt: FAILED - %s" % (n, msg[0].strip() if msg else str(e).splitlines()[-1]))

print("\nN2: N bases scored as Q0. Read of 50 nt, all Q35, with Ns at positions 45-49 carrying quality character 'I' (Q40)")
seq = "ACGT" * 11 + "A" + "NNNNN"
recs = [("r", seq, [35] * 45 + [40] * 5)]
for step in ("TRAILING:20", "SLIDINGWINDOW:4:20", "AVGQUAL:35", "MAXINFO:50:0.9"):
    out, _ = R.run_se(target, recs, [step])
    print("  %-20s -> %s" % (step, "%d nt" % len(out[0][1]) if out else "dropped"))

print("\nN3: automatic Phred detection on 100 reads whose qualities are all Q30-41 (chars '?'..'J')")
recs = [("r%d" % i, "ACGT" * 25, [30 + (i + j) % 12 for j in range(100)]) for i in range(100)]
try:
    out, log = R.run_se(target, recs, ["MINLEN:1"], autodetect=True)
    print("  detected: %s" % [l for l in log.splitlines() if "detected" in l])
except RuntimeError as e:
    print("  %s" % [l for l in str(e).splitlines() if "Unable" in l][0])
recs2 = [("r%d" % i, "ACGT" * 25, [26 + (i + j) % 21 for j in range(100)]) for i in range(100)]
try:
    out, log = R.run_se(target, recs2, ["MINLEN:1"], autodetect=True)
    print("  Q26-46: detected: %s" % [l for l in log.splitlines() if "detected" in l])
except RuntimeError as e:
    print("  Q26-46 (chars 59-79, impossible as phred64): %s" % [l for l in str(e).splitlines() if "Unable" in l][0])
recs3 = [("r%d" % i, "ACGT" * 25, [25 + (i + j) % 20 for j in range(100)]) for i in range(100)]
out, log = R.run_se(target, recs3, ["MINLEN:1"], autodetect=True)
print("  Q25-44 (one char in 33-58): %s" % [l.strip() for l in log.splitlines() if "detected" in l])

print("\nN4: TRAILING:20 on '?' + 20 x '+' (base 0 is Q30, the rest Q10)")
out, _ = R.run_se(target, [("r", "A" * 21, [30] + [10] * 20)], ["TRAILING:20"])
print("  -> %s (README: 1 nt); LEADING:20 on the mirror image:" % ("%d nt" % len(out[0][1]) if out else "dropped"), end=" ")
out, _ = R.run_se(target, [("r", "A" * 21, [10] * 20 + [30])], ["LEADING:20"])
print("%s" % ("%d nt" % len(out[0][1]) if out else "dropped"))

print("\nN5: HEADCROP:10 on a 10 nt read and SLIDINGWINDOW:4:20 on 1-3 nt reads of Q40")
out, _ = R.run_se(target, [("r", "A" * 10, [40] * 10)], ["HEADCROP:10"])
print("  HEADCROP:10 on 10 nt: %s" % ("%d nt" % len(out[0][1]) if out else "dropped"))
out, _ = R.run_se(target, [("r%d" % n, "A" * n, [40] * n) for n in (1, 2, 3, 4)], ["SLIDINGWINDOW:4:20"])
print("  SLIDINGWINDOW:4:20 on 1,2,3,4 nt of Q40: kept %s" % [len(s) for _, s, _ in out])

print("\nN6: SLIDINGWINDOW:4:20 on Q [30,30,30,30,30,30,10,10,10,10,30,30]")
q = [30, 30, 30, 30, 30, 30, 10, 10, 10, 10, 30, 30]
out, _ = R.run_se(target, [("r", "A" * 12, q)], ["SLIDINGWINDOW:4:20"])
print("  jar keeps %d nt; first window below 20 starts at base 5 (avg 25 -> base 4: [30,30,10,10] = 20 passes; base 5: [30,10,10,10] = 15 fails)"
      % len(out[0][1]))
print("  as coded: keep to the end of window 4 (8 nt), then strip trailing bases < 20 -> 6 nt; literal README: cut at base 5 -> 5 nt")

print("\nN7: ILLUMINACLIP simple mode, maximum-range score vs plain sum; adapter 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC' (33 nt), threshold 10")
IDX = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"
fa = os.path.join(tmp, "a.fa"); open(fa, "w").write(">A\n%s\n" % IDX)
# (a) 20 adapter bases then 13 mismatching bases at Q30 at the read end: sum = 20*0.602 - 13*3 < 10, max range = 12.0 -> clipped
ins = "ACGT" * 10
tail = "".join({"A": "C", "C": "G", "G": "T", "T": "A"}[c] for c in IDX[20:])
seq = ins + IDX[:20] + tail; q = [30] * len(seq)
out, _ = R.run_se(target, [("a", seq, q)], ["ILLUMINACLIP:%s:2:30:10" % fa])
print("  (a) 20 matching adapter bases followed by 13 mismatching Q30 bases: plain sum %.1f, max-range %.1f -> jar %s"
      % (20 * R.LOG10_4 - 13 * 3.0, 20 * R.LOG10_4, "clipped to %d" % len(out[0][1]) if out and len(out[0][1]) < len(seq) else "not clipped"))
# (b) 11 matches, Q35 mismatch, 3 matches, Q35 mismatch, 17 matches: plain sum = 31*0.602 - 7 = 11.7; the run-merging
#     heuristic cannot absorb either -3.5 (its 3-match neighbour is only 1.8), so max-range = 17*0.602 = 10.2:
#     threshold 10 clips under both rules, threshold 11 clips by the README's sum but not as coded
ad = list(IDX); ad[11] = {"A": "C", "C": "G", "G": "T", "T": "A"}[ad[11]]; ad[15] = {"A": "C", "C": "G", "G": "T", "T": "A"}[ad[15]]
seq = ins + "".join(ad); q = [35] * len(seq)
for thr in (10, 11):
    out, _ = R.run_se(target, [("b", seq, q)], ["ILLUMINACLIP:%s:2:30:%d" % (fa, thr)])
    print("  (b) two Q35 mismatches at adapter positions 11 and 15: plain sum %.1f, max-range %.1f, threshold %d -> jar %s"
          % (31 * R.LOG10_4 - 7.0, 17 * R.LOG10_4, thr, "clipped to %d" % len(out[0][1]) if out and len(out[0][1]) < len(seq) else "not clipped"))
