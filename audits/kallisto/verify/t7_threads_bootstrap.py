"""T7: threads, bootstraps and run_info.json.

(a) `quant -b B --plaintext` with -t 1, 2, 4: number of bs_abundance_*.tsv
    files written, the run_info.json n_bootstraps field, the exit status and
    any message.  In main.cpp (quant) the multi-threaded bootstrap branch is
    `#ifdef USE_HDF5 BootstrapThreadPool pool(...) #endif`; on a build
    without HDF5 (the CMake default since 0.50, and gen_release.sh) the branch
    is empty.  With -t 1 the same build writes all B tables, so the -t 1
    tables are the reference: with -t > 1 every bootstrap should still be
    written, and with the same --seed give identical tables (seeds are drawn
    before the branch).
(b) Determinism: abundance.tsv and run_info counts with -t 1 vs -t 4.
(c) run_info.json: n_processed / n_pseudoaligned / n_unique /
    p_pseudoaligned against the truth on a sample with 10 % random
    (unalignable) pairs and 0.5 % substitution errors in the rest:
    n_processed = all pairs; random pairs never pseudoalign; p_pseudoaligned
    = 100 * n_pseudoaligned / n_processed to one decimal.
"""
import os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *

rng = random.Random(8)
d = tmpdir()
ver = kversion()
print("kallisto", ver)

tx = make_transcriptome(rng, n_genes=40, max_iso=4)
names = list(tx)
idx = build_index(tx, d)
rho = {n: rng.lognormvariate(1, 1) for n in names}
p = gauss_fld(250, 40)
frags, _ = simulate(rng, tx, rho, p, 20000, read_len=75)


def mutate(s, rate):
    s = list(s)
    for i in range(len(s)):
        if rng.random() < rate:
            s[i] = rng.choice([c for c in "ACGT" if c != s[i]])
    return "".join(s)


fails = 0
B = 8
ref = None
print("\n(a) bootstraps, -b %d --plaintext --seed 42" % B)
for t in (1, 2, 4):
    out = os.path.join(d, "bs_t%d" % t)
    r1 = os.path.join(d, "a_1.fq"); r2 = os.path.join(d, "a_2.fq")
    write_fastq(r1, [x[3] for x in frags]); write_fastq(r2, [x[4] for x in frags])
    pr = run_quant_files(idx, out, ["--plaintext", "-b", str(B), "--seed", "42", r1, r2], threads=t)
    files = sorted(f for f in os.listdir(out) if f.startswith("bs_abundance_"))
    ri = read_run_info(os.path.join(out, "run_info.json"))
    msgs = [l.strip() for l in pr.stderr.splitlines() if "bstrp" in l or "boot" in l.lower() or "warn" in l.lower()]
    tabs = [read_abundance(os.path.join(out, "bs_abundance_%d.tsv" % b)) for b in range(B)
            if os.path.exists(os.path.join(out, "bs_abundance_%d.tsv" % b))]
    if t == 1:
        ref = tabs
        same = None
    else:
        same = (len(tabs) == len(ref) and all(
            all(abs(a[n]["est_counts"] - b[n]["est_counts"]) < 1e-6 for n in names) for a, b in zip(tabs, ref)))
    ok = len(files) == B and ri["n_bootstraps"] == B and (same is None or same)
    fails += not ok
    print("%s -t %d: exit %d, bs_abundance files %d of %d, run_info n_bootstraps %d, identical to -t 1: %s; bootstrap messages: %d lines%s"
          % ("ok  " if ok else "FAIL", t, pr.returncode, len(files), B, ri["n_bootstraps"],
             "-" if same is None else same, len(msgs), (" (last: %r)" % msgs[-1][-60:]) if msgs else ""))

print("\n(b) determinism, -t 1 vs -t 4")
o1 = os.path.join(d, "bs_t1"); o4 = os.path.join(d, "bs_t4")
a1 = read_abundance(os.path.join(o1, "abundance.tsv")); a4 = read_abundance(os.path.join(o4, "abundance.tsv"))
r1i = read_run_info(os.path.join(o1, "run_info.json")); r4i = read_run_info(os.path.join(o4, "run_info.json"))
mx = max(abs(a1[n]["est_counts"] - a4[n]["est_counts"]) for n in names)
ok = mx < 1e-3 and all(r1i[k] == r4i[k] for k in ("n_processed", "n_pseudoaligned", "n_unique"))
fails += not ok
print("%s est_counts max |diff| %.2e; n_processed %d/%d, n_pseudoaligned %d/%d, n_unique %d/%d"
      % ("ok  " if ok else "FAIL", mx, r1i["n_processed"], r4i["n_processed"], r1i["n_pseudoaligned"],
         r4i["n_pseudoaligned"], r1i["n_unique"], r4i["n_unique"]))

print("\n(c) run_info with random pairs and substitution errors")
comp = Compat(tx)
mix = []
n_rand = 0
for x in frags:
    if rng.random() < 0.10:
        mix.append(("RANDOM", 0, 0, rand_seq(rng, 75), rand_seq(rng, 75), False)); n_rand += 1
    else:
        mix.append((x[0], x[1], x[2], mutate(x[3], 0.005), mutate(x[4], 0.005), x[5]))
for t in (1, 4):
    out, err = run_quant(idx, d, mix, name="mix_t%d" % t, threads=t, extra=["--plaintext"])
    ri = read_run_info(os.path.join(out, "run_info.json"))
    ab = read_abundance(os.path.join(out, "abundance.tsv"))
    tot = sum(v["est_counts"] for v in ab.values())
    p_exp = "%.1f" % (100.0 * ri["n_pseudoaligned"] / ri["n_processed"])
    ok = (ri["n_processed"] == len(mix) and ri["n_pseudoaligned"] <= len(mix) - n_rand
          and abs(tot - ri["n_pseudoaligned"]) < 0.5 and ("%.1f" % ri["p_pseudoaligned"]) == p_exp)
    fails += not ok
    print("%s -t %d: n_processed %d (pairs %d), n_pseudoaligned %d (<= %d non-random), sum est_counts %.1f, p_pseudoaligned %s (recomputed %s)"
          % ("ok  " if ok else "FAIL", t, ri["n_processed"], len(mix), ri["n_pseudoaligned"], len(mix) - n_rand,
             tot, ri["p_pseudoaligned"], p_exp))

print("\nFAILURES:", fails)
