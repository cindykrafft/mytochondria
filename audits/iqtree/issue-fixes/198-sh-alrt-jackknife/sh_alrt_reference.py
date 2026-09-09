"""Independent SH-aLRT reference for one branch of the ML tree (issue #198).

Reads the ML tree (with 'SH-aLRT/UFBoot' labels), builds the two NNI neighbours of the
internal branch whose label is LABEL, has IQ-TREE compute site log-likelihoods for the three
trees (branch lengths re-optimised), then does the SH-aLRT RELL procedure of
PhyloTree::testOneBranch in numpy with three resampling schemes:
  bootstrap                     (what -alrt is defined with; unmodified IQ-TREE without -j/-J)
  delete-half jackknife         (what unmodified IQ-TREE 3.1.3 does when -j/-J is given)
  delete-half jackknife x 2     (jackknife pseudo-value, expectation restored)
Usage: python3 sh_alrt_reference.py <iqtree3> <aln> <treefile> <label> [reps] [seed]
"""
import re, subprocess, sys, os
import numpy as np

iqtree, aln, treefile, label = sys.argv[1:5]
reps = int(sys.argv[5]) if len(sys.argv) > 5 else 20000
seed = int(sys.argv[6]) if len(sys.argv) > 6 else 1

# --- minimal Newick parser -------------------------------------------------------------
class N:
    def __init__(s): s.ch=[]; s.name=""; s.bl=None; s.lab=""
def parse(t):
    i=0
    def node():
        nonlocal i
        n=N()
        if t[i]=='(':
            i+=1
            while True:
                n.ch.append(node())
                if t[i]==',': i+=1; continue
                if t[i]==')': i+=1; break
            m=re.match(r'[^:,;()]*', t[i:]); n.lab=m.group(0); i+=len(n.lab)
        else:
            m=re.match(r'[^:,;()]+', t[i:]); n.name=m.group(0); i+=len(n.name)
        if i < len(t) and t[i]==':':
            m=re.match(r':([^,;()]+)', t[i:]); n.bl=m.group(1); i+=len(m.group(0))
        return n
    return node()
def newick(n):
    s = ("("+",".join(newick(c) for c in n.ch)+")"+n.lab) if n.ch else n.name
    return s + (":"+n.bl if n.bl else "")
def find(n, lab, parent=None):
    if n.lab == lab: return n, parent
    for c in n.ch:
        r = find(c, lab, n)
        if r: return r
    return None

t = open(treefile).read().strip().rstrip(';')
root = parse(t)
node, parent = find(root, label)
assert node and parent and len(node.ch) == 2, "label not found on a binary internal node"
sibs = [c for c in parent.ch if c is not node]
assert sibs, "node is the root"
sib = sibs[0]
def strip(n):
    n.lab=""
    for c in n.ch: strip(c)
trees = {}
strip(root); trees["ml"] = newick(root)+";"
for k, child in enumerate(node.ch):
    # swap child k of the node with the sibling subtree
    ic = parent.ch.index(sib); jc = node.ch.index(child)
    parent.ch[ic], node.ch[jc] = child, sib
    trees["nni%d" % (k+1)] = newick(root)+";"
    parent.ch[ic], node.ch[jc] = sib, child   # undo

# --- site log-likelihoods from IQ-TREE ------------------------------------------------
sitelh = {}; lnl = {}
for k, nw in trees.items():
    open("ref_%s.nwk" % k, "w").write(nw + "\n")
    subprocess.run([iqtree, "-s", aln, "-te", "ref_%s.nwk" % k, "-m", "JC", "-wsl", "-T", "1",
                    "--prefix", "ref_%s" % k, "-redo", "-quiet"], check=True)
    line = [l for l in open("ref_%s.sitelh" % k) if l.startswith("Site_Lh")][0]
    sitelh[k] = np.array(line.split()[1:], float)
    lnl[k] = sitelh[k].sum()
print("log-likelihoods: ML %.4f  NNI1 %.4f  NNI2 %.4f" % (lnl["ml"], lnl["nni1"], lnl["nni2"]))
L = np.vstack([sitelh["ml"], sitelh["nni1"], sitelh["nni2"]])   # 3 x nsite
lh = L.sum(1)
aLRT = lh[0] - max(lh[1], lh[2])
n = L.shape[1]
rng = np.random.default_rng(seed)

def sh_alrt(sampler):
    ok = 0
    for r in range(reps):
        w = sampler()
        lh_new = L @ w
        cs = lh_new - lh
        s = np.sort(cs)[::-1]
        if aLRT > (s[0] - s[1]) + 0.05: ok += 1
    return 100.0 * ok / reps

def boot():
    return np.bincount(rng.integers(0, n, n), minlength=n).astype(float)
def jack():
    w = np.zeros(n); w[rng.choice(n, n // 2, replace=False)] = 1.0; return w
def jack2():
    return 2.0 * jack()

print("branch %s: aLRT = %.3f over %d sites, %d RELL replicates" % (label, aLRT, n, reps))
print("  bootstrap RELL               : SH-aLRT = %.1f" % sh_alrt(boot))
print("  delete-half jackknife RELL   : SH-aLRT = %.1f" % sh_alrt(jack))
print("  delete-half jackknife x 2    : SH-aLRT = %.1f" % sh_alrt(jack2))
