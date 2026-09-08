#!/bin/sh
# Minimal reproduction for the `samtools stats` coverage-distribution wrap-around.
# Two 50-bp blocks on the same 50 positions plus one block 1,500 bp downstream:
#   truth  COV: 50 positions at depth 2, 50 positions at depth 1
#   got    COV: 50 positions at depth 3
# Usage: sh mcve_st1_stats_cov_spliced.sh [samtools]
SAMTOOLS=${1:-samtools}
T=$(mktemp -d)
A=$(printf 'A%.0s' $(seq 50)); Q=$(printf 'I%.0s' $(seq 50))
printf '@HD\tVN:1.4\tSO:coordinate\n@SQ\tSN:ref\tLN:5000\n' > $T/spliced.sam
printf 'r1\t0\tref\t1\t60\t50M\t*\t0\t0\t%s\t%s\n' "$A" "$Q" >> $T/spliced.sam
printf 'r2\t0\tref\t1\t60\t50M1450N50M\t*\t0\t0\t%s%s\t%s%s\n' "$A" "$A" "$Q" "$Q" >> $T/spliced.sam
$SAMTOOLS --version | head -1
echo "expected: COV [1-1] 1 50 / COV [2-2] 2 50"
echo "got:"
$SAMTOOLS stats $T/spliced.sam | grep '^COV'
# The same two reads with a 1,000-bp intron (block within the 1,500-position buffer) are reported correctly:
sed 's/50M1450N50M/50M1000N50M/' $T/spliced.sam > $T/short.sam
echo "with a 1,000-bp intron instead:"
$SAMTOOLS stats $T/short.sam | grep '^COV'
rm -r $T
