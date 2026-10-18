"""Shared helpers for the minimap2 harnesses.

Every truth in these harnesses is computed here, in Python, from the planted
sequence (random references with known repeats, edits, junctions and fragment
lengths) or from the documented formulas -- never from minimap2's own output.

The binary is taken from $MM2 (default: `minimap2` on PATH); the harnesses print
`minimap2 --version` first so every captured .out names its build.
"""
import os, random, subprocess, tempfile, math

MM2 = os.environ.get("MM2", "minimap2")
COMP = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}
NT4 = {"A": 0, "C": 1, "G": 2, "T": 3}


def version():
    return subprocess.run([MM2, "--version"], capture_output=True, text=True).stdout.strip()


def rand_seq(rng, n):
    return "".join(rng.choice("ACGT") for _ in range(n))


def revcomp(s):
    return "".join(COMP[c] for c in reversed(s))


def other_base(rng, b):
    return rng.choice([x for x in "ACGT" if x != b])


def tmpdir():
    return tempfile.mkdtemp(prefix="mm2h_", dir=os.environ.get("MM2_TMP"))


def write_fasta(path, recs):
    with open(path, "w") as f:
        for name, seq in recs:
            f.write(f">{name}\n")
            for i in range(0, len(seq), 80):
                f.write(seq[i:i + 80] + "\n")


def write_fastq(path, recs):
    with open(path, "w") as f:
        for name, seq in recs:
            f.write(f"@{name}\n{seq}\n+\n{'I' * len(seq)}\n")


def run(args, check=True):
    p = subprocess.run([MM2] + list(args), capture_output=True, text=True)
    if check and p.returncode != 0:
        raise RuntimeError(p.stderr[-2000:])
    return p.stdout


def parse_sam(text):
    out = []
    for line in text.splitlines():
        if not line or line[0] == "@":
            continue
        f = line.split("\t")
        rec = {"qname": f[0], "flag": int(f[1]), "rname": f[2], "pos": int(f[3]),
               "mapq": int(f[4]), "cigar": f[5], "rnext": f[6], "pnext": int(f[7]),
               "tlen": int(f[8]), "seq": f[9], "tags": {}}
        for t in f[11:]:
            k, ty, v = t.split(":", 2)
            rec["tags"][k] = int(v) if ty == "i" else float(v) if ty == "f" else v
        out.append(rec)
    return out


def parse_paf(text):
    out = []
    for line in text.splitlines():
        f = line.split("\t")
        rec = {"qname": f[0], "qlen": int(f[1]), "qs": int(f[2]), "qe": int(f[3]), "strand": f[4],
               "tname": f[5], "tlen": int(f[6]), "ts": int(f[7]), "te": int(f[8]),
               "nmatch": int(f[9]), "blen": int(f[10]), "mapq": int(f[11]), "tags": {}}
        for t in f[12:]:
            k, ty, v = t.split(":", 2)
            rec["tags"][k] = int(v) if ty == "i" else float(v) if ty == "f" else v
        out.append(rec)
    return out


def cigar_ops(c):
    ops, n = [], ""
    for ch in c:
        if ch.isdigit():
            n += ch
        else:
            ops.append((int(n), ch)); n = ""
    return ops


def aligned_pairs(rec, ref):
    """Walk the CIGAR of a SAM record against the reference.
    Returns (query-in-alignment-orientation, list of ops with sequences)."""
    seq = rec["seq"]
    q = 0; t = rec["pos"] - 1
    cols = []  # (op, qbase or None, tbase or None)
    for n, op in cigar_ops(rec["cigar"]):
        if op == "S":
            q += n
        elif op == "H":
            pass
        elif op in "M=X":
            for i in range(n):
                cols.append(("M", seq[q + i], ref[t + i]))
            q += n; t += n
        elif op == "I":
            cols.append(("I", seq[q:q + n], None)); q += n
        elif op == "D":
            cols.append(("D", None, ref[t:t + n])); t += n
        elif op == "N":
            cols.append(("N", None, ref[t:t + n])); t += n
    return cols


def port_as(cols, a, b, q, e, q2, e2, sc_ambi=1):
    """minimap2's documented scoring: match a, mismatch -b, ambiguous -sc_ambi,
    a gap of length l costs min(q + l*e, q2 + l*e2) (manual, -O/-E). Introns are not
    scored here (splice mode is not checked with this port)."""
    s = 0
    for op, x, y in cols:
        if op == "M":
            if x not in NT4 or y not in NT4:
                s -= sc_ambi
            else:
                s += a if x == y else -b
        elif op in "ID":
            l = len(x if op == "I" else y)
            s -= min(q + l * e, q2 + l * e2)
    return s


def port_nm(cols):
    nm = 0
    for op, x, y in cols:
        if op == "M":
            if x != y or x not in NT4:
                nm += 1
        elif op == "I":
            nm += len(x)
        elif op == "D":
            nm += len(y)
    return nm


def port_de(cols):
    """de:f -- gap-compressed divergence: 1 - matches / (M columns + gap opens)."""
    m = cols_m = gapo = 0
    for op, x, y in cols:
        if op == "M":
            cols_m += 1
            if x == y and x in NT4:
                m += 1
        elif op in "ID":
            gapo += 1
    return 1.0 - m / (cols_m + gapo)


def port_md(cols):
    md, run_ = "", 0
    for op, x, y in cols:
        if op == "M":
            if x != y:
                md += f"{run_}{y}"; run_ = 0
            else:
                run_ += 1
        elif op == "D":
            md += f"{run_}^{y}"; run_ = 0
    return md + (str(run_) if run_ > 0 else "")


def port_cs(cols):
    cs, run_ = "", 0
    for op, x, y in cols:
        if op == "M":
            if x != y:
                if run_:
                    cs += f":{run_}"; run_ = 0
                cs += f"*{y.lower()}{x.lower()}"
            else:
                run_ += 1
        else:
            if run_:
                cs += f":{run_}"; run_ = 0
            if op == "I":
                cs += "+" + x.lower()
            elif op == "D":
                cs += "-" + y.lower()
            elif op == "N":
                cs += f"~{y[:2].lower()}{len(y)}{y[-2:].lower()}"
    if run_:
        cs += f":{run_}"
    return cs


def mutate(rng, s, n_sub=0, ins=(), dels=(), protect=0):
    """Apply substitutions at random positions (away from the ends by `protect`),
    then the listed insertions [(pos, seq)] and deletions [(pos, len)] in
    descending position order. Returns the new sequence."""
    s = list(s)
    pos = rng.sample(range(protect, len(s) - protect), n_sub) if n_sub else []
    for p in pos:
        s[p] = other_base(rng, s[p])
    edits = [(p, "I", x) for p, x in ins] + [(p, "D", l) for p, l in dels]
    for p, kind, x in sorted(edits, reverse=True):
        if kind == "I":
            s[p:p] = list(x)
        else:
            del s[p:p + x]
    return "".join(s)


def noisy(rng, s, sub=0.03, ins=0.02, dele=0.02):
    """ONT-like read: independent substitution/insertion/deletion per base."""
    out = []
    for c in s:
        r = rng.random()
        if r < dele:
            continue
        if r < dele + sub:
            out.append(other_base(rng, c))
        else:
            out.append(c)
        if rng.random() < ins:
            out.append(rng.choice("ACGT"))
    return "".join(out)
