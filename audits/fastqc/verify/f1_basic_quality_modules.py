"""F1: the modules whose numbers reach papers directly, recomputed from the
input: Basic Statistics (total sequences, %GC, sequence length, mean length),
Per base sequence quality (mean / median / quartiles / 10th / 90th per
position against exact statistics of the qualities written), Per sequence
quality scores (the histogram of per-read mean qualities against the exact
per-read means), Per base sequence content and N content (exact percentages),
Sequence Length Distribution, and the quality-encoding detection for a file
whose qualities are all >= 31.
"""
import random, sys, os, collections, statistics, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(1)
print(f"FastQC {version()}")
d = tmpdir()

# ---- library A: 2,000 reads of 100 bp, per-position quality drawn from a position-dependent set
reads = []; quals_by_pos = collections.defaultdict(list); read_means = []; comp = collections.defaultdict(collections.Counter)
for i in range(2000):
    seq = list(rand_seq(rng, 100))
    if i % 50 == 0:
        for p in (10, 11, 12): seq[p] = "N"
    q = [max(2, min(41, int(rng.gauss(38 - p * 0.15, 4)))) for p in range(100)]
    for p in range(100):
        quals_by_pos[p + 1].append(q[p]); comp[p + 1][seq[p]] += 1
    read_means.append(sum(q) / 100)
    reads.append((f"r{i}", "".join(seq), qstr(q)))
