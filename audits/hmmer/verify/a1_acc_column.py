"""A1: the domtblout/main-output 'acc' column versus its documented definition.

User guide (tabular.tex, field 22): 'acc: The mean posterior probability of aligned residues in
the MEA alignment'. Code (p7_tophits.c): oasc / (1 + |jenv - ienv|), where oasc is the optimal
accuracy score of the *envelope* (expected number of correctly decoded residues over the whole
envelope, flanking N/C residues included). Truth here: the mean of the per-residue posterior
probabilities printed on the PP line of each domain's alignment (one character per aligned
target residue: '*' = [0.95,1.0], digit d = [d/10 - 0.05, d/10 + 0.05)), compared with acc for
domains whose envelope equals the alignment and for domains whose envelope is wider.
"""
import os, re
import _hm

R = _hm.Report("A1 domain 'acc' column vs the mean posterior probability of aligned residues")
db, truth = _hm.protein_db()
mid = {c: (0.975 if c == "*" else (0.025 if c == "0" else int(c) / 10.0)) for c in "*0123456789"}
lo = {c: (0.95 if c == "*" else max(0.0, int(c) / 10.0 - 0.05)) for c in "*0123456789"}
hi = {c: (1.0 if c == "*" else min(1.0, int(c) / 10.0 + 0.05)) for c in "*0123456789"}
rows = []
for fam in ("fn3", "Pkinase", "globins4"):
    o = _hm.path(fam + ".out")
    _hm.run([_hm.prog("hmmsearch"), "-o", o, "--notextw", os.path.join(_hm.TUT, fam + ".hmm"), db])
    doms, _ = _hm.read_main_domains(o)
    lines = open(o).read().splitlines()
    cur, dn = None, None
    pp = {}
    for i, ln in enumerate(lines):
        if ln.startswith(">> "): cur = ln.split()[1]
        m = re.match(r"^\s+== domain (\d+)", ln)
        if m: dn = int(m.group(1))
        if ln.rstrip().endswith(" PP") and cur and dn:
            pp[(cur, dn)] = ln.rstrip()[:-3].strip()
    for k, d in doms.items():
        if k not in pp: continue
        s = [c for c in pp[k] if c in mid]
        rows.append((fam, k, d, sum(mid[c] for c in s) / len(s), sum(lo[c] for c in s) / len(s), sum(hi[c] for c in s) / len(s)))
same = [r for r in rows if r[2]["ef"] == r[2]["af"] and r[2]["et"] == r[2]["at"]]
wide = [r for r in rows if not (r[2]["ef"] == r[2]["af"] and r[2]["et"] == r[2]["at"])]
for lab, grp in (("envelope == alignment", same), ("envelope wider than alignment", wide)):
    inside = sum(1 for r in grp if r[4] - 0.005 <= r[2]["acc"] <= r[5] + 0.005)
    below = sum(1 for r in grp if r[2]["acc"] < r[4] - 0.005)
    R.note("%s: %d domains; acc within the PP-derived bounds for %d, below them for %d" % (lab, len(grp), inside, below))
    if grp:
        ex = sorted(grp, key=lambda r: r[2]["acc"] - r[3])[:3]
        for fam, k, d, m, l, h in ex:
            R.note("   %s %s #%d ali %d-%d env %d-%d: acc %.2f, mean PP of aligned residues %.2f [%.2f, %.2f]" % (fam, k[0], k[1], d["af"], d["at"], d["ef"], d["et"], d["acc"], m, l, h))
R.check(all(r[4] - 0.005 <= r[2]["acc"] <= r[5] + 0.005 for r in same), "acc agrees with the PP line when the envelope equals the alignment")
R.check(all(r[4] - 0.005 <= r[2]["acc"] <= r[5] + 0.005 for r in wide),
        "acc = mean posterior probability of aligned residues (documented) when the envelope is wider",
        "%d of %d domains fall below the bounds" % (sum(1 for r in wide if r[2]["acc"] < r[4] - 0.005), len(wide)))
R.done()
