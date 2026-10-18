"""J1: -x splice junction placement and transcript strand.

Genes are planted in a random genome: 4-8 exons (60-400 bp) separated by
introns (80 bp - 20 kb) whose ends carry GT..AG (75 %), GC..AG (15 %) or
AT..AC (10 %). Each junction is checked for positional ambiguity in Python: the
intron can slide by s bases without changing the spliced sequence iff the bases
leaving one side equal the bases entering the other; slides that also keep a
canonical GT-AG motif make the junction ambiguous under any splice model, and
those are counted separately. Genes are on both genome strands; reads are the
full transcript or a random 70-100 % of it, in sense or antisense orientation,
error-free and ONT-like (~7 % error).

Truth: each N operation in the CIGAR must coincide with a planted intron
(exact start and end), and ts:A must be '+' for sense reads and '-' for antisense
reads (format.c prints the strand relative to the read; align.c flips it for
reverse-strand hits).
"""
import os, sys, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(13)
G = 6000000
ref = list(rand_seq(rng, G))
genes = []
cur = 20000
MOTIF = [("GT", "AG", 0.75), ("GC", "AG", 0.15), ("AT", "AC", 0.10)]
while len(genes) < 120:
    n_ex = rng.randint(4, 8)
    strand = "+" if rng.random() < .5 else "-"
    exons, introns = [], []
    pos = cur
    for i in range(n_ex):
        el = rng.randint(60, 400)
        exons.append((pos, pos + el)); pos += el
        if i < n_ex - 1:
            il = rng.choice([rng.randint(80, 300), rng.randint(300, 3000), rng.randint(3000, 20000)])
            x = rng.random(); acc = 0
            for dn, ac, p in MOTIF:
                acc += p
                if x <= acc: break
            if strand == "+":
                ref[pos:pos + 2] = list(dn); ref[pos + il - 2:pos + il] = list(ac)
            else:  # transcript on the genome - strand: genome + shows revcomp(acceptor) ... revcomp(donor)
                ref[pos:pos + 2] = list(revcomp(ac)); ref[pos + il - 2:pos + il] = list(revcomp(dn))
            introns.append((pos, pos + il, dn + "-" + ac)); pos += il
    genes.append((exons, introns, strand))
    cur = pos + 20000
assert cur < G
refs = "".join(ref)
d = tmpdir(); fa = os.path.join(d, "ref.fa"); write_fasta(fa, [("chr1", refs)])


def ambiguity(st, en):
    """Return the list of slides s != 0 (|s| <= 12) that keep the spliced sequence, and
    those of them that land on GT-AG / CT-AC (either genome strand)."""
    out, canon = [], []
    for s in range(-12, 13):
        if s == 0: continue
        if s > 0:
            ok = refs[st:st + s] == refs[en:en + s]
        else:
            ok = refs[st + s:st] == refs[en + s:en]
        if ok:
            out.append(s)
            m = refs[st + s:st + s + 2] + "-" + refs[en + s - 2:en + s]
            if m in ("GT-AG", "CT-AC"):
                canon.append(s)
    return out, canon


print(version(), f" genome {G} bp, {len(genes)} planted genes, "
      f"{sum(len(g[1]) for g in genes)} introns")
reads, truth = [], {}
for gi, (exons, introns, strand) in enumerate(genes):
    tx = "".join(refs[a:b] for a, b in exons)   # genome + strand
    for k in range(6):
        sub = tx
        if k >= 2:
            L = int(len(tx) * rng.uniform(.7, 1.0)); o = rng.randint(0, len(tx) - L); sub = tx[o:o + L]
        sense_seq = sub if strand == "+" else revcomp(sub)
        sense = k % 2 == 0
        s = sense_seq if sense else revcomp(sense_seq)
        err = k >= 4
        if err:
            s = noisy(rng, s, sub=0.03, ins=0.02, dele=0.02)
        name = f"g{gi}_{k}_{'sense' if sense else 'anti'}_{'ont' if err else 'exact'}"
        reads.append((name, s)); truth[name] = (gi, sense, err)
fq = os.path.join(d, "tx.fq"); write_fastq(fq, reads)

intron_set = {}
amb_class = {}
for gi, (exons, introns, strand) in enumerate(genes):
    for st, en, motif in introns:
        sl, canon = ambiguity(st, en)
        intron_set[(st, en)] = (gi, motif)
        amb_class[(st, en)] = "unambiguous" if not sl else ("slides keep sequence, none canonical" if not canon else "a canonical alternative exists")

for label, args in (("-x splice", ["-ax", "splice"]), ("-x splice:hq", ["-ax", "splice:hq"])):
    recs = [r for r in parse_sam(run(args + ["-t1", fa, fq])) if not r["flag"] & 0x904]
    stats = collections.defaultdict(collections.Counter)
    ts_ok = ts_bad = ts_none = 0
    bad_examples = []
    for r in recs:
        gi, sense, err = truth[r["qname"]]
        cls = "ONT-like" if err else "exact"
        t = r["pos"] - 1
        for n, op in cigar_ops(r["cigar"]):
            if op in "MDN=X":
                if op == "N":
                    key = (t, t + n)
                    if key in intron_set:
                        stats[cls]["N on a planted intron"] += 1
                        stats[cls + " / " + intron_set[key][1]]["exact"] += 1
                    else:
                        # nearest planted intron
                        near = min(intron_set, key=lambda k: abs(k[0] - t) + abs(k[1] - (t + n)))
                        off = (t - near[0], t + n - near[1])
                        amb = amb_class[near]
                        stats[cls]["N off a planted intron"] += 1
                        stats[cls + " / off by " + ("same shift" if off[0] == off[1] else "different")][amb] += 1
                        stats[cls + " / off, planted motif"][intron_set[near][1]] += 1
                        if len(bad_examples) < 6 and not err:
                            bad_examples.append((r["qname"], near, off, intron_set[near][1], amb))
                t += n
        ts = r["tags"].get("ts")
        if ts is None:
            ts_none += 1
        elif (ts == "+") == sense:
            ts_ok += 1
        else:
            ts_bad += 1
    print(f"\n[{label}] {len(recs)} primary records of {len(reads)} reads")
    for k in sorted(stats):
        print(f"  {k:45s} {dict(stats[k])}")
    print(f"  ts:A relative to the read: correct {ts_ok}, wrong {ts_bad}, absent {ts_none}")
    for ex in bad_examples:
        print("   off-intron example (exact read):", ex)
# How many planted introns are ambiguous at all
print("\nplanted introns by ambiguity:", dict(collections.Counter(amb_class.values())))

if os.environ.get("J1_DEBUG"):
    recs = [r for r in parse_sam(run(["-ax", "splice", "-t1", fa, fq])) if not r["flag"] & 0x904]
    tsc = collections.Counter()
    for r in recs:
        gi, sense, err = truth[r["qname"]]
        tsc[(genes[gi][2], "sense" if sense else "anti", "rev" if r["flag"] & 16 else "fwd", r["tags"].get("ts"))] += 1
    print("DBG ts table (gene strand, read orientation, SAM strand, ts):", dict(tsc))
    for r in recs:
        if r["qname"] in ("g3_0_sense_exact", "g6_0_sense_exact"):
            print("DBG", r["qname"], r["pos"], r["cigar"], r["tags"].get("ts"), r["tags"]["NM"])
    for gi in (3, 6):
        for st, en, m in genes[gi][1]:
            print("DBG intron", gi, st, en, m, refs[st-6:st] + "|" + refs[st:st+8], refs[en-8:en] + "|" + refs[en:en+6])
