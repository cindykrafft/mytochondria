"""E1: sequence and domain E-values, -Z / --domZ scaling, hmmscan Z, thread invariance.

Truth: E = Z * P with P = exp(-lambda (s - tau)) for s >= tau (1 otherwise), lambda/tau from
the HMM file's 'STATS LOCAL FORWARD' line (the documented Forward-score exponential tail);
Z = number of target sequences (hmmsearch/phmmer) or models (hmmscan) unless -Z;
c-Evalue uses domZ = number of reported targets unless --domZ; i-Evalue uses Z.
Recomputed from the printed bit scores (rounded to 0.1), so tolerance is ~ +/-9 %.
"""
import os, sys
import _hm

R = _hm.Report("E1 E-values and search-space scaling")
db, truth = _hm.protein_db()
N = _hm.fasta_count(db)
hmms = {h["name"]: h for f in ("globins4", "fn3", "Pkinase") for h in _hm.read_hmms(os.path.join(_hm.TUT, f + ".hmm"))}


def search(hmmname, extra=(), tag="d"):
    tb, dt, o = _hm.path("%s_%s.tbl" % (hmmname, tag)), _hm.path("%s_%s.dtbl" % (hmmname, tag)), _hm.path("%s_%s.out" % (hmmname, tag))
    _hm.run([_hm.prog("hmmsearch"), "-o", o, "--tblout", tb, "--domtblout", dt] + list(extra) +
            [os.path.join(_hm.TUT, hmmname + ".hmm"), db])
    return _hm.read_tbl(tb), _hm.read_domtbl(dt), o


def check_formula(name, tbl, dtbl, Z, domZ=None, label=""):
    tau, lam = hmms[name]["stats"]["FORWARD"]
    nbad = sum(1 for r in tbl if not (_hm.eval_close(r["E"], Z * _hm.exp_surv(r["sc"], tau, lam), lam=lam)
                                      and _hm.eval_close(r["dE"], Z * _hm.exp_surv(r["dsc"], tau, lam), lam=lam)))
    R.check(nbad == 0, "%s %s: full-seq and best-domain E = Z*P(score), Z=%g, %d targets" % (name, label, Z, len(tbl)),
            "%d mismatches" % nbad)
    if domZ is None: domZ = len(tbl)
    nbi = sum(1 for r in dtbl if not _hm.eval_close(r["iE"], Z * _hm.exp_surv(r["dsc"], tau, lam), lam=lam))
    nbc = sum(1 for r in dtbl if not _hm.eval_close(r["cE"], domZ * _hm.exp_surv(r["dsc"], tau, lam), lam=lam))
    R.check(nbi == 0 and nbc == 0, "%s %s: i-Evalue = Z*P, c-Evalue = domZ*P (domZ=%g), %d domains" % (name, label, domZ, len(dtbl)),
            "%d i-E, %d c-E mismatches" % (nbi, nbc))
    # tblout 'rep' column == number of domtblout rows for that target
    cnt = {}
    for d in dtbl: cnt[d["t"]] = cnt.get(d["t"], 0) + 1
    nrep = sum(1 for r in tbl if r["rep"] != cnt.get(r["t"], 0))
    R.check(nrep == 0, "%s %s: tblout 'rep' equals domtblout rows per target" % (name, label), "%d differ" % nrep)


for name in ("globins4", "fn3", "Pkinase"):
    tbl, dtbl, _ = search(name)
    check_formula(name, tbl, dtbl, N, label="default")
    tblZ, dtblZ, _ = search(name, ["-Z", "1000000", "--domZ", "50"], tag="Z")
    check_formula(name, tblZ, dtblZ, 1e6, 50, label="-Z 1e6 --domZ 50")
    # reported set: with -Z larger, fewer pass E<=10; every reported target must satisfy it
    tau, lam = hmms[name]["stats"]["FORWARD"]
    over = [r for r in tblZ if 1e6 * _hm.exp_surv(r["sc"] + 0.05, tau, lam) > 10]
    R.check(not over, "%s: every target reported under -Z 1e6 has E <= 10" % name, "%d over" % len(over))
    tbl1, dtbl1, _ = search(name, ["--cpu", "0"], tag="cpu0")
    tbl4, dtbl4, _ = search(name, ["--cpu", "4"], tag="cpu4")
    same = [(r["t"], r["E"], r["sc"]) for r in tbl1] == [(r["t"], r["E"], r["sc"]) for r in tbl] == [(r["t"], r["E"], r["sc"]) for r in tbl4]
    samed = [(d["t"], d["af"], d["at"], d["ef"], d["et"], d["iE"]) for d in dtbl1] == [(d["t"], d["af"], d["at"], d["ef"], d["et"], d["iE"]) for d in dtbl4]
    R.check(same and samed, "%s: --cpu 0, default (2) and --cpu 4 give identical tables" % name)

