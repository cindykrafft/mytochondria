#!/usr/bin/env python3
"""TC1: in ILLUMINACLIP palindrome mode a mismatch is penalised by the integer
quotient Q/10 (0 for Q < 10, 1 for Q 10-19, ...) instead of the documented Q/10.

IlluminaClippingTrimmer.calculatePalindromeDifferenceQuality (main @ ef98d62,
src/main/java/org/usadellab/trimmomatic/trim/IlluminaClippingTrimmer.java:493-496):
    if (qual1 < qual2) likelihood[i] = -qual1 / 10;   // int / int -> truncated
    else               likelihood[i] = -qual2 / 10;
whereas simple mode (calculateDifferenceQuality, :556) divides by 10.0f.

Usage: python3 tc1_palindrome_int_division.py <trimmomatic.jar | build dir> [--quick]

Part A  a constructed pair (50 nt reads, 40 nt insert -> 60 aligned bases, six
        mismatches placed outside the two seed 16-mers): with the mismatches at
        Q9 the README score is 54 x 0.602 - 6 x 0.9 = 27.1 (< 30, nothing to
        clip) while the coded score is 32.5 (>= 30): the jar clips read 1 to
        40 nt and drops read 2. At Q10 both rules give 26.5 and nothing is
        clipped, at Q35 both give 11.5.
Part C  4,000 synthetic TruSeq3 pairs with read-through and quality-correlated
        errors: jar vs as-coded port (100 % expected), and how many pairs change
        outcome when the penalty is Q/10 as documented (seeds unchanged), with
        the planted insert length as truth.
Part D  the seed heuristic on the same pairs, for scale (a documented design choice).
Part E  Part C repeated with a NovaSeq-like binned profile (Q2/Q12/Q23/Q37) and
        with a high-quality profile (Q30-41).
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trimmomatic_ref as R

target = sys.argv[1]
quick = "--quick" in sys.argv
rng = random.Random(11)

P1 = "TACACTCTTTCCCTACACGACGCTCTTCCGATCT"   # PrefixPE/1 (TruSeq3-PE-2.fa), 34 nt
P2 = "GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT"   # PrefixPE/2, 34 nt
FA_LINES = [(">PrefixPE/1", P1), (">PrefixPE/2", P2),
            (">PE1", "TACACTCTTTCCCTACACGACGCTCTTCCGATCT"), (">PE1_rc", "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTA"),
            (">PE2", "GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT"), (">PE2_rc", "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC")]
tmp = os.path.join(os.environ.get("TMPDIR", "/tmp"), "trimmo_pal_%d" % os.getpid())
os.makedirs(tmp, exist_ok=True)
fa = os.path.join(tmp, "TruSeq3-PE-2.fa")
with open(fa, "w") as fh:
    for n, s in FA_LINES:
        fh.write("%s\n%s\n" % (n, s))
STEP = "ILLUMINACLIP:%s:2:30:10" % fa


def make_pair(rng, L, n=100):
    """Read-through pair for insert length L: R1 = F + rc(P2) + random, R2 = rc(F) + rc(P1) + random."""
    F = R.rand_seq(rng, L)
    r1 = (F + R.rc(P2) + R.rand_seq(rng, n))[:n]
    r2 = (R.rc(F) + R.rc(P1) + R.rand_seq(rng, n))[:n]
    return r1, r2


def with_errors(rng, seq, quals, scale):
    out = []
    for b, q in zip(seq, quals):
        if rng.random() < scale * min(1.0, 10 ** (-q / 10.0)):
            out.append(rng.choice([c for c in "ACGT" if c != b]))
        else:
            out.append(b)
    return "".join(out)


def outcome(out, name):
    l1 = {n: len(s) for n, s, _ in out["1P"] + out["1U"]}.get(name)
    l2 = {n: len(s) for n, s, _ in out["2P"] + out["2U"]}.get(name)
    return l1, l2


# ---------------------------------------------------------------- Part A
print("Part A: constructed pair, reads 50 nt, insert 40 nt (60 aligned bases), ILLUMINACLIP:TruSeq3-PE-2.fa:2:30:10")
rngA = random.Random(3)
L = 40
r1, r2 = make_pair(rngA, L, n=50)
# six mismatches in read 2, outside the two seed 16-mers of this geometry (read 2 positions 4-35)
mm_pos = [0, 2, 37, 39, 42, 45]
r2m = list(r2)
for p in mm_pos:
    r2m[p] = {"A": "C", "C": "G", "G": "T", "T": "A"}[r2m[p]]
r2m = "".join(r2m)
T = L + 2 * len(P1)
for qmm, label in ((9, "Q9"), (2, "Q2"), (10, "Q10"), (19, "Q19"), (35, "Q35")):
    q1 = [35] * 50
    q2 = [35] * 50
    for p in mm_pos:
        q2[p] = qmm
    s_doc, ov = R.palindrome_score(r1, q1, r2m, q2, P1, P2, T, int_division=False)
    s_cod, _ = R.palindrome_score(r1, q1, r2m, q2, P1, P2, T, int_division=True)
    out, log = R.run_pe(target, [("p", r1, q1)], [("p", r2m, q2)], [STEP])
    l1, l2 = outcome(out, "p")
    port = R.IlluminaClip(fa, 2, 30, 10).process((r1, q1), (r2m, q2))
    print("  mismatches at %-4s README score %5.2f  coded score %5.2f  -> jar: read1 %-8s read2 %-8s (README expects %s; as-coded port %s)"
          % (label + ":", s_doc, s_cod, "%d nt," % l1 if l1 else "dropped,", "%d nt" % l2 if l2 else "dropped",
             "clip to 40 / drop" if s_doc >= 30 else "both untouched, 50 nt",
             "clip/drop" if port[0] == 40 else "untouched"))
print("  (%d aligned bases: 54 matches x 0.60206 = %.2f; six mismatches at Q9 cost 6 x 0.9 = 5.4 by the README and 6 x 0 as coded)" % (ov, 54 * R.LOG10_4))
print("  MCVE input (Q9 case):\n    read1 %s\n    read2 %s\n    mismatch positions in read2 (0-based): %s" % (r1, r2m, mm_pos))

# ---------------------------------------------------------------- Part C / E
NP = 800 if quick else 4000


def profile(rng, n, kind):
    if kind == "novaseq":   # binned Q2/Q12/Q23/Q37, tail-weighted Q2
        out = []
        for i in range(n):
            f = i / max(1, n - 1)
            u = rng.random()
            out.append(2 if u < 0.02 + 0.12 * f * f else 12 if u < 0.06 + 0.15 * f else 23 if u < 0.2 + 0.1 * f else 37)
        return out
    return R.rand_quals(rng, n, kind)


def run_cohort(kind, seed):
    rng = random.Random(seed)
    pairs = []
    for i in range(NP):
        L = rng.randint(0, 130)
        r1, r2 = make_pair(rng, L)
        q1 = profile(rng, 100, kind); q2 = profile(rng, 100, kind)
        scale = rng.choice([0.5, 1.0, 2.0, 4.0])
        r1 = with_errors(rng, r1, q1, scale); r2 = with_errors(rng, r2, q2, scale)
        pairs.append(("q%d_L%d" % (i, L), r1, q1, r2, q2, L))
    clip = R.IlluminaClip(fa, 2, 30, 10)
    out, log = R.run_pe(target, [(n, a, b) for n, a, b, c, d, L in pairs], [(n, c, d) for n, a, b, c, d, L in pairs], [STEP])
    got1 = {n: len(s) for n, s, _ in out["1P"] + out["1U"]}
    got2 = {n: len(s) for n, s, _ in out["2P"] + out["2U"]}
    same = 0; changed = []; noseed_diff = 0
    q_bins = {"Q<10": 0, "Q10-19": 0, "Q20-29": 0, "Q>=30": 0}
    for n, a, b, c, d, L in pairs:
        k1, k2 = clip.process((a, b), (c, d))
        if got1.get(n) == k1 and got2.get(n) == k2:
            same += 1
        f1, f2 = clip.process((a, b), (c, d), int_division=False)
        if (f1, f2) != (k1, k2):
            changed.append((n, L, k1, f1))
        d1, d2 = clip.process((a, b), (c, d), int_division=False, use_seeds=False)
        if (d1, d2) != (f1, f2):
            noseed_diff += 1
        if L < 100:
            T = L + 2 * len(P1)
            qa_ = R.zero_ns(a, b); qb_ = R.zero_ns(c, d)
            p = len(P1); skip1 = max(0, T - (len(c) + p)); skip2 = max(0, T - (len(a) + p))
            for i in range(T - skip1 - skip2):
                o1 = i + skip1; o2 = skip2 + (T - skip1 - skip2) - i - 1
                c1 = P1[o1] if o1 < p else a[o1 - p]
                c2 = R.comp_ch(P2[o2] if o2 < p else c[o2 - p])
                if c1 != "N" and c2 != "N" and c1 != c2:
                    qm = min(100 if o1 < p else qa_[o1 - p], 100 if o2 < p else qb_[o2 - p])
                    q_bins["Q<10" if qm < 10 else "Q10-19" if qm < 20 else "Q20-29" if qm < 30 else "Q>=30"] += 1
    touched = sum(1 for n, a, b, c, d, L in pairs if got1.get(n, 0) != 100 or got2.get(n, 0) != 100)
    print("  jar == as-coded port (integer penalty, seeds): %d/%d pairs; pairs touched by the jar: %d/%d (read-through planted in %d)"
          % (same, NP, touched, NP, sum(1 for p in pairs if p[5] < 100)))
    coded_right = sum(1 for n, L, k1, f1 in changed if k1 == L)
    doc_right = sum(1 for n, L, k1, f1 in changed if f1 == L)
    print("  pairs whose outcome changes when the penalty is Q/10 as documented (seeds unchanged): %d/%d" % (len(changed), NP))
    print("     of these, the coded clip equals the planted insert length in %d, the documented clip in %d" % (coded_right, doc_right))
    for n, L, k1, f1 in changed[:4]:
        T1 = (k1 if k1 is not None else 0) + 2 * len(P1)
        rec = next(p for p in pairs if p[0] == n)
        sc_c, _ = R.palindrome_score(rec[1], rec[2], rec[3], rec[4], P1, P2, T1, True)
        sc_d, _ = R.palindrome_score(rec[1], rec[2], rec[3], rec[4], P1, P2, T1, False)
        print("     e.g. %s: planted insert %d, coded keeps %s (score at that geometry %.1f as coded, %.1f by the README), documented keeps %s"
              % (n, L, k1, sc_c, sc_d, f1))
    print("  seed heuristic for scale: README rule without seeds vs coded seeds (float penalty in both): %d/%d pairs differ" % (noseed_diff, NP))
    print("  mismatches inside the planted read-through overlaps by the lower quality: %s" % q_bins)


print("\nPart C: %d synthetic pairs (insert 0-130 nt, reads 100 nt, quality-correlated errors, 'mixed' profile with a low-quality tail)" % NP)
run_cohort("mixed", 11)
print("\nPart E1: NovaSeq-like binned profile (Q2/Q12/Q23/Q37)")
run_cohort("novaseq", 12)
print("\nPart E2: high-quality profile (Q30-41 throughout)")
run_cohort("high", 13)

# ---------------------------------------------------------------- Part F
print("\nPart F: false positives. 3,000 pairs of independent random 100 nt reads (no insert, no adapter), 'mixed' profile with errors")
rngF = random.Random(21)
pairsF = []
for i in range(3000):
    a = R.rand_seq(rngF, 100); c = R.rand_seq(rngF, 100)
    b = profile(rngF, 100, "mixed"); d = profile(rngF, 100, "mixed")
    pairsF.append(("f%d" % i, a, b, c, d))
clip = R.IlluminaClip(fa, 2, 30, 10)
out, log = R.run_pe(target, [(n, a, b) for n, a, b, c, d in pairsF], [(n, c, d) for n, a, b, c, d in pairsF], [STEP])
got1 = {n: len(s) for n, s, _ in out["1P"] + out["1U"]}; got2 = {n: len(s) for n, s, _ in out["2P"] + out["2U"]}
fp_jar = sum(1 for n, a, b, c, d in pairsF if got1.get(n, 0) != 100 or got2.get(n, 0) != 100)
fp_cod = sum(1 for n, a, b, c, d in pairsF if clip.process((a, b), (c, d)) != (100, 100))
fp_doc = sum(1 for n, a, b, c, d in pairsF if clip.process((a, b), (c, d), int_division=False) != (100, 100))
fp_full = sum(1 for n, a, b, c, d in pairsF if clip.process((a, b), (c, d), int_division=False, use_seeds=False) != (100, 100))
print("  pairs touched: jar %d, as-coded port %d, port with Q/10 penalty %d, README rule without seeds %d  (of 3000)" % (fp_jar, fp_cod, fp_doc, fp_full))