fq = os.path.join(d, "A.fq"); write_fastq(fq, reads)
m = run(fq)
b = basic(m)
gc = sum(c["G"] + c["C"] for c in comp.values()); acgt = sum(c["A"] + c["C"] + c["G"] + c["T"] for c in comp.values())
print(f"   Basic Statistics: {b}")
report("Basic: Total Sequences 2000, Sequence length 100", b["Total Sequences"] == "2000" and b["Sequence length"] == "100")
report(f"Basic: %GC = floor(100*GC/ACGT) = {100 * gc // acgt} (exact {100 * gc / acgt:.3f})", b["%GC"] == str(100 * gc // acgt))

# per base quality: --nogroup so every position is its own row
m2 = run(fq, ["--nogroup"])
rows = m2["Per base sequence quality"]["rows"]
bad = 0
for r in rows:
    pos = int(r[0]); qs = quals_by_pos[pos]; cnt = collections.Counter(qs)
    exp = dict(mean=statistics.mean(qs), median=fastqc_percentile(cnt, 50), lq=fastqc_percentile(cnt, 25), uq=fastqc_percentile(cnt, 75), p10=fastqc_percentile(cnt, 10), p90=fastqc_percentile(cnt, 90))
    got = dict(mean=float(r[1]), median=float(r[2]), lq=float(r[3]), uq=float(r[4]), p10=float(r[5]), p90=float(r[6]))
    if abs(got["mean"] - exp["mean"]) > 1e-9 or any(got[k] != exp[k] for k in ("median", "lq", "uq", "p10", "p90")):
        bad += 1
        if bad <= 3: print(f"   position {pos}: got {got} expected {exp}")
report(f"Per base sequence quality (--nogroup): mean exact and percentiles equal the port of QualityCount.getPercentile on {len(rows) - bad}/{len(rows)} positions", bad == 0)
# the port's percentile is the floor(p*N)-th smallest value; compare with the conventional (nearest-rank, ceil) definition
diffs = 0
for r in rows:
    pos = int(r[0]); qs = sorted(quals_by_pos[pos]); n = len(qs)
    conv = {50: qs[-(-50 * n // 100) - 1], 25: qs[-(-25 * n // 100) - 1], 10: qs[-(-10 * n // 100) - 1]}
    if conv[50] != float(r[2]) or conv[25] != float(r[3]) or conv[10] != float(r[5]): diffs += 1
print(f"   positions where FastQC's percentile (floor(pN)-th value) differs from the nearest-rank (ceil(pN)-th) value: {diffs}/{len(rows)} (N = 2000 per position)")

# per sequence quality: histogram of per-read means
rows = m["Per sequence quality scores"]["rows"]
hist = {int(r[0]): float(r[1]) for r in rows}
exact_floor = collections.Counter(int(x) for x in read_means)            # FastQC: integer division of the ASCII sum
exact_round = collections.Counter(int(math.floor(x + 0.5)) for x in read_means)   # Java Math.round: half up
ok_floor = all(hist.get(k, 0) == v for k, v in exact_floor.items()) and sum(hist.values()) == 2000
ok_round = all(hist.get(k, 0) == v for k, v in exact_round.items())
print(f"   per-read mean qualities: exact mean of means {statistics.mean(read_means):.3f}; FastQC histogram mean {sum(k * v for k, v in hist.items()) / sum(hist.values()):.3f}")
report("Per sequence quality scores: histogram equals the floor of each read's mean quality", ok_floor)
report("Per sequence quality scores: histogram equals each read's mean quality rounded to the nearest integer", ok_round,
       "" if ok_round else "(each read's mean is truncated toward zero: the histogram sits about 0.5 below the true means)")

# per base sequence content and N content (--nogroup)
rows = m2["Per base sequence content"]["rows"]; bad = 0
for r in rows:
    pos = int(r[0]); c = comp[pos]; tot = c["A"] + c["C"] + c["G"] + c["T"]
    exp = [100 * c[x] / tot for x in "GATC"]
    if any(abs(float(r[i + 1]) - exp[i]) > 1e-9 for i in range(4)): bad += 1
report(f"Per base sequence content (--nogroup): %G/%A/%T/%C exact (N excluded from the denominator) on {len(rows) - bad}/{len(rows)}", bad == 0)
rows = m2["Per base N content"]["rows"]; bad = 0
for r in rows:
    pos = int(r[0]); c = comp[pos]; tot = sum(c.values())
    if abs(float(r[1]) - 100 * c["N"] / tot) > 1e-9: bad += 1
report(f"Per base N content (--nogroup): exact on {len(rows) - bad}/{len(rows)}", bad == 0)

# grouped rows (default grouping): the group mean is the unweighted mean of the per-position means, percentiles the mean of per-position percentiles over positions with > 100 observations
rows = m["Per base sequence quality"]["rows"]
groups = base_groups(100)
report(f"Per base sequence quality (default grouping): {len(rows)} rows, labels match the port of makeLinearBaseGroups", [r[0] for r in rows] == [f"{a}-{b}" if a != b else str(a) for a, b in groups])
bad = 0
for r, (a, bb) in zip(rows, groups):
    means = [statistics.mean(quals_by_pos[p]) for p in range(a, bb + 1)]
    meds = [fastqc_percentile(collections.Counter(quals_by_pos[p]), 50) for p in range(a, bb + 1)]
    if abs(float(r[1]) - statistics.mean(means)) > 1e-9 or abs(float(r[2]) - statistics.mean(meds)) > 1e-9: bad += 1
report("Per base sequence quality (default grouping): group mean = mean of per-position means, group median = mean of per-position medians", bad == 0)

# ---- library B: variable lengths (trimmed reads) 30-120 bp, lengths known
reads = []; lens = collections.Counter()
for i in range(3000):
    L = rng.choice([30, 50, 75, 100, 101, 110, 120]) if i % 7 else 120
    lens[L] += 1
    reads.append((f"v{i}", rand_seq(rng, L), qstr([36] * L)))
fq = os.path.join(d, "B.fq"); write_fastq(fq, reads)
m = run(fq); b = basic(m)
total = sum(lens.values()); tb = sum(L * n for L, n in lens.items())
srt = sorted(L for L, n in lens.items() for _ in range(n)); median_up = srt[total // 2]
print(f"   Basic Statistics (variable lengths): {b}")
report(f"Basic: Sequence length '{min(lens)}-{max(lens)}', Mean Length floor({tb}/{total}) = {tb // total}, Median Length {median_up}",
       b["Sequence length"] == f"{min(lens)}-{max(lens)}" and b.get("Mean Length", str(tb // total)) == str(tb // total) and b.get("Median Length", str(median_up)) == str(median_up))
rows = m["Sequence Length Distribution"]["rows"]
got = {}
for r in rows:
    if "-" in r[0]:
        lo, hi = map(int, r[0].split("-"))
    else:
        lo = hi = int(r[0])
    got[(lo, hi)] = float(r[1])
exp_ok = all(abs(v - sum(n for L, n in lens.items() if lo <= L <= hi)) < 1e-9 for (lo, hi), v in got.items()) and abs(sum(got.values()) - total) < 1e-9
report(f"Sequence Length Distribution: {len(rows)} bins sum to {total} and each bin equals the count of reads in its range", exp_ok)

# ---- library C: every quality >= 31 (chars >= '@'): which encoding is reported?
reads = [(f"h{i}", rand_seq(rng, 50), qstr([rng.choice([31, 33, 36, 37]) for _ in range(50)])) for i in range(500)]
fq = os.path.join(d, "C.fq"); write_fastq(fq, reads)
m = run(fq); b = basic(m)
rows = m["Per base sequence quality"]["rows"]
print(f"   all qualities in 31-37 (Phred+33, chars '@'..'F'): Encoding reported '{b['Encoding']}', per-base mean at position 1 = {rows[0][1]} (true mean about 34.3)")
report("Encoding: a Phred+33 file whose lowest quality is 31 is reported as Sanger / Illumina 1.9", b["Encoding"].startswith("Sanger"),
       "" if b["Encoding"].startswith("Sanger") else "(the lowest character decides: '@' (64) and above is taken as an offset-64 encoding, so every quality is reported 31 too low)")