# hmmscan: Z = number of models in the pressed database; scores symmetric with hmmsearch
hdb = _hm.path("models.hmm")
with open(hdb, "w") as f:
    for fn in ["globins4", "fn3", "Pkinase"]:
        f.write(open(os.path.join(_hm.TUT, fn + ".hmm")).read())
    for fn in sorted(os.listdir(_hm.TST)):
        if fn.endswith(".hmm") and fn not in ("20aa.hmm",):
            txt = open(os.path.join(_hm.TST, fn)).read()
            if "ALPH  amino" in txt and txt.startswith("HMMER3/f"): f.write(txt)
models = _hm.read_hmms(hdb)
_hm.run([_hm.prog("hmmpress"), "-f", hdb])
nm = len(models)
qs = [s for s in ("fn3_000_x1", "fn3_004_x2", "Pkinase_002_x3", "globins4_005_x3") if s in truth]
seqs = {}
cur = None
for ln in open(db):
    if ln.startswith(">"): cur = ln[1:].split()[0]; seqs[cur] = []
    else: seqs[cur].append(ln.strip())
allstats = {m["name"]: m["stats"]["FORWARD"] for m in models}
for q in qs:
    qf = _hm.write_fasta(_hm.path(q + ".fa"), [(q, "".join(seqs[q]))])
    tb, dt = _hm.path(q + ".scan.tbl"), _hm.path(q + ".scan.dtbl")
    _hm.run([_hm.prog("hmmscan"), "-o", "/dev/null", "--tblout", tb, "--domtblout", dt, hdb, qf])
    rows = _hm.read_tbl(tb)
    nbad = sum(1 for r in rows if not _hm.eval_close(r["E"], nm * _hm.exp_surv(r["sc"], *allstats[r["t"]])))
    R.check(nbad == 0 and rows, "hmmscan %s: E = (#models=%d) * P(score), %d hits" % (q, nm, len(rows)), "%d mismatches" % nbad)
    # symmetry: the same comparison via hmmsearch gives the same bit score
    fam = q.split("_")[0]
    tbS = _hm.path(q + ".sym.tbl")
    _hm.run([_hm.prog("hmmsearch"), "-o", "/dev/null", "--tblout", tbS, os.path.join(_hm.TUT, fam + ".hmm"), qf])
    s1 = [r["sc"] for r in rows if r["t"] == fam]; s2 = [r["sc"] for r in _hm.read_tbl(tbS)]
    R.check(s1 == s2, "hmmscan vs hmmsearch bit score for %s vs %s" % (q, fam), "%s vs %s" % (s1, s2))

# phmmer: query model built on the fly, its STATS are not visible; check Z scaling only
q = qs[0]; qf = _hm.path(q + ".fa")
t1, t2 = _hm.path("ph1.tbl"), _hm.path("ph2.tbl")
_hm.run([_hm.prog("phmmer"), "-o", "/dev/null", "--tblout", t1, qf, db])
_hm.run([_hm.prog("phmmer"), "-o", "/dev/null", "--tblout", t2, "-Z", "1000000", "-E", "1e9", qf, db])
a = {r["t"]: r for r in _hm.read_tbl(t1)}; b = {r["t"]: r for r in _hm.read_tbl(t2)}
ratios = [b[k]["E"] / a[k]["E"] for k in a if k in b and a[k]["E"] > 0]
ok = ratios and all(abs(x / (1e6 / N) - 1) < 0.06 for x in ratios)
R.check(ok, "phmmer: E(-Z 1e6)/E(default) = 1e6/N = %.1f for %d hits" % (1e6 / N, len(ratios)),
        "range %.1f-%.1f" % (min(ratios), max(ratios)) if ratios else "no hits")
R.done()
