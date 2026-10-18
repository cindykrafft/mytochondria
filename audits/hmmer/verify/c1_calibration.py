"""C1: hmmbuild calibration (lambda, mu, tau) and the empirical accuracy of P-values.

Truths:
 (a) p7_Lambda(): lambda = log 2 + 1.44 / (M * H), H = mean match-state relative entropy in
     bits against the default null (p7_AminoFrequencies / uniform DNA). Recomputed here from
     the emission probabilities written in the .hmm file (5-decimal -ln p).
 (b) The documented meaning of P: on sequences drawn i.i.d. from the null model, the
     fraction of comparisons with P <= p should be ~p in the tail (the user guide quotes a
     +/-15 % precision for tau). Sequences drawn here with Python's RNG; hmmsearch run with
     --max -Z 1 so that the printed E-value is P.
 (d) --eent effective sequence number: the built model's mean match relative entropy equals the
     target max(ere, (esigma - log2(2/(M(M+1))))/M), ere = 0.59 (amino) / 0.62 (DNA), esigma = 45
     (p7_builder.c effective_seqnumber), unless all sequences together stay above it.
 (c) hmmbuild calibration is deterministic for a fixed --seed (default 42) and identical
     across builds for the same input alignment.
"""
import math, os, random, sys
import _hm

R = _hm.Report("C1 calibration")
for fam in ("globins4", "fn3", "Pkinase", "MADE1"):
    sto = os.path.join(_hm.TUT, fam + ".sto")
    out = _hm.path(fam + ".hmm")
    _hm.run([_hm.prog("hmmbuild"), "-o", "/dev/null", out, sto])
    out2 = _hm.path(fam + ".2.hmm")
    _hm.run([_hm.prog("hmmbuild"), "-o", "/dev/null", out2, sto])
    H = _hm.read_hmms(out)[0]; H2 = _hm.read_hmms(out2)[0]
    bg = _hm.BGF if H["alph"] == "amino" else [0.25] * 4
    lam = math.log(2) + 1.44 / (H["M"] * _hm.mean_match_relent(H, bg))
    lam_file = H["stats"]["FORWARD"][1]
    R.check(abs(lam - lam_file) < 6e-5 and H["stats"]["MSV"][1] == H["stats"]["VITERBI"][1] == lam_file,
            "%s: lambda = log2 + 1.44/(M H) = %.5f; file %.5f (all three)" % (fam, lam, lam_file))
    R.check(H["stats"] == H2["stats"], "%s: hmmbuild twice with default seed gives identical STATS" % fam,
            "%s / %s" % (H["stats"], H2["stats"]))
    M = H["M"]; et = max(0.59 if H["alph"] == "amino" else 0.62, (45.0 - math.log2(2.0 / (M * (M + 1)))) / M)
    R.check(abs(_hm.mean_match_relent(H, bg) - et) < 0.003 or _hm.mean_match_relent(H, bg) > et,
            "%s: entropy weighting hits its target: mean match relent %.4f vs max(ere, (esigma - log2(2/(M(M+1))))/M) = %.4f" % (fam, _hm.mean_match_relent(H, bg), et))
    R.note("%s STATS: %s" % (fam, " ".join("%s %.4f %.5f" % (k, *v) for k, v in sorted(H["stats"].items()))))

# (b) empirical P-value calibration on i.i.d. null sequences
rng = random.Random(77)
NS = int(os.environ.get("C1_NSEQ", "100000"))
L = 300
db = _hm.write_fasta(_hm.path("null.fa"), [("n%06d" % i, _hm.rand_protein(rng, L)) for i in range(NS)])
for fam in ("globins4", "fn3", "Pkinase"):
    hm = _hm.path(fam + ".hmm")
    for extra, lab in (([], "default"), (["--nonull2"], "--nonull2")):
        tb = _hm.path("null_%s_%s.tbl" % (fam, lab))
        _hm.run([_hm.prog("hmmsearch"), "-o", "/dev/null", "--tblout", tb, "--max", "-Z", "1", "-E", "1", "--cpu", "4"] + extra + [hm, db])
        P = [r["E"] for r in _hm.read_tbl(tb)]
        line = []
        ok = True
        for p in (1e-1, 1e-2, 1e-3, 1e-4):
            obs = sum(1 for x in P if x <= p)
            exp = NS * p
            sd = math.sqrt(exp)
            line.append("P<=%g: %d (expect %.0f)" % (p, obs, exp))
            if p <= 1e-3 and not (exp / 1.5 - 3 * sd <= obs <= 1.5 * exp + 3 * sd): ok = False   # the exponential tail is only claimed below P ~ 1e-3
        R.check(ok, "%s %s: null comparisons with P <= 1e-3, 1e-4 within x1.5 of N*p (P<=0.1, 0.01 shown, not judged), L=%d, N=%d" % (fam, lab, L, NS), "; ".join(line))
R.done()
