"""s1: AS, NM, MD, CIGAR and POS of single-end bwa mem alignments against
planted edits.

Truth: reads cut from a random reference at known positions with known
substitutions, Ns, insertions and deletions. For every primary record:
  - POS/strand equal the planted origin (POS shifted by a left soft clip
    or a left-normalised indel is accepted when the CIGAR explains it);
  - NM and MD equal the values recomputed in Python from SEQ, the
    reference and the printed CIGAR (SAM spec semantics);
  - AS equals the best local Smith-Waterman score of the read against the
    reference window, computed in Python with the documented scheme
    (bwa.1 -L: "the SAM AS tag reports the best SW score; clipping penalty
    is not deduced");
  - the printed CIGAR scores at least as well as the planted edits
    (otherwise BWA reported a worse alignment than the truth).
"""
import random
import sys
from _synth import *

rng = random.Random(11)
REF_LEN = 300000
ref = rand_seq(rng, REF_LEN)
fa = os.path.join(WORK, "s1_ref.fa")
write_fasta(fa, [("chr1", ref)])
index(fa)

header("reference %d bp random, single-end, defaults" % REF_LEN)

classes = []


def make(name, L, edits_fn, n=12):
    classes.append((name, L, edits_fn, n))


def apply_edits(L, edits, start):
    """edits: list of (kind, pos_in_read_template, len). Builds the read from
    the reference at `start`, returns (read, truth_score)."""
    # build the read left to right over the reference
    read = []
    r = start
    tscore = 0
    ev = {p: (k, l) for k, p, l in edits}
    i = 0
    while len(read) < L:
        if i in ev:
            k, l = ev[i]
            if k == "sub":
                read.append(rng.choice([x for x in "ACGT" if x != ref[r]]))
                r += 1
                tscore -= 4
            elif k == "N":
                read.append("N")
                r += 1
                tscore -= 1
            elif k == "ins":
                read.extend(rand_seq(rng, l))
                tscore -= 6 + l
            elif k == "del":
                r += l
                tscore -= 6 + l
                read.append(ref[r])
                r += 1
                tscore += 1
        else:
            read.append(ref[r])
            r += 1
            tscore += 1
        i += 1
    read = "".join(read[:L])
    return read, tscore, r


def subs(k):
    return lambda L: [("sub", p, 1) for p in rng.sample(range(10, L - 10), k)]


make("perfect", 100, lambda L: [], 12)
make("perfect", 150, lambda L: [], 12)
for k in (1, 2, 3, 5):
    make("%d subs" % k, 100, subs(k))
    make("%d subs" % k, 150, subs(k))
for p in (0, 1, 2, 3, 4, 6):
    make("sub at read pos %d" % p, 100, (lambda p: lambda L: [("sub", p, 1)])(p))
    make("sub at read pos L-1-%d" % p, 100, (lambda p: lambda L: [("sub", L - 1 - p, 1)])(p))
make("2 Ns", 100, lambda L: [("N", p, 1) for p in rng.sample(range(10, 90), 2)])
for l in (1, 2, 3, 5):
    make("%d-bp insertion mid" % l, 100, (lambda l: lambda L: [("ins", rng.randrange(30, 70), l)])(l))
    make("%d-bp deletion mid" % l, 100, (lambda l: lambda L: [("del", rng.randrange(30, 70), l)])(l))
    make("%d-bp deletion mid" % l, 150, (lambda l: lambda L: [("del", rng.randrange(40, 110), l)])(l))
make("1-bp insertion at 12", 100, lambda L: [("ins", 12, 1)])
make("2-bp deletion at 12", 100, lambda L: [("del", 12, 2)])
make("sub+ins+del", 150, lambda L: [("sub", 20, 1), ("ins", 60, 2), ("del", 110, 3)])

reads = []
truth = {}
rid = 0
for name, L, fn, n in classes:
    for j in range(n):
        start = rng.randrange(1000, REF_LEN - 1000)
        edits = fn(L)
        read, tscore, end = apply_edits(L, edits, start)
        strand = rng.random() < 0.5
        rname = "r%d" % rid
        rid += 1
        truth[rname] = (name, L, start, end, strand, tscore, read)
        reads.append((rname, revcomp(read) if strand else read))
