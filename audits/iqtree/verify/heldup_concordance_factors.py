#!/usr/bin/env python3
"""Site and gene concordance factors (--scf / --gcf) against exact ports.

sCF (Minh, Hahn & Lanfear 2020): for each internal branch, quartets are drawn with one
taxon from each of the four subtrees around the branch; for each quartet the parsimony-
informative sites are split into the three quartet topologies; sCF is the mean over
quartets of the concordant fraction (x100), sN the mean number of decisive sites.
  * 4-taxon tree: only one quartet exists, so the reported sCF must equal the exact
    fraction regardless of --scf.
  * 6-taxon tree ((A,B),(C,D),(E,F)): every branch has four quartets; the exhaustive
    average is compared with --scf 20000 within Monte-Carlo error; a per-quartet dump
    (--cf-quartet) is checked exactly against the port.
gCF: a gene-tree set built here (topologies chosen by hand, some taxa missing) against
a port of tree/discordance.cpp:computeGeneConcordance (decisive = at least one taxon in
each of the four subtrees; concordant = the induced split is in the gene tree; gDF1/gDF2
the two NNI alternatives; gDFP the rest).
"""
import os, sys, re, itertools, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iqt

print("binary:", iqt.IQTREE2); print(iqt.version())
D = os.path.join(iqt.RUNDIR, "cf"); os.makedirs(D, exist_ok=True)
NUC = "ACGT"

def quartet_counts(seqs, q):
    a, b, c, d = (seqs[i] for i in q)
    n = [0, 0, 0]
    for i in range(len(a)):
        s = (a[i], b[i], c[i], d[i])
        if any(x not in NUC for x in s): continue
        if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]: n[0] += 1
        if s[0] == s[2] and s[1] == s[3] and s[0] != s[1]: n[1] += 1
        if s[0] == s[3] and s[1] == s[2] and s[0] != s[1]: n[2] += 1
    return n

def read_cf_stat(path):
    hdr = None; rows = {}
    for line in open(path):
        if line.startswith("#"): continue
        f = line.rstrip("\n").split("\t")
        if hdr is None: hdr = f; continue
        rows[int(f[0])] = dict(zip(hdr, f))
    return rows


def branch_keys(branch_tree_text, taxa):
    """Map branch ID (internal node name in the .cf.branch tree) -> the two-taxon side of its split."""
    root = iqt.parse_newick(branch_tree_text)
    out = {}
    def rec(n):
        if not n.children: return {n.name}
        cl = set().union(*[rec(c) for c in n.children])
        if n.name and n.name.isdigit():
            side = cl if len(cl) == 2 else set(taxa) - cl
            if len(side) == 2: out[int(n.name)] = "".join(sorted(side))
        return cl
    rec(root)
    return out

# ---------------- 4 taxa: exact
rng = np.random.default_rng(3)
freqs = np.full(4, 0.25); Q = iqt.gtr_Q([1] * 6, freqs)
root4 = iqt.parse_newick("((A:0.1,B:0.1):0.05,C:0.1,D:0.1);")
names, seqs = iqt.simulate(root4, 300, Q, freqs, rng)
iqt.write_fasta(os.path.join(D, "aln4.fa"), names, seqs)
# NOTE: "((A,B),(C,D));" has a bifurcating root, which IQ-TREE reads as a rooted tree and then
# skips the branch at the root ("2018-12-11: do not consider internal branch at the root"),
# reporting sCF = NA for the only internal branch. Recorded in the review; the unrooted form is used.
open(os.path.join(D, "t4r.nwk"), "w").write("((A,B),(C,D));\n")
iqt.run(["-t", "t4r.nwk", "-s", "aln4.fa", "--scf", "100", "-seed", "1", "-T", "1"], "cf4_rooted", cwd=D)
print("4 taxa, rooted-style Newick ((A,B),(C,D)): cf.stat rows ->",
      [(k, v["sCF"]) for k, v in read_cf_stat(os.path.join(D, "cf4_rooted.cf.stat")).items()],
      "| log:", [l.strip() for l in open(os.path.join(D, "cf4_rooted.log")) if "rooted tree" in l][:1])
