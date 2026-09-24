"""A1: the stderr alignment summary ("N reads; of these: ... overall alignment
rate") recomputed from the SAM records it describes, under the default mode,
--no-mixed, --no-discordant, -k 2, and with --un-conc/--al-conc/--un/--al
files whose record counts must match the summary lines.

Library: 400 pairs and 200 unpaired reads with a known mix of classes
(concordant unique, concordant in a duplicated region, discordant (wrong
orientation or too far), one mate unalignable (non-genomic), both unalignable,
one mate in a duplicated region while the other is unalignable).
"""
import random, sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(9)
G = 120000
ref = list(rand_seq(rng, G))
# a duplicated 2-kb region (exact copy) for multi-mappers
ref[100000:102000] = ref[50000:52000]
refs = "".join(ref)
d = tmpdir()
write_fasta(os.path.join(d, "ref.fa"), [("chr1", refs)])
idx = build_index(os.path.join(d, "ref.fa"), os.path.join(d, "ref"))
print(f"bowtie2 {version()}  reference {G} bp with one exact 2-kb duplication")

def junk(n):
    return "".join(rng.choice("ACGT") for _ in range(n))

pairs = []; classes = {}
def addpair(name, cls, m1, m2):
    pairs.append((m1, m2)); classes[name] = cls
k = 0
for i in range(150):   # concordant unique
    p = 2000 + i * 300; k += 1
    m1, m2 = mate_pair(f"cu{k}", refs, p, rng.randint(250, 450), 100, 100, edits1=[("mm", 40, "A")] if i % 3 == 0 else [])
    addpair(f"cu{k}", "conc_unique", fq(m1), fq(m2))
for i in range(60):    # concordant in the duplicated region -> two concordant placements
    p = 50000 + i * 25; k += 1
    m1, m2 = mate_pair(f"cd{k}", refs, p, 300, 100, 100)
    addpair(f"cd{k}", "conc_dup", fq(m1), fq(m2))
for i in range(50):    # discordant: too far apart (5 kb)
    p = 60000 + i * 60; k += 1
    m1 = make_read(f"df{k}", refs, p, 100, fw=True); m2 = make_read(f"df{k}", refs, p + 5000, 100, fw=False)
    addpair(f"df{k}", "discord", fq(m1), fq(m2))
for i in range(30):    # discordant: wrong orientation (both forward)
    p = 70000 + i * 60; k += 1
    m1 = make_read(f"do{k}", refs, p, 100, fw=True); m2 = make_read(f"do{k}", refs, p + 200, 100, fw=True)
    addpair(f"do{k}", "discord", fq(m1), fq(m2))
for i in range(50):    # mate 2 unalignable
    p = 75000 + i * 60; k += 1
    m1 = make_read(f"m1{k}", refs, p, 100, fw=True)
    addpair(f"m1{k}", "one_mate_unique", fq(m1), (f"m1{k}", junk(100), "I" * 100))
for i in range(30):    # mate 1 in the duplicated region, mate 2 unalignable
    p = 50500 + i * 30; k += 1
    m1 = make_read(f"md{k}", refs, p, 100, fw=True)
    addpair(f"md{k}", "one_mate_dup", fq(m1), (f"md{k}", junk(100), "I" * 100))
for i in range(30):    # both unalignable
    k += 1
    addpair(f"nn{k}", "none", (f"nn{k}", junk(100), "I" * 100), (f"nn{k}", junk(100), "I" * 100))
unp = []; uclasses = {}
for i in range(120):
    p = 80000 + i * 100
    rd = make_read(f"u{i}", refs, p, 100, fw=(i % 2 == 0)); unp.append(fq(rd)); uclasses[f"u{i}"] = "unique"
for i in range(40):
    p = 51000 + i * 20
    rd = make_read(f"ud{i}", refs, p, 100); unp.append(fq(rd)); uclasses[f"ud{i}"] = "dup"
for i in range(40):
    unp.append((f"un{i}", junk(100), "I" * 100)); uclasses[f"un{i}"] = "none"
print(f"library: {len(pairs)} pairs ({collections.Counter(classes.values())}), {len(unp)} unpaired ({collections.Counter(uclasses.values())})")

def sam_counts(recs):
    """Counts as the summary defines them, from the SAM: pairs by YT, mates of
    non-concordant/non-discordant pairs by alignment, unpaired reads."""
    by = {}
    for r in recs:
        if r.flag & 256:   # secondary (-k mode): the summary counts reads, not alignments
            by.setdefault((r.qname, r.flag & 192), []).append(r)
            continue
        by.setdefault((r.qname, r.flag & 192), []).insert(0, r)
    c = collections.Counter()
    pairs_seen = set()
    for (q, m), rs in by.items():
        r = rs[0]
        if m == 0:   # unpaired read
            c["unpaired"] += 1
            if r.flag & 4: c["unp0"] += 1
            elif r.tags.get("XS") is not None or len(rs) > 1: c["unpM"] += 1
            else: c["unp1"] += 1
            continue
        if q in pairs_seen: continue
        pairs_seen.add(q)
        c["paired"] += 1
        yt = r.tags.get("YT")
        if yt == "CP":
            multi = r.tags.get("XS") is not None or len(rs) > 1
            c["concM" if multi else "conc1"] += 1
        else:
            c["conc0"] += 1
            if yt == "DP": c["disc1"] += 1
            else:
                for mm in (64, 128):
                    rr = by[(q, mm)]
                    c["mates"] += 1
                    if rr[0].flag & 4: c["mate0"] += 1
                    elif rr[0].tags.get("XS") is not None or len(rr) > 1: c["mateM"] += 1
                    else: c["mate1"] += 1
    return c

