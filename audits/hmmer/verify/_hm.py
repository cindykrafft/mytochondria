"""Shared helpers for the HMMER harnesses.

Build selection: HMMER_BIN=<dir with hmmsearch, hmmscan, ...> (default: develop build).
Every truth below is computed here in Python from the documented formulas and the
values HMMER itself prints or stores (HMM file STATS lines, tabular columns); the
synthetic sequences are drawn with Python's own RNG, not with HMMER/Easel tools.
"""
import math, os, random, re, subprocess, sys, tempfile

SCR = os.environ.get("HM_SCRATCH",
    "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/audit-hmmer")
BIN = os.environ.get("HMMER_BIN", os.path.join(SCR, "hmmer", "src"))
TUT = os.path.join(SCR, "hmmer", "tutorial")
TST = os.path.join(SCR, "hmmer", "testsuite")
WORK = tempfile.mkdtemp(prefix="hmv_", dir=os.environ.get("HM_WORK", SCR))

AA = "ACDEFGHIKLMNPQRSTVWY"
# p7_AminoFrequencies() (src/hmmer.c), the default protein null model
BGF = [0.0787945, 0.0151600, 0.0535222, 0.0668298, 0.0397062, 0.0695071, 0.0229198,
       0.0590092, 0.0594422, 0.0963728, 0.0237718, 0.0414386, 0.0482904, 0.0395639,
       0.0540978, 0.0683364, 0.0540687, 0.0673417, 0.0114135, 0.0304133]


def version():
    out = run([prog("hmmsearch"), "-h"]).splitlines()
    return out[1].strip("# ").split(";")[0] if len(out) > 1 else "?"


def prog(name):
    return os.path.join(BIN, name)


