**Filed 2026-09-04 as PR #207** (issue #203; comment posted on the issue).

# iqtree/iqtree3 #203 — `setRootNode()` assertion when the `-o` outgroup is absent from a partition tree (also #89)

_Prepared 2026-09-03 against `iqtree/iqtree3` `master` @ `8977d31a` (version string 3.1.3,
2026-08-03). Nothing has been filed or pushed; this directory is the kit._

## The issue

- **#203** "IQ-TREE 3.1.3 crashes in PhyloTree::setRootNode() with a valid single-taxon
  outgroup" — https://github.com/iqtree/iqtree3/issues/203 (opened 2026-08-16, 0 comments).
  Reporter's claim: `-s concat.fasta -p partitions.txt -m MFP -bb 1000 -bnni -o <taxon>`
  on 14 DNA sequences in two partitions (ITS: 14 sequences; LSU: 6 sequences, the other 8
  gap-only) aborts right after "Time for fast ML tree search" with
  `phylotree.cpp:486: PhyloTree::setRootNode(): Assertion 'root' failed`, although the
  outgroup is in the alignment and in the inferred tree; without `-o` it runs.
- **#89** "Assertion `root' failed error" — https://github.com/iqtree/iqtree3/issues/89
  (2025-09-17, 5 comments, unreadable from this session): `-lmap 2000 -o A,B,C,...`
  aborts with the same assertion from `readTreeStringSeqName()` inside
  `computeQuartetLikelihoods()`. Same cause, fixed by the same change.
- **#135** and **#102** (2026-02-21, 2025-10-17) report the same assertion at line 489 on
  large concatenated data; their bodies do not show the command line, so they are
  "very likely the same", not verified.

No open or closed PR mentions `setRootNode`, the outgroup or these issue numbers
(`mcp__github__search_pull_requests`, two queries, 0 results).

## Diagnosis (`master` @ `8977d31a`)

`PhyloTree::setRootNode()` (`tree/phylotree.cpp:471-505`) looks the `-o` taxon up with
`findNodeName()` and `ASSERT(root)`s (line 486 for a single taxon, 494 for a list). It is
called with `params->root` from `getTreeString()` (`tree/phylotree.cpp:603-608`),
`readTreeString()`/`readTreeStringSeqName()` and many places in `tree/iqtree.cpp`, on
**every** `PhyloTree`, not only on the top-level tree:

- with a partition model, each partition of the `PhyloSuperTree` is a `PhyloTree` whose
  alignment holds only the taxa that have data in that partition
  (`SuperAlignment::taxa_index`); a taxon with no data in a partition is not a leaf of
  that partition tree. `IQTree::saveCheckpoint()` → `PhyloTree::getTreeString()` is
  called on the partition trees during ModelFinder's fast ML tree search
  (`main/phylotesting.cpp:740-` `computeFastMLTree`, stack trace in
  `repro.before.out`), and `PartitionModel::computeMarginalLhForPartitions()`
  (`model/partitionmodel.cpp`) does the same when the `.iqtree` report is written, so a
  fixed model (`-m GTR+G`) crashes too, just later;
- with `-lmap`, `PhyloTree::computeQuartetLikelihoods()` (`tree/quartet.cpp:898-949`)
  builds a 4-taxon alignment and tree per quartet and reads it with
  `readTreeStringSeqName()`, which calls `setRootNode(params->root)`; the outgroup is in
  almost no quartet.

The outgroup is validated against the alignment before any of this
(`tree/iqtree.cpp:751-758` "Specified outgroup taxon ... not found";
`main/phyloanalysis.cpp:3397-3401`), so the assertion never catches a user error — it
only fires on trees that legitimately lack the taxon. The root of an unrooted
`PhyloTree` fixes the traversal order only; the likelihood does not depend on it.

**Trigger**, established by execution (`repro.sh`): `-o T` where `T` has no data in at
least one partition (`-p`, `-q` and `-Q` alike, `-m MFP` and `-m GTR+G` alike), or
`-o` combined with `-lmap`. `-o` with a taxon that has data in every partition, and
runs without `-o`, are fine.

## The fix (`0001-Fix-setRootNode-assertion-when-the-outgroup-is-absen.patch`, branch `fix/issue-203-outgroup-absent-from-partition`)

