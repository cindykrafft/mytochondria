"""Shared helpers for the kallisto harnesses.

Builds random transcriptomes (genes with isoforms that share exons, plus
deliberately short transcripts), simulates reads under kallisto's own
generative model with known abundances and a known fragment-length
distribution, runs `kallisto index` / `kallisto quant`, parses
abundance.tsv and run_info.json, and holds independent Python ports of the
documented quantities:

  * effective length  L_eff = L - mu_L + 1, mu_L = mean of the FLD truncated
    at L (Bray et al. 2016, Online Methods; kallisto computes mu_L from the
    empirical FLD of paired-end data or a truncated Gaussian for --single);
  * TPM = 1e6 * (c_t / L_eff_t) / sum_s (c_s / L_eff_s);
  * the EM on equivalence classes, run to a tight tolerance;
  * exact compatibility classes for error-free reads (the set of targets
    whose sequence contains every read of the fragment, either strand).

Every harness takes the kallisto binary as argv[1] (default $KALLISTO).
Truths are computed here, never read back from kallisto.
"""
import json, math, os, random, subprocess, sys, tempfile, collections

COMP = str.maketrans("ACGTN", "TGCAN")


def kbin():
    return sys.argv[1] if len(sys.argv) > 1 else os.environ.get("KALLISTO", "kallisto")


def kversion():
    p = subprocess.run([kbin(), "version"], capture_output=True, text=True)
    return (p.stdout + p.stderr).strip().split()[-1]


def tmpdir():
    base = os.environ.get("KHARNESS_TMP")
    return tempfile.mkdtemp(prefix="kh_", dir=base)


def revcomp(s):
    return s.translate(COMP)[::-1]


def rand_seq(rng, n):
    return "".join(rng.choice("ACGT") for _ in range(n))


# ---------------------------------------------------------------- transcriptome

def make_transcriptome(rng, n_genes=60, max_iso=4, exon_len=(60, 400),
                       n_exons=(2, 8), extra=()):
    """Return ordered dict name -> sequence. Genes have isoforms built as exon
    subsets (shared exons -> multi-transcript equivalence classes). `extra` is
    a list of (name, seq) appended verbatim."""
    tx = collections.OrderedDict()
    for g in range(n_genes):
        ne = rng.randint(*n_exons)
        exons = [rand_seq(rng, rng.randint(*exon_len)) for _ in range(ne)]
        n_iso = rng.randint(1, max_iso)
        seen = set()
        for i in range(n_iso):
            if i == 0:
                keep = tuple(range(ne))
            else:
                keep = tuple(e for e in range(ne) if rng.random() < 0.7)
                if len(keep) == 0:
                    keep = (rng.randrange(ne),)
            if keep in seen:
                continue
            seen.add(keep)
            tx["g%03d_t%d" % (g, i)] = "".join(exons[e] for e in keep)
    for name, s in extra:
        tx[name] = s
    return tx


def write_fasta(path, tx):
    with open(path, "w") as f:
        for n, s in tx.items():
            f.write(">%s\n" % n)
            for i in range(0, len(s), 70):
                f.write(s[i:i + 70] + "\n")


