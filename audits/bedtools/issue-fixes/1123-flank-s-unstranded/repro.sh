#!/usr/bin/env bash
# Reproduction for arq5x/bedtools2 issue #1123: `bedtools flank -s` produces no
# output for records that have no "+"/"-" strand in column 6 (BED3/4/5 input,
# or "." strand). Synthetic data only. Usage: BT=/path/to/bedtools bash repro.sh
set -u
BT=${BT:-bedtools}
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT; cd "$T"
printf 'chr1\t1000\n' > my.genome
printf 'chr1\t100\t200\n' > bed3.bed
printf 'chr1\t100\t200\tf1\t0\t.\nchr1\t500\t600\tf2\t0\t-\n' > dot.bed
printf 'chr1\t100\t200\t+\nchr1\t500\t600\t-\n' > bed4_strand_in_col4.bed
echo "bedtools $($BT --version | cut -d' ' -f2)"
for f in bed3.bed dot.bed bed4_strand_in_col4.bed; do
  for opt in "" "-s"; do
    echo "== flank -i $f -l 5 -r 0 $opt"
    $BT flank -i $f -g my.genome -l 5 -r 0 $opt | sed 's/^/   /'
  done
done
echo "== slop -i bed3.bed -l 5 -r 0 -s   (slop treats a strand-less record as forward)"
$BT slop -i bed3.bed -g my.genome -l 5 -r 0 -s | sed 's/^/   /'
