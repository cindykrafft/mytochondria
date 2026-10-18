"""X1: what HM1 and HM2 do to the numbers a paper takes from hmmsearch.

Runs the tutorial fn3, Pkinase and globins4 models against (a) human Swiss-Prot (20,431 reviewed
entries, fetched from rest.uniprot.org; md5 recorded next to it) and (b) a synthetic stress set
of 300 multidomain sequences (2-6 emitted domains, half with a biased-composition segment
inserted inside the domain) plus 2,000 random sequences, with four builds of the same develop
source: unchanged, HM1 fix only, HM2 fix only, both fixes (the fix branch). Reports how many
sequence/domain rows change, by how much, and the largest examples. Default options throughout.
"""
import os, sys
import _hm

S = _hm.SCR
builds = [("develop", os.path.join(S, "hmmer", "src")), ("HM1 only", os.path.join(S, "pA", "src")),
          ("HM2 only", os.path.join(S, "pB", "src")), ("HM1+HM2", os.path.join(S, "hmmer-fix", "src"))]
dbs = [("human Swiss-Prot", os.path.join(S, "data", "uniprot", "human_sprot.fa")),
       ("stress multidomain", os.path.join(S, "data", "stress_multidom.fa"))]
print("# X1 null2-by-trace fixes: effect on hmmsearch tables (default options)")
for b in builds: print("# build %-9s %s" % (b[0], b[1]))
for dbname, db in dbs:
    print("\n## %s (%d sequences)" % (dbname, _hm.fasta_count(db)))
    for fam in ("fn3", "Pkinase", "globins4"):
        hmm = os.path.join(_hm.TUT, fam + ".hmm")
        res = {}
        for bn, bd in builds:
            tb, dt = _hm.path("%s_%s_%s.tbl" % (dbname[:5], fam, bn[:3])), _hm.path("%s_%s_%s.dtbl" % (dbname[:5], fam, bn[:3]))
            _hm.run([os.path.join(bd, "hmmsearch"), "--cpu", "4", "-o", "/dev/null", "--tblout", tb, "--domtblout", dt, hmm, db])
            res[bn] = ({r["t"]: r for r in _hm.read_tbl(tb)}, _hm.read_domtbl(dt))
        a, ad = res["develop"]
        nclu = sum(1 for k in a if a[k]["clu"] > 0)
        for bn, _ in builds[1:]:
            b, bd_ = res[bn]
            com = [k for k in a if k in b]
            ds = [b[k]["sc"] - a[k]["sc"] for k in com]
            er = [b[k]["E"] / a[k]["E"] for k in com if a[k]["E"] > 0]
            key = lambda d: (d["t"], d["ef"], d["et"])
            da = {key(d): d for d in ad}; db_ = {key(d): d for d in bd_}
            dch = [k for k in da if k in db_ and (da[k]["dsc"], da[k]["dbias"], da[k]["iE"]) != (db_[k]["dsc"], db_[k]["dbias"], db_[k]["iE"])]
            inc = len({k for k in a if a[k]["E"] <= 0.01} ^ {k for k in b if b[k]["E"] <= 0.01})
            print("%-9s %-8s reported %4d (clustered %3d): seq score changed %3d, max |d| %.1f bits, E ratio %.2f-%.2f; domain rows changed %3d; reported-set diff %d; E<=0.01 set diff %d"
                  % (fam, bn, len(a), nclu, sum(1 for x in ds if x), max(map(abs, ds)) if ds else 0, min(er) if er else 1, max(er) if er else 1,
                     len(dch), len(set(a) ^ set(b)), inc))
        b, _ = res["HM1+HM2"]
        top = sorted((k for k in a if k in b), key=lambda k: -abs(b[k]["sc"] - a[k]["sc"]))[:3]
        for k in top:
            if b[k]["sc"] != a[k]["sc"]:
                print("    e.g. %-28s score %6.1f -> %6.1f  bias %4.1f -> %4.1f  E %8.2g -> %8.2g  (clu %d, dom %d)"
                      % (k[:28], a[k]["sc"], b[k]["sc"], a[k]["bias"], b[k]["bias"], a[k]["E"], b[k]["E"], a[k]["clu"], a[k]["dom"]))
