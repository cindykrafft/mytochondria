"""T4: --fr-stranded / --rf-stranded.

Targets come in antisense pairs: B_i contains the reverse complement of a
stretch of A_i (an antisense overlap of 150-600 bp), so an unstranded read
from the overlap is compatible with both.  Reads are simulated from A and B
with known abundances (A_i and B_i differ by up to 20-fold) under a stranded
protocol ('fr': read 1 on the transcript strand, 'rf': read 1 reverse),
paired-end and single-end.  For each protocol x option the run's
n_pseudoaligned and est_counts are compared with the truth: with the
matching option every read keeps exactly its source among the overlapping
pair (exact stranded compatibility computed in Python); with the opposite
option a read is kept exactly when it is compatible on the other strand
(i.e. it lies in an antisense overlap, and then belongs to the partner);
unstranded keeps every read and splits overlap reads by the EM.  The
expected n_pseudoaligned / n_unique of every run is computed from the exact
classes.  Single-end runs use --single-overhang so that the overhang filter
(T3) does not enter.
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *

rng = random.Random(4)
d = tmpdir()
print("kallisto", kversion())

tx = collections.OrderedDict()
for i in range(25):
    a = rand_seq(rng, rng.randint(800, 2000))
    ov = rng.randint(150, 600)
    st = rng.randint(0, len(a) - ov)
    b = rand_seq(rng, rng.randint(0, 400)) + revcomp(a[st:st + ov]) + rand_seq(rng, rng.randint(100, 500))
    tx["A%02d" % i] = a
    tx["B%02d" % i] = b
names = list(tx)
idx = build_index(tx, d)
rho = {}
for i in range(25):
    rho["A%02d" % i] = rng.lognormvariate(1, 1)
    rho["B%02d" % i] = rho["A%02d" % i] * rng.choice([0.05, 0.2, 1, 5, 20])
comp = Compat(tx)
p = gauss_fld(220, 35)
nidx = {n: i for i, n in enumerate(names)}

fails = 0
for paired in (True, False):
    for proto in ("fr", "rf"):
        frags, expected = simulate(rng, tx, rho, p, 30000, read_len=75, paired=paired, strand=proto)
        # exact stranded compatibility: read 1 on the transcript strand for fr
        def ec_str(x, proto=proto):
            r1fw = (proto == "fr")
            e = comp.stranded_targets(x[3], r1fw)
            if paired:
                e &= comp.stranded_targets(x[4], not r1fw)
            return frozenset(e)
        ex = [ec_str(x) for x in frags]
        n_true = len(frags)
        src_ok = sum(1 for x, e in zip(frags, ex) if e == frozenset([nidx[x[0]]]))
        print("\n%s %s-stranded: %d fragments; exact stranded class = {source} for %d"
              % ("paired" if paired else "single", proto, n_true, src_ok))
        for opt in ("unstranded", "--fr-stranded", "--rf-stranded"):
            extra = ["--plaintext"] + ([] if opt == "unstranded" else [opt]) + ([] if paired else ["--single-overhang"])
            if opt == "unstranded":
                exo = [comp.fragment_ec(x[3], x[4] if paired else None) for x in frags]
            else:
                exo = [ec_str(x, opt[2:4]) for x in frags]
            exp_al = sum(1 for e in exo if e); exp_u = sum(1 for e in exo if len(e) == 1)
            out, err = run_quant(idx, d, frags, paired=paired, name="s_%d_%s_%s" % (paired, proto, opt.strip("-")),
                                 extra=extra, single_l=220, single_s=35)
            ab = read_abundance(os.path.join(out, "abundance.tsv"))
            ri = read_run_info(os.path.join(out, "run_info.json"))
            simc = collections.Counter(x[0] for x in frags)
            err_abs = sum(abs(ab[n]["est_counts"] - simc[n]) for n in names)
            matching = (opt == "--%s-stranded" % proto)
            opposite = (opt != "unstranded" and not matching)
            ok = ri["n_pseudoaligned"] == exp_al and ri["n_unique"] == exp_u
            if matching:
                # every read kept and assigned to its source exactly
                ok = ok and err_abs < 1e-6
            fails += not ok
            print("%s   %-14s n_pseudoaligned %6d (exact %6d), n_unique %6d (exact %6d); sum |est - simulated source counts| = %.1f"
                  % ("ok  " if ok else "FAIL", opt, ri["n_pseudoaligned"], exp_al,
                     ri["n_unique"], exp_u, err_abs))
print("\nFAILURES:", fails)
