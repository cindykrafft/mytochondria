"""F2: Per sequence GC content and Sequence Duplication Levels recomputed.

GC: a port of GCModel (each read's GC count is spread over the percentage
bins that a count of that read length can claim), of the modal-GC / standard
deviation estimate and of the normal "theoretical distribution" and its
deviation percentage; then the read-length truncation: the module uses only
the first 100 bases of a 101-199-bp read (first 200 of 200-999, first
multiple of 1000 beyond), so a 150-bp library whose last 50 bases are poly-G
(the 2-colour artefact) gets the GC distribution of its first 100 bases.

Duplication: libraries with known duplication structure below and above the
100,000-unique-sequence tracking limit, compared with the exact
"percent of sequences remaining if deduplicated" and level histogram.
"""
import random, sys, os, collections, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(2)
print(f"FastQC {version()}")
d = tmpdir()

def gc_model_bins(L):
    claiming = [0] * 101; models = {}
    for pos in range(L + 1):
        lo = max(0.0, min(L, pos - 0.5)); hi = max(0.0, min(L, pos + 0.5))
        lp = int(math.floor(lo * 100 / L + 0.5)); hp = int(math.floor(hi * 100 / L + 0.5))   # Math.round
        for p in range(lp, hp + 1): claiming[p] += 1
    for pos in range(L + 1):
        lo = max(0.0, min(L, pos - 0.5)); hi = max(0.0, min(L, pos + 0.5))
        lp = int(math.floor(lo * 100 / L + 0.5)); hp = int(math.floor(hi * 100 / L + 0.5))
        models[pos] = [(p, 1.0 / claiming[p]) for p in range(lp, hp + 1)]
    return models

