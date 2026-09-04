"""Shared helpers for the IQ-TREE 2 verification harnesses.

Runs the shipped binary (path from $IQTREE2, default: the project's master build) on
synthetic alignments made here, and provides an independent numpy implementation of
the phylogenetic likelihood (Felsenstein pruning under a time-reversible model with
discrete-gamma / invariable-site / Lewis +ASC extensions) as the reference.
"""
import os, re, subprocess, sys, math, itertools
import numpy as np

SCRATCH = "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/iqtree"
IQTREE2 = os.environ.get("IQTREE2", SCRATCH + "/iqtree2/build/iqtree2")
RUNDIR = os.environ.get("IQTREE_RUNDIR", SCRATCH + "/runs")
NUC = "ACGT"

def run(args, prefix, cwd=None, quiet=True):
    """Run iqtree2 with -pre prefix; returns (stdout, iqtree_report_text)."""
    cwd = cwd or RUNDIR
    os.makedirs(cwd, exist_ok=True)
    cmd = [IQTREE2] + list(args) + ["-pre", prefix, "-redo"] + (["-quiet"] if quiet else [])
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("iqtree2 failed (%d): %s\n%s\n%s" % (p.returncode, " ".join(cmd), p.stdout[-2000:], p.stderr[-2000:]))
    rep = open(os.path.join(cwd, prefix + ".iqtree")).read() if os.path.exists(os.path.join(cwd, prefix + ".iqtree")) else ""
    return p.stdout, rep

def version():
    return subprocess.run([IQTREE2, "--version"], capture_output=True, text=True).stdout.splitlines()[0]

def write_fasta(path, names, seqs):
    with open(path, "w") as fh:
        for n, s in zip(names, seqs):
            fh.write(">%s\n%s\n" % (n, s))

# ---------------------------------------------------------------- model matrices
def gtr_Q(rates, freqs):
    """GTR rate matrix, rates order (AC, AG, AT, CG, CT, GT), normalised to 1 subst/site."""
    r = np.zeros((4, 4))
    idx = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    for k, (i, j) in enumerate(idx):
        r[i, j] = r[j, i] = rates[k]
    Q = r * np.asarray(freqs)[None, :]
    np.fill_diagonal(Q, -Q.sum(axis=1))
    mu = -np.dot(freqs, np.diag(Q))
    return Q / mu

def P_matrix(Q, t):
    w, V = np.linalg.eig(Q)
    return np.real(V @ np.diag(np.exp(w * t)) @ np.linalg.inv(V))

# ---------------------------------------------------------------- discrete gamma
def gamma_rates_mean(alpha, k):
    """Yang (1994) discrete gamma, mean of each of k equal-probability bins (eqs 9-10)."""
    from scipy.stats import gamma as G
    from scipy.special import gammainc
    cuts = G.ppf(np.arange(1, k) / k, alpha, scale=1.0 / alpha)
    # E[r | bin] = k * (F_{alpha+1}(cut_i) - F_{alpha+1}(cut_{i-1})), F_{a+1} the gamma(a+1, 1/a) cdf
    F = np.concatenate([[0.0], gammainc(alpha + 1, cuts * alpha), [1.0]])
    return k * np.diff(F)

def gamma_rates_median(alpha, k):
    """Yang (1994) median variant: the (2i+1)/(2k) quantiles, rescaled to mean 1."""
    from scipy.stats import gamma as G
    q = G.ppf((2 * np.arange(k) + 1) / (2.0 * k), alpha, scale=1.0 / alpha)
    return q * k / q.sum()

# ---------------------------------------------------------------- trees
class Node:
    def __init__(self, name=None):
        self.name, self.children, self.length = name, [], 0.0

def parse_newick(s):
    """Minimal Newick parser: returns root Node; branch lengths on children."""
    s = s.strip().rstrip(";")
    pos = [0]
    def node():
        n = Node()
        if s[pos[0]] == "(":
            pos[0] += 1
            while True:
                n.children.append(node())
                if s[pos[0]] == ",":
                    pos[0] += 1; continue
                if s[pos[0]] == ")":
                    pos[0] += 1; break
        m = re.match(r"[^:,()\[\]]*", s[pos[0]:])
        n.name = m.group(0) or None
        pos[0] += len(m.group(0))
        if pos[0] < len(s) and s[pos[0]] == "[":   # skip annotations
            e = s.index("]", pos[0]); pos[0] = e + 1
        if pos[0] < len(s) and s[pos[0]] == ":":
            m = re.match(r":([-+0-9.eE]+)", s[pos[0]:])
            n.length = float(m.group(1)); pos[0] += len(m.group(0))
        return n
    return node()

def leaves(n):
    return [n] if not n.children else [l for c in n.children for l in leaves(c)]

