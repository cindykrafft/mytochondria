"""Z1: -Z in the scan programs.

hmmscan -h / man: '-Z <x>: set # of comparisons done, for E-value calculation'; nhmmscan -h
prints the same text and its header echoes '# sequence search space set to: <x>'.
Truth: E-values are proportional to the search-space size, so -Z k * (default size) must scale
every E-value by k (hmmscan: default = number of models). Also checked: nhmmscan and nhmmer
give the same E-value for the same single-model comparison (both use P * 2L / MAXL).
"""
import os, random
import _hm

R = _hm.Report("Z1 -Z in hmmscan and nhmmscan")
# hmmscan
db, truth = _hm.protein_db()
hdb = _hm.path("two.hmm")
open(hdb, "w").write(open(os.path.join(_hm.TUT, "fn3.hmm")).read() + open(os.path.join(_hm.TUT, "Pkinase.hmm")).read())
_hm.run([_hm.prog("hmmpress"), "-f", hdb])
seqs, cur = {}, None
for ln in open(db):
    if ln.startswith(">"): cur = ln[1:].split()[0]; seqs[cur] = []
    else: seqs[cur].append(ln.strip())
q = sorted(k for k in seqs if k.startswith("fn3"))[:5]
qf = _hm.write_fasta(_hm.path("q.fa"), [(k, "".join(seqs[k])) for k in q])
t0, t1 = _hm.path("s0.tbl"), _hm.path("s1.tbl")
_hm.run([_hm.prog("hmmscan"), "-o", "/dev/null", "--tblout", t0, hdb, qf])
_hm.run([_hm.prog("hmmscan"), "-o", "/dev/null", "--tblout", t1, "-Z", "2000", "-E", "1e6", hdb, qf])
a = {(r["t"], r["q"]): r["E"] for r in _hm.read_tbl(t0)}; b = {(r["t"], r["q"]): r["E"] for r in _hm.read_tbl(t1)}
rat = [b[k] / a[k] for k in a if k in b and a[k] > 0]
R.check(rat and all(abs(x / 1000 - 1) < 0.06 for x in rat), "hmmscan: -Z 2000 (vs 2 models) scales E by 1000 (%d hits)" % len(rat),
        "ratios %.0f-%.0f" % (min(rat), max(rat)) if rat else "")

# nhmmscan / nhmmer
hmmf = _hm.path("MADE1.hmm")
open(hmmf, "w").write(open(os.path.join(_hm.TUT, "MADE1.hmm")).read())
_hm.run([_hm.prog("hmmpress"), "-f", hmmf])
rng = random.Random(3)
s = list(_hm.rand_dna(rng, 100000))
for i, d in enumerate(_hm.emit_core(os.path.join(_hm.TUT, "MADE1.hmm"), 3, 4)):
    p = 20000 * (i + 1); s[p:p + len(d)] = list(d)
qd = _hm.write_fasta(_hm.path("dq.fa"), [("dq", "".join(s))])
n0, n1, nh = _hm.path("n0.tbl"), _hm.path("n1.tbl"), _hm.path("nh.tbl")
o1 = _hm.path("n1.out")
_hm.run([_hm.prog("nhmmscan"), "-o", "/dev/null", "--tblout", n0, hmmf, qd])
_hm.run([_hm.prog("nhmmscan"), "-o", o1, "--tblout", n1, "-Z", "1000", hmmf, qd])
_hm.run([_hm.prog("nhmmer"), "-o", "/dev/null", "--tblout", nh, hmmf, qd])
A = {(r["af"], r["at"]): r["E"] for r in _hm.read_nhmmer_tbl(n0)}
B = {(r["af"], r["at"]): r["E"] for r in _hm.read_nhmmer_tbl(n1)}
C = {(r["af"], r["at"]): r["E"] for r in _hm.read_nhmmer_tbl(nh)}
hdr = [ln for ln in open(o1) if "search space" in ln]
R.note("nhmmscan header with -Z 1000: %s" % (hdr[0].strip() if hdr else "(no line)"))
for k in sorted(A): R.note("hit %d-%d: nhmmscan E %.2g | nhmmscan -Z 1000 E %.2g | nhmmer E %.2g" % (k[0], k[1], A[k], B.get(k, float('nan')), C.get(k, float('nan'))))
R.check(A == C, "nhmmscan and nhmmer give the same E-values for the same one-model comparison (%d hits)" % len(A))
rat = [B[k] / A[k] for k in A if k in B and A[k] > 0]
R.check(rat and all(abs(x / 1000 - 1) < 0.06 for x in rat), "nhmmscan: -Z 1000 (vs 1 model) scales E by 1000",
        "E-values unchanged: ratios %s" % sorted(set(round(x, 3) for x in rat)))
R.done()
