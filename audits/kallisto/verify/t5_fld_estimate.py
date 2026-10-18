"""T5: the paired-end fragment-length distribution estimate.

kallisto estimates the FLD from the first 10,000 pairs that pseudoalign to
exactly one target, using KmerIndex::mapPair, which returns a length only
when both mates' first k-mers lie on the same unitig, in the same EC block
(ProcessReads.cpp: `u.cardinality() == 1`, `0 < tl < 1000`).

Truth: fragments simulated from Gaussian FLDs; compared are the simulated
mean over all fragments, over the fragments whose exact class has one
target, and the "estimated average fragment length" kallisto prints; also
the effective lengths kallisto reports against L - mu_L + 1 from the true
FLD, and the resulting TPM shift by target length.

Transcriptomes: (S) single-isoform genes of 1.5-4 kb (one unitig per
target); (M) multi-isoform genes with 60-250-bp exons (unitigs break at
every exon shared by a subset of isoforms).
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sim import *

rng = random.Random(7)
d = tmpdir()
print("kallisto", kversion())

sets = {
    "S": dict(n_genes=150, max_iso=1, exon_len=(300, 800), n_exons=(3, 6)),
    "M": dict(n_genes=150, max_iso=6, exon_len=(60, 250), n_exons=(5, 12)),
}
for key, kw in sets.items():
    tx = make_transcriptome(rng, **kw)
    names = list(tx)
    idx = build_index(tx, d)
    comp = Compat(tx)
    rho = {n: rng.lognormvariate(1, 1) for n in names}
    for (m, s) in [(200, 30), (300, 60), (400, 80)]:
        p = gauss_fld(m, s)
        frags, expected = simulate(rng, tx, rho, p, 40000, read_len=75, paired=True)
        ex = [comp.fragment_ec(x[3], x[4]) for x in frags]
        all_mean = sum(x[2] for x in frags) / len(frags)
        u = [x[2] for x, e in zip(frags, ex) if len(e) == 1]
        u_mean = sum(u) / len(u)
        u10 = u[:10000]
        u10_mean = sum(u10) / len(u10)
        out, err = run_quant(idx, d, frags, paired=True, name="fld_%s_%d" % (key, m), extra=["--plaintext"])
        est = stderr_mean_fl(err)
        ab = read_abundance(os.path.join(out, "abundance.tsv"))
        ntx = len(names)
        print("\n[%s] %d targets, FLD N(%d,%d): mean all fragments %.1f | unique-class fragments %.1f (first 10,000: %.1f) | kallisto estimate %.1f (%+.1f vs all)"
              % (key, ntx, m, s, all_mean, u_mean, u10_mean, est, est - all_mean))
        # eff length and TPM consequence
        el_true = [eff_len_model(p, min(len(tx[n]), 999)) + max(0, len(tx[n]) - 999) for n in names]
        el_k = [ab[n]["eff_length"] for n in names]
        c = [ab[n]["est_counts"] for n in names]
        t_k = tpm_from(c, el_k)
        t_t = tpm_from(c, el_true)
        bins = [(0, 500), (500, 1000), (1000, 2000), (2000, 100000)]
        for lo, hi in bins:
            sel = [i for i, n in enumerate(names) if lo <= len(tx[n]) < hi and c[i] > 0]
            if not sel:
                continue
            r = [t_k[i] / t_t[i] for i in sel]
            r.sort()
            print("   L in [%5d,%5d): %3d targets, TPM(kallisto eff_length) / TPM(true-FLD eff_length): median %.3f, range %.3f-%.3f"
                  % (lo, hi, len(sel), r[len(r) // 2], r[0], r[-1]))
