#!/bin/sh
# Run every harness on every build; outputs <harness>.<label>.out next to the scripts.
# Usage: BUILDS=/path/to/builds sh run_all.sh   (expects $BUILDS/b-<label>/bwa)
set -e
BUILDS=${BUILDS:?set BUILDS to the directory holding b-master, b-v0.7.17, ...}
cd "$(dirname "$0")"
for label in master v0.7.17 v0.7.15 0.7.12 patched; do
  exe=$BUILDS/b-$label/bwa
  [ -x "$exe" ] || continue
  work=$BUILDS/work-$label; mkdir -p "$work"
  for h in s1_scoring_tags m1_mapq p1_pairing c1_split_reads; do
    [ -f $h.py ] || continue
    BWA=$exe BWA_LABEL=$label BWA_WORK=$work python3 $h.py > $h.$label.out 2>&1 || true
  done
done
# calibration: released vs patched on the same reads
if [ -x "$BUILDS/b-patched/bwa" ]; then
  BWA=$BUILDS/b-master/bwa BWA_ALT=$BUILDS/b-patched/bwa BWA_WORK=$BUILDS/work-master \
    python3 m2_mapq_calibration.py > m2_mapq_calibration.master_vs_patched.out 2>&1
fi
