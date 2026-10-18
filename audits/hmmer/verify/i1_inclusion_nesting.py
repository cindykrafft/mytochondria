"""I1: are included hits always reported hits?

Man pages: 'Inclusion thresholds are stricter than reporting thresholds'; p7_tophits_Threshold()
comment: '(sequence|domain) must be reported to be included'. Sequences follow this (a target
must pass -E to be flagged included). Truth for domains: with --domE stricter than --incdomE, a
domain that is not reported should not be included either. Observed through the -A alignment
(which holds the included domains), the tblout 'rep'/'inc' columns and the domtblout rows.
"""
import os, re
import _hm

R = _hm.Report("I1 inclusion nested in reporting")
db, _ = _hm.protein_db()
hmm = os.path.join(_hm.TUT, "fn3.hmm")
for extra, lab in ((["-E", "1e-20"], "-E 1e-20 (default --incE 0.01)"), (["--domE", "1e-12"], "--domE 1e-12 (default --incdomE 0.01)")):
    a, t, d = _hm.path("a.sto"), _hm.path("t.tbl"), _hm.path("d.dtbl")
    _hm.run([_hm.prog("hmmsearch"), "-o", "/dev/null", "-A", a, "--tblout", t, "--domtblout", d] + extra + [hmm, db])
    rows = _hm.read_tbl(t)
    ndom_rep = len(_hm.read_domtbl(d))
    seqs_in_ali = {ln.split()[1].split("/")[0] for ln in open(a) if ln.startswith("#=GS")}
    ndom_ali = sum(1 for ln in open(a) if ln.startswith("#=GS"))
    rep_targets = {r["t"] for r in rows}
    R.note("%s: %d targets reported, %d domains reported (domtblout); tblout sum(rep)=%d sum(inc)=%d; -A alignment: %d domains from %d targets"
           % (lab, len(rows), ndom_rep, sum(r["rep"] for r in rows), sum(r["inc"] for r in rows), ndom_ali, len(seqs_in_ali)))
    R.check(seqs_in_ali <= rep_targets and ndom_ali <= ndom_rep and all(r["inc"] <= r["rep"] for r in rows),
            "%s: every included target/domain is also reported" % lab,
            "%d included domains but only %d reported" % (ndom_ali, ndom_rep) if ndom_ali > ndom_rep else "")
R.done()
