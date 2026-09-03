#!/bin/sh
# Reproduction for iqtree/iqtree3 issue #203 (and #89, same cause).
# Usage: IQTREE3=/path/to/iqtree3 sh repro.sh [workdir]
# Writes a 14-taxon, 2-partition DNA alignment in which 8 taxa (the outgroup
# among them) have no data in the second partition, then runs the three
# commands that abort on master with
#   phylotree.cpp:486: PhyloTree::setRootNode(): Assertion `root' failed.
set -u
IQTREE3=${IQTREE3:?set IQTREE3 to the binary}
W=${1:-repro203_work}; mkdir -p "$W"; cd "$W"
python3 - <<'PY'
import random
random.seed(7)
names = ["sp%02d" % i for i in range(13)] + ["outgroup_taxon"]
L1, L2 = 300, 200
base1 = [random.choice("ACGT") for _ in range(L1)]
base2 = [random.choice("ACGT") for _ in range(L2)]
def mut(s, r): return "".join(random.choice("ACGT") if random.random() < r else c for c in s)
with open("aln.fa", "w") as f, open("aln_full.fa", "w") as g:
    for i, nm in enumerate(names):
        r = 0.05 + 0.02 * i
        s1, s2 = mut(base1, r), mut(base2, r)
        g.write(">%s\n%s%s\n" % (nm, s1, s2))
        if i >= 6: s2 = "-" * L2          # sp06..sp12 and the outgroup: no data in p2
        f.write(">%s\n%s%s\n" % (nm, s1, s2))
with open("parts.nex", "w") as f:
    f.write("#nexus\nbegin sets;\n  charset p1 = 1-%d;\n  charset p2 = %d-%d;\nend;\n" % (L1, L1 + 1, L1 + L2))
PY
run() { # label, args...
  label=$1; shift
  "$IQTREE3" "$@" -T 1 -seed 1 -redo -quiet > "$label.stdout" 2>&1; rc=$?
  printf '%-52s exit=%s  %s\n' "$label" "$rc" "$(grep -m1 'Assertion\|BEST SCORE\|Total tree length' "$label.stdout" "$label.log" 2>/dev/null | head -1 | sed 's/^[^:]*://')"
  if [ $rc -eq 0 ]; then printf '    %s\n' "$(grep -m1 'Log-likelihood of the tree\|BEST SCORE FOUND' "$label.iqtree" "$label.log" | head -1 | sed 's/^[^:]*://')"; fi
}
echo "binary: $("$IQTREE3" --version 2>&1 | head -1)"
run "203a: -p parts -m MFP -o outgroup_taxon"     -s aln.fa -p parts.nex -m MFP   -o outgroup_taxon -pre 203a
run "203b: -p parts -m GTR+G -o outgroup_taxon"   -s aln.fa -p parts.nex -m GTR+G -o outgroup_taxon -pre 203b
run "203c: -p parts -m GTR+G -o sp00 (has data)"  -s aln.fa -p parts.nex -m GTR+G -o sp00 -pre 203c
run "89a:  -lmap 50 -m JC -o outgroup_taxon"      -s aln_full.fa -m JC -lmap 50 -o outgroup_taxon -pre 89a
run "89b:  -lmap 50 -m JC -o outgroup_taxon,sp12" -s aln_full.fa -m JC -lmap 50 -o outgroup_taxon,sp12 -pre 89b
