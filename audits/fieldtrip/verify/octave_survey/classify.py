#!/usr/bin/env python3
"""Classify the outcomes of octave_survey.py by cause and print the tables for the write-up.

    classify.py octave_survey.tsv [--out results.tsv]

Categories (first matching rule wins; the rules are regexes on the message column):
  pass                 test passed
  ft-startswith        FieldTrip's compat/octave/startsWith.m or endsWith.m shadowing Octave's own (>= 7) and
                       mishandling cell-array patterns: an error (strncmp: nonconformant cell arrays) or, when the
                       sizes happen to agree, a wrong-sized result that ft_senstype.m:444 then trips over
  ft-nanmean           nanmean/nanstd/nanmax... missing: ft_platform_supports('stats') errors on an undefined
                       variable, ft_defaults swallows it and never adds external/stats
  dpss-hack            dpss called with two outputs on external/signal/dpss_hack (issue #2614)
  mex                  a MEX file that is not compiled for Octave (spm12, gifti, bemcp, ...)
  external             an external binary or toolbox that is not installed (OpenMEEG, dipoli, xunit, MOxUnit, hbf)
  data                 the test loads a file from the Donders file system despite DATA no
  matlab-only          a MATLAB function or syntax that Octave 8.4 does not have (strip, pad, table, envelope,
                       round(x,n), corr(x,y,...), save -nocompression, parula, mle, checkcode, ...)
  graphics             figure/graphics functionality missing under the gnuplot toolkit without a display
  octave-difference    the test ran to an assertion or an error inside FieldTrip's own code: a behavioural or
                       numerical difference between MATLAB and Octave, or a real FieldTrip problem; listed
                       individually
  timeout / crash      the runner's own outcomes
"""
import argparse, collections, re, sys

RULES = [
    ("ft-startswith", r"compat/octave/(startsWith|endsWith)\.m|mx_el_and: nonconformant arguments \(op1 is 1x2, op2 is 1x3\) @ fileio/private/ft_senstype\.m:444"),
    ("ft-nanmean", r"'nan(mean|std|max|min|sum|var|median)' undefined|function for @nan(mean|std|max|min|sum|var)"),
    ("dpss-hack", r"dpss_hack"),
    ("mex", r"not compiled - see Makefile|Could not locate the MEX file|'bem_Cii_lin' undefined|'meg_leadfield1' undefined|'CalcMD5' undefined|'spm_existfile' undefined|direct_method_v5b"),
    ("external", r"OpenMEEG not found|no dipoli executable|XUNIT toolbox is not available|moxunit_throw_test_skipped_exception|hbf_mesh/hbf_SolidAngle"),
    ("data", r"load: unable to find file /project/"),
    ("matlab-only", r"'(strip|pad|table|array2table|envelope|alphamap|checkcode|mle|contains)' undefined|"
                    r"Invalid call to round|corr: function called with too many inputs|Unrecognized option '-nocompression'|"
                    r"'taylorwin' not found|'parula' not found|nargout: number of output arguments unavailable for built-in function objects|"
                    r"binary operator '==' not implemented for 'cell' by 'cell'|buffer: n must be an integer|copyfile: no files to move|"
                    r"audiowrite: failed to open output file"),
    ("graphics", r"Invalid call to colormap|invalid default property 'colormap'|__go_patch__|getframe: not implemented|zoom: function called|"
                 r"rotate3d: function called|__marching_cube__|wrong type argument 'sq_string'"),
]

def classify(outcome, msg):
    if outcome == "PASS": return "pass"
    if outcome == "TIMEOUT": return "timeout"
    if outcome == "CRASH": return "crash"
    for cat, rx in RULES:
        if re.search(rx, msg): return cat
    return "octave-difference"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tsv"); ap.add_argument("--out", default=None)
    a = ap.parse_args()
    rows = [l.rstrip("\n").split("\t") for l in open(a.tsv) if not l.startswith("test\t")]
    rows.sort()
    out = []
    for r in rows:
        r = (r + [""] * 6)[:6]
        out.append(r + [classify(r[1], r[5])])
    if a.out:
        with open(a.out, "w") as f:
            f.write("test\toutcome\tseconds\twalltime\tmem\tcategory\tmessage\n")
            for r in out: f.write("\t".join([r[0], r[1], r[2], r[3], r[4], r[6], r[5]]) + "\n")
    c = collections.Counter(r[6] for r in out)
    n = len(out)
    print(f"{n} tests")
    for cat, k in c.most_common():
        print(f"{cat:18s} {k:4d}  {100*k/n:5.1f} %")
    print()
    for cat in ("octave-difference", "matlab-only", "graphics", "mex", "external", "data", "dpss-hack", "timeout", "crash"):
        sel = [r for r in out if r[6] == cat]
        if not sel: continue
        print(f"## {cat} ({len(sel)})")
        for r in sel: print(f"- {r[0]}: {r[5][:160]}")
        print()

if __name__ == "__main__":
    main()