def site_pattern_likelihoods(root, patterns, Q, freqs, rate=1.0):
    """Felsenstein pruning; patterns: array (npat, ntaxa) of state ints (-1 = gap/unknown);
    taxa order = order of leaf names in `names` mapping. Returns per-pattern likelihoods."""
    names = [l.name for l in leaves(root)]
    def partial(n):
        if not n.children:
            i = names.index(n.name)
            st = patterns[:, i]
            L = np.zeros((len(patterns), 4))
            L[np.arange(len(patterns)), np.where(st < 0, 0, st)] = 1.0
            L[st < 0] = 1.0
            return L
        L = np.ones((len(patterns), 4))
        for c in n.children:
            P = P_matrix(Q, c.length * rate)
            L *= partial(c) @ P.T
        return L
    return partial(root) @ np.asarray(freqs)

def loglik(root, patterns, weights, Q, freqs, gamma=None, pinv=0.0, asc=False):
    """Total log-likelihood. gamma = (alpha, k, 'mean'|'median') or None.
    pinv: proportion of invariable sites. asc: Lewis (2001) variable-sites-only correction."""
    if gamma:
        alpha, k, kind = gamma
        rates = gamma_rates_mean(alpha, k) if kind == "mean" else gamma_rates_median(alpha, k)
        if pinv > 0: rates = rates / (1 - pinv)
        props = np.full(k, (1 - pinv) / k)
    else:
        rates = np.array([1.0 / (1 - pinv) if pinv > 0 else 1.0]); props = np.array([1 - pinv])
    def site_lh(pats):
        L = np.zeros(len(pats))
        for r, p in zip(rates, props):
            L += p * site_pattern_likelihoods(root, pats, Q, freqs, r)
        if pinv > 0:
            const = np.array([len(set(x[x >= 0])) <= 1 for x in pats])
            # invariable-site term: pi_state if the (observed) states are all one state
            for j, x in enumerate(pats):
                if const[j]:
                    obs = set(x[x >= 0])
                    L[j] += pinv * (freqs[obs.pop()] if obs else 1.0)
        return L
    L = site_lh(patterns)
    lnL = float(np.sum(weights * np.log(L)))
    if asc:
        const_pats = np.array([[s] * patterns.shape[1] for s in range(4)])
        Lc = site_lh(const_pats)
        lnL -= float(np.sum(weights)) * math.log(1.0 - Lc.sum())
    return lnL

# ---------------------------------------------------------------- simulation
def simulate(root, nsites, Q, freqs, rng, gamma=None):
    """Simulate an alignment down `root` under Q; returns dict name->str."""
    names = [l.name for l in leaves(root)]
    rates = np.ones(nsites)
    if gamma:
        alpha, k = gamma
        rates = rng.choice(gamma_rates_mean(alpha, k), size=nsites)
    seqs = {}
    def down(n, states):
        if not n.children:
            seqs[n.name] = "".join(NUC[s] for s in states); return
        for c in n.children:
            new = np.empty(nsites, dtype=int)
            for s in range(4):
                idx = np.where(states == s)[0]
                if len(idx) == 0: continue
                # per-site rates: draw per site
                for i in idx:
                    P = P_matrix(Q, c.length * rates[i])
                    new[i] = rng.choice(4, p=np.clip(P[s], 0, None) / np.clip(P[s], 0, None).sum())
            down(c, new)
    down(root, rng.choice(4, size=nsites, p=freqs))
    return names, [seqs[n] for n in names]

def patterns_from_seqs(seqs):
    """Collapse columns into unique patterns; returns (patterns int array, weights)."""
    cols = list(zip(*seqs))
    uniq = {}
    for c in cols:
        uniq[c] = uniq.get(c, 0) + 1
    pats = np.array([[NUC.index(ch) if ch in NUC else -1 for ch in c] for c in uniq])
    w = np.array(list(uniq.values()), dtype=float)
    return pats, w

# ---------------------------------------------------------------- report parsing
def report_value(rep, key):
    m = re.search(re.escape(key) + r"\s*:?\s*(-?[0-9.]+)", rep)
    return float(m.group(1)) if m else None

def report_gamma_table(rep):
    """Parse the 'Category  Relative_rate  Proportion' table; returns list of (rate, prop)."""
    out = []
    m = re.search(r"Category\s+Relative_rate\s+Proportion\n((?:.*\n)+?)(?:\n|Relative rates)", rep)
    if not m: return out
    for line in m.group(1).splitlines():
        f = line.split()
        if len(f) >= 3 and f[0].isdigit() and f[0] != "0":
            out.append((float(f[1]), float(f[2])))
    return out

def splits_from_newick(s, taxa):
    """All nontrivial bipartitions of an unrooted tree as frozensets (smaller side, tie: sorted)."""
    root = parse_newick(s)
    out = set()
    all_t = frozenset(taxa)
    def rec(n):
        if not n.children: return frozenset([n.name])
        cl = frozenset().union(*[rec(c) for c in n.children])
        if 1 < len(cl) < len(taxa) - 1:
            other = all_t - cl
            out.add(min(cl, other, key=lambda x: (len(x), sorted(x))))
        return cl
    rec(root)
    return out
