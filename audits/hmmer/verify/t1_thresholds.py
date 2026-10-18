"""T1: reporting and inclusion thresholds (-E, -T, --domE, --domT, --incE, --incdomE,
--cut_ga/--cut_tc/--cut_nc) in hmmsearch and hmmscan.

Truth (user guide 'Controlling reporting/inclusion thresholds'; man pages): a target is reported
if E <= -E (or score >= -T); a domain of a reported target is reported if its *conditional*
E-value (domZ = number of reported targets) <= --domE (or score >= --domT); inclusion likewise
with --incE/--incdomE, and a domain can only be included if its target is. --cut_ga uses the
model's GA1 for targets and GA2 for domains (reporting and inclusion). The predicted sets are
computed in Python from a permissive run's scores (scores do not depend on thresholds) and the
STATS line, then compared with the tables and the '!' marks of the thresholded run.
"""
import os
import _hm

R = _hm.Report("T1 reporting and inclusion thresholds")
db, truth = _hm.protein_db()
N = _hm.fasta_count(db)


def run(hmm, extra, tag):
    tb, dt, o = _hm.path(tag + ".tbl"), _hm.path(tag + ".dtbl"), _hm.path(tag + ".out")
    _hm.run([_hm.prog("hmmsearch"), "-o", o, "--tblout", tb, "--domtblout", dt] + extra + [hmm, db])
    return _hm.read_tbl(tb), _hm.read_domtbl(dt), _hm.read_main_domains(o)


for fam in ("fn3", "Pkinase", "globins4"):
    hmm = os.path.join(_hm.TUT, fam + ".hmm")
    H = _hm.read_hmms(hmm)[0]; tau, lam = H["stats"]["FORWARD"]
    allt, alld, _ = run(hmm, ["-E", "1e9", "--domE", "1e9"], fam + "_all")
    P = lambda s: _hm.exp_surv(s, tau, lam)
    for E in (10, 1e-3, 1e-10):
        t, d, (doms, incl) = run(hmm, ["-E", str(E)], "%s_E%g" % (fam, E))
        pred = {r["t"] for r in allt if r["E"] <= E}
        amb = {r["t"] for r in allt if abs(r["E"] / E - 1) < 0.06}
        got = {r["t"] for r in t}
        R.check((pred ^ got) <= amb, "%s -E %g: reported targets = {E <= %g} (%d)" % (fam, E, E, len(got)), "diff %s" % sorted(pred ^ got)[:4])
        # domains: conditional E = domZ * P(dom score), domZ = #reported
        domZ = len(got)
        predd = {(r["t"], r["af"], r["at"]) for r in alld if r["t"] in got and domZ * P(r["dsc"]) <= 10}
        gotd = {(r["t"], r["af"], r["at"]) for r in d}
        ambd = {(r["t"], r["af"], r["at"]) for r in alld if r["t"] in got and abs(domZ * P(r["dsc"]) / 10 - 1) < 0.08}
        R.check((predd ^ gotd) <= ambd, "%s -E %g: reported domains = {domZ*P <= 10}, domZ=%d (%d domains)" % (fam, E, domZ, len(gotd)), "diff %s" % sorted(predd ^ gotd)[:3])
        # inclusion (defaults --incE 0.01, --incdomE 0.01)
        predi = [r["t"] for r in t if r["E"] <= 0.01]
        R.check(set(predi) == set(incl), "%s -E %g: targets above the inclusion line = {E <= 0.01} (%d)" % (fam, E, len(incl)))
        bad = [(k, v["cE"]) for k, v in doms.items() if v["inc"] != (k[0] in incl and v["cE"] <= 0.01)]
        R.check(not bad, "%s -E %g: domain '!' marks = target included and c-Evalue <= 0.01" % (fam, E), "%d differ %s" % (len(bad), bad[:3]))

    for T in (20.0, 50.0):
        t, d, (doms, incl) = run(hmm, ["-T", str(T), "--domT", str(T - 5)], "%s_T%g" % (fam, T))
        pred = {r["t"] for r in allt if r["sc"] >= T}
        amb = {r["t"] for r in allt if abs(r["sc"] - T) <= 0.05}
        got = {r["t"] for r in t}
        R.check((pred ^ got) <= amb, "%s -T %g: reported targets = {score >= T} (%d)" % (fam, T, len(got)), "diff %s" % sorted(pred ^ got)[:4])
        gotd = {(r["t"], r["af"], r["at"]) for r in d}
        predd = {(r["t"], r["af"], r["at"]) for r in alld if r["t"] in got and r["dsc"] >= T - 5}
        ambd = {(r["t"], r["af"], r["at"]) for r in alld if abs(r["dsc"] - (T - 5)) <= 0.05}
        R.check((predd ^ gotd) <= ambd, "%s --domT %g: reported domains = {dom score >= domT}" % (fam, T - 5), "diff %s" % sorted(predd ^ gotd)[:3])

    if H["cut"]:
        for cut in ("GA", "TC", "NC"):
            c1, c2 = H["cut"][cut]
            t, d, (doms, incl) = run(hmm, ["--cut_" + cut.lower()], "%s_%s" % (fam, cut))
            got = {r["t"] for r in t}
            pred = {r["t"] for r in allt if r["sc"] >= c1}
            amb = {r["t"] for r in allt if abs(r["sc"] - c1) <= 0.05}
            R.check((pred ^ got) <= amb, "%s --cut_%s: reported targets = {score >= %s1 = %.2f} (%d)" % (fam, cut.lower(), cut, c1, len(got)), "diff %s" % sorted(pred ^ got)[:4])
            predd = {(r["t"], r["af"], r["at"]) for r in alld if r["t"] in got and r["dsc"] >= c2}
            gotd = {(r["t"], r["af"], r["at"]) for r in d}
            ambd = {(r["t"], r["af"], r["at"]) for r in alld if abs(r["dsc"] - c2) <= 0.05}
            R.check((predd ^ gotd) <= ambd, "%s --cut_%s: reported domains = {dom score >= %s2 = %.2f} (%d)" % (fam, cut.lower(), cut, c2, len(gotd)), "diff %s" % sorted(predd ^ gotd)[:3])
            bad = [k for k, v in doms.items() if v["inc"] != (v["sc"] >= c2 - 0.05)]
            R.check(set(incl) == got and not bad, "%s --cut_%s: every reported target included; domain '!' = dom score >= %s2" % (fam, cut.lower(), cut), "bad %s" % bad[:3])

