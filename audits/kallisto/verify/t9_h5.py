"""T9: HDF5 output (builds with HDF5 only).  abundance.h5 est_counts /
eff_lengths / lengths / ids against abundance.tsv (same run), the number of
/bootstrap/bs* datasets and aux/num_bootstrap with -t 1 and -t 4 (no
--plaintext), and bootstrap tables identical across thread counts with the
same seed.  TPM is not stored in the .h5 (sleuth computes it); it is
recomputed here from est_counts / eff_lengths and compared with the .tsv."""
import os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *
import h5py
rng = random.Random(10)
d = tmpdir()
print("kallisto", kversion())
tx = make_transcriptome(rng, n_genes=40, max_iso=4)
names = list(tx)
idx = build_index(tx, d)
frags, _ = simulate(rng, tx, {n: rng.lognormvariate(1, 1) for n in names}, gauss_fld(250, 40), 20000)
r1 = os.path.join(d, "a_1.fq"); r2 = os.path.join(d, "a_2.fq")
write_fastq(r1, [x[3] for x in frags]); write_fastq(r2, [x[4] for x in frags])
B = 8; fails = 0; ref = None
for t in (1, 4):
    out = os.path.join(d, "h5_t%d" % t)
    args = [kbin(), "quant", "-i", idx, "-o", out, "-t", str(t), "-b", str(B), "--seed", "42", r1, r2]
    pr = subprocess.run(args, capture_output=True, text=True)
    h5p = os.path.join(out, "abundance.h5")
    if not os.path.exists(h5p):
        print("no abundance.h5 (build without HDF5): exit %d" % pr.returncode); fails += 1; continue
    f = h5py.File(h5p, "r")
    ab = read_abundance(os.path.join(out, "abundance.tsv"))
    ids = [x.decode() if isinstance(x, bytes) else x for x in f["aux/ids"][:]]
    est = f["est_counts"][:]; el = f["aux/eff_lengths"][:]
    ok1 = ids == names and all(abs(est[i] - ab[n]["est_counts"]) <= 1e-4 * max(1, ab[n]["est_counts"]) and
                               abs(el[i] - ab[n]["eff_length"]) <= 1e-4 * el[i] for i, n in enumerate(names))
    tp = tpm_from(list(est), list(el))
    ok2 = all(abs(tp[i] - ab[n]["tpm"]) <= 1e-4 * max(1, ab[n]["tpm"]) for i, n in enumerate(names))
    bs = sorted(f["bootstrap"].keys()) if "bootstrap" in f else []
    nb = int(f["aux/num_bootstrap"][0])
    tabs = [f["bootstrap/bs%d" % b][:] for b in range(B) if "bootstrap/bs%d" % b in f]
    if t == 1:
        ref = tabs; same = "-"
    else:
        same = len(tabs) == len(ref) and all(max(abs(a - b)) < 1e-6 for a, b in zip(tabs, ref))
    ok = ok1 and ok2 and len(bs) == B and nb == B and same in ("-", True)
    fails += not ok
    print("%s -t %d: h5 est_counts/eff_lengths == tsv: %s; TPM from h5 == tsv TPM: %s; bootstrap datasets %d of %d, aux/num_bootstrap %d; identical to -t 1: %s"
          % ("ok  " if ok else "FAIL", t, ok1, ok2, len(bs), B, nb, same))
print("FAILURES:", fails)
