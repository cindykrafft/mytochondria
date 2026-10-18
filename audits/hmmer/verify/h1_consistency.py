"""H1: consistency checks with an independent route to the same number.

 (a) Filter heuristics do not change scores or E-values (man pages: 'changing filter thresholds
     does not alter bit scores, E-values, or alignments'): default vs --max on human Swiss-Prot,
     every target found by both gets the same E-value and score.
 (b) jackhmmer's last round equals hmmsearch with the checkpointed model of that round
     (--chkhmm), same database: same targets, same scores to 0.1 bit; E-values equal up to the
     rounding of the model file (5-decimal -ln p emission/transition parameters).
"""
import os
import _hm

R = _hm.Report("H1 consistency: --max vs default, jackhmmer vs hmmsearch on its checkpoint")
sp = os.path.join(_hm.SCR, "data", "uniprot", "human_sprot.fa")
for fam in ("fn3", "Pkinase"):
    hmm = os.path.join(_hm.TUT, fam + ".hmm")
    t0, t1 = _hm.path(fam + "_def.tbl"), _hm.path(fam + "_max.tbl")
    _hm.run([_hm.prog("hmmsearch"), "--cpu", "4", "-o", "/dev/null", "--tblout", t0, hmm, sp])
    _hm.run([_hm.prog("hmmsearch"), "--cpu", "4", "-o", "/dev/null", "--tblout", t1, "--max", hmm, sp])
    a = {r["t"]: r for r in _hm.read_tbl(t0)}; b = {r["t"]: r for r in _hm.read_tbl(t1)}
    com = [k for k in a if k in b]
    diff = [k for k in com if (a[k]["E"], a[k]["sc"], a[k]["dsc"]) != (b[k]["E"], b[k]["sc"], b[k]["dsc"])]
    R.check(not diff and len(com) == len(a), "%s on human Swiss-Prot: %d default hits all found under --max with identical E/score (--max adds %d)" % (fam, len(a), len(b) - len(com)),
            "%d differ" % len(diff))

db, _ = _hm.protein_db()
jdb = _hm.path("jdb.fa")
open(jdb, "w").write(open(db).read() + open(os.path.join(_hm.TUT, "globins45.fa")).read())
chk = _hm.path("jk")
jo, jt = _hm.path("jk.out"), _hm.path("jk.tbl")
_hm.run([_hm.prog("jackhmmer"), "-N", "4", "--chkhmm", chk, "--tblout", jt, "-o", jo, os.path.join(_hm.TUT, "HBB_HUMAN"), jdb])
rounds = sorted(int(f.split("-")[-1].split(".")[0]) for f in os.listdir(_hm.WORK) if f.startswith("jk-") and f.endswith(".hmm"))
last = rounds[-1]
ht = _hm.path("hs.tbl")
_hm.run([_hm.prog("hmmsearch"), "-o", "/dev/null", "--tblout", ht, "%s-%d.hmm" % (chk, last), jdb])
A = {r["t"]: r for r in _hm.read_tbl(jt)}; B = {r["t"]: r for r in _hm.read_tbl(ht)}
R.note("jackhmmer: %d rounds; last round %d targets" % (last, len(A)))
same_t = set(A) == set(B)
sc_ok = all(abs(A[k]["sc"] - B[k]["sc"]) <= 0.1 for k in A if k in B)
e_ok = all(1 / 1.11 <= A[k]["E"] / B[k]["E"] <= 1.11 for k in A if k in B and B[k]["E"] > 0)   # two %.2g roundings
nd = sum(1 for k in A if k in B and A[k]["E"] != B[k]["E"])
R.check(same_t and sc_ok and e_ok, "jackhmmer round %d = hmmsearch with jk-%d.hmm: same targets, scores within 0.1 bit, E within two %%.2g roundings (x1.11)" % (last, last),
        "%d of %d printed E-values differ in the second digit" % (nd, len(A)))
R.done()