`setRootNode()` now handles the single-taxon and list cases in one loop: outgroup taxa
that are not leaves of the tree at hand are skipped; if none is left the tree is rooted
at its first taxon, exactly as when no `-o` is given; the "branch separating outgroup"
search for a multi-taxon outgroup uses only the taxa present in the tree and is skipped
when fewer than two are present (which would otherwise print a spurious "Branch
separating outgroup is not found" for every partition tree). 22 lines added, 13 removed
in `tree/phylotree.cpp`; the `ASSERT(root)` stays for the fallback.

Unchanged behaviour, checked byte-for-byte (`.treefile`, `.iqtree` minus the time lines):
`-p` runs without `-o` and with an outgroup that has data everywhere (`203d`, `203e`
in `repro.sh`), and a multi-taxon `-o A,B` run where the pair is not a clade (the three
pre-existing "Branch separating outgroup is not found" warnings appear on `main` and on
the branch alike).

## Reproduction

`repro.sh` writes a 14-taxon, 500-column DNA alignment in two partitions (300 + 200) in
which `sp06`–`sp12` and `outgroup_taxon` are gap-only in the second partition (the
shape of the reporter's data), plus the same alignment without the gaps for the `-lmap`
cases, and runs seven commands. `IQTREE3=<binary> sh repro.sh <workdir>`.

`repro.before.out` (`master` @ `8977d31a`, built here):

```
203a  -p parts.nex -m MFP -o outgroup_taxon    exit=134  ERROR: phylotree.cpp:486: ... Assertion `root' failed.
203b  -p parts.nex -m GTR+G -o outgroup_taxon  exit=134  ERROR: phylotree.cpp:486: ... Assertion `root' failed.
203c  -q parts.nex -m GTR+G -o outgroup_taxon  exit=134  ERROR: phylotree.cpp:486: ... Assertion `root' failed.
203d  -p parts.nex -m GTR+G -o sp00 (has data) exit=0    Log-likelihood of the tree: -3375.3349 (s.e. 92.2056)
203e  -p parts.nex -m GTR+G, no -o             exit=0    Log-likelihood of the tree: -3375.3349 (s.e. 92.2056)
89a   -lmap 50 -m JC -o outgroup_taxon         exit=134  ERROR: phylotree.cpp:486: ... Assertion `root' failed.
89b   -lmap 50 -m JC -o outgroup_taxon,sp12    exit=134  ERROR: phylotree.cpp:494: ... Assertion `root' failed.
```

`repro.after.out` (branch):

```
203a  -p parts.nex -m MFP -o outgroup_taxon    exit=0    Log-likelihood of the tree: -3381.8910 (s.e. 92.0602)
203b  -p parts.nex -m GTR+G -o outgroup_taxon  exit=0    Log-likelihood of the tree: -3375.3347 (s.e. 92.2057)
203c  -q parts.nex -m GTR+G -o outgroup_taxon  exit=0    Log-likelihood of the tree: -3375.5297 (s.e. 92.1975)
203d  -p parts.nex -m GTR+G -o sp00 (has data) exit=0    Log-likelihood of the tree: -3375.3349 (s.e. 92.2056)
203e  -p parts.nex -m GTR+G, no -o             exit=0    Log-likelihood of the tree: -3375.3349 (s.e. 92.2056)
89a   -lmap 50 -m JC -o outgroup_taxon         exit=0    Log-likelihood of the tree: -4489.86 (s.e. 78.35)
89b   -lmap 50 -m JC -o outgroup_taxon,sp12    exit=0    Log-likelihood of the tree: -4489.86 (s.e. 78.35)
```

(203b differs from 203d/203e in the fourth decimal because the tree search is seeded
per traversal order — the same kind of difference `-o` produces on `main` for any
outgroup; the `.iqtree` report says "Tree is UNROOTED although outgroup taxon
'outgroup_taxon' is drawn at root" as for a normal `-o` run.)

The crash also reproduces on the project's own test data: in `test_scripts/test_data/turtle.fa`
+ `turtle.nex`, `phrynops` has no data in the fourth partition (and
`emys_orbicularis`, `chelonoidis_nigra` in the third and fourth), so
`-p turtle.nex -o phrynops` and `-lmap 100 -o phrynops` abort on `main`.

## Test

The project's regression test is `test_scripts/test_iqtree.sh` (and the PowerShell twin
`test_iqtree.ps1`, both run by `.github/workflows`), a list of commands on the turtle
data, checked by `test_scripts/verify_results.sh` against the log-likelihoods in
`test_scripts/test_data/expect_ans.txt` (threshold 1). The patch adds two commands to
both scripts and two rows to `expect_ans.txt`:

```
turtle.nex.outgroup.iqtree   Log-likelihood of the tree   -5352.2653   1   (-p turtle.nex -o phrynops -m GTR+G)
turtle.lmap.outgroup.iqtree  Log-likelihood of the tree   -5377.9500   1   (-lmap 100 -o phrynops -m GTR+G)
```

Both commands abort on `main` (no `.iqtree` file; `verify_results.sh` reports
"File not found") and pass on the branch; the values are deterministic across repeated
runs (`-T 1 -seed 73073`).

| | `main` @ `8977d31a` | branch |
|---|---|---|
| `test_iqtree.sh` + `verify_results.sh`, existing 21 checks | 21 PASS | 21 PASS |
| the two new checks | 0 of 2 (both commands abort) | 2 of 2 PASS (23 of 23 overall, every command exit 0) |

Note on the harness: `test_iqtree.sh` wraps each command in `/usr/bin/time`, which this
container lacks; it was run through a copy with that wrapper removed (`test_iqtree_notime.sh`,
one `sed` on line 36) and `verify_results.sh` pointed at the output directory. Nothing
else changed.

Linter: the repository has no `.clang-format`, clang-tidy is off by default
(`USE_CLANG_TIDY=OFF`), and there is no formatter in CI; `git diff --check` is clean and
the new code follows the surrounding style (4-space indent, braces on every `if`).

## Build

Fresh `git clone --depth 1` + submodules (`lsd2`, `cmaple`), `cmake -DCMAKE_C_COMPILER=gcc
-DCMAKE_CXX_COMPILER=g++ -DEIGEN3_INCLUDE_DIR=<eigen 3.4.0 clone>
-DFETCHCONTENT_SOURCE_DIR_GOOGLETEST=<googletest clone>`, `make iqtree3` (gcc 13.3,
cmake 3.28, OpenMP, system Boost 1.83 headers; the project's build used Boost 1.86 headers,
which only matter for the symmetry test's binomial). "IQ-TREE version 3.1.3 for Linux x86
64-bit". The disk filled once during the build (shared scratch); the `cmaple` binary
target was skipped (`make iqtree3`), which does not affect `iqtree3`.

## Other candidates considered (61 open issues read by title, 15 by body)

| issue | why / why not |
|---|---|
| **#203 / #89 / #135 / #102** (chosen) | four open reports of one assertion; reproduced in the first attempt from the reporter's description; fix is local, 35 lines with tests |
| #196 "Jackknife proportion is inverted" (2026-08-01, 1 comment) | probably a real wrong-number: `tools.cpp` samples `floor((1-jack_prop)*n)` sites while the help says "subsampling proportion"; but the fix is a naming decision (swap the code, or reword the help) for the maintainers, and at the default 0.5 nothing changes |
| #192 "+FU silently ignored for codon (GY) models in 3.1.2, correct in 2.4.0" (2026-07-23) | good wrong-number regression with a table of reproductions, but needs the codon model parser and a 61-frequency file; the reporter's data are in an attachment this session cannot fetch, and the fix may span the model string parser — left as second choice |
| #204 alisim `free(): invalid next size` on partitioned simulation (2026-08-20, 0 comments) | crash on valid input, no comments; needs the reporter's partition file (attachment) to know which combination overflows; AliSim was not checked |
| #143 / #100 / #110 / #107 ModelFinder `initFromNestedModel` assertion with `+ASC` (12 comments on #143) | most-discussed open bug; the 12 unreadable comments make it likely the maintainers are already on it, and the reporter says it depends on which sites are cut ("really random") |
| #85 `-te` does not constrain the tree under `--scfl` | a documented option doing nothing, but needs the reporter's 400-locus data and `--scfl` was not checked |
| #13 alrt + ufboot error, #65 `-madd` in MFP, #55 `-fs` with `+ASC+G4` | bodies mention data this session cannot get, or are unclear without the comments |

## Caveats

- The comments on #89, #135, #102 could not be read; #135/#102 are attributed to this
  cause from the identical assertion, line and the partitioned/`-o` setting only.
- The maintainers might prefer not to call `setRootNode(params->root)` on partition and
  quartet trees at all (e.g. pass `nullptr` from `computeQuartetLikelihoods()` and from
  the per-partition `saveCheckpoint()`/`computeMarginalLhForPartitions()` paths). That
  touches four call sites in three files instead of one function and would still leave
  the assertion for any other path; the fallback inside `setRootNode()` is the smaller
  change. A `VB_MED`-level note when the fallback is taken could be added if wanted.
- The two new `expect_ans.txt` values come from this Linux/gcc build; CI also runs the
  script under clang on macOS/ARM and on Windows with a threshold of 1 log-likelihood
  unit, the same margin as the existing rows.

## Files

| file | what |
|---|---|
| `0001-Fix-setRootNode-assertion-when-the-outgroup-is-absen.patch` | `git format-patch` of the one commit on `fix/issue-203-outgroup-absent-from-partition` |
| `repro.sh`, `repro.before.out`, `repro.after.out` | reproduction and its output on `main` and on the branch |
| `pr-body.md`, `comment.md` | PR text (title on the first line) and the issue comment |
