"""T2: pseudoalignment and the EM.

Random transcriptome of multi-isoform genes (shared exons), error-free
paired-end reads simulated under kallisto's model with known abundances.

(a) Pseudoalignment: for every fragment the exact compatibility class (the
    targets containing both mates, either strand) is computed in Python.
    On builds that have `kallisto bus --num` (0.50+) the per-read EC from
    output.bus is compared with it read by read; on every build quant's
    n_pseudoaligned / n_unique are compared with the exact classes.
(b) EM: an independent EM (weights 1/eff_len, kallisto's eff_length from
    abundance.tsv) is run on the exact classes to a relative tolerance of
    1e-13 and compared with kallisto's est_counts.  The gap measures
    kallisto's stopping rule (EMAlgorithm.h: stop when no target with
    alpha > 0.01 changes by more than 1 % in a round, after >= 50 rounds,
    then zero alpha < 1e-8 and run one more round).
(c) Truth: est_counts vs the expected counts of the simulation.
"""
import os, random, struct, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *

rng = random.Random(2)
d = tmpdir()
ver = kversion()
print("kallisto", ver)


def read_bus(path):
    with open(path, "rb") as f:
        data = f.read()
    assert data[:4] == b"BUS\x00"
    version, bclen, umilen, tlen = struct.unpack("<IIII", data[4:20])
    off = 20 + tlen
    recs = []
    while off + 32 <= len(data):
        bc, umi, ec, cnt, flags, pad = struct.unpack("<QQiIII", data[off:off + 32])
        recs.append((bc, umi, ec, cnt, flags))
        off += 32
    return recs


def read_ec(path):
    ecs = {}
    with open(path) as f:
        for line in f:
            a, b = line.split()
            ecs[int(a)] = frozenset(int(x) for x in b.split(","))
    return ecs


fails = 0
for rep, (n_genes, max_iso, nfr) in enumerate([(80, 5, 40000), (150, 6, 80000)]):
    tx = make_transcriptome(rng, n_genes=n_genes, max_iso=max_iso, exon_len=(40, 300), n_exons=(3, 9))
    names = list(tx)
    idx = build_index(tx, d)
    rho = {n: (rng.lognormvariate(1, 1.5) if rng.random() > 0.15 else 0.0) for n in names}
    p = gauss_fld(250, 40)
    frags, expected = simulate(rng, tx, rho, p, nfr, read_len=75, paired=True)
    comp = Compat(tx)
    exact = [comp.fragment_ec(x[3], x[4]) for x in frags]
    ec_counts = collections.Counter(e for e in exact if e)
    n_al = sum(1 for e in exact if e)
    n_u = sum(1 for e in exact if len(e) == 1)
    out, err = run_quant(idx, d, frags, paired=True, name="em%d" % rep, extra=["--plaintext"])
    ab = read_abundance(os.path.join(out, "abundance.tsv"))
    ri = read_run_info(os.path.join(out, "run_info.json"))
    print("\nset %d: %d targets, %d fragments, %d distinct exact classes" % (rep, len(names), len(frags), len(ec_counts)))
    ok = ri["n_pseudoaligned"] == n_al and ri["n_unique"] == n_u and ri["n_processed"] == len(frags)
    fails += not ok
    print("%s run_info: n_processed %d (sim %d), n_pseudoaligned %d (exact %d), n_unique %d (exact %d)"
          % ("ok  " if ok else "FAIL", ri["n_processed"], len(frags), ri["n_pseudoaligned"], n_al, ri["n_unique"], n_u))
    # per-read check through bus --num
    if not ver.startswith("0.4"):
        bd = os.path.join(d, "bus%d" % rep)
        pr = subprocess.run([kbin(), "bus", "-i", idx, "-o", bd, "-x", "bulk", "--paired", "--num",
                             os.path.join(d, "em%d_1.fq" % rep), os.path.join(d, "em%d_2.fq" % rep)],
                            capture_output=True, text=True)
        if pr.returncode == 0:
            recs = read_bus(os.path.join(bd, "output.bus"))
            ecs = read_ec(os.path.join(bd, "matrix.ec"))
            per = {}
            for bc, umi, ec, cnt, flags in recs:
                per[flags] = ecs[ec]
            same = sum(1 for i, e in enumerate(exact) if per.get(i, frozenset()) == e)
            sup = sum(1 for i, e in enumerate(exact) if per.get(i) is not None and per[i] > e)
            sub = sum(1 for i, e in enumerate(exact) if per.get(i) is not None and per[i] < e)
            miss = sum(1 for i, e in enumerate(exact) if e and i not in per)
            ok = same == len(frags)
            fails += not ok
            print("%s bus --num per-read EC == exact class for %d/%d fragments (superset %d, subset %d, unassigned %d)"
                  % ("ok  " if ok else "NOTE", same, len(frags), sup, sub, miss))
    # independent EM on the exact classes with kallisto's eff lengths
    el = [ab[n]["eff_length"] for n in names]
    alpha, iters = em(ec_counts, el, len(names), tol=1e-13)
    kc = [ab[n]["est_counts"] for n in names]
    m = [(abs(kc[i] - alpha[i]), i) for i in range(len(names))]
    tot_abs = sum(x[0] for x in m)
    big = [(x, i) for x, i in m if alpha[i] >= 10]
    rel = sorted(((abs(kc[i] - alpha[i]) / alpha[i], i) for _, i in big), reverse=True)
    print("     EM to 1e-13 (%d rounds) vs kallisto est_counts: sum |diff| %.1f of %d reads (%.3f %%); targets with >= 10 reads: %d"
          % (iters, tot_abs, n_al, 100 * tot_abs / n_al, len(big)))
    for q in (1, 5, 10):
        k = sum(1 for r, _ in rel if r > q / 100)
        print("       targets off by > %d %%: %d" % (q, k))
    for r, i in rel[:6]:
        print("       %-10s kallisto %10.2f  converged EM %10.2f  rel %.3f  truth %.1f"
              % (names[i], kc[i], alpha[i], r, expected[names[i]]))
    # zeroing: targets kallisto reports 0 but converged EM gives >= 1
    z = [(names[i], alpha[i]) for i in range(len(names)) if kc[i] == 0 and alpha[i] >= 1]
    print("     targets at 0 in kallisto with >= 1 read in the converged EM: %d %s" % (len(z), z[:5]))
    # truth
    tr = [expected[n] for n in names]
    err_k = sum(abs(a - b) for a, b in zip(kc, tr)) / n_al
    err_e = sum(abs(a - b) for a, b in zip(alpha, tr)) / n_al
    print("     mean abs error vs truth per read: kallisto %.4f, converged EM %.4f" % (err_k, err_e))
    # TPM check against the converged EM
    tk = [ab[n]["tpm"] for n in names]
    te = tpm_from(alpha, el)
    print("     max |TPM kallisto - TPM converged| = %.1f TPM" % max(abs(a - b) for a, b in zip(tk, te)))

print("\nFAILURES:", fails)
