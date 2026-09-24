"""P1: paired-end constraints. Concordance (FLAG 0x2 / YT:Z:CP) and TLEN for
pairs of known fragment length against -I/-X, --fr/--rf/--ff, --no-overlap,
--no-contain and --dovetail, compared with a port of peClassifyPair (pe.cpp);
then the same pairs under -3/-5 hard trimming, --trim-to and --local soft
clipping, where the manual says the -I/-X constraint "is applied with respect
to the untrimmed mates" and the SAM TLEN is documented as the outer distance
of the mapped bases.
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(5)
G = 80000
refs = rand_seq(rng, G)
d = tmpdir()
write_fasta(os.path.join(d, "ref.fa"), [("chr1", refs)])
idx = build_index(os.path.join(d, "ref.fa"), os.path.join(d, "ref"))
print(f"bowtie2 {version()}  reference {G} bp random")

def recs_by_pair(recs):
    out = {}
    for r in recs:
        out.setdefault(r.qname, {})[1 if r.flag & 64 else 2] = r
    return out

def pair_status(r):
    return r.tags.get("YT"), bool(r.flag & 2), r.tlen

# ---------- 1. fragment length vs -I/-X and orientation, no trimming
def block1():
    print("\n1. fragment length vs -I 200 -X 500 (100-bp mates, FR):")
    mates = []; truth = {}
    pos = 1000
    for fl in (150, 199, 200, 201, 250, 400, 499, 500, 501, 600, 1200):
        m1, m2 = mate_pair(f"fl{fl}", refs, pos, fl, 100, 100)
        mates.append((fq(m1), fq(m2))); truth[f"fl{fl}"] = fl; pos += 2000
    recs, err = align(idx, mates=mates, args=["-I", "200", "-X", "500"])
    ok = True
    for name, pr in recs_by_pair(recs).items():
        fl = truth[name]
        exp = classify_pair(0, 100, True, fl - 100, 100, False, maxfrag=500, minfrag=200)
        yt, conc, tl = pair_status(pr[1])
        want_conc = exp != "DISCORD"
        line_ok = conc == want_conc and (not conc or abs(tl) == fl) and pr[1].tlen == -pr[2].tlen
        ok &= line_ok
        print(f"   fragment {fl:4d}: YT {yt} FLAG&2 {int(conc)} TLEN {pr[1].tlen:5d}/{pr[2].tlen:5d}  port {exp:8s} {'' if line_ok else '<-- differs'}")
    report("block 1: concordance and TLEN follow -I/-X on untrimmed 100-bp mates", ok)

def block2():
    print("\n2. orientation policies (fragment 300, 100-bp mates):")
    ok = True
    for orient in ("FR", "RF", "FF"):
        m1, m2 = mate_pair(f"o{orient}", refs, 20000, 300, 100, 100, orient=orient)
        for pol in ("--fr", "--rf", "--ff"):
            recs, err = align(idx, mates=[(fq(m1), fq(m2))], args=[pol])
            pr = recs_by_pair(recs)[f"o{orient}"]
            yt, conc, tl = pair_status(pr[1])
            want = (orient == pol[2:].upper())
            line_ok = conc == want and (not conc or (abs(pr[1].tlen) == 300 and pr[1].tlen == -pr[2].tlen))
            ok &= line_ok
            print(f"   pair {orient} under {pol}: YT {yt} FLAG&2 {int(conc)} TLEN {pr[1].tlen:5d}/{pr[2].tlen:5d} {'' if line_ok else '<-- differs'}")
    report("block 2: --fr/--rf/--ff classify the three layouts as documented, TLEN signed by position", ok)

def block3():
    print("\n3. overlap / containment / dovetail (defaults: overlap ok, contain ok, dovetail not):")
    ok = True
    cases = [  # (label, off1, len1, off2, len2) offsets relative to a base, mate1 fw, mate2 rc
        ("separate", 0, 100, 200, 100),
        ("overlap40", 0, 100, 60, 100),
        ("contain_mate2_inside_mate1", 0, 150, 20, 100),
        ("identical_extents", 0, 100, 0, 100),
        ("dovetail20", 20, 100, 0, 100),
    ]
    base = 30000
    for label, o1, l1, o2, l2 in cases:
        m1 = make_read(label, refs, base + o1, l1, fw=True)
        m2 = make_read(label, refs, base + o2, l2, fw=False)
        for opts in ([], ["--no-overlap"], ["--no-contain"], ["--dovetail"]):
            recs, err = align(idx, mates=[(fq(m1), fq(m2))], args=opts)
            pr = recs_by_pair(recs)[label]
            exp = classify_pair(o1, l1, True, o2, l2, False, olap_ok="--no-overlap" not in opts, contain_ok="--no-contain" not in opts, dovetail_ok="--dovetail" in opts)
            yt, conc, tl = pair_status(pr[1])
            want = exp != "DISCORD"
            outer = max(o1 + l1, o2 + l2) - min(o1, o2)
            line_ok = conc == want and (not conc or abs(tl) == outer)
            ok &= line_ok
            print(f"   {label:30s} {' '.join(opts) or 'default':14s}: YT {yt} FLAG&2 {int(conc)} TLEN {pr[1].tlen:5d}/{pr[2].tlen:5d}  port {exp:8s} {'' if line_ok else '<-- differs'}")
        base += 1000
    report("block 3: overlap/contain/dovetail options behave as the port of peClassifyPair", ok)

# ---------- 4. trimming and soft clipping: what does -X bound, and what does TLEN report?
def block4():
    print("\n4. -I/-X under -3/-5 hard trimming (manual: the constraint 'is applied with respect to the untrimmed mates'):")
    ok_doc = True
    rows = []
    for fl, trim, X in ((520, 20, 500), (560, 40, 500), (500, 20, 500), (230, 20, None)):
        m1, m2 = mate_pair(f"t{fl}_{trim}", refs, 40000 + fl, fl, 100, 100)
        args = ["-3", str(trim), "-5", str(trim)] + (["-X", str(X)] if X else ["-I", "200", "-X", "500"])
        recs, err = align(idx, mates=[(fq(m1), fq(m2))], args=args)
        pr = recs_by_pair(recs)[f"t{fl}_{trim}"]
        yt, conc, tl = pair_status(pr[1])
        aligned_extent = fl - 2 * trim   # each mate loses `trim` bases at both ends; the outer ends of the fragment lose one trim each
        doc_expect = (200 if not X else 0) <= fl <= (X or 500)
        rows.append((fl, trim, args, yt, conc, pr[1].tlen, pr[2].tlen, aligned_extent, doc_expect))
        ok_doc &= (conc == doc_expect)
        print(f"   fragment {fl} (untrimmed), -3 {trim} -5 {trim}, {' '.join(args[4:])}: aligned extent {aligned_extent}, YT {yt} FLAG&2 {int(conc)} TLEN {pr[1].tlen}/{pr[2].tlen}; per the manual (untrimmed {fl} vs the bounds) concordant={doc_expect}")
    report("block 4: -I/-X applied to the untrimmed fragment as the manual says", ok_doc,
           "" if ok_doc else "(the constraint is checked on the aligned extents; TLEN reports the untrimmed extent)")

    print("\n5. --trim-to and one-sided -3/-5 (100-bp mates, fragment 540 or 520, -X 500): which extent does -X bound, and what does TLEN report?")
    rows = []
    for label, fl, args, mapped in (("--trim-to 3:80 (inner 20 bp off each mate)", 540, ["--trim-to", "3:80"], 540),
                                    ("--trim-to 5:80 (outer 20 bp off each mate)", 540, ["--trim-to", "5:80"], 500),
                                    ("-5 20 (outer 20 bp off each mate)", 520, ["-5", "20"], 480),
                                    ("-3 20 (inner 20 bp off each mate)", 520, ["-3", "20"], 520)):
        m1, m2 = mate_pair("tt", refs, 50000, fl, 100, 100)
        recs, err = align(idx, mates=[(fq(m1), fq(m2))], args=args + ["-X", "500"])
        pr = recs_by_pair(recs)["tt"]
        yt, conc, tl = pair_status(pr[1])
        rows.append((mapped, conc, tl))
        print(f"   {label:44s}: untrimmed outer distance {fl}, mapped outer distance {mapped}, CIGAR {pr[1].cigar}/{pr[2].cigar}, YT {yt} FLAG&2 {int(conc)} TLEN {pr[1].tlen}/{pr[2].tlen}")
    report("block 5: with -3/-5 and --trim-to, |TLEN| is the mapped outer distance and -X bounds that same distance", all(abs(tl) == mapped and conc == (mapped <= 500) for mapped, conc, tl in rows))

    print("\n6. --local soft clipping (20 bases of non-genomic sequence on the 3' end of each mate, fragment 480 + 2x20 = 520 outer, -X 500):")
    # mates: mate1 = 80 genomic + 20 junk; mate2 = revcomp(80 genomic) + 20 junk; genomic outer distance 480
    junk = "ACGT" * 5
    f0 = 60000; fl = 480
    g1 = refs[f0:f0 + 80]; g2 = revcomp(refs[f0 + fl - 80:f0 + fl])
    j1 = "".join({"A": "C", "C": "A", "G": "T", "T": "G"}[b] for b in refs[f0 + 80:f0 + 100])
    j2 = "".join({"A": "C", "C": "A", "G": "T", "T": "G"}[b] for b in revcomp(refs[f0 + fl - 100:f0 + fl - 80]))
    mates = [(("sc", g1 + j1, "I" * 100), ("sc", g2 + j2, "I" * 100))]
    for X in (500, 470):
        for extra in ([], ["--soft-clipped-unmapped-tlen"]):
            recs, err = align(idx, mates=mates, args=["--local", "-X", str(X)] + extra)
            pr = recs_by_pair(recs)["sc"]
            yt, conc, tl = pair_status(pr[1])
            print(f"   -X {X} {' '.join(extra):28s}: CIGAR {pr[1].cigar}/{pr[2].cigar}, mapped outer distance {fl}, YT {yt} FLAG&2 {int(conc)} TLEN {pr[1].tlen}/{pr[2].tlen}")
    recs, err = align(idx, mates=mates, args=["--local", "-X", "500"])
    pr = recs_by_pair(recs)["sc"]
    report("block 6: --local: |TLEN| equals the outer distance of the mapped bases (SAM TLEN definition)", abs(pr[1].tlen) == fl,
           f"(TLEN {pr[1].tlen}: soft-clipped bases are included; -X 500 was satisfied by the mapped extent {fl})")
    # soft clips on the inner side: fragment 210, -I 200; the mapped extent 170 < I
    print("\n7. --local, junk on the 5' ends (inner clips), fragment 210 outer, -I 200 -X 500:")
    f0 = 62000; fl = 210
    g1 = refs[f0 + 20:f0 + 100]; g2 = revcomp(refs[f0 + fl - 100:f0 + fl - 20])
    j1 = "".join({"A": "C", "C": "A", "G": "T", "T": "G"}[b] for b in refs[f0:f0 + 20])
    j2 = "".join({"A": "C", "C": "A", "G": "T", "T": "G"}[b] for b in revcomp(refs[f0 + fl - 20:f0 + fl]))
    mates = [(("ic", j1 + g1, "I" * 100), ("ic", j2 + g2, "I" * 100))]
    for extra in ([], ["--soft-clipped-unmapped-tlen"]):
        recs, err = align(idx, mates=mates, args=["--local", "-I", "200", "-X", "500"] + extra)
        pr = recs_by_pair(recs)["ic"]
        yt, conc, tl = pair_status(pr[1])
        print(f"   {' '.join(extra) or 'default':28s}: CIGAR {pr[1].cigar}/{pr[2].cigar}, mapped outer distance {fl - 40}, clipped outer distance {fl}, YT {yt} FLAG&2 {int(conc)} TLEN {pr[1].tlen}/{pr[2].tlen}")

block1(); block2(); block3(); block4()

def block8():
    print("\n8. --local, junk on both 5' ends (outer clips), mapped outer distance 480, clipped outer distance 520, -X 500:")
    f0 = 64000; fl = 520
    g1 = refs[f0 + 20:f0 + 100]; g2 = revcomp(refs[f0 + fl - 100:f0 + fl - 20])
    j1 = "".join({"A": "C", "C": "A", "G": "T", "T": "G"}[b] for b in refs[f0:f0 + 20])
    j2 = "".join({"A": "C", "C": "A", "G": "T", "T": "G"}[b] for b in revcomp(refs[f0 + fl - 20:f0 + fl]))
    mates = [(("oc", j1 + g1, "I" * 100), ("oc", j2 + g2, "I" * 100))]
    res = {}
    for extra in ([], ["--soft-clipped-unmapped-tlen"]):
        recs, err = align(idx, mates=mates, args=["--local", "-X", "500"] + extra)
        pr = recs_by_pair(recs)["oc"]
        yt, conc, tl = pair_status(pr[1])
        res[tuple(extra)] = (conc, tl)
        print(f"   {' '.join(extra) or 'default':28s}: CIGAR {pr[1].cigar}/{pr[2].cigar}, YT {yt} FLAG&2 {int(conc)} TLEN {pr[1].tlen}/{pr[2].tlen}")
    conc, tl = res[()]
    report("block 8: a pair reported concordant under -X 500 has |TLEN| <= 500", (not conc) or abs(tl) <= 500,
           "" if (not conc) or abs(tl) <= 500 else f"(concordant with TLEN {tl}: -X bounds the mapped extent, TLEN includes the outer soft clips unless --soft-clipped-unmapped-tlen)")

block8()
