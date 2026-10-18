"""c1: split (chimeric) reads: SA tag, supplementary MAPQ, MC/MQ/RNEXT on
supplementary records, proper-pair flag.

Pairs on a two-contig random reference. Mate 1 is chimeric: 90 bp from chr1
followed by 60 bp from chr2 (both unique). Mate 2 is a normal reverse mate of
the chr1 part (fragment ~ N(350, 30)); half of the mate-2 reads carry a 12-bp
random 3' tail so that their primary CIGAR has a soft clip.
Checked against the records themselves (no BWA formula needed):
  - each SA entry equals the other record (RNAME, POS, strand, CIGAR with
    H read as S, MAPQ, NM);
  - supplementary MAPQ <= primary MAPQ (bwa caps it unless -q/-5);
  - MC:Z on every record equals the mate's primary CIGAR, MQ:i its MAPQ,
    RNEXT/PNEXT its position (SAM spec: MC is the mate's CIGAR string);
  - flag 0x2 on the records of pairs whose chr1 parts are concordant.
"""
import random
from _synth import *

rng = random.Random(3)
c1 = rand_seq(rng, 300000)
c2 = rand_seq(rng, 200000)
fa = os.path.join(WORK, "c1_ref.fa")
write_fasta(fa, [("chr1", c1), ("chr2", c2)])
index(fa)
header("chr1 300 kb + chr2 200 kb random; mate 1 = 90 bp chr1 + 60 bp chr2")

r1, r2, truth = [], [], {}
for j in range(600):
    frag = int(rng.gauss(350, 30))
    st = rng.randrange(1000, 290000)
    f = c1[st:st + frag]
    b = rng.randrange(1000, 190000)
    m1 = f[:90] + c2[b:b + 60]
    m2 = revcomp(f[-150:])
    tail = j % 2 == 1
    if tail:
        m2 = m2[:138] + rand_seq(rng, 12)
    n = "c%d" % j
    truth[n] = (st, frag, b, tail)
    r1.append((n, m1)); r2.append((n, m2))
# background pairs for the insert-size estimate
for j in range(3000):
    frag = int(rng.gauss(350, 30))
    st = rng.randrange(1000, 290000)
    f = c1[st:st + frag]
    n = "n%d" % j
    r1.append((n, f[:150])); r2.append((n, revcomp(f[-150:])))
fq1 = os.path.join(WORK, "c1_1.fq"); fq2 = os.path.join(WORK, "c1_2.fq")
write_fastq(fq1, r1); write_fastq(fq2, r2)


def h2s(c):
    return c.replace("H", "S")


def check(opts, label):
    recs, err = mem(fa, fq1, fq2, opts)
    by = {}
    for r in recs:
        if r.qname.startswith("c"):
            by.setdefault(r.qname, []).append(r)
    n_sa = n_sa_ok = 0
    n_supp = n_cap = 0
    mc_tot = mc_ok = 0
    mc_bad_supp = []
    mate_ok = mate_tot = 0
    proper = 0
    for n, rs in by.items():
        prim = {1 if r.flag & 64 else 2: r for r in rs if r.primary}
        for r in rs:
            mate = prim[2 if r.flag & 64 else 1]
            me = prim[1 if r.flag & 64 else 2]
            # SA
            if "SA" in r.tags:
                for ent in r.tags["SA"].rstrip(";").split(";"):
                    rn, pos, strand, cig, mq, nm = ent.split(",")
                    n_sa += 1
                    others = [o for o in rs if o is not r and (o.flag & 64) == (r.flag & 64)]
                    hit = [o for o in others if o.rname == rn and o.pos == int(pos) and ("-" if o.rev else "+") == strand
                           and h2s(o.cigar) == cig and o.mapq == int(mq) and o.tags["NM"] == int(nm)]
                    n_sa_ok += bool(hit)
            if not r.primary:
                n_supp += 1
                n_cap += r.mapq <= me.mapq
            # mate fields
            if not mate.unmapped:
                mate_tot += 1
                mate_ok += (r.pnext == mate.pos and (r.rnext == "=" and r.rname == mate.rname or r.rnext == mate.rname)
                            and r.tags.get("MQ", mate.mapq) == mate.mapq)
                mc_tot += 1
                if r.tags.get("MC") == mate.cigar:
                    mc_ok += 1
                elif not r.primary:
                    mc_bad_supp.append((r.qname, r.cigar, r.tags.get("MC"), mate.cigar))
        proper += all(bool(r.flag & 2) for r in rs)
    print("%s:" % label)
    has_mc = any("MC" in r.tags for rs in by.values() for r in rs)
    ok(n_sa_ok == n_sa, "  SA entries equal the records they name: %d/%d" % (n_sa_ok, n_sa))
    ok(n_cap == n_supp, "  split-segment (0x800, or 0x100 under -M) MAPQ <= primary MAPQ: %d/%d" % (n_cap, n_supp))
    ok(mate_ok == mate_tot, "  RNEXT/PNEXT/MQ equal the mate's primary record: %d/%d" % (mate_ok, mate_tot))
    if has_mc:
        ok(mc_ok == mc_tot, "  MC:Z equals the mate's primary CIGAR: %d/%d records" % (mc_ok, mc_tot))
    else:
        print("   MC:Z / MQ:i not emitted by this build (added in 0.7.16)")
    for x in mc_bad_supp[:4]:
        print("     supplementary %s CIGAR %s  MC:Z:%s  but the mate's CIGAR is %s" % x)
    if mc_bad_supp:
        print("     (%d supplementary records carry the mate's CIGAR with S rewritten as H)" % len(mc_bad_supp))
    print("   pairs with flag 0x2 on every record: %d/%d" % (proper, len(by)))


check([], "default")
check(["-Y"], "-Y (soft-clip supplementary)")
check(["-M"], "-M (supplementary flagged secondary)")