def gc_port(seqs):
    dist = [0.0] * 101; cache = {}
    for s in seqs:
        L = len(s)
        if L > 1000: s = s[:(L // 1000) * 1000]
        elif L > 100: s = s[:(L // 100) * 100]
        L = len(s)
        if L == 0: continue
        if L not in cache: cache[L] = gc_model_bins(L)
        for p, inc in cache[L][sum(1 for b in s if b in "GC")]:
            dist[p] += inc
    total = sum(dist)
    first_mode = max(range(101), key=lambda i: (dist[i], -i))
    mode = 0.0; dups = 0; fell_top = True; fell_bottom = True
    for i in range(first_mode, 101):
        if dist[i] > dist[first_mode] - dist[first_mode] / 10: mode += i; dups += 1
        else: fell_top = False; break
    for i in range(first_mode - 1, -1, -1):
        if dist[i] > dist[first_mode] - dist[first_mode] / 10: mode += i; dups += 1
        else: fell_bottom = False; break
    mode = first_mode if (fell_bottom or fell_top) else mode / dups
    sd = math.sqrt(sum((i - mode) ** 2 * dist[i] for i in range(101)) / (total - 1))
    theo = [total * math.exp(-((i - mode) ** 2) / (2 * sd * sd)) / math.sqrt(2 * math.pi * sd * sd) for i in range(101)]
    dev = 100 * sum(abs(theo[i] - dist[i]) for i in range(101)) / total
    return dist, dev

def status_from(dev): return "fail" if dev > 30 else "warn" if dev > 15 else "pass"

# ---- GC on 100-bp reads with GC ~ N(0.45, 0.06) (read-level GC drawn, bases placed at random)
def make_reads(n, L, gc_mean, gc_sd, tail=""):
    out = []
    for i in range(n):
        g = min(1, max(0, rng.gauss(gc_mean, gc_sd)))
        s = "".join(rng.choice("GC") if rng.random() < g else rng.choice("AT") for _ in range(L))
        out.append((f"g{i}", s + tail, qstr([36] * (L + len(tail)))))
    return out

reads = make_reads(4000, 100, 0.45, 0.06)
fq = os.path.join(d, "gc100.fq"); write_fastq(fq, reads); m = run(fq)
rows = m["Per sequence GC content"]["rows"]; got = [float(r[1]) for r in rows]
dist, dev = gc_port([s for _, s, _ in reads])
report(f"GC content, 100-bp reads: the 101-bin distribution equals the port of GCModel (max abs diff {max(abs(a - b) for a, b in zip(got, dist)):.2e}); status {m['Per sequence GC content']['status']} vs port deviation {dev:.2f} % -> {status_from(dev)}",
       max(abs(a - b) for a, b in zip(got, dist)) < 1e-6 and m["Per sequence GC content"]["status"] == status_from(dev))

# ---- 150-bp reads: whole-read GC vs the first 100 bases
reads = make_reads(4000, 100, 0.45, 0.06, tail="G" * 50)   # 150-bp reads, last 50 bases G
fq = os.path.join(d, "gc150.fq"); write_fastq(fq, reads); m = run(fq)
rows = m["Per sequence GC content"]["rows"]; got = [float(r[1]) for r in rows]
mean_got = sum(i * v for i, v in enumerate(got)) / sum(got)
true_gc = [100 * sum(1 for b in s if b in "GC") / len(s) for _, s, _ in reads]
first100 = [100 * sum(1 for b in s[:100] if b in "GC") / 100 for _, s, _ in reads]
print(f"   150-bp reads with a 50-base poly-G tail: mean whole-read GC {sum(true_gc) / len(true_gc):.1f} %, mean GC of the first 100 bases {sum(first100) / len(first100):.1f} %, FastQC distribution mean {mean_got:.1f} %; Basic Statistics %GC {basic(m)['%GC']}")
report("GC content, 150-bp reads: the distribution reflects the whole read (documentation: 'across the whole length of each sequence')", abs(mean_got - sum(true_gc) / len(true_gc)) < 1.0,
       "" if abs(mean_got - sum(true_gc) / len(true_gc)) < 1.0 else "(only the first 100 bases of a 101-199-bp read enter the module)")
dist, dev = gc_port([s for _, s, _ in reads])
report("GC content, 150-bp reads: matches the port that truncates to the first 100 bases", max(abs(a - b) for a, b in zip(got, dist)) < 1e-6)

# ---- duplication
def dup_truth(seqs):
    c = collections.Counter(s[:50] for s in seqs)
    n = len(seqs); dedup = len(c)
    levels = collections.Counter()
    for s, k in c.items():
        slot = min(k, 10) if k <= 10 else (">10" if k <= 50 else ">50" if k <= 100 else ">100" if k <= 500 else ">500" if k <= 1000 else ">1k" if k <= 5000 else ">5k" if k <= 10000 else ">10k")
        levels[str(slot) if isinstance(slot, int) else slot] += k
    return 100.0 * dedup / n, {k: 100.0 * v / n for k, v in levels.items()}

def dup_lib(n_unique, dup_spec, L=60):
    """dup_spec: list of (copies, number_of_sequences)."""
    seqs = [rand_seq(rng, L) for _ in range(n_unique)]
    for copies, nseq in dup_spec:
        for _ in range(nseq):
            s = rand_seq(rng, L); seqs += [s] * copies
    rng.shuffle(seqs)
    return seqs

for label, seqs in (("30k unique + 5k x2 + 1k x5 + 20 x200 (under the 100k limit)", dup_lib(30000, [(2, 5000), (5, 1000), (200, 20)])),
                    ("250k unique + 20k x2 + 5k x5 + 50 x500 (over the 100k limit)", dup_lib(250000, [(2, 20000), (5, 5000), (500, 50)])),
                    ("40k unique + 2k x50 (heavy duplication)", dup_lib(40000, [(50, 2000)]))):
    reads = [(f"d{i}", s, qstr([36] * len(s))) for i, s in enumerate(seqs)]
    fq = os.path.join(d, "dup.fq"); write_fastq(fq, reads); m = run(fq)
    mod = m["Sequence Duplication Levels"]
    total_dedup = float([c for c in mod.get("comments", []) if c.startswith("#Total Deduplicated")][0].split("\t")[1])
    hdr = [c for c in mod.get("comments", []) if c.startswith("#Duplication Level")][0][1:].split("\t")
    col = hdr.index("Percentage of total")          # 0.11.x also prints a "Percentage of deduplicated" column first
    got_levels = {r[0].rstrip("+"): float(r[col]) for r in mod["rows"]}
    true_dedup, true_levels = dup_truth(seqs)
    worst = max(abs(got_levels.get(k, 0) - v) for k, v in true_levels.items())
    print(f"   {label}: {len(seqs)} reads; Total Deduplicated Percentage {total_dedup:.2f} (true {true_dedup:.2f}); largest level-bin difference {worst:.2f} points; status {mod['status']}")
    report(f"duplication: estimate within 1 point of the truth ({label})", abs(total_dedup - true_dedup) < 1.0 and worst < 1.0)
