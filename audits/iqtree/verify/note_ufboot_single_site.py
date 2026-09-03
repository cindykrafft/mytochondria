#!/usr/bin/env python3
"""UFBoot versus the standard bootstrap on a branch supported by very few sites.

Design: 6 taxa; 500 sites simulated under JC on a tree whose internal branch (AB|CDEF) has
length ZERO (so no site supports it), then k additional parsimony-informative sites that
support AB|CDEF are appended (k = 1, 2, 4). The other two internal branches are well
supported. Reference for the k-site branch: the fraction of standard-bootstrap replicates
containing at least one of the k sites is 1-(1-k/n)^n; IQ-TREE's own standard bootstrap
(-b 200) is run as the empirical reference, and the UFBoot replicate trees (.ufboot) are
inspected to see which topologies the replicates were assigned.
"""
import os, sys, re, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iqt

print("binary:", iqt.IQTREE2); print(iqt.version())
D = os.path.join(iqt.RUNDIR, "single_site"); os.makedirs(D, exist_ok=True)
rng = np.random.default_rng(21)
freqs = np.full(4, 0.25); Q = iqt.gtr_Q([1] * 6, freqs)
root = iqt.parse_newick("((A:0.05,B:0.05):0.0,(C:0.05,D:0.05):0.06,(E:0.05,F:0.05):0.06);")
names, seqs = iqt.simulate(root, 500, Q, freqs, rng)
taxa = sorted(names)
def supports(path):
    s = open(path).read().strip(); out = {}
    def walk(n):
        if not n.children: return frozenset([n.name])
        cl = frozenset().union(*[walk(c) for c in n.children])
        if n.name and 1 < len(cl) < len(taxa) - 1:
            other = frozenset(taxa) - cl
            out[min(cl, other, key=lambda x: (len(x), sorted(x)))] = n.name
        return cl
    walk(iqt.parse_newick(s)); return out
key = frozenset(["A", "B"])
for k in (1, 2, 4):
    extra = {nm: ("C" if nm in ("A", "B") else "A") * k for nm in names}   # AABB-type sites
    seqs_k = [s + extra[nm] for s, nm in zip(seqs, names)]
    n = len(seqs_k[0]); aln = "aln_k%d.fa" % k
    iqt.write_fasta(os.path.join(D, aln), names, seqs_k)
    expect = 100 * (1 - (1 - k / n) ** n)
    iqt.run(["-s", aln, "-m", "JC", "-B", "1000", "--boot-trees", "-seed", "1", "-T", "1"], "ub_k%d" % k, cwd=D)
    ub = supports(os.path.join(D, "ub_k%d.treefile" % k))
    trees = [l.strip() for l in open(os.path.join(D, "ub_k%d.ufboot" % k)) if l.strip()]
    topo = {}
    for t in trees:
        two = [x for x in iqt.splits_from_newick(t, taxa) if len(x) == 2 and x not in (frozenset("CD"), frozenset("EF"))]
        sp = ",".join(sorted("".join(sorted(x)) for x in two)) or "(none)"
        topo[sp] = topo.get(sp, 0) + 1
    iqt.run(["-s", aln, "-m", "JC", "-b", "200", "-seed", "1", "-T", "1"], "sb_k%d" % k, cwd=D)
    sb = supports(os.path.join(D, "sb_k%d.treefile" % k))
    log = open(os.path.join(D, "ub_k%d.log" % k)).read()
    ncand = re.findall(r"(\d+) (?:candidate )?trees? (?:examined|evaluated|processed)[^\n]*", log)
    print("k=%d supporting sites of %d: AB|CDEF UFBoot %s%%  standard -b 200 %s%%  P(replicate has >=1 site) %.1f%%" %
          (k, n, ub.get(key, "absent"), sb.get(key, "absent"), expect))
    print("   other branches: UFBoot %s  standard %s" % ({"|".join(sorted(s)): v for s, v in ub.items() if s != key},
                                                          {"|".join(sorted(s)): v for s, v in sb.items() if s != key}))
    print("   .ufboot: A/B-side split of each replicate tree: %s" % topo)
    print("   log: %s" % (ncand[:2] if ncand else [l.strip() for l in log.splitlines() if "UFBoot" in l or "logl" in l.lower()][:3]))
print("DONE")