def compare(label, args, expect_keys):
    recs, err = align(idx, mates=pairs, unpaired=unp, args=args)
    summ = parse_summary(err)
    c = sam_counts(recs)
    # what the SAM says about each class of pair
    ytc = collections.Counter()
    for r in recs:
        if r.flag & 64:
            ytc[(classes[r.qname], r.tags.get("YT"))] += 1
    print("   pair classes by YT:", dict(sorted(ytc.items())))
    md = [r for r in recs if classes.get(r.qname) == "one_mate_dup" and r.flag & 64]
    if md:
        print(f"   mate 1 of 'one_mate_dup' pairs (aligned in the exact 2-kb duplicate): MAPQ {collections.Counter(r.mapq for r in md)}, XS present {sum('XS' in r.tags for r in md)}/{len(md)}, YT {collections.Counter(r.tags.get('YT') for r in md)}")
    if md and "--no-mixed" not in args:
        report("mates aligned as unpaired (YT:Z:UP) with a second-best alignment (MAPQ 0/1, summary '>1 times') carry XS:i", all("XS" in r.tags for r in md if not r.flag & 4))
    mu = [r for r in recs if classes.get(r.qname) == "one_mate_unique" and r.flag & 64]
    if mu:
        print(f"   mate 1 of 'one_mate_unique' pairs: MAPQ {collections.Counter(r.mapq for r in mu)}, XS present {sum('XS' in r.tags for r in mu)}/{len(mu)}")
    # overall alignment rate as the summary defines it: aligned mates + aligned unpaired over all mates + unpaired
    aligned = 2 * (c["conc1"] + c["concM"] + c["disc1"]) + c["mate1"] + c["mateM"] + c["unp1"] + c["unpM"]
    total = 2 * c["paired"] + c["unpaired"]
    c["rate"] = round(100.0 * aligned / total, 2)
    c["reads"] = c["paired"] + c["unpaired"]
    ok = True
    for key in expect_keys:
        if summ.get(key) != c.get(key, 0):
            ok = False
            print(f"   {key}: summary {summ.get(key)} vs SAM {c.get(key, 0)}")
    print(f"   summary: {summ}")
    return report(f"{label}: summary lines match the SAM-derived counts", ok)

print("\ndefault (mixed mode, discordant search):")
compare("default", [], ["reads", "paired", "conc0", "conc1", "concM", "disc1", "mates", "mate0", "mate1", "mateM", "unpaired", "unp0", "unp1", "unpM", "rate"])
print("\n--no-mixed (manual: discordant alignments are still sought; only the per-mate fallback is disabled):")
compare("--no-mixed", ["--no-mixed"], ["reads", "paired", "conc0", "conc1", "concM", "disc1", "unpaired", "unp0", "unp1", "unpM", "rate"])
recs, err = align(idx, mates=pairs, args=["--no-mixed"])
ndp = sum(1 for r in recs if r.flag & 64 and r.tags.get("YT") == "DP")
report(f"--no-mixed still reports the 80 discordant pairs (found {ndp} YT:Z:DP; summary line 'aligned discordantly 1 time' = {parse_summary(err).get('disc1')})", ndp == 80)
print("\n--no-discordant:")
compare("--no-discordant", ["--no-discordant"], ["reads", "paired", "conc0", "conc1", "concM", "mates", "mate0", "mate1", "mateM", "unpaired", "unp0", "unp1", "unpM", "rate"])
print("\n--no-mixed --no-discordant:")
compare("--no-mixed --no-discordant", ["--no-mixed", "--no-discordant"], ["reads", "paired", "conc0", "conc1", "concM", "unpaired", "unp0", "unp1", "unpM", "rate"])
print("\n-k 2:")
compare("-k 2", ["-k", "2"], ["reads", "paired", "conc0", "conc1", "concM", "disc1", "mates", "mate0", "mate1", "mateM", "unpaired", "unp0", "unp1", "unpM", "rate"])

# --un-conc / --al-conc / --un / --al file counts
print("\n--un-conc/--al-conc/--un/--al record counts vs the summary:")
w = tmpdir()
recs, err = align(idx, mates=pairs, args=["--un-conc", os.path.join(w, "unconc.fq"), "--al-conc", os.path.join(w, "alconc.fq")], wrapper=True)
summ = parse_summary(err)
recs2, err2 = align(idx, unpaired=unp, args=["--un", os.path.join(w, "un.fq"), "--al", os.path.join(w, "al.fq")], wrapper=True)
summ.update({k: v for k, v in parse_summary(err2).items() if k.startswith("unp")})
def nrec(path):
    return sum(1 for _ in open(path)) // 4
counts = {os.path.basename(p): nrec(p) for p in sorted(glob.glob(os.path.join(w, "*.fq")))}
print(f"   files: {counts}")
ok = (counts.get("unconc.1.fq") == summ["conc0"] and counts.get("alconc.1.fq") == summ["conc1"] + summ["concM"]
      and counts.get("un.fq") == summ["unp0"] and counts.get("al.fq") == summ["unp1"] + summ["unpM"])
report("--un-conc = pairs aligned concordantly 0 times, --al-conc = the rest; --un/--al likewise for unpaired reads", ok)
