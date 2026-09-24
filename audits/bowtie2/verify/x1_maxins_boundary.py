"""X1: pairs whose fragment is slightly longer than -X. The anchor mate aligns;
the opposite mate is sought by dynamic programming inside the window that -X
allows, so an alignment that fits the window by opening gaps near the read
end can be found first, and the perfect end-to-end alignment of the same
read a few bases further along is then not reported. Scans fragment lengths
around -X with 100-bp mates from unique random sequence; records the mate
CIGARs, AS, YT and TLEN, and counts pairs where a mate is reported with a gap
although a gap-free perfect alignment exists.
"""
import random, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(21)
G = 200000
refs = rand_seq(rng, G)
d = tmpdir()
write_fasta(os.path.join(d, "ref.fa"), [("chr1", refs)])
idx = build_index(os.path.join(d, "ref.fa"), os.path.join(d, "ref"))
print(f"bowtie2 {version()}  reference {G} bp random; 100-bp mates, 10 pairs per fragment length, no sequencing differences")

def scan(X, lengths, args, label):
    mates = []; truth = {}
    pos = 1000
    for fl in lengths:
        for k in range(10):
            name = f"f{fl}_{k}"
            m1, m2 = mate_pair(name, refs, pos, fl, 100, 100)
            mates.append((fq(m1), fq(m2))); truth[name] = fl; pos += fl + 300
    recs, err = align(idx, mates=mates, args=args + ["-X", str(X)])
    by = collections.defaultdict(dict)
    for r in recs:
        by[r.qname][1 if r.flag & 64 else 2] = r
    print(f"\n{label}: -X {X} {' '.join(args)}")
    print(f"   {'fragment':>8s} {'pairs':>5s} {'CP':>3s} {'DP':>3s} {'UP':>3s}  gapped mates  |TLEN| reported (min-max)   example mate CIGAR / AS")
    total_gapped = 0; over_x_gapped = 0; over_x_pairs = 0
    for fl in lengths:
        yts = collections.Counter(); gapped = 0; tls = []; ex = ""
        for k in range(10):
            pr = by[f"f{fl}_{k}"]
            yts[pr[1].tags.get("YT")] += 1
            tls.append(abs(pr[1].tlen))
            for m in (1, 2):
                r = pr[m]
                if not (r.flag & 4) and ("I" in r.cigar or "D" in r.cigar):
                    gapped += 1
                    ex = ex or f"{r.cigar} / AS {r.tags.get('AS')} MAPQ {r.mapq} XS {r.tags.get('XS')}"
        total_gapped += gapped
        if fl > X:
            over_x_pairs += 10; over_x_gapped += gapped
        print(f"   {fl:8d} {10:5d} {yts.get('CP', 0):3d} {yts.get('DP', 0):3d} {yts.get('UP', 0):3d}  {gapped:12d}  {min(tls):5d}-{max(tls):<5d}                 {ex}")
    report(f"{label}: no mate is reported with a gap (all reads are exact copies of the reference)", total_gapped == 0,
           f"({over_x_gapped} of {2 * over_x_pairs} mates of pairs with fragment > X carry a spurious gap)")

scan(500, list(range(480, 561, 5)) + [580, 600, 650], [], "end-to-end, default")
scan(500, list(range(490, 541, 5)), ["--very-sensitive"], "end-to-end, --very-sensitive")
scan(500, list(range(490, 541, 5)), ["--local"], "local")
scan(300, list(range(290, 341, 5)), [], "end-to-end, -X 300")
scan(500, list(range(490, 541, 5)), ["--no-discordant"], "end-to-end, --no-discordant")
scan(500, list(range(490, 541, 5)), ["--no-mixed"], "end-to-end, --no-mixed")
