"""a1: bwa aln + samse / sampe (BWA-backtrack) on planted edits.

Reads of 36, 50 and 75 bp cut from a random reference with 0-3
substitutions or one 1-2-bp indel in the middle, both strands. Reads with more
than two substitutions inside the 5' 32-bp seed are set aside (the default
-l 32 -k 2 excludes them by design) and reported separately. Checked: POS and
strand at the planted origin, NM/MD equal the Python recomputation from SEQ,
the reference and the CIGAR, and for sampe: TLEN = +/- fragment and flag 0x2 on
every pair (fragments ~ N(250, 25), all well inside the inferred bounds).
"""
import random
from _synth import *

rng = random.Random(17)
REF = 300000
ref = rand_seq(rng, REF)
fa = os.path.join(WORK, "a1_ref.fa")
write_fasta(fa, [("chr1", ref)])
index(fa)
header("bwa aln/samse/sampe, reference 300 kb random")


PLANTED = []


def plant(st, L, kind):
    global PLANTED
    PLANTED = []
    if kind[0] == "sub":
        r = ref[st:st + L]
        PLANTED = rng.sample(range(3, L - 3), kind[1])
        for p in PLANTED:
            r = mutate_sub(rng, r, p)
        return r
    if kind[0] == "ins":
        p = L // 2
        return (ref[st:st + p] + rand_seq(rng, kind[1]) + ref[st + p:st + L])[:L]
    if kind[0] == "del":
        p = L // 2
        return ref[st:st + p] + ref[st + p + kind[1]:st + L + kind[1]]


reads, truth = [], {}
kinds = [("sub", 0), ("sub", 1), ("sub", 2), ("sub", 3), ("ins", 1), ("ins", 2), ("del", 1), ("del", 2)]
i = 0
for L in (36, 50, 75):
    for k in kinds:
        if L == 36 and k[0] == "sub" and k[1] == 3:
            continue   # beyond the default -n for 36 bp
        for j in range(15):
            st = rng.randrange(1000, REF - 1000)
            r = plant(st, L, k)
            rev = j % 2 == 1
            n = "r%d" % i; i += 1
            # differences inside the 5' 32-bp seed of the read (-l 32 -k 2 allows two)
            in_seed = sum(1 for p in PLANTED if (L - 1 - p if rev else p) < 32)
            truth[n] = (st, rev, "%d bp %s %d" % (L, k[0], k[1]), in_seed)
            reads.append((n, revcomp(r) if rev else r))
fq = os.path.join(WORK, "a1.fq")
write_fastq(fq, reads)
sai = os.path.join(WORK, "a1.sai")
out, _ = run([BWA, "aln", "-f", sai, fa, fq])
out, _ = run([BWA, "samse", fa, sai, fq])
recs = parse_sam(out)
cls = {}
excluded = []
for r in recs:
    st, rev, c, in_seed = truth[r.qname]
    d = cls.setdefault(c, [0, 0, 0, 0])
    if in_seed > 2:
        excluded.append((r.qname, c, in_seed, r.unmapped))
        continue
    d[0] += 1
    if r.unmapped:
        continue
    d[1] += 1
    d[2] += (r.rev == rev and r.pos - 1 == st)
    nm, md = nm_md(r.seq, ref, r.pos - 1, r.cigar)
    d[3] += nm == r.tags.get("NM") and md == r.tags.get("MD")
print("   %-16s %4s %6s %8s %6s" % ("class", "n", "mapped", "POS ok", "NM/MD"))
tot = [0, 0, 0, 0]
for c in cls:
    print("   %-16s %4d %6d %8d %6d" % (c, *cls[c]))
    tot = [a + b for a, b in zip(tot, cls[c])]
print("   %d reads have 3 differences inside the 5' 32-bp seed (default -l 32 -k 2, documented); unmapped: %d"
      % (len(excluded), sum(1 for x in excluded if x[3])))
ok(tot[1] == tot[0], "samse: every planted read within the seed rule mapped: %d/%d" % (tot[1], tot[0]))
ok(tot[2] == tot[1], "samse: POS/strand at the planted origin: %d/%d" % (tot[2], tot[1]))
ok(tot[3] == tot[1], "samse: NM/MD equal the recomputation: %d/%d" % (tot[3], tot[1]))

# sampe
r1, r2, tp = [], [], {}
for j in range(2000):
    frag = int(rng.gauss(250, 25))
    st = rng.randrange(1000, REF - 1000)
    f = ref[st:st + frag]
    a, b = f[:50], revcomp(f[-50:])
    if j % 2:
        a, b = b, a
    n = "p%d" % j
    tp[n] = frag
    r1.append((n, a)); r2.append((n, b))
fq1 = os.path.join(WORK, "a1_1.fq"); fq2 = os.path.join(WORK, "a1_2.fq")
write_fastq(fq1, r1); write_fastq(fq2, r2)
s1 = os.path.join(WORK, "a1_1.sai"); s2 = os.path.join(WORK, "a1_2.sai")
run([BWA, "aln", "-f", s1, fa, fq1]); run([BWA, "aln", "-f", s2, fa, fq2])
out, err = run([BWA, "sampe", fa, s1, s2, fq1, fq2])
m = re.search(r"inferred external isize from (\d+) pairs: ([\d.]+) \+/- ([\d.]+)", err)
recs = parse_sam(out)
tl = fl = 0
for r in recs:
    tl += abs(r.tlen) == tp[r.qname]
    fl += bool(r.flag & 2)
print("   sampe insert size printed: %s pairs, %s +/- %s; true mean of the simulated fragments %.2f"
      % (m.group(1), m.group(2), m.group(3), sum(tp.values()) / len(tp)))
ok(tl == len(recs), "sampe: TLEN = +/- fragment: %d/%d" % (tl, len(recs)))
ok(fl == len(recs), "sampe: flag 0x2 on every record: %d/%d" % (fl, len(recs)))