open(os.path.join(D, "t4.nwk"), "w").write("(A,B,(C,D));\n")
n = quartet_counts(seqs, [0, 1, 2, 3])
for nq in (1, 100):
    iqt.run(["-t", "t4.nwk", "-s", "aln4.fa", "--scf", str(nq), "-seed", "1", "-T", "1"], "cf4_%d" % nq, cwd=D)
    row = list(read_cf_stat(os.path.join(D, "cf4_%d.cf.stat" % nq)).values())[0]
    exact = round(100.0 * n[0] / sum(n), 2)
    print("4 taxa --scf %-4d: reported sCF %s sDF1 %s sDF2 %s sN %s | exact counts %s -> sCF %.2f sN %d" %
          (nq, row["sCF"], row["sDF1"], row["sDF2"], row["sN"], n, exact, sum(n)))
    assert abs(float(row["sCF"]) - exact) < 0.011 and int(float(row["sN"])) == sum(n)

# ---------------- 6 taxa: exhaustive average vs sampled, plus per-quartet dump
rng = np.random.default_rng(4)
root6 = iqt.parse_newick("((A:0.1,B:0.1):0.04,(C:0.1,D:0.1):0.04,(E:0.1,F:0.1):0.04);")
names, seqs = iqt.simulate(root6, 400, Q, freqs, rng)
iqt.write_fasta(os.path.join(D, "aln6.fa"), names, seqs)
open(os.path.join(D, "t6.nwk"), "w").write("((A,B),(C,D),(E,F));\n")
idx = {nm: i for i, nm in enumerate(names)}
# branch AB|CDEF: quartets A,B x {C,D} x {E,F}; branch CD|..: C,D x {A,B} x {E,F}; EF: E,F x {A,B} x {C,D}
branches = {"AB": (["A"], ["B"], ["C", "D"], ["E", "F"]), "CD": (["C"], ["D"], ["A", "B"], ["E", "F"]),
            "EF": (["E"], ["F"], ["A", "B"], ["C", "D"])}
exact = {}
for key, (s1, s2, s3, s4) in branches.items():
    vals = []
    for q in itertools.product(s1, s2, s3, s4):
        c = quartet_counts(seqs, [idx[x] for x in q]); vals.append((100.0 * c[0] / sum(c), sum(c)))
    exact[key] = (np.mean([v[0] for v in vals]), np.mean([v[1] for v in vals]), np.std([v[0] for v in vals]))
R = 20000
iqt.run(["-t", "t6.nwk", "-s", "aln6.fa", "--scf", str(R), "-seed", "1", "-T", "1"], "cf6", cwd=D)
rows = read_cf_stat(os.path.join(D, "cf6.cf.stat"))
tree_ids = open(os.path.join(D, "cf6.cf.branch")).read()
print("6 taxa --scf %d: branch table" % R)
keys = branch_keys(tree_ids, list("ABCDEF"))
for bid, row in rows.items():
    key = keys.get(bid, "?")
    ex = exact.get(key, (float("nan"),) * 3)
    se = ex[2] / math.sqrt(R) * 3
    print("   branch %d (%s): reported sCF %s sN %s | exhaustive mean over 4 quartets sCF %.2f sN %.2f" % (bid, key, row["sCF"], row["sN"], ex[0], ex[1]))
    assert abs(float(row["sCF"]) - ex[0]) < max(3 * ex[2] / math.sqrt(R), 0.02) + 0.01
# --cf-quartet writes one row per sampled quartet to .cf.quartet (ID, QuartID, Seq1..Seq4 as
# 1-based sequence IDs, qCF, qCF_N, qDF1, qDF1_N, qDF2, qDF2_N, qN); every row is checked exactly.
iqt.run(["-t", "t6.nwk", "-s", "aln6.fa", "--scf", "50", "--cf-quartet", "-seed", "2", "-T", "1"], "cf6q", cwd=D)
nq = 0
for line in open(os.path.join(D, "cf6q.cf.quartet")):
    if line.startswith("#") or line.startswith("ID"): continue
    f = line.split()
    q = [int(x) - 1 for x in f[2:6]]
    c = quartet_counts(seqs, q)
    assert [int(f[7]), int(f[9]), int(f[11]), int(f[12])] == c + [sum(c)], (line, c)
    nq += 1