# hmmscan --cut_ga on query sequences carrying fn3/Pkinase domains, against a two-model database
hdb = _hm.path("ga2.hmm")
open(hdb, "w").write(open(os.path.join(_hm.TUT, "fn3.hmm")).read() + open(os.path.join(_hm.TUT, "Pkinase.hmm")).read())
_hm.run([_hm.prog("hmmpress"), "-f", hdb])
cuts = {h["name"]: h["cut"]["GA"] for h in _hm.read_hmms(hdb)}
qf = _hm.path("scanq.fa")
seqs, cur = {}, None
for ln in open(db):
    if ln.startswith(">"): cur = ln[1:].split()[0]; seqs[cur] = []
    else: seqs[cur].append(ln.strip())
qs = [k for k in seqs if k.startswith(("fn3", "Pkinase"))][:40] + [k for k in seqs if k.startswith("rnd")][:20]
_hm.write_fasta(qf, [(k, "".join(seqs[k])) for k in qs])
ta, da = _hm.path("scan_all.tbl"), _hm.path("scan_all.dtbl")
_hm.run([_hm.prog("hmmscan"), "-o", "/dev/null", "--tblout", ta, "--domtblout", da, "-E", "1e9", "--domE", "1e9", hdb, qf])
tg, dg = _hm.path("scan_ga.tbl"), _hm.path("scan_ga.dtbl")
_hm.run([_hm.prog("hmmscan"), "-o", "/dev/null", "--tblout", tg, "--domtblout", dg, "--cut_ga", hdb, qf])
A, AD, G, GD = _hm.read_tbl(ta), _hm.read_domtbl(da), _hm.read_tbl(tg), _hm.read_domtbl(dg)
pred = {(r["t"], r["q"]) for r in A if r["sc"] >= cuts[r["t"]][0]}
got = {(r["t"], r["q"]) for r in G}
amb = {(r["t"], r["q"]) for r in A if abs(r["sc"] - cuts[r["t"]][0]) <= 0.05}
R.check((pred ^ got) <= amb, "hmmscan --cut_ga: reported (model, query) pairs = {score >= GA1} (%d)" % len(got), "diff %s" % sorted(pred ^ got)[:4])
predd = {(r["t"], r["q"], r["af"]) for r in AD if (r["t"], r["q"]) in got and r["dsc"] >= cuts[r["t"]][1]}
gotd = {(r["t"], r["q"], r["af"]) for r in GD}
R.check(predd == gotd, "hmmscan --cut_ga: reported domains = {dom score >= GA2} (%d)" % len(gotd), "diff %s" % sorted(predd ^ gotd)[:4])
R.done()
