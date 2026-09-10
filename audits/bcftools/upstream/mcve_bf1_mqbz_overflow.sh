#!/bin/sh
# INFO/MQBZ from bcftools mpileup at one mapping-quality-biased site.
# The two pileups differ only in the number of reference reads.
# $1 = bcftools binary (default: bcftools)
set -e
B=${1:-bcftools}

printf '>ref\n' > ref.fa
awk 'BEGIN{for(i=0;i<200;i++)printf "A"; print ""}' >> ref.fa

for nref in 1140 1400; do
    printf '@HD\tVN:1.6\tSO:coordinate\n@SQ\tSN:ref\tLN:200\n' > in.sam
    awk -v nref=$nref 'BEGIN{
        for(i=0;i<50;i++){ref=ref "A"; q=q "I"}
        alt=substr(ref,1,24) "C" substr(ref,26)
        # reference-matching reads, all at MQ 60
        for(i=1;i<=nref;i++) printf "r%d\t0\tref\t76\t60\t50M\t*\t0\t0\t%s\t%s\n",i,ref,q
        # 100 reads carrying C at ref:100, 40 of them at MQ 30: a real MQ bias
        for(i=1;i<=60;i++)   printf "a%d\t0\tref\t76\t60\t50M\t*\t0\t0\t%s\t%s\n",i,alt,q
        for(i=1;i<=40;i++)   printf "b%d\t0\tref\t76\t30\t50M\t*\t0\t0\t%s\t%s\n",i,alt,q
    }' >> in.sam

    printf 'reads at ref:100 = %d   ' $((nref + 100))
    $B mpileup -f ref.fa -d 100000 in.sam 2>/dev/null |
        awk -F'\t' '$2==100 {n=split($8,a,";"); for(i=1;i<=n;i++) if(a[i]~/^MQBZ=/) print a[i]}'
done