print("   --cf-quartet 50: %d sampled quartets in .cf.quartet, all site counts (qCF_N, qDF1_N, qDF2_N, qN) equal the port's" % nq)

# ---------------- gCF
# NOTE: a 4-taxon gene tree written "((A,B),(C,D));" (bifurcating root) makes --gcf abort with
# "ERROR: Taxon not found in full tree: __root__" (rooted input trees get a __root__ leaf);
# the unrooted spelling is used here and the abort is recorded in the review.
gene_trees = ["((A,B),(C,D),(E,F));"] * 5 + ["((A,C),(B,D),(E,F));"] * 2 + ["((A,D),(B,C),(E,F));"] * 1 + \
             ["((A,B),(C,E),(D,F));"] * 2 + ["((A,B),C,(E,F));", "((A,E),(B,F),(C,D));", "(A,(C,D),(E,F));", "(A,B,(C,D));"] + \
             ["(A,(C,D),(B,(E,F)));"] * 2 + ["(A,(E,F),(B,(C,D)));"]   # NNI neighbours of AB|CDEF: ACD|BEF and AEF|BCD
open(os.path.join(D, "genes_rooted.nwk"), "w").write("((A,B),(C,D));\n")
try:
    iqt.run(["-t", "t6.nwk", "--gcf", "genes_rooted.nwk", "-seed", "1", "-T", "1"], "gcf_rooted", cwd=D)
    print("gCF with a rooted 4-taxon gene tree: completed")
except RuntimeError as e:
    print("gCF with a rooted 4-taxon gene tree ((A,B),(C,D)): %s" % re.findall(r"ERROR[^\n]*", str(e))[:1])
open(os.path.join(D, "genes.nwk"), "w").write("\n".join(gene_trees) + "\n")
iqt.run(["-t", "t6.nwk", "--gcf", "genes.nwk", "-seed", "1", "-T", "1"], "gcf6", cwd=D)
rows = read_cf_stat(os.path.join(D, "gcf6.cf.stat"))
tree_ids = open(os.path.join(D, "gcf6.cf.branch")).read()
taxa6 = list("ABCDEF")
def gcf_port(sub):  # sub = four taxon sets (s1,s2 | s3,s4)
    gN = gC = g1 = g2 = 0
    for gt in gene_trees:
        tx = set(re.findall(r"[A-F]", gt))
        if not all(tx & set(s) for s in sub): continue
        gN += 1
        sp = iqt.splits_from_newick(gt, sorted(tx))
        def has(x):
            x = frozenset(x) & tx; y = tx - x
            return min(x, y, key=lambda z: (len(z), sorted(z))) in sp
        if has(sub[0] + sub[1]): gC += 1
        elif has(sub[0] + sub[2]): g1 += 1
        elif has(sub[0] + sub[3]): g2 += 1
    return gN, gC, g1, g2, gN - gC - g1 - g2
print("gCF on %d gene trees" % len(gene_trees))
keys = branch_keys(tree_ids, list("ABCDEF"))
for bid, row in rows.items():
    key = keys[bid]
    gN, gC, g1, g2, gP = gcf_port(branches[key])
    rep = (int(row["gN"]), int(row["gCF_N"]), int(row["gDF1_N"]), int(row["gDF2_N"]), int(row["gDFP_N"]))
    print("   branch %d (%s): reported gN %s gCF %s gCF_N %s gDF1_N %s gDF2_N %s gDFP_N %s | port gN %d gC %d gDF1 %d gDF2 %d gDFP %d" %
          (bid, key, row["gN"], row["gCF"], row["gCF_N"], row["gDF1_N"], row["gDF2_N"], row["gDFP_N"], gN, gC, g1, g2, gP))
    assert rep == (gN, gC, g1, g2, gP) and abs(float(row["gCF"]) - round(100.0 * gC / gN, 2)) < 0.011
print("\nALL CONCORDANCE-FACTOR CHECKS PASSED")