fq = os.path.join(WORK, "s1.fq")
write_fastq(fq, reads)
recs, err = mem(fa, fq)

per_class = {}
bad = []
doc_as = 0
for rec in recs:
    if not rec.primary:
        continue
    name, L, start, end, strand, tscore, fwd = truth[rec.qname]
    c = per_class.setdefault((name, L), {"n": 0, "pos": 0, "nmmd": 0, "as": 0, "opt": 0, "as_unclip": 0})
    c["n"] += 1
    if rec.unmapped:
        bad.append((rec.qname, name, "unmapped"))
        continue
    lclip, rclip = clip_lengths(rec.cigar)
    pos0 = rec.pos - 1
    span = ref_span(rec.cigar)
    pos_ok = rec.rev == strand and start - 6 <= pos0 <= start + lclip + 6
    c["pos"] += pos_ok
    nm, md = nm_md(rec.seq, ref, pos0, rec.cigar)
    nmmd_ok = (nm == rec.tags.get("NM") and md == rec.tags.get("MD"))
    c["nmmd"] += nmmd_ok
    if not nmmd_ok:
        bad.append((rec.qname, name, "NM/MD %s/%s vs %s/%s" % (rec.tags.get("NM"), rec.tags.get("MD"), nm, md)))
    w0 = max(0, start - 20)
    window = ref[w0:end + 20]
    best = local_sw(rec.seq, window)
    as_ok = rec.tags.get("AS") == best
    c["as"] += as_ok
    if not as_ok:
        bad.append((rec.qname, name, "AS %s vs SW %d (CIGAR %s)" % (rec.tags.get("AS"), best, rec.cigar)))
    cs = cigar_score(rec.seq, ref, pos0, rec.cigar)
    # the planted alignment is end-to-end; BWA may clip instead, which is
    # optimal under the local score + clipping penalty: compare the CIGAR's
    # score minus the clipping penalty actually applied to the planted score
    pen = (5 if lclip else 0) + (5 if rclip else 0)
    opt_ok = cs - pen >= tscore - 0 or cs >= tscore
    c["opt"] += opt_ok
    if not opt_ok:
        bad.append((rec.qname, name, "CIGAR %s scores %d (pen %d) < planted %d" % (rec.cigar, cs, pen, tscore)))
    if not lclip and not rclip and rec.tags.get("AS") != cs:
        c["as_unclip"] += 1
        doc_as += 1
        if doc_as <= 6:
            print("   note: %s %-24s CIGAR %-10s NM %d AS %d, score of the printed alignment %d (documented -L behaviour)"
                  % (rec.qname, name, rec.cigar, rec.tags["NM"], rec.tags["AS"], cs))

print()
print("%-26s %4s %4s %6s %6s %8s %10s" % ("class", "L", "n", "POS", "NM/MD", "AS=SW", "AS!=CIGARsc"))
tot = {"n": 0, "pos": 0, "nmmd": 0, "as": 0, "opt": 0}
for (name, L), c in per_class.items():
    print("%-26s %4d %4d %6d %6d %8d %10d" % (name, L, c["n"], c["pos"], c["nmmd"], c["as"], c["as_unclip"]))
    for k in tot:
        tot[k] += c[k]
print()
ok(tot["pos"] == tot["n"], "POS/strand at the planted origin: %d/%d" % (tot["pos"], tot["n"]))
ok(tot["nmmd"] == tot["n"], "NM and MD equal the independent recomputation: %d/%d" % (tot["nmmd"], tot["n"]))
ok(tot["as"] == tot["n"], "AS equals the best local SW score (documented): %d/%d" % (tot["as"], tot["n"]))
ok(tot["opt"] == tot["n"], "printed CIGAR at least as good as the planted edits: %d/%d" % (tot["opt"], tot["n"]))
print("   unclipped records whose AS differs from the score of the printed alignment: %d (bwa.1 -L documents this)" % doc_as)
for b in bad[:20]:
    print("   ", b)
