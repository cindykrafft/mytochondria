#!/usr/bin/env python3
"""TM2 — MAXINFO's fixed-point normalisation overflows for large target lengths.

MaximumInformationTrimmer scales its two log-score tables to longs with one ratio,
normRatio = max(ratio_length, ratio_quality) (MaximumInformationTrimmer.java:67-68). The
max picks the LARGER ratio, i.e. the one computed for the table with the SMALLER maximum;
the other table is then scaled past Long range, `(long)(array[i] * ratio)` saturates at
Long.MIN_VALUE (`:34`), and `ls + accumQuality` wraps to a large positive score at position 0
(`:94`), so every read is trimmed to one base. calcNormalization also seeds maxVal with
array[0] instead of |array[0]| (`:19`). For targetLength > ~710, exp(targetLength - i - 1)
overflows to Infinity and the length table becomes -Infinity (`:48-50`).

This harness runs the shipped build over a grid of (targetLength, strictness) on
high-quality reads and compares with a double-precision evaluation of the same formula,
then checks typical settings on random reads with realistic qualities (the held-up part).

Usage: python3 tm2_maxinfo_normalisation.py <trimmomatic.jar | build-dir>
"""
import math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_ref as T

build = T.build_from_arg(sys.argv[1])
print("build:", " ".join(build))

def closed_form_boundary():
    """Where does (targetLength-1) * ratio_q exceed Long.MAX_VALUE?  ratio_q = MAX / (maxQ * 2000)
    with maxQ = |log(1 - 10^-0.15)| * s (the code's maxVal skips |array[0]|), so the first
    length-table entry saturates when targetLength - 1 > 2000 * maxQ."""
    maxq1 = abs(math.log(1 - 10 ** (-0.15)))
    return {s: 1 + 2000 * maxq1 * s for s in (0.1, 0.2, 0.3, 0.5, 0.8, 1.0)}

print("\nclosed form: smallest targetLength at which lengthScore[0]*normRatio leaves Long range, per strictness:")
for s, t in closed_form_boundary().items():
    print("   strictness %.1f: targetLength > %.1f" % (s, t))

# ---------------------------------------------------------------- A. grid on Q40 reads of length 300
rng = random.Random(7)
seq = T.rand_seq(rng, 300); q = [40] * 300
targets = [36, 40, 50, 75, 100, 150, 200, 240, 246, 247, 248, 250, 300, 400, 490, 495, 500, 600, 700, 709, 710, 711, 720, 800, 1000]
stricts = [0.1, 0.2, 0.3, 0.5, 0.8, 1.0]
print("\nA. 300-nt all-Q40 read; cell = shipped surviving length / double-precision rule (300 expected everywhere)")
print("   %-8s" % "target" + "".join("%-12s" % ("s=%.1f" % s) for s in stricts))
bad = []
for t in targets:
    row = "   %-8d" % t
    for s in stricts:
        step = "MAXINFO:%d:%s" % (t, s)
        res, log, d = T.run_se(build, [("r", seq, q)], [step])
        got = len(res["r"][0]) if "r" in res else 0
        ref = T.maxinfo_double(seq, q, t, s)
        refl = len(ref[0]) if ref else 0
        row += "%-12s" % ("%d/%d" % (got, refl))
        if got != refl:
            bad.append((t, s, got, refl))
    print(row)
print("   cells where shipped != double-precision rule:", len(bad), "of", len(targets) * len(stricts))
print("   affected (target, strictness) ->", sorted(set((t, s) for t, s, g, r in bad)))

# ---------------------------------------------------------------- B. typical settings on realistic reads (held up?)
def real_read(rng, R):
    seq, quals = [], []
    for i in range(R):
        qq = rng.choice([40, 40, 37, 37, 32, 27]) if i < R * 0.5 else rng.choice([37, 32, 27, 22, 14, 11, 2])
        b = rng.choice("ACGT")
        if rng.random() < 0.005: b = "N"
        seq.append(b); quals.append(qq if b != "N" else 2)
    return "".join(seq), quals

print("\nB. 5,000 reads of 150 nt with an Illumina-like quality profile, typical settings:")
for step in ("MAXINFO:40:0.5", "MAXINFO:35:0.5", "MAXINFO:100:0.2", "MAXINFO:50:0.8", "MAXINFO:36:0.9", "MAXINFO:150:1.0", "MAXINFO:150:0"):
    t, s = int(step.split(":")[1]), float(step.split(":")[2])
    rng = random.Random(hash(step) & 0xffff)
    reads = []
    for k in range(5000):
        sq, qs = real_read(rng, 150); reads.append(("r%d" % k, sq, qs))
    res, log, d = T.run_se(build, reads, [step])
    eq = off1 = diff = dropped = 0
    for name, sq, qs in reads:
        ref = T.maxinfo_double(sq, qs, t, s)
        refl = len(ref[0]) if ref else 0
        got = len(res[name][0]) if name in res else 0
        if got == refl: eq += 1
        elif abs(got - refl) == 1: off1 += 1
        else: diff += 1
        dropped += name not in res
    print("   %-16s shipped == double rule %d/5000, differ by 1 base %d, differ more %d; reads dropped %d | %s" % (step, eq, off1, diff, dropped, T.summary_line(log)))

# ---------------------------------------------------------------- C. the two other paths: target > 710 and strictness 0 with N
print("\nC. targetLength 800, strictness 0.5, 2x300 MiSeq-like reads (300 nt, Q37 until 200 then Q20):")
reads = [("r%d" % k, T.rand_seq(random.Random(k), 300), [37] * 200 + [20] * 100) for k in range(100)]
res, log, d = T.run_se(build, reads, ["MAXINFO:800:0.5"])
lens = sorted(len(v[0]) for v in res.values())
print("   shipped surviving lengths:", (lens[0], lens[-1]) if lens else None, "reads out:", len(res), "|", T.summary_line(log))
refl = [len(T.maxinfo_double(s, q, 800, 0.5)[0]) for _, s, q in reads]
print("   double-precision rule lengths:", (min(refl), max(refl)))
