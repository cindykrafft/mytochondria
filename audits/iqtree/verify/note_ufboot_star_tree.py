#!/usr/bin/env python3
"""UFBoot on alignments with no phylogenetic signal for an internal branch (star tree),
for 4, 5 and 6 taxa, against IQ-TREE's standard bootstrap (-b 200).

Motivation: on a 4-taxon alignment with a single informative site UFBoot reported 100%
support and every one of the 1000 .ufboot trees was the ML topology
(note_degenerate_alignments.py), while the same construction with 6 taxa tracked the
standard bootstrap (note_ufboot_single_site.py). Here the sequences are simulated on a
star tree (all internal branches zero), so no split is truly supported, and the reported
supports and the composition of the .ufboot trees are recorded for each taxon count.
"""
import os, sys, re
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iqt

print("binary:", iqt.IQTREE2); print(iqt.version())
D = os.path.join(iqt.RUNDIR, "star"); os.makedirs(D, exist_ok=True)
freqs = np.full(4, 0.25); Q = iqt.gtr_Q([1] * 6, freqs)
def labels(path):
    return re.findall(r"\)([0-9.]+)", open(path).read())
for ntax in (4, 5, 6):
    taxa = [chr(65 + i) for i in range(ntax)]
    for seed in (1, 2):
        rng = np.random.default_rng(100 * ntax + seed)
        root = iqt.parse_newick("(" + ",".join("%s:0.1" % t for t in taxa) + ");")
        names, seqs = iqt.simulate(root, 500, Q, freqs, rng)
        aln = "star%d_%d.fa" % (ntax, seed); iqt.write_fasta(os.path.join(D, aln), names, seqs)
        iqt.run(["-s", aln, "-m", "JC", "-B", "1000", "--boot-trees", "-seed", "1", "-T", "1"], "ub_%d_%d" % (ntax, seed), cwd=D)
        iqt.run(["-s", aln, "-m", "JC", "-b", "200", "-seed", "1", "-T", "1"], "sb_%d_%d" % (ntax, seed), cwd=D)
        trees = [l.strip() for l in open(os.path.join(D, "ub_%d_%d.ufboot" % (ntax, seed))) if l.strip()]
        topos = {}
        for t in trees:
            key = ";".join(sorted("".join(sorted(s)) for s in iqt.splits_from_newick(t, taxa)))
            topos[key] = topos.get(key, 0) + 1
        ml = re.sub(r":[0-9.e-]+", "", open(os.path.join(D, "ub_%d_%d.treefile" % (ntax, seed))).read().strip())
        log = open(os.path.join(D, "ub_%d_%d.log" % (ntax, seed))).read()
        cand = re.findall(r"(\d+) (?:initial |candidate )?trees?[^\n]*", log)[:2]
        print("%d taxa, replicate alignment %d: ML tree %s" % (ntax, seed, ml))
        print("   UFBoot supports %s   standard bootstrap supports %s" % (labels(os.path.join(D, "ub_%d_%d.treefile" % (ntax, seed))),
                                                                          labels(os.path.join(D, "sb_%d_%d.treefile" % (ntax, seed)))))
        print("   distinct topologies among the 1000 .ufboot trees: %d  (most common %d)" % (len(topos), max(topos.values())))
        print("   log lines: %s" % cand)
print("DONE")