def build_index(tx, d, k=31, extra_args=()):
    fa = os.path.join(d, "tx.fa")
    write_fasta(fa, tx)
    idx = os.path.join(d, "tx.idx")
    args = [kbin(), "index", "-i", idx, "-k", str(k)]
    if not kversion().startswith("0.4"):
        args += ["-T", os.path.join(d, "tmp")]
    args += list(extra_args) + [fa]
    p = subprocess.run(args, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("index failed: " + p.stderr[-2000:])
    return idx


# ---------------------------------------------------------------- FLD

def gauss_fld(mean, sd, maxlen=1000, minlen=1):
    """Discrete FLD p[f], f = 0..maxlen-1, truncated Gaussian (unnormalised ok)."""
    p = [0.0] * maxlen
    for f in range(minlen, maxlen):
        p[f] = math.exp(-0.5 * ((f - mean) / sd) ** 2)
    s = sum(p)
    return [x / s for x in p]


def trunc_mean(p, L):
    """mean of FLD p truncated at L (fragments of length <= L)."""
    L = min(L, len(p) - 1)
    num = sum(f * p[f] for f in range(L + 1))
    den = sum(p[f] for f in range(L + 1))
    return num / den if den > 0 else 0.0


def eff_len_model(p, L):
    """Expected number of (start, length) placements, normalised by P(f<=L):
    sum_{f<=L} p_f (L-f+1) / sum_{f<=L} p_f  ==  L - mu_L + 1."""
    mu = trunc_mean(p, L)
    return L - mu + 1


def placements(p, L):
    """Unnormalised fragment-emission weight of a target of length L:
    sum_{f<=L} p_f (L - f + 1)."""
    return sum(p[f] * (L - f + 1) for f in range(min(L, len(p) - 1) + 1))


# ---------------------------------------------------------------- reads

def draw_frag_len(rng, cdf, L):
    # rejection on f <= L
    for _ in range(10000):
        u = rng.random()
        lo, hi = 0, len(cdf) - 1
        while lo < hi:
            m = (lo + hi) // 2
            if cdf[m] < u:
                lo = m + 1
            else:
                hi = m
        if lo <= L and lo > 0:
            return lo
    return None


def simulate(rng, tx, rho, p, n_frags, read_len=75, paired=True,
             strand=None, min_frag=None, model="kallisto"):
    """Simulate fragments under kallisto's model: target t is drawn with
    probability proportional to rho_t * (L_t - mu_{L_t} + 1) (model="kallisto",
    the default) or rho_t * placements(p, L_t) (model="placements"); the fragment
    length from p truncated at L_t; the start uniformly.  `strand`: None
    (random orientation), 'fr' (read 1 = transcript strand), 'rf' (read 1 =
    reverse strand).  Returns list of (tname, start, flen, r1, r2, flip) and
    the expected-count truth vector."""
    names = list(tx)
    if model == "kallisto":
        # kallisto's likelihood: P(fragment from t) proportional to
        # rho_t * (L_t - mu_{L_t} + 1), mu_L the FLD mean truncated at L
        w = [rho[n] * eff_len_model(p, len(tx[n])) for n in names]
    else:
        # unnormalised placements sum_{f<=L} p_f (L-f+1)
        w = [rho[n] * placements(p, len(tx[n])) for n in names]
    W = sum(w)
    probs = [x / W for x in w]
    cdf = []
    acc = 0.0
    for x in p:
        acc += x
        cdf.append(acc)
    tcdf = []
    acc = 0.0
    for x in probs:
        acc += x
        tcdf.append(acc)
    frags = []
    for i in range(n_frags):
        u = rng.random()
        lo, hi = 0, len(tcdf) - 1
        while lo < hi:
            m = (lo + hi) // 2
            if tcdf[m] < u:
                lo = m + 1
            else:
                hi = m
        n = names[lo]
        s = tx[n]
        L = len(s)
        f = draw_frag_len(rng, cdf, L)
        if f is None:
            continue
        st = rng.randint(0, L - f)
        frag = s[st:st + f]
        rl = min(read_len, f)
        if strand is None:
            flip = rng.random() < 0.5
        elif strand == "fr":
            flip = False
        else:
            flip = True
        a = frag[:rl]
        b = revcomp(frag[-rl:])
        if flip:
            a, b = b, a
        frags.append((n, st, f, a, b, flip))
    expected = {n: n_frags * probs[i] for i, n in enumerate(names)}
    return frags, expected


def write_fastq(path, seqs, prefix="r"):
    with open(path, "w") as f:
        for i, s in enumerate(seqs):
            f.write("@%s%d\n%s\n+\n%s\n" % (prefix, i, s, "I" * len(s)))


def run_quant(idx, d, frags, paired=True, extra=(), name="q", single_l=None,
              single_s=None, threads=1, check=True):
    out = os.path.join(d, name)
    r1 = os.path.join(d, name + "_1.fq")
    write_fastq(r1, [x[3] for x in frags])
    args = [kbin(), "quant", "-i", idx, "-o", out, "-t", str(threads)]
    if not paired:
        args += ["--single", "-l", str(single_l), "-s", str(single_s)]
    if "--plaintext" not in extra and kversion().startswith("0.4"):
        args += ["--plaintext"]
    args += list(extra)
    if paired:
        r2 = os.path.join(d, name + "_2.fq")
        write_fastq(r2, [x[4] for x in frags])
        args += [r1, r2]
    else:
        args += [r1]
    p = subprocess.run(args, capture_output=True, text=True)
    if check and p.returncode != 0:
        raise RuntimeError("quant failed: " + p.stderr[-3000:])
    return out, p.stderr


def run_quant_files(idx, out, files, extra=(), threads=1):
    args = [kbin(), "quant", "-i", idx, "-o", out, "-t", str(threads)] + list(extra) + list(files)
    if kversion().startswith("0.4") and "--plaintext" not in extra:
        args.insert(2, "--plaintext")
    p = subprocess.run(args, capture_output=True, text=True)
    return p


def read_abundance(path):
    res = collections.OrderedDict()
    with open(path) as f:
        next(f)
        for line in f:
            t, L, el, c, tpm = line.rstrip("\n").split("\t")
            res[t] = dict(length=int(L), eff_length=float(el), est_counts=float(c), tpm=float(tpm))
    return res


def read_run_info(path):
    with open(path) as f:
        return json.load(f)


def stderr_mean_fl(stderr):
    for line in stderr.splitlines():
        if "estimated average fragment length" in line:
            return float(line.split(":")[-1])
    return None


# ---------------------------------------------------------------- exact ECs and EM

class Compat:
    """Exact compatibility of error-free reads: targets containing the read
    (either strand). k-mer prefilter, then substring check."""

    def __init__(self, tx, k=31):
        self.tx = tx
        self.names = list(tx)
        self.k = k
        self.km = collections.defaultdict(set)
        for i, n in enumerate(self.names):
            s = tx[n]
            for j in range(len(s) - k + 1):
                self.km[s[j:j + k]].add(i)

    def targets(self, read):
        k = self.k
        if len(read) < k:
            return set()
        c1 = self.km.get(read[:k], set())
        rc = revcomp(read)
        c2 = self.km.get(rc[:k], set())
        out = set()
        for i in c1:
            if read in self.tx[self.names[i]]:
                out.add(i)
        for i in c2:
            if rc in self.tx[self.names[i]]:
                out.add(i)
        return out

    def stranded_targets(self, read, forward):
        """targets containing the read on the transcript strand (forward=True)
        or its reverse complement (forward=False)."""
        k = self.k
        s = read if forward else revcomp(read)
        c = self.km.get(s[:k], set())
        return set(i for i in c if s in self.tx[self.names[i]])

    def fragment_ec(self, a, b=None):
        e = self.targets(a)
        if b is not None:
            e &= self.targets(b)
        return frozenset(e)


def em(ec_counts, eff_lens, n_targets, tol=1e-13, max_iter=200000, alpha0=None):
    """Plain EM on equivalence classes, weights 1/eff_len (kallisto's model).
    ec_counts: dict frozenset(target idx) -> count. Returns alpha (est counts)
    and the number of iterations."""
    N = sum(ec_counts.values())
    alpha = list(alpha0) if alpha0 else [N / n_targets] * n_targets
    items = [(list(e), c) for e, c in ec_counts.items() if c > 0 and len(e) > 0]
    it = 0
    for it in range(1, max_iter + 1):
        nxt = [0.0] * n_targets
        for e, c in items:
            if len(e) == 1:
                nxt[e[0]] += c
                continue
            ws = [alpha[t] / eff_lens[t] for t in e]
            den = sum(ws)
            if den <= 0:
                continue
            for t, w in zip(e, ws):
                nxt[t] += c * w / den
        delta = max((abs(nxt[t] - alpha[t]) / nxt[t]) if nxt[t] > 1e-8 else 0.0
                    for t in range(n_targets))
        alpha = nxt
        if delta < tol:
            break
    return alpha, it


def tpm_from(counts, eff_lens):
    r = [c / l for c, l in zip(counts, eff_lens)]
    s = sum(r)
    return [1e6 * x / s for x in r]


def fmt_row(cols, widths):
    return "  ".join(str(c).rjust(w) for c, w in zip(cols, widths))
