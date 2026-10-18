"""T8: does `quant --bias` complete?  Paired-end and single-end runs with and
without --bias on a small random transcriptome; reports the exit status, the
last stderr line and whether abundance.tsv was written.  (Found while
running T6 across builds: the --bias runs did not finish on 0.50.1/0.51.1.)
The 0.52.0 commit d0ac69b ("fixes issues with num_trans") replaced
index.num_trans by target_lens_.size() in KmerIndex::loadTranscriptSequences
and weights.cpp::update_eff_lens, the code --bias runs."""
import os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *
rng = random.Random(9)
d = tmpdir()
print("kallisto", kversion())
tx = make_transcriptome(rng, n_genes=30)
idx = build_index(tx, d)
rho = {n: 1.0 for n in tx}
p = gauss_fld(250, 40)
for paired in (True, False):
    frags, _ = simulate(rng, tx, rho, p, 5000, paired=paired)
    for extra in ([], ["--bias"]):
        name = "r_%d_%s" % (paired, "bias" if extra else "nobias")
        out, err = run_quant(idx, d, frags, paired=paired, name=name, single_l=250, single_s=40,
                             extra=["--plaintext"] + extra, check=False)
        r1 = os.path.join(d, name + "_1.fq")
        args = [kbin(), "quant", "-i", idx, "-o", out + "_rc", "--plaintext"] + extra
        args += [r1, os.path.join(d, name + "_2.fq")] if paired else ["--single", "-l", "250", "-s", "40", r1]
        pr = subprocess.run(args, capture_output=True, text=True)
        last = [l for l in pr.stderr.splitlines() if l.strip()][-1:]
        print("%-6s %-8s exit %4d  abundance.tsv written: %-5s last stderr line: %s"
              % ("paired" if paired else "single", "--bias" if extra else "default", pr.returncode,
                 os.path.exists(os.path.join(out + "_rc", "abundance.tsv")), last[0][:70] if last else ""))
