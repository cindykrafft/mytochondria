Title: `-set_min N -set_max N` turns the gene set size filter off instead of selecting the sets of size N

<!-- GSEA-MSigDB/gsea-desktop has no issue template; CONTRIBUTING.md asks for a title, a
     clear description and an executable test case. -->

**Description**

`GeneSetCohort.Generator.filterGeneSetsByMembersAndSize` applies the size filter only when
the two thresholds differ:

```java
// src/main/java/edu/mit/broad/genome/alg/gsea/GeneSetCohort.java:188-197
if (geneSetMinSize != geneSetMaxSize) {
    gsets = GeneSetGenerators.removeGeneSetsSmallerThan(gsets, geneSetMinSize, rl);
    gsets = GeneSetGenerators.removeGeneSetsLargerThan(gsets, geneSetMaxSize, rl);
} else { // @note hack
    log.info("Skipped gene set size filtering: max and min thresholds are equal");
}
```

Equal bounds are the most specific request a user can make of the filter — "analyse the
sets of exactly this size" — and they are the one case that is skipped. Every set in the
GMT is then scored and reported with an ES, an NES, a nominal p-value, an FDR q-value and
an FWER p-value. Because the FDR and FWER are computed over the family of sets that
survived the filter, they are computed over a different, larger family than the one the
user asked for. The only trace is an INFO log line; the report and the `.rpt` file still
record the thresholds that were requested.

The skipped branch is also where each set is intersected with the ranked list —
`removeGeneSetsSmallerThan(gsets, min, rl)` calls `GeneSet.cloneDeep(rl)`
(`src/main/java/edu/mit/broad/genome/alg/GeneSetGenerators.java:61-80`). With equal bounds
that never happens, so a set holding a gene that is not in the ranked list reaches the
scoring table, which asks the list for that gene's score, and the run aborts.

**Expected vs got**

The script below writes a 200-gene ranked list and a GMT with three sets of sizes 5, 20
and 60, then runs `GseaPreranked` twice.

**Expected:** `-set_min 20 -set_max 20` reports `SET_20` only.
**Got** (GSEA built from master `dc35c764`, OpenJDK 25.0.4):

```
-set_min 5 -set_max 60  ->  reported (name size): SET_20 20 SET_5 5 SET_60 60
-set_min 20 -set_max 20  ->  reported (name size): SET_20 20 SET_5 5 SET_60 60
```

The first line shows the filter working normally. The second asks for size 20 and gets all
three sets, sizes 5, 20 and 60.

Adding one more set whose members are all present except one produces the second symptom:
with `-set_min 20 -set_max 500` that set is trimmed and the run finishes, and with
`-set_min 20 -set_max 20` the run aborts and writes no report at all:

```
java.lang.IllegalArgumentException: No such name: NOT_IN_LIST
```

**Versions checked (executed, one script, six builds)**

| build | `-set_min 5 -set_max 60` | `-set_min 20 -set_max 20` |
|---|---|---|
| master `dc35c764` | SET_5, SET_20, SET_60 | SET_5, SET_20, SET_60 |
| v4.4.0 (latest release) | SET_5, SET_20, SET_60 | SET_5, SET_20, SET_60 |
| v4.3.2 | SET_5, SET_20, SET_60 | SET_5, SET_20, SET_60 |
| v4.1.0 | SET_5, SET_20, SET_60 | SET_5, SET_20, SET_60 |
| v4.0.3 | SET_5, SET_20, SET_60 | SET_5, SET_20, SET_60 |
| master + the patch below | SET_5, SET_20, SET_60 | **SET_20** |

**Minimal complete verifiable example**

Nothing is downloaded; both input files are written by the script. `GSEA_CP` is a
classpath, e.g. `build/libs/gsea-minimal-user.jar:modules/*`. Releases before 4.2 write the
report as `.xls`, hence the two globs.

```bash
#!/bin/bash
set -e
CP=${GSEA_CP:?set GSEA_CP to gsea.jar:modules/*}
W=$(mktemp -d); cd "$W"
for i in $(seq 0 199); do printf 'g%d\t%s\n' "$i" "$(echo "200 - $i" | bc)"; done > list.rnk
{ printf 'SET_5\tna';  for i in $(seq 0 4);  do printf '\tg%d' "$i"; done; printf '\n'
  printf 'SET_20\tna'; for i in $(seq 0 19); do printf '\tg%d' "$i"; done; printf '\n'
  printf 'SET_60\tna'; for i in $(seq 0 59); do printf '\tg%d' "$i"; done; printf '\n'; } > sets.gmt
for bounds in "5 60" "20 20"; do
  set -- $bounds
  java -cp "$CP" xtools.gsea.GseaPreranked -rnk list.rnk -gmx sets.gmt -out "$W/o$1_$2" \
    -set_min "$1" -set_max "$2" -nperm 100 -rnd_seed 149 -collapse No_Collapse \
    -gui false -zip_report false -plot_top_x 0 -make_sets false -rpt_label run > /dev/null 2>&1
  got=$(cat "$W/o$1_$2"/run.*/gsea_report_for_*.tsv "$W/o$1_$2"/run.*/gsea_report_for_*.xls 2>/dev/null | cut -f1,4 | grep -v '^NAME' | sort | tr '\n' ' ')
  echo "-set_min $1 -set_max $2  ->  reported (name size): $got"
done
rm -rf "$W"
```

Shrinking the example showed that only the equality of the two bounds matters: three sets
and 200 genes are enough, the scoring scheme and the permutation count are irrelevant, and
`-set_min 20 -set_max 21` behaves correctly, which is what isolates the `!=` guard rather
than the filter helpers themselves.

**Proposed fix**

Run the two filters unconditionally. When the bounds are equal they keep exactly the sets
whose in-list size equals that value, which is what the parameter help describes ("Gene
sets smaller than this number are EXLCUDED from the analysis"). A branch with that change
and a JUnit test covering unequal bounds, equal bounds and a set with a member missing from
the ranked list is ready; PR follows. On unmodified master the new test fails with
`array lengths differ, expected: <1> but was: <4>`; with the patch the whole test class
passes and `XMathTest`/`VectorTest` are unchanged (54 passed both ways).

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/gsea)

---
_Generated by [Claude Code](https://claude.ai/code)_
