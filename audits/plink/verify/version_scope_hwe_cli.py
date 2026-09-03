#!/usr/bin/env python3
"""PL1 version scope through the command line only: for the PLINK 1.9 binary given
as argv[1], a variant with genotype counts (hets 2, hom 2, hom 2) (exact HWE p =
185/385 = 0.48052) and one with (hets 2, hom 5, hom 1000) (p = 0.0001495...)
are filtered with thresholds below their p; a correct --hwe keeps both.
Prints the binary's version line, --hardy P, and kept/removed per threshold."""
import os, sys, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import write_pedmap, run, read_table, version
from exact_ref import hwe_p
exe = sys.argv[1]
print(version(exe))
rng = np.random.default_rng(0)
cases = []
g = np.array([[0, 0, 1, 1, 2, 2]]).T.astype(np.int8)
g = np.hstack([g, (rng.random((6, 4)) < 0.5).astype(np.int8) + (rng.random((6, 4)) < 0.5).astype(np.int8)])
cases.append(("hets 2, hom 2, hom 2", g, hwe_p(2, 2, 2), ["0.48", "0.46", "0.45"]))
g2 = np.zeros((1007, 3), np.int8); g2[:2, 0] = 1; g2[2:7, 0] = 2
g2[:, 1:] = (rng.random((1007, 2)) < 0.3).astype(np.int8) + (rng.random((1007, 2)) < 0.3).astype(np.int8)
p2 = hwe_p(2, 5, 1000)
cases.append(("hets 2, hom 5, hom 1000", g2, p2, [f"{float(p2) * (1 - f):.12g}" for f in (3e-5, 1e-4)]))
affected = False
with tempfile.TemporaryDirectory() as tmp:
    for tag, gg, p, thrs in cases:
        pre = write_pedmap(os.path.join(tmp, "d"), gg)
        run(exe, ["--file", pre, "--hardy", "--out", os.path.join(tmp, "h")])
        t = read_table(os.path.join(tmp, "h.hwe"))
        print(f"{tag}: exact p = {float(p):.6g}, --hardy P = {t['P'][0]}")
        for thr in thrs:
            run(exe, ["--file", pre, "--hwe", thr, "--write-snplist", "--out", os.path.join(tmp, "w")])
            kept = "snp1" in [l.strip() for l in open(os.path.join(tmp, "w.snplist"))]
            print(f"  --hwe {thr:<22s}: {'kept' if kept else 'REMOVED'} (expected kept, p > threshold)")
            affected |= not kept
print("verdict:", "AFFECTED" if affected else "unaffected")
