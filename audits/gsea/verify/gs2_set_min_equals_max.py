#!/usr/bin/env python3
"""GS2: when `-set_min` equals `-set_max`, GSEA skips the gene-set size filter entirely.

`GeneSetCohort.Generator.filterGeneSetsByMembersAndSize` runs the min/max filters only
`if (geneSetMinSize != geneSetMaxSize)`; the `else` branch is marked `// @note hack` and
logs "Skipped gene set size filtering: max and min thresholds are equal".  The parameters
are documented as "Gene sets smaller/larger than this number are EXCLUDED from the
analysis".  Two consequences, both checked here on a synthetic list:

  A. `-set_min 20 -set_max 20` analyses sets of size 5, 20, 20 and 900 alike (expected:
     only the two size-20 sets), so every reported set, and the FDR that depends on the
     number of sets, is computed on a collection the user asked to exclude.
  B. the skipped branch is also where sets are restricted to the genes present in the
     ranked list (`cloneDeep(rl)`); with the filter skipped, a set containing an
     identifier absent from the list makes the run fail (`No such name`) instead of
     being restricted, or is scored with the wrong N_H when it is not.
Usage: gs2_set_min_equals_max.py [build]
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C
import gsea_port as P

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
C.banner("GS2: set_min == set_max disables the size filter", BUILD)
W = os.path.join(C.SCRATCH, "gs2", BUILD)
os.makedirs(W, exist_ok=True)

rng = np.random.default_rng(11)
N = 2000
names = ["g%04d" % i for i in range(N)]
scores = C.strictly_decreasing(rng.normal(0, 1, N))
C.write_rnk(os.path.join(W, "list.rnk"), names, scores)

sets_present = {
    "SIZE_5": names[:5],
    "SIZE_20_TOP": names[:20],
    "SIZE_20_RANDOM": list(rng.choice(names, 20, replace=False)),
    "SIZE_900": list(rng.choice(names, 900, replace=False)),
}
C.write_gmt(os.path.join(W, "present.gmt"), sets_present)


def show(r, title):
    print("\n== %s" % title)
    if not r.ok():
        print("   RUN FAILED:", r.error())
        return
    print("   sets analysed: %s" % sorted(r.rows))
    for nm in sorted(r.rows):
        print("   %-16s size=%4d ES=%8.4f NES=%7.3f p=%.3f FDR=%.3f" %
              (nm, r.rows[nm]["size"], r.rows[nm]["es"], r.rows[nm]["nes"], r.rows[nm]["np"], r.rows[nm]["fdr"]))


# A. all members present: min != max (control) vs min == max
show(C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "present.gmt"),
                     os.path.join(W, "out_ctrl"), label="ctrl", set_min=20, set_max=21, nperm=200),
     "A control: -set_min 20 -set_max 21  (expected: SIZE_20_top and SIZE_20_random only)")
show(C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "present.gmt"),
                     os.path.join(W, "out_eq"), label="eq", set_min=20, set_max=20, nperm=200),
     "A: -set_min 20 -set_max 20  (expected: the same two sets)")
show(C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "present.gmt"),
                     os.path.join(W, "out_eq15"), label="eq15", set_min=15, set_max=15, nperm=200),
     "A: -set_min 15 -set_max 15  (expected: no set of size exactly 15 -> error 'none of the gene sets passed')")

# B. a set with identifiers absent from the ranked list (the normal case with MSigDB collections)
sets_absent = dict(sets_present)
sets_absent["SIZE_20_WITH_ABSENT"] = names[100:120] + ["NOT_IN_LIST_%d" % i for i in range(5)]
C.write_gmt(os.path.join(W, "absent.gmt"), sets_absent)
show(C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "absent.gmt"),
                     os.path.join(W, "out_abs_ctrl"), label="absctrl", set_min=20, set_max=21, nperm=200),
     "B control: -set_min 20 -set_max 21 with a set carrying 5 absent ids (expected: restricted to 20, analysed)")
show(C.run_preranked(BUILD, os.path.join(W, "list.rnk"), os.path.join(W, "absent.gmt"),
                     os.path.join(W, "out_abs_eq"), label="abseq", set_min=20, set_max=20, nperm=200),
     "B: -set_min 20 -set_max 20 with the same file")

# expected ES for the record
print("\nport ES (weighted) for reference: " + ", ".join(
    "%s=%.4f" % (nm, P.enrichment_score(scores, P.hit_mask(names, g), 1.0)[0]) for nm, g in sets_present.items()))
print("\nDONE")
