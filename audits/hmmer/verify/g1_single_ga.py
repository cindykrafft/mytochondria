"""G1: a protein Stockholm alignment with a single value on '#=GF GA'.

Easel accepts '#=GF GA <x>;' with one value. For DNA models the HMM reader sets GA2 = GA1 when
the file has one value (p7_hmmfile.c). Truth: --cut_ga should then apply x to domains as well
(or the build should reject the line); a domain threshold of -99999 (p7_CUTOFF_UNSET) is not a
gathering threshold. Observed: the GA line hmmbuild writes and the lowest domain score that
hmmsearch --cut_ga reports.
"""
import os
import _hm

R = _hm.Report("G1 single-value GA line in a protein alignment")
sto = _hm.path("fn3_1ga.sto")
txt = open(os.path.join(_hm.TUT, "fn3.sto")).read()
import re
txt = re.sub(r"^#=GF GA\s+.*$", "#=GF GA   24.50;", txt, flags=re.M)
open(sto, "w").write(txt)
hm = _hm.path("fn3_1ga.hmm")
_hm.run([_hm.prog("hmmbuild"), "-o", "/dev/null", hm, sto])
ga = [ln.strip() for ln in open(hm) if ln.startswith("GA")]
R.note("hmmbuild writes: %s" % ga)
d = _hm.path("g.dtbl"); t = _hm.path("g.tbl")
_hm.run([_hm.prog("hmmsearch"), "-o", "/dev/null", "--cut_ga", "--tblout", t, "--domtblout", d, hm, os.path.join(_hm.SCR, "data", "stress_multidom.fa")])
dom = _hm.read_domtbl(d); seq = _hm.read_tbl(t)
low = sorted(x["dsc"] for x in dom)[:3]
R.note("--cut_ga: %d targets (lowest seq score %.1f), %d domains, lowest domain scores %s" % (len(seq), min(r["sc"] for r in seq), len(dom), low))
R.check(min(x["dsc"] for x in dom) >= 24.5 - 0.05, "--cut_ga applies GA = 24.50 to domains when only one GA value is given",
        "domains down to %.1f bits reported (GA2 written as %s)" % (low[0], ga[0].split()[-1] if ga else "?"))
R.done()
