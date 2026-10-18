"""D1: dv:f (approximate divergence from minimizers, PAF without -c; esterr.c).

mm_est_err() counts matched minimizers n_match between the first and last
anchor of the chain and adds one expected-but-missing minimizer at each end
when both the query and the reference continue past the chain by more than k:

    if (r->qs > avg_k && r->rs > avg_k) ++n_tot;                  // left end
    if (qlen - r->qs > avg_k && l_ref - r->re > avg_k) ++n_tot;   // right end (esterr.c:61)

The right-end test uses r->qs where the query's remaining length is qlen - r->qe.
Truth: an error-free read taken from the reference has divergence 0; the port
of the formula with qe gives 0 for it, the port with qs gives
1 - (n/(n+1))^(1/k) whenever the reference continues past the read.
Reads: error-free, forward and reverse, 500 bp - 20 kb, from the interior of a
random reference, ending exactly at the reference end, and starting at 0.
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(5)
G = 400000
ref = rand_seq(rng, G)
d = tmpdir()
fa = os.path.join(d, "ref.fa")
write_fasta(fa, [("chr1", ref)])
print(version(), f" reference {G} bp random; default preset (map-ont), PAF, no -c")
reads, where = [], {}
for L in (500, 1000, 2000, 5000, 20000):
    for k in range(4):
        st = rng.randint(30000, G - 30000 - L)
        for fw in (True, False):
            s = ref[st:st + L]
            n = f"interior_L{L}_{k}_{'f' if fw else 'r'}"
            reads.append((n, s if fw else revcomp(s))); where[n] = "interior"
    for fw in (True, False):
        n = f"refend_L{L}_{'f' if fw else 'r'}"
        s = ref[G - L:]
        reads.append((n, s if fw else revcomp(s))); where[n] = "ends at the reference end"
        n = f"refstart_L{L}_{'f' if fw else 'r'}"
        s = ref[:L]
        reads.append((n, s if fw else revcomp(s))); where[n] = "starts at the reference start"
fq = os.path.join(d, "r.fq")
write_fastq(fq, reads)
recs = [r for r in parse_paf(run(["-t1", fa, fq])) if r["tags"].get("tp") == "P"]
avg_k = 15.0
print(f"{'read':26s} {'qlen':>6s} {'qs':>4s} {'qe':>6s} {'rs':>7s} {'re':>7s} {'cm':>5s} {'dv:f':>8s} {'port(qe)':>9s} {'port(qs)':>9s}")
n_bad = n_qs = 0
by = {}
for r in recs:
    cm = r["tags"]["cm"]
    dv = r["tags"].get("dv", None)
    # n_match == cm for an error-free read (every chain anchor is a matched minimizer);
    # left/right extra counts per the code with qe (intended) and with qs (as written)
    left = 1 if (r["qs"] > avg_k and r["ts"] > avg_k) else 0
    right_qe = 1 if (r["qlen"] - r["qe"] > avg_k and r["tlen"] - r["te"] > avg_k) else 0
    right_qs = 1 if (r["qlen"] - r["qs"] > avg_k and r["tlen"] - r["te"] > avg_k) else 0
    def port(extra):
        nt = cm + extra
        return 0.0 if cm >= nt else 1.0 - (cm / nt) ** (1.0 / avg_k)
    pqe, pqs = port(left + right_qe), port(left + right_qs)
    ok = dv is not None and abs(dv - 0.0) < 1e-9
    if not ok: n_bad += 1
    if dv is not None and abs(dv - round(pqs, 4)) < 1e-4: n_qs += 1
    by.setdefault(where[r["qname"]], []).append(dv)
    print(f"{r['qname']:26s} {r['qlen']:6d} {r['qs']:4d} {r['qe']:6d} {r['ts']:7d} {r['te']:7d} {cm:5d} {dv!s:>8s} {pqe:9.4f} {pqs:9.4f}")
print(f"\n{len(recs)} error-free reads: dv:f == 0 on {len(recs) - n_bad}; dv:f equals the port with qs on {n_qs}/{len(recs)}")
for w, v in by.items():
    print(f"  {w:32s}: {len(v)} reads, dv:f > 0 on {sum(1 for x in v if x)}; values {sorted(set(v))}")
