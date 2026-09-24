#!/bin/sh
# Minimal reproductions for two `samtools stats` SN counts.
# (a) "reads duplicated" / "bases duplicated" count supplementary records that carry
#     the DUP flag, while "sequences" / "total length" exclude supplementary records.
#     Two pairs, both duplicates, read 2 of pair 0 also has a supplementary record
#     flagged DUP (what `markdup -S` or Picard MarkDuplicates produce):
#       truth  sequences 4, reads duplicated 4 (100 % of the 4 sequences)
#       got    reads duplicated 5 (125 % of the 4 sequences)
# (b) "insert size standard deviation" leaves the isize 0 bin out of the sum of squares
#     while the mean and the denominator include it. Three pairs, TLEN 300, 300 and 0:
#       mean 200 either way; population SD sqrt((100^2+100^2+200^2)/3) = 141.4
#       got    81.6 = sqrt((100^2+100^2)/3)
# Usage: sh mcve_st3_stats_dup_supp_isize_sd.sh [samtools]
SAMTOOLS=${1:-samtools}
T=$(mktemp -d)
A=$(printf 'A%.0s' $(seq 100)); Q=$(printf 'I%.0s' $(seq 100))
H='@HD\tVN:1.4\tSO:coordinate\n@SQ\tSN:ref\tLN:100000\n'
printf "$H" > $T/dup.sam
for i in 0 1; do
  p=$((1000 + i * 1000))
  printf 'p%d\t1123\tref\t%d\t60\t100M\t=\t%d\t300\t%s\t%s\n' $i $p $((p + 200)) "$A" "$Q" >> $T/dup.sam
  printf 'p%d\t1171\tref\t%d\t60\t100M\t=\t%d\t-300\t%s\t%s\n' $i $((p + 200)) $p "$A" "$Q" >> $T/dup.sam
done
printf 'p0\t3219\tref\t9000\t60\t30M70H\t=\t1000\t0\t%s\t%s\n' "$(printf 'A%.0s' $(seq 30))" "$(printf 'I%.0s' $(seq 30))" >> $T/dup.sam
printf "$H" > $T/isize.sam
printf 'q0\t99\tref\t1000\t60\t100M\t=\t1200\t300\t%s\t%s\n'  "$A" "$Q" >> $T/isize.sam
printf 'q1\t97\tref\t1500\t60\t100M\t=\t1700\t0\t%s\t%s\n'    "$A" "$Q" >> $T/isize.sam
printf 'q0\t147\tref\t1200\t60\t100M\t=\t1000\t-300\t%s\t%s\n' "$A" "$Q" >> $T/isize.sam
printf 'q1\t145\tref\t1700\t60\t100M\t=\t1500\t0\t%s\t%s\n'   "$A" "$Q" >> $T/isize.sam
printf 'q2\t99\tref\t2000\t60\t100M\t=\t2200\t300\t%s\t%s\n'  "$A" "$Q" >> $T/isize.sam
printf 'q2\t147\tref\t2200\t60\t100M\t=\t2000\t-300\t%s\t%s\n' "$A" "$Q" >> $T/isize.sam
$SAMTOOLS --version | head -1
echo "(a) expected: sequences 4, reads duplicated 4, supplementary alignments 1, total length 400, bases duplicated 400"
$SAMTOOLS stats $T/dup.sam | grep -E '^SN.(sequences|reads duplicated|supplementary alignments|total length|bases duplicated):'
echo "(b) expected: insert size average 200.0, standard deviation 141.4"
$SAMTOOLS stats $T/isize.sam | grep -E '^SN.insert size (average|standard deviation):'
rm -r $T
