"""N1: nhmmer E-values, -Z (megabases), strands, threads, coordinates.

Truth: nhmmer converts a window P-value to an E-value with E = P * N / W, where N is the
number of residues searched (both strands unless --watson/--crick) and W = the model's MAXL
(p7_tophits_ComputeNhmmerEvalues, nhmmer.c). The man page: '-Z <x>: assert that the total
size of the target sequence database is <x> million bases (Mb), rather than the actual number
of residues searched'. So -Z equal to the true one-strand size must reproduce the default
E-values exactly; P = exp(-lambda (s - tau)) from the HMM's STATS LOCAL FORWARD line.
Homologous segments are MADE1 core emissions inserted into Python-random DNA at recorded
positions, half of them reverse-complemented.
"""
import os, random
import _hm

R = _hm.Report("N1 nhmmer E-values, -Z, strands, threads, coordinates")
hmmf = os.path.join(_hm.TUT, "MADE1.hmm")
H = _hm.read_hmms(hmmf)[0]
tau, lam = H["stats"]["FORWARD"]; W = H["maxl"]
comp = {"A": "T", "C": "G", "G": "C", "T": "A"}
rc = lambda s: "".join(comp[c] for c in reversed(s))

rng = random.Random(5)
inserts = _hm.emit_core(hmmf, 40, 9)
seqs, truth, total = [], [], 0
for i in range(8):                       # 8 sequences, 250 kb each = 2.000000 Mb exactly
    L = 250000
    s = list(_hm.rand_dna(rng, L))
    pos = sorted(rng.sample(range(1000, L - 1000, 5000), 5))
    for j, p in enumerate(pos):
        d = inserts[i * 5 + j]
        strand = "+" if (i + j) % 2 == 0 else "-"
        seg = d if strand == "+" else rc(d)
        s[p:p + len(seg)] = list(seg)     # overwrite, length preserved
        truth.append(("chr%d" % i, strand, p + 1, p + len(seg)))
    seqs.append(("chr%d" % i, "".join(s))); total += L
db = _hm.write_fasta(_hm.path("dna.fa"), seqs)
R.note("database: %d sequences, %d residues (%.6f Mb), %d inserts, W=MAXL=%d" % (len(seqs), total, total / 1e6, len(truth), W))


def nh(extra, tag):
    tb = _hm.path("nh_%s.tbl" % tag)
    _hm.run([_hm.prog("nhmmer"), "-o", "/dev/null", "--tblout", tb] + extra + [hmmf, db])
    return _hm.read_nhmmer_tbl(tb)


def key(r): return (r["t"], r["af"], r["at"])


base = nh([], "default")
R.note("default: %d hits" % len(base))
old = "3.1b2" in _hm.version()          # 3.1b2 spells the strand options --toponly/--bottomonly
TOP, BOT = ("--toponly", "--bottomonly") if old else ("--watson", "--crick")
for strands, N, lab in (([], 2 * total, "both strands"), ([TOP], total, TOP), ([BOT], total, BOT)):
    rows = nh(strands, "f" + lab.strip("-")) if strands else base
    nbad = [r for r in rows if not _hm.eval_close(r["E"], _hm.exp_surv(r["sc"], tau, lam) * N / W, lam=lam)]
    R.check(rows and not nbad, "%s: E = P(score) * %d / %d for %d hits" % (lab, N, W, len(rows)),
            "%d mismatches, e.g. %s" % (len(nbad), nbad[:1]))
    rz = nh(strands + ["-Z", "%.6f" % (total / 1e6)], "Z" + lab.strip("-"))
    a = {key(r): r["E"] for r in rows}; b = {key(r): r["E"] for r in rz}
    diff = [(k, a[k], b.get(k)) for k in a if b.get(k) != a[k]]
    R.check(not diff and set(a) == set(b), "%s: -Z %.6f (true size) reproduces the default E-values" % (lab, total / 1e6),
            "%d differ, e.g. %s" % (len(diff), diff[:2]))
    rz10 = nh(strands + ["-Z", "%.6f" % (10 * total / 1e6), "-E", "1000"], "Z10" + lab.strip("-"))
    b = {key(r): r["E"] for r in rz10}
    ratios = [b[k] / a[k] for k in a if k in b and a[k] > 0]
    R.check(ratios and all(abs(x / 10 - 1) < 0.06 for x in ratios), "%s: -Z 10x true size scales E by 10" % lab,
            "ratios %.3f-%.3f" % (min(ratios), max(ratios)) if ratios else "none")

for c in ("0", "1", "4"):
    rows = nh(["--cpu", c], "cpu" + c)
    same = sorted((key(r), r["E"], r["sc"]) for r in rows) == sorted((key(r), r["E"], r["sc"]) for r in base)
    R.check(same, "--cpu %s gives the same hits, scores and E-values as the default" % c)
rows = nh(["--block_length", "60000"], "blk")
same = sorted((key(r), r["E"], r["sc"]) for r in rows) == sorted((key(r), r["E"], r["sc"]) for r in base)
R.check(same, "--block_length 60000 gives the same hits, scores and E-values as the default",
        "%d vs %d hits" % (len(rows), len(base)))

# coordinates: every insert found once, on the right strand, alignment inside the inserted segment (+/- envelope slack)
found = 0; wrong = []
for (chrom, strand, a, b) in truth:
    hits = [r for r in base if r["t"] == chrom and r["strand"].strip() == strand and
            min(r["af"], r["at"]) <= b and max(r["af"], r["at"]) >= a]
    if len(hits) == 1:
        r = hits[0]; found += 1
        lo, hi = min(r["af"], r["at"]), max(r["af"], r["at"])
        orient_ok = (r["af"] < r["at"]) if strand == "+" else (r["af"] > r["at"])
        if not (orient_ok and lo >= a - 5 and hi <= b + 5 and r["sqlen"] == 250000): wrong.append((chrom, strand, a, b, r["af"], r["at"], r["sqlen"]))
R.check(not wrong, "every insert hit on its own strand has orientation, ali coords inside the insert and sq len right (%d of %d inserts hit)" % (found, len(truth)),
        "wrong: %s" % wrong[:3])
badenv = [r for r in base if not ((r["ef"] <= r["af"] <= r["at"] <= r["et"]) if r["strand"].strip() == "+" else (r["ef"] >= r["af"] >= r["at"] >= r["et"]))]
R.check(not badenv, "envelope contains the alignment on both strands (+: envfrom<=alifrom<=alito<=envto; -: reversed) for %d hits" % len(base), "%s" % badenv[:2])
R.note("MADE1 is a MITE with terminal inverted repeats, so most inserts also give a weaker hit on the opposite strand; not checked")
R.done()
