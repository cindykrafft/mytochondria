#!/usr/bin/env python3
"""UFBoot2 (ultrafast bootstrap): seed reproducibility, thread dependence, and the
support percentages against the bootstrap trees the binary itself writes.

Design: an 8-taxon alignment (500 sites) simulated under JC here; `-B 1000 --boot-trees`
(the .ufboot file holds one tree per replicate). Checks:
  * same seed, same thread count, run twice -> identical .treefile and .ufboot;
  * support on each branch of the ML tree == 100 * (fraction of .ufboot trees containing
    that split), rounded to an integer as the report does;
  * -T 1 vs -T 2 with the same seed: are the supports / bootstrap trees identical?
    (recorded, not asserted: the code seeds per-thread streams);
  * --bnni: supports after NNI refinement, and the refined .ufboot trees again
    reproduce the printed supports;
  * SH-aLRT with the same seed, -T 1 vs -T 2 (recorded).
"""
import os, sys, re, math, hashlib
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iqt

print("binary:", iqt.IQTREE2); print(iqt.version())
D = os.path.join(iqt.RUNDIR, "ufboot"); os.makedirs(D, exist_ok=True)
rng = np.random.default_rng(11)
tree = "(((A:0.05,B:0.07):0.03,(C:0.06,D:0.04):0.02):0.03,((E:0.05,F:0.08):0.04,G:0.09):0.02,H:0.1);"
root = iqt.parse_newick(tree)
freqs = np.full(4, 0.25); Q = iqt.gtr_Q([1] * 6, freqs)
names, seqs = iqt.simulate(root, 500, Q, freqs, rng)
iqt.write_fasta(os.path.join(D, "aln.fa"), names, seqs)
taxa = sorted(names)

def md5(path): return hashlib.md5(open(path, "rb").read()).hexdigest()[:10]

def supports_from_treefile(path):
    """{split: reported support} from a tree with integer labels (or 'x/y' labels -> first field)."""
    s = open(path).read().strip()
    out = {}
    def walk(n, acc):
        if not n.children: return frozenset([n.name])
        cl = frozenset().union(*[walk(c, acc) for c in n.children])
        if n.name and 1 < len(cl) < len(taxa) - 1:
            other = frozenset(taxa) - cl
            key = min(cl, other, key=lambda x: (len(x), sorted(x)))
            acc[key] = n.name
        return cl
    walk(iqt.parse_newick(s), out)
    return out

def split_freqs(ufboot_path):
    trees = [l.strip() for l in open(ufboot_path) if l.strip()]
    cnt = {}
    for t in trees:
        for sp in iqt.splits_from_newick(t, taxa):
            cnt[sp] = cnt.get(sp, 0) + 1
    return cnt, len(trees)

def run_ufboot(prefix, extra):
    iqt.run(["-s", "aln.fa", "-m", "JC", "-B", "1000", "--boot-trees", "-seed", "3"] + extra, prefix, cwd=D)
    return supports_from_treefile(os.path.join(D, prefix + ".treefile")), split_freqs(os.path.join(D, prefix + ".ufboot"))

# 1. reproducibility
s1, (f1, n1) = run_ufboot("ub_t1_a", ["-T", "1"])
s2, (f2, n2) = run_ufboot("ub_t1_b", ["-T", "1"])
same = md5(os.path.join(D, "ub_t1_a.treefile")) == md5(os.path.join(D, "ub_t1_b.treefile")) and \
       md5(os.path.join(D, "ub_t1_a.ufboot")) == md5(os.path.join(D, "ub_t1_b.ufboot"))
print("1. same seed (-seed 3), -T 1, two runs: treefile and .ufboot identical -> %s" % same)
assert same
# 2. support == split frequency
print("2. supports vs split frequencies in the %d .ufboot trees (-T 1):" % n1)
ok = True
for sp, lab in sorted(s1.items(), key=lambda kv: sorted(kv[0])):
    k = f1.get(sp, 0); expect = int(math.floor(100.0 * k / n1 + 0.5))
    flag = "" if int(lab) == expect else "  <-- MISMATCH"; ok &= (int(lab) == expect)
    print("   %-14s reported %3s   %4d/%d = %.1f%% -> %d%s" % ("|".join(sorted(sp)), lab, k, n1, 100.0 * k / n1, expect, flag))
assert ok
# 3. thread dependence
s3, (f3, n3) = run_ufboot("ub_t2", ["-T", "2"])
print("3. same seed, -T 2: .ufboot identical to -T 1 -> %s; supports: %s" %
      (md5(os.path.join(D, "ub_t2.ufboot")) == md5(os.path.join(D, "ub_t1_a.ufboot")),
       {"|".join(sorted(sp)): (s1[sp], s3.get(sp, "absent")) for sp in s1}))
n_tie_diff = sum(1 for a, b in zip(open(os.path.join(D, "ub_t1_a.ufboot")), open(os.path.join(D, "ub_t2.ufboot"))) if a != b)
print("   replicate trees differing between -T 1 and -T 2: %d of %d" % (n_tie_diff, n1))
# 4. -bnni
s4, (f4, n4) = run_ufboot("ub_bnni", ["-T", "1", "--bnni"])
print("4. --bnni (-T 1): supports %s" % {"|".join(sorted(sp)): (s1[sp], s4.get(sp, "absent")) for sp in s1})
ok = True
for sp, lab in s4.items():
    k = f4.get(sp, 0); expect = int(math.floor(100.0 * k / n4 + 0.5)); ok &= (int(lab) == expect)
print("   --bnni supports equal split frequencies of the refined .ufboot trees -> %s" % ok)
assert ok
log = open(os.path.join(D, "ub_bnni.log")).read()
m = re.search(r"Total (\d+) ufboot trees refined", log); print("   log: %s" % (m.group(0) if m else "?"))
# 5. bootstrap correlation printed in the log
for p in ("ub_t1_a", "ub_t2"):
    log = open(os.path.join(D, p + ".log")).read()
    m = re.findall(r"Bootstrap correlation coefficient of split occurrence frequencies: ([0-9.]+)", log)
    print("5. %s: bootstrap correlation coefficient(s) in log: %s" % (p, m))
# 6. SH-aLRT thread dependence
def alrt(prefix, T):
    iqt.run(["-s", "aln.fa", "-m", "JC", "-alrt", "1000", "-seed", "3", "-T", str(T)], prefix, cwd=D)
    return supports_from_treefile(os.path.join(D, prefix + ".treefile"))
a1, a1b, a2 = alrt("sh_t1", 1), alrt("sh_t1b", 1), alrt("sh_t2", 2)
print("6. SH-aLRT -alrt 1000 -seed 3: -T 1 twice identical -> %s; -T 1 vs -T 2 identical -> %s" % (a1 == a1b, a1 == a2))
print("   -T 1: %s" % {"|".join(sorted(sp)): v for sp, v in a1.items()})
print("   -T 2: %s" % {"|".join(sorted(sp)): v for sp, v in a2.items()})
print("UFBOOT CHECKS DONE")
