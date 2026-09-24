"""F3: Overrepresented sequences (count, percentage, the 0.1 % / 1 % thresholds,
the 50-bp truncation) and Adapter Content (the cumulative per-position
percentage of reads containing each 12-mer from adapter_list.txt, averaged over
the base groups) recomputed from libraries with adapters inserted at known
offsets in known fractions of reads.
"""
import random, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(3)
print(f"FastQC {version()}")
d = tmpdir()
UNIV = "AGATCGGAAGAG"; NEXT = "CTGTCTCTTATA"; POLYG = "G" * 12
L = 100; N = 20000
reads = []; ins = collections.Counter()
for i in range(N):
    s = list(rand_seq(rng, L))
    # avoid accidental adapter 12-mers: negligible (4^-12 per position)
    r = rng.random()
    if r < 0.30:
        off = 60; s[off:off + 12] = UNIV; ins[("univ", off)] += 1
    elif r < 0.40:
        off = 20; s[off:off + 12] = UNIV; ins[("univ", off)] += 1
    elif r < 0.45:
        off = 85; s[off:off + 12] = NEXT; ins[("next", off)] += 1
    if i % 200 == 0:
        s[88:100] = POLYG; ins[("polyg", 88)] += 1
    reads.append((f"a{i}", "".join(s), qstr([36] * L)))
# an overrepresented sequence: 120 copies (0.6 %) of one read, and 250 copies (1.25 %) of another
over1 = rand_seq(rng, L); over2 = rand_seq(rng, L)
reads += [(f"o1_{k}", over1, qstr([36] * L)) for k in range(120)]
reads += [(f"o2_{k}", over2, qstr([36] * L)) for k in range(250)]
rng.shuffle(reads)
total = len(reads)
fq = os.path.join(d, "ad.fq"); write_fastq(fq, reads); m = run(fq)

# ---- adapter content port
hdr = m["Adapter Content"]["header"]; rows = m["Adapter Content"]["rows"]
longest_adapter = 12
npos = L - longest_adapter + 1
counts = {name: [0] * npos for name in hdr[1:]}
for n, s, q in reads:
    for name, ad in (("Illumina Universal Adapter", UNIV), ("Nextera Transposase Sequence", NEXT), ("PolyG", POLYG), ("PolyA", "A" * 12),
                     ("Illumina Small RNA 3' Adapter", "TGGAATTCTCGG"), ("Illumina Small RNA 5' Adapter", "GATCGTCGGACT")):
        if name not in counts: continue
        idx = s.find(ad)
        if idx >= 0:
            for p in range(idx, npos): counts[name][p] += 1
groups = base_groups(npos)
bad = 0
for r, (a, b) in zip(rows, groups):
    for j, name in enumerate(hdr[1:]):
        exp = sum(100.0 * counts[name][p - 1] / total for p in range(a, b + 1)) / (b - a + 1)
        if abs(float(r[j + 1]) - exp) > 1e-6: bad += 1
report(f"Adapter Content: {len(rows)} rows x {len(hdr) - 1} adapters equal the port (cumulative % of reads containing the 12-mer at or before the position, averaged over the group)", bad == 0 and len(rows) == len(groups),
       f"(rows {len(rows)} vs groups {len(groups)}; {bad} cells differ)")
last = rows[-1]
print(f"   last row {last[0]}: " + ", ".join(f"{n} {float(v):.2f} %" for n, v in zip(hdr[1:], last[1:])) + f"; expected universal {100 * (ins[('univ', 60)] + ins[('univ', 20)]) / total:.2f} %, Nextera {100 * ins[('next', 85)] / total:.2f} %, PolyG {100 * ins[('polyg', 88)] / total:.2f} %")
print(f"   status {m['Adapter Content']['status']} (warn > 5 %, fail > 10 % in any cell)")
report("Adapter Content: status fail (universal adapter cumulative share 40 % > 10 %)", m["Adapter Content"]["status"] == "fail")

# ---- overrepresented sequences
mod = m["Overrepresented sequences"]; rows = mod["rows"]
got = {r[0]: (int(r[1]), float(r[2])) for r in rows}
exp = {over1[:50]: (120, 100.0 * 120 / total), over2[:50]: (250, 100.0 * 250 / total)}
ok = set(got) == set(exp) and all(got[k][0] == v[0] and abs(got[k][1] - v[1]) < 0.005 for k, v in exp.items())   # master prints the percentage rounded to 2 decimals
print(f"   overrepresented rows: {[(k[:20] + '...', v) for k, v in got.items()]}; expected {[(k[:20] + '...', v) for k, v in exp.items()]}; status {mod['status']}")
report("Overrepresented sequences: the two planted sequences (first 50 bp), their counts and percentages, nothing else", ok)
report("Overrepresented sequences: status fail (one sequence above 1 %)", mod["status"] == "fail")

# a sequence that first appears after the first 100,000 distinct sequences is not tracked
reads2 = [(f"u{i}", rand_seq(rng, 60), qstr([36] * 60)) for i in range(120000)]
late = rand_seq(rng, 60)
reads2 += [(f"late{k}", late, qstr([36] * 60)) for k in range(3000)]   # 2.4 % of the file, all after the 100k-unique limit
fq = os.path.join(d, "late.fq"); write_fastq(fq, reads2); m = run(fq)
rows = m["Overrepresented sequences"]["rows"]
print(f"   3,000 copies (2.4 %) of a sequence first seen after 120,000 distinct sequences: overrepresented rows {len(rows)}, status {m['Overrepresented sequences']['status']}; duplication module Total Deduplicated Percentage {[c for c in m['Sequence Duplication Levels'].get('comments', []) if c.startswith('#Total')][0].split(chr(9))[1][:6]} (true {100 * 120001 / 123000:.2f})")
report("Overrepresented sequences: a 2.4 % sequence first seen after the 100,000-distinct-sequence limit is reported (documented limitation: it is not)", len(rows) == 1)
