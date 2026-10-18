"""T3: single-end reads near the 3' end of a target (default, without
--single-overhang).

In --single mode ProcessReads.cpp drops a target from a read's
pseudoalignment when the read's start plus the mean fragment length (-l)
would run past the target's end (forward reads) or before its start
(reverse reads).  The effective length used for the same target is
L - mu_L + 1 with mu_L the mean of the Gaussian(-l, -s) truncated at L,
i.e. it assumes fragments shorter than -l exist and were counted.

Truth: reads simulated under exactly that model (Gaussian(l, s) truncated
at L, uniform start), with known abundances; one isolated target per length
(unique k-mers, so every read is unambiguous and the EM is trivial).
Compares est_counts with the number of reads simulated from each target,
and TPM with the true TPM, with and without --single-overhang.
Also scans exact read positions to locate the cut.
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *

rng = random.Random(3)
d = tmpdir()
print("kallisto", kversion())

L_list = [120, 150, 180, 200, 220, 250, 300, 350, 400, 500, 700, 1000, 2000, 4000]
tx = collections.OrderedDict(("t%04d" % L, rand_seq(rng, L)) for L in L_list)
idx = build_index(tx, d)
names = list(tx)
rho = {n: 1.0 for n in names}       # equal true abundance (equal TPM)

for (l, s, rl) in [(200, 20, 75), (200, 30, 50), (180, 40, 75), (250, 50, 100)]:
    p = gauss_fld(l, s, minlen=1)
    frags, expected = simulate(rng, tx, rho, p, 60000, read_len=rl, paired=False)
    nsim = collections.Counter(x[0] for x in frags)
    res = {}
    for mode, extra in [("default", []), ("--single-overhang", ["--single-overhang"])]:
        out, err = run_quant(idx, d, frags, paired=False, single_l=l, single_s=s,
                             name="se_%d_%d_%d_%s" % (l, s, rl, mode.strip("-")), extra=["--plaintext"] + extra)
        res[mode] = (read_abundance(os.path.join(out, "abundance.tsv")),
                     read_run_info(os.path.join(out, "run_info.json")))
    true_tpm = 1e6 / len(names)
    print("\n--single -l %d -s %d, %d-bp reads, %d reads, equal true TPM %.0f for every target"
          % (l, s, rl, len(frags), true_tpm))
    for mode in res:
        print("  %-18s n_pseudoaligned %d of %d (p_pseudoaligned %s)" %
              (mode, res[mode][1]["n_pseudoaligned"], res[mode][1]["n_processed"], res[mode][1]["p_pseudoaligned"]))
    print("  %6s %8s %9s | %10s %9s | %10s %9s" % ("L", "eff_len", "simulated", "est(def)", "TPM(def)", "est(ovh)", "TPM(ovh)"))
    for n in names:
        a = res["default"][0][n]; b = res["--single-overhang"][0][n]
        print("  %6d %8.2f %9d | %10.1f %9.0f | %10.1f %9.0f" %
              (len(tx[n]), a["eff_length"], nsim[n], a["est_counts"], a["tpm"], b["est_counts"], b["tpm"]))

# exact position scan: one read at every start position of one 400-bp target,
# both orientations, -l 200; which starts are kept?
L = 400; n = "t0400"; s = tx[n]; rl = 50; l = 200
reads = []
for st in range(0, L - rl + 1):
    reads.append(("f", st, s[st:st + rl]))
    reads.append(("r", st, revcomp(s[st:st + rl])))
fq = os.path.join(d, "scan.fq")
write_fastq(fq, [r[2] for r in reads])
kept = {"f": [], "r": []}
# quantify each read on its own would be slow; bisect with blocks instead:
# run once per orientation with all reads and count, then locate the boundary
for o in ("f", "r"):
    sub = [r for r in reads if r[0] == o]
    lo_ok = []
    # query start positions in chunks of 1 to find the exact cut near the end
    probe = list(range(0, 10)) + list(range(L - l - 10, L - l + 12)) + list(range(l - rl - 10, l - rl + 12)) + list(range(L - rl - 5, L - rl + 1))
    for st in sorted(set(x for x in probe if 0 <= x <= L - rl)):
        r = [x for x in sub if x[1] == st][0]
        fq1 = os.path.join(d, "scan1.fq")
        write_fastq(fq1, [r[2]])
        out = os.path.join(d, "scan_%s_%d" % (o, st))
        pr = run_quant_files(idx, out, ["--single", "-l", str(l), "-s", "20", "--plaintext", fq1])
        ok = pr.returncode == 0 and read_run_info(os.path.join(out, "run_info.json"))["n_pseudoaligned"] == 1
        kept[o].append((st, ok))
print("\nposition scan, target L=%d, %d-bp reads, -l %d (0-based read start on the target strand):" % (L, rl, l))
for o, lab in (("f", "forward reads (fragment = [start, start+l))"), ("r", "reverse reads (fragment ends at start+rl)")):
    k = [st for st, ok in kept[o] if ok]
    dropped = [st for st, ok in kept[o] if not ok]
    print("  %s: probed %d starts, kept %d; dropped starts: %s" % (lab, len(kept[o]), len(k), dropped))
