"""Independent GY94 log-likelihood for the 4-taxon tree with fixed branch lengths.
Q_ij = pi_j * kappa^[transition] * omega^[nonsynonymous] for single-nucleotide changes, 0 otherwise;
normalised so that -sum_i pi_i Q_ii = 1 (IQ-TREE's convention); Felsenstein pruning."""
import numpy as np, itertools, sys
from scipy.linalg import expm
code = {}
bases = "TCAG"; aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
for i,(a,b,c) in enumerate(itertools.product(bases,bases,bases)): code[a+b+c] = aa[i]
sense = [c for c in (a+b+c for a,b,c in itertools.product(bases,bases,bases)) if code[c] != "*"]   # TCAG order
def is_ts(x,y): return {x,y} in ({"A","G"},{"C","T"})
def Q(pi, kappa, omega, order):
    n=len(order); q=np.zeros((n,n))
    for i,ci in enumerate(order):
        for j,cj in enumerate(order):
            if i==j: continue
            diff=[(a,b) for a,b in zip(ci,cj) if a!=b]
            if len(diff)!=1: continue
            r=pi[j]
            if is_ts(*diff[0]): r*=kappa
            if code[ci]!=code[cj]: r*=omega
            q[i,j]=r
    q[np.diag_indices(n)] = -q.sum(1)
    q /= -(pi*np.diag(q)).sum()
    return q
def read_fasta(p):
    seqs={}; name=None
    for l in open(p):
        l=l.strip()
        if l.startswith(">"): name=l[1:]; seqs[name]=""
        else: seqs[name]+=l
    return seqs
seqs=read_fasta("aln.fasta"); nsite=len(seqs["A"])//3
def lnl(pi, order, kappa=1.07, omega=0.8, bl=(0.1,0.1,0.05,0.1,0.1,0.05)):
    idx={c:i for i,c in enumerate(order)}; n=len(order)
    P={k:expm(Q(pi,kappa,omega,order)*b) for k,b in zip("ABxCDy",bl)}
    total=0.0
    for s in range(nsite):
        L={}
        for t in "ABCD":
            v=np.zeros(n); v[idx[seqs[t][3*s:3*s+3]]]=1; L[t]=v
        Lx=(P["A"]@L["A"])*(P["B"]@L["B"]); Ly=(P["C"]@L["C"])*(P["D"]@L["D"])
        root=(P["x"]@Lx)*(P["y"]@Ly)          # rooted at the internal edge midpoint-equivalent: root on x side, y edge 0.05+0.05? see below
        total+=np.log(pi@root)
    return total
# The tree ((A,B):0.05,(C,D):0.05) has one internal branch of 0.1 total; place the root at the (A,B) node: edge to (C,D) node = 0.1, edge x = 0.
pi_u=np.full(61,1/61)
print("uniform +FU lnL (numpy):", lnl(pi_u, sense, bl=(0.1,0.1,0.0,0.1,0.1,0.1)))
skew=np.array([float(x) for x in open("freq_skew.txt").read().split(",")])
print("skew  +FU lnL (numpy, TCAG order):", lnl(skew, sense, bl=(0.1,0.1,0.0,0.1,0.1,0.1)))
order_acgt=[c for c in (a+b+c for a,b,c in itertools.product("ACGT","ACGT","ACGT")) if code[c]!="*"]
# the frequency vector was written in TCAG order; if IQ-TREE indexes states in ACGT order the same numbers land on different codons
pi_map=np.array([skew[sense.index(c)] for c in order_acgt])
print("skew  +FU lnL (numpy, numbers read in ACGT order):", lnl(pi_map, order_acgt, bl=(0.1,0.1,0.0,0.1,0.1,0.1)))