def run(cmd, check=True):
    p = subprocess.run([str(c) for c in cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if check and p.returncode != 0:
        raise RuntimeError("command failed (%d): %s\n%s" % (p.returncode, " ".join(map(str, cmd)), p.stderr))
    return p.stdout


def path(name):
    return os.path.join(WORK, name)


def write_fasta(fn, seqs):
    with open(fn, "w") as f:
        for name, s in seqs:
            f.write(">%s\n" % name)
            for i in range(0, len(s), 60):
                f.write(s[i:i + 60] + "\n")
    return fn


def rand_protein(rng, L, freqs=BGF):
    return "".join(rng.choices(AA, weights=freqs, k=L))


def rand_dna(rng, L):
    return "".join(rng.choices("ACGT", k=L))


# ---------------------------------------------------------------- HMM files
def read_hmms(fn):
    """Parse HMMER3 text HMM(s): name, M, alph, STATS, cutoffs, match emission probs."""
    hmms, cur, in_body = [], None, False
    with open(fn) as f:
        lines = f.read().splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("HMMER3"):
            cur = {"stats": {}, "cut": {}, "mat": []}; in_body = False
        elif ln.startswith("//"):
            hmms.append(cur); cur = None
        elif cur is not None and not in_body:
            t = ln.split()
            if not t: pass
            elif t[0] == "NAME": cur["name"] = t[1]
            elif t[0] == "LENG": cur["M"] = int(t[1])
            elif t[0] == "MAXL": cur["maxl"] = int(t[1])
            elif t[0] == "ALPH": cur["alph"] = t[1]
            elif t[0] in ("GA", "TC", "NC"):
                v = [float(x.rstrip(";")) for x in t[1:3]]
                cur["cut"][t[0]] = (v[0], v[1] if len(v) > 1 else v[0])
            elif t[0] == "STATS": cur["stats"][t[2]] = (float(t[3]), float(t[4]))
            elif t[0] == "HMM":
                in_body = True
                i += 2  # skip transition header; next is COMPO or node 0
                if lines[i].split()[0] == "COMPO": i += 3
                else: i += 2
                continue
        elif cur is not None and in_body:
            t = ln.split()
            if t and t[0].isdigit():
                K = 20 if cur["alph"] == "amino" else 4
                cur["mat"].append([math.exp(-float(x)) for x in t[1:1 + K]])
                i += 3; continue
        i += 1
    return hmms


def mean_match_relent(hmm, bgf):
    """p7_MeanMatchRelativeEntropy(): mean over match states of sum p log2(p/f)."""
    tot = 0.0
    for p in hmm["mat"]:
        tot += sum(pi * math.log2(pi / fi) for pi, fi in zip(p, bgf) if pi > 0)
    return tot / len(hmm["mat"])


def exp_surv(x, tau, lam):
    return 1.0 if x < tau else math.exp(-lam * (x - tau))


def gumbel_surv(x, mu, lam):
    return -math.expm1(-math.exp(-lam * (x - mu)))


# ---------------------------------------------------------------- tabular outputs
def read_tbl(fn):
    """hmmsearch/hmmscan/phmmer/jackhmmer --tblout (protein) rows."""
    rows = []
    for ln in open(fn):
        if ln.startswith("#") or not ln.strip(): continue
        t = ln.split(None, 18)
        rows.append(dict(t=t[0], tacc=t[1], q=t[2], qacc=t[3], E=float(t[4]), sc=float(t[5]), bias=float(t[6]),
                         dE=float(t[7]), dsc=float(t[8]), dbias=float(t[9]), exp=float(t[10]),
                         reg=int(t[11]), clu=int(t[12]), ov=int(t[13]), env=int(t[14]), dom=int(t[15]),
                         rep=int(t[16]), inc=int(t[17])))
    return rows


def read_domtbl(fn):
    rows = []
    for ln in open(fn):
        if ln.startswith("#") or not ln.strip(): continue
        t = ln.split(None, 22)
        rows.append(dict(t=t[0], tacc=t[1], tlen=int(t[2]), q=t[3], qacc=t[4], qlen=int(t[5]), E=float(t[6]),
                         sc=float(t[7]), bias=float(t[8]), n=int(t[9]), of=int(t[10]), cE=float(t[11]),
                         iE=float(t[12]), dsc=float(t[13]), dbias=float(t[14]), hf=int(t[15]), ht=int(t[16]),
                         af=int(t[17]), at=int(t[18]), ef=int(t[19]), et=int(t[20]), acc=float(t[21])))
    return rows


def read_nhmmer_tbl(fn):
    rows = []
    for ln in open(fn):
        if ln.startswith("#") or not ln.strip(): continue
        t = ln.split(None, 15)
        rows.append(dict(t=t[0], q=t[2], hf=int(t[4]), ht=int(t[5]), af=int(t[6]), at=int(t[7]), ef=int(t[8]),
                         et=int(t[9]), sqlen=int(t[10]), strand=t[11], E=float(t[12]), sc=float(t[13]),
                         bias=float(t[14])))
    return rows


def rel(a, b):
    if a == b: return 0.0
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def eval_close(printed, computed, score_halfulp=0.05, lam=0.72):
    """Printed E-values are %9.2g of a value computed from an unrounded score; the score
    column is %6.1f, so the score we recompute from is off by up to 0.05 bits, i.e. a factor
    exp(lam*0.05) ~ 1.037 in E, plus 2-significant-digit rounding of E (<= 5 %)."""
    if computed == 0: return printed == 0
    r = printed / computed
    tol = math.exp(lam * score_halfulp) * 1.051
    return 1 / tol <= r <= tol


class Report:
    def __init__(self, title):
        self.title = title; self.n = 0; self.bad = 0
        print("# %s" % title)
        print("# build: %s  (%s)" % (version(), BIN))

    def check(self, ok, label, detail=""):
        self.n += 1
        if not ok: self.bad += 1
        print("%s  %s%s" % ("ok  " if ok else "FAIL", label, ("  | " + detail) if detail else ""))
        return ok

    def note(self, s):
        print("    " + s)

    def done(self):
        print("# %d checks, %d failed" % (self.n, self.bad))


# ---------------------------------------------------------------- synthetic databases
DATA_BIN = os.path.join(SCR, "hmmer", "src")   # data are always made with one build, for comparability
DATA = os.path.join(SCR, "data"); os.makedirs(DATA, exist_ok=True)


def emit_core(hmmfile, n, seed):
    """Core-model sequences (domain only) from hmmemit; used only as homologous inserts."""
    out = run([os.path.join(DATA_BIN, "hmmemit"), "-N", n, "--seed", seed, hmmfile])
    seqs, cur = [], None
    for ln in out.splitlines():
        if ln.startswith(">"): cur = []; seqs.append(cur)
        else: cur.append(ln.strip())
    return ["".join(s) for s in seqs]


def protein_db(seed=1, nrand=1500, name="protdb"):
    """Random background sequences plus sequences carrying 1-3 emitted domains of globins4,
    fn3 and Pkinase at recorded positions. Returns (fasta path, list of (name, seq, truth))."""
    fn = os.path.join(DATA, "%s_%d.fa" % (name, seed))
    truthfn = fn + ".truth"
    if os.path.exists(fn) and os.path.exists(truthfn):
        truth = {}
        for ln in open(truthfn):
            t = ln.split("\t"); truth[t[0]] = eval(t[1])
        return fn, truth
    rng = random.Random(seed)
    seqs, truth = [], {}
    for i in range(nrand):
        nm = "rnd%05d" % i
        seqs.append((nm, rand_protein(rng, rng.randint(80, 600)))); truth[nm] = []
    for fam, k in (("globins4", 40), ("fn3", 40), ("Pkinase", 30)):
        doms = emit_core(os.path.join(TUT, fam + ".hmm"), 3 * k, seed + 11)
        di = 0
        for j in range(k):
            ncopy = 1 + (j % 3)
            s, spans = rand_protein(rng, rng.randint(10, 80)), []
            for c in range(ncopy):
                d = doms[di]; di += 1
                spans.append((fam, len(s) + 1, len(s) + len(d)))
                s += d + rand_protein(rng, rng.randint(10, 80))
            nm = "%s_%03d_x%d" % (fam, j, ncopy)
            seqs.append((nm, s)); truth[nm] = spans
    # biased-composition decoys: random sequences with low-complexity stretches
    for i in range(60):
        nm = "lowc%03d" % i
        a, b = rng.sample(AA, 2)
        s = rand_protein(rng, rng.randint(40, 150)) + "".join(rng.choice(a + b + b) for _ in range(rng.randint(40, 120))) + rand_protein(rng, rng.randint(40, 150))
        seqs.append((nm, s)); truth[nm] = []
    rng.shuffle(seqs)
    write_fasta(fn, seqs)
    with open(truthfn, "w") as f:
        for nm, sp in truth.items(): f.write("%s\t%r\n" % (nm, sp))
    return fn, truth


def fasta_count(fn):
    return sum(1 for ln in open(fn) if ln.startswith(">"))


def fasta_residues(fn):
    return sum(len(ln.strip()) for ln in open(fn) if not ln.startswith(">"))


def read_main_domains(fn):
    """Per-domain lines from the main (-o) output of hmmsearch/hmmscan/phmmer/jackhmmer
    (last query/round in the file): returns ({(target, n): dict(inc, sc, cE, iE, coords, acc)},
    [targets listed above the '------ inclusion threshold ------' line])."""
    lines = open(fn).read().splitlines()
    starts = [k for k, ln in enumerate(lines) if ln.startswith("Scores for complete seq")]
    k = starts[-1] + 4
    incl, below = [], False
    while k < len(lines) and lines[k].strip():
        if "inclusion threshold" in lines[k]: below = True
        elif not lines[k].strip().startswith("[No hits"):
            t = lines[k].split()
            if not below: incl.append(t[8])
        k += 1
    doms, cur = {}, None
    for ln in lines[starts[-1]:]:
        if ln.startswith(">> "):
            cur = ln.split()[1]
        elif cur and re.match(r"^\s+\d+ [!?]", ln):
            t = ln.split()
            doms[(cur, int(t[0]))] = dict(inc=(t[1] == "!"), sc=float(t[2]), bias=float(t[3]), cE=float(t[4]), iE=float(t[5]),
                                          hf=int(t[6]), ht=int(t[7]), af=int(t[9]), at=int(t[10]), ef=int(t[12]), et=int(t[13]),
                                          acc=float(t[15]))
    return doms, incl
