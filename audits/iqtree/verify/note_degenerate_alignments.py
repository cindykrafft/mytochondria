#!/usr/bin/env python3
"""Degenerate inputs the brief asked about, run on the shipped binary and recorded:
  A. 4 taxa, 100 constant sites (of all four states, so any bootstrap replicate keeps more
     than one state) + 1 parsimony-informative site (AABB pattern): what do
     UFBoot (-B 1000), SH-aLRT and aBayes report for the single internal branch?
     Reference: the informative site is in a bootstrap replicate with probability
     1-(1-1/101)^101 = 63.4%; replicates without it have all three topologies tied.
     IQ-TREE's standard bootstrap (-b 200) is run on the same alignment for comparison,
     and the UFBoot log-likelihood cutoff (tree/iqtree.cpp:2295, trees more than 1 log-
     likelihood unit below it are never assigned to a replicate, :3553) is printed.
  B. 4 taxa, all sites constant: does the run complete, and what are the supports?
  C. Two identical sequences among 5 taxa: IQ-TREE removes duplicates before the
     search and reinserts them; check the tree still contains both and the reported
     likelihood equals the reference at the printed branch lengths.
"""
import os, sys, re, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iqt

print("binary:", iqt.IQTREE2); print(iqt.version())
D = os.path.join(iqt.RUNDIR, "degenerate"); os.makedirs(D, exist_ok=True)
names = ["A", "B", "C", "D"]

# A
const = "ACGT" * 25                      # 100 constant columns (identical across taxa, states vary across columns)
seqs = [const + "A", const + "A", const + "C", const + "C"]
iqt.write_fasta(os.path.join(D, "one_site.fa"), names, seqs)
for seed in (1, 2, 3):
    out, rep = iqt.run(["-s", "one_site.fa", "-m", "JC", "-B", "1000", "-alrt", "1000", "-abayes", "-seed", str(seed), "-T", "1", "--boot-trees"], "one_site_%d" % seed, cwd=D)
    tf = open(os.path.join(D, "one_site_%d.treefile" % seed)).read().strip()
    trees = [l.strip() for l in open(os.path.join(D, "one_site_%d.ufboot" % seed)) if l.strip()]
    cnt = {}
    for t in trees:
        for sp in iqt.splits_from_newick(t, names): cnt["|".join(sorted(sp))] = cnt.get("|".join(sorted(sp)), 0) + 1
    iqt.run(["-s", "one_site.fa", "-m", "JC", "-b", "200", "-seed", str(seed), "-T", "1"], "one_site_sb_%d" % seed, cwd=D)
    sb = re.findall(r"\)([0-9.]+):", open(os.path.join(D, "one_site_sb_%d.treefile" % seed)).read())
    print("A. seed %d: tree %s   (labels: SH-aLRT/aBayes/UFBoot)" % (seed, tf))
    print("   .ufboot split counts: %s  (P(site in replicate) = %.1f%%);  standard bootstrap -b 200: %s%%" % (cnt, 100 * (1 - (1 - 1 / 101) ** 101), sb))
    log = open(os.path.join(D, "one_site_%d.log" % seed)).read()
    print("   log: %s" % re.findall(r"Log-likelihood cutoff on original alignment: [-0-9.]+", log)[:1])
# mechanism: log-likelihoods of the two alternative topologies (all branches optimised) vs the cutoff
for t, nwk in (("alt1", "((A,C),(B,D));"), ("alt2", "((A,D),(B,C));"), ("ml", "((A,B),(C,D));")):
    open(os.path.join(D, t + ".nwk"), "w").write(nwk + "\n")
    out, rep = iqt.run(["-s", "one_site.fa", "-te", t + ".nwk", "-m", "JC", "-T", "1"], "one_site_" + t, cwd=D)
    print("   -te %-16s logL %.4f" % (nwk, iqt.report_value(rep, "Log-likelihood of the tree")))
print("   (tree/iqtree.cpp:3553: a tree is never assigned to a replicate if its original-alignment logL < cutoff - 1)")
# B
seqs = ["ACGT" * 25] * 4
iqt.write_fasta(os.path.join(D, "const.fa"), names, seqs)
try:
    out, rep = iqt.run(["-s", "const.fa", "-m", "JC", "-B", "1000", "-alrt", "1000", "-seed", "1", "-T", "1"], "const", cwd=D)
    print("B. all-constant alignment: completed; tree %s" % open(os.path.join(D, "const.treefile")).read().strip())
    print("   warnings: %s" % [l.strip() for l in open(os.path.join(D, "const.log")) if "WARNING" in l][:4])
except RuntimeError as e:
    print("B. all-constant alignment: refused -> %s" % re.findall(r"ERROR[^\n]*", str(e))[:2])
# C
rng = np.random.default_rng(5)
root = iqt.parse_newick("((A:0.1,B:0.1):0.05,C:0.1,D:0.1);")
freqs = np.full(4, 0.25); Q = iqt.gtr_Q([1] * 6, freqs)
n4, s4 = iqt.simulate(root, 300, Q, freqs, rng)
n5 = n4 + ["E"]; s5 = s4 + [s4[0]]           # E identical to A
iqt.write_fasta(os.path.join(D, "dup.fa"), n5, s5)
out, rep = iqt.run(["-s", "dup.fa", "-m", "JC", "-seed", "1", "-T", "1", "-B", "1000"], "dup", cwd=D)
tf = open(os.path.join(D, "dup.treefile")).read().strip()
L = iqt.report_value(rep, "Log-likelihood of the tree")
pats, w = iqt.patterns_from_seqs(s5)
ref = iqt.loglik(iqt.parse_newick(re.sub(r"\)\d+:", "):", tf)), pats, w, Q, freqs)
print("C. duplicate sequence (E == A): tree %s" % tf)
print("   log: %s" % [l.strip() for l in open(os.path.join(D, "dup.log")) if "identical" in l.lower()][:3])
print("   reported logL %.4f; reference at the printed branch lengths %.4f; diff %.1e" % (L, ref, L - ref))
print("DEGENERATE-INPUT CHECKS DONE")
