#!/bin/bash
# Reproduction for chrchang/plink-ng issue #140 ("Logging bug in bmerge").
#
# Two filesets over the same 3 samples:
#   plus:   4 records, 4 distinct variant IDs
#   normed: 4 records, 3 distinct variant IDs (v2 appears twice)
# Every variant of normed is also in plus.
#
# PLINK 1.9 --bmerge keys the merge on variant ID, so the two 'v2' records of
# normed are one variant in the merged fileset.  The log lines should therefore
# describe normed the same way whichever fileset is the base.
#
# Usage: PLINK=<path to plink 1.9 binary> ./repro.sh
set -u
PLINK=${PLINK:-plink}
tmpdir=$(mktemp -d)
cd "$tmpdir" || exit 1

cat > plus.map <<'MAP'
1	v1	0	100
1	v2	0	200
1	v3	0	300
1	v4	0	400
MAP
cat > plus.ped <<'PED'
F1 S1 0 0 1 1 A G A A C C G G
F1 S2 0 0 1 1 A A A G C T G T
F1 S3 0 0 1 1 G G G G T T T T
PED

# same variants, but v2 is present twice (same position, same alleles)
cat > normed.map <<'MAP'
1	v1	0	100
1	v2	0	200
1	v2	0	200
1	v3	0	300
MAP
cat > normed.ped <<'PED'
F1 S1 0 0 1 1 A G A A A A C T
F1 S2 0 0 1 1 A A A G A G C T
F1 S3 0 0 1 1 G G G G G G T T
PED

"$PLINK" --file plus --make-bed --out plus > /dev/null 2>&1
"$PLINK" --file normed --make-bed --out normed > /dev/null 2>&1
echo "plus.bim:   $(wc -l < plus.bim) records, $(cut -f2 plus.bim | sort -u | wc -l) distinct IDs"
echo "normed.bim: $(wc -l < normed.bim) records, $(cut -f2 normed.bim | sort -u | wc -l) distinct IDs"

for pair in "plus normed" "normed plus"; do
  set -- $pair
  base=$1; other=$2
  echo
  echo "=== --bfile $base --bmerge $other (--merge-mode 6) ==="
  "$PLINK" --bfile "$base" --bmerge "$other".bed "$other".bim "$other".fam \
      --merge-mode 6 --out "diff_$base" > /dev/null 2>&1
  grep -E 'duplicate variant ID|marker(s)? loaded from|to be merged from|Of these|overlapping calls|concordant' "diff_$base.log"
  echo "--- plain merge ---"
  "$PLINK" --bfile "$base" --bmerge "$other".bed "$other".bim "$other".fam \
      --make-bed --out "merged_$base" > /dev/null 2>&1
  echo "merged fileset: $(wc -l < "merged_$base.bim") variants: $(cut -f2 "merged_$base.bim" | tr '\n' ' ')"
done
echo
echo "(workdir $tmpdir)"
